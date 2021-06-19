# heroprotocol

heroprotocol is a [Python](https://www.python.org/downloads/) library and command-line tool to decode Heroes of the Storm replay files into Python data structures.

The tool is available as a [PyPI Package](https://pypi.org/project/heroprotocol/) or as source code.

Currently heroprotocol can decode these structures and events:

* Replay header
* Game details
* Replay init data
* Game events
* Message events
* Tracker events

heroprotocol can be used as a base-build-specific library to decode binary blobs, or it can be run as a standalone tool
to pretty print information from supported replay files.

Note that heroprotocol does not expose game balance information or provide any kind of high level analysis of replays;
it's meant to be just the first tool in the chain for your data mining application.

## Supported Versions

heroprotocol supports all Hereos of the Storm replay files that were played with retail and PTR versions of the game.

## Requirements

* Python 2.7 or 3.x
  * Note: A future release may remove support for Python 2.7
* Python Packages:
  * mpyq 0.2.5+
  * six 1.14.0+

## Installation

Either install/update using pip:

```bash
python -m pip install --upgrade heroprotocol
```

Or clone the repository and run from source:

```bash
git clone https://github.com/Blizzard/heroprotocol.git
python -m pip install -r ./heroprotocol/heroprotocol/requirements.txt
```

## Command Line Arguments

```plain
-h, --help          Show the options that are available.

Tracker Events:
--gameevents        Print all game events including coordinates
--messageevents     Print message events such as ping events
--trackerevents     Print tracker events such as units killed, game stat events,
                    score result event
--attributeevents   Print attribute events, a table of attrid, namespace, and attribute values
--header            Print protocol header including build id and elapsedGameLoops
--details           Print protocol details, e.g. teamId, player names and chosen heroes,
                    player region, game result, observer status
--initdata          Print protocol initdata, e.g. interface settings for every player

Output Options:
--stats             Output stats about the active tracker event to the STDERR stream
--json              Use JSON syntax for output
```

## Example Usage

If you want the output shown directly in the terminal, leave out the `> output.txt`.

```bash
python -m heroprotocol --details "Blackheart's Bay.StormReplay" > output.txt
```

By default, data is output as a Python dictionary object. To output a JSON file, add `--json`.

**Note**, however, that the JSON file is formatted as a sequence/stream of JSON objects and
will likely not parse as regular JSON.

## Tracker Events

Some notes on tracker events:

* Convert unit tag index, recycle pairs into unit tags (as seen in game events) with protocol.unit_tag (index, recycle)
* Interpret the NNet.Replay.Tracker.SUnitPositionsEvent events like this:

```python
unitIndex = event['m_firstUnitIndex']
for i in range(0, len(event['m_items']), 3):
    unitIndex += event['m_items'][i + 0]
    x = event['m_items'][i + 1] * 4
    y = event['m_items'][i + 2] * 4
    # unit identified by unitIndex at the current event['_gameloop'] time
    # is at approximate position (x, y)
```

* Only units that have inflicted or taken damage are mentioned in unit position events, and they occur periodically with a limit of 256 units mentioned per event.
* NNet.Replay.Tracker.SUnitInitEvent events appear for units under construction. When complete you'll see a NNet.Replay.Tracker.SUnitDoneEvent with the same unit tag.
* NNet.Replay.Tracker.SUnitBornEvent events appear for units that are created fully constructed.
* You may receive a NNet.Replay.Tracker.SUnitDiedEvent after either a UnitInit or UnitBorn event for the corresponding unit tag.
* In NNet.Replay.Tracker.SPlayerStatsEvent, m_scoreValueFoodUsed and m_scoreValueFoodMade are in fixed point (divide by 4096 for integer values). All other values are in integers.
* There's a known issue where revived units are not tracked, and placeholder units track death but not birth.

## Reporting Bugs

Please report bugs at the [Heroes of the Storm Bug Report Forum](https://us.forums.blizzard.com/en/heroes/c/bug-report).

## Acknowledgements

The standalone tool uses [mpyq](https://github.com/eagleflo/mpyq) by
[Aku Kotkavuo](https://github.com/eagleflo) to read mopaq files.

Thank you to [healingbrew](https://github.com/healingbrew), [MGatner](https://github.com/mgatner),
[koliva8245](https://github.com/koliva8245), [casualMLG](https://github.com/casualmlg), and others for submitting issues
and feedback.

Thank you to [Christian Clauss](https://github.com/cclauss), [Jingbei Li](https://github.com/petronny), and
[Regner Blok-Andersen](https://github.com/regner) for contributions to the Python 3 update.

Thank you to David Joerg and Graylin Kim of [GGTracker](http://www.ggtracker.com) for design feedback and beta-testing of
the s2protocol library that heroprotocol is based upon.

Thanks to Ben Barrett of [HOTSLogs](http://www.hotslogs.com) for early feedback on and beta-testing of the heroprotocol
library.

## License

Copyright 2021 Blizzard Entertainment

Source code for this project is released to the public under the MIT license.
See the included [LICENSE](LICENSE) file for more information.
