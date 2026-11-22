---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-016-43-multi-type-hard-spheres-in-mathbbrd
section_title: "Multi-Type Hard Spheres in mathbbRd"
section_number: 4.3
pages: 30-41
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Let (rn)n∈N be an increasing sequence of positive real numbers and let Brn(0) ⊂Rd, n ∈N,
be the family of d-dimensional closed balls around 0 with the corresponding radii. To the
sequence (rn)n∈N of radii is associated the sequence of non-negative activities (zn)n∈N such
that the ball Bri has the activity zi. In the setup of hard-core systems in the continuum from
Sect. 2.3, let X be given by all possible translates of these objects. Notice that the closed
balls are compact convex sets that are non-empty and regular closed. We refer to this special
case of a hard-core system as a system of multi-type hard spheres in Rd. We will show a
new sufﬁcient condition for absolute convergence of the activity expansions in these types
of models.
For an integrable function h : X →R we write

X
h(Z)λ(dZ) =

ℓ≥1

Rd h(x + Brℓ(0))dx.
We deﬁne the family of functions (Vr)r>0 by setting for Borel sets D ⊂Rd
Vr(D) :=

Rd 1l{(x+Br(0))∩D̸=∅}dx,
(4.11)
where Br(0) is the d-dimensional closed ball of radius r > 0 around 0. Naturally, the map
Vr coincides with the map V from (4.6) for the grain S given by the closed ball Br(0) and
Cluster Expansions: Necessary...
Page 31 of 47
33
therefore satisﬁes the measurability assumption from Theorem 2.6 (as a function on Dε with
the convention V (∅) = 0). Furthermore, we have Vr({y}) = |Br(0)| and Vr(Bs(y)) =
|Bs(y) ⊕Br(0)| = |Bs+r(0)| (where ⊕denotes the Minkowski sum) for any y ∈Rd and
any numbers r, s > 0.
The following auxiliary result turns out to be essential for the proof of the new sufﬁcient
condition:
Lemma 4.3 Let D1 beaﬁniteunionofboundedconvexregularclosedsubsetsofRd andlet D2
be a d-dimensional ball in Rd. The map (0, ∞) ∋r →Vr(D1∪D2)−Vr (D1)
Vr(D2)
is monotonically
decreasing in r.
Proof First of all, observe that for sets D given by a ﬁnite union of convex, regular closed
subsets of Rd the volume Vr(D) can be written as
Vr(D) = |D| + S(D)r + o(r),
(4.12)
where S(D) denotes the surface area of D. This follows from a generalized version of the
classical Steiner’s formula (see [27, Sect. 4.4]). In particular, we see that the map r →
Vr(D1∪D2)−Vr(D1)
Vr(D2)
is differentiable in r = 0.
Next, we notice that the map satisﬁes the following semi-group property:
Vr+ε(D) = Vε(D ⊕Br(0)).
Therefore, to prove the claim of the lemma, it sufﬁces to consider the differential at zero:
lim
ε↘0
1
ε
 Vε(A ∪B) −Vε(A)
Vε(B)
−|A ∪B| −|A|
|B|

,
where A := D1 ⊕Br(0) and B := D2 ⊕Br(0).
Using the formula (4.12), a simple computation shows that this limit is equal to
|B| (S(A ∪B) −S(A)) −S(B) (|A ∪B| −|A|)
|B|2
.
The monotonicity in the claim of the lemma is then equivalent to
|B| (S(A ∪B) −S(A)) −S(B) (|A ∪B| −|A|) ≤0
or, equivalently,
|B|
S(B) ≤
|A ∪B| −|A|
S(A ∪B) −S(A).
Using the obvious identities |A ∪B| −|A| = |B| −|A ∩B| and S(A ∪B) −S(A) =
S(B) −S(A ∩B), we can rewrite the last inequality as
S(B)
|B| ≤S(A ∩B)
|A ∩B| ,
which holds by the isoperimetric inequality since B = D2 ⊕Br(0) is a ball in Rd (“the ball
is the shape that minimizes the surface area for given volume”, see [7, 3.2.43]).
⊓⊔
The following sufﬁcient condition is, in some sense, a “continuous version” of the Gruber–
Kunz criterion in the setup of hard spheres in Rd. The similarity in the form arises as follows:
To establish the recurrence relations underlying the proof of Gruber–Kunz we selected a
monomer, a single point in Zd, from a conﬁguration of polymers. We follow this idea in the
33
Page 32 of 47
S. Jansen, L. Kolesnikov
proof of the following result, choosing the chopping map C and the selection rule s such
that a tiny snippet that approximates a single point in the continuous space sufﬁciently well
is selected. At the same time we choose an ansatz function a that can be interpreted as the
continuous analogue of the ansatz function from the proof of Corollary 2.8.
Theorem 4.4 In the setup of multi-type hard objects on Rd, assume that the activity z satisﬁes
∃α > 0 :

