---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-038-67-noetherian-group-algebras
section_title: "Noetherian group algebras"
section_number: 6.7
pages: 26-29
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
Theorem. Let k be a ﬁeld of characteristic p ≥ 0, and let G be a polycyclic-by-ﬁnite
group of Hirsch length d.
(a) kG is noetherian Auslander Gorenstein and AS-Gorenstein of in jective di-
mension d.
NOETHERIAN HOPF ALGEBRAS 27
(b) kG is AS-regular if and only if it is Auslander regular if and onl y if G
contains no elements of order p.
Proof. (a) First, kG is noetherian by [Pa, Corollary 10.2.8]. Since we can ﬁnd a
poly-(inﬁnite cyclic) normal subgroup H of ﬁnite index in G [Pa, Lemma 10.2.5], it
is suﬃcient to prove that (i) kH is AS-Gorenstein (respectively Auslander Goren-
stein) when H is poly-(inﬁnite cyclic), and (ii) kH AS-Gorenstein (respectively
Auslander Gorenstein) implies that kG is AS-Gorenstein (respectively Auslander
Gorenstein) when | G : H | is ﬁnite.
(i) We prove this by induction on the Hirsch number d of H. When d = 0 there
is nothing to prove, so assume the result is true for all poly-(inﬁnite cyclic) groups
of Hirsch number less than d. Choose a normal subgroup T of H with H/T = ⟨xT ⟩
inﬁnite cyclic.
AS-Gorenstein property: By the induction hypothesis, Ext i
kT (k, kT ) = δi,d−1k.
Applying kH ⊗kT − to a projective kT −resolution of k, it is easy to prove that, for
all i ≥ 0,
Exti
kH (kH ⊗kT k, kH ) ∼= Exti
kT (k, kT ) ⊗kT kH(6.7.1)
as right kH −modules. In particular, therefore, as right k⟨x⟩−modules,
Exti
kH (kH ⊗kT k, kH ) ∼= δi,d−1k⟨x⟩.
Let’s write H
T ↑k for kH ⊗kT k. The short exact sequence of left kH −modules
0 − →H
T↑k − →H
T↑k − →k − →0,
where the left-hand embedding is given by right multiplication by x − 1, induces
exact sequences
Exti
kH (H
T↑k, kH ) − →Exti
kH (H
T↑k, kH ) − →Exti+1
kH (k, kH ) − →Exti+1
kH (H
T↑k, kH ),
where the left hand and right hand maps are left multiplication by x − 1, [Br2,
Lemma 2.1]. Taking i < d − 2 here, and applying the induction hypothesis together
with (6.7.1), shows that Ext t
kH (k, kH ) = 0 for t ≤ d − 2. Taking i = d − 2, we ﬁnd
in view of (6.7.1) that Ext d−1
kH (k, kH ) is the kernel of the map
Extd−1
kH (H
T↑k, kH ) → Extd−1
kH (H
T↑k, kH ),
a homomorphism ρ between free k⟨x⟩−modules of rank one given by multiplication
by x − 1. Therefore, Ext d−1
kH (k, kH ) is 0 . Moreover, since Ext d+1
kH (H
T↑k, kH ) is 0, by
(6.7.1), the cokernel of ρ is Ext d
kH (k, kH ). Thus Ext d
kH (k, kH ) has k-dimension
one, as required.
Auslander Gorenstein property: Note that kH = kT [t±1; σ] for some automor-
phism σ of kT . By the induction hypothesis, kT is Auslander Gorenstein. By [Ek,
Theorem 4.2], kT [t; σ] is Auslander Gorenstein. By [ASZ2, Proposition 2.1] the
localization kT [t±1; σ] is Auslander Gorenstein.
(ii) This follows because crossed products of ﬁnite groups are Frob enius exten-
sions - see [AB, Lemma 5.4].
(b) This follows from (a) and [Pa, Theorem 10.3.13]. □
Remarks. (a) It is an open question whether all noetherian group algebras
kG come from polycyclic-by-ﬁnite groups G.
28 K.A. BROWN AND J.J. ZHANG
(b) In general a noetherian group algebra kG could have inﬁnite GK-dimension
[KL, Corollary 11.15]. Even when GKdim kG is ﬁnite, it could be larger
than the global dimension of kG. Hence in these cases, kG is not Cohen-
Macaulay.
Poincar´ e duality of group homology and cohomology was investigated by Bieri in
a series of papers beginning with [Bi1]. Given a commutative ring R, a non-negative
integer n and a group G, he deﬁned [Bi2, 5.1.1] G to be a duality group of dimension
n over R if there exists an RG−module C such that, for each RG−module A and
each k ∈ Z, there are isomorphisms
H k(G, A) ∼= Hn−k(G, C ⊗R A)
induced by the cap product. Moreover, [Bi2, Deﬁnition 3.2], G is a Poincar´ e duality
group of dimension n over R if C above is R with almost trivial G−structure, where
this means that the image of G in Aut R(R) is {±Id}.
It’s clear that, for polycyclic-by-ﬁnite groups, Bieri’s results desc ribe the shadow
at the level of group (co)homology of the existence and nature of the dualising
complex for kG. On the other hand it is straightforward to apply the results of
[Bi1], [Bi2] to determine the Nakayama automorphism for kG. In order to do this,
we deﬁne the adjoint trace T of the polycyclic-by-ﬁnite group G as follows. Fix a
series
1 = G0 ⊆ G1 ⊆ · · · ⊆ Gn = G(6.7.2)
of normal subgroups Gi of G whose factors Gi/Gi−1 are either torsion-free Abelian,
or ﬁnite. Provide each torsion-free factor Ai = Gi/Gi−1 with a Z−basis (of cardi-
nality ti, say), so that conjugation by g ∈ G assigns a matrix ˜gi ∈ GLti(Z) to the
pair ( g, Ai). Now deﬁne a map
T : G − → {±1} : g ↦→
∏
i
det(˜gi),
where the product is taken over those i, 1 ≤ i ≤ n, such that Gi/Gi−1 is inﬁnite.
One checks easily that this deﬁnition doesn’t depend on the choice of series (6.7.2),
and that T is a group homomorphism [Bi1, §3.2]. Finally, set Tk to be the compo-
sition of T with the canonical homomorphism from {±1} to k, and use the same
symbol for the resulting representation of kG on k.
Proposition. Let k be a ﬁeld of characteristic p ≥ 0, and let G be a polycyclic-by-
ﬁnite group with Hirsch length d. If p > 0 assume that G contains no elements of
order p.
(a) [Bi2] G is a Poincar´ e duality group over k. The dualising module C is
H d(G, kG); that is, C is the left integral of kG.
(b) The Nakayama automorphism ν of kG is the winding automorphism induced
by the adjoint trace Tk of G in k. That is,
ν(g) = Tk(g)g
for all g ∈ G. In particular, ν is diagonalisable.
(c) Hd(kG, kGν ) ∼= Z(kG) ⁄= 0, and H d(kG, νkG) ∼= kG/[kG, kG] ⁄= 0.
(d) The integral order of kG is either 1 or 2.
NOETHERIAN HOPF ALGEBRAS 29
Proof. (a) The ﬁrst statement is proved in [Bi2, Theorems 5.6.2 and 5.6.4], and the
second is [Bi2, Proposition 5.2.1]. (Of course, (a) also follows from The orem 6.7
and Lemma 3.3.)
(b) By Theorem 6.7, kG is AS-regular. Since the square of the antipode of kG
is the identity, Proposition 4.5(a) shows that the Nakayama automo rphism of kG
is the winding automorphism induced by the right module structure of the left
integral. The calculations in [Bi1, §3.2] show that this right structure is given by
Tk.
(c) This follows from Corollary 5.1.
(d) This is clear from part (b). □
