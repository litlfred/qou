---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-014-35-inner-ﬂuctuations-and-bosons
section_title: "Inner ﬂuctuations and bosons"
section_number: 3.5
pages: 22-29
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
Let us show that the inner ﬂuctuations of the metric give rise to the gauge bosons of
the standard model with their correct quantum numbers. We ﬁrst have to compute A =
Σ ai[D, a′
i]
ai, a′
i ∈A. Since D = ∂/M ⊗1 + γ5 ⊗DF decomposes as a sum of two terms, so
does A and we ﬁrst consider the discrete part A(0,1) coming from commutators with γ5 ⊗DF .
3.5.1. The discrete part A(0,1) of the inner ﬂuctuations.
Let x ∈M and let ai(x) = (λi, qi, mi), a′
i(x) = (λ′
i, q′
i, m′
i), the computation of P ai[γ5 ⊗
DF , a′
i] at x on the subspace corresponding to Hf ⊂HF gives γ5 tensored by the matrices
A(0,1)
3
and A(0,1)
1
deﬁned below. We set
A(0,1)
3
=

0
X
X′
0

⊗13 ,
X =
"
Y ∗
(↑3) ϕ1
Y ∗
(↑3) ϕ2
−Y ∗
(↓3) ¯ϕ2
Y ∗
(↓3) ¯ϕ1
#
,
X′ =

Y(↑3) ϕ′
1
Y(↓3) ϕ′
2
−Y(↑3) ¯ϕ′
2
Y(↓3) ¯ϕ′
1

(3.6)
for the H(3)
F
part, with
ϕ1 =
X
λi(α′
i −λ′
i) ,
ϕ2 =
X
λiβ′
i
(3.7)
ϕ′
1 =
X
αi(λ′
i −α′
i) + βi ¯β′
i ,
ϕ′
2 =
X
(−αiβ′
i + βi(¯λ′
i −¯α′
i)),
(3.8)
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
23
where we used the notation
q =

α
β
−¯β
¯α

for quaternions. For the H(1)
F
part one obtains in the same way
A(0,1)
1
=

0
Y
Y ′
0

,
Y =
"
Y ∗
(↑1) ϕ1
Y ∗
(↑1) ϕ2
−Y ∗
(↓1) ¯ϕ2
Y ∗
(↓1) ¯ϕ1
#
,
Y ′ =

Y(↑1) ϕ′
1
Y(↓1) ϕ′
2
−Y(↑1) ¯ϕ′
2
Y(↓1) ¯ϕ′
1

.
(3.9)
Here the ϕ are given as above by (3.7) and (3.8).
The oﬀdiagonal part of DF , which involves YR, does not contribute to the inner ﬂuctuations,
since it exactly commutes with the algebra AF.
Since the action of AF on H ¯f exactly
commutes with DF , it does not contribute to A(0,1). One lets
q = ϕ1 + ϕ2 j ,
q′ = ϕ′
1 + ϕ′
2 j
(3.10)
where j is the quaternion

0
1
−1
0

