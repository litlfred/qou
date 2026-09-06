---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-004-typicality-and-index-contractions
section_title: "Typicality and index contractions"
section_number: null
pages: 16-21
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
In the previous subsection, we have stated the requirements of crossing symmetry
and modular invariance on the moments of CFT data, which were clearly based
on the same requirements as in the regular CFT bootstrap. Now we will state an
additional assumption on the ensemble, to which we refer astypicality, which has its
origin in the theory of quantum chaos.
In chaotic many-body quantum systems, the Eigenstate Thermalization Hypoth-
esis (ETH) is a statistical ansatz to model the matrix elements of simple operators
Oij =⟨E i|O|E j⟩in high-energy eigenstates [37–41]. Instead of giving the exact, mi-
croscopic matrix elementsO ij, the ETH posits a smoothly varying envelope for the
diagonal matrix elements, and exponentially small erratic noise in the off-diagonal
matrix elements that can effectively be treated as random variables. As shown in [39],
the statistics of these random variables are approximately Gaussian, but important
non-Gaussianities can contribute at leading order to higher point thermal correlators
[65] (in particular out-of-time-ordered ones). The structure of these non-Gaussian
– 16 –
moments is fixed by assuming local unitary invariance in narrow microcanonical
windows around high energy eigenstates:
OU···O U≈O···O.(2.18)
HereO U =UOU †, withUa block-diagonal unitary matrix. This block-diagonal
structure is such thatUacts non-trivially in small microcanonical windows (that
nevertheless contain many energy levels), so as to keep the overall band structure
of the Hamiltonian intact. In the context of ETH, the assumption (2.18) is referred
to as typicality. Just like level repulsion, the intuition behind typicality stems from
random matrix universality: if the Hamiltonian in a narrow energy band resembles
a random matrix, then the relative basis change between the eigenbasis of simple
operators and that of the Hamiltonian should be a random unitary. By averaging
(2.18) overUin the unitary group, we immediately infer the index structure for the
momentsOa1b1···O anbn evaluated in energy eigenstates. Namely, for the moment to
be non-zero, each indexa i should be paired with an indexa j, and eachb k with some
bl. Diagrammatically, the allowed index contractions are visualized by cyclic, cactus
and non-cactus diagrams (see [40]).
This statistical approach to chaos and thermalization, formalized in the ETH, is
of course very similar to our point of view on OPE statistics and, in fact, a sharp
analogy can be made for OPE coefficients of 1 light and 2 heavy operators [13, 29].
More generally, for theories with a gravitational dual,Cijk can be treated as a random
variable as long as at least one index is in the heavy part of the spectrum [2, 3].
If the statistics of these random variables were assumed to be Gaussian, 10 the
index structure of some statistical moment of OPE coefficients would be entirely
fixed by Wick contractions. Although this Gaussian ansatz reproduces many bulk
computations [3], non-Gaussianities are necessary to match the ensemble prediction
with gravitational calculations of multiboundary wormhole topologies [12, 13] and
topologies with higher-genus boundaries [11, 15, 29]. Apart from bulk considera-
tions, these non-Gaussianities are also necessary in order to satisfy the full crossing
symmetry requirements discussed in the previous section [29, 30]. Hence, we can no
longer resort to Wick contractions.
This means we need a different principle to fix the index structure of a given
moment of OPE coefficients. As in the ETH, the full index structure can be fixed
by appealing to a version of typicality, now tailored to 2d CFT. 11 We will focus on
theories with a gap up to the black hole threshold, so we are interested in moments of
Cijk where all indices correspond to heavy primaries (when one or more indices is the
vacuum state, the index structure is trivially fixed by the selection ruleC ij1 =δ ij).
10Here, by Gaussian we mean that the probability distributionµ({h i, ¯hi,Cijk}) for the heavy
OPE coefficients is the form exp(− P
i,j,kf(hi, ¯hi,hj, ¯hj,hk, ¯hk)|Cijk|2), wherefis some smooth
function of the conformal weights.
11This notion of typicality has also been discussed in [13, 29, 42].
– 17 –
For these moments, typicality is the assumption that the average is approximately
invariant under orthogonal transformations in microcanonical windows:
CT
i1i2i3···C T
in−2in−1in ≈ Ci1i2i3···C in−2in−1in, C T
ijk :=
X
a,b,c
TiaTjbTkcCabc.(2.19)
HereTis a block-diagonal orthogonal matrix, with each block acting in a micro-
canonical Hilbert space of dimension eS(∆i) centered at energy ∆i with fixed spinJ i.
The fact thatTis real orthogonal, instead of unitary, follows from the reality con-
dition (2.3) (see also section 2 of [8]). As before, the typicality assumption fixes the
index structure by taking the Haar average over the local rotationsT: the moment
of structure constants in (2.19) is non-zero only if all indices are repeated pairwise.
For example, for the second moment, typicality implies the following structure:
C123C∗
1′2′3′ =
X
σ∈S3
δ1σ(1′)δ2σ(2′)δ3σ(3′) (sgn(σ))J1+J2+J3GS

