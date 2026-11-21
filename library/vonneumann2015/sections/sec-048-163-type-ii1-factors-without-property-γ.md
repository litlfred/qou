---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-048-163-type-ii1-factors-without-property-γ
section_title: "Type II1 factors without property Γ."
section_number: 16.3
pages: 114-120
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Type II1 factors without property Γ.
Theorem 16.3.1. Let Γ be an icc group possessing a subset ∆not containing
the identity and three elements α, β and γ such that
(a)Γ = {1} ∪∆∪α∆α−1
(b)∆, β∆β−1 and γ∆γ−1 are mutually disjoint.
then for x ∈vN(Γ),
||x −tr(x)id||2 ≤14 max{||[x, uα]||2, ||[x, uβ]||2, ||[x, uγ]||2}.
Proof. Write x as P
ν∈Γ xνuν. We will frequently use the formula
||[x, uρ]||2
2 = ||uρ−1xuρ −x||2 =
X
ν∈Γ
|xν −xρνρ−1|2.
By replacing x by x −tr(x)id it suﬃces to prove the result if tr(x) = 0
and we may suppose ||x||2 = 1 so that for such an x we must show 1 ≤
14 max{||[x, uα]||2, ||[x, uβ]||2, ||[x, uγ]||2}.
We ﬁrst make a simple estimate. If Λ is any subset of Γ and ρ ∈Γ then
|
X
ν∈Λ
|xν|2 −
X
ν∈Λ
|xρνρ−1|2|
=
X
ν∈Λ
(|xν| + |xρνρ−1|)||xν| −|xρνρ−1||
≤
X
ν∈Λ
(|xν| + |xρνρ−1|)(|xν −xρνρ−1|)
≤
2||x||2(
X
ν∈Λ
|xν −xρνρ−1|2)1/2
114
so that if ρ ∈{α, β, γ} we have
|
X
ν∈Λ
|xν|2 −
X
ν∈Λ
|xρνρ−1|2| ≤2ϵ
where ϵ = max{||[x, uα]||2, ||[x, uβ]||2, ||[x, uγ]||2}.
Let us now ﬁrst overestimate ||x||2 = 1:
1
≤
X
ν∈∆
|xν|2 +
X
ν∈∆
|xανα−1|2
≤
2
X
ν∈∆
|xν|2 + 2ϵ.
Now underestimate it:
1
≥
X
ν∈∆
|xν|2 +
X
ν∈∆
|xβνβ−1|2 +
X
ν∈∆
|xγνγ−1|2
≥
3
X
ν∈∆
|xν|2 −4ϵ.
Let y = P
ν∈∆|xν|2 and eliminate y from the inequalities 1 ≤2y +2ϵ and
1 ≥3y −4ϵ to obtain
ϵ ≥1/14
as desired.
It is easy to come up with groups having subsets as in the previous the-
orem. For instance if G = F2, free on generators g and h, let ∆be the set
of all reduced words ending in a non-zero power of g. Let α = g, β = h and
γ = h−1. The same works for more than two generators. We conclude:
Theorem 16.3.2. The type II1 factor vN(Fn) for n ≥does not have property
Γ.
115
116
Chapter 17
Bimodules and property T
117
118
Chapter 18
Fermions and Bosons:CAR and
CCR
According to physics lore, the states of a quantum system are given by (the
one-dimensional subspaces of) a Hilbert space H and if two systems have
state spaces H and K, the joint system has state space H ⊗K. Fermions
are particles such that "the wave function of several fermions is antisymmet-
ric" which means that it is the antisymmetric tensor product ΛnH which
describes n identical fermions. Bosons are particles whose wave functions
are symmetric so it is the symmetric tensor power SnH which describes n
identical bosons.
In order to treat families with an unlimited number of
fermions and Bosons we need the fermionic and bosonic Fock spaces (which
are Hilbert space direct sums):
F(H) = ⊕∞
n=0ΛnH
and
S(H) = ⊕∞
n=0SnH.
The passage from H to F(H) or S(H) is known as “second quantisation’.
We will not attempt to explain the physics above but will deﬁne properly
these two Fock spaces and how they give rise to interesting von Neumann
algebras related to physics.
Both these Fock spaces are subspaces of the "full Fock space" or tensor
algebra
T (H) = ⊕∞
n=0 ⊗n H
T (H) is related to quantum physics also though so far in a less funda-
mental way through the large N behaviour of random N × N matrices and
Voiculescu’s free probability.
119
