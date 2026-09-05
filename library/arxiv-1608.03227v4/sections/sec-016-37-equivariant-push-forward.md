---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-016-37-equivariant-push-forward
section_title: "Equivariant push-forward"
section_number: 3.7
pages: 20-20
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
whereI = (f1,...,f n) and functions fi form a regular sequence in S andI is h-invariant. LetZ0 = Spec(R).
The Koszul complex K(I) = (Λ •W⊗ C[Z],d K),W = Cn is h-equivariant and has homologies only in degree
0. Let w∈ Rh and W∈ Sh such that W−w∈ I. Let us choose F = (M,D,∂ )∈ MFh(Z0,w ), M = Sk
then we can construct a matrix factorization hj∗(F )∈ MFh(Z,W ) in two steps.
Step 1: We apply method of subsection 3.2 to construct j∗(F ) = ( ˜M, ˜D +dK +d−)∈ MF(Z,W ).
Step 2 : Use lemma 3.5 to construct ∂− such that ˜F := ( ˜M, ˜D +dK +d−,∂ − +∂)∈ MFh(Z,W ). The
elementF is deﬁned up to isomorphism according to lemma 3.6 and we set j∗(F ) := ˜F . To complete our
construction of the functor:
(3.6) j∗ : MF h(Z0,w )→ MFh(Z,W ).
we still need to discuss the action of the functor on the space of mo rphisms and homotopies between the
morphisms and that is done below.
LetF = (M,D,∂ ), ˜F = ( ˜M, ˜D,∂ )∈ MFh(Z0,w ) and ψ is the morphism between F and ˜F in the
category MF h(Z0,w ). Let us constrict F ′ = (M ′,D ′,∂ ′) = j∗(F ) and ˜F ′ = ( ˜M ′, ˜M ′, ˜∂′) = j∗( ˜F ) as above.
The lemma 3.7 implies that we extend it to the morphism Ψ in MF h(Z,W ). Indeed if we choose a extension
˜ψ∈ HomC[Z](M, ˜M ), of ψ then ˜ψ satisﬁes the assumptions of the lemma 3.7 and the lift Ψ = ˜ψ + ∑
i>0 ˜ψi
exists. Moreover the second part of the lemma implies that the lift is u nique up to the homotopy thus we
have the map:
j∗ : Hom MFh(Z0,w)(F, ˜F )→ HomMFh(Z0,w)(F ′, ˜F ′).
Thus completed our construction of the functor of homotopic cat egories (3.6).