.
Proposition 3.5. 1) The discrete part A(0,1) of the inner ﬂuctuations of the metric is pa-
rameterized by an arbitrary quaternion valued function
H ∈C∞(M, H) ,
H = ϕ1 + ϕ2 j ,
ϕj ∈C∞(M, C)
2) The role of H in the coupling of the ↑-part is related to its role in the coupling of the ↓-part
by the replacement
H 7→˜H = j H.
Proof. 1) First one checks that there are no linear relations between the four terms (3.7) and
(3.8). We consider a single term a[DF , a′]. Taking a = (λ, 0, 0) and a′ = (λ′, 0, 0) gives
ϕ1 = −λλ′ ,
ϕ2 = ϕ′
1 = ϕ′
2 = 0
Taking a = (λ, 0, 0) and a′ = (0, j ¯β′, 0) gives
ϕ′
1 = λβ′ ,
ϕ1 = ϕ′
1 = ϕ′
2 = 0
Similarly, taking a = (0, α, 0) and a′ = (λ′, 0, 0) gives
ϕ′
1 = αλ′ ,
ϕ1 = ϕ2 = ϕ′
2 = 0
while taking a = (0, j ¯β, 0) and a′ = (λ′, 0, 0) gives
ϕ′
2 = β¯λ′ ,
ϕ1 = ϕ2 = ϕ′
1 = 0.
This shows that the vector space Ω(0,1)
D
of linear combinations P
i ai[DF , a′
i] is the space of
pairs of quaternion valued functions q(x) and q′(x).
The selfadjointness condition A = A∗is equivalent to q′ = q∗and we see that the discrete
part A(0,1) is exactly given by a quaternion valued function, H(x) ∈H on M.
2) The transition is given by (ϕ1, ϕ2) 7→(−¯ϕ2, ¯ϕ1), which corresponds to the multiplication
of H = ϕ1 + ϕ2 j by j on the left.
For later purposes let us compute the trace of powers of (D+A(0,1) +JA(0,1)J). Let us deﬁne
D(0,1) = D + A(0,1) + JA(0,1)J.
(3.11)
24
CHAMSEDDINE, CONNES, AND MARCOLLI
Lemma 3.6. 1) On H(3)
F
⊂HF one has
Tr((D(0,1)
3
)2) = 12 |1 + H|2 Tr(Y ∗
(↑3)Y(↑3) + Y ∗
(↓3)Y(↓3))
(3.12)
Tr((D(0,1)
3
)4) = 12 |1 + H|4 Tr((Y ∗
(↑3)Y(↑3))2 + (Y ∗
(↓3)Y(↓3))2)
2) On H(1)
F
⊂HF one has
Tr((D(0,1)
1
)2) = 4 |1 + H|2 Tr(Y ∗
(↑1)Y(↑1) + Y ∗
(↓1)Y(↓1)) + 2 Tr(Y ∗
RYR)
(3.13)
Tr((D(0,1)
1
)4) = 4 |1 + H|4 Tr((Y ∗
(↑1)Y(↑1))2 + (Y ∗
(↓1)Y(↓1))2) + 2 Tr((Y ∗
RYR)2)
+ 8 |1 + H|2 Tr(Y ∗
RYRY ∗
(↑1)Y(↑1))
Proof. 1) The left hand side of (3.13) is given by 2 Tr((A(0,1)
3
)2), after replacing H by 1 + H
to take into account the operator D3. The product X X∗is given by the diagonal matrix
X X∗=
"
Y ∗
(↑3)Y(↑3) (ϕ1 ¯ϕ1 + ϕ2 ¯ϕ2)
0
0
Y ∗
(↓3)Y(↓3) (ϕ1 ¯ϕ1 + ϕ2 ¯ϕ2)
#
= |H|2
"
Y ∗
(↑3)Y(↑3)
0
0
Y ∗
(↓3)Y(↓3)
#
One has Tr((A(0,1)
3
)2) = 3 Tr(X X∗+ X∗X) = 6 Tr(X X∗).
This gives the ﬁrst equality.
Similarly, one has Tr((A(0,1)
3
)4) = 3 Tr((X X∗)2 + (X∗X)2) = 6 Tr((X X∗)2), which gives the
second identity.
2) Let us write the matrix of (D + A(0,1) + JA(0,1)J)1 in the decomposition (↑R, ↓R, ↑L, ↓L
, ¯↑R, ¯↓R, ¯↑L, ¯↓L). We have


0
0
Y ∗
(↑1) ϕ1
Y ∗
(↑1) ϕ2
Y ∗
R
0
0
0
0
0
−Y ∗
(↓1) ¯ϕ2
Y ∗
(↓1) ¯ϕ1
0
0
0
0
Y(↑1) ¯ϕ1
−Y(↓1) ϕ2
0
0
0
0
0
0
Y(↑1) ¯ϕ2
Y(↓1) ϕ1
0
0
0
0
0
0
YR
0
0
0
0
0
¯Y ∗
(↑1) ¯ϕ1
¯Y ∗
(↑1) ¯ϕ2
0
0
0
0
0
0
−¯Y ∗
(↓1)ϕ2
¯Y ∗
(↓1)ϕ1
0
0
0
0
¯Y(↑1)ϕ1
−¯Y(↓1) ¯ϕ2
0
0
0
0
0
0
¯Y(↑1)ϕ2
¯Y(↓1) ¯ϕ1
0
0


The only matrix elements of the square of (D + A(0,1) + JA(0,1)J)1 involving YR or Y ∗
R are


