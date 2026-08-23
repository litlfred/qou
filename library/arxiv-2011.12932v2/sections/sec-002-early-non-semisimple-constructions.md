---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-002-early-non-semisimple-constructions
section_title: "Early non-semisimple constructions"
section_number: null
pages: 3-20
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogythatthenotionofmodularcategorywasanappropriatestructureforbuild- ing"
---
diately sparked a wide interest in the newly born ﬁeld of quantum topology, and
some natural questions quickly emerged. First of all, is it possible to ﬁgure out
the relevant combinatorics for elements of ribbon Hopf algebras arising from the
construction of [53] without relying on their representation theory? Answering this
question required learning how to deal with Hopf algebras themselves, which, in the
relevant family of concrete examples, are not semisimple, and thus are not com-
pletely determined by their simple modules. Therefore, another natural question
was: can we relax the semisimplicity requirement of Turaev? Lawrence explained
in [38] how to construct so-calleduniversal link invariantsusing directly quantum
groups, and thus bypassing their representation theory. These ideas were expanded
by Hennings [29], who upgraded Lawrence’s construction to obtain invariants of
closed oriented 3-manifolds starting from ﬁnite-dimensional factorizable2 ribbon
Hopf algebras. Since semisimplicity was no longer required, this constituted the
ﬁrst non-semisimple generalization of Reshetikhin–Turaev invariants, and the start
of non-semisimple quantum topology. Hennings’ result was reformulated by Kauﬀ-
man and Radford avoiding the use of orientations for framed links [37]. Both of
these constructions were extended by Lyubashenko, who proposed a more general
deﬁnition of modular category with respect to Turaev’s original one, and used it to
build topological invariants of 3-manifolds and projective representations of map-
ping class groups of surfaces [41]. For such a modular categoryC, which is allowed
to be non-semsimple, we denote withLC the corresponding Lyubashenko invari-
ant of closed oriented 3-manifolds. The main families of examples are provided by
categories of ﬁnite-dimensional representations of small quantum groups, without
quotient operations. In Section 8, we discuss the case of¯Uqsl2.
Lyubashenko’s work raised again some natural questions:
(i) Since this construction produces all the desired byproducts one expects
to obtain from a TQFT, is there actually a TQFT lying behind them?
(ii) Given that the loss of algebraic information is successfully avoided, do we
get ﬁner topological invariants and mapping class group representations?
A few results which appeared in the early stages of the development of this new
approach seemed to suggest negative answers to both questions. More precisely, it
was ﬁrst shown by Ohtsuki in a special case [49], and later by Kerler in general
[34], that ifC is a non-semisimple modular category, and ifM is a closed oriented
3-manifold with ﬁrst Betti numberb1(M)> 0, then
LC(M) = 0.
This is a deep obstruction for the deﬁnition of TQFT extensions. Indeed, it is a
standard consequence of symmetric monoidality that the dimension of the state
space VC(Σ) of a closed oriented surfaceΣ for a TQFTVC extending LC is
dimk VC(Σ) = LC(Σ×S1).
This means that Lyubashenko’s invariant associated with a non-semisimple modu-
lar category C cannot be extended to a TQFT, at least not in the sense of Atiyah.
2Factorizability is the appropriate non-degeneracy condition for ribbon Hopf algebras in the
non-semisimple setting, see Section 6.
4 C. BLANCHET AND M. DE RENZI
For years, the most involved achievement in a non-semisimple setting was a re-
sult of Lyubashenko and Kerler [35] which produces a partial version of an Ex-
tended TQFT (ETQFT for short) satisfying only weak monoidality properties.3
Furthermore, it was later shown that, at least for small quantumsl2, Hennings and
Lyubashenko’s invariants can be expressed as functions of Witten–Reshetikhin–
Turaev ones [14]. More precisely, if C is the category of ﬁnite-dimensional rep-
resentations of ¯Uqsl2, and if ¯C is the semisimple quotient ofC inducing Witten’s
invariants, then for every 3-manifoldM we have
LC(M) =h1(M)RT¯C(M),
where h1(M) =|H1(M)| if b1(M) = 0, andh1(M) = 0 if b1(M) > 0. Because of
these hurdles, these deep works were underestimated for quite some time. This is
not to say that the constructions were forgotten, as the number of publications con-
taining reviews of Hennings’ approach witnesses [33, 60, 28]. However, a feeling that
no additional topological information could be accessed through non-semisimple
generalizations of Reshetikhin and Turaev’s work started to spread.
Renormalizednon-semisimpleconstructions. Akeyingredientthatwasmiss-
ing from these early attempts at non-semisimple constructions was the theory of
modiﬁed tracesdeveloped by Geer and Patureau together with many collaborators,
among which Turaev [26], Kujawa [24], and Virelizier [27]. Indeed, one way to ex-
plain the problems we face when trying to generalize Turaev’s TQFT construction
is that the categorical trace operation, which associates scalars to endomorphisms
in a ribbon categoryC, becomes highly degenerate as soon asC is non-semisimple.
For instance, in this case the categorical trace of every endomorphism of any pro-
jective object is zero. Since this operation is pervasive in all quantum topological
constructions, invariants of closed oriented 3-manifolds are bound to vanish a lot
in non-semisimple settings. The idea behindrenormalization consists in replacing
this highly degenerate operation with a non-degenerate analogue, called modiﬁed
trace, which in general is only deﬁned on proper tensor ideals ofC. This approach
was pioneered by Costantino, Geer, and Patureau [12] in a diﬀerent non-semisimple
setting with respect to Lyubashenko’s. Indeed, an alternative (and also potentially
non-semisimple) generalization of Turaev’s notion of modular category, calledrel-
ative modular category, exists. Relative modular categories are so diﬀerent from
Lyubashenko’s modular categories that the two notions intersect exclusively along
Turaev’s modular categories. In other words, if a categoryC is both modular in
the sense of Lyubashenko and relative modular, then it is modular in the sense
of Turaev. The main examples of relative modular categories are associated with
a diﬀerent family of quantum groups, calledunrolled quantum groups. Starting
from a relative modular category, one can deﬁne a topological invariant of closed
oriented 3-manifolds decorated with so-calledadmissible cohomology classeswhich
is called theCGP invariant. Focusing on the unrolled quantum groupUH
q sl2, this
construction was extended for the ﬁrst time to non-semisimple graded TQFTs in
[7]. The adaptation of this result to arbitrary relative modular categories, as well
as a complete extension to graded ETQFTs in general, is presented in [19].
Following the success of these constructions, renormalization was soon applied
to the theory of Hennings and Lyubashenko. This was done at ﬁrst without any
mention to modiﬁed traces, and thus independently of the work of Geer and Pa-
tureau, by Murakami [48]. The resulting invariants of so-calledadmissible knotsin
3Very brieﬂy, an ETQFT is a 2-categorical analogue of a TQFT, i.e. a symmetric monoidal
2-functor from a 2-category of cobordisms to a 2-category of linear categories (several choises are
possible also for the target). Kerler and Lyubashenko’s 2-functors are only deﬁned for connected
surfaces, with symmetric monoidal structure induced by connected sum instead of disjoint union.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 5
3-manifolds were extended to invariants ofadmissible links in 3-manifolds, and re-
formulated in terms of modiﬁed traces, by Beliakova, Blanchet, and Geer [6]. Both
of these works deal exclusively with the case of the restricted quantum group¯Uqsl2.
A generalization of these constructions to arbitrary ﬁnite-dimensional factorizable
ribbon Hopf algebras, as well as corresponding TQFT extensions, was ﬁrst obtained
in [17]. The adaptation of this theory to the general framework of Lyubashenko
was later achieved in [15], where TQFTs are constructed starting from arbitrary,
potentially non-semisimple modular categories. This result recovers both Turaev’s
TQFTs, in the semisimple case, and Lyubashenko’s mapping class group repre-
sentations, in general. It should be remarked, however, that the renormalization
process changes the underlying 3-manifold invariants drastically. In particular, a
complete answer to question (i) is that Lyubashenko’s invariants cannot be ex-
tended to TQFTs, but that his mapping class group representations can.
The invariants and representations arising from the CGP and the renormalized
Lyubashenko constructions are related to each other, see [18] for a discussion of the
quantum group case. Both theories exhibit behaviors which mark a sharp contrast
with respect to the semisimple case. First of all, the CGP invariant associated with
UH
q sl2 forq =i recovers the abelian Reidemeister torsion, which completely classi-
ﬁes lens spaces [7]. This could not be achieved by any Witten–Reshetikhin–Turaev
invariant. Furthermore, the action of Dehn twists along simple closed curves on
states spaces associated with bothUH
q sl2 and ¯Uqsl2 have inﬁnite order [7, 16]. This
is also something that never happens in the semisimple case, and which provides a
positive answer to question(ii). We point out that, to the best of our knowledge,
these remarkable properties of Lyubashenko’s mapping class group representations
had never been noticed before the completion of the TQFT program.
We ﬁnish this section by stressing an important feature of non-semisimple con-
structions. The admissiblity conditions we mentioned in several places have to do
with the fact that modiﬁed traces are generally deﬁned only on proper tensor ideals.
This means that, if we want to add them to our toolbox, we need decorations of
3-manifolds to meet certain requirements. Typically, decorations carry labels given
by objects of a category C, and we need at least one of these labels to belong
to the tensor ideal supporting the modiﬁed trace. It should be noted that these
constraints also aﬀect cobordism categories. Indeed, certain decorated cobordisms
have to be removed from sets of morphisms, and this operation usually breaks the
rigidity of a few objects. In other words, certain decorated surfaces are not du-
alizable in these so-calledadmissible decorated cobordism categories. However, the
symmetric monoidal structure induced by disjoint union remains intact, and so the
resulting TQFTs are indeed symmetric monoidal in the sense of Atiyah.
3. Turaev’s notion of modular category
Using the language of [21], a T-modular category (T for Turaev) is a ribbon
fusion category whose S-matrix is invertible. The deﬁnition originally appeared in
[58, Sec. II.1.2] in a slightly more general form, but the version reported here has
since become rather standard (compare with [9, 59]). In order to better grasp this
notion, let us proceed to unpack the terminology.
First of all, a ribbon category C is a braided rigid monoidal category with a
twist. This means a ribbon category comes equipped with:
(i) a tensor product⊗ : C× C→ C and a tensor unit
 ∈ C;
