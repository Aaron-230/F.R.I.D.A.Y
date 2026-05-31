
# F.R.I.D.A.Y.

F.R.I.D.A.Y. (or Financial Resource Intelligence & Digital Asset Yielder) is an AI Model which can help you in your finanical assistance and needs with the help of Gemini.
I have used AI in the Project for the Chatting with the user but it is not used in the README and in any other parts as well.

## 🚀 About the Project

F.R.I.D.A.Y. (or Financial Resource Intelligence & Digital Asset Yielder) is an AI Model which can help you in your finanical assistance and needs. It runs using the Google Gemini API with Grounded Searching for all your financial assistance and needs. At the start, It will ask these following things:
 - Your Age
 - Your Country of Residence
 - Monthly Income vs Expense 

This will help the AI Model give to better data to understand your queries. You can chat with the AI Model right now using the Link in the Demo Section.

## 🛠️ Built With

**Language:** [Python 3.14 or newer](https://www.python.org/downloads/)
**Libraries:** [Flask](https://pypi.org/project/Flask/), [Google GenAI](https://pypi.org/project/google-genai/), [Markdown](https://pypi.org/project/Markdown/)

## 📺 Demo

![Live GIF](https://github.com/Aaron-230/F.R.I.D.A.Y/blob/main/images/Screen-Recording.gif)

[Demo Link!!!](https://web-ui-0rkx.onrender.com/)

## 🚢 Deployment

Follow these steps to deploy the project to a production environment.

### Prerequisites: Check 🛠️ Built With

### Step-by-Step Instructions
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

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  **Fork** the Project.
2.  Create your **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3.  **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  **Push** to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
