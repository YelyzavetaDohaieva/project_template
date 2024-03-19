import app.io.input as inp
import app.io.output as out


def main():
    inputs = [inp.console_input(),
              inp.file_input('input.txt'),
              inp.pandas_input('Iris.csv')]
    for i in inputs:
        out.console_output(i)
        out.file_output(i)


if __name__ == "__main__":
    main()
