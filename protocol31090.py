# Copyright (c) 2015 Blizzard Entertainment
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from decoders import *


# Decoding instructions for each protocol type.
typeinfos = [
    ('_int',[(0,7)]),  #0
    ('_int',[(0,4)]),  #1
    ('_int',[(0,5)]),  #2
    ('_int',[(0,6)]),  #3
    ('_int',[(0,14)]),  #4
    ('_int',[(0,22)]),  #5
    ('_int',[(0,32)]),  #6
    ('_choice',[(0,2),{0:('m_uint6',3),1:('m_uint14',4),2:('m_uint22',5),3:('m_uint32',6)}]),  #7
    ('_struct',[[('m_userId',2,-1)]]),  #8
    ('_blob',[(0,8)]),  #9
    ('_int',[(0,8)]),  #10
    ('_struct',[[('m_flags',10,0),('m_major',10,1),('m_minor',10,2),('m_revision',10,3),('m_build',6,4),('m_baseBuild',6,5)]]),  #11
    ('_int',[(0,3)]),  #12
    ('_bool',[]),  #13
    ('_array',[(16,0),10]),  #14
    ('_optional',[14]),  #15
    ('_struct',[[('m_data',15,0)]]),  #16
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3),('m_useScaledTime',13,4),('m_ngdpRootKey',16,5),('m_dataBuildNum',6,6)]]),  #17
    ('_fourcc',[]),  #18
    ('_blob',[(0,7)]),  #19
    ('_int',[(0,64)]),  #20
    ('_struct',[[('m_region',10,0),('m_programId',18,1),('m_realm',6,2),('m_name',19,3),('m_id',20,4)]]),  #21
    ('_struct',[[('m_a',10,0),('m_r',10,1),('m_g',10,2),('m_b',10,3)]]),  #22
    ('_int',[(0,2)]),  #23
    ('_optional',[10]),  #24
    ('_struct',[[('m_name',9,0),('m_toon',21,1),('m_race',9,2),('m_color',22,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',23,7),('m_result',23,8),('m_workingSetSlotId',24,9),('m_hero',9,10)]]),  #25
    ('_array',[(0,5),25]),  #26
    ('_optional',[26]),  #27
    ('_blob',[(0,10)]),  #28
    ('_blob',[(0,11)]),  #29
    ('_struct',[[('m_file',29,0)]]),  #30
    ('_optional',[13]),  #31
    ('_int',[(-9223372036854775808,64)]),  #32
    ('_blob',[(0,12)]),  #33
    ('_blob',[(40,0)]),  #34
    ('_array',[(0,6),34]),  #35
    ('_optional',[35]),  #36
    ('_array',[(0,6),29]),  #37
    ('_optional',[37]),  #38
    ('_struct',[[('m_playerList',27,0),('m_title',28,1),('m_difficulty',9,2),('m_thumbnail',30,3),('m_isBlizzardMap',13,4),('m_restartAsTransitionMap',31,16),('m_timeUTC',32,5),('m_timeLocalOffset',32,6),('m_description',33,7),('m_imageFilePath',29,8),('m_campaignIndex',10,15),('m_mapFileName',29,9),('m_cacheHandles',36,10),('m_miniSave',13,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',38,14)]]),  #39
    ('_optional',[9]),  #40
    ('_optional',[34]),  #41
    ('_optional',[6]),  #42
    ('_struct',[[('m_race',24,-1)]]),  #43
    ('_struct',[[('m_team',24,-1)]]),  #44
    ('_blob',[(0,9)]),  #45
    ('_struct',[[('m_name',9,-18),('m_clanTag',40,-17),('m_clanLogo',41,-16),('m_highestLeague',24,-15),('m_combinedRaceLevels',42,-14),('m_randomSeed',6,-13),('m_racePreference',43,-12),('m_teamPreference',44,-11),('m_testMap',13,-10),('m_testAuto',13,-9),('m_examine',13,-8),('m_customInterface',13,-7),('m_testType',6,-6),('m_observe',23,-5),('m_hero',45,-4),('m_skin',45,-3),('m_mount',45,-2),('m_toonHandle',19,-1)]]),  #46
    ('_array',[(0,5),46]),  #47
    ('_struct',[[('m_lockTeams',13,-14),('m_teamsTogether',13,-13),('m_advancedSharedControl',13,-12),('m_randomRaces',13,-11),('m_battleNet',13,-10),('m_amm',13,-9),('m_competitive',13,-8),('m_practice',13,-7),('m_cooperative',13,-6),('m_noVictoryOrDefeat',13,-5),('m_fog',23,-4),('m_observers',23,-3),('m_userDifficulty',23,-2),('m_clientDebugFlags',20,-1)]]),  #48
    ('_int',[(1,4)]),  #49
    ('_int',[(1,8)]),  #50
    ('_bitarray',[(0,6)]),  #51
    ('_bitarray',[(0,8)]),  #52
    ('_bitarray',[(0,2)]),  #53
    ('_bitarray',[(0,7)]),  #54
    ('_struct',[[('m_allowedColors',51,-6),('m_allowedRaces',52,-5),('m_allowedDifficulty',51,-4),('m_allowedControls',52,-3),('m_allowedObserveTypes',53,-2),('m_allowedAIBuilds',54,-1)]]),  #55
    ('_array',[(0,5),55]),  #56
    ('_struct',[[('m_randomValue',6,-26),('m_gameCacheName',28,-25),('m_gameOptions',48,-24),('m_gameSpeed',12,-23),('m_gameType',12,-22),('m_maxUsers',2,-21),('m_maxObservers',2,-20),('m_maxPlayers',2,-19),('m_maxTeams',49,-18),('m_maxColors',3,-17),('m_maxRaces',50,-16),('m_maxControls',10,-15),('m_mapSizeX',10,-14),('m_mapSizeY',10,-13),('m_mapFileSyncChecksum',6,-12),('m_mapFileName',29,-11),('m_mapAuthorName',9,-10),('m_modFileSyncChecksum',6,-9),('m_slotDescriptions',56,-8),('m_defaultDifficulty',3,-7),('m_defaultAIBuild',0,-6),('m_cacheHandles',35,-5),('m_hasExtensionMod',13,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #57
    ('_optional',[1]),  #58
    ('_optional',[2]),  #59
    ('_struct',[[('m_color',59,-1)]]),  #60
    ('_array',[(0,17),6]),  #61
    ('_array',[(0,9),6]),  #62
    ('_struct',[[('m_control',10,-16),('m_userId',58,-15),('m_teamId',1,-14),('m_colorPref',60,-13),('m_racePref',43,-12),('m_difficulty',3,-11),('m_aiBuild',0,-10),('m_handicap',0,-9),('m_observe',23,-8),('m_hero',45,-7),('m_skin',45,-6),('m_mount',45,-5),('m_workingSetSlotId',24,-4),('m_rewards',61,-3),('m_toonHandle',19,-2),('m_licenses',62,-1)]]),  #63
    ('_array',[(0,5),63]),  #64
    ('_struct',[[('m_phase',12,-10),('m_maxUsers',2,-9),('m_maxObservers',2,-8),('m_slots',64,-7),('m_randomSeed',6,-6),('m_hostUserId',58,-5),('m_isSinglePlayer',13,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #65
    ('_struct',[[('m_userInitialData',47,-3),('m_gameDescription',57,-2),('m_lobbyState',65,-1)]]),  #66
    ('_struct',[[('m_syncLobbyState',66,-1)]]),  #67
    ('_struct',[[('m_name',19,-1)]]),  #68
    ('_blob',[(0,6)]),  #69
    ('_struct',[[('m_name',69,-1)]]),  #70
    ('_struct',[[('m_name',69,-3),('m_type',6,-2),('m_data',19,-1)]]),  #71
    ('_struct',[[('m_type',6,-3),('m_name',69,-2),('m_data',33,-1)]]),  #72
    ('_array',[(0,5),10]),  #73
    ('_struct',[[('m_signature',73,-2),('m_toonHandle',19,-1)]]),  #74
    ('_struct',[[('m_gameFullyDownloaded',13,-14),('m_developmentCheatsEnabled',13,-13),('m_multiplayerCheatsEnabled',13,-12),('m_syncChecksummingEnabled',13,-11),('m_isMapToMapTransition',13,-10),('m_startingRally',13,-9),('m_debugPauseEnabled',13,-8),('m_useGalaxyAsserts',13,-7),('m_platformMac',13,-6),('m_cameraFollow',13,-5),('m_baseBuildNum',6,-4),('m_buildNum',6,-3),('m_versionFlags',6,-2),('m_hotkeyProfile',45,-1)]]),  #75
    ('_struct',[[]]),  #76
    ('_int',[(0,16)]),  #77
    ('_struct',[[('x',77,-2),('y',77,-1)]]),  #78
    ('_struct',[[('m_which',12,-2),('m_target',78,-1)]]),  #79
    ('_struct',[[('m_fileName',29,-5),('m_automatic',13,-4),('m_overwrite',13,-3),('m_name',9,-2),('m_description',28,-1)]]),  #80
    ('_int',[(-2147483648,32)]),  #81
    ('_struct',[[('x',81,-2),('y',81,-1)]]),  #82
    ('_struct',[[('m_point',82,-4),('m_time',81,-3),('m_verb',28,-2),('m_arguments',28,-1)]]),  #83
    ('_struct',[[('m_data',83,-1)]]),  #84
    ('_int',[(0,21)]),  #85
    ('_struct',[[('m_abilLink',77,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',24,-1)]]),  #86
    ('_optional',[86]),  #87
    ('_null',[]),  #88
    ('_int',[(0,20)]),  #89
    ('_struct',[[('x',89,-3),('y',89,-2),('z',81,-1)]]),  #90
    ('_struct',[[('m_targetUnitFlags',77,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',77,-4),('m_snapshotControlPlayerId',58,-3),('m_snapshotUpkeepPlayerId',58,-2),('m_snapshotPoint',90,-1)]]),  #91
    ('_choice',[(0,2),{0:('None',88),1:('TargetPoint',90),2:('TargetUnit',91),3:('Data',6)}]),  #92
    ('_struct',[[('m_cmdFlags',85,-5),('m_abil',87,-4),('m_data',92,-3),('m_otherUnit',42,-2),('m_unitGroup',42,-1)]]),  #93
    ('_int',[(0,9)]),  #94
    ('_bitarray',[(0,9)]),  #95
    ('_array',[(0,9),94]),  #96
    ('_choice',[(0,2),{0:('None',88),1:('Mask',95),2:('OneIndices',96),3:('ZeroIndices',96)}]),  #97
    ('_struct',[[('m_unitLink',77,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',94,-1)]]),  #98
    ('_array',[(0,9),98]),  #99
    ('_struct',[[('m_subgroupIndex',94,-4),('m_removeMask',97,-3),('m_addSubgroups',99,-2),('m_addUnitTags',62,-1)]]),  #100
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',100,-1)]]),  #101
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',23,-2),('m_mask',97,-1)]]),  #102
    ('_struct',[[('m_count',94,-6),('m_subgroupCount',94,-5),('m_activeSubgroupIndex',94,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #103
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',103,-1)]]),  #104
    ('_array',[(0,3),81]),  #105
    ('_struct',[[('m_recipientId',1,-2),('m_resources',105,-1)]]),  #106
    ('_struct',[[('m_chatMessage',28,-1)]]),  #107
    ('_int',[(-128,8)]),  #108
    ('_struct',[[('x',81,-3),('y',81,-2),('z',81,-1)]]),  #109
    ('_struct',[[('m_beacon',108,-9),('m_ally',108,-8),('m_flags',108,-7),('m_build',108,-6),('m_targetUnitTag',6,-5),('m_targetUnitSnapshotUnitLink',77,-4),('m_targetUnitSnapshotUpkeepPlayerId',108,-3),('m_targetUnitSnapshotControlPlayerId',108,-2),('m_targetPoint',109,-1)]]),  #110
    ('_struct',[[('m_speed',12,-1)]]),  #111
    ('_struct',[[('m_delta',108,-1)]]),  #112
    ('_struct',[[('m_point',82,-4),('m_unit',6,-3),('m_pingedMinimap',13,-2),('m_option',81,-1)]]),  #113
    ('_struct',[[('m_verb',28,-2),('m_arguments',28,-1)]]),  #114
    ('_struct',[[('m_alliance',6,-2),('m_control',6,-1)]]),  #115
    ('_struct',[[('m_unitTag',6,-1)]]),  #116
    ('_struct',[[('m_unitTag',6,-2),('m_flags',10,-1)]]),  #117
    ('_struct',[[('m_conversationId',81,-2),('m_replyId',81,-1)]]),  #118
    ('_optional',[19]),  #119
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',23,-5),('m_name',9,-4),('m_toonHandle',119,-3),('m_clanTag',40,-2),('m_clanLogo',41,-1)]]),  #120
    ('_array',[(0,5),120]),  #121
    ('_int',[(0,1)]),  #122
    ('_struct',[[('m_userInfos',121,-2),('m_method',122,-1)]]),  #123
    ('_struct',[[('m_purchaseItemId',81,-1)]]),  #124
    ('_struct',[[('m_difficultyLevel',81,-1)]]),  #125
    ('_choice',[(0,3),{0:('None',88),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',81),4:('TextChanged',29),5:('MouseButton',6)}]),  #126
    ('_struct',[[('m_controlId',81,-3),('m_eventType',81,-2),('m_eventData',126,-1)]]),  #127
    ('_struct',[[('m_soundHash',6,-2),('m_length',6,-1)]]),  #128
    ('_array',[(0,7),6]),  #129
    ('_struct',[[('m_soundHash',129,-2),('m_length',129,-1)]]),  #130
    ('_struct',[[('m_syncInfo',130,-1)]]),  #131
    ('_struct',[[('m_queryId',77,-3),('m_lengthMs',6,-2),('m_finishGameLoop',6,-1)]]),  #132
    ('_struct',[[('m_queryId',77,-2),('m_lengthMs',6,-1)]]),  #133
    ('_struct',[[('m_animWaitQueryId',77,-1)]]),  #134
    ('_struct',[[('m_sound',6,-1)]]),  #135
    ('_struct',[[('m_transmissionId',81,-2),('m_thread',6,-1)]]),  #136
    ('_struct',[[('m_transmissionId',81,-1)]]),  #137
    ('_optional',[78]),  #138
    ('_optional',[77]),  #139
    ('_optional',[108]),  #140
    ('_struct',[[('m_target',138,-6),('m_distance',139,-5),('m_pitch',139,-4),('m_yaw',139,-3),('m_reason',140,-2),('m_follow',13,-1)]]),  #141
    ('_struct',[[('m_skipType',122,-1)]]),  #142
    ('_int',[(0,11)]),  #143
    ('_struct',[[('x',143,-2),('y',143,-1)]]),  #144
    ('_struct',[[('m_button',6,-5),('m_down',13,-4),('m_posUI',144,-3),('m_posWorld',90,-2),('m_flags',108,-1)]]),  #145
    ('_struct',[[('m_posUI',144,-3),('m_posWorld',90,-2),('m_flags',108,-1)]]),  #146
    ('_struct',[[('m_achievementLink',77,-1)]]),  #147
    ('_struct',[[('m_hotkey',6,-2),('m_down',13,-1)]]),  #148
    ('_struct',[[('m_abilLink',77,-3),('m_abilCmdIndex',2,-2),('m_state',108,-1)]]),  #149
    ('_struct',[[('m_soundtrack',6,-1)]]),  #150
    ('_struct',[[('m_planetId',81,-1)]]),  #151
    ('_struct',[[('m_key',108,-2),('m_flags',108,-1)]]),  #152
    ('_struct',[[('m_resources',105,-1)]]),  #153
    ('_struct',[[('m_fulfillRequestId',81,-1)]]),  #154
    ('_struct',[[('m_cancelRequestId',81,-1)]]),  #155
    ('_struct',[[('m_researchItemId',81,-1)]]),  #156
    ('_struct',[[('m_mercenaryId',81,-1)]]),  #157
    ('_struct',[[('m_battleReportId',81,-2),('m_difficultyLevel',81,-1)]]),  #158
    ('_struct',[[('m_battleReportId',81,-1)]]),  #159
    ('_int',[(0,19)]),  #160
    ('_struct',[[('m_decrementMs',160,-1)]]),  #161
    ('_struct',[[('m_portraitId',81,-1)]]),  #162
    ('_struct',[[('m_functionName',19,-1)]]),  #163
    ('_struct',[[('m_result',81,-1)]]),  #164
    ('_struct',[[('m_gameMenuItemIndex',81,-1)]]),  #165
    ('_struct',[[('m_purchaseCategoryId',81,-1)]]),  #166
    ('_struct',[[('m_button',77,-1)]]),  #167
    ('_struct',[[('m_cutsceneId',81,-2),('m_bookmarkName',19,-1)]]),  #168
    ('_struct',[[('m_cutsceneId',81,-1)]]),  #169
    ('_struct',[[('m_cutsceneId',81,-3),('m_conversationLine',19,-2),('m_altConversationLine',19,-1)]]),  #170
    ('_struct',[[('m_cutsceneId',81,-2),('m_conversationLine',19,-1)]]),  #171
    ('_struct',[[('m_observe',23,-6),('m_name',9,-5),('m_toonHandle',119,-4),('m_clanTag',40,-3),('m_clanLogo',41,-2),('m_hijack',13,-1)]]),  #172
    ('_struct',[[('m_state',23,-1)]]),  #173
    ('_struct',[[('m_managed',13,-3),('m_target',90,-2),('m_unitGroup',42,-1)]]),  #174
    ('_struct',[[('m_managed',13,-3),('m_target',91,-2),('m_unitGroup',42,-1)]]),  #175
    ('_struct',[[('m_catalog',10,-4),('m_entry',77,-3),('m_field',9,-2),('m_value',9,-1)]]),  #176
    ('_struct',[[('m_index',6,-1)]]),  #177
    ('_struct',[[('m_recipient',12,-2),('m_string',29,-1)]]),  #178
    ('_struct',[[('m_recipient',12,-2),('m_point',82,-1)]]),  #179
    ('_struct',[[('m_progress',81,-1)]]),  #180
    ('_struct',[[('m_status',23,-1)]]),  #181
    ('_struct',[[('m_scoreValueMineralsCurrent',81,0),('m_scoreValueVespeneCurrent',81,1),('m_scoreValueMineralsCollectionRate',81,2),('m_scoreValueVespeneCollectionRate',81,3),('m_scoreValueWorkersActiveCount',81,4),('m_scoreValueMineralsUsedInProgressArmy',81,5),('m_scoreValueMineralsUsedInProgressEconomy',81,6),('m_scoreValueMineralsUsedInProgressTechnology',81,7),('m_scoreValueVespeneUsedInProgressArmy',81,8),('m_scoreValueVespeneUsedInProgressEconomy',81,9),('m_scoreValueVespeneUsedInProgressTechnology',81,10),('m_scoreValueMineralsUsedCurrentArmy',81,11),('m_scoreValueMineralsUsedCurrentEconomy',81,12),('m_scoreValueMineralsUsedCurrentTechnology',81,13),('m_scoreValueVespeneUsedCurrentArmy',81,14),('m_scoreValueVespeneUsedCurrentEconomy',81,15),('m_scoreValueVespeneUsedCurrentTechnology',81,16),('m_scoreValueMineralsLostArmy',81,17),('m_scoreValueMineralsLostEconomy',81,18),('m_scoreValueMineralsLostTechnology',81,19),('m_scoreValueVespeneLostArmy',81,20),('m_scoreValueVespeneLostEconomy',81,21),('m_scoreValueVespeneLostTechnology',81,22),('m_scoreValueMineralsKilledArmy',81,23),('m_scoreValueMineralsKilledEconomy',81,24),('m_scoreValueMineralsKilledTechnology',81,25),('m_scoreValueVespeneKilledArmy',81,26),('m_scoreValueVespeneKilledEconomy',81,27),('m_scoreValueVespeneKilledTechnology',81,28),('m_scoreValueFoodUsed',81,29),('m_scoreValueFoodMade',81,30),('m_scoreValueMineralsUsedActiveForces',81,31),('m_scoreValueVespeneUsedActiveForces',81,32),('m_scoreValueMineralsFriendlyFireArmy',81,33),('m_scoreValueMineralsFriendlyFireEconomy',81,34),('m_scoreValueMineralsFriendlyFireTechnology',81,35),('m_scoreValueVespeneFriendlyFireArmy',81,36),('m_scoreValueVespeneFriendlyFireEconomy',81,37),('m_scoreValueVespeneFriendlyFireTechnology',81,38)]]),  #182
    ('_struct',[[('m_playerId',1,0),('m_stats',182,1)]]),  #183
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',28,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #184
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',58,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',42,5),('m_killerUnitTagRecycle',42,6)]]),  #185
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #186
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',28,2)]]),  #187
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',28,1),('m_count',81,2)]]),  #188
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #189
    ('_array',[(0,10),81]),  #190
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',190,1)]]),  #191
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',42,2),('m_slotId',42,3)]]),  #192
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (76, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (75, 'NNet.Game.SUserOptionsEvent'),
    9: (68, 'NNet.Game.SBankFileEvent'),
    10: (70, 'NNet.Game.SBankSectionEvent'),
    11: (71, 'NNet.Game.SBankKeyEvent'),
    12: (72, 'NNet.Game.SBankValueEvent'),
    13: (74, 'NNet.Game.SBankSignatureEvent'),
    14: (79, 'NNet.Game.SCameraSaveEvent'),
    21: (80, 'NNet.Game.SSaveGameEvent'),
    22: (76, 'NNet.Game.SSaveGameDoneEvent'),
    23: (76, 'NNet.Game.SLoadGameDoneEvent'),
    26: (84, 'NNet.Game.SGameCheatEvent'),
    27: (93, 'NNet.Game.SCmdEvent'),
    28: (101, 'NNet.Game.SSelectionDeltaEvent'),
    29: (102, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (104, 'NNet.Game.SSelectionSyncCheckEvent'),
    31: (106, 'NNet.Game.SResourceTradeEvent'),
    32: (107, 'NNet.Game.STriggerChatMessageEvent'),
    33: (110, 'NNet.Game.SAICommunicateEvent'),
    34: (111, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (112, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (113, 'NNet.Game.STriggerPingEvent'),
    37: (114, 'NNet.Game.SBroadcastCheatEvent'),
    38: (115, 'NNet.Game.SAllianceEvent'),
    39: (116, 'NNet.Game.SUnitClickEvent'),
    40: (117, 'NNet.Game.SUnitHighlightEvent'),
    41: (118, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (123, 'NNet.Game.SHijackReplayGameEvent'),
    44: (76, 'NNet.Game.STriggerSkippedEvent'),
    45: (128, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (135, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (136, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (137, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (141, 'NNet.Game.SCameraUpdateEvent'),
    50: (76, 'NNet.Game.STriggerAbortMissionEvent'),
    51: (124, 'NNet.Game.STriggerPurchaseMadeEvent'),
    52: (76, 'NNet.Game.STriggerPurchaseExitEvent'),
    53: (125, 'NNet.Game.STriggerPlanetMissionLaunchedEvent'),
    54: (76, 'NNet.Game.STriggerPlanetPanelCanceledEvent'),
    55: (127, 'NNet.Game.STriggerDialogControlEvent'),
    56: (131, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (142, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (145, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (146, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (147, 'NNet.Game.SAchievementAwardedEvent'),
    61: (148, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (149, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    63: (76, 'NNet.Game.STriggerPlanetPanelReplayEvent'),
    64: (150, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    65: (151, 'NNet.Game.STriggerPlanetMissionSelectedEvent'),
    66: (152, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (163, 'NNet.Game.STriggerMovieFunctionEvent'),
    68: (76, 'NNet.Game.STriggerPlanetPanelBirthCompleteEvent'),
    69: (76, 'NNet.Game.STriggerPlanetPanelDeathCompleteEvent'),
    70: (153, 'NNet.Game.SResourceRequestEvent'),
    71: (154, 'NNet.Game.SResourceRequestFulfillEvent'),
    72: (155, 'NNet.Game.SResourceRequestCancelEvent'),
    73: (76, 'NNet.Game.STriggerResearchPanelExitEvent'),
    74: (76, 'NNet.Game.STriggerResearchPanelPurchaseEvent'),
    75: (156, 'NNet.Game.STriggerResearchPanelSelectionChangedEvent'),
    77: (76, 'NNet.Game.STriggerMercenaryPanelExitEvent'),
    78: (76, 'NNet.Game.STriggerMercenaryPanelPurchaseEvent'),
    79: (157, 'NNet.Game.STriggerMercenaryPanelSelectionChangedEvent'),
    80: (76, 'NNet.Game.STriggerVictoryPanelExitEvent'),
    81: (76, 'NNet.Game.STriggerBattleReportPanelExitEvent'),
    82: (158, 'NNet.Game.STriggerBattleReportPanelPlayMissionEvent'),
    83: (159, 'NNet.Game.STriggerBattleReportPanelPlaySceneEvent'),
    84: (159, 'NNet.Game.STriggerBattleReportPanelSelectionChangedEvent'),
    85: (125, 'NNet.Game.STriggerVictoryPanelPlayMissionAgainEvent'),
    86: (76, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (76, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (161, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (162, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (164, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (165, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    93: (124, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseItemChangedEvent'),
    94: (166, 'NNet.Game.STriggerPurchasePanelSelectedPurchaseCategoryChangedEvent'),
    95: (167, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (76, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (168, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (169, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (170, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (171, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (76, 'NNet.Game.SGameUserLeaveEvent'),
    102: (172, 'NNet.Game.SGameUserJoinEvent'),
    103: (173, 'NNet.Game.SCommandManagerStateEvent'),
    104: (174, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (175, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (132, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (133, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (134, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (176, 'NNet.Game.SCatalogModifyEvent'),
    110: (177, 'NNet.Game.SHeroTalentSelectedEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (178, 'NNet.Game.SChatMessage'),
    1: (179, 'NNet.Game.SPingMessage'),
    2: (180, 'NNet.Game.SLoadingProgressMessage'),
    3: (76, 'NNet.Game.SServerPingMessage'),
    4: (181, 'NNet.Game.SReconnectNotifyMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    0: (183, 'NNet.Replay.Tracker.SPlayerStatsEvent'),
    1: (184, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (185, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (186, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (187, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (188, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (184, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (189, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (191, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (192, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
}

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = 2

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 7

# The typeid of NNet.Replay.SGameUserId (the type used to encode player ids).
replay_userid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 17

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 39

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 67


def _varuint32_value(value):
    # Returns the numeric value from a SVarUint32 instance.
    for k,v in value.iteritems():
        return v
    return 0


def _decode_event_stream(decoder, eventid_typeid, event_types, decode_user_id):
    # Decodes events prefixed with a gameloop and possibly userid
    gameloop = 0
    while not decoder.done():
        start_bits = decoder.used_bits()

        # decode the gameloop delta before each event
        delta = _varuint32_value(decoder.instance(svaruint32_typeid))
        gameloop += delta

        # decode the userid before each event
        if decode_user_id:
            userid = decoder.instance(replay_userid_typeid)

        # decode the event id
        eventid = decoder.instance(eventid_typeid)
        typeid, typename = event_types.get(eventid, (None, None))
        if typeid is None:
            raise CorruptedError('eventid(%d) at %s' % (eventid, decoder))

        # decode the event struct instance
        event = decoder.instance(typeid)
        event['_event'] = typename
        event['_eventid'] = eventid

        #  insert gameloop and userid
        event['_gameloop'] = gameloop
        if decode_user_id:
            event['_userid'] = userid

        # the next event is byte aligned
        decoder.byte_align()

        # insert bits used in stream
        event['_bits'] = decoder.used_bits() - start_bits

        yield event


def decode_replay_game_events(contents):
    """Decodes and yields each game event from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      game_eventid_typeid,
                                      game_event_types,
                                      decode_user_id=True):
        yield event


def decode_replay_message_events(contents):
    """Decodes and yields each message event from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      message_eventid_typeid,
                                      message_event_types,
                                      decode_user_id=True):
        yield event


def decode_replay_tracker_events(contents):
    """Decodes and yields each tracker event from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    for event in _decode_event_stream(decoder,
                                      tracker_eventid_typeid,
                                      tracker_event_types,
                                      decode_user_id=False):
        yield event


def decode_replay_header(contents):
    """Decodes and return the replay header from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    return decoder.instance(replay_header_typeid)


def decode_replay_details(contents):
    """Decodes and returns the game details from the contents byte string."""
    decoder = VersionedDecoder(contents, typeinfos)
    return decoder.instance(game_details_typeid)


def decode_replay_initdata(contents):
    """Decodes and return the replay init data from the contents byte string."""
    decoder = BitPackedDecoder(contents, typeinfos)
    return decoder.instance(replay_initdata_typeid)


def decode_replay_attributes_events(contents):
    """Decodes and yields each attribute from the contents byte string."""
    buffer = BitPackedBuffer(contents, 'little')
    attributes = {}
    if not buffer.done():
        attributes['source'] = buffer.read_bits(8)
        attributes['mapNamespace'] = buffer.read_bits(32)
        count = buffer.read_bits(32)
        attributes['scopes'] = {}
        while not buffer.done():
            value = {}
            value['namespace'] = buffer.read_bits(32)
            value['attrid'] = attrid = buffer.read_bits(32)
            scope = buffer.read_bits(8)
            value['value'] = buffer.read_aligned_bytes(4)[::-1].strip('\x00')
            if not scope in attributes['scopes']:
                attributes['scopes'][scope] = {}
            if not attrid in attributes['scopes'][scope]:
                attributes['scopes'][scope][attrid] = []
            attributes['scopes'][scope][attrid].append(value)
    return attributes


def unit_tag(unitTagIndex, unitTagRecycle):
    return (unitTagIndex << 18) + unitTagRecycle


def unit_tag_index(unitTag):
    return (unitTag >> 18) & 0x00003fff


def unit_tag_recycle(unitTag):
    return (unitTag) & 0x0003ffff
