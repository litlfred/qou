---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
2 Preliminaries 5
2.1 Lie Groupoids and Groupoid Actions on Manifolds . . . . . . . . . . . . . . . . . . . 5
2.2 Principal Groupoid Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Anafunctors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.4 Lie 2-Groups and crossed Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3 V ersion I: Groupoid-valued Cohomology 16
4 V ersion II: Classifying Maps 18
5 V ersion III: Groupoid Bundle Gerbes 21
5.1 Deﬁnition via the Plus Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
5.2 Properties of Groupoid Bundle Gerbes . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.3 Classiﬁcation by ˇCech Cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
6 V ersion IV: Principal 2-Bundles 33
6.1 Deﬁnition of Principal 2-Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
6.2 Properties of Principal 2-Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
7 Equivalence between Bundle Gerbes and 2-Bundles 38
7.1 From Principal 2-Bundles to Bundle Gerbes . . . . . . . . . . . . . . . . . . . . . . . 39
7.2 From Bundle Gerbes to Principal 2-Bundles . . . . . . . . . . . . . . . . . . . . . . . 48
A Equivariant Anafunctors and Group Actions 57
B Constructing Equivalences between 2-Stacks 59
References 62
1 Introduction
Let G be a Lie group and M be a smooth manifold. There are (among others) the following four
ways to say what a smoothG-bundle overM is:
(1) ˇCech 1-Cocycles : an open cover {Ui} of M , and for each non-empty intersection Ui ∩Uj a
smooth map gij :Ui ∩Uj /d47/d47 G satisfying the cocycle condition
gij ·gjk =gik.
(2) Classifying maps : a continuous map
f :M /d47/d47 BG
to the classifying space BG of the group G.
(3) Bundle 0-gerbes : a surjective submersion π :Y /d47/d47 M and a smooth map g :Y ×M Y /d47/d47 G
satisfying
π∗
12g ·π∗
23g =π∗
13g,
– 2 –
whereπij :Y ×MY ×MY /d47/d47 Y ×MY denotes the projection to the ith and the jth factors.
(4) Principal bundles : a surjective submersion π :P /d47/d47 M with a smooth action of G on P that
preservesπ, such that the map
P ×G /d47/d47 P ×M P : (p,g ) ✤ /d47/d47 (p,p.g )
is a diﬀeomorphism.
It is well-known that these four versions of “smooth G-bundles” are all equivalent. Indeed, (1)
forms the smooth G-valued ˇCech cohomology in degree one, whereas (2) is known to be equivalen t
to continuous G-valued ˇCech cohomology, which in turn coincides with the smooth G-valued ˇCech
cohomology. Further, (3) and (4) form equivalent categories; an d isomorphism classes of the objects
(3) are in bijection with equivalence classes of the cocycles (1).
In this article we provide an analogous picture for smooth Γ -gerbes, where Γ is a strict Lie
2-group. In particular, Γ can be the automorphism 2-group of an o rdinary Lie group G, in which
case the term “non-abelian G-gerbe” is commonly used. We compare the following four versions:
Version I: Smooth, non-abelian ˇCech Γ -cocycles (Deﬁnition 3.6). These form the classical, smooth
groupoid-valued cohomology ˇH1(M, Γ) in the sense of Giraud [Gir71] and Breen [Bre90, Ch.
4], [Bre94].
Version II: Classifying maps (Deﬁnition 4.4). These are continuous maps f : M /d47/d47 B|Γ | to the
classifying space of the geometric realization of Γ; such maps have b een introduced and studied
by Baez and Stevenson [BS09].
Version III: Γ -bundle gerbes (Deﬁnition 5.1.1). These have been developed by Aschieri, Cantini
and Jurco [ACJ05] as a generalization of the abelian bundle gerbes of Murray [Mur96].
Here we present an equivalent deﬁnition by applying a higher categor ical version [NS11] of
Grothendieck’s stackiﬁcation construction to the monoidal pre-2 -stack of principal Γ-bundles.
Version IV: Principal Γ -2-bundles (Deﬁnition 6.1.5). These have been introduced by Bartels
[Bar04]; their total spaces are Lie groupoids on which the Lie 2-grou p Γ acts in a certain
way. Compared to Bartels’ deﬁnition, ours uses a stricter and eas ier notion of such an action.
We prove that all four versions are equivalent, and follow the same lin e of arguments as in the case
of G-bundles outlined above:
• Baez and Stevenson have shown that homotopy classes of classify ing maps of Version II
are in bijection with the continuous groupoid-valued ˇCech cohomology ˇH1
c (M, Γ). We prove
(Proposition 4.1) that the inclusion of smooth into continuous ˇCech Γ-cocycles induces a
bijection ˇH1
c (M, Γ) ∼= ˇH1(M, Γ). These two results establish the equivalence between our
Versions I and II (Theorem 4.6).
– 3 –
• Γ-bundle gerbes and principal Γ-2-bundles over M form bicategories. We prove (Theorem
7.1) that these bicategories are equivalent, and so establish the eq uivalence between Versions
III and IV. Our proof provides explicit 2-functors in both direction s.
• We prove the equivalence between Versions I and III by showing tha t non-abelian Γ-bundle
gerbes are classiﬁed by the non-abelian cohomology group ˇH1(M, Γ) (Theorem 5.3.2).
The ﬁrst aim of this paper is to simplify and clarify the notion of a non-a belian gerbe. This
concerns the notion of a Γ-bundle gerbe (Version III), for which w e give a new, conceptually
clear, and manifestly 2-categorical deﬁnition. It also concerns th e notion of a principal 2-bundle
(Version IV), for which we provide a new deﬁnition that is carefully ba lanced between generality
and simplicity.
The second aim of this paper is to make it possible to compare and tran sfer available results
between the various versions. Indeed, none of the three equivale nces above is available in the
existing literature. As an example why such equivalences can be usef ul, we use Theorem 7.1 – the
equivalence between Γ-bundle gerbes and principal Γ-2-bundles – in order to carry two facts about
Γ-bundle gerbes over to principal Γ-2-bundles. We prove:
1. Principal Γ-2-bundles form a 2-stack over smooth manifolds (Th eorem 6.2.1). This is a new
and evidently important result, since it explains precisely in which way o ne can glue 2-bundles
from local patches.
2. If Γ and Ω are weakly equivalent Lie 2-groups, the 2-stacks of pr incipal Γ-2-bundles and prin-
cipal Ω-2-bundles are equivalent (Theorem 6.2.3). This is another ne w result that generalizes
the well-known fact that principal G-bundles and principal H-bundles form equivalent stacks,
wheneverG and H are isomorphic Lie groups.
The two facts about Γ-bundle gerbes (Theorems 5.1.5 and 5.2.2) on w hich these results are based
are proved in an outmost abstract way: the ﬁrst is a mere consequ ence of the deﬁnition of Γ-bundle
gerbes that we give, namely via a 2-stackiﬁcation procedure for pr incipal Γ-bundles. The second
follows from the fact that principal Γ-bundles and principal Ω-bund les form equivalent monoidal
pre-2-stacks, which we deduce as a corollary of their description b y anafunctors.
The present paper is part of a larger program. In a forthcoming pa per, we address the discussion
of non-abelian lifting problems, in particular string structures. In a second forthcoming paper
we will present the picture of four equivalent versions in a setting with connections , based on
the results of the present paper. Our motivation is to understand the role of 2-bundles with
connections in higher gauge theories, where they serve as “B-ﬁeld s”. Here, two (non-abelian) 2-
groups are especially important, namely the string group [BCSS07] a nd the Jandl group [NS11].
More precisely, string-2-bundles appear in supersymmetric sigma m odels that describe fermionic
– 4 –
string theories [Bun11]; while Jandl-2-bundles appear in unoriented s igma models that describe e.g.
bosonic type-I string theories [SSW07].
This paper is organized as follows. In Section 2 we recall and summariz e the theory of principal
groupoid bundles and their description by anafunctors. The rest o f the paper is based on this
theory. In Sections 3, 4, 5 and 6 we introduce our four versions of smooth Γ-gerbes, and establish
all but one equivalence. The remaining equivalence, the one between bundle gerbes and principal
2-bundles, is discussed in Section 7.
Acknowledgements. We thank Christoph Wockel for helpful discussions. We also thank t he
Erwin Schr¨ odinger Institute in Vienna and the Instituto Superior T´ ecnico in Lisbon for kind invita-
tions. TN is supported by the Collaborative Research Centre 676 “P articles, Strings and the Early
Universe - the Structure of Matter and Space-Time” and the clust er of excellence “Connecting
particles with the cosmos”.