(ii) duality morphisms
←
evX : X∗⊗ X →
 ,
←−
coevX :
 → X⊗ X∗, and
→
evX :X⊗X∗→
 ,
−→
coevX :
 →X∗⊗X for everyX∈ C;
(iii) braiding morphismscX,Y :X⊗Y →Y⊗X for allX,Y ∈ C;
(iv) twist morphismsϑX :X→X for everyX∈ C.
6 C. BLANCHET AND M. DE RENZI
All these structure data are subject to several axioms, which can be found explicilty
in [21, Sec. 2.1, 2.10, 8.1, 8.10], but which can also be understood eﬃciently using a
more visual approach. Indeed, morphisms of a ribbon category can be represented
using an extension ofPenrose graphical notationand string diagrams. Structure
morphisms listed above are represented by elementary diagrams
idX =
 idX∗ =
←
evX =
←−
coevX =
→
evX =
−→
coevX =
cX,Y =
 ϑX =
In general, a morphismf :X1⊗... ⊗Xm→Y1⊗... ⊗Yn which is not expressed
as a combination of structure morphisms is simply placed inside a box
f =
 (1)
These diagrams are read from bottom to top.4 Composition is given by vertical
stacking, while tensor product corresponds to horizontal juxtaposition. Then, the
axioms of a ribbon category translate precisely to the invariance of this diagram-
matic calculus under isotopy and framed Reidemeister moves.
Next, let us ﬁx an algebraically closed5 ﬁeldk. Throughout this paper, we
will use the term “linear” as a shorthand for “k-linear”. Then, let us consider
a linear category C, which is a category whose sets of morphisms carry vector
space structures making compositions into bilinear maps. We say thatC is ﬁnite
if it is equivalent to the category of ﬁnite-dimensional representations of a ﬁnite-
dimensional algebra. This deﬁnition is rather implicit, as no algebra is attached to
C, but it can be reformulated in more explicit terms. In fact, as explained in [21,
Def. 1.8.6], C is ﬁnite if and only if it is abelian and:
(i) it has a ﬁnite number of isomorphism classes of simple objects;
(ii) it has enough projectives;
(iii) its objects have ﬁnite lenght;
(iv) its morphism spaces have ﬁnite dimension.
A fusion category is a ﬁnite semisimple monoidal linear category. Therefore, it is
this assumption that encodes the semisimplicity of T-modular categories.
Finally, for every ribbon fusion category we can deﬁne anS-matrix given by
S(C) :=
(
 )
