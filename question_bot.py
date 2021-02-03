# Question Bot Project #
# The goal is to build a program that can play the game 20 Questions
# for an arbitrary number of yes/no questions

# you'll need a file to store the questions and answers, I'd suggest a csv file with columns like:
# current_answer (a binary list tracking where we are)
# question (a string with the question)
# terminal_question_flag (a boolean that tells us if we're at the end of the tree)


class question_bot(self)

    #this function constructs a question_bot with a certain number of questions
    #and a filename to retrieve the questions and answers

    def __init__(self, num_of_questions, question_file):
    
        self.filename = question_file
        self.current_num_of_questions = 0
        self.max_num_of_questions = 20
        
        #open the question file and put the contents into data
        self.data = csvopen(question_file)
        self.current_answers = []
        
    def write_new_question(self, new_question)
        #write a new yes/no question 
        new_question =
        new_question_location = self.current_answers
    
        #we need to check if the old question is no longer terminal
        #so we check the other branch to see if it is NOT terminal
        #if not, then the old question is no longer terminal
        
        #append the new question to the data
        data =

        #write the new question to the file
        csvwrite(new_question_file)

    def ask_question(self)
        
        #check to see if we're out of questions
        if self.current_num_of_questions > self.max_num_of_questions
            victory = 0
            return victory
        #if we're not out of questions, ask the next question
        self.current_num_of_questions +=1
        else
            #follow the current answers from the beginning to get the next question and whether it
            #is at the end of the tree of questions we have
            new_question, terminal_question_flag = get_question(data, current_answers)

            #ask the user to say yes or no by displaying the new question
            new_answer = 

            #add that answer to the current_answers
            self.current_answers = self.current_answers + new_answer

            #check if we have correctly guessed the item with our last question
            if terminal_question_flag:
                if new_answer ==  :
                    #the bot won!
                    victory = 1
                    return victory
                else
                    self.write_new_question
                    #the bot ran out of questions to ask
                    
            #if we haven't, keep playing!     
            else
                self.ask_question(self, current_answers, current_num_of_questions, data)

    def start_game():
        # make an empty container which will contain your current answers
        self.current_answers = []
        self.current_num_of_questions = 0
        
        #start asking questions!
        self.ask_question(self)

        #ask do you want to play again?
        #Remember that this class still has the old data from before this round
        play_again =

        if play_again
            start_game()
        else
            #thank you for playing!



# main program
maximum_num_of_questions = 20
question_file_name =
bot = question_bot(maximum_num_of_questions, question_file_name)
bot.start_game()
            
           
            
        
