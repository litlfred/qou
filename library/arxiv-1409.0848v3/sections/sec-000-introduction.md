---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-6
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
1. Recollections 6
1.1. Stratiﬁed spaces 6
1.2. Symmetric monoidal ∞-categories 10
2. Factorization 14
2.1. Disk algebras 14
2.2. Factorization homology 17
2.3. Disks and ﬁnite subsets 20
2.4. Localizing with respect to isotopy equivalences 23
2.5. Pushforward 26
2.6. Algebras over a closed interval 30
2.7. Homology theories 32
3. Homotopy invariant homology theories 35
3.1. Classical homology theories 35
3.2. 1-point compactiﬁcations 36
3.3. Compactly supported cohomology 38
3.4. Non-abelian Poincar´ e duality 40
4. Examples of factorization homology theories 42
4.1. Factorization homology of stratiﬁed 1-manifolds 42
4.2. Intersection homology 43
4.3. Link homology theories and Diskfr
d⊂n-algebras 44
2010 Mathematics Subject Classiﬁcation. Primary 57P05. Secondary 55N40, 57R40.
Key words and phrases. Factorization homology. Topological quantum ﬁeld theory. Topological chiral homology.
Knot homology. Conﬁguration spaces. Operads. ∞ -Categories.
DA was partially supported by ERC adv.grant no.228082, and b y the National Science Foundation under Award
No. 0902639. JF was supported by the National Science Founda tion under Award 0902974 and Award 1207758. HLT
was supported by a National Science Foundation Graduate Res earch Fellowship, by the Northwestern University Oﬃce
of the President, by the Centre for Quantum Geometry of Modul i Spaces, and by the National Science Foundation
under Award DMS-1400761.
1
References 51
Introduction
The present work forms an initial step in a formalism for topological q uantum ﬁeld theory using
stratiﬁed spaces. This larger program proposes to understand lo cality in topological quantum ﬁeld
theory by a fusion of the algebra of factorization homology and the geometry of stratiﬁcations. Before
delineating this step and, brieﬂy, this future program, we ﬁrst rev iew the subject of factorization
homology.
Factorization homology is, heuristically, a procedure which takes an n-manifold M and an al-
gebraic input A, such as an En-algebra, and produces an object
∫
MA. The manifold provides the
gluing data, the algebra provides the gluing rules, and one can think o f integrating the multiplica-
tion of the algebra over the gluing data of the manifold. Viewing this ob ject as an invariant of the
manifold, the procedure generalizes usual homology theories; view ing the object as an invariant of
the algebra, it generalizes Hochschild homology when the manifold is th e circle and oﬀers a natural
repository for traces or index-type invariants.
Such a procedure was introduced for algebraic varieties by Beilinson & Drinfeld in their work on
an algebro-geometric formalism for conformal ﬁeld theory; see [Be Dr] and [FG]. In §5.5 of [Lu2],
Lurie deﬁned a topological analogue of their construction – known a s factorization homology or
topological chiral homology – and this topological construction likew ise generalizes the labeled
conﬁguration spaces of Salvatore [Sa] and Segal [Se2]. The main the orem of this area, non-abelian
Poincar´ e duality, naturally generalizes the James construction an d conﬁguration space models of
mapping spaces dating to the 1970s in work of McDuﬀ [Mc] and others – see [AF1] for a more
detailed history.
Another recent catalyst for study in this area has been the appro ach of Costello & Gwilliam to
perturbative quantum ﬁeld theory in [CG]. In mathematical approac hes to topological ﬁeld theory
at least since Atiyah in [At], it is common to organize the formalism aroun d the functoriality of
the state spaces in the theory. This choice leads to cobordisms and , proceeding deeper, higher
categories of cobordisms after Baez & Dolan in [BaDo]. In contrast, Costello & Gwilliam, following
the factorization algebra structures of [BeDr], codify their theor y around the structure of observables,
or operators, rather than state spaces. In their work, the ear lier renormalization machinery of [Co]
is married with the factorization point of view; the intuitive factoriza tion homology procedure
becomes a way of constructing a candidate object
∫
MA of global observables on a space-time M
from the algebra of observables A on Euclidean space. This candidate object
∫
MA is intended to
accurately capture the global observables on M if the quantum ﬁeld theory is perturbative. They
prove a quantization theorem, designed as a mathematical formula tion of physicists methods of
perturbative renormalization, using the Batalin–Vilkovisky formalism applied to derived symplectic
geometry. From this quantization theorem they construct a numb er of interesting examples of such
perturbative ﬁeld theories.
The structural favoring of observables over state spaces has g eometric consequences, namely a
favoring of open embeddings over cobordisms. Dual to restricting ﬁelds, observables can extend by
zero. This is unlike state spaces, where there is no procedure for e xtension by zero, no naturality with
respect to open embeddings, and no values for non-compact manif olds. The cobordism hypothesis
with singularities, after Baez–Dolan [BaDo] and Lurie [Lu3], gives a pro posed classiﬁcation for
certain topological ﬁeld theories in terms of their state spaces. Wit h this in mind, one can ask if
there is a similar classiﬁcation which applies to this class of topological ﬁ eld theories constructed
in [CG] in terms of the Batalin–Vilkovisky formalism, in terms of their obs ervables. Our ﬁrst main
result, Theorem 2.43, can be viewed as just such a classiﬁcation.
2
In the present work, we lay the foundations for a general theory of factorization homology,
following the outline of [AF1] and after the originating work of Lurie in [L u2]. We do this for
stratiﬁed spaces and, more generally, B-manifolds, where B is a collection of basic singularity
types endowed with a tangential structure, applying the theory o f stratiﬁed spaces and tangential
structures developed in [AFT]. This extra level of generality is carrie d out for two reasons. First,
the theory without stratiﬁcations is related to observables on spa ce-time in perturbative ﬁeld theory;
adding nontrivial stratiﬁcations allows one to incorporate boundar y conditions and defects in this
theory, such as Wilson line operators in Chern–Simons. The second r eason concerns the extension
of our theory outside of the perturbative range in quantum ﬁeld th eories; our larger program in
progress (see [AFR] and the papers that follow) uses stratiﬁcatio ns to eﬀect this greater generality.
We now turn to a linear overview of contents of the current work, w hich has three parts.
In the ﬁrst part, we cover the deﬁnition (Deﬁnition 2.14) of factor ization homology as a Kan
extension from Disk(B)-algebras to B-manifolds, and we prove its existence. The ﬁrst main result
is that the symmetric monoidal and underlying left Kan extensions ar e equivalent, and that there
is therefore a comprehensible formula (Theorem 2.15) which comput es factorization homology; this
generalizes a formula for usual homology. To establish this existenc e result and this explicit formula
we prove a general result giving conditions for existence and agree ment of symmetric monoidal and
underlying left Kan extensions in Lemma 2.16. To verify the conditions of this lemma requires
proving that the∞-category Disk(B)/X of basic singularity types embedded in a manifold is sifted,
Corollary 2.28; our proof makes use of a localization result relating dis crete and topological categories
of embedded disks and of Dugger–Isaksen’s work in [DI].
Together with this explicit existence, we prove in Theorem 2.25 the ex istence of push-forwards for
factorization homology along constructible bundles of stratiﬁed sp aces. An immediate consequence is
a Fubini theorem for factorization homology, Corollary 2.29. Along w ith an analysis of factorization
homology in the case of a closed interval, which we identify as a relative tensor product in Proposition
2.34, these results culminate in a main structural theorem. To stat e it, we require some terminology:
let B be an ∞-category of basic singularity types and Mﬂd(B) the collection of stratiﬁed spaces
locally modeled on B; let V be a symmetric monoidal ∞-category which is⊗-sifted cocomplete (see
Deﬁnition 1.15). Below, we next deﬁne the collection of V-valued homology theories H(Mﬂd(B), V)
as a full ∞-subcategory of symmetric monoidal functors Fun⊗(Mﬂd(B), V) satisfying the following
symmetric monoidal generalization of the Eilenberg–Steenrod axiom s.
Deﬁnition 0.1. [Deﬁnition 2.37] The ∞-category of homology theories (over X) is the full ∞-
subcategory
H
(
Mﬂd(B)/X, V
)
⊂ Fun⊗(
Mﬂd(B)/X, V
)
consisting of those H that satisfy the following two properties:
• ⊗-Excision: Let W ∼= W−
⋃
R×W0
W+ denote a collar-gluing among B-manifolds over X.
Then the canonical morphism (2.6.3)
(0.0.1) H(W−)
⨂
H(W0)
H(W+)
≃
−−→H(W )
is an equivalence in V.
• Continuous: Let W0⊂ W1⊂···⊂ X be a sequence of open sub-stratiﬁed spaces of X
with union denoted as ⋃
i≥0
Wi =:W . Then then the canonical morphism
(0.0.2) colim
(
H(W0)→H(W1)→...
) ≃
−−→H(W )
is an equivalence in V.
Absolutely, the∞-category of homology theories (for B-manifolds) is the full ∞-subcategory
H
(
Mﬂd(B), V
)
⊂ Fun⊗(
Mﬂd(B), V
)
3
consisting of those H for which, for each B-manifold X, the restriction H| Mﬂd(B)/X is a homology
theory for X.
The preceding deﬁnition generalizes to stratiﬁed spaces a notion int roduced in [AF1]; see also the
introduction of that work for a discussion of the present concept s, such as ⊗-excision. We can now
state our main result, which generalizes the main result of loco citato from manifolds to stratiﬁed
spaces.
Theorem 0.2 (Theorem 2.43). There is an equivalence between Disk(B)-algebras in V and V-valued
homology theories for B-manifolds
AlgDisk(B)(V)≃ H(Mﬂd(B), V)
deﬁned by sending a Disk(B)-algebraA to the factorization homology
∫
A.
Here the ⊗-excision property of the homology theory becomes a formulation o f the locality of
the ﬁeld theory. The theorem includes a relative version, for a ﬁxed B-manifold X, which in this
interpretation is a ﬁxed space-time. Thus, our result both genera lizes the Eilenberg–Steenrod axioms
and attempts to axiomatize the structure of the observables in a p erturbative topological quantum
ﬁeld theory. This latter topic also lies in the domain of the cobordism hy pothesis, or the cobordism
hypothesis with singularities of [Lu3]. A direct comparison between th ese approaches is possible,
subject to suitable construction of the functor Z, below, proposed in the cobordism hypothesis.
Namely, there should be a commutative diagram below (subject to a s uitable construction of the
dashed functors, which we do not provide in the present work):
AlgDiskn (V)∼
∫
/d15/d15
/d47/d47 (
Algn(V)∼) O(n)
Z
/d15/d15✤
✤
✤
H(Mﬂd(B), V)∼ /d47/d47❴ ❴ ❴Fun⊗(Bordn, Algn(V))
We brieﬂy explain the terms in this picture: Diskn and Mﬂd are the∞-categories of n-disks and
n-manifolds and embeddings; Bordn is the (∞,n )-category of bordisms of manifolds from [Lu3];
and Algn(V) is the higher Morita category, where k-morphisms are framed ( n−k)-disk algebras in
bimodules; the superscript ∼ denotes that we have taken the underlying ∞-groupoids, restricting to
invertible morphisms. The bottom dashed arrow from homology theo ries valued in V to topological
quantum ﬁeld theories valued in Algn(V), assigns to a homology theory F the functor on the bordism
category sending a k-manifold M to F(M ◦× Rn−k), the value of F on a thickening of the interior
of M . There is a similar diagram replacing n with a general collection of basic singularity types B,
where on the right we substitute bordism categories with singularitie s.
We assert that this diagram commutes, but this assertion relies on t he existence of the higher
bordism (∞,n )-category Bordn and on the veriﬁcation of the cobordism hypothesis, i.e., the existen ce
of the dotted arrow Z. A proof by Lurie has been outlined in [Lu3], building on earlier work with
Hopkins. We defer the commutativity of this diagram to a future wor k, after the full completion of
the right hand side.
We turn to a description now of the the second part of this work. Th ere, we apply our main result,
Theorem 2.43, to give a proof of non-abelian Poincar´ e duality, afte r [Sa], [Se2], and Section 5.5.6
of [Lu2]. Further, our Theorem 3.18 is a stratiﬁed generalization, th at there is a homotopy equiva-
lence ∫
X
AE≃ Γc(X,E )
between a factorization homology theory and a space of sections o f a stratiﬁed bundle E over a
B-manifold X, subject to stratum by stratum connectivity conditions on E. The left hand side
can be thought of either as a labeled conﬁguration space or a form o f nonabelian homology with
coeﬃcients in a higher loop space.
4
In the last section of this paper, we detail the structure involved in particular choices of B-
structures. We observe that the intersection homology theories of Goresky & MacPherson ﬁt our
axiomatics. As such, our stratiﬁed theories generalize intersectio n homology in the way that the
unstratiﬁed factorization homology of [Lu2] and [AF1] generalize or dinary homology. We then study
two examples: manifolds with boundary and n-manifolds with a submanifold of ﬁxed dimension d.
Both of these have descriptions as special cases of our main theor em, and each of these descriptions
mix with the form of the higher Deligne conjecture proved by Lurie [L u2], which asserts that the
higher Hochschild cohomology HC∗
Dfr
d
(B) of a framed d-disk algebra B carries a framed ( d + 1)-
disk algebra structure which is characterized by a universal prope rty. In particular, we prove the
following by combining our main theorem and this form of Deligne’s conje cture:
Corollary 0.3. There is an equivalence∫
: AlgDiskfr
d⊂n
(V) ⇆ H(Mﬂdfr
d⊂n, V) :ρ
between Diskfr
d⊂n-algebras in V and V-valued homology theories for framed n-manifolds with a framed
d-dimensional submanifold with trivialized normal bundle. The datum of a Diskfr
d⊂n-algebra is equiv-
alent to the data of a triple (A,B,α ), where A is a Diskfr
n-algebra, B is a Diskfr
d -algebra, and
α :
∫
Sn−d−1A→ HC∗
Dfr
d
(B) is a map of Diskfr
d+1-algebras.
Specializing to the case of 3-manifolds with a 1-dimensional submanifo ld, i.e., to links, the preced-
ing provides an algebraic structure that gives rise to a link homology t heory. To a triple ( A,B,α ),
whereA is a Diskfr
3 -algebra,B is an associative algebra, and α : HC∗(A)→ HC∗(B) is a Diskfr
2 -algebra
map, one can then construct a link homology theory, via factorizat ion homology with coeﬃcients
in this triple. This promises to provide a new source of such knot homo logy theories, similar to
Khovanov homology. Khovanov homology itself does not ﬁt into this s tructure, for a very simple
reason: an open embedding of a noncompact knot ( U,K )⊂ (U ′,K ′) does not deﬁne a map on
Khovanov homologies, from Kh(U,K ) to Kh(U ′,K ′). (In addition, Khovanov homology still has not
been constructed for general manifolds K, other than S3 or R3.) factorization homology theories
can be constructed, however, using the same input as Chern–Simo ns theory, and these appear to
be closely related to Khovanov homology – these theories will be the s ubject of another work, one
which requires a more involved use of stratiﬁcations to capture non perturbative phenomena.
Remark 0.4. In this work, we use Joyal’s quasi-category model of∞-category theory [Jo]. Board-
man & Vogt ﬁrst introduced these simplicial sets in [BV], as weak Kan co mplexes, and their and
Joyal’s theory has been developed in great depth by Lurie in [Lu1] and [Lu2], our primary references;
see the ﬁrst chapter of [Lu1] for an introduction. We use this mode l, rather than model categories or
simplicial categories, because of the great technical advantages for constructions involving categories
of functors, which are ubiquitous in this work. More speciﬁcally, we w ork inside of the quasi-category
associated to this model category of Joyal’s. In particular, each m ap between quasi-categories is
understood to be an iso- and inner-ﬁbration; and (co)limits among q uasi-categories are equivalent
to homotopy (co)limits with respect to Joyal’s model structure.
We will also make use of Kan-enriched categories, such as Snglr of stratiﬁed spaces and conically
smooth embeddings among them. By a functor S→ C to an ∞-category from a Kan-enriched
category we will always mean a functor NS→ C from the simplicial nerve of S.
The reader uncomfortable with the language of ∞-categories can substitute the words “topologi-
cal category” for “∞-category” wherever they occur in this paper to obtain the corre ct sense of the
results, but they should then bear in mind the proviso that technica l diﬃculties may then abound
in making the statements literally true. The reader only concerned w ith algebra in chain com-
plexes, rather than spectra, can likewise substitute “pre-triang ulated diﬀerential graded category”
for “stable∞-category” wherever those words appear, with the same proviso .
Acknowledgements. We are indebted to Kevin Costello for many conversations and his man y
insights which have motivated and informed the greater part of this work. We also thank Jacob
5
Lurie for illuminating discussions, his inspirational account of topolog ical ﬁeld theories, and his
substantial contribution to the theory of ∞-categories. JF thanks Alexei Oblomkov for helpful
conversations on knot homology.
