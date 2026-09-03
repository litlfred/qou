---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-009-33-integrable-pm-graph-fourier-transform-and-ver
section_title: "Integrable PM-graph, Fourier transform and Verlinde formula"
section_number: 3.3
pages: 18-21
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
assume thatA is diagonalizable over C. As a direct consequence of commutativity, allsv, v∈V are
diagonalizable. We denote by {u(i),i = 0,..., |V|− 1} a basis of right eigenvectors and {w(i),i =
0,..., |V|− 1} the dual basis of left eigenvectors normalized so that w(i)(v0) = 1 (as we will see in
the next lemma, any eigenvector has a nonzero coordinate along ev0). We suppose that u(0) =hr
(and thus w(0) =hl). Finally, we denote by θv(i) the eigenvalue of sv on u(i), so that θv(i) is the
eigenvalue ofsv on w(i)). As in Lemma 3.2, the coordinates of w(i) alongB0 are actually given by
the eigenvalues of the family sv.
Lemma 3.7. For all i∈{ 0,..., |V|− 1},
w(i)(v) =θv(i).
Proof. Let y be a left eigenvector with eigenvalue θv(i). Then, since sv(ev0) =ev,
⟨y,ev⟩ =⟨s∗
vy,ev0⟩ =θv(i)⟨y,ev0⟩.
In particular,⟨y,ev0⟩⁄ = 0 for otherwise we would have y = 0. Specifying to y =w(i) yields then
w(i)(v) =θv(i).
□
Remark that sh
v is also diagonalizable on L2
h(V ) with same eigenvalues θv(i),θv(i) and left and
right eigenvectors
˜u(i) = 1
hr·u(i), ˜w(i) = 1
hl·w(i).
(beware that left eigenvectors are taken with respect to the adjoint ( ·)h,∗)).
Deﬁnition 3.8. The Fourier transform ΦV onL2
h(V ) is the morphism from L2
h(V ) to C|V| deﬁned
by
ΦV [x](i) =
⟨
˜w(i),x
⟩
h
.
. With this deﬁnition, a vector u∈L2
h(V ) is a h-probability measure if and only if ΦV [u](0) = 1.
Proposition 3.9. For any x,y∈L2
h(V ),
ΦV [x∗y](i) = ΦV [x](i)ΦV [y](i).
Moreover, ΦV is an isomorphism with inverse
Φ−1
V (ei) = ˜u(i),
where{ei}1≤i≤|V| is the canonical basis of C|V|.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 19
Proof. Letx,y∈L2
h(V ) and 0≤i≤|V|− 1. Then, using the deﬁnition of the convolution product
and the fact that ˜w(i) is an eigenvector of (sh
v)h,∗ with eigenvalueθiv,
ΦV [x∗y](i) =⟨ ˜w(i),x∗y⟩h
=
∑
v∈V
(hr·x)(v)
⟨
˜w(i),sh
v(y)
⟩
h
=
∑
v∈V
(hr·x)(v)
⟨
(sh
v)h,∗( ˜w(i)),y
⟩
h
=
∑
v∈V
(hr·x)(v)θv(i)ΦV [y](i).
Then, by Lemma 3.7,
ΦV [x∗y](i) = ΦV [y](i)
∑
v∈V
(hr·x)(v)w(i)(v) =ΦV [y](i)
∑
v∈V
(hr·x)(v)(hl· ˜w(i))(v)
=ΦV [y](i)
⟨
˜w(i),x
⟩
h
= ΦV [y](i)ΦV [x](i),
which proves the ﬁrst assertion. Then, for 0 ≤i,j ≤|V|− 1,
ΦV
[
˜u(i)
]
(j) =
⟨
˜w(j), ˜u(i)
⟩
h
=δij,
so ΦV is an isomorphism with inverse
Φ−1
V (ei) = ˜u(i).
□
The latter proposition amounts to say that Φ V diagonalizes the convolution product on L2
h(V ).
We can deduce from the above construction a general formula to compute arbitrary convolutions
in L2
h(V ).
Proposition 3.10 (Verlinde formula). Letn≥ 2. Then, for v∈V and x1,...,x n∈L2
h(V )
[x1∗···∗ xn] (v) =
|V|−1∑
i=0
n∏
j=1
ΦV [xj](i)˜ui(v),
and for v1,...,v n∈V ,
sv1...s vn =
∑
v∈V
cv
v1,...,vnsv
with
(8) cv
v1,...,vn =
|V|−1∑
i=0
n∏
j=1
θvj(i)u(i)(v).
Proof. Since ( ˜w(i))0≤i≤|V|−1 is the dual basis of (˜u(i))0≤i≤|V|−1 with respect to⟨·,·⟩h, we have
x1∗···∗ xn =
|V|−1∑
i=1
⟨ ˜w(i),x 1∗···∗ xn⟩h˜u(i) =
∑
i=1|V|−1
ΦV [x1∗···∗ xn](i)˜u(i).
20 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
By Proposition 3.9, we then have
x1∗···∗ xn =
|V|−1∑
i=1
n∏
j=1
ΦV [xj](i)˜u(i),
and the ﬁrst statement is deduced. For the second statement, remark that we also have
sh
v1...s h
vn =
∑
v∈V
cv
v1,...,vnsh
v
with the same coeﬃcients (see Deﬁnition 3.3 and the remark afterwards). By Proposition 3.6 and
the ﬁrst statement,
sh
v1...s h
vn =Mh
( 1
hr(v1)ev1∗···∗ 1
hr(vn)evn
)
= 1∏n
j=1hr(vj)
|V|−1∑
i=1
n∏
j=1
ΦV [evj](i)Mh(˜ui).
On the one hand, for 1 ≤j≤n, we have
ΦV [evj](i) =⟨ ˜w(i),evj⟩h =µh(vj) ˜w(i)(vj) =hr(vj)w(i)(vj) =hr(vj)θvj(i)
by Lemma 3.7. On the other hand,
Mh(˜u(i)) =
∑
v∈V
hr(v)˜u(i)(v)sh
v =
∑
v∈V
u(i)(v)sh
v.
Hence,
sh
v1...s h
vn =
∑
v∈V


