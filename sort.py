import csv

def read_sort_order():
    """Reads the sort order from the UserCommand.txt file."""
    try:
        with open('UserCommand.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None
    
def save_sort_order(order):
    """Saves the sort order to the UserCommand.txt file."""
    with open('UserCommand.txt', 'w') as file:
        file.write(order)

def read_wishlist():
    """Reads data from Wishlist.csv and returns it as a list of lists."""
    wishlist_data = []
    with open('Wishlist.csv','r') as file:
        for line in file:
            # Split each line by commas and strip whitespace
            line_data = line.strip().split(',')
            wishlist_data.append(line_data)
    return wishlist_data
        

def write_wishlist(data):
    """Writes sorted data back to Wishlist.csv, overwriting existing data."""
    with open('Wishlist.csv', 'w') as file:
        for row in data:
            file.write(','.join(row) + '\n')

def sort_by_title(row):
    """Helper function to get the title column for sorting."""
    return row[2].strip()   # Row[2] corresponds to the Title column and removes any leading or trailing whitespace



def sort_by_price(row):
    """Helper function to get the price column for sorting."""
    try:
        return float(row[4].strip())    # Row[4] corresponds to the Price column and removes any leading or trailing whitespace   
    except ValueError:  # If row[4] cannot be converted to a float, a ValueError is raised and catches the error
        return 0.0  # Returns 0.0 as a fallback value so that it will not crash and provides a default value for invalid or missing prices

def get_sort_key(order):
    """Returns teh appropraite sorting function based on the order."""
    if order == 'TA' or order =='TD':
        return sort_by_title
    elif order == 'PA' or order == 'PD':
        return sort_by_price
    return sort_by_title

def sort_wishlist(data, order):
    """Sorts wishlist data based on the user's order choice."""
    if not data:
        return data
    
    # Step 1: Extract the header and content rows manually
    header = data[0]
    content_rows = data[1:]

    # Step 2: Determine sorting key
    sort_key = get_sort_key(order)

    # Step 3: Determine whether to sort in reverse
    reverse = order in ['TD', 'PD']

    # Step 4: Sort the content rows
    content_rows.sort(key=sort_key, reverse=reverse)

    # Step 5: Return the header along with the sorted content rows
    return [header] + content_rows


def print_titles_and_prices(sorted_wishlist):
    # Extract the header and indices for the 'Title' and 'Price USD' columns
    header = sorted_wishlist[0]
    title_index = header.index('Title')  # Find the index of the 'Title' column
    price_index = header.index('Price USD')  # Find the index of the 'Price USD' column

    print("\nCourse Titles and Prices:\n")
    for row in sorted_wishlist[1:]:
        title = row[title_index]  # Get the course title
        price = row[price_index]  # Get the course price
        print(f"Title: {title} | Price: {price} USD")
        
def main():
    # Step 1: Read sort order from the UserCommand.txt
    sort_order = read_sort_order() or 'PA'
    if sort_order:
        print(f"Sort order read from file: {sort_order}")
    else:
        print("No sort order specified. Using default PA.")
    
    # Step 2: Read the wishlist data from Wishlist.csv
    wishlist_data = read_wishlist()

    # Step 3: Sort the wishlist data based on the order read
    sorted_wishlist = sort_wishlist(wishlist_data, sort_order)

    # Step 4: Write the sorted data back to Wishlist.csv
    write_wishlist(sorted_wishlist)

    # Step 5: Display teh sorting information (Price Ascending, Price Descending, Title Ascending, or Title Ascending)
    order_description = {
        'PA': 'ascending order (PA)',
        'PD': 'descending order (PD)',
        'TA': 'ascending order (TA)',
        'TD': 'descending order (TD)',
    }
    print(f"\nThe courses are sorted in {order_description.get(sort_order, 'unsorted')}.")

    # Step 6: Print the titles and prices from the sorted wishlist 
    print_titles_and_prices(sorted_wishlist) 

if __name__ == "__main__":
    main()