ℓ≥1
|Brℓ|eα|Brℓ+r1|zℓ< eα|Br1| −1,
(4.13)
where by |Br| we denote the (Lebesgue) volume of a ball of radius r > 0. Then the activity
expansions ρn(X1, . . . , Xn; z) converge absolutely.
Remark 4.3 Activity expansions for systems with inﬁnitely many types of objects are not
particularly well-studied in statistical mechanics. In the case of ﬁnitely many types, we
expect our result to exceed Kotecký–Preiss but to be weaker then Fernández–Procacci—as
in the special case of a single type treated above (see Remark 4.2). The general case, for
rn →∞in particular, remains to be investigated.
Proof Again, our strategy is to show that condition (i) from Theorem 2.6 is satisﬁed for an
appropriate ansatz function a. By assumption, r1 is the radius of the smallest ball present in
the system. Set a(D) := αVr1(D) for D ∈Dε, where Vr1 is given by (4.11) and α satisﬁes
(4.13). Choose some chopping map C and let D ∈Dε (the snippet-size ε > 0 is to be
speciﬁed later in the proof). Just as in the proof of Theorem 4.2, independently of the choice
of the snippet E1 (i.e., independently of the selection rule s), we obtain the following upper
bound for the left-hand side of the inequality from condition (i):
eαC1(ε) eα[V (D′∪E1)−V (D′)−V (E1)]
∞

k=1
zk
k!

Xk I(E1; D′, Y1, . . . , Yk) eαV (Y)λk(dY). (4.14)
The positive number C1(ε) converges towards 0 for ε ↘0 and is precisely the bound from
(4.9) in the proof of Theorem 4.2 for Y given by a translate of Br1(0), i.e., by a sphere of
minimal volume present in the system.
The summand for k = 1 in (4.14) is equal to

ℓ≥1
zℓeα|Brℓ+r1|

X
1{r(Y1)=rℓ}1{Y1∩E1̸=∅,Y1∩D′=∅}λ(dY1).
Notice that the integrals in the last expression are equal to [Vrℓ(D′ ∪E1)−Vrℓ(D′)] for every
ℓ∈N.
The summand for any k ≥2 in (4.14) is bounded from above by

ℓ1,...,ℓk
zℓ1 . . . zℓke
α
k
i=1
|Brℓi +r1| 
Xk
k
i=1
1{r(Yi)=rℓi }
k
i=1
1{Yi∩E1̸=∅,Yi∩D′=∅}1{Y1,...,Yk disjoint}λk(dY),
(4.15)
which—by arguments similar to the ones used for the bound C1(ε)—is again bounded by
C2(ε)

ℓ1,...,ℓk
zℓ1 . . . zℓke
α
k
i=1
|Brℓi +r1|
|Brℓ1 | . . . |Brℓk |
(4.16)
Cluster Expansions: Necessary...
Page 33 of 47
33
for a positive constant C2(ε) that is independent of k and satisﬁes C2(ε) ↘0 for ε ↘0.
Notice that the sum in (4.16) is ﬁnite for every k ∈N by assumption (4.13) [since it is simply
given by the k-th power of the left-hand side of the inequality in (4.13)]. Moreover, by the
same argument as in the proof of Theorem 4.2, the expression in (4.15) does vanish for all
but ﬁnitely many k ∈N, i.e., there exists a number N ∈N such that (4.15) is equal to zero
for all k ≥N + 1.
Altogether we get the upper bound
eαC1(ε) eα[V (D′∪E1)−V (D′)−V (E1)] ×