|V|−1∑
i=1
n∏
j=1
θvj(i)u(i)(v)

sh
v,
and we thus get
cv
v1,...,vn =
|V|−1∑
i=0


n∏
j=1
θvj(i)

u(i)(v).
□
Remark 3.11. The formula (8) is called the Verlinde formula, since it is exactly the same formula
that appears in the special case where the graph comes from the fusion ring in conformal ﬁeld theory,
see [2]. Let{vj}0≤j≤|V|−1 be an enumeration of the vertices of V , with v0 the root of the PM graph
as before, and write S = (θvi(j))0≤i,j≤|V|−1. Then, by Lemma 3.7 and the deﬁnition of the dual
basisu(i)
(
S−1)
ij =u(i)(vj).
Hence, (8) specializes in the more common formula svisvj =∑|V|−1
k=0 Nk
ijsvk with
Nk
ij =
|V|−1∑
l=0
SilSjl
(
S−1)
lk.
Note that a term 1
S0l
often appearing in the literature disappears in our case due to our normal-
ization of the vectors w(i), 0≤ i≤| V|− 1. In the special case of the quantum cohomology of
the Grassmannian which is the subject of the present paper, this formula is known as Vafa and
Intriligator’s formula, see [5].
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 21
When A is normal with respect to ⟨·,·⟩, then A is diagonalizable in an orthogonal basis and,
with our convention, we can choose
(9) u(i) = 1
‖w(i)‖2w(i)
for 0≤i≤|V|− 1. In particular, hr = 1
‖hl‖2hl and thus
µh = 1
‖hl‖2hl·hl.
In this case,{˜ui, 1≤i≤|V|} is an orthogonal basis of L2
h(V ) with‖˜ui‖2
h = ‖hl‖2
‖w(i)‖2 and then ΦV is
an isometry from L2
h(V ) to C|V| endowed with the Hilbert space structure ⟨ei,ej⟩ =δij
‖hl‖2
‖w(i)‖2 .
