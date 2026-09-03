---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-003-the-aklt-state-and-its-spt-order
section_title: "The AKLT State and its SPT Order"
section_number: null
pages: 4-6
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
The seminal work of Affleck, Kennedy, Lieb, and Tasaki [27] marked a watershed moment in
quantum magnetism by furnishing an exactly solvable model that provided rigorous foundation
for Haldane’s conjecture regarding the existence of a spectral gap in antiferromagnetic spin-1
chains. The AKLT Hamiltonian, defined on a one-dimensional lattice with spin-1 degrees of
freedom, embodies profound physical insights through its elegantly simple form:
ˆHAKLT =
∑
⟨i,j⟩
[
⃗Si·⃗Sj + 1
3(⃗Si·⃗Sj)2
]
,
where ⃗Si = (Sx
i,Sy
i,Sz
i ) are spin-1 operators satisfyingsu(2) commutation relations
[Sx,Sy] =iS z,[S y,Sz] =iS x,[S z,Sx] =iS y
The AKLT state is defined on a spin-1 chain, where the physical Hilbert space at each site
isH 1∼= C3, spanned by theS z-eigenbasis{|+⟩,|0⟩,|−⟩}. Its construction relies on an auxiliary,
virtual spin-½spaceH 1
2
∼= C2 with the orthonormal basis{| ↑⟩,| ↓⟩}, which is projectively
embedded into the physical spin-1 space.
The AKLT state admits a canonical MPS representation that exactly captures its entanglement
structure. The fundamental objects are three local matrices{A +,A 0,A−}∈M 2(C) that mediate
between the physical spin-1 space and the auxiliary spin-½space:
A+ =
√
2
3σ+, A 0 =
√
1
3σz, A − =−
√
2
3σ− (3)
Here, the operatorsσ +,σ −, andσ z act on the virtual spaceC 2, which is spanned by the
basis vectors|↑⟩=
(
1
0
)
and|↓⟩=
(
0
1
)
. Their explicit action is defined by the following outer
products:
σ+ =
(
0 1
0 0
)
, σ − =
(
0 0
1 0
)
, σ z =
(
1 0
0−1
)
For ann-site periodic chain, the AKLT state is constructed as the uniform MPS:
|ψ(n)
AKLT⟩=
∑
k1,...,kn∈{+,0,−}
Tr (Ak1Ak2···A kn)|k 1k2···k n⟩(4)
Figure 1 illustrates how pairs of spin-½particles can be combined to form an effective spin-1
degree of freedom. At the lower level, the red circles grouped in ellipses represent the tensor
product spaceH 1
2
⊗H 1
2
, which naturally decomposes into a three-dimensional triplet sector and a
4
|ψ−⟩ |ψ−⟩ |ψ−⟩ |ψ−⟩
: qubit (spin 1/2){|↑⟩,|↓⟩}
: singlet|ψ −⟩= 1√
2(|↑↓⟩−|↓↑⟩)
: projection|+⟩⟨↑↑|+|0⟩ 1√
2(⟨↑↓|+⟨↓↑|) +|−⟩⟨↓↓|
: triplet (spin 1)
Figure 1: Schematic diagram with eight qubits on the top row, grouped pairwise into singlet
states (dashed ellipses), and projected downward into three spin-1 triplet nodes on the lower row.
The increased vertical spacing highlights the correspondence between the two levels.
one-dimensional singlet sector. The upper blue circles correspond to the symmetric triplet space,
which carries the spin-1 representation.
The projectionP:H 1
2
⊗H 1
2
→H 1 implements the Clebsch-Gordan decomposition 1
2⊗ 1
2 = 1⊕0:
P=|+⟩⟨↑↑|+|−⟩⟨↓↓|+|0⟩ 1√
2 (⟨↑↓|+⟨↓↑|).(5)
This projection satisfiesP †P= Π sym andPP † =1IH1, establishing an isometric embedding that
encodes the Haldane phase through its entanglement structure. Quantum channels channels
are fundamental objects in the analysis of the AKLT model. The AKLT channel is defined on
B(H 1
2
)≡M 2(C) as:
ΦAKLT(Z) =
∑
k∈{+,0,−}
AkZA†
k.(6)
The quantum channel Φ AKLT is bi-stochastic: it is both trace-preserving Tr(Φ AKLT(Z)) =
Tr(Z) and identity-preserving Φ AKLT(1IH1/2) =1I H1/2. When interpreted as a transfer matrix
within the valence-bond-solid formalism, its spectral structure dictates the system’s correlation
functions: the largest eigenvalue is unity, while the second largest eigenvalue in magnitude,λ 2,
sets the dominant correlation length viaξ−1 =−ln|λ 2|[30]. The contractive nature of the channel
upon iteration, a direct consequence of this spectral gap, underpins the mixing behavior and the
exponential decay of correlations characteristic of the gapped phase of the AKLT state [52].
LetGbe a subgroup of the special orthogonal group in three dimensionsG= SO(3), which
constitutes our symmetry group. This group acts on the physical and virtual spaces of our sys-
tem via distinct unitary representations. The physical Hilbert space isH 1, on whichGacts via
the fundamental, integer-spin representationρ:G→U(H 1
2
), which is isomorphic to the spin-1
representation. The virtual, or auxiliary, Hilbert space isH 1
2
, whereGacts via the projective
spin-½representationπ:G→U(H 1
2
). This representationπis projective, meaning it satisfies
the composition ruleπ(g 1)π(g2) =ω(g 1,g 2)π(g1g2) for allg 1,g 2∈G, with a non-trivial cocycle
5
ω:G×G→U(1). The cohomology class [ω] is a non-trivial element of the second group cohomol-
ogyH 2(SO(3),U(1)), which is isomorphic toZ 2, thereby encoding the double-cover relationship
between SO(3) and SU(2) [31].
A crucial property of the AKLT state, which guarantees its non-trivial SPT phase [26], is the
exact intertwining relation between the virtual representationπand the physical representationρ.
This relation is mathematically expressed as follows: For everyg∈Gand for everyk∈{+,0,−},
The MPS tensors{A k′}satisfy the following covariance relation:
∑
k′
ρ(g)kk′Ak′ =π(g)A kπ(g)† (7)
whereρ(g) kk′ =⟨k|ρ(g)|k ′⟩denotes the matrix element of the operatorρ(g). This equation means
that a symmetry transformationgapplied to the physical index of the tensor is equivalent to a
conjugation of the virtual operators by the projective representationπ(g) [29].
The symmetry action extends naturally to the dihedral groupD 2∼= Z2×Z 2, a finite subgroup
of SO(3) consisting ofπ-rotations about three orthogonal axes. This subgroup is a key symmetry
of the AKLT Hamiltonian. The non-triviality of the SPT phase under thisD 2 symmetry is
detected by the Ogata index [35], aZ 2-valued topological invariant. For a translation-invariant
MPS that is invariant under the dihedral groupD 2 ={e,g x,gy,gz}(the group ofπ-rotations
about orthogonal axes), the SPT phase is classified by aZ 2 index. This index is determined by
the projective commutation relation of the symmetry actions on the virtual space.
LetU g be the unitary operators implementing the symmetryg∈D 2 on the physical spin-1
space. For the generatorsg x andg y, the projective algebra is:
U 2
x =η xI, U 2
y =η yI, U xUy =η xyUyUx,
withη x,ηy,ηxy∈{±1}. TheZ 2 index characterizing the SPT phase is given byθ=η xy.
For the AKLT state, with virtual space dimensiond= 2, one findsη x =η y = +1 butη xy =−1,
yielding the non-trivial indexθ=−1. This value is a topological invariant, which can be computed
via the gauge-invariant formula:
θ= 1
dTr(UxUyU†
xU†
y).
Substitutingd= 2 andU xUyU†
xU†
y =−Ifor the AKLT state confirmsθ=−1 [29, 30].