ℓ≥1
zℓeα|Brℓ+r1|[Vrℓ(D′ ∪E1) −Vrℓ(D′)]+
C2(ε)

2≤k≤N

ℓ1,...,ℓk
zℓ1 . . . zℓke
α
k
i=1
|Brℓi +r1|
|Brℓ1 | . . . |Brℓk |
	
.
As in the single-type case, we see that it is sufﬁcient to prove the strict inequality
eα[V (D′∪E1)−V (D′)−V (E1)] 
ℓ≥1
zℓeα|Brℓ+r1|[Vrℓ(D′ ∪E1)−Vrℓ(D′)] < eα[V (D′∪E1)−V (D)]−1
for small values of ε > 0 and, consequently, for small volumes of the snippet E1 contained
in an ε-ball.
To do so, we bound [Vrℓ(D′ ∪E1) −Vrℓ(D′)] from above by [Vrℓ(D′ ∪Bε) −Vrℓ(D′)]
for every ℓ∈N, where Bε is the ball of radius ε containing the snippet E1. Then we use
Lemma 4.3 to obtain
[Vrℓ(D′ ∪Bε) −Vrℓ(D′)] ≤[Vrm(D′ ∪Bε) −Vrm(D′)] Vrℓ(Bε)
Vrm(Bε)
for m ≤ℓ(since in that case rm ≤rℓholds by assumption) and therefore

ℓ≥1
zℓeα|Brℓ+r1|[Vrℓ(D′ ∪E1)−Vrℓ(D′)]≤Vr1(D′ ∪Bε) −Vr1(D′)
Vr1(Bε)

ℓ≥1
zℓeα|Brℓ+r1|Vrℓ(Bε).
By dominated convergence and assumption (4.13) we can choose ε > 0 small enough to
strictly bound the right-hand side of the last equation by
Vr1(D′ ∪E1) −Vr1(D′)
Vr1(E1)
(eαVr1(E1) −1).
Finally, it sufﬁces to show the inequality
eα[V (D′∪E1)−V (D′)−V (E1)] Vr1(D′ ∪E1) −Vr1(D′)
Vr1(E1)
(eα|Vr1(E1)| −1) ≤eα[V (D′∪E1)−V (D)] −1
(4.17)
as in (4.5) to conclude the proof.
⊓⊔
4.4 Tonks Gas on Z
Next we turn to the discrete one-dimensional Tonks gas with translationally invariant activ-
ities. That is, in the setup of subset polymers from Sect. 2.4 for d = 1, let (zℓ)ℓ∈N be a
33
Page 34 of 47
S. Jansen, L. Kolesnikov
sequence of non-negative numbers and consider the activity
z(X) =

zℓ,
X = {m, m + 1, . . . , m + ℓ−1} for some m ∈Z,
0,
else.
(4.18)
Theorem 4.5 Let d = 1 and let (zℓ)ℓ∈N be a sequence of non-negative activities.
(a) Suppose there exists α > 0 such that
∞

ℓ=1
eαℓzℓ≤eα −1.
(4.19)
Then T (D; z) is absolutely convergent for all ﬁnite subsets D ⊂Z.
(b) Conversely, if T (D; z) is absolutely convergent for all ﬁnite subsets D ⊂Z, then there
exists α > 0 such that (4.19) holds true.
Remark 4.4 The condition (4.19) is exactly the necessary and sufﬁcient criterion for absolute
convergence of the activity expansion of the pressure in the system derived in [13]. While
the result itself is not novel, we consider the proof to be instructive since it demonstrates how
our approach can provide conditions improving on the Fernández–Procacci criterion. In this
concrete setup even the optimal result—recovering the whole domain of convergence—can
be achieved.
The proof of the sufﬁcient condition relies on a reﬁnement of Theorem 2.7. Roughly, we
weaken condition (i) to consider the Kirkwood–Salsburg inequalities being satisﬁed only for
single rods rather than for arbitrary conﬁgurations of rods; at the same time we specify the
selection rule by assuming that the leftmost (or, alternatively, the rightmost) element {x} is
always picked from any given domain.
Proposition 4.6 Suppose there exists a non-negative function a(·) from the ﬁnite intervals of
Z to [0, ∞) with a(∅) = 0 and for every ﬁnite interval D of Z with x = min D such that

