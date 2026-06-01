
# F.R.I.D.A.Y.

F.R.I.D.A.Y. (or Financial Resource Intelligence & Digital Asset Yielder) is an AI Model which can help you in your finanical assistance and needs with the help of Gemini.
I have used AI in the Project for the Chatting with the user but it is not used in the README and in any other parts as well.

At the start, It will ask these following things:
 - Your Age
 - Your Country of Residence
 - Monthly Income vs Expense 

This will help the AI Model give to better data to understand your queries. You can chat with the AI Model right now using the Link in the Demo Section.

I have also implemented a Memory Bank System in order to remember the current conversation till you chat with it.

I made this is python with the GoogleGenAI, Flask and Markdown libraries.
Here is a Live Demo Link and a GIF to show the project.

>[!NOTE]
>If you get the Critical Uplink error, it means that my free gemini limit is over and you would have to wait till the next day in order to chat with it.

![Live GIF](https://github.com/Aaron-230/F.R.I.D.A.Y/blob/main/images/Screen-Recording.gif)

[Demo Link!!!](https://web-ui-0rkx.onrender.com/)

### Step-by-Step Instructions to clone and experiment with the project.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Aaron-230/F.R.I.D.A.Y.git
    cd F.R.I.D.A.Y
    ```
2.  **Set up Gemini and Python:**
    Edit the `Client = genai.Client(api_key=API_KEY)` in `Main.py` file by changing the `API_KEY` to the API Key which you copied from the [Google Gemini](https://aistudio.google.com/api-keys) and setup the Python Environments with all the necessary libraries.
    
3.  **Deployment Command:**
    ```python
	   $ python3 main.py
    ```

>[!NOTE]
>You can also use `python main.py` to run the code as well

>[!IMPORTANT]
>Make sure that you are in the Cloned Repository Folder and not on the main user folder.

Feel free to contribute to the project and add new and great feature. Any contributions you make are **greatly appreciated**.
Here is how to contribute to the project!

1.  **Fork** the Project.
2.  Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.
