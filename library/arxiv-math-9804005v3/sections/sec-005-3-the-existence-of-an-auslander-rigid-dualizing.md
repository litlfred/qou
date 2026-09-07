---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-005-3-the-existence-of-an-auslander-rigid-dualizing
section_title: "The existence of an Auslander rigid dualizing complex is transferre d to related"
section_number: 3
pages: 4-6
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
algebras (Propositions 4.18 and 4.20, Corollaries 4.17, 5.10 and 5.11).
The canonical dimension, denoted by Cdim, is deﬁned when A has an Auslan-
der dualizing complex (Deﬁnition 2.9). It is an exact ﬁnitely partitive dim ension
function (Theorem 2.10). Local duality implies that the canonical dim ension is
symmetric in the graded case (Proposition 4.13). Therefore if A is a connected
graded algebra with an Auslander balanced dualizing complex, the can onical di-
mension Cdim is exact, ﬁnitely partitive, and symmetric on graded mod ules. Note
that the Krull dimension, denoted by Kdim, is exact and ﬁnitely partit ive, but it is
unknown whether it is symmetric. On the other hand Gelfand-Kirillov d imension,
denoted by GKdim, is symmetric, but neither exact nor ﬁnitely partit ive in general.
Hence the canonical dimension is the better dimension function – at le ast in the
graded or ﬁltered case.
The study of dualizing complexes over noncommutative rings presen ts many
interesting and subtle questions. We conclude the introduction by m entioning two
of them:
Question 0.10. Which (noetherian, aﬃne) k-algebras have (rigid) dualizing com-
plexes?
Question 0.11. Is a rigid dualizing complex is always Auslander?
Acknowledgments. We thank M. Artin and M. Van den Bergh for many useful
conversations and email correspondences.
1. Dualizing complexes
Letk be a ﬁeld and let A be an associative k-algebra with 1. All A-modules will
be by default left modules, and we denote by ModA the category of left A-modules.
Let A◦ be the opposite algebra, and let Ae := A ⊗A◦ where ⊗ = ⊗k. Thus an
Ae-module M is, in the conventional notation, an A-A-bimodule AMA central over
k. Most of our deﬁnitions and results have a left-right symmetry, ex pressible by
the exchange A ↔ A◦. Since these symmetries are evident we shall usually not
mention them.
RINGS WITH AUSLANDER DUALIZING COMPLEXES 5
Let D(ModA) be the derived category of A-modules, and let D⋆(ModA), for
⋆ = b, +, − or blank, be the full subcategories of bounded, bounded below, bo unded
above, or unbounded complexes respectively [RD].
Given another k-algebra B, the forgetful functor Mod(A ⊗B◦) → ModA is
exact, and so induces a functor D⋆(Mod(A ⊗B◦)) → D⋆(ModA). Now A ⊗B◦ is
a projective A-module, so any projective (resp. ﬂat, injective) ( A ⊗B◦)-module is
projective (resp. ﬂat, injective) over A.
Consider k-algebras A,B,C . For complexes M ∈ D(Mod(A ⊗B◦)) and N ∈
D(Mod(A ⊗C◦)), with either M ∈ D− or N ∈ D+, there is a derived functor
R HomA(M,N ) ∈ D(Mod(B ⊗C◦)).
It is calculated by replacing M with an isomorphic complex in D−(Mod(A ⊗B◦))
which consists of projective modules over A; or by replacing N with an isomorphic
complex in D+(Mod(A ⊗C◦)) which consists of injective modules over A. For full
details see [RD] and [Ye1]. Note that for modules M and N , viewed as complexes
concentrated in degree 0, one has
HqR HomA(M,N ) = Extq
A(M,N ),
the latter being the usual Ext.
Because the forgetful functors Mod(A ⊗ B◦) → ModA etc. commute with
R HomA(−, −) there is no need to mention them explicitly.
A complex N ∈ D+(ModA) is said to have ﬁnite injective dimension if there is
an integer q0 with Extq
A(M,N ) = 0 for all q >q0 and M ∈ ModA.
For the rest of this section A denotes a left noetherian k-algebra and B denotes
a right noetherian k-algebra. (For instance we could take A = B a two-sided
noetherian algebra.) Observe that the algebra A ⊗B◦ need not be left noetherian.
The subcategory ModfA of ﬁnitely generated A-modules is abelian and closed
under extensions. Hence there is a full triangulated subcategory Df (ModA) ⊂
D(ModA) consisting of all complexes with ﬁnitely generated cohomologies.
Dualizing complexes over commutative rings were introduced in [RD]. Th e non-
commutative graded version ﬁrst appeared in [Ye1], and we now give a slightly
more general version.
Deﬁnition 1.1. Assume A and B are k-algebras, with A left noetherian and B
right noetherian. A complex R ∈ Db(Mod(A ⊗B◦)) is called a dualizing complex if
it satisﬁes the three conditions below:
(i) R has ﬁnite injective dimension over A and B◦.
(ii) R has ﬁnitely generated cohomology modules over A and B◦.
(iii) The canonical morphisms B → R HomA(R,R ) in D(ModBe), and A →
R HomB◦ (R,R ) in D(ModAe), are both isomorphisms.
In case A =B, we shall say that R is a dualizing complex over A.
Condition (i) is equivalent to having an isomorphism R ∼=I ∈ Db(ModA ⊗B◦),
where each Iq is injective over A and over B◦.
Example 1.2. Suppose A is commutative and R is a dualizing complex in the
sense of [RD]. If we consider R as a complex of bimodules, by identifying A =A◦,
then R is a dualizing complex in the sense of the deﬁnition above. According to
[Ye3], if SpecA is connected, then any dualizing complex R′ overA is isomorphic to
R ⊗AP [n], where P is an invertible bimodule (not necessarily central!) and n ∈ Z.
