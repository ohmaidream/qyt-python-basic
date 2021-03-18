from CH1 import vocab

correct = {}
wrong = {}

while True:
    for words in vocab.keys():
        answer = input(words)
        if answer == vocab.get(words):
            print("good")
            correct[words] = vocab.get(words)
            del wrong[words]
        else:
            answer = input(words)
            if answer == vocab.get(words):
                print("good")
                correct[words] = vocab.get(words)
                del wrong[words]
            else:
                print(vocab.get(words))
                wrong[words] = vocab.get(words)
    if len(vocab) != len(correct):
        again = input("do you want to try again? y/n")
        if again == 'n':
            print(wrong)
            break
    else:
        print("Congratulations!")
        break
