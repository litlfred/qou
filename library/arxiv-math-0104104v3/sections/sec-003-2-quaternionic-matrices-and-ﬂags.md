---
doc_id: arxiv-math-0104104v3
doc_title: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds"
section_id: sec-003-2-quaternionic-matrices-and-ﬂags
section_title: "Quaternionic matrices and ﬂags"
section_number: 2
pages: 2-4
source_pdf: 0104104v3.pdf
source_sha256: e2154399f783aa9b
doc_brief: "Geometry of Four-vector Fields on Quaternionic Flag Manifolds — The purpose of this paper is to describe certain natural 4-ve ctor ﬁelds on quaternionic ﬂag manifolds, which geometrically determ ine"
---
We begin with some generalities on quaternionic matrices for which we d eﬁne
the following subgroups of GLn(H):
R := {diag(r1,...,r n)|ri∈ R+}
U := {upper triangular matrices with 1’s along the diagonal }
Vw := {U∈U|
(
PwUP −1
w
) t
∈U}
here Pw denotes the permutation matrix
(Pw)i,j =δi,w (j) for w∈Sn
D := {diag(d1,...,d n)| di∈ H∗}
B := UD
Now for G∈ GLn(H) we recall the strict Bruhat normal form [3] of G as:
G =UDPwV
Here all the matrices are uniquely determined: the matrix D = diag(d1,...,d n)
belongs toD;Pw is, as usual, the permutation matrix corresponding to w∈Sn;
both U and V belong to U; and we further require that PwVP −1
w is lower
triangular with 1’s along the diagonal, i.e. V ∈V w. This decomposition allows
us to deﬁne the Dieudonn´ e determinant [2] as the residue of sgn(w)· ∏ di in
H/[H, H] = R+. Moreover, by means of the strict Bruhat normal form, we
obtain the Bruhat decomposition:
GLn(H) =
∐
w∈Sn
BPwVw.
DenotingZw :={BPwVw}, we obtain from the Bruhat decomposition a param-
eterization of GLn(H) by Sn. The condition that Vw :=wVw −1 is lower trian-
gular implies in the case of w = e that V e =V must be both upper and lower
triangular hence equals the identity matrix and hence dimR(Ze) = dimR(B).
Takingw to be the longest permutation, wl = (n (n− 1)··· 2 1), rotates the
matrix V by 180 ◦ so that it is lower triangular. As no further conditions on
the entries of V are imposed, we have that dimR(Zwl ) = 4 n2. In general, we
Quatrisson structures and H-ﬂags 3
deﬁne the length of a permutation w, len(w), to be the minimal number of ad-
jacent transpositions required in a factorization of the permutat ion. One readily
sees that the maximal number of non-zero entries allowed in V , so that Vw is
lower triangular, is exactly len(w) so that dimR(Zw) = 4· len(w) + dimR(B).
We will see later that the entries of V give coordinates on the Bruhat cells of
quaternionic ﬂags.
Denoting conjugate transpose by ( ·)∗, we have the Lie group:
Sp(n) :={g∈ GLn(H)| g∗g = e}
We also identify the corresponding Lie algebra:
spn :={X∈ gln(H)|X +X ∗ = 0}
with TxSp(n) for x∈ GLn(H) by left translation. One knows that matrices in
Sp(n) have Dieudonn´ e determinant 1, and thus lie inside the semi-simple group:
SL(n) :={g∈ GLn(H)| det(g) = 1}.
We deﬁne the spheroid to be Σ := Sp(1)n≃ (S3)n, whose elements are of the
form diag(exp(s1),..., exp(sn)) where the si are purely quaternionic (no real
component). This is a subgroup of D, and we have, in fact, that:
D = Σ ×R
We denote the corresponding Lie algebra by s. The full quaternionic ﬂag of Hn,
which we denote Fn, can now be identiﬁed as Fn≃ Σ\Sp(n)≃B\ GLn(H).
Using the second identiﬁcation of Fn, we denote Cw :=B\Zw, which we call
the Bruhat cells of the ﬂag. By our discussion above, we see that dimR(Cw) =
4· len(w).
Example. Consider the space HP1 identiﬁed as HP1 ≃ Σ\Sp(2)≃ S4 from
which we obtain the ﬁbration:
Σ≃S3×S3≃ Sp(1)× Sp(1) → Sp(2)
↓
HP1≃S4
.
The Bruhat decomposition yeilds a decomposition of Σ \Sp(2)≃ HP1 into
the cellsC(12) andCe which have real dimensions 4 and 0 respectively. We view
the cells under the identiﬁcations that C(12)≃N 2 =
(
1 ∗
0 1
)
≃ H andCe is
the North pole.
Recall that S4 has neither a symplectic nor a complex structure (nor even an
almost complex [13]). This is one of the reasons for introducing the te traplectic
structure in [6]. ©