Y∋x,
Y∩D′=∅
z(Y) ea(D′∪Y)−a(D′) ≤ea(D′∪{x})−a(D′) −1,
(4.20)
where we set D′ = D\{x}. Then T (D, z) is absolutely convergent, for all ﬁnite D ⊂Z
(interval or not).
Proof We revisit the proof of the implication (i) ⇒(ii) of Theorem 2.7 given on p. 24 and
prove ﬁrst by induction over N that ˜TN(D; z) ≤exp(a(D)), for all ﬁnite discrete intervals
D ⊂Z. For N = 1, the inequality is trivial because ˜T1(D; z) = 1{|D|≤1} ≤1 ≤exp(a(D)).
Now, suppose ˜TN(D; z) ≤exp(a(D)) for some N ∈N and all discrete intervals D ⊂Z.
Let D ⊂Z be any discrete interval. If D = ∅, then ˜TN+1(D; z) = 1 ≤exp(a(D)). If D
is non-empty, let x := min D (or, alternatively, x := max D) and set D′ = D\{x}, then
Proposition 3.12 yields
˜TN+1(D; z) = ˜TN(D′; z) +

Y∋x:
Y∩D′=∅
z(Y) ˜TN(D′ ∪Y; z).
Since all the arguments D′ and D′ ∪Y of ˜TN on the right side of this identity are again ﬁnite
discrete intervals, the inductive hypothesis and our assumption (4.20) imply that
˜TN+1(D; z) ≤ea(D′) +

Y∋x:
Y∩D′=∅
z(Y)ea(D′∪Y) ≤ea(D).
Cluster Expansions: Necessary...
Page 35 of 47
33
This completes the inductive proof of the inequality ˜TN(D; z) ≤exp(a(D)). Passing to the
limit N →∞, we get ˜T (D; z) ≤exp(a(D)) < ∞for all intervals D ⊂Z. The convergence
extends to all ﬁnite sets because log ˜T (·; z) is subadditive.
⊓⊔
Proof of Theorem 4.5(a) Consider the selection rule s(D) := min D that picks the left-most
point of a ﬁnite set. For α > 0 and L ∈N let
VL(D) :=
{X ⊂Z | X is an L-rod, X ∩D̸ = ∅}

and a(D) ≡aα,L(D) := α VL(D). The choice of α and L is speciﬁed later. For a non-empty
interval D, write x := s(D) = min(D), and D′ := D \ {x}. If D′ is non-empty, then
condition (4.20) reads
∞

ℓ=1
zℓeαℓ≤eα −1.
(4.21)
Indeed in that case for each ℓthere is a single ℓ-rod X that contains x but does not intersect
D′ (note that x + 1 ∈D′ because of the assumption that D is an interval and x = min D).
The rod is simply the ℓ-rod with right-most endpoint x. Moreover VL(D′ ∪X)−VL(D′) = ℓ
and VL(D′ ∪{x}) −VL(D′) = 1.
On the other hand if D′ is empty, then the number of ℓ-rods that contain any given site
x ∈Zd is equal to ℓand the number of L-rods intersecting an ℓ-rod is equal to L + ℓ−1,
therefore condition (4.20) reads instead
∞

ℓ=1
ℓzℓeα(ℓ+L−1) ≤eαL −1.
(4.22)
The proof of Theorem 4.5 is complete once we check the existence of α > 0 and L ∈N such
that the inequalities (4.21) and (4.22) hold true. Set
h(u) := 1 +
∞

