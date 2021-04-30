# Maist NLP

Natural Language Processing module for Yonsei MAIST  
Support List
- Korean

## Environment
```
python 3.8 ~
```

## Install
```
pip -U git+https://git@github.com/Yonsei-Maist/maist-nlp
```

## Use
```
# lib
## data manager


# ko
## use HanJaMo
from ko.character.spelling import HanJaMo

han = HanJaMo()
res = han.divide("반갑습니다.")  # ㅂㅏㄴㄱㅏㅂㅅㅡㅂㄴㅣㄷㅏ.
res = han.union(res)  # 반갑습니다.
```

## Author
```
Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05.~
```

## Maintainer
```
Chanwoo Gwon, arknell@yonsei.ac.kr (2021.04)
```