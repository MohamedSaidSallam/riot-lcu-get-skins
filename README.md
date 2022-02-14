# League of Legends: Get and Search Skins

[![License][license-image]][license-url]

A powershell script that uses Riot LCU API to exports the owned skins and skins in loot to a file. Along with a python script to search for a skin in multiple files so you can get your skins and your friends' skins and search for common skins for a five man same skin line team.

> Raising Awareness: If you are sending this script for a friend to run, Please inform them that they shouldn't run scripts without making sure they are safe. and even if a friend sent it to them they should confirm that "that friend" is actually their friend talking to them.

## Installation

Make sure you have [Python](https://www.python.org/) installed.

## Usage

### getSkins.ps1

> Please make sure the League of legends client is open for the script to work.

Open power shell and paste the content of the [getSkins.ps1](getSkins.ps1) (or run the script if you have that option enabled on your system).

Two files should have been written in the same place the powershell terminal is open (the path written before cursor): ``skins.json`` and ``skinsLoot.json``.

Either send them to your friend who's collecting all the skins files or put them in the ``players`` folder to search the content of the files.

### searchByText.py

Place all the skins files in the ``players`` folder. If you are searching files from multiple people rename them accordingly (keep the ``.json`` and ``.loot.json`` part).

Open a terminal in the same folder as ``searchByText.py``. then run

```bash
py searchByText.py Infernal
```

Replace "Infernal" with any search word.

#### Example Output

```bash
$ py searchByText.py infernal
PLAYER 1
        Infernal Akali
PLAYER 2
         None :(
PLAYER 3
        Infernal Galio
        Infernal Shen (loot)
PLAYER 4
         None :(
PLAYER 5
        Infernal Nasus
        Infernal Mordekaiser
PLAYER 6
        Infernal Mordekaiser
PLAYER 7
        Infernal Alistar
PLAYER 8
         None :(
PLAYER 9
        Infernal Akali
PLAYER 10
        Infernal Amumu
        Infernal Akali
        Infernal Varus
```

#### Example Help

```text
$ py searchByText.py -h
usage: searchByText.py [-h] [--players-folder [PLAYERS_FOLDER ...]] searchString [searchString ...]

Searches the skins json files in the players folder for a given string

positional arguments:
  searchString          the string to search for in the skins json (using .contains())

options:
  -h, --help            show this help message and exit
  --players-folder [PLAYERS_FOLDER ...]
                        the folder that contains the skins json files
```

## Tools Used

* [Visual Studio Code](https://code.visualstudio.com/)
* [LCU API documentation](http://www.mingweisamuel.com/lcu-schema/tool/#//)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

[license-image]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[license-url]: https://opensource.org/licenses/MIT