Y ∗
RYR + Y ∗
(↑1)Y(↑1)|H|2
0
0
0
0
0
Y ∗
R ¯Y ∗
(↑1) ¯ϕ1
Y ∗
R ¯Y ∗
(↑1) ¯ϕ2
0
0
0
0
0
0
0
0
0
0
0
0
Y(↑1)Y ∗
R ¯ϕ1
0
0
0
0
0
0
0
Y(↑1)Y ∗
R ¯ϕ2
0
0
0
0
0
YRY ∗
(↑1) ϕ1
YRY ∗
(↑1) ϕ2
¯Y ∗
(↑1) ¯Y(↑1)|H|2 + YRY ∗
R
0
0
0
0
0
0
0
0
0
0
0
¯Y(↑1)YRϕ1
0
0
0
0
0
0
0
¯Y(↑1)YRϕ2
0
0
0
0
0
0
0


This shows that one only gets two additional terms involving YR for Tr((D + A(0,1) +
JA(0,1)J)2
1) and each gives Tr(YRY ∗
R). The trace Tr((D + A(0,1) + JA(0,1)J)4
1) is the Hilbert-
Schmidt norm square of (D+A(0,1) +JA(0,1)J)2
1 and we just need to add to the terms coming
from the same computation as (3.12) the contribution of the terms involving YR. The term
Y ∗
RYR+Y ∗
(↑1)Y(↑1)|H|2 contributes (after replacing H 7→1+H) by 2|1+H|2 Tr(Y ∗
RYRY ∗
(↑1)Y(↑1))
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
25
and Tr((Y ∗
RYR)2). The term ¯Y ∗
(↑1) ¯Y(↑1)|H|2 +YRY ∗
R gives a similar contribution. All the other
terms give simple additive contributions. One gets the result using
Tr(¯Y(↑1)YRY ∗
R ¯Y ∗
(↑1)) = Tr(Y ∗
RYRY ∗
(↑1)Y(↑1))
which follows using complex conjugation from the symmetry of YR i.e. ¯YR = Y ∗
R.
Thus, we obtain for the trace of powers of D(0,1) the formulae
Tr((D(0,1))2) = 4 a |1 + H|2 + 2 c
(3.14)
and
Tr((D(0,1))4) = 4 b |1 + H|4 + 2 d + 8 e |1 + H|2 ,
(3.15)
where
a
=
Tr(Y ∗
(↑1)Y(↑1) + Y ∗
(↓1)Y(↓1) + 3(Y ∗
(↑3)Y(↑3) + Y ∗
(↓3)Y(↓3)))
(3.16)
b
=
Tr((Y ∗
(↑1)Y(↑1))2 + (Y ∗
(↓1)Y(↓1))2 + 3(Y ∗
(↑3)Y(↑3))2 + 3(Y ∗
(↓3)Y(↓3))2)
c
=
Tr(Y ∗
RYR)
d
=
Tr((Y ∗
RYR)2)
e
=
Tr(Y ∗
RYRY ∗
(↑1)Y(↑1)).
Remark 3.7. The coeﬃcients in (3.16) appear in the physics literature in the renormal-
ization group equation for the Yukawa parameters.
For instance, one can recognize the
coeﬃcients a and b respectively as the Y2(S) and H(S) of [1].
3.5.2. The vector part A(1,0) of inner ﬂuctuations.
Let us now determine the other part A(1,0) of A, i.e.
A(1,0) =
X
ai[(∂/M ⊗1), a′
i] .
(3.17)
We let ai = (λi, qi, mi), a′
i = (λ′
i, q′
i, m′
i) be elements of A = C∞(M, AF ). We obtain the
following.
1. A U(1) gauge ﬁeld
Λ =
X
λi dλ′
i
(3.18)
2. An SU(2) gauge ﬁeld
Q =
X
qi dq′
i
(3.19)
3. A U(3) gauge ﬁeld
V ′ =
X
mi dm′
i.
(3.20)
For 1) notice that we have two expressions to compute since there are two diﬀerent actions
of λ(x) in L2(M, S) given respectively by
ξ(x) 7→λ(x) ξ(x) ,
ξ(x) 7→¯λ(x) ξ(x).
For the ﬁrst one, using (3.2), the expression Λ = P λj[(∂/M ⊗1), λ′
j] is of the form
Λ =
√
−1
X
λj∂µλ′
jγµ = Λµ γµ
26
CHAMSEDDINE, CONNES, AND MARCOLLI
and it is self-adjoint when the scalar functions
Λµ =
√
−1
X
λj∂µλ′
j
are real valued. It follows then that the second one is given by
X ¯λj[(∂/M ⊗1), ¯λ′
j] =
√
−1
X ¯λj∂µ¯λ′
jγµ = −Λµ γµ.
Thus, we see that, even though we have two representations of the λ(x), these generate only
one U(1) gauge potential. We use the notation
Λµ = g1
2 Bµ
(3.21)
for this U(1) gauge potential, which will play the role of the generator of hypercharge (not
to be confused with the electromagnetic vector potential).
For 2) notice that the action of quaternions H can be represented in the form
q = f0 +
X
i fα σα ,
f0 , fα ∈C∞(M, R)
where σα are the Pauli matrices
σ1 =

