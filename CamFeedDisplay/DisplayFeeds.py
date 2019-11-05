#!/usr/bin/env python2

import json
import time
import subprocess

CAM_DATA = './cameraFeeds.json'

def display_feeds():
	'''Reads a JSON file and starts any camera feeds that aren't already started'''
	# Open JSON file
	print 'Reading JSON file...'
	with open(CAM_DATA) as feeds_json:
		feeds = json.load(feeds_json)['feeds']
	
	#Retrieve the names of open screen sessions
	open_screen_sessions = get_open_screen_sessions()
	
	# Start each feed, if needed
	print 'Starting feeds...'
	for feed in feeds:
		# If the feed doesn't exist yet (based on the session existing), start it
		if feed['feed-name'] not in open_screen_sessions:
			start_feed(
				feed['feed-name'],
				feed['display-name'],
				feed['rtsp-uri'],
				feed['width'],
				feed['height'],
				feed['x-position'],
				feed['y-position']
			)
	print 'All feeds running.'

def get_open_screen_sessions():
	'''Returns the names of all currently open screen sessions'''
	print 'Checking for open screens...'
	screen_names = []
	for screen in subprocess.check_output('ls /var/run/screen/S-*/',shell=True).split('\n'):
		if len(screen) > 0:
			screen_names.append(screen.split('.')[-1])
	return screen_names
	
def start_feed(feed_name, display_name, rtsp_uri, width, height, x_position, y_position):
	'''
	Opens a new screen session and starts the RTSP
	stream with ffplay in the given size and location
	'''
	print 'Starting ' + display_name + ' feed...'
	ffplay_cmd = 'screen -dmS {} sh -c \'ffplay -noborder -hide_banner -exitonmousedown -an -ss 10 -window_title "{}" -i {} -x {} -y {} -left {} -top {}\''.format(feed_name, display_name, rtsp_uri, width, height, x_position, y_position)
	subprocess.call(ffplay_cmd,shell=True)
	print 'Feed running...'
	time.sleep(5)


def main():
	display_feeds()
	
if __name__ == '__main__':
	main()

