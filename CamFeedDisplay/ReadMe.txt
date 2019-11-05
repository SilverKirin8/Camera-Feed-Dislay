								****************************
								*   Camera Feed Display    *
								* Created by Randy McClure *
								****************************
# Installation
Ensure the following packages are installed:
Screen
	$> sudo apt install screen
	Note: May need to install "libutempter0" package directly (need more testing)
Python
	$> sudo apt-get install python

Extract and copy the "CamFeedDisplay" directory into any directory of your choosing.
	- When executing the script, you will need to include the full path to the script file, 
	open the terminal in the "CamFeedDisplay" directory (change the current working
	directory to "CamFeedDisplay", or add the "CamFeedDisplay" directory to the 
	PATH environment variable.
Add execute permission to the "DisplayFeeds.py" script
	$> sudo chmod +x ./installDir/CamFeedDisplay/DisplayFeeds.py


# Usage
1) Pick a template from the the "CamFeedTemplates" directory
	Note: See "Camera Template Layouts" below for previews of camera layouts and 
		corresponding template names
	Note: To create a custom feed display, see "Creating a Custom Feed Display"
2) Copy it to the root "CamFeedDisplay" directory
	Note: The template should be a neighbor to the "DisplayFeeds.py" file.
3) Rename the copied template to "cameraFeeds.json"
4) Edit the JSON file
	4.1) Replace each "[Camera Feed Name]" with a name for the feed
		Note: This value is only visible when manually administering screen sessions.
	4.2) Replace each "[Display Name]" with a user-friendly name for the feed
		Note: This name is seen in the top left corner of each feed.
	4.3) Replace each "[RTSP Stream ID ...]" with the RTSP stream URI
		Note: Retrieve this URI from the camera management console.
5) Save the file after making the necessary changes
6) Execute the script with the following command in a terminal
	$> /path/to/install/dir/CamFeedDisplay/DisplayFeeds.py
	Note: If you change the working directory in the terminal to the "CamFeedDisplay" 
		directory, just use ./ istead of the full path. If the "CamFeedDisplay" 
		directory is included in the PATH environment variable, you can run the 
		script directly.


# Self-Healing
To allow the feeds to automatically restart, create a cron job that 
executes "DisplayFeeds.py"
	Note: The cron job should include the full path to "DisplayFeeds.py" script file.
		If the "CamFeedDisplay" directory is included in the PATH environment 
		variable, you can run the script directly.
	Example:
	The following cron job checks for dead feeds every 10 minutes and restarts them.
	*/10 * * * * /path/to/install/dir/CamFeedDisplay/DisplayFeeds.py >/path/to/install/dir/CamFeedDisplay/DisplayFeeds.log 2>&1


								***************************
								* Camera Template Layouts *
								***************************
			*** 1 Camera ***								  *** 4 Cameras ***
		   <1camTemplate.json>								<4camTemplate-2x2.json>
+-----------------------------------------+		+--------------------+--------------------+
|                                         |		|                    |                    |
|                                         |		|                    |                    |
|                                         |		|         1          |          2         |
|                                         |		|                    |                    |
|                                         |		|                    |                    |
|                    1                    |		+--------------------+--------------------+
|                                         |		|                    |                    |
|                                         |		|                    |                    |
|                                         |		|         3          |          4         |
|                                         |		|                    |                    |
|                                         |		|                    |                    |
+-----------------------------------------+		+--------------------+--------------------+

		  *** 6 Cameras - 2x3 ***					*** 6 Cameras - 1 large, 5 small ***
		  <6camTemplate-2x3.json>						 <6camTemplate-1lg5sm.json>
+-------------+-------------+-------------+		+---------------------------+-------------+
|             |             |             |		|                           |             |
|             |             |             |		|                           |      2      |
|      1      |      2      |      3      |		|                           |             |
|             |             |             |		|             1             +-------------+
|             |             |             |		|                           |             |
+-------------+-------------+-------------+		|                           |      3      |
|             |             |             |		|                           |             |
|             |             |             |		+-------------+-------------+-------------+
|      4      |      5      |      6      |		|             |             |             |
|             |             |             |		|      4      |      5      |      6      |
|             |             |             |		|             |             |             |
+-------------+-------------+-------------+		+-------------+-------------+-------------+

	*** 7 Cameras - 3 large, 4 small ***					 *** 9 Cameras ***
		 <7camTemplate-3lg4sm.json>						  <9camTemplate-3x3.json>
