---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
2. Preliminary deﬁnitions and notation 6
2.1. Simplicial sets 7
2.2. Commutative Diﬀerential Graded Algebras 8
2.3. Dwyer-Kan localization and ( ∞, 1)-categories 8
3. Derived higher Hochschild functor 10
3.1. Naive axiomatic approach to higher Hochschild homology 10
3.2. Higher Hochschild as an ( ∞, 1)-functor 15
3.3. Pointed simplicial sets and modules 22
4. Factorization algebras and derived Hochschild functor over spa ces 25
4.1. The Hochschild ( ∞, 1)-functor in Top 25
4.2. (Pre)Factorization algebras 28
4.3. Locally constant factorization algebras and En-algebras 37
5. Relationship with topological chiral homology 40
5.1. Review of topological chiral homology ` a la Lurie 40
1
2 G. GINOT, T. TRADLER, AND M. ZEINALIAN
5.2. Locality axiom and the equivalence of topological chiral homology
with higher Hochschild functor for CDGAs 43
5.3. Relation with the Blob complex 47
5.4. Topological chiral homology as a factorization algebra 49
5.5. Some applications 55
References 59
1. Introduction
In this paper, we study the higher Hochschild chain 1 complex CH •
X• (A), func-
torially assigned to a simplicial set X• (or a topological space), and a commu-
tative diﬀerential graded algebra (CDGA) A, from an axiomatic point of view.
Recently, motivated by topological quantum ﬁeld theories, severa l concepts inte-
grating (higher) categories of spaces or manifolds with those of alg ebras of diﬀerent
types have arisen. We also study the relationship between higher Ho chschild chains,
factorization algebras [8, 9], topological chiral homology [26, 25] a nd the blob com-
plex [29]. Higher Hochschild homology was ﬁrst introduced by Pirashvili in [30].
The higher Hochschild complexes (as well as other aforementioned c oncepts) are a
generalization of the well-known and classical Hochschild complex. In fact, for the
case of the standard simplicial set model X• =S1
• for the circle, CH •
S1•
(A) reduces
to the standard Hochschild complex CH•(A) = A⊗•+1, see [17, 18].
In contrast with most other generalizations, higher Hochschild cha ins are de-
ﬁned over any (simplicial set model of a) space and not only (stratiﬁed) man-
ifolds. However, this forces us to restrict our attention to CDGAs or at best
to E∞-algebras. More precisely, the higher Hochschild chains form a bifun ctor
CH :sSet×CDGA→CDGA from the categories of simplicial sets and diﬀerential
graded commutative algebras to the latter category. The functo riality with respect
to spaces (and not merely manifold embeddings) is a key feature whic h allows us to
derive algebraic operations on the higher Hochschild chain complexes from maps of
topological spaces. For instance, it was crucially used to study the Hodge decom-
position of Hochschild homology (Pirashvili [30]) or to give and study mo dels of
(higher) string topology [12, 13]. Also, its underlying combinatorial p roperties allow
a generalization of Chen’s iterated integral [13]. Higher Hochschild is a lso a conve-
nient setting to study holonomy of (higher) gerbes (for instance s ee [35]) or compute
the observables of classical topological ﬁeld theories, see [8] and § 4.2. The higher
Hochschild homology satisﬁes many axioms similar to those of Eilenberg -Steenrod
for singular homology: naturality in each variable, commutations with coproducts
in both variable, homotopy invariance and the dimension axiom, see Co rollary 2.
However, to fully appreciate the higher Hochschild functor, one ne eds to go be-
yond mere homology and consider the higher Hochschild chains in a derived setting
which allows to formulate the analogue of the excision axiom . This axiom, remi-
niscent of the locality axioms of topological ﬁeld theories, asserts t hat Hochschild
chains maps the homotopy pushout of simplicial sets to the derived t ensor product of
algebras, i.e. homotopy pushout of CDGAs. This gluing property together with th e
1Note, that in this paper we are using a cohomological grading for our diﬀerential graded
modules, see Convention (7) on page 7. Also, this paper only d eals with Hochschild chains and
Hochschild homology, and never with Hochschild cochains or Hochschild cohomology.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 3
homotopy invariance allow to build many examples of Hochschild chain co mplexes
and to do computations as demonstrated in [13]. Further, such an enhancement is
needed in order to correctly compare the higher Hochschild functo r with more so-
phisticated concepts, such as topological chiral homology, which n aturally lies in a
homotopical setting. More precisely, we interpret the higher Hoch schild chains as a
(derived) bifunctor from the (∞, 1)-categoriessSet∞ of simplicial sets and CDGA ∞
of CDGAs, which are suitable localizations of the categories of simplicia l sets and
CDGAs, with respect to (weak) homotopy equivalences and quasi-is omorphisms.
This framework (instead of simply homology) is also needed to keep tr ack of the
topology of topological spaces modeled by the simplicial sets; for ins tance the usual
Hochschild complex CH ∗(A) interpretated in an ( ∞, 1)-category retains a circle
action governing cylic homology as shown in [26, 34]. Here, following Rez k and
Lurie [31, 26], an ( ∞, 1)-category means a complete Segal space. In our context,
the (∞, 1)-categories we considered are obtained by a Dwyer-Kan localizat ion pro-
cess from standard model categories, though the results of this paper should not
depend on the particular chosen approach to ( ∞, 1)-categories, see also Remark 1.
Our ﬁrst main result is the following theorem.
Theorem 1. The Hochschild chains lift as a functor of (∞, 1)-categories CH :
sSet∞×CDGA ∞→CDGA ∞ which satisﬁes the following axioms
(1) value on a point: there is a natural equivalence of CDGAs CH •
pt(A)∼=A.
(2) monoidal: there are natural equivalences of CDGAs
CH •∐ Xi•(A)∼=
⨂
CH •
Xi•(A)
(3) homotopy gluing/pushout: CH sends homotopy pushout in sSet∞ to
homotopy pushout in CDGA ∞, i.e. there is a natural equivalence of CDGAs
CH •
X•∪h
Z•Y•(A)∼=CH •
X• (A)⊗L
CH •
Z• (A)CH •
Y•(A).
Furthermore, the above axioms actually deﬁne the (derived) higher Hochschild
chains: indeed our second main result, Theorem 2 can be rephrased as
Theorem 2. The Hochschild chains is the unique bifunctor sSet∞×CDGA ∞→
CDGA ∞ satisfying the axioms (1), (2), (3) in Theorem 1.
These two results actually follow from the fact that CDGA is tensored over
simplicial sets and the general formalism of ( ∞, 1)-categories as in [22, 25] and
allow to interpret the Hochschild functor as a (derived) mapping sta ck in the con-
text of [32], see Corollary 15. We also show that the derived Hochsch ild functor
CH : sSet∞×CDGA ∞ → CDGA ∞ has many good formal properties: for in-
stance it commutes with ﬁnite (homotopy) colimits in both arguments and with
ﬁnite products of simplicial spaces (Corollary 5 and Proposition 5). F urther, the
locality axioms leads to an Eilenberg-Moore spectral sequence comp uting the higher
Hochschild homology (Corollary 3).
We also deal with the pointed versions of higher Hochschild chains, wh ich allows
to deﬁne Hochschild chains over a pointed simplicial set X• of a CDGA A with
coeﬃcient in an A-module M and establish similar results for this theory.
By homotopy invariance, we can deﬁne CH •
X (A) for a topological space X, gen-
eralizing the concept for a simplicial set X•, in such a way that all of the above
properties still hold. With this, we can now oﬀer interpretations of CH •
X (A) in
4 G. GINOT, T. TRADLER, AND M. ZEINALIAN
various contexts. First, in Section 4, we use these properties to g ive an interpre-
tation of Hochschild chains over spaces of a CDGA A as a factorization algebra
in any dimension. The concept of factorization algebras (see [8, 9]) is inspired
by Topological Quantum Field Theory, in which they appear naturally t o encode
observables. They were inspired by the work of Beilinson and Drinfeld [3] (in an
algebraic-geometry framework). Roughly speaking a factorizatio n algebra F is a
rule which (covariantly) associate cochain complexes to open subse ts of a space X
together with multiplications
F (U1)⊗···⊗F (Un)→F (V )
for any family of pairwise disjoint open subsets of an open set V in X. It should
satisfy a “cosheaf-like” condition, meaning that F (V ) can be computed by ˇCech
complexes indexed on nice enough covers, called factorizing covers , see [8] and
Section 4.2. The (derived) global sections of a factorization algebr aF is also called
the factorization homology of F and is denoted HF (F,X ).
In this context we prove that the higher Hochschild chain functor d eﬁnes a
commutative factorization algebra CHX (A), if X admits a good cover whose fac-
torization homology is precisely the derived Hochschild chains CH •
X (A).
Theorem 4. Let X be a topological space with a factorizing good cover and A be
a CDGA. Assume further that there is a basis of open sets in X which is also a
factorizing good cover. Then the assignment CHX :U↦→CH •
U (A) is a factorization
algebra on X.
In particular, this applies when X is a manifold. Further, we prove that any
factorization algebra for which F (U ) (for contractible U ) is naturally equivalent to
a CDGA A is canonically equivalent to CHX (A).
Corollary 10. LetX be a topological space with a suﬃciently nice cover, let A be
a CDGA, and let F be a strongly constant factorization algebra on X of type A.
Then there is a natural equivalence of factorization algebr asF∼=CHX (A).
In particular, there is a natural equivalence HF (F )∼=CH •
X (A) in k-Mod ∞.
In Section 5, we establish a relationship between the topological chiral homology
functor deﬁned by Lurie [26, 25] and both the higher Hochschild fun ctor and fac-
torization algebras. To obtain a comparison between these functo rs, it is important
to note that they are deﬁned in two diﬀerent setting with a common in tersection.
Topological chiral homology, denoted
∫
MA, is deﬁned for any En-algebraA (where
En is an operad equivalent to the little cubes in dimension n) and an m-dimensional
manifoldM ,m≤n, such that M×Dn−m is framed (we say M isn-framed). Fur-
ther
∫
MA is an En−m-algebra which is also a module over the En−m+1-algebra∫
∂M A. Topological chiral homology can be interpreted as an invariant of f ramed
manifolds produced by an extended ( ∞,n )-Topological Field Theory in the sense
of [26]; the theory in question takes values in an ( ∞,n )-category of En-algebras
whosen-morphisms are (homotopy types) of chain complexes. Note that t opologi-
cal chiral homology depends on and comes with a choice of a sequenc e of maps of
operads,
E1
/d31 /d127 /d47/d47E2
/d31 /d127 /d47/d47...... /d31 /d127 /d47/d47En
/d31 /d127 /d47/d47...... /d47/d47 /d47/d47Com
which allows one to interpret a CDGA as an En-algebra for any n. When A is a
CDGA, things simplify greatly, and we can give a simple description of
∫
MA in
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 5
terms of the higher Hochschild complex of A. Using excision for topological chiral
homology, see Proposition 11, we prove, in a rather geometric way:
Theorem 5. LetM be a manifold endowed with a framing of M×Dk and A be a
diﬀerential graded commutative algebra viewed as an Em+k-algebra. Then topolog-
ical chiral homology of M with coeﬃcients in A, denoted by ∫
MA is equivalent to
CH •
M (A) viewed as an Ek-algebra.
In other words, topological chiral homology and higher Hochschild c hains coin-
cide on their common intersection for an n-framed manifold M , and a CDGA A.
As an immediate corollary, in that case,
∫
MA is independent of the n-framing, see
§ 5.5.
In Section 5.3, we explain brieﬂy the relationship between topological chiral
homology and the blob complex [29]. More precisely, topological chiral homology
extends to all manifolds provided that it is applied to an EO(n)
n -algebra, i.e. an
algebra over the semi-direct product of the En-operad with the orthogonal group
O(n) or said otherwise an En-algebra homotopically O(n)-invariant. The blob
complex can also be deﬁned for such algebras and any closed manifold and agrees
with topological chiral homology in that case, see Proposition 12.
The relation between factorization algebras, derived higher Hochs child chains
and topological chiral homology for CDGAs can be pushed further. Indeed, the
data of an En-algebra are equivalent to those of a locally constant factorization
algebra in Rn [9, 25], see Proposition 10. Further, the assumptions of having an
En-algebra and a framed manifold to deﬁne topological chiral homology can be
replaced by the one of having a suitable (kind of) cosheaf of En-algebras on an
n-dimensional manifold N . Such a cosheaf is called an E⊗
N -algebra [25] and is also
inspired by the work of Beilinson-Drinfeld [3]. The techniques develope d to compare
Hochschild chains with factorization algebras and topological chiral homology leads
to Theorem 6 which can be rephrased as
Theorem 6. LetM be a manifold of dimension n.
(1) Topological chiral homology deﬁnes a natural (∞, 1)-functorTC M from the
category of E⊗
M×Rd -algebras to the category of locally constant factorizatio n
algebras on M with value in Ed-algebras, such that ∫
MA∼=HF (TC M,M ).
(2) The functor TC M (A) is an equivalence.
Finally in Section 5.5, we derive some applications of our results to give a n
interpretation of topological chiral homology in terms of maping spa ces and to
prove that topological chiral homology satisﬁes the exponential la w, i.e., if M and
N are manifolds and A is an Ed[M×N ]-algebra, then, there is an equivalence of
Ed-algebras ∫
M×N
A ∼=
∫
M
( ∫
N
A
)
see Corollary 17.
Let us outline the philosophy intertwining the diﬀerent concepts stu died here.
Given an n-framed manifold M of dimension m (i.e. M× Rn−m is framed), and an
En-algebra A, we can form the topological chiral homology
∫
MA (or equivalently
consider factorization algebra homology), which can be thought of as a colimit of
tensor products of A indexed by balls in the manifold. Now, if we embed M×Rn−m
6 G. GINOT, T. TRADLER, AND M. ZEINALIAN
inM×Rn−m+1 equipped with the induced framing, one can form
∫
MB for anEn+1-
algebra. But two diﬀerent framings of M× Rn−m may become equivalent after the
embedding. Since a CDGA C is an Ek-algebra (as well as an E⊗
M -algebra) for
all k,
∫
MC should not be able to distinguish diﬀerent framings. Since manifolds
embed in euclidean spaces, we further see that
∫
MC should makes sense for any
manifold. Note that constant factorization algebra can be pulled ba ck along open
immersions and pushed forward any map. This hints that any deform ation retract
of a manifold should also have a well deﬁned topological chiral homolog y (with
value in a C) equivalent to the one of the manifold. All of this suggests that, fo r
CDGAs, topological chiral homology may be extended to any CW-com plex and is
a homotopy invariant, which is precisely realized by the derived higher Hochschild
functor. Said otherwise, higher Hochschild is the “limit” for n going to ∞ of
topological chiral homology deﬁned as an invariant of manifolds of dim ension n.
One of the emerging pattern here is that there is a balance to keep in between
the manifolds and the algebraic structure needed to produce a (de rived) invariant.
For instance, in order to consider En-algebras, one need to consider only at most
n-dimensional manifolds (possibly with extra structure such as a fra ming). In
particular, working with only associative algebras restricts attent ion to manifolds
of dimension 1. At the opposite side of the spectrum, restricting to CDGAs allows
to build and study explicit examples in a much easier way and to compute them
when adding the usual Rational Homotopy techniques to the axioma tic properties
satisﬁed by the theory.
We choose to work with commutative diﬀerential graded algebras sin ce we are
mainly interested in the characteristic zero case. However, it is also possible to
work with simplicial commutative algebras, and all our results should m akes sense
in this setting. Simplicial commutative algebras are better behaved if one wants to
deal with positive characteristic.
Acknowledgments. We would like to thank the referees, David Ayala, Kevin
Costello and Owen Gwilliam for many useful discussions and comments. The ﬁrst
author would like to thank the Einstein Chair at CUNY for their invitatio n, and
the second and third would like to thank IH ´ES for inviting them. The second and
third authors were partially supported by the NSF grant DMS-0757 245, and by the
Max-Planck Institute for Mathematics in Bonn, Germany.