i,j∈I
where Γ (C) = {Vi|i∈I} is a set of representatives of isomorphism classes of
simple objects of C. We say a ribbon fusion categoryC is T-modular ifS(C) is
invertible. This requirement can be understood as a non-degeneracy condition for
the braiding of a ribbon fusion category.
4Remark that the convention used here for orientations is opposite to the one used by Turaev,
but also widely used.
5This condition is not necessary, but convenient.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 7
We ﬁnish this section with an additional deﬁnition. TheMüger centerM(C) of
a ribbon category C is the full subcategory of so-calledtransparent objects of C,
that is,X∈M(C) ifcY,X◦cX,Y = idX⊗Y for everyY ∈ C. The Müger center of a
ribbon categoryC is said to be trivial if every transparent object ofC is isomorphic
to a direct sum of copies of the tensor unit
. Then, a ribbon fusion categoryC has
trivial Müger center if and only ifS(C) is invertible [11, Prop. 1.1]. This equivalent
non-degeneracy condition for the braiding ofC will be useful later on.
4. Semisimple quantum inv ariants and TQFTs
The diagrammatic interpretation for morphisms of ribbon categories which was
discussed earlier highlights the fundamental interplay between algebra and topol-
ogy arising in this context. In fact, it is a result of Turaev that certain topological
gadgets called ribbon graphs provide the relevant topological structure underly-
ing Penrose graphical notation [58, Thm. I.2.5]. Indeed, isotopy classes of ribbon
graphs can be organised as morphisms of a categoryRC, and the graphical calculus
introduced above can be implemented by a functor
FC : RC→ C
called the Reshetikhin–Turaev functor. This technology plays a fundamental role
in every construction discussed in this survey.
Starting from a T-modular categoryC, Turaev showed how to construct a topo-
logical invariantRTC of closed oriented 3-manifolds decorated with closed6 ribbon
graphs. By their very deﬁnition, ribbon graphs have a rather hybrid nature, be-
tween topology and algebra. This of course can be seen as a strenght of the theory,
which allows for great ﬂexibility. However, for the beneﬁt of those who are look-
ing for a purely topological point of view, the construction can be understood as
producing, in particular, a family{RTV}V∈C of topological invariants of framed
oriented links inside 3-manifolds, where each invariantRTV is obtained by choos-
ing the objectV ∈ C as a label for every component of the link. The deﬁnition
of these topological invariants is based on surgery presentations, which allow us to
interpret framed links inS3 as closed oriented 3-manifolds. The main idea consists
in choosing orientations and labels for a surgery presentation, and then using the
Reshetikhin–Turaev functorFC in order to extract a scalar. The choice needs to be
made in such a way that the resulting scalar is invariant under orientation reversals
and Kirby moves. Turaev came up with such a label, which is given by a formal
linear combination of objects ofC called theKirby color, and given by
Ω :=
∑
i∈I
dimC(Vi)·Vi,
where againΓ (C) ={Vi|i∈I} is a set of representatives of isomorphism classes
of simple objects ofC, and where
dimC(X) = trC(idX) =
→
evX◦
←−
coevX
isthe categorical dimensionofanobject X∈ C, whichcoincideswiththe categorical
trace of its identity endomorphism. Labeling components of a framed oriented link
using the Kirby color is a shortcut that has to be understood through multilinear
expansions. More precisely, ifL is a framed oriented link featuring a component
K labeled by Ω, and if Li is obtained fromL by replacing the label ofK with
6A ribbon graph isclosed if it has no boundary vertices, and thus represents an endomorphism
of the tensor unit
 of C under the Reshetikhin–Turaev functorFC.
8 C. BLANCHET AND M. DE RENZI
Vi∈Γ (C), then we set
FC(L) :=
∑
i∈I
dimC(Vi)FC(Li).
This oriented framed link invariant is already preserved under Kirby II moves,
as the terminology might suggest. In order to obtain invariance under Kirby I
moves, we need a normalization coeﬃcient. This is deﬁned in terms of the so-called
stabilization coeﬃcients
∆+ :=FC
(
 )
∈ k, ∆− :=FC
(
 )
∈ k.
As a consequence of T-modularity, their product∆+∆− is invertible, and so we
can choose two parametersD,δ∈ k× satisfying
D2 = ∆+∆−, δ = ∆+
D = D
∆−
.
The deﬁnition of the topological invariantRTC depends on the choice ofD, which
uniquely determinesδ. If M is a closed oriented 3-manifold, ifT⊂M is a closed
ribbon graph, and ifL⊂S3 is a surgery presentation ofM, which we assume having
𝓁 components and signatureσ, and which we equip with an arbitrary orientation
and the labelΩ on every component, then
RTC(M,T ) := D−1−𝓁δ−σFC(L∪T )
is a topological invariant of the pair(M,T ).
The universal construction of [8] extends the invariantRTC to a dual pair of
TQFTs given by a covariant functorVC and a contravariant oneV′
C. This means
that, for a closed oriented surfaceΣ, we obtain dual vector spaces VC(Σ) and
V′
C(Σ) supporting respectively left and right actions of decorated cobordisms. If
¯Σ is obtained fromΣ by reversing its orientation, we have a natural isomorphism
V′
C(Σ)∼= VC( ¯Σ). This means we can simply focus on the covariant TQFTVC. If
Σg is a closed oriented surface of genusg, then
VC(Σg)∼=
⨁
i1,...,ig∈I
C


 ,
g⨂
j=1
Vij⊗V∗
ij

. (2)
Since C is semisimple, this vector space can be rewritten, using fusion rules, in
terms of labelings of trivalent graphs, with diﬀerent graphs determining diﬀerent
decompositions. If G is an oriented trivalent graph, whose sets of vertices and egdes
are denotedV and E respectively, then, for every vertexv∈ V, we denote withv−
the set of incoming germs of edges with targetv, and we denote withv+ the set of
outgoing germs of edges with sourcev. A fundamental labeling ofE is a function
i : E→I, and for everyv∈ V the morphism space
C(i,v ) := C

⨂
e∈v−
Vi(e),
⨂
e∈v+
Vi(e)


is called the multiplicity module of i in v. Then, let us consider the embedded
oriented trivalent graph
Gg :=
 ⊂ R3, (3)
