---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-018-13-discussion
section_title: "Discussion"
section_number: 13
pages: 18-20
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
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
