---
doc_id: arxiv-2605.09605v2
doc_title: "Cocycle Actions on Hidden Quantum Markov Models:"
section_id: sec-003-appedix-hidden-quantum-markov-models
section_title: "Appedix: Hidden Quantum Markov Models"
section_number: null
pages: 12-17
source_pdf: 2605.09605v2.pdf
source_sha256: 24496fb444a2b558
doc_brief: "Cocycle Actions on Hidden Quantum Markov Models: — We develop a symmetry action framework for hidden quantum Markov models (HQMMs) tailored to one-dimensional quantum spin systems and"
---
LetHandKbe separable Hilbert spaces, representing the hidden and observable degrees of
freedom at a single lattice site, respectively. The corresponding single-site algebras are defined as
theC ∗-algebras of bounded linear operators:A H :=B(H) andA O :=B(K), each equipped with
the operator norm and containing the identity operator. For each siten∈Z, the full single-site
algebra is the spatialC ∗-tensor product
A{n} :=A H⊗AO∼=B(H⊗K),
where the isomorphism holds by separability ofHandK.
For a finite subset Λ⊂Z, the finite-volume composite algebra is theC ∗-tensor product over
the sites:
AΛ :=
⨂
n∈Λ
A{n} =
⨂
n∈Λ
(
AH⊗AO
)
n
,
where (AH⊗A O)n denotes an isomorphic copy of the single-site algebra localized at positionn.
The finite-volume hidden and observable subalgebras are given respectively by
AH,Λ :=
⨂
n∈Λ
(AH)n,A O,Λ :=
⨂
n∈Λ
(AO)n,
which satisfy the factorizationA Λ =A H,Λ⊗AO,Λ.
For eachn∈Z, define the hidden embeddingj (n)
H :A H ↪→AH,Z by
j(n)
H (X) :=
⨂
k∈Z
X(H)
k , X (H)
k =



Xifk=n,
IAH otherwise,
12
extended continuously to the completion. This map is an isometric∗-homomorphism. The ob-
servable embeddingj (n)
O :A O ↪→AO,Z is defined analogously as
j(n)
O (Y) :=
⨂
k∈Z
Y (O)
k , Y (O)
k =



