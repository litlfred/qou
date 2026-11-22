---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-008-6-entanglement-testing
section_title: "Entanglement testing"
section_number: 6
pages: 9-10
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
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
