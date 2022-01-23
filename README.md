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

Before installing the program below, install [python](https://www.python.org/downloads/) first. Then download script [main.py](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/main/main.py) and install [chromium] for windows

```bash
pip install -r requirements.txt
```

## Settings

1. Change the [Username](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/ef985856dd180f45fb79c0d840463341b33efacd/colab.py#L145) with your NIM.
2. Change the [Password](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/ef985856dd180f45fb79c0d840463341b33efacd/colab.py#L146) with your PIC.
3. Change the course data [here](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/ef985856dd180f45fb79c0d840463341b33efacd/colab.py#L23-L80).
4. Change chromium storage address [here](https://github.com/mnovel/BOT-ABSENSI-UMM/blob/e98ea2b928aff18ec9046929f9cfb221f904252d/main.py#L104)

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
