
def show_messages(messages):
    for msg in messages:
        print(msg)
def send_messages(messages,sent_messages):
    while messages:
        current_sms = sms.pop(0)
        print(f"The message that is being sent right now is: {current_sms}")
        sent_messages.append(current_sms)
        print(sent_messages)
    
sms = ['hi','how are you doin?','Its raining outside']
sent_messages = []
show_messages(sms)
send_messages(sms,sent_messages)