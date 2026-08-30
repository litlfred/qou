---
doc_id: arxiv-2508.03145v1
doc_title: "Θ-Categories and Tannakian duality"
section_id: sec-000--categories
section_title: "-Categories"
section_number: null
pages: 2-5
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
doc_brief: "Θ-Categories and Tannakian duality — We introduce a notion ofΘ-categories, which is a refinement of the notion of symmetric monoidal∞-categories."
---
defined as functors out ofΓ, the category of pointed finite sets. In [Toe06]
certain stacks, calledschematic homotopy types, have been identified as the
expected duals to Tannakian∞-categories and have been used notably in
the setting of non-abelian Hodge theory (see [KPT08]). Thanks to the foun-
dational work of Lurie, actual Tannaka duality statements have been proven
by several authors, see for instance [Lur11], [Wal12] and [Iwa18]. However,
except in the specific case of characteristic zero, these results are obtained
in the setting of E∞-algebras, which do not relate well to the theory of
schematic homotopy types of [Toe06], and therefore do not provide the ex-
pected Tannakian interpretations for schematic homotopy types.
The starting point of this work is the simple observation that any notion
of Tannakian∞-category solely based on symmetric monoidal∞-categories
will fail to relate nicely to schematic homotopy types, or to stacks in alge-
braic geometry in general. Indeed, for any stackF on the fpqc-site of affine
schemes, the symmetric monoidal∞-category QCoh(F ) of quasi-coherent
sheaves comes equipped with natural extra operations, namely the derived
symmetric power operations. These cannot be reconstructed purely from the
symmetric monoidal structure, and their existence is a theoretical obstruc-
tion for any Tannakian-type reconstruction result in algebraic geometry.
A second incarnation of this discrepancy can be seen at the level of com-
mutative algebras. The theory of schematic homotopy types from [Toe06]
uses co-simplicial commutative rings, a sub-class of theLSym-algebras (see
e.g. [BCN21,Rak20]) typically used in derived, as opposed to spectral, al-
gebraic geometry. In characteristic zero, theseLSym-algebras coincide with
theE∞-algebras that exist naturally in any symmetric monoidal∞-category,
but have an additional algebraic structure in general.
The purpose of this short note is to introduce a rudimentary notion of
Θ-categories, which is a refinement of the notion of symmetric monoidal
∞-categories suited for a Tannakian interpretation of schematic homotopy
types and similar stacks. The point of view adopted here will be somewhat
minimalist and takes the second discrepancy mentioned above as its starting
point. It is based on the principle thatΘ-categories should morally be sym-
2
metric monoidal∞-categories in which an internal notion ofLSym-algebras
exists. We implement this idea by defining Θ-categories simply as pairs
(T,M ), consisting of a symmetric monoidal∞-category and a monadM over
T equipped with a map from theE∞-monad and satisfying some conditions
(see Definition 1.5). The typical example to keep in mind is the case whereF
is a stack,T = QCoh(F ) is its∞-category of quasi-coherent complexes and
M is theLSym-monad, given by the direct sum of derived symmetric powers
E7→L
n LSymn(E). The main content of our work is that this definition
gives rise to a well-behaved(2,∞)-category of Θ-categories, from which a
Tannakian duality theorem can be proven (see Theorem 2.9). In particular,
we show that any TannakianΘ-category T is equivalent, as a symmetric
monoidal∞-category, to dPerf(Fib LSym(T )), the∞-category of ind-perfect
complexes on a certain stack ofLSym-fiber functors. The stacks obtained as
stacks of LSym-fiber functors are moreover essentially the schematic homo-
topy types of [Toe06].
To finish this introduction, we would like to mention that the present
approach to Θ-categories is not optimal. The reader will for instance ob-
serve some limitations and unnatural conditions in our main result, Theorem
2.9. This is the price to pay for our minimalist approach, but we mention
some possible modifications and improvements in a final comment (see Re-
mark 2.15). We also want to mention that a more systematic theory of
Θ-categories as symmetric monoidal∞-categories with additional symmet-
ric powers is presently under investigation by the first author. We believe
that the outcome of this work will allow for stronger and more natural re-
sults in a near future. Nevertheless, Theorem 2.9 can be applied in several
important situations to construct interesting Tannakian duals, such as the
theory of Nori’s motives (from which we can extract a motivic homotopy
type defined as a stack overSpec Z), or the theory of exponential complexes
appearing in [KKP08] (from which we can extract theexponential homotopy
type associated to an algebraic variety). These specific schematic homotopy
theories will be studied elsewhere.
1 Θ-Categories
1.1 µ-Categories
We let∞-CatR
pr be the(2,∞)-category of presentable(1,∞)-categories and
right adjoints (i.e. limit preserving accessible∞-functors). We have the cor-
responding (2,∞)-category Fun(∆1,∞-CatR
pr), of morphisms in∞-CatR
pr.
3
For any objectf : T′→T in Fun(∆1,∞-CatR
pr), we will denote byf∗ : T→
T′ the left adjoint tof, and sometimes writef∗ instead off.
Definition 1.1.An objectf∗ : T′→T in Fun(∆1,∞-CatR
pr) is aµ-category
if f∗ is conservative and preserves sifted colimits.
Note that, by the Barr–Beck theorem [Lur22, Thm. 4.7.0.3] the condition
of being aµ-category implies that the canonical factorization off∗
T′→ LModM(T )→T,
induces an equivalenceT′≃ LModM(T ). Here M = f∗f∗ is the monad on
T associated with the adjunction(f∗,f∗), andLModM(T ) is the∞-category
of M-modules inT.
Definition 1.2. Let f∗ : T′
1→ T1 and g∗ : T′
2→ T2 be twoµ-categories in
the sense of Definition 1.1. Aµ-morphism fromT′
1→T1 toT′
2→T2 consists
of a commutative square in∞-Cat
T′
1
u //
f∗

