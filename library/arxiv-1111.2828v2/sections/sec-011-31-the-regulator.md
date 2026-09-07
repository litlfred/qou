---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-011-31-the-regulator
section_title: "The regulator"
section_number: 3.1
pages: 12-13
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
z as [z; p, q] =
(
log(z) + pπi, log(1 − z) + qπi
)
, where p, q ∈ Z are even integers. There is a well
deﬁned regulator map
(3.6)
R : ˆP(C) → C/4π2Z,
[z; p, q] ↦→Li2(z) + 1
2 (log(z) + pπi)(log(1 − z) − qπi) − π2/6.
3.2. The PSL(2, C)-variant of the extended Bloch group. There is another variant of the
extended Bloch group using ﬂattenings [z; p, q], where p and q are allowed to be odd. This group is
deﬁned as above using the set
(3.7) ˆCodd =
{
(e, f) ∈ C2⏐⏐ ± exp(e) ± exp(f ) = 1
}
,
and ﬁts in a diagram similar to ( 3.5). We use a subscript PSL to denote the variant allowing odd
ﬂattenings. We have an exact sequence
(3.8) 0 /d47/d47 Z/4Z /d47/d47 ˆB(C) /d47/d47 ˆB(C)PSL /d47/d47 0.
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 13
For odd ﬂattenings, the regulator ( 3.6) is well deﬁned modulo π2Z.
Theorem 3.3 (Neumann [ 20], Goette-Zickert [ 16]). There are natural isomorphisms
(3.9) H3(PSL(2, C)) ∼= ˆB(C)PSL, H 3(SL(2, C)) ∼= ˆB(C)
such that the Cheeger-Chern-Simons classes agree with the r egulators. □
The following result is needed in Section 7. The ﬁrst part is proved in Zickert [ 29, Lemma 3.16],
and the second has a similar proof, which we leave to the reade r.
Lemma 3.4. For (e, f) ∈ˆC and p, q ∈ Z, we have
(e + 2πip, f + 2πiq) − (e, f) = χ(qe − pf + 2pqπi) ∈ ˆP(C),(3.10)
(e + πip, f + πiq) − (e, f) = χ(qe − pf + pqπi) ∈ ˆP(C)PSL.(3.11) □
3.3. Arbitrary ﬁelds. In Zickert [ 29], extended Bloch groups ˆBE(F ) and ˆBE(F )PSL are deﬁned
for an arbitrary ﬁeld F and a primitive extension E of F ∗ by Z. The deﬁnitions are as above using
the sets
(3.12) ˆEF =
{
(e, f) ∈ E2⏐⏐ π(e) + π(f ) = 1
}
, (ˆEF )odd =
{
(e, f) ∈ E2⏐⏐ ±π(e) ± π(f ) = 1
}
.
If F is a number ﬁeld, the extended Bloch groups are up to canonical isomorphism independent of
the choice of extension, so we may omit the subscript E.
Theorem 3.5 (Zickert [29, Theorem 1.1]) . Let F be a number ﬁeld. There is a natural isomorphism
(3.13) K ind
3 (F ) ∼= ˆB(F )
respecting Galois actions. □
Corollary 3.6 (Zickert [ 29, Corollary 7.14]) . For each embedding τ : F → C, the induced map
τ : ˆB(F ) → ˆB(C) is injective. □
Corollary 3.7 (Galois descent; Zickert [ 29, Corollary 7.15]) . Let F2 : F1 be an extension of number
ﬁelds. An element in ˆB(F2) is in ˆB(F1) if and only if it is invariant under all automorphisms of F2
over F1. □
