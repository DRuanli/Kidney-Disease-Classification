"""
This code block configures a logger object - comprehensive logging system for a Python application.
It directs log messages to both a file and the console, providing a robust mechanism for tracking:
application behavior, debugging, and monitoring.

Benefits:
- Improved Debugging: Provides detailed information about application behavior.
- Persistent Logging: Stores log messages in a file for later analysis.
- Real-Time Monitoring: Displays log messages in the console during execution.
- Granular Control: Allows for fine-grained control over logging levels and formats.
- Standardized Approach: Uses the standard Python logging library.

Key Features:
- Dual output: Logs messages to both a persistent file (running_logs.log) and the console (sys.stdout). This provides both immediate feedback and a historical record.
- Customizable log format (logging_str).
- Automatic log directory creation.
- Configurable log level (INFO+): Sets the minimum log level to logging.INFO, filtering out less critical DEBUG messages while capturing important information, warnings, errors, and critical events.
- Custom named logger.

Variables:
- logging_str: Log message format.
- log_dir: Stores the name of the directory where log files are stored.
- log_filepath: Stores the full path to the log file.
- logger: Stores the custom logger instance.

Workflow:
1. Import Libraries:
- Imports necessary modules (os, sys, logging).
2. Define Log Format:
- Sets the logging_str variable to define the log message format.
3. Set Log File Path:
- Defines the log_dir and log_filepath variables.
- Creates the log directory if it doesn't exist.
4. Configure Logging:
- Calls logging.basicConfig() to set the log level, format, and handlers.
- Creates a FileHandler to write logs to a file.
- Creates a StreamHandler to write logs to the console.
5. Create Custom Logger:
- Calls logging.getLogger() to create a named logger instance.
6. Use the Logger:
- Throughout the application, the logger object is used to record log messages at various levels (e.g., logger.info(), logger.error()).

Usage:
1. Place this code block at the beginning of your Python script or within a configuration module.
2. Use the logger object to log messages throughout your application:
- logger.info("Informational message")
- logger.debug("Debug message")
- logger.warning("Warning message")
- logger.error("Error message")
- logger.critical("Critical error message")

"""
import os
import sys
import logging

# Define logging format
# [timestamp: log label name:
# where the module from (e.g.template.py): error caught]
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")