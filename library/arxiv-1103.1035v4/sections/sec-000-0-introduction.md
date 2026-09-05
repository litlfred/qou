---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-9
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
1. Some Facts about DG Lie Algebras 4
2. The Reduced Deligne Groupoid 7
3. DG Lie Quasi-isomorphisms – Nilpotent Algebras 10
4. DG Lie Quasi-isomorphisms – Pronilpotent Algebras 14
5. Some Facts on 2-Groupoids 18
6. The Deligne 2-Groupoid 21
7. L ∞ Morphisms and Coalgebras 24
8. L ∞ Quasi-isomorphisms between Pronilpotent Algebras 26
References 31
0. I ntroduction
Let K be a ﬁeld of characteristic 0. By parameter algebra over K we mean a
complete local noetherian commutative K-algebra R, with maximal ideal m, such
that R/m = K. The important example is R = K[[¯h]], the ring of formal power
series in the variable ¯h.
Date: 6 February 2012.
Key words and phrases. DG Lie algebras, L-inﬁnity morphisms, Deligne groupoid, Deformation
quantization.
Mathematics Subject Classiﬁcation 2000. Primary: 53D55; Secondary: 17B40, 14B10, 18D05.
This research was supported by the Israel Science Foundation.
1
arXiv:1103.1035v4  [math.QA]  10 Feb 2012
2 AMNON YEKUTIELI
Let (R, m) be a parameter algebra, and let g = ⨁
i∈Z gi be a DG (differential
graded) Lie algebra over K. There is an induced pronilpotent DG Lie algebra
mˆ⊗ g =
⨁
i∈Z
mˆ⊗ gi.
A solution ω∈ mˆ⊗ g1 of the Maurer-Cartan equation
d(ω) + 1
2 [ω, ω] = 0
is called an MC element. The set of MC elements is denoted by MC (g, R). There
is an action of the gauge group exp(mˆ⊗ g0) on the set MC (g, R), and we write
(0.1) MC(g, R) := MC(g, R)/ exp(mˆ⊗ g0),
the quotient set by this action.
The Deligne groupoid Del(g, R), introduced in [GM], is the transformation
groupoid associated to the action of the group exp (mˆ⊗ g0) on the set MC (g, R).
So the set π0(Del(g, R)) of isomorphism classes of objects of this groupoid equals
MC(g, R). In [GM, Theorem 2.4] it was proved that if R is artinian, g and h are DG
Lie algebras concentrated in the degree range [0, ∞) (we refer to this as the “non-
negative nilpotent case”), and φ : g→ h is a DG Lie algebra quasi-isomorphism,
then the induced morphism of groupoids
Del(φ, R) : Del(g, R)→ Del(h, R)
is an equivalence.
We introduce the reduced Deligne groupoid Delr(g, R), which is a certain quo-
tient of the Deligne groupoid Del(g, R); see Section 2 for details. If the Deligne
2-groupoid Del2(g, R) is deﬁned (see below), then
(0.2) Delr(g, R) = π1(Del2(g, R)).
However the groupoid Delr(g, R) always exists. This new groupoid also has the
property that
π0(Delr(g, R)) = MC(g, R).
Here is the ﬁrst main result of our paper. It is a generalization to the un-
bounded pronilpotent case (i.e. the DG Lie algebras g and h can be unbounded,
and the parameter algebra R doesn’t have to be artinian) of [GM, Theorem 2.4].
Our proof is similar to that of [GM, Theorem 2.4]: we also use obstruction classes.
Theorem 0.3. Let R be a parameter algebra over K, and let φ : g→ h be a DG Lie
algebra quasi-isomorphism over K. Then the morphism of groupoids
Delr(φ, R) : Delr(g, R)→ Delr(h, R)
is an equivalence.
This is Theorem 4.2 in the body of the paper.
A DG Lie algebra g = ⨁
i∈Z gi is said to be of quantum type if gi = 0 for all
i <−1. A DG Lie algebra ˜g is said to be of quasi quantum type if there exists
a DG Lie quasi-isomorphism ˜g→ g, for some quantum type DG Lie algebra g.
Important examples of such DG Lie algebras are given in Example 6.2. In Section
6 we prove that if R is artinian, or if g is of quasi quantum type, then the Deligne
2-groupoid Del2(g, R) exists. The original construction (see [Ge]) applied only to
the case when R is artinian and g is of quantum type.
Here is the second main result of this paper (repeated as Theorem 6.13):
MC ELEMENTS 3
Theorem 0.4. Let R be a parameter algebra, let g and h be DG Lie algebras, and let
φ : g→ h be a DG Lie algebra quasi-isomorphism. Assume either of these two conditions
holds:
(i) R is artinian.
(ii) g and h are of quasi quantum type.
Then the morphism of 2-groupoids
Del2(φ, R) : Del2(g, R)→ Del2(h, R)
is a weak equivalence.
The proof of Theorem 0.4 relies on Theorem 0.3, via formula (0.2). Theorem
0.4 plays a crucial role in our new proof of twisted deformation quantization, in the
revised version of [Ye4].
An L∞ morphism Φ : g→ h is a sequence Φ ={φj}j≥1 of K-linear functions
φj :⋀jg→ h
that generalizes the notion of DG Lie algebra homomorphism φ : g→ h. Thus φ1 :
g→ h is a DG Lie algebra homomorphism, up to a homotopy given by φ2; and so
on. See Section 7 for details. The morphism Φ is called an L ∞ quasi-isomorphism
if φ1 : g → h is a quasi-isomorphism. The concept of L ∞ morphism gained
prominence after the Kontsevich Formality Theorem from 1997 (see [Ko2]).
An L∞ morphism Φ : g→ h induces an R-multilinear L∞ morphism
ΦR ={φR,j}j≥1 : mˆ⊗ g→ mˆ⊗ h.
Given an element ω∈ mˆ⊗ g1 we write
(0.5) MC (Φ, R)(ω) := ∑
j≥1
1
j! φR,j(ω, . . . ,ω| {z }
j
)∈ mˆ⊗ h1.
This sum converges in them-adic topology of mˆ⊗ h1. It is known that the function
MC(Φ, R) sends MC elements to MC elements, and it respects gauge equivalence
(see Propositions 8.2 and 8.7). So there is an induced function MC(Φ, R) from
MC(g, R) to MC(h, R).
Here is the third main result of our paper.
Theorem 0.6. Let g and h be DG Lie algebras, let R be a parameter algebra, and let
Φ : g→ h be an L∞ quasi-isomorphism, all over the ﬁeld K. Then the function
MC(Φ, R) : MC(g, R)→ MC(h, R)
is bijective.
This is Theorem 8.13 in the body of the paper. We emphasize that this result is
in the unbounded pronilpotent case. The proof of Theorem 0.6 goes like this: we
use the bar-cobar construction to reduce to the case of a DG Lie algebra quasi-
isomorphism ˜Φ : ˜g→ ˜h; and then we use Theorem 0.3.
Theorem 0.6 was known in the nilpotent case; see [Ko2, Theorem 4.6], and
[CKTB, Theorem 3.6.2]. The proof sketched in [Ko2, Section 4.5] relies on the
structure of L ∞ algebras. The proof in [CKTB, Section 3.7] relies on the work of
Hinich on the Quillen model structure of coalgebras. It is not clear whether these
methods work also in the pronilpotent case.
In this paper we only consider pronilpotent DG Lie algebras of the form mˆ⊗ g.
Presumably Theorems 0.3, 0.4 and 0.6 can be extended to a more general setup –
see Remark 4.4.
4 AMNON YEKUTIELI
Acknowledgments. I wish to thank James Stasheff, Vladimir Hinich, Michel
Van den Bergh, William Goldman, Oren Ben Bassat, Marco Manetti and Ronald
Brown for useful conversations. Thanks also to the referee for reading the paper
carefully and providing several constructive remarks.
1. S ome Facts about DG Lie Algebras
Let K be a ﬁeld of characteristic 0. Given K-modules V, W we write V⊗ W
and Hom(V, W) instead of V⊗K W and HomK(V, W), respectively.
Deﬁnition 1.1. By parameter algebra over K we mean a complete noetherian local
commutative K-algebra R, with maximal ideal m, such that R/m = K. We call m
a parameter ideal.
The most important example is of course R = K[[¯h]], where ¯h is a variable,
called the deformation parameter.
Note that R = K⊕ m, so the ring R can be recovered from the nonunital algebra
m. For any j∈ N let Rj := R/mj+1 and mj := m/mj+1. So R0 = K, each Rj is an
artinian local ring with maximal ideal mj, R∼= lim←j Rj, and m∼= lim←j mj.
Let us ﬁx a parameter algebra (R, m). Given an R-module M, its m-adic comple-
tion is
ˆM := lim
←j
(Rj⊗R M).
The module M is called m-adically complete if the canonical homomorphism M→
ˆM is bijective. (Some texts would say that M is complete and separated.) Since
R is noetherian, the m-adic completion ˆM of any R-module M is m-adically com-
plete; see [Ye5, Corollary 3.5].
Given an R-module M and a K-module V let us write
(1.2) Mˆ⊗ V := lim
←j
(Rj⊗R (M⊗ V)),
namely Mˆ⊗ V is the m-adic completion of the R-module M⊗ V. If W is another
K-module, then there is a unique R-module isomorphism
Mˆ⊗ (V⊗ W)∼= (Mˆ⊗ V)ˆ⊗ W
that commutes with the canonical homomorphisms from M⊗ V⊗ W; hence we
shall simply denote this complete R-module by Mˆ⊗ Vˆ⊗ W.
Let g =⨁
i∈Z gi be a DG Lie algebra over K. (There is no ﬁniteness assumption
on g.) For any i let mˆ⊗ gi be the complete tensor product as in (1.2). We get a
pronilpotent R-linear DG Lie algebra
(1.3) mˆ⊗ g :=
⨁
i∈Z
mˆ⊗ gi,
with differential d and graded Lie bracket [−,−] induced from g.
Recall that the Maurer-Cartan equation in mˆ⊗ g is
(1.4) d (ω) + 1
2 [ω, ω] = 0
for ω∈ mˆ⊗ g1. A solution of this equation is called an MC element of mˆ⊗ g. The
set of MC elements is denoted by MC (mˆ⊗ g). In degree 0 we have a pronilpo-
tent Lie algebra mˆ⊗ g0, so there is an associated pronilpotent group exp (mˆ⊗ g0),
called the gauge group, and a bijective function
exp : mˆ⊗ g0→ exp(mˆ⊗ g0)
called the exponential map.
MC ELEMENTS 5
An element γ∈ mˆ⊗ g0 acts on mˆ⊗ g by the derivation
(1.5) ad (γ)(α) := [ γ, α].
We view ad (γ) as an element of Rˆ⊗ End(g)0. Let g := exp(γ)∈ exp(mˆ⊗ g0),
and deﬁne
(1.6) Ad (g) := exp(ad(γ)) = ∑
i≥0
1
i! ad(γ)i∈ Rˆ⊗ End(g)0
(this series converges in the m-adic topology). The element Ad (g) is an R-linear
automorphism of the graded Lie algebra mˆ⊗ g. There is an induced group auto-
morphism Ad (g) of the group exp (mˆ⊗ g0), and this automorphism satisﬁes the
equation
(1.7) Ad (g)(h) = g◦ h◦ g−1
for all h∈ exp(mˆ⊗ g0).
There is another action of γ∈ mˆ⊗ g0 on ω∈ mˆ⊗ g1:
(1.8) af (γ)(ω) := [ γ, ω]− d(γ) = ad(γ)(ω)− d(γ).
This is an afﬁne action, namely
af(γ)∈ Rˆ⊗
(
End(g1)⋉ g1)
.
Consider the elements g := exp(γ)∈ exp(mˆ⊗ g0) and
(1.9) Af (g) := exp(af(γ)) = ∑
i≥0
1
i! af(γ)i∈ Rˆ⊗
(
End(g1)⋉ g1)
.
(The series above converges in the m-adic topology.) We get an afﬁne action Af of
the group exp(mˆ⊗ g0) on the R-module mˆ⊗ g1. For ω∈ mˆ⊗ g1 this becomes
Af(g)(ω) = exp(ad(γ))(ω) + 1− exp(ad(γ))
ad(γ) (d(γ)).
The arguments in [GM, Section 1.3] (which refer to the case when gi are all ﬁnite
dimensional over K, gi = 0 for i < 0, and R is artinian) are valid also in our
inﬁnite case (cf. [Ge, Section 2.2]), and they show that Af (g) preserves the set
MC(mˆ⊗ g). (This can be proved also using the method of Lemma 1.14.) We write
(1.10) MC(mˆ⊗ g) := MC(mˆ⊗ g)
exp(mˆ⊗ g0) ,
the quotient set by this action. Given a homomorphism of DG Lie algebras φ :
g→ h, and homomorphism of parameter algebras f : (R, m)→ (S, n), there is an
induced function
(1.11) MC(φ⊗ f ) : MC(mˆ⊗ g)→ MC(nˆ⊗ h).
We shall need the following sort of algebraic differential calculus (which is
used a lot implicitly in deformation theory). Let K[t] be the polynomial algebra
in a variable t, and let M be a K-module. A polynomial f (t)∈ K[t]⊗ M deﬁnes
a function f : K→ M, namely for any λ∈ K the element f (λ)∈ M is gotten
by substitution t↦→ λ. We refer to f : K→ M as a polynomial function, or as a
polynomial path in M.
Let K[ϵ] := K[t]/(t2), where ϵ is the class of t. Given f (t)∈ K[t]⊗ M and
λ∈ K we denote by f (λ + ϵ)∈ K[ϵ]⊗ M the result of the substitution t↦→ λ + ϵ.
6 AMNON YEKUTIELI
Lemma 1.12. Let f (t)∈ K[t]⊗ M. If
f (λ + ϵ) = f (λ)
in K[ϵ]⊗ M for all λ∈ K, then f (λ) = f (0) for all λ∈ K.
Proof. This is an elementary calculation; note that K has characteristic 0. □
Given an element ω∈ MC(mˆ⊗ g), consider the R-linear operator (of degree 1)
(1.13) d ω := d + ad(ω)
on mˆ⊗ g.
Lemma 1.14. Let ω, ω′∈ MC(mˆ⊗ g), and let g ∈ exp(m⊗ g0) be such that ω′ =
Af(g)(ω). Then for any i∈ Z the diagram of R-modules
mˆ⊗ gi Ad(g) //
dω

