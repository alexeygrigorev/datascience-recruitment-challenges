# Spectrm AI Hiring Challenge

Knowing what to say is not always easy - especially if you're a chatbot. 

Generating answers from scratch is very difficult and would most likely result in [nonsense](http://benjamin.wtf/) or [worse](https://twitter.com/tayandyou) - but definitely not a pleasant user experience. Therefore we're taking one step back and instead provide the correct replies which now "only" have to be chosen in the right dialog context.

In this challenge you're given a dataset with fictional dialogs (adapted from \[1\]) from which one reply is missing and additionally a list with all missing replies. Your task is to map all missing replies to the correct conversation.

### Dataset
The dataset consists of 4 files:
`train_dialog.txt` and `test_dialog.txt` each contain the conversations. The format is always `c#####` indicating the conversation number separated by `+++$+++` from the reply text. For example one conversation from the training set is the following:
```
c03253 +++$+++ Wow! This is like my dream room! Are these all records!
c03253 +++$+++ I have about fifteen hundred 78s at this point. I've tried to pare down my collection to the essential...
c03253 +++$+++ God, look at this poster!  I can't believe this room! You're the luckiest guy in the world! I'd kill to have stuff like this!
c03253 +++$+++ Please... go ahead and kill me! This stuff doesn't make you happy, believe me.
c03253 +++$+++ You think it's healthy to obsessively collect things? You can't connect with other people so you fill your life with stuff...  I'm just like all the rest of these pathetic collector losers.
```
All original conversations are at least four lines long and always the second to last line is missing in the dialogs.

The missing replies are found in the files `train_missing.txt` and `test_missing.txt` respectively. For the training dialogs, the conversation number is given with the reply as in the dialog files, e.g. the missing line to the above conversation would be
```
c03253 +++$+++ Oh, come on! What are you talking about?
```
The missing lines for the test dialogs always have `c00000` as the conversation number but are otherwise formatted the same as the training file.
While some of the short replies might be the same, every missing reply belongs to exactly one conversation.

### Task
Your task is now to take the missing test replies and map them to the corresponding dialogs. More specifically you should write a script `match_dialogs.py` which can be called with the path to a file with the incomplete dialogs and the path to the missing replies and then outputs a file `test_missing_with_predictions.txt` in the same format as `test_missing.txt` only with actual conversation numbers from `test_dialog.txt` instead of `c00000`.

You can chose whatever approach you want to solve the task, we only ask you to please write your code in **Python 2.7** and if you use any external libraries provide a `requirements.txt` file from which these libraries can be installed with `pip install -r requirements.txt` (you might want to use a virtual environment and when you're done call `pip freeze > requirements.txt`). 

While it is okay to use other resources such as pretrained word embeddings to solve the task, we ask you not to train your algorithm using the original conversations provided with \[1\] as this would lead to overfitting, i.e. considered cheating.

You should **turn in all the code required to solve the task**, i.e. which allows us to create the `test_missing_with_predictions.txt` file from the file without labels. Besides the accuracy of the predicted conversation labels we will also evaluate your code with respect to efficiency, maintainability, and readability (it might not hurt to have a look at some [style guides](https://google.github.io/styleguide/pyguide.html)).

In addition to the code which solves the task please turn in a text file or pdf with **answers to the following questions**:

1. Describe your approach. Which methods did you chose and why?
2. How do you evaluate your performance?
3. Where are the weaknesses of your approach? What has to be considered when applying an approach like this in practice?

Feedback to the challenge itself is appreciated as well. We acknowledge that this task is quite hard and we do not expect a perfect solution. We're more interested in how you approach a difficult problem, how you think and code. If you don't have the time to implement everything you wanted to try out, it is also okay if you only turn in a basic solution and then when answering the questions explain which other approaches might improve the performance.

We hope you'll have fun with this challenge and we're very much looking forward to your solution! If you have any questions please send an email to franzi@spectrm.de. If you already have an interview scheduled with us, please **send us your solution at least two days before your interview** to give us enough time to review it. Thanks!



\[1\]   "Chameleons in imagined conversations: A new approach to understanding coordination of linguistic style in dialogs"  
     Cristian Danescu-Niculescu-Mizil and Lillian Lee  
     Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics, ACL 2011.  
