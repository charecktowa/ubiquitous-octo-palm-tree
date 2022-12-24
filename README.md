# ubiquitous-octo-palm-tree
It is a simple Python script that uses `PyWhatKit` and ChatGPT Wrapper to send messages generated with ChatGPT.

## Why?
I hate to send messages in days like Christmas or New Year's Eve, so I decided to use ChatGPT to generate different messages to different people. 

## TODO
- [ ] Refactor some code (maybe?)
- [ ] Allow somehow import multiple contacts from somewhere
- [ ] Maybe use directly OpenAI API instead of ChatGPT
- [ ] Allow some input to generate different messages according to the person that the message is sent
- [ ] Create a CLI-like application

## Install
I think I should improve this section. But simple install `requirements.txt`

```bash
$ pip install requirements.txt
```

After that edit the app.py file and edit gpt_input variable in order to generate a message and edit number variable with contact number.

Before running the script, make sure to install a browser in playwright and then "install" and run `chatgpt install`in order to get access to ChatGPT

```bash
playwright install firefox
chatgpt install

```