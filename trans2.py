from time import sleep
from google_trans_new import google_translator  
translator = google_translator()  
i = 0
j = 0
dest_lang = input("Enter code of dest language : ")
# translated_line = translator.translate("They are taking so long to hatch!", lang_tgt=dest_lang)
# #sleep(2)
# #writer.write(translated_line)
# print(translated_line)
# '''
with open("sub.txt",'r',encoding="utf-8") as reader , open('trans.srt','w',encoding="utf-8") as writer:
   for line in reader:
        i= i+1
        if(line =="\n"):        
            writer.write("\n"+line)
            i = 0
        if(i == 1):
            if(j ==1):
                line = line.split('\n')[0]
                writer.write(line[-1]+"\n")
                j = j+1
            else:   
                writer.write(line)
        if(i == 2):
            writer.write(line)
        if(i > 2):
            
            translated_line = translator.translate(line, lang_tgt=dest_lang)
            #sleep(2)
            #print(type(translated_line))
            try:
                writer.write(translated_line)
                print(translated_line)
            except:
                writer.write(translated_line[0])
                print(translated_line[0])
