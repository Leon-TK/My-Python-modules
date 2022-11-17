WIN_PATH_MAX_LEN = 3000
WIN_FILE_MAX_LEN = 220
WIN_PATH_DELIMITER = '\\'

WIN_EXCLUDE_CHARS1 = [chr(1), chr(2), chr(3), chr(4), chr(5), chr(6), chr(8),chr(9),chr(10),chr(11),chr(12),chr(13),
    chr(14),chr(15),chr(16),chr(17),chr(18),chr(19),chr(20),chr(21),
    chr(22),chr(23),chr(24),chr(25),chr(26),chr(27),chr(28),chr(29),chr(30),chr(31)]
WIN_EXCLUDE_CHARS2 = "< > : \" \\ | / ? * 0".split()
WIN_EXCLUDE_CHARS2_B = "< > \" \\ | / ? * 0".split() #exception for disk:\ case
WIN_EXCLUDE_STRINGS = "CON PRN AUX NUL COM1 COM2 COM3 COM4 COM5 COM6 COM7 COM8 COM9 LPT1 LPT2 LPT3 LPT4 LPT5 LPT6 LPT7 LPT8 LPT9".split()

DOT = "."
D_DOT = ".."