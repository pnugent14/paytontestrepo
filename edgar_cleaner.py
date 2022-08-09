

#Function to remove tags and special characters
def clean_html_text(html_text):
    """function to get rid of all non-alphabet characters and puts all lower-case

    Args:
        html_text (str): raw html text

    Returns:
        str: raw text
    """
    import re 
    clean_text=(re.sub(r"[^a-zA-Z0-9]+", ' ', html_text))
    clean_text=clean_text.lower()
    return clean_text

#Function to take in html, convert to text, then clean, and save to a destination folder
def write_clean_html_text_files(input_folder, dest_folder):
    """writes all the cleaned html text to new .txt files

    Args:
        input_folder (directory): folder of html files to be cleaned
        dest_folder (directory): folder where cleaned .txt files will be saved
    """
    import os
    from bs4 import BeautifulSoup as bs

    os_directory = os.fsencode(input_folder) #inside paranthesis will become input folder
    
    for file in os.listdir(os_directory):
        start_filename = os.fsdecode(file)
        if start_filename.endswith("html"): # will only grab html files
            #Grabbing the file to read the text from
            complete_start_file_path = os.path.join(input_folder, start_filename)    
            start_file = open(complete_start_file_path, "r")
            contents = start_file.read()
            start_file.close()
            soup = bs(contents)
            text_to_clean = soup.get_text()
            
            #clean the text
            completed_clean_text = clean_html_text(text_to_clean)

            #Save text file with cleaned text to destination folder
            save_path = dest_folder
            name_of_file = start_filename.replace(".html", '') #same name as start file then save as 
            completeName = os.path.join(save_path, name_of_file+".txt")         
            file1 = open(completeName, "w")
            toFile = completed_clean_text
            file1.write(toFile)
            file1.close()

