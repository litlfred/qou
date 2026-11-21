---
doc_id: arxiv-2605.09605v2
doc_title: "Cocycle Actions on Hidden Quantum Markov Models: Symmetry Protection and Topological Order"
section_id: sec-004-appedix-hidden-quantum-markov-models
section_title: "Appedix: Hidden Quantum Markov Models"
section_number: null
pages: 12-17
source_pdf: 2605.09605v2.pdf
source_sha256: 24496fb444a2b558
toc_source: outline
doc_brief: "Cocycle Actions on Hidden Quantum Markov Models: Symmetry Protection and Topological Order — We develop a symmetry action framework for hidden quantum Markov models (HQMMs) tailored to"
---
Appedix: Hidden Quantum Markov Models
Let H and K be separable Hilbert spaces, representing the hidden and observable degrees of
freedom at a single lattice site, respectively. The corresponding single-site algebras are defined as
the C∗-algebras of bounded linear operators: AH := B(H) and AO := B(K), each equipped with
the operator norm and containing the identity operator. For each site n ∈Z, the full single-site
algebra is the spatial C∗-tensor product
A{n} := AH ⊗AO ∼= B(H ⊗K),
where the isomorphism holds by separability of H and K.
For a finite subset Λ ⊂Z, the finite-volume composite algebra is the C∗-tensor product over
the sites:
AΛ :=
O
n∈Λ
A{n} =
O
n∈Λ

AH ⊗AO

n,
where (AH ⊗AO)n denotes an isomorphic copy of the single-site algebra localized at position n.
The finite-volume hidden and observable subalgebras are given respectively by
AH,Λ :=
O
n∈Λ
(AH)n,
AO,Λ :=
O
n∈Λ
(AO)n,
which satisfy the factorization AΛ = AH,Λ ⊗AO,Λ.
For each n ∈Z, define the hidden embedding j(n)
H : AH ,→AH,Z by
j(n)
H (X) :=
O
k∈Z
X(H)
k
,
X(H)
k
=



X
if k = n,
IAH
otherwise,
extended continuously to the completion. This map is an isometric ∗-homomorphism. The ob-
servable embedding j(n)
O
: AO ,→AO,Z is defined analogously as
j(n)
O (Y ) :=
O
k∈Z
Y (O)
k
,
Y (O)
k
=



Y
if k = n,
IAO
otherwise.
The composite embedding at site n is j(n) := j(n)
H ⊗j(n)
O , satisfying j(n)(X ⊗Y ) = j(n)
H (X)·j(n)
O (Y ).
For any finite Λ ⊂Z, the embedding jΛ : N
n∈Λ(AH ⊗AO) ,→AZ is defined on elementary tensors
by
jΛ
 O
n∈Λ
(Xn ⊗Yn)

=
Y
n∈Λ
j(n)(Xn ⊗Yn),
with the product taken in increasing order of indices.
These embeddings are consistent: for
Λ ⊂Λ′, we have jΛ′ ◦ιΛ,Λ′ = jΛ, where ιΛ,Λ′ is the inclusion map tensoring with identities on the
additional sites.
The collection {AΛ, ιΛ,Λ′} forms a directed system under inclusion. The local algebra is the
algebraic direct limit Aloc
Z := S
Λ⊂Z finite AΛ, and the quasi-local C∗-algebra is its norm completion
AZ := Aloc
Z
∥·∥. When dim(H ⊗K) < ∞, AZ is a uniformly hyperfinite (UHF) C∗-algebra. The
hidden and observable quasi-local algebras AH,Z and AO,Z are constructed analogously, satisfying
the spatial tensor product relation AZ ∼= AH,Z ⊗AO,Z.
The shift automorphism σ ∈Aut(AZ) is defined on elementary tensors by σ
 N
n∈Z An

