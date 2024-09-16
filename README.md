# coding-python

### create virtual environment:
* Create viratual env
    * `python -m venv .env`
        * or `python3 -m venv .env`
    * `source .env/bin/activate`

* install python libraries of list in requirements.txt.
    * `pip install -r requirements.txt`

* (If needed)automatic generate requirements.
    * `pip freeze > requirements.txt`

# Data types
Type check way is `type("string") is str` as `type("<value>" is <type>)`.

* String
    * 説明
        * 文字、文字列。
    * 宣言
        * `s = "string"`
* int
    * 説明
        * 整数、小数点を含まない。値は無限
    * 宣言
        * `i = 123`
* float
    * 説明
        * 浮動小数点、小数点を含む数値
    * 宣言
        * `s = 1.5`
    * 無限大 Infinity
        * `float("inf")`
* bool
    * 説明
        * 真偽値。True / False (先頭は大文字)
    * 宣言
        * `positive = True`
        * `negative = False`
        * b = bool()

list
tuple
set
and others
