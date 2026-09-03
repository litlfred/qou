---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-004-hqmm-structure-of-the-aklt-state
section_title: "HQMM Structure of the AKLT State"
section_number: null
pages: 6-12
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
The AKLT state’s unique structure can be naturally formulated as a HQMM, revealing a profound
connection between topological quantum matter and quantum stochastic processes. This frame-
work cleanly separates the system into hidden virtual degrees of freedom that encode topological
information and observable physical degrees accessible to measurement.
TheHidden Quantum Markov Modelfor the AKLT chain is specified by the generative triplet
ΞAKLT = (ϕ0,EH,EO,H) where:
•ϕ 0 :B(H 1
2
)→Cinitializes the hidden system
•E H :B(H 1
2
)⊗B(H 1
2
)→B(H 1
2
) governs the hidden dynamics of the spin-½system.
•E O,H :B(H 1
2
)⊗B(H 1)→B(H 1
2
) emission transition expectation that encodes the spin-1
system through the spin-½hidden system.
The sequential structure follows quantum causality through the transition map
EXℓ,Yℓ(·) =E H(EO,H(Xℓ⊗Yℓ)⊗·) (8)
6
generating the complete state
φO,H(X⊗Y) =ϕ 0◦EX0,Y0◦EX1,Y1◦···◦E Xn,Yn(1IH 1
2
),(9)
whereX=X 1⊗···X n∈B(H 1
2
)⊗n andY=Y 1⊗···Y n∈B(H 1)⊗n.
This HQMM formulation provides a powerful framework for understanding how the AKLT
state’s topological properties emerge from the hidden quantum Markovian dynamics, which we
will now analyze through the lens of symmetry protection.
HQMM for AKLT Spin Chain
spin-½(hidden)
spin-1 (observation)
B(H 1
2
) B(H 1
2
) B(H 1
2
)
···
B(H 1
2
)
B(H1) B(H1) B(H1)
···
EX0,Y0 EX1,Y1 EXn,Yn
Y0 Y1 Yn
X0 X1 Xn IH 1
2
ϕ0
t= 0 t= 1 t=n t=n+ 1
Hidden correlations in the AKL T chain:The HQMM represents sequential tran-
sitions between virtual spin-½degrees of freedom (hidden system) and physical spin-1
measurements (observation system) via transition mapsE Xi,Yi that generate the com-
plete quantum state correlations while preserving the valence bond solid structure.
This HQMM formulation provides powerful quantum information tools to analyze entangle-
ment scaling, quantum memory effects, and topological stability under decoherence, establishing
fundamental connections between quantum many-body physics and quantum computational mod-
els.
In the subsequent analysis, we will explicitly derive the transition expectations governing
the system’s dynamics and elucidate the intricate correlation structure of the underlying hidden
Markov model. This will be achieved by examining how the hidden algebraB(H 1
2
)⊗N, which
encodes the virtual spin network responsible for topological entanglement, correlates with the
observation algebraB(H 1)⊗N, representing the physically measurable degrees of freedom, via the
CPIP mapsE H andE O,H implemented through precise virtual isometryVthat captures the
hidden entanglement structure of the model and an observation isometryW, that preserves the
SPT order.
The mappingV:H 1
2
→H 1
2
⊗H 1
2
is a partial isometry that builds entanglement between
virtual spin spaces. A specific choice ofVis given by:
V=|Ψ −⟩⟨↑|+|Ψ +⟩⟨↓|,(10)
where|Ψ −⟩= 1√
2(|↑↓⟩−|↓↑⟩) is the singlet state forming the original AKLT valence bonds,
and|Ψ +⟩= 1√
2(|↑↓⟩+|↓↑⟩) is the symmetric triplet component. While this specificVis a
canonical choice, various other isometries can be selected to encode the system’s entanglement
and symmetry, each leading to a different physical state that can still saturate the maximal
entanglement of the underlying virtual system.
Complementarily, theobservation isometryW:H 1
2
→H 1
2
⊗H1 maps virtual states to physical
spin-1 observables:
Wξ=
∑
k∈{+,0,−}
Akξ⊗|k⟩,∀ξ∈H 1
2
(11)
7
where the matricesA k are the standard AKLT MPS tensors. This structure explicitly reveals the
AKLT state as a quantum autoregressive process, where sequential application ofWgenerates
the physical spin-1 chain from the virtual space evolution.
Lemma 3.1.The mapE H :B(H 1
2
)⊗B(H 1
2
)→B(H 1
2
)defined by the Stinespring dilation
EH(X⊗X ′) =V †(X⊗X ′)V(12)
whereV:H 1
2
→ H1
2
⊗H 1
2
is the partial isometry from (10), constitutes a hidden transition
expectation CPIP. The dual quantum channelE ∗
H :B(H 1
2
)→B(H 1
2
)⊗B(H 1
2
), defined via the
Hilbert-Schmidt adjoint, acts as:
E∗
H(ρ) =VρV †.(13)
This implements virtual bond preparation in the AKLT entanglement structure.
Proof.We first verify thatVis a partial isometry. From the definition (10), we computeV †V:
V†V|↑⟩=V †
(
1√
2(|↑↓⟩−|↓↑⟩)
)
= 1
2(|↑⟩+|↓⟩)− 1
2(−|↑⟩+|↓⟩) =|↑⟩,
V†V|↓⟩=V †
(
1√
2(|↑↓⟩+|↓↑⟩)
)
= 1
2(|↑⟩+|↓⟩) + 1
2(−|↑⟩+|↓⟩) =|↓⟩.
HenceV †V=1I, provingVis an isometry (and therefore a partial isometry).
Complete positivity ofE H follows from the Stinespring dilation: for anyn∈NandP≥0 in
B(Cn⊗H 1
2
⊗H 1
2
),
(1In⊗EH)(P) = (1In⊗V) †P(1In⊗V)≥0.
Unitality is immediate:
EH(1IH 1
2
⊗1IH 1
2
) =V †(1IH 1
2
⊗1IH 1
2
)V=V †V=1I H 1
2
.
For the dual channel, take anyX,X ′,ρ∈B(H 1
2
):
⟨EH(X⊗X ′),ρ⟩ HS = Tr[(V†(X⊗X ′)V)†ρ]
= Tr[V†(X′†⊗X†)Vρ]
= Tr[(X′†⊗X†)VρV †]
=⟨X⊗X ′,VρV †⟩HS.
where we used the cyclic property of the trace. This provesE ∗
H(ρ) =VρV †.
Forρ=p|↑⟩⟨↑|+ (1−p)|↓⟩⟨↓|, we compute:
E∗
H(ρ) =p·V|↑⟩⟨↑|V † + (1−p)·V|↓⟩⟨↓|V †
= p
2(|↑↓⟩−|↓↑⟩)(⟨↑↓|−⟨↓↑|)
+ 1−p
2 (|↑↓⟩+|↓↑⟩)(⟨↑↓|+⟨↓↑|)
= 1
2|↑↓⟩⟨↑↓|+ 1
2|↓↑⟩⟨↓↑|
+ 1−2p
2 (|↑↓⟩⟨↓↑|+|↓↑⟩⟨↑↓|)
This expression is verified by checking the extreme cases: whenp= 1 (pure|↑⟩), we recover the
singlet state projector (up to normalization), and whenp= 0 (pure|↓⟩), we obtain the triplet
state projector.
8
Remark 3.2.The hidden transition expectationE H and its dualE ∗
H link the dynamics of the
AKLT chain at consecutive times. The dual channelE ∗
H acts on density matrices, extending a
stateρ (n) at timento an entangled bipartite stateE ∗
H(ρ(n)) =Vρ (n)V† at times(n−1,n).
Conversely,E H acts on operators. Its action on a generic operatorXis given by the conditional
expectation:
EH(X) =V †XV.
This projects the joint operatorXon the bipartite system(n−1,n)down to an operator on the
marginal system at timen, enforcing the Markovian structure viaρ (n) =E H(ρ(n−1,n)).
This structure reveals the AKLT chain’s quantum memory: the isometryVcreates the virtual
singlets that propagate correlations, with the virtual bond space correlating successive temporal
slices.
This dual pair of operations (E H,E ∗
H) constitutes a consistent family of conditional expec-
tations and state preparations that implement the quantum Markov property. The composition
EH◦E∗
H =1IH 1
2
ensures that extending then marginalizing returns the original state, whileE ∗
H◦EH
projects onto the range ofV, which encodes the specific entanglement structure of the AKLT virtual
bonds. This mathematical structure provides a precise formulation of how the HQMM captures
the temporal correlations and entanglement propagation in symmetry-protected topological phases.
Lemma 3.3.LetW:H 1
2
→ H1
2
⊗H 1 be the partial isometry from (11). The mapE O,H :
B(H 1
2
)⊗B(H 1)→B(H 1
2
)defined by
EO,H(X⊗Y) =W †X⊗YW=
∑
k,k′
⟨k′|Y|k⟩A kXA†
k′ (14)
is an emission transition expectation. Its dual channelE ∗
O,H :B(H 1
2
)→B(H 1
2
)⊗B(H 1)acts as:
E∗
O,H(Z) =
∑
k,k′
A†
kZAk′⊗|k⟩⟨k′|.(15)
Proof.The proof proceeds by systematically establishing each property of the emission transition
expectation and its dual channel. We begin by verifying thatWis indeed a partial isometry.
ComputingW †Wusing the explicit form from (11) yields: Here is the paraphrased text usingA k
andA k′ notation:
W†W=
(∑
k
A†
k⊗⟨k|
)(∑
k′
Ak′⊗|k′⟩
)
=
∑
k,k′
A†
kAk′⊗⟨k|k′⟩=
∑
k
A†
kAk =1IH 1
2
,
where the final equality represents the fundamental completeness relation satisfied by the AKLT
MPS matrices, confirming the isometric property.
The equivalence between the Stinespring form and the explicit Kraus representation is estab-
lished through direct computation:
W†(X⊗Y)W=
(∑
k
A†
k⊗⟨k|
)
(X⊗Y)
(∑
k′
Ak′⊗|k′⟩
)
=
∑
k,k′
A†
kXAk′⊗⟨k|Y|k′⟩=
∑
k,k′
⟨k′|Y|k⟩A kXA†
k.
where the adjoint symmetry of the inner product ensures the final form matches the definition.
Complete positivity follows immediately from the Stinespring dilation: for any positive opera-
torPin the amplified space, the map (1I n⊗EO,H)(P) manifests as a conjugation by the isometric
extension (1In⊗W), preserving positivity. Unitality is verified through the chain:
EO,H(1IH 1
2
⊗1IH1) =W †(1IH 1
2
⊗1IH1)W=W †W=1I H 1
2
demonstrating preservation of the identity.
9
The dual channel characterization emerges from the Hilbert-Schmidt adjoint relation. For
arbitrary operatorsX,Y,Z, we systematically derive:
⟨EO,H(X⊗Y),Z⟩ HS = Tr[(W†(X⊗Y)W) †Z] =⟨X⊗Y,WZW †⟩HS,
establishingE ∗
O,H(Z) =WZW †. The explicit Kraus form follows by expanding this expression:
WZW† =
(∑
k
A[k]⊗|k⟩
)
Z
(∑
k′
A[k′]†⊗⟨k′|
)
=
∑
k,k′
A[k]ZA [k′]†⊗|k⟩⟨k′|,
completing the demonstration of all stated properties.
Theorem 3.4.Letϕ 0 be an initial state onB(H 1
2
),E H :B(H 1
2
)⊗B(H 1
2
)→B(H 1
2
)the hidden
transition expectation (12), andE O,H :B(H 1
2
)⊗B(H 1)→B(H 1
2
)the emission transition expecta-
tion (14). For the HQMMφ O,H associated with the tripleΞ = (ϕ 0,EH,EO,H)and local observables
X⊗Y= ⨂n
i=1Xi⊗Yi, we have:
φO,H(X⊗Y) =
∑
k1,...,kn
k′
1,...,k′
n
( n∏
ℓ=1
⟨kℓ|Yℓ|k′
ℓ⟩
)
φk1,...,kn
k′
1,...,k′
n
(X),(16)
where the coefficient functionals are given by the nested composition:
φk1,...,kn
k′
1,...,k′
n
(X) =ϕ 0
(
V†
(
Ak1X1A†
k′
1
⊗···⊗V †
(
AknXnA†
k′n
⊗1IH
)
V···
)
V
)
.(17)
Proof.The fundamental building block (2) of the HQMMs emerges from the expression:
EXℓ,Yℓ(Z) =E H(EO,H(Xℓ⊗Yℓ)⊗Z),∀Z∈B H
Substituting the emission transition expectation:
EXn,Yn(1IH) =E H
(
EO,H(X⊗Y)⊗1I H 1
2
)
(14)
=E H

