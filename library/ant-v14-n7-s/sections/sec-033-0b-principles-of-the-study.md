---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-033-0b-principles-of-the-study
section_title: "0B. Principles of the study"
section_number: null
pages: 46-48
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
instead, the harmonic Frobenius, deﬁned in [Jarossay 2015, Deﬁnition 2.3.5], (we will reproduce it in
Section 1D). It is a variant of the Frobenius which is much simpler and more natural from the point of
view of multiple harmonic sums, and computing it sufﬁces to compute the Frobenius.
Whereas the Frobenius is an isomorphism of bundles with connection, the harmonic Frobenius is a
map on a space which contains the noncommutative generating series of weighted multiple harmonic
sums harm((ni)d;(ξi)d+1)= mnd+···+n1hm((ni)d;(ξi)d+1).
We will use the fact that the harmonic Frobenius can be expressed in two ways:
(a) One “in terms of integrals”, i.e., in which the coefﬁcients of the harmonic Frobenius are expressed in
terms of p-adic cyclotomic multiple zeta values, which are integrals and which we want to compute.
(b) Another one “in terms of series”, in which the coefﬁcients of the harmonic Frobenius are certain
sums of series expressed in terms of the numbers har pα((ni)d;(ξi)d+1), which are explicit.
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1713
In [Jarossay 2015], by writing these two expressions and observing that they are equal, we get an
expression for p-adic cyclotomic multiple zeta values in terms of the numbers harpα((ni)d;(ξi)d+1) and
vice-versa. We are going to do something similar here, not for the harmonic Frobenius but for the study of
the numbers harq˜α((ni)d;(ξi)d+1), as functions of˜α∈ N∗. Since the harmonic Frobenius can be expressed
in terms of these numbers, this will directly provide a study of the iterated harmonic Frobenius in terms
of its number of iterations.
After some preliminaries (Section 1) we will do this study in terms of integrals (Section 2), in terms
of series (Section 3), and we will use the fact that these two ways give the same result (Section 4). In
Section 5 we will go back from the harmonic Frobenius to the Frobenius.
Moreover, we will keep track of the motivic structure underlying this framework. Indeed, p-adic
cyclotomic multiple zeta values are reductions of p-adic periods [Yamashita 2010], and there is a motivic
Galois action on the pro-unipotent fundamental groupoid of P1\{ 0,µ N,∞} [Deligne and Goncharov
2005, Section 5].
The Frobenius is expressed by means of the Ihara action (1-1), which is the image of the motivic Galois
action by a certain morphism (see Section 1A3). In [Jarossay 2015], the passage from the Frobenius
to the harmonic Frobenius lifts to a passage from the Ihara action to an operation which we called the
pro-unipotent harmonic action of integrals, and we also ﬁnd a pro-unipotent harmonic action of series
(see Section 1D). The interest of pro-unipotent harmonic actions is that, being byproducts of the motivic
Galois action, they retain certain properties of motivic Galois actions; and having a computation which
keeps track of the motivic Galois action is key for us. The pro-unipotent harmonic actions are the main
objects in our papers [Jarossay 2014; 2016a; 2016b] in which we show the compatibility between our
computation and the motivic Galois theory of p-adic cyclotomic multiple zeta values.
Establishing the deﬁnition of pro-unipotent harmonic actions requires enriching the pro-unipotent
fundamental groupoid, which is a groupoid in afﬁne schemes over P1\{ 0,µ N,∞} by turning it into a
groupoid in ultrametric complete normed algebras [Jarossay 2015, Section 1].
0C. A few deﬁnitions. The study will require new deﬁnitions. First, we will deﬁne an ad hoc notion
of contraction mapping (Deﬁnition 1B.2). We will show that the Frobenius at base-points (⃗11,⃗10) is a
contraction in our ad hoc sense. This will shed light on the dynamics of the Frobenius which has a unique
ﬁxed point. Thus, the ultrametric framework established in [Jarossay 2015] will be crucial here because
in this framework we will introduce a notion of contraction mapping and we will see that the Frobenius is
a contraction. Keeping track of the motivic structures will also require new deﬁnitions.
We will study harq˜α as a function of˜α “in terms of integrals” (Section 2) by viewing harq˜α via their
expression in terms of p-adic cyclotomic multiple zeta values proved in the main theorem of [Jarossay
2015]. This will be done in two different ways, corresponding to the two types of p-adic cyclotomic
multiple zeta values evoked in Section 0A:
(i) A way involving the ﬁxed point of the Frobenius and the numbers ζ KZ
q . It will lead us to introduce a
pro-unipotent harmonic action of integrals at (1, 0),◦
∫1,0
har (Deﬁnition 2A.3), which is a variant of
1714 David Jarossay
the notion introduced in [Jarossay 2015]. Another point of view on this object will be explained in
the Appendix.
(ii) A way involving the numbersζp,α0. It will lead us to introduce a map iter∫
har(a,3) of iteration of the
harmonic Frobenius of integrals at(1, 0), (3 and a are formal variables which represent respectively
q˜α and˜α/˜α0) (Deﬁnition 3B.1).
In the study of harq˜α as a function of˜α in terms of series (Section 3), we do not have an analogue of
the ﬁxed point and the study will lead us to introduce a map of iteration of the harmonic Frobenius of
series iter6
har(a,3) (Deﬁnition 3B.1).
Finally, in Section 4, we will relate Sections 2 and 3 by deﬁning a map of comparison between series
and integrals, which will be injective thanks to the results of Sections 2 and 3.
As in [Jarossay 2015] these deﬁnitions enable us to express the computation not number by number,
but as a new structure on the pro-unipotent fundamental group, which is more efﬁcient. Indeed, this
structure retains certain features of the motivic Galois theory of periods, which will be crucial in our
subsequent papers [Jarossay 2014; 2016a; 2016b] in which we will relate the motivic Galois theory of
p-adic cyclotomic multiple zeta values to our formulas.
