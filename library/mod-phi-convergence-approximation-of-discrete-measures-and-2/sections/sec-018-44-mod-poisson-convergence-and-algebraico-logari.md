---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-018-44-mod-poisson-convergence-and-algebraico-logari
section_title: "Mod-Poisson convergence and algebraico-logarithmic singularities"
section_number: 4.4
pages: 48-56
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
singularities
The discussion of Section 4.3 can be extended to any statistic of a random
combinatorial object, whose double generating series admits a certain form
of singularity. Suppose given a combinatorial class, that is to say a sequence
C = (Cn)n∈N of ﬁnite sets. We write card Cn = |Cn|. In this paragraph, we
shall in particular study the following two examples, cf. [32, Section 5,
Example 2] and [30, p. 449 and p. 671]:
(1) Fn = F([[1, n]] , [[1, n]]) is the set of maps from the ﬁnite set [[1, n]] to
itself. It has cardinality nn.
(2) Pn = (Fq[t])n is the set of monic polynomials of degree n with
coeﬃcients in the ﬁnite ﬁeld Fq, where q = pe is some prime power.
It has cardinality qn.
This is mainly to ﬁx the ideas, and the techniques hereafter can be applied
to many other examples from the aforementioned sources. We consider
a statistic X : F
n∈N Cn →N, and we denote by Xn the random variable
TOME 70 (2020), FASCICULE 3
1162
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
obtained by evaluating X on an element of Cn chosen uniformly at random.
We introduce the bivariate generating function
F(z, w) =
∞
X
n=0
zn
n!
X
c∈Cn
wX(c) =
∞
X
n=0
zn (card Cn)
n!
E[wXn]
or F(z, w) =
∞
X
n=0
zn X
c∈Cn
wX(c) =
∞
X
n=0
zn (card Cn) E[wXn].
Suppose that for any w, F(z, w) is a complex analytic function on a domain
∆0(r(w), R(w), φ), and admits an algebraico-logarithmic singularity at z =
r(w), that writes as
F(z, w) = K(w)
 
1
1 −
z
r(w)
!α(w) 
log
1
1 −
z
r(w)
!β(w)
(1 + o(1)).
Then, the coeﬃcient cn(w) of zn in F(z, w) has for asymptotics:
cn(w) =
K(w)
Γ(α(w))(r(w))−n nα(w)−1(log n)β(w)

1 + O

1
log n

,
see [29]. Moreover, the O(
1
log n) is actually a O( 1
n) if β(w) = 0, or if α(w) =
0 and β(w) = 1; cf. [33]. If w stays in a suﬃciently small compact subset
of C, then one can take a uniform constant in the O( · ), which leads to an
asymptotic formula for the expectations E[wXn]:
E[wXn] = cn(w)
cn(1)
= K(w)
K(1)
Γ(α(1))
Γ(α(w))
 r(1)
r(w)
n
nα(w)−α(1) (log n)β(w)−β(1)

1 + O

1
log n

,
again with a smaller remainder O( 1
n) if β(w) = 0 for all w. In this para-
graph, we shall concentrate on this particular case; the case β(w)̸ = 0
is more commonly observed in probabilistic number theory, see our next
paragraph 4.5.
Example 4.4. — If f ∈Fn = F([[1, n]] , [[1, n]]), the functional graph cor-
responding to f is the directed graph G(f) with vertex set [[1, n]], and with
edges (k, f(k)), k ∈[[1, n]]. Since f is a map, G(f) is a disjoint union of
cycles on which trees are grafted, see [28] and Figure 4.2. We denote X(f)
the number of connected components of the functional graph G(f). This
generalizes the notion of cycle of a permutation. If T = (Tn)n∈N is the com-
binatorial class of unordered rooted labeled trees, recall that its generating
function T(z) = P∞
n=1
zn
n! |Tn| is the solution of T(z) = zeT (z), because a
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1163
rooted tree is constructed recursively by taking a node and connecting to
it a set of trees (also, Cayley’s theorem gives card Tn = nn−1).
1
3
4
7
5
8
6
2
Figure 4.2. The functional graph associated to the function f
:
[[1, 8]] →[[1, 8]] with word 38471814, here with one connected compo-
nent.
The class C = (Cn)n∈N of cycles on such trees has generating series
C(z) =
∞
X
n=0
zn
n! |Cn|
=
∞
X
n=0
X
k1+···+kr=n
|Tk1| |Tk2| · · · |Tkr|
r n!