and let us denote withVg and Eg its sets of vertices and edges respectively. We
should think ofΣg as being identiﬁed with the boundary of a regular neighborhood
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 9
of Gg. Then, the state spaceVC(Σg) decomposes as a direct sum of tensor products
of multiplicity modules
VC(Σg)∼=
⨁
i:Eg→I
⨂
v∈Vg
C(i,v ). (4)
5. T-modular categories from small quantum sl2
The Witten–Reshetikhin–Turaev TQFT was ﬁrst constructed from the restricted
quantum group of sl2 at even roots of unity. A careful exposition can be found
in [58], while a popular alternative construction, based on Jones–Kauﬀman skein
theory, can be found in [8]. This skein construction also produces TQFTs when the
quantum parameter is an odd root of unity. Referring to Witten’s gauge picture,
these are calledSO(3)-TQFTs. We choose this family as a demonstrative example,
and develop in this section the construction of the underlying modular categories,
corresponding to the so-called small quantum group ofsl2 at odd roots of unity.
We start by ﬁxing an odd integer3⩽r∈ Z, and we consider the primitiverth
root of unityq =e
2πi
r . For every integerk> 0 we introduce the notation
{k} :=qk−q−k, {k}′ :=qk +q−k, [k] :={k}
{1}, [k]! :=
k∏
j=1
[j].
The small quantum group¯Uqsl2, ﬁrst deﬁned by Lusztig in [40], can be constructed
as the C-algebra with generators{E,F,K} and relations
Er =Fr = 0, K r = 1,
KEK−1 =q2E, KFK −1 =q−2F, [E,F ] = K−K−1
q−q−1 ,
and with Hopf algebra structure obtained by setting
∆(E) =E⊗K + 1⊗E, ε (E) = 0, S (E) =−EK−1,
∆(F ) =K−1⊗F +F⊗ 1, ε (F ) = 0, S (F ) =−KF,
∆(K) =K⊗K, ε (K) = 1, S (K) =K−1.
Remark that Lusztig considers the opposite coproduct, while we are using the one
of Kassel [31, Sec. VII.1]. A basis of¯Uqsl2 is given by
{
EaFbKc| 0⩽a,b,c ⩽r− 1
}
,
as proved in [40, Thm. 5.6]. Furthermore,¯Uqsl2 supports the structure of a ribbon
Hopf algebra. Indeed, anR-matrix R∈ ¯Uqsl2⊗ ¯Uqsl2 is given by
R := 1
r
r−1∑
a,b,c=0
{1}a
[a]! q
a(a−1)
2 −2bcKbEa⊗KcFa,
R−1 = 1
r
r−1∑
a,b,c=0
{−1}a
[a]! q−a(a−1)
2 +2bcEaKb⊗FaKc,
while aribbon elementv∈ ¯Uqsl2 is given by
v := i
r−1
2
√r
r−1∑
a,b=0
{−1}a
[a]! q−a(a−1)
2 + (r+1)(a−b−1)2
2 FaKbEa,
v−1 = i−r−1
2
√r
r−1∑
a,b=0
{1}a
[a]! q
a(a−1)
2 + (r−1)(a+b−1)2
2 FaKbEa.
10 C. BLANCHET AND M. DE RENZI
An explicit formula forR ﬁrst appeared in [52, Sec. 3.5], see also [50, Sec. 4.5] for
a diﬀerent one. The expression forv reported here can be obtained by adapting
the proof of [23, Thm. 4.1.1]. A pivotal element g∈ ¯Uqsl2 is given byg := K.
It is proved in [31, Prop. XIV.6.5] that this choice deﬁnes a compatible ribbon
structure, in the sense thatv =ug−1 for theDrinfeld elementu∈ ¯Uqsl2 given by
u := S(R′′)R′, where the notationR = R′⊗R′′ hides a sum. Thus the category
C = ¯Uqsl-mod of ﬁnite-dimensional left¯Uqsl2-modules is a ribbon category.
For every integer0⩽n⩽r− 1 we denote withVn the ¯Uqsl2-module with basis
{an
i ∈Vn| 0⩽i⩽n}
and action given, for all integers0⩽i⩽n, by
K·an
i =qn−2ian
i,
E·an
i = [i][n−i + 1]an
i−1,
F·an
i =an
i+1,
where an
−1 := an
n+1 := 0. These ¯Uqsl2-modules are all simple and self-dual, and
every simple object of C is isomorphic to Vn for some 0 ⩽ n ⩽ r− 1. Their
categorical dimension is
dimC(Vn) = trC(idVn) = [n + 1].
We will see later that the categoryC is not semisimple. However, starting fromC,
we can obtain a fusion category as follows. Let us set
I =
{
2n
⏐⏐⏐ 0⩽n⩽ r− 3
2
}
,
let us consider the set of simple objects
Γ ( ¯C) ={Vi∈ C|i∈I},
and let ˜C denote the full monoidal subcategory ofC generated byΓ ( ¯C). A mor-
phism f∈ C(V,W ) is negligible if
trC(g◦f) = 0
for every morphism g ∈ C(W,V ). An example of a negligible morphism is the
identity idVr−1 of the so-calledSteinberg moduleVr−1. Negligible morphisms of ˜C
form a linear congruence7 N( ˜C) in ˜C, see [47, Sec. II.8]. This means that we can
deﬁne a quotient category¯C := ˜C/N( ˜C) whose objects coincide with those of˜C,
and whose morphism spaces are given by
¯C(V,W ) := ˜C(V,W )/N( ˜C)(V,W ).
Proposition 5.1. The category ¯C is T-modular.
Proof. It follows from [1, Cor. 4.1] that ¯C is semisimple. This means that ¯C
is a ribbon fusion category, and we only need to check that its S-matrixS( ¯C)
is invertible. Thanks to [11, Prop. 1.1], this happens if and only if none of the
columns ofS( ¯C) is colinear to the one corresponding to the tensor unit
. Then,
let us consider the matrix
S(C) :=
(
 )
0⩽i,j⩽r−1
.
7The termtensor ideal is often used instead. Remark however that there are two concurring
notions of tensor ideal, with the other one arising in the context of modiﬁed traces. In order to
avoid confusion, we use Mac Lane’s terminology here.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 11
It follows from an easy computation, which mimics [36, Lem. 3.27], that
S(C)i,j = [(i + 1)(j + 1)]
for all 0⩽i,j ⩽r− 1. Remark that this formula explains why we need to restrict
ourselves to the full subcategory ˜C of C. Indeed, the column (Si,j)0⩽j⩽r−1 is
colinear to the column(Sr−i−2,j)0⩽j⩽r−1 for every integer0⩽i⩽r− 1. We claim
now that the S-matrixS( ¯C) is given by the submatrix
S := (S(C)2i,2j)0⩽i,j⩽r−3
2
of S(C). The fact that no column ofS is colinear to the ﬁrst one follows from
r−3
2∑
i=0
[2i + 1]Si,j =
r−3
2∑
i=0
[2i + 1][(2i + 1)(2j + 1)]
= 1
2


