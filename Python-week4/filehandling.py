# Create a program that reads a file and writes a modified version to a new file.


def modify_file(filename, modified_file):
    with open(filename, 'r') as old_file:
        f_content= old_file.read()
        
    f_modified = f_content.upper()
    
    with open(modified_file,'w') as new_file:
        new_file.write(f_modified)
        
        
    print(f'the modified content is in uppercase and has now been written in {modified_file}')
    
    



    
    

        
        

        

        
        
        
        