---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-013-55-disconnected-reconstruction-and-the-entanglem
section_title: "Disconnected reconstruction and the entanglement wedge"
section_number: 5.5
pages: 28-32
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
Now let’s consider what bulk operators can be constructed on boundary regions with
more than one connected component. First we extend the deﬁnition of the causal wedge
to disconnected regions:
– 26 –
Deﬁnition 6. Suppose that A is a boundary region, which is a union of connected
componentsA1,A 2,... . The causal wedge ofA, denotedC[A], is deﬁned as the union
of the causal wedges of the components of A,C[A] =⋃
iC[Ai].
Since we have already established that any bulk operator in C[Ai] is reconstructable
on Ai if Ai is connected, it follows immediately from this deﬁnition that even for
disconnected regions any bulk operator in C[A] is reconstructable on A.
The causal wedge contains bulk operators which can be reconstructed when we
apply the greedy algorithm to the connected components of A one at a time. But the
greedy algorithm might advance further into the bulk, beyond the causal wedge, when
applied to A instead. Speciﬁcally, there could be a 2 n-index tensor just beyond the
causal wedge of A withn or more legs crossing the union of greedy geodesics γ⋆
Ai∪γ⋆
Aj,
even though fewer than n legs cross γ⋆
Ai or γ⋆
Aj individually. Then applying the greedy
algorithm toAi∪Aj moves the cut past this tensor. This step may then render further
tensors eligible for inclusion, and in fact we will see that sometimes the greedy algorithm
can move far beyond the causal wedge C[A]
Figure 13. Disconnected reconstruction of a central operator beyond the causal wedge. Each
of two separate connected boundary regions is too small for reconstruction of the central
operator, yet the reconstruction is possible on the union of the two regions. In this example
the greedy algorithm reaches the central tensor when applied to both connected components
at once, but not when applied to either component by itself.
A concrete ﬁrst example illustrating reconstruction of a bulk operator outside the
causal wedge is shown in ﬁgure 13. In this example, A is the union of two connected
componentsA1 andA2, and the full operator algebra of the central tensor can be pushed
– 27 –
to eitherAc
1 orAc
2. This implies that no nontrivial operator acting on the central tensor
can be pushed to either A1 or A2. For every nontrivial operator φ in the algebra there
is another operator φ′ which does not commute with φ. If φ′ can be pushed to Ac
1,
then surely φ cannot be pushed to A1, because operators supported on complementary
regions must commute. The same argument applies to A2. Yet the greedy algorithm
applied to A reaches the central tensor, showing that its full operator algebra can be
pushed to the union of A1 and A2.
That operators beyond the causal wedge of A can be reconstructed on A has deep
potential implications for AdS/CFT. Perturbative gravity techniques like the AdS-
Rindler reconstruction can be used to construct bulk operators in the causal wedge
but not beyond. Yet there has been speculation in the literature that reconstruction
should be possible in a larger region, the entanglement wedge [40], see also [41, 42, 67].
In AdS/CFT, the entanglement wedgeE[A] is deﬁned by ﬁrst ﬁnding the minimal area
surface γA used in the RT formula, and then drawing a codimension one ( i.e., two-
dimensional for AdS 3) spatial slice in the bulk whose only boundaries are γA and A.
The bulk domain of dependence of this slice is then deﬁned as the entanglement wedge
E[A]. The entanglement wedge contains the causal wedge, but can be much larger in
some cases. Figure 14 illustrates a simple example highlighting the distinction between
the causal and entanglement wedges. 5
We would like to investigate whether bulk operators in the entanglement wedge
are reconstructable for holographic codes, but how should the entanglement wedge be
deﬁned? A deﬁnition of E[A] close to that used in AdS/CFT is:
Deﬁnition 7. Suppose A is a (not necessarily connected) boundary region. The ge-
ometric entanglement wedge of A is the set of bulk points in the bulk region
bounded byA andγA, whereγA is the minimal bulk geodesic whose boundary matches
the boundary of A. If there is more than one minimal bulk geodesic, γA is chosen to
make the geometric entanglement wedge as large as possible.
The main motivation for the conjecture that operators in the entanglement wedge
are reconstructable in AdS/CFT comes from the validity of the RT formula for discon-
nected regions. (Additional evidence was given in [1] based on a typicality argument.)
But we have already seen above that the RT formula does not hold exactly in holo-
graphic codes, so we should not necessarily expect the entanglement wedge conjecture
5In excited states where the geometry deviates from pure AdS, there are diﬀerences between the
entanglement wedge and the causal wedge even for connected boundary regions. We will not try to
capture this in our toy models, since without a theory of dynamics we cannot capture the full spacetime
deﬁnitions of these regions. Our discussion is limited to the case where we stick with states near the
vacuum, in which case A needs to be disconnected for its causal wedge and entanglement wedge to
diﬀer.
– 28 –
A
A
A
A
Figure 6 . A reconstruction phase transition? As we increase the region A, the extremal-
area codimension two surface of smallest area whose boundary is @A, shown as the solid lines,
changes discontinuously. Does this mean that we can now reconstruct the point in the center
as an operator on A?
operator algebra quantum error correction requires sub-AdS scale bulk locality. This
is a special property of those CFTs that have local holographic duals, which we have
here reformulated in the language of quantum information theory.
4.3 Disconnected regions and quantum secret sharing
So far we have only discussed the erasure of connected regions of the boundary. More
general erasures are also interesting. Consider for example the AdS3 situation depicted
in ﬁgure 6. Here we consider a region A which is the union of two disjoint intervals; in
other words we have erased two disjoint intervals. Can we choose a code subspace where
we can realize the bulk operator in the center as an operator acting on A or A?I f t h e
AdS-Rindler reconstruction is the last word on bulk reconstruction [ 7], then the answer
is clearly no; this point lies neither in WC [A]n o ri n WC [A]. This is possible within
the context of quantum error correction, but only if both A and A can access partial
information about the code subspace. For example, say that A had no information
whatsoever about which state of the code subspace we are in. Then by deﬁnition
(3.12)w o u l dh o l d ,s ow ec o u l dr e c o v e rt h ei n f o r m a t i o nf r o mA. We are not, however,
able to determine whether or not such partial information is really present.
In fact there have been recent conjectures in the literature that this operator can
still be reconstructed in A as long as A is bigger than A; more generally, the claim is that
one can do reconstruction throughout the entanglement wedge, which is deﬁned as the
bulk domain of dependence of any bulk spacelike surface whose boundary is the union
of A and the codimension two extremal-area surface of minimal area whose boundary
is @A [8, 25, 26]. In the ﬁgure, the intersection of the entanglement wedge with a
–2 0–
Figure 14 . The intersection of the entanglement wedge E[A] with a bulk time-slice, in the
case where A has two connected components. Minimal geodesics in the bulk are solid lines.
When A is smaller than Ac, we have the situation on the left and the causal wedge agrees
with the entanglement wedge. When A is bigger, however, the minimal geodesics switch and
the entanglement wedge becomes larger. In particular the point in the center lies in the E[A]
but notC[A].
to hold in detail for the geometric entanglement wedge. Instead, as in deﬁning the
causal wedge, we prefer a deﬁnition that makes the reconstructability manifest:
Deﬁnition 8. Suppose A is a (not necessarily connected) boundary region. The
greedy entanglement wedge of A, denotedE[A], is the set of bulk points reached
by applying the greedy algorithm to all connected components of A simultaneously.
With this deﬁnition, bulk local operators in E[A] are automatically reconstructable in
A, using the isometry deﬁned by PA to push these operators to the boundary. The
greedy algorithm also ensures that the interior boundary ofE[A] is the greedy geodesic
γ⋆
A, though not necessarily the minimal geodesic γA.
A drawback of this deﬁnition is that E[A] includes only the bulk local operators
which can be reconstructed on A using the greedy algorithm; it might miss additional
bulk operators which can be reconstructed by other methods. In fact we can ﬁnd exam-
ples of codes such that some bulk local operators lying outsideE[A] can be reconstructed
onA, as discussed in appendix E. These codes typically have special properties, such as
symmetries, which make the reconstruction possible. If we know nothing more about
the perfect tensors used to construct the code, aside from their perfection, we have no
general reason to expect that bulk operators far outside the greedy entanglement wedge
will be reconstructable. That said, we confess that we lack a complete understanding
of when reconstruction is possible, and hope that further progress on this issue can be
achieved in future work.
– 29 –
