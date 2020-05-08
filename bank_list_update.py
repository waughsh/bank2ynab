"""
Helper script to update README.md to reflect banks listed in bank2ynab.conf
"""

import re

def get_banks(file):
    """
    :param file: filename for config file
    :return banks: list of bank names
    """
    with open(file, "r") as f:
        file_contents = f.read()    
    
    bracket_regex = re.compile("\n\[(.*)\]\n")
    banks = bracket_regex.findall(file_contents)
    
    return banks[1:]
def edit_readme(file, start, end, banks):
    """
    :param file: filename for readme file
    :param start: string indicating start of section to replace
    :param end: string indicating end of section to replace
    :param banks: list of banks
    """

    bank_list_text = start + "\n"
    for bank in banks:
       bank_list_text += "1. {}\n".format(bank)
    bank_list_text += end
    
    with open(file, "r") as f:
        file_contents = f.read()
      
    logging.info("Writing new list to {}".format(file))

    with open(file, "w") as f:
        list_regex = re.compile("({})(.*)({})".format(start, end), re.DOTALL)
        file_contents = list_regex.sub(bank_list_text, file_contents)
        f.write(file_contents)
# Variables
config_file = "bank2ynab.conf"
readme_file = "README.md"
start_token = "<!--AUTO BANK UPDATE START-->"
end_token = "<!--AUTO BANK UPDATE END-->"
run(config_file, readme_file, start_token, end_token)
