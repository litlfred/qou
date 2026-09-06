---
doc_id: arxiv-math-0505056v2
doc_title: "Matrix factorizations and link homology II"
section_id: sec-001-proofs
section_title: "Proofs"
section_number: null
pages: 12-37
source_pdf: 0505056v2.pdf
source_sha256: 1b6580406c3d35b5
doc_brief: "Matrix factorizations and link homology II — To a presentation of an oriented link as the closure of a braid we assign a complex of bigraded vector spaces."
---
1. Product factorizations, graph homology and Koszul compl exes.
Given a polynomial ring R and a pair of elements a1,b 1 ∈R, we denote
by (a1,b 1) the factorization
R
a1
− →R
b1
− →R.
12
Given a ﬁnite set of such pairs ( ai,bi), 1 ≤ i ≤ n, we denote by ( a, b) their
tensor product (over R):
(a, b)
def
= ⊗i(ai,bi), a = (a1,...,a n), b = (b1,...,b n).
We will also write ( a, b) in the column form


a1 b1
a2 b2
... ...
an bn


and call it a Koszul factorization. By an elementary transformatio n of rows
i and j we mean a modiﬁcation
(
ai bi
aj bj
)
[ij]λ
− − →
(
ai bi +λbj
aj −λai bj
)
for some λ ∈ R. We denote it by [ ij]λ. All other rows of ( a, b) are left
unchanged. An elementary transformation takes a Koszul facto rization (a, b)
to an isomorphic factorization, since we’re only changing a basis vect or in
the free R-module underlying the factorization ( a, b).
Suppose now that y is one of the generators of the polynomial ring R, so
we can write R =R′[y], and that the potential w = ∑ aibi lies in R′ (in this
situation we say that y is an internal variable). Then any factorization M
overR restricts to (an inﬁnite rank) factorization over R′, which we denote
M ′. Assume furthermore that one of the rows in ( a, b) has the form (0,y −µ)
whereµ ∈R′. Denote by (a′, b′) the factorization overR′ obtained from (a, b)
by removing the row (0,y −µ) and substituting µ fory everywhere in all other
rows.
Proposition 3 Factorizations (a′, b′) and (a, b)′ are chain homotopy equiv-
alent.
Proof: By changing a variable y → y −µ we reduce to the case µ = 0.
We can write ai = a′
i +ya′′
i and bi = b′
i +yb′′
i where a′
i,b ′
i ∈ R′. Applying
elementary transformations to rows (0 ,y ) and (ai,bi) we reduce the latter to
(ai,b ′
i), while (0,y ) is transformed into ( ∑ aib′′
i,y ). Next, change ( ∑ aib′′
i,y )
into (y, ∑ aib′′
i ) (this shifts factorization M to M⟨1⟩) and apply elementary
transformations to rows ( ai,b ′
i) and ( y, ∑ aib′′
i ). The row ( ai,b ′
i) becomes
(a′
i,b ′
i), while the row with y turns into (y, ∑ (aib′′
i +a′′
ib′
i)). Since the potential
does not depend on y, the latter sum is zero. Now shift ( y, 0) back to (0 ,y ).
13
The result is the Koszul factorization, isomorphic to ( a, b), with rows (a′
i,b ′
i)
and (0,y ). This factorization is the tensor product of ( a′, b′), as deﬁned above,
and (0,y ). Therefore, ( a, b) is isomorphic, as an R-factorization, to the total
factorization of the bifactorization
(a′, b′) ⊗R′R′[y]
0
− →(a′, b′) ⊗R′ R′[y]
y
− →(a′, b′) ⊗R′ R′[y].
As a factorization over the smaller ring R′, it decomposes into a direct sum
of contractible factorizations which are the total factorizations of
(a′, b′) ⊗yj+1 0
− →(a′, b′) ⊗yj y
− →(a′, b′) ⊗yj+1,
for j ≥ 0, and the factorization ( a′, b′). Proposition follows. □
Remark: The second half of the above proof just says that the complex
of R′-modules
0 − →R′[y]
y
− →R′[y] − →0
is the direct sum of contractible complexes
0 − →R′yj y
− →R′yj+1 − →0
and the complex 0 − →R′ − →0.
Suppose we are given a planar marked graph Γ , possibly with boundary.
To Γ we assigned a Koszul factorization C(Γ) which has a rather special
form. Each arc in Γ contributes the row ( a,xi −xj) to the Koszul matrix of
C(Γ), where xi and xj are the labels at the endpoints of the arc. Each wide
edge in Γ contributes two rows
(
a xi +xj −xk −xl
0 xixj −xkxl
)
to the Koszul matrix, where xi,xj, xk,xl are the labels bounding the edge.
If Γ has m1 arcs and m2 wide edges, the Koszul matrix of C(Γ) will have
n = m1 + 2m2 rows. Permute these rows so that the ﬁrst m1 +m2 rows
have the form (a,z ) where z’s are some linear functions of xi’s. We call these
rows linear rows. The last m2 rows have the form (0,xixj −xkxl) for various
quadruples of indices ( i,j,k,l ). Call these quadratic rows.
Apply elementary transformations with λ = 1 to the ﬁrst row paired with
every other linear row. In other words, we convert b1 tob1 +b2 + · · ·+bm1+m2
and subtract a1 = a from ap = a for p = 2, 3,...,m 1 +m2. The Koszul
matrix transforms into a matrix with the ﬁrst row ( a, ∑ ǫixi) where the sum
is over all boundary points of Γ and ǫi = ±1 depending on the orientation of
Γ at that point. All other linear rows acquire the form (0 ,z ), with the same
14
linear functions z as before. Nothing happens to the quadratic rows. The
Koszul matrix now has the form

a b 1
0 b2
· · · · · ·
0 bn


