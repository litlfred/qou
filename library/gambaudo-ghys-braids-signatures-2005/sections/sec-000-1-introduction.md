---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Bull. Soc. math. France 133 (4), 2005, p. 541–579"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Bull. Soc. math. France 133 (4), 2005, p. 541–579 — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
This paper deals with the interaction of the following two st andard construc-
tions in knot theory.
• Braids and closed braids [4], [12].
In the plane R2, we consider the sequence of points x0
i = (i, 0) (for i =
1, 2,...) and we denote by D2(r) the disc of radius r, centered at the origin.
Texte re¸ cu le 13 octobre 2003, r´ evis´ e le 12 janvier 2004, accept´ e le 17 f´ evrier 2004.
Jean-Marc Gambaudo , Universit´ e de Bourgogne, UFR des Sciences et Techniques, UMR
5584 du CNRS, Institut de Math´ ematiques de Bourgogne, 9, Av enue Alain Savary, 21078
Dijon Cedex (France) • E-mail : gambaudo@u-bourgogne.fr
´Etienne Ghys , Unit´ e de Math´ ematiques Pures et Appliqu´ ees de l’´Ecole Normale Sup´ erieure
de Lyon, UMR 5669 du CNRS, 46, All´ ee d’Italie, 69364 Lyon Ced ex 07 (France)
E-mail : ghys@umpa.ens-lyon.fr
2000 Mathematics Subject Classiﬁcation. — 57M25.
Key words and phrases. — Knots, links, signature, Meyer cocy cle, Maslov class.
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE 0037-9484/2005/541/$5 . 00
c© Soci´ et´ e Math´ ematique de F rance
542 GAMBAUDO (J.-M.) & GHYS (E.)
In the space Xn of n-tuples of distinct points of D2(n + 1
2 ), we consider the
equivalence relation that identiﬁes two n-tuples if one is obtained from the
other by a permutation of the indices. We denote by ~Xn the quotient space
and by π n :Xn → ~Xn the natural projection. The fundamental group of ~Xn,
based at π n(x0
1,x 0
2,...,x 0
n), is called the n-th Artin braid group and is denoted
by Bn; its elements are called braids. Any braid γ in Bn is represented by a
path t ∈ [0, 1] ↦→(xt
1,x t
2,...,x t
n) ∈ Xn, i.e. by a system of n disjoint arcs
t ↦→(t,x t
i) in the cylinder [0 , 1] × D2(n + 1
2 ), such that π n(x1
1,x 1
2,...,x 1
n) =
π n(x0
1,x 0
2,...,x 0
n).
The identiﬁcation ( x, 0) ≈ (x, 1) for all x in D2(n + 1
2 ) produces a ﬁnite
collection of simple closed oriented curves in the solid tor us R/ Z × D2(n + 1
2 ),
images of the arcs t ↦→ (t,x t
i). The usual embedding of the solid torus in
3-space R3 and the compactiﬁcation of R3 with a point at inﬁnity, allow us
to associate with any braid γ an oriented link i.e. a collection of disjoint
embeddings of an oriented circle in the 3-sphere S3, called the closed braid
associated with γ , and denoted by ˆγ (see Figure 1).
Figure 1. Closure of a braid
• Signature of links [7], [11].
Let λ ⊂ S3 be an oriented link in S3 and let us choose a Seifert surface :
an oriented surface Sλ embedded in S3 whose oriented boundary is λ . The
ﬁrst homology group H1(Sλ ; Z) is equipped with a bilinear Seifert form B
in the following way. If x and y are two oriented closed curves on Sλ , one
deﬁnes B(x,y ) as the linking number of x with a curve y⋆ obtained from y
by pushing y a little away from Sλ along the positive direction transverse
toSλ . Clearly B(x,y ) only depends on the homology classes of x andy onSλ .
TurningB into a symmetric bilinear form
~B(x,y ) = B(x,y ) +B(y,x )
and tensoring by R, we get a symmetric bilinear form on the vector space
H1(Sλ ; R). It turns out that the signature of this symmetric form is in depen-
dent of the choice of the Seifert surface: it is the signature of the oriented
link λ , denoted sign( λ ) ∈ Z. For deﬁniteness, we recall that the signature of
a quadratic form is the number of + signs minus the number of − signs in an
orthogonal basis.
The notion of signature of an oriented link can be generalize d as follows.
Tensoring by C, we get a bilinear form on the vector space H1(Sλ ; C). Consider
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 543
α
 ∈ B3 i3(α
) ∈ B4
Figure 2. Adding a trivial strand
a complex number ω ⁄= 1 (usually chosen as a root of unity) and the hermitian
form
~Bω (x,y ) = (1 −ω )B(x,y) + (1 −ω )B(y,x ).
The signature of this hermitian form is again independent of the choice of the
Seifert surface: it is the ω -signature, signω (λ ) ∈ Z, of the oriented link λ . In the
case ω = −1, we recover the signature of the oriented link.
There is a natural sequence of embeddings B1 ⊂ B2 ⊂ · · · ⊂Bn ⊂ · · ·of
the braid groups. The embedding in of Bn in Bn+1 amounts to adding an
additional “trivial” strand (see Figure 2). The union of thi s inﬁnite chain of
groups is the inﬁnite braid group B∞ . Note that
signω (α ) = sign ω
(
in(α )
)
since a Seifert surface for ˆin(α ) is obtained from a Seifert surface for ˆα by
adding a disjoint disc. Therefore, the function sign ω (ˆα ) is well deﬁned on B∞ .
Combining these constructions, for eachω , we get a map from B∞ to Z which
associates with a braid γ the signature sign ω (ˆγ ). We are now in a position to
raise the question:
Given two braids α andβ in the braid group B∞ and a root of unity ω , what
can be said about the quantity
signω ( ˆα ·β ) − signω (ˆα ) − signω ( ˆβ )?
We give an explicit answer to this question. Before giving a p recise state-
ment we need to recall another construction which again is st andard in low
dimensional topology.
• The Burau representation and the Meyer cocycle .
Burau deﬁned an explicit linear representation of Bn in GL(n − 1, Z[t,t − 1]),
where t denotes some indeterminate. These representations combin e to a
representation of B∞ in the ascending union GL(∞, Z[t,t − 1]) of the groups
GL(n − 1, Z[t,t − 1]).
If one specializes t as a complex number ω , we get a linear representation
Bω in GL(∞, C). In [13], Squier shows that if ω is a complex number of modu-
lus 1, the image of Bω is contained in the unitary group of some non degenerate
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
544 GAMBAUDO (J.-M.) & GHYS (E.)
hermitian form. Since the imaginary part of such a hermitian form is a sym-
plectic form, the Burau representation provides symplecti c representations:
Bω : B∞ − → Sp(∞, R)
where we denote by Sp(∞, R) the ascending union of the symplectic groups
Sp(2g, R) (consisting of the symplectic automorphisms γ of R∞ which are the
identity on all vectors of the canonical basis of R∞ except for a ﬁnite number
of them).
In Section 2, we shall give more information concerning this Burau-Squier
representation. We shall give explicit formulas for the symplectic form and a
topological interpretation which (hopefully) will shed so me light on the sym-
plectic nature of the Burau representation, originally int roduced by Squier in
purely algebraic terms.
The symplectic group Sp(2g, R) is not simply connected; its universal cover
~Sp(2g, R) deﬁnes a central extension
0 → Z − → ~Sp(2g, R) − → Sp(2g, R) → 1.
This determines a cohomology class in H 2(Sp(2g, R); Z), called the Maslov
class. It turns out that 4 times the Maslov class can be repres ented explicitly
by an integral valued Meyer cocycle which is invariant by conjugation. We shall
give more motivation and background for this cocycle in Subs ection 3.2 but
for the time being we only mention the following “computatio nal” deﬁnition
(see [9]):
Letγ 1 andγ 2 be two elements in Sp(2g, R) and denote by Eγ 1,γ 2 the inter-
section of the images of γ − 1
1 − id and γ 2 − id. If e belongs to Eγ 1,γ 2, choose two
vectorsv1 and v2 such that e =γ − 1