r−3
2∑
i=0
[2i + 1][(2i + 1)(2j + 1)] +
r−3
2∑
i=0
[2i + 1][(2i + 1)(2j + 1)]


= 1
2


r−3
2∑
i=0
[2i + 1][(2i + 1)(2j + 1)] +
r−3
2∑
i=0
[r− 2i− 1][(r− 2i− 1)(2j + 1)]


= 1
2


r−3
2∑
i=0
[2i + 1][(2i + 1)(2j + 1)] +
r−1
2∑
i=1
[2i][2i(2j + 1)]


= 1
2
r−1∑
i=0
[i][i(2j + 1)] = 1
2
r−1∑
i=0
{i}{i(2j + 1)}
{1}2 = 1
2
r−1∑
i=0
{2i(j + 1)}′−{ 2ij}′
{1}2
=−δ0,j
r
{1}2. □
It follows then from the construction thatΓ ( ¯C) is a set of representatives of
isomorphism classes of simple objects of¯C. A direct computation gives thestabi-
lization parameters
∆− =−i
r−1
2 r
1
2q
r+3
2
{1} , ∆+ = i−r−1
2 r
1
2q
r−3
2
{1} ,
and we ﬁx the square root
D = ir
3
2
{1}
of the product∆+∆−, which uniquely determines the coeﬃcient
δ =i−r+1
2 q
r−3
2 ,
as well as the corresponding normalization ofRT¯C.
Thanks to equation (4), state spaces of closed oriented surfaces for the TQFT
V ¯C extending RT¯C can be written as direct sums of tensor products of multiplicity
modules. It turns out that all multiplicity modules in¯C have dimension at most
one. In particular, if Σg is a closed oriented surface of genusg, then a basis of
V ¯C(Σg) is determined by so-calledr-triangular labelings of the set of edgesEg of
the graph Gg represented in (3). Ifv∈ Vg is a vertex, andv−∪v+ ={e,e′,e′′} is
the set of germs of edges which are incident tov, then a labelingi : Eg→I is said
to ber-triangular inv if it satisﬁes the inequalities
|i(e′)−i(e′′)|⩽i(e)⩽i(e′) +i(e′′), i (e) +i(e′) +i(e′′)< 2r− 2.
12 C. BLANCHET AND M. DE RENZI
A labelingi : Eg→I isr-triangular 8 if it isr-triangular in everyv∈ Vg. Thanks to
the next statement, the dimension ofV ¯C(Σg) is obtained by countingr-triangular
labelings ofi : Eg→I.
Proposition 5.2. The multiplicity module
¯C(i,v )∼= ¯C(
 ,Vi(e)⊗Vi(e′)⊗Vi(e′′))
has dimension one ifi is r-triangular inv, and zero otherwise.
Proof. Since ¯C is a fusion category, the dimension of¯C(
 ,Vi(e)⊗Vi(e′)⊗Vi(e′′)) is
equal to the multiplicity ofV∗
i(e)
∼=Vi(e) in the decomposition ofVi(e′)⊗Vi(e′′) in ¯C.
The decomposition ofVi(e′)⊗Vi(e′′) into a sum of indecomposable¯Uqsl2-modules
in C is given by
Vi(e′)⊗Vi(e′′)∼=
min
{
i(e′ )+i(e′′)
2 ,r−i(e′ )+i(e′′)
2 −2
}
⨁
n=|i(e′ )−i(e′′)|
2
V2n⊕
r−1
2⨁
n=r−i(e′ )+i(e′′)
2 −1
P2n,
where P2n is the projective cover ofV2n, see Section 8. A similar formula for even
values ofr is established in [57], and the proof can be adapted. SinceP2n is a direct
summand ofVr−1⊗Vr−1, its identity is negligible. In particular, the decomposition
of Vi(e′)⊗Vi(e′′) in the category ¯C reduces to
Vi(e′)⊗Vi(e′′)∼=
min
{
i(e′)+i(e′′)
2 ,r−i(e′)+i(e′′)
2 −2
}
⨁
n=|i(e′ )−i(e′′)|
2
V2n.
This proves the proposition. □
As an example, the state space of the torusΣ1 =S1×S1 has dimension
dimC VC(Σ1) = r− 1
2 .
Since every Dehn twist is sent to (the projective class of) a matrix of ﬁnite or-
der, the projective representation of the genus one mapping class groupMod(Σ1)
in PGLC(VC(Σ1)) is never faithful, although it has very interesting asymptotic
faithfulness properties asr tends to inﬁnity, see [2, Thm. 1].
6. Lyubashenko’s notion of modular category
An L-modular category (L for Lyubashenko) can be deﬁned as a ﬁnite ribbon
category whose Müger center is trivial. Remark that this is not the original deﬁ-
nition of Lyubashenko, but it is equivalent to it. This is a consequence of a result
of Shimizu [56], who compared several notions of non-degeneracy for the braiding
of a ﬁnite ribbon category, proving the equivalence of four diﬀerent conditions.
Among these, we can ﬁnd Lyubashenko’s original one, as well as the short property
used above. This formulation makes it clear that T-modular categories are just
semisimple L-modular categories.
In order to review Lyubashenko’s deﬁnition, letC be a ﬁnite ribbon category,
and let us consider the functorH : Cop× C→ C determined by(X,Y )↦→X∗⊗Y.
We recall the classical notion of adinatural transformation of sourceH, which is
given by an objectZ ∈ C equipped with a family{dX : X∗⊗X → Z}X∈C of
morphisms of C satisfying
dX◦ (f∗⊗ idX) =dY◦ (idY∗⊗f)
8Such a labeling is calledr-admissible in [8], but we change terminology here because admis-
sibility will be a diﬀerent condition, and a key one, in the non-semisimple construction.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 13
for every morphismf :X→Y of C, see [47, Sec. IX.4]. We usually abuse notation,
andsimplydenotedinaturaltransformationsbytheirunderlyingobjects. The coend
of H is the universal dinatural transformation of sourceH, which means it is an
object L∈ C with a dinatural family of structure morphismsiX : X∗⊗X→ L
satisfying the following condition: for every dinatural transformationZ of source
H there exists a unique morphism𝓁Z : L→Z such that the diagram
Y∗⊗X X∗⊗X
Y∗⊗Y L
Z
f∗⊗ idX
iXidY∗⊗f
iY
dX
dY
𝓁Z
(5)
commutes for every morphismf :X→Y of C. It has been proved by Majid [44]
and Lyubashenko [42, 43] that, sinceC is a ﬁnite ribbon category, the coend ofH
always exists, and furthermore it supports the structure of a braided Hopf algebra
in C. This means that it admits:
(i) a productµ : L⊗ L→ L and a unitη :
 → L;
