---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-30
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
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
Sec. 2 we provide some preliminaries. In Sec. 3
we introduce the families of quantitative entan-
glement witnesses. In Sec. 3, we show how our
families of witness quantify entanglement dimen-
sionality. In Sec. 5 we discuss the relation be-
tween the rα-negativity and the operator space
entanglement entropy.
In Sec. 6 we introduce
an algorithm for entanglement testing in mixed
states, as well as the Schmidt rank and opera-
tor Schmidt rank testing. In Sec. 7 we propose
a certification scheme for the minimal depth to
prepare a given state. In Sec. 8 we discuss the en-
tanglement properties of pseudorandom density
matrices and pseudoentanglement. In Sec. 9 we
discuss the entanglement phase diagram of Haar
random and stabilizer states. In Sec. 10 we dis-
cuss the effects of noise on the entanglement in
Haar random states. In Sec. 11 we introduce al-
gorithms to compute our witnesses using matrix
product states and matrix product operators. In
Sec. 12 we provide numerical results on our wit-
nesses in mixed many-body systems in various
mixed-state settings. Finally, in Sec. 13 we pro-
vide a discussion of our results.
A number of
technical points and proofs are reported in the
appendices.
2
Preliminaries
We consider a system of n qubits associated
with the Hilbert space Hn = Nn
j=1 Hj, where
Hj ≃C2. For a pure state of n qubits |ψ⟩, the
bipartite entanglement between complementary
subsystems A and B can be quantified by the
entanglement R´enyi entropy
Sα(|ψ⟩) =
1
1 −α ln tr(ρα
A),
(1)
where ρA = trB(|ψ⟩⟨ψ|) is the reduced density
matrix.
A pure state has zero entanglement
entropy iff it is an unentangled product state
|ψ⟩= |ψA⟩⊗|ψB⟩. Sα(|ψ⟩) has the monotonicity
property Sα(|ψ⟩) ≥Sβ(|ψ⟩) for α ≤β.
For a general mixed quantum state of n qubits
ρ, the bipartite entanglement between comple-
mentary subsystems A and B can be quantified
from the partial transpose
ρΓ = Γ(ρ) ,
(2)
where Γ denotes the partial transposition on sub-
system B. More precisely, it is a linear map that
acts as Γ(XA ⊗YB) = XA ⊗Y T
B , where the su-
perscript T denotes matrix transpose. In other
words, the matrix elements of the partial tran-
pose are given by

a, b′

 ρΓ 

a′, b

 = ⟨a, b| ρ

a′, b′
 ,
(3)
where a and b denote computational basis states
in subsystems A and B, respectively. A necessary
condition for a separable state is that their PT
is always positive-semidefinite (Peres-Horodecki
criterion) [56, 83]. That is, a state with a non-
positive PT (NPT state) is entangled. The con-
verse is not true as there exists PPT entangled
states, also known as bound entangled states.
The entanglement monotone related to the PPT
condition is the PT negativity (also known as log-
arithmic negativity), which is defined by [107]
E(ρ) = ln∥ρΓ∥1 = ln
X
i
|λi| ,
(4)
where λi are eigenvalues of ρΓ.
Note that the
trace norm of an operator X is given by ∥X∥1 =
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
4
√
X†X. Hereafter, we will drop the dependence
on ρ when the state in question is clear from the
context.
The computation of PT negativity generally
requires full diagonalization of ρΓ, which is ex-
ponentially costly. To overcome this challenge, it
is useful to analyze the more tractable (integer)
moments of the partial transpose
pα(ρ) = tr((ρΓ)α)
(5)
for integer α
=
1, 2, . . . .
Note that p2
=
tr(ρ2) is equivalent to the purity of ρ, with 2-
R´enyi entropy S2 = −ln(p2).
These PT mo-
ments can be utilized to derive necessary and
sufficient conditions of entanglement in mixed
states [40, 79, 119]. For example, the so-called
p3-PPT condition reads [40]
ρ ∈SEP =⇒p3 ≥p2
2.
(6)
Any state violating this condition is NPT and
therefore entangled. One can define a quantity
related to the p3-PPT condition [21]
˜E3(ρ) = 1
2 ln
 
p2
2
p3
!
,
(7)
such that ˜E3(ρ) > 0 implies that the state is en-
tangled. Thus, ˜E3(ρ) is an entanglement witness
for mixed states. While the p3-PPT condition is
a practical tool to detect entanglement in mixed
states, it is not known whether it is quantitatively
(e.g. in terms of inequalities) related to the PT
negativity.
An alternative approach to detect entangle-
ment in mixed states is via the CCNR crite-
rion [24]. We define the realignment matrix Rρ
as

a, a′

 Rρ

b, b′
 = ⟨a, b| ρ

a′, b′
 ,
(8)
which provides a necessary condition for separa-
bility that ∥Rρ∥1 ≤1. The CCNR negativity is
defined by [73, 117, 118]
C(ρ) = ln∥Rρ∥1 = ln
X
i
|λi|,
(9)
where λi are singular values of Rρ. Unlike the
PT negativity, C(ρ) is not a proper entanglement
measure, since it can become negative. Never-
theless, by the CCNR criterion, C(ρ) > 0 implies
that the state is entangled, and thus it serves as
an entanglement witness. We further denote the
moments of the realignment matrix as
rα(ρ) = tr((R†
ρRρ)α/2) =
X
i
|λi|α.
(10)
We will also consider two other entanglement
monotones. First, the fidelity of separability is
defined as [25, 97, 103]
DF(ρ) = min
σ∈SEP −ln F(ρ, σ)
(11)
where we have the Uhlmann fidelity F(ρ, σ) =
tr(√ρσ)2 [61].
Finally, the robustness of entanglement [109] is
given by
R(ρ) = min s s.t ρ = (1+s)ρ+
s −sρ−
s ,
ρ+
s , ρ−
s ∈SEP .
(12)
3
Quantitative
entanglement
wit-
nesses
In this section, we formally introduce the en-
tanglement witnesses based on the PT moments
and realignment moments.
We also define the
symmetry-resolved witnesses in the presence of a
global symmetry.
3.1
From the PT moments
For an n-qubit state ρ, we define our entangle-
ment witness, pα-negativity, as
Eα(ρ) =
1
2 −α ln (˜pα) + 1 −α
2 −α ln (p2)
=
1
2 −α[ln(˜pα) + (α −1)S2(ρ)] ,
(13)
where we define ˜pα(ρ) = tr((|ρΓ|)α). Note that
˜pα = pα for even integer α. Eα(ρ) is an entan-
glement witness since Eα(ρ) > 0 implies that the
state is entangled. To see this, let qi = λ2
i /p2,
which forms a probability distribution since qi >
0 and P
i qi = 1. We will consider the (classical)
α-R´enyi entropy
Hα({q}) =
1
1 −α ln
 X
i
qα
i
!
,
(14)
which is known to satisfy the monotonicity Ha ≥
Hb for a < b.
Since we can write Eα(ρ) =
1
2(Hα/2({q})−S2(ρ)), it immediately follows that
the pα-negativity also satisfies the monotonicity
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
5
Eα ≥Eβ for α < β.
Importantly, this implies
that
Eα(ρ) ≤E(ρ) ,
(15)
for α ≥1, since E(ρ) ≡E1(ρ). Thus, Eα(ρ) > 0
implies E(ρ) > 0, which in turn guarantees that
the state is entangled. From the derivation, we
can also deduce that the inequality is saturated
iff the distribution qi is flat (equivalently, when
the absolute values of the spectrum |λi| is flat).
For pure states |ψ⟩, Eα(|ψ⟩) = Sα/2(|ψ⟩) for any
α, where Sα is the α-R´enyi entanglement entropy.
As such, the pα-negativities can be viewed as a
generalization of entanglement R´enyi entropies to
mixed states, inheriting some of their nice prop-
erties.
The pα-negativity has the following proper-
ties: i) Invariant under local unitaries UA ⊗UB,
i.e.
Eα(UA ⊗UBρU†
A ⊗U†
B) = Eα(ρ), ii) Ad-
ditive, i.e.
Eα(ρ ⊗σ) = Eα(ρ) + Eα(σ).
iii)
−1
2S2(ρ) ≤Eα(ρ) ≤1
2(n ln 2 −S2(ρ)). The lower
bound follows from Eα(ρ) = 1
2(Hα/2({q})−S2(ρ))
and Hα/2({q}) ≥0, while the upper bound is
shown in Appendix C. Note that Eα is not an
entanglement monotone [108] because it can be
non-positive for entangled states.
Importantly, the pα-negativity goes beyond
simply determining the presence of entangle-
ment. Indeed, as shown in Eq. (15), Eα provides
a lower bound on the PT negativity for α ≥1,
thus classifying it as a quantitative entanglement
witness [36]. Namely, the value of Eα offers quan-
titative information regarding the amount of en-
tanglement present in the state. Therefore, Eα al-
lows one not only to detect the entanglement but
also to infer the quantitative value of the entan-
glement, which is useful to answer the question of
how useful a given state is, say, to perform cer-
tain quantum information tasks.
Furthermore,
we derive the inequality
E(ρ) ≤ln(2R(ρ) + 1)
(16)
in Appendix E. Therefore, our witnesses also pro-
vide a lower bound to the robustness of entangle-
ment.
The pα-negativity for α < 1 is not an entan-
glement witness since it is always non-negative.
Nevertheless, it remains useful to provide upper
bounds for the PT negativity (see Appendix C).
Moreover, Eα(ρ) = 0 for α < 1 implies E(ρ) = 0,
thus it provides a sufficient (but not necessary)
condition for separability.
We will be particularly interested in the p4-
negativity
E4(ρ) = 1
2 ln
 
p3
2
p4
!
= 1
2[−ln(p4)−3S2(ρ)] . (17)
For pure states, we have E4 = S2(ρA), and the in-
equality in Eq. (15) becomes S2(ρA) ≤S1/2(ρA),
which follows from the hierarchy of α-R´enyi en-
tanglement entropy.
We also note that ˜E3 =
S3(ρA) for pure states, which also provides a
lower bound to S1/2(ρA).
This lower bound is
weaker than S2(ρA), since S2(ρA) ≥S3(ρA).
However, ˜E3 cannot provide a lower bound to E
in the general case, since p3 can be zero or nega-
tive [40], in which case ˜E3 is not well-defined.
Notably, E4 can be measured efficiently with-
out reconstructing ρ. Indeed, p4 can be measured
by a quantum circuit composed of O(n) control-
SWAP gates that acts on 4 copies of ρ [22, 46].
See Appendix A for details.
Moreover, p2 =
tr
 ρ2 can be measured efficiently via SWAP test
or Bell measurements. The joint preparation of
4 copies of ρ may still be challenging in cur-
rent experiments, and an alternative measure-
ment scheme is through classical shadow [58] or
randomized measurements [39, 122]. While these
schemes generally require exponential number of
samples, they have been applied to experimen-
tally detect entanglement [17, 40, 79].
We remark that the difference between ˜E3 and
E4 is given by
E4 −˜E3 = 1
2 ln ˜r2,
(18)
where
˜r2 = p2p3
p4
,
(19)
which is studied in [21] as a tool to distinguish
entanglement phase diagram in random states.
3.2
From the realignment moments
We also define entanglement witnesses based on
the CCNR negativity C(ρ) using the realignment
matrix moments. We define the rα-negativity as
Cα(ρ) =
1
2 −α ln (rα) + 1 −α
2 −α ln (r2)
=
1
2 −α[ln(rα) + (α −1)S2(ρ)] ,
(20)
Using similar argument for the pα-negativity, by
replacing pα with rα, one can show that Cα sat-
isfies the monotonicity Cα ≥Cβ for α < β, which
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
6
implies
Cα(ρ) ≤C(ρ),
(21)
where C(ρ) ≡C1(ρ). Although C(ρ) is not an en-
tanglement monotone, it provides a lower bound
to the robustness of entanglement via
C(ρ) ≤ln(2R(ρ) + 1),
(22)
as shown in Appendix E. Therefore, Cα(ρ) for
α ≥1 also serves as a quantitative entanglement
witness, as it provides a lower bound to the ro-
bustness of entanglement.
In particular, the r4-negativity reads
C4(ρ) = 1
2 ln
 
r3
2
r4
!
= 1
2[−ln(r4)−3S2(ρ)] , (23)
where C4(ρ) > 0 implies that the state is entan-
gled. We can give bounds −1
2S2(ρ) ≤C4(ρ) ≤
min(nA, nB) ln 2 −1
2S2(ρ), where nA(B) is the
number of qubits in A(B). (see Appendix C for
the upper bound). The witness C4 can be mea-
sured by a scheme similar to that for E4 [68],
without full-state tomography.
As detailed in
Appendix B, we introduce a new measurement
scheme which employs a constant-depth circuit
of Clifford gates, offering a significant advantage
in terms of experimental feasibility. It can also
be measured via randomized measurements as
demonstrated in previous experiments [17, 88].
3.3
Symmetry-resolved
entanglement
wit-
nesses
We will now discuss how to exploit symmetry to
enhance the bounds from the witnesses. We will
first focus on the witnesses from the PT moments
before commenting on the realignment moments.
In the presence of a global symmetry, the den-
sity matrix ρ can be split into different charge sec-
tors. For concreteness, we consider a global U(1)
symmetry where the state commutes with the to-
tal number operator Q = P
i(I −Zi)/2.
Such
a state has a block-diagonal form ρ = L
q ρ(q),
where ρ(q) is a block corresponding to the charge
q.
In a bipartite system, we can write Q =
QA + QB, where QA(B) = P
i∈A(B)(I −Zi)/2.
In this case, the partial transpose commutes
with Q′ = QA −QT
B and it can be cast in the
block diagonal form [30, 79]: we denote as ρΓ
(q)
the resulting blocks, where q indicates the charge.
We denote the corresponding moments as p(q)
α ,
with
p(q)
α
= tr((ρΓ
(q))α).
(24)
We can exploit this to define p4-negativity in a
given block
E(q)
4 (ρ) = 1
2 ln
 
