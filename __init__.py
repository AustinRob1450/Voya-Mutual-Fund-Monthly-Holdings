import logging

# Create a logger for the main program
main_logger = logging.getLogger('main')
main_logger.setLevel(logging.DEBUG)

# Create a file handler for the main program
main_file_handler = logging.FileHandler('main_log.log')
main_file_handler.setLevel(logging.DEBUG)

# Create a console handler for the main program
main_console_handler = logging.StreamHandler()
main_console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the main program handlers
main_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
main_file_handler.setFormatter(main_formatter)
main_console_handler.setFormatter(main_formatter)

# Add the handlers to the main logger
main_logger.addHandler(main_file_handler)
main_logger.addHandler(main_console_handler)

# Create a logger for tools
tools_logger = logging.getLogger('tools')
tools_logger.setLevel(logging.DEBUG)

# Create a file handler for tools
tools_file_handler = logging.FileHandler('tools_log.log')
tools_file_handler.setLevel(logging.DEBUG)

# Create a console handler for tools
tools_console_handler = logging.StreamHandler()
tools_console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the tools handlers
tools_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
tools_file_handler.setFormatter(tools_formatter)
tools_console_handler.setFormatter(tools_formatter)

# Add the handlers to the tools logger
tools_logger.addHandler(tools_file_handler)
tools_logger.addHandler(tools_console_handler)

main_logger = logging.getLogger('main')
tools_logger = logging.getLogger('tools')
