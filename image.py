import speech_recognition
from gtts import gTTS
import os
print("1. learn A")
print("2. learn B")
print("3, learn c")
print("enter your choice")

x=int(input())
if x==1:
    import speech_recognition
    from gtts import gTTS
    import os
    UserVoiceRecognizer = speech_recognition.Recognizer()
    print("speak something:")
    while(1):
        try:

            with speech_recognition.Microphone() as UserVoiceInputSource:
    
                UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
    
                # The Program listens to the user voice input.
                UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
    
                UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.upper()
                print(UserVoiceInput_converted_to_Text)
                first=UserVoiceInput_converted_to_Text.index('A')
                # last=UserVoiceInput_converted_to_Text.rindex()
                if UserVoiceInput_converted_to_Text == 'A':
                
                    mytxt = 'perfect!,move on to the next module'

    # Language we want to use
                    language1 = 'en'

                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)

                    myobj1.save("output1.mp3")

    # Play the converted file
                    os.system("start output1.mp3")
                
                elif first == 0:
                    mytext = UserVoiceInput_converted_to_Text[1:]
                elif (first>0) :
                    mytext = 'Oh no!you said' + UserVoiceInput_converted_to_Text[0:first] +'at the begining  and' + UserVoiceInput_converted_to_Text[(first+1):] +'at the end'
                else :
                    mytext = 'wrong word'

                    # Language we want to use
                language = 'en'

                myobj = gTTS(text=mytext, lang=language, slow=False)

                myobj.save("output.mp3")

    # Play the converted file
                os.system("start output.mp3")
                    
        except KeyboardInterrupt:
            print('A KeyboardInterrupt encountered; Terminating the Program !!!')
            exit(0)

        except speech_recognition.UnknownValueError:
            print("No User Voice d+etected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
if (x ==2):

    UserVoiceRecognizer = speech_recognition.Recognizer()
    print("speak something:")
    while(1):
        try:

            with speech_recognition.Microphone() as UserVoiceInputSource:
    
                UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
    
                # The Program listens to the user voice input.
                UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
    
                UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.upper()
                print(UserVoiceInput_converted_to_Text)
                first=UserVoiceInput_converted_to_Text.index('B')
                # last=UserVoiceInput_converted_to_Text.rindex()
                if UserVoiceInput_converted_to_Text == 'B':
                
                    mytxt = 'perfect!,move on to the next module'

    # Language we want to use
                    language1 = 'en'

                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)

                    myobj1.save("output1.mp3")

    # Play the converted file
                    os.system("start output1.mp3")
                
                elif first == 0:
                    mytext = UserVoiceInput_converted_to_Text[1:]
                elif (first>0) :
                    mytext = 'Oh no!you said' + UserVoiceInput_converted_to_Text[0:first] +'at the begining  and' + UserVoiceInput_converted_to_Text[(first+1):] +'at the end'
                else :
                    mytext = 'wrong word'

                    # Language we want to use
                language = 'en'

                myobj = gTTS(text=mytext, lang=language, slow=False)

                myobj.save("output.mp3")

    # Play the converted file
                os.system("start output.mp3")
                    
        except KeyboardInterrupt:
            print('A KeyboardInterrupt encountered; Terminating the Program !!!')
            exit(0)

        except speech_recognition.UnknownValueError:
            print("No User Voice d+etected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
if (x ==3):

    UserVoiceRecognizer = speech_recognition.Recognizer()
    print("speak something:")
    while(1):
        try:

            with speech_recognition.Microphone() as UserVoiceInputSource:
    
                UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
    
                # The Program listens to the user voice input.
                UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
    
                UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
                UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.upper()
                print(UserVoiceInput_converted_to_Text)
                first=UserVoiceInput_converted_to_Text.index('C')
                # last=UserVoiceInput_converted_to_Text.rindex()
                if UserVoiceInput_converted_to_Text == 'C':
                
                    mytxt = 'perfect!,move on to the next module'

    # Language we want to use
                    language1 = 'en'

                    myobj1 = gTTS(text=mytxt, lang=language1, slow=False)

                    myobj1.save("output1.mp3")

    # Play the converted file
                    os.system("start output1.mp3")
                
                elif first == 0:
                    mytext = UserVoiceInput_converted_to_Text[1:]
                elif (first>0) :
                    mytext = 'Oh no!you said' + UserVoiceInput_converted_to_Text[0:first] +'at the begining  and' + UserVoiceInput_converted_to_Text[(first+1):] +'at the end'
                else :
                    mytext = 'wrong word'

                    # Language we want to use
                language = 'en'

                myobj = gTTS(text=mytext, lang=language, slow=False)

                myobj.save("output.mp3")

    # Play the converted file
                os.system("start output.mp3")
                    
        except KeyboardInterrupt:
            print('A KeyboardInterrupt encountered; Terminating the Program !!!')
            exit(0)

        except speech_recognition.UnknownValueError:
            print("No User Voice d+etected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
