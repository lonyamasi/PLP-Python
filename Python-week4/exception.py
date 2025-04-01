

#Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
def get_valid_filename():
    while True:
        filename = input("Enter the filename to read: ") #provide the path/filename
        try:
            with open(filename, 'r') as file:
                return filename
        except FileNotFoundError:
            print("Error: The specified file does not exist. Please try again.")
        except IOError:
            print("Error: The file could not be read. Please try again.")
            
            
def modify_file(filename, modified_file):
    with open(filename, 'r') as old_file:
        f_content= old_file.read()
        
    f_modified = f_content.upper()
    
    with open(modified_file,'w') as new_file:
        new_file.write(f_modified)
        
        
    print(f'the modified content is in uppercase and has now been written in {modified_file}')
    
    
input_filename = get_valid_filename()
output_filename = "new_file.txt"  # Replace with your desired output file name
modify_file(input_filename, output_filename)



#to check whether content in new_file.txt is in uppercase

with open('new_file.txt', 'r') as f:
    print(f.read())
    
    