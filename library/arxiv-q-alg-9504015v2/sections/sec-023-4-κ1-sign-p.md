---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-023-4-κ1-sign-p
section_title: "(κ−1) sign( p"
section_number: 4
pages: 24-28
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
q )
(
|p|
K
)
. (4.20)
This ends the proof of the lemma.
To ﬁnish the proof of Proposition 4.1 we rearrange some phase fact ors of eqs. (4.9) and
(4.12). We substitute a relation
sign
(
˜L
)
= sign (L) +
N∑
j=1
t(j)−1∑
t=1
sign

 p(j)
t
q(j)
t

 (4.21)
into the factor e−i π
4 κ sign( ˜L) of eq. (4.9). Then we calculate the combination of phases coming
from that factor and from eq. (4.12) (we drop the index j):
ˇq( 1
4 −4∗)∑ ¯t
t=1 mt+(2∗− 1
2)∑ ¯t
t=1 sign
(
pt
qt
)
e
−i π
2 κ
∑ ¯t−1
t=1 sign
(
pt
qt
)
(4.22)
= ˇq( 1
4 −4∗)
∑ ¯t
t=1 mt+(2∗− 1
2 ) sign(
p
q ) ˇq(2∗− 1
2 − κK
4 )∑ ¯t−1
t=1 sign
(
pt
qt
)
= ˇq( 1
4 −4∗)
[ ∑ ¯t
t=1 mt−3
∑ ¯t−1
t=1 sign
(
pt
qt
)]
ˇq(2∗− 1
2 ) sign( p
q )
= ˇq( 1
4 −4∗)Φ( U (p,q )) ˇq(2∗− 1
2) sign(
p
q )
We used here eq. (2.7) and the formula
Φ( U (p,q)) =
¯t∑
t=1
mt − 3
¯t−1∑
t=1
sign
(
pt
qt
)
(4.23)
(see [10] and references therein).
A combination of eqs. (4.9), (4.12), (4.21) and (4.22) leads to eq. (4 .8). This concludes
the proof of Proposition 4.1.
As an application of the Proposition 4.1 let us calculate the invariant of a lens space Lp,q.
This manifold is constructed by a U (−p,q) surgery on an unknot in S3. Since
Jα(unknot; k) =
sin
(
π
K α
)
sin
(
π
K
) , (4.24)
23
we can say that Lp,q is constructed by a chain surgery U (−q,−p) = SU (−p,q) applied to an
empty knot, times a factor
√
K
sin( π
K ) . Then we can read the result directly from eq. (4.8) by
setting there N = 1, sign ( L) = 0, α = 1 and
U (−q,−p) =


−q s
−p r

 (4.25)
instead of U (p,q):
Z ′(Lp,q) =
(
|p|
K
)
sign (p) ˇq4∗(p∗(q−r)−Φ( U (−q, −p))) ˇq2∗ ˇq2∗p∗
− ˇq−2∗p∗
ˇq − 1
=
(
|p|
K
)
sign (p) ˇq3s∨(q,p) ˇq2∗ ˇq2∗p∗
− ˇq−2∗p∗
ˇq − 1 (4.26)
=
(
|p|
K
)
sign (p) ˇq3s∨(q,p) (−1)p∗+1 ˇq
p∗
2 − ˇq− p∗
2
ˇq
1
2 − ˇq− 1
2
,
here s∨(q, p) is the “checked” Dedekind sum, that is, its denominator is inverted modulo K
as in eq. (1.13). We used the relation ˇ q2∗
= −ˇq
1
2 in order to derive the last expression in this
equation. Although it might look simpler than the previous one, it obsc ures the fact that
Z ′(Lp,q) ∈ Z Z[ˇq]. Also note that the expression ˇ q
p∗
2 by itself is ambiguous since p∗ is deﬁned
only modulo K.
Comparing the second expression in the r.h.s. of eq. (4.26) with the formula for the trivial
connection contribution to Witten’s invariant of the lens space
Z (tr)(Lp,q; k) = Z(S3; k) sign (p)√
|p|
ˇq3s(p,q) ˇq
p
2 − ˇq− p
2
ˇq
1
2 − ˇq− 1
2
(4.27)
derived in [10] we can easily check the relation (1.20).
The formula (4.8) also allows us to check the Proposition 1.1 for Seifer t manifolds which
are rational homology spheres. Consider an ( N + 1)-component link L in S3 consisting
of N unknots Lj, 1 ≤ j ≤ N simply linked to a single unknot L0. A Seifert manifold
X
(
p1
q1
, . . . , pn
qn
)
is constructed by performing ( pj, qj) surgeries on the components Lj and a
(0, 1) surgery on L0 (see, e.g. [9]). The Jones polynomial of L is known [1] to be equal to
Jβ,α1,...,αN (L; k) = 1
sin
(
π
K
)
∏ N
j=1 sin
(
π
K βαj
)
sinN −1
(
π
K β
) , (4.28)
24
here β is the color of L0 and αj are the colors of Lj. The signature of L is equal to
sign (L) = − sign
( H
P
)
+
N∑
j=1
sign
(
qj
pj
)
(4.29)
Here we introduced notations
P =
N∏
j=1
pj, H = P
N∑
j=1
qj
pj
, (4.30)
so that
⏐
⏐
⏐
⏐
⏐H1
(
X
(
p1
q1
, . . . , pn
qn
)) ⏐
⏐
⏐
⏐
⏐ = |H|. (4.31)
The Proposition 4.1 provides the following expression for the invarian t of the Seifert
manifold X
( p1
q1
, . . . , pn
qn
)
:
Z ′(X; k) = i
2
√
K ei π
4 κ sign( H
P )eiπ 3
4
K−2
K sign( H
P ) ˇq( 1
2 −2∗) sign( H
P )
×
∑ ′
−K≤β ≤K
β ∈2Z Z+1
(ˇq−2∗β − ˇq2∗β)Z ′
β(L(con); k), (4.32)
here
Z ′
β(L(con); K) =

 sin