with b1 = ∑ ǫixi. After this change of basis, every row but the ﬁrst one has
the ﬁrst term zero. Hence, it comes from a one-term Koszul comp lex
0 − →R
bp
− →R − →0
by collapsing cohomological grading from Z to Z2. Likewise, the tensor prod-
uct of all rows save the ﬁrst is a factorization obtained from the Ko szul
complex of the sequence ( b2,b 3,...,b n) by collapsing the grading.
Note that our polynomial ring is, in addition, bigraded. Taking all grad -
ings into account, the collapse is from a triple grading to a bigrading (s ee
ﬁgure 3). No cyclic components appear in the collapsed grading since the dif-
ferential has nonzero bidegree (1 , 1). Finally, observe that in the new Koszul
matrix parameter a appears only once, in the ﬁrst row.
Next consider the case when Γ is closed (has no boundary points). T he
ﬁrst row becomes ( a 0) and the whole factorization comes from the Koszul
complex of the sequence ( a,b 2,...,b n). by collapsing its grading. Moreover,
a plays a purely decorative role, and, using proposition 3, we can thro w out
this row simultaneously with removing a from the list of variables, which
would then have only xi’s. In other words, the cohomology H(Γ) of the
factorizationC(Γ) is isomorphic to the cohomology of the Koszul complex of
the sequence (b2,b 3,...,b n), with the trigrading collapsed to a bigrading.
Thus, although the 2-periodic complex C(Γ) as well as its cohomology
H(Γ) are Q[a]-modules, a acts trivially on H(Γ).
2. Maps χ0,χ 1 revisited.
Recall the row operation [ ij]λ on a Koszul matrix of a factorization:
( ai bi
aj bj
)
− →
( ai bi +λbj
aj −λai bj
)
Denote by |0⟩ and |1⟩ the standard basis vectors in factorizations ( ai,bi) and
(aj,bj):
R|0⟩
ai
− →R|1⟩
bi
− →R|0⟩,
R|0⟩
aj
− →R|1⟩
bj
− →R|0⟩.
15
Let |00⟩, |01⟩, |10⟩, |11⟩ be the standard basis vectors in the tensor product
factorization (ai,bi) ⊗ (aj,bj). The row operation [ ij]λ corresponds to the
isomorphism of factorizations
(ai,bi) ⊗ (aj,bj) ∼= (ai,bi +λbj) ⊗ (aj −λai,bj)
which takes the standard basis of the LHS factorization to the bas is
|00⟩, |01⟩, |10> +λ|01⟩, |11⟩
of the RHS tensor product.
Denote by ψ(y) the following morphism between two Koszul factoriza-
tions:
R
x
− − − →R
yz
− − − →R
1
↓ y
↓ 1
↓
R
xy
− − − →R
z
− − − →R
Lemma 1 The following squares are commutative:
( a1 b1
a2 b2c2
)
Id⊗ψ (c2)
− − − − − →
( a1 b1
a2c2 b2
)
[12]λ
↓ [12]λc 2
↓
( a1 b1 +λb2c2
a2 −λa1 b2c2
)
Id⊗ψ (c2)
− − − − − →
( a1 b1 +λb2c2
(a2 −λa1)c2 b2
)
(
a1 b1
a2 b2c2
)
Id⊗ψ (c2)
− − − − − →
(
a1 b1
a2c2 b2
)
[21]λc 2
↓ [21]λ
↓
( a1 −λc2a2 b1
a2 c2(b2 +λb1)
)
Id⊗ψ (c2)
− − − − − →
( a1 −λc2a2 b1
a2c2 b2 +λb1
)
Proof: direct computation. □
Denote by ψ′(y) the ”opposite” morphism of ψ(y):
R
xy
− − − →R
z
− − − →R
y
↓ 1
↓ y
↓
R
x
− − − →R
yz
− − − →R
16
The analogue of lemma 1 holds for ψ′ as well (just reverse all horizontal arrows
in the commutative diagrams above). We call ψ and ψ′ ﬂip morphisms.
Starting with the Koszul matrices for C(Γ 0) and C(Γ 1) and applying a
row transformation to each of them, we get the following equivalent Koszul
forms for these factorizations:
C(Γ 0) :
(
a x 1 −x4
a x 2 −x3
)
[12]1
− − →
(
a x 1 +x2 −x3 −x4
0 x2 −x3
)
(8)
C(Γ 1) :
( a x 1 +x2 −x3 −x4
0 x1x2 −x3x4
)
[21]−x2
− − − − →
( a x 1 +x2 −x3 −x4
0 ( x2 −x3)(x4 −x2)
)
(9)
The ﬁrst rows of these new Koszul matrices for C(Γ 0),C (Γ 1) are identical
while the second rows look related. In fact, there is a ﬂip morphism ψ(x4−x2)
from (0, (x2 −x3)(x4 −x2)) to (0,x 2 −x3):
R
0
− − − →R
(x2−x3)(x4−x2)
− − − − − − − − − →R
1
↓ x4−x2
↓ 1
↓
R
0
− − − →R
x2−x3
− − − − − − − →R
and the ﬂip morphism ψ′(x4 −x2) back. Tensoring these ﬂip morphisms with
the identity morphism on the ﬁrst row, we obtain maps of factorizat ions
Id ⊗ψ′(x4 −x2) : C(Γ 0) − →C(Γ 1), Id ⊗ψ(x4 −x2) : C(Γ 1) − →C(Γ 0).
Lemma 2 Maps Id ⊗ψ′(x4 −x2) and Id ⊗ψ(x4 −x2) are equal to χ0 and
χ1, respectively.
The proof is a straightforward linear algebra computation. □
Therefore, our deﬁnition of the complex C(D) of factorizations assigned
to a tangle diagram can be rewritten via modiﬁed Koszul matrices as a bove
and maps ψ,ψ ′. We’ll use this alternative presentation in our proof of the
invariance of C(D) below. The new deﬁnition simpliﬁes the appearance of
C(D) by creating more zeros in the Koszul matrices of C(Γ) and making
the diﬀerential easier to describe and understand (at the cost of breaking
the ”lateral” symmetry x1 ↔ x2, x3 ↔ x4 of the original Koszul matrices).
The diﬀerential acts now as the identity on all but m2 rows, where m2 is the
number of crossings of D.
3. Markings don’t matter.
To deﬁne the complex C(D) for a tangle diagram D, we need to place
several marks on D: at least one on each internal edge and each circle and
17
x1x2
x3
x1x2
x1 x2
x3 x4
x1 x2
x3 x4
x5
Γ 2Γ 1
Figure 10: Mark removal equivalences
some (possibly none) on each external edge (an edge containing a b oundary
point). In this subsection we prove proposition 1 that was stated e arlier and
says that, up to chain homotopy equivalence, C(D) does not depend on how
marks are placed on the edges of D.
Lemma 3 Factorizations Γ 1 and Γ 2 are isomorphic in hmfw if Γ 2 is ob-
tained from Γ 1 by removing a mark.
Proof: It’s enough to check this property locally. We depicted two such
local pairs (Γ 1, Γ 2) in ﬁgure 10, and refer the reader to [KR] for a more de-
tailed treatment. We only check the isomorphism for the top pair in ﬁg ure 10,
other cases are similar. We transform the Koszul matrix of C(Γ 1) as follows:


