from cal_setup import get_calendar_service
import datetime
from os.path import dirname, abspath


DIR = dirname(dirname(dirname(abspath(__file__))))
TEXT_DIR = f'{DIR}/CALENDAR_ID'
name = open(TEXT_DIR).readline()

def create(body):
    # creates new event
    service = get_calendar_service()
    # If have any specific calendar just replace calendar id with primary
    event_result = service.events().insert(
        calendarId=f'{name}', body=body
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


def list_events_summary():
    service = get_calendar_service()
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTCtime
    print('Getting List of events')
    events_result = service.events().list(
        calendarId=f'{name}', timeMin=now,
        maxResults=100, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    event_list = [new_event['summary'] for new_event in events]
    return event_list
