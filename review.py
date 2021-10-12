from cunyzero import db
from cunyzero import app

#sum of professor's ratings
ratingSum = 0
#Amount of ratings there are
ratingAmount = 0
#Current rating, add into db
studentRating = 0
#professors avg 
professorRatingAverage = ratingSum / ratingAmount
#taboo words in the review
tabooWords = 0
#cout warnings
warningCount = 0
#check if grade is given
gradingCheck = False

#add review and rating to db after getting the input
def writeRateReview():
    #inputReview = request.form['review']
    #inputRating = request.form['rating']
    #inputProfessor = request.form['professor']
    #inputStudent = request.form['student']

    #checks if there are taboo words
    #manageTaboo(inputReview)

    #insert(professorReviews).values(
    # professor = inputProfessor, 
    # rating = inputRating, 
    # review = inputReview, 
    # student = inputStudent)
    return 0

#pause after professor give grade
def allowRating():
    #check if grades are given ????
    # gradingCheck = 
    if (gradingCheck == False):
        writeRateReview()
    else:
        print('You cannot write a review at this time')

#professor's warnings 
def warnProfessor():
    #select the warning column for the professors and +1 to their warning
    #update(professorReviews).values(
    # )

    #add up the 
    #professorWarningCount = 0
    #if professorRatingAverage <= 2:
        #add a warning in the database?
    #   print('Students are not satisified with your teaching')
        #when the professor gets a warning check if it's their 3rd one
    #   if professorWarningCount == 3:
    #        suspendProfessor()
    return 0

def suspendProfessor():
    #terminate account?
    return 0

#Warns the author for writing taboo words from taboo db/list
def manageTaboo(review):
    #splitReview.split()
    #tabooList = session.query(x).all()

    #for word in splitReview:
    #   if word in tabooList:
    #       tabooFiltering(word)
    #       tabooWords++

    #reviewCensored = ' '.join(splitReview)

    # if tabooWords == 0:
    #   print("Good Review")
    # elif tabooWords < 3:
    #   print("Your review contains taboo words")
    # if tabooWords >= 3:
    #   remove review and give 2 warnings
    #   review.erase()
    tabooWords = 0
    #return reviewCensored


# turn taboo words to **
def tabooFiltering(word):
    word.replace(word,"*")