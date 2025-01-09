import os, shutil, datetime
import requests, urllib
import pandas as pd
import glob

class Tools:
    def __init__(self):
        self.date = str(datetime.date.today())
        self.data_path = ""
        self.folder_path = ""
        self.master_path = ""
        self.broken_urls = []

    def copy_files(self, src_dir, dst_dir):
        """
        Copies files from src_dir to dst_dir.

        Args:
            src_dir (str): Source directory path.
            dst_dir (str): Destination directory path.
        """

        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
        if not os.path.exists(dst_dir):
            raise FileNotFoundError(f"Destination directory '{dst_dir}' does not exist.")
        
        # Copy files
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dst_file = os.path.join(dst_dir, filename)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)
                print(f"Copied '{filename}' to '{dst_dir}'")

    def create_folder_structure(self):
        """
        Creates a folder structure based on the current date.

        Args:
            root_dir (str): Root directory path.
        """

        # Create the root directory if it doesn't exist
        if not os.path.exists("Historicals"):
            os.makedirs("Historicals")
        

        today = datetime.date.today()

        # Format the date as DD/MM/YY
        date_str = str(today)

        # Create the folder path
        folder_path = os.path.join("Historicals", date_str)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        self.data_path = os.path.join("Historicals", date_str, "data")    
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)

        self.master_path = os.path.join("Historicals", date_str, "master")    
        if not os.path.exists(self.master_path):
            os.makedirs(self.master_path)

        return self.data_path


    def check_url(self, url) -> bool:
        """
        Checks if a URL is valid.

        Args:
            url (str): URL to check.

        Returns:
            bool: True if the URL is valid, False otherwise.
        """

        url_Obj = requests.head(url)

        if url_Obj.status_code != 200:
            print("URL's that are not working properly:\n", url)
            self.broken_urls.append(url)
        
        return url_Obj.status_code == 200

    def download_excel(self, url_list):
        """
        Downloads excel files from a list of URLs and saves them to a folder.

        Args:
            url_list (list): List of URLs to download.
        """
        for url in url_list:
            good_url = self.check_url(url)
            if good_url:
                if not os.path.exists(os.path.join(self.data_path, url.split("/")[-1])):
                    print("File not in folder: ", url.split("/")[-1])
                    print("Downloading file: ", url.split("/")[-1])

                    file = urllib.request.urlretrieve(url, os.path.join(self.create_folder_structure(), url.split("/")[-1]))
                    if file is None:
                        print("File could not be downloaded")
                    else:
                        print("File downloaded successfully")
            else:
                continue

    def create_master_file(self):

        """
        Creates a master file from a list of excel files

        Args:
            excel_folder (list): List of excel files

        Returns:
            pandas.DataFrame: Master file dataframe
        """
        master_file = pd.DataFrame()
        staging_df = pd.DataFrame()
        files = glob.glob(self.data_path + "/*.xls")

        for file in files:
            try:
                df = pd.read_excel(file, header = 3)
                staging_df = pd.concat([df])
                
                master_file = pd.concat([master_file, staging_df])
            except:
                continue
        
        os.chdir(self.master_path)
        try:
            master_file.to_excel(f"Master_{self.date}.xlsx", index=False)

            print("Master file saved successfully")
        except Exception as e:
            print("Error saving master file:", e)

    def remove_rows_by_keyword(self):
        """
        Removes rows from the master file if the first column contains a string that starts with the keyword "Important"
        which is a common disclosure used in the excel files.

        Returns:
            pandas.DataFrame: Filtered DataFrame with rows removed
        """
        
        df = pd.read_excel(f"Master_{self.date}.xlsx")
        
        # Function to check if a cell value starts with the keyword
        def starts_with_keyword(cell_value):
            
            if isinstance(cell_value, str):
                return cell_value.startswith("Important")
            return False
        
        # Apply the function to the first column and filter out matching rows
        df_filtered = df[~df.iloc[:, 0].apply(starts_with_keyword)]
        df_filtered = df_filtered.dropna(how='all')
        
        # Write the filtered DataFrame back to an Excel file
        df_filtered.to_excel(f"output_file_{self.date}.xlsx", index=False)



    def print_whale(self):
        print("         __   __")
        print("             __ \ / __")
        print("             /  \ | /  \ ")
        print("                 \|/")
        print("            _,.---v---._")
        print("   /\__/\  /            \ ")
        print("   \_  _/ /              \ " + "         That was over-whale-ming!")
        print("     \ \_|           @ __|")
        print("      \                \_")
        print("       \     ,__/       /")
        print("     ~~~`~~~~~~~~~~~~~~/~~~~")