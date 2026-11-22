---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-008-22-fixed-points-and-ffpf-knots
section_title: "Fixed points and ffpf knots"
section_number: 2.2
pages: 8-10
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Vela-Vick proved in [BVV18] that
dim [
HFK(K, g −1) ≥1.
We will focus on knots for which equality is achieved, motivating the following definition:
Definition 2.6. A knot K ⊂S3 is ffpf (for “fibered and fixed-point-free”) if it is fibered of some
genus g ≥1, and
dim [
HFK(K, g −1) = 1.
We will justify this terminology in Proposition 2.9, which says that if a knot is ffpf then no pseudo-
Anosov component of its monodromy can have fixed points.
This class of knots includes all nontrivial L-space knots and most almost L-space knots [BS24a],
where K ⊂S3 is said to be an almost L-space knot if
dim d
HF(S3
m(K)) = m + 2
for sufficiently large integers m:
L-SPACES AND KNOT TRACES
9
Lemma 2.7. Any nontrivial L-space knot, or almost L-space knot of genus g ≥3, is ffpf.
Proof. L-space knots are fibered [Ghi08, Ni07], with dim [
HFK(K, g −1) ≤1 [OS05, Theorem 1.2].
Almost L-space knots of genus g ≥2 are fibered [BS24a, Proposition 3.9], and if g ≥3 then the
inequality dim [
HFK(K, g −1) ≤1 follows from [BS24a, Remark 3.12]; see also [Bin23]. The lemma
then follows from Baldwin–Vela-Vick’s inequality in the other direction [BVV18].
□
Lemma 2.8. If K is an ffpf knot, then it is prime, it is not a (±1, q)-cable for any q ≥2, and its
monodromy is veering.
Proof. Suppose K has genus g ≥1. If K were a nontrivial connected sum, then the proof of [BVV18,
Corollary 1.4] would show that dim [
HFK(K, g−1) ≥2. If instead K were the (±1, q)-cable of some
companion knot C, with q ≥2, then their Alexander polynomials would satisfy
∆K(t) = ∆C(tq),
with nonzero ti-coefficient only when i is a multiple of q; but then g = q · g(C) implies that ∆K(t)
has tg−1-coefficient ag−1 = 0, and so
dim [
HFK(K, g −1) ≡χ( [
HFK ∗(K, g −1)) = ag−1 = 0
(mod 2).
In either case, this contradicts dim [
HFK(K, g−1) = 1, so K must be prime and not a (±1, q)-cable.
Lastly, the monodromy of K is veering by [Ni20, Theorem A.1].
□
The ffpf condition has the following geometric consequence, which in combination with Theorem
2.4 will ultimately let us recover a ffpf knot from its 0-surgery in the next subsection:
Proposition 2.9. Let K be a ffpf knot with monodromy h : Σ →Σ, and let (φ, Γ) be the Nielsen–
Thurston form of h. Then for each pseudo-Anosov component S of Σ \ Γ that is fixed setwise by
φ, the restriction of φ to S is freely isotopic to a pseudo-Anosov map with no fixed points.
Proof. Suppose that K has genus g ≥1. In the proof of [Ni22, Theorem 1.2], Ni constructs a closed
surface P = Σ ∪Σ′ and a homeomorphism σ : P →P such that
• σ|Σ = h, which implies in particular that σ fixes ∂Σ pointwise;
• σ|Σ′ is the monodromy of some fibered cable knot L′ ⊂S1 × S2;
• the symplectic Floer homology of the mapping class of σ is given by
dim HF symp(P, σ) = dim [
HFK(K, g −1) −1;
• if (φ′, Γ′) is the Nielsen–Thurston form of σ|Σ′, then
(φ ∪φ′, Γ ∪∂Σ ∪Γ′)
is the Nielsen–Thurston form of σ.
Cotton-Clay describes how to compute the symplectic Floer homology of a mapping class in [CC09,
Theorem 4.2]; see also [Ni22, Theorem 1.3]. Most importantly for us, interior fixed points of pseudo-
Anosov components contribute linearly independent elements to Floer homology. In particular, if
S is a pseudo-Anosov component of Σ \ Γ and hence of P \ (Γ ∪∂Σ ∪Γ′), with φ(S) = S, and if
φ|S = (φ ∪φ′)|S
is freely isotopic to a pseudo-Anosov map with m fixed points, then
m ≤dim HF symp(P, σ).
10
JOHN A. BALDWIN AND STEVEN SIVEK
The ffpf condition on K, combined with the third item above, then says that
m ≤dim HF symp(P, σ) = dim [
HFK(K, g −1) −1 = 0.
Therefore, m = 0 as claimed in the proposition.
□
