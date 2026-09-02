---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-001-2-review-1-droplet-description-of-unitary-matrix
section_title: "Review 1 : Droplet description of unitary matrix models"
section_number: 2
pages: 5-7
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
---
We start with a very brief discussion on droplet description of diﬀerent large N phases of a generic
UMM. The partition function of UMM is given by,
Z =
∫
[dU]eS (U) (2.1)
where [dU] is the Haar measure and S (U) is a generic function of N× N unitary matrices U. The
Haar measure [ dU] and S (U) are invariant under unitary transformation. A particular class, but
yet general, of unitary matrix models is given by the following action
S (U) = N
Q∑
n=1
βn
n
(
TrU n + TrU†n)
(2.2)
where Q is any arbitrary positive integer and βns are some arbitrary real parameters. This model
is called the single plaquette model. This model has applications in lattice gauge theory. Partition
functions for diﬀerent large N Chern-Simons matter theories can also be written as a single pla-
quette model [10]. The large N phase structure of (2.2) for Q = 2 has been studied in [11, 12].
A special case of single plaquette model is Gross-Witten-Wadia model [13, 14], where βn>1 = 0.
5
The GWW model is one of the exactly solvable models and it appears in many contexts in physics
as well as in mathematics.
Since both the Haar measure and the action in equation (2.1) are invariant under unitary transfor-
mations, one can go to a diagonal basis
U→{ eiθ1,··· eiθi,··· , eiθN},
whereθis are the eigenvalues ofU. In the large N limit a particular distribution of these eigenvalues
on unit circle dominates the partition function. Deﬁning a distribution function (called eigenvalue
density)ρ(θ)
ρ(θ) = 1
N
N∑
i=1
δ(θ−θi) = dx
dθ (2.3)
one can show that in the large N limit the eigenvalue density satisﬁes the saddle point equa-
tion
−
∫
dθ′ cot
(θ−θ′
2
)
ρ(θ′) =
∑
n
βn cos nθ, with
∫
dθρ(θ) = 1. (2.4)
This equation is obtained by extremising the eﬀective action associated with the partition function
(2.1). For a given set of parameters{βn} one can solve this equation to ﬁnd ρ(θ) corresponding to
diﬀerent large N phases of the model under consideration. Di ﬀerent large N phases are classiﬁed
by number and positions of gaps inρ(θ) [11–15] on a unit circle.
A unitary matrix model can be equivalently analysed in terms of S U(N) (or U(N)) representa-
tions [7, 16–18], which are expressed in terms of Young diagrams and hence the generic partition
function (2.1) can be written in Young diagram basis as well. Expanding the partition function in
representation basis one ﬁnds
Z =
∑
{hi}
∑
⃗k,⃗l
ε(⃗β,⃗k)ε(⃗β,⃗l)
z⃗kz⃗l
χ⃗h(C(⃗k))χ⃗h(C(⃗l)) where , ε (⃗β,⃗k) =
∞∏
n=1
(Nβn)kn, z⃗k =
∞∏
n=1
kn!nkn. (2.5)
Here,{h1,··· , hN} are a set of hook numbers characterising a Young diagram, χ⃗h(C(⃗k)) is the
character of the permutation group S k for a conjugacy classC(⃗k) with k = ∑
n nkn in representation
{hi}. In the large N limit the partition function (2.5) is dominated by a Young diagram which is
characterised by a density function u(h)
u(h) =− dx
dh. (2.6)
Since h(x) is a monotonically decreasing function of x, Young density has an upper and lower cap
1≥ u(h)≥ 0∀ x∈ [0, 1]. Large N phases are characterised by di ﬀerent u(h). It is di ﬃcult to
ﬁnd a saddle point equation for u(h) for a generic plaquette model (2.2), but one can reconstruct
dominant Young diagrams [18] through the droplet picture. See Appendix A.2 for details.
6
