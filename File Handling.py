#File Handling

#Creating first feedback file
with open("C:\\Users\\Lenovo\\Desktop\\Python\\Feedback1.txt",'w') as file:
   file.write("Customer's Feedback in First file:")
   file.write("\n Sonal: 5 - Excellent Service!!")
   file.write("\n Shaurya: 4 - Good Service, but could improve.")
   file.write("\n Omkar: 3 - Average Service, needs improvement.")
   file.write("\n Aarti: 4 - Quality Service.")
   file.write("\n Sagar: 5 - Very Efficient Service")
   file.write("\n Prasad: 5 - Excellent Service.")
   file.write("\n Kabir: 2 - Poor Service, needs improvement.")

#Creating second feedback file
with open("C:\\Users\\Lenovo\\Desktop\\Python\\Feedback2.txt",'w') as file:
   file.write("Customer's Feedback in Second file:")
   file.write("\n Swapnil: 5 - Very Good Service!")
   file.write("\n Diptee: 1 - Poor Service, must improve.")
   file.write("\n Rohini: 3 - Average Service, needs improvement.")
   file.write("\n Punam: 2 - Poor Service.")
   file.write("\n Devansh: 3 - Average Service.")
   file.write("\n Hemangi: 4 - Good Service!")

#Creating third feedback file
with open("C:\\Users\\Lenovo\\Desktop\\Python\\Feedback3.txt",'w') as file:
   file.write("Customer's Feedback in Third file:")
   file.write("\n Mahesh: 5 - Excellent Service!.")
   file.write("\n Vruddhi: 5 - Efficient Service!")
   file.write("\n Angad: 4 - Good Service!!")
   file.write("\n Komal: 3 - Average Service, needs improvement.")
   file.write("\n Athang: 1 - Very Bad Service.")
   file.write("\n Rishiv: 3 - Average Service ")
   file.write("\n Harshvardhan: 1 - Very Poor Service.")

#Function is defined/created to read the feedback files
def readfdbfiles(filenames):
    feedbacks = []
    for filename in filenames:
        try:
            with open(filename, 'r') as file:
                feedbacks.extend(file.readlines())
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An error occurred while reading {filename}: {e}")
    return feedbacks

# Function is defined/created to process the feedback data
def processfdbdata(feedbacks):
    processedfdbs = []
    totalratings = 0
    for feedback in feedbacks:
        try:
            customername, rest = feedback.split(': ', 1)
            rating, comment = rest.split(' - ', 1)
            rating = int(rating)
            processedfdbs.append((customername, rating, comment))
            totalratings += rating
        except ValueError:
            print(f"Error: Invalid format in the feedback entry: {feedback}")
    
    average_rating = totalratings/len(processedfdbs) if processedfdbs else 0
    return processedfdbs, average_rating

# Function is defined/created to assemble the file paths
def asm():
    # Assemble the file paths
    path = "C:\\Users\\Lenovo\\Desktop\\Python\\"
    filenames = [
        path + "Feedback1.txt",
        path + "Feedback2.txt",
        path + "Feedback3.txt"
    ]
    return filenames

# Function is defined/created to write a summary file
def writesummaryfile(filename, processedfdbs, average_rating):
    try:
        with open(filename, 'w') as file:
            file.write("Summary is generated successfully!!\n")
            file.write(f"\nTotal Feedback Entries: {len(processedfdbs)}\n")
            file.write(f"\nAverage Rating: {average_rating:.2f}\n")
            file.write("\nFeedbacks:\n")
            for feedback in processedfdbs:
                file.write(f"{feedback[0]}: {feedback[1]} - {feedback[2]}\n")
    except Exception as e:
        print(f"An error occurred while writing to {filename}: {e}")

#To read the feedbacks from all three input feedback files 
def adp():
    files = asm()
    feedbacks = readfdbfiles(files)
    processedfdbs, average_rating = processfdbdata(feedbacks)
    writesummaryfile('FeedbacksSummary.txt', processedfdbs, average_rating)
if __name__ == "__main__":
    adp()
