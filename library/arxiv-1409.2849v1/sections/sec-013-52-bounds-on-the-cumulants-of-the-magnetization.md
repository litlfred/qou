---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-013-52-bounds-on-the-cumulants-of-the-magnetization
section_title: "Bounds on the cumulants of the magnetization"
section_number: 5.2
pages: 41-48
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
tion, we now have to gather the estimates given by Theorem 21 to get the asymptotics
of the cumulants κ(2r)(Mn) of the magnetization.
42 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
5.2.1. Reordering of indices and compositions. Since the joint cumulants of spins have
been computed for ordered spins i1 ≤ i2 ≤ . . .≤ i2r, in the right-hand side of the
expansion
κ(2r)(Mn) =
n
∑
i1,...,i2r=1
κ(σ(i1), . . . ,σ(i2r)),
we need to reorder the indices i1, . . . ,i2r, and take care of the possible identities be-
tween these indices. We shall say that a sequence of indices i1, . . . ,ir has type c =
(c1, . . . ,cl) with the ci positive integers and|c| = ∑l
i=1 ci = r if, after reordering, the
sequence of indices writes as
i′
1 = i′
2 = . . . = i′
c1 < i′
c1+1 = i′
c1+2 =··· = i′
c1+c2 < i′
c1+c2+1 =··· .
Here, i′
k stands for the k-th element of the reordered sequence. For instance, the se-
quence of indices (3, 2, 3, 5, 1, 2) becomes after reordering (1, 2, 2, 3, 3, 5), so it has type
(1, 2, 2, 1). The type of a sequence of indices of length r can be any composition of size
r, and we denote Cr the set of these compositions. Conversely, given a composition of
size r and length l, in order to construct a sequence of indices (i1, . . . ,ir) with type c
and with values in [ [1, n] ], one needs:
• to choose which indices i will fall into each class (i′
1, . . . ,i′
c1), (i′
2, . . . ,i′
c1+c2), etc.;
there are (r
c
)
= r!
c1! c2!··· cl!
possibilities there.
• and then to choose 1 ≤ j1 < j2 <··· < jl ≤ n so that j1 = i′
1 =··· = i′
c1,
j2 = i′
2 =··· = i′
c1+c2, etc.
As a consequence,
κ(2r)(Mn) = ∑
c∈C2r
∑
1≤j1<j2<···<j𝓁(c)≤n
(2r
c
)
κ
(
σ(j1)c1, . . . ,σ(j𝓁(c))c𝓁(c)
)
= (−1)r−1
∑
c∈C2r
∑
δ∈D∗
2r
(2r
c
)
C(δ) B(n, c, δ)
where C(δ) = ∏2r−1
i=1 δi is the quantity computed in the previous paragraph, and
B(n, c, δ) = ∑
1≤j1<j2<···<j𝓁(c)≤n
x∑{a<b}∈ν(δ)(ib−ia),
the indices i being computed from the indices j according to the rule previously ex-
plained, namely,
j1 = i1 =··· = ic1;
j2 = ic1+1 =··· = ic1+c2;
... ...
j𝓁(c) = ic1+···+c𝓁(c)−1+1 =··· = i2r.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS43
Example. Suppose r = 1. There are two compositions of size 2, namely, (2) and (1, 1),
and one trivial tree with 0 edge; therefore,
κ(2)(Mn) = B(n, (2),•) + 2 B(n, (1, 1),•)
=
n
∑
j1=1
1 + 2 ∑
1≤j1<j2≤n
xj2−j1.
The double geometric sum has the same asymptotics as ∑n
j1=1 ∑∞
j2=j1+1 xj2−j1 = n x
1−x,
so
κ(2)(Mn)≃ n 1 + x
1− x = n e2β.
It is not hard to convince oneself that the approximation performed in the previous
example can be done in any case, so that a correct estimate ofB(n, c, δ) is n B(c, δ), with
B(c, δ) = ∑
0=j1<j2<···<j𝓁(c)
x∑{a<b}∈ν(δ)(ib−ia).
In this new expression, the indices j are unbounded (except the ﬁrst one, ﬁxed to 0),
and what we mean by approximation is that
n B(c, δ) = B(n, c, δ) + O(1),
with a positive remainder corresponding to terms of the geometric series with indices
larger than n. So:
Proposition 23. An upper bound, and in fact an estimate of|κ(2r)(Mn)| is
|κ(2r)(Mn)|≤ n ∑
c∈C2r
∑
δ∈D∗
2r
(2r
c
)
B(c, δ) C(δ).
5.2.2. Computation of the functional B. There is a simple algorithm that allows to com-
pute B(c, δ) for any Dyck path δ and any composition c. Let us explain it with the
path δ associated to the non-crossing pairing ν of Figure 9 and with the composition
c = ( 3, 2, 1, 2, 2). This composition c corresponds to some identiﬁcations of indices,
which we make appear on the diagram of the pairing ν as follows:
18
FIGURE 18. Identiﬁcations of indices corresponding to the composition
c = (3, 2, 1, 2, 2).
We now contract the green edges added above, obtaining thus:
44 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
j1 j2 j3 j4 j5
19
FIGURE 19. Contraction of the diagram of a non-crossing partition along
a composition.
This new diagram corresponds to the following simpliﬁcation of the sum B(c, δ):
B(c, δ) = ∑
0=i1=i2=i3<i4=i5<i6<i7=i8<i9=i10
xi10+i9+i8−i7+i6−i5−i4+i3−i2−i1
= ∑
0=i1<i4<i6<i7<i9
x2i9+i5−2i4−i1 because of the identities of indices;
= ∑
0=j1<j2<j3<j4<j5
x(j5−j1)+(j5−j2)+(j3−j2) by relabeling the indices.
So, the new diagram, which we call the contraction of ν along c and denote ν↓c, can be
read similarly as the previous diagrams of pairings, that is to say that
B(c, δ) = ∑
0=j1<j2<j3<j4<j5
x(ν(δ))↓c,
where xν↓c stands for the product of factors xb−a,{a < b} running over the bonds of
the contracted diagram ν↓c.
Given a contracted diagram ρ = ν↓c of length 𝓁(c), denote δ1(ρ) the number of
bonds opened between j1 and j2; δ2(ρ) the number of bonds opened between j2 and j3;
δ3(ρ) the number of bonds opened between j3 and j4; etc. up to δ𝓁(c)−1(ρ). For instance,
in the previous example, there is one bond opened between j1 and j2 (the one starting
from j1); 3 bonds opened between j2 and j3 (the previous bond, which has not been
closed, and the two bonds starting from j2); and 2 bonds opened between j3 and j4 and
between j4 and j5. So (δ1, δ2, δ3, δ4) = ( 1, 3, 2, 2).
Proposition 24. Set ρ = ( ν(δ))↓c. One has
B(c, δ) =
𝓁(c)−1
∏
i=1
xδi(ρ)
1− xδi(ρ) .
Example. Consider the previous contracted diagram ρ5, and the corresponding sum
B5 = ∑
0=j1<j2<j3<j4<j5
x(j5−j1)+(j5−j2)+(j3−j2).
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS45
We reduce inductively the size of the contracted diagram as follows. We ﬁrst write
B5 = ∑
0=j1<j2<j3<j4<j5
x2(j5−j4)+(j4−j1)+(j4−j2)+(j3−j2)
=
(
∑
0=j1<j2<j3<j4
x(j4−j1)+(j4−j2)+(j3−j2)
)(
∞
∑
j5=j4+1
x2(j5−j4)
)
= x2
1− x2
(
∑
0=j1<j2<j3<j4
x(j4−j1)+(j4−j2)+(j3−j2)
)
= xδ4
1− xδ4
B4,
where B4 is the sum corresponding to the diagram ρ4 which is obtained from ρ5 by
identifying j4 and j5:
j1 j2 j3 j4
20
FIGURE 20. Reduction of the diagram of Figure 19.
We can then do it again to go to size 3:
B4 = ∑
0=j1<j2<j3<j4
x2(j4−j3)+(j3−j1)+(j3−j2)+(j3−j2)
=
(
∑
0=j1<j2<j3
x(j3−j1)+2(j3−j2)
)(
∞
∑
j4=j3+1
x2(j4−j3)
)
= x2
1− x2
(
∑
0=j1<j2<j3
x(j3−j1)+2(j3−j2)
)
= xδ3
1− xδ3
B3,
where B3 is the sum corresponding to the diagram ρ3 which is obtained from ρ4 by
identifying j3 and j4:
j1 j2 j3
21
FIGURE 21. Further reduction of the diagram of Figure 19.
Two more operations yield similarly the factors xδ2
1−xδ2 and xδ1
1−xδ1 .
Proof of Proposition 24. The algorithm presented above on the example gives clearly a
proof of the formula by induction on 𝓁(c). Indeed, at each step of the induction, the
term that is factorized is
∞
∑
j𝓁(c)=j𝓁(c)−1+1
xδ𝓁(c)−1(j𝓁(c)−j𝓁(c)−1) = xδ𝓁(c)−1
1− xδ𝓁(c)−1
,
46 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
because δ𝓁(c)−1 is the number of bonds ending at j𝓁(c). Then, as for the other factor, one
obtains it by replacing j𝓁(c) by j𝓁(c)−1 in the sum B(c, δ), and this amounts to do the
identiﬁcation between j𝓁(c)−1 and j𝓁(c) in the contracted diagram. This identiﬁcation
and reduction to lower length does not change the valuesδ1, . . . ,δ𝓁(c)−2, so the formula
is proven. □
We recall that a descent of a composition c = (c1, . . . ,c𝓁) is one of the integers
c1, c1 + c2, c1 + c2 + c3, . . . ,c1 +··· + c𝓁−1.
For instance, the descents of c = (3, 2, 1, 2, 2) are 3, 5, 6 and 8. The set of descents D(c)
of a composition c of size r can be any subset of [ [1, r− 1] ], so in particular, card Cr =
2r−1. The contraction of diagrams along compositions presented at the beginning of
this paragraph satisﬁes the rule:
{δ1(ρ), . . . ,δ𝓁(c)−1(ρ)} ={δd, d∈ D(c)} if ρ = ( ν(δ))↓c .
So, B(c, δ) = ∏d∈D(c)
xδd
1−xδd , and Proposition 23 becomes:
Theorem 25. An upper bound, and in fact an estimate of|κ(2r)(Mn)| is
|κ(2r)(Mn)|
n ≤ ∑
c∈C2r
∑
δ∈D∗
2r
A(c) B(c, δ) C(δ)
with A(c) = (2r
c ), B(c, δ) = ∏d∈D(c)
xδd
1−xδd and C(δ) = ∏2r−1
i=1 δi.
Example. Suppose r = 2. There is one Dyck path inD∗
4, with C(δ) = 2 since δ1 = δ3 = 1
and δ2 = 2. The compositions of size 4 are (4), (3, 1), (2, 2), (1, 3), (2, 1, 1), (1, 2, 1),
(1, 1, 2) and (1, 1, 1, 1); their contributions A(c) B(c, δ) are equal to
1, 4x
1− x, 6x2
1− x2 , 4x
1− x, 12x3
(1− x)(1− x2), 12x2
(1− x)2 , 12x3
(1− x)(1− x2), 24x4
(1− x)2(1− x2).
So,
|κ(4)(Mn)|≃ 2n
(
1 + 8x
1− x + 6x2
1− x2 + 12x2
(1− x)2 + 24x3
(1− x)(1− x2) + 24x4
(1− x)2(1− x2)
)
≃ 2n (1 + x)(1 + 4x + x2)
(1− x)3 = n (3 e6β− e2β).
5.2.3. Explicit bound on cumulants and the mod-Gaussian convergence. By examining the
asymptotics of the ﬁrst cumulants written as rational functions in x, one is lead to the
following result. Set
Pr(x) =

 ∑
