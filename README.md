# dune-to-gsheets

Uploads the results of Dune Analytics queries to a google sheet.

## Installation

### Generating Google API Key
To allow a script to use Google Drive API we need to authenticate our self towards Google. To do so, we need to create a project, describing the tool and generate credentials. Please use your web browser and go to [Google console](https://console.cloud.google.com/apis/dashboard) and :

Choose “Create Project” in popup menu on the top.
- A dialog box appears, so give your project a name and click on “Create” button.
- On the left-side menu click on “API Manager”.
- A table of available APIs is shown. Switch “Drive API” and click on “Enable API” button. Other APIs might be switched off, for our purpose.
- On the left-side menu click on “Credentials”.
- In section “OAuth consent screen” select your email address and give your product a name. Then click on “Save” button.
- In section “Credentials” click on “Add credentials” and switch “OAuth 2.0 client ID”.
- A dialog box “Create Cliend ID” appears. Select “Application type” item as “Other”.
- Click on “Create” button.
- Click on “Download JSON” icon on the right side of created “OAuth 2.0 client IDs” and store the downloaded file on your file system. Please be aware, the file contains your private credentials, so take care of the file in the same way you care of your private SSH key; i.e. move downloaded JSON file to ~/.gdrive_private.
- **Copy the downloaded JSON file into the root directory of the dune-to-gsheets project. Rename the file to `dune-to-gsheets.json`** 
- Then, the first time you run it your browser window will open a google authorization request page. Approve authorization and then the credentials will work as expected. 
	- If you do not approve authorization you will receive errors in execution:
		- `Access Not Configured. Drive API has not been used in project`<PROJECT_ID>`before or it is disabled. Enable it by visiting `https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=<PROJECT_ID>` then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry."`
		- `'Google Sheets API has not been used in project `<PROJECT_ID>` before or it is disabled. Enable it by visiting `https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project= <PROJECT_ID>` then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.'`
	- Follow these links to approve authorization

### Configuring Dune Login
In `dune-to-gsheets/config.json` add your username and password for Dune Analytics to the configuration:

    {
	    "duneanalytics":{
		    "username":"** NEW USERNAME **",
		    "password":"** NEW PASSWORD **"
	    },
	    "googlesheets":{
		    "spreadsheetkey": ""
	    }
	}
  
### Configuring Google Workbook
In `dune-to-gsheets/config.json` add the key of the target workbook:

    {
	    "duneanalytics":{
		    "username":"username",
		    "password":"password"
	    },
	    "googlesheets":{
		    "spreadsheetkey": "** 1xg_v5n2QbRbBM.............26SD5pgzRBY **"
	    }
	}
  




