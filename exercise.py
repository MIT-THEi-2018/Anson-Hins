class request_board:

    name = []

    id = 0

    detail = []

    begin = input("Welcome to our board, are you going to post or search? \n")

    if(begin == "post"):

        post_name = input("Please enter your name \n")

        name.append(post_name)

        request_info =  input("Please enter your request with detail. \n")

        if(request_info is None):
   
            print('Invalid input, please retry')

        else:       

            detail.append(request_info)
        
            print("Thank you for using our board!")









       


    



                

            





        