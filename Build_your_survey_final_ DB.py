
import webbrowser as wb

'''This part of the survey asks questions about JTC. 
If the answer is "no" then the first part of the survey 
is irrelevant and the survey will jump to the questions
 toward the bottom which are more general.''' 


'''Picking yes or no determines what survey you will take! 
I would advise you to go through the yes and no for optimal fun!!'''


answer_1 = input("\n\n1- Are you a part of the Justice Through Code (JTC) Program? \nAnswer:'yes' or 'no'")
if answer_1  == "yes":
    wb.open("https://centerforjustice.columbia.edu/sites/default/files/styles/cu_crop/public/content/JTC%20Banner%20Image.png?h=2755c18e&itok=HRt6moQh")
    answer_1 = input("\nLucky you! \n\n2- What do you think about the Program so far? \nAnswer:'awesome' or 'excellent'") 
    if answer_1 == "awesome":
        print("\nAwesome!")
    if answer_1 == "excellent":
        print ("\nExcellent!")



    answer_3 = input("\n\n3- What do you think about the people who are teaching you how to code? \nHow about we rate some code masters to find out? Let's start with Mattan! \n(Recipient of the Dean's Award for Teaching Excellence!) \nwould you say he is: 'great', or 'greatest'?")
    if answer_3 == "greatest":
        print("\nYou got it!! I think he is the greatest too!")
       
    else: 
        print("\nAww, are you sure just great?! \nI think he is greater than > just great!")

    

    answer_4 = input("\n\n4- Next up, lets rate Paul\n(Soon to be DR., AKA DJ Bloomy Bloom and GitHub Pro!) \nis he:'cool', or 'coolest'?")
    if answer_4 == "coolest":
        print("\nFor sure!! I think he is the coolest too!")
    else: 
        print("\nAww, are you sure just cool?!\nI think he is cooler than > just cool!")



    answer_5 = input("\n\n5- And now, lets rate Ash \n(The Pro Front engineer with a Master's Degree from Dubai!) \nis he:'best', or 'bestest'?")
    if answer_5 == "bestest":
        print("\nDefinitely!! I think he is the bestest too!")
    else: 
        print("\nAww, are you sure just best?!\nI think he is bester than > just best!")



    TA_6a = input("\n\n6a- Who is your favorite TA?")
    print("Your favorite TA is " + TA_6a)
    TA_6b = input("\n6b- Why did you choose " + TA_6a) 
    if  TA_6b == "\n ":
        print("\nAww, that's wonderful!!")
        
    else: 
        print("\nAww, that's nice!")



    answer_7 = input("\n\n7- Now, we can't forget our Program Assistant, the wonderful Alanna\n(who keeps us up to date with announcements,\nand knows if you are in class or not :) \nis she:'nice', or 'nicest'?")
    if answer_7 == "nicest":
        print("\nYou know it!! I think she is the nicest too!")
    else: 
        print("\nAww, are you sure just nice?!")



        answer_8 = input("\n\n8- Our final rating will be Aedan Macdonald \n- (Founder and Program Manager, Justice Through Code - Columbia University) \nis he:'awesome', or 'awesomest'?")
    if answer_8 == "awesomest":
        print("\nYep, pretty accurate!! I think he is the awesomest too!")
    else: 
        print("\nAww, are you sure just awesome?!")



        answer_9 = input("\n\n9- Now tell me, Would you recommend this Program to others?, \n'yes' or 'no'?")
    if answer_9 == "yes":
        print("\nThat's nice of you...I would too!")
    else: 
        print("\nAww, that's kind of dissapointing!")
  


    answer_last_question_10 = input("\n\n~~~~~Well that's the end of my survey, before you go, would you be so kind to rate my survey please?~~~~~ \nam I: 'Fantassssstic'(that's 5 s's), 'or what'?'")
    if answer_last_question_10 == "Fantassssstic" or answer_last_question_10 == "fantastic":
        print("\nAww,:) stop it, you're making me blush! You are Fantassssstic too! \nThanks for taking my survey! I hope you had fun! Have a beautiful day!!")
        wb.open("https://i.pinimg.com/originals/ce/a1/cd/cea1cd4c9185badd83cd50dc5f6e1a31.png")
    else: 
        print("\nAww,:( ok! Thanks for taking my survey! Have a beautiful day!!")
        wb.open("https://grammarchicblog.files.wordpress.com/2017/08/thank-701985_1920.jpg")
        wb.open("https://media.swncdn.com/cms/CROSSCARDS/34129-ccc_HaveBeautifulDay.1100w.tn.jpg")
    exit()
 
