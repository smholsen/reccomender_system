import json
import os

input_filename = '../one_week/20170101'
rootPath = os.path.abspath('.')
input_file = rootPath + os.sep + input_filename

active_time_appender = open('active_time_data.txt', 'a')
keywords_appender = open('keywords_data.txt', 'a')

first_keywords_line = True
first_active_time_line = True
print('Starting')


def rate_article(time_spent_on_article):
    # Time spent on article is denoted in seconds.
    # This value is used to determine the users rating for the given article.
    # If the did spend time on the article, and does not early click away,
    # then we assume that the user enjoyed reading the article, and we give the article a rating of 1.
    # If the user quickly clicked away from the article, we assume the user did not enjoy it, and we give the
    # article a low rating from the user.
    # Thus, we here assume a rating range of 0 through 1 and denote it binary.
    # This drastically affects our scoring for the actual testing of our fitting, described in more detail in the
    # core_recommender script.
    if time_spent_on_article > 20:
        return 1
    else:
        return 0

# Before we continue with the filtering of our datasets, we need to do some additional pre processing.
# From what I gather, SciKit Learn's cross validation library only accepts numeric values,
# even for their ID fields.
# I guess I believe this is because it wants to be as generic as possible but I am not sure.
# Now, this seems weird, so I am not sure, but this is what I found,
# and after trials and fails I propose we do the following:
# We can run through the sets before we do the actual filtering and encode each userID and articleID to numeric values.
# I suggest that this is better than doing it while we are

for line in open(input_file):
    obj = json.loads(line.strip())
    try:
        uid, iid = obj['userId'], obj['id']
        keywords = obj['keywords'] if 'keywords' in obj else 'None'
        active_time = str(obj['activeTime']) if 'activeTime' in obj else '0'
    except Exception as e:
        # TODO Wtf happened here? Also specify Exceptions. Needed though?
        # I say fuck it, What could co so wrong?  ᕕ( ᐛ )ᕗ
        continue

    if not keywords == 'None':
        s = u'*'.join([uid, iid, keywords])
        if first_keywords_line:
            keywords_appender.write(s)
            first_keywords_line = False
        else:
            keywords_appender.write('\n')
            keywords_appender.write(s)
    if not active_time == '0':

        # TODO: We should implement a smarter method to evaluate articles based on the users behavior.
        # Here we should implement a method give some sort of rating from the user to the article.
        # Currently I just implemented a simple boolean check to see whether or not the user spent time on the article.
        # Please see the rate_article fn for a better explanation.

        article_rating = rate_article(active_time)

        s = u'*'.join([uid, iid, article_rating])
        if first_active_time_line:
            active_time_appender.write(s)
            first_active_time_line = False
        else:
            active_time_appender.write('\n')
            active_time_appender.write(s)
print('Done')