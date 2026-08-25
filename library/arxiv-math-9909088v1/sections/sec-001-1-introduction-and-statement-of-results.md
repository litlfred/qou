---
doc_id: arxiv-math-9909088v1
doc_title: "THE GAUSS MAP AND A NONCOMP ACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEA VES ON SEMIABELIAN V ARIETIES"
section_id: sec-001-1-introduction-and-statement-of-results
section_title: "Introduction and statement of results"
section_number: 1
pages: 1-3
source_pdf: 9909088v1.pdf
source_sha256: 52cfb568951f195f
doc_brief: "THE GAUSS MAP AND A NONCOMPACT RIEMANN-ROCH FORMULA FOR CONSTRUCTIBLE SHEAVES ON SEMIABELIAN VARIETIES — For an irreducible subvariety Z in an algebraic group G we deﬁne an integer gdeg( Z)≥ 0 as the"
---
Let X be a smooth algebraic variety over C and F be a constructible sheaf of
C-vector spaces on X. As in other situations, we have the Riemann-Roch problem:
express χ(X, F) = ∑
i(−1)i dim H i(X, F) in terms of some intrinsic geometric in-
variants of X and F. One such invariant is the characteristic cycle CC (F) which is a
formal Z-linear combination ∑
ν nν [Λ ν ] of irreducible conic Lagrangian subvarieties
Λ ν in the cotangent bundle T ∗X, see [14] for background. When X is compact, the
Riemann-Roch problem has a nice solution, namely [13]:
(1.1) χ(X, F) = ( CC (F), [X])T ∗X ,
where the right hand side is the intersection index, in T ∗X, of CC (F) and the zero
section X⊂ T ∗X. It can be calculated, for instance, by deforming X to the graph
of a C ∞ 1-form so that the intersection becomes transverse, and the n counting
intersection points (with multiplicities and signs).
Both the deﬁnition of CC (F) and the formula (1.1) (for compact X) extend to
the case when F is a bounded constructible complex (i.e., a complex of sheav es with
constructible cohomology).
When X is not compact, χ(X, F) still makes sense, but (1.1) is not applicable.
We face, therefore, an interesting noncompact Riemann-Roch problem of ﬁnding
χ(X, F) in terms of invariants intrinsic to X (in particular, not involving the choice
of compactiﬁcation).
The purpose of this paper is to exhibit such a “noncompact Rie mann-Roch
formula” in a particular class of situations. Namely, suppo se that X = G is an
algebraic group with Lie algebra g. For γ∈ g∗, let ωγ be the corresponding left-
invariant 1-form on G, and Ω γ ⊂ T ∗G be its graph. The Ω γ then form a natural
family of deformations of X and we can use them to make sense of the intersection
1
2 J. FRANECKI, M. KAPRANOV
index in (1.1) even when G is not compact. More precisely, if Λ ⊂ T ∗G is an
irreducible conic Lagrangian subvariety and γ∈ g∗ is generic, then Λ∩Ω γ consists of
ﬁnitely many transversal intersection points; their numbe r will be denoted gdeg(Λ)
and called the Gaussian degree of Λ. To explain the name, recall that Λ has the
form T ∗
Z X for an irreducible subvariety Z⊂ X (notation: T ∗
Z X will always mean
the closure of the conormal bundle to the smooth locus Zsm of Z). Denoting
k = dim(Z), we have the left Gauss map
Γ Z : Z→ G(k, g) , z ↦→z−1(TzZ)⊂ TeG = g
which is a rational map, regular on Zsm. The number gdeg(Λ) is the degree of Γ Z
in an appropriate sense, see section 2. For example, if Z is a hypersurface, then the
source and the target of Γ Z have the same dimension, and gdeg(Λ) is the degree of
Γ Z in the usual sense.
Note that gdeg(Λ) ≥ 0 by construction. We now formulate the main result of
this note. Recall [2] that a semiabelian variety is an algebr aic group G which is an
extension
(1.2) 1 → T→ G→ A→ 1,
where A is an abelian variety and T∼
= (C∗)n is an algebraic torus.
(1.3) Theorem. Let G be a semiabelian variety, F a bounded constructible complex
on G and CC (F) = ∑
ν nν [Λ ν ]. Then
χ(G, F) =
∑
ν
nν gdeg(Λ ν ).
(1.4) Corollary. If, in the situation of (1.3), F is a perverse sheaf, then χ(G, F)≥
0.
Indeed, for F a perverse sheaf, all nν≥ 0. Here we use the conventions of [1] for
the deﬁnition of (middle) perversity.
(1.5) Corollary. If G is semiabelian and Z⊂ G is a smooth closed subvariety,
then the number (−1)dim(Z)χ(Z, C) is nonnegative and coincides with gdeg(Z).
Indeed, C
Z [dim(Z)] is perverse and its characteristic cycle is [ T ∗
Z G] taken with
multiplicity 1.
Corollary 1.4 for G = (C∗)n was proven by Loeser-Sabbah [12] and given a diﬀer-
ent proof (applicable to etale sheaves) by Gabber-Loeser [4 ]. In the case when G is
an abelian variety, Corollary 1.4 seems to be new, even thoug h Theorem 1.3 in this
case does not need a special proof, being a consequence of (1. 1). Moreover, since
the general proof of Theorem 1.3 given below is extremely sim ple and transparent,
we believe that our approach exhibits the true reason behind the Loeser-Sabbah
observation. Further, another result of [4] identiﬁes irre ducible perverse sheaves
F on ( C∗)n such that χ((C∗)n, F) = 1, with complexes of solutions of hyperge-
ometric systems (essentially, of the A-hypergeometric systems [5][11], see [6] for
a comparison of the two points of view). On the other hand, in [ 12] the second
author classiﬁed irreducible hypersurfaces in ( C∗)n for which the Gauss map has
degree 1 and identiﬁed them with (reduced) A-discriminantal hypersurfaces. The
NONCOMPACT RIEMANN-ROCH 3
latter describe the characteristic varieties of the A-hypergeometric system. Thus
our approach explains the analogy between these two results .
Unfortunately, Theorem 1.3 cannot be straightforwardly ge neralized to more
general algebraic groups. For example, if G is nonabelian reductive, then it contains
aﬃne spaces Am for m ranging from 0 to the number of positive roots of G. The
Euler characteristic of Am being 1, Corollary 1.5 (and thus Theorem 1.3) cannot
hold. The same applies when G, while commutative, contains Ga, the additive
group. Nevertheless, we believe that there should exist gen eralizations of Theorem
1.3 which involve some particular classes of constructible sheaves and complexes.
We are grateful to V. Ginzburg for several useful remarks on t he ﬁrst version
of the text. A part of the results of this paper were included i n the thesis of the
ﬁrst author [3]. The second author was partially supported b y the National Science
Foundation.
