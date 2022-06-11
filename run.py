import random


class Question:
    def __init__(self, no, desc, correct_ans, options):
        """
        INITIALIZE A QUESTION

        :param no:
        :param desc:
        :param correct_ans:
        :param options:
        """
        self.q_no = no
        self.desc = desc
        self.correct_ans = correct_ans
        self.options = options


class QuestionBank:
    def __init__(self, subject):
        """
        Initializing QuestionBank
        """
        self.subject = subject
        self.questions = []

    def add_question(self, question):
        if isinstance(question, Question):
            self.questions.append(question)
            print('Question Added to Question Bank')

    def update_question(self, q_no, q_desc=None, correct_ans=None, options=None):
        if q_no in [question.q_no for question in self.questions]:
            if q_desc:
                for index, question in enumerate(self.questions):
                    if question.q_no == q_no:
                        self.questions[index].desc = q_desc
                        break
                    else:
                        pass
            if correct_ans:
                for index, question in enumerate(self.questions):
                    if question.q_no == q_no:
                        self.questions[index].correct_ans = correct_ans
                        break
                    else:
                        pass
            if options:
                for index, question in enumerate(self.questions):
                    if question.q_no == q_no:
                        self.questions[index].options = options
                        break
                    else:
                        pass
            print('Question Updated Successfully')
        else:
            print('No question found against this question id')

    def delete_question(self, q_no):
        for index, question in enumerate(self.questions):
            if question.q_no == q_no:
                self.questions.remove(question)
                print('Question Removed from Question Bank')
                break
            else:
                pass

    def get_questions(self):
        return self.questions


class Test:
    def __init__(self, questions_bank):
        """
        INITIALIZING TEST CLASS

        :param questions_bank:
        """
        self.question_bank = questions_bank
        self.test_bank = []

    def generate_test(self, no_questions=None):
        if no_questions:
            self.test_bank = random.sample(self.question_bank.get_questions(), no_questions)
        else:
            self.test_bank = random.sample(self.question_bank.get_questions(), len(self.question_bank.get_questions()))
        print('Test Generated Successfully .....\n')

    def get_test(self):
        return self.test_bank


if __name__ == '__main__':

    user = True
    while user:

        qb1 = None
        q1 = None
        print('Press 1 to Create New QuestionBank')
        print('Press 2 to Create New Question')
        print('Press 3 to Create Test')
        print('Press 4 to Update Questions')
        print('Press 5 to Delete Questions')
        print('Press 6 to exit')
        option = input('Select a option from Menu ')
        # Creating new questions bank qb1
        if option == 1:
            _subject = input('Please enter Subject name ')
            if _subject:
                qb1 = QuestionBank(subject=_subject)

        if option == 2:
            _qno = int(input('\nPlease provide Following information \nQuestion no '))
            _qdesc = input('Question Description ')
            _corr_ans = input('Correct Answer ')
            _options = input('Comma separated options ')
            _options = _options.split(',')

            if _qno and _qdesc and _corr_ans and _options:
                # creating new question for question bank
                q1 = Question(_qno, _qdesc, _corr_ans, _options)
            if q1 and qb1:
                qb1.add_question(q1)
        # q1 = Question(1, 'Full form of CPU is ______ ', 'Central Processsing Unit',
        #               ['Central Primary Unit', 'Central Processsing Unit',
        #                'Center Processsing Unit', 'None of Above'])
        # q2 = Question(2, 'Which one is input device _______ ', 'Keyboard',
        #               ['Monitor', 'Printer', 'Keyboard', 'None of Above'])
        # q3 = Question(3, 'Which one is output device _______ ', 'Head Phone',
        #               ['Head Phone', 'Mouse', 'Pen Drive', 'None of Above'])
        # q4 = Question(4, 'Father of Computer is _______ ', 'Charles Babbage',
        #               ['Jonny Depp', 'Charles Babbage', 'Charles Dickens', 'None of Above'])
        # q5 = Question(5, 'Which one is one of the best Media Player ______ ', 'VLC',
        #               ['Media Player', 'VLC', 'KM Player', 'None of Above'])

        # adding questions to question bank qb1
        qb1.add_question(q1)
        # qb1.add_question(q2)
        # qb1.add_question(q3)
        # qb1.add_question(q4)
        # qb1.add_question(q5)

        questions = qb1.get_questions()

        # for question in questions:
        #     print(question.desc + '\n' + ', '.join(question.options))

        # qb1.update_question(5, correct_ans='Vlc Media Player')
        # qb1.delete_question(5)

        print(f"\n{'*' * 35}")

        test1 = Test(qb1)
        test1.generate_test()
        test_questions = test1.get_test()

        print(f"{'*' * 10} TEST {'*' * 10}")
        for ind, _question in enumerate(test_questions):
            print(f'\nQ.No:{ind + 1} ' + _question.desc + '\n' + ', '.join(_question.options))
