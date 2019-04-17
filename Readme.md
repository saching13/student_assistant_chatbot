## Steps to run the bot for testing
 - Run the following endpoint hook to register the custom actions
   
    ``` code
    python3 -m rasa_core_sdk.endpoint --actions actions
    ```
- Run the duckling server for slot detection
   ``` code
   docker run -p 8000:8000 rasa/duckling
   ```

- Run the agent code
     