---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-033-2-dt-is-dense-iﬀt-is-preclosed-in-that-case-t-t
section_title: "D(T ∗) is dense iﬀT is preclosed. In that case T = T ∗∗."
section_number: 2
pages: 87-88
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
3. If T is preclosed then (T)∗= T ∗.
Proof. Note that (η, σ) ∈Γ(T ∗) iﬀ< Tξ, η >=< ξ, σ > for all ξ ∈D(T)
iﬀ< (−Tξ, ξ), (η, σ) >= 0. Hence
Γ(T ∗) = {(−Tξ, ξ) : ξ ∈D(T)}⊥= (uΓ(T))⊥= uΓ(T)⊥,
where u : H ⊕H →H ⊕H is the unitary operator u(ξ, η) = (−η, ξ). Now:
1. Orthogonal complements are closed, hence Γ(T ∗) is closed.
2. Γ(T) = (Γ(T)⊥)⊥= u∗Γ(T ∗)⊥, so
(0, ξ) ∈Γ(T)
⇔
(−ξ, 0) ∈Γ(T ∗)⊥
⇔
0 =< (−ξ, 0), (η, T ∗η) >= −< ξ, η > for all η ∈D(T ∗)
⇔
ξ ∈D(T ∗)⊥.
Hence T is preclosed iﬀD(T ∗)⊥= {0} iﬀD(T ∗) is dense.
In that case Γ(T ∗∗) = uΓ(T ∗)⊥= u2Γ(T)⊥⊥= −Γ(T) = Γ(T), so
T ∗∗= T.
3. T ∗= T ∗= T ∗∗∗= (T)∗.
Deﬁnition 12.1.17. An operator T is symmetric if T ⊂T ∗. Equivalently
< Tξ, η >=< ξ, Tη > for all ξ, η ∈D(T). T is self-adjoint if T = T ∗. A
self-adjoint operator T is positive if < Tξ, ξ >≥0 for all ξ ∈D(T).
87
12.2