c∈C2r
∑
δ∈D∗
2r
A(c) B(c, δ) C(δ)

 (1− x)2r−1.
For instance, P1(x) = 1 + x and P2(x) = 2 (1 + x)(1 + 4x + x2).
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS47
Proposition 26. For every r≥ 1 and every x∈ (0, 1),
0≤ Pr(x)≤ (2r)!
r!
(2r− 2)!
(r− 1)! .
Proof. For every composition c and every path δ, B(c, δ) (1− x)2r−1 is a non-negative
and convex function of x on [0, 1]. Therefore, 0 ≤ Pr(x) ≤ x Pr(0) + ( 1− x) Pr(1).
When x = 1, all the rational functions B(c, δ) (1− x)2r−1 vanish, except when c has
2r− 1 descents, that is to say that c = (1, 1, . . . , 1). Then, A(c) = ( 2r)!, and
lim
x→1
B(c, δ) =
2r−1
∏
i=1
1
δi
= 1
C(δ).
Therefore,
Pr(1) = ( 2r)! (card D∗
2r) = (2r)!
r!
(2r− 2)!
(r− 1)! .
On the other hand, when x = 0, all the rational functions B(c, δ) (1− x)2r−1 vanish,
except when c has no descent, that is to say that c = (2r). Then, A(c) = 1 and
Pr(0) = Q(r) = ∑
δ∈D∗
2r
A(δ).
Among all Dyck paths in D∗
2r, the one with the maximal product of values G(δ) is
(0, 1, 2, . . . ,r− 1, r, r− 1, . . . , 2, 1, 0). So,
Pr(0)≤ r! (r− 1)! (card D∗
2r) = ( 2r− 2)!≤ Pr(1).
It follows that Pr(x)≤ x Pr(1) + (1− x) Pr(1) = Pr(1). □
Corollary 27. For every r,
|κ(2r)(Mn)|≤ n (2r− 1)!! (2r− 3)!! (e2β + 1)2r−1.
Proof. Indeed,
|κ(2r)(Mn)|≤ n

 ∑
