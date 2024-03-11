import unittest
import os

import pandas as pd

from app.io.input import std_file_in, pd_file_in


class StdFileInTest(unittest.TestCase):

    def test_empty(self):
        if "test_std_file_in_empty.txt" in os.listdir():
            os.remove("test_std_file_in_empty.txt")
        open("test_std_file_in_empty.txt", mode="w").close()
        text = std_file_in("test_std_file_in_empty.txt")
        self.assertEqual(text, "", msg="Read some info while reading empty file")
        if "test_std_file_in_empty.txt" in os.listdir():
            os.remove("test_std_file_in_empty.txt")

    def test_default(self):
        if "test_std_file_in_default.txt" in os.listdir():
            os.remove("test_std_file_in_default.txt")
        with open("test_std_file_in_default.txt", mode="w") as f:
            f.write("Hello World!")
        text = std_file_in("test_std_file_in_default.txt")
        self.assertEqual(text, "Hello World!", msg="Read wrong info while reading file")
        if "test_std_file_in_default.txt" in os.listdir():
            os.remove("test_std_file_in_default.txt")

    def test_all_ascii(self):
        if "test_std_file_in_all_ascii.txt" in os.listdir():
            os.remove("test_std_file_in_all_ascii.txt")
        with open("test_std_file_in_all_ascii.txt", mode="w") as f:
            f.write("".join([chr(i) for i in range(32, 127)]))
        text = std_file_in("test_std_file_in_all_ascii.txt")
        self.assertEqual(text, "".join([chr(i) for i in range(32, 127)]), msg="Could not read all ascii characters")
        if "test_std_file_in_all_ascii.txt" in os.listdir():
            os.remove("test_std_file_in_all_ascii.txt")


class PdFileInTest(unittest.TestCase):

    def test_one_line(self):
        if "test_pd_file_in_one_line.txt" in os.listdir():
            os.remove("test_pd_file_in_one_line.csv")
        with open("test_pd_file_in_one_line.csv", mode="w") as f:
            f.write("Hello,World")
        text = pd_file_in("test_pd_file_in_one_line.csv")
        pd.testing.assert_frame_equal(text, pd.DataFrame(columns=["Hello", "World"]))
        if "test_pd_file_in_one_line.csv" in os.listdir():
            os.remove("test_pd_file_in_one_line.csv")

    def test_multiple_line(self):
        if "test_pd_file_in_default.csv" in os.listdir():
            os.remove("test_pd_file_in_default.csv")
        with open("test_pd_file_in_default.csv", mode="w") as f:
            f.write("x,y\n1,1\n2,4\n3,9\n4,16")
        text = pd_file_in("test_pd_file_in_default.csv")
        pd.testing.assert_frame_equal(text, pd.DataFrame([(1, 1), (2, 4), (3, 9), (4, 16)], columns=["x", "y"]))
        if "test_pd_file_in_default.csv" in os.listdir():
            os.remove("test_pd_file_in_default.csv")

    def test_all_ascii(self):
        if "test_pd_file_in_all_ascii.csv" in os.listdir():
            os.remove("test_pd_file_in_all_ascii.csv")
        with open("test_pd_file_in_all_ascii.csv", mode="w") as f:
            f.write("".join([chr(i) for i in range(32, 127)]))
        text = pd_file_in("test_pd_file_in_all_ascii.csv")
        pd.testing.assert_frame_equal(text, pd.DataFrame(columns="".join([chr(i) for i in range(32, 127)]).split(",")))
        if "test_pd_file_in_all_ascii.csv" in os.listdir():
            os.remove("test_pd_file_in_all_ascii.csv")


if __name__ == "__main__":
    unittest.main()
