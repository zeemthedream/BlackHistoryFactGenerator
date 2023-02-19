# Black History Fact Generator 
Beginner friendly python project that generates random facts about black history using the [Black History Fact API](https://blackhistoryapi.com/) and [Google Custom Search Api](https://developers.google.com/custom-search/v1/introduction).

# Preliminary Instructions (In the order of the code walkthrough video)
### Black History Fact API
1. Get API Key from [Black History Fact Api](https://blackhistoryapi.com/) by signing up (free and API key will be sent to your email)
   - paste API key into secret.py file

### Google Custom Search API
2. Generate an API Key for your Custom Search Engine: https://developers.google.com/custom-search/v1/introduction
   - paste custom search API key into secret.py file
3. Restrict this API Key to be used for the Custom Search API only: https://console.cloud.google.com/apis/credentials
4. Create a new Programmable Search Engine (Used for searching images of people): https://programmablesearchengine.google.com/controlpanel/all
    - Include useful websites for (sites to search) images
    - Make sure to enable "Image search" on for Search Settings
    - paste engine code into secret.py file

## Packages/Libraries needed for this project
``` 
import io
import requests
import webbrowser
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image
from googleapiclient.discovery import build
from secret import blackHistoryToken, googleApiKey, engineCode
```

Installing Google and PIL packages through terminal:
1. `pip install google-api-python-client`
2. `pip install pillow`
 