(ii) a coproduct ∆ : L→ L⊗ L and a counitε : L→
 ;
(iii) an antipodeS : L→ L.
Allthesestructuremorphismsareuniquelydeterminedbytheuniversalproperty(5)
of L. Indeed, they can be deﬁned as the unique morphisms ofC that satisfy
for allX,Y ∈ C. Remark that the productµ is actually determined by a universal
property satisﬁed by the so-calleddouble coend L⊗ L, and it requires a Fubini
14 C. BLANCHET AND M. DE RENZI
theorem for coends [47, Prop. IX.8] whose name comes from the standard notation
L =
∫ X∈C
X∗⊗X,
see also [35, Prop. 5.1.2]. We should point out that, dually, every ﬁnite ribbon
category C also admits anend
E =
∫
X∈C
X⊗X∗,
which is similarly deﬁned as a universal dinatural transformation, see Appendix A
for details. Equivalent constructions can be carried out exploiting the properties
of E, which are completely analogous to those ofL, and it is for historical reasons
that we focus onL instead of E, following Lyubashenko.
From a topological point of view, what we said so far hints at the fact that the
universal property (5) of the coendL provides an alternative to the Reshetikhin–
Turaev functor for extracting morphisms of C from diagrams of certain framed
orientedtangles. Forinstance, aHopfpairing ω : L⊗L→
 isuniquelydetermined
by the equality
for allX,Y ∈ C. Then, following Lyubashenko’s original deﬁnition, an L-modular
category is a ﬁnite ribbon category for which the Hopf pairingω is non-degenerate,
meaning that it induces an isomorphism betweenL and L∗. Remark how similar
thedeﬁningdiagramfor ω iswithrespecttotheonedeﬁningtheS-matrixofTuraev.
In fact, whenC is semisimple, then Prop. A.1 and [33, Lem. 2] give
E∼=
⨁
i∈I
Vi⊗V∗
i , L∼=
⨁
i∈I
V∗
i ⊗Vi,
and ω is non-degenerate if and only if the S-matrix is invertible [35, Prop. 7.4.3].
An alternative condition for the modularity of C is that a certain morphism
D : L→ E calledthe Drinfeld mapisanisomorphism, see[22, Prop.4.11]. When C
is the categoryH-mod of ﬁnite-dimensional representations of a ﬁnite-dimensional
ribbon Hopf algebraH, then let us denote withad the adjoint representation of
H, which is given by the vector spaceH equipped with the adjoint leftH-action
deﬁned by
adx(y) =x(1)yS(x(2))
for allx,y∈H, where we are using Sweedler’s notation∆(x) =x(1)⊗x(2) for the
coproduct. Similarly, let us denote with coad the coadjoint representationof H,
which is given by the vector spaceH∗ equipped with the coadjoint leftH-action
deﬁned by
coadx(ϕ)(y) =ϕ(S(x(1))yx(2))
for allx,y∈H and ϕ∈H∗. Then Prop. A.2 and [33, Lem. 3] give
E∼= ad, L∼= coad.
In this setting, the Drinfeld mapD : coad→ ad was ﬁrst deﬁned in [20, Prop. 3.3]
as the H-module morphism determined by D(ϕ) := ( ϕ⊗ idH)(R21R12), where
R12 = R∈ H⊗H is the R-matrix ofH, andR21∈ H⊗H is obtained fromR
by reversing the order of its components. The elementM = R21R12∈ H⊗H is
sometimes called theM-matrix, or monodromy matrix, ofH. By deﬁnition,H is
factorizable if D is an isomorphism.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 15
When C is modular, an integral of the coend L is a morphism9 Λ :
 → L
satisfying
µ◦ (Λ⊗ idL) = Λ◦ε =µ◦ (idL⊗ Λ).
In analogy with Sweedler’s result for Hopf algebras in the category of ﬁnite-dimen-
sional vector spaces, the coendL admits an integral, which is unique up to scalar
[42, Thm. 6.1]. WhenC is semisimple, then, up to scalar, we have
Λ = (dimC(Vi)·
−→
coevVi)i∈I,
which means that we can think of an integralΛ of the coend L as extending the
Kirby color to the non-semisimple case. WhenC is the categoryH-mod of ﬁnite-
dimensional representations of a ﬁnite-dimensional factorizable ribbon Hopf algebra
H, then, up to scalar, we have
Λ(1) =λ∈H∗,
where λ∈H∗ is a classical right integral on the Hopf algebraH. See [33, Sec. 2.5]
for both claims.
The algebraic setup discussed up to here is suﬃcient to perform Lyubashenko’s
construction, but in order to obtain TQFTs, we also need the theory of modiﬁed
traces. Let us present the key deﬁnitions by focusing on a relevant special case. We
denote by Proj(C) the full subcategory of projective objects ofC, which forms a
tensor idealin C, in the sense that it is closed under retracts and absorbent under
tensor products, see [24, Def. 3.1.1]. Atrace on Proj(C) is a family of linear maps
t :={tP : EndC(P )→ k}P∈Proj(C)
satisfying:
(i) Cyclicity: tP




= tQ




for allP,Q∈ Proj(C), f∈ C(P,Q ), andg∈ C(Q,P );
(ii) Partial trace: tP⊗X



 = tP




