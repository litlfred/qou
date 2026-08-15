---
doc_id: 1172-5
doc_title: "OPTIMISTIC CALCULATIONS ABOUT THE $\mathrm{W}\mathrm{I}\mathrm{T}\mathrm{T}\mathrm{E}\mathrm{N}-\mathrm{R}\mathrm{E}\mathrm{s}\mathrm{H}\mathrm{E}\mathrm{T}\mathrm{I}\mathrm{K}\mat"
section_id: sec-000-1-introduction
section_title: "INTRODUCTION"
section_number: 1
pages: 1-3
source_pdf: 1172-5.pdf
source_sha256: 21b7a0e13bd208fc
doc_brief: "OPTIMISTIC CALCULATIONS ABOUT THE $\mathrm{W}\mathrm{I}\mathrm{T}\mathrm{T}\mathrm{E}\mathrm{N}-\mathrm{R}\mathrm{E}\mathrm{s}\mathrm{H}\mathrm{E}\mathrm{T}\mathrm{I}\mathrm{K}\mathrm{H}\mathrm{I}\mat"
---
In [2] R. Kashaev deﬁned a link invariant by using quantum dilogarithm and
conﬁrmed that his invariants grow exponentially with the growth rates the hyper-
bolic volumes (times a constant) for three hyperbolic knots with small numbers of
crossings. He also conjectured that this holds for every hyperbolic knot.
J. Murakami and I proved that Kashaev’s link invariant is essentially (up to
normalization) the same as the Jones polynomial colored with $N$-dimensional rep-
resentation evaluated at the N-th root of unity. Moreover we generalized Kashaev’s
conjecture to the following conjecture.
Conjecture 1.1 (Volume Conjecture, [9]). Let $J_{N}(K)$be the $N$-colored Jones
polynomial of a knot $K$evaluated at $\exp(\frac{2\pi\sqrt{-1}}{N})$. Then
$\lim_{Narrow\infty}\frac{\log|J_{N}(I\mathrm{f})|}{N}=\frac{v_{3}}{2\pi}||K||$,
where $||K||$is the Gromov norm (or the simplicial volume) of the complement of $K$
and $v_{3}$is the hyperbolic volume of the regular ideal tetrahedron.
Recent developments toward the Volume Conjecture can be found in [3, 14, 13,
8, 10].
It is natural to ask whether a similar formula holds for closed three-manifolds re-
placing the colored Jones polynomial with the $\mathrm{W}\mathrm{i}\mathrm{t}\mathrm{t}\mathrm{e}\mathrm{n}^{-}\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{h}\mathrm{e}\mathrm{t}\mathrm{i}\mathrm{k}\mathrm{h}\mathrm{i}\mathrm{n}$-Turaev $SU(2)$
invariant associated with the N-th root of unity. But an argument using Heegaard
splitting and Topological Quantum Field Theory tells us that the growth of the
WRT invariant is a polynomial, showing that a similar limit in the Volume Con-
jecture vanishes. (After the ﬁrst attempt of this work I learned this argument from
D. Thurston and J. Roberts; it was also pointed out by S. Garoufalidis, V. Turaev
and K. Walker independently.)
Date: 31 May, 2000.
2000 MathematicsSubject Classiﬁcation.Primary $57\mathrm{M}27$; Secondary$57\mathrm{M}25,57\mathrm{M}50,17\mathrm{B}37$,
$81\mathrm{R}50$.
?tM}2r@O8&5f=j9V5fO?
1172 4,2000 G/70-79 70
The aim of this article is to be optimistic to calculate (fake) limits of the loga-
rithms of the WRT invariants of closed three-manifolds obtained from the ﬁgure-
eight knot by Dehn surgeries with integral coeﬃcients. I will follow Kashaev’s
calculation in [2] formally and optimistically, and deduce an analytic function with
integer parameter corresponding to the surgery coeﬃcient. The function turns out
to describe not only the (simplicial) volume but also the Chern-Simons invariant of
the manifold. (J. Murakami told me to look at the Chern-Simons invariants after
my earlier calculations. See [10] for a similar relation between the Chern-Simons
invariants and the colored Jones polynomials for knots and links.)
I do not know what these optimistic calculations mean. But this is not a coin-
cidence and there should be something behind it!
Acknowledgments. This article is for the proceedings of the workshop ‘Recent
Progress toward the Volume Conjecture’ held at the International Institute for Ad-
vanced Study from 14th to 17th March, 2000 (http: $//\mathrm{w}\mathrm{w}\mathrm{w}.\ddot{\mathrm{u}}\mathrm{a}\mathrm{s}.\mathrm{o}\mathrm{r}.\mathrm{j}\mathrm{P}/\mathrm{r}\mathrm{e}\mathrm{s}\mathrm{e}\mathrm{a}\mathrm{r}\mathrm{c}\mathrm{h}/\mathrm{s}\mathrm{u}\mathrm{u}\mathrm{k}\mathrm{e}\mathrm{n}/$
$200\mathrm{o}\mathrm{o}314\mathrm{e}\mathrm{n}\mathrm{g}.\mathrm{h}\mathrm{t}\mathrm{m}\mathrm{l})$, supported by the Research Institute of Mathematical Sciences,
Kyoto University. I thank the IIAS for its hospitality and the RIMS for its ﬁnancial
support.
I am grateful to K. Saito, who encouraged me to organize the workshop.
Thanks are also due to the participants of the workshop, and to K. Ichihara,
K. Motegi, J. Murakami, J. Roberts, M. Teragaito, D. Thurston and Y. Yokota for
their helpful comments.
2. THE $\mathrm{w}\mathrm{I}\mathrm{T}\mathrm{T}\mathrm{E}\mathrm{N}^{-\mathrm{R}\mathrm{N}}\mathrm{E}\mathrm{S}\mathrm{H}\mathrm{E}\mathrm{T}\mathrm{I}\mathrm{K}\mathrm{H}\mathrm{I}$-TURAEV INV ARIANT
Let $J_{n}(K;t)$be the colored Jones polynomial of a knot $K$associated with the n-
dimensional representation of the Lie algebra $sl_{2}(\mathbb{C})$. We normalize $J_{n}(K;t)$so that
$tn/2-t^{-}n/2$
$J_{2}(K;t)$is the Jones polynomial and $J_{n}(O;t)=\overline{t^{1/2}-t-1/2}$with $O$the unknot.
Due to T. Le the colored Jones polynomial of the ﬁgure-eight knot $4_{1}$is
$J_{n}(4_{1} ; t)=m=n-1 \sum_{0l}\prod_{1=}m(t(n+\iota)/2-t-(n+l)/2)(t^{(n-l)/2}-t-(n-\iota)/2)$.
(K. Habiro obtained the same formula by a diﬀerent technique.) Let $M_{p}$be the
closed three-manifold obtained from $S^{3}$by Dehn surgery along the ﬁgure-eight
knot with coeﬃcient $p\in \mathbb{Z}$. We denote by $\tau_{N}(M_{\mathrm{p}})$the $\mathrm{W}\mathrm{i}\mathrm{t}\mathrm{t}\mathrm{e}\mathrm{n}^{-}\mathrm{R}\mathrm{e}\mathrm{s}\mathrm{h}\mathrm{e}\mathrm{t}\mathrm{i}\mathrm{k}\mathrm{h}\mathrm{i}\mathrm{n}$-Turaev
invariant of $M_{p}$associated with the Lie group $sl_{2}(\mathbb{C})$and with level $N-2$ . Then
from [5, (1.9)],
(2.1) $\tau_{N}(M_{p})=\sqrt{\frac{2}{N}}\sin\frac{\pi}{N}\exp(\frac{-3\pi\sqrt{-1}}{4})q^{(p)}-/4\sum_{n=}^{N}3[n]^{2}qJ_{n}pn^{2}/4(4_{1}-11)$; $q$
if $p>0$ . Here $q=\exp(\frac{2\pi\sqrt{-1}}{N})$and $[n]=\frac{q-n/2q^{-}/n2}{q^{1/2}-q^{-}1/2}$. Note that our $J_{n}(K;q)$
is $[n]J_{Kn}\mathrm{o}$, with the notation in [5]. Since
$[n]\prod_{1\iota=}^{m}(q-q^{-(n+)}(n+l)/2\iota/2)(q^{(\iota)/}n-2-q-(n-\iota)/2)$
$=\frac{\prod_{t=}^{m}-m(q^{(}n+l)/2-q^{-}(n+\iota)/2)}{q/2-1q^{-}1/2}$
$=\frac{(1-q^{n-m})(1-q)n-m+1\ldots(1-q)n+m\cross(-1)q^{-n}(2m+1)/2}{q^{1/2}-q^{-}1/2}$
71
$=\frac{-q^{-n()}2m+1/2}{q-1/2q-1/2}\cross\frac{(q)_{n+m}}{(q)n-m-1}$
we have
$\tau_{N}(M_{p})=P(N)N-1n\sum=1mn\sum_{=0}-1\frac{(q)_{n}(q)_{n+m}}{(q)_{n}-1(q)_{n-}m-1}q^{n(}-m-n)pn/4)$
where $(q)_{k}=(1-q)(1-q^{2})\cdots(1-q^{k})$and $P(N)$is a function of $N$with polynomial
growth. Note that this also holds for a non-positive $p$.
