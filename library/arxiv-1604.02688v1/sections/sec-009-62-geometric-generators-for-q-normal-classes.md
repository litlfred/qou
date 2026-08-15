---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-009-62-geometric-generators-for-q-normal-classes
section_title: "Geometric generators for Q-normal classes"
section_number: 6.2
pages: 13-16
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Theorem 2.1] (also see Luo-Tillmann [LT08, §2]) shows that the space˜N(T; R)⊂ R7n of all
closed normal classes satisfying Haken’s matching equations (including, for example, the
boundary tori) has a basis given byedge solutions ˜Ei and tetrahedron solutions ˜Tj where
1≤i,j ≤n. These project toedge solutionsEi and tetrahedron solutionsTj under the map
which forgets triangular coordinates, giving the imageN(T; R)⊂ R3n. DeﬁneQ0(T; R) as
the solutions of theQ-matching equations corresponding to closed normal surfaces. It is a
result of [Tol98] that theQ-coordinates determine a normal surface up to multiples of the
peripheral normal tori and soQ0(T; R) =N(T; R).
When considering the map from all closed normal classes toQ-normal solution space, the
closed normal surface solutions coming from the boundary tori map to the zero vector. Thus,
such a map introduces one linear relation for each cusp, which in fact gives the only relations
(see for example the proof of [KR04, Theorem 3.1]), sodimQ0(T; R) = 2n−r, Explicitly,
the quad coordinates forEi are precisely the coeﬃcients in theedge equationfor theith edge
in T, and the quad coordinates forTj are (1, 1, 1) in thejth tetrahedron and (0, 0, 0) in all
other tetrahedra.
The spaceQ(T; R) of all Q-normal classes is spanned byedge solutions, tetrahedron so-
lutions and peripheral curve solutions (see [KR04, Theorem 3.1]). The peripheral curve
solutions are linearly independent from the edge and tetrahedron solutions, and there are
twolinearlyindependentperipheralcurvesolutions Mk,Lk percuspcorrespondingtoachoice
of basis (“meridian”µk, “longitude”λk) ofH1(∂kM; R) for each component∂kM of ∂M. In
fact, a suitable choice ofn−r edge solutions together with then tetrahedral solutions and
the 2r peripheral solutions form a basis for the real solution spaceQ(T; R), which therefore
has dimension 2n +r (which also follows from [KR04, Theorem 3.1]).
In fact the statements above follow from the symplectic relations of Neumann-Zagier (see
[NZ85], [Neu92], [Cho06]). LetA be then×3n gluing equation matrix forT, with rows given
by E1,...,E n. Then the n× 3n matrix ofQ-matching equationsB is given byB = AC
where C is the 3n× 3n block diagonal matrix made up ofn copies of


0 1 −1
−1 0 1
1 −1 0