mˆ⊗ gi
dω′

mˆ⊗ gi+1 Ad(g) // mˆ⊗ gi+1
is commutative.
Proof. Since mˆ⊗ gi and mˆ⊗ gi+1 are m-adically complete R-modules, it sufﬁces to
verify this after replacing R with Rj. Therefore we can assume that R is artinian.
Consider the DG Lie algebra K[t]⊗ m⊗ g. Let γ := log(g)∈ m⊗ g0, and
deﬁne
g(t) := exp(tγ)∈ exp(K[t]⊗ m⊗ g0)⊂ K[t]⊗ R⊗ End(g0).
So g(0) = 1 and g(1) = g. Next let
ω(t) := Af(g(t))(ω)∈ K[t]⊗ m⊗ g1,
which is an MC element of K[t]⊗ m⊗ g, and it satisﬁes ω(0) = ω and ω(1) = ω′.
Consider the polynomial
f (t) := Ad(g(1− t))◦ dω(t)◦ Ad(g(t))∈ K[t]⊗ R⊗ Hom(gi, gi+1).
It satisﬁes
f (0) = Ad(g)◦ dω
and
f (1) = dω′◦ Ad(g).
We will prove that f is constant. See diagram below depicting f (λ), λ∈ K.
m⊗ gi Ad(g(λ)) //

