---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-017-6-bounds-for-the-degree-and-coefficients-of-the
section_title: "Bounds for the degree and coefficients of the colored Jones function"
section_number: 6
pages: 14-16
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
6.1. Bounds for the degree. In this section we give a bound for the coeﬃcients of the colored Jon es
polynomial, and deduce Theorem 1.12. This and the next section are logically independent from the previou s
Sections 4 and 5.
For a Laurent polynomial f (q) =∑ M
k=m akqk, with amaM ⁄= 0, let us deﬁne deg +(f ) = M and deg −(f ) =
m. In [
Lˆ e06] the second author showed that there are quadratic bounds for the degrees of the colored Jones
polynomial.
Suppose the knot K has a planar projection with c + 2 crossings. Let ω be the writhe number, i.e. the
number of positive crossing minus the number of negative ones. The n by [ Lˆ e06, Proposition 2.1], taking into
account the change of variable, the framing, and the normalization , one has the following bounds for the
degrees of JK,n (q).
Proposition 6.1. With the above notations, there are constants s± such that
deg+(JK,n ) ≤ (c + 2)(n − 1)2 + 2(n − 1)(s+ − 1) − ω(n2 − 1)
4
deg−(JK,n ) ≥ − (c + 2)(n − 1)2 + 2(n − 1)(s− − 1) + ω(n2 − 1)
4 .
The constants s± have transparent geometric meaning, but we don’t need their exac t values here.
Another proof of the quadratic bounds, though less as explicit, fo r the degrees of the colored Jones
polynomial using the theory of q-holomorphic functions is given in Section 10.1.
6.2. Bounds for the coeﬃcients. For a Laurent polynomial f ∈ Z[q±1/ 4], we deﬁne ||f ||1 as in Deﬁnition
4.1, i.e. ||f ||1 is the sum of the absolute values of its coeﬃcients. Observe that
(21) ||f + g||1 ≤ ||f ||1 + ||g||1, ||f g||1 ≤ ||f ||1 ||g||1.
Since ||{j}||1 = 2, we have, for k ≤ n
(22) ||{a}k||1 =
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
a∏
j=a−k+1
{j}
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
1
≤ 2k ≤ 2n
It is known that the quantum binomial
[ m
k
]
is a Laurent polynomial in q1/ 2 with positive integer
coeﬃcients, hence its l1-norm is obtained by putting q1/ 2 = 1, which is the classical binomial
(m
k
)
. One has,
if m ≤ n,
(23)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
[ m
k
]⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
1
=
(m
k
)
≤ 2m ≤ 2n
Theorem 6.2. For every knot K of c + 2 crossings and every n we have:
(24) ||JK,n ||1 ≤ nc4cn.
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 15
Proof. The proof of the Theorem is easy using the state sum deﬁnition of th e colored Jones polynomial: The
colored Jones polynomial is the sum, over all states, of the weights of the states. There are nc states, the
weight of each is the product of several q-factorials and q-binomial coeﬃcients for which an upper bound
can be easily found. Let us now go to the details of the proof.
The knot K is the closure of a (1 , 1)-tangle T (or long knot), with orientation given by the direction from
the bottom boundary point to the top boundary point. The crossin g points of the diagram of T (on the
standard 2-plane) break T into 2 c + 5 arcs, two of which are boundary (i.e. each contains a boundary point
of T ). The two crossings adjacent to the boundary arcs are called boundary crossings.
To get from c + 2 to c in the estimate, we will choose the (1 , 1)-tangle T such that (1) when going along
T , starting at the bottom boundary point, we must pass the very ﬁr st crossing (resp. very last crossing) by
an overpass (respectively, an underpass) and (2) the two stran ds at each crossing are pointing upwards, as
in the following ﬁgure:
(25)
a
b+k a−k
b
k
b
a+kb−k
a
k
Here is how to get such a (1 , 1)-tangle T . Consider a diagram of K on a 2-sphere S2. The c + 2 crossings
break the knot diagram into 2 c + 4 arcs. At each crossing we have an overpass and an underpass. When
we go along the knot starting at some point, following the direction of the orientation, we pass through all
these underpasses and overpasses. Hence there must be an arc which starts at an underpass and ends at an
overpass, assuming there is at leat one crossing. Remove from S2 a small disk which is a small neighborhood
of a point inside this arc. What is left is a long knot diagram on a disk, whic h can also be considered as a
(1, 1)-tangle diagram in the strip R × [0, 1] in the standard 2-plane which satisﬁes requirement (1). Using
the isotopy of the form
which moves crossings (positive or negative) into standard upright position, we get the desired (1 , 1)-tangle.
A state k is an assignment of numbers, called the colors, to the crossings of t he diagram of T , where each
color is in {0, . . . , n− 1}. For a ﬁxed state we will color the 2 c + 5 arcs as follow. First color the bottom
boundary arc by 0. Going along the diagram of T from the bottom boundary point, if we are on an arc of
color a and pass a crossing, the next arc will have color a + k or a − k, according as the pass is an underpass
or an overpass, see ( 25). Here k is the color of the crossing.
We will only consider states such that the colors of arcs are betwee n 0 and n − 1 and the color of the
top boundary arc is 0. The under/overpass conﬁguration at the t wo boundary crossings ensures that the
two boundary crossings have color 0, otherwise the arcs next to t he two boundary arcs would have negative
colors. It follows that the number of states is at most nc.
The weights of the positive crossing (on the left) and negative cros sing (on the right in ( 25)) are
R+(n; a, b, k) = (unit)
[ b + k
k
]
{n − 1 + k − a}k,(26)
R−(n; a, b, k) = (unit)
[
a + k
k
]
{n − 1 + k − b}k,(27)
where (unit) stands for ± a power of q±1/ 4, which does not aﬀect the l1 norm. Note that both a + k and
b + k in the above formulas are between 0 and n − 1.
The weight of a maximum/minimum point is a also ± a power of q±1/ 4, whose exact formula is not
important for us. Let F (n, k) denote the product of weights of all the crossings and all the ext reme points.
Then
16 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
(28) JK,n (q) =
∑
k
F (n, k).
Using the estimates ( 23) and ( 22), we see that ||R±(n; a, b, k)||1 ≤ 4n. Since the weight of the two
boundary crossing is just a unit, the l1 norm of F (n, k) is less than 4 cn. From ( 28) and the fact that there
are nc states, we get ||JK,n ||1 ≤ nc4cn. □
Since there is a constant b such that nc ≤ bn, we have the following.
Theorem 6.3. For every knot K, there is a constant A6 such that for every positive integer n,
||JK,n ||1 ≤ (A6)n.
