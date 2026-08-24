---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-227-0-ip
section_title: "Ip"
section_number: 0
pages: 163-167
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
A.8.1. Some inhomogeneous equations. — Like in the theory of linear
diﬀerential equations, many interesting examples come in dimension 2; see for
instance example 3.3.2 page 38 , and the more detailed studie s of chapter 2,
paragraph 2.3.1 and chapter 7, section 7.1.
So let a,b∈K ∗ andu∈K. Extensions of Mb := (K, Φb) byMa := (K, Φa)
have form Na,b,u := (K 2, ΦAu) where Au :=
(a u
0 b
)
. An isomorphism of
extensions from Na,b,u to Na,b,v would be a matrix F :=
(1 f
0 1
)
such that
bσf−af =v−u. More generally, the space Ext(Mb,M a) is isomorphic to the
cokernel of theC-linear mapbσ−a fromK to itself. We shall call cohomological
equation the following ﬁrst order inhomogeneous equation:
(A.1) bσf−af =u.
This can be seen as the obstruction to ﬁnding an isomorphism F from A0 to
Au.
158APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
More generally, let L :=a0 +··· +anσn∈D . By vectorializing the corre-
sponding equation we get a system with matrix:
A =







0 1 0 ... 0
0 0 1 ... 0
.
.
. .
.
. .
.
. ... .
.
.
0 0 0 ... 1
−a0/an −a1/an −a2/an −... −an−1/an







.
Actually,M := (K n, ΦA)≃ (D/DL)∨. From corollary A.7.5, we deduce:
CokerL≃ Γ1(M)≃ Ext(1
,M ).
This can be seen as an obstruction to ﬁnding an isomorphism
(In X
0 1
)
from
(A 0
0 1
)
to
(A U
0 1
)
. In fact, an isomorphism
(In X
0 1
)
from
(A U
0 1
)
to
(A V
0 1
)
would correspond to a solution of σX−AX =V−U. Assuming for
instance an = 1 and writing xi the components of X, this gives the equations
σxi− xi = vi−ui (i = 1,...,n − 1) and σxn + a0x1 +··· + an−1xn =
vn−un. From this, one can solve trivially to get an equivalent of U with
components 0,..., 0,u (exercice for the reader). And, if U has this form,
ﬁnding an isomorphism
(In X
0 1
)
from
(A 0
0 1
)
to
(A U
0 1
)
is equivalent
to solving Lx1 = u. Still more generally, it is easy to see that ﬁnding an
isomorphism
(In X
0 Ip
)
from
(A 0
0 B
)
to
(A U
0 B
)
is equivalent to solving
(σX)B−AX = U, and to obtain anew an identiﬁcation of the cokernel of
X↦→(σX)B−AX with Ext
(
(K p, ΦB), (K n, ΦA)
)
.
A.8.2. A homotopy. — The following is intended to be an explanation of
the equivalence of various computations above. Let (K,σ ) be a diﬀerence ﬁeld
with constant ﬁeld C. The σ-diﬀerence operator P :=σn +a1σn−1 +··· +an
gives rise to a C-linear complex K P→K. Writing AP the companion matrix
described in 2.1.2.1, we also have a complex K n ∆→ K n, where we have set
A.8. THE COHOMOLOGICAL EQUATION 159
∆ :=σ−AP . We then have a morphism of complexes:
K P−−−−→K
V


↓ I


↓
K n ∆−−−−→K n
, where V (f) :=





f
σqf
.
.
.
σn−1
q f




 and I(g) :=





0
.
.
.
0
g




.
(The equality ∆ ◦V = I◦P is obvious.) We now introduce the operators
Pi :=σn−i +a1σn−i−1 +··· +an−i (they are related to the Horner scheme for
P ). We then have a morphism of complexes in the opposite direct ion:
K P−−−−→K
π1
↑

 Π
↑


K n ∆−−−−→K n
, where π1



f1
.
.
.
fn


 :=f1 and Π



g1
.
.
.
gn


 :=
n∑
i=1
Pigi.
(Of course, one must check that Π ◦ ∆ = P◦π1.) Clearly ( π1, Π)◦ (V,I ) is
the identity of the ﬁrst complex. We are going to see that ( V,I )◦ (π1, Π) is
homotopic to the identity of the second complex, whence thei r homological
equivalence (see [ 12,§2.4, def. 4,5 and prop. 5]). To that end, we introduce
a backward operator K n ∆ ′
←K n deﬁned by the following relation:
∆′



g1
.
.
.
gn


 :=



g′
1
.
.
.
g′
n


, where g′
i :=
∑
j+k=i−1
σjgk =⇒
{
V◦π1− IdK n = ∆′◦ ∆,
I◦ Π− IdK n = ∆◦ ∆′.
(The computations are mechanical and again left to the reade r.) This implies
that the two complexes are indeed homotopic.
