---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-005-2-proofs-twisted-nz-matrices
section_title: "Proofs: twisted NZ matrices"
section_number: 2
pages: 8-12
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
In this section we give proofs of the properties of the twisted NZ matrices, namely the
relation to the NZ matrices of cyclic covers (Theorem 1.1), the symplectic properties (The-
orem 1.2), and the behavior under 2–3 Pachner moves (Theorem 1.4).
TWISTED NEUMANN–ZAGIER MATRICES 9
Proof. (of Theorem 1.1) It is clear that T (n) hasnN tetrahedra, asT hasN tetrahedra ∆j,
j = 1,...,N . Fixing a lift ~∆j of each ∆j to the inﬁnite cyclic cover, we choose lifts of the
tetrahedra ofT (n) byµk·~∆j for k = 0,...,n − 1. Similarly, we choose lifts of the edges of
T (n). Then it is clear from the construction of the n-fold cyclic cover that
G(n)□
k =


G□
nk G□
nk+1 ··· G□
nk+n−1
G□
nk−1 G□
nk ··· G□
nk+n−2
... ... ... ...
G□
nk−n+1 G□
nk−n+2 ··· G□
nk

 (28)
for all k∈ Z , which implies
G(n)□ =


∑
r≡0 G□
r
∑
r≡1 G□
r ··· ∑
r≡n−1 G□
r∑
r≡n−1 G□
r
∑
r≡0 G□
r ··· ∑
r≡n−2 G□
r
... ... ... ...∑
r≡1 G□
r
∑
r≡2 G□
r ··· ∑
r≡0 G□
r

 (29)
