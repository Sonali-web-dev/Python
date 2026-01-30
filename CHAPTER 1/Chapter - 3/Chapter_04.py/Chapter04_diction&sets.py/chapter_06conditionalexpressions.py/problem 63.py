p1 = "Subscribe this channel"
p2 = "Comment this page"
p3 = "Click on this browser"
p4 = " buy now "
message = input("Enter your comment:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is a spam")
else:
    print("This message is not a spam")
    # This programme commonly made for filteration of spam numbers