Yifk=n,
IAO otherwise.
The composite embedding at sitenisj (n) :=j (n)
H ⊗j (n)
O , satisfyingj (n)(X⊗Y) =j (n)
H (X)·j (n)
O (Y).
For any finite Λ⊂Z, the embeddingj Λ :⨂
n∈Λ(AH⊗AO)↪→AZ is defined on elementary tensors
by
jΛ
(⨂
n∈Λ
(Xn⊗Yn)
)
=
∏
n∈Λ
j(n)(Xn⊗Yn),
with the product taken in increasing order of indices. These embeddings are consistent: for
Λ⊂Λ ′, we havej Λ′◦ι Λ,Λ′ =j Λ, whereι Λ,Λ′ is the inclusion map tensoring with identities on the
additional sites.
The collection{A Λ,ι Λ,Λ′}forms a directed system under inclusion. The local algebra is the
algebraic direct limitA loc
Z :=⋃
Λ⊂ZfiniteAΛ, and the quasi-localC ∗-algebra is its norm completion
AZ :=Aloc
Z
∥·∥
. When dim(H⊗K)<∞,A Z is a uniformly hyperfinite (UHF)C ∗-algebra. The
hidden and observable quasi-local algebrasA H,Z andA O,Z are constructed analogously, satisfying
the spatial tensor product relationA Z∼=AH,Z⊗AO,Z.
The shift automorphismσ∈Aut(A Z) is defined on elementary tensors byσ
(⨂
n∈ZAn
)
=
⨂
n∈ZAn+1, extended continuously. It satisfiesσ◦j (n) =j (n+1) for alln∈Z, and{σ n}n∈Z
forms aZ-action onA Z. There exists a strongly continuous one-parameter automorphism group
τ:R→Aut(A Z) withτ 1 =σ, constructed via the crossed productA Z ⋊σ Z, with LiouvillianH
satisfyingτ t = exp(itH)(·) exp(−itH). The triple (A Z,R,τ) is aC ∗-dynamical system.
Restricting to the half-infinite chain indexed byN 0 ={0,1,2,...}, the one-sided quasi-local
algebra is
AN0 :=
⋃
m∈N0
m⨂
n=0
(AH⊗AO)n
∥·∥
,
with the embeddingsj (n)
H ,j (n)
O ,j (n) restricted ton≥0. The shift restricts to a non-unital
endomorphismσ + :A N0 → AN0 given byσ +(A) =I {0}⊗Aunder the identificationA N0
∼=
A{0}⊗A N0.
For eachn∈N 0, define the finite-volume algebraA [0,n] :=⨂n
k=0(AH⊗AO)k, a finiteC∗-tensor
product. Form≤n, the natural embeddingι m,n :A [0,m] ↪→A[0,n] appendsn−midentity factors.
The family{A [0,n],ιm,n}m≤n forms an inductive system, andA N0 is the norm completion of its
inductive limit [19, 17].
Let{φ n}n∈N0 be a sequence where eachφ n is a state onA [0,n]. The sequence is said to satisfy
theKolmogorov compatibility conditionif for allm≤n,
φn◦ιm,n =φ m.
This condition guarantees consistency of expectation values across different volumes.
Lemma A.1(Projective Limit State).If{φ n}n∈N0 satisfies the Kolmogorov compatibility condi-
tion, then there exists a unique stateφonA N0 such thatφ| A[0,n] =φ n for alln. Moreover, for
anyA∈A N0,φ(A) = lim n→∞φn(An)wheneverA n∈A [0,n] converges toAin norm.
Proof.For any local observableAbelonging to someA [0,n], setφ(A) =φ n(A). Compatibility
makes this well-defined. This gives a linear functional on the dense subalgebra of local observables,
which is positive and satisfiesφ(I) = 1. Hence it extends uniquely to a state on the whole algebra
AN0 by continuity. The approximation property follows directly from the construction.
13
The HQMM structure is encoded in a completely positive unital (CPU) map
T:A H⊗AH⊗AO→A H,
which governs the joint evolution of hidden and observable degrees of freedom across adjacent
sites. For anyX∈A H andY∈A O, define the sliced mapsT X,Y :A H→A H by
TX,Y (Z) :=T(X⊗Z⊗Y).
Given an initial stateϕ 0 onA H, we construct finite-volume states as follows. For eachn∈N 0,
defineφ n onA [0,n] on elementary tensors by
φn
( n⨂
k=0
(Xk⊗Yk)
)
:=ϕ 0◦TX0,Y0◦TX1,Y1◦···◦T Xn,Yn(IAH),
where the composition denotes successive application of the maps, andϕ 0 is evaluated on the
resulting element ofA H.
Theorem A.2(Global HQMM State).LetT:A H⊗A H⊗A O→A H be a CPU map andϕ 0
a state onA H. For eachn∈N 0, the functionalφ n defined above extends uniquely to a state
onA [0,n]. The sequence{φ n}n∈N0 satisfies the Kolmogorov compatibility condition, and thus there
exists a unique stateφonA N0 such thatφ| A[0,n] =φ n for alln. Thisφis called the global HQMM
state generated by(ϕ 0,T).
Proof.Unitality and complete positivity ofTimply that eachT X,Y is a CP map for fixed positive
elementsXandY, and ifX=I AH andY=I AO the mapZ↦→TIAH,IAH
(Z) =T(I AH⊗Z⊗
IAO) is CPU . Hence for a given sequence of positive elementsX i,Yi,i= 0,1,···,n, the map
ϕ0◦T X0,Y0◦···◦T Xn,Yn(·) is a positive linear functional onA H. Moreover,φ n(I) = 1. By the
universal property of theC ∗-tensor product,φ n extends to a state onA [0,n]. For compatibility,
considerA∈A [0,n] and its embeddingι n,n+1(A) =A⊗(I AH⊗IAO). Then
φn+1(ιn,n+1(A)) =ϕ 0◦TX0,Y0◦···◦T Xn,Yn◦T IAH,IAO
(IAH).
Unitality ofTgivesT IAH,IAO
=IAH, so the right-hand side equalsϕ 0◦TX0,Y0◦···◦T Xn,Yn(IAH) =
φn(A). By linearity and continuity,φ n+1◦ιn,n+1 =φ n, and similarly for allm≤n. The existence
and uniqueness ofφfollow from Lemma 1.
The hidden marginal stateφ H onA H,N0 is defined by restriction: forA∈A H,N0,φ H(A) :=
φ(A⊗I AO,N0
). For a local observable ⨂n
k=0Xk, this becomes
φH
( n⨂
k=0
Xk
)
=ϕ 0◦TX0,IAO
◦···◦T Xn,IAO
(IAH),
defining a quantum Markov chain onA H,N0. The observation marginalφ O onA O,N0 is defined
analogously: forB∈A O,N0,φ O(B) :=φ(IAH,N0
⊗B). For a local observable ⨂n
k=0Yk,
φO
( n⨂
k=0
Yk
)
=ϕ 0◦T IAH,Y0◦···◦T IAH,Yn(IAH),
which represents the statistics of the observed process. The global stateφserves as a coupling of
these two marginals.
Two distinct causal structures arise as special realizations ofT, corresponding to different
orderings of hidden transition and observable emission. LetE H :A H⊗AH→A H be a CPU map
describing the hidden transition, andE H,O :A H⊗AO→A H a CPU map describing the emission.
Theconventionalcausal structure is
14
T (conv)(X⊗X ′⊗Y) =E H
(
EH,O(X⊗Y)⊗X ′
)
,(27)
where emission acts first on the current hidden stateXand observableY, followed by the transi-
tion that propagates the result together with the subsequent hidden stateX ′. Thecausalcausal
structure is
T (caus)(X⊗X ′⊗Y) =E H,O
(
EH(X⊗X ′)⊗Y
)
.(28)
where the hidden transition acts first on the current hidden stateXand the subsequent hidden
stateX ′, followed by emission coupling the evolved state with the observableY. Both reduce
to the same classical hidden Markov model when all algebras commute, but they yield distinct
quantum correlation structures.
ThisC∗-dynamical framework provides the rigorous foundation for analyzing symmetry-protected
topological order in HQMMs. The quasi-local algebraA N0, equipped with the shift endomorphism
σ+ and the embedding structurej (n), supports the definition of the generative triple (ϕ0,EH,EH,O)
and the two causal structuresT (conv) andT (caus) as particular instances.
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
classically quantized solitons of the one-dimensional easy-axis N´ eel state.Physical Review
Letters50(15), 1153 (1983).
[2] Pollmann, F., Turner, A. M., Berg, E., Oshikawa, M.: Entanglement spectrum of a topolog-
ical phase in one dimension.Physical Review B81, 064439 (2010).
[3] Pollmann, F., Berg, E., Turner, A. M., Oshikawa, M.: Symmetry protection of topological
order in one-dimensional quantum spin systems.Physical Review B85, 075125 (2012).
15
[4] Affleck, I., Kennedy, T., Lieb, E. H., Tasaki, H.: Rigorous results on valence-bond ground
states in antiferromagnets.Physical Review Letters59(7), 799 (1987).
[5] Affleck, I., Kennedy, T., Lieb, E. H., Tasaki, H.: Valence bond ground states in isotropic quan-
tum antiferromagnets.Communications in Mathematical Physics115(3), 477–528 (1988).
[6] Ogata, Y.: AZ 2-index of symmetry protected topological phases with time reversal symmetry
for quantum spin chains.Communications in Mathematical Physics374(2), 705–734 (2020).
[7] Ogata, Y.: Classification of gapped ground state phases in quantum spin systems. In:In-
ternational Congress of Mathematicians, pp. 4142–4161. European Mathematical Society,
Helsinki (2023).
[8] Tasaki, H.: Rigorous index theory for one-dimensional interacting topological insulators.
Journal of Mathematical Physics64, 041903 (2023).
[9] Chen, X., Gu, Z.-C., Wen, X.-G.: Classification of gapped symmetric phases in one-
dimensional spin systems.Physical Review B83, 035107 (2011).
[10] Chen, X., Gu, Z.-C., Wen, X.-G.: Complete classification of one-dimensional gapped quantum
phases in interacting spin systems.Physical Review B84, 235128 (2011).
[11] Stephen, D. T., Wang, D.-S., Prakash, A., Wei, T.-C., Raussendorf, R.: Computational power
of symmetry-protected topological phases.Physical Review Letters119, 010504 (2017).
[12] de Groot, C., Turzillo, A., Schuch, N.: Symmetry protected topological order in open quan-
tum systems.Quantum6, 856 (2022).
[13] de Groot, C., Stephen, D. T., Molnar, A., Schuch, N.: Inaccessible entanglement in symmetry
protected topological phases.Journal of Physics A: Mathematical and Theoretical53(33),
335302 (2020).
[14] Sati, H., Schreiber, U.: Identifying anyonic topological order in fractional quantum anomalous
Hall systems.Applied Physics Letters128(2) (2026).
[15] Accardi, L., Soueidi, E. G., Lu, Y. G., Souissi, A.: Hidden quantum Markov processes.Infinite
Dimensional Analysis, Quantum Probability and Related Topics28(04), 2450007 (2025).
[16] Accardi, L., Soueidi, E. G., Lu, Y. G., Souissi, A.: Algebraic hidden processes and hidden
Markov processes.Infinite Dimensional Analysis, Quantum Probability and Related Topics
29(01), 2450009 (2026).
[17] Parthasarathy, K. R.:An Introduction to Quantum Stochastic Calculus. Springer, Berlin
(2012).
[18] Choi, M.-D.: Completely positive linear maps on complex matrices.Linear Algebra and Its
Applications10(3), 285–290 (1975).
[19] Bratteli, O., Robinson, D. W.:Operator Algebras and Quantum Statistical Mechanics, Vols.
1 and 2, 2nd edn. Springer, Berlin (1987).
[20] Taranto, P., Elliott, T. J., Milz, S.: Hidden quantum memory: Is memory there when
somebody looks?Quantum7, 991 (2023).
[21] Li, X.-Y., et al.: A new quantum machine learning algorithm: split hidden quantum Markov
model inspired by quantum conditional master equation.Quantum8, 1232 (2024).
[22] Voigt, F. R.: Adapted unitary cocycles and quantum Markov processes: a cohomological
approach. Doctoral dissertation (2025).
16
[23] Fannes, M., Nachtergaele, B., Werner, R. F.: Finitely correlated states of quantum spin
chains.Communications in Mathematical Physics144, 443–490 (1992).
[24] Fannes, M., Nachtergaele, B., Werner, R. F.: Ground states of VBS models on Cayley trees.
Journal of Statistical Physics66, 939–973 (1992).
[25] Souissi, A., Andolsi, A.: A hidden quantum Markov model framework for entanglement
and topological order in the AKLT chain.The European Physical Journal Plus141(4), 404
(2026).
[26] Ragone, M.: SO(n) AKLT chains as symmetry protected topological quantum ground states.
Ph.D. thesis, University of California, Davis (2024).
[27] Xiong, C. Z.: Minimalist approach to the classification of symmetry protected topological
phases.Journal of Physics A: Mathematical and Theoretical51(44), 445001 (2018).
[28] Szab´ o, G.: On a categorical framework for classifying C∗-dynamics up to cocycle conjugacy.
Journal of Functional Analysis280, 108927 (2019).
[29] Souissi, A., Barhoumi, A.: Causal architecture in hidden quantum Markov models.
arXiv:2602.19120 (2026).
[30] Smith, A., Kim, M. S., Pollmann, F., Knolle, J.: Simulating quantum many-body dynamics
on a current digital quantum computer.npj Quantum Information5, 106 (2019).
[31] Kallel, S., Sati, H., Schreiber, U.: Higher-Dimensional Anyons via Higher Cohomotopy.
arXiv:2601.03150 (2026).
[32] Kitaev, A.: Anyons in an exactly solved model and beyond.Annals of Physics321(1), 2–111
(2006).
17
