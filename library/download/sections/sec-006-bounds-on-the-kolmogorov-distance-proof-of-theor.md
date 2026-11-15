---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-006-bounds-on-the-kolmogorov-distance-proof-of-theor
section_title: "Bounds on the Kolmogorov distance. Proof of Theorem 1.2"
section_number: null
pages: 20-23
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
As before, let Fn denote the empirical measure associated with observations x1,...,xn and F =
EFn their mean with respect to a given probability measure μ on Rn. In this section, we derive
uniform bounds on Fn(x) −F(x), based on Proposition 6.3, and thus prove Theorem 1.2. For
applications to the matrix scheme, we shall also replace F, which may be difﬁcult to determine,
by the well-behaving limit law G (with the argument relying on Proposition 6.4).
Let the random variables X1,...,Xn have joint distribution μ, satisfying LSI(σ 2), and assume
that F has a ﬁnite Lipschitz seminorm M = ∥F∥Lip. Deﬁne
β = (Mσ)2/3
n1/3
.
Proof of Theorem 1.2. We use the inequalities (6.5) and (6.6) to derive an upper bound on
∥Fn −F∥= supx |Fn(x) −F(x)|. (For the sake of extension of Theorem 1.2 to Theorem 7.1
below, we relax the argument and do not assume that F is continuous.)
So, ﬁx r > 0 and an integer N ≥2. One can always pick up points −∞= x0 ≤x1 ≤··· ≤
xN−1 ≤xN = +∞with the property that
F(xi−) −F(xi−1) ≤1
N ,
i = 1,...,N.
(7.1)
Note that Fn(x0) = Fn(x0) = 0 and Fn(xN) = Fn(xN) = 1. It then follows from (6.5) that
P

max
1≤i≤N[Fn(xi−) −F(xi−)] ≥βr

≤(N −1)e−2r3/27
and, similarly, by (6.6),
P

max
1≤i≤N[F(xi−1) −Fn(xi−1)] ≥βr

≤(N −1)e−2r3/27.
Hence, for the random variable
ξN = max

max
1≤i≤N[Fn(xi−) −F(xi−)], max
1≤i≤N[F(xi−1) −Fn(xi−1)]

,
we have that
P{ξN ≥βr} ≤2(N −1)e−2r3/27.
(7.2)
Now, take any point x ∈R different from all of the xj’s and select i from 1,...,n such that
xi−1 < x < xi. Then, by (7.1),
Fn(x) −F(x) ≤Fn(xi−) −F(xi−1)
= [Fn(xi−) −F(xi−)] + [F(xi−) −F(xi−1)] ≤ξN + 1
N .
Similarly,
F(x) −Fn(x) ≤F(xi−) −Fn(xi−1)
= [F(xi−) −F(xi−1)] + [F(xi−1) −Fn(xi−1)] ≤ξN + 1
N .
Therefore, |Fn(x) −F(x)| ≤ξN + 1
N , which also extends by continuity from the right to all
points xj. Thus, ∥Fn −F∥≤ξN + 1
N and, by (7.2),
P

∥Fn −F∥> βr + 1
N
	
≤2(N −1)e−2r3/27.
Note that this also holds automatically in the case N = 1. Choose N = [ 1
βr ] + 1. We then have
1
N ≤βr and get
P{∥Fn −F∥> 2βr} ≤2
βr e−2r3/27.
Finally, changing 2βr into r, we arrive at the bound (1.5) of Theorem 1.2,
P{∥Fn −F∥> r} ≤4
r exp

−2
27
 r
β
3	
,
(7.3)
and so the constant c = 2/27.
It remains to derive the bound on the mean E∥Fn −F∥. Given 0 ≤r0 ≤1, we can write,
using (7.3),
E∥Fn −F∥=
 1
0
μ{∥Fn −F∥> r}dr =
 r0
0
+
 1
r0
(7.4)
≤r0 + 4
r0
exp

−2
27
r0
β
3	
.
This bound also holds for r0 > 1.
First, assume that 0 < β ≤1 and choose r0 = 3β log(1 + 1
β ). Then, for the last term in (7.4),
we have
4
r0
exp

−2
27
r0
β
3	
=
4
3β log(1 + 1/β)e−2log(1+1/β)
= 4
3
β
(1 + β)2 log1/3(1 + 1/β)
≤Bβ log1/3

1 + 1
β

with some constant B satisfying (1+β)3 log(1+ 1
β ) ≥( 4
3B )3/2. For example, we can take B = 2
and then, by (7.4), we have
E∥Fn −F∥≤5β log1/3

1 + 1
β

.
(7.5)
As for the values β ≥1, simple calculations show that the right-hand side of (7.5) is greater
than 1, so the inequality (1.6) is fulﬁlled with C = 5.
Theorem 1.2 is therefore proved.
□
Remark. If Mσ in Theorem 1.2 were of order 1, then E∥Fn −F∥would be of order at most
( logn
n )1/3. Note, however, that under PI(σ 2), and if all EXi = 0, the quantity Mσ is separated
from zero and, more precisely, Mσ ≥
1
√
12.
Indeed, by Hensley’s theorem in dimension 1 [1,26], in the class of all probability densi-
ties p(x) on the line, the expression (

x2p(x)dx)1/2 esssupx p(x) is minimized for the uni-
form distribution on symmetric intervals and is therefore bounded from below by 1/
√
12.
Since F is Lipschitz, it has a density p with M = esssupx p(x). On the other hand, it fol-
lows from the Poincaré-type inequality that σ 2 ≥Var(Xi) = EX2
i . Averaging over all i’s, we
get σ 2 ≥

x2 dF(x), so Mσ ≥(

x2p(x)dx)1/2 esssupx p(x).
With similar arguments based on Proposition 6.4, we also obtain the following generalization
of Theorem 1.2.
Theorem 7.1. Assume that X1,...,Xn have a distribution on Rn satisfying LSI(σ 2). Let G be
a distribution function with ﬁnite Lipschitz seminorm M. Then, for all r > 0,
P{∥Fn −G∥≥r + ∥F −G∥} ≤4
r exp

−2
27
 r
β
3	
,
where β = (Mσ)2/3n−1/3. In particular,
E∥Fn −G∥≤5β log1/3

1 + 1
β

+ ∥F −G∥.
Remarks. It remains unclear whether or not one can involve the i.i.d. case in the scheme of
Poincaré or logarithmic Sobolev inequalities to recover the rate 1/√n for E∥Fn −F∥, even if
some further natural assumptions are imposed (which are necessary, as we know from Exam-
ples 1 and 2). In particular, one may assume that the quantities M and σ are of order 1, and that
EXi = 0, Var(Xi) = 1. The question is the following: under, say, LSI(σ 2), is it true that
E∥Fn −F∥≤C
√n
with some absolute C? Or at least E|Fn(x) −F(x)| ≤C
√n for individual points?
