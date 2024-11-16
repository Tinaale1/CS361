Microservice Overview:
    This microservice allows user to request and receive sorted Wishlist data based on preferences saved by the user in UserCommand.txt. 
    The service reads sorting preferences from the file and sorts the Wishlist in ascending or descending 

Communication Contract:
    1. Requesting Data from the Microservice:
        To request data from the microservice, the program should send a request with the sorting order saved in UserCommand.txt. 
        Then call sort_wishlist() with the data and the saved sorting order. 
            The sorting options available are:
                TA: Title in ascending order
                TD: Title in descending order
                PA: Price in ascending order
                PD: Price in descending order
        Example Call to Request Data: 
          1. Save the sort preference in UserCommand.txt 
              save_sort_order("TA")
          2. Read the current sort preference from UserCommand.txt
              sort_order = read_sort_order()
          3. Retrieve the Wishlist data from Wislist.csv to be stored
              wishlist_data = read_wishlist()
          4. Call sort_wishlist with the data and sorting preference 
              sorted_wishlist = sort_wishlist(wishlist_data, sort_order)
    2. Receiving Data from the Microservice:
        After the sort_wishlist() function processes the request, it returns a sorted list of wishlist entries.
        The program can then access this sorted data for further processing or displaying to the user using.
        Example Call to Receive Data:
          1. Display the sorted data (Title and Price) in the requested order
                print_titles_and_prices(sorted_data)
                
![UML Sequence Diagram](https://github.com/Tinaale1/CS361/blob/6a69a4af4ed20d6831816e4357fd21e2bc14bc44/UML%20Sequence%20Diagram.png)
