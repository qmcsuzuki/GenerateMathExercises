# 概要
ジョルダン標準形 J を指定すると、ジョルダン標準形が J になるランダムな問題が帰ってきます。

# 使い方
```
J = [[-1,0,0],[0,2,1],[0,0,2]]
make_problem_Jordan_normal_form(J)
```

## 隠し変数
make_problem_Jordan_normal_form(J, need_info=True, need_ans=True)

情報、解答がいらない場合はオフにできる
