---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-022-the-open-closed-2d-tqft-from-a-calabi-yau-manifo
section_title: "The open-closed 2d TQFT from a Calabi-Yau manifold."
section_number: null
pages: 28-29
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
Associated to a Calabi-Yau manifold X there are two standard 2d TQFTs
coming from string theory, imaginatively named the A-model and the B-
model: it is the B-model we will be interested in here. In the B -model the
boundary conditions are supposed to be “generated” by compl ex submani-
folds of X so the boundary conditions are taken to be complexes of coher ent
sheaves on X; the open string category is then supposed to be the derived
category of coherent sheaves on X. This is indeed a Calabi-Yau category,
which is why such categories are so named: for each E and F , the requi-
site pairing Hom•
D(X)(E , F ) ⊗ Hom•
D(X)(F , E )→ k[− dim X] comes from the
Serre pairing as a Calabi-Yau manifold is precisely a manifo ld with a trivial
canonical bundle.
According to the physics, the closed string state space C should be
Hom•
D(X×X)(O∆ , O∆ ), in other words, the Hochschild cohomology algebra
HH•(X). As X is Calabi-Yau, a trivialization of the canonical bundle ind uces
an isomorphism between Hochschild cohomology and Hochschi ld homology,
up to a shift. This means that the closed string space C has both the coho-
mological product and the Mukai pairing, and these make C into a Frobenius
algebra.
We need to specify the algebra maps iE : C→ OE E . These are maps
iE : Hom•(O∆ , O∆ )→ Hom•(E , E )
28
which can be given by interpreting E as a kernel pt→ X and taking iE to
be convolution with the identity on E . This is given diagrammatically on
an element ϕ ∈ Hom•(O∆ , O∆ ) as follows.
ϕ ↦→
E
ϕ 
X pt
.
At this point it should be noted that C is to be thought of as the centre
of the category O. The notion of centre is generalized from algebras to cat-
egories by taking the centre of a category to be the natural tr ansformations
of the identity functor; however, in a 2-category an appropr iate notion of
the centre of an object is the set of 2-endomorphisms of the id entity mor-
phism on that object. This means that C is the centre, in this sense, of the
category O in the 2-category V ar.
The map going the other way, iE : Hom•(E , E )→ Hom•(O∆ , O∆ ) is given
by taking the trace, namely for e ∈ HomD(X)(E , E ) the map is given by
E
e
X pt
↦→ pteX
E
.
This deﬁnition relies on the fact that X is Calabi-Yau, so that the Serre
kernel is, up to a shift, just the identity 1-morphism IdX.
An argument similar to Proposition 11 shows that iE and iE are adjoint.
In order to argue that we indeed have an open-closed TQFT it re mains to
show that the Cardy Condition holds. In fact, we will prove a m ore general
