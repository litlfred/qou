---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-024-numerical-realization-of-motivic-functions
section_title: "Numerical realization of motivic functions"
section_number: null
pages: 75-80
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
This section is not used in further consideration, its goal i s only to show
that the abstractly deﬁned ring
M
G,µ
(X) can be realized as certain ring of
functions with numerical values.
Let Z be a scheme of ﬁnite type over a ﬁnite ﬁeld k≃ Fq endowed with
an action of the group µn of roots of 1 such that n<p =char Fq. We choose
a prime l⁄= p. Let us deﬁne Y as the quotient ( Z× (A1
k\{ 0}))/µn with
respect to the diagonal action of µn. Then we have a morphism
π :Y→ A1
k\{ 0}, (z,t )↦→tn∀(z,t )∈ (Z× A1
k\{ 0})(
Fq).
Let j : A1
k\{ 0}→ A1
k be the natural embedding. We deﬁne the number
NZ = TrFr (F (j∗π!(Ql,Y ))|s=1)∈
Ql ,
which is the trace of the Frobenius Fr of the ﬁber at s = 1 of the Fourier
transform of the l-adic sheaf j∗π!(Ql,Y ), where Ql,Y denotes the constant
sheaf Ql on Y . In fact the number NZ can be considered as an element of
the cyclotomic ﬁeld Q(ηp), where ηp is a primitive p-th root of 1:
1 +ηp +··· +ηp−1
p = 0 .
We have a canonical non-trivial character χ : Fq→ Q(ηp)∗ given by the
composition of the trace Tr Fq→Fp : Fq→ Fp with the additive character
χp : Fp→ Q(ηp)∗, m modp↦→ηm
p .
Then
NZ =
∑
s∈(A1
k\{0})(Fq )
#(π−1(s)(Fq))χ(s) .
Notice that the last formula makes sense for constructible Z as well.
Let now X be a constructible set over a ﬁeld k,char k = 0, endowed with
an action of an aﬃne algebraic group G.
16In this way we have circumvented the problem of deﬁning the ca tegory of G-equivariant
motivic sheaves.
75
Deﬁnition 13 We call a model for (X,G ) the following choices:
• a ﬁnitely generated subring R⊂ k,
• a schemeX→ Spec(R) of ﬁnite type,
• an aﬃne group scheme G→ Spec(R) together with an embedding G֒→
GL(N)R,
• an action of G onX ,
• a constructible identiﬁcation over k ofX× Spec(R)Spec(k) with X, as
well as an isomorphism of groups G×Spec(R)Spec(k)≃G over k, com-
patible with the actions.
Such a model always exists, and models form a ﬁlterted system . With a
given model for ( X,G ) we associate a commutative unital ring
K(X ) = lim −→
{open U⊂(X×GL(n))/G}
∏
{closed x∈U}
Q(ηchar k(x)) ,
where k(x) is the residue ﬁeld of x (which is a ﬁnite ﬁeld).
Suppose that we are given a model for ( X,G ) and let f∈M G,µ(X). As
always we assume that the µ-action on X is good and factors through the
action of some µn.
Deﬁnition 14 A model for f compatible with the model (R,X,G) for (X,G )
consists of the following data:
• a ﬁnite set J, numbers Nj,dj,nj ∈ Z, where j ∈ J, such that all
numbersNj are positive and invertible in O(X ),
• G×µNj -equivariant morphisms of constructible sets Yj→X given for
eachj∈J, whereYj→X areG× µNj -schemes of ﬁnite type, and we
endowX with the trivial action of the group µNj ,
These data are required to satisfy the condition that
f =
∑
j∈J
nj [Yj×Spec(R)Spec(k)→X]· Ldj.
76
Models for f always exist. Moreover, for any ﬁnite collection ( fi)I∈I of ele-
ments ofMG,µ(X) there exists a model for ( X,G ) with compatible models
for (fi)I∈I .
Having a model for f we can associate with it an element fnum∈K(X )
in the following way. Let x∈ (X× GL(N)R)/G be a closed point. We can
apply the considerations of the beginning of this section to the ﬁber Zj,x over
the point x, of the map (Yj×GL(N)R)/G→ (X× GL(N)R)/G, whereYj is
the scheme from the deﬁnition of the model for f . Then for each j we obtain
an element NZj,x ∈ Q(ηp),p =char k(x). Finally, we set
fnum(x) :=
∑
j∈J
njqdj
x NZj,x ,
whereqx := #k(x). Hence we realize f as a function with values in numbers.
5 Orientation data on odd Calabi-Yau cate-
gories
Considerations of this section are reminiscent of those in Q uantum Field
Theory when one tries to deﬁne determinants for the Gaussian integral in a
free theory.
5.1 Remarks on the motivic Milnor ﬁber of a quadratic
form
Although the theory of motivic Milnor ﬁber was deﬁned over a ﬁ eld of char-
acteristic zero, an essential part of considerations below has meaning over an
arbitrary ﬁeld k,char k⁄= 2 if we replace the notion of motivic Milnor ﬁber
by its l-adic version.
Let now V be a k-vector space endowed with a non-degenerate quadratic
form Q. We deﬁne an element
I(Q) = (1−MF 0(Q))L− 1
2 dimV∈M µ(Spec(k))[L±1/2] ,
where L1/2 is a formal symbol which satisﬁes the relation ( L1/2)2 = L, and
Q is interpreted as a function on V . Then the motivic Thom-Sebastiani
theorem implies that
I(Q1⊕Q2) = I(Q1)I(Q2) .
77
Also we have I(Q) = 1, if Q is a split form: Q =∑
1≤i≤nxiyi for V = k2n.
Therefore, we have a homomorphism of groups
I :Witt (k)→ (Mµ(Spec(k))[L±1/2])× ,
where Witt (k) is the Witt group of the ﬁeld k. We can think of it as a
multiplicative character. Let us denote by J2(k) := J2(Spec(k)) the quotient
of the group Z×k×/(k×)2 by the subgroup generated by the element (2 ,−1).
There is an obvious homomorphism Witt (k)→ J2(k) given for a quadratic
form Q by
[Q]↦→(rkQ, det(Q) mod(k×)2) .
Notice that all “motivic realizations” of I(Q) in the sense of Section 4.1
depend only on the image of [ Q] in J2(k). This is similar to the classical
formula (for k = R and a positive deﬁnite form Q)
∫
V
exp(−Q(x))dx = (2π)− 1
2 dimV (det(Q))−1/2
in the sense that the answer depends on dim V and det(Q) only. In particular,
the homomorphism of rings
Mµ(Spec(k))→K0(Db
constr(Gm, Ql))
(see Section 4.1, (ii), (iii) and Section 4.2) induces (by co mbining with the
above character) a homomorphism of abelian groups
Witt (k)→ (K0(Db
constr(Gm, Ql))[L±1/2])× .
It is easy to see that it factors through the homomorphism Witt (k)→J2(k).
For example the element of K0-group corresponding to the pair ( n,a ),n ∈
2Z + 1,a∈ k× is represented by L−1/2[F ] where F is a local system on Gm
associated with the double cover of Gm given by y↦→y2a,y∈ Gm(k).
Question 1 The above considerations give rise to the following questio n.
Let us consider the family of quadratic forms Qa1,a2(x,y ) = a1x2
1 + a2x2
2
wherea1,a 2∈ k×. Is it true that [Qa1,a2] = [Qa′
1,a′
2] in K0(Var k) as long as
a1a2 =a′
1a′
2?
We expect that the answer to the Question is negative, and thi s is the
main reason for introducing the equivalence relation for th e motivic functions
in Section 4.5.
78
The above considerations can be generalized to arbitrary co nstructible
(or ind-constructible) sets. Namely, let X be a constructible set over k. We
deﬁne the group J2(X) as the quotient of the group
Constr(X, Z)×
(
Constr(X, Gm)/Constr (X, Gm)2)
by the subgroup consisting of the elements (2 f, (−1)f ),f ∈ Constr(X, Z),
where we denote by Constr(X,Y ) the set of constructible maps X → Y .
To a constructible vector bundle V → X endowed with a non-degenerate
quadratic form Q = (Qx)x∈X we associate the element
I(V,Q ) := (1−MF 0(Q))L− 1
2 dimV∈ (Mµ(X)[L±1/2])× .
Here we treat each Qx as a formal power series on the ﬁber Vx and dimV∈
Constr(X, Z). One can show that this correspondence gives rise to a homo-
morphism of groups
I :J2(X)→ (M
µ
(X)[L±1/2])× .
This fact has a simple “numerical” counterpart: for the case k≃ Fq, two
aﬃne quadrics given by equations Q1(x) = 0 ,Q 2(x) = 0 have the same
number of points if Q1,Q 2 are two non-degenerate quadratic forms of equal
rank and determinant.
Let us consider a symmetric monoidal category sPic 2(X) consisting of
constructible super line bundles L→X endowed with an isomorphismL⊗2≃
1X, where 1X is a trivial even line bundle on X. It is easy to see that the
group J2(X) is the group of isomorphism classes of objects of sPic 2(X). If
V → X is a constructible super vector bundle, V = Veven⊕ Π Vodd then
there is a well-deﬁned super line bundle (called super deter minant bundle)
sdet(V )→X given by
sdet(V ) := Π dimV even−dimV odd(
∧topVeven⊗ (∧topVodd)∗)
,
where Π is the parity change functor.
Recall canonical isomorphisms:
1. sdet(V∗)≃ sdet(Π( V ))≃ (sdet(V ))∗,
2. sdet(⊕i∈IVi)≃⊗ i∈I sdet(Vi),
3. if V carries an odd diﬀerential d then sdet(V )≃ sdet(H•(V,d )),
79
4. for an exact triangle of complexes ( V•
1,d 1)→ (V•
2,d 2)→ (V•
3,d 3) there
is a canonical isomorphism
sdet(V•
2 )≃ sdet(V•
1 )⊗ sdet(V•
3 ) .
In case if V carries a non-degenerate quadratic form Q = (Qx)x∈X we
have a canonical isomorphism sdet( V )≃ (sdet(V ))∗. Therefore in this case
we have a well-deﬁned object of sPic 2(X). Its class in the group J2(X) is
represented by the pair
(dimV, {det(Qx)}x∈X mod(Constr(X, Gm))2) .
The above considerations can be generalized to the case when X is acted
by an algebraic group G. Then one replaces the category sPic 2(X) by the
category sPic 2(X,G ) of G-equivariant constructible super line bundles L
endowed with a G-equivariant isomorphism L⊗2≃ 1X. The group of iso-
morphism classes of sPic 2(X,G ) we denote by J2(X,G ). In what follows we
will often omit the word “equivariant” in the consideration s involving the
category sPic 2(X,G ).
Remark 19 Let us make an additional assumption that √−1∈ k. In this
case the quadratic form x2 +y2 = (x +√−1y)(x−√−1y) is split. Then
MF 0(x2 +y2) = 1− L and we can consider the element L1/2 := 1−MF 0(x2)
which enjoys the property (L1/2)2 = L. Furthermore, the group J2(X) can be
canonically identiﬁed with the product
Constr(X, Z/2Z)×Constr(X, Gm)/(Constr(X, Gm))2 .
Therefore the isomorphism classes of objects of sPic 2(X) can be identiﬁed
with pairs (constructible µ2-function, constructible µ2-torsor).