n
k1, . . . , kr

zn
=
∞
X
r=1
1
r
X
k1,...,kr⩾1
|Tk1| · · · |Tkr|
(k1)! · · · (kr)! zk1+···+kr
=
∞
X
r=1
(T(z))r
r
= log

1
1 −T(z)

.
On the second line of this computation, the multinomial coeﬃcient comes
from the choice of the distribution of the integers of [[1, n]] into the r dif-
ferent trees, and the factor 1
r comes from the fact that r distinct cyclic
permutations of the choices yield the same cycle of trees. Finally, a func-
tional graph is a set of cycles of trees, so,
F(z) =
∞
X
n=0
zn
n! |Fn| = exp(C(z)) =
1
1 −T(z).
TOME 70 (2020), FASCICULE 3
1164
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Moreover, counting connected components of functional graphs amounts to
count a factor w for each cycle, hence,
F(z, w) =
∞
X
n=0
zn
n!
X
f∈Fn
wX(f) = exp(wC(z)) =

1
1 −T(z)
w
.
The generating series of rooted trees is classically known to have radius
of convergence
1
e, and a square-root type singularity at z =
1
e, see [28,
Formula (11)]:
T(z) = 1 −
p
2(1 −ez) + O(1 −ez).
Therefore,
F(z, w) = 2−w
2

1
1 −ez
 w
2
(1 + o(1)),
and the previous discussion applies with K(w) = 2−w
2 , α(w) =
w
2 and
β(w) = 0. Consequently,
E[wXn] = e
1
2 log n
2 (w−1) Γ( 1
2)
Γ( w
2 )

1 + O
 1
n

,
with a remainder that is uniform if w remains on the unit circle. We shall
next interpret this result as a mod-Poisson convergence, and deduce from
it the construction of approximation schemes.
Example 4.5. — If P ∈Pn = (Fq[t])n, then it writes uniquely as a prod-
uct of monic irreducible polynomials, each of these monic irreducible poly-
nomials appearing with a certain multiplicity. In terms of generating series,
introducing the combinatorial class I = (In)n∈N of monic irreducibles, this
can be rewritten as:
P(z) =
X
P ∈P
zdeg P =
Y
P ∈I
(1 + zdeg P + z2 deg P + · · · ) =
Y
P ∈I
1
1 −zdeg P
= exp
 X
P ∈I
log

1
1 −zdeg P
!
= exp
 ∞
X
k=1
X
P ∈I
zk deg P
k
!
= exp
 ∞
X
k=1
I(zk)
k
!
,
where P(z) = P
n⩾0 |Pn| zn and I(z) = P
n⩾1 |In| zn. Similarly, if Y (P)
and Z(P) are respectively the number of distinct irreducible factors and
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1165
the number of irreducible factors counted with multiplicity for P, then
PY (z, w) =
X
P ∈P
wY (P ) zdeg P =
Y
P ∈I
1 + (w −1)zdeg P
1 −zdeg P
= exp
 ∞
X
k=1
X
P ∈I
zk deg P
k
−((1 −w)zdeg P )k
k
!
= exp
 ∞
X
k=1
I(zk) (1 −(1 −w)k)
k
!
and
PZ(z, w) =
X
P ∈P
wZ(P ) zdeg P =
Y
P ∈I
1
1 −wzdeg P
= exp
 ∞
X
k=1
X
P ∈I
wkzk deg P
k
!
= exp
 ∞
X
k=1
wk I(zk)
k
!
.
Note that P(z) is simply equal to P∞
n=0 qnzn =
1
1−qz. On the other hand,
the number |In| of irreducible monic polynomials of degree n is given by
Gauss’ formula
|In| = 1
n
X
d|n
µ
n
d

