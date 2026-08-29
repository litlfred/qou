---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-032-43-depoissonization-and-proof-of-theorem-4-fix-s
section_title: "Depoissonization and proof of Theorem 4. Fix some m = 1, 2, . . . and"
section_number: 4.3
pages: 26-33
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4 — 35 sections: Introduction; Plancherel measures. Given a ﬁnite; Poissonization and correlation fun"
---
denote by Fn the distribution function of λ1, . . . , λm under the Plancherel measure
Mn,
Fn(x1, . . . , xm) = Mn ({λ | λi < xi , 1 ≤i ≤m}) .
ASYMPTOTICS OF PLANCHEREL MEASURES
507
Also, set
F(θ, x) = e−θ
∞
X
k=0
θk
k! Fk(x).
This is the distribution function corresponding to the measure M θ.
The measures Mn can be obtained as distribution at time n of a certain random
growth process of a Young diagram; see e.g. [42]. This implies that
Fn+1(x) ≤Fn(x) ,
x ∈Rm .
Also, by construction, Fn is monotone in x and similarly
F(θ, x) ≤F(θ, y) ,
xi ≤yi ,
i = 1, . . . , m .
(4.17)
We shall use these monotonicity properties together with the following lemma.
Lemma 4.7 (Johansson, [16]). There exist constants C > 0 and n0 > 0 such that
for any nonincreasing sequence {bn}∞
n=0 ⊂[0, 1],
1 ≥b0 ≥b1 ≥b2 ≥b3 ≥· · · ≥0,
and its exponential generating function
B(θ) = e−θ
∞
X
k=0
θk
k! · bk
we have for all n > n0 the following inequalities:
B(n + 4
√
n ln n) −C
n2 ≤bn ≤B(n −4
√
n ln n) + C
n2 .
This lemma implies that for all x ∈Rm
F(n + 4
√
n ln n, x) −C
n2 ≤Fn(x) ≤F(n −4
√
n ln n, x) + C
n2 .
(4.18)
Set
¯1 = (1, . . . , 1) .
Theorem 5 asserts that
F

θ, 2θ
1
2 ¯1 + θ
1
6 x

→F(x),
θ →+∞,
x ∈Rm,
(4.19)
where F(x) is the corresponding distribution function for the Airy ensemble. Note
that F(x) is continuous.
Denote n± = n ± 4
√
n ln n. Then for i = 1, . . . , m
2n
1
2
± + n
1
6
± xi = 2n
1
2 + n
1
6 xi + O((ln n)1/2) .
Hence, for any ε > 0 and all suﬃciently large n we have
2n
1
2
+ + n
1
6
+ (xi −ε) ≤2n
1
2 + n
1
6 xi ≤2n
1
2
−+ n
1
6
−(xi + ε) ,
for i = 1, . . . , m. By (4.17) this implies that
F

n+, 2n
1
2 ¯1 + n
1
6 x

≥F

n+, 2n
1
2
+ ¯1 + n
1
6
+ (x −ε ¯1)

,
F

n−, 2n
1
2 ¯1 + n
1
6 x

≤F

n−, 2n
1
2
−¯1 + n
1
6
−(x + ε ¯1)

.
508
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
From this and (4.18) we obtain
F

n+, 2n
1
2
+ ¯1 + n
1
6
+ (x −ε ¯1)

−C
n2
≤Fn

2n
1
2 ¯1 + n
1
6 x

≤F

n−, 2n
1
2
−¯1 + n
1
6
−(x + ε ¯1)

+ C
n2 .
From this and (4.19) we conclude that
F (x −ε ¯1) + o(1) ≤Fn

2n
1
2 ¯1 + n
1
6 x

≤F (x + ε ¯1) + o(1)
as n →∞. Since ε > 0 is arbitrary and F(x) is continuous we obtain
Fn

2n
1
2 ¯1 + n
1
6 x