a x 1 +x5 −x3 −x4
0 x1x5 −x3x4
a x 2 −x5

 [13]1
− →


a x 1 +x2 −x3 −x4
0 x1x5 −x3x4
0 x2 −x5


The variable x5 is internal. According to proposition 3 with y = x5 we can
remove the last row of the RHS matrix, substitute x2 for x5 everywhere else
and forget about x5. We end up with the Koszul matrix of C(Γ 2). □
To show independence of D on the number and position of marks, we
need to check compatibility of the isomorphisms C(Γ 1) ∼=C(Γ 2) above with
maps χ0,χ 1. We’ll only work through one case and leave the others to an
interested reader. Let’s check that complexes of factorizations
0 − →C(Γ 1
1)
χ 1
− →C(Γ 0
1) − →0
18
x1 x2
x3 x4
x5
x1
x3 x4
x2
χ  1
Γ 1
0Γ 1
  1
x1
x3 x4
x2
χ  1
x1 x2
x3 x4
Γ 2
0Γ 2
  1
Figure 11:
and
0 − →C(Γ 1
2)
χ 1
− →C(Γ 0
2) − →0 (10)
are chain homotopy equivalent, for ﬁgure 11 diagrams. The ﬁrst co mplex,
written via Koszul matrices, has the form


a x 1 +x5 −x3 −x4
0 ( x5 −x3)(x4 −x5)
a x 2 −x5

 Id⊗ψ (x4−x5)⊗Id
− − − − − − − − − − →


a x 1 +x5 −x3 −x4
0 x5 −x3
a x 2 −x5


Applying [13]1 simultaneously to both matrices we get an isomorphic complex


a x 1 +x2 −x3 −x4
0 ( x5 −x3)(x4 −x5)
0 x2 −x5

 Id⊗ψ (x4−x5)⊗Id
− − − − − − − − − − →


a x 1 +x5 −x3 −x4
0 x5 −x3
0 x2 −x5


The only internal variable is x5. We switch from x5 tox =x2 −x5. We think
ofx as an internal variable, while a,x 1,x 2,x 3,x 4 are external. Both matrices
have identical bottom rows (0 ,x ) and the diﬀerential is the identity on that
row. Therefore, we can eliminate x from the complex, reducing the ground
ring to Q[a,x 1,x 2,x 3,x 4], crossing out the bottom row and setting x = 0.
The resulting complex
(
a x 1 +x2 −x3 −x4
0 ( x2 −x3)(x4 −x2)
)
Id⊗ψ (x4−x2)
− − − − − − − →
(
a x 1 +x2 −x3 −x4
0 x2 −x3
)
19
DD 2  1
Figure 12: Type IA Reidemeister move
χ 1
Γ 1x1
x2
x4
Γ  0x1
x2
x4
x1
x4
Γ
Figure 13: Resolutions of D2
is isomorphic to (10). □
4. Invariance under Reidemeister move I.
Consider type IA Reidemeister move as depicted in ﬁgure 12. The com -
plex C(D2){0, 2} has the form
0 − →C(Γ 1)
χ 1
− →C(Γ 0) − →0,
see ﬁgure 13. In terms of Koszul matrices, the complex is given by
( a x 1 −x4
0 0
)
Id⊗ψ (x4−x2)
− − − − − − − →
( a x 1 −x4
0 0
)
(we set x3 =x2 in the formulas (8), (9) for Γ 0 and Γ 1).
The diﬀerential is the identity on the ﬁrst row, and on the second ro w
given by
R
0
− − − →R{−1, 3}
0
− − − →R
1
↓ x4−x2
↓ 1
↓
R
0
− − − →R{−1, 1}
0
− − − →R
Therefore, the complex splits into a direct sum of a contractible com plex and
the tensor product of ( a,x 1 −x4) with
0 − →R{−1, 3}
x4−x2
− − − →R{−1, 1} − →0.
20
D D  1 2
Figure 14: Type IB Reidemeister move
Since x2 is an internal variable, we can remove a contractible summand
0 − →R{−1, 3}
x4−x2
− − − →R(x4 −x2){−1, 1} − →0
from the above complex and reduce the ground ring to R′ = Q[a,x 1,x 4].
We get the complex (a,x 1 −x4) shifted by {−1, 1}[−1]. Thus,C(D2){0, 2} ∼=
C(Γ) {−1, 1}[−1], for Γ as in ﬁgure 13. Since Γ ∼=D1, there is an isomorphism
C(D2){1, 1}[1] ∼=C(D1). We record this as
Proposition 4 Complexes of matrix factorizations C(D1) andC(D2){1, 1}[1]
are isomorphic as objects of K(hmfw), with w =a(x1 −x4).
A similar computation takes care of the Reidemeister move IB:
Proposition 5 Complexes of matrix factorizations C(D1) and C(D2) are
isomorphic as objects of K(hmfw), for D1,D 2 depicted in ﬁgure 14.
5. Invariance under Reidemeister move IIa.
D D  1 2
Figure 15: Type IIa move
Complexes of matrix factorizations C(D1) and C(D2), for the diagrams
depicted in ﬁgure 15, live in the category K(hmfw) with w = a(x1 +x2 −
x3 −x4), viewed as an element of the ground ring R = Q[a,x 1,x 2,x 3,x 4]. The
complexC(D2) ∼=C(Γ 01) lies entirely in cohomological degree zero, since D2
has no crossings.
21
Γ 01
x1 x2
x3
x4
x5 x6
Γ 11
x1 x2
x4x3
x5 x6
Γ 10
x1 x2
x3 x4
x5 x6
Γ 00
x1 x2
x3
x4
x5 x6
f1
f2
Figure 16: Four resolutions of D1
Proposition 6 Complexes of matrix factorizations C(D1) and C(D2) are
equivalent as objects of K(hmfw).
Proof: It suﬃces to show that f1 is an isomorphism (in hmfw) from
C(Γ 00) to a direct summand of C(Γ 10), and that there is a decomposition
C(Γ 10) ∼= Im(f ) ⊕M
with f2 restricting to an isomorphism between M and C(Γ 11). Then C(D1)
would be isomorphic to a direct sum of contractible complexes
0 − →C(Γ 00)
Id
− →Im(f ) − →0,
0 − →M
f2
− →C(Γ 11) − →0
and the factorization C(Γ 01), isomorphic to C(D2).
We start by writing down the diagram of factorizations and maps
C(Γ 00)
f1
− →C(Γ 10)
f2
− →C(Γ 11)
and simplify them in hmfw by removing contractible direct summand fac-
22
torizations from each of the three terms. The diagram has the for m


