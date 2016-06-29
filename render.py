import codecs

from bs4 import BeautifulSoup

import sarge


def load_raw():
    f = codecs.open('README.md', 'r', 'utf8')
    return f


def extract_equations(raw):
    soup = BeautifulSoup(raw, 'lxml')
    equation_tags = soup.find_all('img', class_="equation")
    equations = dict(
        (item['src'], item['data-expr'])
        for item in equation_tags
    )
    return equations


def create_svg(filename, maths):
    sarge.run("mimetex '{0}' -o -e {1}".format(maths, filename))


def main():
    f = load_raw()
    equations = extract_equations(f)
    for filename, maths in equations.items():
        create_svg(filename, maths)


if __name__ == '__main__':
    main()
