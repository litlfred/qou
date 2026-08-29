---
doc_id: arxiv-2605.09605v2
doc_title: "Cocycle Actions on Hidden Quantum Markov Models:"
section_id: sec-001-cocycle-actions-and-symmetry-protection-in-hqmms
section_title: "Cocycle Actions and Symmetry Protection in HQMMs"
section_number: null
pages: 3-11
source_pdf: 2605.09605v2.pdf
source_sha256: 24496fb444a2b558
doc_brief: "Cocycle Actions on Hidden Quantum Markov Models: — We develop a symmetry action framework for hidden quantum Markov models (HQMMs) tailored to one-dimensional quantum spin systems and"
---
LetGbe a locally compact group. In quantum systems, symmetry actions are typically imple-
mented by unitary representations. However, within the framework ofHQMMs, the hidden sector
may carry aprojectiverepresentation, reflecting the anomalous nature of the symmetry in the
corresponding symmetry-protected topological (SPT) phase. This projective character is encoded
in a 2-cocycle, which defines an element of the second cohomology groupH 2(G,U(1)). Through-
out the remainder of the paper, the notation associated with the HQMM formalism is introduced
in Appendix A.
Aprojective unitary representationofGon a Hilbert spaceHis a mapπ:G→U(H) such
that for allg,h∈G,
π(g)π(h) =ω(g,h)π(gh),(1)
whereω:G×G→U(1) is a measurable function satisfying the 2-cocycle condition:
ω(g,h)ω(gh,k) =ω(g,hk)ω(h,k),∀g,h,k∈G.(2)
The cocycleωis called themultiplierof the projective representation. Two projective representa-
tionsπandπ ′ are equivalent if there exists a functionλ:G→U(1) such thatπ ′(g) =λ(g)π(g),
which induces a cohomologous cocycleω ′(g,h) =λ(g)λ(h) λ(gh)ω(g,h). The equivalence class
[ω]∈H 2(G,U(1)) is a topological invariant characterizing the projective representation.
3
LetHandKbe the separable Hilbert spaces introduced in Section 1, representing the hidden
and observable degrees of freedom, respectively. Letπ:G→U(H) be a projective representation
ofGon the hidden space with associated 2-cocycleω π∈H 2(G,U(1)), and letρ:G→U(K) be
an ordinary (linear) unitary representation on the observable space, corresponding to the trivial
cocycleω ρ(g,h) = 1.
The algebraic action ofGon the single-site algebrasA H =B(H) andA O =B(K) is defined
via the adjoint action:
α(H)
g (X) :=π(g)Xπ(g) †, β g(Y) :=ρ(g)Yρ(g) †,(3)
for allX∈A H,Y∈A O, andg∈G. These actions extend naturally to the quasi-local algebras
AH,N0 andA O,N0 via the tensor product structure, i.e., for elementary tensors,
α(H)
g
( n⨂
k=0
Xk
)
=
n⨂
k=0
π(g)Xkπ(g)†, β g
( n⨂
k=0
Yk
)
=
n⨂
k=0
ρ(g)Ykρ(g)†.(4)
The projective nature ofπmanifests in the composition law:
α(H)
g ◦α (H)
h = Ad
(
ωπ(g,h)IH
)
◦α (H)
gh ,(5)
which reflects the fact thatα (H) is an action up to inner automorphisms implemented by the scalar
cocycleω π. For the linear representationρ, the corresponding actionβsatisfiesβ g◦β h =β gh
without any phase.
We now formulate the precise symmetry requirements that define a covariant HQMM. These
conditions encapsulate how the projective symmetry acts on the generative structure.
ϕ0
(
π(g)Zπ(g)†
)
=ϕ 0(Z)∀g∈G,∀Z∈A H.(6)
EH
(
π(g)Z1π(g)†⊗π(g)Z 2π(g)†
)
=π(g)E H(Z1⊗Z 2)π(g)† ∀g∈G,∀Z 1,Z 2∈A H.(7)
EH,O
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g)†
)
=π(g)E H,O(X⊗Y)π(g) † ∀g∈G,∀X∈A H,∀Y∈A O.(8)
The covariance condition (8) is the central structural relation. It states thatE O,H intertwines
the projectiveG-action onA H with the linearG-action onA O, i.e.,E O,H◦(α(H)
g ⊗βg) =α (H)
g ◦EO,H.
This intertwining absorbs the projective anomaly of the hidden sector, forcing the observable sector
to transform under an ordinary representation.
A central extension perspective illuminates the cohomological significance of these conditions.
Consider the short exact sequence
1−→U(1)−→ ~G−→G−→1,
where ~Gis the central extension ofGby U(1) determined by the cocycleω. Thenπlifts to a
linear representation ~πof ~GonHsatisfying ~π((g,λ)) =λπ(g) forλ∈U(1). The emission map
covariance condition (8) then becomes
EH,O
(
~π((g,λ))X ~π((g,λ))†⊗ρ(g)Yρ(g) †
)
= ~π((g,λ))E H,O(X⊗Y) ~π((g,λ))†,
where the U(1) phaseλcancels on both sides. Hence the emission map provides acocycle in-
tertwinerbetween the centrally extended hidden dynamics and the linear observable dynamics.
The existence of such an intertwiner implies that the obstruction [ω]∈H 2(G,U(1)) is trivialized
when passing through the mapE H,O, meaning that the compositionE H,O◦(·⊗id AO) converts the
projective action on the first tensor factor into a linear action on the image.
4
The interplay between projective and linear representations manifests richly in the tensor
product structure of the HQMM. Consider the tensor product representationπ⊗ρ:G→U(H⊗K)
defined by (π⊗ρ)(g) :=π(g)⊗ρ(g). Its composition law follows from (1):
(π⊗ρ)(g)(π⊗ρ)(h) =π(g)π(h)⊗ρ(g)ρ(h) =ω(g,h)π(gh)⊗ρ(gh) =ω(g,h) (π⊗ρ)(gh).
Thusπ⊗ρis a projective representation ofGwith the same cocycleωasπ. Consequently, the
composite actionα (H)
g ⊗βg onA H⊗AO satisfies
(α(H)
g ⊗βg)◦(α (H)
h ⊗βh) = Ad
(
ω(g,h)IH⊗K
)
◦(α (H)
gh ⊗βgh),
so the projective nature persists at the level of the composite system. The covariance condition
(8) exactly cancels the projective phase coming from the hidden sector. As a result, althoughα (H)
itself is projective, its composition withE O,H becomes linear. This cancellation is the algebraic
hallmark of a consistent, anomaly-free coupling between the hidden and observable sectors at
their interface.
More generally, take two projective representationsπ 1 andπ 2 ofG, with cocyclesω 1 andω 2
respectively. Their tensor productπ 1⊗π2 is again projective, with cocycleω 1ω2 given by pointwise
multiplication. Their tensor productπ 1⊗π 2 satisfies
(π1⊗π 2)(g)(π1⊗π 2)(h) =ω 1(g,h)ω 2(g,h) (π 1⊗π 2)(gh),
so the cocycle of the tensor product is the pointwise productω 1ω2. In the HQMM setting,
the hidden transition mapE H sends the tensor product of two projective representationsπ⊗π
(cocycleω 2) to a single copyπ(cocycleω). Equivariance (7) then forces [ω 2] = [ω] inH 2(G,U(1)).
This holds automatically only whenωis a coboundary orGhas special properties; otherwise,
the equivariance must be twisted. In the generic case where [ω] has order greater than 1, this
condition forces a refinement of the equivariance structure, typically implemented by a 2-cocycle
on the map itself, leading to the notion oftwisted equivariancethat we shall explore in subsequent
sections.
We now turn to the analysis of the two causal structures introduced in Section 1. Recall that
the conventional and causal structures are defined by (27) and (28), respectively in terms of the
generative mappings (EH,EH,O) as:
For each structure, we define the corresponding sliced maps that propagate the hidden state
forward. For the conventional structure, defineT (conv)
X,Y :A H→A H by
T (conv)
X,Y (Z) :=T (conv)(X⊗Z⊗Y) =E H
(
EH,O(X⊗Y)⊗Z
)
.(9)
For the causal structure, defineT (caus)
X,Y :A H→A H by
T (caus)
X,Y (Z) :=T (caus)(X⊗Z⊗Y) =E H,O
(
EH(X⊗Z)⊗Y
)
.(10)
These sliced maps encapsulate the sequential dynamics: given a current hidden stateZand
an incoming pair (X,Y) representing the left neighbor hidden operator and the local observable,
they produce the updated hidden state after the site.
Lemma 2.1.Under the symmetry conditions(7)and(8), for allg∈G,X,Z∈A H, andY∈A O,
T (conv)
π(g)Xπ(g) †,ρ(g)Yρ(g) †
(
π(g)Zπ(g)†
)
=π(g)T (conv)
X,Y (Z)π(g)†.(11)
Proof.The proof follows directly from the covariance property (8) ofE H,O and the equivariance
5
property (7) ofE H:
T (conv)
π(g)Xπ(g) †,ρ(g)Yρ(g) †
(
π(g)Zπ(g)†
)
=E H
(
EH,O
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
⊗π(g)Zπ(g) †
)
(8)
=E H
(
π(g)EH,O(X⊗Y)π(g) †⊗π(g)Zπ(g) †
)
(7)
=π(g)E H
(
EH,O(X⊗Y)⊗Z
)
π(g)†
=π(g)T (conv)
X,Y (Z)π(g)†.
Lemma 2.2.Under the symmetry conditions(7)and(8), for allg∈G,X,Z∈A H, andY∈A O,
T (caus)
π(g)Xπ(g) †,ρ(g)Yρ(g) †
(
π(g)Zπ(g)†
)
=π(g)T (caus)
X,Y (Z)π(g)†.(12)
Proof.The proof proceeds analogously, employing the equivariance property (7) ofE H first, fol-
lowed by the covariance property (8) ofE H,O:
T (caus)
π(g)Xπ(g) †,ρ(g)Yρ(g) †
(
π(g)Zπ(g)†
)
=E H,O
(
EH
(
π(g)Xπ(g)†⊗π(g)Zπ(g) †
)
⊗ρ(g)Yρ(g) †
)
(7)
=E H,O
(
π(g)EH(X⊗Z)π(g) †⊗ρ(g)Yρ(g) †
)
(8)
=π(g)E H,O
(
EH(X⊗Z)⊗Y
)
π(g)†
=π(g)T (caus)
X,Y (Z)π(g)†.
Theorem 2.3.LetΞ = (ϕ 0,EH,EH,O)be an HQMM satisfying the symmetry conditions(6),(7),
and(8). Letφ (conv) andφ (caus) be the global states onA N0 generated by the conventional and causal
transition maps, respectively, via the construction of Theorem 1. Then for allg∈G,A∈A H,N0,
andB∈A O,N0,
φ(conv)
(
α(H)
g (A)⊗β g(B)
)
=φ (conv)(A⊗B),(13)
φ(caus)
(
α(H)
g (A)⊗β g(B)
)
=φ (caus)(A⊗B).(14)
In particular, both global states are invariant under the combined projective-linear action ofG.
Consequently, the hidden marginalsφ (conv)
H andφ (caus)
H are invariant under the projective action
α(H), and the observable marginalsφ (conv)
O andφ (caus)
O are invariant under the linear actionβ.
Proof.We present the proof for the conventional structure; the proof for the causal structure is
entirely analogous, with Lemma 2.2 replacing Lemma 2.1.
LetA= ⨂n
k=0Xk∈A H,N0 andB= ⨂n
k=0Yk∈A O,N0 be elementary tensors supported on sites
0,...,n. The extension to arbitrary local observables follows by linearity and continuity, and the
inductive limit construction ensures the result holds for all quasi-local observables.
Recall from Theorem 1 that the finite-volume state onA [0,n] is given by
φ(conv)
n
( n⨂
k=0
(Xk⊗Yk)
)
=ϕ 0◦T (conv)
X0,Y0 ◦T (conv)
X1,Y1 ◦···◦T (conv)
Xn,Yn (IAH),(15)
where the composition denotes successive application of the sliced maps. In what follows, for
(c)∈{(conv),(caus)}we denote the composition of the transition mapsT (c)
Xj,Yj by
6
⃝n
k=mTXk,Yk :=T (c)
Xm,Ym◦T (c)
X1,Y1◦···◦T (c)
Xn,Yn
We prove by induction onnthat for allg∈G,
⃝n
k=0T (conv)
π(g)Xkπ(g)†,ρ(g)Y kρ(g)†(IAH) =π(g)
(
⃝n
k=0T (conv)
Xk,Yk (IAH)
)
π(g)†.(16)
For a single site, Lemma 2.1 withZ=I AH together with the observation thatπ(g)I AHπ(g)† =
IAH yields
T (conv)
π(g)X0π(g)†,ρ(g)Y 0ρ(g)†(IAH) =π(g)T (conv)
X0,Y0 (IAH)π(g)†.
Assume the claim holds for chains of lengthn. For lengthn+ 1, define the composition for
the lastn+ 1 sites:
Cn :=⃝ n+1
k=1T (conv)
Xk,Yk ,D n :=⃝ n+1
k=1T (conv)
π(g)Xkπ(g)†,ρ(g)Y kρ(g)†.
By the induction hypothesis applied to the sites 1,...,n+ 1,
Dn(IAH) =π(g)C n(IAH)π(g)†.(17)
Now compute the full composition forn+ 1 sites:
⃝n+1
k=0T (conv)
π(g)Xkπ(g)†,ρ(g)Y kρ(g)†(IAH)
=T (conv)
π(g)X0π(g)†,ρ(g)Y 0ρ(g)†
(
Dn(IAH)
)
=T (conv)
π(g)X0π(g)†,ρ(g)Y 0ρ(g)†
(
π(g)C n(IAH)π(g)†
)
by (17)
=π(g)T (conv)
X0,Y0
(
Cn(IAH)
)
π(g)† by Lemma 2.1
=π(g)
(
⃝n+1
k=0T (conv)
Xk,Yk (IAH)
)
π(g)†.
This completes the induction.
Now apply the initial stateϕ 0. By the invariance condition (6),
φ(conv)
n
(
α(H)
g (A)⊗β g(B)
)
=ϕ 0
(
⃝n
k=0T (conv)
π(g)Xkπ(g)†,ρ(g)Y kρ(g)†(IAH)
)
=ϕ 0
(
π(g)
(
⃝n
k=0T (conv)
Xk,Yk (IAH)
)
π(g)†
)
=ϕ 0
(
⃝n
k=0T (conv)
Xk,Yk (IAH)
)
=φ (conv)
n (A⊗B).
Since this holds for all finitenand the embeddingsι m,n are compatible with the group actions
(i.e.,ι m,n◦(α (H)
g ⊗βg) = (α(H)
g ⊗βg)◦ι m,n), the projective limit stateφ (conv) onA N0 satisfies (13).
Proof for the causal structure.The proof follows exactly the same inductive structure, withT (caus)
replacingT (conv) and Lemma 2.2 replacing Lemma 2.1. The finite-volume state is
φ(caus)
n
( n⨂
k=0
(Xk⊗Yk)
)
=ϕ 0◦T (caus)
X0,Y0 ◦T (caus)
X1,Y1 ◦···◦T (caus)
Xn,Yn (IAH).
One proves by induction that
⃝n
k=0T (caus)
π(g)Xkπ(g)†,ρ(g)Y kρ(g)†(IAH) =π(g)
(
⃝n
k=0T (caus)
Xk,Yk (IAH)
)
π(g)†,
using Lemma 2.2 at each step. Applyingϕ 0 and its invariance (6) yields (14).
The cohomology class [ω]∈H 2(G,U(1)) thus emerges as a well-defined invariant of the HQMM
state. It classifies the projective nature of the hidden representation and, together with the
covariance conditions (7) and (8), provides the algebraic characterization of the SPT order. The
emission mapE H,O serves as acocycle intertwinerthat mediates between the projective hidden
dynamics and the linear observable dynamics, effectively absorbing the anomaly at the interface.
7
3 Application to AKLT’s Symmetry-Protected Topologi-
cal Order
The AKLT state [4] stands as a paradigmatic example of a SPT phase in 1D. Its topologi-
cal protection originates from a projective representation of the symmetry group on the vir-
tual degrees of freedom—a structure that aligns naturally with the HQMM framework devel-
oped in the preceding sections. This projective character is encoded in a nontrivial 2-cocycle
[ω]∈H 2(SO(3),U(1)) ∼= Z2, which obstructs the lifting of the symmetry action on the hidden
space to a linear representation. Within the HQMM formalism, this obstruction is precisely ab-
sorbed by the emission mapE O,H, which acts as acocycle intertwinermediating between the
projective hidden dynamics and the linear observable dynamics.
We now demonstrate how the abstract covariance conditions established earlier—specifically
(7) and (8)—manifest concretely in the AKLT construction. This reveals that SPT order is not
merely a static property of the ground state but is dynamically preserved under the quantum
Markov evolution generated by the HQMM. In doing so, we extend the analysis of topological
order in emission transitions introduced in [25] to a more structural and algebraic level, grounding
the classification of SPT phases within the operator-algebraic framework of quantum stochastic
processes.
LetG= SO(3) denote the symmetry group. The physical Hilbert space isK=H 1, on which
Gacts via the linear spin-1 representationρ:G→U(H 1). The hidden (virtual) Hilbert space is
H=H 1/2, whereGacts via the irreducible projective spin-1/2 representationπ:G→U(H 1/2).
The projective nature ofπis captured by a 2-cocycleω:G×G→U(1) satisfying the composition
law
π(g1)π(g2) =ω(g 1,g 2)π(g 1g2)∀g 1,g 2∈G,(18)
together with the cocycle condition (2). The cohomology class [ω]∈H 2(SO(3),U(1)) is the
generator ofZ 2, reflecting the double-cover relation SU(2)→SO(3) [10, 26], and serves as the
topological invariant distinguishing the nontrivial SPT phase.
Let{|k⟩} k=+,−,0 denote the standard orthonormal basis ofH 1 corresponding to the eigenstates
ofS z with eigenvalues +1,−1,0, respectively. The AKLT state is represented as a translation-
invariant matrix product state with virtual dimension 2. Its local tensors are linear operators
Ak∈B(H 1/2) defined by
A+ = 1√
2
(
0 1
0 0
)
, A 0 = 1√
2
(
1 0
0−1
)
, A − = 1√
2
(
0 0
−1 0
)
,
expressed in the standard basis ofH 1/2∼= C2. These operators satisfy the fundamental intertwin-
ing relation that encodes the SPT order [2]:
∑
k′
ρ(g)kk′Ak′ =π(g)A kπ(g)† ∀g∈G,∀k∈{+,0,−},(19)
whereρ(g) kk′ =⟨k|ρ(g)|k ′⟩denotes the matrix element of the physical representation. This
relation asserts that a symmetry transformation applied to the physical index is equivalent to
conjugation of the virtual operators by the projective representationπ(g).
The emission mapE H,O :A H⊗AO→A H is defined by its action on elementary tensors as
EH,O(X⊗Y) =
∑
k,k′∈{+,0,−}
⟨k′|Y|k⟩A kXA†
k′, X∈A H, Y∈A O.(20)
This map is completely positive and unital. Indeed, positivity follows from the representation
EH,O(X⊗Y) = ∑
k,k′⟨k′|Y|k⟩A kXA†
k′ =∑
kAkXA†
k whenY=I AO, and the general case follows
from the fact thatYcan be diagonalized and the sum overk,k ′ can be reorganized as a sum over
kwith appropriate coefficients.
8
The hidden transition mapE H :A H⊗A H→A H for the AKLT chain is given by the multi-
plication map
EH(Z1⊗Z 2) =Z 1Tr(Z2), Z 1,Z 2∈A H.(21)
This map is completely positive and unital, as it is the∗-homomorphism induced by the multi-
plication operation onB(H 1/2).
We now verify that the generative triple (ϕ 0,EH,EO,H) satisfies the symmetry conditions (6),
(7), and (8). The verification proceeds through a sequence of lemmas establishing the sym-
metry properties at each level of the construction, culminating in Theorem 3.5. This theorem
demonstrates that the global HQMM statesφ (conv) andφ (caus) are invariant under the combined
projective-linear action of SO(3). Together with the nontriviality of the cocycle [ω], this invari-
ance certifies that the AKLT state realizes a nontrivial SPT phase within the HQMM framework
and that this topological protection persists under quantum Markov evolution.
The initial stateϕ 0 :A H→Cis defined as the vector state associated with the fixed point of
the projective representation. Sinceπis irreducible, there exists a unique (up to scalar) vector
Ω∈H 1/2 satisfyingπ(g)Ω =λ(g)Ω for some phaseλ(g). For the spin-1/2 representation, one
may take Ω to be the eigenvector ofπ(g z) with eigenvalue 1, which yields a state satisfying
ϕ0(π(g)Zπ(g)†) =ϕ 0(Z)∀g∈G,∀Z∈A H,(22)
since the phase factors cancel in the expectation value.
Lemma 3.1.Letπ:G→U(H 1/2)be the projective spin-1/2representation andρ:G→U(H 1)
the linear spin-1representation. The emission mapE H,O defined in(20)satisfies the covariance
condition
EH,O
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
=π(g)E H,O(X⊗Y)π(g) † (23)
for allg∈G,X∈A H, andY∈A O.
Proof.Fixg∈G,X∈A H, andY∈A O. By definition (20),
EH,O
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
=
∑
m,m′
⟨m|ρ(g)Yρ(g)†|m′⟩Am
(
π(g)Xπ(g)†
)
A†
m′.
Using the resolution of the identity ∑
k|k⟩⟨k|=I H1 and the unitarity ofρ(g), we expand the
matrix element:
⟨m|ρ(g)Yρ(g)†|m′⟩=
∑
k,k′
⟨m|ρ(g)|k⟩⟨k|Y|k ′⟩⟨k′|ρ(g)†|m′⟩=
∑
k,k′
ρ(g)mk⟨k|Y|k′⟩ρ(g)m′k′.
Substituting this expression yields
LHS =
∑
k,k′
⟨k|Y|k′⟩