(p(q)
2 )3
p(q)
4
!
.
(25)
By similar arguments as the non-symmetry-
resolved case, one can show that
E(q)
4 (ρ) ≤E(q)(ρ) ,
(26)
where
E(q)(ρ) = ln∥ρΓ
(q)∥2
1 = ln
X
i
|λ(q)
i | ,
(27)
where λ(q)
i
are the eigenvalues of ρΓ
(q). It is easy
to see that E(q)(ρ) ≤E(ρ) for any given block,
and combining with Eq. (26), we obtain
E(q)
4 (ρ) ≤E(ρ) .
(28)
Thus,
E(q)
4 (ρ)
plays
a
similar
role
as
the
symmetry-resolved p3-PPT condition [79], which
is able to detect entanglement using symmetry-
resolved moments for a fixed charge.
Notably,
one can enhance the detection capability and ob-
tain a tighter lower bound for the negativity by
combining all quantum number blocks. We de-
fine the symmetry-resolved (SR) p4-negativity as
ESR
4 (ρ) = ln

X
q
v
u
u
t(p(q)
2 )3
p(q)
4

.
(29)
We have
ESR
4 (ρ) ≤E(ρ) .
(30)
Thus, ESR
4 (ρ) is also a quantitative entanglement
witness.
Note that, we can also define
˜E2(ρ) = 1
2 ln (p2) = −1
2S2(ρ) ,
(31)
which satisfies
˜E2(ρ) ≤E(ρ) .
(32)
However, this inequality is not useful for entan-
glement detection since ˜E2(ρ) ≤0 for any state
ρ. Nevertheless, the symmetry-resolved version
˜ESR
2 (ρ) = ln
 X
q
√p2
!
,
(33)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
7
is not necessarily non-positive, so that it may al-
ready provide a nontrivial witness of entangle-
ment since we have
˜ESR
2 (ρ) ≤E(ρ) .
(34)
By Jensen’s inequality, one can show the upper
bound ˜ESR
2 (ρ) ≤1
2(ln Nq−S2(ρ)), where Nq is the
number of quantum number. For the global U(1)
symmetry, this bound scales as O(ln n) since
Nq = n+1. Thus, while ˜ESR
2 (ρ) is more tractable
since it only involves the second PT moment, it
has a drawback that it can only provide a lim-
ited lower bound to the negativity. In particular,
it cannot be used to certify volume-law entan-
glement. Furthermore, ˜ESR
2 (ρ) fails to detect en-
tanglement when the states are too mixed, with
S2(ρ) ≥ln(n + 1).
Let us also mention that the SR witnesses can
be used to detect the entanglement of arbitrary
states, including those that do not have any sym-
metry [79]. Indeed, there exists a quantum chan-
nel Λ that maps a state ρ to σ = Λ(ρ) that has a
block-diagonal structure with respect to the de-
sired symmetry. This channel is a local opera-
tion, which cannot increase the PT negativity.
This implies
ESR
4 (σ) ≤E(σ) ≤E(ρ),
(35)
which shows that ESR
4 (Λ(ρ)) is also a quantitative
entanglement witness.
Further, the SR witnesses can be defined in
a similar way using the realignment matrix mo-
ments. It is known that the singular values of Rρ
can be split into charge sectors q which are eigen-
values of QA ⊗1 −1 ⊗QT
A [88]. The symmetry-
resolved moments are
r(q)
α
=
X
i
|λ(q)
i |α.
(36)
Then, we define
CSR
4 (ρ) = ln

X
q
v
u
u
t(r(q)
2 )3
r(q)
4

.
(37)
and
˜CSR
2 (ρ) = ln
 X
q
√r2
!
,
(38)
as our SR witnesses from the realignment matrix
moments. Note that the CCNR negativity is not
known to satisfy monotonicity under LOCC, and
therefore the SR witnesses are only applicable for
systems with symmetry, unlike the PT witnesses.
4
Quantifying
entanglement
dimen-
sionality
Beyond traditional entanglement measures, en-
tanglement dimensionality has been identified
as a crucial resource that quantifies the min-
imum dimension required to represent a given
state [105].
This is formally measured by the
Schmidt number, which we define as follows.
Consider the Schmidt decomposition for a pure
state |ψ⟩in the subsystem A:
|ψ⟩=
s(|ψ⟩)
X
i=1
p
λi |i⟩A |i⟩B ,
(39)
where λi are known as the Schmidt coefficients
The number of nonzero Schmidt coefficients is
called the Schmidt rank s(|ψ⟩), which is an en-
tanglement monotone for pure states [108]. For
mixed states, we can extend this concept using
a convex-roof construction to define the Schmidt
number as [94, 105]
s(ρ) =
min
ρ=P
i pi|ψi⟩⟨ψi| max
i
s(|ψi⟩),
(40)
where the minimum is taken over all possible
pure-state decompositions ρ =
P
i pi |ψi⟩⟨ψi|.
The Schmidt number is also an entanglement
monotone for general mixed states [105].
Determining the exact Schmidt number for a
given mixed state is a challenging task.
Con-
sequently, there has been significant interest in
finding efficient methods to bound this quantity
in experiments. Previous works have introduced
techniques based on fidelity witnesses [94, 105],
covariance matrices [64], and symmetric informa-
tionally complete measurement [75]. In the fol-
lowing, we demonstrate that our witnesses also
provide a lower bound to the Schmidt number.
For pure states, the Schmidt rank is equivalent
to the exponential of the entanglement R´enyi en-
tropy eS0(|ψ⟩). Therefore, it can be lower bounded
by the R´enyi entropies as ln s(|ψ⟩) ≥Sα(|ψ⟩) for
any α > 0.
Following this idea, the pα-negativity also pro-
vides a lower bound to the Schmidt number for
all mixed states. To show this, we first establish
that the Schmidt number is bounded by the PT
negativity as
E(ρ) ≤ln s(ρ).
(41)
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
8
The proof is given in Appendix 41. As a conse-
quence, the Schmidt number is also bounded by
the pα negativity due to Eq. (15). In particular,
we have
E4(ρ) ≤ln s(ρ)
(42)
and similarly
C4(ρ) ≤ln s(ρ) .
(43)
This provides an efficient lower bound to the
Schmidt number.
5
Relation to operator space entangle-
ment entropy
Next, we discuss the connection between the rα-
negativity and the operator space entanglement
entropy (OSEE) [86]. For a mixed state ρ, the
operator Schmidt decomposition with respect to
the bipartition A and B is given by [120]
ρ
q
tr(ρ2
A)
=
X
i
q
λO
i OA,i ⊗OB,i ,
(44)
where λO
i
are the operator Schmidt coefficients
and {OA,i} and {OB,i} are a set of orthonormal
operators in the subsystem A and B, respectively.
The operator Schmidt decomposition can be ob-
tained by vectorizing the (normalized) operator
|ρ⟩=
ρ
√
tr(ρ2
A) and performing the Schmidt de-
composition for pure states on |ρ⟩. The R´enyi
OSEE is given by [86]
SO
α (ρ) =
1
1 −α ln
 X