qd,
as can be seen by gathering the elements of Fqn according to their irre-
ducible polynomials over Fq (here, µ is the arithmetic Möbius function).
Consequently,
I(z) =
X
n⩾1
|In| zn =
X
k⩾1
X
d⩾1
µ(k) qd zdk
dk
=
X
k⩾1
µ(k)
k
log

1
1 −qzk

.
We split I(z) into two parts: the ﬁrst term k = 1 and the remainder
R(z) =
X
k⩾2
µ(k)
k
log

1
1 −qzk

.
The remainder R(z) is an analytic function in z on the open disk of radius
q−1/2, whereas the ﬁrst term log
1
1−qz is analytic on the smaller open disk
TOME 70 (2020), FASCICULE 3
1166
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
of radius q−1. It follows that
PY (z, w) =

1
1 −qz
w
exp

wR(q−1) +
X
k⩾2
I(q−k) (1 −(1 −w)k)
k
+ o(1)


PZ(z, w) =

1
1 −qz
w
exp

wR(q−1) +
X
k⩾2
I(q−k) wk
k
+ o(1)


in the neighborhood of the singularity z = q−1. These algebraic singularities
with exponents α(w) = w and β(w) = 0 lead to the asymptotic formulas
E[wYn] = e(log n+R(q−1))(w−1)
Γ(w)
exp

X
k⩾2
(−1)k−1I(q−k)
k
(w −1)k + O
 1
n


E[wZn] = e(log n+R(q−1))(w−1)
Γ(w)
exp

X
k⩾2
I(q−k)
k
(wk −1) + O
 1
n

.
Thus, if a statistic X of a random combinatorial object has a double
generating series that admits an algebraico-logarithmic singularity, then
in many cases one can deduce from it the mod-Poisson convergence of
(Xn)n∈N. We restate hereafter the previous computations in this frame-
work. We note ϕ(D) the Euler function (number of integers in [[1, D]] that
are coprime with D), which satisﬁes the identity ϕ(D) = P
m|D µ(m) D
m; and
S(z) =
X
k⩾2
ϕ(k)
k
log

1
1 −qzk

,
which is analytic on the open disk of radius q−1/2.
Theorem 4.6. — Let Xn be the number of components of a random
map in F([[1, n]] , [[1, n]]), and Yn and Zn be the numbers of irreducible
factors of a random monic polynomial in (Fq[t])n∈N, counted respectively
without and with multiplicity. The sequences of random variables (Xn)n∈N,
(Yn)n∈N and (Zn)n∈N converge mod-Poisson with parameters
λX
n = 1
2 (log 2n + γ) ;
λY
n = log n + R(q−1) + γ;
λZ
n = log n + S(q−1) + γ.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1167
and limiting functions ψX/Y/Z(ξ) = P∞
k=0 ek(X/Y/Z) (eiξ −1)k, where the
parameters ek(X), ek(Y ) and ek(Z) correspond to the specialisations of Sym:
pk⩾2(X) =
X
n⩾1
1
(2n −1)k ;
p1(X) = 0 ;
pk⩾2(Y ) = ζ(k) + I(q−k) ;
p1(Y ) = 0 ;
pk⩾2(Z) = ζ(k) + (−1)k−1 X
n⩾1
|In|
(qn −1)k ;
p1(Z) = 0.
Moreover, in each case, one has ψn(ξ) −ψ(ξ) = O( 1
n) uniformly on the
cycle.
Proof. — Each time we set w = eiξ in the previous calculations, and we
also rewrite the residue so that it does not involve a power of w −1 equal
to 1.
(1) Number of connected components of a random map. One can write
the inﬁnite products
Γ( 1
2)
Γ( w
2 ) = e
γ
2 (w−1)
∞
Y
n=1
1 +
w
2 −1
n
1 −
1
2n
e−w−1
2n
= e
γ
2 (w−1)
∞
Y
n=1

1 + w −1
2n −1

e−w−1
2n
= e( γ
2 +log 2) (w−1)
∞
Y
n=1

1 + w −1
2n −1

