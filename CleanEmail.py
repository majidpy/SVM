# notes:
# This modules takes plain text or html page and cleans it by remove all the html tags
# In return, it counts number of http, https or <a> tags.
# It also counts number of dollar signs and emails in the body.

from bs4 import BeautifulSoup
import re


def main():
    print('Please import the module')


class CleanBody:

    def __init__(self, body):
        self.body = body
        self.clean_body = body
        self.html_count = 0
        self.email_count = 0
        self.dollar_count = 0

    def a_tag_count(self):
        # if there is html tags in the body of the email
        soup = BeautifulSoup(self.body, 'lxml')
        all_a_tags = soup.find_all('a')
        if all_a_tags:
            self.html_count += len(all_a_tags)
            for tag in all_a_tags:
                patt = re.compile(str(tag))
                self.body = re.sub(patt, 'httpaddr', self.body)

        # if there is plain text in the body of the text
        patt = re.compile('(http|https)\S+')
        http_tags = re.findall(patt, self.body)
        self.body = re.sub(patt, 'httpaddr', self.body)
        self.html_count += len(http_tags)

        return self.html_count

    def email_tag_count(self):
        patt = re.compile('\S+@\S+\.\S+')
        email_tags = re.findall(patt, self.body)
        self.body = re.sub(patt, 'emailaddr', self.body)
        self.email_count += len(email_tags)

        return self.email_count

    def dollar_tag_count(self):
        patt = re.compile('\$\s?\d+\.?\d+')
        dollar_tags = re.findall(patt, self.body)
        self.body = re.sub(patt, 'dollarnumb', self.body)
        self.dollar_count += len(dollar_tags)

        return self.dollar_count

    def remove_all_tags(self):

        # first make sure all <a> tags are counted for, and not to accidentally remove them
        print('number of <a> tags before starting to remove the tags is: {}'.format(self.a_tag_count()))

        # make sure all $ signs are removed and counted
        print('number of $ signs before starting to remove them is: {}'.format(self.dollar_tag_count()))

        # make sure all emails are removed and counted
        print('number of emails before starting to remove them is: {}'.format(self.email_tag_count()))

        # removing numbers
        patt = re.compile('\d+\.?\d*')
        self.body = re.sub(patt, 'number', self.body)

        # removing special characters
        patt = re.compile('\W')
        self.body = re.sub(patt, ' ', self.body)

        # return clean text
        soup = BeautifulSoup(self.body, 'lxml')
        self.clean_body = ' '.join(soup.find_all(text=True))

        return self.clean_body

if __name__ == '__main__':
    main()
