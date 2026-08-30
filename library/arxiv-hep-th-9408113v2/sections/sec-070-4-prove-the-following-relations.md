---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-070-4-prove-the-following-relations
section_title: "Prove the following relations"
section_number: 4
pages: 78-80
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
i)
∑
λ
dimV (n)
λ ·Kλ,µ(1) =
∏
j
(
n +µj− 1
µj
)
,
ii)
∑
λ
[
n
λ′
]
q
·Kλ,µ(1) =
∏
j
[
n +µj− 1
µj
]
q
.
Here
[
n
λ
]
:=
∏
x=(i,j)∈λ
1−qn+i−j
1−qh(x) is the generalized q-binomial coeﬃcient; V (n)
λ is the
highest weight λ irreducible representation of gl(n) and Kλ,µ(1) is the Kostka number.
Hint: use the Littelwood formula
∑
λ
sλ(x1,...,x n)sλ(y1,...,y m) =
n∏
i=1
m∏
j=1
1
1−xiyj
.
5. (Construction of elements in C(F )). We use the notation from the Section 2.3.1.
Deﬁnition 8. Every equation of the following form
X A∏
r∈I
(1−ζ kr
mX r)Ar = 1, (1)
whereA,k r,A r are integers,ζm = exp
(2πi
m
)
∈F , and I is a ﬁnite set of natural numbers,
is called a (generalized) cyclotomic equation.
Now, suppose that a∈F ∗,a⁄= 1 satisﬁes the cyclotomic equation (1), and let a natural
numberN satisfy
i) 2 | NA ,
ii) r| NA ,m| (NA r/r)kr, for r∈I.Show that
b :=
∑
r∈I
(NA r/r)[ζ kr
mar]∈C(F ).
Remark. Letb be the image of b in the Bloch group B(F ). It is an interesting problem
to ﬁnd an eﬀective criteria when b∈B(F )tor.
Dilogarithm identities 79
2.5. Quantum dilogarithm.
Let us remind that the Euler dilogarithm Li2(x) is deﬁned for 0 ≤x≤ 1 by
Li2(x) =
∑
n≥1
xn
n2.
Deﬁnition 9 (q-analog of Euler’s dilogarithm or quantum dilogarithm). Quantum
dilogarithmLi2(x;q) is the following formal series
Li2(x;q) =
∑
n≥1
xn
n(1−qn). (2.52)
Before stating the basic properties of the quantum dilogari thm, let us remind the
deﬁnition of the two q-exponential functions (see e.g. [GR], Appendix II)
eq(x) =
∑
n≥0
xn
(q)n
= 1
(x)∞
, (2.53)
Eq(x) =
∑
n≥0
q
n(n−1)
2 xn
(q)n
= (−x)∞.
Here we use the standard q-analysis notation:
(x)∞ := (x;q)∞ =
∏
n≥0
(1−xqn), (x)n := (x;q)∞
(xqn;q)∞
.
It is clear from the deﬁnition (2.53) that
(1 +x)Eq(qx) = Eq(x), e q(qx) = (1−x)eq(x), e q−1(x) = Eq(−qx). (2.54)
Lemma 8. We have
i) Li2(x;q) = log(eq(x)),
ii) Li2(x;q) +Li2(x;q−1) =− log(1−x).
Proof. it is clear from (2.54) that
Li2(qx;q) = Li2(x;q) + log(1−x).
Hence, if Li2(x;q) =
∑
n≥1
anxn, then qnan =an− 1
n .
80 Anatol N. Kirillov
Proposition H (Euler-Maclaurin’s summation formula). If f∈C2n([M,N ]), M and
N integers, then
N∑
m=M
f (m) =
∫ N
M
f (t)dt + 1
