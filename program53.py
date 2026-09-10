# # python program to detect a comment is spam or not 

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
user = input("Enter the comment: ").lower()
is_spam = any(keyword in user for keyword in spam_keywords)
if is_spam:
    print("Comment is a spam !!!!")
else:
    print("Comment is safe.")
