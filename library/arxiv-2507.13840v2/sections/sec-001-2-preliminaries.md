---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 4-5
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
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