∑
m,m′
ρ(g)mkρ(g)m′k′Am
(
π(g)Xπ(g)†
)
A†
m′

.
DefineS k,k′ as the inner sum. Since the sums overmandm ′ factorize,
Sk,k′ =
(∑
m
ρ(g)mkAm
)(
π(g)Xπ(g)†
)(∑
m′
ρ(g)m′k′A†
m′
)
.
Applying the covariance condition (19) to the first factor gives
∑
m
ρ(g)mkAm =π(g)A kπ(g)†.
For the third factor, take the adjoint of (19) applied to indexk ′:
∑
m′
ρ(g)m′k′A†
m′ =
(∑
m′
ρ(g)m′k′Am′
)†
=
(
π(g)Ak′π(g)†
)†
=π(g)A†
k′π(g)†.
9
Substituting these expressions intoS k,k′ and usingπ(g) †π(g) =I H1/2,
Sk,k′ =
(
π(g)Akπ(g)†
)(
π(g)Xπ(g)†
)(
π(g)A†
k′π(g)†
)
=π(g)A kXA†
k′π(g)†.
Therefore,
LHS =
∑
k,k′
⟨k|Y|k′⟩π(g)A kXA†
k′π(g)† =π(g)

∑
k,k′
⟨k|Y|k′⟩AkXA†
k′