+--------------------+--------------------+		+-------------+-------------+-------------+
|                    |                    |		|             |             |             |
|                    |                    |		|      1      |      2      |      3      |
|         1          |          2         |		|             |             |             |
|                    |                    |		+-------------+-------------+-------------+
|                    |                    |		|             |             |             |
+--------------------+----------+---------+		|      4      |      5      |      6      |
|                    |    4     |    5    |		|             |             |             |
|                    |          |         |		+-------------+-------------+-------------+
|         3          +----------+---------+		|             |             |             |
|                    |    6     |    7    |		|      7      |      8      |      9      |
|                    |          |         |		|             |             |             |
+--------------------+----------+---------+		+-------------+-------------+-------------+

   *** 10 Cameras - 2 large, 8 small ***				  *** 12 Cameras - 3x4 ***
		<10camTemplate-2lg8sm.json>						  <12camTemplate-3x4.json>
+--------------------+----------+---------+		+----------+---------+----------+---------+
|                    |    2     |    3    |		|          |         |          |         |
|                    |          |         |		|    1     |    2    |    3     |    4    |
|         1          +----------+---------+		|          |         |          |         |
|                    |    4     |    5    |		+----------+---------+----------+---------+
|                    |          |         |		|          |         |          |         |
+--------------------+----------+---------+		|    5     |    6    |    7     |    8    |
|                    |    7     |    8    |		|          |         |          |         |
|                    |          |         |		+----------+---------+----------+---------+
|         6          +----------+---------+		|          |         |          |         |
|                    |    9     |   10    |		|    9     |    10   |    11    |    12   |
|                    |          |         |		|          |         |          |         |
+--------------------+----------+---------+		+----------+---------+----------+---------+

   *** 12 Cameras - 3 large, 9 small ***		  *** 13 Cameras - 1 large, 12 small ***
		<12camTemplate-3lg9sm.json>					   <13camTemplate-1lg12sm.json>
+--------------------+--------------------+		+--------------------+----------+---------+
|                    |                    |		|                    |    2     |    3    |
|                    |                    |		|                    |          |         |
|         1          |          2         |		+          1         +----------+---------+
|                    |                    |		|                    |    4     |    5    |
|                    |                    |		|                    |          |         |
+--------------------+------+------+------+		+----------+---------+----------+---------+
|                    |  4   |  5   |  6   |		|    6     |    7    |    8     |    9    |
|                    +------+------+------+		|          |         |          |         |
|         3          |  7   |  8   |  9   |		+----------+---------+----------+---------+
|                    +------+------+------+		|    10    |    11   |    12    |    13   |
|                    |  10  |  11  |  12  |		|          |         |          |         |
+--------------------+------+------+------+		+----------+---------+----------+---------+

* 15 Cameras - 2 large, 4 medium, 9 small *					 *** 16 Cameras ***
	  <15camTemplate-2lg4med9sm.json>					  <16camTemplate-4x4.json>
+--------------------+--------------------+		+----------+---------+----------+---------+
|                    |                    |		|    1     |    2    |    3     |    4    |
|                    |                    |		|          |         |          |         |
+          1         +          2         +		+----------+---------+----------+---------+
|                    |                    |		|    5     |    6    |    7     |    8    |
|                    |                    |		|          |         |          |         |
+----------+---------+------+------+------+		+----------+---------+----------+---------+
|    3     |    4    |  7   |  8   |  9   |		|    9     |    10   |    11    |    12   |
|          |         +------+------+------+		|          |         |          |         |
+----------+---------|  10  |  11  |  12  |		+----------+---------+----------+---------+
|    4     |    6    +------+------+------+		|    13    |    14   |    15    |    16   |
|          |         |  13  |  14  |  15  |		|          |         |          |         |
+----------+---------+------+------+------+		+----------+---------+----------+---------+


############## Directory Structure ##############
.../installDir/CameraFeedDisplay/DisplayFeeds.py
								/cameraFeeds.json
								/CamFeedTemplates/1camTemplate.json
												 /4camTemplate-2x2.json
												 /6camTemplate-1lg5sm.json
												 /6camTemplate-2x3.json
												 /7camTemplate-3lg4sm.json
												 /9camTemplate-3x3.json
												 /10camTemplate-2lg8sm.json
												 /12camTemplate-3lg9sm.json
												 /12camTemplate-3x4.json
												 /13camTemplate-1lg12sm.json
												 /15camTemplate-2lg4med9sm.json
												 /16camTemplate-4x4.json
