from bottle import route, run, template, request, abort, redirect, static_file
from kviz-model import Model

 kviz-model = Model('vprasanja.json')


 @route('/res/<filename:path>')
 def resource(filename):
     return static_file(filename, root='res/')


 @route('/')
 def index():
     return template('templates/index.tpl')


 @route('/question/<id>')
 def question(id):
     id = int(id)

     if not model.has_question(id):
         abort(404, 'No such question.')

     question = model.get_question(id)

     return template('templates/question.tpl', text=question['text'], id=id)


 @route('/submit', method='POST')
 def submit():
     id = int(request.forms.get('question'))
     answer = int(request.forms.get('answer'))

     user = model.current_user()
     model.answer(user, id, answer)

    #vrne na prvo stran
     if model.has_question(id + 1):
         redirect('/question/{}'.format(id + 1))
     else:
         redirect('/result')


 @route('/result')
 def result():
     return template('templates/result-cover.tpl')


 @route('/showresult')
 def show_result():
     user = model.current_user()
     model.drop_user(user)  # The user data is no longer needed in cache at this point.

     result = model.get_results(user)
     return template('templates/results.tpl', result=result)


 if __name__ == '__main__':
     run()