T′
2
g∗

T1 v
//T2,
withu andv colimit preserving∞-functors, and such that the induced nat-
ural transformationg∗◦v⇒u◦f∗ is an equivalence. We will write
∞-Catµ⊂ Fun(∆1,∞-Cat)
for the (non-full) sub-(2,∞)-category ofµ-categories andµ-morphisms.
Remark 1.3. Let us highlight the variance of the∞-functors in the above
definition: we have decided to use theleft adjointsu and v, instead of their
right adjointsu∗ and v∗ to specify the variance. Aµ-morphism is therefore
given by a commutative square as in Definition 1.2 that isright adjointable
in the sense of [Lur22, Def. 4.7.4.13].
Remark 1.4. The condition on aµ-morphism implies that we have several
canonical equivalences between functors, obtained by taking various adjoints
g∗◦v≃u◦f∗ v◦f∗≃g∗◦u v ∗◦g∗≃f∗◦u∗.
4
Using this, there are various equivalent ways of definingµ-morphisms. For
instance, a µ-morphism from T′
1 → T1 to T′
2 → T2 can equivalently be
encoded by aleft adjointable square in∞-Cat of the form
T′
2
u∗ //
f∗

T′
1
g∗

T2 v∗
//T1,
This exhibits∞-Catµ ⊂ Fun(∆1,∞-CatR
pr)op as a (non-full) sub-(2,∞)-
category of theopposite (2,∞)-category of morphisms in∞-CatR
pr.
By definition, an objectT′→T can also be written, up to equivalence,
as the forgetful∞-functor LModM(T )→ T for a monadM on T, which
furthermorecommuteswithsiftedcolimits. Objectsin ∞-Catµ cantherefore
be identified, up to equivalence, with pairs(T′,M ), withT a presentable∞-
category and M a sifted colimit preserving monad on T. Morphisms in
∞-Catµ can then be viewed as∞-functors endowed with compatibility data
with the monads; see [Hau21] for more details. This is our justification for
the terminologyµ-category, whereµ stands formonad.
We will often present objects in∞-Catµ as pairs(T,M ) of a presentable
∞-category T and a sifted colimit preserving monad M on T. The ∞-
category T will be called theunderlying∞-category of the object (T,M ).
The association (T,M )7→T defines an evident forgetful(2,∞)-functor
∞-Catµ→∞ -CatL
pr,
where∞-CatL