ℓ=1
zℓuℓ
(u ∈R+).
Conditions (4.21) and (4.22) are equivalent to
h(eα) ≤eα,
h′(eα) ≤1 −e−αL.
(4.23)
Notice that h is convex and monotone increasing with h(0) = 1. The assumption (4.19)
yields the existence of some u = eα > 0 such that h(u) < u. On the other hand, clearly
h(0) = 1 > 0. Therefore the mean-value theorem yields the existence of a point ˜u ∈(0, u)
such that h(˜u) = ˜u. The point ˜u is necessarily larger then 1 because h(˜u) is. Suppose by
contradiction that h′(˜u) ≥1. Then the convexity of h implies
h(u) ≥h(˜u) + h′(˜u)(u −˜u) ≥h(˜u) + (u −˜u) = u,
which contradicts the assumption h(u) < u. Therefore h(˜u) = ˜u > 1 and h′(˜u) < 1.
Replacing α with ˜α := log ˜u if needed, and picking L = L(α) large enough, we ﬁnd that
(4.23) is satisﬁed for some α > 0. This concludes the proof.
⊓⊔
Proof of Theorem 4.5(b) Let a(D) := log ˜T (D; z) = log T (D; −z). In view of Eq. (2.15)
and the alternating sign property, we have
a(D) =
∞

k=1
1
k!

(Y1,...,Yk)∈Xk
1l{∃i: Yi∩D̸=∅}
ϕT
k(Y1, . . . , Yk)
 z(Y1) · · · z(Yk).
33
Page 36 of 47
S. Jansen, L. Kolesnikov
By Proposition 3.12, for every D ⊂Z \ {1}, we have

Y∋1,
Y∩D=∅
z(X)ea(D∪Y)−a(D) ≤ea(D∪{1})−a(D) −1.
(4.24)
Let us choose D ⊂Z ∩(−∞, 0] with 0 ∈D. Then for every given ℓ∈N, the unique rod of
length ℓthat contains 1 but does not intersect D is the rod {1, . . . , ℓ}, and we obtain
∞

ℓ=1
zℓea(D∪{1,...,ℓ})−a(D) ≤ea(D∪{1})−a(D) −1.
(4.25)
Let D0 := D and for m ≥1 set Dm := D ∪{1, . . . , m}. The exponent on the left-hand side
in (4.25) may be written as
a(D ∪{1, . . . , ℓ}) −a(D) =
ℓ

m=1

a(Dm) −a(Dm−1)

.
(4.26)
Now
a(Dm) −a(Dm−1)
=
∞

k=1
1
k!

(Y1,...,Yk)∈Xk

1l{∃i: Yi∩Dm̸=∅} −1l{∃i: Yi∩Dm−1̸=∅}
	ϕT
k(Y1, . . . , Yk)
z(Y1) · · · z(Yk).
The only clusters (Y1, . . . , Yk) that contribute to the sum are those that intersect Dm but do
not intersect Dm−1. This is only possible if one of the Yi’s contains m and all of them are
contained in Z ∩[m, ∞). Thus
a(Dm) −a(Dm−1)
=
∞

k=1
1
k!

(Y1,...,Yk)∈Xk
1l{∃i: Yi∋m}1l{∀i: Yi⊂[m,∞)}
ϕT
k(Y1, . . . , Yk)
z(Y1) · · · z(Yk).
Because of the translational invariance, the value of the sum does not depend on m. Thus
a(Dm) −a(Dm−1) = α > 0 for all m ≥1 and some α > 0. Turning back to (4.26), we
obtain
a(D ∪{1, . . . , ℓ}) −a(D) = ℓα
and then (4.25) yields ∞
ℓ=1 zℓexp(αℓ) ≤exp(α) −1.
⊓⊔
4.5 Tonks Gas on R
Next, we want to consider the continuous version of the one-dimensional Tonks gas. Let
(Lℓ)ℓ∈N be sequence of strictly positive numbers and X the space of compact intervals
I ⊂R with lengths |I| ∈{Lℓ| ℓ∈N}. The map R × N, (x, ℓ) →[x −Lℓ/2, x + Lℓ/2] is
a bijection between R × N and X. The reference measure λ is deﬁned by the equality

X
h(X)λ(dX) =
∞

ℓ=1
 ∞
−∞
h

x −Lℓ
2 , x + Lℓ
2

dx
Cluster Expansions: Necessary...
Page 37 of 47
33
for all non-negative measurable functions h : X →R+. We assume that the activity is of the
form
z(X) =

