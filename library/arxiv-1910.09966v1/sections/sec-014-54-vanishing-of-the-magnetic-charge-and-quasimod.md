---
doc_id: arxiv-1910.09966v1
doc_title: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics"
section_id: sec-014-54-vanishing-of-the-magnetic-charge-and-quasimod
section_title: "Vanishing of the Magnetic Charge and Quasimodularity"
section_number: 5.4
pages: 26-29
source_pdf: 1910.09966v1.pdf
source_sha256: 21798500c98ed25a
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
---
ity
One may wonder whether there is no magnetic charge anymore. Our argument
is only partially satisfying because there are many incompressible surfaces inside
of a hyperbolic knot complement serving as representatives for magnetic charges.
Therefore, we need a stronger argument why the symmetry between electric and
magnetic charge is broken. As explained above, the Dehn twists of the boundary
torus are the generators of the mapping class (or isotopy) group. According to
Atiyah [63], the framing can be used to deﬁne a central extension ˆΓ
1→ Z→ ˆΓ→ Γ→ 1
26
of the mapping class group Γ so that there is a section s : Γ → ˆΓ inducing
a splitting of the sequence above. This section deﬁnes a canonical 2-cocycle
c for the central extension that is given by the signature of the corresponding
4-manifold (see [63] for the details). However, in case of the torus, for the
group Γ = SL(2, Z), there is no non-zero homomorphism Γ → Z and so the
splitting s1 : Γ → ˆΓ is unique. Therefore, the canonical section s is not a
homomorphism and the framing (used in the deﬁnition of this section) leads
to a breaking of the modular invariance i.e., the invariance w.r.t. Γ. This fact
is simply expressed by considering the diﬀerence of the two sections s(γ) and
s1(γ) for γ∈ Γ, which is given by the logarithm of the Dedekind η−function,
related to quasimodular functions. Thus, our deﬁnition of the electric charge
breaks explicitly the electro-magnetic duality and we get a vanishing magnetic
charge.
6 Drinfeld–Turaev Quantization and Quantum
States
In [66, 67], we discussed the appearance of quantum states from knots known
as Turaev–Drinfeld quantization. The idea for the following construction can
be simply expressed. We start with two 3-manifolds and consider a cobor-
dism between them. This cobordism is a 4-manifold with a branched cover-
ing branched over a surface with self-intersections. Here, it is enough to re-
strict to a special class of these surfaces, so-called ribbon surfaces (see [68]).
The 3-manifolds are chosen to be hyperbolic knot complements, denoted by
Y1,Y 2. A hyperbolic structure is deﬁned by a homomorphismπ1(Yi)→SL(2, C)
(∈Hom(π1(Yi),SL (2, C))) up to conjugation. Now, we extend this structure to
the entire cobordism, denoted by Cob(Y1,Y 2). The branching set of Cob(Y1,Y 2)
is a surface S with non-trivial fundamental group π1(S). This surface can be
changed without any change of Cob(Y1,Y 2). One change can be described as
crossing change. Now, we have all ingredients for the Drinfeld–Turaev quanti-
zation:
• The surface S (branching set of Cob(Y1,Y 2)) is inducing a representation
π1(S)→SL(2, C).
• The space of all representationsX(S,SL (2, C)) =Hom(π1(S),SL (2, C))/SL(2, C)
has a natural Poisson structure (induced by the bilinear on the group) and
the Poisson algebra (X(S,SL (2, C),{} ) of complex functions over them
is the algebra of observables.
• The Skein module K−1(S× [0, 1]) (i.e., t =−1) has the structure of an
algebra isomorphic to the Poisson algebra (X(S,SL (2, C)),{} ). (see also
[69, 70]).
• The skein algebra Kt(S× [0, 1]) is the quantization of the Poisson algebra
(X(S,SL (2, C)),{} ) with the deformation parameter t = exp(h/4) (see
also [69]) .
27
Figure 9: Crossings L∞,Lo,Loo.
To understand these statements, we have to introduce the skein module
Kt(M) of a 3-manifold M (see [71]). For that purpose, we consider the set of
linksL(M) in M up to isotopy and construct the vector space CL(M) with
basisL(M). Then, one can deﬁne CL[[t]] as ring of formal polynomials having
coeﬃcients in CL(M). Now, we consider the link diagram of a link, i.e., the
projection of the link to the R2 having the crossings in mind. Choose a disk
in R2 so that one crossing is inside this disk. If the three links diﬀer by the
three crossings Loo,Lo,L∞ (see ﬁgure 9) inside of the disk, then these links are
skein related. Then, in CL[[t]], one writes the skein relation L∞−tLo−t−1Loo
which depends only on the group SL(2, C), . Furthermore, let L⊔O be the
disjoint union of the link with a circle. Then, one writes the framing relation
L⊔O + (t2 +t−2)L. Let S(M) be the smallest submodule of CL[[t]] containing
both relations. Then, we deﬁne the Kauﬀman bracket skein module byKt(M) =
CL[[t]]/S(M). The modiﬁcation of S by using the skein relations is one of the
allowed changes of the branching set to keep Cob(Y1,Y 2).
Now, we list the following general results about this module:
• The module K−1(M) for t =−1 is a commutative algebra.
• LetS be a surface. Then, Kt(S×[0, 1]) carries the structure of an algebra.
The algebra structure of Kt(S× [0, 1]) can be simply seen by using the
diﬀeomorphism between the sum S× [0, 1]∪SS× [0, 1] along S and S× [0, 1].
Then, the product ab of two elements a,b ∈ Kt(S× [0, 1]) is a link in S×
[0, 1]∪S S× [0, 1] corresponding to a link in S× [0, 1] via the diﬀeomorphism.
The algebra Kt(S× [0, 1]) is in general non-commutative for t⁄=−1. For the
following, we will omit the interval [0, 1] and denote the skein algebra byKt(S).
As shown in [72, 66, 23], the skein algebra serves as the observable algebra of
a quantum ﬁeld theory. For this approach via branched coverings, the branching
sets of knot complements (representing the fermions) are special braids (6-plats,
see above). Any diﬀerent braid is a diﬀerent state or better than a diﬀerent
quantum state but not a diﬀerent particle. As explained above, the charge
28
spectrum is enough to describe one generation of particles (two leptons, two
quarks). The appearance of diﬀerent generations will be discussed below.
