---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-007-41-preliminaries-the-sign-determined-torsion-of
section_title: "Preliminaries: the sign-determined torsion of a CW-complex"
section_number: 4.1
pages: 12-14
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
sic notions and results about the sign–determined Reidemei ster torsion introduced by Tu-
raev which are needed in this paper. Details can be found in Mi lnor’s survey [Mil66] and
in Turaev’s monograph [Tur02].
Torsion of a chain complex. Let C∗ = (0 /d47/d47
Cn
dn /d47/d47Cn−1
dn−1 /d47/d47···
d1 /d47/d47C0 /d47/d470) be a
chain complex of ﬁnite dimensional vector spaces over C. Choose a basis ci of Ci and
a basis hi of the i-th homology group Hi = Hi(C∗). The torsion of C∗ with respect to these
choices of bases is deﬁned as follows.
Let bi be a sequence of vectors in Ci such that di(bi) is a basis of Bi−1 = im(di : Ci→
Ci−1) and let ~hi denote a lift of hi in Zi = ker(di : Ci → Ci−1). The set of vectors
di+1(bi+1)~hibi is a basis of Ci. Let [ di+1(bi+1)~hibi/ci]∈ C∗ denote the determinant of the
transition matrix between those bases (the entries of this matrix are coordinates of vectors
in di+1(bi+1)~hibi with respect to ci). The sign-determined Reidemeister torsion of C∗ (with
respect to the bases c∗ and h∗) is the following alternating product (see [Tur01, Deﬁnition
3.1]):
(23) Tor( C∗, c∗, h∗) = (−1)|C∗|·
n∏
i=0
[di+1(bi+1)~hibi/ci](−1)i+1
∈ C∗.
12
Here
|C∗| =
∑
k/greaterorequalslant0
αk(C∗)βk(C∗),
where αi(C∗) = ∑i
k=0 dim Ck and βi(C∗) = ∑i
k=0 dim Hk.
The torsion Tor(C∗, c∗, h∗) does not depend on the choices of bi and ~hi. Note that if C∗
is acyclic (i.e. if Hi = 0 for all i), then|C∗| = 0.
Torsion of a CW-complex. Let W be a ﬁnite CW-complex and ρ be an SL2(C)-representa-
tion of π1(W). We deﬁne the sl2(C)ρ-twisted chain complex of W to be
C∗(W; sl2(C)ρ) = C∗(~W; Z)⊗Z[π1(W)] sl2(C)ρ.
Here C∗(~W; Z) is the complex of the universal cover with integer coe ﬃcients which is
in fact a Z[π1(W)]-module (via the action of π1(W) on ~W as the covering group), and
sl2(C)ρ denotes the Z[π1(W)]-module via the composition Ad◦ ρ, where Ad : SL 2(C)→
Aut(sl2(C)), A↦→AdA, is the adjoint representation. The chain complex C∗(W; sl2(C)ρ)
computes the sl2(C)ρ-twisted homology of W which we denote as Hρ
∗(W) = Hi(W; Ad◦ ρ).
Let
{
e(i)
1 , . . . ,e(i)
ni
}
be the set of i-dimensional cells of W. We lift them to the uni-
versal cover and we choose an arbitrary order and an arbitrar y orientation for the cells{
˜e(i)
1 , . . . ,˜e(i)
ni
}
. IfB ={a, b, c} is an orthonormal basis of sl2(C), then we consider the corre-
sponding basis over C
ci
B =
{
˜e(i)
1 ⊗ a, ˜e(i)
1 ⊗ b, ˜e(i)
1 ⊗ c, . . . ,˜e(i)
ni⊗ a, ˜e(i)
ni⊗ b, ˜e(i)
ni⊗ c
}
of Ci(W; sl2(C)ρ) = C∗(~W; Z)⊗Z[π1(W)] sl2(C)ρ. Now choosing for each i a basis hi of the
sl2(C)ρ-twisted homology Hρ
i (W), we can compute the torsion
Tor(C∗(W; sl2(C)ρ), c∗
B, h∗)∈ C∗.
The cells
{
˜e(i)
j
}
0⩽i⩽dim W,1⩽j⩽ni
are in one–to–one correspondence with the cells ofW, their
order and orientation induce an order and an orientation for the cells
{
e(i)
j
}
0⩽i⩽dim W,1⩽j⩽ni
.
Again, corresponding to these choices, we get a basis ci over R of Ci(W; R).
Choose an homology orientation of W, which is an orientation of the real vector space
H∗(W; R) =
⨁
i/greaterorequalslant0 Hi(W; R). Let o denote this chosen orientation. Provide each vector
space Hi(W; R) with a reference basis hi such that the basis
{
h0, . . . ,hdim W
}
of H∗(W; R) is
positively oriented with respect to o. Compute the sign–determined Reidemeister torsion
Tor(C∗(W; R), c∗, h∗)∈ R∗ of the resulting based and homology based chain complex and
consider its sign
τ0 = sgn (Tor(C∗(W; R), c∗, h∗))∈{± 1}.
We deﬁne the (sign–reﬁned) twisted Reidemeister torsion of W (with respect to h∗ and
o) to be
(24) TOR( W; sl2(C)ρ, h∗, o) = τ0· Tor(C∗(W; sl2(C)ρ), c∗
B, h∗)∈ C∗.
This deﬁnition only depends on the combinatorial class of W, the conjugacy class of ρ, the
choice of h∗ and the homology orientation o. It is independent of the orthonormal basisB
of sl2(C), of the choice of the lifts ˜e(i)
j , and of the choice of the positively oriented basis of
H∗(W; R). Moreover, it is independent of the order and orientation o f the cells (because
they appear twice).
One can prove that TOR is invariant under cellular subdivisi on, homeomorphism and
simple homotopy equivalences. In fact, it is precisely the s ign (−1)|C∗| in Eq. (23) which
ensures all these important invariance properties to hold.
13
