@echo off
setlocal

rem Whoah this site rules: http://www.dostips.com/DtTutoFunctions.php
rem for debug

if "%2" == "" goto:ShowUsage

echo Replay File: %~n1

rem I assume that Python 2.7.1. is in your PATH environment variable.

set _path_to_heroprotocol=..\heroprotocol.py
set _out_directory=%2
set _out_target_directory_name="%2\%~n1"

if not exist %_path_to_heroprotocol% (
	echo I can not find your hero protocol at %_path_to_heroprotocol%.
	endlocal
	exit /B -1
)

set _target_game_events="%_out_directory%\%~n1\game_events.json"
call:Touch %_target_game_events%
set _target_message_events="%_out_directory%\%~n1\message_events.json"
call:Touch %_target_message_events%
set _target_tracker_events="%_out_directory%\%~n1\tracker_events.json"
call:Touch %_target_tracker_events%
set _target_attribute_events="%_out_directory%\%~n1\attribute_events.json"
call:Touch %_target_attribute_events%
set _target_header="%_out_directory%\%~n1\header.json"
call:Touch %_target_header%
set _target_details="%_out_directory%\%~n1\details.json"
call:Touch %_target_details%
set _target_init_data="%_out_directory%\%~n1\init_data.json"
call:Touch %_target_init_data%
set _target_stats="%_out_directory%\%~n1\stats.json"
call:Touch %_target_stats%

call:EnsureDirectoryExists %_out_directory%
call:EnsureDirectoryExists %_out_target_directory_name%

if NOT EXIST %1 (
	echo REPLAY DOES NOT EXIST.
	endlocal
	exit /B -2
)

echo Decoding Game Events. This takes a moment.
py %_path_to_heroprotocol% %1 --gameevents --json > %_target_game_events%

echo Decoding Message Events.
py %_path_to_heroprotocol% %1 --messageevents --json > %_target_message_events%

echo Decoding Tracker Events. Give it a sec.
py %_path_to_heroprotocol% %1 --trackerevents --json > %_target_tracker_events%

echo Decoding Attribute Events.
py %_path_to_heroprotocol% %1 --attributeevents --json > %_target_attribute_events%

echo Decoding Header.
py %_path_to_heroprotocol% %1 --header --json > %_target_header%

echo Decoding Details.
py %_path_to_heroprotocol% %1 --details --json > %_target_details%

echo Decoding Init Data.
py %_path_to_heroprotocol% %1 --initdata --json > %_target_init_data%

echo Decoding Stats.
py %_path_to_heroprotocol% %1 --stats --json > %_target_stats%

echo DumpAllData has finished successfully.
endlocal
exit /B 0

:Touch 
	echo Touching %1.
	echo $null >> %1
goto:eof

:EnsureDirectoryExists 
	if not exist %1 (
		mkdir %1
	)
goto:eof

:ShowUsage
	echo use:
	echo 	DumpAllData.cmd 'path-to-replay' 'folder-to-output-to'
	echo.
	echo.
	echo details:
	echo 	-- 'folder-to-output-to' will be created if it does not exist.
goto:eof