→F(x),
n →∞,
x ∈Rm,
which is the statement of Theorem 4.
Appendix A. General properties of determinantal point processes
In this Appendix, we collect some necessary facts about determinantal point
processes, their correlation functions, Fredholm determinants, and convergence of
trace class operators.
Let X be a countable set, let Conf(X) = 2X be the set of subsets of X and denote
by Conf(X)0 ⊂Conf(X) the set of ﬁnite subsets of X. We call elements of Conf(X)
conﬁgurations. Let L be a kernel on X, that is, a function on X × X also viewed as
a matrix of an operator in H = ℓ2(X).
By a determinantal point process on X we mean a probability measure on
Conf(X)0 such that
Prob(X) =
det

L(xi, xj)

xi∈X
det(1 + L)
,
X ∈Conf(X)0 .
Here the determinant in the numerator is the usual determinant of linear algebra,
whereas the determinant in the denominator is, in general, a Fredholm determinant.
Some suﬃcient conditions under which det(1 + L) makes sense are described in the
following subsection.
A.1. Fredholm determinants and determinantal processes. Let H be a com-
plex Hilbert space, L(H) the algebra of bounded operators in H, and L1(H), L2(H)
the ideals of trace class and Hilbert–Schmidt operators, respectively.
Assume we are given a splitting H = H+ ⊕H−. According to this splitting,
write operators A ∈L(H) in block form, A =
A++
A+−
A−+
A−−

, where
A++ : H+ →H+,
A+−: H−→H+,
A−+ : H+ →H−,
A−−: H−→H−.
The algebra L(H) is equipped with a natural Z2-grading. Speciﬁcally, given A, its
even part Aeven and odd part Aodd are deﬁned as follows:
Aeven =
A++
0
0
A−−

,
Aodd =
 0
A+−
A−+
0

.
Denote by L1|2(H) the set of operators A ∈L(H) such that Aeven is in the trace
class L1(H) while Aodd is in the Hilbert–Schmidt class L2(H). It is readily seen
ASYMPTOTICS OF PLANCHEREL MEASURES
509
that L1|2(H) is an algebra. We endow it with the topology induced by the trace
norm on the even part and the Hilbert–Schmidt norm on the odd part.
It is well known that the determinant det(1 + A) makes sense if A ∈L1(H). It
can be characterized as the only function which is continuous in A with respect to
the trace norm ∥A∥1 = tr
√
AA∗and which coincides with the usual determinant
when A is a ﬁnite–dimensional operator. See, e.g., [33].
Proposition A.1. The function A 7→det(1 + A) admits a unique extension to
L1|2(H), which is continuous in the topology of that algebra.
Proof. For A ∈L1|2(H), set
det(1 + A) = det((1 + A)e−A) · etr Aeven.
(A.1)
As is well known (e.g., [33]),
A 7→(1 + A)e−A −1
is a continuous map from L2(H) to L1(H).
Next, A 7→tr Aeven evidently is a
continuous function on L1|2(H). Consequently, (A.1) is well deﬁned and is a con-
tinuous function on L1|2(H). When A ∈L1(H), (A.1) agrees with the conventional
deﬁnition, because then
det((1 + A)e−A) · etr Aeven = det(1 + A)e−tr A+tr Aeven = det(1 + A).
This concludes the proof.
Corollary A.2. If {Pn} is an ascending sequence of even projection operators in
H such that Pn →1 strongly, then
det(1 + A) = lim
n→∞det(1 + PnAPn).
Proof. Indeed, PnAPn approximates A in the topology of L1|2(H).
Corollary A.3. If A, B ∈L1|2(H), then
det(1 + A) det(1 + B) = det((1 + A)(1 + B)).
Proof. Indeed, this is true for ﬁnite–dimensional A, B, and then we use the conti-
nuity argument.
In our particular case, the splitting of H = ℓ2(X) will come from a splitting of
X = X+ ⊔X−into two complementary subsets as follows:
H± = ℓ2(X±) .
An operator L in H will be viewed as an inﬁnite matrix whose rows and columns
are indexed by elements of X. Given X ⊂X, we denote by LX the corresponding
ﬁnite submatrix in L.
Proposition A.4. If L ∈L1|2(H), then
X
X
det LX = det(1 + L),
(A.2)
where summation is taken over all ﬁnite subsets X ⊂X including the empty set
with the understanding that det L∅= 1.
The exact meaning of the sum in the left-hand side is explained in the proof.
510
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Proof. Given a ﬁnite subset Y ⊂X, we assign to it, in the natural way, a projection
operator PY . Note that PY is even. By elementary linear algebra, we have
X
X⊆Y
det LX = det(1 + PY LPY ).
Assume Y becomes larger and larger, so that in the limit it covers the whole X.
Then the left-hand side tends to the left-hand side of (A.2). More precisely, this is
evident if all the minors det LX are nonnegative. In general, instead of proving that
the sum in the left-hand side of (A.2) is absolutely convergent we simply deﬁne it
as
X
X
det LX = lim
{Y }
X
X⊆Y
det LX .
On the other hand, the right-hand side tends to det(1 + L) by Corollary A.2.
Remark A.5. Suppose that L =
 0
