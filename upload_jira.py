import pysftp,glob
from jira import JIRA

srv = pysftp.Connection(host="", username="",password="")
authed_jira = JIRA('https://vuclipdev.atlassian.net/', basic_auth=(username, passowrd))

issue=raw_input('Enter jira ID::')
files=srv.listdir('/tmp/test1/')
file=srv.listdir('/tmp/test2/')

for i,j in zip(files,file):
	srv.chdir('/tmp/test1/')
	print i
	print srv.get(i)
	srv.chdir('/tmp/test2/')
	print j
	print srv.get(j)

for opfiles in glob.glob('/home/roshans/testing/v*.csv'):
	authed_jira.add_attachment(issue,opfiles)

authed_jira.add_comment(issue,'files uploaded')


