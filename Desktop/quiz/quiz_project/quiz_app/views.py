# Create your views here.
from django.shortcuts import render, redirect
from .models import Quiz, Answer, UserAnswer


def quiz(request):
    if request.method == 'POST':
        answer_id = request.POST.get('answer')
        if answer_id is None:
            request.session['message'] = 'Please select an answer.'
            # Return the current question page with an error message
            quizzes = Quiz.objects.all()
            quiz = quizzes[request.session['question_number'] - 1]
            answers = Answer.objects.filter(quiz=quiz)
            context = {
                'quiz': quiz,
                'answers': answers,
                'score': request.session['score'],
                'question_number': request.session['question_number'],
                'total_questions': quizzes.count(),
                'message': request.session['message']
            }
            return render(request, 'quiz.html', context)
        
        # Get the answer object and the quiz object
        answer = Answer.objects.get(id=answer_id)
        quiz = answer.quiz
        
        request.session['message'] = ''
        
        # Delete the previous answer object for the same user and quiz
        UserAnswer.objects.filter(user=request.user, answer__quiz=quiz).delete()
        
        if answer.score > 0:
            request.session['score'] += answer.score
        else:
            correct_answer = Answer.objects.get(quiz=answer.quiz, score__gt=0)
            request.session['message'] = f"Sorry, the correct answer was '{correct_answer.text}'."
        # Create a new UserAnswer object
        user_answer = UserAnswer(user=request.user, answer=answer, score=answer.score)
        user_answer.save()
        
        request.session['question_number'] += 1
        quizzes = Quiz.objects.all()
        
        if request.session['question_number'] > quizzes.count():
            return redirect('results')
        
        quiz = quizzes[request.session['question_number'] - 1]
        answers = Answer.objects.filter(quiz=quiz)
        context = {
            'quiz': quiz,
            'answers': answers,
            'score': request.session['score'],
            'question_number': request.session['question_number'],
            'total_questions': quizzes.count(),
            'message': request.session['message']
        }
        return render(request, 'quiz.html', context)
    
    else:
        request.session['score'] = 0
        request.session['question_number'] = 1
        request.session['message'] = ''
        quizzes = Quiz.objects.all()
        quiz = quizzes[0]
        answers = Answer.objects.filter(quiz=quiz)
        context = {
            'quiz': quiz,
            'answers': answers,
            'score': request.session['score'],
            'question_number': request.session['question_number'],
            'total_questions': quizzes.count(),
            'message': request.session['message']
        }
        return render(request, 'quiz.html', context)


def results(request):
    user_answers = UserAnswer.objects.filter(user=request.user)
    total_score = sum(user_answer.score for user_answer in user_answers)
    context = {
        'user_answers': user_answers,
        'total_score': total_score
    }
    return render(request, 'results.html', context)