∑
kn,k′n
⟨kn|Yn|k′
n⟩AknXnA†
k′n
⊗1IH 1
2


(12)
=
∑
kn,k′n
⟨kn|Yn|k′
n⟩EH
(
AknXnA†
k′n
⊗1IH 1
2
)
We now compute then-fold composition by induction. For the base casen= 1:
φO,H(X1⊗Y 1) =ϕ 0◦EX1,Y1(1IH) =
∑
k1,k′
1
⟨k1|Y1|k′
1⟩ϕ0
(
EH(Ak1X1A†
k′
1
⊗1IH 1
2
)
)
,
which matches the theorem statement. For the inductive step, assume the decomposition holds
forn−1:
EX2,Y2◦···◦E Xn,Yn(1IH) =
∑
k2,...,kn
k′
2,...,k′
n
( n∏
ℓ=2
⟨kℓ|Yℓ|k′
ℓ⟩
)
EH
(
Ak2X2A†
k′
2
⊗···⊗E H
(
AknXnA†
k′n
⊗1IH 1
2
)
···
)
.
10
ApplyingE X1,Y1 to this expression:
EX1,Y1◦EX2,Y2◦···◦E Xn,Yn(1IH 1
2
)
=
∑
k1,k′
1
⟨k1|Y1|k′
1⟩EH
(
Ak1X1A†
k′
1
⊗EX2,Y2◦···◦E Xn,Yn(1IH 1
2
)
)
=
∑
k1,...,kn
k′
1,...,k′
n
( n∏
ℓ=1
⟨kℓ|Yℓ|k′
ℓ⟩
)
EH
(
Ak1X1A†
k′
1
⊗EH
(
Ak2X2A†
k′
2
⊗···⊗E H
(
AknXnA†
k′n
⊗1IH 1
2
)
···
))
.
Applying the initial stateϕ 0 yields the desired result:
φO,H(X⊗Y) =
∑
k1,...,kn
k′
1,...,k′
n
( n∏
ℓ=1
⟨kℓ|Yℓ|k′
ℓ⟩
)
φk1,...,kn
k′
1,...,k′
n
(X),
where the coefficient functionals are precisely the nested compositions in (17). This completes
the proof, demonstrating how the forward transition maps naturally generate the hierarchical
structure of the HQMM.
Corollary 3.5.In the notation of Theorem 3.4, the HQMM structure induces two naturally
defined processes with distinct mathematical characteristics:
1. The marginal processφ H on the hidden algebraB(H 1
2
)⊗N, defined by
φH(X) =φ O,H(X⊗1I⊗n
H1),
constitutes aquantum Markov chain. This process admits the explicit recursive representa-
tion:
φH(X) =
∑
k1,...,kn
ϕ0
(
V†
(
Ak1X1A†
k′
1
⊗···⊗V †
(
AknXnA†
k′n
⊗1IH
)
V···
)
V
)
(18)
whereΦ AKLT :B(H 1
2
)→B(H 1
2
)denotes the quantum channel associated with the AKLT
model, as specified in (6).
2. The marginal processφ O on the observable algebraB(H 1)⊗N, obtained via
φO(Y) =φ O,H(1I⊗n
H 1
2
⊗Y),
exhibitsnon-Markovianbehavior. Its structure is given by:
φO(Y) =
∑
k1,...,kn
k′
1,...,k′
n
( n∏
ℓ=1
⟨kℓ|Yℓ|k′
ℓ⟩
)
φk1,...,kn
k′
1,...,k′
n
(1I⊗n
H 1
2
),(19)
where the coefficient functionalsφ k1,...,kn
k′
1,...,k′
n
are precisely those defined in equation (17)
Proof.1.To establish thatφ H is a quantum Markov chain with the representation (18), we
begin with the definition:
φH(X) =φ O,H(X⊗1I⊗n
H1).
Substituting into Theorem 3.4 withY ℓ =1IH1 for allℓ, we observe that the matrix elements
simplify as:
⟨kℓ|1IH1|k′
ℓ⟩=δ kℓ,k′
ℓ
.
11
This diagonalization collapses the double summation in (16) to a single sum over indicesk1,...,k n:
φH(X) =
∑
k1,...,kn
φk1,...,knk1,...,kn(X).
Now examining the coefficient functionals (17) under this diagonal constraint, we find that at
each time stepℓ, the expressionA kℓXℓA†
kℓ appears. Crucially, summing overk ℓ yields the AKLT
channel: ∑
kℓ
AkℓXℓA†
kℓ = ΦAKLT(Xℓ).
Substituting this into the nested structure of (17) recursively yields the claimed representation
(18). The quantum Markov property is manifest in this recursive composition structure. Indeed,
we can write:
φH(X1⊗···⊗X n) =ϕ 0◦EX1◦EX2◦···◦E Xn(1IH 1
2
)
where the transition mapsE X :B(H 1
2
)→B(H 1
2
) are defined by:
EX(ρ) =E H (ΦAKLT(X)⊗ρ).
This composition structure explicitly demonstrates that the process depends only on the current
state, satisfying the quantum Markov property.
1.For the observation process, we setX=1I ⊗n
H 1
2
in Theorem 3.4, yielding immediately:
φO(Y) =φ O,H(1I⊗n
H 1
2
⊗Y) =
∑
k1,...,kn
k′
1,...,k′
n
( n∏
ℓ=1
⟨kℓ|Yℓ|k′
ℓ⟩
)
φk1,...,kn
k′
1,...,k′
n
(1I⊗n
H 1
2
),
which is exactly (19). The non-Markovian character ofφ O follows from the fact that the coeffi-
cient functionalsφ k1,...,kn
k′
1,...,k′
n
(1I⊗n
H 1
2
) encode the full history of the hidden process through the nested
composition in (17). Unlike the Markovian hidden process, the observation statistics at any
time depend on the entire past history of hidden state evolution, mediated through the emission
transition expectationE O,H.
The hidden processφ H (Eq. 18) is a QMC on the infinite tensor product algeberaB(H 1
2
)⊗N,
which is strongly related to the AKLT structure. Namely, its correlations are governed by the
AKLT quantum channel. This means that its Markovian evolution directly reflects the physical
properties of the AKLT spin chain.
This provides a concrete, physical example of a QMC, connecting an abstract stochastic process
to a well-studied many-body system. This link offers a powerful new framework that allows more
significant probabilistic interpretations for SPT phases.