i
(λO
i )α
!
.
(45)
A state ρ has zero OSEE iff it can be written
as a product state in the form of ρ = ρA ⊗ρB.
The OSEE quantifies the representability of the
state |ρ⟩as a matrix product state, since it plays
a similar role as the entanglement R´enyi entropy
for pure states [95].
Therefore, while OSEE is
not a good measure of mixed-state entanglement
(since separable mixed states can have non-zero
OSEE), it has a direct relevance to the simula-
bility of a mixed state using the well-established
tools of matrix product states [29], originally de-
veloped for simulation of pure states.
Furthermore, the OSEE can be directly related
to the CCNR negativity [88]. Indeed, one can see
that the operator Schmidt coefficients λi are sim-
ply the (rescaled) singular values of the realign-
ment matrix Rρ. Therefore, the R´enyi OSEE are
related to the realignment moments by
SO
α (ρ) =
1
1 −α ln(r2α) +
α
1 −αS2(ρ).
(46)
6
Entanglement testing
While witnessing indicates the presence of entan-
glement, it is not a necessary criterion, as there
are entangled states that have non-positive wit-
ness. An alternative way to study entanglement
is via property testing [18, 74]: Here, one asks
whether a given state has a property, or is it far
from it? Notably, as our witnesses are quantita-
tive, they can be utilized for this task.
We now give an efficient testing algorithm to
determine whether a state ρ has high or low en-
tanglement, where we assume that ρ has low en-
tropy S2(ρ) = O(log n). This has been an open
problem, as only for for S2 = 0 efficient tests
for entanglement have been known [38], while
for S2 = ω(log n), testing entanglement has been
shown to be inherently inefficient [10]. Here, we
design an efficient algorithm to test for entangle-
ment which reliably distinguishes states depend-
ing on their entanglement:
Theorem 1 (Efficient testing of entanglement).
Let ρ be an n-qubit state with S2(ρ) = O(log n)
where for a bipartition it is promised that
either
(a) E(ρ) = O(log n) and DF(ρ) = O(log n) ,
or
(b) E(ρ) = ω(log n) and DF(ρ) = ω(log n) .
Then, there exists an efficient quantum algorithm
to distinguish case (a) and (b) using poly(n)
copies of ρ with high probability.
We provide a short sketch of the proof idea
in the following: For case (a) one has E4(ρ) =
O(log n), which follows from the bound on E
of Eq. (15).
Case (b) implies that S2(ρA) =
ω(log n), which can be shown using a bound on
the fidelity of separability
Sα(ρA(B)) ≥DF(ρ),
(47)
which is proven in Appendix D. Then, efficiency
of testing follows from the efficient algorithms to
estimate case (a) via E4(ρ) (see Appendix A or
Ref. [22, 46]) and case (b) via S2(ρA) using SWAP
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
9
tests. In particular, E4(ρ) can be measured using
SWAP tests involving 4 copies of ρ, while S2 can
be measured using 2 copies. Note that for E4(ρ)
to be efficiently estimated to additive precision,
we require the condition S2(ρ) = O(log n).
Next, we also give an efficient testing algo-
rithm for the operator Schmidt rank, defined as
the number of non-zero operator Schmidt coef-
ficients. It is also equivalent to the (exponential
of) OSEE SO
α for α = 0. As mentioned in the pre-
vious section, while the OSEE does not directly
quantify mixed-state entanglement, it determines
whether the state can be efficiently represented
as a matrix product operator.
In the case of pure states, testing whether the
Schmidt rank of a state across a given bipartition
is at most r can be done using a technique known
as weak Schur sampling [26] using O(r2) copies.
This algorithm requires entangled measurements
on many copies of the state. For easier extension
to mixed states, we first give a simplified testing
algorithm for the Schmidt rank. We define the
set of states of at most Schmidt rank r as Mr =
{|η⟩: |η⟩= Pr
i=1
√λi |ϕi⟩A ⊗|ϕi⟩B}, and the
maximum overlap of |ψ⟩with the states in Mr
as Fr(|ψ⟩) = max|η⟩∈Mr | ⟨η|ψ⟩|2. Now, we give
a testing algorithm which only utilizes two-copy
measurements:
Theorem 2 (Efficient testing of Schmidt rank).
Let |ψ⟩be an n-qubit state where it is promised
that
either
(a) Fr(|ψ⟩) ≥ϵ1 ,
or
(b) , Fr(|ψ⟩) ≤ϵ2 ,
across a given bipartition, where it is assumed
that ϵ2
1/r > ϵ2 + 2ϵ. Assuming ϵ = 1/poly(n),
there exists an efficient quantum algorithm to dis-
tinguish case (a) and (b) using O(r2) two-copy
measurements of |ψ⟩with high probability.
The proof is given in Appendix J, where the
key idea is to make use of the inequality
tr(ρ2
A) ≤Fr(|ψ⟩) ≤
q
rtr(ρ2
A).
(48)
Therefore, we can distinguish the two cases sim-
ply by measuring the purity tr(ρ2
A), which can be
done by two-copy measurements of the state.
Now,
we
consider
the
maximum
fidelity
FO
r (ρ) = max|O⟩∈MO
r | ⟨O|ρ⟩|2 [111], where
MO
r = {|O⟩:
O
q
tr(O2
A)
=
X
i
q
λO
i OA,i ⊗OB,i}
(49)
is the set of operators whose operator Schmidt
rank is at most r. By similar idea as the Schmidt
rank testing, we give a testing algorithm for the
operator Schmidt rank across a given bipartition:
Theorem
3
(Efficient
testing
of
operator
Schmidt rank). Let ρ be an n-qubit state where it
is promised that
either
(a) FO
r (ρ) ≥ϵ1 ,
or
(b) FO
r (ρ) ≤ϵ2 ,
across a given bipartition, where it is assumed
that tr(ρ2
A) = 1/poly(n) and (ϵ2
1/r−ϵ2) tr(ρ2
A)2 >
1/poly(n). Then, there exists an efficient quan-
tum algorithm to distinguish case (a) and (b) us-
ing O(r2) copies of ρ with high probability.
The proof, as given in Appendix K, is along
the same line as the Schmidt rank testing, re-
placing the purity by r4/r2
2. Note that r4 can be
efficiently measured by the algorithm detailed in
Appendix B, while r2 is simply the purity.
7
Circuit depth certification
A key task is to certify the depth of the cir-
cuit that was used to prepare a given quantum
state ρ.
For noiseless circuits, i.e.
S2(ρ) = 0,
the circuit depth can be certified efficiently using
Bell measurements [51]. We now prove that the
same task is also efficient for noisy quantum cir-
cuits, assuming the final state has low entropy,
i.e. S2(ρ) = O(log n).
We apply a noisy circuit of d layers ρ = Λd ◦
Λd−1 · · · ◦Λ1(|0⟩⟨0|), where Λi consists of noisy
two-qubit gates implemented in a fixed architec-
ture. The entanglement usually grows with each
layer, and can be used to bound the total depth.
One chooses an bipartition of equal size, where
the cut is placed such that the two-qubit gates
that act across the cut are minimal. Then, the
maximal possible entanglement is only a func-
tion of the |∂A| two-qubit gates that act across
the cut, while all other gates cannot increase en-
tanglement.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
10
We now bound the maximal entanglement gen-
erated in such circuits: We show that, the overall
entanglement after d layers is bounded as
E(ρ) ≤d|∂A| ln 2 .
(50)
The proof is given in Appendix G.
With this bound, we can efficiently certify the
minimal circuit depth d that generated a given
state ρ by measuring E4(ρ).
In particular, we
have
d ≥
1
|∂A| ln 2E4(ρ) .
(51)
where we used the inequality Eq. (15). By mea-
suring E4(ρ), one can certify d, where the esti-
mator of E4(ρ) gives a non-trivial lower bound
on d as long as S2(ρ) = O(log n).
We derive
the error bounds on the estimator for certifica-
tion in Appendix H. For example, when we have
E4 = ω(log n), our estimator correctly determines
d = ω(log n) using a polynomial number of mea-
surements.
8
Pseudorandom density matrices and
pseudoentanglement
Our quantitative witnesses have direct implica-
tions on recent developments in quantum cryp-
tography.
In particular, pseudorandom states
(PRS) have been proposed as efficiently prepara-
ble pure state ensembles that are indistinguish-
able from Haar random states by any efficient
quantum algorithm [59]. Such states have been
generalized to mixed states, known as pseudoran-
dom density matrices (PRDMs). They are effi-
ciently preparable states which are indistinguish-
able from random mixed states with entropy S2
for any efficient algorithm [10]. Their formal def-
inition is given in Appendix I.
For pure states, it has been shown that PRS
(which are equivalent to PRDMs with S2 = 0)
must have ω(log n) entanglement entropy [2, 59].
Further, it has been shown that PRDMs with
S2 = ω(log n) can possess any amount of entan-
glement.
However, the entanglement property
of PRDMs for bounded entropy S2 = O(log n)
has been unclear. We now show that for S2 =
O(log n), the entanglement of PRDMs as mea-
sured by PT negativity is bounded as follows:
Proposition 1 (Entanglement of PRDM). Any
ensemble of PRDMs with entropy S2 = O(log n)
must have PT negativity E(ρ) = ω(log n) with
high probability.
This is proven in Appendix I. The key idea is
to assume by contradiction that there exists a
PRDM with E(ρ) = O(log n).
This would im-
ply that p4 = 1/poly(n), which can be efficiently
distinguished from Haar random states via the
efficient measurement of the PT moment p4 in
Appendix A.
A related notion is pseudoentanglement [2, 10],
which are (efficiently preparable) ensemble of
states with low entanglement g(n) that are in-
distinguishable from an ensemble with high en-
tanglement f(n). The formal definition is given
in Appendix I. Our results allow to provide new
bounds on pseudoentanglement of mixed states.
A fundamental question is the difference in en-
tanglement between the two ensembles, which
is dubbed the pseudoentanglement gap. Previ-
ous works have shown that the pseudoentangle-
ment gap is bounded as f(n) = Θ(n) vs g(n) =
ω(log n) for pure states, i.e. S2(ρ) = 0 [2], while
for highly mixed states with S2(ρ) = ω(log n),
one finds the maximal possible gap of f(n) =
Θ(n) vs g(n) = 0 [10].
However, the gap for
weakly mixed states S2(ρ) = O(log n) has been
an open problem.
Here, we now compute the entanglement in
terms of PT negativity and fidelity of separa-
bility. Then, we can bound the largest possible
pseudoentanglement gap as follows:
Proposition 2 (Pseudoentanglement of mixed
states). Pseudoentangled state ensembles with
entropy S2 = O(log n) can have a pseudoentan-
glement gap of at most f(n) = Θ(n) vs g(n) =
ω(log n), where entanglement is measured by both
PT negativity E(ρ) and fidelity of separability
DF(ρ).
Proof. This follows directly from contradiction:
Assume there exists pseudoentangled state en-
sembles with low-entanglement g(n) = E(ρ) =
DF(ρ)
=
O(log n),
and
high-entanglement
f(n) = E(ρ) = DF(ρ) = Θ(log n).
Then, via
Thm. 1 and assuming S2(ρ) = O(log n), those
ensembles can be efficiently distinguished, thus
they cannot be pseudoentangled.
We note that pseudoentanglement is connected
to the existence of a fundamental primitive of
quantum cryptography [14]: EFI pairs are pairs
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
11
of mixed states that are statistically far, yet in-
distinguishable for any efficient quantum algo-
rithm. EFI pairs require pseudoentanglement to
exist [47], thus our bounds place potential restric-
tions on EFI pairs as well.
9
Entanglement phase diagram
In this section, we discuss the entanglement
phase diagram in two different sets of states:
Haar random states and stabilizer states.
9.1
Haar random states
We will consider a tripartite system in a pure
state |ψ⟩∈HA ⊗HB ⊗HC, where |ψ⟩is Haar
random. Here, the region X consists of nX qubits
with Hilbert space dimension LX = 2nX, where
X ∈{A, B, C}. We also denote nAB = nA + nB
and LAB = LALB = 2nAB. We will analyze the
Haar-random induced mixed states ρ = trC(|ψ⟩)
which are generated by tracing out subsystem C
from tripartite pure Haar random states.
For
nC = 0, such random states are Haar random
states, while for nC →∞, they asymptotically
become maximally mixed states.
Their entanglement properties have been stud-
ied in [100] using the PT negativity E(ρ) (see
also [5, 7, 8, 13, 41]).
We now denote the average over the Haar mea-
sure µn of n-qubit states as EH[.] ≡Eρ∈µn[.].
The scaling behavior of the average negativity,
EH[E(ρ)], determines an entanglement phase di-
agram for Haar random states as a function of
the partition sizes, which consists of three dif-
ferent “entanglement phases”.
This includes:
(Phase I) For nC > nAB, EH[E(ρ)] vanishes and
thus, on average, ρ is PPT. This phase is called
the PPT phase. (Phase II) For nC < nAB and
nB > n/2, EH[E(ρ)] ∼nA and thus the subsys-
tem A is maximally entangled with the subsys-
tem B, yet it is not entangled with the subsys-
tem C. In other words, the entanglement in this
phase is fully bipartite. This phase is called the
maximally entangled (ME) phase.
By symme-
try, the ME phase also appears for nA > n/2.
(Phase III) For nC < nAB and nA, nB < n/2, the
states are tripartite entangled since all three sub-
systems A, B, and C are mutually entangled, and
EH[E(ρ)] ∼(nAB −nC)/2. This phase is called
the Entanglement Saturation (ES) phase.
The
phase diagram is sketched in Fig. 1b. Here, we
show that the PT negativity in all three phases is
exactly reproduced (in the leading order) by the
p4-negativity.
The Haar average of the PT moments for inte-
ger α is given by [100]
EH[pα] ≃
1
(LALBLC)α
X
τ∈µα
Lc(τ)
C
Lc(σ+◦τ)
A
Lc(σ−◦τ)
B
,
(52)
where σ± are two special permutations defined
as σ±(k) = (k ± 1) mod n, i.e. cyclic (and anti-
cyclic) permutations. Here, for any permutation
τ ∈µα, c(τ) is the number of cycles in τ, includ-
ing the cycles of length one. By Eq. (52), one
can obtain the thermodynamic limit of EH[pα]
for various partition sizes and compute the PT
negativity by analytic continuation as
EH[E(ρ)] ≃lim
α→1/2 ln EH[p2α],
(53)
as done in Ref. [100]. We will now see how the
negativity can be simply obtained by utilizing the
p4-negativity, without requiring any knowledge
on the higher PT moments.
For the analysis, we will utilize the upper
bounds for the PT negativity:
E(ρ) ≤min{nA ln 2, nB ln 2, 1
2(nAB ln 2−S2(ρAB)}.
(54)
These bounds are shown in Appendix C through
the pα-negativity for α < 1.
In Haar ran-
dom states, EH[S2(ρAB)] ≥−ln EH[Tr
 ρ2
AB
] ≃
min(nAB ln 2, nC ln 2), where the first inequality
is because the function f(x) = −ln x is convex.
Thus, we have an upper bound for EH[E(ρ)] as
EH[E(ρ)] ≤min{nA ln 2, nB ln 2,
(55)
1
2(nAB ln 2 −min(nAB ln 2, nC ln 2))}.
(56)
Next, we compute EH[E4(ρ)], which gives a lower
bound for EH[E(ρ)].
Using Eq. (55), we can already deduce that,
for nC > nAB, EH[E(ρ)] ≲0 from the third upper
bound. This immediately implies that this phase
is a PPT phase, with EH[E(ρ)] ≃0. Although
E4 is not necessary to obtain the negativity in
this phase, we compute it here for completeness.
In this phase, EH[pα] ≃L1−α
AB in the thermody-
namic limit [100]. In particular, EH[p4] ≃L−3
AB,
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
12
and thus EH[−ln p4] ≳3nAB ln 2. We also have
−ln p2 = S2(ρAB) ≤nAB ln 2.
It follows that
EH[E4(ρ)] = EH[−1
2 ln p4 + 3
2 ln p2] ≳0. Combin-
ing EH[E4(ρ)] ≤EH[E(ρ)] and the upper bound
obtained above, we obtain EH[E4] ≃0.
Thus,
EH[E4] has the same leading order as EH[E].
Next, for nC < nAB and both nA < n/2 and
nB < n/2, one gets in the thermodynamic limit
EH[pα] ≃









CkLAB
(LABLC)k ,
α = 2k
(2k + 1)Ck
(LABLC)k ,
α = 2k + 1,
where Ck =
 2k
k
/(k + 1) is the kth Catalan num-
ber. In particular, EH[p4] ≃L−1
ABL−2
C , and thus
EH[−ln p4] ≳nAB ln 2+2nC ln 2. Since −ln p2 ≤
nC ln 2, we have EH[E(ρ)] ≥EH[E4(ρ)] ≳1
2(nAB−
nC) ln 2. Combining with the third upper bound
in Eq. (55), we obtain
EH[E] ≃EH[E4] ≃1
2(nAB −nC) ln 2.
(57)
Finally, when nAB > nC and nA > n/2, we
obtain in the thermodynamic limit
EH[pα] ≃





L1−α
C
L2−α
B
,
α = 2k
(LCLB)1−α
α = 2k + 1.
In particular,
EH[p4]
≃
L−2
B L−3
C ,
and thus
EH[−ln p4] ≳2nB ln 2 + 3nC ln 2. We again ob-
tain EH[E(ρ)] ≥EH[E4(ρ)] ≳nB ln 2. The case in
which nAB > nC and nB > N/2 is obtained by
replacing LB with LA in the latter formula. Com-
bining with the first and second upper bound in
Eq. (55), we obtain
EH[E] ≃EH[E4] ≃min(nA, nB) ln 2.
(58)
To sum up, we find that the leading order of
EH[E4] in the thermodynamic limit is identical
to EH[E] in all the three entanglement phases
of Haar random states.
Specifically, this is es-
tablished by showing that EH[E] is lower and
upper bounded by the same leading-order scal-
ing, thus fixing the scaling of EH[E] even without
considering higher-order moments. In contrast,
EH[E] was previously obtained by computing all
the PT moments, followed by analytic continu-
ation [100]. This has a remarkable implication:
the PT negativity in Haar-random states can be
obtained in the leading order by utilizing low-
order PT moments, which can be estimated ex-
perimentally and computed numerically, thereby
obviating the need for the generally more intri-
cate task of computing all PT moments. Addi-
tionally, we stress that our analysis above does
not make any assumption of self-averaging, i.e.
E[ln X] ≃ln E[X].
This ensures the generality
of the argument, which implies that these results
hold for any state design which is at least a 4-
design, where the resulting entanglement phase
diagram reproduces that of the Haar random in-
duced mixed states.
In addition, we note that the results above sim-
ilarly hold for the pα-negativity for α ≥0, as
detailed in Appendix L. This behavior resembles
the scaling of entanglement R´enyi entropies in
Haar random states, which saturate their maxi-
mal values (in the leading order) for any R´enyi
index α [77, 82].
9.2
Stabilizer states
Pure stabilizer states |ψS⟩are states generated
by applying Clifford unitaries UC onto the |0⟩
state. Here, Clifford unitaries UC are unitaries
generated from Hadamard, S-gate and CNOT
gates [44].
Clifford unitaries map (under con-
jugation) any n-qubit Pauli operator P to some
n-qubit Pauli operator, P ′, i.e. P ′ = UCPU†
C. It
is known by the Gottesman-Knill theorem that
stabilizer states can be simulated efficiently on
classical computers [1, 43–45].
As shown in Ref. [16], any three-partite sta-
bilizer state |ψS⟩can be decomposed into GHZ
states, Bell states, and product states, dis-
tributed among the three parties, A, B, and C.
That is, |ψ⟩can be written as
|ψS⟩
=
UAUBUC |0⟩⊗sA
A
|0⟩⊗sB
B
|0⟩⊗sC
C
|GHZ⟩⊗gABC
ABC
|EPR⟩⊗eAB
AB
|EPR⟩⊗eAC
AC
|EPR⟩⊗eBC
BC
,
(59)
with UA, UB, UC unitary Clifford operators on
A, B, C, respectively, |EPR⟩AB denotes a two-
qubit EPR pair with one qubit in A and the other
in B (similarly for |EPR⟩AC and |EPR⟩BC), and
|GHZ⟩ABC is a three-qubit GHZ state with one
qubit in each of A, B, and C. Given the decompo-
sition above, one can directly see that the entan-
glement negativity is given by E(ρ) = eAB [93].
It can also be seen that the negativity spectrum
of stabilizer states is constrained to two values
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
13
λi = ±√p3, i.e all eigenvalues λi of ρΓ are ei-
ther √p3 or −√p3. One can then obtain the PT
moments of stabilizer states as [21]
p2
=
1
2
gABC+eAC+eBC
p3
=
1
4
eAB 1
4
gABC+eAC+eBC
p4
=
1
4
eAB 1
8
gABC+eAC+eBC
.
(60)
The PT negativity for stabilizer states is then
given by a simple function of the PT moments
as [21]
E(ρ) = ˜E3(ρ)
for all stabilizer states.
(61)
This shows that stabilizer states are PPT iff they
satisfy the p3-PPT condition [40]. Analogously,
we find that
E(ρ) = E4(ρ)
for all stabilizer states.
(62)
Namely, stabilizer states saturate the bound in
Eq. (15). This also follows from the flatness of
the PT spectrum discussed above.
We now consider a tripartite system in a pure
state |ψ⟩∈HA ⊗HB ⊗HC, where |ψ⟩is a ran-
dom stabilizer state.
The entanglement phase
diagram as a function of the partition size can
be obtained using E(ρ) = ˜E3(ρ).
Since stabi-
lizer states form a 3-design [62, 123], we have
ES[p2,3] = EH[p2,3], where ES[.] denotes the av-
erage over stabilizer states.
Therefore, we can
again compute ES[E] by using the upper bounds
in Eq. (55) and obtaining a lower bound to ES[ ˜E3]
using a similar approach as in the Haar random
case.
Note that the upper bounds in Eq. (55)
are obtained from the second moments, and thus
they also apply to stabilizer states. One can then
verify that
ES[E] = ES[ ˜E3] ≃0,
(63)
for nC > nAB,
ES[E] = ES[ ˜E3] ≃1
2(nAB −nC) ln 2,
(64)
for nC < nAB and both nA < n/2 and nB < n/2,
and
ES[E] = ES[ ˜E3] ≃min(nA, nB) ln 2,
(65)
for nC < nAB and either nA > n/2 or nB > n/2.
In particular, the entanglement phase diagram
reproduces that of Haar random states, despite
the fact that stabilizer states do not form a 4-
design [124].
It was shown, for example, that
the quantity ˜r2, which is a function of the PT
moments up to the fourth order (see Eq. (19)),
takes different values across the phase diagram
for Haar random and stabilizer states [21], thus
also highlighting the limitation of ˜r2 in distin-
guishing entanglement phases. We further note
that, since the relation E(ρ) = ˜E3(ρ) is specific to
stabilizer states, the results presented above do
not necessarily extend to other state 3-designs.
Further, the realignment moments of stabilizer
states are given by [117]
rα
=
1
2
SAB+( α
2 −1)(SA+SB)
,
(66)
where SA denotes the entanglement of the sub-
system A. The CCNR negativity for stabilizer
states is then given by
C(ρ) = SA + SB
2
−SAB,
(67)
which also yields
C(ρ) = C4(ρ)
for all stabilizer states,
(68)
thus saturating the bound in Eq. (21). This im-
plies that the singular values of the realignment
matrix are flat.
10
Entanglement and noise
In this section, we analyze the average bipartite
entanglement of Haar-random pure states sub-
jected to global depolarizing noise.
These sys-
tems approximate deep random quantum circuits
with local noise [31]. We are interested in deter-
mining under which condition entanglement sur-
vives in the presence of noise. We consider Haar
states subject to global depolarizing noise
ρ′ = (1 −p) |ψ⟩⟨ψ| + pI/2n,
(69)
with noise probability p and |ψ⟩being drawn
from the Haar measure. One can show that the
R´enyi-2 entropy of the depolarized state is given
by EH[S2[ρ′]]
=
−ln
(1 −p)2 + p(2 −p)/2n.
Now, let p′
α be the PT moment of the depolar-
ized Haar-random states and pα those of a Haar-
random state. Then, the mean values EH[p′
α] can
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
14
be expressed in terms of the mean values EH[pα]
as
EH[p′
α] =
α
X
k=0
 
α
k
!
(1−ϵ)kEH[pk](ϵ/2n)α−k , (70)
with E[p0] = p0 = 2n.
For any fixed p < 1 and n →∞, we find that
the leading term EH[E4] ≃min(nA, nB) ln 2 for
extensive subsystems nA and nB. Therefore, the
averaged bipartite entanglement entropy of the
depolarized state, quantified by the PT negativ-
ity, is unchanged from that of the pure state,
which follows the Page curve [82]. As a conse-
quence, E4 is remarkably effective in detecting
mixed-state entanglement in Haar states even in
the presence of strong noise.
We further consider exponential noise p =
1 −2−βn with fixed β, and determine for which
β the witness E4 can successfully detect entan-
glement.
For β ≤1/2, we have EH[S2(ρ′)] ≃
2βn ln 2.
Moreover, using Eq. (70), we obtain
EH[p4] ≃2−4βn−2nB, yielding
EH[E4] ≳min(nA, nB) ln 2 −βn ln 2.
(71)
Thus,
we
detect
entanglement
via
E4
>
0
for
extensive
subsystems
whenever
β
<
min(nA, nB)/n. Beyond detection, the value of
E4 in Eq. (71) shows rigorously that the nega-
tivity obeys a volume law in the entangled re-
gions. Notably, the p3-PPT condition is unable
to show the volume law. In fact, the PT neg-
ativity can also be obtained by considering the
distribution of the Schmidt coefficients of a Haar
random state, yielding [101]
EH[E] ≃min(nA, nB) ln 2 −βn ln 2.
(72)
Thus, E4 matches E in depolarized Haar random
states, i.e. EH[E4] ≃EH[E]. This highlights the
effectiveness of E4 to quantitatively detect entan-
glement, even under exponentially strong noise.
We provide further discussion on the effects of
global depolarizing noise on entanglement in Ap-
pendix O.
11
Matrix product states and matrix
product operators algorithms
Here, we introduce algorithms to compute par-
tial transpose and realignment moments for ma-
trix product states (MPS) and matrix product
operators (MPO).
Let us consider a system of n qubits in a pure
state |ψ⟩given by an MPS of bond dimension χ:
|ψ⟩=
X
s1,s2,··· ,sn
As1
1 As2
2 · · · Asn
n |s1, s2, · · · sn⟩
(73)
with Asi
i being χ × χ matrices, except at the left
(right) boundary where As1
1 (Asn
n ) is a 1×χ (χ×
1) row (column) vector.
Here si ∈{0, 1} is a
local computational basis.
We then study the
entanglement within ρ = trC(|ψ⟩⟨ψ|), where C
is a subsystem of |ψ⟩. The case of translation-
invariant MPS is discussed in Appendix M.
We also consider a density matrix ρ of n qubits
represented in the following MPO form
ρ =
X
s,s′
W
s1,s′
1
1
W
s2,s′
2
2
· · · W sn,s′
n
n
|s1, · · · , sn⟩⟨s′
1, · · · , s′
n|
(74)
with W
si,s′
i
i
being χ × χ matrices, except at the
left (right) boundary where W s1,s′
1 (or W sn,s′
n) is
a 1 × χ (χ × 1) row (column) vector.
11.1
Partial transpose moments
The PT moments pα can be computed efficiently
for integer α ≥1 for MPS. To do so, we write pα
as
pα =
X
a(γ),a′
(γ),b(γ),b′
(γ)
α
Y
γ=1
h
δa′
(γ),a(σ+(γ))δb′
(γ),b(σ−(γ))
⟨a(γ), b(γ)|ρ|a′
(γ), b′
(γ)⟩
i
.
(75)
Using this identity, we can compute pα for MPS
by forming a transfer matrix at each site, defined
as
Li =
X
{s(γ),s′
(γ)}
α
Y
γ=1
δs′
(γ),s(π(γ))
α
O
γ=1
A
s(γ)
i
⊗A
s′
(γ)
i
,
(76)
where A indicates the complex conjugate of A,
π() is a permutation of indices, with π = σ+ if
i ∈A, π = σ−if i ∈B, and π = e if i ∈C. The
terms δs′
(γ),s(π(γ)) imply contractions of physical
indices s′
(γ) and s(π(γ)). We now define a tensor
L initialized to L = L1 and iteratively compute
L →LLi, for i = 2, · · · , n. At each step (before
the final site), L is a tensor with 2α indices, each
of size χ. To minimize the contraction cost, each
of the tensors Ai is contracted to L one by one,
yielding the overall cost of O
 nαχ2α+1.
The
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
15
p4 =
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
a
r4 =
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
W1
W2
W3
W4
W5
W6
b
Figure 2: MPO contractions to compute (a) p4 and (b) r4. The system size is n = 6 and we take A = {1, 2, 3} and
B = {4, 5, 6}.
tensor L after the final iteration is a scalar, which
is equivalent to pα.
The
algorithm
can
be
straightforwardly
adapted to MPO, and the MPO contraction is
sketched in Fig. 2(a). We define the transfer ma-
trix
Li =
X
{s(γ),s′
(γ)}
α
Y
γ=1
δs′
(γ),s(π(γ))
α
O
γ=1
W
s(γ),s′
(γ)
i
, (77)
and the algorithm proceeds as above: We define
L = L1 and iteratively compute L →LLi, for
i = 2, · · · , n, as illustrated in Fig. 3. The final
contracted tensor is equivalent to pα. We note
that cost to contract L for MPOs is given by
O
 nαχα+1.
Wi
Wi
Wi
Wi
L
L
a
Wi
Wi
Wi
Wi
L
L
b
Figure 3: Update of the tensor L →LLi in the calcula-
tion of p4 if (a) i ∈A or (b) i ∈B.
11.2
Realignment moments
For the realignment moment, we first consider an
MPO with the subsystem A = {1, 2, · · · , nA} and
B = Ac. The MPO contraction for computing r4
is sketched in Fig. 2(b). Viewing the MPO as an
MPS with two physical indices, one can see that
the contraction is equivalent to the purity of the
MPS. Similarly, higher order rα is equivalent to
the higher order α−R´enyi entanglement entropy
of the corresponding MPS. The latter can be ob-
tained from the Schmidt coefficients of the MPS,
which can be calculated using standard MPS rou-
tines with cost O(nχ3) for any α. Indeed, as has
been discussed in Sec. 5, the Schmidt coefficients
of the (normalized) MPO correspond to the sin-
gular values of the realignment matrix Rρ.
In
this way, the CCNR negativity C can be exactly
computed efficiently.
Given MPS |ψ⟩, we are interested in comput-
ing entanglement of the mixed state ρ = trC(|ψ⟩),
with subsystem C connected to the right bound-
ary of MPS. Since the density matrix ρ can be
represented by an MPO with bond dimension χ2,
where the local tensors are U
si,s′
i
i
= Asi
i ⊗A
s′
i
i , the
CCNR negativity can be naively obtained with
cost O(nχ6). We now propose an algorithm with
a reduced cost.
Let us compute entanglement for ρ with bi-
partition A = {1, 2, · · · , nA}, B = {nA + 1, nA +
2, · · · , nA +nB}. We note that the algorithm can
be adapted for the case where A and B are con-
tiguous segments in the left and right parts of
the MPS, respectively (see Appendix N). First,
we place the orthogonality center of the MPS on
the site nA. Next, we define the transfer matrix
Ri =
X
{s,s′}
As
i ⊗As′
i ⊗As′
i ⊗As
i,
(78)
for i ∈B.
We also define R = 1χ ⊗1χ and
compute R →RiR iteratively for i = nA +
nB, · · · , nA +1, with cost O(nχ5). The final ten-
sor R is a tensor with four indices Rα,α′,β,β′. The
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
16
tensor L can be defined in a similar way from
the left part of the MPS. Because the orthog-
onality center is placed at nA, L is simplified to
Lα,α′,β,β′ = Λα,β′Λβ,α′, where Λ = P
s As
nA⊗As
nA.
Next, we compute
Γα,α′,γ,γ′ =
X
β,β′
Rα,α′,β,β′Λβ,γ′Λγ,β′.
(79)
Writing Γ as a χ2 × χ2 matrix by combining in-
dices Γ(α,α′),(γ,γ′), one can see that
rα = tr(Γα/2),
(80)
for even integer α. Thus, the eigenvalues of Γ are
the squared singular values of Rρ, and the CCNR
negativity can again be exactly computed. The
diagonalization of Γ can be done with cost O(χ6),
which results in the overall cost of O(χ6 + nχ5).
Note that, for α = 4, r4 = tr(Γ2) can be com-
puted more efficiently by matrix multiplication,
and thus the cost for computing r4 is O(nχ5).
12
Mixed-state
entanglement
in
many-body systems
While entanglement of pure many-body systems
has been routinely studied [4], characterizing it
in mixed states has remained a significant chal-
lenge due to the inherent difficulty in comput-
ing mixed-state entanglement measures in many-
body systems. Mixed states are ubiquitous, aris-
ing naturally from finite temperature, noise, or
partial tracing.
With our witnesses, we now
study the entanglement in mixed many-body sys-
tems, demonstrating their potential for charac-
terizing entanglement in various physical phe-
nomena. In the following, we focus on the wit-
nesses from the PT moments.
First, we consider the transverse-field Ising
model
HTFIM = −
n−1
X
k=1
σx
kσx
k+1 −h
n
X
k=1
σz
k
(81)
where h is the transverse field and we impose
open boundary condition. In this model, there is
a transition from the ferromagnetic phase to the
paramagnetic phase at hc = 1. The critical point
is governed by the Ising CFT with central charge
c = 1/2 [32]. The TFIM possesses Z2 symmetry,
generated by Q
i σz
i .
As initial warm-up to understand our wit-
nesses, we begin with the pure ground state
of n = 12 sites, and we set nA = nB = 5
sites in the middle as the subsystem, where
A and B are adjacent, contiguous subsystems.
We show E, ˜E3, E4 in Fig. 4(a), where the in-
equalities E4, ESR
4 , ˜ESR
2
≤E are confirmed. The
entanglement is detected by all the witnesses
˜E3, E4, ESR
4 , ˜ESR
2
in the interval h ∈[0, 2], where
the state is indeed entangled, as confirmed by
positive E. Next, we consider disconnected inter-
vals A and B consisting of nA = nB = 5 sites on
the left and right end of the chain, respectively.
As shown in Fig. 4(b), the non-SR witnesses
˜E3, E4 fail to detect entanglement in a large inter-
val, as it becomes negative for h ≳0.9. The SR
witnesses ESR
4 , ˜ESR
2 , defined with respect to the Z2
symmetry, display significant improvement over
the non-SR ones, only becoming slightly negative
at h ≳1.5, where the PT negativity is indeed
close to zero.
Now, we subject the ground state of the TFIM
to noise, turning it into a mixed state, where
each qubit is affected by single-qubit depolari-
sation noise Γ(ρ) = (1 −p)ρ + ptr1(ρ)I1/2 with
probability p. This channel preserves the Z2 sym-
metry of the systems, so that the SR witnesses
can still be utilized. Fig. 5(a) shows E4 for n = 6
and nA = nB = 3. We see that, for small enough
p, E4 is effective in detecting the entanglement.
Further, we compare various entanglement wit-
nesses with n = 6, nA = 3, and p = 0.05 in
Fig. 5(b). We again find that the SR witnesses
are more reliable in detecting entanglement. Fur-
ther, we show the witnesses as a function of p in
Fig. 6(a). We find that the PT negativity van-
ishes above a value pc, a phenomena reminiscent
of sudden death that is known to occur at finite-
temperature systems [102]. Indeed, we confirm
that, at finite temperature, the PT negativity
vanishes for T ≳1.5 at h = 1.5, as shown in
Fig. 6(b). Here, n = 10 and nA = nB = 5. Once
again, we see the advantage of SR witnesses in
witnessing entanglement in this case, becoming
negative at higher temperature than the non-SR
counterpart. At finite temperature, the PT nega-
tivity has been shown to follow an area law scal-
ing [102]. Using the bounds shown in Sec. 3.1
and 3.3, it immediately follows that our quan-
titative witnesses are bounded by the area law
scaling.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
17
0.5
1.0
1.5
2.0
h
0.0
0.2
0.4
Witness
E
˜E3
E4
ESR
4
˜ESR
2
a
0.5
1.0
1.5
2.0
h
−0.1
0.0
0.1
0.2
b
Figure 4: Entanglement witnesses for the groundstate
of the TFIM (81) of n = 12 sites and subsystem size
nA = nB = 5 for (a) connected and (b) disconnected
partitions as a function of the transverse field h.
0.0
0.5
1.0
1.5
2.0
h
0.0
0.2
0.4
0.6
E4
p = 0.005
p = 0.01
p = 0.02
p = 0.05
a
0.0
0.5
1.0
1.5
2.0
h
0.0
0.2
0.4
Witness
E
˜E3
E4
ESR
4
˜ESR
2
b
Figure 5: Entanglement witnesses for the groundstate
of the TFIM (81) of n = 6 sites under depolarization
noise. The partition size is nA = 3. In (a), we show
E4 for different depolarisation probability p.
For p ∈
{0.005, 0.01}, E4 detects the entanglement at all interval
of h considered. In (b), we show different entanglement
witnesses for p = 0.05.
0.00
0.25
0.50
0.75
1.00
p
−1.5
−1.0
−0.5
0.0
0.5
Witness
E
˜E3
E4
ESR
4
˜ESR
2
a
0
1
2
T
−1.5
−1.0
−0.5
0.0
b
Figure 6: Entanglement witnesses for the TFIM (81)
(a) under depolarization noise with n = 6 and h = 1,
and (b) at finite temperature T with n = 10 sites and
h = 1.5. The partition size is nA = n/2.
We further illustrate the entanglement wit-
nesses for the ground-state of the XXZ model,
which Hamiltonian reads
HXXZ = −
n−1
X
k=1
(σx
kσx
k+1 + σy
kσy
k+1 + ∆σz
kσz
k+1)
(82)
with the anisotropy ∆. The model has a U(1)
symmetry related to magnetization conserva-
tion.
We compute the ground state within
the half-filling excitation symmetry sector Np =
Pn
k=1 σz
k = 0.
The system hosts an antiferro-
magnetic phase when ∆< −1, a critical phase
for ∆∈[−1, 1], and a ferromagnetic phase for
∆> 1. We will analyze the entanglement in the
range ∆∈[−4, 1].
The results for the tripartite case are shown in
Fig. 7, with the same partitions as in the TFIM.
In this case, all the witnesses considered can de-
tect the entanglement of the ground states for
all ∆, both for connected and disconnected par-
titions.
−4
−2
0
∆
0.0
0.2
0.4
0.6
0.8
Witness
E
˜E3
E4
ESR
4
˜ESR
2
a
−4
−2
0
∆
0.0
0.2
0.4
b
Figure 7: Entanglement witnesses for the groundstate of
the XXZ model (82) of n = 12 sites and subsystem size
nA = nB = 5 for (a) connected and (b) disconnected
partitions as a function of the anisotropy ∆.
13
Discussion
In this work, we introduced a generalization of
entanglement Renyi entropies to mixed states,
which we call the pα-negativity.
For α = 1,
it equals the PT negativity, while for α > 1 it
serves as a quantitative witness for mixed state
entanglement. In other words, they offer useful
quantitative information about the degree of en-
tanglement by rigorously bounding entanglement
monotones [36]. Further, we showed that sym-
metries can be exploited to enhance the entan-
glement witnessing capabilities, improving over
previous symmetry-resolved approaches. We also
introduced similar witnesses based on the CCNR
criterion [24], dubbed the rα-negativity.
The
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
18
CCNR negativity bounds the robustness of en-
tanglement, thus making the witnesses quantita-
tive. Notably, both C4 and E4 can be efficiently
measured on quantum computers. In particular,
C4 can be measured in experiment via SWAP
tests, using only a single layer of CNOT and
Hadamard gates acting on 4 copies of ρ, while
E4 requires a linear number of Toffoli gates. C4
requires only Clifford gates and constant-depth
circuit to be measured via Bell measurements,
which is an essential advantage for benchmarking
early fault-tolerant quantum computers.
This
protocol can also be applied to efficiently mea-
sure the operator space entanglement entropy.
By leveraging our witnesses, we obtain several
powerful results regarding entanglement proper-
ties across diverse scenarios. We provide an al-
gorithm to test whether a state has O(log n) or
ω(log n) entanglement, which is efficient as long
as the state is weakly mixed, i.e.
the 2-R´enyi
entropy scales at most as S2 = O(log n). This
bound is tight, as testing is inherently inefficient
for S2 = ω(log n) [10]. This test generalizes the
efficient testing algorithm that was previously
only known for pure states [2], to the mixed states
setting. Similarly, we show that any pseudoran-
dom density matrices with S2 = O(log n) must
have PT negativity E = ω(log n).
Our results
also have direct implications on quantum cryp-
tography: We show that the pseudoentanglement
gap, i.e. the capability of low-entangled states
to mimic high-entangled states, is fundamentally
constrained for mixed states with bounded en-
tropy S2 = O(log n), with the gap of f(n) = Θ(n)
vs g(n) = ω(log n), generalizing the previously
known constraint for pure states. The optimal
gap is only achieved for highly mixed states with
S2 = ω(log n), where one finds f(n) = Θ(n)
vs g(n) = 0 [10].
Thus, we resolve the ques-
tion of the pseudoentanglement gap as a function
of entropy, with the complete summary given in
Tab. 2. While usually entropy in quantum states
is associated negatively with noise and destroy-
ing quantumness, we find the opposite is true
in quantum cryptography: Here, entropy is an
important resource needed to hide information
about quantum resources such as entanglement
from eavesdroppers [54]. To completely hide en-
tanglement, one requires S2 = ω(log n), which we
find is tight. These findings complement our re-
cent work [53], where we found analogous results
for the mixed-state nonstabilizerness.
We can also robustly certify the circuit depth
needed to prepare a given quantum state. In par-
ticular, we can efficiently determine the minimum
depth of the circuit even when the state is sub-
jected to noise, assuming the final state is weakly
mixed.
Previously, such certification was only
possible for pure states, i.e. in noiseless quantum
circuits [51]. In addition, we provide an efficient
algorithm to test the Schmidt rank for pure states
and the operator Schmidt rank for mixed states.
Our witness provides a significant simplifica-
tion in determining the entanglement phase di-
agram of Haar random states:
it can be en-
tirely characterized by computing only the p4-
negativity.
This is done by exploiting the fact
that the p4-negativity provides a lower bound for
the PT negativity. By explicitly computing the
Haar average of the p4-negativity, we find that
it saturates the upper bound of the PT negativ-
ity, which implies that the latter must also sat-
urate the maximal value. Remarkably, this ap-
proach stands in contrast to the previous more
intricate methods, which required calculating all
PT moments and then analytically continuing to
the PT negativity [100]. As a direct consequence,
we demonstrate that any 4-design exhibits the
same entanglement phase diagram as Haar ran-
dom states. We note that entanglement transi-
tions in Haar random states have been observed
in experiment by full-state tomography [67], and
our results provide a scalable route to observe the
transitions in larger devices.
We further show that the Haar average of the
pα-negativity is also close to its maximal value for
any α ≥0. This parallels the behavior of entan-
glement R´enyi entropies in Haar random states,
which are similarly close to their maximal val-
ues for any R´enyi index α. This further demon-
strates the similarity between the pα-negativities
and the entanglement R´enyi entropies, highlight-
ing the significant potential of the former to char-
acterize mixed-state entanglement in many-body
systems.
Surprisingly, we find that stabilizer states also
share the same phase diagram, despite not form-
ing exact 4-designs [124]. We also investigate the
impact of noise on the entanglement of pure Haar
random states. Our findings show that the p4-
negativity remains effective in capturing entan-
glement properties in this case. Notably, we ob-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
19
serve that the volume-law entanglement survives
for sufficiently large subsystems, even when sub-
jected to exponentially strong noise.
Our work also makes progress on the compu-
tation of entanglement in extensive mixed many-
body systems, which has been a challenge. Mixed
states can be represented as MPOs or as purifi-
cations in form of MPS, both of bond dimension
χ.
For MPS of bond dimension χ, we provide
an efficient algorithm to compute PT moment
pα for integer α > 1 in O(nαχ2α+1), while for
mixed states written as MPO it can be computed
in O(nαχα+1).
Similarly, C can be computed
in O(nχ3) for MPO, while for MPS the cost is
O(nχ5) for computing the realignment moment
r4.
We show that our entanglement witnesses
can be used to characterize the entanglement
of ground states for the TFIM and XXZ model
when subject to noise or when subsystems have
been traced out. Notably, we find that E4, which
is efficient for MPS, characterizes entanglement
nearly as well as the PT negativity E, which is
difficult to compute. Further, we find that our
symmetry-resolved witnesses can detect entan-
glement significantly better than standard wit-
nesses, both for discrete and continuous symme-
tries, promising to be useful in symmetric many-
body systems.
Taken together, these results
demonstrate the potential of pα-negativity and
its symmetry resolution to characterize mixed-
state entanglement in large many-body systems,
where the PT negativity is no longer tractable.
In summary, our work presents several sig-
nificant results concerning mixed-state entangle-
ment that were previously understood only in
the context of pure states. In pure states, these
insights often relied on entanglement R´enyi en-
tropies. We have been able to extend these find-
ings to mixed states through the introduction of
the pα-negativity, showcasing its role as a pow-
erful generalization of entanglement R´enyi en-
tropies for mixed systems. While pα-negativity
is not an entanglement monotone, its function
as a quantitative entanglement witness enables
it to effectively characterize mixed-state entan-
glement properties, as evidenced by our findings.
Given the widespread utility of entanglement
R´enyi entropies in understanding pure-state en-
tanglement, we anticipate that our witnesses will
find further applications in deepening our under-
standing of mixed-state entanglement.
Our work opens several interesting avenues for
future research. A key direction involves explor-
ing the applications of these quantitative entan-
glement witnesses in the characterization of en-
tanglement in many-body quantum systems. We
posit that the p4-negativity can serve as a cru-
cial tool in the study of entanglement phases and
properties in general mixed states.
In particu-
lar, it would be interesting to extend the mini-
mal membrane picture of entanglement spread-
ing [78] to non-complementary subsystems. Fur-
ther, investigations into tripartite entanglement
at measurement-induced criticality [93], and in
noisy monitored circuits [65, 66, 87, 113] are also
warranted. It would also be interesting to study
whether pα-negativity can characterize finite-
temperature phase transitions [70] and detect
topological order at finite temperature [52, 71].
Future research could also explore the construc-
tion of entanglement witnesses for fermionic sys-
tem, where the PT negativity is defined based
on a different notion of partial transpose [98, 99].
Another interesting direction is to extend our
ideas for the quantitative detection of multipar-
tite entanglement [68]. Finally, we posit the ques-
tion whether it is possible to construct proper
mixed-state entanglement monotones that are
also efficiently measurable.
Acknowledgments
P.S.T. acknowledges funding by the Deutsche
Forschungsgemeinschaft
(DFG,
German
Re-
search Foundation) under Germany’s Excellence
Strategy – EXC-2111 – 390814868.
Author contributions
P.S.T. conceived the initial idea and carried out
most of the analytical and numerical calculations,
with the guidance of T.H. T.H. developed the
analysis of pseudorandom density matrices and
pseudoentanglement, and the measurements of
the witnesses. Both authors discussed the results
and contributed to the writing of the manuscript.
References
[1] Scott Aaronson and Daniel Gottesman.
Improved simulation of stabilizer circuits.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
20
Phys.
Rev.
A,
70:052328,
Nov
2004.
DOI: 10.1103/PhysRevA.70.052328. URL
https://link.aps.org/doi/10.1103/
PhysRevA.70.052328.
[2] Scott Aaronson, Adam Bouland, Bill Fef-
ferman, Soumik Ghosh, Umesh Vazirani,
Chenyi Zhang, and Zixin Zhou.
Quan-
tum pseudoentanglement.
arXiv preprint
arXiv:2211.00747, 2022.
URL https://
doi.org/10.48550/arXiv.2211.00747.
[3] Shruti Aggarwal, Satyabrata Adhikari, and
A. S. Majumdar. Entanglement detection
in arbitrary-dimensional bipartite quan-
tum systems through partial realigned mo-
ments. Phys. Rev. A, 109:012404, Jan 2024.
DOI: 10.1103/PhysRevA.109.012404. URL
https://link.aps.org/doi/10.1103/
PhysRevA.109.012404.
[4] Luigi
Amico,
Rosario
Fazio,
Andreas
Osterloh,
and Vlatko Vedral.
Entan-
glement in many-body systems.
Rev.
Mod.
Phys.,
80:517–576,
May
2008.
DOI: 10.1103/RevModPhys.80.517.
URL
https://link.aps.org/doi/10.1103/
RevModPhys.80.517.
[5] GUILLAUME AUBRUN. Partial transpo-
sition of random states and non-centered
semicircular
distributions.
Random
Matrices:
Theory and Applications, 01
(02):1250001, April 2012.
ISSN 2010-
3271.
DOI: 10.1142/s2010326312500013.
URL
http://dx.doi.org/10.1142/
S2010326312500013.
[6] Guillaume Aubrun and Ion Nechita. Re-
aligning random states. Journal of Math-
ematical Physics, 53(10):4759115, Octo-
ber
2012.
ISSN
1089-7658.
DOI:
10.1063/1.4759115. URL http://dx.doi.
org/10.1063/1.4759115.
[7] Guillaume Aubrun, Stanis law J. Szarek,
and
Deping
Ye.
Phase
transitions
for random states and a semicircle law
for
the
partial
transpose.
Physical
Review
A,
85(3):030302,
March
2012.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.85.030302.
URL http://dx.doi.
org/10.1103/PhysRevA.85.030302.
[8] Guillaume Aubrun, Stanislaw J. Szarek,
and Deping Ye. Entanglement thresholds
for random induced states.
Communica-
tions on Pure and Applied Mathematics, 67
(1):129–171, May 2013.
ISSN 1097-0312.
DOI: 10.1002/cpa.21460. URL http://dx.
doi.org/10.1002/cpa.21460.
[9] Joonwoo Bae, Dariusz Chru´sci´nski, and
Beatrix C. Hiesmayr.
Mirrored entan-
glement witnesses.
npj Quantum Infor-
mation, 6(1):15, February 2020.
ISSN
2056-6387. DOI: 10.1038/s41534-020-0242-
z.
URL http://dx.doi.org/10.1038/
s41534-020-0242-z.
[10] Nikhil Bansal, Wai-Keong Mok, Kishor
Bharti,
Dax Enshan Koh,
and Tobias
Haug.
Pseudorandom density matrices.
PRX Quantum, 6:020322, May 2025. DOI:
10.1103/PRXQuantum.6.020322.
URL
https://link.aps.org/doi/10.1103/
PRXQuantum.6.020322.
[11] Bruno Bertini, Katja Klobas, and Tsung-
Cheng
Lu.
Entanglement
negativity
and mutual information after a quan-
tum
quench:
Exact
link
from
space-
time
duality.
Physical
Review
Let-
ters,
129(14):140503,
September
2022.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.129.140503. URL http://dx.doi.
org/10.1103/PhysRevLett.129.140503.
[12] Kishor
Bharti,
Alba
Cervera-Lierta,
Thi
Ha
Kyaw,
Tobias
Haug,
Sumner
Alperin-Lea,
Abhinav Anand,
Matthias
Degroote, Hermanni Heimonen, Jakob S.
Kottmann, Tim Menke, Wai-Keong Mok,
Sukin Sim, Leong-Chuan Kwek, and Al´an
Aspuru-Guzik.
Noisy intermediate-scale
quantum algorithms.
Reviews of Modern
Physics,
94(1):015004,
February
2022.
ISSN 1539-0756.
DOI: 10.1103/revmod-
phys.94.015004.
URL http://dx.doi.
org/10.1103/RevModPhys.94.015004.
[13] Udaysinh T. Bhosale, Steven Tomsovic,
and Arul Lakshminarayan. Entanglement
between two subsystems, the wigner semi-
circle and extreme-value statistics. Phys-
ical Review A, 85(6):062331, June 2012.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.85.062331.
URL http://dx.doi.
org/10.1103/PhysRevA.85.062331.
[14] Zvika Brakerski, Ran Canetti, and Lu-
owen
Qian.
On
the
Computational
Hardness Needed for Quantum Cryptog-
raphy.
In Yael Tauman Kalai, editor,
14th
Innovations
in
Theoretical
Com-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
21
puter Science Conference (ITCS 2023),
volume 251 of Leibniz International Pro-
ceedings in Informatics (LIPIcs), pages
24:1–24:21,
Dagstuhl,
Germany,
2023.
Schloss Dagstuhl – Leibniz-Zentrum f¨ur
Informatik.
ISBN
978-3-95977-263-1.
DOI: 10.4230/LIPIcs.ITCS.2023.24. URL
https://drops.dagstuhl.de/entities/
document/10.4230/LIPIcs.ITCS.2023.
24.
[15] Samuel L Braunstein. Geometry of quan-
tum inference.
Physics Letters A, 219
(3-4):169–174, 1996.
DOI: 10.1016/0375-
9601(96)00365-9.
[16] Sergey Bravyi, David Fattal, and Daniel
Gottesman.
Ghz extraction yield for
multipartite stabilizer states.
Journal
of
Mathematical
Physics,
47(6):062106,
June 2006.
ISSN 1089-7658.
DOI:
10.1063/1.2203431. URL http://dx.doi.
org/10.1063/1.2203431.
[17] Tiff Brydges, Andreas Elben, Petar Ju-
rcevic, Benoˆıt Vermersch, Christine Maier,
Ben P. Lanyon, Peter Zoller, Rainer Blatt,
and Christian F. Roos. Probing r´enyi en-
tanglement entropy via randomized mea-
surements.
Science, 364(6437):260–263,
April 2019.
ISSN 1095-9203.
DOI:
10.1126/science.aau4963.
URL http://
dx.doi.org/10.1126/science.aau4963.
[18] Harry Buhrman, Lance Fortnow, Ilan New-
man, and Hein R¨ohrig.
Quantum prop-
erty testing.
SIAM Journal on Com-
puting,
37(5):1387–1400,
2008.
DOI:
10.1137/S009753970444241.
[19] Pasquale
Calabrese,
John
Cardy,
and
Erik Tonni.
Entanglement negativity in
quantum field theory.
Physical Review
Letters, 109(13):130502, September 2012.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.109.130502. URL http://dx.doi.
org/10.1103/PhysRevLett.109.130502.
[20] Pasquale
Calabrese,
John
Cardy,
and
Erik Tonni.
Finite temperature entan-
glement negativity in conformal field the-
ory.
Journal of Physics A: Mathematical
and Theoretical, 48(1):015006, December
2014. ISSN 1751-8121. DOI: 10.1088/1751-
8113/48/1/015006. URL http://dx.doi.
org/10.1088/1751-8113/48/1/015006.
[21] Jose Carrasco, Matteo Votto, Vittorio Vi-
tale, Christian Kokail, Antoine Neven, Pe-
ter Zoller, Benoˆıt Vermersch, and Bar-
bara Kraus.
Entanglement phase dia-
grams from partial transpose moments.
Physical Review A, 109(1):012422, January
2024. ISSN 2469-9934. DOI: 10.1103/phys-
reva.109.012422.
URL http://dx.doi.
org/10.1103/PhysRevA.109.012422.
[22] Hilary A. Carteret.
Noiseless quantum
circuits
for
the
peres
separability
cri-
terion.
Physical Review Letters, 94(4):
040502, January 2005.
ISSN 1079-7114.
DOI:
10.1103/physrevlett.94.040502.
URL
http://dx.doi.org/10.1103/
PhysRevLett.94.040502.
[23] C. Castelnovo.
Negativity and topolog-
ical order in the toric code.
Physical
Review A, 88(4):042319,
October 2013.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.88.042319.
URL http://dx.doi.
org/10.1103/PhysRevA.88.042319.
[24] K. Chen and L.-A. Wu.
A matrix re-
alignment method for recognizing entangle-
ment. Quantum Information and Compu-
tation, 3(3):193–202, May 2003. ISSN 1533-
7146. DOI: 10.26421/qic3.3-1. URL http:
//dx.doi.org/10.26421/QIC3.3-1.
[25] Lin Chen, Martin Aulbach, and Michal Ha-
jduˇsek. Comparison of different definitions
of the geometric measure of entangle-
ment. Phys. Rev. A, 89:042305, Apr 2014.
DOI: 10.1103/PhysRevA.89.042305. URL
https://link.aps.org/doi/10.1103/
PhysRevA.89.042305.
[26] Andrew M. Childs,
Aram W. Harrow,
and Pawe l Wocjan.
Weak Fourier-Schur
Sampling, the Hidden Subgroup Problem,
and the Quantum Collision Problem, page
598–609. Springer Berlin Heidelberg, 2007.
ISBN 9783540709183. DOI: 10.1007/978-
3-540-70918-3˙51.
URL http://dx.doi.
org/10.1007/978-3-540-70918-3_51.
[27] Dariusz
Chru´sci´nski
and
Gniewomir
Sarbicki.
Entanglement witnesses:
con-
struction,
analysis
and
classification.
Journal
of
Physics
A:
Mathemati-
cal
and
Theoretical,
47(48):483001,
November
2014.
ISSN
1751-8121.
DOI:
10.1088/1751-8113/47/48/483001.
URL
http://dx.doi.org/10.1088/
1751-8113/47/48/483001.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
22
[28] Chia-Min Chung,
Vincenzo Alba,
Lars
Bonnes, Pochung Chen, and Andreas M.
L¨auchli. Entanglement negativity via the
replica trick:
A quantum monte carlo
approach.
Physical Review B,
90(6):
064401, August 2014.
ISSN 1550-235X.
DOI: 10.1103/physrevb.90.064401.
URL
http://dx.doi.org/10.1103/PhysRevB.
90.064401.
[29] J. Ignacio Cirac, David P´erez-Garc´ıa, Nor-
bert Schuch, and Frank Verstraete.
Ma-
trix
product
states
and
projected
en-
tangled pair states:
Concepts, symme-
tries,
theorems.
Reviews
of
Modern
Physics,
93(4):045003,
December
2021.
ISSN 1539-0756.
DOI: 10.1103/revmod-
phys.93.045003.
URL http://dx.doi.
org/10.1103/RevModPhys.93.045003.
[30] Eyal Cornfeld, Moshe Goldstein, and Eran
Sela.
Imbalance entanglement:
Symme-
try decomposition of negativity.
Phys-
ical Review A, 98(3):032302, September
2018. ISSN 2469-9934. DOI: 10.1103/phys-
reva.98.032302.
URL http://dx.doi.
org/10.1103/PhysRevA.98.032302.
[31] Alexander M. Dalzell, Nicholas Hunter-
Jones, and Fernando G. S. L. Brand˜ao.
Random
quantum
circuits
transform
local noise into global white noise. Com-
munications
in
Mathematical
Physics,
405(3):78,
March
2024.
ISSN
1432-
0916.
DOI: 10.1007/s00220-024-04958-z.
URL
http://dx.doi.org/10.1007/
s00220-024-04958-z.
[32] Philippe Di Francesco, Pierre Mathieu, and
David S´en´echal.
Conformal field theory.
Graduate texts in contemporary physics.
Springer, New York, NY, 1997.
DOI:
10.1007/978-1-4612-2256-9.
URL https:
//cds.cern.ch/record/639405.
[33] Yi-Ming Ding,
Yin Tang,
Zhe Wang,
Zhiyan
Wang,
Bin-Bin
Mao,
and
Zheng
Yan.
Tracking
the
variation
of
entanglement
r´enyi
negativity:
A
quantum
monte
carlo
study.
Phys.
Rev. B, 111:L241108, Jun 2025.
DOI:
10.1103/PhysRevB.111.L241108.
URL
https://link.aps.org/doi/10.1103/
PhysRevB.111.L241108.
[34] Souvik
Dutta
and
Thomas
Faulkner.
A canonical purification for the entan-
glement
wedge
cross-section.
Journal
of
High
Energy
Physics,
2021(3):178,
March 2021.
ISSN 1029-8479.
DOI:
10.1007/jhep03(2021)178.
URL http://
dx.doi.org/10.1007/JHEP03(2021)178.
[35] Carl Eckart and Gale Young.
The ap-
proximation of one matrix by another of
lower rank. Psychometrika, 1(3):211–218,
September 1936.
ISSN 1860-0980.
DOI:
10.1007/bf02288367.
URL http://dx.
doi.org/10.1007/BF02288367.
[36] J
Eisert,
F
G
S
L
Brand˜ao,
and
K M R Audenaert.
Quantitative en-
tanglement
witnesses.
New
Journal
of
Physics,
9(3):46–46,
March
2007.
ISSN
1367-2630.
DOI:
10.1088/1367-
2630/9/3/046. URL http://dx.doi.org/
10.1088/1367-2630/9/3/046.
[37] Viktor
Eisler
and
Zolt´an
Zimbor´as.
Entanglement
negativity
in
the
har-
monic chain out of equilibrium.
New
Journal
of
Physics,
16(12):123020,
December
2014.
ISSN
1367-2630.
DOI:
10.1088/1367-2630/16/12/123020.
URL
http://dx.doi.org/10.1088/
1367-2630/16/12/123020.
[38] Artur K. Ekert, Carolina Moura Alves,
Daniel
K.
L.
Oi,
Micha l
Horodecki,
Pawe l Horodecki, and L. C. Kwek.
Di-
rect estimations of linear and nonlinear
functionals of a quantum state.
Phys.
Rev. Lett., 88:217901, May 2002.
DOI:
10.1103/PhysRevLett.88.217901.
URL
https://link.aps.org/doi/10.1103/
PhysRevLett.88.217901.
[39] A. Elben,
B. Vermersch,
C. F. Roos,
and P. Zoller. Statistical correlations be-
tween locally randomized measurements:
A toolbox for probing entanglement in
many-body
quantum
states.
Physi-
cal Review A, 99(5):200501, May 2019.
ISSN
2469-9934.
DOI:
10.1103/phys-
reva.99.052323.
URL http://dx.doi.
org/10.1103/PhysRevA.99.052323.
[40] Andreas Elben,
Richard Kueng,
Hsin-
Yuan
(Robert)
Huang,
Rick
van
Bij-
nen, Christian Kokail, Marcello Dalmonte,
Pasquale Calabrese, Barbara Kraus, John
Preskill, Peter Zoller, and Benoˆıt Ver-
mersch.
Mixed-state entanglement from
local randomized measurements.
Phys-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
23
ical Review Letters, 125(20), November
2020. ISSN 1079-7114. DOI: 10.1103/phys-
revlett.125.200501. URL http://dx.doi.
org/10.1103/PhysRevLett.125.200501.
[41] Motohisa Fukuda and Piotr ´Sniady. Par-
tial transpose of random quantum states:
Exact formulas and meanders.
Jour-
nal of Mathematical Physics, 54(4):042202,
April 2013.
ISSN 1089-7658.
DOI:
10.1063/1.4799440. URL http://dx.doi.
org/10.1063/1.4799440.
[42] Juan
Carlos
Garcia-Escartin
and
Pe-
dro Chamorro-Posada.
swap test and
hong-ou-mandel
effect
are
equivalent.
Phys.
Rev.
A,
87:052330,
May
2013.
DOI: 10.1103/PhysRevA.87.052330. URL
https://link.aps.org/doi/10.1103/
PhysRevA.87.052330.
[43] Daniel Gottesman.
Stabilizer codes and
quantum
error
correction.
Caltech
Ph.
D.
PhD thesis, Thesis, eprint:
quant-
ph/9705052, 1997.
[44] Daniel Gottesman. The heisenberg repre-
sentation of quantum computers.
arXiv
quant-ph/9807006, 1998.
URL https://
arxiv.org/abs/quant-ph/9807006.
[45] Daniel Gottesman. Theory of fault-tolerant
quantum computation. Phys. Rev. A, 57:
127–137, Jan 1998.
DOI: 10.1103/Phys-
RevA.57.127.
URL https://link.aps.
org/doi/10.1103/PhysRevA.57.127.
[46] Johnnie Gray, Leonardo Banchi, Abolfazl
Bayat,
and Sougato Bose.
Machine-
learning-assisted many-body entanglement
measurement.
Physical
Review
Let-
ters,
121(15):150503,
October
2018.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.121.150503. URL http://dx.doi.
org/10.1103/PhysRevLett.121.150503.
[47] Alex Grilo and ´Alvaro Y´ang¨uez.
Quan-
tum pseudoresources imply cryptography.
IACR Communications in Cryptology, 2
(4):2, January 2026.
ISSN 3006-5496.
DOI: 10.62056/ahbngyl7s.
URL http://
dx.doi.org/10.62056/ahbngyl7s.
[48] Otfried G¨uhne and Norbert L¨utkenhaus.
Nonlinear entanglement witnesses.
Phys.
Rev. Lett., 96:170502, May 2006.
DOI:
10.1103/PhysRevLett.96.170502.
URL
https://link.aps.org/doi/10.1103/
PhysRevLett.96.170502.
[49] Otfried G¨uhne and G´eza T´oth.
En-
tanglement detection.
Physics Reports,
474(1-6):1–75, April 2009.
ISSN 0370-
1573. DOI: 10.1016/j.physrep.2009.02.004.
URL
http://dx.doi.org/10.1016/j.
physrep.2009.02.004.
[50] Michael JW Hall. Random quantum corre-
lations and density operator distributions.
Physics Letters A, 242(3):123–129, 1998.
DOI: 10.1016/S0375-9601(98)00190-X.
[51] Dominik Hangleiter and Michael J. Gul-
lans. Bell sampling from quantum circuits.
Phys. Rev. Lett., 133:020601, Jul 2024.
DOI:
10.1103/PhysRevLett.133.020601.
URL
https://link.aps.org/doi/10.
1103/PhysRevLett.133.020601.
[52] O. Hart and C. Castelnovo.
Entangle-
ment negativity and sudden death in the
toric code at finite temperature.
Physi-
cal Review B, 97(14):144410, April 2018.
ISSN
2469-9969.
DOI:
10.1103/phys-
revb.97.144410.
URL http://dx.doi.
org/10.1103/PhysRevB.97.144410.
[53] Tobias Haug and Poetri Sonya Tarabunga.
Efficient witnessing and testing of magic
in mixed quantum states.
npj Quantum
Info., 12(1):40, Feb 2026.
ISSN 2056-
6387.
DOI: 10.1038/s41534-026-01189-
z.
URL
https://doi.org/10.1038/
s41534-026-01189-z.
[54] Tobias Haug, Nikhil Bansal, Wai-Keong
Mok, Dax Enshan Koh, and Kishor Bharti.
Pseudorandom
quantum
authentication.
arXiv preprint arXiv:2501.00951, 2025.
[55] Tobias Haug, Kishor Bharti, and Dax En-
shan Koh.
Pseudorandom unitaries are
neither real nor sparse nor noise-robust.
Quantum,
9:1759,
June
2025.
ISSN
2521-327X.
DOI: 10.22331/q-2025-06-04-
1759. URL https://doi.org/10.22331/
q-2025-06-04-1759.
[56] Micha l Horodecki, Pawe l Horodecki, and
Ryszard Horodecki. Separability of mixed
states:
necessary and sufficient condi-
tions.
Physics
Letters
A,
223(1–2):
1–8,
November
1996.
ISSN
0375-
9601. DOI: 10.1016/s0375-9601(96)00706-
2.
URL http://dx.doi.org/10.1016/
S0375-9601(96)00706-2.
[57] Ryszard
Horodecki,
Pawe l
Horodecki,
Micha l Horodecki, and Karol Horodecki.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
24
Quantum entanglement. Reviews of Mod-
ern Physics, 81(2):865–942, June 2009.
ISSN 1539-0756.
DOI: 10.1103/revmod-
phys.81.865.
URL http://dx.doi.org/
10.1103/RevModPhys.81.865.
[58] Hsin-Yuan Huang, Richard Kueng, and
John Preskill.
Predicting many prop-
erties of a quantum system from very
few measurements.
Nature Physics, 16
(10):1050–1057, June 2020.
ISSN 1745-
2481.
DOI:
10.1038/s41567-020-0932-
7.
URL http://dx.doi.org/10.1038/
s41567-020-0932-7.
[59] Zhengfeng Ji, Yi-Kai Liu, and Fang Song.
Pseudorandom quantum states.
In An-
nual International Cryptology Conference,
pages 126–152. Springer,
2018.
DOI:
10.1007/978-3-319-96878-0˙5.
[60] Nathaniel Johnston and David W. Kribs.
Duality of entanglement norms. Houston J.
Math., 41(3):831–847, 2015. URL https:
//arxiv.org/abs/1304.2328.
[61] Richard Jozsa. Fidelity for mixed quantum
states. Journal of Modern Optics, 41(12):
2315–2323, December 1994.
ISSN 1362-
3044.
DOI: 10.1080/09500349414552171.
URL
http://dx.doi.org/10.1080/
09500349414552171.
[62] Richard Kueng and David Gross.
Qubit
stabilizer states are complex projective 3-
designs.
arxiv:1510.02767, 2015.
URL
https://arxiv.org/abs/1510.02767.
[63] Yirun Arthur Lee and Guifre Vidal. Entan-
glement negativity and topological order.
Physical Review A, 88(4):042318, October
2013. ISSN 1094-1622. DOI: 10.1103/phys-
reva.88.042318.
URL http://dx.doi.
org/10.1103/PhysRevA.88.042318.
[64] Shuheng Liu, Matteo Fadel, Qiongyi He,
Marcus Huber, and Giuseppe Vitagliano.
Bounding
entanglement
dimensionality
from the covariance matrix.
Quantum,
8:1236,
January
2024.
ISSN
2521-
327X.
DOI: 10.22331/q-2024-01-30-1236.
URL
http://dx.doi.org/10.22331/
q-2024-01-30-1236.
[65] Shuo Liu, Ming-Rui Li, Shi-Xin Zhang,
Shao-Kai Jian,
and Hong Yao.
Uni-
versal kardar-parisi-zhang scaling in noisy
hybrid quantum circuits.
Physical Re-
view
B,
107(20):L201113,
May
2023.
ISSN
2469-9969.
DOI:
10.1103/phys-
revb.107.l201113.
URL http://dx.doi.
org/10.1103/PhysRevB.107.L201113.
[66] Shuo Liu, Ming-Rui Li, Shi-Xin Zhang,
and Shao-Kai Jian.
Entanglement struc-
ture and information protection in noisy
hybrid quantum circuits.
Physical Re-
view Letters, 132(24):240402, June 2024.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.132.240402. URL http://dx.doi.
org/10.1103/PhysRevLett.132.240402.
[67] Tong Liu, Shang Liu, Hekang Li, Hao
Li, Kaixuan Huang, Zhongcheng Xiang,
Xiaohui Song, Kai Xu, Dongning Zheng,
and
Heng
Fan.
Observation
of
en-
tanglement transition of pseudo-random
mixed states.
Nature Communications,
14(1):1971,
April
2023.
ISSN
2041-
1723.
DOI: 10.1038/s41467-023-37511-
y.
URL http://dx.doi.org/10.1038/
s41467-023-37511-y.
[68] Zhenhuan Liu,
Yifan Tang,
Hao Dai,
Pengyu Liu, Shu Chen, and Xiongfeng
Ma.
Detecting entanglement in quan-
tum
many-body
systems
via
permuta-
tion
moments.
Physical
Review
Let-
ters,
129(26):260501,
December
2022.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.129.260501. URL http://dx.doi.
org/10.1103/PhysRevLett.129.260501.
[69] Benjamin Lovitz and Angus Lowe. Nearly
tight bounds for testing tree tensor network
states. IEEE Transactions on Information
Theory, 72(5):3074–3097, May 2026. ISSN
1557-9654. DOI: 10.1109/tit.2026.3670320.
URL http://dx.doi.org/10.1109/TIT.
2026.3670320.
[70] Tsung-Cheng
Lu
and
Tarun
Grover.
Structure
of
quantum
entanglement
at
a
finite
temperature
critical
point.
Physical
Review
Research,
2(4):043345,
December
2020.
ISSN
2643-1564.
DOI:
10.1103/physrevresearch.2.043345.
URL
http://dx.doi.org/10.1103/
PhysRevResearch.2.043345.
[71] Tsung-Cheng
Lu,
Timothy
H.
Hsieh,
and Tarun Grover.
Detecting topolog-
ical
order
at
finite
temperature
using
entanglement negativity.
Physical Re-
view Letters,
125(11),
September 2020.
ISSN
1079-7114.
DOI:
10.1103/phys-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
25
revlett.125.116801. URL http://dx.doi.
org/10.1103/PhysRevLett.125.116801.
[72] Bivas Mallick, Ananda G. Maity, Nirman
Ganguly, and A. S. Majumdar.
Higher-
dimensional-entanglement
detection
and
quantum-channel
characterization
using
moments of generalized positive maps.
Physical Review A, 112(1):012416, July
2025. ISSN 2469-9934. DOI: 10.1103/nzrc-
8yrt. URL http://dx.doi.org/10.1103/
nzrc-8yrt.
[73] Alexey
Milekhin,
Pratik
Rath,
and
Wayne
Weng.
Computable
cross
norm
in
tensor
networks
and
holog-
raphy.
arxiv:2212.11978, 2024.
URL
https://arxiv.org/abs/2212.11978.
[74] Ashley Montanaro and Ronald de Wolf. A
survey of quantum property testing. The-
ory of Computing, 1(1):1–81, 2016. ISSN
1557-2862. DOI: 10.4086/toc.gs.2016.007.
URL http://dx.doi.org/10.4086/toc.
gs.2016.007.
[75] Simon
Morelli,
Marcus
Huber,
and
Armin Tavakoli.
Resource-efficient high-
dimensional entanglement detection via
symmetric projections.
Physical Review
Letters,
131(17):170201,
October
2023.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.131.170201. URL http://dx.doi.
org/10.1103/PhysRevLett.131.170201.
[76] Saheli
Mukherjee,
Bivas
Mallick,
Sahil
Gopalkrishna
Naik,
Ananda
G.
Maity, and A. S. Majumdar.
Detecting
genuine multipartite entanglement using
moments of positive maps. Phys. Rev. A,
112:062428, Dec 2025. DOI: 10.1103/ffch-
xyv2. URL https://link.aps.org/doi/
10.1103/ffch-xyv2.
[77] Celine Nadal, Satya N. Majumdar, and
Massimo Vergassola.
Phase transitions
in the distribution of bipartite entangle-
ment of a random pure state.
Physi-
cal Review Letters, 104(11):110501, March
2010. ISSN 1079-7114. DOI: 10.1103/phys-
revlett.104.110501. URL http://dx.doi.
org/10.1103/PhysRevLett.104.110501.
[78] Adam Nahum, Jonathan Ruhman, Sagar
Vijay, and Jeongwan Haah.
Quantum
entanglement growth under random uni-
tary dynamics.
Physical Review X, 7
(3):031016, July 2017.
ISSN 2160-3308.
DOI: 10.1103/physrevx.7.031016.
URL
http://dx.doi.org/10.1103/PhysRevX.
7.031016.
[79] Antoine Neven, Jose Carrasco, Vittorio
Vitale, Christian Kokail, Andreas Elben,
Marcello Dalmonte, Pasquale Calabrese,
Peter Zoller, Benoˆıt Vermersch, Richard
Kueng, and Barbara Kraus.
Symmetry-
resolved entanglement detection using par-
tial
transpose
moments.
npj
Quan-
tum Information, 7(1):152, October 2021.
ISSN 2056-6387. DOI: 10.1038/s41534-021-
00487-y.
URL http://dx.doi.org/10.
1038/s41534-021-00487-y.
[80] Michael A. Nielsen and Isaac L. Chuang.
Quantum Computation and Quantum In-
formation:
10th
Anniversary
Edition.
Cambridge University Press, 2011. ISBN
9781107002173.
[81] Ryan O’Donnell and John Wright. Quan-
tum spectrum testing.
In Proceedings
of the forty-seventh annual ACM sympo-
sium on Theory of Computing, STOC ’15,
page 529–538. ACM, June 2015.
DOI:
10.1145/2746539.2746582.
URL http://
dx.doi.org/10.1145/2746539.2746582.
[82] Don N. Page.
Average entropy of a
subsystem.
Physical Review Letters, 71
(9):1291–1294, August 1993.
ISSN 0031-
9007.
DOI: 10.1103/physrevlett.71.1291.
URL
http://dx.doi.org/10.1103/
PhysRevLett.71.1291.
[83] Asher
Peres.
Separability
criterion
for density matrices.
Physical Review
Letters,
77(8):1413–1415,
August 1996.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.77.1413.
URL http://dx.doi.
org/10.1103/PhysRevLett.77.1413.
[84] M.
B.
Plenio.
Logarithmic
negativ-
ity:
A
full
entanglement
monotone
that
is
not
convex.
Physical
Re-
view Letters, 95(9):090503, August 2005.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.95.090503.
URL http://dx.doi.
org/10.1103/PhysRevLett.95.090503.
[85] John
Preskill.
Quantum
computing
in the nisq era and beyond.
Quan-
tum,
2:79,
August 2018.
ISSN 2521-
327X.
DOI: 10.22331/q-2018-08-06-79.
URL
http://dx.doi.org/10.22331/
q-2018-08-06-79.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
26
[86] Tomaˇz Prosen and Iztok Piˇzorn.
Op-
erator space entanglement entropy in a
transverse
ising
chain.
Physical
Re-
view A, 76(3):032316,
September 2007.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.76.032316.
URL http://dx.doi.
org/10.1103/PhysRevA.76.032316.
[87] Dongheng Qian and Jing Wang.
Pro-
tect
measurement-induced
phase
tran-
sition
from
noise.
Physical
Review
Letters,
134(2):020403,
January
2025.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.134.020403. URL http://dx.doi.
org/10.1103/PhysRevLett.134.020403.
[88] Aniket Rath, Vittorio Vitale, Sara Mur-
ciano,
Matteo
Votto,
J´erˆome
Dubail,
Richard Kueng, Cyril Branciard, Pasquale
Calabrese, and Benoˆıt Vermersch.
En-
tanglement
barrier
and
its
symmetry
resolution:
Theory
and
experimen-
tal observation.
PRX Quantum, 4(1):
010318, February 2023.
ISSN 2691-3399.
DOI:
10.1103/prxquantum.4.010318.
URL
http://dx.doi.org/10.1103/
PRXQuantum.4.010318.
[89] Albert Rico.
State–entanglement-witness
contraction.
Phys.
Rev.
Lett.,
135:
170201, Oct 2025.
DOI: 10.1103/d6q5-
k7sh. URL https://link.aps.org/doi/
10.1103/d6q5-k7sh.
[90] Albert Rico and Felix Huber.
Entangle-
ment detection with trace polynomials.
Phys. Rev. Lett., 132:070202, Feb 2024.
DOI:
10.1103/PhysRevLett.132.070202.
URL
https://link.aps.org/doi/10.
1103/PhysRevLett.132.070202.
[91] Paola
Ruggiero,
Vincenzo
Alba,
and
Pasquale Calabrese.
Entanglement neg-
ativity in random spin chains.
Physi-
cal Review B, 94(3):035152, July 2016.
ISSN
2469-9969.
DOI:
10.1103/phys-
revb.94.035152.
URL http://dx.doi.
org/10.1103/PhysRevB.94.035152.
[92] Paola
Ruggiero,
Vincenzo
Alba,
and
Pasquale
Calabrese.
Negativity
spec-
trum of one-dimensional conformal field
theories.
Physical
Review
B,
94(19):
195121, November 2016. ISSN 2469-9969.
DOI: 10.1103/physrevb.94.195121.
URL
http://dx.doi.org/10.1103/PhysRevB.
94.195121.
[93] Shengqi Sang, Yaodong Li, Tianci Zhou,
Xiao
Chen,
Timothy
H.
Hsieh,
and
Matthew P.A. Fisher. Entanglement neg-
ativity at measurement-induced critical-
ity.
PRX Quantum, 2(3), July 2021.
ISSN 2691-3399.
DOI: 10.1103/prxquan-
tum.2.030313. URL http://dx.doi.org/
10.1103/PRXQuantum.2.030313.
[94] Anna Sanpera, Dagmar Bruß, and Ma-
ciej Lewenstein.
Schmidt-number wit-
nesses and bound entanglement.
Physi-
cal Review A, 63(5):050301, April 2001.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.63.050301.
URL http://dx.doi.
org/10.1103/PhysRevA.63.050301.
[95] Norbert
Schuch,
Michael
M.
Wolf,
Frank Verstraete, and J. Ignacio Cirac.
Entropy
scaling
and
simulability
by
matrix
product
states.
Phys.
Rev.
Lett.,
100:030504,
Jan
2008.
DOI:
10.1103/PhysRevLett.100.030504.
URL
https://link.aps.org/doi/10.1103/
PhysRevLett.100.030504.
[96] Jiheon Seong, Jin-Woo Kim, Seungchan
Seo, Seung-Hyun Nam, Anindita Bera,
Dariusz
Chru´sci´nski,
June-Koo
Kevin
Rhee, Heonoh Kim, and Joonwoo Bae.
Practical and efficient verification of entan-
glement with incomplete measurement set-
tings. APS Open Science, 1:000008, April
2026. ISSN 3070-2240. DOI: 10.1103/sgbs-
7228. URL http://dx.doi.org/10.1103/
sgbs-7228.
[97] Daniel
Shapira,
Yishai
Shimoni,
and
Ofer
Biham.
Groverian
measure
of
entanglement for mixed states.
Phys.
Rev. A, 73:044301,
Apr 2006.
DOI:
10.1103/PhysRevA.73.044301.
URL
https://link.aps.org/doi/10.1103/
PhysRevA.73.044301.
[98] Hassan Shapourian and Shinsei Ryu. En-
tanglement negativity of fermions: Mono-
tonicity, separability criterion, and clas-
sification of few-mode states.
Physical
Review A, 99(2):022310, February 2019.
ISSN
2469-9934.
DOI:
10.1103/phys-
reva.99.022310.
URL http://dx.doi.
org/10.1103/PhysRevA.99.022310.
[99] Hassan Shapourian, Ken Shiozaki, and
Shinsei Ryu.
Partial time-reversal trans-
formation and entanglement negativity in
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
27
fermionic systems. Physical Review B, 95
(16):165601, April 2017. ISSN 2469-9969.
DOI: 10.1103/physrevb.95.165101.
URL
http://dx.doi.org/10.1103/PhysRevB.
95.165101.
[100] Hassan Shapourian,
Shang Liu,
Jonah
Kudler-Flam,
and
Ashvin
Vishwanath.
Entanglement
negativity
spectrum
of
random mixed states:
A diagrammatic
approach.
PRX Quantum, 2(3):030347,
September
2021.
ISSN
2691-3399.
DOI:
10.1103/prxquantum.2.030347.
URL
http://dx.doi.org/10.1103/
PRXQuantum.2.030347.
[101] Adam L. Shaw,
Zhuo Chen,
Joonhee
Choi,
Daniel K. Mark,
Pascal Scholl,
Ran Finkelstein, Andreas Elben, Soonwon
Choi, and Manuel Endres.
Benchmark-
ing highly entangled states on a 60-atom
analogue quantum simulator. Nature, 628
(8006):71–77, March 2024.
ISSN 1476-
4687.
DOI: 10.1038/s41586-024-07173-
x.
URL http://dx.doi.org/10.1038/
s41586-024-07173-x.
[102] Nicholas E. Sherman, Trithep Devakul,
Matthew B. Hastings, and Rajiv R. P.
Singh.
Nonzero-temperature
entangle-
ment negativity of quantum spin mod-
els:
Area
law,
linked
cluster
expan-
sions, and sudden death.
Physical Re-
view
E,
93(2):022128,
February
2016.
ISSN
2470-0053.
DOI:
10.1103/phys-
reve.93.022128.
URL http://dx.doi.
org/10.1103/PhysRevE.93.022128.
[103] Alexander Streltsov, Hermann Kamper-
mann, and Dagmar Bruß. Linking a dis-
tance measure of entanglement to its con-
vex roof. New Journal of Physics, 12(12):
123004, December 2010. ISSN 1367-2630.
DOI:
10.1088/1367-2630/12/12/123004.
URL
http://dx.doi.org/10.1088/
1367-2630/12/12/123004.
[104] Jakub Szczepaniak, Owidiusz Makuta, and
Remigiusz Augusiak.
Entanglement wit-
nesses for stabilizer states and subspaces
beyond qubits.
Reports on Progress in
Physics, 88(11):117602, November 2025.
ISSN
1361-6633.
DOI:
10.1088/1361-
6633/ae1b67.
URL http://dx.doi.org/
10.1088/1361-6633/ae1b67.
[105] Barbara M. Terhal and Pawe l Horodecki.
Schmidt
number
for
density
matrices.
Physical Review A, 61(4):040301, March
2000. ISSN 1094-1622. DOI: 10.1103/phys-
reva.61.040301.
URL http://dx.doi.
org/10.1103/PhysRevA.61.040301.
[106] Emanuele
Tirrito,
Poetri
Sonya
Tarabunga,
Gugliemo
Lami,
Titas
Chanda,
Lorenzo Leone,
Salvatore FE
Oliviero, Marcello Dalmonte, Mario Col-
lura, and Alioscia Hamma.
Quantifying
nonstabilizerness
through
entanglement
spectrum flatness. Physical Review A, 109
(4):L040401, 2024.
URL https://doi.
org/10.1103/PhysRevA.109.L040401.
[107] G. Vidal and R. F. Werner.
Com-
putable measure of entanglement.
Phys-
ical Review A,
65(3):032314,
February
2002. ISSN 1094-1622. DOI: 10.1103/phys-
reva.65.032314.
URL http://dx.doi.
org/10.1103/PhysRevA.65.032314.
[108] Guifr´e Vidal.
Entanglement monotones.
Journal
of
Modern
Optics,
47(2–3):
355–376,
February 2000.
ISSN 1362-
3044.
DOI: 10.1080/09500340008244048.
URL
http://dx.doi.org/10.1080/
09500340008244048.
[109] Guifr´e Vidal and Rolf Tarrach.
Ro-
bustness of entanglement.
Physical Re-
view
A,
59(1):141–155,
January
1999.
ISSN
1094-1622.
DOI:
10.1103/phys-
reva.59.141.
URL http://dx.doi.org/
10.1103/PhysRevA.59.141.
[110] Fo-Hong Wang and Xiao Yan Xu.
En-
tanglement r´enyi negativity of interact-
ing fermions from quantum monte carlo
simulations.
Nature
Communications,
16(1):2637,
Mar
2025.
ISSN
2041-
1723.
DOI: 10.1038/s41467-025-57971-
8.
URL
https://doi.org/10.1038/
s41467-025-57971-8.
[111] Xiaoguang
Wang,
Chang-Shui
Yu,
and
X.X.
Yi.
An
alternative
quan-
tum
fidelity
for
mixed
states
of
qu-
dits.
Physics Letters A, 373(1):58–60,
December
2008.
ISSN
0375-9601.
DOI:
10.1016/j.physleta.2008.10.083.
URL
http://dx.doi.org/10.1016/j.
physleta.2008.10.083.
[112] Yiding Wang,
Tinggui Zhang,
Xiaofen
Huang, and Shao-Ming Fei.
Moments
based
entanglement
criteria
and
mea-
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
28
sures.
Journal of Physics A: Mathemat-
ical and Theoretical, 57(20):205301, May
2024. ISSN 1751-8121. DOI: 10.1088/1751-
8121/ad40e3.
URL http://dx.doi.org/
10.1088/1751-8121/ad40e3.
[113] Zack Weinstein, Yimu Bao, and Ehud
Altman. Measurement-induced power-law
negativity in an open monitored quantum
circuit.
Physical Review Letters, 129(8):
080501, August 2022.
ISSN 1079-7114.
DOI:
10.1103/physrevlett.129.080501.
URL
http://dx.doi.org/10.1103/
PhysRevLett.129.080501.
[114] Xueda Wen, Po-Yao Chang, and Shin-
sei Ryu.
Topological entanglement neg-
ativity in chern-simons theories.
Jour-
nal of High Energy Physics, 2016(9):12,
September 2016.
ISSN 1029-8479.
DOI:
10.1007/jhep09(2016)012.
URL http://
dx.doi.org/10.1007/JHEP09(2016)012.
[115] Kai-Hsin Wu,
Tsung-Cheng Lu,
Chia-
Min Chung, Ying-Jer Kao, and Tarun
Grover.
Entanglement
renyi
negativ-
ity
across
a
finite
temperature
tran-
sition:
A monte carlo study.
Phys.
Rev. Lett., 125:140603, Sep 2020.
DOI:
10.1103/PhysRevLett.125.140603.
URL
https://link.aps.org/doi/10.1103/
PhysRevLett.125.140603.
[116] Elisabeth
Wybo,
Michael
Knap,
and
Frank Pollmann.
Dynamics of negativity
of a wannier–stark many-body localized
system coupled to a bath. physica status
solidi (b), 259(5):2100161, 2022.
DOI:
https://doi.org/10.1002/pssb.202100161.
URL
https://onlinelibrary.wiley.
com/doi/abs/10.1002/pssb.202100161.
[117] Chao Yin and Shang Liu. Mixed-state en-
tanglement measures in topological order.
Physical Review B, 108(3):131601, July
2023. ISSN 2469-9969. DOI: 10.1103/phys-
revb.108.035152.
URL http://dx.doi.
org/10.1103/PhysRevB.108.035152.
[118] Chao Yin and Zhenhuan Liu.
Universal
entanglement and correlation measure in
two-dimensional conformal field theories.
Physical Review Letters, 130(13), March
2023. ISSN 1079-7114. DOI: 10.1103/phys-
revlett.130.131601. URL http://dx.doi.
org/10.1103/PhysRevLett.130.131601.
[119] Xiao-Dong Yu, Satoya Imai, and Otfried
G¨uhne.
Optimal
entanglement
certi-
fication
from
moments
of
the
partial
transpose.
Physical Review Letters, 127
(6):060504, August 2021. ISSN 1079-7114.
DOI:
10.1103/physrevlett.127.060504.
URL
http://dx.doi.org/10.1103/
PhysRevLett.127.060504.
[120] Paolo Zanardi. Entanglement of quantum
evolutions. Phys. Rev. A, 63:040304, Mar
2001. DOI: 10.1103/PhysRevA.63.040304.
URL
https://link.aps.org/doi/10.
1103/PhysRevA.63.040304.
[121] Tinggui
Zhang,
Naihuan
Jing,
and
Shao-Ming Fei.
Quantum separability
criteria based on realignment moments.
Quantum
Information
Processing,
21
(8):276,
August
2022.
ISSN
1573-
1332.
DOI: 10.1007/s11128-022-03630-6.
URL
http://dx.doi.org/10.1007/
s11128-022-03630-6.
[122] You
Zhou,
Pei
Zeng,
and
Zhenhuan
Liu.
Single-copies
estimation
of
en-
tanglement negativity.
Physical Review
Letters, 125(20):200502, November 2020.
ISSN
1079-7114.
DOI:
10.1103/phys-
revlett.125.200502. URL http://dx.doi.
org/10.1103/PhysRevLett.125.200502.
[123] Huangjun Zhu. Multiqubit clifford groups
are
unitary
3-designs.
Physical
Re-
view A, 96(6):062336,
December 2017.
ISSN
2469-9934.
DOI:
10.1103/phys-
reva.96.062336.
URL http://dx.doi.
org/10.1103/PhysRevA.96.062336.
[124] Huangjun Zhu, Richard Kueng, Markus
Grassl, and David Gross.
The clifford
group fails gracefully to be a unitary 4-
design.
arXiv:1609.08172, 2016.
URL
https://arxiv.org/abs/1609.08172.
[125] Karol
Zyczkowski
and
Hans-J¨urgen
Sommers.
Induced
measures
in
the
space of mixed quantum states.
Jour-
nal
of
Physics
A:
Mathematical
and
General,
34(35):7111–7125,
aug
2001.
DOI:
10.1088/0305-4470/34/35/335.
URL
https://doi.org/10.1088%
2F0305-4470%2F34%2F35%2F335.
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
29
Appendix
We provide proofs and additional details supporting the claims in the main text.
