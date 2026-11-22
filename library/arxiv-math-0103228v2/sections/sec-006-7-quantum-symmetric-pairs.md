---
doc_id: arxiv-math-0103228v2
doc_title: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002"
section_id: sec-006-7-quantum-symmetric-pairs
section_title: "Quantum symmetric pairs"
section_number: 7
pages: 37-62
source_pdf: 0103228v2.pdf
source_sha256: 7d66dbbd4b87798f
toc_source: inferred
doc_brief: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002 — Coideal subalgebras of the quantized enveloping algebra ar e sur- veyed, with selected proofs included."
---
We turn now to the theory of quantum symmetric pairs. First, w e present
the construction and characterization of the coideal subal gebras used to form
such pairs. The results are drawn from [L2] and [L3], but the m ethods
in this paper are often simpler. The involutions used to cons truct these
algebras are given in a concrete fashion here. The relations for the coideal
subalgebras as algebras are also presented more explicitly . Moreover, using
the results of Section 4, we give a new, less intricate, proof of the uniqueness
characterization for the subalgebras used to form quantum s ymmetric pairs
(see Theorem 7.5 below.) The Harish-Chandra module and symm etric space
37
theory associated to these pairs is also described with the a id of Sections 2
and 3.
A symmetric pair is deﬁned for each Lie algebra involution (e quivalently,
a Lie algebra automorphism of order 2) of g. More precisely, let θ be a
Lie algebra involution of g. Write gθ for the Lie subalgebra of g consisting
of elements ﬁxed by θ. The pair g, gθ is a classical symmetric pair. A
classiﬁcation of involutions and classical symmetric pair s up to isomorphism
can be found in [He1, Chapter 10, Sections 2, 5, and 6] and [OV, Section
4.1.4].
Let p = {v ∈ g|θ(v) = −v}. A commutative Lie subalgebra of g which is
reductive in g and is equal to its centralizer in p is called a Cartan subspace
of p (see [D, 1.13.5].) A Cartan subalgebra h′ of g is called maximally split
([V, Section 0.4.1]) with respect to θ provided that h′∩p is a Cartan subspace
of p. By [D, 1.13.6, 1.13.7], p contains Cartan subspaces and moreover each
Cartan subspace can be extended to a Cartan subalgebra of g.
Recall that we have already speciﬁed a Cartan subalgebra h of g. Let θ
be an involution of g such that h is maximally split with respect to θ. Let
L be the set of Lie algebra automorphisms ψ of g such that ψ(p ∩ h) is a
subset of h. If ψ ∈ L then h is also maximally split with respect to the
involutionψθψ −1. By [D, 1.13.7 and 1.13.8], one can replace θ byψθψ −1 for
some ψ ∈ L so that θ also satisﬁes the following conditions:
(7.1) θ(h) = h;
(7.2) if θ(hi) = hi then θ(ei) = ei and θ(fi) = fi;
(7.3) if θ(hi) ⁄= hi then θ(ei) (resp. θ(fi)) is a nonzero root vector in n−
(resp. n+).
By [D, 1.13.8], θ also induces an automorphism Θ of the root system ∆.
Now consider an arbitrary involution θ′ of g. One can ﬁnd a Lie algebra
automorphism Υ of g so that h is maximally split with respect to the in-
volution Υ θ′Υ −1. In the quantum case, we do not have as much ﬂexibility
in “moving” involutions around using an automorphism of U. In particular,
there is only one choice of quantum Cartan subalgebra, since the only invert-
ible elements of U are the nonzero scalars and the elements of T . Hence any
automorphism ofU restricts to an automorphism of T . Thus the relationship
between an involution of g and the particular Cartan subalgebra h is impor-
tant in lifting the involution to the quantum case. In this se ction, we call
38
an involution θ of g a maximally split involution if h is maximally split with
respect to θ and θ satisﬁes (7.1), (7.2), and (7.3). (Similar terminology was
introduced in [Di, Section 5].) We discuss lifts of maximall y split involutions
and the associated quantum symmetric pairs. There are also a few scattered
results on quantum symmetric pairs when the involution is no t maximally
split. The reader is referred to [G] and [BF] for more informa tion.
For the remainder of this section, let θ be a maximally split involution
with respect to the ﬁxed Cartan subalgebra h. Consider the Cartan subspace
a = p ∩ h of p. Since a is subset of h, the action of ad a on g is semisimple.
Givenλ ∈ a∗, set
gλ = {x ∈ g|(ada)x =λ(a)x for all a ∈ a}.
Let
Σ = {λ ∈ a∗| gλ ⁄= 0}.
We can write g = ⊕λ ∈Σ gλ . Furthermore, by [OV, Theorem 3.4.2], Σ is an
abstract root system called the restricted root system asso ciated to θ (or
more precisely, to g, a.) A classiﬁcation of restricted root systems associated
to involutions can be found in [Kn, Chapter VI, Section 11] (s ee also [He1,
Chapter X, Section F under Exercises and Further Results]). Note that an
abstract root system is slightly more general than an ordina ry root system
(often called a reduced root system) described in [H, Chapte r III]. Good
references for abstract root systems are [Kn, Chapter II, Se ction 5] and [OV,
Chapter 3, Section 1.1]. The abstract root systems have been classiﬁed as the
set of reduced root systems and one additional nonreduced fa mily referred
to as type BC ([Kn, Chapter II, Section 8]).
Before discussing the quantum case, we further describe the action ofθ on
the generators of g. Set ∆ Θ = {α ∈ ∆ |Θ( α) = α} where Θ is the associated
root system automorphism. This is the root system for the sem isimple Lie
subalgebra m of g generated by the ei,f i,h i with θ(hi) = hi. Write m =
m− ⊕ mo ⊕ m+ for the obvious triangular decomposition of m. Set πΘ =
∆ Θ ∩π. Note that πΘ is a set of positive simple roots for the root system ∆ Θ .
WriteQ(πΘ ) for the lattice of integral linear combinations of the simp le roots
in πΘ . Let Q+(πΘ ) be the set of nonnegative integral linear combinations of
the elements in πΘ .
Note that πΘ = Θ( π) ∩π. Also, Θ( −αi) ∈ ∆ + for all αi /∈ πΘ by (7.3).
39
It follows that
(7.4) Θ( −αi) ∈
∑
α j /∈π Θ
Nαj +Q+(πΘ )
for each αi /∈πΘ . Since Θ is a root system automorphism, every element of
∆ can be written as an integral linear combination of roots in {Θ( αi)|αi ∈π}
where either all the coeﬃcients are positive or all the coeﬃc ients are negative.
Hence each αi /∈ πΘ can be written as a linear combination of elements in
{Θ( αi)|αi /∈πΘ } ∪πΘ with just negative integers as coeﬃcients. Observation
(7.4) thus implies that there exists a permutation p on the set {i |αi ∈π−πΘ }
such that for each αi ∈π −πΘ ,
(7.5) Θ( −αi) −αp(i) ∈Q+(πΘ ).
Choose a maximal subset π∗ ofπ −πΘ such that if j =p(j) then αj ∈π∗
and if j ⁄=p(j), then exactly one of the pair αj,α p(j) is in π∗. Consider i such
thatαi ∈π∗. The root vector ep(i) associated to the simple root αp(i) satisﬁes
(adfj)ep(i) = [fj,e p(i)] = 0 for all αj ∈πΘ . Thus ep(i) is a lowest weight vector
for the action of ad m−. Let V be the corresponding simple ad m module
generated by ep(i). By (7.3), θ(fi) is a root vector in n+. Furthermore
(7.5) implies that the weight of this root vector is αp(i) plus some element
in Q+(πΘ ). Thus θ(fi) can be written as a bracket [ a1[a2,..., [as−1,a s]... ]
where exactly one of the aj equals ep(i) and the others are elements of m+.
Using the Jacobi identity, we see that θ(fi) is an element of (ad m+)ep(i).
In particular θ(fi) is an element of V . Furthermore, since elements of m+
commute with fi and thus with θ(fi), we see that θ(fi) must be a highest
weight vector of V . Thus we can ﬁnd a sequence of elements αi1,...,α ir in
πΘ and a sequence of positive integers m1,...,m r such that (up to a slight
adjustment of θ)
(7.6) θ(fi) = (ad e(m1)
i1 · · ·e(mr)
ir )ep(i).
Heree(m)
j =em
j /m!. We may further assume that both the sequence of roots
and the sequence of integers are chosen so that each (ad e(ms)
is · · ·e(mr)
ir )ep(i),
1 ≤ s ≤ r, is an extreme vector of V . (In particular, (ad e(ms)
is · · ·e(mr)
ir )ep(i)
is a highest weight vector for the action of ad eis and (ade(ms−1)
is−1 · · ·e(mr)
ir )ep(i)
is a lowest weight vector for the action of ad fis.) Suppose that the sequence
40
αj1,...,α js of elements in πΘ and the positive integers n1,...,n s also satisfy
this condition on extreme vectors and that ∑
kmkαik = ∑
knkαjk. By [Ve],
(ade(m1)
i1 · · ·e(mr )
ir )ep(i) = (ad e(n1)
j1 · · ·e(ns)
js )ep(i). Thus (7.6) is independent of
the choice of such sequences.
Using lowest weight vectors instead of highest weight vecto rs, we obtain
(7.7) θ(ep(i)) = (ad f (mr)
ir · · ·f (m1)
i1 )fi
up to a nonzero scalar. A straightforward sl 2 computation shows that
(ade(m1)
i1 · · ·e(mr )
ir )[(adf (mr)
ir · · ·f (m1)
i1 )fi] = fi
and
(7.8) (ad f (mr )
ir · · ·f (m1)
i1 )[(ade(m1)
i1 · · ·e(mr)
ir )ep(i)] = ep(i).
Since θ2 is the identity, the scalar in (7.7) must be 1.
Set m(i) = m1 +... +mr. Now [ θ(ei),θ (fi)] = θ(hi) is an element of h
by (7.1). Furthermore, by (7.2) and (7.3), θ(hi) must be the coroot hΘ( α i)
associated to the root Θ( αi). The description of the Chevalley basis for
g given in [H, Proposition 25.2 and Theorem 25.2] ensures that both θ(ei)
and θ(fi) are Chevalley basis vectors up to a sign. Furthermore, by [H ,
Proposition 25.2(b)] and (7.6),we must have
θ(ei) = ( −1)m(i)(adf (m1)
i1 · · ·f (mr)
ir )fp(i).
Similarly, by [H, Proposition 25.2(b)] and (7.7)
θ(fp(i)) = ( −1)m(i)(ade(mr )
ir · · ·e(m1)
i1 )ei.
Note that when p(i) = i, we have
(ade(mr )
ir · · ·e(m1)
i1 )ei = (ade(m1)
i1 · · ·e(mr )
ir )ei.
Hence m(i) is even in this case.
The above analysis allows us to better describe the root spac e automor-
phism Θ. Let W ′ denote the Weyl group associated to the root system ∆ Θ
of m considered as a subgroup of the Weyl group of ∆. Let wo denote the
longest element of W ′. Note that wo is a product of reﬂections in W ′ but can
41
also be considered as an element of W . Let d be the diagram automorphism
on πΘ such that d = −wo when restricted to πΘ . Note that d induces a
permutation on the set {i|αi ∈πΘ } which we also denote by d. In particular,
givenαi ∈πΘ ,d (αi) = αd(i). Extend d to a function on π, and thus to ∆, by
setting d(αi) = αp(i) for αi /∈πΘ . It follows that Θ = −wod. Note that this
forces d to be a diagram automorphism of the larger root system ∆.
Before lifting θ to the quantum case, we recall and introduce more no-
tation. The right adjoint action is deﬁned by (6.4). This act ion on the
generators of U is given by:
(adryi)b =byi −yitibt−1
i (adrxi)b =t−1
i bxi −t−1
i xib (adrti)b =t−1
i bti
for 1 ≤ i ≤ n. Recall the deﬁnitions of [ m]q and qi used to deﬁne the
quantized enveloping algebra ((1.4)-(1.7)). The divided p owers of xi and yi
are deﬁned by x(m)
i =xm
i /[m]qi! and y(m)
i =ym
i /[m]qi!. (Note that these are
quantum analogs of the divided power e(m)
i .) Let M denote the subalgebra
of U generated by the corresponding elements xi,y i,t i,t −1
i where θ(hi) = hi.
Note that M is just a copy of the quantized enveloping algebra Uq(m) so
this notation is consistent with that of Section 6. Let ι be the C algebra
automorphism of U ﬁxing xit−1
i and tiyi for 1 ≤ i ≤ n, sending t to t−1 for
allt ∈T andq toq−1. Recall the sequences αi1,...,α ir andm1,...,m r used
in (7.6) and (7.7). (As in the classical case, using [Lu, Prop osition 39.3.7],
the description of ˜θ(yi) in (7.12) below is independent of the choice of such
sequences.)
In the next theorem, we lift θ to a C algebra automorphism of U. This
is in the spirit of [L2, Theorem 3.1]. The main diﬀerence here is that we do
not insist that ˜θ is a C algebra involution on all of U.
Theorem 7.1 There exists a C algebra automorphism ˜θ on U such that:
(7.9) ˜θ(xi) = xi and ˜θ(yi) = yi for all αi ∈πΘ .
(7.10) ˜θ(τ (λ)) = τ (Θ( −λ)) for all τ (λ) ∈T.
(7.11) ˜θ(q) = q−1.
(7.12) ˜θ(yi) = [(ad rx(m1)
i1 · · ·x(mr )
ir )t−1
p(i)xp(i)]
and ˜θ(yp(i)) = ( −1)m(i)[(adrx(mr )
ir · · ·x(m1)
i1 )t−1
i xi] for αi ∈π∗.
42
Furthermore, ˜θ2 is the identity when restricted to M and to T . Finally, ˜θ
specializes to θ as q goes to 1.
Proof: To show that ˜θ extends to a C algebra automorphism of U, we relate
it to Lusztig’s automorphisms. Let Two be Lusztig’s automorphism associated
to wo, the longest element of W ′. We follow the notation of [DK, Section
1.6]. Fix αi ∈ πΘ . Recall that −wo(αi) = αd(i). By [DK, Section 1.6 and
Proposition 1.6], Two sends yi to a nonzero scalar multiple of xd(i)t−1
d(i), sends
xi to a nonzero scalar multiple of yd(i)td(i), and sends ti tot−1
d(i). Furthermore,
one checks using [DK, Remark 1.6] that for each αi /∈πΘ the composition
(ι ◦Two)(t−1
p(i)xp(i)) = ui[(adrx(m1)
i1 · · ·x(mr )
ir )t−1
p(i)xp(i)]
for some nonzero scalar ui.
Deﬁne a function ˜θ on the generators of U using (7.9), (7.10), (7.11),
(7.12), and setting
˜θ(xi) = u−1
i (ι ◦Two)(yp(i)tp(i)) and ˜θ(xp(i)) = ( −1)m(i)u−1
p(i)(ι ◦Two)(yiti)
for each αi ∈ π∗. It is clear from (7.9) and (7.10) that ˜θ extends to a C
algebra automorphism on both M and T . Now ˜θ2 is clearly the identity on
M. Since Θ is an involution on the root system of g, condition (7.10) ensures
that ˜θ also restricts to an involution on the group T .
We check that ˜θ extends to a C algebra automorphism ofU. In particular,
˜θ(yi)˜θ(xi) − ˜θ(xi)˜θ(yi) = ( ι ◦Two)(yp(i)xp(i) −xp(i)yp(i)) = ˜θ(yixi −xiyi) for
αi /∈πΘ . Furthermore, for αi ∈πΘ , (ι◦Two)(td(i)xd(i)) = yi = ˜θ(yi) up to some
nonzero scalar. Hence the ˜θ(yi), 1 ≤i ≤n satisfy the quantum Serre relations
(1.7). Similarly, (ι ◦Two)(yiti) = xd(i) = ˜θ(xd(i)) up to a nonzero scalar when
αi ∈ πΘ . It follows that the ˜θ(xi) for 1 ≤ i ≤ n satisfy the quantum Serre
relations (1.7). Moreover, ˜θ preserves the relations between the xi and the
yj for 1 ≤i,j ≤n. Thus ˜θ extends to a C algebra automorphism ˜θ of U.
Now consider an element b in M ∪T ∪ {yi|1 ≤i ≤n} and write ¯b for its
specialization as q goes to 1. Note that the specialization of ˜θ(b) is just θ(¯b).
This is enough to force ˜θ to specialize to θ. ✷
We are now ready to introduce the quantum analog of U(gθ ). Set
TΘ = {τ (λ)|Θ( λ) = λ},
43
a subgroup of T . Let B =B˜θ be the subalgebra of U generated by M, TΘ ,
and the elements
Bi =yiti + ˜θ(yi)ti
forαi /∈πΘ . The next result shows that B is a coideal subalgebra of U. This
fact combined with the results of Sections 1 and 4 is used belo w to describe
the relations satisﬁed by these generators. As a consequenc e, we show below
that B specializes to U(gθ ) as q goes to 1.
Theorem 7.2 B is a left coideal subalgebra of U.
Proof: We need to check that
(7.13) ∆ (b) ∈U ⊗B
for all b ∈B. Since ∆ is an algebra homomorphism from U to U ⊗U, it is
suﬃcient to check (7.13) for a set of generators of B. Now B is generated
by the elements Bi, for αi /∈ πΘ , and two Hopf algebras: M and the group
algebra generated by TΘ . In particular, each b ∈ M and each b ∈ TΘ
satisﬁes (7.13). Hence it is suﬃcient to check (7.13) holds f or the remaining
generators, namely when b =Bi for αi /∈πΘ .
Set M+ =U + ∩ M. Note that tit−1
p(i) is in TΘ for all i withαi /∈πΘ . Thus
by (6.5) and the deﬁnition of ˜θ, the element ˜θ(yi)ti satisﬁes the following nice
property with respect to the comultiplication of U:
(7.14)
∆ (˜θ(yi)ti) ∈ti ⊗ ˜θ(yi)ti +U ⊗ (M ∩G+U o)t−1
p(i)ti
⊂ti ⊗ ˜θ(yi)ti +U ⊗ M+TΘ .
This combined with the formula for ∆ (yiti) (see (1.8) and (1.10) ) yields
(7.15) ∆ (Bi) ∈ti ⊗Bi +U ⊗ M+TΘ ⊂U ⊗B
and the theorem follows. ✷
We turn now to understanding the relations satisﬁed by the ge nerators of
B. The elements Bi have already been deﬁned when αi /∈πΘ . Set Bi =yiti
forαi ∈πΘ . Given a tuple I = (i1,...,i r), set |I| =r, wt(I) = αi1 +... +αir ,
BI =Bi1 · · ·Bir, and YI =yi1ti1 · · ·yirtir .
44
Recall ((1.4) and (1.11)) that xiyjtj =q(−α i,α j )yjtjxi wheneverj ⁄=i. By
Theorem 7.1, ˜θ(xi) = xi wheneverαi ∈πΘ . Furthermore, ˜θ(yj) and yj have
the same weight with respect to the adjoint action of TΘ . Hence
(7.16) xiBj =q(−α i,α j )Bjxi and τ (λ)Bj =q(λ, −α j)Bjτ (λ)
for all αi ∈πΘ with αj /∈πΘ , and τ (λ) ∈TΘ . It follows that
(7.17) B =
∑
I
BIM+TΘ .
Let J be a set such that {YJ|J ∈ J } is a basis for G−. Note that BJ =YJ +
(terms of higher weight) for each tuple J. The triangular decomposition (4.1)
ofU implies that the subspaces {YJM+TΘ |J ∈ J }, and hence the subspaces
{BJ M+TΘ |J ∈ J }, are linearly independent.
Let Fij be the function in two variables X1 and X2 deﬁned by
Fij(X1,X 2) =
1−aij∑
m=0
(−1)m
[
1 −aij
m
]
qi
X
1−aij −m
1 X2X m
1 .
The quantum Serre relations (1.7) are the set of equations Fij(yi,y j) = 0 for
i ⁄= j. A straightforward computation shows that if ( λi,α j) = (λj,α i) then
Fij(yiτ (λi),y jτ (λj)) = 0. Hence
(7.18) Fij(yiti,y jtj) = 0.
It follows that the generators yiti of G− satisfy the same relations as the
generators of U −. Furthermore, since (Θ( −αi),α j) = (Θ( −αj),α i), we have
(7.19) Fij(˜θ(yi)ti, ˜θ(yj)tj) = 0.
We show below that the Bi for 1 ≤ i ≤ n satisfy relations which come
from the quantum Serre relations on G−. First, we consider the evaluation
of the function Fij at Bi, Bj in a few special cases.
If both αi andαj are in πΘ , then Fij(Bi,B j) = Fij(yiti,y jtj). Similarly, if
αi ∈πΘ and αj /∈πΘ , then Fij(Bi,B j) = Fij(yiti,y jtj) +Fij(˜θ(yi)ti, ˜θ(yj)tj).
Hence (7.18) and (7.19) imply that
(7.20) if αi ∈πΘ then Fij(Bi,B j) = 0.
45
Now suppose that i and j are chosen such that π0, 0(Yij) is nonzero. It
follows thatYij must have a zero weight summand. Checking the possibilities
for the quantum Serre relations, we must have aij = 0 and Θ( αi) = −αj. In
particular, Bi =yiti +q−2
i xjt−1
j ti and Bj =yjtj +q−2
i xit−1
i tj. A straightfor-
ward computation shows that
(7.21) if aij = 0 and Θ( αi) = −αj then
Fij(Bi,B j) = BiBj −BjBi = (t−1
i tj −t−1
j ti)/(qi −q−1
i ).
Given λ ∈ Q(π), let Pλ be the projection of B onto U −G+τ (λ) with
respect to the direct sum decomposition of Lemma 1.3 applied to the coideal
B. The next lemma provides more detailed information about Fij(Bi,B j).
Lemma 7.3 Let Yij = Fij(Bi,B j) for i ⁄= j and λij = (1 −aij)αi +αj. If
(πβ,γ ◦Pλ ij )(Yij) ⁄= 0 then [β,γ ] ⁄= 0, τ (λij −β) /∈TΘ , and τ (λij −γ) /∈TΘ .
Proof: Set Pij = Pλ ij . Suppose that ( π0, 0 ◦Pij)(Yij) ⁄= 0. It follows that
π0, 0(Yij) ⁄= 0. Hence aij = 0 and Θ( αi) = −αj. Now λij = αi +αj in this
case. By (7.21) Pij(Yij) = Pij(t−1
i tj −t−1
j ti) = 0. Therefore, π0, 0(Yij) = 0 for
all choices of i and j.
By (7.20), we may assume that αi is not in πΘ . Assume that β and γ
are chosen so that πβ,γ (Yij) ⁄= 0. Note that Yij can be written as a sum of
monomials in 2 −aij terms where 1 −aij of those terms are from the set
{yiti, ˜θ(yi)ti} and the other term is from the set {yjtj, ˜θ(yj)tj}. It follows
that γ =s1αp(i) +s2αp(j) +η for some η ∈Q+(πΘ ) and nonnegative integers
s1 and s2 such that s1 ≤ 1 −aij and s2 ≤ 1. Set γ′ =s1αi +s2αj and note
that τ (γ −γ′) is in TΘ . The above description of the monomials which add
to Yij further implies that γ′ +β ≤ λij. Moreover, by (7.18), 0 ≤ β < λij
and by (7.19), 0 ≤γ′ <λ ij. Now β andγ′ are both linear combinations of αi
andαj. Thus the lemma follows if neither αi norαj are elements of Q+(πΘ ).
In the case when αj ∈πΘ , (7.19) further implies that that 0 ≤γ′ <λ ij −αj
and 0 ≤β <λij −αi. The lemma thus follows in this case as well. ✷
The next result gives a description of the generators and rel ations of B.
Theorem 7.4 Let ˜B be the algebra freely generated over M+TΘ by the el-
ements ˜Bi, 1 ≤ i ≤ n. Then there exist elements cij
J ∈ M +TΘ such that
B ∼= ˜B/L whereL is the ideal generated by the following elements:
46
(i) τ (λ) ˜Biτ (−λ) −q−(λ,α i) ˜Bi for all τ (λ) ∈TΘ and αi /∈πΘ .
(ii) t−1
j xj ˜Bi− ˜Bit−1
j xj −δij(tj −t−1
j )/(qj −q−1
j ) for all αj ∈πΘ and 1 ≤i ≤n.
(iii)
1−aij∑
m=0
(−1)m
[
1 −aij
m
]
qi
˜B
1−aij −m
i ˜Bj ˜Bm
i −
∑
{J∈J |wt(J)<(1−aij )α i+α j }
˜BJcij
J
for each i ⁄=j, 1 ≤i,j ≤n.
Proof: Relations (i) and (ii) follow from (7.16) and (1.4). We now sh ow that
theBi, 1 ≤i ≤n, satisfy the relations described in (iii). Fix a quantum Ser re
relationY =Fij(Bi,B j) for given αi,α j with i ⁄=j. Set λ = (1 −aij)αi +αj
andZ =Pλ (Y ). By (4.7), ((Pλ ◦π0, 0)⊗Id)∆ (Y ) = (π0, 0⊗Id)∆ (Z). Moreover,
(4.7) ensures that
(π0, 0 ⊗Id)∆ (Z) = τ (λ) ⊗Z.
By (7.15) and (7.17), we have
(7.22) ∆ (Y ) ∈τ (λ) ⊗Y +
∑
{J| wt(J)<λ }
U ⊗BJ M+TΘ .
Now if J has weight less than λ, one checks from (1.7) that there is no
quantum Serre relation of weight greater than or equal to −λ. Hence if
wt(J)<λ then J is an element of the set J . Now, (7.22) implies that
((Pλ ◦π0, 0) ⊗Id)∆ (Y ) ∈τ (λ) ⊗ (Y +
∑
{J∈J | wt(J)<λ }
BJ M+TΘ )
Thus we can ﬁnd X ∈
∑
{J∈J |wt(J)<λ }BJ M+TΘ such that Y +X = Z. We
obtain a relation of the form described in (iii) by proving Z = 0.
Recall the notation of Section 4, Filtration II. Assume that Z is nonzero
and hence max( Z) is nonempty. Choose [ β,γ ] ∈ max(Z). It follows that
πβ,γ (Z) ⁄= 0. By Lemma 7.3, [ β,γ ] ⁄= [0, 0], and neither τ (λ −β) nor τ (λ −
γ) is an element of TΘ . Write ( πβ, 0 ⊗Id)(∆ (Z)) =
∑
vi ⊗ui where the
vi ∈ U −
β τ (λ) and the ui ∈ G+T . We may assume that the vi are linearly
independent elements of U −
−βτ (λ). Note that at least one of the ui has a
(nonzero) summand of weight γ inG+
γ τ (λ −β). By (7.19), the maximality of
47
[β,γ ], and the fact that β ⁄= 0, each ui is in G+T ∩ ∑
{J∈J |wt(J)<λ }BJ M+TΘ .
This intersection is just M+TΘ . Hence τ (λ −β) ∈TΘ , a contradiction. This
forcesβ = 0. It follows that ( π0,γ ⊗Id)(∆ (Z)) ∈U ⊗τ (λ−γ). Again τ (λ−γ)
must be in TΘ . This contradiction forces max( Z) to be empty. In particular,
Z = 0.
We have shown that B is isomorphic to a homomorphic image of ˜B/L. A
consequence of relations (i), (ii), and (iii) is that M+TΘ ˜BI ⊂ ∑
J∈J ˜BJ M+TΘ +
L for each tuple I. Thus
˜B/L =
⨁
J∈J
( ˜BJ M+TΘ +L).
Since the elements Bi in B satisfy the relations (i), (ii), (iii), we also have
the following direct sum decomposition:
B =
⨁
J∈J
(BJ M+TΘ ).
Therefore B ∼= ˜B/L. ✷
Note that (7.20) and (7.21) both provide examples of the rela tions de-
scribed in Theorem 7.4 (iii). We illustrate how to compute th ecij
J in a more
complicated example. Consider the case where Θ( αi) = −αi, Θ( αj) = −αj
and aij = −1. So Bi = yiti + q−2
i xi and Bj = yjtj + q−2
j xj and Y =
B2
iBj − (qi +q−1
i )BiBjBi +BjB2
i. Thus by (1.9) and (1.10),
∆ (Br) = Br ⊗ 1 +tr ⊗Br
for r =i,j . It follows that
∆ (Y ) = t2
itj ⊗Y + (B2
itj − (qi +q−1
i )BitjBi +tjB2
i ) ⊗Bj +W ⊗B
for some W which satisﬁes π0, 0(W ) = 0. A straightforward computation
using the relations of U shows thatPλ ◦π0, 0((B2
itj −(qi +q−1
i )BitjBi +tjB2
i ) =
−q−1
i t2
itj. Thus
0 = (Pλ ◦π0, 0) ⊗Id(∆ (Y ) = t2
itj ⊗Y −q−1
i t2
itj ⊗Bj.
It follows that
B2
iBj − (qi +q−1
i )BiBjBi +BjB2
i =q−1
i Bj.
48
(This relation is also computed in [L1, Lemma 2.2 (2.2)]. The generators for
U and B are somewhat diﬀerent in [L1]. In particular, when αi = −Θ( αi),
Bi in [L1] is equal to yiti +xi in the notation of this paper. Thus using a
Hopf algebra automorphism of U, the Bi in [L1] corresponds to q−1
i times
theBi deﬁned in this paper. This explains the diﬀerence in coeﬃcie nt of Bj
found in the two papers.) Note that a similar argument shows t hat cij
J = 0
whenever −αi ⁄=αp(i) and −αi ⁄=αp(j). The cij
J are computed in [L1, Lemma
2.2] for the cases when aij ≥ −2 and Θ( −αi) = αp(i).
Note that the generators of B specialize to the generators of U(gθ ) as
q goes to 1. Thus the specialization of BJ M+TΘ is contained in U(gθ ).
Moreover the set of spaces {BJ M+TΘ , J ∈ J } remain linearly independent
after specialization. As q goes to 1, since these spaces span B, we conclude
that B specializes to U(gθ ).
The algebraB also satisﬁes a maximality condition. Indeed, suppose that
C is a subalgebra of U containing B and that C also specializes to U(gθ ).
Then by [L2, Theorem 4.9], C =B. The proof in [L2] uses a quantum version
of the Iwasawa decomposition. The result also follows direc tly from Theorem
7.4. The idea is as follows. Recall the notation of Section 6. SetN +
Θ =N +
π Θ .
By (6.6) (interchanging the roles of N +
π ′ with N −
π ′), we have
U =
∑
J∈J
YJ M+TN +
Θ .
By induction on |J| (as in [L2, Lemma 4.3]), one can show that U is spanned
by the spacesB;Bt,t /∈TΘ ; andBT (N +
Θ )+ where (N +
Θ )+ is the augmentation
ideal of N +
Θ . Let X be in C. Subtracting an element of B if necessary, we
may assume that X is a linear combination of elements in B(t − 1)/(q − 1)
fort /∈TΘ , and BT (N +
Θ )+. Assume that X is nonzero. Rescale X by a power
of (q − 1) so that it is an element of ˆC − (q − 1) ˆC. It follows that X does
not specialize to an element of U(gθ ). This contradiction forces X = 0 and
thusB =C.
We have shown that the algebra B satisﬁes the following properties.
(7.23) B is a left coideal in U.
(7.24) B specializes to U(gθ ).
(7.25) If B ⊂ C and C is a subalgebra of U which specializes to U(gθ ) then
B =C.
49
We now turn to characterizing all subalgebras of U which satisfy (7.23),
(7.24), and (7.25). First, we present two variations which s atisfy these con-
ditions as well.
Variation 1: For sake of simplicity, we assume ﬁrst that g is simple. Recall
the permutationp used in (7.5). Suppose that there exists an r ∈ {1, 2,...,n }
such thatαr /∈πΘ andp(r) ⁄=r. Assume further that ( αr, Θ( αr)) ⁄= 0. Recall
the Cartan subspace a = {x ∈ h|θ(x) = −x} and the restricted root system
Σ associated to θ introduced at the beginning of this section. Let β be the
restricted root corresponding to er. Note that β is just the restriction of
αr ∈ h∗ to a∗. Furthermore, (ad a)[er, Θ( fr)] = 2β(a)[er, Θ( fr)] for all a ∈ a.
In particular, the restricted root system Σ contains both β and 2β. Thus Σ
is nonreduced and hence must be of type BC . One can choose the positive
roots of Σ so that each αj restricted to a∗ is either zero or a simple positive
root in Σ. Furthermore, αr and αj restrict to the same root if and only if
j = r or j = p(r). It follows from [Kn, Chapter II, Section 8] that there is
exactly one positive simple root in Σ such that twice this roo t is also in Σ.
Hence r and p(r) are the only values of j such that (αj, Θ( αj)) ⁄= 0.
Let c be an element in A = C[q,q −1](q−1) which specializes to 1 as q goes
to 1. Deﬁne the C algebra automorphism ˜θc of U by
˜θc(yr) = c−1 ˜θ(yr)
˜θc(xr) = c˜θ(xr)
and ˜θc agrees with ˜θ on all other generators of U. Note that ˜θc is also a
C algebra automorphism of U which specializes to θ and restricts to ˜θ on
MTΘ . Deﬁne B˜θ c in the same way as B˜θ using ˜θc instead of ˜θ. Thus B˜θ c
is generated by M, TΘ , and elements Bc
i = yiti + ˜θc(yi)ti for αi /∈ πΘ .
Moreover,Bc
i =Bi for i ⁄=r. Since ˜θc(yi) is a scalar multiple of ˜θ(yi) for all
i, the proof of Theorem 7.2 also works for B˜θ c. Hence B˜θ c is a left coideal
subalgebra of U. Consider a quantum Serre relation Fij(yi,y j) where either
i or j equals r. Note that if Θ( αi) = −αj then, by the assumptions on
r, {i,j } = {r,p (r)} and (αi,α j) ⁄= 0. Thus as in the proof of Lemma 7.3,
(π0, 0◦Pij)(Fij(Bc
i,B c
j )) ⁄= 0 whenever i ⁄=j. Hence the arguments for B˜θ used
to prove Lemma 7.3 and Theorem 7.4 work for B˜θ c as well. In particular,
B˜θ c satisﬁes conditions (7.23), (7.24), and (7.25).
Note that B˜θ c is not isomorphic to B˜θ via a Hopf algebra automorphism
of U for c ⁄= 1. It appears unlikely in general that two such algebras are
50
isomorphic using just an algebra isomorphism. It should be n oted that the
existence of this one parameter family of analogs is implici t in the proof of
[L2, Theorem 5.8]. However, it was mistakenly concluded in t he paragraph
directly preceding [L2, Theorem 5.8] that all the analogs of Variation 1 were
isomorphic to B˜θ via a Hopf algebra automorphism.
In the general semisimple case, the one parameter c is replaced by a
multiparameter c. In particular, each parameter corresponds to a pair of
roots αij,α p(ij) such that (αij, Θ( αij )) ⁄= 0. The automorphism ˜θc is deﬁned
in a similar fashion to ˜θc. Let [Θ] be the set of automorphisms of the form
˜θc. Following the convention in [L3], we refer to B˜θ ′, ˜θ′ ∈ [Θ] as a standard
analog of U(gθ ).
Variation 2: Let S1 be the subset of π −πΘ consisting of those roots αi such
that Θ( αi) = −αi. Let S be the subset of S1 such that if αi ∈ S andαj ∈ S 1
then 2(αi,α j)/(αj,α j) is even. Let S be the set of n tuples s = (s1,...,s n)
such that each si is in A = C[q,q −1](q−1) and si ⁄= 0 implies αi ∈ S . Given
ˆθ ∈ [Θ], let Bˆθ, s be the subalgebra of U generated by TΘ , M, the Bi for
αi ∈π − S, and the Bi, s deﬁned by
Bi, s =yiti +q−(α i,α i)xi +siti
forαi ∈ S . In particular, when the entries of s are all zero, Bi, s is just equal
to Bi.
Note that
∆ (Bi, s) = ti ⊗Bi + (yiti +q−(α i,α i)xi) ⊗ 1.
Thus by the same arguments as in Theorem 7.2 , Bˆθ, s is a left coideal subalge-
bra of U. Note that if τ (λ) ∈TΘ andαi ∈ S then (λ,α i) = 0. It follows that
aBi, s = Bi, sa for all αi ∈ S and a ∈ MTΘ . Recall the notation of Lemma
7.3. To show that Bˆθ, s satisﬁes the conditions (7.23), (7.24), and (7.25), it
suﬃces to check for all i,j , i ⁄= j, that ( π0, 0 ◦Pij)(Fij(Bi, s,B j, s)) = 0. A
lengthy but routine computation shows that this holds exact ly when the n
tuple s is in S.
Following the convention in [L3], the Bˆθ, s, ˆθ ∈ [Θ] are called nonstandard
analogs of U(gθ ). A nonstandard analog Bˆθ, s is not isomorphic to a standard
analog using a Hopf algebra automorphism of U. However, ([L2, Lemma
5.7]) Bˆθ, s is isomorphic as an algebra to Bˆθ .
51
Nonstandard analogs were ﬁrst observed (to the suprise of th e author) in
[L2, Section 5]. In [L3, Section 2], nonstandard analogs wer e claimed to exist
when S is deﬁned using the larger set S1 instead of S. (See in particular the
deﬁnition of S given following [L3, (2.11)] and Theorem 2.1].) Our analysi s
in Variation 2 corrects this point.
We are now ready to show that the only possible subalgebras of U which
satisfy (7.23), (7.24), and (7.25) are our standard and nons tandard analogs
associated to an automorphism in [Θ]. In particular, we give a new proof
of [L2, Theorem 5.8] using the approach and results of Sectio n 4. Note that
when the restricted roots Σ associated to the involution θ do not contain a
component of type BC , then all the analogs described below are isomorphic
to each other as algebras. This is precisely what Theorem 5.8 in [L2] states.
On the other hand, by the discussion of Variation 1, if Σ conta ins m com-
ponents of type BC , then there is an m parameter family of analogs up to
algebra isomorphism.
Theorem 7.5 A subalgebraB ofU satisﬁes (7.23), (7.24), and (7.25) if and
only if B is isomorphic as an algebra to Bˆθ for some ˆθ ∈ [Θ] . In particular, B
is isomorphic to a standard or nonstandard analog of U(gθ ) corresponding to
an element ˆθ in [Θ] and an element s in S via a Hopf algebra automorphism
of U.
Proof: We use the notation of the second ﬁltration introduced in Sec tion 4.
Let B be a subalgebra of U which satisﬁes (7.23), (7.24), and (7.25). The
proof of this theorem has three steps:
(i) B ∩T =TΘ
(ii) B ∩U + = M+
(iii) gr GB ∩G− =G−.
More precisely, we ﬁrst prove that B ∩T is a subgroup of TΘ andB ∩U oU + is
a coideal subalgebra of M+TΘ . We then use the second ﬁltration introduced
in Section 4 to analyze gr GB ∩G− and thus prove (iii). This information is
then used to show that B ∩U +U o specializes to U(gθ ) ∩U(n+ + h). Next
we obtain (i) and (ii). The last part of the proof takes a close r look at the
52
generators of B whose tip is in G− and show they are of the desired form.
The details follow.
Consider the set B ∩T . By (7.24), B ∩T is a subset of TΘ . Hence
B ∩T =B ∩TΘ . Note that any element of B can be written as a direct sum
of weight vectors with respect to B ∩T . Hence by (7.25), we may assume
thatB ∩TΘ is a group. Condition (7.23) and Lemma 4.2 ensure that B ∩U o
is the group algebra generated by B ∩TΘ . Since TΘ is free abelian of ﬁnite
rank, B ∩TΘ is free abelian of rank at most the rank of TΘ .
Consider the coideal subalgebra B ∩U +U o ofB. We show that B ∩U +U o
is a subalgebra of M+TΘ . By Lemma 1.3, B ∩U oU + is a direct sum of the
vector spaces B ∩G+τ (µ), where τ (µ) ∈T . Suppose that c ∈B ∩G+τ (µ).
Choose γ maximal with respect to the standard partial ordering on Q+(π)
so that π0,γ (c) ⁄= 0 and γ ∈Q+(πΘ ). Then by (4.7),
π0,γ (c) ∈G+
γ τ (µ) ⊗Y
where Y ∈ τ (µ −γ) +
∑
γ ′>γ G+
γ ′−γτ (µ −γ). Since B is a coideal, Y is an
element ofB. Rescaling if necessary, we may assume that Y is in ˆB−(q−1) ˆB.
Hence Y specializes to a nonzero element in U(gθ ). The choice of γ implies
that γ′ −γ /∈Q+(πΘ ) for all γ′ which appear in the deﬁnition of Y . Hence,
Y ∈ τ (µ −γ) + (q − 1)
∑
γ ′>γ ˆG+
γ ′−γτ (µ −γ). But then ( q − 1)−1(Y − 1) is
also in ˆB and thus specializes to an element of U(gθ ). This forces τ (µ −γ),
and thus τ (µ), to be in TΘ . Now consider λ maximal such that π0,λ (c) ⁄= 0.
Then by (4.7), τ (µ −λ) ∈TΘ . Hence λ ∈Q+(πΘ ). Note that if λ′ ∈Q+(π)
and λ′ < λ then λ′ is also in Q+(πΘ ). It follows that c is a sum of weight
vectors with weights in Q+(πΘ ). In particular, c ∈ M +TΘ and B ∩U oU + is
a subalgebra of M+TΘ .
We next analyze the part of B whose top degree terms are in G−. To
do this, we introduce the left B module B/N where N is the left ideal
B(B ∩ (U +U o)+) of B. (Here ( U +U o)+ is equal to the augmentation ideal of
U +U o.) The ﬁltration G on B induces a ﬁltration which we also denote by
G on B/N which makes gr GB/N into a gr GB module. By Theorem 4.9, the
only important contributions to this graded module occur in bidegree (m, 0)
form ≥ 0. In particular, gr GB/N is spanned by elements b +N whereb ∈B
and tip(b) ∈G−. Note that the subspace of G− of elements of bidegree less
than or equal to ( m, 0) is ﬁnite dimensional. Thus the ﬁltration on B/N is
a ﬁnite discrete ﬁltration. Moreover, gr GB is ﬁnitely generated by the image
53
of the generators of B described in Corollary 4.10. Hence we have equality of
Gelfand Kirillov dimension: GKdim gr G(B/N) = GKdim B/N ([KL, Prop.
6.6]). Now gr GB/N identiﬁes with gr G(B)∩G− as a left gr G(B)∩G− module.
It is straightforward to check that the GK dimension of gr GB/N as a gr GB
module is equal to the GK dimension of gr GB/N as a gr G(B) ∩G− module.
Hence, the form of the generators of B given in Corollary 4.10 implies that
GKdim gr GB/N ≤ dim n−.
Let r be a Lie subalgebra of gθ . A standard argument similar to the argu-
ment in the previous paragraph yields that the U(gθ ) moduleU(gθ )/(U(gθ )r)
has GK dimension equal to dim gθ − dim r. (This follows for example from
[D, Proposition 2.2.7].) Consider the ˆB module ˆB/ ˆN. Write ¯N for the spe-
cialization of N at q = 1. By Theorem 4.1, B ∩ (U +U o) specializes to the
enveloping algebra of a Lie subalgebra, say s, of gθ . Note that ¯N =U(gθ )s.
NowB ∩U +U o ⊂ M +TΘ . Hence s is a Lie subalgebra of m+ + (gθ ∩ h). The
map which sends each b+ ˆN in ˆB/ ˆN to ¯b+ ¯N inU(gθ )/ ¯N allows us to special-
ize the left ˆB module ˆB/ ˆN to the U(gθ ) module U(gθ )/ ¯N atq = 1. We can
choose generating sets for B and B/N which specialize to generating sets of
U(gθ ) and U(gθ )/ ¯N respectively. Hence GKdim B/N ≥ GKdim U(gθ )/ ¯N .
Note that
GKdim U(gθ )/ ¯N = dim gθ − dim s
≥ dim gθ − dim(m+ + (gθ ∩ h))
= dim n−.
By the previous paragraph, this inequality is an equality. H ence
GKdim U(gθ )/ ¯N = GKdim n− = GKdim G−.
Moreover dim s = dim( m+ + (gθ ∩ h)). Since s is a subalgebra of m+ +
(gθ ∩ h), it follows that s = m+ + (gθ ∩ h). Thus B ∩U +U o specializes to
U(m+ + (gθ ∩ h)).
Recall the set ∆ ′ of Corollary 4.10 used to deﬁne the generators of B
whose top degree term is in G−. The description of the generators of B in
Corollary 4.10 implies that GKdim B/N is equal to the number of elements
in ∆ ′. Since the number of elements in ∆ + is just the dimension of n−, it
follows that ∆ ′ = ∆ +. Hence by Corollary 4.10, B contains elementsyiti +bi,
1 ≤ i ≤ n, where bi is in U +U o. It follows that tip( B) ∩G− = G−. This
proves (iii).
54
LetN ′ be the left ideal of B ∩U +U o generated by the augmentation ideal
of B ∩U o. We can analyze the left B ∩U +U o module (B ∩U +U o)/N′ in a
similar fashion to the analysis of B/N. It follows that B∩U +U o =B∩M+TΘ
contains elements xi +ci ∈ ˆB for each αi ∈ πΘ . Furthermore, ci ∈ U o and
B ∩U o specializes to U(gθ ∩ h). Now B ∩U o is just the group algebra
generated by B ∩TΘ . Therefore, rank B ∩TΘ = rank TΘ . Hence we can ﬁnd
generators of TΘ such that a power of each generator lies in B. This in turn
implies that B can be written as a direct sum of TΘ weight spaces. By the
maximality condition (7.25) of B, we obtain B ∩TΘ = TΘ . This completes
the proof of step (i).
Since TΘ ⊂ B, any element in U +U o ∩B = M+TΘ ∩B is a sum of TΘ
weight vectors contained in B. Thus xi +ci ∈B impliesxi ∈B. In particular
B containsxi for all αi ∈πΘ . Hence B ∩U +U o = M+TΘ and (ii) follows.
Fix i and consider again the element yiti +bi in B where bi ∈ U +U o.
Replacing bi by another element in U +U o if necessary, we may assume that
yiti +bi is a weight vector for the action of TΘ . By Lemma 1.3, we may
further assume that bi ∈G+ti. First consider the case when αi ∈πΘ . Choose
β maximal with respect to the standard partial ordering on Q(π) such that
π0,β (bi) ⁄= 0. By (4.7), ( π0,β ⊗Id)∆ (yiti +bi) is a nonzero element of G+
β ti ⊗
τ (−β)ti. Hence τ (−β)ti ∈TΘ and β ∈Q+(πΘ ). If 0 <γ <β , then γ is also
in Q+(πΘ ). Thus supp( bi) is a subset of {0} ×Q+(πΘ ). This forces bi to be
an element of M+TΘ and so yiti ∈B.
Now assume that αi /∈ πΘ . Choose β such that [0 ,β ] ∈ max(b). Then
by (4.11), ( π0,β ⊗Id)∆ (yiti +bi) is a nonzero element of G+
β ti ⊗τ (−β)ti.
In particular, τ (−β)ti = τ (−β +αi) is in TΘ . Since β ∈ Q+(π), it follows
that β ∈ αi +Q+(πΘ ) or β ∈ αp(i) +Q+(πΘ ). However, β must also be of
the same TΘ weight as −αi. The only possibility is β = Θ( −αi). By the
uniqueness property of the YI,j andXI,j discussed in Section 6 (see (6.3) and
the following discussion), the β weight term is a scalar multiple of ˜θ(yi)ti.
Indeed this is necessary in order for ∆ (yiti +bi) to be an element of U ⊗B.
Thereforebi =c˜θ(yi)ti +dti for some scalar c and elementd ∈G+ of bidegree
less than bideg( ˜θ(yi)ti). By (7.23),
∆ (yiti +bi) ∈ti ⊗ (yiti +bi) +U ⊗B.
By (1.8), (1.10), and (7.14), it follows that
∆ (dti) ∈ti ⊗dti +U ⊗ M+TΘ .
55
Since αi /∈ πΘ , this forces dti to be a scalar multiple of ti. Hence, up to
a Hopf algebra automorphism of U, the only possibility for B is one of the
standard or nonstandard analogs of U(gθ ). ✷
Let us return for now to our ﬁrst analog B˜θ . Recall the deﬁnition of the
antiautomorphismκ. One checks that κ((adrxj)b) = −((adryj)κ(b)) for any
b ∈U and 1 ≤j ≤n. Recall that m(i) = m1 + · · · +mr. Hence
κ[(adrx(m1)
i1 · · ·x(mr )
ir )t−1
p(i)xp(i)] = ( −1)m(i)(adry(m1)
i1 · · ·y(mr)
ir )yp(i).
A straightforward Uq(sl 2) computation as in the classical case (see (7.8))
yields
(adry(m1)
i1 · · ·y(mr)
ir )(adrx(mr )
ir · · ·x(m1)
i1 )t−1
i xi =t−1
i xi.
Set yj ·btp(i) =btp(i)q(α p(i),α j)yj −yjtjbtp(i)t−1
j for any b ∈U and 1 ≤i,j ≤n.
Note that yj ·btp(i) = ((ad ryj)b)tp(i). Recall the deﬁnition of π∗ immediately
following (7.5). We have
(−1)m(i)[y(m1)
i1 · · ·y(mr)
ir ·Bp(i)]t−1
p(i)ti
= ([( −1)m(i)(adry(m1)
i1 · · ·y(mr)
ir )yp(i)]ti +t−1
i xiti
= κ(˜θ(yi)ti) +q−(α i,α i)κ(yiti)
is an element of B˜θ for each αi ∈π∗. A similar argument shows that
κ(˜θ(yp(i))tp(i)) +q−(α i,α i)κ(yp(i)tp(i))
is also inB˜θ for eachαi ∈π∗. Thus one can ﬁnd a Hopf algebra automorphism
Υ in HR such that Υ restricts to the identity on M and TΘ and Υ( B)
contains κ(Υ( Bi)) for each αi /∈πΘ . Furthermore, one can show that Υ( B)
is generated by M, TΘ , and the κ(Υ( Bi)), αi /∈ πΘ . Now κ(Υ( M)) = M
and κ(Υ( TΘ )) = TΘ . It follows that κ(Υ( B)) = Υ( B). Hence the results of
Section 2 hold for B.
The same argument works for analogs of Variations 1 and 2 prov ided
that all entries of the tuples involved are from R(q). In particular, let [Θ] r
be the set {θb| all entries of b are in R(q)}. We refer to analogs of the
form Bθ b, s for θb ∈ [Θ] r and all entries of s are in R(q) as real analogs of
U(gθ ). Given θb ∈ [Θ] r, one can ﬁnd Υ ∈ H R such that Υ −1κΥ( Bθ b) = Bθ b.
Furthermore, for any s such that all of its entries are in R(q), we also have
56
that Υ −1κΥ( Bθ b, s) = Bθ b, s. Hence, we may apply results of Section 2 to all
real analogs of U(gΘ ).
Consider a real analog B of U(gθ ). Given a U module M, set X(M)
equal to the sum of all the ﬁnite-dimensional unitary B submodules of M.
The next result on basic Harish-Chandra modules associated to the pair U,B
follows from Section 2.
Theorem 7.6 Let B be a real analog of U(gθ ) and let M be a U module.
Then any ﬁnite-dimensional U module is a B unitary module and a Harish-
Chandra module for the pair U,B . Furthermore both F (U) and X(M) are
Harish-Chandra modules for the pair U,B .
We continue the assumption that B is a real analog of U(gθ ). Using
the approach of Section 3, we can deﬁne the quantum homogeneo us space
associated to B. The left invariants Rq[G]B
l are often referred to as Rq[G/K]
(or Aq[G/K]) in the literature (see for example [NS,(2.5)]). Here K can be
thought of merely as a symbol or as the complexiﬁcation of the compact
Lie group in G with Lie algebra gθ . Thus the homogeneous space G/K
is a symmetric space. The notation Rq[G/K] suggests that the right B
invariants ofRq[G] is the quantum analog of the ring of regular functions on
G/K. In [L3], it is shown that B is a “good” analog of U(gθ ) for constructing
quantum symmetric spaces in the sense of [Di, end of Section 3 ]. In particular,
Rq[G/K] has the same left U module structure as its classical counterpart
(see Theorem 7.8 below). We summarize this and related resul ts here. A
good survey on how to construct quantum symmetric spaces whi ch includes
a description of the classical situation is [Di]. For furthe r information about
classical symmetric spaces, the reader is referred to [He1] and [He2].
A ﬁnite-dimensional U moduleV is called a spherical module for B if the
space of invariantsV B has dimension 1. Recall the notion of Cartan subspace
and restricted root system introduced at the beginning of th is section. Let
a be the Cartan subspace {x ∈ h|θ(x) = −x} and let Σ be the associated
restricted root system. Let P +
Θ be the subset of P +(π) containing those λ
such that
(i) (λ,β ) = 0 for all β ∈Q(π) such that Θ( β) = β;
(ii) the restriction ˜λ ofλ to a∗ satisﬁes ( ˜λ,β )/(β,β ) is an integer for every
restricted root β.
57
The set P +
Θ is exactly the set of dominant integral weights such that the
corresponding ﬁnite-dimensional simple g module is spherical ([Kn, Theorem
8.49]). By [L3, Theorem 4.2 and Theorem 4.3] we have the same c lassiﬁcation
in the quantum case.
Theorem 7.7 LetL(λ) be a ﬁnite-dimensional U module with highest weight
λ up to some possible roots of unity. Then
(i) dim L(λ)B ≤ 1.
Moreover,
(ii) dim L(λ)B = 1 if and only if λ ∈P +
Θ .
We sketch the proof here and refer the reader to [L3] for full d etails. Let
vλ denote the highest weight generating vector of L(λ). Recall that for each
y ∈ G− there exists a b ∈ B such that b = y+ higher weight terms. Now
L(λ) is spanned by weight vectors of the form yvλ where y ∈ G−. Hence
dimL(λ)/B+vλ ≤ 1 where B+ is the augmentation ideal of B. Statement (i)
follows from the fact that B+vλ ∩L(λ)B is empty. A careful analysis using
the form of the generators of B further shows that vλ ∈B+vλ if and only if
λ /∈P +
Θ . This in turn implies (ii). The argument turns out to be much m ore
delicate when B is a nonstandard analog. ✷
Theorem 7.7, the Peter-Weyl decomposition of Rq[G], (3.1), and (3.4)
imply the following characterization of Rq[G]B
l as a right U module.
Theorem 7.8 There is an isomorphism of right U modules
Rq[G]B
l ∼=
⨁
λ ∈P +
Θ
L(λ)∗
There is an analogous statement for the right B invariants ofRq[G]. One
can also describe the B bi-invariants in a nice way. Identifying L(λ) with a
subspace of Rq[G]B
l , set H(λ) = Rq[G]B
bi ∩L(λ). Note that H(λ) is a trivial
left and right B module. Moreover, by Theorem 7.7, H(λ) is one-dimensional
if λ ∈P +
Θ and zero otherwise. The following direct sum decomposition into
trivial one-dimensional B bimodules is thus an immediate consequence of
Theorem 7.8.
58
Rq[G]B
bi ∼=
⨁
λ ∈P +
Θ
H(λ).
Let A be the subgroup of T consisting of those elements τ (λ) such that
Θ( λ) = −λ. Thus A can be thought of as a quantum version of a. Let WΘ de-
note the Weyl group associated to the restricted root system Σ. Since Σ ⊂ a∗,
a and hence A inherit an action of WΘ . The author has recently shown that,
Rq[G]B
bi is commutative and moreover is isomorphic to C(q)[A]WΘ . Thus, the
H(λ) are natural choices of quantum zonal spherical functions ( see [Di, the
discussion concerning (3.4)]). In special cases, these qua ntum zonal spher-
ical functions have been determined to be Macdonald polynom ials or other
q hypergeometric series (see for example [K], [N], [DN], [NS] ). Preliminary
work by the author suggests that this should be true in genera l.
It should be noted that these papers use analogs of U(gθ ) whose deﬁnition
diﬀers from the deﬁnition of the B˜θ and its variations found in this paper.
In [NM], one-sided coideal subalgebras are used. By [L2, Sec tion 6], using
Theorem 7.5, these are shown to be examples of the analogs pre sented here.
In other papers, two-sided coideals analogs of gθ are used. The specialization
of these two-sided coideals generate a much larger subalgeb ra than U(gθ ).
The important object in these papers, used to deﬁne quantum s ymmetric
spaces, is the left ideal generated by these two-sided coide als analogs of gθ .
It seems likely that these left ideals can be shown to be gener ated by the
augmentation ideal of one of the analogs presented here. Thi s is certainly
true for the left coideals studied in [K] and also for those in [N] ( combine
[N, Section 2.4] with [L2, Section 6]).
REFERENCES
[AJS] H.H. Andersen, J.C. Jantzen, and W. Soergel, Represen tations of quan-
tum groups at a p-th root of unity and of semisimple groups in characteristic
p: Independence of p, Ast´ erisque220, Soc. Math. France, Paris (1994).
[BF] W. Baldoni and P.M. Frajria, The quantum analog of a symm etric pair:
a construction in type ( Cn,A 1 ×Cn−1), Trans. Amer. Math. Soc. 8 (1997),
3235-3276.
[CP] V. Chari and A. Pressley, A Guide to Quantum Groups , Cambridge
University Press, Cambridge, (1995).
59
[DK] C. DeConcini and V.G. Kac, Representations of quantum g roups at
roots of 1, In: Operator Algebras, Unitary Representations, Enveloping A l-
gebras, and Invariant Theory , Progress in Math. 92, Birkh¨ auser, Boston
(1990), 471-506.
[Di] M.S. Dijkhuizen, Some remarks on the construction of qu antum sym-
metric spaces, In: Representations of Lie Groups, Lie Algebras and Their
Quantum Analogues, Acta Appl. Math. 44 (1996), no. 1-2, 59-80.
[DN] M.S. Dijkhuizen and M. Noumi, A family of quantum projec tive spaces
and related q-hypergeometric orthogonal polynomials, Trans. Amer. Math.
Soc. 350 (1998), no. 8, 3269-3296.
[D] J. Dixmier, Alg` ebres Enveloppantes, Cahiers Scientiﬁques, XXXVII,
Gauthier-Villars, Paris (1974).
[G] V. Guizzi, A classiﬁcation of unitary highest weight mod ules of the quan-
tum analogue of the symmetric pair ( An,A n−1), J. Algebra 192 (1997), 102-
129.
[H] J.E. Humphreys, Introduction to Lie Algebras and Representation Theory,
Springer-Verlag, New York (1972).
[HS] I. Heckenberger and K. Schmudgen, Classiﬁcation of bic ovariant dif-
ferential calculi on the quantum groups SL q(n + 1) and Sp q(2n), J. Reine
Angew. Math. 502 (1998), 141-162.
[He1] S. Helgason, Diﬀerential Geometry, Lie Groups, and Symmetric Spaces,
Pure and Applied Mathematics 80, Academic Press, New York (1978).
[He2] S. Helgason, Groups and Geometric Analysis, Integral Geometry, In-
variant Diﬀerential Operators, and Spherical Functions, Pure and Applied
Mathematics 113, Academic Press, Inc., Orlando (1984).
[J] N. Jacobson, Basic Algebra II, W. H. Freeman and Company, San Fran-
cisco (1980).
[JL1] A. Joseph and G. Letzter, Local ﬁniteness of the adjoin t action for
quantized enveloping algebras, J. of Algebra 153 (1992), 289 -318.
[JL2] A. Joseph and G. Letzter, Separation of variables for q uantized en-
veloping algebras, American Journal of Math. 116 (1994), 127-177.
60
[JL3] A. Joseph and G. Letzter, Verma module annihilators fo r quantized
enveloping algebras, Ann. Sci. Ecole Norm. Sup. (4) 28 (1995), no. 4,
493-526.
[Jo] A. Joseph, Quantum Groups and Their Primitive Ideals , Springer-Verlag,
New York (1995).
[Ka] V.G. Kac, Inﬁnite-Dimensional Lie Algebras, Third ed., Cambridge
University Press, Cambridge (1990).
[Ke] M.S. K´ eb´ e,O-alg` ebres quantiques,C. R. Acad. Sci. Paris, Ser. I Math.
322 (1996), no. 1, 1-4.
[KS] A. Klimyk and K. Schm¨ udgen, Quantum Groups and Their Represen-
tations, Texts and Monographs in Physics, Springer-Verlag, Berlin (1997).
[Kn] A. W. Knapp, Lie Groups Beyond an Introduction, Progress in Math.
140, Birkh¨ auser, Boston (1996).
[K] T. Koornwinder, Askey-Wilson polynomials as zonal sphe rical functions
on the SU(2) quantum group. SIAM J. Math. Anal. 24 (1993), no. 3,
795–813.
[KL] G.R. Krause and T.H. Lenagan, Growth of Algebras and Gelfand-Kirillov
Dimension, Research Notes in Mathematics 116, Pitman, London (1985).
[L1] G. Letzter, Subalgebras which appear in quantum Iwasaw a decomposi-
tions, Canadian Journal of Math. 49 (1997), no. 6, 1206-1223.
[L2] G. Letzter, Symmetric pairs for quantized enveloping a lgebras, J. Algebra
220 (1999), no. 2, 729-767.
[L3] G. Letzter, Harish-Chandra modules for quantum symmet ric pairs, Rep-
resentation Theory, An Electronic Journal of the AMS 4 (1999) 64-96.
[Lu] G. Lusztig, Introduction to Quantum Groups, Progress in Math. 110,
Birkh¨ auser, Boston (1994).
[M] S. Montgomery, Hopf Algebras and Their Actions on Rings, CBMS Re-
gional Conference Series in Mathematics 82, American Mathematical Society,
Providence (1993).
[N] M. Noumi, Macdonald’s symmetric polynomials as zonal sp herical func-
tions on some quantum homogeneous spaces, Advances in Mathematics 123
(1996), no. 1, 16-77.
61
[NS] M. Noumi and T. Sugitani, Quantum symmetric spaces and r elated q-
orthogonal polynomials, In: Group Theoretical Methods in Physics (ICGTMP)
(Toyonaka, Japan, 1994), World Sci. Publishing, River Edge , N.J. (1995) 28-
40.
[OV] A. L. Onishchik and E. B. Vinberg, Lie Groups and Lie Algebras III:
Structure of Lie Groups and Lie Algebras, Springer-Verlag, Berlin (1994).
[R] M. Rosso, Groupes Quantiques, Repr´ esentations Lin´ ea ires et Applica-
tions, Th` ese, Paris 7 (1990).
[Ve] D.N. Verma, Structure of certain induced representati ons of complex
semisimple Lie algebras, Bulletin of the American Mathematical Society 74
(1968), 160-166.
[V] D. Vogan, Representations of Real Reductive Lie Groups, Progress in
Math. 15, Birkh¨ auser, Boston (1981).
—————–
letzter@math.vt.edu
62
