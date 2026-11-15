---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-006-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-6
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
2.1. The Ising model. We consider the Ising model on a ﬁnite subset Λ of Zd. We use the notation
of [10], that we deﬁne now.
Let EΛ := {{i, j} ⊂Λ : ∥i −j∥1 = 1} be the set of nearest neighbour pairs in Λ. (Here, and through-
out the paper, ∥i −j∥1 denotes the graph distance in Zd between two points i and j.) To each spin
conﬁguration ω, we associate its Hamiltonian
HΛ;β,h(ω) := −β
X
{i,j}∈EΛ
σi(ω)σj(ω) −h
X
i∈Λ
σi(ω),
where β ≥0 and h are two real parameters, respectively called inverse temperature and magnetic ﬁeld.
The probability of a spin conﬁguration ω is given by the Gibbs distribution
µΛ;β,h(ω) :=
1
ZΛ;β,h
e−HΛ;β,h(ω),
where
ZΛ;β,h :=
X
ω∈{−1,1}Λ
e−HΛ;β,h(ω)
is called the partition function.
The quantities deﬁned so far are with “free boundary conditions”, which means that the value of
the spins outside of Λ is not taken into consideration. We can also deﬁne the same quantities with
boundary condition, by considering the Ising model on the full lattice Zd, but where the values of the
spins outside of Λ are ﬁxed. Fixing a spin conﬁguration η ∈{−1, 1}Zd, we deﬁne a spin conﬁguration
in Λ with boundary condition η as an element of the set
Ωη
Λ :=
n
ω ∈{−1, 1}Zd : ωi = ηi, ∀i /∈Λ
o
.
We now deﬁne the Hamiltonian as
Hη
Λ;β,h(ω) := −β
X
{i,j}∈Eb
Λ
σi(ω)σj(ω) −h
X
i∈Λ
σi(ω),
where Eb
Λ :=

{i, j} ⊂Zd : ∥i −j∥1 = 1 and {i, j} ∩Λ̸ = ∅
	
.
The Gibbs distribution of the Ising model in Λ with boundary condition η and parameters β and h
is the probability distribution deﬁned on Ωη
Λ by
µη
Λ;β,h(ω) :=
1
Zη
Λ;β,h
e−Hη
Λ;β,h(ω),
where
Zη
Λ;β,h :=
X
ω∈Ωη
Λ
e−Hη
Λ;β,h(ω)
is the partition function with boundary condition η.
The most classical boundary conditions are the + boundary condition, where ηi = +1 for all i ∈Zd,
and the −boundary condition, where ηi = −1 for all i ∈Zd. When considering quantities with +
(resp. −) boundary condition, we write them with superscript + (resp. −), e.g. µ+
Λ;β,h(ω).
6
JEHANNE DOUSSE AND VALENTIN F´ERAY
We now take an increasing sequence Λn of ﬁnite subsets of Zd with S
n≥1 Λn = Zd. It is a well-
known fact (see, e.g., [10, Chapter 3]) that the sequence of measures µ+
Λn;β,h converges in the weak
sense towards a measure denoted µ+
β,h as n →∞. In the high temperature case (β < βc(d), h = 0)
or in the presence of a magnetic ﬁeld (h̸ = 0), the limiting measure is independent of the choice of
boundary conditions. At low temperature (β > βc(d), h = 0), the limiting measure depends on the
boundary conditions; in this article, we restrict ourselves to + boundary conditions to have a well-
deﬁned limiting measure in all cases. Also, we drop the superscript + and denote the limiting measure
by µβ,h.
In this article, we work with this limiting measure µβ,h and prove our central limit theorem under
this measure. In comparison with the measure µ+
Λn;β,h, it has the advantage to be translation invariant,
which simpliﬁes in particular the variance estimates.
