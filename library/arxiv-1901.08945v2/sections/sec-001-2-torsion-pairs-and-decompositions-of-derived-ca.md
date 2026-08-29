---
doc_id: arxiv-1901.08945v2
doc_title: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES"
section_id: sec-001-2-torsion-pairs-and-decompositions-of-derived-ca
section_title: "Torsion pairs and decompositions of derived categories"
section_number: 2
pages: 5-13
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
doc_brief: "DECOMPOSITIONS OF DERIVED CATEGORIES OF GERBES — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group decomposes accordi ng to the char- acters of"
---
We give criteria ensuring that a torsion pair in an abelian category give s rise
to a semi-orthogonal decomposition on the level of derived catego ries. Our main
assumption on the torsion pair is that its two components are abelian subcategories
6 DANIEL BERGH AND OLAF M. SCHN ¨URER
of the ambient abelian category. For bounded derived categories t his is straight-
forward (see Theorem 2.7) as soon as some foundational results for such torsion
pairs are established (see Proposition 2.5). Our result for unbounded derived cat-
egories (see Theorem 2.22) needs some technical assumptions on eﬀectiveness of
inverse and direct truncation systems introduced in Section 2.3. Fortunately, these
assumptions are satisﬁed for the derived category D qc(X) of an algebraic stack (see
Example 2.19 and Proposition 2.20).
2.1. T orsion pairs. We remind the reader of the notion of a torsion pair . Some-
times the terminology torsion theory is used in the literature. Standard references
are [ BR07, I.1], [ Bor94, 1.12], [ Dic66].
Deﬁnition 2.1. A torsion pair in an abelian category B is a pair ( T, F ) of strictly
full subcategories of B such that the following two conditions hold:
(TP1) Any object B ∈ B ﬁts into a short exact sequence
0 →T →B →F → 0
with T ∈ T and F ∈ F .
(TP2) We have Hom B(T,F ) = 0 for all objects T ∈ T and F ∈ F .
Remark 2.2. Let ( T, F ) be a torsion pair in an abelian category B. The axioms of
a torsion pair immediately imply that the short exact sequence in (TP1) is unique
up to unique isomorphism and functorial in B ∈ B . In particular, there are functors
t : B → T and f : B → F together with natural transformations t → id and id →f
giving rise to short exact sequences
0 →t(B) →B →f (B) → 0,
for each object B ∈ B . The object B is in T (resp. F ) if and only if f (B) = 0 (resp.
t(B) = 0). The functor t is right adjoint to the inclusion functor T → B , and the
functor f is left adjoint to the inclusion functor F → B .
Recall that an abelian subcategory of an abelian category is a strictly full subcate-
gory which is abelian and whose inclusion functor is exact. A weak Serre subcategory
is an abelian subcategory which is closed under extensions in the ambie nt category.
If it is even closed under taking subobjects and quotients in the amb ient category,
it is called a Serre subcategory.
Remark 2.3. In the following we are only interested in torsion pairs ( T, F ) where
both T and F are abelian subcategories. These torsion pairs are traditionally calle d
hereditary and cohereditary. We do not use this terminology.
Example 2.4. Let B be the category of representations of the A2-quiver 1 → 2
over some ring. If T (resp. F ) denotes the subcategory of representations supported
at the vertex 2 (resp. 1) then ( T, F ) is clearly a torsion pair in B. Moreover, both
T and F are abelian subcategories of B.
Proposition 2.5. Let (T, F ) be a torsion pair in an abelian category B. If both T
and F are abelian subcategories of B, then the following statements are true.
(a) HomB(F,T ) = 0 for all objects F ∈ F and T ∈ T .
(b) Both the right adjoint to the inclusion functor T → B and the left adjoint to
the inclusion functor F → B are exact, i.e., in the notation of Remark 2.2,
both functors t and f are exact.
(c) Both T and F are Serre subcategories of B.
(d) Extn
B(T,F ) = 0 for all objects T ∈ T , F ∈ F and all integers n ∈ Z.
DECOMPOSITIONS 7
Remark 2.6. The most interesting part of Proposition 2.5 is certainly the Ext-
vanishing result in part (d). After writing down its proof we learned that Brion
has recently obtained the same result [ Bri18, Lemma 2.3]. For the convenience of
the reader we give a full proof of Proposition 2.5 even though parts (a), (b), (c) are
well-known or straightforward.
Proof. (a) Letϕ : F →T be a morphism from F ∈ F toT ∈ T . By (TP1), we may
put Ker(ϕ) into a short exact sequence 0 →T ′ → Ker(ϕ) →F ′ → 0 with T ′ ∈ T
and F ′ ∈ F . Since the composition of monomorphisms T ′ → Ker(ϕ) →F is zero,
by (TP2), we have T ′ = 0 and Ker( ϕ) ∈ F . Similarly one shows Cok( ϕ) ∈ T .
But then Im(ϕ) is the cokernel of Ker( ϕ) →F and the kernel of T → Cok(ϕ) and
hence is in F ∩ T since both F and T are abelian subcategories, i.e., Im( ϕ) = 0
and ϕ = 0.
(b) We use the notation of Remark 2.2. Clearly, t and f are additive. Let
0 → B1 → B2 → B3 → 0 be a short exact sequence in B. Then we obtain a
commutative diagram with exact rows
0 /d47/d47t(B3) /d47/d47B3 /d47/d47f (B3) /d47/d47 0
0 /d47/d47t(B2) /d47/d47
/d79/d79
B2 /d47/d47
/d79/d79
f (B2) /d47/d47
/d79/d79
0
0 /d47/d47t(B1) /d47/d47
/d79/d79
B1 /d47/d47
/d79/d79
f (B1) /d47/d47
/d79/d79
0.
We view the columns as complexes in B by adding zeroes. Then the diagram is
a short exact sequence of complexes and gives rise to a long exact s equence on
cohomology. Since the middle column is exact, since the cohomology ob jects of
the left (resp. right) column are in T (resp. F ), and since there are no nonzero
morphisms from F to T , by (a), the other two columns are also exact. This shows
that t and f are exact.
(c) LetF →B →F ′ be an exact sequence in B whereF andF ′ are objects of F .
To see that F is a Serre subcategory of B we need to see that B ∈ F . The functor
t : B → T is exact, by (b), and hence yields the exact sequence t(F ) →t(B) →t(F ′)
in T . Since t(F ) = 0 = t(F ′) we obtain t(B) = 0, i.e., B ∈ F .
The same argument proves that T is a Serre subcategory of B.
(d) The claim is trivially true for n< 0. For n = 0 it is true by axiom (TP2) of
a torsion pair.
Forn = 1 we need to prove that Ext 1
B(T,F ) = 0 for T ∈ T and F ∈ F . Using
Yoneda extensions (and [ SP19, Tag 06XU]) it is enough to show that any short
exact sequence 0 → F → B → T → 0 in B splits. Since t is exact, by (b), and
t(F ) = 0, we obtain a morphism of short exact sequences
0 /d47/d47 0 /d47/d47
/d15/d15
t(B) ∼ /d47/d47
/d15/d15
t(T ) /d47/d47
∼
/d15/d15
0
0 /d47/d47F /d47/d47B /d47/d47T /d47/d47 0
in B; the vertical arrow on the right is an isomorphism since T ∈ T and hence
f (T ) = 0. This shows that our sequence splits. (Since Hom B(T,F ) = 0, the
splitting is in fact unique.)
Now let n ≥ 2. Let f ∈ Extn
B(T,F ), i.e., f : T → ΣnF is a morphism in
D(B). The n-extension f can be written as the composition of a 1-extension and
an (n − 1)-extension: this is easy to prove directly or follows alternatively u sing
8 DANIEL BERGH AND OLAF M. SCHN ¨URER
Yoneda extensions and [ SP19, Tag 06XU]. Anyhow, there is an object B ∈ B such
that f is the composition
f : T
g
− →Σn−1B
Σ n−1h
− − − − →ΣnF,
where g and h : B → ΣF are morphisms in D( B). The long exact Ext B(−,F )-
sequence obtained from the short exact sequence 0 → t(B) → B
π
− →f (B) → 0
yields an isomorphism
π∗ : Ext 1
B(f (B),F )
∼
− →Ext1
B(B,F )
since we already know that Ext 1
B(t(B),F ) and Hom B(t(B),F ) vanish. Hence h has
the form h =h′ ◦π for a (unique) morphism h′ : f (B) → ΣF in D( B). Then
f = (Σ n−1h) ◦g = (Σ n−1h′) ◦ (Σn−1π) ◦g.
By induction, the ( n − 1)-extension (Σ n−1π) ◦g : T → Σn−1f (B) vanishes. Hence
f = 0. □
2.2. Decompositions of bounded derived categories. If S is a weak Serre
subcategory of an abelian category B, the full subcategory of D( B) of objects with
cohomology objects in S is denoted D S(B). Let D −
S (B), D +
S (B), and D b
S(B) denote
the full subcategories of D S(B) of objects whose cohomology is bounded above,
bounded below, and bounded, respectively. All these categories a re strictly full
triangulated subcategories of D( B), see, e.g., [ SP19, Tag 06UQ]. We refer the reader
to [ BS17, Subsection 5.1] for the notion of a semi-orthogonal decompositio n.
Theorem 2.7. Let B be a weak Serre subcategory of an abelian category A. Let T
and F be abelian subcategories of B forming a torsion pair (T, F ) in B. Assume
that
(2.1) Ext n
A(T,F ) = 0
for all objects T ∈ T , F ∈ F and all integers n. Then
Db
B(A) = ⟨Db
F (A), Db
T (A)⟩
is a semi-orthogonal decomposition.
Remark 2.8. Condition ( 2.1) is automatically satisﬁed in the special case when
B = A, by Proposition 2.5.(d). In general, the condition is automatically satisﬁed
for n ≤ 1 by the same proposition, since B is closed under extensions.
Proof. By Proposition 2.5.(c), F and T are Serre subcategories of B, hence weak
Serre subcategories of A, and D b
F (A) and D b
T (A) are strictly full triangulated sub-
categories of D b
B(A).
Repeated use of truncation shows that D b
B(A) coincides with its smallest strictly
full triangulated subcategory containing B. Axiom (TP1) shows that it is also
its smallest such subcategory containing both F and T . In particular, D b
B(A) is
generated, as a triangulated category, by its subcategories D b
F (A) and D b
T (A).
By truncation and condition ( 2.1), there are no nonzero morphisms from D b
T (A)
to D b
F (A). □
2.3. Some notes on homotopy limits of truncations. Our aim is to state
and prove Theorem 2.22 in the following subsection 2.4 which is the analog of
Theorem 2.7 for unbounded derived categories. In order to to this, we need so me
terminology and some basic observations.
We refer the reader to [ Nee01, Deﬁnition 1.6.4] for the notion of a homotopy
colimit. The deﬁnition of a homotopy limit is dual.
Let A be an abelian category. We propose the following terminology.
DECOMPOSITIONS 9
Deﬁnition 2.9.
(a) An inverse system
(Fn)n∈N = (... →Fn+1 →Fn →... →F2 →F1 →F0)
in D( A) is an inverse truncation system if for each n ∈ N the object Fn
is in D ≥−n(A) and the map τ≥−nFn+1 → Fn induced by the transition
morphism is an isomorphism (cf. Remark 2.13 for a reformulation).
(b) If D( A) has countable products, an inverse truncation system ( Fn)n∈N in
D(A) is eﬀective if the induced maps H p(holimnFn) → limn Hp(Fn), are
isomorphisms for all p ∈ Z. Our assumption ensures the existence of ho-
motopy limits, and all limits lim n Hp(Fn) exist by Remark 2.13 below.
Dually, we deﬁne a direct truncation system in the obvious way. If D( A) has
countable coproducts we can talk about eﬀectiveness of direct truncation systems.
Example 2.10. Given any object F in D( A), we get an inverse truncation sys-
tem (τ≥−nF )n∈N whose transition morphisms are the natural maps between the
truncations. Similarly, we get a direct truncation system ( τ≤nF )n∈N.
Deﬁnition 2.11. An inverse (resp. direct) truncation system is called standard if
it is isomorphic to an inverse (resp. direct) truncation system as in E xample 2.10.
Remark 2.12. Informally, one may think of an arbitrary inverse truncation syste m
as obtained from a possibly non-existing object by truncation. Eﬀe ctiveness says
that the natural candidate for such an object, the homotopy limit , indeed does the
job. We explain this in Remark 2.14 below.
Remark 2.13. An inverse system ( Fn)n∈N in D( A) is an inverse truncation system
if and only if H p(Fn) = 0 for all p< −n and the maps Hp(Fn+1) → Hp(Fn) induced
by the transition maps are isomorphisms for all p ≥ −n. This just means that the
induced inverse systems (H p(Fn))n∈N look as follows.
... ∼ /d47/d47 H1(F2) ∼ /d47/d47 H1(F1) ∼ /d47/d47 H1(F0)
... ∼ /d47/d47 H0(F2) ∼ /d47/d47 H0(F1) ∼ /d47/d47 H0(F0)
... ∼ /d47/d47 H−1(F2) ∼ /d47/d47 H−1(F1) /d47/d47 0
... ∼ /d47/d47 H−2(F2) /d47/d47 0 /d47/d47 0
In particular, then all limits lim n Hp(Fn) exist in A.
Remark 2.14. Assume that D( A) has countable products. Let G := holimnFn be
a homotopy limit of an inverse truncation system ( Fn)n∈N. It comes together with
morphisms G → Fn, for all n ∈ Z. Since Fn ∈ D≥−n(A) they come from unique
morphisms τ≥−nG → Fn. Then, as a consequence of Remark 2.13, the following
conditions are equivalent.
(a) The inverse truncation system ( Fn)n∈N is eﬀective.
(b) For all p ∈ Z there is an integer n ≥ −p such that H p(G) → Hp(Fn) is
an isomorphism; this condition is then automatically true for all intege rs
n ≥ −p.
(c) The morphism ( τ≥−nG)n∈N → (Fn)n∈N of inverse truncation systems is an
isomorphism.
In particular, any eﬀective inverse truncation system is standard in the sense of
Deﬁnition 2.11; more precisely, up to canonical isomorphism it is obtained by trun-
cation from its homotopy limit.
We address the natural question whether an object is the homoto py limit of its
truncations.
10 DANIEL BERGH AND OLAF M. SCHN ¨URER
Lemma 2.15 (Objects as homotopy limits of their truncations) . LetF be an object
of D(A) and assume that D(A) has countable products. If the inverse truncation
system (τ≥−nF )n∈N is eﬀective there is a triangle
F →
∏
n∈N
τ≥−nF →
∏
n∈N
τ≥−nF → ΣF
in D(A) which exhibits F as a homotopy limit of its truncations and whose ﬁrst
morphism is induced by the truncation maps F →τ≥−nF .
Proof. LetG be a homotopy limit of the given inverse system with deﬁning triangle
G →
∏
τ≥−nF →
∏
τ≥−nF → ΣG.
The obvious map from F to the second term of this triangle comes from a (possibly
non-unique) morphism γ : F → G to its ﬁrst term which makes the upper left
triangle in the following diagram commutative. Since the map G →τ≥−nF factors
through the truncation map G →τ≥−nG, we obtain the commutative diagram
F /d47/d47
γ
/d15/d15
τ≥−nF
G /d47/d47
/d60/d60①①①①①①①①① τ≥−nG.
/d79/d79
Its right vertical arrow is an isomorphism since the inverse truncat ion system
(τ≥−nF )n∈N is eﬀective, by the equivalent statements in Remark 2.14. Hence the
inverse of this arrow is the morphism τ≥−n(γ) which is therefore an isomorphism.
Since n ∈ N was arbitrary, this implies that γ is an isomorphism. The claim fol-
lows. □
We now provide instances of inverse and direct truncation systems that are
eﬀective. The following proposition is essentially Remark 2.3 in [ BN93].
Proposition 2.16. Let A be an abelian category. If A has countable products
which are exact then any inverse truncation system in D(A) is eﬀective. Dually,
if A has exact countable coproducts then any direct truncation s ystem in D(A) is
eﬀective.
Proof. Since the statements are dual, it is enough to prove one of them. We prove
the ﬁrst statement.
It is clear that D( A) has all countable products. Let ( Fn)n∈N be an inverse
truncation system in D( A). Consider a homotopy limit holim nFn together with a
deﬁning triangle
holimnFn →
∏
n
Fn
1−σ
− − − →
∏
n
Fn → Σ holimnFn,
whereσ is the shift map. Since A has exact countable products, the functor H p(−)
preserves countable products for all p. Hence, we get an exact sequence
...
δ
− →Hp(holimnFn) →
∏
n
Hp(Fn)
1−σ
− − − →
∏
n
Hp(Fn)
δ
− →Hp+1(holimnFn) →...
in A where σ is again the shift map. Note that the inverse system (H p(Fn))n∈N is
zero for n <−p and constant for n ≥ −p (cf. Remark 2.13). Hence Remark 2.17
below shows that all morphisms 1 −σ in our exact sequence are epimorphisms, i.e.,
all connecting morphisms δ vanish. Hence the canonical morphism
Hp(holimnFn) → lim
n
Hp(Fn)
is an isomorphism, i.e., our inverse truncation system is eﬀective. □
DECOMPOSITIONS 11
Remark 2.17. If an inverse system ( Gn)n∈N in an additive category with countable
products is eventually constant in the sense that there is an N ∈ N such that all
transition morphisms Gn+1 →Gn forn ≥N are isomorphisms, then the morphism
“identity minus shift”
1 −σ :
∏
n∈N
Gn →
∏
n∈N
Gn
is a split epimorphism: there is a morphism f in the other direction such that
(1 −σ) ◦f = id. We leave the easy proof of this fact to the reader.
Example 2.18. If R is an arbitrary ring, then all inverse and direct truncation
systems in the derived category D(Mod( R)) of R-modules are eﬀective, by Propo-
sition 2.16.
Example 2.19. If (X, O) is a ringed topos, then the category of O-modules is
Grothendieck abelian. In particular, it has arbitrary small product s and coproducts
and all coproducts are exact; in particular, any direct truncation system in D(X) is
eﬀective, by Proposition 2.16. Products, however, need not be exact. Nevertheless,
certain inverse truncation systems may still be eﬀective, see Prop osition 2.20 below.
The following proposition follows from the proof of [ SP19, Tag 0D6M], which
basically is an abstract version of a result by B¨ okstedt–Neeman [BN93, Lemma 5.3].
Proposition 2.20. Let X be an algebraic stack. Then any inverse truncation
system in D(X) with terms in Dqc(X) is eﬀective.
Proof. It is clear that D( X) has all products. Let ( Fn)n∈N be an inverse truncation
system in D(X) whose terms Fn lie in D qc(X).
By the deﬁnition of an inverse truncation system, the transition mo rphism
Fn+1 →Fn factors as Fn+1 →τ≥−nFn+1
∼
− →Fn, and we obtain a triangle
Σn+1 H−n−1(Fn+1) →Fn+1 →Fn → Σn+2 H−n−1(Fn+1)
for each n ∈ N. Fix p ∈ Z. Since the cohomology sheaves are assumed to be
quasi-coherent, the functor H p(U, −) vanishes on the ﬁrst and fourth term of this
triangle for all n ≥ −p and all aﬃne schemes U which are smooth over X. Hence
Hp(U,Fn+1) → Hp(U,Fn) is an isomorphism for all n ≥ −p, i.e., the inverse system
(Hp(U,Fn))n∈N of abelian groups is eventually constant. By Remark 2.17, the
morphism “identity minus shift”
1 −σ :
∏
n
Hp(U,Fn) →
∏
n
Hp(U,Fn)
is a (split) epimorphism. Its kernel is lim n Hp(U,Fn).
Note that the functors Hq(U, −) = Hq(RΓ(U, −|U )) commute with products since
the functors restriction to U and RΓ(U, −) are right adjoints and products are exact
in the category of abelian groups. Hence applying H p(U, −) to the deﬁning triangle
of the homotopy limit holim nFn yields an exact sequence
... → Hp(U, holimnFn) →
∏
n
Hp(U,Fn)
1−σ
− − − →
∏
n
Hp(U,Fn) →...
of abelian groups. Since all morphisms 1 −σ are surjective, as observed above, this
sequence splits into short exact sequences, and we get isomorphis ms
Hp(U, holimnFn)
∼
− →lim
n
Hp(U,Fn)
∼
− →Hp(U,Fm)
for all m ≥ −p. For an arbitrary object G in D(X), the sheaf Hp(G) is the sheaf as-
sociated to the presheaf U ↦→Hp(U,G ). Hence the canonical map H p(holimnFn) →
Hp(Fm) is an isomorphism for all m ≥ −p. This means that our system is eﬀective,
by Remark 2.14. □
12 DANIEL BERGH AND OLAF M. SCHN ¨URER
2.4. Decompositions of unbounded derived categories. Now we can state
and prove Theorem 2.22.
Remark 2.21. Let B be a weak Serre subcategory of an abelian category A and let
T and F be abelian subcategories of B forming a torsion pair ( T, F ) in B. Consider
an arbitrary triangle
B′ →B →B′′ → ΣB′
in D B(A). Then we have B′ in D T (A) and B′′ in D F (A) if and only if the long
exact cohomology sequence splits up into short exact sequences
0 → Hp(B′) → Hp(B) → Hp(B′′) → 0
with ﬁrst term H p(B′) in T and third term H p(B′′) in F , for each p ∈ Z. The
“if”-part is trivial, and the “only if”-part is a simple consequence of t he fact that
HomB(F,T ) vanishes for each object F in F and T in T , by Proposition 2.5.(a).
Theorem 2.22. Let B be a weak Serre subcategory of an abelian category A. Let
(T, F ) be a torsion pair in B where both T and F are abelian subcategories of B.
Assume that
Extn
A(T,F ) = 0
for all objects T ∈ T , F ∈ F and all integers n ∈ Z. Assume that D(A) has
countable products and coproducts. If every inverse and eve ry direct truncation
system in D(A) with terms in DB(A) is eﬀective, in the sense of Deﬁnition 2.9,
then
DB(A) = ⟨DF (A), DT (A)⟩
is a semi-orthogonal decomposition.
Proof. Semi-orthogonality: We claim that
(2.2) Hom D(A)(L,R ) = 0
for all objects L ∈ DT (A) and R ∈ DF (A).
Our proof is a straightforward d´ evissage argument. Assume ﬁrs t that L is in
D−
T (A) and that R is in D +
F (A). Then any morphism L → R factors as L →
τ≥nL → τ≤mR → R for suﬃciently small n and suﬃciently large m. Hence the
morphism vanishes by Theorem 2.7.
Keep the assumption on L and assume that R is an arbitrary object of D F (A).
Eﬀectiveness of inverse truncation systems with terms in D B(A) and Lemma 2.15
provide a triangle
R →
∏
n∈N
τ≥−nR →
∏
n∈N
τ≥−nR → ΣR
in D( A). The functor Hom D(A)(L, −) vanishes on the second and third term and
their shifts by the universal property of products, boundednes s from below of the
truncations and the vanishing result already proven. Hence it vanis hes also on the
ﬁrst term as desired.
Similarly, eﬀectiveness of direct truncation systems with terms in D B(A) and the
dual of Lemma 2.15 give (2.2) for arbitrary objects L in D T (A) and R in D F (A).
Completeness: To ﬁnish the proof, we need to show that any object B in
DB(A) ﬁts into a triangle
(2.3) T →B →F → ΣT
with T in D T (A) and F in D F (A).
Assume ﬁrst that B is an object in D −
B (A) and consider its associated stan-
dard inverse truncation system ( Bn)n∈N where Bn = τ≥−nB (see Example 2.10).
DECOMPOSITIONS 13
Since the cohomology of each Bn is bounded, the semi-orthogonal decomposition
in Theorem 2.7 provides commutative squares
Tn /d47/d47
/d15/d15
Tn+1
/d15/d15
Bn /d47/d47Bn+1,
Hp(Tn) /d47/d47
/d15/d15
Hp(Tn+1)
/d15/d15
Hp(Bn) /d47/d47 Hp(Bn+1),
where each Tn is the projection of Bn to D b
T (A) along this semi-orthogonal de-
composition. By Remark 2.21, the vertical maps in the right diagram are just the
torsion subobjects with respect to the torsion pair ( T, F ). The characterization
of inverse truncation systems in Remark 2.13 and the fact that ( Bn)n∈N is such
a system make it clear that ( Tn)n∈N is such a system as well. By assumption, it
is eﬀective, and hence obtained from its homotopy limit T in D( A) by truncation
in a canonical way, see Remark 2.14. Without loss of generality we may hence
assume that Tn = τ≥−nT for all n ∈ N. It is clear that T ∈ D−
T (A). Note that T
and B are the homotopy limits of the eﬀective inverse truncation systems (Tn)n∈N
and (Bn)n∈N, by Lemma 2.15. Hence the morphism ( Tn)n∈N → (Bn)n∈N of in-
verse systems induces a morphism T →B which makes the following two squares
commutative.
T /d47/d47
/d15/d15
Tn
/d15/d15
B /d47/d47Bn
Hp(T ) /d47/d47
/d15/d15
Hp(Tn)
/d15/d15
Hp(B) /d47/d47 Hp(Bn)
Obviously, the horizontal arrows in the right square are isomorphisms for alln ≥ −p.
Hence Hp(T ) → Hp(B) is the torsion subobject with respect to the torsion pair
(T, F ), for each p ∈ Z. Complete the morphism T → B to a triangle as in ( 2.3).
Then the associated long exact sequence on cohomology splits up int o short exact
sequences with H p(F ) in F . In particular, the object F is in D −
F (A).
This establishes the semi-orthogonal decomposition D −
B (A) = ⟨D−
F (A), D−
T (A)⟩.
By the dual version of the argument above, starting with an objec tB in D B(A) and
using the fact that all direct truncation systems with terms in D B(A) are eﬀective,
we get the desired semi-orthogonal decomposition of D B(A). □
