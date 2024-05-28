course_name = "CourseHub"  # Variable for the course name
book_count = 50  # Variable for the number of books

print("Welcome to " + course_name + "!")  # Output a welcome message
print("Current book count: " + str(book_count))  # Output the number of books

book_name = input("Enter the book name: ")  # Prompt the user to enter the book name
print("You have entered: " + book_name)  # Output the entered book name

author_name = input("Enter the author's name: ")  # Get author's name
concatenated_str = book_name + " by " + author_name  # Concatenation
print("Concatenated String: " + concatenated_str)

print("Book name in lowercase: " + book_name.lower())
print("Author name in uppercase: " + author_name.upper())

stock_str = input("Enter the stock quantity: ")  # Input stock quantity as a string
stock_int = int(stock_str)  # Convert stock quantity to an integer

# Check if the book is available based on stock quantity
if stock_int > 0:
    print("The book '" + book_name + "' by " + author_name + " is available with " + str(stock_int) + " copies in stock.")
else:
    print("The book '" + book_name + "' by " + author_name + " is not available as it is out of stock.")
