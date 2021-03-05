
import webbrowser as wb

'''This part of the survey asks questions about JTC. If the answer is "no" then the first part of the survey 
is irrelevant and the survey will jump to the questions toward the bottom which are more general.''' 

answer_1 = input("1- Are you a part of the Justice Through Code (JTC) Program? \nAnswer:'yes' or 'no'")
if answer_1  == "yes":
    wb.open("https://centerforjustice.columbia.edu/sites/default/files/styles/cu_crop/public/content/JTC%20Banner%20Image.png?h=2755c18e&itok=HRt6moQh")
    answer_1 = input("Lucky you! \n2- What do you think about the Program so far? \nAnswer:'awesome' or 'excellent'") 
    if answer_1 == "awesome":
        print("Awesome!")
    if answer_1 == "excellent":
        print ("Excellent!")



    answer_3 = input("3- What do you think about the people who are teaching you how to code? \nHow about we rate some code masters to find out? Let's start with Mattan! \n(Recipient of the Dean's Award for Teaching Excellence!) \nwould you say he is:\n 'great', or 'greatest'?")
    if answer_3 == "greatest":
        print("You got it!! I think he is the greatest too!")
       
    else: 
        print("Aww, are you sure just great?! \nI think he is greater than > just great!")

    

    answer_4 = input("4- Next up, lets rate Paul\n(Soon to be DR., AKA DJ Bloomy Bloom and GitHub Pro!) \nis he:\n'cool', or 'coolest'?")
    if answer_4 == "coolest":
        print("For sure!! I think he is the coolest too!")
    else: 
        print("Aww, are you sure just cool?!\nI think he is cooler than > just cool!")



    answer_5 = input("5- And now, lets rate Ash \n(The Pro Front engineer with a Master's Degree from Dubai!) \nis he:\n'best', or 'bestest'?")
    if answer_5 == "bestest":
        print("Definitely!! I think he is the bestest too!")
    else: 
        print("Aww, are you sure just best?!\nI think he is bester than > just best!")



    TA_6a = input("6a- Who is your favorite TA?")
    print("Your favorite TA is " + TA_6a)
    TA_6b = input("6b- Why did you choose " + TA_6a) 
    if  TA_6b == " ":
        print("Aww, that's wonderful!!")
        
    else: 
        print("Aww, that's nice!")



    answer_7 = input("7- Now, we can't forget our Program Assistant, the wonderful Alanna\n(who keeps us up to date with announcements,\nand knows if you are in class or not :) is she:\n'nice', or 'nicest'?")
    if answer_7 == "nicest":
        print("You know it!! I think she is the nicest too!")
    else: 
        print("Aww, are you sure just nice?!")



        answer_8 = input("8- Our final rating will be Aedan Macdonald - (Founder and Program Manager, Justice Through Code - Columbia University)is he:\n'awesome', or 'awesomest'?")
    if answer_8 == "awesomest":
        print("Yep, pretty accurate!! I think he is the awesomest too!")
    else: 
        print("Aww, are you sure just awesome?!")



        answer_9 = input("9- Now tell me, Would you recommend this Program to others?, 'yes' or 'no'?")
    if answer_9 == "yes":
        print("That's nice of you...I would too!")
    else: 
        print("Aww, that's kind of dissapointing!")
  


    answer_last_question_10 = input("~~~~~Well that's the end of my survey, before you go, would you be so kind to rate my survey please? am I:\n 'Fantassssstic'(that's 5 s's), 'or what'?'~~~~~")
    if answer_last_question_10 == "Fantassssstic" or answer_last_question_10 == "fantastic":
        print("Aww,:) stop it, you're making me blush! You are Fantassssstic too! \nThanks for taking my survey! I hope you had fun! Have a beautiful day!!")
        wb.open("https://i.pinimg.com/originals/ce/a1/cd/cea1cd4c9185badd83cd50dc5f6e1a31.png")
    else: 
        print("Aww,:( ok! Thanks for taking my survey! Have a beautiful day!!")
        wb.open("https://media.swncdn.com/cms/CROSSCARDS/34129-ccc_HaveBeautifulDay.1100w.tn.jpg")
    
    exit()
 
# This is the end of the survey if the initial answer to the initial question is yes.

else: 
    print("Aww, that's sad, you are missing out!")


# This part is the general survey if the initial answer to the initial question is no.

color = input("2- So, tell me what's your fovorite color?")
print("Your favorite color is " + color)
 wb.open("https://londonimageinstitute.com/wp-content/uploads/2020/01/How-to-Empower-Yourself-with-Color-Psychology-Varying-Colors.jpg")


song = input("3- What's your favorite song?")
print("Your favorite song is " + song)
 wb.open("https://images-na.ssl-images-amazon.com/images/I/414KqITjsTL._SX331_BO1,204,203,200_.jpg")


number = input("4- What's your favorite number?")
print("Your favorite number is " + number)
 wb.open("https://i.pinimg.com/originals/e2/18/51/e218516fb589993da767699eb4162b2d.jpg")


season = input("5- What's your favorite season?")
print("Your favorite season is " + season)
 wb.open("")


food = input("6- What's your favorite food?")
print("Your favorite food is " + food)
 wb.open("")


game = input("7- What's your favorite game?")
print("Your favorite game is " + game)
 wb.open("")


drink = input("8- What's your favorite drink?")
print("Your favorite drink is " + drink)
 wb.open("")


dessert = input("9- What's your favorite dessert?")
print("Your favorite dessert is " + dessert)
 wb.open("")


artist = input("10- What's your favorite artist?")
print("Your favorite artist is " + artist)
 wb.open("")


answer = input("Well that's the end of my survey, before you go, would you be so kind to rate my survey please? am I:\n Fantastic, or What?")
if answer == "Fantastic":
        print("Aww,:) stop it, you're making me blush! You are fantastic too!")

else: 
        print("Aww,:( ok! Enjoy the rest of your day!")
    # credit for ideas from the last part of the survey are from: https://www.youtube.com/watch?v=Smf8zCE7X_4
print("Thanks for taking my survey! I hope you had fun!")
    




   