# This is the end of the survey if the initial answer to the initial question is yes.

else: 
    print("Aww, that's sad, you are missing out!")


# This part is the general survey if the initial answer to the initial question is no.

color = input("\n2- So, tell me what's your fovorite color?")
wb.open("https://londonimageinstitute.com/wp-content/uploads/2020/01/How-to-Empower-Yourself-with-Color-Psychology-Varying-Colors.jpg")
print("\nYour favorite color is " + color)

song = input("\n3- What's your favorite song?")
print("\nYour favorite song is " + song)
wb.open("https://images-na.ssl-images-amazon.com/images/I/414KqITjsTL._SX331_BO1,204,203,200_.jpg")


number = input("\n4- What's your favorite number?")
print("\nYour favorite number is " + number)
wb.open("https://i.pinimg.com/originals/e2/18/51/e218516fb589993da767699eb4162b2d.jpg")


season = input("\n5- What's your favorite season?")
print("\nYour favorite season is " + season)
wb.open("https://www.thoughtco.com/thmb/RNaeVO-S3GdPZl_GOEaRM5uoY_4=/1333x1000/smart/filters:no_upscale()/the-four-seasons-3079618-v1sffinal-2dbeeaadecf443f1aea5e83f86de7077.png")


food = input("\n6- What's your favorite food?")
print("\nYour favorite food is " + food)
wb.open("https://upload.wikimedia.org/wikipedia/commons/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg")


game = input("\n7- What's your favorite game?")
print("\nYour favorite game is " + game)
wb.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJ_rJn7rkhO9df6Gx7Af2_nbpd9dRykxMQWBWY433Ouv8DKkAC8OrE_3P9OOVaRUG3c6FkEh0&usqp=CAc")


drink = input("\n8- What's your favorite drink?")
print("\nYour favorite drink is " + drink)
wb.open("https://www.dietdoctor.com/wp-content/uploads/2017/04/LC-Drinks_edited2_2400.jpg")


dessert = input("\n9- What's your favorite dessert?")
print("\nYour favorite dessert is " + dessert)
wb.open("https://img.buzzfeed.com/store-an-image-prod-us-east-1/JTDXIrMvx.png?output-format=auto&output-quality=auto&downsize=500:*")


artist = input("\n10- What's your favorite artist?")
print("\nYour favorite artist is " + artist)
wb.open("https://www.google.com/search?q=artists&tbm=isch&ved=2ahUKEwjs3u_VwZfvAhVFD98KHevcDjMQ2-cCegQIABAA&oq=artists&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCABQsZ4EWLGeBGDEpgRoAHAAeACAATqIATqSAQExmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=20dBYKyFOsWe_AbrubuYAw&bih=722&biw=1536&rlz=1C1ONGR_enUS937US937")


answer = input("\nWell that's the end of my survey, before you go, would you be so kind to rate my survey please? am I:\n Fantastic, or What?")
if answer == "Fantastic":
        print("\nAww,:) stop it, you're making me blush! You are fantastic too!")
        wb.open("https://e7.pngegg.com/pngimages/925/558/png-clipart-smiley-emoji-emoticon-sticker-blushing-emoji-miscellaneous-face.png")
else: 
        print("\nAww,:( ok! Enjoy the rest of your day!")
    # credit for ideas from the last part of the survey are from: https://www.youtube.com/watch?v=Smf8zCE7X_4
print("\nThanks for taking my survey! I hope you had fun!")
wb.open("https://media.swncdn.com/cms/CROSSCARDS/34129-ccc_HaveBeautifulDay.1100w.tn.jpg")

# The end of my fantassssstic survey!


   