m⊗ gi
dω(λ)

// m⊗ gi

m⊗ gi+1 // m⊗ gi+1 Ad(g(1−λ)) // m⊗ gi+1
Take any λ∈ K. Then
f (λ + ϵ)− f (λ) =
Ad(g(1− ϵ− λ))◦
(
dω(λ+ϵ)◦ Ad(g(ϵ))− Ad(g(ϵ))◦ dω(λ)
)
◦ Ad(g(λ))
in K[ϵ]⊗ R⊗ Hom(gi, gi+1). A calculation shows that
Ad(g(ϵ)) = 1 + ϵ· ad(γ)∈ K[ϵ]⊗ R⊗ End(g)
MC ELEMENTS 7
and
ω(λ + ϵ) = ω(λ) + ϵ· [γ, ω(λ)]− ϵ· d(γ)∈ K[ϵ]⊗ m⊗ g1.
Hence for any α∈ R⊗ g−1 we have
(
dω(λ+ϵ)◦ Ad(g(ϵ))
)
(α) =
d(α) + ϵ· d([γ, α]) + [ω(λ + ϵ), α] + ϵ[ω(λ + ϵ), [γ, α]]
and (
Ad(g(ϵ))◦ dω(λ
)
(α) =
d(α) + [ω(λ), α] + ϵ[γ, d(α)] + ϵ[γ, [ω(λ), α]] .
After expanding terms and using the graded Jacobi identity we see that
(
dω(λ+ϵ)◦ Ad(g(ϵ))
)
(α) =
(
Ad(g(ϵ))◦ dω(λ
)
(α)
in K[ϵ]⊗ R⊗ g0. Therefore f (λ + ϵ) = f (λ). By Lemma 1.12 we conclude that f
is constant. □
Proposition 1.15. (1) Let ω∈ MC(mˆ⊗ g). Then dω is a degree 1 derivation of
the graded Lie algebra mˆ⊗ g, and dω◦ dω = 0. We obtain a new DG Lie algebra
(mˆ⊗ g)ω, with the same Lie bracket [−,−], and a new differential dω.
(2) Let g∈ exp(mˆ⊗ g0), and let ω′ := Af(g)(ω)∈ MC(mˆ⊗ g). Then
Ad(g) : (mˆ⊗ g)ω→ (mˆ⊗ g)ω′
is an isomorphism of DG Lie algebras.
Proof. (1) This is well known (and very easy to check).
(2) Let γ := log(g) ∈ mˆ⊗ g0. Since ad (γ) is a derivation of the graded Lie
algebra mˆ⊗ g, it follows that Ad (g) = exp(ad(γ)) is an automorphism of mˆ⊗ g.
By Lemma 1.14 this automorphism exchanges d ω and dω′. □
2. T he Reduced Deligne Groupoid
As before, K is a ﬁeld of characteristic 0, (R, m) is a parameter algebra over K,
and g =⨁
i∈Z gi is a DG Lie algebra over K.
Let us write
(2.1) MC (g, R) := MC(Rˆ⊗ g)
and
(2.2) G (g, R) := exp(mˆ⊗ g0).
Given ω, ω′∈ MC(g, R), let
(2.3) G (g, R)(ω, ω′) :={g∈ G(g, R)| Af(g)(ω) = ω′}.
As in [GM] we deﬁne the Deligne groupoid Del(g, R) to be the transformation
groupoid associated to the action of the gauge group G(g, R) on the set MC(g, R).
So the set of objects of Del(g, R) is MC(g, R), and the set of morphisms ω→ ω′
in this groupoid is G (g, R)(ω, ω′). Identity morphisms and composition in the
groupoid are those of the group G (g, R).
Now suppose ω, ω′∈ MC(g, R) and g∈ G(g, R)(ω, ω′). Since
Af(g◦ h◦ g−1) = Af(g)◦ Af(h)◦ Af(g)−1
for any h, and in view of (1.7), there is a group isomorphism
(2.4) Ad (g) : G(g, R)(ω, ω)→ G(g, R)(ω′, ω′).
8 AMNON YEKUTIELI
Given ω∈ MC(g, R) there is the derivation d ω of formula (1.13). Let us deﬁne
(2.5) ar
ω := Im
(
dω : mˆ⊗ g−1→ mˆ⊗ g0)
and
(2.6) (mˆ⊗ g0)(ω) := Ker
(
dω : mˆ⊗ g0→ mˆ⊗ g1)
.
These are R-submodules of mˆ⊗ g0.
Lemma 2.7. Let ω∈ MC(g, R). Consider the bijection of sets
exp : mˆ⊗ g0 ≃− →exp(mˆ⊗ g0) = G(g, R).
(1) The module (mˆ⊗ g0)(ω) is a Lie subalgebra of mˆ⊗ g0, and
exp
(
(mˆ⊗ g0)(ω)
)
= G(g, R)(ω, ω)
as subsets of G(g, R).
(2) The module ar
ω is a Lie ideal of the Lie algebra (mˆ⊗ g0)(ω), and the subset
Nr
ω = Nr(g, R)ω := exp(ar
ω)
is a normal subgroup of G(g, R)(ω, ω).
(3) Let g∈ G(g, R) and ω′ := Af(g)(ω). Then
Ad(g)
(
Nr
ω
)
= Nr
ω′.
Proof. (1) Since d ω is a graded derivation of the graded Lie algebra mˆ⊗ g, its
kernel is a graded Lie subalgebra, and its image is a graded Lie ideal in the
kernel. In degree 0 we get a Lie subalgebra (mˆ⊗ g0)(ω), and a Lie ideal ar
ω in it.
Because dω is a continuous homomorphism between complete R-modules, its
kernel (mˆ⊗ g0)(ω) is closed; so this is a closed Lie subalgebra of mˆ⊗ g0. This im-
plies that the subset exp
(
(mˆ⊗ g0)(ω)
)
is a closed subgroup of G(g, R). Moreover,
let γ∈ mˆ⊗ g0 and g := exp(γ). In the proof of [Ge, Theorem 2.2] it is shown that
dω(γ) = 0 iff Af(g)(ω) = ω. This shows that
exp
(
(mˆ⊗ g0)(ω)
)
= G(g, R)(ω, ω).
(2) We already know that ar
ω is a Lie ideal of (mˆ⊗ g0)(ω); but since this is not a
closed ideal in general, it is not immediate that the subset exp (ar
ω) is a normal
subgroup of exp
(
(mˆ⊗ g0)(ω)
)
.
Consider the CBH series
F(x1, x2) = ∑
j≥1
Fj(x1, x2),
where Fj(x1, x2) are homogeneous elements of degree i in the free Lie algebra in
the variables x1, x2 over Q. It is known (cf. [Bo]) that
(2.8) exp (γ1)· exp(γ2) = exp(F(γ1, γ2))
for γ1, γ2∈ mˆ⊗ g0.
Let us deﬁne a bracket [−,−]ω on mˆ⊗ g−1 as follows:
[α1, α2]ω := [dω(α1), α2].
In general this is not a Lie bracket (the Jacobi identity may fail). However, since
dω is a square zero derivation of the graded Lie algebra mˆ⊗ g, we have
dω([α1, α2]ω) = [ dω(α1), dω(α2)].
For any j≥ 1 and α1, α2∈ mˆ⊗ g−1 consider the element Fj,ω(α1, α2)∈ mˆ⊗ g−1
gotten by evaluating the Lie polynomial Fj(x1, x2) at xi↦→ αi, using the bracket
MC ELEMENTS 9
[−,−]ω. Now take any γ1, γ2∈ ar
ω, and choose α1, α2∈ mˆ⊗ g−1 such that γi =
dω(αi). Then
dω(Fj,ω(α1, α2)) = Fj(γ1, γ2)∈ mˆ⊗ g0.
Let
α := ∑j≥1 Fj,ω(α1, α2)∈ mˆ⊗ g−1
and γ := dω(α)∈ ar
ω. By continuity we get F(γ1, γ2) = γ. From this and formula
(2.8) we see that Nr
ω = exp(ar
ω) is a subgroup of G (g, R) = exp(mˆ⊗ g0).
Similarly, Lemma 1.14(2) implies that the subset exp (ar
ω) is invariant under
the operations Ad (g), g∈ G(g, R)(ω, ω). Therefore Nr
ω is a normal subgroup of
G(g, R)(ω, ω).
(3) According to Lemma 1.14(2) we know that Ad (g)(ar
ω) = ar
ω′. □
Note that the set G (g, R)(ω, ω′) has a left action by the group Nr
ω′, and a right
action by the group Nr
ω. Deﬁne
(2.9) G r(g, R)(ω, ω′) := G(g, R)(ω, ω′)/Nr
ω ,
the quotient set. So there is a surjective function
(2.10) η1 : G(g, R)(ω, ω′)→ Gr(g, R)(ω, ω′).
By Lemma 2.7(3), the multiplication map of G (g, R) induces maps
(2.11) G r(g, R)(ω, ω′)× Gr(g, R)(ω′, ω′′)→ Gr(g, R)(ω, ω′′)
for any ω, ω′, ω′′∈ MC(g, R). If ω′ = ω then Gr(g, R)(ω, ω) is a group.