e−w−1
2n−1
by using the identity P∞
n=1
1
2n−1 −
1
2n = log 2. In the last inﬁnite
product, one recognizes the same form as in Section 4.1, with pa-
rameters pj =
1
2j−1.
(2) Number of distinct irreducible factors of a random monic polyno-
mial. One rewrites the asymptotic formula for E[wYn]:
e(log n+R(q−1)+γ)(w−1)
 ∞
Y
n=1

1 + w −1
n

e−w−1
n
!
×

Y
k⩾2
(−1)k−1 I(q−k)
k
(w −1)k


= e(log n+R(q−1)+γ)(w−1)

Y
k⩾2
(−1)k−1 (w −1)k
k
 ∞
X
n=1
1
nk + I(q−k)
!
.
TOME 70 (2020), FASCICULE 3
1168
R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Again we recognize the formula
exp
 ∞
X
k=1
(−1)k−1(w −1)k
k
pk
!
=
∞
X
k=0
ek (w −1)k.
(3) Number of irreducible factors of a random monic polynomial, count-
ed with multiplicity. The factor Γ(w)−1 is dealt with exactly as in
the previous case. Therefore, we only have to deal with the term
exp(P
k⩾2
I(q−k)
k
(wk −1)). However,
X
k⩾2
I(q−k)
k
(wk −1)
=
X
k⩾2
k
X
l=1
I(q−k)
k
k
l

(w −1)l
=

X
k⩾2
I(q−k)

(w −1) +
∞
X
l=2

X
k⩾l
k
l
 I(q−k)
k

(w −1)l.
The coeﬃcient of (w −1) can be rewritten as follows:
X
k⩾2
I(q−k) =
X
k⩾2
m⩾1
µ(m)
m
log

1
1 −q1−km

=
X
D=km⩾2
log

1
1 −q1−D
 X
m|D
m̸=D
µ(m)
m
=
X
D⩾2
ϕ(D) −µ(D)
D
log

1
1 −q1−D

= S(q−1) −R(q−1).
On the other hand, if l ⩾2, then the coeﬃcient of (w −1)l rewrites
as
X
k⩾l
k
l
 I(q−k)
k
= 1
l
X
k⩾l
X
m⩾1
µ(m)
m
k −1
l −1

log

1
1 −q1−km

= 1
l
X
m,n⩾1
µ(m)
nm qn X
k⩾l
k −1
l −1

q−k(mn)
= 1
l
X
D⩾1
|ID|
(qD −1)l
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1169
by setting D = nm on the last line. We conclude that the Fourier
transform E[wZn] has asymptotics
e(log n+S(q−1)+γ)(w−1)
× exp


∞
X
l=2

(−1)l−1 ζ(l) +
X
D⩾1
|ID|
(qD −1)l

(w −1)l
l

,
and the term of degree 1 in (w −1) is separated from the other
terms.
□
From Theorem 4.6, one can easily construct approximation schemes of
the sequences (Xn)n∈N, (Yn)n∈N and (Zn)n∈N, which yield distances that
are arbitrary large negative powers of log n. For instance, suppose that
one wants to approximate the law of Yn by a signed measure νn, such
that dTV(µn, νn) = O(
1
(log n)2 ). By Theorem 3.11, we can take the derived
scheme of the approximation scheme of order r = 3, that is to say the
sequence of measures (σn)n∈N with Fourier transforms
c
σn(ξ) = e(log n+R(q−1)+γ)(eiξ−1)
×

1 −ζ(2) + I(q−2)
2
(eiξ −1)2 + ζ(3) + I(q−3)
3
(eiξ −1)3

.
One has in this situation
dTV(Xn, σn)
≃
1
(log n)2
(ζ(2) + I(q−2))2
8
+ ζ(4) + I(q−4)
4
 Z
R
|G4(α)| dα
√
2π

.
Remark 4.7. — A central limit theorem for the random variables Yn has
been proved by Rhoades in [51]. Our results immediately yield the speed
of convergence of this analogue on function ﬁelds of the Erdős–Kac central
limit theorem.
