---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-006-4-equilibrium-measure-and-g-function
section_title: "Equilibrium Measure and g-function"
section_number: 4
pages: 17-18
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
In this Section, the equilibrium measure is explicitly calculated for each γ > 0
(Lemma 4.3) and, using this equilibrium measure, the g-function (4.8) is introduced
in order to convert the RHP (1.26) into a RHP which is normalized to be I at ∞.
Let Σ denote the unit circle oriented counterclockwise and f(eiθ) = f(z) be a
non-negative, periodic, smooth function on Σ. Let pq(z) = κqzq + · · · be the q-
th normalized orthogonal polynomial with respect to the weight f(eiθ) dθ
2π on the
unit circle. Deﬁne the polynomial p∗
q(z) ≡zq ¯pq(1/z) = zqpq(1/¯z) (see [Sz1]). We
consider the following RHP : Let Y (z) be the 2×2 matrix-valued function satisfying









Y (z)
is analytic in
C −Σ,
Y+(z) = Y−(z)
 
1
1
zk+1 f(z)
0
1
!
on
Σ,
Y (z)z−(k+1)σ3 = I + O( 1
z)
as
z →∞.
(4.1)
The following Lemma is the starting point of our calculations.
18
JINHO BAIK, PERCY DEIFT, AND KURT JOHANSSON
Lemma 4.1. (cf. [FIK], [DKMVZ1]) The RHP (4.1) has a unique solution
Y (z) =
 
1
κk+1 pk+1(z)
1
κk+1
R
Σ
pk+1(s)
s−z
f(s)ds
2πisk+1
−κkp∗
k(z)
−κk
R
Σ
p∗
k(s)
s−z
f(s)ds
2πisk+1
!
.
Proof. Existence : Using the property of Cauchy operator C+ −C−= I, where
Ch(z) ≡
R
Σ
h(s)
s−z ds, it is a straightforward calculation to show that the above ex-
pression for Y satisﬁes the jump condition. The asymptotics at ∞codes in precisely
the fact that the p′
ks are the normalized orthogonal polynomials for the weight
f(eiθ)dθ.
Uniqueness : Suppose that there is another solution ˜Y of RHP. Noting
det

1
1
zk+1 f(z)
0
1

= 1, we have that det ˜Y is entire, and →1 as z →∞. Therefore
by Liouville’s theorem, det ˜Y ≡1. In particular, ˜Y is invertible. Now set Z =
Y ˜Y −1. Then it has no jump on Σ hence is entire. Also, Z →I as z →∞, and
therefore Z ≡I.
From this Lemma, we have
κ2
k = −Y21(0)
(4.2)
Therefore the RHP (1.26) has a unique solution and (1.27) is veriﬁed.
Again set q = k + 1 and
γ = 2
√
λ
q
.
(4.3)
We are interested in the case when q and 2
√
λ are of the same order , or more
precisely, γ →1. In this Section, and also in Sections 5 and 6, we consider the
RHP (1.26) with parameter γ and q,









Y (z; q)
analytic in
C −Σ,
Y+(z; q) = Y−(z; q)
 
1
1
zq e
qγ
