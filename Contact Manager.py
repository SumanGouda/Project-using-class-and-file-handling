class Contact :
    def __init__(self,name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def create_contact(self):
        with open ("Contact.txt","a") as f:
            f.write(f"{self.name},{self.phone},{self.email}\n")

    
    def delete_contact(self, remove_name):
        with open ("Contact.txt","r") as f:
            lines = f.readlines()
            #Makes a list of all the lines in the text file.
            
        updated_lines = [line for line in lines if remove_name not in line]
        #List comprehension, takes out those line from the list lines which do not have remove_name variable. 
        
        with open ("Contact.txt","w") as f:
            f.writelines(updated_lines)
            #Overwrite the content.
            
    def view_contact(self):
        with open ("Contact.txt","r") as f:
            read = f.read()
            print(read)
            
    def search_contact(self, name):
        with open ("Contact.txt","r") as f:
            lines = f.readlines()
        
        search_line = [line for line in lines if name.lower() in line.lower()]
        if search_line:
            print(search_line)
            for contact in search_line:
                print(contact.strip())
        else:
            print("Contact not found.")
            
# Creating contacts
c1 = Contact("Alice", "1234567890", "alice@example.com")
c1.create_contact()

c2 = Contact("Bob", "9876543210", "bob@example.com")
c2.create_contact()

# View contacts
c1.view_contact()

# Search
c1.search_contact("bob")

# Delete a contact
c1.delete_contact("Alice")

# View after deletion
c1.view_contact()

            
            
                
        
            
    
            
            