0
1
1
0

,
σ2 =

0
−i
i
0

,
σ3 =

1
0
0
−1

.
(3.22)
The Pauli matrices are self-adjoint. Thus the terms of the form
f0 [(∂/M ⊗1), i f ′
α σα]
are self-adjoint. The algebra of quaternions admits the basis (1, iσα). Thus, since the elements
of this basis commute with ∂/M, one can rewrite
X
qi[(∂/M ⊗1), q′
i] =
X
f0 [(∂/M ⊗1), f ′
0] +
X
fα [(∂/M ⊗1), i f ′
α σα],
where all f and f ′ are real valued functions. Thus, the self-adjoint part of this expression is
given by
Q =
X
fα [(∂/M ⊗1), i f ′
α σα],
which is an SU(2) gauge ﬁeld. We write it in the form
Q = Qµ γµ ,
Qµ = g2
2 W α
µ σα.
(3.23)
Using (3.2), we see that its eﬀect is to generate the covariant derivatives
∂µ −i
2 g2 W α
µ σα.
(3.24)
For 3), this follows as a special case of the computation of the expressions of the form
A =
X
ai[(∂/M ⊗1), a′
i] ,
ai , a′
i ∈C∞(M, MN(C)).
One obtains Cliﬀord multiplication by all matrix valued 1-forms on M in this manner. The
self-adjointness condition A = A∗then reduces them to take values in the Lie algebra of
U(N) through the identiﬁcations A = i H and
Lie(U(N)) = {H ∈MN(C) , H∗= −H} .
We now explain how to reduce V ′ to the Lie subalgebra SU(3) of U(3). We consider the
following analogue of Deﬁnition 2.13 of the unimodular subgroup SU(AF ).
Deﬁnition 3.8. A gauge potential A is “unimodular” iﬀTr(A) = 0.
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
27
We can now parameterize the unimodular gauge potentials and their adjoint action, i.e. the
combination A + J A J−1.
Proposition 3.9.
1. The unimodular gauge potentials are parameterized by a U(1) gauge
ﬁeld B, an SU(2) gauge ﬁeld W and an SU(3) gauge ﬁeld V .
2. The adjoint action A + J A J−1 on Hf is obtained by replacing ∂µ by ∂µ + Aµ where
Aµ = (Aq
µ ⊕Aℓ
µ) ⊗13 (where the 13 is for the three generations), and
Aq
µ =


−2i
3 g1Bµ ⊗13
0
0
0
i
3g1Bµ ⊗13
0
0
0
(−i
2g2W α
µ σα −i
6g1Bµ ⊗12) ⊗13


+ 14 ⊗

−i
2g3V i
µλi

,
Aℓ
µ =


0
0
0
0
i g1Bµ
0
0
0
(−i
2g2W α
µ σα + i
2g1Bµ ⊗12)

.
Here the σα are the Pauli matrices (3.22) and λi are the Gell-mann matrices
λ1 =


0
1
0
1
0
0
0
0
0

, λ2 =


0
i
0
−i
0
0
0
0
0

, λ3 =


1
0
0
0
−1
0
0
0
0

, λ4 =


0
0
1
0
0
0
1
0
0


(3.25)
λ5 =


0
0
−i
0
0
0
i
0
0

, λ6 =


0
0
0
0
0
1
0
1
0

, λ7 =


0
0
0
0
0
−i
0
i
0

, λ8 =
1
√
3


1
0
0
0
1
0
0
0
−2


which are self-adjoint and satisfy the relation
Tr(λiλj) = 2δij .
(3.26)
Proof. 1) The action of A on the subspace Hf is of the form


Λ
0
0
0
0
−Λ
0
0
0
0
Q11
Q12
0
0
Q21
Q22


