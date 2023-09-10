from time import strftime
from flask import Flask,request,jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_hng_data():
    slack_name = request.args.get('slack_name','jAyJOet')
    track = request.args.get('track','Backend')

    present_day = datetime.datetime.utcnow().strftime('%A   %D')

    date = datetime.datetime.utcnow()
    utc_time = strftime('%H:%M:%S UTC')

    github_repo_url = ''
    github_file_url = ''


    hngx_user={
        "slackname": slack_name, 
        "current day": present_day,
        "current UTC_time": utc_time,
        "Track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "Status_code": 200,
                                }
    
    return jsonify(hngx_user)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

