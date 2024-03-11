from app.io.input import console_in, std_file_in, pd_file_in
from app.io.output import console_out, std_file_out


def main():
    a = console_in()
    b = std_file_in("./data/test_in.txt")
    c = pd_file_in("./data/test_in.csv")
    console_out(a)
    std_file_out("./data/test_out1.txt", a)
    console_out(b)
    std_file_out("./data/test_out2.txt", b)
    console_out(c)
    std_file_out("./data/test_out3.txt", c)


if __name__ == "__main__":
    main()