zℓ,
X = [x, x + Lℓ] for some ℓ∈N, x ∈R,
0,
else
for some sequence (zℓ)ℓ∈N of non-negative numbers. We assume that rod lengths are bounded
from below, i.e., there exists δ > 0 such that
inf
ℓ∈N Lℓ≥δ.
(4.27)
From here on, we will consider the following chopping map: For X = [x, x + Lℓ] ∈X, let
C(X) = {E1, . . . , Em}consistoftheintersectionsof X withtheintervals[x+(k−1)ε, x+kε)
with k ∈Z, where ε ∈(0, δ). The space of snippets Eε consists of intervals [a, b] and [a, b)
of length b −a ≤ε.
Theorem 4.7 In the setup of multi-type Tonks gas on R, under the assumption (4.27):
(a) Suppose there exists α > 0 such that
∞

ℓ=1
eαLℓzℓ< α.
(4.28)
Then the expansion for T (D; z) is absolutely convergent, for all bounded sets D ⊂R.
(b) Conversely, if T (D; z) is absolutely convergent for all bounded subsets D ⊂R, then
there exists α > 0 such that (4.28) holds true with “≤” instead of “<”.
Remark 4.5 The theorem essentially recovers the necessary and sufﬁcient convergence cri-
terion from [13] (derived there for the activity expansion of the pressure in the system).
The sufﬁcient condition in [13] is (4.28) with “≤” instead of “<”. Again, while the result
itself is not novel, its proof demonstrates the potential of our approach to go beyond the
Fernández-Procacci criterion—also in continuous setups.
First we prove an auxiliary result, the analogue of Proposition 4.6 for the continuous
setup, which is not quite as trivial. We introduce the following notion: Deﬁne the ε-gap-ﬁlling
operation · by setting D := D∪{x ∈R| ∃y, z ∈D with y < x < z such that z −y ≤ε} for
any D ⊂R. Let P be some subset of the power set of R, we say that a function ξ : P →R
does not see gaps of diameter at most ε if it is invariant under the ε-gap-ﬁlling operation, i.e.,
if ξ(D) = ξ(D) for all D ∈P.
Proposition 4.8 Suppose that there exists a non-negative, measurable map a(·) deﬁned on
ﬁnite unions of (bounded) intervals which does not see gaps of diameter at most ε and
satisﬁes the following system of inequalities: For any (bounded) interval D with C(D) =
{E1, . . . , En}, E1, . . . , En ∈Eε, where the chopping map C is deﬁned as above, there is a
subinterval Es ⊂D of length at most ε, such that
∞

k=1
1
k!

Xk I(Es; D′; Y1, . . . , Yk)ea(D′∪Y1∪···∪Yk)−a(D′)λk
z(dY) ≤ea(Es∪D′)−a(D′) −1,
(4.29)
where we set D′ := D\Es and I(Es; D′; Y1, . . . , Yk) is the indicator from Eq. (2.16). Then
T (D; z) is absolutely convergent for all bounded subsets D ⊂R.
33 Page 38 of 47 S. Jansen, L. Kolesnikov

Proof We can modify the Kirkwood-Salsburg-type equations k? from Chapter 3.3 as follows:
If &(-) is a function from D, to R, that does not see gaps of diameter at most ¢ and satisfies the
measurability assumption from Theorem 2.6, define the function Hk (possibly assuming
the value “‘oo”’) by

(#28)(D) = ns2)6( ES U...U Ey )

for D € Dy with E,,..., E, C E, and C(D) = {E),..., Ey}, where Dis given by “filling
gaps” of diameter at most ¢ in D C R as defined above.

Notice that for any such function &(-) (that does not see gaps of diameter at most ¢ and
satisfies the measurability assumption from Theorem 2.6)

Hs Ea RE
holds, where «3& is the function defined by (3.9). In particular, the left hand side of the
equation is well-defined. Since the functions Ty(-3z), N € N, and T(-; z) do not see gaps

of diameter at most ¢ (by our assumption ¢ < 6 and the respective definitions), Proposition
3.10 implies

