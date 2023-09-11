from time import strftime,strptime
from flask import Flask,request,jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_hng_data():
    slack_name = request.args.get('slack_name',
                                  default='jAyJOet',
                                 )
    track = request.args.get('track',
                             default='backend',                   
                            )

    present_day =  datetime.datetime.utcnow().strftime('%A')

    

    github_repo_url = 'https://github.com/jAyJOet/HNGx_Projects.git'
    github_file_url = 'https://github.com/jAyJOet/HNGx_Projects/blob/master/main.py'


    hngx_user={
        "slack_name": slack_name, 
        "current_day": present_day,
        "utc_time": f'{datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}',
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
                                }
    if not slack_name or not track:
        return jsonify({'error': 'Two arguments are required'}), 400

    if slack_name == hngx_user['slack_name'] and track == hngx_user['track']:
        return jsonify(hngx_user), 200
    else:
        return jsonify({'error': 'One or both parameters not found'}), 404
       


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