1 2 3

+
X
τ,σ∈A3
δτ(1)σ(1′)δτ(2)τ(3)δσ(2′)σ(3′)GD

τ(2)
τ(1)
σ(2′)

.(2.20)
This is a sum over all pairings of 6 indices, with in total (6−1)!! = 15 terms, where
we have split the sum into the two distinct contraction patterns that can appear
for two OPE coefficients (recall eq. (2.5)). The first sum, corresponding to the
‘sunset’ contractionC 123C∗
123, is over the symmetric groupS 3, with sign factors that
account for the permutation property (2.3). The functionG S is a real-valued, totally
symmetric smooth function of the conformal weightsh 1,2,3, ¯h1,2,3, whose functional
form will be discussed below. The second term is a double sum over the alternating
groupA 3 ={Id,(123),(132)}, corresponding to the contractions of ‘dumbbell’ type
Cτ(1)τ(2)τ(2)Cτ(1)σ(2′)σ(2′). The real functionG D also depends smoothly on the weights
{ha, ¯ha}a∈{τ(1),τ(2),σ(2′)} in the heavy regime and vanishes whenJτ(1) is odd.12 Because
the functions multiplying the Kronecker delta’s are smooth, they are approximately
constant over a narrow microcanonical window in whichTacts, which explains why
the structure (2.20) indeed obeys the typicality condition (2.19).
For the higher statistical moments, the index structure is similarly fixed to be
a sum over pairwise index contractions. Because each OPE coefficient has three
indices, this automatically implies that all odd moments vanish. 13 The non-zero
12In each term of (2.20),G D is the same function, but evaluated on different conformal weights,
as specified by the even permutationsτandσ.
13The fact that odd moments vanish also already follows from the fact that the canonical normal-
ization of the CFT operatorO i is unchanged underO i→−O i, so there is no canonical definition
of the overall sign of a moment containing an odd number of appearances ofO i. Let us also remark
that the statement that odd moments vanish holds in the ‘pure’ gravity ensemble, where all non-
vacuum states are above the black hole threshold. If we allow states in the conical defect regime,
we can get non-vanishing odd moments: for a contribution to the cubic moment, see [13].
– 18 –
index contractions can be visualized again by trivalent graphs Γ, such as the ones
depicted in (2.6), so that the general ansatz compatible with typicality is
Ci1i2i3···C in−2in−1in =
X
pairingsP
δP
i1···in sgn(P)G Γ

{ha, ¯ha}ea∈Γ

