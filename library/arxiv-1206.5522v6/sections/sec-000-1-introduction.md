---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-6
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
2. B-framed disks and manifolds 6
2.1. B-framings 6
2.2. Disks 9
2.3. Manifolds with boundary 11
2.4. Localizing with respect to isotopy equivalences 12
3. Homology theories for topological manifolds 14
3.1. Disk algebras 14
3.2. Factorization homology over oriented 1-manifolds with boundar y 17
3.3. Homology theories 18
3.4. Pushforward 19
3.5. Homology theories 23
4. Nonabelian Poincar´ e duality 26
5. Commutative algebras, free algebras, and Lie algebras 28
5.1. Factorization homology with coeﬃcients in commutative algebras 28
5.2. Factorization homology with coeﬃcients in free n-disk algebras 31
5.3. Factorization homology from Lie algebras 35
References 36
2010 Mathematics Subject Classiﬁcation. Primary 55N40. Secondary 57R56, 57N35.
Key words and phrases. Factorization algebras. En-algebras. Topological quantum ﬁeld theory. Topological c hiral
homology. Koszul duality. Little n-disks operad. ∞-Categories. Goodwillie–W eiss manifold calculus.
DA was partially supported by ERC adv.grant 228082 and by the National Science Foundation under Award
0902639. JF was supported by the National Science Foundatio n under award 0902974 and 1207758; part of the
writing was completed while JF was a visitor at Universit´ e P ierre et Marie Curie in Jussieu as a guest of the
Foundation Sciences Math´ ematiques de Paris.
1
1. Introduction
Factorization homology takes an algebraic input, either an n-disk algebra or more generally a
stack over n-disk algebras, and outputs a homology-type theory for n-dimensional manifolds. In the
case where the input coeﬃcients are an n-disk algebra, this factorization homology – the topological
chiral homology introduced by Lurie [Lu2] – satisﬁes an analogue of t he axioms of Eilenberg and
Steenrod. This work proves this statement and some consequenc es aﬀorded by this point of view.
While the subject of factorization homology is new, at least in name, it has important roots
and antecedents. Firstly, it derives from the factorization algebr as of Beilinson and Drinfeld [BD],
a profound and elegant algebro-geometric elaboration on the role o f conﬁguration space integrals
in conformal ﬁeld theory. Our work is in essence a topological versio n of theirs, although the
topological setting allows for arguments and conclusions ostensibly unavailable in the algebraic
geometry. Secondly, it has an antecedent in the labeled conﬁgurat ion space models of mapping
spaces dating to the 1970s; it is closest to the models of Salvatore [ Sa] and Segal [Se3], but see also
[Ka], [B¨ o], [Mc], [Ma], and [Se1]. Factorization homology thus lies at the br oad nexus of Segal’s
ideas on conformal ﬁeld theory [Se2] and his ideas on mapping spaces articulated in [Se1] and [Se3].
In keeping with these two directions, we oﬀer two primary motivation s for the study of factor-
ization homology. Returning to our ﬁrst point, factorization homolo gy with coeﬃcients in n-disk
algebras are homology theories for topological manifolds satisfying a generalization of the Eilenberg–
Steenrod axioms for ordinary homology; as such, it generalizes ord inary homology in a way that is
only deﬁned on n-manifolds and not necessarily on arbitrary topological spaces. Se cond, these ho-
mology theories deﬁne topological quantum ﬁeld theories. Following t he vision of Costello–Gwilliam
[CG], factorization homology with coeﬃcients in n-disk stacks oﬀers an a algebraic model for the
observables in a general topological quantum ﬁeld theory. The spe cial case of n-disk algebra coef-
ﬁcients corresponds to n-dimensional ﬁeld theories whose global observables are determine d by the
local observables, as in a perturbative quantum ﬁeld theory.
We ﬁrst elaborate on the homology theory motivation, which serves as the main artery running
through this work. One can pose the following question: what can a h omology theory for topological
manifolds be? Singular homology, of course, provides one answer. O ne might not want it to be the
only answer, since singular homology is not speciﬁc to manifolds and ca n be equally well deﬁned
for all topological spaces; likewise, it is functorial with respect to a ll maps of spaces, not just those
that are speciﬁcally meaningful for manifolds (such as embeddings o r submersions). One could
thus ask for a homology theory which is speciﬁc to manifolds, not deﬁ ned on all spaces, and which
might thereby distinguish manifolds which are homotopic but not home omorphic and distinguish
embeddings that are homotopic but not isotopic through embedding s. That is, one could ask for a
homology theory for manifolds that can detect the more reﬁned an d interesting aspects of manifold
topology. The question then becomes, do such homology theories e xist?
One might address this question by ﬁrst making it more precise, by de ﬁning exactly what one
means by a homology theory for manifolds; since we know what a homo logy theory for spaces
constitutes, by the Eilenberg–Steenrod axioms, one might simply mo dify those axioms as little as
possible, but so as to work only for manifolds and with the maximum pos sibility that new theories
might arise.
Reformulating the Eilenberg–Steenrod axioms slightly, one can think of an ordinary homology
theory F as a functor Spacesﬁn→ Ch from the topological category of spaces homotopy equivalent
to ﬁnite CW complexes to the topological category of projective ch ain complexes 1 satisfying two
conditions:
• The canonical morphism ⨁
J F(Xα)→ F(∐
J Xα) is an equivalence for any ﬁnite set J;
1There is the standard functor | MapCh
( C∗ (∆ • ),−) | : Ch → Top to topological spaces given by the Dold–Kan
correspondence. While this functor does not send tensor pro duct to Cartesian product, it does so up to a coherent
natural transformation. The internal hom-objects of Ch thus give a topological enrichment.
2
• Excision: for any diagram of coﬁbrations of spaces X ′←֒→X ′′, the resulting map of
chain complexes
F(X ′) ⊕
F(X)
F(X ′′)−→ F
(
X ′⊔
X
X ′′
)
is a quasi-isomorphism.
The ﬁrst condition can be restated as saying that the functor F is symmetric monoidal with
respect to the disjoint union and direct sum. Let H(Spaces, Ch⊕) stand for the collection of such
functors. The Eilenberg–Steenrod axioms for ordinary homology c an then be reformulated as follows.
Theorem 1.1 (Eilenberg–Steenrod). Evaluation on a point, ev∗ : H(Spaces, Ch⊕)→ Ch, deﬁnes
an equivalence between homology theories valued in chain co mplexes with direct sum and chain
complexes. The inverse is given by singular homology, the fu nctor assigning to a chain complex V
the functor C∗(−, V ) of singular chains with coeﬃcients in V .
In particular, each homology theory F is equivalent to the functor of singular chains with coeﬃ-
cients in the chain complex F(∗), which is the value of F on the singleton: C∗(−, F(∗))≃ F. Further,
every natural transformation of homology theories F→ F′ is determined by the map F(∗)→ F′(∗).
To adapt this deﬁnition to manifolds, we make two substitutions:
(1) We replace Spacesﬁn with Mﬂdn, the collection of topological n-manifolds, not necessarily
closed but with suitably ﬁnite covers, with embeddings as morphisms.
(2) We replace the target Ch⊕ by a general symmetric monoidal ∞-category V.
As so, we deﬁne H(Mﬂdn, V) to be the collection of all symmetric monoidal functors from Mﬂdn to
V that satisfy a monoidal version of excision. We arrive at the following analogue of the Eilenberg–
Steenrod axioms, for V a symmetric monoidal∞-category satisfying a technical condition (Deﬁnition
3.4).
Theorem 1.2. There is an equivalence between homology theories for topol ogical n-manifolds valued
in V and n-disk algebras in V
∫
: AlgDiskn (V) /d47/d47 H(Mﬂdn, V) : evRn ./d111/d111
This equivalence is implemented by the factorization homol ogy functor
∫
from the left, and evaluation
on Rn from the right.
The n-disk algebras appearing in the theorem are equivalent to the En-algebras of Boardman and
Vogt [BV] together with an extra compatible action of the group of a utomorphisms of Rn. Thus, at
ﬁrst glance, this result appears diﬀerent and more complicated tha n the Eilenberg–Steenrod axioms
because the characterization as V alone has been replaced by n-disk algebras in V. This is for two
reasons, each of substance. For one, the object Rn has more structure than a singleton; for instance,
automorphisms of Rn form an interesting and noncontractible space, whereas the auto morphisms
of a singleton is just a point. Secondly, the symmetric monoidal stru cture of V is not necessarily
the coproduct, so there need not be a canonical map V ⊗ V → V for each object V ∈ V; this
allows for a multiplicative form of homology. Nonetheless, our result d oes specialize to Eilenberg
and Steenrod’s, as we shall see in Example 3.28. In particular, in the e xample V = Ch⊕, these
n-disk algebras are equivalent to just chain complexes with an action o f the automorphisms of Rn,
and these homology theories are then just ordinary homology twist ed by the tangent bundle.
This result has a number of immediate applications and leads to new pro ofs of known results.
For instance, it gives a one line proof that factorization homology of the circle, in the case V is chain
complexes with tensor product, is Hochschild homology. It also gives a new and short proof of the
nonabelian Poincar´ e duality of Salvatore [Sa], Segal [Se3], and Lurie [L u2]. We give further results
and computations in Section 5.
The second motivation for factorization homology comes from math ematical physics. In the
various axiomatics for topological quantum ﬁeld theory after Sega l [Se2], one restricts to compact
3
manifolds, possibly with boundary; the locality of a quantum ﬁeld theo ry is then reﬂected in the
functoriality of gluing cobordisms. However, it is frequently possible to deﬁne a quantum ﬁeld
theory on noncompact manifolds, such as Euclidean space. Since th ere are more embeddings between
general noncompact manifolds than between closed manifolds, one might then expect the axiomatics
of this situation to be slightly diﬀerent were one to account for the s tructure in which one can restrict
a ﬁeld, or extend an observable, along an open embedding֒→M ′.
Our notion of a homology theory for manifolds is thus simultaneously a n attempt to axiomatize
the structure of the observables in a quantum ﬁeld theory which is t opologically invariant – here
the⊗-excision of the homology theory becomes a version of the locality of the ﬁeld theory – and
Theorem 3.24 becomes an algebraic characterization of part of the structure of such quantum ﬁeld
theories. There is another characterization of extended topolog ical ﬁeld theories, namely the Baez–
Dolan cobordism hypothesis, Lurie’s proof of which is outlined in [Lu3], building on earlier work
with Hopkins and inspired by ideas of Costello [Cos]. These two charact erizations are comparable
in several ways. In particular, there is a commutative diagram
AlgDisksm
n
(V)∼
∫
/d15/d15
/d47/d47 (
Algn(V)∼) O(n)
Z
/d15/d15
H(Mﬂdsm
n , V)∼ /d47/d47 Fun⊗(Bordsm
n , Algn(V)) .
This picture should be understood only as impressionistic, and we brie ﬂy explain the terms in
this picture (see §4.1 of [Lu3] for more explanation): Disksm
n and Mﬂdsm
n are the ∞-categories of
smooth n-disks and n-manifolds with smooth embeddings; Bordsm
n is the (∞, n)-category of smooth
bordisms of manifolds from [Lu3]; and Algn(V) is the higher Morita category, where k-morphisms are
Diskfr
n−k-algebras in bimodules; the superscript ( −)∼ denotes underlying ∞-groupoids, discarding
non-invertible morphisms. The bottom horizontal functor from ho mology theories valued in V to
topological quantum ﬁeld theories valued in Algn(V), assigns to a homology theory F the functor
on the bordism category sending a k-manifold M with corners to F(M ◦× Rn−k), the value of F on
a collar-thickening of M .
Our characterization of homology theories can thereby be seen as an analogue of the cobordism
hypothesis for the observables in a topological quantum ﬁeld theor y where one allows for noncompact
manifolds and a strong locality principle by which local observables det ermine global observables. 2
Not all topological ﬁeld theories come from such homology theories, and the question of which do and
do not is an interesting one. Costello and Gwilliam use closely related idea s in studying more general
quantum ﬁeld theories which are not topologically invariant, and the s etting of their work suggests
that perturbative quantum ﬁeld theories are exactly those amena ble to this characterization; see
[CG] and [Gw]. The structure of observables of a topological quantu m ﬁeld theory which is not
perturbative is better described by a generalization of factorizat ion homology with coeﬃcients given
by a stack over n-disk algebras [Fra1], e.g., an algebraic variety X whose ring of functions OX is
enhanced to have a compatible structure of an n-disk algebra.
Factorization homology and related ideas have recently become the subject of closer study; in
addition to Lurie’s originating work, see [Lu2] and [Lu3], and Costello an d Gwiliam [CG], see also
[An], [GTZ2], [Gw], and [MW]. We expect the theory of factorization homo logy to be a source
of interesting future mathematics and to carry many important ma nifold invariants. Especially
fertile ground lies in low-dimensional topology, in the study of 3-manif old and knot invariants,
where invariants stemming from the homology of conﬁguration spac es are already prevalent. This
2There is a slight, but interesting, diﬀerence in that the hom ology theory characterization applies successfully
to topological manifolds (as well as piecewise linear or smo oth), whereas the cobordism hypothesis requires that
the manifolds involved have at least a piecewise linear stru cture; the absence of triangulations for nonsmoothable
topological 4-manifolds appears as a genuine obstruction.
4
is a source of work joint with Tanaka in [AFT2], where we construct fa ctorization knot homology
theories from a 3-disk algebra with extra structure.
It is a compelling general question as to how much of manifold topology can be captured by
factorization homology; this question is closely related to the Goodw illie–Weiss manifold calculus
[We]. Factorization homology of M is determined by an object EM , the presheaf of spaces on n-disks
determined by embeddings into M , which is an a priori weaker invariant of M than M itself. EM
encodes the homotopy type of M , the homotopy type of all higher conﬁguration spaces Conf j(M )
of M , and the tangent bundles T Conf i(M ), as well as coherence data relating these, and it would
be very interesting to know when this is suﬃcient to reconstruct M .
Implementation of ∞-categories. In this work, we use Joyal’s quasi-category model of ∞-
category theory [Jo]. Boardman and Vogt ﬁrst introduced these s implicial sets in [BV], as weak
Kan complexes, and their and Joyal’s theory has been developed in gr eat depth by Lurie in [Lu1]
and [Lu2], our primary references; see the ﬁrst chapter of [Lu1] f or an introduction. We use this
model, rather than model categories or simplicial categories, beca use of the great technical advan-
tages for constructions involving categories of functors, which a re ubiquitous in this work.
More speciﬁcally, we work inside of the quasi-category associated t o this model category of Joyal’s.
In particular, each map between quasi-categories is understood t o be an iso- and inner-ﬁbration;
(co)limits among quasi-categories are equivalent to homotopy (co) limits with respect to Joyal’s
model structure. As we work in this way, we refer the reader to th ese sources for ∞-categorical
versions of numerous familiar results and constructions among ord inary categories. To point, we
will make repeated use of the ∞-categorical adjoint functor theorem (Corollary 5.5.2.9 of [Lu1]); the
straightening-unstraightening equivalence between Cartesian ﬁb rations over an ∞-category C and
Cat∞-valued contravariant functors from C (Theorem 3.2.0.1 of [Lu1]), and likewise between right
ﬁbrations over C and space-valued presheaves on C (Theorem 2.2.1.2 of [Lu1]); the ∞-categorical
version of the Yoneda functor C→ PShv(C)≃ RFibC as it evaluates on objects as c↦→C/c (see §5.1
of [Lu1]).
We will also make use of topological categories, such as Mﬂdn of n-manifolds and embeddings
among them. By a functor S→ C from a topological category to an ∞-category C we will always
mean a functor N Sing S→ C from the simplicial nerve of the Kan-enriched category obtained by
applying the product preserving functor Sing to the morphism topological spaces.
The reader uncomfortable with this language can substitute the wo rds “topological category”
for “∞-category” wherever they occur in this paper to obtain the corre ct sense of the results, but
they should then bear in mind the proviso that technical diﬃculties ma y then abound in making
the statements literally true. The reader only concerned with algeb ras in chain complexes, rather
than spectra, can likewise substitute “pre-triangulated diﬀerent ial graded category” for “stable ∞-
category” wherever those words appear, with the same proviso.
Notation.
• Spaces is the∞-category of spaces. This ∞-category has numerous constructions and char-
acterizations: as the Kan-enriched category of Kan complexes; as the free small colimit
completion of the terminal ∞-category∗; and as ∞-groupoids.
• Diskn and Mﬂdn are ordinary categories of manifolds with embeddings; Diskn and Mﬂdn
are topological categories of manifolds with embeddings, where the spaces of embeddings
carry the compact-open topology. See Deﬁnition 2.18 versus Deﬁn ition 2.1.
• Top(n) is the topological group of homeomorphisms of Rn, endowed with the compact-open
topology.
• After Deﬁnition 2.7, we ﬁx a space B with a map B→ BTop(n) and consider B-framed
n-manifolds. Any occurrence of B thereafter refers to this choice.
• We use colim and lim to denote colimits and limits in ∞-categories, which correspond to
homotopy colimits and limits in topological categories or model categories. (In t he one or
5
two places where we use a point-set colimit, we employ unmistakeably j arring notation to
distinguish the two.)
• For k a ring we use the notation Modk for the ∞-category of k-modules. This is an ∞-
category associated to the diﬀerential graded category of chain complexes over k. (See §1.3
of [Lu2] for a thorough account.) We will sometimes use the notation Chk for this ∞-
category, and should k be the integers we drop it from the subscript.
• En will stand for the topological operad of little n-cubes, as deﬁned in [BV].
• C∗(X) is the singular chains on a topological space X.
• Sym(V ) is the free commutative algebra on an object V of a symmetric monoidal∞-category.
In a symmetric monoidal ∞-category, commutative algebras are equivalent to E∞-algebras,
so Sym(V ) is also the free E∞-algebra on V .
• For X∈ X an object of an ∞-category, we notate X/X and XX/ for the over- and under-
∞-categories. For ( A→ X) and ( B→ X) two objects of X/X , we may denote the space of
morphisms from the ﬁrst to the second as Map/X (A, B).
Acknowledgments 1.3. JF foremost thanks Kevin Costello for many conversations on this s ub-
ject, which have motivated and clariﬁed this work, from Theorem 3.2 4 to the computations of the
following sections, and without which JF likely would not have pursued it . Our joint works with
Hiro Lee Tanaka build and improve on many of the ideas here, and we th ank him for his collabo-
ration. JF ﬁrst learned the basic idea of factorization homology in co nversations with Jacob Lurie
and Dennis Gaitsgory in 2007, and we have both beneﬁtted greatly f rom their generosity in sharing
many other insights in these intervening years. JF thanks Sasha Be ilinson and Mike Hopkins for
their great inﬂuence which has shaped his thoughts on this subject . We also thank Gr´ egory Ginot
and Owen Gwilliam for helpful conversations and Pranav Pandit for co mments on an earlier draft
of this paper. We thank Amabel Wilson and Theo Johnson–Freyd for correcting the hypotheses in
the statement of Proposition 5.3. Finally, we thank the anonymous r eferee whose careful feedback
has considerably improved this article.