(
π
K
)
sin
(
π
K β
)


N −1 N∏
j=1
Z ′
β(L−pj,qj ; K), (4.33)
Z ′
β(L−pj,qj ; K) =
(
|qj|
K
)
sign (qj)√
K e
−i π
K κ sign
(
qj
pj
)
e
−iπ 3
4
K−2
K sign
(
qj
pj
)
(4.34)
×ˇq−4∗Φ( U (pj ,q j )) ˇq(2∗− 1
2 ) sign
(
qj
pj
)
×
∑ ′
−K≤α j ≤K
α j ∈2Z Z+1
(1≤j≤N)
sin
(
π
K βαj
)
sin
(
π
K
) ˇq4∗q∗
j (pjα2
j +sj) i
2
(
ˇq−2∗q∗
j αj − ˇq2∗q∗
j αj
)
.
(4.35)
In these formulas Z ′
β(L−pj,qj ; k) is an invariant of the β-colored link L0 inside the lens space
L−pj,qj constructed by the ( pj, qj) surgery on the unknot Lj. Z ′
β(L(con); k) is the invariant of
the β-colored knot L0 inside the connected sum of lens spaces
L(con) = L−p1,q1# · · ·#L−pN ,qN . (4.36)
25
The calculation of invariants Z ′
β(L−pj,qj ; k) runs similar to that of Z ′(Lp,q; k) of eq. (4.26).
The only diﬀerence is that by taking a sum over αj we go from ˜U
(pj ,qj)
αj 1 to ˜U
(−qj ,pj)
β1 rather
than to ˜U
(−qj ,pj)
11 . As a result,
Z ′
β(L−pj ,qj; k) =
(
|pj|
K
)
sign (pj) ˇq4∗p∗
j qj−3s∨(qj,pj) ˇq−4∗p∗
j qjβ2 ˇq−2∗p∗
j β − ˇq2∗p∗
j β
ˇq−2∗
− ˇq2∗ (4.37)
and
Z ′(X; k) = i
2
√
K ei π
4 κ sign( H
P )eiπ 3
4
K−2
K sign( H
P ) ˇq( 1
2 −2∗) sign( H
P ) (4.38)
×
(
|p|
K
)
sign (P ) ˇq4∗P ∗H−3
∑ N
j=1 s∨(qj ,pj)
× 1
ˇq−2∗
− ˇq2∗
∑ ′
−K≤β ≤K
β ∈2Z Z+1
ˇq−4∗P ∗Hβ 2
∏ N
j=1(ˇq−2∗p∗
j β − ˇq2∗p∗
j β)
ˇq−2∗
− ˇq2∗
The preexponential factor of eq. (4.38) can be put in the form
J(β)(ˇq−2∗β − ˇq2∗β), (4.39)
where
J(β) =
∏ N
j=1(ˇq−2∗p∗
j β − ˇq2∗p∗
j β)
(ˇq−2∗
− ˇq2∗
)(ˇq−2∗β − ˇq2∗β)N −1 . (4.40)
It is easy to check that the function J(β) belongs to Z Z[ˇq] and satisﬁes the properties of the
Jones polynomial described in Proposition 1.2. Therefore the full ma chinery of Section 3
could be applied to the sum of eq. (4.38) in order to convert it to the in tegral and ultimately
prove the Proposition 1.1 for Seifert manifolds. However there is an easier way. The numbers
p∗
j , 1 ≤ j ≤ N determine a set of positive integer numbers Λ( p∗
1, . . . , p∗
N ) ∈ I N and multiplicity
factors Cn(p∗
1, . . . , p∗
N ) ∈ Z Z, n ∈ Λ( p∗
1, . . . , p∗
N ) such that
∏ N
j=1(ˇq−2∗p∗
j β − ˇq2∗p∗
j β)
(ˇq−2∗β − ˇq2∗β)N −1 =
∑
n∈Λ( p∗
1,...,p∗
N )
Cn(p∗
1, . . . , p∗
N )(ˇq−2∗nβ − ˇq2∗nβ). (4.41)
Now we can apply eq. (3.5) to the calculation of the sum
1
ˇq−2∗
− ˇq2∗
∑ ′
−K≤β ≤K
β ∈2Z Z+1
ˇq−4∗P ∗Hβ 2
∏ N
j=1(ˇq−2∗p∗
j β − ˇq2∗p∗
j β)
(ˇq−2∗β − ˇq2∗β)N −2 (4.42)
26
= 2
ˇq−2∗
− ˇq2∗
∑
n∈Λ
Cn
∑ ′
−K≤β ≤K
β ∈2Z Z+1
ˇq−4∗P ∗Hβ 2
(ˇq−2∗(n+1)β − ˇq−2∗(n−1)β)
= 2
√
K
( P ∗H
K
)
ei π
