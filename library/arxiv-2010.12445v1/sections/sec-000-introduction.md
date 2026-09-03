---
doc_id: arxiv-2010.12445v1
doc_title: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2010.12445v1.pdf
source_sha256: 16e9ca22ecc1f296
doc_brief: "STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — Given a quasi-compact category ﬁbered in groupoids X and a monoidal subcat- egory C of its category of locally free sheaves Vect"
---
Classical (non-neutral) Tannaka’s duality over a ﬁeld k establishes a correspondence between
k-Tannakian categories and aﬃne gerbes over k. More precisely given a k-Tannakian category C
we can deﬁne a ﬁbered category Π C : Aﬀ /k → (groupoids) by
Π C(A) = {k-linear, strong monoidal and exact functors C→ Vect(A)}
where Aﬀ /k is the category of aﬃne schemes over k and Vect(A) = Vect(SpecA) is the category
of ﬁnitely presented locally free sheaves on Spec A. It is then proved that Π C is an aﬃne gerbe
and the functor
C → Vect(Π C), X ↦− →(Γ ∋ Π C(A) ↦→Γ X ∈ Vect(A))
is a k-linear and strong monoidal equivalence. Here and in what fo llows we think sheaves (e.g
locally free, quasi-coherent) on a ﬁbered category as funct ors from the ﬁbered category itself to
the corresponding ﬁbered category of sheaves (see [ Ton20, Section 1] for details).
Conversely if ∆ is an aﬃne gerbe over k then Vect (∆) is a k-Tannakian category and the
functor
∆ → Π Vect(∆) , (s : SpecA → ∆) ↦− →(s∗
| Vect(∆) : Vect(∆) → Vect(A))
is an equivalence. This is called Tannaka’s reconstruction while the previous equivalence is called
Tannaka’s recognition.
In this paper we want to generalize Tannaka’s reconstructio n in two ways: consider more
general ﬁbered categories and proper subcategories of the c ategory of locally free sheaves and
introduce generalized stacks of ﬁber functors.
Fix a base commutative ring R. Consider a category ﬁbered in groupoids X over Aﬀ /R and
a monoidal subcategory C ⊆ Vect(X ) that we assume is closed under taking duals. Let Y be
another category ﬁbered in groupoids over R. Given an R-linear functor Γ : C → Vect(Y) we say
that Γ is right exact if it is exact on right exact sequences (in the a mbient category QCoh (X )),
whose terms are direct sum of sheaves in C (see 3.1 for a precise deﬁnition). We deﬁne Fib X , C(Y)
as the groupoid of R-linear, right exact and strong monoidal functors Γ : C → Vect(Y). We deﬁne
the category ﬁbered in groupoids Fib X , C : Aﬀ /R → (groupoids) by
FibX , C(A) = FibX , C(SpecA) = {R-linear, strong monoidal and right exact functors C→ Vect(A)}
1
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 2
We will show that under mild hypothesis on C the category Fib X , C is automatically ﬁbered in
groupoids even without forcing it (see 5.1). Notice also that Fib X , C is a stack for the fpqc
topology. The analogy with classical Tannaka’s duality is t hat Π Vect(∆) = Fib∆ , Vect(∆) for an
aﬃne gerbe ∆ overR =k (see 3.4).
There are two natural functors. An R-linear, strong monoidal and right exact functor
G : C → Vect(FibX , C), GE (Γ ∋ FibX , C(A)) = Γ E ∈ Vect(A)
and a map of ﬁbered categories
PC : X − → FibX , C, (s : SpecA → X ) ↦− →(s∗
|C : C − →VectA)
which generalize the maps deﬁned in the case of aﬃne gerbes.
We address two problems: when PC is an equivalence and, if this is not the case, what can we
say about the category Fib X , C. Notice that the composition P ∗
C ◦ G : C → Vect(X ) is the natural
inclusion, so that, if PC is an equivalence, then G is fully faithful.
By a quasi-compact ﬁbered category we mean a category ﬁbered in groupoids X admitting a
map U → X from an aﬃne scheme which is representable by fpqc covering o f algebraic spaces.
We say that a full subcategory D ⊆ QCoh(X ) generates QCoh(X ) if any quasi-coherent sheaf on
X is a quotient of a direct sum of sheaves in D. We prove the following generalization of classical
Tannaka’s reconstruction (see 3.4).
Theorem A (3.2, 3.3). Let X be a quasi-compact stack over R for the fpqc topology with quasi-
aﬃne diagonal and C ⊆ VectX be a full, monoidal subcategory with duals generating QCoh X .
Then PC : X → FibX , C is an equivalence and, if Y is a category ﬁbered in groupoids over R, the
functor
Hom(Y, X ) − →FibX , C(Y), (Y
f
− − → X) ↦− →f ∗
|C : C − →Vect(Y)
is an equivalence of categories.
In the case C = VectX , the functor PVect(X ) has already been proved to be an equivalence in
the neutral case, that is X = BRG, where G is a ﬂat and aﬃne group scheme over R (see [Bro13,
Theorem 1.2], where R is a Dedekind domain, and [ Sch13, Theorem 1.3.2] for general rings R),
for particular quotient stacks over a ﬁeld (see [ Sav06] and 2.10) and for quasi-compact and quasi-
separated schemes (see [ BC14, Proposition 1.8]). More generally, although not explicit ly stated
elsewhere, for stacks with the resolution property and with aﬃne diagonal (which is automatic
in the algebraic case, see [ Tot02]) the fact that PVect(X ) is an equivalence is equivalent to the
known analogous results where Vect is replaced by QCoh (−) (for those results and other variants
with Coh(−) or the derived category D(−) see [Lur04, Sch12, BC14, Bra14, Bha16, HR14]): one
can pass from quasi-coherent sheaves to locally free sheave s via dualizable objects and, for the
converse, extend functors from Vect (−) to QCoh (−) following the proof of [ Bha16, Corollary
3.2]. We complete this picture by showing that in general the resolution property implies the
aﬃneness of the diagonal (see 2.9).
The proof we present here does not follow this strategy and on e of the main ingredients is
the classiﬁcation of quasi-compact stacks whose quasi-coh erent sheaves are generated by global
sections, called pseudo-aﬃne. We show that a quasi-compact stack X is pseudo-aﬃne if and only
if it is a sheaf with a ﬂat monomorphism X → SpecB for some B (one can take B = H0(OX ), see
2.2). Moreover we show that a pseudo-aﬃne algebraic stack is qua si-aﬃne (see 2.8), which has
already been observed in [ Gro13, Proposition 3.1], and that a quasi-compact ﬂat monomorphi sm
of algebraic stacks is quasi-aﬃne (see 2.7), which was proved in [ Ray67].
The characterization of pseudo-aﬃne sheaves and Theorem A are a consequence of the theory
developed in [ Ton20], where a correspondence between linear functors C → Mod(A) and quasi-
coherent sheaves on X × A is discussed. We summarize in Section 1 the results used.
STACKS OF FIBER FUNCTORS AND TANNAKA’S RECONSTRUCTION 3
As explained above pseudo-aﬃne sheaves are used in the proof of Theorem A. On the other
hand, another consequence of Theorem A is a diﬀerent characterization of pseudo-aﬃne sheaves:
we show that a sheaf U is pseudo-aﬃne if and only if it is the (sheaf) intersection o f quasi-compact
open subsets of an aﬃne scheme Spec B (one can take B = H0(OU ), see 4.2).
A consequence of this new characterization is a partial answ er to our second initial question,
the nature of Fib X , C, and a partial converse to Theorem A.
Theorem B (5.1). Let X be a quasi-compact ﬁbered category over R and C ⊆ VectX be a full
monoidal subcategory with duals. If R is not a Q-algebra assume moreover that Symn E ∈ C
for all E ∈ C and n ∈ N. Then FibX , C is a quasi-compact fpqc stack with aﬃne diagonal and
the subcategory {GE }E∈C ⊆ Vect(FibX , C) generates QCoh(FibX , C). In particular FibX , C has the
resolution property.
We also consider the substack Fib f
X , C of Fib X , C of functors Γ : C → Vect(A) such that f (E) =
rk Γ E for all E ∈ C , where f is a rank function f : C → N. In Theorem 5.1 we prove that Fib f
X , C is
non empty if and only if there exists a geometric point ξ: Spec Ω → X such that f (E) = rkξ∗E
for all E ∈ C and that, in this case, Fib f
X , C is also a quasi-compact stack with aﬃne diagonal and
the resolution property.
In Theorem 5.1 is also discussed a criterion to deduce that Fib X , C is an algebraic stack, but
we still think this is very unsatisfactory (see 5.2).
We expect that G : C → Vect(FibX , C) is fully faithful in general, which would imply that
X → FibX , Vect(X ) is universal among maps from X to quasi-compact fpqc stacks with quasi-
aﬃne diagonal and the resolution property, but we are unable to prove it (see 5.19).
We conclude the paper by looking at the “baby case” C = {OX }. In this case Fib X , {OX } is
the pseudo-aﬃne sheaf intersection of all quasi-compact op en subsets of Spec H 0(OX ) containing
the image of X → Spec H0(OX ) (see 5.20). In 5.22 we show that Fib X , {OX } is not algebraic in
general, even if X is an integral scheme of ﬁnite type over a ﬁeld.
The outline of the paper is the following. In the ﬁrst section we describe the theory of
sheaﬁﬁcation functors from [ Ton20] and some results about frame bundles. In the second section
we give a ﬁrst description of pseudo-aﬃne stacks and, in the t hird section, prove Theorem A. In
the fourth section we give a diﬀerent description of pseudo- aﬃne stacks, which is then used in
the last section to prove Theorem B.
