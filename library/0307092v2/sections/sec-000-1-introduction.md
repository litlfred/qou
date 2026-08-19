---
doc_id: 0307092v2
doc_title: "Published: 14 February 2004"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class Walter D Neumann — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
There are several variations of the deﬁnition of the Bloch gr oup in the litera-
ture; by [7] they diﬀer at most by torsion and they agree with ea ch other for
algebraically closed ﬁelds. In this paper we shall use the fo llowing.
Deﬁnition 1.1 Let k be a ﬁeld. The pre-Bloch group P(k) is the quotient of
the free Z–module Z(k − {0, 1}) by all instances of the following relation:
[x] − [y] + [ y
x ] − [ 1 − x−1
1 − y−1 ] + [ 1 − x
1 − y ] = 0 , (1)
This relation is usually called the ﬁve term relation . The Bloch group B(k) is
the kernel of the map
P(k) → k∗ ∧Z k∗, [z] ↦→2
(
z ∧ (1 − z)
)
.
(In [15] the additional relations
[x] = [1 − 1
x ] = [ 1
1 − x ] = −[ 1
x ] = −[ x − 1
x ] = −[1 − x]
were used. These follow from the ﬁve term relation when k is algebraically
closed, as shown by Dupont and Sah [7]. Dupont and Sah use a diﬀe rent ﬁve
term relation but it is conjugate to the one used here by z ↦→1
z .)
There is an exact sequence due to Bloch and Wigner:
0 → Q/Z → H3(PSL(2, C)δ; Z) → B (C) → 0.
The superscript δ means “with discrete topology.” We will omit it from now
on.
B(C) is known to be uniquely divisible, so it has canonically the structure of a
Q–vector space (Suslin [21]). It’s Q–dimension is inﬁnite and conjectured to be
countable (the “Rigidity Conjecture,” equivalent to the co njecture that B(C) =
B(Q), where Q is the ﬁeld of algebraic numbers). In particular, the Q/Z in
the Bloch–Wigner exact sequence is precisely the torsion of H3(PSL(2, C); Z),
so any ﬁnite torsion subgroup is cyclic.
In the present paper we deﬁne an extended Bloch group ˆB(C) by replacing
C − { 0, 1} in the deﬁnition of B(C) by an abelian cover and appropriately
lifting the ﬁve term relation (1). Our main results are that w e can lift the
Bloch–Wigner map H3(PSL(2, C); Z) → B (C) to an isomorphism
λ : H3(PSL(2, C); Z)
∼
=− → ˆB(C)
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 415
Moreover, the “Roger’s dilogarithm function” (see below) g ives a natural map
R : ˆB(C) → C/π2Z.
We show that the composition
R ◦ λ : H3(PSL(2, C); Z) → C/π2Z
is the Cheeger–Chern–Simons class (cf [3]), so it can also be described as
i(vol +i cs), where cs is the universal Chern–Simons class. It has been a long-
standing problem to provide such a computation of the Chern– Simons class.
Dupont in [5] gave an answer modulo π2Q and our computation is a natural
lift of his.
We show that any complete hyperbolic 3–manifold M of ﬁnite volume has a
natural “fundamental class” in H3(PSL(2, C); Z). For compact M the existence
of this class is easy and well known: M = H3/Γ is a K(Γ , 1)–space, so the inclu-
sion Γ → Isom+(H3) = PSL(2 , C) induces H3(M ) = H3(Γ) → H3(PSL(2, C)),
and the class in question is the image of the fundamental clas s [ M ] ∈ H3(M ).
For non-compact M the existence is shown in Section 14. The Cheeger–Chern–
Simons class applied to this class gives i(vol(M ) + i cs(M )) where vol( M ) is
hyperbolic volume and cs( M ) is the Chern–Simons invariant. This Chern–
Simons invariant is deﬁned modulo π2Z and for compact M it arises here as
the Chern–Simons invariant for the ﬂat P SL(2, C)–bundle over M . According
to J. Dupont, this is the same as the Chern–Simons invariant f or the Rie-
mannian connection over M (private communication; this is proved modulo
6–torsion in [6] and our results also provide conﬁrmation—s ee [4] for discus-
sion). However, the Chern–Simons invariant for the Riemann ian connection
carries slightly more information, since it is deﬁned modul o 2 π2 rather than
modulo π2 . For non-compact M we show that the Chern–Simons invariant is
the one deﬁned by Meyerhoﬀ [11], which is naturally only deﬁn ed modulo π2 .
This fundamental class of M in H3(PSL(2, C); Z) determines an element ˆβ(M )
∈ ˆB(C). Our results describe ˆβ(M ) directly in terms of an ideal triangulation
of M , as a lift of the Bloch invariant β(M ) ∈ B (C) deﬁned in [15]. We need a
“true” ideal triangulation, which is more restrictive than the “degree 1” ideal
triangulations that suﬃced in [15]. The ideal triangulatio ns resulting from Dehn
ﬁlling that are used by the programs Snappea [22] and Snap [10 ] (see also [4]) are
not true, but we describe ˆβ(M ) in terms of these “Dehn ﬁlling triangulations”
in Theorems 14.5 and 14.7, and deduce practical simplicial f ormulae for Chern–
Simons invariants of hyperbolic 3–manifolds.
The formula of Theorem 14.5 exhibits directly the analytic r elationship, conjec-
tured in [16] and proved in [24], between volume and Chern–Si mons invariant of
Geometry & Topology, Volume 8 (2004)
416 Walter D Neumann
hyperbolic manifolds, and gives an independent proof of it. A similar formula
for Chern–Simons invariant was derived from [16, 24] in [13] , but that formula
was only accurate up to an unknown constant on any given Dehn s urgery space
(the constant was conjectured to be a multiple of π2/6, and our results now
conﬁrm this). Snappea and versions of Snap prior to 1.10.2 us e versions of that
formula, and use a bootstrapping procedure to discover the c onstant and obtain
the Chern–Simons invariant for many manifolds. Thanks to Ol iver Goodman,
Snap now implements the formula of Theorem 14.7 and can thus c ompute the
Chern–Simons invariant for any hyperbolic manifold.
More generally, any ﬂat PSL(2 , C) bundle over a closed oriented 3–manifold
M determines a class in H3(PSL(2, C); Z) and our results give a simplicial
computation of this class as an element of ˆB(C).
The main results of this paper were announced in [14] and part ial proofs were
in the preliminary preprint [17]. This paper corrects the te ntative statement
in [14] (also in [17]) that our map λ is not an isomorphism but has a cyclic
kernel of order 2. There is a related error in Section 6B of [4] : it is wrongly
stated that the Cheeger–Chern–Simons class takes values in C/2π2Z rather
than C/π2Z (and therefore that the fundamental class in H3(PSL(2, C); Z) of
a cusped hyperbolic 3–manifold has a mod 2 ambiguity).
