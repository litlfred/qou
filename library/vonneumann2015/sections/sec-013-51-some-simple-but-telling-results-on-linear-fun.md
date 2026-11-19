---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-013-51-some-simple-but-telling-results-on-linear-fun
section_title: "Some simple but telling results on linear functionals."
section_number: 5.1
pages: 31-32
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
functionals.
We begin with a result about linear functionals of independent interest.
Theorem 5.1.1. Let V be a subspace of B(H) and let φ : V →C be a linear
functional. The following are equivalent:
(i) There are vectors in H, ξ1, ξ2, ..., ξn and η1, η2, ..., ηn with
φ(x) =
n
X
i=1
⟨xξi, ηi⟩
(ii) φ is weakly continuous.
(iii) φ is strongly continuous.
Proof. (i) ⇒(ii) ⇒(iii) are obvious, so suppose φ is strongly continuous.
One may use the seminorms
pPn
i=1 ||aξi||2 as {ξ1, ξ2, ..., ξn} ranges over all
ﬁnite subsets of H to deﬁne the strong topology. Srong continuity implies
that there is an ϵ > 0 and {ξ1, ξ2, ..., ξn} such that
pPn
i=1 ||aξi||2 < ϵ implies
|φ(a)| ≤1. But then if
pPn
i=1 ||aξi||2 = 0 then multiplying a by large scalars
implies φ(a) = 0. Otherwise it is clear that |φ(a)| ≤1
ϵ
pPn
i=1 ||aξi||2.
Now let ξ = ξ1 ⊕...ξn ∈⊕iH and let K = (V ⊗1)(ξ).
Then deﬁne
˜φ on V ⊗1(ξ) by ˜φ(⊕ixξi) = φ(x).
Observe that ˜φ is well-deﬁned and
continuous so extends to K which means there is a vector η = ⊕ηi ∈K with
φ(x) = ˜φ(x ⊗1)(η) = ⟨(x ⊗1)(ξ), η⟩.
Exercise 5.1.2. Replace weak and strong by ultraweak and ultrastrong, and
the ﬁnite sequences of vectors by ℓ2-convergent ones in the previous theorem.
31
Corollary 5.1.3. If C is a convex subset of B(H), its weak and strong clo-
sures coincide.
Proof. Two locally convex vector spaces with the same continuous linear
functionals have the same closed convex sets. This is a consequence of the
Hahn-Banach theorem to be found in any text on functional analysis.
Corollary 5.1.4. If dim H = ∞the strong and ultrastrong topologies diﬀer
on B(H).
Proof. Let (ξi) be an orthonormal basis of H and let ω(x) = P
i
1
n2⟨xξi, ξi⟩.
Then ω is ultraweakly continuous but not strongly continuous. For if it were
weakly continuous it would be of the form Pn
i=1⟨xνi, ηi⟩and ω(p) = 0 where p
is the projection onto the orthogonal complement of the vector space spanned
by the νi. But by positivity ω(p) = 0 forces p(ξi) = 0 for all i.
