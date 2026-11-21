---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-100-c2-matricial-description-of-difference-modules
section_title: "Matricial description of difference modules"
section_number: C.2
pages: 148-149
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
Here, we
assume that the K-module E is free of ﬁnite rank n. This assumption will
be maintained in A.3.3 and A.4.2, where we pursue the matricial description.
We then see that the diﬀerence module M = (E, Φ) is then isomorphic to
some (Kn, ΦA) (example A.2.2).
Indeed, choosing a basis B allows one to
identify E with Kn. It is then clear that Φ(B) is also a basis of E, whence
the existence of A ∈GLn(K) such that Φ(B) = BA−1. If x ∈E has the
coordinate column vector X ∈Kn in basis B, i.e. if x = BX, computing
Φ(x) = Φ(BX) = Φ(B)σ(X) = BA−1σ(X) shows that Φ(x) ∈E has the
A.3. FINITELY FILTERED DIFFERENCE MODULES
143
coordinate column vector A−1σ(X); we thus may identify (E, Φ) ≃(Kn, ΦA),
where ΦA(X) := A−1σ(X).
Morphisms from (Kn, ΦA) to (Kp, ΦB) are matrices F ∈Matp,n(K) such
that (σF)A = BF and their composition boils down to matrix product. In
particular, isomorphism of modules is described by gauge transformations:
(Kn, ΦA) ≃(Kp, ΦB) ⇐⇒n = p and ∃F ∈GLn(K) : B = F[A] := (σF)AF −1.
Remark A.3.1. — A similar description can be given for free modules of
inﬁnite rank. Such a K-module is isomorphic to K(I), and one should replace
GLn(K) by GLI(K) and Matp,n(K) by MatJ×I(K). Inﬁnite “matrices” are
to be understood as follows: elements of EndK(K(I)) are families (ai,j) of
elements of K indexed by I × I and such that each column (j ﬁxed) has ﬁnite
support. The set MatI(K) := EndK(K(I)) is a unitary ring and GLI(K) :=
AutK(K(I)) is its group of units. There is a similar condition for MatJ×I(K).
