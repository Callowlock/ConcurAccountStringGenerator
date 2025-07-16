===========================================
        3rd ELEMENT GENERATOR – README
===========================================

ABOUT THIS TOOL
---------------
This program helps you quickly generate a properly formatted Excel file used for coding employees into your business system. It creates a file called `output.xlsx` based on user-entered fields such as department, store number, names, and coding values.

REQUIREMENTS
------------
- No installation needed
- Just double-click the EXE file to launch

HOW TO USE
----------
1. Open the program
2. Fill in each field with the appropriate values
3. Use commas to separate multiple entries  
   Example: John, Jane, Mike
4. Make sure every field has the same number of entries
5. Select whether middle initials are required (Y/N)
6. Click **Generate** to create your Excel file
7. The file will be saved in the same folder as the EXE

FIELD DETAILS
-------------

► Department(s)
    - Enter the department numbers listed in the interface (0–8)
    - Example: 0,3,7

► Sector #(s)
    - Enter store numbers
    - Example: 123,879,354

► First Name(s)
    - One per person, comma separated
    - Example: John,Jane,Mike

► Require Middle Initial?
    - Select "Y" or "N"
    - If "Y", you MUST fill the Middle Initial field with matching entries
    - Use a blank entry for people without a middle initial (e.g., A,,C)

► Middle Initial(s)
    - Required ONLY if "Require Middle Initial?" is set to "Y"
    - Match count with other entries
    - Example: A,,C

► Last Name(s)
    - One per person
    - Example: Smith,Johnson,Doe

► Third Element(s)
    - A code for each employee
    - Automatically converted to uppercase
    - Example: jsmith,ataco,ksalamander

► Delete Flag(s)
    - Use Y or N
    - One per employee
    - Example: Y,Y,N

NOTES
-----
✔ It’s okay to enter values in lowercase — they’ll be properly formatted  
✔ Spaces before/after commas are automatically removed  
✔ All fields must have the same number of entries — one per employee  
✔ The output file will be named `output.xlsx`  
✔ You’ll see a preview of your input and a success or error message in the app

TROUBLESHOOTING
---------------
❌ Error: Length mismatch  
→ One or more fields have more or fewer entries than the others

❌ Error: Department(s) input is empty  
→ Department(s) field must include at least one valid department number

❌ Error: Unknown department code "X"  
→ You entered a department number not in the range 0–8

❌ Error: Sector Number(s) input is empty  
→ You must include a store number for each employee

❌ Error: First Name(s) input is empty  
→ You must include a first name for each employee

❌ Error: Last Name(s) input is empty  
→ You must include a last name for each employee

❌ Error: Middle Initial(s) input is empty  
→ If middle initials are required, this field must contain an entry for each employee (use blanks where needed)

❌ Error: Third Element(s) input is empty  
→ This field must include a third element code for each employee

❌ Error: Delete Flag(s) input is empty  
→ You must include Y or N for each employee

❌ Error: Invalid delete flag "X"  
→ Delete flags must be Y or N only (case-insensitive)

❌ Error: Unexpected error  
→ If none of the above apply, an unhandled issue may have occurred

===========================================