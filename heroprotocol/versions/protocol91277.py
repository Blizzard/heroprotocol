#!/usr/bin/env python
#
# Copyright 2015-2021 Blizzard Entertainment. Subject to the MIT license.
# See the included LICENSE file for more information.
#

import six

from heroprotocol.decoders import CorruptedError, BitPackedBuffer, BitPackedDecoder, VersionedDecoder


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
    ('_struct',[[('m_name',9,-20),('m_clanTag',41,-19),('m_clanLogo',42,-18),('m_highestLeague',25,-17),('m_combinedRaceLevels',43,-16),('m_randomSeed',6,-15),('m_racePreference',44,-14),('m_teamPreference',45,-13),('m_testMap',13,-12),('m_testAuto',13,-11),('m_examine',13,-10),('m_customInterface',13,-9),('m_testType',6,-8),('m_observe',24,-7),('m_hero',46,-6),('m_skin',46,-5),('m_mount',46,-4),('m_banner',46,-3),('m_spray',46,-2),('m_toonHandle',20,-1)]]),  #47
    ('_array',[(0,5),47]),  #48
    ('_struct',[[('m_lockTeams',13,-16),('m_teamsTogether',13,-15),('m_advancedSharedControl',13,-14),('m_randomRaces',13,-13),('m_battleNet',13,-12),('m_amm',13,-11),('m_competitive',13,-10),('m_practice',13,-9),('m_cooperative',13,-8),('m_noVictoryOrDefeat',13,-7),('m_heroDuplicatesAllowed',13,-6),('m_fog',24,-5),('m_observers',24,-4),('m_userDifficulty',24,-3),('m_clientDebugFlags',21,-2),('m_ammId',43,-1)]]),  #49
    ('_int',[(1,4)]),  #50
    ('_int',[(1,8)]),  #51
    ('_bitarray',[(0,6)]),  #52
    ('_bitarray',[(0,8)]),  #53
    ('_bitarray',[(0,4)]),  #54
    ('_bitarray',[(0,2)]),  #55
    ('_bitarray',[(0,7)]),  #56
    ('_struct',[[('m_allowedColors',52,-6),('m_allowedRaces',53,-5),('m_allowedDifficulty',52,-4),('m_allowedControls',54,-3),('m_allowedObserveTypes',55,-2),('m_allowedAIBuilds',56,-1)]]),  #57
    ('_array',[(0,5),57]),  #58
    ('_array',[(0,10),19]),  #59
    ('_struct',[[('m_randomValue',6,-28),('m_gameCacheName',29,-27),('m_gameOptions',49,-26),('m_gameSpeed',12,-25),('m_gameType',12,-24),('m_maxUsers',2,-23),('m_maxObservers',2,-22),('m_maxPlayers',2,-21),('m_maxTeams',50,-20),('m_maxColors',3,-19),('m_maxRaces',51,-18),('m_maxControls',1,-17),('m_mapSizeX',10,-16),('m_mapSizeY',10,-15),('m_mapFileSyncChecksum',6,-14),('m_mapFileName',30,-13),('m_mapAuthorName',9,-12),('m_modFileSyncChecksum',6,-11),('m_slotDescriptions',58,-10),('m_defaultDifficulty',3,-9),('m_defaultAIBuild',0,-8),('m_cacheHandles',36,-7),('m_hasExtensionMod',13,-6),('m_isBlizzardMap',13,-5),('m_isPremadeFFA',13,-4),('m_isCoopMode',13,-3),('m_isRandomTestValue',13,-2),('m_disabledHeroList',59,-1)]]),  #60
    ('_optional',[1]),  #61
    ('_optional',[2]),  #62
    ('_struct',[[('m_color',62,-1)]]),  #63
    ('_array',[(0,17),6]),  #64
    ('_struct',[[('m_hero',19,-2),('m_tier',10,-1)]]),  #65
    ('_array',[(0,10),65]),  #66
    ('_struct',[[('m_control',10,-26),('m_userId',61,-25),('m_teamId',1,-24),('m_colorPref',63,-23),('m_racePref',44,-22),('m_difficulty',3,-21),('m_aiBuild',0,-20),('m_handicap',0,-19),('m_observe',24,-18),('m_logoIndex',6,-17),('m_hero',46,-16),('m_skin',46,-15),('m_mount',46,-14),('m_workingSetSlotId',25,-13),('m_rewards',64,-12),('m_toonHandle',20,-11),('m_tandemLeaderUserId',61,-10),('m_hasSilencePenalty',13,-9),('m_hasVoiceSilencePenalty',13,-8),('m_isBlizzardStaff',13,-7),('m_hasActiveBoost',13,-6),('m_banner',46,-5),('m_spray',46,-4),('m_announcerPack',46,-3),('m_voiceLine',46,-2),('m_heroMasteryTiers',66,-1)]]),  #67
    ('_array',[(0,5),67]),  #68
    ('_struct',[[('m_phase',12,-11),('m_maxUsers',2,-10),('m_maxObservers',2,-9),('m_slots',68,-8),('m_randomSeed',6,-7),('m_hostUserId',61,-6),('m_isSinglePlayer',13,-5),('m_pickedMapTag',10,-4),('m_gameDuration',6,-3),('m_defaultDifficulty',3,-2),('m_defaultAIBuild',0,-1)]]),  #69
    ('_struct',[[('m_userInitialData',48,-3),('m_gameDescription',60,-2),('m_lobbyState',69,-1)]]),  #70
    ('_struct',[[('m_syncLobbyState',70,-1)]]),  #71
    ('_struct',[[('m_name',20,-1)]]),  #72
    ('_blob',[(0,6)]),  #73
    ('_struct',[[('m_name',73,-1)]]),  #74
    ('_struct',[[('m_name',73,-3),('m_type',6,-2),('m_data',20,-1)]]),  #75
    ('_struct',[[('m_type',6,-3),('m_name',73,-2),('m_data',34,-1)]]),  #76
    ('_array',[(0,5),10]),  #77
    ('_struct',[[('m_signature',77,-2),('m_toonHandle',20,-1)]]),  #78
    ('_struct',[[('m_gameFullyDownloaded',13,-14),('m_developmentCheatsEnabled',13,-13),('m_testCheatsEnabled',13,-12),('m_multiplayerCheatsEnabled',13,-11),('m_syncChecksummingEnabled',13,-10),('m_isMapToMapTransition',13,-9),('m_debugPauseEnabled',13,-8),('m_useGalaxyAsserts',13,-7),('m_platformMac',13,-6),('m_cameraFollow',13,-5),('m_baseBuildNum',6,-4),('m_buildNum',6,-3),('m_versionFlags',6,-2),('m_hotkeyProfile',46,-1)]]),  #79
    ('_struct',[[]]),  #80
    ('_int',[(0,16)]),  #81
    ('_struct',[[('x',81,-2),('y',81,-1)]]),  #82
    ('_struct',[[('m_which',12,-2),('m_target',82,-1)]]),  #83
    ('_struct',[[('m_fileName',30,-5),('m_automatic',13,-4),('m_overwrite',13,-3),('m_name',9,-2),('m_description',29,-1)]]),  #84
    ('_int',[(1,32)]),  #85
    ('_struct',[[('m_sequence',85,-1)]]),  #86
    ('_null',[]),  #87
    ('_int',[(0,20)]),  #88
    ('_int',[(-2147483648,32)]),  #89
    ('_struct',[[('x',88,-3),('y',88,-2),('z',89,-1)]]),  #90
    ('_struct',[[('m_targetUnitFlags',81,-7),('m_timer',10,-6),('m_tag',6,-5),('m_snapshotUnitLink',81,-4),('m_snapshotControlPlayerId',61,-3),('m_snapshotUpkeepPlayerId',61,-2),('m_snapshotPoint',90,-1)]]),  #91
    ('_choice',[(0,2),{0:('None',87),1:('TargetPoint',90),2:('TargetUnit',91)}]),  #92
    ('_struct',[[('m_target',92,-4),('m_time',89,-3),('m_verb',29,-2),('m_arguments',29,-1)]]),  #93
    ('_struct',[[('m_data',93,-1)]]),  #94
    ('_int',[(0,26)]),  #95
    ('_struct',[[('m_abilLink',81,-3),('m_abilCmdIndex',2,-2),('m_abilCmdData',25,-1)]]),  #96
    ('_optional',[96]),  #97
    ('_choice',[(0,2),{0:('None',87),1:('TargetPoint',90),2:('TargetUnit',91),3:('Data',6)}]),  #98
    ('_optional',[90]),  #99
    ('_struct',[[('m_cmdFlags',95,-7),('m_abil',97,-6),('m_data',98,-5),('m_vector',99,-4),('m_sequence',85,-3),('m_otherUnit',43,-2),('m_unitGroup',43,-1)]]),  #100
    ('_array',[(0,6),2]),  #101
    ('_choice',[(0,2),{0:('None',87),1:('Mask',52),2:('OneIndices',101),3:('ZeroIndices',101)}]),  #102
    ('_struct',[[('m_unitLink',81,-4),('m_subgroupPriority',10,-3),('m_intraSubgroupPriority',10,-2),('m_count',3,-1)]]),  #103
    ('_array',[(0,6),103]),  #104
    ('_array',[(0,6),6]),  #105
    ('_struct',[[('m_subgroupIndex',2,-4),('m_removeMask',102,-3),('m_addSubgroups',104,-2),('m_addUnitTags',105,-1)]]),  #106
    ('_struct',[[('m_controlGroupId',1,-2),('m_delta',106,-1)]]),  #107
    ('_struct',[[('m_controlGroupIndex',1,-3),('m_controlGroupUpdate',12,-2),('m_mask',102,-1)]]),  #108
    ('_struct',[[('m_count',3,-6),('m_subgroupCount',3,-5),('m_activeSubgroupIndex',2,-4),('m_unitTagsChecksum',6,-3),('m_subgroupIndicesChecksum',6,-2),('m_subgroupsChecksum',6,-1)]]),  #109
    ('_struct',[[('m_controlGroupId',1,-2),('m_selectionSyncData',109,-1)]]),  #110
    ('_struct',[[('m_chatMessage',29,-1)]]),  #111
    ('_struct',[[('m_unitTag',6,-3),('m_buttonSlotA',10,-2),('m_buttonSlotB',10,-1)]]),  #112
    ('_struct',[[('m_speed',12,-1)]]),  #113
    ('_int',[(-128,8)]),  #114
    ('_struct',[[('m_delta',114,-1)]]),  #115
    ('_struct',[[('x',89,-2),('y',89,-1)]]),  #116
    ('_struct',[[('m_point',116,-4),('m_unit',6,-3),('m_pingedMinimap',13,-2),('m_option',89,-1)]]),  #117
    ('_struct',[[('m_verb',29,-2),('m_arguments',29,-1)]]),  #118
    ('_struct',[[('m_alliance',6,-2),('m_control',6,-1)]]),  #119
    ('_struct',[[('m_unitTag',6,-1)]]),  #120
    ('_struct',[[('m_unitTag',6,-2),('m_flags',10,-1)]]),  #121
    ('_struct',[[('m_conversationId',89,-2),('m_replyId',89,-1)]]),  #122
    ('_optional',[20]),  #123
    ('_struct',[[('m_gameUserId',1,-6),('m_observe',24,-5),('m_name',9,-4),('m_toonHandle',123,-3),('m_clanTag',41,-2),('m_clanLogo',42,-1)]]),  #124
    ('_array',[(0,5),124]),  #125
    ('_int',[(0,1)]),  #126
    ('_struct',[[('m_userInfos',125,-2),('m_method',126,-1)]]),  #127
    ('_struct',[[('m_button',81,-2),('m_metaKeyFlags',81,-1)]]),  #128
    ('_choice',[(0,3),{0:('None',87),1:('Checked',13),2:('ValueChanged',6),3:('SelectionChanged',89),4:('TextChanged',30),5:('MouseEvent',128)}]),  #129
    ('_struct',[[('m_controlId',89,-3),('m_eventType',89,-2),('m_eventData',129,-1)]]),  #130
    ('_struct',[[('m_soundHash',6,-2),('m_length',6,-1)]]),  #131
    ('_array',[(0,7),6]),  #132
    ('_struct',[[('m_soundHash',132,-2),('m_length',132,-1)]]),  #133
    ('_struct',[[('m_syncInfo',133,-1)]]),  #134
    ('_struct',[[('m_queryId',81,-3),('m_lengthMs',6,-2),('m_finishGameLoop',6,-1)]]),  #135
    ('_struct',[[('m_queryId',81,-2),('m_lengthMs',6,-1)]]),  #136
    ('_struct',[[('m_animWaitQueryId',81,-1)]]),  #137
    ('_struct',[[('m_sound',6,-1)]]),  #138
    ('_struct',[[('m_transmissionId',89,-2),('m_thread',6,-1)]]),  #139
    ('_struct',[[('m_transmissionId',89,-1)]]),  #140
    ('_optional',[82]),  #141
    ('_optional',[81]),  #142
    ('_optional',[114]),  #143
    ('_struct',[[('m_target',141,-6),('m_distance',142,-5),('m_pitch',142,-4),('m_yaw',142,-3),('m_reason',143,-2),('m_follow',13,-1)]]),  #144
    ('_struct',[[('m_skipType',126,-1)]]),  #145
    ('_int',[(0,11)]),  #146
    ('_struct',[[('x',146,-2),('y',146,-1)]]),  #147
    ('_struct',[[('m_button',6,-5),('m_down',13,-4),('m_posUI',147,-3),('m_posWorld',90,-2),('m_flags',114,-1)]]),  #148
    ('_struct',[[('m_posUI',147,-3),('m_posWorld',90,-2),('m_flags',114,-1)]]),  #149
    ('_struct',[[('m_achievementLink',81,-1)]]),  #150
    ('_struct',[[('m_hotkey',6,-2),('m_down',13,-1)]]),  #151
    ('_struct',[[('m_abilLink',81,-3),('m_abilCmdIndex',2,-2),('m_state',114,-1)]]),  #152
    ('_struct',[[('m_soundtrack',6,-1)]]),  #153
    ('_struct',[[('m_key',114,-2),('m_flags',114,-1)]]),  #154
    ('_struct',[[('m_error',89,-2),('m_abil',97,-1)]]),  #155
    ('_int',[(0,19)]),  #156
    ('_struct',[[('m_decrementMs',156,-1)]]),  #157
    ('_struct',[[('m_portraitId',89,-1)]]),  #158
    ('_struct',[[('m_functionName',20,-1)]]),  #159
    ('_struct',[[('m_result',89,-1)]]),  #160
    ('_struct',[[('m_gameMenuItemIndex',89,-1)]]),  #161
    ('_int',[(-32768,16)]),  #162
    ('_struct',[[('m_wheelSpin',162,-2),('m_flags',114,-1)]]),  #163
    ('_struct',[[('m_button',81,-1)]]),  #164
    ('_struct',[[('m_cutsceneId',89,-2),('m_bookmarkName',20,-1)]]),  #165
    ('_struct',[[('m_cutsceneId',89,-1)]]),  #166
    ('_struct',[[('m_cutsceneId',89,-3),('m_conversationLine',20,-2),('m_altConversationLine',20,-1)]]),  #167
    ('_struct',[[('m_cutsceneId',89,-2),('m_conversationLine',20,-1)]]),  #168
    ('_struct',[[('m_leaveReason',2,-1)]]),  #169
    ('_struct',[[('m_observe',24,-7),('m_name',9,-6),('m_toonHandle',123,-5),('m_clanTag',41,-4),('m_clanLogo',42,-3),('m_hijack',13,-2),('m_hijackCloneGameUserId',61,-1)]]),  #170
    ('_optional',[85]),  #171
    ('_struct',[[('m_state',24,-2),('m_sequence',171,-1)]]),  #172
    ('_struct',[[('m_sequence',171,-2),('m_target',90,-1)]]),  #173
    ('_struct',[[('m_sequence',171,-2),('m_target',91,-1)]]),  #174
    ('_struct',[[('m_catalog',10,-4),('m_entry',81,-3),('m_field',9,-2),('m_value',9,-1)]]),  #175
    ('_struct',[[('m_index',6,-1)]]),  #176
    ('_struct',[[('m_shown',13,-1)]]),  #177
    ('_struct',[[('m_recipient',12,-2),('m_string',30,-1)]]),  #178
    ('_struct',[[('m_recipient',12,-2),('m_point',116,-1)]]),  #179
    ('_struct',[[('m_progress',89,-1)]]),  #180
    ('_struct',[[('m_status',24,-1)]]),  #181
    ('_struct',[[('m_abilLink',81,-3),('m_abilCmdIndex',2,-2),('m_buttonLink',81,-1)]]),  #182
    ('_struct',[[('m_behaviorLink',81,-2),('m_buttonLink',81,-1)]]),  #183
    ('_choice',[(0,2),{0:('None',87),1:('Ability',182),2:('Behavior',183),3:('Vitals',162)}]),  #184
    ('_struct',[[('m_announcement',184,-4),('m_announceLink',81,-3),('m_otherUnitTag',6,-2),('m_unitTag',6,-1)]]),  #185
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2),('m_controlPlayerId',1,3),('m_upkeepPlayerId',1,4),('m_x',10,5),('m_y',10,6)]]),  #186
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_x',10,2),('m_y',10,3)]]),  #187
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_killerPlayerId',61,2),('m_x',10,3),('m_y',10,4),('m_killerUnitTagIndex',43,5),('m_killerUnitTagRecycle',43,6)]]),  #188
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_controlPlayerId',1,2),('m_upkeepPlayerId',1,3)]]),  #189
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1),('m_unitTypeName',29,2)]]),  #190
    ('_struct',[[('m_playerId',1,0),('m_upgradeTypeName',29,1),('m_count',89,2)]]),  #191
    ('_struct',[[('m_unitTagIndex',6,0),('m_unitTagRecycle',6,1)]]),  #192
    ('_array',[(0,10),89]),  #193
    ('_struct',[[('m_firstUnitIndex',6,0),('m_items',193,1)]]),  #194
    ('_struct',[[('m_playerId',1,0),('m_type',6,1),('m_userId',43,2),('m_slotId',43,3)]]),  #195
    ('_struct',[[('m_key',29,0)]]),  #196
    ('_struct',[[('__parent',196,0),('m_value',29,1)]]),  #197
    ('_array',[(0,6),197]),  #198
    ('_optional',[198]),  #199
    ('_struct',[[('__parent',196,0),('m_value',89,1)]]),  #200
    ('_array',[(0,6),200]),  #201
    ('_optional',[201]),  #202
    ('_struct',[[('m_eventName',29,0),('m_stringData',199,1),('m_intData',202,2),('m_fixedData',202,3)]]),  #203
    ('_struct',[[('m_value',6,0),('m_time',6,1)]]),  #204
    ('_array',[(0,6),204]),  #205
    ('_array',[(0,5),205]),  #206
    ('_struct',[[('m_name',29,0),('m_values',206,1)]]),  #207
    ('_array',[(0,21),207]),  #208
    ('_struct',[[('m_instanceList',208,0)]]),  #209
    ('_struct',[[('m_hero',29,0),('m_controllingTeam',6,1)]]),  #210
    ('_struct',[[('m_hero',29,0),('m_controllingPlayer',6,1)]]),  #211
    ('_struct',[[('m_hero',29,0),('m_newControllingPlayer',6,1)]]),  #212
]

