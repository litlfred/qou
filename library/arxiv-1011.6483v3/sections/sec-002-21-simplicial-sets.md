---
doc_id: arxiv-1011.6483v3
doc_title: "DERIVED HIGHER HOCHSCHILD HOMOLOGY"
section_id: sec-002-21-simplicial-sets
section_title: "Simplicial sets"
section_number: 2.1
pages: 6-10
source_pdf: 1011.6483v3.pdf
source_sha256: 7a425e51860c37a4
doc_brief: "DERIVED HIGHER HOCHSCHILD HOMOLOGY — W e study the higher Hochschild chain functor, factorizatio n alge- bras and their relationship with topological chiral homolo gy."
---
graded algebras will be respectively denoted by sSet and CDGA. The
category of commutative graded algebra will be denoted CGA. Unless
otherwise stated, all algebras will be assumed to be unital.
(3) We will simply refer to commutative diﬀerential graded algebras a s CDGAs.
(4) The (∞, 1)-categories of simplicial sets and commutative diﬀerential grade d
algebras will be respectively denoted by sSet∞ and CDGA ∞.
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 7
(5) Let n≥ 1 be an integer. By an En-algebra we mean an algebra over an
En-operad. Unless otherwise stated, we work in the context of oper ads
of diﬀerential graded k-modules or ∞-operads in k-Mod ∞. We will write
En-Alg∞ for the (∞, 1)-category of En-algebras.
(6) We work with a cohomological grading (unless otherwise stated) for all our
(co)homology groups and graded spaces, even when we use subsc ripts to
denote the grading. In particular, all diﬀerentials are of degree +1 , of the
form d : Ai → Ai+1 and the homology groups Hi(X) of a space X are
concentrated in non-positive degree.
(7) We will denote by CHn
X• (A) the Hochschild chain complex over X• with
value in A of total degree n. This Hochschild chain complex was noted
diﬀerently in the papers [12, 13]. We choose this notation in order to p ut
emphasis on the covariance of the Hochschild chain functor with respect to
X• and the fact that we are considering cohomological degree.
2.1. Simplicial sets. Denote by ∆ the category whose objects are the ordered sets
[k] ={0, 1,...,k }, and morphisms f : [k]→ [l] are non-decreasing maps f (i)≥f (j)
fori>j . In particular, we have the morphisms δi : [k− 1]→ [k],i = 0,...,k , which
are injections that miss i and we have surjections σj : [k + 1]→ [k],i = 0,...,k ,
which send j and j + 1 to j.
A simplicial set is by deﬁnition a contravariant functor from ∆ to the category of
setsSets or written as a formula, Y• : ∆ op→S ets. Denote by Yk =Y•([k]), and call
its elements simplicies. The image of δi underY• is denoted by di :=Y•(δi) : Yk→
Yk−1, fori = 0,...,k , and is called the ith face. Similarly, si :=Y•(σi) : Yk→Yk+1,
fori = 0,...,k , is called the ith degeneracy. An element in Yk is called a degenerate
simplex, if it is in the image of some si, otherwise it is called non-degenerate.
A simplicial set is said to be ﬁnite if Yk is ﬁnite for every object [ k]∈ ∆. A
pointed simplicial set is a contravariant functor into the category Sets∗ of pointed
ﬁnite sets, Y• : ∆ op →S ets∗. In particular, each Yk = Y•([k]) has a preferred
element called the base point, and all diﬀerentials di and degeneracies si preserve
this base point.
A morphism of (ﬁnite or not, pointed or not) simplicial sets is a natura l trans-
formation of functors f• : X• → Y•. Thus f• is given by a sequence of maps
fk : Xk → Yk (preserving the base point in the pointed case), which commute
with the faces fkdi = difk+1, and degeneracies fk+1si = sifk for all k≥ 0 and
i = 0,...,k .
One of the most important construction for us is the pushout.
Deﬁnition 1. Let X•,Y •, and Z• be simplicial sets, and let f• : Z•→ X• and
g• :Z•→Y• be maps of simplicial sets. We deﬁne the wedge W• =X•∪Z• Y• of
X• and Y• along Z• as the simplicial space given by Wk = (Xk∪Yk)/∼, where
∼ identiﬁes fk(z) = gk(z) for all z∈ Zk. The face maps are deﬁned as dW•
i (x) =
dX•
i (x),dW•
i (y) = dY•
i (y) and the degeneracies are sW•
i (x) = sX•
i (x),sW•
i (y) =
sY•
i (y) for any x∈Xk֒→Wk and y∈Yk֒→Wk. It is clear that W• is well-deﬁned
and there are simplicial maps X•
i•→W• and Y•
j•→W•.
If X• is a pointed simplicial set, then we can make W• into a pointed simplicial
set by declaring the base point to be the one induced from the inclusio nX•→W•.
(Note that this is in particular the case, when X•,Y •,Z •,f • and g• are in the
pointed setting.)
8 G. GINOT, T. TRADLER, AND M. ZEINALIAN
2.2. Commutative Diﬀerential Graded Algebras. We let CDGA be the cat-
egory of commutative diﬀerential graded algebras (over the char acteristic zero ﬁeld
k). We do not assume the underlying chain complexes of our algebras t o be bounded
since in practice, it happens that one has to consider the Hochschild chains of de
Rham forms on a space, which is generally Z-graded. We follow the approach of [32,
Chapter 1.1] and [16] for the model category properties of CDGA and modules over
CDGAs. Recall from [19, Section 2.3], that there is a standard coﬁbr antly generated
closed model category structure on the category of unbounded chain complexes for
which ﬁbrations are epimorphisms and (weak) equivalences are quas i-isomorphisms.
It is further a symmetric monoidal model category with respect to the tensor prod-
ucts of chain complexes.
Since we work in characteristic zero, there is a standard closed mod el category
structure on CDGA [16, Theorem 4.1.1] as well, for which ﬁbrations are epimor-
phisms and (weak) equivalences are quasi-isomorphisms (of CDGAs) . The category
CDGA also has a monoidal structure given by the tensor product (over t he ground
ﬁeld k) of diﬀerential graded commutative algebras, which makes CDGA a sym-
metric monoidal model category. Note that since k is assumed to be a ﬁeld, this
monoidal structure is given by an exact bifunctor.
Also note that CDGA is simplicially enriched. Indeed, given A,B ∈ CDGA,
we can form Map CDGA (A,B ) the simplicial set of maps [ n]↦→HomCDGA (A,B⊗
Ω ∗(∆ n)) (where Ω ∗(∆ n) is the CDGA of forms on the n-dimensional standard
simplex).
For any CDGA A, one can consider its category of diﬀerential graded (left)
modules, that we will denote by A-Mod . Again it has a natural model category
structure with ﬁbrations being epimorphisms and weak equivalences being quasi-
isomorphisms. Further all assumptions in [32, Chapter 1.1] are satis ﬁed. In partic-
ular, the tensor product of A-modules makes A-Mod a symmetric monoidal model
category (in the sense of [19]) such that the functor M⊗A− preserves weak equiv-
alences when M is coﬁbrant. Moreover, for any CDGA A, the category A−CDGA
of diﬀerential graded commutative A-algebra, in other words commutative monoid
objects in A-Mod , has a natural structure of proper model category such that, for
any coﬁbrant A-algebra B, the base change functor B⊗A− : A-Mod→ B-Mod
preserves weak equivalences [32, Chapter 1.1].
2.3. Dwyer-Kan localization and (∞, 1)-categories. The (∞, 1)-categories that
we are concerned about in this paper arise from model categories s tructures via the
Dwyer-Kan localization turning them into simplicial categories. Indee d simplicial
categories are model for (∞, 1)-categories [5]. We now explain brieﬂy how one gets
(∞, 1)-categories out of model categories such as those considered in Section 2.1, 2.2
above.
Following [31, 26], by an ( ∞, 1)-category we mean a complete Segal space. Rezk
has shown that the category of simplicial spaces has a (simplicial clos ed) model
structure, denoted CSeSp such that a complete Segal space is precisely a ﬁbrant
object for this model structure [31, Theorem 7.2]. Note that the re is also a (simpli-
cial closed) model category structure, denoted SeSp, on the category of simplicial
spaces such that a ﬁbrant object in the SeSp structure is precisely a Segal space.
We let R :SeSp→S eSp be a ﬁbrant replacement functor. Rezk [31] has deﬁned a
completion functor X•→ ˆX• which, to a Segal space, associates an equivalent com-
plete Segal space. Thus, the composition X•↦→ˆR(X•) gives a (ﬁbrant replacement
DERIVED HIGHER HOCHSCHILD, TCH, F ACTORIZATION ALGEBRAS 9
in the model category CSeSp) functor LCSeSp from simplicial spaces to complete
Segal spaces.
It remains to explain how to go from a model category to a simplicial sp ace. The
standard key idea is to use Dwyer-Kan localization. Let M be a model category
andW be its subcategory of weak-equivalences. We denote LH (M,W) its ham-
mock localization, see [10]. One of the main property of LH(M,W) is that it is a
simplicial category and that the (usual) category π0(LH (M,W)) is the homotopy
category ofM. Further, every weak equivalence has a (weak) inverse in LH(M,W).
WhenM is further a simplicial model category, then for every pair ( x,y ) of objects
HomLH (M,W)(x,y ) is naturally homotopy equivalent to the derived mapping space
RHom(x,y ).
It follows that any model category M gives functorially rise to the simplicial
category LH (M,W). Taking the nerve N•(LH (M,W)) we obtain a simplicial
space. Composing with the complete Segal Space replacement func tor we get
a functor M →L∞(M) := LCSeSp(N•(LH(M,W))) from model categories to
(∞, 1)-categories (that is complete Segal spaces).
Example 1. Applying the above procedure to the model category of simplicial
setssSet, we obtain the (∞, 1)-categorysSet∞. Similarly from the model category
CDGA of CDGAs we obtain the ( ∞, 1)-category CDGA ∞. Note that a simplicial
set is determined by its (∞, 0) path groupoid and therefore the category of simplicial
sets should be thought of as the ( ∞, 1) category of all ( ∞, 0) groupoids. Further,
the tensor product (over k) of algebras is a monoidal functor which gives CDGA
a structure of monoidal model category, see [19]. Thus CDGA ∞ also inherits the
structure of a symmetric monoidal ( ∞, 1)-category in the sense of [31, 26]. Simi-
larly, the disjoint union of simplicial sets endows sSet and sSet∞ with symmetric
monoidal structures.
The model category of topological spaces yields the ( ∞, 1)-categoryTop ∞. Since
sSet and Top are Quillen equivalent [14, 19], the associated ( ∞, 1)-categories are
equivalent (as (∞, 1)-categories): sSet∞
∼
⇄
∼
Top ∞, where the left and right equiva-
lences are respectively induced by the singular set and geometric re alization func-
tors.
One can also consider the pointed versions sSet∞∗ and Top ∞∗ of the above
(∞, 1)-categories (using the model categories of these pointed vers ions [19]).
Example 2. As recalled in Section 2.2, there are model categories categories
A-Mod and A-CDGA of modules and commutative algebras over a CDGA A.
Thus the above procedure gives us (∞, 1)-categoriesA-Mod ∞ andA-CDGA ∞ and
the base change functor lifts to an ( ∞, 1)-functor. Further, if f :A→B is a weak
equivalence, the natural functor f∗ : B-Mod → A-Mod induces an equivalence
B-Mod ∞
∼
→A-Mod ∞ of (∞, 1)-categories since it is a Quillen equivalence.
Moreover, if f : A→B is a morphism of CDGAs, it induces a natural functor
f ∗ :A-Mod→B-Mod,M ↦→M⊗AB, which is an equivalence of ( ∞, 1)-categories
when f is a quasi-isomorphism, and is a (weak) inverse of f∗ (see [32] or [20]).
Here we also (abusively) denote f ∗ : A-Mod ∞→ B-Mod ∞ and f∗ : B-Mod ∞→
A-Mod ∞ the (derived) functors of ( ∞, 1)-categories induced by f . Since we are
working over a ﬁeld of characteristic zero, the same results applies to monoids in
A-Mod and B-Mod , that is to the categories A-CDGA ∞ and B-CDGA ∞. Also
10 G. GINOT, T. TRADLER, AND M. ZEINALIAN
note that, if f :A→B, g :A→C are CDGAs homomorphisms, we can form the
(homotopy) pushout D∼=B⊗L
AC.
Let us denote p : B→ D and q : C→ D the natural CDGAs maps. We thus
get two natural base change ((∞, 1)-)functorsC-Mod ∞
f ∗◦g∗
⇒
p∗◦q∗
B-Mod ∞. Given any
M ∈ C-Mod , the natural map f ∗◦g∗(M )→ p∗◦q∗(M ) is an equivalence [32,
Proposition 1.1.0.8].
The (∞, 1)-categoryCDGA ∞ is tensored oversSet∞ (and thusTop ∞ as well) as
follows from [22, §4.4.4]. We refer to [22, 25] for tensored ( ∞, 1)-categories (which
is the obvious analogue of the classical notion of tensored categor ies over Top or
sSet); we simply recall that an ( ∞, 1)-categoryC is tensored over sSet∞ if there
exists an (∞, 1)-functorC× sSet∞→C , denoted (C,X •)↦→C ⊠X•, together with
natural equivalences
Map C
(
C ⊠X•,D
) ∼= MapsSet∞
(
X•,Map C
(
C,D
))
.
In fact, the tensor A ⊠X• is precisely realized by the Hochschild derived functor,
see Theorem 1.
Example 3. We denote En-Alg∞ the (∞, 1)-category of En-algebras which is
given by algebras over any En-(∞-)operads as introduced in [25, Section 5.1] in
the symmetric monoidal (( ∞, 1)-)category (k-Mod ∞,⊗). It is equivalent to the
(∞, 1)-category associated to model categories (deduced for insta nce from [16,
Theorem 4.1.1]) of algebras over the usual operad of singular chains on the lit-
tlen-dimensional disk operad or as algebras over the Barratt-Eccles o perad (which
is an Hopf operad) [4].
Remark 1. There are other functors that yields a complete Segal space out o f a
model category. For instance, one can use the classiﬁcation diagr am of Rezk [31].
Let againM be a model category and, for any integer n, letM[n] be the (model)
category of n-composables morphisms, that is the category fo functors from t he
poset [n] to M. The classiﬁcation diagram ofM is the simplicial space n ↦→
N•(We(M[n])) where We(M[n]) is the subcategory of weak equivalences of M[n].
Then taking a Reedy ﬁbrant replacement yields another complete Segal space
N•(We(M[n]))f [6, Theorem 6.2], [31, Theorem 8.3]. It is known that the Segal
spaceN•(We(M[n]))f is equivalent to LCSeSp(N•(LH (M,W))) [6].
More generally, there are several model for ( ∞, 1)-categories and several equiv-
alent ways to obtain an ( ∞, 1)-category out of a “homotopy theory”. We believe
the results of this paper can easily be applied to the favorite model o f the reader.
