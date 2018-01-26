#！/usr/bin/env/python3
#-*- coding: utf-8-*-
#试卷生成器，每份试卷题目顺序将会被打乱,试卷问题为每个州的首府

import random

#The quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
   'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
   'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#产生若干份试卷，这里以两份为例
for quiznum in range(2):

	quizfile = open('capitalsquiz%s.txt' %(quiznum+1), 'w')
	answerfile = open('capitalsquiz_answer%s.txt' %(quiznum+1), 'w')

	#写标题
	quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizfile.write(('' * 20) + 'State Captial Quiz (Form %s)' %(quiznum+1))
	quizfile.write('\n\n')

	#打乱capital中州的顺序
	states = list(capitals.keys())
	random.shuffle(states)

	#对每个州的首府进行提问
	for questionNum in range(50):

		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)] #在列表中删除正确答案，使该列表只存储错误的答案
		wrongAnswers = random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions) #打乱选项顺序

		quizfile.write('%s. What is the captial of %s?\n' %(questionNum+1, states[questionNum]))
		for i in range(4):
			quizfile.write('	%s. %s\n' %('ABCD'[i], answerOptions[i]))
			quizfile.write('\n')

		#向答案文件中写入答案
		answerfile.write('%s. %s\n' %(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
	quizfile.close()
	answerfile.close()
