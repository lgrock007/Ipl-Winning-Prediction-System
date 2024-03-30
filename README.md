The IPL Winning Prediction System utilizes logistic regression algorithm implemented with NumPy and Pandas to predict the outcome of IPL matches. It reads match-related data from a dataset using Pandas, preprocesses the data, selects relevant features, and trains a logistic regression model. This model is then used to predict the probability of winning for each team based on input parameters such as batting team, bowling team, city, target runs, current score, overs, and wickets. The system provides users with accurate predictions, aiding cricket enthusiasts in making informed decisions and analyzing match outcomes effectively.

Here's a brief description of the system's functionality:

1. **Input Selection**: Users can select the batting team, bowling team, and the host city ground where the match is being played. They can also input the target run set by the batting team.

2. **Match Status Input**: Users can input the current score, completed overs, and the number of wickets gone in the match.

3. **Prediction**: After providing the necessary inputs, users can click on the "Predict Probability" button to trigger the prediction process.

4. **Probability Display**: The system predicts the probability of winning for both the batting and bowling teams based on the provided inputs and displays the results in a table format. The probabilities are represented as percentages.

5. **Usage**: This system can be used by cricket enthusiasts, fans, and even analysts to get insights into the potential outcomes of IPL matches based on historical data and match conditions.

6. **Deployment**: The system is deployed as a web application using Streamlit, making it accessible to users through a web browser. It utilizes machine learning models trained on historical IPL match data to make predictions.

Tools and technologies Used :

1. **Python**: Python is the primary programming language used for building the prediction model, data manipulation, and web application development.

2. **Jupyter Lab**: JupyterLab is utilized for data analysis, model training, and testing. It provides an interactive development environment suitable for exploring data and experimenting with machine learning algorithms.

3. **Streamlit**: Streamlit is used to create the web application interface for the prediction system. It allows developers to build interactive web applications using simple Python scripts, making it easy to integrate machine learning models and data visualization.

4. **Visual Studio Code (VSCode)**: VSCode serves as the integrated development environment (IDE) for writing and managing the Python codebase. It offers features like syntax highlighting, code completion, and debugging tools, enhancing the development workflow.