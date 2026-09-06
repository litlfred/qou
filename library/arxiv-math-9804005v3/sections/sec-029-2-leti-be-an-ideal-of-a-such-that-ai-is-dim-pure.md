---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-029-2-leti-be-an-ideal-of-a-such-that-ai-is-dim-pure
section_title: "LetI be an ideal of A such that A/I is dim-pure and let q be a prime ideal of"
section_number: 2
pages: 15-16
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
A that is minimal over I. Then dimA/q = dimA/I.
Proof. This is completely analogous to [KL] 9.6 and 9.5.
Recall from [GL] that Spec A is said to have normal separation provided that
for any pair prime ideals p ⫋ q, the factor q/p contains a nonzero normal element
of A/p. Under the assumptions of the lemma we say that Tauvel’s height formula
holds in A provided
height p + dimA/p = dimA
for all primes p.
Theorem 2.22. Suppose that A is a noetherian k-algebra,R is an Auslander du-
alizing complex over A and CdimR is weakly symmetric. Let p ⫋ q be prime ideals
ofA with height q/p = 1. If there exists an element a ∈ q − p that is normal modulo
p, then CdimRA/p = CdimRA/q + 1.
Proof. Use the proof of [GL] Theorem 1.4, but replace GKdim by Cdim R, and use
Lemma 2.21 instead of [Len] Lemmas 2 and 3.
Theorem 2.23. Suppose that A is a noetherian k-algebra,R is an Auslander du-
alizing complex over A and CdimR is weakly symmetric. If SpecA is normally
separated, then A is catenary. If in addition A is prime, then Tauvel’s height for-
mula holds.
Proof. The proof of [GL] Theorem 1.6 works here after we replace GKdim by
CdimR.
We call attention to Question 3.15 regarding the possible symmetry o f CdimR.
The Macaulay property of [SZ] is adapted in the following way, to be us ed later
in the paper.
Deﬁnition 2.24. Suppose R is an Auslander dualizing complex over A. Let dim
be an exact dimension function on ﬁnitely generated A-modules. If there is some
integerc such that
dimM = CdimRM +c
for all M ∈ ModfA, then we say R is Macaulay with respect to dim, or that R is
dim-Macaulay.
Note that if R =A, then “GKdim-Macaulay” is equivalent to “Cohen-Macaulay”
as it is used in [Bj], [Lev], [ASZ], and [SZ]. This is because GKdim M +jR(M ) =
c = dimA in this case.
Example 2.25. IfA is a commutative aﬃne k-algebra and R is any central dual-
izing complex over A, then R is Auslander and GKdim-Macaulay. In this case we
also have Kdim M = GKdimM for all ﬁnitely generated A-modules M .
