---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY"
section_id: sec-018-41-the-first-explicit-examples
section_title: "The first explicit examples"
section_number: 4.1
pages: 26-27
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
The most easily understood, and constructed, hyperbolic 3-manifolds which are not convex
cocompact arise as covers of closed hyperbolic 3-manifolds which fiber over the circle. Thurston
showed that if ϕ :S→S is a pseudo-Anosov homeomorphim then its mapping torus
Mϕ =S× [0, 1]/(x, 0)∼ (ϕ(x), 1)
is homeomorphic to a hyperbolic 3-manifold Nϕ. Since Nϕ is closed, it is itself a convex co-
compact hyperbolic 3-manifold. (We recall that ϕ is pseudo-Anosov if whenever C is a simple
closed curve on S, then ϕn(C) is not homotopic to C for any n> 0.)
IfNϕ = H3/Γϕ, then Λ(Γϕ) =∂H3 (since if Λ(Γ)̸=∂H3, one may easily check, using the fact
that C(NΓ)̸=NΓ and our analysis of the complement of the convex core, that NΓ has infinite
volume).
Let Γ 0
ϕ⊂ Γϕ denote the normal subgroup of Γ ϕ associated to the subgroup π1(S×{ 1
2)⊂
π1(Mϕ). Since Γ 0
ϕ is normal in Γϕ, Λ(Γ0
ϕ) is a closed Γϕ invariant subset of ∂H3, Therefore,
Λ(Γϕ)⊂ Λ(Γ0
ϕ)
so Λ(Γ0
ϕ) =∂H3.
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS 27
Let N 0
ϕ = H3/Γ0
ϕ be the regular infinite cyclic cover of Nϕ. Since Λ(Γ 0
ϕ) = ∂H3, we see
that C(N 0
ϕ) = N 0
ϕ, so N 0
ϕ is not convex cocompact (since N 0
ϕ has infinite volume). One may
constructN 0
ϕ explicitly by cutting Nϕ along an embedded surface in the homotopy class of the
fiber to obtain a “lego block” L which is homeomorphic to S× [0, 1]. One then constructs N 0
ϕ
from infinitely many lego blocks by gluing the top boundary of thenth lego block to the bottom
boundary of the (n + 1)st lego block (by an isometry in the homotopy class of ϕ). The group
⟨C⟩ of covering transformations of the cover N 0
ϕ→Nϕ then acts by translation (twisted by ϕ)
in the collection of lego blocks.
This picture gives us a coarse understanding of the geometry of N 0
ϕ. One initially surprising
fact is that the volume of r-balls inN 0
ϕ grows linearly inr. There is, possibly apocryphal, story
that when Thurston was first asked which 3-manifolds could be hyperbolic, he guessed that
3-manifolds fibering over the circle could not be, based on this consequence.
We will focus on two features of this example. First, if we take a simple closed curve α on
S and consider its associated geodesic α∗ of α, we see that ϕn(α)∗ = Cn(α∗) for all n∈ Z.
This implies that the sequence of geodesics {Cn(α∗)}n∈ N is a sequence of geodesics exiting
the “‘upward-pointing end” of N 0
ϕ each of which is homotopic to a simple closed curve on S.
Similarly,{C−n(α∗)}n∈ N is a sequence of geodesics exiting the “downward-pointing end” of
N 0
ϕ each of which is homotopic to a simple closed curve on S.
Second, let Y be a minimal surface in Nϕ in the homotopy class of the fiber. One key fact is
that in its intrinsic metric, Y has curvature bounded above by −1. Then, the pre-image of Y
is an infinite family {Yn}n∈Z of minimal surfaces in N 0
ϕ so that Yn =Cn(Y0) for all n∈ Z. So
{Yn}n∈N is an infinite family of surface whose intrinsic curvature is bounded above by−1, each
of which is in the homotopy class of S×{ 0}, which exits the upward-pointing end of N 0
ϕ.
Historical Remarks: The majority of Thurston’s proof of his hyperbolization theorem for closed
3-manifolds which fibre over the circle is contained in his preprint [77]. A complete proof, using
the technology of R-trees in place of Thurston’s use of pleated surfaces, is given by Otal [66].
The first explicit example was discovered by Jørgensen [42] and is the cover of a finite volume
hyperbolic 3-manifold fibering over the circle associated to the fibre subgroup (which was a
punctured torus in his case). Greenberg [37] was the first to abstractly show the existence of
hyperbolic 3-manifolds with finitely generated fundamental group which are not geometrically
finite.
