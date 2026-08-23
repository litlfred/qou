---
doc_id: arxiv-1705.01853v2
doc_title: "Line operators in the Standard Model"
section_id: sec-006-2-a-review-of-line-operators
section_title: "A Review of Line Operators"
section_number: 2
pages: 4-8
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
doc_brief: "Line operators in the Standard Model — There is an ambiguity in the gauge group of the Standard Model."
---
We start by reviewing the properties of line operators, described in [1], that we will
later need.
Wilson lines are operators which describe the insertion of an inﬁnitely m assive, elec-
trically charged particle sitting at the origin of space [6]. They are labe lled by repre-
sentations R of the gauge group G, and given by
WR = TrR P exp
(
i
∫
dt A 0
)
Wilson lines exist for all representations R, regardless of the dynamical matter content
of the theory. This means, in particular, that diﬀerent gauge grou ps G will have a
diﬀerent spectrum of Wilson lines, even if they share a common Lie alge bra g. We
denote the weight lattice of g as Λ w. Then the representations of the universal cover of
3
G — which we denote as ˜G — are labelled by points in the lattice Λ w/W where W is
the Weyl group. Representations of G = ˜G/ Γ are labelled by an appropriate sublattice
Λ w/W .
’t Hooft lines are operators which describe the insertion of an inﬁnite ly massive,
magnetically charged particle sitting at the origin of space [7]. They ar e best thought
of as defect operators, in which the gauge ﬁelds have suitable boun dary conditions
imposed on the worldline of the magnetic source [8]. For a gauge group G, ’t Hooft
lines are labelled by some sublattice of Λ mw/W where Λ mw is the magnetic weight
lattice [9]; it is the weight lattice of the dual Lie algebra g⋆, or the dual of the root
lattice of g.
More generally, we may probe the theory with a dyonic Wilson-’t Hooft line. These
are labelled by some sublattice of (Λ w × Λ mw)/W [8]. We will denote the weights as
(λ e, λ m) ∈ Λ w × Λ mw, with the identiﬁcation ( λ e, λ m) ∼ (wλ e, wλ m), where w ∈ W .
Given a choice of gauge group G = ˜G/ Γ, we would like to determine the allowed
spectrum of line operators. This problem was solved in [1] for connec ted groups. (Here
we consider only line operators which enjoy an independent existenc e, as opposed to
those which survive only on the boundary of a surface operator.) C ertain line operators
exist regardless of the choice of the discrete quotient Γ. For the W ilson lines, these
correspond to the root lattice Λ r ⊂ Λ w. They include, for example, the Wilson line in
the adjoint representation. Diﬀerent choices of Γ then determine which of the remaining
Wilson lines are allowed. These can be characterised by their transfo rmation under
Λ w/ Λ r = Z( ˜G), the centre of ˜G.
A similar story plays out for the ’t Hooft lines: for every choice of G = ˜G/ Γ there is
a ’t Hooft line corresponding to the co-root lattice Λ cr ⊂ Λ mw or, equivalently the root
lattice of g⋆. The remaining ’t Hooft lines are characterised by Λ mw/ Λ cr = Z( ˜G) and
their admissibility depends on the choice of Γ.
The upshot of this is that line operators decompose into classes, lab elled by the
(ze, z m) ∈ Z( ˜G) × Z( ˜G)
Furthermore, the line operators form a group; the operator pro duct gives rise to an
addition law while the reversal of orientation provides an inverse. Th ese properties are
enough to ensure that if one member of the class labelled by ( ze, z m) is present in the
theory the the entire class is present.
4
eZ
Z m
eZ
Z m
eZ
Z m
eZ
Z m
Figure 1: The spectrum of line operators for: a) SU (3); b) SU (3)/ Z3 at θ = 0; c) SU (3)/ Z3
at θ = 2π ; d) SU (3)/ Z3 at θ = 4π .
The admissible electric line operators ( ze, 0) are determined by the choice of gauge
group G = ˜G/ Γ, with only those ze which are invariant under Γ present. The magnetic
and dyonic line operators are then restricted by Dirac quantisation . To be speciﬁc,
consider gauge groups with centre Z( ˜G) = ZN . In this case both ze and zm are
integers mod N. Two lines ( ze, z m) and ( z′ e, z ′ m) can both exist as operators only if
zez′ m − zmz′ e = 0 mod N (2.1)
This is the Dirac quantisation condition for non-Abelian lines. The impor tant role
played by the centre of the gauge group in Dirac quantisation was ﬁr st pointed out by
Corrigan and Olive [10].
An Example: SU (N) vs SU (N)/ ZN
For g = su(N), the centre of the group is Z(SU (N)) = ZN . When the gauge group
is G = S(N), all electric line operators are allowed; that is ze = 0 , 1, 2, . . . , N − 1. In
contrast, the magnetic line operators are restricted to lie on the m agnetic root lattice,
meaning that zm = 0. The resulting set of line operators for SU (3) are shown in Figure
1a, plotted in the ( ze, z m) lattice. The ﬁgure shows the charges extended to ze,m ∈ Z;
the key physics can be seen in the grey box, which restricts to ze,m = 0, 1, 2. The lattice
is then formed by tiling this box.
For SU (N)/ ZN , the only purely electric line operators lie on the root lattice. They
have (ze, z m) = (0 , 0). The magnetic line operators are more interesting and there are
several, diﬀerent solutions to the quantisation condition (2.1). The simplest such solu-
tion is to admit the purely magnetic line operators (0 , z m) with zm = 0, 1, 2, . . . N − 1.
No further dyonic operators are then allowed. The resulting spect rum of line operators
for G = SU (3)/ Z3 is shown in Figure 1b.
5
For G = SU (N)/ ZN (but not for all other gauge groups [1]), other solutions to (2.1)
are generated by the theta angle. This arises through the Witten e ﬀect [2] – which
holds for line operators as well as dynamical particles [8, 11] – and en sures that, in the
presence of θ ⁄= 0, purely magnetic line operators turn into dyonic line operators. I n
particular, as θ → θ + 2π, each line operator picks up an electric charge given by
λ e → λ e + λ m ⇒ ze → ze + zm
For the G = SU (N) theory, the set of line operators transforms into itself under
θ → θ + 2π. In contrast, for G = SU (N)/ ZN , the set of line operators turns into
something diﬀerent. This means that the theory with θ = 0 is not the same as the
theory with θ = 2 π. Instead, for G = SU (N)/ ZN , the theta angle takes values in the
range
θ ∈ [0, 2πN )
This extended range of θ is associated to the fact that G = SU (N)/ ZN admits instan-
tons with fractional charge 1 /N . Starting with the set of line operators generated by
(ze, z m) = (0 , 1), under a shift θ → θ + 2πk we have a new theory with line operators
generated by ( ze, z m) = ( k, 1). For G = SU (3)/ Z3, the set of line operators are shown
in Figures 1c and 1d for k = 1 and k = 2 respectively.
How Does the Dynamics Diﬀer?
In four-dimensional Minkowski spacetime, R3,1, the diﬀerence between Yang-Mills with
gauge group SU (N) and SU (N)/ ZN is rather formal. In particular, any local observer
is blind to the distinction. Nonetheless, the diﬀerent line operators m ean that there
are subtle diﬀerences between the two theories. This appears, fo r example, after con-
ﬁnement. In either theory, the conﬁning phase can be viewed as ar ising through the
condensation of magnetic monopoles with charge λ m ∈ Λ mr. For SU (N) Yang-Mills,
these are the minimally charged monopoles. However, for SU (N)/ ZN , these are not
the minimum charge. This means that (at θ = 0) this theory exhibits topological order,
with an emergent magnetic discrete ZN gauge symmetry in the infra-red [1].
The diﬀerence between the two theories takes on a more meaningfu l role when the
theory is compactiﬁed on a space with non-trivial topology, since no w the Wilson line
for the ZN gauge symmetry can get an expectation value, resulting in diﬀerent physics
in the lower dimension. This is perhaps clearest in the N = 1 super Yang-Mills, where
one has more control over the dynamics. When compactiﬁed on a cir cle, or on a higher
dimensional torus, the Witten indices for SU (N) and SU (N)/ ZN diﬀer [12, 13].
6