on leptons and quarks. Thus, it is traceless, since Q is traceless as a linear combination of
the Pauli matrices. The action of A on the subspace H ¯f is given by Λ on the subspace of
leptons and by V ′ on the space of quarks. One has 4 leptons and 4 quarks per generation
(because of the two possible chiralities) and the color index is taken care of by V ′. Thus, the
unimodularity condition means that we have
3 · 4 · (Λ + Tr(V ′)) = 0.
Thus, we can write V ′ as a sum of the form
V ′ = −V −1
3


Λ
0
0
0
Λ
0
0
0
Λ

= −V −1
3 Λ 13,
(3.27)
where V is traceless, i.e. it is an SU(3) gauge potential.
2) Since the charge conjugation antilinear operator JM commutes with ∂/M, it anticommutes
with the γµ and the conjugation by J introduces an additional minus sign in the gauge
28
CHAMSEDDINE, CONNES, AND MARCOLLI
potentials. The computation of A + J A J−1 gives, on quarks and leptons respectively, the
matrices


Λ −V ′
0
0
0
0
−Λ −V ′
0
0
0
0
Q11 −V ′
Q12
0
0
Q21
Q22 −V ′




0
0
0
0
0
−2Λ
0
0
0
0
Q11 −Λ
Q12
0
0
Q21
Q22 −Λ


Thus, using (3.27), we obtain for the (1, 0)-part of the inner ﬂuctuation A + J A J−1 of the
metric the matrices


4
3 Λ + V
0
0
0
0
−2
3 Λ + V
0
0
0
0
Q11 + 1
3 Λ + V
Q12
0
0
Q21
Q22 + 1
3 Λ + V




0
0
0
0
0
−2Λ
0
0
0
0
Q11 −Λ
Q12
0
0
Q21
Q22 −Λ


This completes the proof.
Remark 3.10. Thus, we have obtained exactly the gauge bosons of the standard model,
coupled with the correct hypercharges YL, YR. They are such that the electromagnetic charge
Qem is determined by 2 Qem = YR for right handed particles. One also has 2 Qem = YL +2 I3,
where I3 is the third generator of the weak isospin group SU(2). For Qem one gets the same
answer for the left and right components of each particle and 2
3, −1
3 for the u, d quarks,
respectively, and 0 and −1 for the ν and the e leptons, respectively.
3.5.3. Independence.
It remains to explain why the ﬁelds H = ϕ1 + j ϕ2 of Proposition 3.5 and B, W, V of Propo-
sition 3.9 are independent of each other.
Proposition 3.11. The unimodular inner ﬂuctuations of the metric are parameterized by
independent ﬁelds ϕ1, ϕ2, B, W, V , as in Propositions 3.5 and 3.9.
Proof. Let Z be the real vector bundle over M, with ﬁber at x
C ⊕C ⊕T ∗
xM ⊕T ∗
xM ⊗Lie(SU(2)) ⊕T ∗
xM ⊗Lie(SU(3)).
By construction the inner ﬂuctuations are sections of the bundle Z.
The space of sections S obtained from inner ﬂuctuations is in fact not just a linear space over
R, but also a module over the algebra C∞(M, R) which is the real part of C∞(M, AF ) (Lemma
3.2). Indeed, the inner ﬂuctuations are obtained as expressions of the form A = P aj [D, a′
j].
One has to check that left multiplication by f ∈C∞(M, R) does not alter the self-adjointness
condition A = A∗. This follows from Proposition 3.1, since we are replacing aj by faj, where
f commutes with A and is real so that f = f ∗.
To show that S = C∞(M, Z) it is enough to know that one can ﬁnd sections in S that span
the full vector space Zx at any given point x ∈M. Then C∞(M, R)-linearity shows that the
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
29
same sections continue to span the nearby ﬁbers. Using a partition of unity one can then
express any global section of Z as an element of S.
Choose ﬁrst the elements ai(y) = (λi, qi, mi), a′
i(y) = (λ′
i, q′
i, m′
i) independent of y ∈N(x)
in a neighborhood of x. Using Proposition 3.5, one knows that H(x) can be an arbitrary
element of H, while B(x), W(x), V (x) all vanish because they are diﬀerential expressions of
the a′
i.
The independence of λ, q and m in the formulae (3.18), (3.19), (3.20) implies that one can
construct arbitrary B(x), W(x), V (x) in the form P
i ai[D, a′
i]. These, however, will not
suﬃce to give an arbitary value for ϕ1 and ϕ2, but this can be corrected by adding an
element of the form described above, with vanishing B, W, and V .