a x 1 +x2 −x5 −x6
0 x2 −x6
a x 5 +x6 −x3 −x4
0 ( x6 −x4)(x3 −x6)


f1
− →


a x 1 +x2 −x5 −x6
0 ( x2 −x6)(x5 −x2)
a x 5 +x6 −x3 −x4
0 ( x6 −x4)(x3 −x6)


f2
− →


a x 1 +x2 −x5 −x6
0 ( x2 −x6)(x5 −x2)
a x 5 +x6 −x3 −x4
0 x6 −x4


with
f1 = Id ⊗ψ′(x5 −x2) ⊗ Id⊗2, f 2 = Id ⊗3 ⊗ψ(x3 −x6).
Apply row transformation [13] 1 to all three Koszul matrices. The new ma-
trices will have identical ﬁrst rows ( a,x 1 +x2 −x3 −x4) and identical third
rows (0,x 5 +x6 −x3 −x4). We remove the third rows and exclude internal
variablex5 substitutingx3 +x4−x5 in its place everywhere else. The diagram
becomes the tensor product of the Koszul factorization ( a,x 1 +x2 −x3 −x4)
and the diagram
(
x2 −x6
(x6 −x4)(x3 −x6)
)
g1
− →
(
(x2 −x6)(x3 +x4 −x6 −x2)
(x6 −x4)(x3 −x6)
)
g2
− →
(
(x2 −x6)(x3 +x4 −x6 −x2)
x6 −x4
)
where
g1 =ψ′(x3 +x4 −x6 −x2) ⊗ Id, g 2 = Id ⊗ψ(x3 −x5).
We omitted the ﬁrst columns from the Koszul matrices, since their t erms are
all zeros. The only internal variable left is x6. The bottom term in the ﬁrst
two factorizations is
(x6 −x4)(x3 −x6) = −x2
6 + (x3 +x4)x6 −x3x4.
Let R′ = Q[a,x 1,x 2,x 3,x 4] be the polynomial ring on all external variables.
Currently we’re working over the ring R′[x6]. We remove the bottom term
from the ﬁrst two factorizations simultaneously reducing to R′, imposing the
relation x2
6 = (x3 +x4)x6 −x3x4, and treating multiplication by x6 as an
endomorphism of the free R′-moduleR′[x6]/((x6 −x4)(x3 −x6)). Likewise, in
the rightmost factorization, we remove the bottom row ( x6 −x4), reduce to
23
the ground ring R′ and impose the relation x6 =x4. Our diagram simpliﬁes
to
R′1 ⊕R′x6
x2−x6
− − − → R′1 ⊕R′x6
1
↓ x3+x4−x6−x2
↓
R′1 ⊕R′x6
(x2−x4)(x3−x2)
− − − − − − − − − →R′1 ⊕R′x6
x6→x4
↓ x6→x4
↓
R′ (x2−x4)(x3−x2)
− − − − − − − − − →R′
where, for instance, the bottom row denotes the factorization
R′ 0
− →R′ (x2−x4)(x3−x2)
− − − − − − − − − →R′
and the maps g1,g 2 are given by vertical arrows. Stripping oﬀ a contractible
summand
R′1
1
− →R′(x2 −x6)
from the ﬁrst factorization, we reduce it to
R′(x6 +x2 −x3 −x4)
(x2−x4)(x2−x3)
− − − − − − − − − →R′1.
The middle factorization is a direct sum of two isomorphic (up to gradin g
shift) factorizations
R′1
(x2−x4)(x3−x2)
− − − − − − − − − →R′1
and
R′(x6 +x2 −x3 −x4)
(x2−x4)(x3−x2)
− − − − − − − − − →R′(x6 +x2 −x3 −x4).
The map g1 takes the top factorization (in its reduced form) isomorphically
onto the second summand of the middle factorization. The map g2 restricts
to an isomorphism from the ﬁrst direct summand of the middle factor ization
to the bottom factorization. Our claim and the proposition follow. □
The invariance under the mirror image of the ﬁgure 15 move can be
veriﬁed similarly.
6. Invariance under Reidemeister move III.
Let factorization Υ be given by the following Koszul matrix:


a x 1 +x2 +x3 −x4 −x5 −x6
0 x1x2 +x1x3 +x2x3 −x4x5 −x4x6 −x5x6
0 x1x2x3 −x4x5x6


24
x2 x3x1
Γ 1
x5 x6x4
Γ 1
x5 x6x4
Γ 2
x4 x5 x6
x2 x3x1
Γ 3
x4 x5 x6
x1 x2 x3
Γ4
x4 x5 x6
x1 x2 x3
Figure 17: Diagrams Γ 1, Γ 2, Γ 3, Γ 4
The gradings are normalized so that the diﬀerential has bidegree (1 , 1). For
instance, the bottom row denotes the factorization
R
0
− →R{−1, 5}
x1x2x3−x4x5x6
− − − − − − − − − →R
withR = Q[a,x 1,...,x 6]. The potential is w =a(x1 +x2 +x3 −x4 −x5 −x6).
Proposition 7 In hmfw there are isomorphisms
C(Γ 1) ∼= C(Γ 4){0, 2} ⊕ Υ, (11)
C(Γ 3) ∼= C(Γ 2){0, 2} ⊕ Υ, (12)
for Γ 1, Γ 2, Γ 3, Γ 4 depicted in ﬁgure 17.
Proof: To prove the ﬁrst isomorphism, we place labels x7,x 8,x 9 (from
top to bottom) on the three marks of Γ 1 and write C(Γ 1) in the Koszul form
C(Γ 1) =