# Map from protocol NNet.Game.*Event eventid to (typeid, name)
game_event_types = {
    5: (80, 'NNet.Game.SUserFinishedLoadingSyncEvent'),
    7: (79, 'NNet.Game.SUserOptionsEvent'),
    9: (72, 'NNet.Game.SBankFileEvent'),
    10: (74, 'NNet.Game.SBankSectionEvent'),
    11: (75, 'NNet.Game.SBankKeyEvent'),
    12: (76, 'NNet.Game.SBankValueEvent'),
    13: (78, 'NNet.Game.SBankSignatureEvent'),
    14: (83, 'NNet.Game.SCameraSaveEvent'),
    21: (84, 'NNet.Game.SSaveGameEvent'),
    22: (80, 'NNet.Game.SSaveGameDoneEvent'),
    23: (80, 'NNet.Game.SLoadGameDoneEvent'),
    25: (86, 'NNet.Game.SCommandManagerResetEvent'),
    26: (94, 'NNet.Game.SGameCheatEvent'),
    27: (100, 'NNet.Game.SCmdEvent'),
    28: (107, 'NNet.Game.SSelectionDeltaEvent'),
    29: (108, 'NNet.Game.SControlGroupUpdateEvent'),
    30: (110, 'NNet.Game.SSelectionSyncCheckEvent'),
    32: (111, 'NNet.Game.STriggerChatMessageEvent'),
    33: (112, 'NNet.Game.SDynamicButtonSwapEvent'),
    34: (113, 'NNet.Game.SSetAbsoluteGameSpeedEvent'),
    35: (115, 'NNet.Game.SAddAbsoluteGameSpeedEvent'),
    36: (117, 'NNet.Game.STriggerPingEvent'),
    37: (118, 'NNet.Game.SBroadcastCheatEvent'),
    38: (119, 'NNet.Game.SAllianceEvent'),
    39: (120, 'NNet.Game.SUnitClickEvent'),
    40: (121, 'NNet.Game.SUnitHighlightEvent'),
    41: (122, 'NNet.Game.STriggerReplySelectedEvent'),
    43: (127, 'NNet.Game.SHijackReplayGameEvent'),
    44: (80, 'NNet.Game.STriggerSkippedEvent'),
    45: (131, 'NNet.Game.STriggerSoundLengthQueryEvent'),
    46: (138, 'NNet.Game.STriggerSoundOffsetEvent'),
    47: (139, 'NNet.Game.STriggerTransmissionOffsetEvent'),
    48: (140, 'NNet.Game.STriggerTransmissionCompleteEvent'),
    49: (144, 'NNet.Game.SCameraUpdateEvent'),
    50: (80, 'NNet.Game.STriggerAbortMissionEvent'),
    55: (130, 'NNet.Game.STriggerDialogControlEvent'),
    56: (134, 'NNet.Game.STriggerSoundLengthSyncEvent'),
    57: (145, 'NNet.Game.STriggerConversationSkippedEvent'),
    58: (148, 'NNet.Game.STriggerMouseClickedEvent'),
    59: (149, 'NNet.Game.STriggerMouseMovedEvent'),
    60: (150, 'NNet.Game.SAchievementAwardedEvent'),
    61: (151, 'NNet.Game.STriggerHotkeyPressedEvent'),
    62: (152, 'NNet.Game.STriggerTargetModeUpdateEvent'),
    64: (153, 'NNet.Game.STriggerSoundtrackDoneEvent'),
    66: (154, 'NNet.Game.STriggerKeyPressedEvent'),
    67: (159, 'NNet.Game.STriggerMovieFunctionEvent'),
    76: (155, 'NNet.Game.STriggerCommandErrorEvent'),
    86: (80, 'NNet.Game.STriggerMovieStartedEvent'),
    87: (80, 'NNet.Game.STriggerMovieFinishedEvent'),
    88: (157, 'NNet.Game.SDecrementGameTimeRemainingEvent'),
    89: (158, 'NNet.Game.STriggerPortraitLoadedEvent'),
    90: (160, 'NNet.Game.STriggerCustomDialogDismissedEvent'),
    91: (161, 'NNet.Game.STriggerGameMenuItemSelectedEvent'),
    92: (163, 'NNet.Game.STriggerMouseWheelEvent'),
    95: (164, 'NNet.Game.STriggerButtonPressedEvent'),
    96: (80, 'NNet.Game.STriggerGameCreditsFinishedEvent'),
    97: (165, 'NNet.Game.STriggerCutsceneBookmarkFiredEvent'),
    98: (166, 'NNet.Game.STriggerCutsceneEndSceneFiredEvent'),
    99: (167, 'NNet.Game.STriggerCutsceneConversationLineEvent'),
    100: (168, 'NNet.Game.STriggerCutsceneConversationLineMissingEvent'),
    101: (169, 'NNet.Game.SGameUserLeaveEvent'),
    102: (170, 'NNet.Game.SGameUserJoinEvent'),
    103: (172, 'NNet.Game.SCommandManagerStateEvent'),
    104: (173, 'NNet.Game.SCmdUpdateTargetPointEvent'),
    105: (174, 'NNet.Game.SCmdUpdateTargetUnitEvent'),
    106: (135, 'NNet.Game.STriggerAnimLengthQueryByNameEvent'),
    107: (136, 'NNet.Game.STriggerAnimLengthQueryByPropsEvent'),
    108: (137, 'NNet.Game.STriggerAnimOffsetEvent'),
    109: (175, 'NNet.Game.SCatalogModifyEvent'),
    110: (176, 'NNet.Game.SHeroTalentTreeSelectedEvent'),
    111: (80, 'NNet.Game.STriggerProfilerLoggingFinishedEvent'),
    112: (177, 'NNet.Game.SHeroTalentTreeSelectionPanelToggledEvent'),
}