F(s2) =e + #72.
and
Tw4i(-sz) = eC) + (4 T)(-3 2).

Assumption (4.29) is equivalent to e(D) + (#3 e")(D) < et) for any interval D C R. We
prove by induction over N that Ty(D; z) < e@) for all N € N and all intervals D C R.
For N = 1, we have by our assumption

T\(D, z) = e(D) < e(D) + (#2 e")(D) < e@)

for all intervals D C R. Next, assume for some N € N that Ty(D; z) < e@) for all intervals
DCR, then

Ty41(D; 2) = e(D) + X Ty (D; 2) < e(D) + (He (D) < &™,

where the first inequality holds by the inductive hypothesis, by monotonicity of HS on non-
negative functions and by the observation that for intervals D C R all the arguments of &
appearing in the definition of (#8 &)(D) are again intervals.

This completes the induction and proves Ty (D; z) < e“() for all N € N and all intervals
D CR. Taking the limit N — 00 yields the corresponding bound for T (D; z). The claim for
arbitrary bounded subsets follows since every bounded subset is contained in some compact
interval and

T (Di; 2) < T(D2, 2)
for Dj} C D2 CR. o

Proof of Theorem 4.7(a) In analogy to the discrete case, fora > 0 and L > 0 let

oo
Vi(D) =| Mte,x+LInDZey ax.
=

D Springer
Cluster Expansions: Necessary...
Page 39 of 47
33
and a(D) ≡aα,L(D) := α VL(D). The choice of α and L is speciﬁed later in the proof. We
apply Proposition 4.8 with the choice of the chopping map introduced at the beginning of
this subsection and the selection rule s that picks the leftmost snippet.
Remember the indicator I(E1; D′; Y1, . . . , Yk) from Eq. (2.16). We show that there exists
α > 0 such that
∞

k=1
1
k!

Xk I(E1; D′; Y1, . . . , Yk)eα[VL(D′∪Y1∪···∪Yk)−VL(D′)]λk
z(dY)
≤eαVL(D′∪E1)−VL(D′) −1
(4.30)
for all intervals D′ = [a, b) ⊂R or D′ = [a, b], including the empty set D′ = ∅, and all
snippets E1 = [(k −1)ε, a) ∈Eε.
If D′ is non-empty, then because of infℓ∈N Lℓ≥ε and |E1| ≤ε there cannot be two
or more disjoint rods in X that intersect E1 but do not intersect D′, so the inequality to be
proven reduces to

X
eα(VL(D′∪Y)−VL(D′))1{Y∩E1̸=∅, Y∩D′=∅}λz(dY) ≤eα(VL(D′∪E1)−VL(D′)) −1. (4.31)
Assuming that L ≥ε, this is equivalent to
∞

ℓ=1
zℓ
 |E1|
0
eα(Lℓ+x)dx ≤eα|E1| −1.
(4.32)
The integral on the left-hand side is equal to exp(αLℓ)[exp(α|E1|) −1]/α, so we ﬁnd
that (4.30) is equivalent to
∞

ℓ=1
zℓeαLℓ≤α,
which holds true because of the assumption (4.28).
If D′ is empty, we note that there can be at most two disjoint rods in X that intersect the
snippet E1, hence (4.30) becomes

X
eαVL(Y)1l{Y∩E1̸=∅}λz(dY) + 1
2

X2 eαVL(Y1∪Y2)1l{Y1∩E1̸=∅, Y2∩E1̸=∅, Y1∩Y2=∅}λ2
z

d(Y1, Y2)

≤eαVL(E1) −1.
(4.33)
The right-hand side is equal to exp(α(L + |E1|)) −1. The ﬁrst term on the left-hand side is
equal to
∞

ℓ=1
zℓ(Lℓ+ |E1|)eα(L+Lℓ) =
∞

ℓ=1
zℓLℓeα(L+Lℓ) + O(ε).
The second term on the left-hand side of (4.33) is equal to
∞

ℓ,r=1
zℓzr

E2
1
1l{x<y} eαVL([x−Lℓ,y+Lr])dxdy
which is bounded by
 ∞

ℓ=1
zℓeαLℓ
	2
eα(ε+L)|E1|2 = O(ε2).
33
Page 40 of 47
S. Jansen, L. Kolesnikov
For the inequality (4.33) to be satisﬁed, it is sufﬁcient that
∞

ℓ=1
LℓzℓeαLℓ+ O(ε) ≤eα|E1| −e−αL.
(4.34)
Arguments similar to the proof of Theorem 4.5(b), applied to the convex function h : R+ →
R, h(u) := 1 + ∞
ℓ=1 zℓuLℓ, show that under condition (4.28) there exists α > 0 such that
not only condition (4.28) holds true but in addition
h′(eα) =
∞

ℓ=1
LℓzℓeαLℓ< 1.
Thus one can choose L = L(α) large enough and ε small enough so that (4.34) and
hence (4.33) hold true.
⊓⊔
Proof of Theorem 4.7(b) We proceed as in the proof of Theorem 4.5(b). Suppose that the
expansions are absolutely convergent and deﬁne
a(D) := log T (D; −z) =
∞

k=1
1
k!

Xk 1l{∃i∈[n]: Yi∩D̸=∅}
ϕT
k(Y1, . . . , Yk)
 λk
z(dY).
Then by Proposition 3.13 and since infℓ∈N Lℓis bounded from below by ε > 0,

X
1l{X∩E1̸=∅, X∩D′=∅} ea(D′∪X)−a(D′)λz(dX) ≤ea(D′∪E1)−a(D′) −1
(4.35)
for example for E1 = [0, ε) and D′ = [ε, ε + L] with L > 0 and ε sufﬁciently small.
Before we evaluate the two sides of the inequality, we note two useful properties of a(·).
First, the map a does not see gaps of diameter at most ε. Precisely, if X = [x −Lℓ, x] with
x ∈[0, ε) and D′ is as above, then
a(D′ ∪X) = a([x −Lℓ, ε + L]).
Indeed, any rod Yi ∈X that intersects [0, ε) must also intersect D′ ∪X because it has a
length |Yi| ≥ε. Second, because of translational invariance, the weight a(D) of a non-empty
interval depends only on its length |D|. We check that in addition, it is an afﬁne function of
the length. For x ∈R, deﬁne
α(x) :=
∞

ℓ=1
zℓ
∞

k=0
1
k!

Xk 1l{∀i∈[k]: Yi⊂(−∞,x]}
ϕT
1+k(Y1, . . . , Yk, [x −Lℓ, x])
 λk
z(dY).
The quantity α(x) is best thought of as an integral over clusters in which the right-most
rod [x −Lℓ, x] has its right end pinned at x. By translational invariance, α(x) is actually
independent of x and we may write α(x) ≡α for some scalar α ≥0. Now let I = [a, b] and
J = [b, c] with a < b < c. Then
a(I ∪J) −a(J) =
∞

k=1
1
k!

Xk 1l{∃i∈[k]: Yi∩I̸ =∅}1l{∀i∈[k]: Yi∩J=∅}
ϕT
k(Y1, . . . , Yk)
 λk
z(dY).
Any cluster (Y1, . . . , Yk) that intersects I but not J has its right-most end in [a, b), therefore
a(I ∪J) −a(J) =

I
α(x)dx = α |I|.
Cluster Expansions: Necessary...
Page 41 of 47
33
With these two observations, the left-hand side of (4.35) becomes
∞

ℓ=1
zℓ
 ε
0
ea([x−Lℓ,x]∪D′)−a(D′)dx =
∞

ℓ=1
zℓ
 ε
0
eα(x+Lℓ)dx =
∞

ℓ=1
zℓeαLℓ1
α (eαε −1)
while the right-hand side of (4.35) is exp(αε) −1. It follows that
∞

ℓ=1
zℓeαLℓ≤α.
⊓⊔
Funding Open Access funding enabled and organized by Projekt DEAL. The authors did not receive support
from any funding body for the submitted work.
Data Availability Data sharing not applicable to this article as no datasets were generated or analysed during
the current study.
Declarations
Competing Interests The authors have no competing interests to declare that are relevant to the content of
this article.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included in the
article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is
not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder.
To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
