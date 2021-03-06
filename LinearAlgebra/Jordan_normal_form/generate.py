import numpy as np

""" How to use?
example 1:
# J = [[-1,0,0],[0,2,1],[0,0,2]]
# make_problem_Jordan_normal_form(J)

example2:
J = [[-1,0,0,0],[0,2,1,0],[0,0,2,1],[0,0,0,2]]
make_problem_Jordan_normal_form(J,difficulty=8)
"""


"""
テキトーな n*n ユニモジュラ行列を１つ得る
（単位行列に対して、行or列変形をランダムに繰り返すというアルゴリズム）
difficulty: ユニモジュラ行列の「複雑度」（基本変形の最大回数）
"""
def random_unimodular(n,difficulty):
    from random import randint, sample
    if difficulty==None: difficulty = n*3
    A = np.eye(n,n)
    for _ in range(difficulty):
        # j-th のベクトルを c 倍して i-th に足す
        i,j = sample(range(n), 2)  
        c, = sample([-2,-1,1,2], 1)

        if randint(0,1)==0: #行基本変形
            A[i] += c*A[j]
        else: #列基本変形
            A[:, i:i+1] += c*A[:, j:j+1] 
    
    #unimodularを確認
    assert abs(np.linalg.det(A) - 1) < 1e-5
    return np.matrix(A)


"""
np.matrix形式の行列 A を
整数成分のリスト形式に変換
"""
def mat2intlist(A):
    return np.round(A).astype(int).tolist()


"""
行列 P,Q,J(ジョルダン標準形),A の情報を
texのコメント形式で出力
"""
def show_info(P,Q,J,A):
    print("情報")
    x = "P^{-1}"
    print(f"% P={mat2intlist(P)}")
    print(f"% Q={x}={mat2intlist(Q)}")
    print(f"% J={J}")
    print(f"% A = PJQ = {mat2intlist(A)}")
    print()

"""
問題をtexとして出力
"""
def show_problem(A):
    print("問題")
    print(f"${mat2tex(A)}$\nのジョルダン標準形を求めよ。\n")

"""
解答をtexとして出力
"""
def show_ans(P,Q,J,A):
    print("答え")
    print(f"\\[\n{mat2tex(Q)}{mat2tex(A)}{mat2tex(P)}={mat2tex(J)}\\]\n")



"""
行列 A をtex形式に変換した文字列を返す
"""
def mat2tex(A):
    res = "\\begin{pmatrix}\n"
    for line in mat2intlist(A):
        res += " & ".join(map(str,line)) + " \\\\\n"
    res += "\\end{pmatrix}\n"
    return res


"""
ジョルダン標準形が J になるような行列の問題を生成する
A = PJP^{-1}となる
つまり、広義固有空間の基底は P の縦ベクトルたちからなる
difficulty: 問題の難しさ（大きいほど難しい）デフォルトは 3*n
"""
def make_problem_Jordan_normal_form(J,difficulty=None):
    n = len(J)
    P = random_unimodular(n,difficulty)
    Q = np.linalg.inv(P) 
    A = P@np.matrix(J)@Q

    # P,Q,A は整数行列であることを確認
    assert np.all(np.abs(P@Q - np.eye(n)) < 1e-5)
    assert np.all(np.abs(P - np.round(P)) < 1e-5)
    assert np.all(np.abs(Q - np.round(Q)) < 1e-5)
    assert np.all(np.abs(A - np.round(A)) < 1e-5)

    show_info(P,Q,J,A)
    show_problem(A)
    show_ans(P,Q,J,A)
    