a x 1 +x2 −x8 −x7
0 ( x2 −x7)(x8 −x2)
a x 7 +x3 −x9 −x6
0 ( x3 −x6)(x9 −x3)
a x 8 +x9 −x4 −x5
0 ( x9 −x5)(x4 −x9)


Applying transformations [13] 1 and [15] 1 we get a matrix with the third and
ﬁfth rows
(0,x 7 +x3 −x9 −x6), (0,x 8 +x9 −x4 −x5).
25
We use these rows to exclude internal variables x7 and x8 and reduce C(Γ 1)
to the following Koszul form


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x2 +x3 −x6 −x9)(x4 +x5 −x2 −x9)
0 ( x3 −x6)(x9 −x3)
0 ( x9 −x5)(x4 −x9)


Notice that variables a andx1 appear only in the ﬁrst row. Moreover, Koszul
forms of factorizations Υ and C(Γ 4) have the same ﬁrst row. Next, we ignore
the ﬁrst row of C(Γ 1) and operate on the other three rows. The ﬁrst column
of the Koszul matrix then consists of zeros and we omit it. To simplify the
factorization


(x2 +x3 −x6 −x9)(x4 +x5 −x2 −x9)
(x3 −x6)(x9 −x3)
(x9 −x5)(x4 −x9)


we use the last term to reduce to at most linear terms in the last rema ining
internal variablex9. Remove the last row and impose the relation x2
9 = (x4 +
x5)x9 −x4x5. Modulo this relation and after adding the second row, the ﬁrst
row loses x9 and the matrix becomes
( (x3 −x6)(x4 +x5 −x2 −x3) + (x2 −x5)(x4 −x2)
(x3 −x6)(x9 −x3)
)
Nowx9 appears only in the bottom row, which we can write as
R1 ⊕Rx9
(x3−x6)(x9−x3)
− − − − − − − − − →R1 ⊕Rx9.
Changing basis of the free R-module on the left hand side from {1,x 9} to
{1,x 9 +x3 −x4 −x5} and of the module on the right to {1,x 9 −x3}, we
decompose this complex into a direct sum of
R(x9 +x3 −x4 −x5)
(x3−x4)(x5−x3)(x3−x6)
− − − − − − − − − − − − − − →R1
and
R1
x3−x6
− − − →R(x9 −x3).
Adding the other rows, we obtain a decomposition of C(Γ 1) into direct sum
of factorizations with Koszul matrices


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x3 −x6)(x4 +x5 −x2 −x3) + (x2 −x5)(x4 −x2)
0 ( x3 −x4)(x3 −x5)(x3 −x6)


26
D D  1 2
Figure 18: Reidemeister move III
and


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x3 −x6)(x4 +x5 −x2 −x3) + (x2 −x5)(x4 −x2)
0 x3 −x6

,
the latter shifted by {0, 2} due to the bidegree (0 , 2) vector x9 −x3 being
a generator of the module R(x9 −x3). It is easy to check that the matrices
above describe factorizations Υ and C(Γ 4), respectively. □
Proposition 8 Complexes C(D1) and C(D2), for diagrams depicted in ﬁg-
ure 18, are isomorphic in the category K(hmfw).
Proof is similar to the one in [KR]. The complex C(D1) consists of eight
factorizations assigned to diagrams depicted in ﬁgure 19 (also see ﬁ gure 6).
We ignore the overall shift by {0, −2} in the resolution of each crossing,
which was needed for the invariance under the Reidemeister move II a, but
does not make any diﬀerence for Reidemeister move III. Propositio n 7 tells
tells us that
C(Γ 111) ∼= Υ ⊕C(Γ 100){0, 2}
(also observe that Γ 100 ∼= Γ 001), while our proof of the invariance under the
Reidemeister move IIa implies
C(Γ 101) ∼=C(Γ 100){0, 2} ⊕C(Γ 100).
A computation similar to the one in that proof shows that the map χ1 :
C(Γ 111) − →C(Γ 101), when restricted to the direct summand isomorphic to
C(Γ 100){0, 2}, is an isomorphism onto a direct summand of C(Γ 101), while
our proof of proposition 6 implies that χ1 : C(Γ 101) − →C(Γ 001) is an iso-
morphism when restricted to the direct summand C(Γ 100) of C(Γ 101).
After removing contractible summands
0 − →C(Γ 100){0, 2}
∼=− →C(Γ 100){0, 2} − →0
27
Γ 111
 000Γ
Γ 010
Γ 101
Γ 011
Γ 110
Γ 001
Γ 100
Figure 19: Resolution cube of D1
28
 000Γ
Γ 010
Γ 100 Γ 001
Γ 011
Γ 110
Υ
Figure 20: Complex C ′
and
0 − →C(Γ 100)
∼=− →C(Γ 100) − →0
we reduce C(D1) to a complex C ′ that is graphically depicted in ﬁgure 20,
factorization Υ assigned to the diagram Y.
Lemma 4 The complexC ′ ∼=C(D1) is indecomposable in the categoryK(hmfw).
In other words, we cannot write C ′ ∼= M ⊕N for two nontrivial objects
M,N ofK(hmfw). Indeed, invariance under the Reidemeister move IIa tells
us that tensoring with a complex of factorizations assigned to a cro ssing is
an invertible functor. Precisely, it’s an invertible functor from the c ategory
K(hmfv) to K(hmfu) where v =ax3 +ax4 +f (x),u =ax1 +ax2 +f (x), and
f (x) is any polynomial in variables x disjoint from x1,...,x 4. An invertible
functor is indecomposable iﬀ the identity functor is. The identity fun ctor, in
general, corresponds to the diagram comprised of n parallel lines, compatibly
oriented (the diagram of the trivial braid). Its factorization S can be written
as the tensor product of (a,xi −xn+i), overi = 1,...,n. An easy computation
(for instance, as in the proof of the next lemma) shows that the ho m space
Homhmfw(S,S ) of bigrading-preserving factorization homomorphisms up to
chain homotopies is one-dimensional. Therefore, S and the identity functor
29
are indecomposable, for otherwise a projection onto a direct summ and would
ensure that the above hom space is at least 2-dimensional. □
Lemma 5 For any arrow Γ − → Γ ′ in ﬁgure 20, the space of bidegree-
preserving maps C(Γ) → C(Γ ′) is one-dimensional (over the ground ﬁeld
Q) and is generated by χ1.
We can prove the lemma on a case-by-case basis, separately for ea ch
arrow. In general, to compute the dimension of Hom hmfw(M,N ), for matrix
factorizations M,N, with N of ﬁnite rank, we use the isomorphism
EXThmfw(M,N ) ∼=H(N ⊗RM•)
where EXT refers to taking ext groups of the pair M,N in all bidegrees, M•
is the R-module dual of M, and H stands for cohomology. Restricting the
left hand side to Hom corresponds to taking the bidegree (0 , 0) summand of
the right hand side. The dual of a Koszul factorization ( ai,bi) is the Koszul
factorization (bi, −ai), with suitably shifted gradings.
For instance, to determine the dimension of the space
Homhmfw(C(Γ 110),C (Γ 100))
(the bottom arrow in ﬁgure 20) we ﬁrst write the Koszul matrix of C(Γ 110) :


