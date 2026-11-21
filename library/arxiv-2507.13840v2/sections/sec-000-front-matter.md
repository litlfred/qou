---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-000-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Quantifying mixed-state entanglement via partial transpose
and realignment moments
Poetri Sonya Tarabunga1,2 and Tobias Haug3
1Technical University of Munich, TUM School of Natural Sciences, Physics Department, 85748 Garching, Germany
2Munich Center for Quantum Science and Technology (MCQST), Schellingstr. 4, 80799 M¨unchen, Germany
3Quantum Research Center, Technology Innovation Institute, Abu Dhabi, UAE
Entanglement plays a crucial role in
quantum information science and many-
body physics, yet quantifying it in mixed
quantum
many-body
systems
has
re-
mained a notoriously difficult problem.
Here, we introduce families of quantita-
tive entanglement witnesses, constructed
from partial transpose and realignment
moments, which provide rigorous bounds
on entanglement monotones as well as en-
tanglement dimensionality. Our witnesses
can be efficiently measured using SWAP
tests or variants of Bell measurements,
thus making them directly implementable
on current hardware. Leveraging our wit-
nesses, we present several novel results on
entanglement properties of mixed states,
both in quantum information and many-
body physics.
We develop efficient algo-
rithms to test whether mixed states with
bounded entropy have low or high entan-
glement, which previously was only possi-
ble for pure states. We also provide an ef-
ficient algorithm to test the Schmidt rank
using only two-copy measurements, and
the operator Schmidt rank using four-copy
measurements. Further, our witnesses ro-
bustly certify the quantum circuit depth
in the presence of noise, as well as the
Schmidt rank of mixed states.
Finally,
we show that the entanglement phase di-
agram of Haar random states, quantified
by the partial transpose negativity, can
be fully established solely by computing
our witness, a result that also applies to
any state 4-design. Our witnesses can also
be efficiently computed for matrix prod-
Poetri Sonya Tarabunga: poetri.tarabunga@tum.de
Tobias Haug: tobias.haug@u.nus.edu
uct states, thus enabling the characteriza-
tion of entanglement in extensive many-
body systems. Finally, we make progress
on the entanglement required for quan-
tum cryptography, establishing rigorous
limits on pseudoentanglement and pseu-
dorandom density matrices with bounded
entropy.
Our work opens new avenues
for quantifying entanglement in large and
noisy quantum systems.
1
Introduction
Entanglement is a key resource in quantum infor-
mation science, and, at the same time, is of cen-
tral importance in the characterization of quan-
tum many-body systems [4, 57]. While the quan-
titative characterization of entanglement in pure
states is well-established through measures such
as the entanglement (R´enyi) entropy [108], the
extension to the case of mixed states presents
formidable challenges.
The advent of modern
noisy intermediate-scale quantum (NISQ) de-
vices [12, 85], which are inherently prone to ex-
perimental noise, makes the characterization of
mixed states particularly critical for the bench-
marking and verification of these devices.
In
particular, characterizing the entanglement prop-
erties of noisy quantum systems is essential to
gauge the performance of NISQ devices, espe-
cially since noise tends to hamper entanglement
generation. This urgent need necessitates the de-
velopment of efficient methods to quantify entan-
glement in complex noisy systems, a task that
is notoriously more difficult than its pure-state
counterpart.
One of the most common approaches for quan-
tifying mixed-state entanglement is based on the
celebrated positive partial transpose (PPT) cri-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
1
arXiv:2507.13840v2  [quant-ph]  11 Aug 2026
terion, which states that any separable state has
a partial transpose with nonnegative eigenval-
ues [56, 83]. This criterion leads to the PT neg-
ativity [84, 107] (also known as the logarithmic
negativity), a widely used and computable en-
tanglement monotone which essentially measures
the negative eigenvalues of the partial transpose.
While the PT negativity has found extensive ap-
plications in analytical studies [19, 20, 23, 37, 52,
63, 92, 114], it typically requires intricate calcu-
lations to obtain the full spectrum of the partial
transpose. Furthermore, experimentally measur-
ing the PT negativity generally necessitates full-
state tomography, thereby severely limiting its
applicability in real-world experiments.
To overcome this challenge, previous works
have focused on the simpler task of witness-
ing [40, 68, 79, 119], which aims to determine
whether a given state is entangled or not.
It
has been shown that this detection task can
be performed by considering only low-order PT
moments [40, 68, 79, 119] and other positive
maps [3, 72, 76, 112, 121], which are easier to
measure in experiments.
While such advance-
ments offer a more practical means for entangle-
ment detection, a mere binary detection provides
a very limited characterization of entanglement.
As such, they have not been adopted in the study
of entanglement in quantum many-body systems.
Ultimately, the crucial task of quantitatively and
efficiently assessing the degree of entanglement in
large, mixed systems remains a major challenge.
While direct quantification using entanglement
measures remains an unresolved problem, we
show that quantitative witnessing, i.e. a method
that provides not only detection but also quanti-
tative information about entanglement [36], can
be performed efficiently. In this work, we intro-
duce a family of quantitative entanglement wit-
nesses for mixed states called the pα-negativity.
The pα-negativity is monotonic, and the PT neg-
ativity is recovered when α = 1. While the pα-
negativity is not an entanglement monotone for
α > 1, it crucially serves as a quantitative wit-
ness for mixed-state entanglement by providing a
lower bound on the PT negativity. This property
is paramount, as it provides not just a yes/no
answer to the presence of entanglement but of-
fers valuable information about its quantitative
amount.
We further demonstrate how the ex-
ploitation of state symmetries can significantly
enhance the efficacy of these witnessing capa-
bilities, offering a substantial improvement over
previous symmetry-resolved approaches [79, 88].
Complementing the pα-negativity, we also intro-
duce the rα-negativity, a related family of wit-
nesses derived from the computable cross norm
or realignment (CCNR) criterion [24]. We show
that both families provide lower bounds for the
robustness of entanglement [109], an entangle-
ment monotone, and the Schmidt number [105],
which serves as a measure of entanglement di-
mensionality.
We focus on the case of α = 4
for both families, which we show to be efficiently
measurable on quantum computers and numer-
ically accessible via matrix product states.
In
this sense, our witnesses play a similar role to
entanglement R´enyi entropies, which have been
instrumental for studying entanglement in pure
states. Indeed, the latter are efficiently measur-
able for integer orders α ≥2 and provide lower
bounds on the von Neumann entanglement en-
tropy. Notably, both the pα-negativities and rα-
negativities collapse to the entanglement R´enyi
entropies when the state is a pure state.
We
note that the pα-negativity and rα-negativity
are examples of nonlinear entanglement wit-
nesses [48, 89, 90], i.e. nonlinear functionals of
the density matrix, in contrast to the more stan-
dard linear witnesses [9, 27, 49, 96, 104].
For
α = 4, both witnesses can be measured efficiently
without full-state tomography, as is the case for
conventional linear entanglement witnesses.
We remark that various R´enyi generalizations
of the PT negativity have been previously in-
troduced in the literature [19, 63], and are of-
ten employed in numerical studies [28, 33, 110,
110, 115, 116], when the complete PT spectrum
is not available.
However, it remained unclear
how these quantities genuinely reflect the entan-
glement properties of the system, beyond simply
serving as a “proxy” for the PT negativity, with
a lack of rigorous justification. In fact, some of
these quantities are not even well-defined in cer-
tain cases, such as for Werner states (see Ap-
pendix P). While a recent experiment [101] in-
troduced and measured a quantity that lower
bounds the PT negativity, it relies on assump-
tions of closeness to, and knowledge on entangle-
ment, of the target pure state, limiting its appli-
cability beyond classically simulable regimes.
Our work directly addresses these shortcom-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
2
ings, since our pα-negativities have a clearly de-
fined role as quantitative witnesses and are com-
pletely agnostic about the state in question. This
allows us to derive several significant results on
entanglement properties of mixed states, includ-
ing concrete applications in entanglement test-
ing, pseudoentanglement, circuit depth certifica-
tion, and entanglement phase diagram in Haar
random and stabilizer states.
Regarding entanglement testing, we introduce
an algorithm to test whether a mixed state ex-
hibits O(log n) or ω(log n) entanglement, where n
is the number of qubits. The algorithm is efficient
for weakly mixed states with 2-R´enyi entropy
S2 = O(log n).
Furthermore, we elucidate the
entanglement properties of pseudorandom den-
sity matrix (PRDM) [10], defined as an ensemble
of states that is computationally indistinguish-
able from Haar random states by any efficient
quantum algorithm. In particular, we show that
any PRDM with low entropy S2 = O(log n) must
have PT negativity E = ω(log n).
PPT 
states
a)
b)
Low 
entanglement
High 
entanglement
?
c)
Figure 1: a) Schematic representation of n-qubit state
space in terms of the PT negativity E(ρ). Darker re-
gions indicate higher values of E(ρ).
Measuring the
p4-negativity, E4(ρ), provides a lower bound on E(ρ),
thereby restricting the possible values of E(ρ) within the
state space. b) Entanglement phase diagram of Haar
random states and stabilizer states for partition sizes
nA, nB, nC. The entanglement is between subsystems
A and B, while subsystem C is traced out. There are
three different phases: positive partial transpose (PPT),
entanglement saturation (ES) and maximally entangled
(ME). (c) Illustration of entanglement testing, where
one needs to determine whether a given state has low or
high entanglement.
These findings have direct implications for
quantum
cryptography
and
pseudoentangle-
ment [59]. We demonstrate a fundamental con-
straint on pseudoentanglement, which describes
states with low entanglement g(n) that are com-
putationally indistinguishable from states with
high entanglement f(n) by any efficient quantum
algorithm [2, 10, 55]. We show that for mixed
states with low entropy S2 = O(log n), the pseu-
doentanglement gap is fundamentally limited to
f(n) = Θ(n) vs g(n) = ω(log n), mimicking the
constraints known for pure states.
This result
also establishes that the optimal pseudoentangle-
ment gap is achieved only for highly mixed states
with S2 = ω(log n), where the gap is f(n) = Θ(n)
vs g(n) = 0 [10]. This implies that entropy is
a necessary resource for securely hiding infor-
mation about entanglement from eavesdroppers.
Our work completes the understanding of the
complexity of testing and pseudoentanglement as
a function of the state’s entropy, with a complete
summary provided in Tab. 1 and Tab. 2, respec-
tively.
Further, we provide efficient algorithms to ro-
bustly certify the circuit depth of weakly mixed
states, which so far was only possible for perfectly
pure states. We also show how to efficiently test
the Schmidt rank as well as the operator Schmidt
rank.
In the context of many-body physics, under-
standing the generic entanglement properties of
quantum states is a fundamental task. Our p4-
negativity witness leads to a remarkable simplifi-
cation in characterizing the entanglement phase
diagram of Haar random states. Unlike previous
cumbersome methods that necessitated calculat-
ing all PT moments and their subsequent ana-
lytical continuation to extract the PT negativ-
ity [100], our approach only requires computing
the p4-negativity.
As a corollary, we establish
that any state 4-design, a set of quantum states
that mimics Haar random states up to fourth mo-
ments, exhibits the identical entanglement phase
diagram as Haar random states.
Surprisingly,
we also discover that stabilizer states, a classi-
cally simulable class of quantum states [1, 43–
45], share the same entanglement phase diagram
as Haar random states, despite the fact that they
do not form a 4-design. Furthermore, we investi-
gate the impact of noise on the entanglement of
pure Haar random states, showing that the p4-
negativity effectively captures their entanglement
properties even in the presence of noise.
No-
tably, our findings reveal a surprising resilience:
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
3
volume-law entanglement persists for sufficiently
large subsystems, even when subjected to expo-
nentially strong noise, highlighting the robust-
ness of entanglement in generic quantum sys-
tems.
Entropy
Copies
S2 = 0
O(poly(n)) [38]
S2 = O(log n)
O(poly(n)) [this work]
S2 = ω(log n)
2ω(log n) [10]
Table 1: Number of copies of state ρ needed to test
whether mixed state ρ has O(log n) or ω(log n) entan-
glement, as characterized by PT negativity E(ρ) and
fidelity of separability DF(ρ).
Complexity depends on
2-R´enyi entropy S2 = −ln tr(ρ2).
Entropy
f(n) vs g(n)
S2 = 0
Θ(n) vs ω(log n) [2]
S2 = O(log n)
Θ(n) vs ω(log n) [this work]
S2 = ω(log n)
Θ(n) vs 0 [10]
Table 2: Pseudoentanglement gap f(n) vs g(n) between
high-entanglement and low-entanglement state ensem-
bles, depending on 2-R´enyi entropy S2 = −ln tr(ρ2).
Entanglement is characterized by PT negativity E(ρ) and
fidelity of separability DF(ρ).
We summarize our main results in Fig. 1. The
rest of the paper is structured as follows.
In