for allP∈ Proj(C), X∈ C, andf∈ EndC(P⊗X).
Wesayatrace ton Proj(C)isnon-degenerateif, forallP∈ Proj(C)andX∈ C, the
bilinear pairingtP (_◦_) : C(X,P )×C(P,X )→ kdetermined by(g,f )↦→ tP (g◦f)
is non-degenerate. Thanks to [25, Cor. 5.6], for a modular10 category C there exists
a tracet on Proj(C), which is unique up to scalar and furthermore non-degenerate.
When C is semisimple, then Proj(C) = C, and the standard categorical trace
trC is the unique trace on C up to scalar. When C is the category H-mod of
ﬁnite-dimensional representations of a ﬁnite-dimensional factorizable11 ribbon Hopf
9The source ofΛ might be a diﬀerent invertible object in general, called theobject of integrals,
but here we are supposingC is modular.
10The statement is a particular case of a much more general existence and uniqueness result,
see [25, Thm. 5.5].
11Again, hypotheses for this result can be considerably relaxed, but we prefer to avoid intro-
ducing more terminology.
16 C. BLANCHET AND M. DE RENZI
algebraH, there is a natural correspondence between the space of traces onProj(C)
and the spaces of so-calledsymmetrized integrals onH, see [5, Thm. 1].
7. Non-semisimple quantum inv ariants and TQFTs
Using the coendL and the integralΛ, it is possible to develop a diagrammatic
calculus which steps outside of the framework provided by the Reshetikhin–Turaev
functor. This time, the topological gadgets underlying this graphical notation are
called bichrome graphs. Very roughly speaking, bichrome graphs are ribbon graphs
whose edges can be of two kinds, eitherred (and unlabeled) orblue (and labeled
as usual by objects ofC). Similarly, coupons (which, for standard ribbon graphs,
correspond to boxes like the one represented in (1)) are partitioned in two groups,
according to the edges they meet, and can thus be eitherbichrome (and unlabeled)
or blue (and labeled as usual by morphisms ofC). These ribbon graphs are subject
to certain restrictions, see [15, Sec. 3.1] for details. An example of a bichrome
graph, with red components represented as dashed-dotted lines, is given by
This can be understood as representing a morphism of C with source V∗⊗U
and target L⊗W∗. Indeed, just like standard ribbon graphs, bichrome graphs
can be arranged as morphisms of a category12 RΛ, and we can interpretRC as the
subcategory whose morphisms are exclusively blue bichrome graphs. Then, the idea
behind bichrome graphs is essentially the following: on the one hand, the red part
of the graph should be interpreted as prescribing surgery instructions, and it has
to be processed through Lyubashenko’s algorithm, that is, invoking the universal
property (5) of the coend L, in order to extract a morphism ofC (red minima
of diagrams translate to the integralΛ under this correspondence); on the other
hand, the blue part supports the standard graphical calculus implemented by the
Reshetikhin–Turaev functor. There exists a coherent way of harmonizing the two
approaches, which is realized by a functor
FΛ : RΛ→ C
restricting toFC on RC, and called theLyubashenko–Reshetikhin–Turaev functor,
see [15, Sec. 3.1].
Starting from an L-modular categoryC, Lyubashenko’s construction can be re-
formulated as producing a topological invariantLC of closed oriented 3-manifolds
decorated with closed bichrome graphs. As explained in Section 2, this invariant
cannot be extended to a TQFT unlessC is semisimple, in which case everything
boils down to Turaev’s theory. However, in the non-semisimple case, one can con-
struct a renormalized invariantL′
C of closed oriented 3-manifolds decorated with
so-called admissible closed bichrome graphs. We say a bichrome graph isadmissible
if it features at least a projective objectP∈ Proj(C) among the labels of its blue
edges. In particular, just like in the semisimple case, the theory can be understood
12Our notation for the category of bichrome graphsRΛ features the integral Λ in order to
highlight the relevant functor this category supports, but remark that the deﬁnition ofRΛ itself
is actually independent of the choice ofΛ.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 17
as producing a family{L′
P}P∈Proj(C) of topological invariants of framed oriented
links inside 3-manifolds. However, this time it is crucial not to allow empty links,
and to restrict to projective objects for the parametrization.
The ﬁrst step for the construction ofL′
C is the deﬁnition of a renormalized invari-
ant of admissible closed bichrome graphs. Acutting presentationof an admissible
closed bichrome graphT is a bichrome graphTP satisfying
=T
for some P ∈ Proj(C). Remark that every admissible bichrome graph admits
a cutting presentation, which is simply obtained by cutting open one of its blue
edges carrying projective label. However, cutting presentations are by no means
unique. For instance, we might have several blue edges with projective labels to
choose from, and these could all determine inequivalent presentations. Nonetheless,
if T is an admissible closed bichrome graph, and ifTP is a cutting presentation of
T, then
F′
C(T ) := tP (FΛ(TP ))
is a topological invariant ofT. The proof of this result essentially follows from
the deﬁning properties of the tracet, which were designed explicitly to obtain
these kinds of renormalized topological invariants. Now, in order to extend this
construction to 3-manifolds, we need again a normalization coeﬃcient, just like
in the semisimple theory. This is deﬁned in terms of the so-calledstabilization
coeﬃcients
∆+ :=FΛ
(
 )
∈ k, ∆− :=FΛ
(
 )
∈ k.
Just like in the fusion case, it is a consequence of L-modularity that the product
∆+∆− is invertible, and so we can choose two parametersD,δ∈ k× satisfying
D2 = ∆+∆−, δ = ∆+
D = D
∆−
.
The deﬁnition of the topological invariantL′
C depends again on the choice ofD,
which uniquely determinesδ. IfM is a closed oriented 3-manifold, ifT⊂M is an
admissible closed bichrome graph, and ifL⊂ S3 is a surgery presentation ofM,
which we assume having𝓁 components and signatureσ, and to which we assign an
arbitrary orientation and the color red, then
L′
C(M,T ) := D−1−𝓁δ−σF′
Λ(L∪T )
is a topological invariant of the pair(M,T ).
Just like in Section 4, the universal construction of [8] extends the invariantL′
C
to a dual pair of TQFTs given by a covariant functorVC and a contravariant one
V′
C. Again, this means that, for every closed oriented surfaceΣ, we obtain dual
vector spaces VC(Σ) and V′
C(Σ) supporting respectively left and right actions of
decorated cobordisms. This time, if¯Σ is obtained fromΣ by reversing its orienta-
tion, the isomorphism V′
C(Σ)∼= VC( ¯Σ) is no longer natural, as a consequence of
the admissibility condition. Indeed, ifΣg is a closed oriented surface of genusg,
then the contravariant state spaceV′
C(Σg) can be naturally identiﬁed with
V′
C(Σg)∼= C(L⊗g,
 ). (6)
18 C. BLANCHET AND M. DE RENZI
On the other hand, the covariant state spaceVC(Σg), which is isomorphic to the
linear dual ofV′
C(Σg), can be naturally identiﬁed with
VC(Σg)∼= C(P
 , E⊗g)/ radR⟨_,_⟩g, (7)
