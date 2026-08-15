---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY"
section_id: sec-010-21-basic-definitions
section_title: "Basic Definitions"
section_number: 2.1
pages: 16-17
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS RICHARD D. CANARY — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
Throughout the lecture course, M will denote a compact, oriented, irreducible 3-manifold,
possibly with boundary, with infinite fundamental group. A 3-manifold M is said to be irre-
ducible if every embedded 2-sphere in M bounds a 3-ball in M. These assumptions guarantee
that the universal cover ofM is contractible. We will often be considering the simple case where
M =S×[0, 1] andS is a closed surface. Moreover,S will always denote a closed oriented surface
in these notes.
Ifρ :π1(M)→ PSL(2,C ) is a discrete, faithful representation, thenρ(π1(M)) then we obtain
a hyperbolic 3-manifold
Nρ = H3/ρ(π1(S)).
Since M and Nρ both have contractible universal cover and ρ gives an identification of the
fundamental groups of M and Nρ, we obtain a homotopy equivalence
hρ :M→Nρ
so that (hρ)∗ : π1(M)→ π1(Nρ) = ρ(π1(M)) is conjugate to ρ. We think of hρ as a marking
of a hyperbolic 3-manifold (much as in the setting of Teichm ¨uller space) and think of the pair
(Mρ,hρ) as a marked hyperbolic 3-manifold.
Let gAH(M)⊂ Hom(π1(M), PSL(2, C) denote the space of discrete faithful representations
of π1(M) into PSL(2, C) and let AH(M) be its image in the quotient character variety
X(M) = Hom(π1(M), PSL(2, C)//PSL(2, C).
(The double back-slash indicates that we are taking the geometric invariant theory quotient
which givesX(M) the structure of the variety. We will not need to worry about this construction
but there is an open neighborhood of the set of discrete faithful representation on which the
quotient is simply the usual quotient and the image of the neighborhood lies in the smooth
part of the character variety.) In analogy with Teichm ¨uller space, we may think of this as the
space of marked hyperbolic 3-manifolds homotopy equivalent toM (up to orientation-preserving
isometry).
It is a classical consequence of the Margulis lemma that AH(M) is a closed subset of X(M).
When AH(M) is not a single point, it will not be an open subset of X(M).
Theorem 2.1. If M is a compact 3-manifold whose fundamental group is not virtually abelian,
then AH(M) is a closed (possibly empty) subset of X(M).
Exercise: Show that if H2 is a handlebody of genus two, then AH(H2) is not open in X(M).
Hint: It suffices to consider representations into PSL(2, R).
A discrete, faithful representation ρ : π1(M)→ PSL(2, C) is said to be convex cocompact
if ρ(π1(M) is convex cocompact. Let CC (M) be the set of convex cocompact representations
in AH(M). Moreover, a discrete, faithful representation ρ : π1(M)→ PSL(2, C) is said to
be a convex cocompact uniformization of M if hρ : M→ Nρ is homotopic to an orientation-
preserving homeomorphism jρ : M→ C1(Nρ). Let CC0(M) be the set of convex cocompact
uniformizations of M in AH(M).
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS 17
Thurston completely characterized which manifolds with boundary have convex cocompact
uniformizations.
Thurston’s Hyperbolization Theorem (special case): IfM is an irreducible, compact 3-manifold
with non-empty boundary and π1(M) is infinite and does not contain a subgroup isomorphic to
Z⊕ Z, then M admits a convex cocompact uniformization.
The best source for Thurston’s original proof of his hyperbolization theorem is the article of
Morgan [61], although portions of Thurston’s proof appear in his papers [74, 78]. Otal [65] and
Kapovich [43] discuss other proofs of his theorem.
