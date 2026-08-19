---
doc_id: hdr
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-006-schur-elements-and-the-a-function
section_title: "Schur elements and the a-function"
section_number: null
pages: 21-23
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "HAL Id: tel-01411063 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: Algebras of"
---
From now on, set R := Z[q,q−1] and let K⊆ C be a ﬁeld such that he algebra K(q)Hq(W,L ) is split
semisimple.
Using the standard basis of the Iwahori–Hecke algebra, we deﬁne the linear map τ :Hq(W,L )→R
by setting
τ(Tw) :=
{ 1 if w = 1,
0 otherwise .
18
The map τ is a symmetrising form onHq(W,L ), and the elements (Tw−1)w∈W form a basis ofHq(W,L )
dual to the standard basis with respect to τ (that is,τ(Tw−1Tw′) =δw,w′) [GePf, Proposition 8.1.1]. The
map τ is called the canonical symmetrising form onHq(W,L ), because it specialises to the canonical
symmetrising form on the group algebra Z[W ] when q↦→ 1.
Now, the map τ can be extended to K(q)Hq(W,L ) by extension of scalars. By Tits’s deformation
theorem, the specialisation q ↦→ 1 induces a bijection between the set of irreducible representations
Irr(K(q)Hq(W,L )) of K(q)Hq(W,L ) and the set of irreducible representations Irr( W ) of W . For E∈
Irr(W ), we will denote by VE the corresponding irreducible representation of K(q)Hq(W,L ) and by sE
the Schur element ofHq(W,L ) associated with VE. We have sE∈ ZK[q,q−1] for all E∈ Irr(W ), where
ZK denotes the integral closure of Z in K.
Example 2.4 The irreducible representations of the symmetric group Sn are parametrised by the par-
titions ofn. For W = S3, there are three irreducible representations. Let E(3),E(2,1) andE(1,1,1) denote
respectively the trivial, reﬂection and sign representation of S3. Using again the notation of Example
2.1, we have
sE(3) = (q2l + 1)(q4l +q2l + 1), sE(2,1) =q2l + 1 +q−2l, sE(1,1,1) = (q−2l + 1)(q−4l +q−2l + 1).
We can deﬁne the functions a : Irr(W )→ Z and A : Irr(W )→ Z by setting
a(E) :=−valuationq(sE) and A(E) :=−degreeq(sE).
Note that both functions depend on L. For brevity, we will write aE for a(E) and AE for A(E).
Example 2.5 Following Example 2.4, for W = S3, we have
aE(3) = 0, aE(2,1) = 2l, aE(1,1,1) = 6l and AE(3) =−6l, AE(2,1) =−2l, AE(1,1,1) = 0.
The Schur elements ofHq(W,L ) have been explicitly calculated for all ﬁnite Coxeter groups:
• for type An by Steinberg [St1],
• for type Bn by Hoefsmit [Ho],
• for type Dn by Benson and Gay [BeGa] (it derives from type Bn with the use of Cliﬀord theory),
• for dihedral groups I2(m) by Kilmoyer and Solomon [KiSo],
• for F4 by Lusztig [Lu1],
• for E6 and E7 by Surowski [Su],
• for E8 by Benson [Be],
• for H3 by Lusztig [Lu2],
• for H4 by Alvis and Lusztig [AlLu].
There have been other subsequent proofs of the above results. For example, Iwahori–Hecke algebras of
typesAn andBn are special cases of Ariki–Koike algebras, whose Schur elements have been independently
obtained by Geck–Iancu–Malle [GIM] and Mathas [Mat].
A case-by-case analysis shows that the Schur elements of Hq(W,L ) can be written in the form
sE =ξEq−aE
∏
Φ∈CycE
Φ(qnE,Φ) (2.2)
whereξE∈ ZK,nE,Φ∈ Z>0 and CycE is a family of K-cyclotomic polynomials (see [GePf, Chapters 10
& 11], [Ch4, Theorem 4.2.5 & Proposition 4.3.5]).
Example 2.6 Following Example 2.4, for W = S3, we have
sE(3) = Φ2(q2l)Φ3(q2l), sE(2,1) =q−2lΦ3(q2l), sE(1,1,1) =q−6lΦ2(q2l)Φ3(q2l),
where Φn denotes the n-th Q-cyclotomic polynomial.
19
