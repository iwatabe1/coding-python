"""
ハッシュ関数：
文字列を入力すると、ハッシュ化した文字列(または数値)を返却する関数。
要件：
1.出力するデータ長が変わらない。
2.入力が同じなら出力されるハッシュ値は同じになる。
3.異なる入力であっても出力されるハッシュ値が同じになる可能性がある。(衝突)
4.ハッシュ値から元の文字列を逆引きで出力することはできない。

ハッシュ化に使用されるアルゴリズム：
SHA-2が代表的。MD-5やSHA-1には脆弱性がある。

ただし、ハッシュテーブルに利用するものは単純化して捉えて良い。
文字列→数値

ハッシュテーブル：
ハッシュ関数を通して得られた数値の配列の位置に対応する文字列を格納する。

例えば、みかん → ハッシュ関数 → 4の場合。
配列の4番目にみかんと対応する値(値段など)を格納する。
みかんを検索すると、ハッシュ関数で4が返却されるので、プログラムは配列の4番目を確認する。
配列の4番目から、みかんと値(値段など)を取得できる。
配列例：{"":"","","","","","みかん":"100"}
線形の検索や２分探索などが不要になる。
時間計算量: O(1)

pythonでは、dictonary型として定義されている。
dict = {}
"""