# The typeid of the NNet.Game.EEventId enum.
game_eventid_typeid = 0

# Map from protocol NNet.Game.*Message eventid to (typeid, name)
message_event_types = {
    0: (178, 'NNet.Game.SChatMessage'),
    1: (179, 'NNet.Game.SPingMessage'),
    2: (180, 'NNet.Game.SLoadingProgressMessage'),
    3: (80, 'NNet.Game.SServerPingMessage'),
    4: (181, 'NNet.Game.SReconnectNotifyMessage'),
    5: (185, 'NNet.Game.SPlayerAnnounceMessage'),
}

# The typeid of the NNet.Game.EMessageId enum.
message_eventid_typeid = 1

# Map from protocol NNet.Replay.Tracker.*Event eventid to (typeid, name)
tracker_event_types = {
    1: (186, 'NNet.Replay.Tracker.SUnitBornEvent'),
    2: (188, 'NNet.Replay.Tracker.SUnitDiedEvent'),
    3: (189, 'NNet.Replay.Tracker.SUnitOwnerChangeEvent'),
    4: (190, 'NNet.Replay.Tracker.SUnitTypeChangeEvent'),
    5: (191, 'NNet.Replay.Tracker.SUpgradeEvent'),
    6: (186, 'NNet.Replay.Tracker.SUnitInitEvent'),
    7: (192, 'NNet.Replay.Tracker.SUnitDoneEvent'),
    8: (194, 'NNet.Replay.Tracker.SUnitPositionsEvent'),
    9: (195, 'NNet.Replay.Tracker.SPlayerSetupEvent'),
    10: (203, 'NNet.Replay.Tracker.SStatGameEvent'),
    11: (209, 'NNet.Replay.Tracker.SScoreResultEvent'),
    12: (187, 'NNet.Replay.Tracker.SUnitRevivedEvent'),
    13: (210, 'NNet.Replay.Tracker.SHeroBannedEvent'),
    14: (211, 'NNet.Replay.Tracker.SHeroPickedEvent'),
    15: (212, 'NNet.Replay.Tracker.SHeroSwappedEvent'),
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

# The typeid of NNet.Replay.SInitData (the type used to store the initial lobby).
replay_initdata_typeid = 71


def _varuint32_value(value):
    # Returns the numeric value from a SVarUint32 instance.
    for v in six.itervalues(value):
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
        _ = buffer.read_bits(32)
        attributes['scopes'] = {}
        while not buffer.done():
            value = {}
            value['namespace'] = buffer.read_bits(32)
            value['attrid'] = attrid = buffer.read_bits(32)
            scope = buffer.read_bits(8)
            value['value'] = buffer.read_aligned_bytes(4)[::-1].strip(b'\x00')
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
