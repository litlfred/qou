---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-003-31-the-universal-diagram-and-automodel
section_title: "The Universal Diagram and Automodel"
section_number: 3.1
pages: 10-12
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
Although we are using the “English” notation for Young diagrams, but the limit shape of Young
diagrams takes a simple form in rotated French notation. A typical shape of Young diagram in
French notation is given in ﬁg. 2. The centres of boxes are marked with ( X, Y) coordinates. The
function X(Y) speciﬁes a particular shape of Young diagram in this notation. However, it is more
X
Y
Figure 2: Typical structure of a Young diagram in French notation.
convenient to rotate this diagram anti-clock wise by π/4 and work in the redeﬁned coordinates
u = 1
2(Y− X) v = 1
2(Y + X). (3.9)
A Young diagram in this notation 4 is depicted in ﬁgure 3. Note that here the coordinate u is
4There is another advantage to draw the Young diagrams in rotated French notation. A transition from λk toλk+1
occurs when one keeps a box at any of the minima of rotated diagram. Putting a box at diﬀerent minima corresponds
to diﬀerent diagrams at k + 1 level. Therefore the transition probabilities are denoted by µa where a is the position of
a minimum. To ﬁnd µa we deﬁne two polynomials P(x) = ∏n
a=1(x− xa) and Q(x) = ∏n−1
a=1(x− ya), where x1,··· , xn
are positions of consecutive minima and y1,··· , yn−1 are consecutive maxima. The transition probability from λk to
λk+1 by adding a box at ath minima is given by decomposing the quotient into partial fraction
n∑
a=1
µa
x− xa
= Q(x)
P(x). (3.10)
10
X
Y
Figure 3: Typical structure of a 45◦ anti-clockwise rotated Young diagram.
diﬀerent than the Young diagram density deﬁned in (5.10). For a ﬁnite number of boxes the
function v(u) is rough and zig-zag i.e. v′(u) =±1. As the number of boxes goes very large we
deﬁne a rescaled function
ˆvk(u) = v(u
√
k)√
k
(3.11)
such that the area under the curve is ﬁnite and the boundary curve becomes smooth. It was ob-
served by [3, 4] that when the growth process follows Plancherel transition probability (1.1) the
asymptotic shape of rescaled Young diagrams converges uniformly to a unique curve given by
lim
k→∞
ˆvk(u)≡ Ω(u) =

2
π(u sin−1 u
2 +
√
4− u2) if |u|≤ 2
|u| if |u|> 2. (3.12)
In the continuum limit Kerov introduced [5] charge of a diagram, denoted byσ(u) and is given by
(we are using the notation that ˆv(u) = ˆvk(u) in the large k limit)
σ(u) = 1
2 (ˆv(u)−| u|). (3.13)
Therefore,
σ′(u) =
{ 1
2 + ˆv′(u)
2 for u< 0
− 1
2 + ˆv′(u)
2 for u> 0
. (3.14)
One can deﬁne moments of a diagram
pn =−n
∫
un−1dσ(u) (3.15)
such that area of a diagram (area covered under the curve ˆv(h)) is given by A = (p2− p2
1)/2. It is
convenient to consider a moment generating function
S (x) =
∞∑
n=1
pn
n x−n =
∫ dσ(u)
u− x. (3.16)
11
The moment generating function as well as the sequence of moments determine the charge and
hence the diagram (ˆv(u)) completely. The moment generating function plays an important role in
our large k analysis of partition function.
In [5] Kerov introduced a dynamical model for the growth of Young diagrams. For every contin-
uous Young diagram characterized by the function ˆv(u), one can deﬁne the function v(u, t), called
the automodel tableaux which depends on two variables u and t as
ˆv(u, t) =
√
t ˆv(u/
√
t) for t> 0. (3.17)
Kerov showed that the Young diagrams, following Plancherel growth, belong to automodel class
and satisfy the equation
∂tˆv(u, t) = 1
2t(ˆv(u, t)− u∂uˆv(u, t)). (3.18)
In terms of charges the automodel equation is given by,
∂tσ′(u, t) + u
2tσ
′′
(u, t) = 0. (3.19)
