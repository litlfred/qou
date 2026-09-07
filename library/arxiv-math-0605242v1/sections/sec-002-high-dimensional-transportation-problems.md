---
doc_id: arxiv-math-0605242v1
doc_title: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel §"
section_id: sec-002-high-dimensional-transportation-problems
section_title: "High dimensional transportation problems"
section_number: null
pages: 3-6
source_pdf: 0605242v1.pdf
source_sha256: 65fac7285e4a77f4
doc_brief: "N-Fold Integer Programming Jesús A. De Loera∗ Raymond Hemmecke † Shmuel Onn ‡ Robert Weismantel § — In this article we study a broad class of integer programming problem s in variable dimension."
---
A d-way transportation polytope is the set of all m1 × · · · × md nonnegative arrays x = (xi1,...,id) such
that the sums of the entries over some of their lower dimensio nal subarrays ( margins) are speciﬁed.
3
For simplicity of exposition, we shall concentrate here onl y on d-way line-sum polytopes, of the form
T =


 x ∈ Rm1×···×md
+ :
∑
i1
xi1,...,id = ui2,...,id ,
∑
i2
xi1,...,id = ui1,i3,...,id , . . . ,
∑
id
xi1,...,id = ui1,...,id− 1


 .
Transportation polytopes and their integer points (called contingency tables by statisticians), have
been studied and used extensively in the operations researc h literature and in the context of secure
statistical data disclosure by public agencies such as the c ensus bureau and the national center for
health statistics. In the operations research literature, one is typically interested in the integer and
linear transportation problems, which are the integer and l inear programming problems over the trans-
portation polytope, see e.g. [2, 15, 17, 18, 22, 23] and refer ences therein. In the statistics community,
one is often interested in the values an entry can attain in al l tables with ﬁxed margins, related to the
security of the entry under margin disclosure, and in the con struction of a Markov basis allowing a
random walk on the set of tables with ﬁxed margins, see e.g. [1 , 3, 4, 7, 8, 14] and references therein.
It is well known that the system deﬁning a 2-way transportati on polytope is totally unimodular.
This implies that all the above problems are easy in this case . However, already 3-way transportation
problems are much harder. Consider the problem of deciding i f a given 3-way line-sum polytope of
r × s × l arrays (with r rows, s columns and l layers) contains an integer point: the computational
complexity of this problem provides useful indication abou t the diﬃculty of the problems mentioned
above. If r, s, l are all ﬁxed, then the problem is solvable in polynomial time by integer programming
in ﬁxed dimension rsl. On the other hand, if r, s, l are all variable part of the input, then the problem
is NP-complete [14]. The in-between cases are much more deli cate. The case of two parameters r, s
variable and one parameter l ﬁxed was recently resolved in [5], where it was shown to be NP- complete,
strengthening [14]. Moreover, very recently, in [6], the fo llowing striking universality result was shown.
Proposition 2.1 Any rational polytope P = {y ∈ Rn
+ : Ay = b} is polynomial time representable as
a 3-way line-sum transportation polytope of size r × s × 3 for some (polynomially bounded) r and s,
T = { x ∈ Rr×s×3
+ :
∑
i
xi,j,k= wj,k,
∑
j
xi,j,k= vi,k,
∑
k
xi,j,k= ui,j } .
Here representable means that there is a coordinate-erasin g projection from Rr×s×3 onto Rn providing
a bijection between T and P and between the sets of integer points T ∩ Zr×s×3 and P ∩ Zn. Thus, any
rational polytope is an r × s × 3 line-sum polytope, and any integer (respectively, linear) programming
problem is equivalent to an integer (respectively, linear) r × s × 3 line-sum transportation problem.
This result led to the solution of several open problems from [22] and [23] and had several implications
on the complexity of Markov bases and the entry security prob lem, see [6] and [7] for more details.
4
However, the last case, of two parameters r, s ﬁxed and one parameter l variable, has remained
open and intriguing. Here, as a consequence of Theorem 1.1, w e are able to resolve this problem and
show that both the decision and optimization problems are po lynomial time solvable.
Corollary 2.2 Fix any r, s . Then there is a polynomial time algorithm that, given l, integer objective
vector c, and integer line-sums (ui,j), (vi,k) and (wj,k), solves the integer transportation problem
min{ cx : x ∈ Nr×s×l ,
∑
i
xi,j,k= wj,k,
∑
j
xi,j,k= vi,k,
∑
k
xi,j,k= ui,j } .
Proof. We formulate the 3-way integer transportation problem as an n-fold integer program with
n := l, p := r + s, and q := r · s. Reindex the variables as xk
i,j := xi,j,k so that the variables vector
is x = ( x1, . . . , x n) with xk = ( xk
i,j) ∈ Nr×s a 2-way r × s table - the kth layer of the 3-way table x.
Similarly write c = (c1, . . . , c n) with ck ∈ Zr×s for the objective vector. Next, put b := (b0, b 1, . . . , b n),
with b0 ∈ Nrs deﬁned by b0 := ( ui,j), and bk ∈ Nr+s deﬁned by bk := (( vi,k), (wj,k)) for k = 1 , . . . , n .
Finally, let A be the p×q = (r+s)×r·s matrix of equations for the usual 2-way transportation poly tope,
forcing row-sums and column-sums on each of the r × s layers xk by Axk = bk, k = 1 , . . . , n . Then
the equations Axk = bk force the line-sums vi,k and wj,k, and the additional n-fold integer program
binding constraint ∑ n
k=1 xk = b0 forces the “long” line-sums ui,j. This completes the encoding. Since
r, s are ﬁxed, so are p, q , and A, and therefore, the corollary follows from Theorem 1.1. □
Example 2.3 Consider the case r = s = 3 (the smallest where the problem is genuinely 3-dimension al).
Then p = 6, q = 9, and writing xk = (xk
1,1, x k
1,2, x k
1,3, x k
2,1, x k
2,2, x k
2,3, x k
3,1, x k
3,2, x k
3,3), the matrix A which
deﬁnes the n-fold program providing the formulation of the 3 × 3 × l transportation problem is
A =


1 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
1 0 0 1 0 0 1 0 0
0 1 0 0 1 0 0 1 0
0 0 1 0 0 1 0 0 1


.
Already for this case, of 3 × 3 × l tables, the only polynomial time algorithm for the correspo nding
line-sum integer transportation problem we are aware of is t he one guaranteed by Corollary 2.2 above.
Corollary 2.2 extends to transportation problems of any dim ension d, for long tables, namely, of
size m1 × · · · × md−1 × l, where m1, . . . , m d−1 are ﬁxed and only the length l is variable, as follows.
5
Corollary 2.4 Fix d, m 1, . . . , m d−1. Then there is a polynomial time algorithm that, given l, integer
objective c, and line-sums (ui2,...,id), . . . , (ui1,...,id− 1), solves the long multiway transportation problem
min{cx : x ∈ Nm1×···×md− 1×l :
∑
i1
xi1,...,id = ui2,...,id , . . . ,
∑
id
xi1,...,id = ui1,...,id− 1 } .
Proof. The long multiway transportation problem can be encoded as a n n-fold integer program with
n := l, p := ∑ d−1
i=1 mi, and q := ∏ d−1
i=1 mi, by reindexing the variables as xid
i1,...,id− 1 := xi1,...,id, letting
A be the matrix of equations of line-sums of ( d − 1)-way transportation polytope of m1 × · · · × md−1
arrays, and proceeding in direct analogy to the proof of Coro llary 2.2. The details are omitted. □