{0, 0} a {1, −1} x1 +x2 −x4 −x7
{0, 0} a {1, −1} x7 +x3 −x5 −x6
{0, 0} 0 {1, −3} (x2 −x4)(x2 −x7)
{0, 0} 0 {1, −3} (x3 −x5)(x3 −x6)


Here x7 is the variable assigned to the internal mark of Γ 110. We also added
two columns indicating the bidegrees of R. For instance, the second row
denotes the factorization
R{0, 0}
a
− →R{1, −1}
x7+x3−x5−x6
− − − − − − − − →R{0, 0}.
After we apply [12] 1, the second row becomes (0,x 7 +x3 −x5 −x6); we get rid
of it and of the variable x7. Thus,C(Γ 110) is isomorphic to the factorization
assigned to the Koszul matrix


{0, 0} a {−1, 1} x1 +x2 +x3 −x4 −x5 −x6
{0, 0} 0 {−1, 3} (x2 −x4)(x2 +x3 −x5 −x6)
{0, 0} 0 {−1, 3} (x3 −x5)(x3 −x6)

.
30
The dual C(Γ 110)• of C(Γ 110) can be represented by the matrix


{0, 0} x1 +x2 +x3 −x4 −x5 −x6 {1, −1} − a
{0, 0} (x2 −x4)(x2 +x3 −x5 −x6) {1, −3} 0
{0, 0} (x3 −x5)(x3 −x6) {1, −3} 0


and the tensor product complex C(Γ 110)• ⊗C(Γ 100) by


{0, 0} a {−1, 1} x1 +x2 −x4 −x5
{0, 0} 0 {−1, 3} (x2 −x4)(x2 −x5)
{0, 0} a {−1, 1} x3 −x6
{0, 0} x1 +x2 +x3 −x4 −x5 −x6 {1, −1} − a
{0, 0} (x2 −x4)(x2 +x3 −x5 −x6) {1, −3} 0
{0, 0} (x3 −x5)(x3 −x6) {1, −3} 0


,
where the ﬁrst three rows describe C(Γ 100). We do transformation [13] 1 and
shift rows 4 and 5 by one each. We get


{0, 0} a {−1, 1} x1 +x2 +x3 −x4 −x5 −x6
{0, 0} 0 {−1, 3} (x2 −x4)(x2 −x5)
{0, 0} 0 {−1, 1} x3 −x6
{1, −1} − a {0, 0} x1 +x2 +x3 −x4 −x5 −x6
{1, −3} 0 {0, 0} (x2 −x4)(x2 +x3 −x5 −x6)
{0, 0} (x3 −x5)(x3 −x6) {1, −3} 0


We apply the transformation [14] −1, then shift rows 1 and 6 to obtain


{−1, 1} 0 {0, 0} a
{0, 0} 0 {−1, 3} (x2 −x4)(x2 −x5)
{0, 0} 0 {−1, 1} x3 −x6
{1, −1} 0 {0, 0} x1 +x2 +x3 −x4 −x5 −x6
{1, −3} 0 {0, 0} (x2 −x4)(x2 +x3 −x5 −x6)
{1, −3} 0 {0, 0} (x3 −x5)(x3 −x6)


.
Cross out row 3 and convert x6 to x3 everywhere else. The matrix reduces
to 

{−1, 1} 0 {0, 0} a
{0, 0} 0 {−1, 3} (x2 −x4)(x2 −x5)
{1, −1} 0 {0, 0} x1 +x2 −x4 −x5
{1, −3} 0 {0, 0} (x2 −x4)(x2 −x5)
{1, −3} 0 {0, 0} 0


.
31
We apply [24] 1, then remove rows 1 and 3 simultaneously with getting rid of
the variables a and x5. The resulting matrix is


{0, 0} 0 {−1, 3} (x2 −x4)(x4 −x1)
{1, −3} 0 {0, 0} 0
{1, −3} 0 {0, 0} 0

.
Let now R′ = Q[x1,x 2,x 3,x 4]. The cohomology of the complex described by
this matrix is the tensor product of the quotient R′/((x2 −x4)(x4 −x1)) and
the bigraded vector space
(Q{1, −3} ⊕ Q) ⊗ (Q{1, −3} ⊕ Q).
The bigraded dimension of R′/((x2 −x4)(x4 −x1)) has the form 1 + α where
α ∈ q2Z[q2], while that of the second term is (1 + tq−3)2. Therefore, the
bigraded dimension of the cohomology of the complex C(Γ 110)• ⊗C(Γ 100)
has the form
(1 +α)(1 + 2tq−3 +t2q−6).
Writing it as a polynomial in t with coeﬃcients being power series in q,
we see that the coeﬃcient of the term t0q0 equals 1. Therefore, the bide-
gree (0, 0) summand of the homology is one-dimensional, and the hom space
Homhmfw(C(Γ 110),C (Γ 100)) has dimension 1 .
To show that χ1 : C(Γ 110) − →C(Γ 100) (corresponding to the splitting
of the right wide edge of Γ 110 into two parallel lines) generates this one-
dimensional space, it suﬃces to show that χ1 is not null-homotopic. We can
write the factorizations and the map in the following Koszul form


a x 1 +x2 −x4 −x7
0 ( x2 −x4)(x2 −x7)
a x 7 +x3 −x5 −x6
0 ( x3 −x5)(x3 −x6)


χ 1
− →


