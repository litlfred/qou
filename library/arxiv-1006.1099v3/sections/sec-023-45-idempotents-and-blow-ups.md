---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-023-45-idempotents-and-blow-ups
section_title: "Idempotents and blow-ups"
section_number: 4.5
pages: 41-49
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
pencil of hypersurface sections with smooth base locus B = H0∩H1 ⊂ X. For simplicity,
we suppose π1(B) = 0. We also ﬁx an additional “reference” hyperplane section Href linearly
equivalent to the Hi but not in the pencil deﬁning B, so there is an associated net of hyperplanes
⟨H0,H 1,H ref⟩. We denote by b : Y → X the blow-up Y = BlB(X) along the base locus, and
by E⊂ Y the exceptional divisor; note that E∼= B× P1 canonically, since the normal bundle
νB/X∼=L⊗ C2 for the line bundle L =νHi/X . We assume:
• X,B and Y are all monotone (Fano); c1(X) = (d + 2)H with d≥ 2;
• c1(L|B) is proportional to c1(B); B has even minimal Chern number ≥ 2;
• B contains a Lagrangian sphere .
(4.10)
The ﬁrst assumption determines the size λ of the blow-up parameter, i.e. the area of the ruling
curve P1⊂E. We actually strengthen the ﬁrst assumption, and demand that
• c1(Y )− PD[E] = b∗c1(X)− 2PD[E] is ample, so contains K¨ ahler forms; (4.11)
note that this implies there are K¨ ahler forms on Y which give the ruling curves P1⊂E twice the
area they have for the monotone form. Recall our notation ( •,ω )− for the symplectic manifold
(•,−ω). As in (4.7), we consider the two correspondences
Γ R =B×S1
eq ⊂ B−× (B× P1)
where S1
eq⊂ P1 denotes the equator and
Γ E =UνE ⊂ E−×Y
42 IV AN SMITH
where νE → E is the normal bundle to E in Y and UνE denotes a circle sub-bundle. The
correspondences are equipped with bounding Spin structures. As in Lemma 4.21, by choosing
the radius of this subbundle and the symplectic forms appropriately :
Lemma 4.27. Under hypothesis (4.11), the correspondences Γ E and Γ R can be chosen to be
embedded monotone Lagrangian submanifolds, with embedded monotone composition Γ = Γ R◦
Γ E⊂B−×Y .
Proof. Let H⊂Z be a codimension 2 symplectic submanifold of a symplectic manifold ( Z,ω Z ),
with the symplectic form ωH = (ωZ )|H . Equip the normal bundle ν→ H with a Hermitian
metric. The symplectic form on a neighbourhood of the zero-sectio n in the total space of ν is
Ω ν =π∗ωH + 1
2d(r2α) (4.12)
wherer is the radial co-ordinate and α is a connection form for the bundle satisfying dα =−π∗τ ,
with τ a curvature 2-form on H with [τ ] = [ c1(ν)] as obtained from Chern-Weil theory. Note
that the form Ω ν is a standard area form on the ﬁbres of the disk bundle. The symplec tic form
induced on the reduced space Hred of the co-isotropic submanifold which is the boundary of the
radiusr disk bundle in ν diﬀers from ωH by subtracting r2τ/ 2. In particular, when it is possible
to take r =
√
2, the reduced form lies in the cohomology class [ ωH−c1(ν)], compare to Lemma
4.21.
The symplectic normal bundle to B× P1∼= E⊂ Y is the tensor product π∗
BL⊗ π∗
P1O(−1),
with ﬁrst Chern class ( c1(L),−1)∈H 2(B)⊕H 2(P1). We ﬁx a tensor product Hermitian metric
and connexion, taking τ to be a product 2-form. The ruling P1⊂E has area 1 for a monotone
K¨ ahler formωmon on Y which is cohomologous to the ﬁrst Chern class. By hypothesis, we ha ve
K¨ ahler formsω onY for which the area of P1 is> 2. After normalising the K¨ ahler form near E,
one can blow down to obtain a symplectic form on X which contains a radius
√
2 +δ disk bundle
around the base locus B; compare to [66, Lemma 7.11] or [43, Theorem 2.3]. If we now blow
up again by amount 1, the exceptional divisor E⊂ (Y,ω mon) naturally lies inside a standard
symplectic disk bundle whose ﬁbres have area 1 + δ. This is suﬃciently large to contain an
embedded circle bundle UνE in which the circles bound ﬁbre disks of area 1. (Blowing down and
up in this way eﬀects a symplectic inﬂation. Indeed, when Gompf puts symplectic structures
on Lefschetz pencils in general dimension, he precisely patches in a large symplectic disk bundle
over the base locus [43, p.279, and his embedding ϕ onto a disk bundle of radius R].)
From (4.12), the reduced space of the co-isotropic UνE has symplectic form ( ωY )|E−τ in
cohomology class
[ωY ]|E− [(c1(L),−1)]. (4.13)
We can view Y ⊂X× P1 as a divisor in class ( c1(L), 1). It follows that the monotone form ωY
lies in cohomology class (c1(X)−c1(L), 1)∈image
(
H 2(X)⊕H 2(P1)→H 2(Y )
)
(the latter map
being an isomorphism by the Lefschetz theorem in our examples). Co mbining this with (4.13)
and noting that c1(B) = c1(X)|B− 2c1(L), by adjunction, shows that the reduced symplectic
form on B× P1 coming from the co-isotropic UνE is monotone.
We have arranged that the coisotropic deﬁning the Lagrangian cor respondence Γ E lives inside
the blow-upBlB(νB/X ) = Tot O(−1)(E) of a large disk normal bundle to B inX. By construction,
all Maslov index 2 disks in this open subset have the same area, compa re to Lemma 4.19. Since
H1(B) = 0, these local disks together with rational curves in the total s pace span H2(E×Y, Γ E),
hence are suﬃcient to detect monotonicity. It follows that Γ E is monotone. The corresponding
statement for Γ R is trivial, taking the monotone forms on B andB×P1; and monotonicity is then
inherited by the Lagrangian composition (note this is well-deﬁned sinc e the symplectic forms on
B× P1 arising as the output of Γ R and the input of Γ E do co-incide). □
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 43
Remark 4.28. We emphasise that there are two diﬀerent symplectic forms on B× P1 in play;
ﬁrst, the non-monotone form arising by restricting a monotone fo rm on Y to E⊂ Y ; second,
the monotone form arising from co-isotropic reduction of the boun dary of a suitable disk bundle
νE⊂Y . We only use the Fukaya category of the monotone form; as a mild ab use of notation, we
will continue to write E for the space B× P1 even though it is not equipped with the symplectic
form it inherits from the embedding in the ambient space Y .
Remark 4.29. For the case of interest in this paper, namely (2 , 2)-intersections in P2g+1 with
g≥ 2, the ampleness hypothesis (4.11) holds by Lemma 4.4. When g = 1, this conditions fails;
the class c1(P3)− 2PD[E] lies on the boundary of the K¨ ahler cone of the blow-up of P3 along a
complete intersection elliptic curve. In that case, there is no monot one correspondence, which
ﬁts with the fact that the elliptic curve has no balanced Fukaya cate gory and F(Σ 1) is naturally
deﬁned over Λ C.
Remark 4.30. There is another viewpoint on the composite correspondence Γ = Γ R◦ Γ E which
is often useful. Again starting from a K¨ ahler form on Y which is standard in a large disk bundle
over E, we perform a symplectic cut [61] along the boundary of a sub-disk b undle. Algebro-
geometrically, symplectic cutting is eﬀected by deformation to the n ormal cone [40, Chapter
5]. We obtain a space with two components meeting along a divisor. One component is a F1-
bundle over B, given by projective completion of the normal bundle to E, and the other Y ′ is
holomorphically isomorphic to Y , but equipped with a diﬀerent K¨ ahler form (of smaller volume).
The hypothesis (4.11) implies that one can perform the cut so as to o btain a K¨ ahler form which
is monotone on the total space of the F1-bundle. The associated monotone P2-bundle over B is
the completion P(L⊕L⊕O ) of its normal bundle. Being the projectivisation of a direct sum
of line bundles, the structure group reduces to a maximal torus T 2≤ PGL 3(C), which implies
that there is a (cohomologous) linear K¨ ahler form on the P2-bundle for which parallel transport
preserves the ﬁbrewise Lagrangian torus which is the monotone to rus in P2. Globally, this gives
rise to a Lagrangian submanifold
Γ cut =T 2 ˜×B ⊂ P(L⊗2⊕O )×B (4.14)
which is a monotone 2-torus bundle over the diagonal ∆ B. If one now blows back up and moreover
smooths the normal crossing locus of the symplectic cut, in each ca se deforming the symplectic
form in a region disjoint from Γ cut, one obtains a Lagrangian correspondence Γ cut⊂ B×Y ,
which is exactly Γ.
As remarked above, Γ = T 2 ~×B is a 2-torus bundle, which in general is diﬀerentiably non-
trivial. However, given any simply-connected Lagrangian L⊂B, the restriction of the correspon-
dence to L is trivial (because the symplectic line bundle L→ L is ﬂat and hence trivial), and the
geometric composition of L with the correspondence is a Lagrangian submanifold diﬀeomorphic
to a product L×T 2⊂Y .
The quilted Floer theory of Mau, Wehrheim and Woodward, Theorem 3 .10 of Section 3.4,
associates to a monotone Lagrangian submanifold Γ ⊂ M −×N a Z2-graded A∞-functor Φ Γ :
F(M )→ F#(N ), where F#(•) is the A∞-category of generalised Lagrangian correspondences.
Theorem 3.14 implies that the functors Φ Γ R◦ Φ Γ E and Φ Γ R◦Γ E are quasi-isomorphic.
Lemma 4.31. The functor Φ Γ R◦Γ E is quasi-isomorphic to a functor with image in the fully
faithfully embedded A∞-subcategory F(Y )⊂ F#(Y ).
Sketch. Write Γ = Γ R◦ Γ E ⊂ B−×Y . For every object L∈ F(B) the image of L under Γ
is a smooth Lagrangian submanifold ˆL in Y . Quilt theory, via Theorem 3.14, again provides a
quasi-isomorphism of functors F(pt)→ F#(Y ) with images ˆL and Φ Γ (L); the quasi-isomorphism
44 IV AN SMITH
of functors implies that the target objects
ˆL
∼
−→ {pt
L
−→B
Γ
−→Y} = Φ Γ (L)
are quasi-isomorphic objects of F#(Y ), and in particular HF ( ˆL, Φ Γ (L))∼= HF ( ˆL, ˆL). More
explicitly, the Floer chain group
CF ( ˆL,{pt
L
→B
Γ
→Y}) = CF ( ˆL× Γ −, ∆ ×L)
where the RHS is computed in Y ×Y −×B. These Lagrangian submanifolds meet cleanly,
and projection to the ﬁrst factor identiﬁes the clean intersection locus with ˆL. A chain-level
representative e∈ CF ( ˆL× Γ −, ∆ ×L) = C∗( ˆL) for the identity 1 ∈ HF ( ˆL, ˆL) provides the
desired quasi-isomorphism. Similarly,
CF (pt
L0
→B
Γ
→Y, pt
L1
→B
Γ
→Y )
is given by chains on the intersection locus (Γ × Γ −)∩ (L−
0× ∆ Y×L1)⊂B−×Y×Y −×B, and
this clean intersection is exactly ˆL0∩L1 = ˆL0∩ ˆL1. Projection to the central two factors Y×Y −
again identiﬁes the Floer chain group with CF ( ˆL0, ˆL1). The subcategories of F#(Y ) generated
by the ˆL-images and the corresponding generalised Lagrangian branes are quasi-equivalent, and
the former lies inside F(Y ). □
We will henceforth replace Φ Γ by such a quasi-isomorphic functor to F(Y ), without however
changing our notation. We would like this composite correspondence Γ to behave like a sheaf of
Cliﬀord algebras over B. One can ﬁlter the Floer complex for T 2 ˜×B by projecting generators
down to critical points of a Morse function on B and ﬁltering by Morse degree. This yields a
spectral sequence of rings
E∗,∗
2 =H ∗(B;HF (T 2,T 2))∼=H ∗(B)⊗Cl 2 ⇒ HF (T 2 ˜×B,T 2 ˜×B)
In the simplest case, the spectral sequence degenerates, the n on-trivial idempotents in the Clif-
ford algebra survive to E∞, and they split the total correspondence, as in Remark 4.24. This w as
trivially the situation in the example considered in Lemma 4.19, where B ={pt}. In general,
the picture is less clear: even additively the Floer cohomology of the c omposite correspondence
is more complicated, coming from the non-triviality of the normal bun dleL of the original hy-
perplanes Hi⊂X. However, this complication becomes irrelevant on the appropriate summand
of the Fukaya category of the base locus.
Lemma 4.32. SupposeL∈ F(B; 0), and let Γ L denote its image under the correspondence Γ =
Γ R◦ Γ E. Either HF (Γ L, Γ L) = 0 for all L∈ F(B; 0), or there is an isomorphism HF (Γ L, Γ L)∼=
HF (L,L )⊗Cl 2 of QH ∗(B; 0)-modules.
Proof. We work with the monotone symplectic forms provided by Lemma 4.27. The Floer coho-
mology of L×S1
eq⊂B−× P1 can be computed using the K¨ unneth theorem, since all holomorphic
curves split in the obvious product description, as does their defor mation theory. One therefore
gets
HF (L×S1
eq,L×S1
eq) ∼= HF (L,L )⊗HF (S1
eq,S 1
eq).
By the K¨ unneth theorem in quantum cohomology, QH ∗(E)∼= QH ∗(B)⊗QH ∗(P1). We next
apply the quantum Gysin sequence, in the form of Theorem 3.3, or ra ther its Lagrangian analogue.
This says that HF (Γ L, Γ L) is the cone on quantum cup-product on HF (L×S1
eq,L×S1
eq) by the
corrected Euler class e +σ· 1, where σ∈ K counts Maslov index 2 disks through a global angular
chain for UνE . In our case, writing t∈QH 2(P1) for the fundamental class,
e =h⊗ 1 + 1⊗ (−t)
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 45
where h = c1(L|B)∈ H 2(B) is the restriction of c1(νH/X ). Recall that our initial assumptions
imply this is proportional to c1(B). We should therefore compute quantum product by
h⊗ 1 + (1⊗ (σ· 1−t)) : HF (L,L )⊗HF (S1
eq,S 1
eq)→HF (L,L )⊗HF (S1
eq,S 1
eq).
Now for L in the nilpotent summand F(B; 0),h↦→0∈HF (L,L ) by Lemma 3.1, and the above
therefore simpliﬁes to the map
x⊗y↦→x⊗ (σ1−t)y
which has cone HF (L,L )⊗Cone(σ1−t). If σ⁄= 1 then the map is id ⊗ (invertible) and hence
HF (Γ L, Γ L) = 0, so Γ L is quasi-isomorphic to zero for every L. If σ = 1 this map vanishes and
thenHF (Γ L, Γ L)∼=HF (L,L )⊗Cl 2. Since the quantum Gysin sequence is an exact sequence of
QH ∗-modules, the statement on the module structure follows. □
The force of Lemma 4.32 is that to obtain a conclusion for an arbitrar yL∈ F(B; 0), it suﬃces
to ﬁnd a single such L for which HF (Γ L, Γ L)⁄= 0. We now aim to prove this non-vanishing when
L is a Lagrangian sphere as provided by hypothesis (4.10). Let U⊂L ⊕2→ B denote an open
neighbourhood of B⊂X, symplectomorphic to a sub-disk bundle of the normal bundle. Write
Ltaut for a symplectic disk bundle neighbourhood of E⊂ Y inside its normal bundle, which is
just the tautological bundle over E = P(L⊕2). Since π2(B×Y, Γ) = π2(B×BlB(U), Γ), all
possible homotopy classes of holomorphic disk with boundary on Γ are visible in B×BlB(U).
Lemma 4.33. If for some Lagrangian sphere L⊂ B all holomorphic disks of Maslov index 2
with boundary on Γ L lie inside a disk bundle Ltaut→E, then Γ L⁄≃0.
Proof. We continue to write Γ = Γ R◦ Γ E. There is a canonical projection
p :B×BlB(U) −→ B×B (4.15)
under which Γ ↦→∆ B. Any Lagrangian sphere L⊂ B necessarily lies in F(B; 0) since B has
minimal Chern number≥ 2. Disks with non-constant image in B×B under the map of Equation
4.15 have Maslov number at least 4. Therefore the only Maslov index 2 disks with boundary on
Γ E(L×S1
eq) lie in homotopy classes which project trivially to B×B, and thus lie in Bl0(C2)-ﬁbres
of the projection p, with boundary on T 2-ﬁbres of Γ ∼=T 2 ˜×B. All such disks are therefore visible
in the model of Lemma 4.19, and in that case we know σ = 1 since we know a priori that the
Floer cohomology of the torus T was non-vanishing. (In the model one can check explicitly that
only one of the three holomorphic disks through the generic point of T has boundary passing
through a global angular chain for the unit circle ﬁbration of O(−1)→ P1.) □
Since Y = BlB(X) is the blow-up of a base locus of a pencil of hyperplanes {Ht}, it has
a natural ﬁbration structure π : Y → P1, with ﬁbre homologous to π∗H−E. We choose a
holomorphic volume form Ω on Y which has poles along the reducible divisor
DΩ = E + [π−1(0)] + [π−1(∞)] +dHref (4.16)
where we recall c1(X) = (d + 2)H. For suitable choices of ﬁbres H0 =π−1(0) and H∞ =π−1(∞)
we have L×T 2⊂Y\DΩ . Remark 4.20 implies that L×T 2 can be graded with respect to Ω.
Lemma 4.34. Suppose dimC(B)> 1. Then Maslov index 2 disks with boundary on L×T 2 meet
exactly one of E, H0 and H∞ once, and are disjoint from Href . In particular, no such Maslov
index 2 disk can project onto P1 under π.
Proof. Since dimC(B) > 1, the Lagrangian sphere L is simply connected, which implies that
H2(B)→H2(B,L ) is surjective. One can therefore assume that the Maslov index fo r holomorphic
disks in B with boundary on L is given by intersection number with dHref∩B. The choice of
holomorphic volume form then implies that Maslov index of disks with bou ndary on L×T 2 is
given by their intersection number with DΩ . The result follows. □
46 IV AN SMITH
Example 4.35. (Auroux) The hypothesis on dim( B) plays a deﬁnite role. Take a pencil of linear
hyperplanes in P3 with base locus P1 and blow that up. This may be done torically, and we
obtain a toric variety whose moment map is a truncated tetrahedro n. The Lagrangian L×T 2 is
just the monotone torus T 3 which is the central ﬁbre of that moment map, and it bounds one
family of Maslov index 2 disks for each facet of the moment polytope, in particular it bounds 5
families, not all of which miss the reference hyperplane Href if this is taken to be one face of the
tetrahedron.
This is because the original Lagrangian L⊂B is an equatorial S1⊂ P1, in particular it bounds
Maslov index 2 disks. The natural map H2(B)→H2(B,L ) is not surjective; although the ﬁrst
Chern class “contains” Href with multiplicity d = 2, the actual toric divisor which naturally
represents it does not contain Href with multiplicity 2, but rather Href and another homologous
component.
Away from B∩Href , the original net of hyperplanes on X deﬁnes a map to P2. Blowing up
along B, one obtains a map φ from Y\(E∩Href ) to the ﬁrst Hirzebruch surface F1. Then
(1) the projection map π is the composite Y\(E∩Href )
φ
−→ F1→ P1, with the second map
the natural projection;
(2) the proper transforms of H0 and H∞ lie over the ﬁbres of F1 over 0,∞∈ P1;
(3) the divisors E andHref (minus their common intersection) live over the −1 respectively
+1 section of F1.
This is pictured schematically in Figure 5, via the usual moment map imag e for F1. The ﬁbre
over the centre of gravity • is a monotone Lagrangian torus T⊂ F1.
Figure 5. The moment polytope for F1 and associated divisors
Lemma 4.36. Assuming that dimC(B) > 1 and that the hypotheses (4.10, 4.11) hold, then
Γ L⁄= 0 for a Lagrangian sphere L⊂B.
Proof. The proof uses a degeneration argument modelled on deformation t o the normal cone;
compare to [95, Section 5]. We symplectically blow up Y× C along E×{ 0}; the resulting space
W has an obvious projection p to C, which we take to be holomorphic. The zero-ﬁbre has two
components, one of which C0 is diﬀeomorphic to E but with a K¨ ahler form of smaller volume
(shifted in cohomology class by a real multiple of the divisor E), and the other of which C1 is
the projective completion of the normal bundle to E, hence is the total space of an F1-bundle
overB. We can arrange that:
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 47
(1) The total space W of the blow-up carries a K¨ ahler form Ω which on the component C1
co-incides with the form obtained by symplectic reduction of the co- isotropic UνE⊂ Y
appearing in Lemma 4.27. In particular, C1 contains the monotone Lagrangian sub-
manifold KL = L×T 2 which is the Cliﬀord torus bundle over L⊂ B, as in Remark
4.30.
(2) The total space ( W, Ω) of the blow-up contains a Lagrangian submanifold L diﬀeomorphic
to L×T 2× [0,∞), ﬁbring over the positive real half-line in C, with p−1(0)∩ L =KL.
(3) The generic ﬁbre of π is a K¨ ahler manifold symplectomorphic to Y with its monotone
form, and the Lagrangian submanifold L∩π−1(t) is Hamiltonian isotopic to Γ E(L).
The proof relies on a picking a suitable symplectic connexion on the reg ular part of the ﬁbration
near the component C1 and parallel transporting KL along the real axis, compare to an identical
construction in the case B ={pt} given in [96, Section 4]. The last statement in (3) follows from
the reformulation of Γ E given in Remark 4.30.
We now consider a sequence ( uk : D2→ W ) of holomorphic disks in W with boundary on
the total Lagrangian L. Assume moreover that for each k, the disk uk has image inside the ﬁbre
p−1(tk) for some sequence tk→ 0 of positive real numbers. Gromov compactness in the total
space (W, L) implies that there is some limit stable disk u∞, but since the projections p◦ut are
constant maps, that limit disk must lie entirely in the zero ﬁbre of p. The general description of
a Gromov-Floer limit of disks as a tree of holomorphic disks and sphere bubbles, see for instance
[35], implies that u∞ has at least one disk component inside C1, with boundary on KL, and that
any component of u∞ meeting C0\(C0∩C1) must be a rational curve, since L∩C0 =∅.
We now suppose that all the disks uk have Maslov index 2. Any non-constant disk in C1 with
boundary on KL has Maslov index≥ 2, by monotonicity. Moreover, any non-trivial holomorphic
sphere in C0 has strictly positive Chern number, since that space is a Fano variet y. It follows
that the limit disk u∞ has no component contained in C0, and indeed no component which
intersects the divisor C0∩C1 (such a component would be glued to a non-constant sphere in
the component C0 or it would not be locally smoothable to the nearby ﬁbre; compare to t he
degeneration formula for Gromov-Witten invariants [45]). Therefo re, for suﬃciently large k, the
holomorphic disk uk must live inside the open neighbourhood of E⊂ π−1(tk) bound by UνE .
The result now follows from Lemma 4.33. □
Remark 4.37. Another viewpoint on the previous proof is also informative. The ﬁbr ation over
F1 has a (generally singular) discriminant curve, whose amoeba projec ts to some complicated
subset of the moment map image. However, this image is disjoint from the−1-section, because
we originally chose Href transverse to B (i.e. a net of hypersurfaces with smooth base locus).
A holomorphic rescaling of F1 (the lift of the holomorphic action on P2 taking [x :y :z]↦→[x :
y : cz] where we obtain F1 from blowing up [0 : 0 : 1]) will move the discriminant into a small
neigbourhood of Href . On the other hand, the symplectic structure on Y was constructed, via
inﬂation, to contain a large standard symplectic disk bundle, contain ing the monotone Lagrangian
L×T 2, cf. the proof of Lemma 4.27. In consequence, we may assume tha t the monotone L×T 2
projects into the upper half of Figure 5, whilst the discriminant lies in t he lower half.
The eﬀect of deformation to the normal cone is to make the K¨ ahler form standard in a
neighbourhood of E containing L×T 2. Suppose we start with a net of sections obtained by
perturbation from a net on the normal crossing degeneration whic h are degree 1 in the P2-ﬁbres
of P(L⊗2⊕O ) (we have essentially linearised, replacing s0 and s1 by Ds0,Ds 1 which span the
normal bundle of B⊂ X). As in Remark 4.30, one can then suppose – after smoothing and
small compactly supported perturbation of the symplectic form ne ar the normal crossing divisor
– that L×T 2 ﬁbres over T. There is now a Lagrangian isotopy of L×T 2, moving the image
point in the moment polytope towards the facet E at the top of Figure 5. Since this is not a
48 IV AN SMITH
Hamiltonian isotopy, and the Lagrangian does not stay monotone, t here may a priori be wall-
crossing. However, Maslov index zero disks project holomorphically to F1, where Maslov index is
given by intersection number with the toric boundary. The project ion of any such wall-crossing
disk must therefore be constant, so it in fact lay inside a ﬁbre of the projection φ. Equivalently,
the disk would lie inside a copy of B. The Lagrangian isotopy viewed inside B is monotone, since
π1(L) = 0, so in fact there is no wall-crossing. We move L×T 2 into a small neighbourhood of E
without changing the families of Maslov 2 disks which it bounds. These c an now be understood
by projection to F1; each disk hits one of E,H 0,H ∞, and there are 3 well-known families of such
disks, which were those visible in Lemma 4.33.
Lemma 4.32 now says that HF (Γ L, Γ L)∼= HF (L,L )⊗Cl 2 as a module over QH ∗(B; 0).
Although the ring structure on the second tensor factor is not a priori determined by the quantum
Gysin sequence, for degree reasons the Floer product amongst t he codimension 1 cycles given by
the circle factors L×{pt}× S1 and L×S1×{pt} is completely determined by disks of Maslov
index 2. The constraints on the Maslov 2 disks obtained in the proof o f Lemma 4.36 are suﬃcient
to imply that
HF (Γ L, Γ L) ∼= HF (L,L )⊗Cl 2
as a ring. This is true for all Lagrangian spheres L∈ F(B; 0), hence for any such L the image
Γ L has a non-trivial idempotent. We can analyse the Floer cohomology HF (Γ, Γ) of the entire
correspondence Γ ⊂B×Y via an analogous Gysin sequence, using the fact that Γ is the image
of a Lagrangian submanifold ∆ B×S1
eq⊂B×E under a correspondence B×E↝ B×Y (the
appropriate symplectic forms come from Remark 4.28). Taking the 0 -generalised eigenspace for
the action of c1(B), we again arrive at the mapping cone of a quantum product
∗ (e +σ· 1) : QH ∗(B; 0)⊗HF (S1
eq,S 1
eq)−→QH ∗(B; 0)⊗HF (S1
eq,S 1
eq) (4.17)
withe =h⊗ 1 + 1⊗ (−t) as before. Now h acts nilpotently, rather than trivially, on QH ∗(B; 0).
Lemma 4.32, and non-triviality of Γ L for some L, shows that σ = 1 in (4.17), which means
that the second term 1 ⊗ (σ· 1−t) acts trivially on HF (S1
eq,S 1
eq), so HF (Γ, Γ; 0 B) inherits a
Cliﬀord algebra factor. The idempotents for the individual Γ L derived above have as common
source an idempotent for Γ arising from splitting this Cliﬀord algebra. We deduce that the
functor Φ Γ associated to Γ by quilt theory has non-trivial idempotents, if one v iews its domain
as the nilpotent summand F(B; 0). We now appeal to Lemma 4.17 to see that there is a functor
Φ +
Γ : Tw F(B; 0)→ Tw π F(Y ) associated to either choice of idempotent in the Cliﬀord algebra
factor (strictly, associated to a choice of idempotent up to homot opy for the chosen cohomological
idempotent).
Lemma 4.38. The functor Φ +
Γ is fully faithful.
Proof. LetLi,i = 1, 2, be objects of F(B; 0). For simplicity we suppose they are simply-connected
(this is the only case which shall be used in the sequel). The functor Φ +
Γ takes these to idempotent
summands of Li×T 2, which we formally denote by ( Li×T 2)+. According to Equation 4.5, we
know
HF ((Li×T 2)+, (Lj×T 2)+) ∼= (+i)HF (Li×T 2,L j×T 2)(+j)
where the RHS denotes the action on the cohomological morphism gr oup of the relevant idem-
potents under the module structure of that group for HF (Li×T 2,L i×T 2) on the left and
HF (Lj×T 2,L j×T 2) on the right. From the proof of Lemma 4.32, the idempotents both come
from a ﬁxed idempotent p∈HF (T 2,T 2), via an isomorphism
HF ((Li×T 2)+, (Lj×T 2)+) ∼= HF (Li,L j)⊗p·HF (T 2,T 2)·p.
The second tensor factor is just a copy of the coeﬃcient ﬁeld K, completing the proof. □
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 49
Proposition 4.39. Assuming (4.10, 4.11) and that dimC(B) > 1, there is a fully faithful em-
beddingDπF(B; 0)֒→DπF(Y ).
This is exactly the content of Lemmas 4.31 and 4.38. Now take B =Q0∩Q1⊂ P2g+1 for some
g >1, so the space Y→ P1 is the relative quadric. Lemma 4.4 shows that the crucial hypothesis
(4.11) holds, and Proposition 4.39 yields one of the embeddings of The orem 1.1.
