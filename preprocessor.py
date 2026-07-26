import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s(?:AM|PM)\s-\s'

    messages = re.split(pattern, data)[1:]

    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=False)
    df['message_date'] = df['message_date'].str.replace(' - ', '', regex=False)

    df['message_date'] = pd.to_datetime(
        df['message_date'],
        format='%m/%d/%y, %I:%M %p'
    )
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date

    df['time'] = df['date'].dt.strftime('%I:%M %p')

    period = []

    for hour in df['hour']:
        start = hour % 12
        end = (hour + 1) % 12

        if start == 0:
            start = 12
        if end == 0:
            end = 12

        start_ampm = "AM" if hour < 12 else "PM"
        end_ampm = "AM" if (hour + 1) % 24 < 12 else "PM"

        period.append(f"{start} {start_ampm} - {end} {end_ampm}")

    df['period'] = period

    return df