---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-017-2-the-other-cases-x-x1-x2-or-x3-are-similar-2
section_title: "The other cases X =X1, X2 or X3 are similar. 2"
section_number: 2
pages: 20-21
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 27 sections: ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE"
---
4.0.2. Proof of Step 2. Consider QH-tetrahedra (∆,b, w), (∆′,b′, w′) glued along a 2-face F . Denote
as usual by Fs, Ft the abstract 2-faces of ∆, ∆ ′ corresponding to F . Recall that the vertices v0, v1,
v2 ofFs andFt are ordered by the branchings b andb′ respectively; the gluing Fs→Ft is encoded by
an even permutation p :=σr(F) of the vertices, where σ is the 2-cycle (v0v1v2) and r(F )∈ Z/3Z.
Assume that a standard representation of the triangle algebra ρs :T →End(CN) is given on Fs,
where the generators Y0 labels the edge [v0,v 1], and Y1 labels the edge [v0,v 2]. Using the gluing, ρs
is the pull-back of a standard representation ρt :T →End(CN) on Ft, where now Y0 labels the edge
[vp(0),vp(1)], and Y1 labels the edge [vp(0),vp(2)]. So Yi on Fs corresponds to Yp−1(i) on Ft.
We have:
Lemma 4.3. The endomorphism (QT
N)r(F) intertwins ρs and ρt. Namely, for all X inT we have
(QT
N)r(F)◦ρs(X) =ρt(X)◦ (QT
N)r(F).
Proof. It is enough to check this on generators, where it follows fromQT
NAi(QT
N)−1 =Ai−1 (indices
mod(3)). This is straightforward to check. 2
Note thatQN has order 3 up to multiplication by 4-th roots of 1 (see [5], Lemma 7.3: if N = 2n+1,
we haveQ3
N =φ−1
N IN, where φN =
(n+1
N
)
if N≡ 1 mod(4), and φN =
(n+1
N
)
i if N≡ 3 mod(4)).
4.0.3. Proof of Step 3. Let (TCφ,˜b, w) be a layered QH-triangulation of the cylinder Cφ as usual.
Recall that for everyj∈{ 0,...,k }, the triangulated surface (S,λj) inherits a weak branching ˜bj from
its positive side in (T, ˜b, w). Order as τj
1,...,τ j
2m the branched abstract triangles of (λj,˜bj). For every
i∈{ 1,..., 2m}, order as ei
0, ei
1, ei
2 the edges of the triangle τj
i , as described before Proposition 4.1
and Lemma 4.3. Label ei
k with the generator Yi
k of a copy of the triangle algebra T .
Assume that for some j∈{ 0,...,k } we are given a standard local representation
ρj = (ρj
1⊗... ⊗ρj
2m)◦iλj : Tq
λj
→ End((CN)⊗2m)
where the standard representations ρj
i :T → End(CN) are associated to the triangles τj
i . As in
(18), put ρj
i(Yk) := yj
i,kAk. By the very deﬁnition of iλj (see (17)), for any edge es of λj, with edge
generator Xs∈ Tq
λj
, we have (as usual we denote a monomial ⊗jAj inT⊗2m by omitting the terms
Aj = 1):
(a) ρj(Xs) = yj
li,ai
yj
ri,bi
Ali
ai⊗Ari
bi
, if es is an edge of two distinct triangles τj
li
and τj
ri, and eli
ai,
eri
bi
are the edges of τj
li
, τj
ri respectively identiﬁed to es.