π(g)† =π(g)E H,O(X⊗Y)π(g) †,
which completes the proof.
Lemma 3.2.The hidden transition mapE H defined in(21)satisfies the equivariance condition
EH
(
π(g)Z1π(g)†⊗π(g)Z 2π(g)†
)
=π(g)E H(Z1⊗Z 2)π(g)† (24)
for allg∈GandZ 1,Z 2∈A H.
Proof.By definition,
EH
(
π(g)Z1π(g)†⊗π(g)Z 2π(g)†
)
=
(
π(g)Z1π(g)†
)(
π(g)Z2π(g)†
)
=π(g)Z 1π(g)†π(g)Z2π(g)†.
Sinceπ(g) †π(g) =I H1/2,
π(g)Z1π(g)†π(g)Z2π(g)† =π(g)Z 1Z2π(g)† =π(g)E H(Z1⊗Z 2)π(g)†.
Lemma 3.3.Letπ:G→U(H 1/2)be the irreducible projective spin-1/2representation ofG=
SO(3). A stateϕ 0 onA H =B(H 1/2)is said to beG-invariant if it satisfies the invariance condition
ϕ0
(
π(g)Zπ(g)†
)
=ϕ 0(Z)∀g∈G,∀Z∈A H.(25)
For the irreducible representationπ, the set ofG-invariant states consists of a single element,
namely the normalized trace
ϕ0(Z) = 1
dim(H1/2) TrH1/2(Z) = 1
2 Tr(Z), Z∈A H.
This state is unique and serves as the canonical initial state for the AKLT HQMM.
Proof.We establish the result in two parts: first, we show that the normalized trace satisfies the
invariance condition; second, we prove uniqueness.
Invariance of the normalized trace.For anyg∈Gand anyZ∈A H,
ϕ0
(
π(g)Zπ(g)†
)
= 1
2 Tr
(
π(g)Zπ(g)†
)
.
By the cyclicity of the trace, Tr(π(g)Zπ(g)†) = Tr(Zπ(g)†π(g)). Sinceπ(g) is unitary,π(g) †π(g) =
IH1/2, whence
Tr(Zπ(g)†π(g)) = Tr(Z).
Thereforeϕ 0(π(g)Zπ(g)†) = 1
2 Tr(Z) =ϕ 0(Z), establishing (25).
Uniqueness.Letϕbe any state onB(H 1/2) satisfying (25). By the Riesz representation
theorem for finite-dimensional Hilbert spaces, there exists a unique density operatorρ∈B(H 1/2)
such thatϕ(Z) = Tr(ρZ) for allZ∈A H, withρ≥0 and Tr(ρ) = 1. The invariance condition
(25) implies
Tr
(
ρπ(g)Zπ(g) †
)
= Tr(ρZ)∀g∈G,∀Z∈A H.
10
Using the cyclicity of the trace on the left-hand side,
Tr
(
π(g)†ρπ(g)Z
)
= Tr(ρZ)∀g∈G,∀Z∈A H.
Since this holds for allZ, we obtain
π(g)†ρπ(g) =ρ∀g∈G,
or equivalently,π(g)ρ=ρπ(g) for allg∈G. Thusρbelongs to the commutant of the irreducible
representationπ, i.e.,ρ∈π(G) ′. By Schur’s lemma, the commutant of an irreducible represen-
tation consists of scalar multiples of the identity:π(G) ′ ={λI H1/2 :λ∈C}. Henceρ=λI H1/2
for someλ∈C. Positivity requiresλ≥0, and the normalization condition Tr(ρ) = 1 gives
λdim(H 1/2) = 1, i.e.,λ= 1/dim(H 1/2) = 1/2. Consequently,
ϕ(Z) = Tr
(
1
2 IH1/2Z
)
= 1
2 Tr(Z) =ϕ 0(Z),
proving uniqueness.
Remark 3.4.The uniqueness of the invariant state is a direct consequence of the irreducibility of
the projective representationπ. In the AKLT construction, the virtual spaceH 1/2 carries the irre-
ducible spin-1/2representation ofSO(3), which forces the initial state to be the maximally mixed
stateϕ 0(Z) = 1
2 Tr(Z). This state is often interpreted as the infinite-temperature state on the vir-
tual degrees of freedom, and its uniqueness under the symmetry ensures that the resulting HQMM
state inherits the topological protection without additional parameters. Wereπreducible, a convex
family of invariant states would exist, potentially allowing for symmetry-preserving deformations
that could trivialize the SPT order.
Theorem 3.5.LetΞ = (ϕ 0,EH,EH,O)be the HQMM defined by(25),(21), and(20). Letφ (c)
with(c)∈{(caus),(conv)}, be the global state onA N0 generated byΞvia the conventional causal
structure(9)and(10). Then for allg∈G,A∈A H,N0, andB∈A O,N0,
φ(c)
(
α(H)
g (A)⊗β g(B)
)
=φ (c)(A⊗B),(26)
whereα (H)
g = Ad(π(g))andβ g = Ad(ρ(g)).
Proof.Lemma 3.1 and Lemma 3.2 together verify the hypotheses of Theorem 2.3. The result
then follows directly.
Corollary 3.6.The global HQMM stateφ (conv) generated by the AKLT tensors carries a nontrivial
SPT order characterized by the projective cocycle[ω]∈H 2(SO(3),U(1))∼= Z2. The emission map
EO,H acts as a cocycle intertwiner mediating between the projective hidden dynamics and the linear
observable dynamics, thereby preserving the topological protection throughout the quantum Markov
evolution.
Thus, when viewed as a stationary state of a causal HQMM, the AKLT state exhibits a
robust SPT order encoded in the nontrivial cohomology class [ω]. This hierarchical symmetry
preservation—from local tensors through the emission map and hidden transition to the global
state—reveals how SPT order emerges from the consistent interplay between hidden dynamics
and symmetry constraints across all scales of the system [2, 8].