=
N
n∈Z An+1, extended continuously.
It satisfies σ ◦j(n) = j(n+1) for all n ∈Z, and {σn}n∈Z
forms a Z-action on AZ. There exists a strongly continuous one-parameter automorphism group
τ : R →Aut(AZ) with τ1 = σ, constructed via the crossed product AZ ⋊σ Z, with Liouvillian H
satisfying τt = exp(itH)(·) exp(−itH). The triple (AZ, R, τ) is a C∗-dynamical system.
Restricting to the half-infinite chain indexed by N0 = {0, 1, 2, . . . }, the one-sided quasi-local
algebra is
AN0 :=
[
m∈N0
m
O
n=0
(AH ⊗AO)n
∥·∥
,
with the embeddings j(n)
H , j(n)
O , j(n) restricted to n ≥0.
The shift restricts to a non-unital
endomorphism σ+ : AN0 →AN0 given by σ+(A) = I{0} ⊗A under the identification AN0 ∼=
A{0} ⊗AN0.
For each n ∈N0, define the finite-volume algebra A[0,n] := Nn
k=0(AH ⊗AO)k, a finite C∗-tensor
product. For m ≤n, the natural embedding ιm,n : A[0,m] ,→A[0,n] appends n−m identity factors.
The family {A[0,n], ιm,n}m≤n forms an inductive system, and AN0 is the norm completion of its
inductive limit [19, 17].
Let {φn}n∈N0 be a sequence where each φn is a state on A[0,n]. The sequence is said to satisfy
the Kolmogorov compatibility condition if for all m ≤n,
φn ◦ιm,n = φm.
This condition guarantees consistency of expectation values across different volumes.
Lemma A.1 (Projective Limit State). If {φn}n∈N0 satisfies the Kolmogorov compatibility condi-
tion, then there exists a unique state φ on AN0 such that φ|A[0,n] = φn for all n. Moreover, for
any A ∈AN0, φ(A) = limn→∞φn(An) whenever An ∈A[0,n] converges to A in norm.
Proof. For any local observable A belonging to some A[0,n], set φ(A) = φn(A). Compatibility
makes this well-defined. This gives a linear functional on the dense subalgebra of local observables,
which is positive and satisfies φ(I) = 1. Hence it extends uniquely to a state on the whole algebra
AN0 by continuity. The approximation property follows directly from the construction.
The HQMM structure is encoded in a completely positive unital (CPU) map
T : AH ⊗AH ⊗AO →AH,
which governs the joint evolution of hidden and observable degrees of freedom across adjacent
sites. For any X ∈AH and Y ∈AO, define the sliced maps TX,Y : AH →AH by
TX,Y (Z) := T (X ⊗Z ⊗Y ).
Given an initial state ϕ0 on AH, we construct finite-volume states as follows. For each n ∈N0,
define φn on A[0,n] on elementary tensors by
φn
 n
O
k=0
(Xk ⊗Yk)
!
:= ϕ0 ◦TX0,Y0 ◦TX1,Y1 ◦· · · ◦TXn,Yn(IAH),
where the composition denotes successive application of the maps, and ϕ0 is evaluated on the
resulting element of AH.
Theorem A.2 (Global HQMM State). Let T : AH ⊗AH ⊗AO →AH be a CPU map and ϕ0
a state on AH. For each n ∈N0, the functional φn defined above extends uniquely to a state
on A[0,n]. The sequence {φn}n∈N0 satisfies the Kolmogorov compatibility condition, and thus there
exists a unique state φ on AN0 such that φ|A[0,n] = φn for all n. This φ is called the global HQMM
state generated by (ϕ0, T ).
Proof. Unitality and complete positivity of T imply that each TX,Y is a CP map for fixed positive
elements X and Y , and if X = IAH and Y = IAO the map Z 7→TIAH ,IAH (Z) = T (IAH ⊗Z ⊗
IAO) is CPU . Hence for a given sequence of positive elements Xi, Yi, i = 0, 1, · · · , n, the map
ϕ0 ◦TX0,Y0 ◦· · · ◦TXn,Yn(·) is a positive linear functional on AH. Moreover, φn(I) = 1. By the
universal property of the C∗-tensor product, φn extends to a state on A[0,n]. For compatibility,
consider A ∈A[0,n] and its embedding ιn,n+1(A) = A ⊗(IAH ⊗IAO). Then
φn+1(ιn,n+1(A)) = ϕ0 ◦TX0,Y0 ◦· · · ◦TXn,Yn ◦TIAH ,IAO(IAH).
Unitality of T gives TIAH ,IAO = IAH, so the right-hand side equals ϕ0 ◦TX0,Y0 ◦· · · ◦TXn,Yn(IAH) =
φn(A). By linearity and continuity, φn+1 ◦ιn,n+1 = φn, and similarly for all m ≤n. The existence
and uniqueness of φ follow from Lemma 1.
The hidden marginal state φH on AH,N0 is defined by restriction: for A ∈AH,N0, φH(A) :=
φ(A ⊗IAO,N0). For a local observable Nn
k=0 Xk, this becomes
φH
 n
O
k=0
Xk
!
= ϕ0 ◦TX0,IAO ◦· · · ◦TXn,IAO(IAH),
defining a quantum Markov chain on AH,N0. The observation marginal φO on AO,N0 is defined
analogously: for B ∈AO,N0, φO(B) := φ(IAH,N0 ⊗B). For a local observable Nn
k=0 Yk,
φO
 n
O
k=0
Yk
!
= ϕ0 ◦TIAH ,Y0 ◦· · · ◦TIAH ,Yn(IAH),
which represents the statistics of the observed process. The global state φ serves as a coupling of
these two marginals.
Two distinct causal structures arise as special realizations of T , corresponding to different
orderings of hidden transition and observable emission. Let EH : AH ⊗AH →AH be a CPU map
describing the hidden transition, and EH,O : AH ⊗AO →AH a CPU map describing the emission.
The conventional causal structure is
T (conv)(X ⊗X′ ⊗Y ) = EH

EH,O(X ⊗Y ) ⊗X′
,
(27)
where emission acts first on the current hidden state X and observable Y , followed by the transi-
tion that propagates the result together with the subsequent hidden state X′. The causal causal
structure is
T (caus)(X ⊗X′ ⊗Y ) = EH,O

EH(X ⊗X′) ⊗Y

.
(28)
where the hidden transition acts first on the current hidden state X and the subsequent hidden
state X′, followed by emission coupling the evolved state with the observable Y . Both reduce
to the same classical hidden Markov model when all algebras commute, but they yield distinct
quantum correlation structures.
This C∗-dynamical framework provides the rigorous foundation for analyzing symmetry-protected
topological order in HQMMs. The quasi-local algebra AN0, equipped with the shift endomorphism
σ+ and the embedding structure j(n), supports the definition of the generative triple (ϕ0, EH, EH,O)
and the two causal structures T (conv) and T (caus) as particular instances.
Declarations
Conflict of Interest
The authors declare no conflict of interest.
Data Availability
No data were generated or analyzed during this study.
CRediT authorship contribution statement
Abdessatar Souissi: Conceptualization, Investigation, Resources, Methodology, Writing – original
draft, Writing – review & editing.
Abdessatar Barhoumi: Visualization, Project administration, Methodology, Resources, Project
administration.
Data availability
No data was used for the research described in the article.
Funding
The authors received no funding for this work.
References
[1] Haldane, F. D. M.: Nonlinear field theory of large-spin Heisenberg antiferromagnets: semi-
classically quantized solitons of the one-dimensional easy-axis N´eel state. Physical Review
Letters 50(15), 1153 (1983).
[2] Pollmann, F., Turner, A. M., Berg, E., Oshikawa, M.: Entanglement spectrum of a topolog-
ical phase in one dimension. Physical Review B 81, 064439 (2010).
[3] Pollmann, F., Berg, E., Turner, A. M., Oshikawa, M.: Symmetry protection of topological
order in one-dimensional quantum spin systems. Physical Review B 85, 075125 (2012).
[4] Affleck, I., Kennedy, T., Lieb, E. H., Tasaki, H.: Rigorous results on valence-bond ground
states in antiferromagnets. Physical Review Letters 59(7), 799 (1987).
[5] Affleck, I., Kennedy, T., Lieb, E. H., Tasaki, H.: Valence bond ground states in isotropic quan-
tum antiferromagnets. Communications in Mathematical Physics 115(3), 477–528 (1988).
[6] Ogata, Y.: A Z2-index of symmetry protected topological phases with time reversal symmetry
for quantum spin chains. Communications in Mathematical Physics 374(2), 705–734 (2020).
[7] Ogata, Y.: Classification of gapped ground state phases in quantum spin systems. In: In-
ternational Congress of Mathematicians, pp. 4142–4161. European Mathematical Society,
Helsinki (2023).
[8] Tasaki, H.: Rigorous index theory for one-dimensional interacting topological insulators.
Journal of Mathematical Physics 64, 041903 (2023).
[9] Chen, X., Gu, Z.-C., Wen, X.-G.:
Classification of gapped symmetric phases in one-
dimensional spin systems. Physical Review B 83, 035107 (2011).
[10] Chen, X., Gu, Z.-C., Wen, X.-G.: Complete classification of one-dimensional gapped quantum
phases in interacting spin systems. Physical Review B 84, 235128 (2011).
[11] Stephen, D. T., Wang, D.-S., Prakash, A., Wei, T.-C., Raussendorf, R.: Computational power
of symmetry-protected topological phases. Physical Review Letters 119, 010504 (2017).
[12] de Groot, C., Turzillo, A., Schuch, N.: Symmetry protected topological order in open quan-
tum systems. Quantum 6, 856 (2022).
[13] de Groot, C., Stephen, D. T., Molnar, A., Schuch, N.: Inaccessible entanglement in symmetry
protected topological phases. Journal of Physics A: Mathematical and Theoretical 53(33),
335302 (2020).
[14] Sati, H., Schreiber, U.: Identifying anyonic topological order in fractional quantum anomalous
Hall systems. Applied Physics Letters 128(2) (2026).
[15] Accardi, L., Soueidi, E. G., Lu, Y. G., Souissi, A.: Hidden quantum Markov processes. Infinite
Dimensional Analysis, Quantum Probability and Related Topics 28(04), 2450007 (2025).
[16] Accardi, L., Soueidi, E. G., Lu, Y. G., Souissi, A.: Algebraic hidden processes and hidden
Markov processes. Infinite Dimensional Analysis, Quantum Probability and Related Topics
29(01), 2450009 (2026).
[17] Parthasarathy, K. R.: An Introduction to Quantum Stochastic Calculus. Springer, Berlin
(2012).
[18] Choi, M.-D.: Completely positive linear maps on complex matrices. Linear Algebra and Its
Applications 10(3), 285–290 (1975).
[19] Bratteli, O., Robinson, D. W.: Operator Algebras and Quantum Statistical Mechanics, Vols.
1 and 2, 2nd edn. Springer, Berlin (1987).
[20] Taranto, P., Elliott, T. J., Milz, S.: Hidden quantum memory: Is memory there when
somebody looks? Quantum 7, 991 (2023).
[21] Li, X.-Y., et al.: A new quantum machine learning algorithm: split hidden quantum Markov
model inspired by quantum conditional master equation. Quantum 8, 1232 (2024).
[22] Voigt, F. R.: Adapted unitary cocycles and quantum Markov processes: a cohomological
approach. Doctoral dissertation (2025).
[23] Fannes, M., Nachtergaele, B., Werner, R. F.: Finitely correlated states of quantum spin
chains. Communications in Mathematical Physics 144, 443–490 (1992).
[24] Fannes, M., Nachtergaele, B., Werner, R. F.: Ground states of VBS models on Cayley trees.
Journal of Statistical Physics 66, 939–973 (1992).
[25] Souissi, A., Andolsi, A.: A hidden quantum Markov model framework for entanglement
and topological order in the AKLT chain. The European Physical Journal Plus 141(4), 404
(2026).
[26] Ragone, M.: SO(n) AKLT chains as symmetry protected topological quantum ground states.
Ph.D. thesis, University of California, Davis (2024).
[27] Xiong, C. Z.: Minimalist approach to the classification of symmetry protected topological
phases. Journal of Physics A: Mathematical and Theoretical 51(44), 445001 (2018).
[28] Szab´o, G.: On a categorical framework for classifying C∗-dynamics up to cocycle conjugacy.
Journal of Functional Analysis 280, 108927 (2019).
[29] Souissi, A., Barhoumi, A.:
Causal architecture in hidden quantum Markov models.
arXiv:2602.19120 (2026).
[30] Smith, A., Kim, M. S., Pollmann, F., Knolle, J.: Simulating quantum many-body dynamics
on a current digital quantum computer. npj Quantum Information 5, 106 (2019).
[31] Kallel, S., Sati, H., Schreiber, U.: Higher-Dimensional Anyons via Higher Cohomotopy.
arXiv:2601.03150 (2026).
[32] Kitaev, A.: Anyons in an exactly solved model and beyond. Annals of Physics 321(1), 2–111
(2006).
