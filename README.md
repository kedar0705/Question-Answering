# Question-Answering

To run the FastAPI Question-Answering application and make requests to it using `request.py`, follow these steps:

1. Install the required dependencies:
   - `fastapi`: install it using `pip install fastapi`.
   - `transformers`: install it using `pip install transformers`.
   - `uvicorn`: install it using `pip install uvicorn`.
   - `requests`: install it using `pip install requests`.

2. Save the FastAPI code to a file, for example, `main.py`.

3. Create a Python file, for example, `request.py`, and save the provided code to it.

4. Run the FastAPI application using the following command:
   > uvicorn main:app --reload
   
   This will start the server on `http://127.0.0.1:8000/`.

5. In the `request.py` file, uncomment the lines under `data` and replace the example context and question with your own data. Alternatively, you can use the `input()` function to input the context and question at runtime.

6. Run the `request.py` file:
   > python request.py

   You will be prompted to enter the context and question. After entering them, the script will send a `POST` request to the FastAPI server.

7. The server will process the request and return the answer as a `JSON` response.

8. The `request.py` script will extract the answer from the response and print it.

By following these steps, you should be able to run the FastAPI application and make requests to it using the provided `request.py` script. Remember to have the FastAPI application running before executing the `request.py` script.



https://github.com/kedar0705/Question-Answering/assets/86918750/7b98ab19-9f7b-482f-9cb4-1d8f2604f9ee



