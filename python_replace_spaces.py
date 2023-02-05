while(True):
    
    sentence = input("Cümle: ")
    sentence = sentence.replace(" ", "_")

    def BoslukCevir(sent):
        print("_" +sent)

    BoslukCevir(sentence)