A
−A∗
0

, where A is of Hilbert–Schmidt class.
Then L ∈L1|2(H). It is readily seen that det LX ≥0 for all X, and it is worth
noting that det LX = 0 unless |X+| = |X−|. By Proposition A.4, we can deﬁne a
probability measure on ﬁnite subsets X of X by
Prob(X) =
det LX
det(1 + L) ,
X ∈Conf(X)0 .
A.2. Correlation functions of determinantal processes. Given X ∈Conf(X)0,
let ρ(X) be the probability that a random conﬁguration contains X, that is,
ρ(X) = Prob ({Y ∈Conf(X)0, X ⊂Y }) .
We call ρ(X) the correlation functions. The fundamental fact about determinantal
point processes is that their correlation functions again have a determinantal form.
Proposition A.6. Let L be as above and set K = L(1 + L)−1. Then ρ(X) =
det KX.
Proof. We follow the argument in [11], Exercise 5.4.7. Let f(x) be an arbitrary
function on X such that f(x) = 1 for all but a ﬁnite number of x’s. Form the
probability generating functional:
Φ(f) =
X
X
Y
x∈X
f(x) · Prob(X).
Then, viewing f as a diagonal matrix, we get
Φ(f) =
P
X det(fL)
det(1 + L)
= det(1 + fL)
det(1 + L) ,
where the last equality is justiﬁed by Proposition A.4 applied to the operator fL.
Now, set g(x) = f(x) −1, so that g(x) = 0 for all but ﬁnitely many x’s. Then
we can rewrite this relation as
Φ(f) = det(1 + fL)
det(1 + L) = det(1 + L + gL)
det(1 + L)
= det(1 + gK),
where the last equality follows by Corollary A.3.
ASYMPTOTICS OF PLANCHEREL MEASURES
511
Next, as gK is in L1|2(H) (it is even ﬁnite–dimensional), this can be rewritten
as
Φ(f) =
X
X
det((gK)X) =
X
X
Y
x∈X
g(x) · det KX.
On the other hand, by the very deﬁnition of Φ(f),
Φ(f) =
X
X
Y
x∈X
g(x) · ρ(X).
This implies ρ(X) = det KX, as desired.
Remark A.7. If L =
 0
A
−A∗
0

, then
K =

AA∗(1 + AA∗)−1
(1 + AA∗)−1A
−(1 + A∗A)−1A∗
A∗A(1 + A∗A)−1

.
In the recent survey [35], the determinantal formula ρ(X) = det KX for the
correlation functions is taken as a deﬁnition. The paper [35] contains a more general
and detailed discussion of the basics of the theory of determinantal processes which
in [35] are called determinantal random point ﬁelds.
A.3. Complementation principle. In this section we discuss a simple but useful
observation which was communicated to us by S. Kerov. Consider an arbitrary
probability measure on Conf(X) such that its correlation functions
ρ(X) = Prob({Y ∈Conf(X), X ⊂Y }) ,
X ∈Conf(X)0 ,
have a determinantal form
ρ(X) = det
h
K(xi, xj)
i
xi∈X
for some kernel K.
Let Z ⊂X be an arbitrary subset of X.
Consider the symmetric diﬀerence
mapping
△Z : Conf(X) →Conf(X) ,
Y 7→Y △Z ,
which is an involution in Conf(X).
Let Prob△= (△Z)∗Prob be the image of
our probability measure under △Z and let ρ△(X) be the correlation functions of
the measure Prob△.
Deﬁne a new kernel K△as follows.
Let Z′ = X \ Z be
the complement of Z and write the matrix K in block form with respect to the
decomposition X = Z′ ⊔Z:
KZ′⊔Z =
A
B
C
D