(see Tillmann [Til08]). We can also regardC as the linear mapC : R3n→ R3n given by
C(a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn) = (−b1+c1,−c1+a1,−a1+b1,..., −bn+cn,−cn+an,−an+bn).
Then theQ-matching equations have coeﬃcientsC(Ei) for i = 1,...,n . (Compare Section
6.1 above.)
14 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Now the skew-symmetric pairing of Neumann-Zagier is given by
ω : R3n× R3n→ R, ω (x,x′) =Cx·x′
where· denotes the dot product. Explicitly, given vectors
x = (a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn),x′ = (a′
1,b′
1,c′
1,a′
2,b′
2,c′
2,...,a ′
n,b′
n,c′
n)∈ (R3)n
we have
ω(x,x′) =
n∑
j=1
(⏐⏐⏐⏐
aj a′
j
bj b′
j
⏐⏐⏐⏐ +
⏐⏐⏐⏐
bj b′
j
cj c′
j
⏐⏐⏐⏐ +
⏐⏐⏐⏐
cj c′
j
aj a′
j
⏐⏐⏐⏐
)
.
(Compare [Neu92, Cho06].)
It follows thatS∈ R3n satisﬁes theQ-matching equations if and only if
ω(Ei,S ) =C(Ei)·S = 0 for alli = 1,...,n. (17)
It is immediate that each tetrahedral solutionTj satisﬁes theQ-matching equations; in
fact, C(Tj) = 0 so ω(x,Tj) = −ω(Tj,x ) = −C(Tj)· x = 0 for all x ∈ R3n. Further,
the Neumann-Zagier symplectic relationssay that all symplectic products ofEi,Mk,Lk for
i = 1,...,n , k = 1,...,r are zero except that
ω(Lk,Mk) = 2 =−ω(Mk,Lk) for eachk = 1,...,r.
Hence, we can conclude that the edge solutionsEi and peripheral solutionsMk,Lk satisfy the
Q-matchingequations. Infact, withsomemoreanalysis, itcanbeenseenthatthetetrahedral
solutions together with a suitable choice ofn−r edge solutions and the peripheral solutions
form a basis for the real solution spaceQ(T; R), which has dimension2n +r.
As mentioned above, there is a basis for theQ-coordinates of spun normal surfaces given by
appropriately chosen edge solutions{Ei}n−r
i=1, all tetrahedral solutions{Tj}n
j=1, and peripheral
solutions{pkMk +qkLk}r
k=1. Hence for each choice ofxi,yj,pk,qk∈ R we obtain a spun
normal class
S =
∑
i
xiEi +
∑
j
yiTj +
∑
k
(pkMk +qkLk).
A normal surface has two important invariants; its Euler characteristic and its boundary
slope. These invariants give rise to two linear maps on the normal surface solution space
Q(T; R).
Deﬁnition 6.1.The formal Euler characteristicis the linear map
χ :Q(T; R)→ R, χ (S) =
∑
i
−2xi−
∑
j
yj
giving the usual Euler characteristic for embedded closed and spun normal surfaces.
(See [LT08] for a detailed discussion of the closed case, and Appendix A for the spun
normal case using generalised angle structures.)
Deﬁnition 6.2.The boundary map
∂ :Q(T; R)→H1(∂M ; R), ∂ (S) = 2
∑
k
(pkµk +qkλk)
THE 3D-INDEX AND NORMAL SURF ACES 15
gives the boundary slope and the direction of spinning for embedded spun normal surfaces.
Here µk and λk are the meridian and longitude of cuspk as deﬁned previously.
(See Tillmann [Til08] for the details.1) Note that at each cusp, a tail of a spun normal
surface is an inﬁnite annulus spiralling into the cusp. There are two possible directions of
spinning for each such a tail.
We can compute the boundary in terms of the Neumann-Zagier symplectic form: since
ω(S,Mk) =ω(pkMk +qkLk,Mk) =−2qk
and
ω(S,Lk) =ω(pkMk +qkLk,Lk) = 2pk
we have
∂(S) =
∑
k
(−ω(S,Lk)µk +ω(S,Mk)λk).
Note that
∂(S) = 0 if and only ifS deﬁnes a closed normal class.
Hence N(T; R) is the solution space of theQ-matching equations (17) together with the
additional equations
ω(Mk,S ) =ω(Lk,S ) = 0 for allk = 1,...,r. (18)
We now deﬁne a quadratic function which will play an important role in understanding
the degree of terms in the 3D-index sums.
Deﬁnition 6.3.We deﬁne adouble arcfunction
δ :Q(T; R)→ R, δ (S) =
∑
j
(ajbj +bjcj +cjaj), (19)
for
S = (a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn).
Note that forS∈ Q(T; Z+), ajbj +bjcj +cjaj counts the number of arcs of intersection
between the quads ofS in tetrahedronj. In particular,
a normal surface solutionS∈Q(T; Z+) is embedded if and only ifδ(S) = 0.
There is also an associated symmetric bilinear function
δ :Q(T; R)×Q(T; R)→ R
such that
δ(S +S′) =δ(S) +δ(S′) + 2δ(S,S′) for allS,S′∈Q(T; R). (20)
Explicitly
δ(S,S′) = 1
2
∑
j
(ajb′
j +bjc′
j +cja′
j) + (a′
jbj +b′
jcj +c′
jaj)
1Our sign convention is opposite to that in [Til08] and Regina v.4.96 ([Bur]), but is consistent with the
boundary map deﬁned in [Neu92] and discussed in §7 below.
16 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
if S and S′ have quad coordinates inR3n given by
[S] = (a1,b 1,c 1,a 2,b 2,c 2,...,a n,bn,cn)
and
[S′] = (a′
1,b′
1,c′
1,a′
2,b′
2,c′
2,...,a ′
n,b′
n,c′
n).
