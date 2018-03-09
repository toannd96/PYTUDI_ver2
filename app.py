import json, os, re
from flask import Flask, render_template, request, url_for, redirect
import requests

app = Flask(__name__)


@app.route('/words', methods=['GET','POST'])
def fetch_word():
    if request.method == "POST":
        word = request.form.get("word")
        if all(ord(char) < 128 for char in word) is True:
            url = 'https://api.tracau.vn/WBBcwnwQpV89/s/'+word+'/en'
            r = requests.get(url)
            data = r.json()
            items = data['tratu']
            for i in items:
                return (i['fields']['fulltext'])
            else:
                return "<b class='title_case'></b> Không tìm thấy từ mà bạn yêu cầu"
            return redirect(url_for('show_index'))
            
        else:
            url = 'https://api.tracau.vn/WBBcwnwQpV89/s/'+word+'/vi'
            r = requests.get(url)
            data = r.json()
            items = data['tratu']
            for i in items:
                    return (i['fields']['fulltext']) 
            else:
                return "<b class='title_case'></b> Không tìm thấy từ mà bạn yêu cầu"
            return redirect(url_for('show_index'))


@app.route('/')
def show_index():
    return render_template("search.html")

@app.errorhandler(403)
def not_found_error(error):
    error_code = "Error 403 - Forbidden"
    error_message = "Xin lỗi, truy cập bị từ chối hoặc bị cấm!"
    return render_template('error.html',
                           error_code = error_code,
                           error_message=error_message), 403

@app.errorhandler(404)
def not_found_error(error):
    error_code = "Error 404 - File not found"
    error_message = "Xin lỗi, trang yêu cầu không được tìm thấy!"
    return render_template('error.html',
                           error_code = error_code,
                           error_message=error_message), 404

@app.errorhandler(405)
def not_allowed_error(error):
    error_code =  "Error 405 - Method not allowed"
    error_message = "Xin lỗi, phương pháp này không được phép!"
    return render_template('error.html',
                           error_code = error_code,
                           error_message = error_message), 405

@app.errorhandler(500)
def internal_error(error):
    error_code = "Error 500 - Internal Server Error"
    error_message = "Xin lỗi, đã xảy ra lỗi máy chủ nội bộ!"
    return render_template('error.html',
                           error_code = error_code,
                           error_message = error_message), 500

if __name__ == '__main__':
    app.run(debug = True)
