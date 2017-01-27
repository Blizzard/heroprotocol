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
    ('_blob',[(16,0)]),  #16
    ('_struct',[[('m_dataDeprecated',15,0),('m_data',16,1)]]),  #17
    ('_struct',[[('m_signature',9,0),('m_version',11,1),('m_type',12,2),('m_elapsedGameLoops',6,3),('m_useScaledTime',13,4),('m_ngdpRootKey',17,5),('m_dataBuildNum',6,6),('m_replayCompatibilityHash',17,7)]]),  #18
    ('_fourcc',[]),  #19
    ('_blob',[(0,7)]),  #20
    ('_int',[(0,64)]),  #21
    ('_struct',[[('m_region',10,0),('m_programId',19,1),('m_realm',6,2),('m_name',20,3),('m_id',21,4)]]),  #22
    ('_struct',[[('m_a',10,0),('m_r',10,1),('m_g',10,2),('m_b',10,3)]]),  #23
    ('_int',[(0,2)]),  #24
    ('_optional',[10]),  #25
    ('_struct',[[('m_name',9,0),('m_toon',22,1),('m_race',9,2),('m_color',23,3),('m_control',10,4),('m_teamId',1,5),('m_handicap',0,6),('m_observe',24,7),('m_result',24,8),('m_workingSetSlotId',25,9),('m_hero',9,10)]]),  #26
    ('_array',[(0,5),26]),  #27
    ('_optional',[27]),  #28
    ('_blob',[(0,10)]),  #29
    ('_blob',[(0,11)]),  #30
    ('_struct',[[('m_file',30,0)]]),  #31
    ('_optional',[13]),  #32
    ('_int',[(-9223372036854775808,64)]),  #33
    ('_blob',[(0,12)]),  #34
    ('_blob',[(40,0)]),  #35
    ('_array',[(0,6),35]),  #36
    ('_optional',[36]),  #37
    ('_array',[(0,6),30]),  #38
    ('_optional',[38]),  #39
    ('_struct',[[('m_playerList',28,0),('m_title',29,1),('m_difficulty',9,2),('m_thumbnail',31,3),('m_isBlizzardMap',13,4),('m_restartAsTransitionMap',32,16),('m_timeUTC',33,5),('m_timeLocalOffset',33,6),('m_description',34,7),('m_imageFilePath',30,8),('m_campaignIndex',10,15),('m_mapFileName',30,9),('m_cacheHandles',37,10),('m_miniSave',13,11),('m_gameSpeed',12,12),('m_defaultDifficulty',3,13),('m_modPaths',39,14)]]),  #40
    ('_optional',[9]),  #41
    ('_optional',[35]),  #42
    ('_optional',[6]),  #43
    ('_struct',[[('m_race',25,-1)]]),  #44
    ('_struct',[[('m_team',25,-1)]]),  #45
    ('_blob',[(0,9)]),  #46
    ('_struct',[[('m_name',9,-18),('m_clanTag',41,-17),('m_clanLogo',42,-16),('m_highestLeague',25,-15),('m_combinedRaceLevels',43,-14),('m_randomSeed',6,-13),('m_racePreference',44,-12),('m_teamPreference',45,-11),('m_testMap',13,-10),('m_testAuto',13,-9),('m_examine',13,-8),('m_customInterface',13,-7),('m_testType',6,-6),('m_observe',24,-5),('m_hero',46,-4),('m_skin',46,-3),('m_mount',46,-2),('m_toonHandle',20,-1)]]),  #47
    ('_array',[(0,5),47]),  #48
    ('_struct',[[('m_lockTeams',13,-16),('m_teamsTogether',13,-15),('m_advancedSharedControl',13,-14),('m_randomRaces',13,-13),('m_battleNet',13,-12),('m_amm',13,-11),('m_competitive',13,-10),('m_practice',13,-9),('m_cooperative',13,-8),('m_noVictoryOrDefeat',13,-7),('m_heroDuplicatesAllowed',13,-6),('m_fog',24,-5),('m_observers',24,-4),('m_userDifficulty',24,-3),('m_clientDebugFlags',21,-2),('m_ammId',43,-1)]]),  #49
    ('_int',[(1,4)]),  #50
    ('_int',[(1,8)]),  #51
    ('_bitarray',[(0,6)]),  #52
    ('_bitarray',[(0,8)]),  #53
    ('_bitarray',[(0,2)]),  #54
    ('_bitarray',[(0,7)]),  #55
    ('_struct',[[('m_allowedColors',52,-6),('m_allowedRaces',53,-5),('m_allowedDifficulty',52,-4),('m_allowedControls',53,-3),('m_allowedObserveTypes',54,-2),('m_allowedAIBuilds',55,-1)]]),  #56
    ('_array',[(0,5),56]),  #57
    ('_struct',[[('m_randomValue',6,-26),('m_gameCacheName',29,-25),('m_gameOptions',49,-24),('m_gameSpeed',12,-23),('m_gameType',12,-22),('m_maxUsers',2,-21),('m_maxObservers',2,-20),('m_maxPlayers',2,-19),('m_maxTeams',50,-18),('m_maxColors',3,-17),('m_maxRaces',51,-16),('m_maxControls',10,-15),('m_mapSizeX',10,-14),('m_mapSizeY',10,-13),('m_mapFileSyncChecksum',6,-12),('m_mapFileName',30,-11),('m_mapAuthorName',9,-10),('m_modFileSyncChecksum',6,-9),('m_slotDescriptions',57,-8),('m_defaultDifficulty',3,-7),('m_defaultAIBuild',0,-6),('m_cacheHandles',36,-5),('m_hasExtensionMod',13,-4),('m_isBlizzardMap',13,-3),('m_isPremadeFFA',13,-2),('m_isCoopMode',13,-1)]]),  #58
    ('_optional',[1]),  #59
    ('_optional',[2]),  #60
    ('_struct',[[('m_color',60,-1)]]),  #61
    ('_array',[(0,4),46]),  #62
    ('_array',[(0,17),6]),  #63
    ('_struct',[[('m_control',10,-19),('m_userId',59,-18),('m_teamId',1,-17),('m_colorPref',61,-16),('m_racePref',44,-15),('m_difficulty',3,-14),('m_aiBuild',0,-13),('m_handicap',0,-12),('m_observe',24,-11),('m_logoIndex',6,-10),('m_hero',46,-9),('m_skin',46,-8),('m_mount',46,-7),('m_artifacts',62,-6),('m_workingSetSlotId',25,-5),('m_rewards',63,-4),('m_toonHandle',20,-3),('m_tandemLeaderUserId',59,-2),('m_hasSilencePenalty',13,-1)]]),  #64
    ('_array',[(0,5),64]),  #65
    ('_struct',[[('m_phase',12,-11),('m_maxUsers',2,-10),('m_maxObservers',2,-9),('m_slots',65,-8),('m_randomSeed',6,-7),('m_hostUserId',59,-6),('m_isSinglePlayer',13,-5),('m_pickedMapTag',10,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #66
    ('_struct',[[('m_userInitialData',48,-3),('m_gameDescription',58,-2),('m_lobbyState',66,-1)]]),  #67
    ('_struct',[[('m_syncLobbyState',67,-1)]]),  #68
    ('_struct',[[('m_name',20,-1)]]),  #69
    ('_blob',[(0,6)]),  #70
    ('_struct',[[('m_name',70,-1)]]),  #71
    ('_struct',[[('m_name',70,-3),('m_type',6,-2),('m_data',20,-1)]]),  #72
    ('_struct',[[('m_type',6,-3),('m_name',70,-2),('m_data',34,-1)]]),  #73
    ('_array',[(0,5),10]),  #74
    ('_struct',[[('m_signature',74,-2),('m_toonHandle',20,-1)]]),  #75
    ('_struct',[[('m_gameFullyDownloaded',13,-14),('m_developmentCheatsEnabled',13,-13),('m_testCheatsEnabled',13,-12),('m_multiplayerCheatsEnabled',13,-11),('m_syncChecksummingEnabled',13,-10),('m_isMapToMapTransition',13,-9),('m_debugPauseEnabled',13,-8),('m_useGalaxyAsserts',13,-7),('m_platformMac',13,-6),('m_cameraFollow',13,-5),('m_baseBuildNum',6,-4),('m_buildNum',6,-3),('m_versionFlags',6,-2),('m_hotkeyProfile',46,-1)]]),  #76
    ('_struct',[[]]),  #77
    ('_int',[(0,16)]),  #78
    ('_struct',[[('x',78,-2),('y',78,-1)]]),  #79
    ('_struct',[[('m_which',12,-2),('m_target',79,-1)]]),  #80
    ('_struct',[[('m_fileName',30,-5),('m_automatic',13,-4),('m_overwrite',13,-3),('m_name',9,-2),('m_description',29,-1)]]),  #81
    ('_int',[(1,32)]),  #82
    ('_struct',[[('m_sequence',82,-1)]]),  #83
    ('_null',[]),  #84
    ('_int',[(0,20)]),  #85
    ('_int',[(-2147483648,32)]),  #86
    ('_struct',[[('x',85,-3),('y',85,-2),('z',86,-1)]]),  #87
    ('_struct',[[('m_targetUnitFlags',78,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',78,-4),('m_snapshotControlPlayerId',59,-3),('m_snapshotUpkeepPlayerId',59,-2),('m_snapshotPoint',87,-1)]]),  #88
    ('_choice',[(0,2),{0:('None',84),1:('TargetPoint',87),2:('TargetUnit',88)}]),  #89
    ('_struct',[[('m_target',89,-4),('m_time',86,-3),('m_verb',29,-2),('m_arguments',29,-1)]]),  #90
    ('_struct',[[('m_data',90,-1)]]),  #91
    ('_int',[(0,25)]),  #92
    ('_struct',[[('m_abilLink',78,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',25,-1)]]),  #93
    ('_optional',[93]),  #94
    ('_choice',[(0,2),{0:('None',84),1:('TargetPoint',87),2:('TargetUnit',88),3:('Data',6)}]),  #95
    ('_optional',[87]),  #96
    ('_struct',[[('m_cmdFlags',92,-7),('m_abil',94,-6),('m_data',95,-5),('m_vector',96,-4),('m_sequence',82,-3),('m_otherUnit',43,-2),('m_unitGroup',43,-1)]]),  #97
    ('_int',[(0,9)]),  #98
    ('_bitarray',[(0,9)]),  #99
    ('_array',[(0,9),98]),  #100
    ('_choice',[(0,2),{0:('None',84),1:('Mask',99),2:('OneIndices',100),3:('ZeroIndices',100)}]),  #101
    ('_struct',[[('m_unitLink',78,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',98,-1)]]),  #102
    ('_array',[(0,9),102]),  #103
    ('_array',[(0,9),6]),  #104
    ('_struct',[[('m_subgroupIndex',98,-4),('m_removeMask',101,-3),('m_addSubgroups',103,-2),('m_addUnitTags',104,-1)]]),  #105
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',105,-1)]]),  #106
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',12,-2),('m_mask',101,-1)]]),  #107
    ('_struct',[[('m_count',98,-6),('m_subgroupCount',98,-5),('m_activeSubgroupIndex',98,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #108
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',108,-1)]]),  #109
    ('_struct',[[('m_chatMessage',29,-1)]]),  #110
    ('_struct',[[('m_speed',12,-1)]]),  #111
    ('_int',[(-128,8)]),  #112
    ('_struct',[[('m_delta',112,-1)]]),  #113
    ('_struct',[[('x',86,-2),('y',86,-1)]]),  #114
    ('_struct',[[('m_point',114,-4),('m_unit',6,-3),('m_pingedMinimap',13,-2),('m_option',86,-1)]]),  #115
    ('_struct',[[('m_verb',29,-2),('m_arguments',29,-1)]]),  #116
    ('_struct',[[('m_alliance',6,-2),('m_control',6,-1)]]),  #117
    ('_struct',[[('m_unitTag',6,-1)]]),  #118
    ('_struct',[[('m_unitTag',6,-2),('m_flags',10,-1)]]),  #119
    ('_struct',[[('m_conversationId',86,-2),('m_replyId',86,-1)]]),  #120
    ('_optional',[20]),  #121
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',24,-5),('m_name',9,-4),('m_toonHandle',121,-3),('m_clanTag',41,-2),('m_clanLogo',42,-1)]]),  #122
    ('_array',[(0,5),122]),  #123
    ('_int',[(0,1)]),  #124
    ('_struct',[[('m_userInfos',123,-2),('m_method',124,-1)]]),  #125
    ('_choice',[(0,3),{0:('None',84),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',86),4:('TextChanged',30),5:('MouseButton',6)}]),  #126
    ('_struct',[[('m_controlId',86,-3),('m_eventType',86,-2),('m_eventData',126,-1)]]),  #127
    ('_struct',[[('m_soundHash',6,-2),('m_length',6,-1)]]),  #128
    ('_array',[(0,7),6]),  #129
    ('_struct',[[('m_soundHash',129,-2),('m_length',129,-1)]]),  #130
    ('_struct',[[('m_syncInfo',130,-1)]]),  #131
    ('_struct',[[('m_queryId',78,-3),('m_lengthMs',6,-2),('m_finishGameLoop',6,-1)]]),  #132
    ('_struct',[[('m_queryId',78,-2),('m_lengthMs',6,-1)]]),  #133
    ('_struct',[[('m_animWaitQueryId',78,-1)]]),  #134
    ('_struct',[[('m_sound',6,-1)]]),  #135
    ('_struct',[[('m_transmissionId',86,-2),('m_thread',6,-1)]]),  #136
    ('_struct',[[('m_transmissionId',86,-1)]]),  #137
    ('_optional',[79]),  #138
    ('_optional',[78]),  #139
    ('_optional',[112]),  #140
    ('_struct',[[('m_target',138,-6),('m_distance',139,-5),('m_pitch',139,-4),('m_yaw',139,-3),('m_reason',140,-2),('m_follow',13,-1)]]),  #141
    ('_struct',[[('m_skipType',124,-1)]]),  #142
    ('_int',[(0,11)]),  #143
    ('_struct',[[('x',143,-2),('y',143,-1)]]),  #144
    ('_struct',[[('m_button',6,-5),('m_down',13,-4),('m_posUI',144,-3),('m_posWorld',87,-2),('m_flags',112,-1)]]),  #145
    ('_struct',[[('m_posUI',144,-3),('m_posWorld',87,-2),('m_flags',112,-1)]]),  #146
    ('_struct',[[('m_achievementLink',78,-1)]]),  #147
    ('_struct',[[('m_hotkey',6,-2),('m_down',13,-1)]]),  #148
    ('_struct',[[('m_abilLink',78,-3),('m_abilCmdIndex',2,-2),('m_state',112,-1)]]),  #149
    ('_struct',[[('m_soundtrack',6,-1)]]),  #150
    ('_struct',[[('m_key',112,-2),('m_flags',112,-1)]]),  #151
    ('_struct',[[('m_error',86,-2),('m_abil',94,-1)]]),  #152
    ('_int',[(0,19)]),  #153
    ('_struct',[[('m_decrementMs',153,-1)]]),  #154
    ('_struct',[[('m_portraitId',86,-1)]]),  #155
    ('_struct',[[('m_functionName',20,-1)]]),  #156
    ('_struct',[[('m_result',86,-1)]]),  #157
    ('_struct',[[('m_gameMenuItemIndex',86,-1)]]),  #158
    ('_int',[(-32768,16)]),  #159
    ('_struct',[[('m_wheelSpin',159,-2),('m_flags',112,-1)]]),  #160
    ('_struct',[[('m_button',78,-1)]]),  #161
    ('_struct',[[('m_cutsceneId',86,-2),('m_bookmarkName',20,-1)]]),  #162
    ('_struct',[[('m_cutsceneId',86,-1)]]),  #163
    ('_struct',[[('m_cutsceneId',86,-3),('m_conversationLine',20,-2),('m_altConversationLine',20,-1)]]),  #164
    ('_struct',[[('m_cutsceneId',86,-2),('m_conversationLine',20,-1)]]),  #165
    ('_struct',[[('m_leaveReason',1,-1)]]),  #166
    ('_struct',[[('m_observe',24,-7),('m_name',9,-6),('m_toonHandle',121,-5),('m_clanTag',41,-4),('m_clanLogo',42,-3),('m_hijack',13,-2),('m_hijackCloneGameUserId',59,-1)]]),  #167
    ('_optional',[82]),  #168
    ('_struct',[[('m_state',24,-2),('m_sequence',168,-1)]]),  #169
    ('_struct',[[('m_sequence',168,-2),('m_target',87,-1)]]),  #170
    ('_struct',[[('m_sequence',168,-2),('m_target',88,-1)]]),  #171
    ('_struct',[[('m_catalog',10,-4),('m_entry',78,-3),('m_field',9,-2),('m_value',9,-1)]]),  #172
    ('_struct',[[('m_index',6,-1)]]),  #173
    ('_struct',[[('m_shown',13,-1)]]),  #174
    ('_struct',[[('m_recipient',12,-2),('m_string',30,-1)]]),  #175
    ('_struct',[[('m_recipient',12,-2),('m_point',114,-1)]]),  #176
    ('_struct',[[('m_progress',86,-1)]]),  #177
    ('_struct',[[('m_status',24,-1)]]),  #178
    ('_struct',[[('m_abilLink',78,-3),('m_abilCmdIndex',2,-2),('m_buttonLink',78,-1)]]),  #179
    ('_struct',[[('m_behaviorLink',78,-2),('m_buttonLink',78,-1)]]),  #180
    ('_choice',[(0,2),{0:('None',84),1:('Ability',179),2:('Behavior',180),3:('Vitals',159)}]),  #181
    ('_struct',[[('m_announcement',181,-4),('m_announceLink',78,-3),('m_otherUnitTag',6,-2),('m_unitTag',6,-1)]]),  #182
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #183
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_x',10,2),('m_y',10,3)]]),  #184
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',59,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',43,5),('m_killerUnitTagRecycle',43,6)]]),  #185
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #186
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2)]]),  #187
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',29,1),('m_count',86,2)]]),  #188
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #189
    ('_array',[(0,10),86]),  #190
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',190,1)]]),  #191
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',43,2),('m_slotId',43,3)]]),  #192
    ('_struct',[[('m_key',29,0)]]),  #193
    ('_struct',[[('__parent',193,0),('m_value',29,1)]]),  #194
    ('_array',[(0,6),194]),  #195
    ('_optional',[195]),  #196
    ('_struct',[[('__parent',193,0),('m_value',86,1)]]),  #197
    ('_array',[(0,6),197]),  #198
    ('_optional',[198]),  #199
    ('_struct',[[('m_eventName',29,0),('m_stringData',196,1),('m_intData',199,2),('m_fixedData',199,3)]]),  #200
    ('_struct',[[('m_value',6,0),('m_time',6,1)]]),  #201
    ('_array',[(0,6),201]),  #202
    ('_array',[(0,5),202]),  #203
    ('_struct',[[('m_name',29,0),('m_values',203,1)]]),  #204
    ('_array',[(0,21),204]),  #205
    ('_struct',[[('m_instanceList',205,0)]]),  #206
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (77, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (76, 'NNet.Game.SUserOptionsEvent'),
    9: (69, 'NNet.Game.SBankFileEvent'),
    10: (71, 'NNet.Game.SBankSectionEvent'),
    11: (72, 'NNet.Game.SBankKeyEvent'),
    12: (73, 'NNet.Game.SBankValueEvent'),
    13: (75, 'NNet.Game.SBankSignatureEvent'),
    14: (80, 'NNet.Game.SCameraSaveEvent'),
    21: (81, 'NNet.Game.SSaveGameEvent'),
    22: (77, 'NNet.Game.SSaveGameDoneEvent'),
    23: (77, 'NNet.Game.SLoadGameDoneEvent'),
    25: (83, 'NNet.Game.SCommandManagerResetEvent'),
    26: (91, 'NNet.Game.SGameCheatEvent'),
    27: (97, 'NNet.Game.SCmdEvent'),
    28: (106, 'NNet.Game.SSelectionDeltaEvent'),
    29: (107, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (109, 'NNet.Game.SSelectionSyncCheckEvent'),
    32: (110, 'NNet.Game.STriggerChatMessageEvent'),
    34: (111, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (113, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (115, 'NNet.Game.STriggerPingEvent'),
    37: (116, 'NNet.Game.SBroadcastCheatEvent'),
    38: (117, 'NNet.Game.SAllianceEvent'),
    39: (118, 'NNet.Game.SUnitClickEvent'),
    40: (119, 'NNet.Game.SUnitHighlightEvent'),
    41: (120, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (125, 'NNet.Game.SHijackReplayGameEvent'),
    44: (77, 'NNet.Game.STriggerSkippedEvent'),
    45: (128, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (135, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (136, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (137, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (141, 'NNet.Game.SCameraUpdateEvent'),
    50: (77, 'NNet.Game.STriggerAbortMissionEvent'),
    55: (127, 'NNet.Game.STriggerDialogControlEvent'),
    56: (131, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (142, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (145, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (146, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (147, 'NNet.Game.SAchievementAwardedEvent'),
    61: (148, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (149, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    64: (150, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    66: (151, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (156, 'NNet.Game.STriggerMovieFunctionEvent'),
    76: (152, 'NNet.Game.STriggerCommandErrorEvent'),
    86: (77, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (77, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (154, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (155, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (157, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (158, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (160, 'NNet.Game.STriggerMouseWheelEvent'),
    95: (161, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (77, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (162, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (163, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (164, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (165, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (166, 'NNet.Game.SGameUserLeaveEvent'),
    102: (167, 'NNet.Game.SGameUserJoinEvent'),
    103: (169, 'NNet.Game.SCommandManagerStateEvent'),
    104: (170, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (171, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (132, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (133, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (134, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (172, 'NNet.Game.SCatalogModifyEvent'),
    110: (173, 'NNet.Game.SHeroTalentTreeSelectedEvent'),
    111: (77, 'NNet.Game.STriggerProfilerLoggingFinishedEvent'),
    112: (174, 'NNet.Game.SHeroTalentTreeSelectionPanelToggledEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (175, 'NNet.Game.SChatMessage'),
    1: (176, 'NNet.Game.SPingMessage'),
    2: (177, 'NNet.Game.SLoadingProgressMessage'),
    3: (77, 'NNet.Game.SServerPingMessage'),
    4: (178, 'NNet.Game.SReconnectNotifyMessage'),
    5: (182, 'NNet.Game.SPlayerAnnounceMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    1: (183, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (185, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (186, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (187, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (188, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (183, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (189, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (191, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (192, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
    10: (200, 'NNet.Replay.Tracker.SStatGameEvent'),
    11: (206, 'NNet.Replay.Tracker.SScoreResultEvent'),
    12: (184, 'NNet.Replay.Tracker.SUnitRevivedEvent'),
}

# The typeid of the NNet.Replay.Tracker.EEventId enum.
tracker_eventid_typeid = 2

# The typeid of NNet.SVarUint32 (the type used to encode gameloop deltas).
svaruint32_typeid = 7

# The typeid of NNet.Replay.SGameUserId (the type used to encode player ids).
replay_userid_typeid = 8

# The typeid of NNet.Replay.SHeader (the type used to store replay game version and length).
replay_header_typeid = 18

# The typeid of NNet.Game.SDetails (the type used to store overall replay details).
game_details_typeid = 40

# The typeid of NNet.Replay.SInitData (the type used to store the inital lobby).
replay_initdata_typeid = 68


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