whereP
 is the projective cover of the tensor unit
, and where the bilinear pairing
⟨_,_⟩g : C(L⊗g,
 )× C(P
 , E⊗g)→ k is determined by
⟨f′,f⟩g = tP
(
η
 ◦f′◦ (D−1)⊗g◦f
)
for the Drinfeld map D : L → E and the injective envelope13 monomorphism
η
 :
 → P
 . When C is semisimple, then P
 =
 , η
 = id
 , and⟨_,_⟩g is
non-degenerate, so that we recover the description of (2).
8. L-modular categories from small quantum sl2
The small quantum group¯Uqsl2 introduced in Section 5 is factorizable. This is
proved in [46, Ex. 3.4.3] by looking directly at the M-matrixM∈ ¯Uqsl2⊗ ¯Uqsl2,
which is given by
M := 1
r
r−1∑
a,b,c,d=0
{1}a+b
[a]![b]!q
a(a−1)+b(b−1)
2 −2cd−(b+c)(b−d)FbKcEa⊗EbKdFa.
This means the categoryC = ¯Uqsl-mod of ﬁnite-dimensional left¯Uqsl2-modules is
L-modular, see [42, Rem. 3.6.1].
An integral Λ : C→ coad is determined by the linear formλ = Λ(1)∈ ( ¯Uqsl2)∗
deﬁned as
λ
(
EaFbKc)
:= r3
{1}2r−2δa,r−1δb,r−1δc,1,
see [41, Prop. A.5.1]. Remark that Lyubashenko uses Lusztig’s coproduct, which
explains why the formula written here deﬁnes a right integral, instead of a left one.
A direct computation gives thestabilization parameters
∆− =λ(v) =i
r−1
2 r
3
2q
r+3
2 , ∆+ =λ(v−1) =i−r−1
2 r
3
2q
r−3
2 ,
and we ﬁx the square root
D =r
3
2
of the product∆+∆−, which uniquely determines the coeﬃcient
δ =i−r−1
2 q
r−3
2 ,
as well as the corresponding normalization ofL′
C.
In order to illustrate the diﬀerence between the L-modular categoryC and its
T-modular subquotient ¯C deﬁned in Section 5, let us describe projective covers
of simple objects of C. For every integer 0⩽ n⩽ r− 2 we denote withPn the
¯Uqsl2-module with basis
{an
i,xn
j,yn
j,bn
i ∈Pn| 0⩽i⩽n, 0⩽j⩽r−n− 2}
13Projective covers coincide with injective envelopes in modular categories.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 19
and action given, for all integers0⩽i⩽n and 0⩽j⩽r−n− 2, by
K·an
i =qn−2ian
i,
E·an
i = [i][n−i + 1]an
i−1,
F·an
i =an
i+1,
K·xn
j =q−n−2j−2xn
j,
E·xn
j =−[j][n +j + 1]xn
j−1,
F·xn
j =
{
xn
j+1 0⩽j <r−n− 2,
an
0 j =r−n− 2,
K·yn
j =q−n−2j−2yn
j,
E·yn
j =
{
an
n j = 0,
−[j][n +j + 1]yn
j−1 0<j ⩽r−n− 2,
F·yn
j =yn
j+1,
K·bn
i =qn−2ibn
i,
E·bn
i =
{
xn
r−n−2 i = 0,
an
i−1 + [i][n−i + 1]bn
i−1 0<i ⩽n,
F·bn
i =
{
bn
i+1 0⩽i<n,
yn
0 i =n,
where an
−1 := an
n+1 := xn
−1 := yn
r−n−1 := 0. These modules are all projective,
indecomposable, and self-dual, and every indecomposable projective object ofC is
isomorphic to eitherPr−1 =Vr−1 or Pn for some 0⩽n⩽r− 2. Their categorical
dimension is
dimC(Pn) = trC(idPn) = 0.
However, the normalization tVr−1(idVr−1) = 1 uniquely determines a trace t on
Proj(C) which satisﬁes
tPn(idPn) ={n + 1}′,
as follows from a computation that can be adapted from [13, Lem. 6.9] (remark
the diﬀerence between the pivotal elementg =K and the one used by Costantino,
Geer, and Patureau for their right duality morphisms, which accounts for the sign
appearing in their formula).
Thanks to equations (6) and (7), state spaces of closed oriented surfaces for the
TQFTs VC and V′
C extending L′
C can be written in terms of morphism spaces inC
involving tensor powers of the endE∼= ad and of the coendL∼= coad. We point
out that, althoughad and coad can be described very explicitly, their description
is rather complicated. For instance, they are not projective objects ofC, as follows
from an explicit decomposition into indecomposable summands computed by Ostrik
[51]. IfΣg isaclosedorientedsurfaceofgenus g, thenequation(6)identiﬁes V′
C(Σg)
with C(coad⊗g,
 ). On the other hand, equation (7) describes the dual vector space
VC(Σg) as a quotient ofC(P0, ad⊗g). In the example of the torusΣ1 =S1×S1,
since C(coad,
 ) can be naturally identiﬁed with the centerZ( ¯Uqsl2) of ¯Uqsl2, then
V′
C(Σ1)∼=Z( ¯Uqsl2).
On the other hand, the quotient ofC(P0, ad⊗g) can be naturally identiﬁed with
the Hochschild homologyHH0( ¯Uqsl2) = ¯Uqsl2/[ ¯Uqsl2, ¯Uqsl2] of ¯Uqsl2, so that
VC(Σ1)∼= HH0( ¯Uqsl2).
20 C. BLANCHET AND M. DE RENZI
The dimension of both spaces is
dimC VC(Σ1) = dimCZ( ¯Uqsl2) = 3r− 1
2 ,
as computed by Kerler in [32, Lem. 14]. In the same paper, Kerler independently
redeﬁnes and computes Lyubashenko’s projective representation of the genus one
mapping class group Mod(Σ1) in PGLC(Z( ¯Uqsl2)), see [32, Thm. 2]. He conjec-
tures an explicit decomposition of this representation, and he veriﬁes his conjecture
for r = 3 and r = 5 in [32, Sec. 3.6]. Remark that in both cases the resulting
representation of Mod(Σ1) is faithful modulo the centerZ(Mod(Σ1))∼= Z/2Z. Up
to isomorphism, Kerler–Lyubashenko’s representations are precisely those induced
by the contravairant TQFTV′
C for C = ¯Uqsl-mod, see [16, Thm. 1.2].
