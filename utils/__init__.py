import logging
import boto3
import yaml


def get_log_level(level_string):
    levels = {
        "DEBUG":logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "CRITICAL":logging.CRITICAL
    }
    return levels[level_string]


def get_yaml(path):
    with open(path, 'r') as stream:
        try:
            fileData = yaml.load(stream)
            return fileData
        except yaml.YAMLError as exc:
            print(exc)
            return None
