---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-022-82-a-technical-lemma
section_title: "A technical lemma."
section_number: 8.2
pages: 54-55
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
A technical lemma.
Let us prove a lemma which shows what the techniques developed so far can
be good for. It will be crucial in our treatment of Tomita-Takesaki theory.
It is a “Radon-Nikodym” type theorem inspired by one due to Sakai([]).
ﬁnd reference
Lemma 8.2.1. Let λ ∈R+ be given and let φ be a faithful ultraweakly
continuous state on a von Neumann algebra M. Let ψ ∈M∗be such that
|ψ(y∗x)| ≤
p
φ(x∗x)
p
φ(y∗y). Then there is an a ∈M1/2 (elements of norm
≤1/2) so that
ψ(x) = λφ(ax) + λ−1φ(xa).
Proof. For a ∈M let θa(x) = φ(λax + λ−1xa). Then the map α : M →M∗,
α(a) = θa, is continuous for the topologies of duality between M and M∗.
But we know that this topology on M is the ultraweak topology so that
α(M1) is a compact convex set. By contradiction suppose that ψ is not in
α(M).
Then by Hahn-Banach there is an h ∈M with ℜ(ψ(h)) > D where
D = supa∈M1/2 ℜ(θa(h)). But if h = u|h| = |h∗|u is the polar decomposition
of h, we have
θu∗/2(h) = 1/2(λφ(|h|) + λ−1φ(|h∗|))
so that
2D ≥λφ(|h|) + 1
λφ(|h∗|) ≥2
p
φ(|h|)
p
φ(|h∗|).
But also D < |ψ(h)| = |ψ(u|h|1/2|h|1/2)| ≤
p
φ(|h|)
p
φ(u|h|u∗), a contradic-
tion.
54
Chapter 9
Standard form of a II1 factor and
II∞factors.
