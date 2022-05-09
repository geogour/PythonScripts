import pandas as pd
import yagmail
import os

sender = os.environ['SENDER']
receiver = os.environ['RECEIVER']
password = os.environ['PASSWORD']
yag = yagmail.SMTP(user=sender, password=password)
subject = ["""CSV bill amount"""]

df = pd.read_csv('contacts.csv')

def generate_file(filename,content):
  with open(filename, 'w') as file:
    file.write(str(content))

for index, row in df.iterrows():
  name = row['name']
  amount = row['amount']
  receiver = row['email']
  filename = name + ".txt"
  generate_file(filename, amount)
  contents = [f"""Hello {name} ,your bill is {amount} and your file attached""", {filename}]
  
  yag.send(to=receiver, subject=subject, contents=contents)
  print("Email Sent!")
