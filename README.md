Chatbot.py is a Python program designed to assist students by providing information about university courses, professors' office hours, and library schedules.

Key Features:
Course Information: Users can ask about course schedules by mentioning the course code. If available in the dictionary, the chatbot will return the course's time and location.
Professor Information: Users can inquire about professors' office hours by providing the professor's last name. The chatbot will respond with office location and hours if the professor is in the dictionary.
Library Information: The chatbot provides the library's opening hours and borrowing rules.

How It Works:
The program listens for user input in a continuous loop.
It first checks if the user query contains the word "course". If so, it processes the course details and returns the information about timing and classroom.
If the query does not mention a course but includes "library", it provides the library’s hours and rules.
If neither course nor library information is requested, the chatbot will look for "professor" and return office hours and location if the professor's name is found.
If the query is a greeting (e.g., "hello", "hi"), the chatbot will return a response based on the predefined greeting list.
If the query does not match any of the above, the chatbot will inform the user that it couldn’t understand the request.