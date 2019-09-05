import os
import re

Input_File = os.path.join("Resources", "paragraph_1.txt")

with open(Input_File) as textfile:

    Para = textfile.read()

#Approximate word count 
Word_Count = len(Para.split(" "))

#Approximate sentence count
Sentences = re.split("(?<=[.!?]) +", Para)
Sentence_Count = len(Sentences)

#Approximate letter count (per word)
Letter = re.sub('[^a-zA-Z]', '', Para)
Letter_Count = format(len(Letter)/Word_Count, '.2f')

#Average sentence length (in words)
Avg_Sentence_Length = format(Word_Count/len(Sentences))


#Displayiny the Paragraph Analysis Output
Para_Analysis = (
f"\n---------------------------------------------------------------\n\n"
f"                   Paragraph Analysis \n"
f"\n---------------------------------------------------------------\n\n"
f"Approximate Word Count: {Word_Count} \n\n"
f"Approximate Sentence Count: {Sentence_Count} \n\n"
f"Average Letter Count (per word): {Letter_Count} \n\n"
f"Average Sentence Length (in words) : {Avg_Sentence_Length} \n\n"
f"---------------------------------------------------------------\n" 

)

print(Para_Analysis)

# Write all of the election data to a text file
outputfile = os.path.join("../PyParagraph/Output", "Paragraph_Analysis_Output.txt")
with open(outputfile, "w") as txt_file:
    txt_file.write(Para_Analysis)
        
print("\nThe Paragraph Analysis Data has been exported to Paragraph_Analysis_Output.txt file in the Output Folder\n")