a x 1 +x2 −x4 −x7
0 ( x2 −x4)(x2 −x7)
a x 7 +x3 −x5 −x6
0 x3 −x6


with χ1 = Id ⊗3 ⊗ψ(x3 −x5). Applying row transformation [13] 1 to each
matrix and then excluding x7 we reduce the map to


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x2 −x4)(x2 +x3 −x5 −x6)
0 ( x3 −x5)(x3 −x6)

 χ 1
− →


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x2 −x4)(x2 +x3 −x5 −x6)
0 x3 −x6


with χ1 = Id ⊗2 ⊗ψ(x3 −x5). Turn both Γ 110 and Γ 100 into closed diagrams
ˆΓ 110 and ˆΓ 100 by connecting top endpoints of each diagram with its bottom
32
endpoints by three disjoint arcs. To check that χ1 is not null-homotopic, it’s
enough to verify that the induced map on cohomology
ˆχ1 :H(ˆΓ 110) − →H(ˆΓ 100)
is non-trivial. We represent this map in Koszul form as


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x2 −x4)(x2 +x3 −x5 −x6)
0 ( x3 −x5)(x3 −x6)
a x 4 −x1
a x 5 −x2
a x 6 −x3


ˆχ 1
− →


a x 1 +x2 +x3 −x4 −x5 −x6
0 ( x2 −x4)(x2 +x3 −x5 −x6)
0 x3 −x6
a x 4 −x1
a x 5 −x2
a x 6 −x3


