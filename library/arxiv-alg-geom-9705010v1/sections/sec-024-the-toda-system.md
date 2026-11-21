---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-024-the-toda-system
section_title: "The Toda system"
section_number: null
pages: 31-32
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
A simple way to describe the Toda system is via the construction of Adler-
Kostant-Symes. Start with a decomposition g = a ⊕b of a Lie algebra g as vector
space direct sum of two of its subalgebras a, b. This induces a dual decomposition
g∗= a∗⊕b∗, an injection i := b∗֒ →g∗, and a projection π : g ։ b. Let Ox ⊂b∗
denote the coadjoint orbit of some x ∈b∗. The image i(Ox) ⊂g∗has, in general,
nothing to do with the coadjoint orbit Oi(x) of i(x) in g∗. So i∗of a G-invariant
function f on g∗can be a complicated, non-constant function on Ox. The AKS claim
is that any two such, i∗f1 and i∗f2, Poisson commute with respect to the natural
(Kirillov-Kostant) symplectic structure σOx on Ox. Indeed, let vj ∈g correspond
to the diﬀerential dfj|i(x) ∈g∗∗= g, so i∗dfj is given by π(vj). G-invariance of fj
implies that vj is conormal to Oi(x), i.e. that
0 = ⟨i(x), [g, vj]⟩.
We set aj := vj −π(vj) ∈a, and compute:
{i∗f1, i∗f2}Ox = σOx(πv1, πv2)
= ⟨x, [π(v1), π(v2)]b⟩
= ⟨i(x), [π(v1), π(v2)]g⟩
= ⟨i(x), [v1, π(v2)]g⟩−⟨i(x), [a1, π(v2)]g⟩
= ⟨i(x), [v1, π(v2)]⟩−⟨i(x), [a1, v2]⟩+ ⟨i(x), [a1, a2]⟩.
We have just seen that the ﬁrst two terms vanish when f1, f2 are G-invariant, and
the third term vanishes since it pairs i(x) ∈b∗= a⊥with [a1, a2] ∈a. This proves
AKS.
A shifted version of AKS is very convenient in applications. Replace the in-
clusion i : b∗֒ →g∗by its shifted version ǫ + i, where ǫ is an element of g∗which
annihilates [a, a] and [b, b]. The above argument goes through verbatim. For exam-
ple, take g = sl(n), a = strictly lower triangular matrices, b = upper triangulars,