where≡ means the equality of integers in modulon. This completes the proof of Theorem 1.1.
□
Proof. (of Theorem 1.2) Following Neumann [Neu92], we consider the Z [t±1]-module V gen-
erated by variables Zj,Z′
j,Z′′
j subject to linear relations Zj +Z′
j +Z′′
j = 0 for 1 ≤ j≤ N.
We deﬁne a symplectic form on V as
⟨Zi,Z′′
j⟩ =⟨Z′
i,Zj⟩ =⟨Z′′
i,Z′
j⟩ =δij (30)
and
⟨cZj,Z′′
j⟩ =⟨Zj, ¯cZ′′
j⟩ =c, c ∈ Z [t±1]
where δij is the Kronecker delta and ¯ : Z [t±1]→ Z [t±1] is the involution induced from the
inversion t↦→ t−1. Note that ⟨Z′′
i,Zj⟩ =⟨Z′′
i,−Z′
j−Z′′
j⟩ =−δij and similarly,⟨Zi,Z′
j⟩ =
⟨Z′
i,Z′′
j⟩ =−δij.
We associate an element Ei∈V to each edge ei ofT as
Ei =
N∑
j=1
G(t)ijZj + G′(t)ijZ′
j + G′′(t)ijZ′′
j. (31)
In what follows, we use the same argument given in the proof of [Cho06, Thm.3.6] to show
that
⟨Ea,Eb⟩ = 0 for all 1 ≤a,b≤N. (32)
Considering the linear expansion of ⟨Ea,Eb⟩ using the equation (31), we have a non-trivial
term when the edges ea andeb appear in some ∆j with diﬀerent shape parameters. Without
loss of generality, suppose thatea andeb have parametersZj andZ′′
j , respectively. It is clear
that ~∆j containsµα·~ea andµβ·~eb for someα andβ∈ Z . Equivalently,µ−α·~∆j andµ−β·~∆j
are attached to ~ea and~eb, respectively. We thus get a non-trivial term
⟨t−αZj,t−βZ′′
j⟩ =tβ−α (33)
10 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
in the linear expansion from the triple ( ~∆j,µα·~ea,µβ·~eb). On the other hand, considering
the face-pairing of the face of ∆ j containing ea and eb, there is another tetrahedron ∆ i
(possibly i = j), which also contains both ea and eb. It follows that ~∆i contains µα+γ·~ea
and µβ+γ·~eb for some γ ∈ Z . From this triple ( ~∆i,µα+γ·~ea,µβ+γ·~eb), we get another
non-trivial term−t(β+γ)−(α+γ) =−tβ−α which we can pair with the term (33) to cancel out.
Note that we have the minus sign here, since the face-pairing is orientation-reversing: the
shape parameters of ea and eb for ∆i are either (Zi,Z′
i), (Z′
i,Z′′
i ), or (Z′′
i,Zi). In this way,
every non-trivial term that appears in the expansion of⟨Ea,Eb⟩ is paired to cancel out. This
proves the equation (32). We then directly obtain the desired equation (17), since we have
⟨Ea,Eb⟩ =
N∑
j=1
⟨
G(t)ajZj + G′(t)ajZ′
j + G′′(t)ajZ′′
j, G(t)bjZj + G′(t)bjZ′
j + G′′(t)bjZ′′
j
⟩
=
N∑
j=1
G(t)aj(G′′(1/t)bj− G′(1/t)bj) + G′(t)aj(G(1/t)bj− G′′(1/t)bj) + G′′(t)aj(G′(1/t)bj− G(1/t)bj)
=
N∑
j=1
(G(t)aj− G′(t)aj)(G′′(1/t)bj− G′(1/t)bj)− (G′′(t)aj− G′(t)aj)(G(1/t)bj− G′(1/t)bj)
=
N∑
j=1
A(t)ajB(1/t)bj− B(t)ajA(1/t)bj.
□
Proof. (of Theorem 1.4) Recall that a 2–3 Pachner move on T is determined by two tetra-
hedra ∆α and ∆β with a common face in T . Dividing the bipyramid ∆ α∪ ∆β into three
tetrahedra ∆a, ∆b, and ∆c as in Figure 2, we obtain a new ideal triangulation T with one
additional edge e0. We choose lifts of the ﬁve tetrahedra ∆ α, ∆β, ∆a, ∆b, ∆c and the edge
e0 (to the inﬁnite cyclic cover) such that ~∆α∪~∆β and ~∆a∪~∆b∪~∆c are the same bipyramid
containing~e0. Note that the (twisted) gluing equation of e0 is
logz′
a + logz′
b + logz′
c = 2π
√
−1. (34)
↔↔
zαz′
α
z′′
α
zβ
z′
βz′′
β
z′
c
zc z′′
c
z′
b
zb
z′′
b
z′
a
z′′
a za
z′
a
Figure 2. 2-3 Pachner move.
TWISTED NEUMANN–ZAGIER MATRICES 11
There are nine edges on the bipyramid whose gluing equations are aﬀected by the Pachner
move: three at the triangle of the base pyramid and six others on the bipyramid but not on
its base. The six edges give
logzα = logzb + logz′′
c logz′
α = logz′′
a + logzc logz′′
α = logza + logz′′
b
logzβ = logz′′
b + logzc logz′
β = logz′′
a + logzb logz′′
β = logza + logz′′
c, (35)
and the three edges give
logzα + logzβ = logz′
a logz′
α + logz′′
β = logz′
b logz′′
α + logz′
β = logz′
c. (36)
The relations (36) are obtained from the relations (35) up to the gluing equation (34) of e0
and the relation log z + logz′ + logz′′ =π√−1. For instance,
logzα + logzβ = logzb + logz′′
c + logz′′
b + logzc
= 2π
√
−1− logz′
b− logz′
c
= logz′
a.
Therefore, we can obtain the twisted gluing equation matrices G
□
(t) forT from the twisted
gluing equation matrices for T by substituting logz□
α and logz□
β in terms of the right hand
side of equation (35) and the substitution is correct up to the gluing equation of e0 and the
relation logz + logz′ + logz′′ = π√−1. In matrix form, this implies that for some lower
triangular matrix Q =
(
1 0
∗ IN
)
and an integer matrix C, we have
(
G(t)a G(t)b G(t)c
)
= Q
(
0 0 0
G′′(t)α + G′′(t)β G(t)α + G′(t)β G′(t)α + G(t)β
)
+ C,
(
G
′
(t)a G
′
(t)b G
′
(t)c
)
= Q
(
1 1 1
0 0 0
)
+ C,
(
G
′′
(t)a G
′′
(t)b G
′′
(t)c
)
= Q
(
0 0 0
G′(t)α + G′(t)β G′′(t)α + G(t)β G(t)α + G′′(t)β
)
+ C.
(37)
HereIN is the identity matrix of sizeN andXj is thej-th column of a matrixX. Multiplying
P =
(
1 0
G′(t)α + G′(t)β IN
)
Q−1 on both sides of Equation (37), we obtain
P
(
G(t)a G(t)b G(t)c
)
=
(
0 0 0
G′′(t)α + G′′(t)β G(t)α + G′(t)β G′(t)α + G(t)β
)
+ P C,
P
(
G
′
(t)a G
′
(t)b G
′
(t)c
)
=
(
1 1 1
G′(t)α + G′(t)β G′(t)α + G′(t)β G′(t)α + G′(t)β
)
+ P C,
P
(
G
′′
(t)a G
′′
(t)b G
′′
(t)c
)
=
(
0 0 0
G′(t)α + G′(t)β G′′(t)α + G(t)β G(t)α + G′′(t)β
)
+ P C .
(38)
12 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
It follows that
P
(
A(t)a A(t)b A(t)c
)
=
(
−1 −1 −1
B(t)α + B(t)β A(t)α A(t)β
)
,
P
(
B(t)a B(t)b B(t)c
)
=
(
−1 −1 −1
0 A (t)β + B(t)α A(t)α + B(t)β
)
,
where P is a lower triangular matrix with 1’s on the diagonal. □