.
By deﬁnition, set
K△
Z′⊔Z =

A
B
−C
1 −D

.
We have the following
Proposition A.8. ρ△(X) = det
h
K△(xi, xj)
i
xi∈X .
512
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
Proof. Set X1 = X \ Z, X2 = Z \ X. By the inclusion-exclusion principle we have
ρ△(X) = Prob ({Y ∈Conf(X), X1 ⊂Y, X2 ∩Y = ∅})
=
X
S⊂X2
(−1)|S|ρ(X1 ∪S) .
This alternating sum is easily seen to be identical by linearity to the expansion of
det
h
K△(xi, xj)
i
xi∈X using
 A
B
−C
1 −D

=
 A
B
−C
−D

+
0
0
0
1

.
A.4. Convergence of trace class operators. Let K1, K2, . . . and K be Hermit-
ian nonnegative operators in L1(H). The following proposition is a special case of
Theorem 2.20 in the book [34] (we are grateful to P. Deift for this reference). For
the reader’s convenience we give a proof here.
Proposition A.9. The following conditions are equivalent:
(i) ∥Kn −K∥1 →0;
(ii) tr Kn →tr K and Kn →K in the weak operator topology.
First, we prove a lemma:
Lemma A.10. Let X =
 A
B
B∗
D

be a nonnegative operator 2 × 2 matrix. Then
∥B∥1 ≤
√
tr A · tr D.
Proof of Lemma A.10. Without loss of generality one can assume that the block B
is a nonnegative diagonal matrix, B = diag(b1, b2, . . . ). Write the blocks A and D
as matrices, too, and let ai and di be their diagonal entries. Since X ≥0, we have
b2
i ≤aidi and therefore
∥B∥1 =
X
bi ≤
X p
aidi ≤
qX
ai ·
X
di ≤
√
tr A · tr D.
Proof of Proposition A.9. Clearly, (i) implies (ii).
To check the converse claim,
write K in block form,
K =

A
B
B∗
D

,
where A is of ﬁnite size and tr D is small. Write all the Kn’s in block form with
respect to the same decomposition of the Hilbert space,
Kn =

An
Bn
B∗
n
Dn

.
Since Kn →K weakly, we have convergence of ﬁnite blocks, An →A, which implies
tr An →tr A. Since tr Kn →tr K, we get tr Dn →tr D, so that all the traces tr Dn
are small together with tr D provided that n is large enough.
ASYMPTOTICS OF PLANCHEREL MEASURES
513
Write
K′ =
A
0
0
0

and similarly for Kn. Then
∥Kn −K∥1 ≤∥Kn −K′
n∥1 + ∥K′
n −K′∥1 + ∥K′ −K∥1.
In the right-hand side, the ﬁrst and the third summands are small because of the
lemma, while the second summand is small because it is equal to ∥An −A∥1.
Proposition A.11. The map (A1, . . . , An) 7→det(I + λ1A1 + · · · + λnAn) deﬁnes
a continuous map from (L1(H))n to the algebra of entire functions in n variables
with the topology of uniform convergence on compact sets.
Proof. The fact that det(I + λ1A1 + · · · + λnAn) is holomorphic in {λi} for any
trace class operators A1, . . . , An is proved in [33]. The continuity of the map follows
from the inequality
| det(I + B) −det(I + C)| ≤∥B −C∥1 exp(∥B∥1 + ∥C∥1 + 1)
which holds for any B, C ∈L1(H); see [30, 34].
