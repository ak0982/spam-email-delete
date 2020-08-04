#!/usr/bin/python3.6
"""AutoDelete
This script auto deletes messages from your gmail inbox.
The perfect usecase is deleting the OTP messages received from banks after certain time period.
or deleting the messages received from certain services which doesn't have unsubscribe option.
Many parts of this script are copied from EZGmail by Al Sweigart (https://github.com/asweigart/ezgmail)
"""

import os
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import errors
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('u_auto_delete_it.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

SCOPES = 'https://mail.google.com/'  # read-write mode
SERVICE = None


class AutoDeleteException(Exception):
    pass  # This class exists for this module to raise for AutoDelete-specific problems.


def init(user_id='me', token_file='token.json', credentials_file='credentials.json'):
    """Populates SERVICE  global variable
    The account is determined by the credentials.json file, downloaded from Google, and token.json. If the token.json file hasn't been generated yet, this function will open the browser to a page to let the user log in to the Gmail account that he will use.
    Parameters
    __________
    user_id : str
        User id of the Gmail User (default is 'me')
    token_file : str
        The filename of 'token.json' file (This is auto downloaded when this function runs)
    credentials_file : str
        The filename of 'credentials.json. This can be downloaded from 'https://developers.google.com/gmail/api/quickstart/python and clicking "Enable the Gmail API'
    Returns
    _______
    SERVICE
    """

    global SERVICE

    if not os.path.exists(credentials_file):
        raise AutoDeleteException('Can\'t find credentials file at %s. You can download this file from https://developers.google.com/gmail/api/quickstart/python and clicking "Enable the Gmail API"' % (os.path.abspath(credentials_file)))

    store = file.Storage(token_file)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(credentials_file, SCOPES)
        creds = tools.run_flow(flow, store)
    SERVICE = build('gmail', 'v1', http=creds.authorize(Http()))


def search(query, user_id='me'):
    """Returns a list of gmail thread objects of all the messages matching query
    Parameters
    __________
    query : str
        The string Exactly you will use in Gmail's Search Box
        label:UNREAD
        from:abc@email.com
        subject:hello
        has:attachment
        more described at https://support.google.com/mail/answer/7190?hl=en
    user_id : str
        User id of the Gmail User (default is 'me')
    Returns
    _______
    list
        List of Messages that match the criteria of the query.
        Note that the returned list contains Message IDs, you must use get with the appropriate ID to get the details of a Message.
    """

    if SERVICE is None:
        init()

    try:
        response = SERVICE.users().messages().list(userId=user_id,
                                                   q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = SERVICE.users().messages().list(userId=user_id, q=query,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages
        # print(len(messages))

    except errors.HttpError as e:
        logger.exception(f'An error occurred:{e}')



def delete_messages(query, user_id='me'):
    """Deletes the message matching the query
    Parameters
    __________
    query : str
        The string Exactly you will use in Gmail's Search Box
        label:UNREAD
        from:username@email.com
        subject:hello
        has:attachment
        more described at https://support.google.com/mail/answer/7190?hl=en
    user_id : str
        User id of the Gmail User (default is 'me')
    """
    messages = search(query)
    print(len(messages))

    if messages:
        for message in messages:
            print(message)
            SERVICE.users().messages().delete(userId=user_id, id=message['id']).execute()
            logger.info(f'Message with id: {message["id"]} deleted successfully.')
    else:
        logger.info("There was no message matching the query.")


def queryy():


    logger.info("Deleting messages from abc@gmail.com.")
    delete_messages('from:mailout@maillist.codeproject.com' )

    delete_messages('mailed-by:student@internshala.com'     )

    
 #  update+kjdkku_dkmvm@facebookmail.com
    delete_messages('from:Codeforces@codeforces.com')    

   
    delete_messages('from:onlinecourses@nptel.iitm.ac.in'            )
    delete_messages('from:info@content.sonyliv.com'            )
    delete_messages('from:info@naukri.com'            )
    delete_messages('from:no-reply@e.udemymail.com'            )
    delete_messages('from:no-reply@ncb.flipkart.com'          )
    delete_messages('from:team@unacademy.com'          )
    delete_messages('from:no-reply@swiggy.in'            ) 

    delete_messages('from:curiosity-noreply@quora.com'            ) 
    delete_messages('from:updates@academia-mail.com'            ) 
    delete_messages('from:student@internshala.com'            ) 
    delete_messages('from:updates@academia-mail.com'            )
    delete_messages('from:student@internshala.com'            )
    delete_messages('from:curiosity-noreply@quora.co'            )
    delete_messages('from:noreply@youtube.com'            )
    delete_messages('from:curiosity-noreply@quora.com'            )
    delete_messages('from:no-reply@m.mail.coursera.org'            )
    delete_messages('from:recommendations@inspire.pinterest.com'            )
    delete_messages('from:recommendations@explore.pinterest.com'            )
    delete_messages('from:demand@mail.adobe.com'            )
    delete_messages('from:premium@academia-mail.com'            )
    delete_messages('from:hello@accounts.scribd.com'            )
    delete_messages('from:digest-noreply@quora.com'            )

    delete_messages('from:noreply@redditmail.com'            )
    delete_messages('from:no-reply@mail.instagram.com'            )
    delete_messages('from:udemy@email.udemy.com'            )
    delete_messages('from:mail@info.paytm.com'            )
    delete_messages('from:quota-of-quotes-space@quora.com'            )
    delete_messages('from:noreply@codeforces.com'            )
    delete_messages('from:no-reply@paytm.com'            )
    delete_messages('from:no-reply@sampark.gov.in'            )
    delete_messages('from:no-reply@geeksforgeeks.org'            )
    delete_messages('from:digest-noreply@quora.com'            )
    delete_messages('from:news_alerts@shiksha.com'            )
    delete_messages('from:yonobysbi@sbi.co.in'            )
    delete_messages('from:no-reply@travel.e-redbus.in'            )
    delete_messages('from:no-reply@t.mail.coursera.org'            )
    delete_messages('from:noreply@hedera.com'            )
    delete_messages('from:security@facebookmail.com'            )
    delete_messages('from:verify@unimartemaills.com'            )

    delete_messages('from:life-is-beautiful-space@quora.com'            )
    delete_messages('from:Notification@jio.com'            )
    delete_messages('from:info@crm.sonyliv.com'            )
    delete_messages('from:greetings@travel.e-redbus.in'            )
    delete_messages('from:hackers@hackerrankmail.com'            )
    delete_messages('from:no-reply@updates.bookmyshow.com'            )
    delete_messages('from:info@crm.sonyliv.com'            )
    delete_messages('from:anirbanfuture@gmail.com'            )
    delete_messages('from:shipment-tracking@amazon.in'            )
    delete_messages('from:hindi-digest-noreply@quora.com'            )
    delete_messages('from:auto-confirm@amazon.in'            )
    delete_messages('from:payments-update@amazon.in'            )
    delete_messages('from:hello@explore.bookmyshow.com'            )

    delete_messages('from:naukrialerts@naukri.com'            )
    delete_messages('from:store-news@amazon.in'            )
    delete_messages('from:history-of-india-space@quora.com'            )
    delete_messages('from:learn@codecademy.com'            )
    delete_messages('from:info@easemytrip.com'            )
    delete_messages('from:hello@newsletter.bookmyshow.com'            )
    delete_messages('from:do-not-reply@amazon.in'            )
    delete_messages('from:gssportssgc@iiitg.ac.in'            )
    delete_messages('from:naukrialerts@naukri.com'            )
    delete_messages('from:noreply@olacabs.comnoreply@olacabs.com'            )
    delete_messages('from:noreply-local-guides@google.com'            )
    delete_messages('from:gswelfaresgc@iiitg.ac.in'            )

    
    delete_messages('from:info@myntra.com'            )
    delete_messages('from:recharges@amazon.in'            )
    delete_messages('from:AmazonPay-balance@amazon.in'            )
    delete_messages('from:do-not-reply@amazon.in'            )
    delete_messages('from:naukrialerts@naukri.com'            )
    delete_messages('from:digest-noreply@quora.com'            )

    delete_messages('from:digest-noreply@quora.com'            )
    delete_messages('from:digest-noreply@quora.com'            )
    delete_messages('from:digest-noreply@quora.com'            )















































if __name__ == '__main__':

    queryy()

 #    logger.info("Deleting messages from abc@gmail.com.")
 #    delete_messages('from:mailout@maillist.codeproject.com' )

 #    delete_messages('mailed-by:student@internshala.com'     )

    
 # #  update+kjdkku_dkmvm@facebookmail.com
 #    delete_messages('from:Codeforces@codeforces.com')    

   
 #    delete_messages('from:onlinecourses@nptel.iitm.ac.in'            )
 #    delete_messages('from:info@content.sonyliv.com'            )
 #    delete_messages('from:info@naukri.com'            )
 #    delete_messages('from:no-reply@e.udemymail.com'            )
 #    delete_messages('from:no-reply@ncb.flipkart.com'          )
 #    delete_messages('from:team@unacademy.com'          )
 #    delete_messages('from:no-reply@swiggy.in'            ) 

 #    delete_messages('from:curiosity-noreply@quora.com'            ) 
 #    delete_messages('from:updates@academia-mail.com'            ) 
 #    delete_messages('from:student@internshala.com'            ) 
 #    delete_messages('from:updates@academia-mail.com'            )
 #    delete_messages('from:student@internshala.com'            )
 #    delete_messages('from:curiosity-noreply@quora.co'            )
 #    delete_messages('from:noreply@youtube.com'            )
 #    delete_messages('from:curiosity-noreply@quora.com'            )
 #    delete_messages('from:no-reply@m.mail.coursera.org'            )
 #    delete_messages('from:recommendations@inspire.pinterest.com'            )
 #    delete_messages('from:recommendations@explore.pinterest.com'            )
 #    delete_messages('from:demand@mail.adobe.com'            )
 #    delete_messages('from:premium@academia-mail.com'            )
 #    delete_messages('from:hello@accounts.scribd.com'            )

   