.(2.21)
The sum is over the set of partitions ofnelements inton/2 pairs (wherenis even).
To each pairingPwe associate a trivalent graph Γ (really an equivalence class up to
relabellings of the edges) and a product of Kronecker delta’sδ P :=Q
(a,b)∈Pδiaib. We
define the sign ofPby labeling the edges of Γ and choosing an orientation for each
vertex; then we define sgn(P) := Q
vabc∈Γ sgn(vabc)Jia+Jib+Jic where sgn(vabc) is 1 if
the index labelsabcare ordered clockwise; and−1 if they are ordered anti-clockwise.
When two index labels coincide, we also define sgn(v abb) = 1. These±signs are
necessary for compatibility of the ansatz with the permutation property (2.3) of the
OPE coefficients.
There are a few things to note about the ansatz (2.21) predicted by typicality.
First, there are more allowed contractions in (2.21) than in the ETH. This is because
the Haar average is taken over orthogonal matrices, whereas in ‘standard’ ETH the
average is over the unitary group. 14 Hence, the ETH ansatz forO aibi always pairs
ana i-index with ana j-index, andb i withb j, while in the CFT case (2.21) any index
can be paired to any other index. This means that, for example, the analog of the
dumbbell contractionC122C133 is absent in ETH, because in ETH the connected part
ofO22O33 is zero forE 2̸=E 3.
Second, the non-zero contraction patterns in (2.21) are naturally encoded in
averages of genus-gpartition functionsZ[Σ g], expanded in Virasoro conformal blocks
as in (2.4). However, as explained in the previous section, although the sum over
pairings is finite (with (2n−1)!! terms), there is an infinite number of conformal
blocks. So, for each graph topology Γ, the functionG Γ can itself be an infinite sum
of contributions. In gravity, these contributions consist of bulk topologies with a
boundary given by a marked Riemann surface, schematicallyG Γ =P
MΓ
Zgrav[MΓ],
as will be explained in section 3. However, so far we have not assumed a bulk dual,
and hence the functionsG Γ only need to be sufficiently smooth for (2.21) to obey the
typicality assumption (2.19).
Third, in the literature on OPE statistics it is customary, by a slight abuse of
notation (also perpetrated by some of the present authors), to refer to the functions
GΓ by the corresponding moment Q
vijk∈ΓCijk. For example, we could write
C123C∗
123 =G S(h1,2,3, ¯h1,2,3).(2.22)
This is not an abuse of notation as long as all indices are different, because only a
single term in the sum of (2.20) will be non-zero. However, when some indices coin-
cide, this is no longer entirely correct: for example, C122C122 receives contributions
14Straightforward extensions of the ETH to the GOE have also been discussed, see [66].
– 19 –
from both the sunset and dumbbell contractions,G S andG D (see below). This obser-
vation may seem like a minor detail, but it is at the root of answering our question
why non-handlebodies appear in the sum over topologies! Saving a full explanation
of this fact for section 4, let us now briefly discuss the structure of the ansatz (2.21)
when a subset of the indices is repeated.
Implications of typicality for repeated indices.Typicality implies that mo-
ments of OPE coefficients are non-zero only when all indices are paired. This includes
contractions in which indices are repeatedmore than once. For example, for the OPE
variance, the typicality ansatz (2.19) forO 1̸=O 2 reads:
C122C122 =
 
1 + (−1)J1

GS

1 2 2

+GD

2
1
2

.(2.23)
Note that the factor
 
1 + (−1)J1

in the first term projects onto even spinJ 1, in
accordance with the fact thatC 122 vanishes whenJ 1 is odd.15
Similarly, when all indices coincide, all contractions contribute:
C111C111 = 3
 
1 + (−1)J1

GS

1 1 1

+ 9GD

1
1
1

.(2.24)
These combinatorial factors (or ‘degeneracies’) in the statistical moments of OPE
coefficients will be important when we match to gravity in sections 4 and 5. An
entirely analogous observation holds for higher moments of OPE coefficients: when
a subset of indices coincide, there are more terms in the ansatz (2.21) that can
contribute, which can originate from different graph topologies.
One interesting point to observe here is that index repetition is not a notion
that is invariant under crossing. For example, consider the contribution to C113C223
from the index contractionδ 12. Let us rewrite the discrete Kronicker delta using the
continuous Dirac deltaδ 2(h1−h 2)≡δ(h 1−h 2)δ(¯h1− ¯h2), multiplied by appropri-
ate densities of statesρ i≡ρ(h i, ¯hi). Under the one-point S-transform, this index
contraction gets mapped to:
Z
dh1d¯h1δ2(h1−h 2)ρ2ρ3C113C223|Sh1h4[h3]|2 =ρ2ρ3C223C223|Sh2h4[h3]|2.(2.25)
By the crossing equation (2.17b), the RHS now contributes to ρ2ρ3ρ4C223C443, and is
non-zero even whenh 2 andh 4 do not coincide. So we see that crossing symmetry re-
lates moments with repeated pairs of indices to moments with distinct (non-repeated)
pairs of indices. This interplay between crossing symmetry and typicality will be at
the heart of the mechanism that, on the bulk side, will be responsible for generating
a large class of non-handlebodies in the sum over topologies.
15The functionG D is non-zero only for evenJ 1, which follows from (2.3) and (2.20) evaluated on
the dumbbell contraction C122C133 withO 2̸=O 3.
– 20 –