,
and ˆχ1 = Id ⊗2 ⊗ψ(x3 −x5) ⊗ Id⊗3. Doing transformations [14] 1, [15]1, [16]1
and excluding x4, x5, x6 and a, we reduce the map to the form
( 0 0
0 0
)
ˆχ 1
− →
( 0 0
0 0
)
,
where ˆχ1 = Id ⊗ψ(x3 −x2) and the ground ring is Q[x1,x 2,x 3] (we took
the quotient by the ideal ( x1 −x4,x 2 −x5,x 3 −x6,a )). Clearly, ˆχ1 induces a
nontrivial map on cohomology, and χ1 is not null-homotopic.
Using symmetries of the graphs and factorizations, the other cas es of the
lemma can be reduced to verifying that the hom spaces
Homhmfw(Υ,C (Γ 110)) and Hom hmfw(C(Γ 100),C (Γ 000))
are both one-dimensional and generated by χ1. Actual computations, similar
to the one above, are left to a curious reader. For the ﬁrst of the two hom
spaces, by χ1 we mean the composition of χ1 :C(Γ 111) − →C(Γ 110) with the
inclusion of Υ as a direct summand of C(Γ 111). □
Lemma 6 For any arrow Γ − → Γ ′ in ﬁgure 20, factorizations C(Γ) and
C(Γ ′) are not isomorphic in hmfw.
Sketch of proof: Form the closures ˆΓ and ˆΓ ′ by connecting top endpoints of
each diagram with its bottom endpoints by 3 disjoint arcs. A direct co mputa-
tion shows that complexes C(ˆΓ) and C(ˆΓ ′) have non-isomorphic cohomology
groups (their two-variable Poincare polynomials are diﬀerent). □
Thus, the complex C ′, depicted in ﬁgure 20, consists of 6 factorizations
and its diﬀerential is a sum of 10 maps, one for each arrow of the ﬁgu re.
33
Each map is either 0 or a nonzero multiple of the unique (up to rescaling )
nontrivial map between the two factorizations. For each arrow b : Γ − →Γ ′
choose a nontrivial map m(b) : C(Γ) →C(Γ ′).
Lemma 7 For any two composable arrows Γ
b1
− →Γ ′ b2
− →Γ ′′ the composition
m(b2)m(b1) is nontrivial in hmfw.
Proof: It suﬃces to check that the composition
Υ ⊂C(Γ 111)
χ 1
− →C(Γ 110)
χ 1
− →C(Γ 100)
χ 1
− →C(Γ 000) (13)
is not null-homotopic. Denote the composition of the last 3 maps by χ′
1 and
the corresponding ”adjoint” composition
C(Γ 000)
χ 0
− →C(Γ 100)
χ 0
− →C(Γ 110)
χ 0
− →C(Γ 111)
byχ′
0. We claim that the map χ′
1prχ′
0 is non-zero, where pr is the projection
from C(Γ 111) onto its direct summand Υ . The map χ′
0 has degree (0 , 6)
and the product χ′
1χ′
0 is equal to the multiplication by ( x4 −x2)2(x5 −x3)
endomorphism of C(Γ 000), since the composition χ1χ0 is the multiplication
by a suitable linear combination of x’s. The complementary direct summand
of C(Γ 111) is isomorphic to C(Γ 100){0, 2}. Denote by ~pr the projection onto
this direct summand. Then pr + ~pr is the identity endomorphism of C(Γ 111).
The composition χ′
1 ~prχ′
0 factors though a degree (0 , 2) endomorphism of
C(Γ 110). This endomorphism is a composition
C(Γ 110) − →C(Γ 100) − →C(Γ 110)
where the ﬁrst map has degree (0 , 0) and the second–degree (0 , 2). These
maps are, necessarily, rational multiples of χ0 and χ1 (corresponding to the
right wide edge of Γ 110) and their composition is a rational multiple of the
multiplication byx3−x5. Hence, the composition χ′
1 ~prχ′
0 is a rational multiple
of the multiplication by ( x3 −x5)2(x2 −x4). To show that
χ′
1prχ′
0 =χ′
1χ′
0 −χ′
1 ~prχ′
0
is not null-homotopic, we observe that the right hand side is the multip lica-
tion by
(x4 −x2)2(x5 −x3) −µ(x3 −x5)2(x2 −x4)
endomorphism of C(Γ 000), for some rational µ. The image of Q[x1,...,x 6] in
the endomorphism ring of C(Γ 000) is the quotient ring by relations x1 =x4,
x2 =x5 and x3 =x6. The polynomial above simpliﬁes to
(x1 −x2)2(x2 −x3) −µ(x3 −x2)2(x2 −x1) ⁄= 0
34
in Q[x1,x 2,x 3]. Therefore, the composition χ′
1prχ′
0 is not null-homotopic, and
so is the map Υ − →C(Γ 000) in formula (13). Lemma 7 follows. □
The diﬀerential in the complex C ′ can be written as
d =
∑
b
λbm(b),
with λb ∈ Q, and the sum over all arrows b.
Lemma 8 All coeﬃcients λb are nonzero rational numbers.
Assume otherwise: λb = 0 for some b. Every square in the diagram of C ′
anticommutes, and from lemma 7 we derive that some other λ’s would have
to be zero. In fact, there will be enough zero maps to split the comp lex into
the direct sum of at least two subcomplexes, each comprised of two or four
factorizations in ﬁgure 20. Speciﬁcally, the complex will either decom pose
into a direct sum of 3 subcomplexes of the form
0 − →C(Γ)
m(b)
− →C(Γ ′) − →0 (14)
for some three arrows b, or as the direct sum of one subcomplex of type (14)
and the complementary summand containing the other four factor izations.
A decomposition of C ′ into a direct sum of 3 subcomplexes contradicts
lemmas 4, 6. To see the impossibility of the decomposition of the secon d kind,
it’s enough to show that the complementary summand cannot be triv ial in
hmfw. This summand would consist of four factorizations that sit in the
vertices of one of the four squares in ﬁgure 20. For instance, it co uld have
the form
0 − →C(Y ) − →C(Γ 110) ⊕C(Γ 011) − →C(Γ 010) − →0.
Triviality of the summand would imply that its identity map is null-homotopic.
In particular, the identity map of the rightmost factorization in the complex
would factor through a map to the middle term. This map should have
bidegree (0, 0). The following lemma establishes the contradiction.
Lemma 9 For any arrow Γ − →Γ ′ in ﬁgure 20 we have
Homhmfw(C(Γ ′),C (Γ)) = 0.
35
Thus, any bidegree zero map is trivial. The lemma can be proved in the
same way as lemma 5. □
Lemma 8 follows. □
To summarize, we established that the coeﬃcients λb in the diﬀerential
for the complex C ′ are all nonzero. Rescaling, if necessary, we can turn them
into 1’s and −1’s. Moreover, the complex C ′ is uniquely determined, up
to isomorphism, by the condition that λb ⁄= 0 for all b. We have C(D1) ∼=
C ′. Nearly identical arguments show that C(D2) ∼= C ′ as well. Therefore,
C(D1) ∼=C(D2), and proposition 8 follows. □
7. Computing the Euler characteristic.
Given a braid diagram D, the complexes C(Dσ±1
i ) are, up to shifts, the
cones of maps χ0,χ 1 between factorizations assigned to diagrams D andDei
where ei denotes a wide edge placed between i-th and ( i + 1)-st strands of
the braid. See Section 1 and ﬁgure 6 for details. Recall that ⟨D⟩ denotes
the Euler characteristic of cohomology H(D). Our deﬁnition of C(Dσ±1
i ) via
cones implies the following relations on the Euler characteristics:
⟨Dσi⟩ = ⟨Dei⟩ −q2⟨D⟩,
⟨Dσ−1
i ⟩ = q−2(⟨Dei⟩ − ⟨D⟩).
Excluding ⟨Dei⟩, we get
q−1⟨Dσi⟩ −q−1⟨Dσ−1
i ⟩ = (q−1 −q)⟨D⟩,
which is the relation satisﬁed by the function F (D) deﬁned in Section 1. If
D is the one-strand braid diagram of the unknot, H(D) ∼= Q[x]{−1, 1} and
⟨D⟩ = t−1
q−1 −q,
which is our normalization of F (D). Propositions proved above imply that
⟨D⟩ satisﬁes all other deﬁning properties of F (D). Therefore, ⟨D⟩ = F (D)
and Theorem 2 follows. □
Acknowledgements: The idea to consider matrix factorizations with
the potentialax came up when the authors were attending Virginia Topology
Conference in December of 2004. We’d like to thank Slava Krushkal a nd
Frank Quinn, the conference organizers, for bringing us togethe r and creating
an inspiring research atmosphere. M.K. is grateful to Sergei Guko v, Peter
Ozsv´ ath, Jacob Rasmussen, Albert Schwarz and Oleg Viro for inte resting
36
discussions. We’d like to acknowledge NSF support via grants DMS-04 07784
and DMS-0196131.
References
[APS] M. Asaeda, J. Przytycki and A. Sikora, Categoriﬁcation of t he Kauﬀ-
man bracket skein module of I-bundles over surfaces, Algebr. Geo m. Topol.
4 (2004) 1177-1210, arXiv math.QA/0409414.
[AF] B. Audoux and T. Fiedler, A Jones polynomial for braid-like isotop ies
of oriented links and its categoriﬁcation, arXiv math.GT/0503080.
[BN] D. Bar-Natan, Khovanov’s homology for tangles and cobordism s, arXiv
math.GT/0410495.
[G] B. Gornik, Note on Khovanov link cohomology, arXiv math.QA/0402 266.
[GSV] S. Gukov, A. Schwarz and C. Vafa, Khovanov-Rozansky hom ology
and topological strings, arXiv hep-th/0412243.
[HOMFLY] P. Freyd, D. Yetter, J. Hoste, W. B. R. Lickorish, K. Millet t and
A. Ocneanu, A new polynomial invariant of knots and links, Bull. AMS.
(N.S.) 12 2, 239–246, 1985.
[K] M. Khovanov, Link homology and Frobenius extensions, math.QA/0411447.
[KR] M. Khovanov and L. Rozansky, Matrix factorizations and link ho mol-
ogy, math.QA 0401268.
[L] E. S. Lee, An endomorphism of the Khovanov invariant, math.GT/0210213.
[OS] P. Ozsv´ ath and Z. Szab´ o, Holomorphic disks and knot invariants, arXiv
math.GT/0209056.
[PT] J. Przytycki and P. Traczyk, Conway Algebras and Skein Equiv alence
of Links, Proc. AMS 100, 744-748, 1987.
[R1] J. Rasmussen, Floer homology and knot complements, math.GT/ 0306378.
[R2] J. Rasmussen, Khovanov homology and the slice genus, math.GT/0402131.
[V] O. Viro, Private communication.
Mikhail Khovanov, Department of Mathematics, University of Califo rnia,
Davis, CA 95616, mikhail@math.ucdavis.edu
Lev Rozansky, Department of Mathematics, University of North C arolina
Chapel Hill, NC 27599, rozansky@math.unc.edu
37
