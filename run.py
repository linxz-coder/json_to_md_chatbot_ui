import json
import os

folder_path = '.'  # 当前文件夹路径

# 找到第一个json文件
json_file = None
for file in os.listdir(folder_path):
    if file.endswith('.json'):
        json_file = file
        break

if json_file:
    with open(json_file) as f:
        data = json.load(f)
    with open('chatbot_content.md', 'w') as mdfile:
        for conversation in data['history']:
            for message in conversation['messages']:
                role = message['role']
                content = message['content']
                if role == 'user':
                    mdfile.write('# ' + '问题：' + content + '\n\n')
                elif role == 'assistant':
                    mdfile.write('回答：' + content + '\n\n' + '<br/>' + '\n\n')
else:
    print('文件夹中没有找到json文件。')
