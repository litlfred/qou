---
doc_id: arxiv-math-0103228v2
doc_title: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002"
section_id: sec-001-2-harish-chandra-modules
section_title: "Harish-Chandra modules"
section_number: 2
pages: 9-14
source_pdf: 0103228v2.pdf
source_sha256: 7d66dbbd4b87798f
toc_source: inferred
doc_brief: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002 — Coideal subalgebras of the quantized enveloping algebra ar e sur- veyed, with selected proofs included."
---
Consider a Lie subalgebra k of the semisimple Lie algebra g. A Harish-
Chandra module associated to the pair g, k is a g module which can be writ-
ten as a direct sum of ﬁnite-dimensional simple k modules. Harish-Chandra
modules are an important tool in classical representation t heory. This is
especially true when g, k is a symmetric pair. Harish-Chandra modules asso-
ciated to symmetric pairs provide an algebraic approach to t he representation
theory of real reductive Lie groups.
There is a nice introduction to the theory of Harish-Chandra modules
presented in [D, Chapter 9] from an algebraic point of view. T he ﬁrst section
of [D, Chapter 9] only assumes that k is reductive in g. A basic result which
is used repeatedly in this chapter of [D] is the following.
Theorem 2.1 ([D, Proposition 1.7.9]) The direct sum of all the ﬁnite-di-
mensional simple k modules inside a g module is a Harish-Chandra module
for the pair g, k.
This theorem allows one to ﬁnd large Harish-Chandra modules inside of
inﬁnite-dimensional g modules. Its proof uses the fact that k is reductive in
g and that U(g) is a locally ﬁnite ad U(g) module.
In the quantum setting, Uq(k) is not always a subalgebra of Uq(g) when k
is a Lie subalgebra of g. However, one often ﬁnds a quantum analog of U(k)
which is a one-sided coideal subalgebra of Uq(g). Thus any good theory of
quantum Harish-Chandra modules must work for pairs Uq(g),I whereI is a
one-sided coideal subalgebra of Uq(g). In order to begin such a theory, it is
necessary to have an analog of Theorem 2.1. This presents two diﬃculties.
The ﬁrst is that U, in contrast to the classical situation, is not a locally ﬁni te
adU module. (We will return to this obstruction in Section 4.) Th e second
is: what does it mean for a coideal subalgebra to be reductive in U?
In this section, we present a quantum version of Theorem 2.1 u sing the
locally ﬁnite part F (U) of U and a certain condition on coideal subalgebras
which substitutes for reductivity. The material of this sec tion is based on [L1,
Section 4] and [L3, Section 3]. This result sets the stage for the development
of a quantum Harish-Chandra module theory. Indeed, the auth or has checked
that many of the results of [D, Section 9.1] and their proofs c arry over to
9
coideal subalgebras satisfying this quantum version of The orem 2.1. Some
properties of quantum principal series modules analogous t o those in [D,
Section 9.3] are proved in [L3, Section 6]. Spherical module s (see [D, 9.5.4])
have been classiﬁed in the quantum case (see Section 7, Theor em 7.7 and
[L3, Section 4]). This is discussed further in Section 7.
Recall the deﬁnition of the adjoint action (1.2) and deﬁne
(2.1) F (U) = {v ∈U| dim(adU)v <∞}.
By [JL1, Corollary 2.3, Theorem 5.12, and Theorem 6.4], F (U) is an algebra,
it can be written as a direct sum of ﬁnite-dimensional simple U modules, and
it is “large” in U. It is also true that F (U) is a left coideal of U, a subject
we will return to in Section 5.
Fix a left coideal subalgebra I of U. Note that
F (U)I = {
∑
firi|fi ∈F (U),r i ∈I}
is also a subalgebra ofU. This follows from the fact that rf =
∑
r(1)ǫ(r(2))f =∑
((adr(1))f )r(2) for any r ∈I and f ∈F (U). Since I is a left coideal, each
r(2) ∈I. Furthermore the ad-invariance of F (U) implies that (ad r(1))f is in
F (U). We use F (U)I to deﬁne Harish-Chandra modules.
Deﬁnition 2.2 A Harish-Chandra module for the pair U,I is an F (U)I
module which is a direct sum of ﬁnite-dimensional simple I modules.
Let us take a closer look at the condition that k is reductive in g. Reduc-
tivity means that (ad k) acts semisimply on g. This assumption is enough to
prove that k is itself reductive and that the center of k can be extended to
a Cartan subalgebra of g. It is unclear what the corresponding assumption
in the quantum case, namely that (ad I) acts semisimply on F (U), implies.
It seems unlikely that this assumption alone will yield an an alog of Theorem
2.1.
Of course, there would be no problem if I acted semisimply on all ﬁnite-
dimensional I modules. When I turns out to be a Hopf subalgebra of U
isomorphic to a quantized enveloping algebra of a semisimpl e Lie subalgebra
of g, this is certainly true. However, complete reducibility do es not hold
in general for the large class of coideal subalgebras consid ered in Section 7.
Thus we need a replacement for the notion of reductive in g. This substitute
10
is invariance under the action of a certain conjugate linear antiautomorphism
of U.
Let κ denote the conjugate linear form of the quantum Chevalley an -
tiautomorphism. In particular, let UR(q) denote the R(q) subalgebra of U
generated by xi,y i,t ±1
i , for 1 ≤ i ≤ n. The antiautomorphism κ of UR(q) is
deﬁned by κ(xi) = yiti, κ(yi) = t−1
i xi and κ(t) = t for all t ∈ T . We then
extend κ to U using conjugation. More precisely, given a ∈ C, write ¯a for
the complex conjugate of a. Set ¯q =q. Then κ(au) = ¯aκ(u) for all u ∈UR(q).
It is straightforward to check using (1.8), (1.9), and (1.10 ) that
(2.2) ∆ (κ(b)) = (κ ⊗κ)∆ (b)
for all b ∈ U. Moreover κ gives U the structure of a Hopf ∗ algebra where
∗ =κ ([CP, Section 4.1F ]).
For the remainder of this section, we assume that I is a left coideal
subalgebra such that κ(I) = I. Thus one can think of I as a ∗ subalgebra of
U.
The ﬁeld R(q) can be made into a real ordered ﬁeld ([J, Section 11.1])
where the positive elements are deﬁned as follows. Write a po lynomial f (q)
in the form (q − 1)s(fm(q − 1)m + · · ·+f1(q − 1) +f0) where each fi ∈ R and
m,s ∈ N. Then f (q) is positive if and only if f0> 0. An element h ∈ R(q) is
positive if and only if h can be written as a quotient of positive polynomials.
This induces a total order on R(q).
We next specify a class of “nice” ﬁnite-dimensional I modules.
Deﬁnition 2.3 AnI moduleW is called unitary if it admits a sesquilinear
form SW (i.e. linear in the ﬁrst variable and conjugate linear in the second
variable) such that
(i) SW (av,w ) = SW (v,κ (a)w) for all a ∈I and v,w in W
(ii) SW (v,v ) is a positive element of R(q) for each nonzero vector v ∈W
(iii) SW (v,w ) = SW (w,v ) for all v and w in W .
Let W be a ﬁnite-dimensional unitary I module. Choose a nonzero vec-
tor v ∈ W such that SW (v,v ) = 1. Now suppose that w ∈ W such that
SW (w,v ) = 0. By Deﬁnition 2.3(iii), it follows that SW (v,w ) also equals
11
zero. Hence one can show using induction that W has an orthonormal basis
with respect to SW .
The following result and its corollary show that I has an extensive family
of unitary modules, namely the ﬁnite-dimensional simple I submodules of
any ﬁnite-dimensional simple U module.
Theorem 2.4 Every ﬁnite-dimensional unitary I module can be written as
a direct sum of ﬁnite-dimensional simple unitary I modules.
Proof: Let W be a ﬁnite-dimensional unitary I module with sesquilinear
form S = SW as in Deﬁnition 2.3. Let V be a ﬁnite-dimensional simple
I submodule inside of W . By Deﬁnition 2.3, the restriction of S to W
again satisﬁes conditions (i), (ii), and (iii). Furthermor e, Deﬁnition 2.3(i)
implies that the orthogonal complement W ⊥ of W with respect to S is an
I module. Hence V ∼= W ⊕W ⊥, a direct sum of unitary I modules with
smaller dimension. The proof follows by induction on dim V . ✷
Corollary 2.5 Every ﬁnite-dimensional simple U module V is a Harish-
Chandra module for the pair U, I.
Proof: Let V be a ﬁnite-dimensional simple U module. It is well known
that ﬁnite-dimensional U modules are a direct sum of their weight spaces.
Moreover, the weight space of maximal weight is one dimensio nal. Let v be
a basis vector for this highest weight space and note that v generates V as
a U module. The vector v is called a highest weight generating vector of V .
Recall that U −
+ denotes the augmentation ideal of U −. Note that U −
+v is the
subspace of V spanned by those weight vectors whose weights are strictly
less than that of v. Furthermore, V is the direct sum of C(q)v and U −
+v.
Letϕ be the projection of U ontoU o using the direct sum decomposition
U = U o ⊕Y (1.14). Deﬁne a sesquilinear form S on V by S(v,v ) = 1 and
S(av,bv ) = S(v,ϕ (κ(a)b)v) for all a,b ∈ U. Since ϕ(b) = 0 for all b in U −
+ ,
it follows that S(v,U −
+v) = 0.
Note that S satisﬁes Deﬁnition 2.3(i). As in say ([L1, Lemma 4.2]), S
specializes to the classical positive deﬁnite Shapovalov f orm of [Ka, 11.5 and
Theorem 11.7]. Thus ([L1, Lemma 4.2]) S(w,w ) ⁄= 0 for any nonzero vector
w ∈V . It is straightforward to check that S restricts to a R(q) bilinear form
on UR(q)v. Moreover, S restricted to ˆUR(q) takes values in R[q,q −1](q−1).
12
Let w be an element in ˆUR(q)v. We can write S(w,w ) = f (q) with f (q) in
R[q,q −1](q−1). Since the specialization of S is positive deﬁnite, we must have
that f (1) ≥ 0. It follows that f (q) ≥ 0. This fact and the nondegeneracy
property implies that S satisﬁes Deﬁnition 2.3(ii).
Recall the direct sum decomposition (1.14) of U. Note that κ(Y ) = Y and
κ(a) = a for all a ∈ U o ∩UR(q). Therefore ϕ(κ(b)) = ϕ(b) for all b ∈ UR(q).
It follows that S is symmetric when restricted to UR(q)v. In particular, S
satisﬁes Deﬁnition 2.3(iii). Thus V is a unitary I module. The result now
follows from Theorem 2.4. ✷
Note that we cannot expect ∆ (I) to be a subset of I ⊗I. Hence the
tensor product of two I modules does not necessarily admit an action of I
via the comultiplication of U. However, since I is a left coideal, the tensor
product V ⊗W of a U module V with an I module W is an I module. In
particular,a(v ⊗w) =
∑
a(1)v ⊗a(2)w for all v ⊗w ∈V ⊗W anda ∈I. The
next lemma shows that the notion of unitary behaves well with respect to
the tensor product of a U module with an I module.
Lemma 2.6 LetV be a ﬁnite-dimensional U module and let W be a ﬁnite-
dimensional unitary I module. Then V ⊗W is a ﬁnite-dimensional unitary
I module.
Proof: Let SV (resp. SW ) denote the sesquilinear form on V (resp. W )
satisfying the conditions of Deﬁnition 2.3. Deﬁne a sesquil inear form S =
SV ⊗W onV ⊗W by setting S(a ⊗b,a ′ ⊗b′) = SV (a,a ′)SW (b,b ′). It is easy to
check Deﬁnition 2.3(iii) holds for S. Let {vi} be an orthonormal basis for V
with respect to SV and let {wi} be an orthonormal basis for W with respect
toSW . Then S(
∑
bijvi ⊗wj,
∑
bijvi ⊗wj) =
∑
bij¯bij. Thus Deﬁnition 2.3(ii)
holds for S. Condition (2.2) on κ ensures that S satisﬁes Deﬁnition 2.3(i). In
particular, for c ∈I, we have S(c(a ⊗b),a ′ ⊗b′) = S(
∑
c(1)a ⊗c(2)b,a ′ ⊗b′) =
S(a ⊗b, ∑ κ(c(1))a′ ⊗κ(c(2))b′) = S(a ⊗b,κ (c)(a′ ⊗b′)). ✷
We now obtain a quantum analog of Theorem 2.1.
Theorem 2.7 The sum of all the ﬁnite-dimensional simple unitary I mod-
ules inside of the F (U)I moduleM is a Harish-Chandra module for the pair
U,I .
13
Proof: Assume that W is a ﬁnite-dimensional simple unitary I module
contained in M. It suﬃces to show that the F (U)I module generated by
W is a direct sum of ﬁnite-dimensional simple unitary modules . Note that
F (U)IW =F (U)W =IF (U)W is an I module. The vector space F (U)⊗W
is also an I module where the action is given by
a · (f ⊗w) =
∑
(ada(1))f ⊗a(2)w
for allf ∈F (U),w ∈W , anda ∈I. Furthermore, F (U)W is a homomorphic
image of the I moduleF (U) ⊗W . Recall that F (U) is a direct sum of ﬁnite-
dimensional simple (adU) modules. By Corollary 2.5, each ﬁnite-dimensional
simple (ad U) module is a unitary I module. Thus by Lemma 2.6, F (U) ⊗
W , and hence F (U)W , splits into a direct sum of ﬁnite-dimensional simple
unitary I modules. ✷
Let HR be the set of all Hopf algebra automorphisms of U which restrict
to a Hopf algebra automorphism of UR(q). Let Υ ∈ H R. Suppose that I is
a left coideal subalgebra such that Υ −1κΥ( I) = I. Then the results of this
section hold for I where we deﬁne unitary I modules using Υ −1κΥ instead
of κ.
