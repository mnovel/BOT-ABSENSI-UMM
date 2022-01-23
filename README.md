# AUTO ABSENSI UMM DENGAN MENGGUNAKAN PYTHON

This program is a bot used for attendance on the website https://lms.umm.ac.id and https://infokhs.umm.ac.id. Bot will automatically attendance when it has entered lecture hours.

## Installation Kali Linux

Before installing the program below, install [python3](https://www.python.org/downloads/) first, and install [chromium](https://sites.google.com/chromium.org/driver/) for kali linux

```bash
$ git clone https://github.com/mnovel/BOT-ABSENSI-UMM
$ cd mnovel/BOT-ABSENSI-UMM
$ pip install -r requirements.txt
$ telegram-send --configure
```

## Installation Windows

Before installing the program below, install [python](https://www.python.org/downloads/) first. Then download script [main.py](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/main/main.py) and install [chromium](https://sites.google.com/chromium.org/driver/) for windows

```bash
pip install -r requirements.txt
telegram-send --configure
```

## Settings

1. Change the [Username](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/140259994a7d966101312ba58767f49ce3c2718a/main.py#L161) with your NIM.
2. Change the [Password](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/140259994a7d966101312ba58767f49ce3c2718a/main.py#L162) with your PIC.
3. Change the course data [here](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/140259994a7d966101312ba58767f49ce3c2718a/main.py#L25-L82).
4. Change chromium storage address [here](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/140259994a7d966101312ba58767f49ce3c2718a/main.py#L111)

## Usage In Kali Linux

```bash
$ python3 main.py
```

## Usage In Windows

```bash
$ python main.py
```

## Usage In Google Colab

1. Copy script [colab.py](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/main/colab.py)
2. Paste in [Google Colab](https://colab.research.google.com/)
3. Run

## License

[MIT](https://choosealicense.com/licenses/mit/)