c∈C2r
∑
δ∈D∗
2r
A(c) B(c, δ) C(δ)

 = n Pr(x)
(1− x)2r−1
≤ n Pr(1)
(1− x)2r−1 = n
( 1
1− x
)2r−1 (2r)!
r!
(2r− 2)!
(r− 1)! .
Replacing x by tanh β allows to conclude, and this gives another proof of Theorem 3.
We rewrite the logarithm of the Laplace transform of n−1/4Mn as
∞
∑
r=1
κ(2r)(Mn)
(2r)! z2r n−r/2 = κ(2)(Mn) z2
2n1/2 + κ(4)(Mn) z4
24n +
∞
∑
r=3
κ(2r)(Mn)
(2r)! z2r n−r/2.
48 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
The series on the right-hand side is smaller than
∞
∑
r=3
(2r− 1)!! (2r− 3)!!
(2r)! (eβ + 1)2r−1 z2r n1−r/2≤ n−1/2
∞
∑
r=3
((e2β + 1)z)2r n−(r−3)/2
≤ n−1/2 ((e2β + 1)z)6
1− ((e2β + 1)z)2 n−1/2 ,
so it goes uniformly to zero on every compact set of the plane. On the other hand, we
have seen that κ(2)(Mn) = n e2β− O(1) and−κ(4)(Mn) = n (3 e6β− e2β)− O(1), so we
conclude that
E
[
ez Mn
n1/4
]
e− n1/2e2β z2
2 = e− (3 e6β−e2β) z4
24
(
1 + O(n−1/2)
)
,
and this is indeed the content of Theorem 3. □
