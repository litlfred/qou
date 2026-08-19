---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-005-112-hypothesis-approximate-factorization-of-char
section_title: "Hypothesis: approximate factorization of characters"
section_number: 1.12
pages: 6-9
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
lowing we will use the following convention. If χn : Pn → R is a function
on the set of partitions of n, we will extend its domain to the set
P≤n :=
⨆
0≤k≤n
Pk
of partitions of smaller numbers by setting
(1.10) χn(π) := χn(π, 1n−|π|) for |π| ≤ n,
i.e. we extend the partition π by adding an appropriate number of parts, each
equal to 1.
In this way the cumulant kχn
ℓ (l1, . . . , lℓ) is well deﬁned if n ≥ l1 + · · ·+ lℓ
is large enough.
Deﬁnition 1.1. Assume that for each integer n ≥ 1 we are given a function
χn : Pn → R. We say that the sequence (χn) has approximate factorization
property [ ´Sni06] if for each integer ℓ ≥ 1 and all integers l1, . . . , lℓ ≥ 2 the
limit
(1.11) lim
n→∞
kχn
ℓ (l1, . . . , lℓ) n
l1+···+lℓ+ℓ−2
2
exists and is ﬁnite.
We say that the sequence (χn) has enhanced approximate factorization
property if, additionally, in the case ℓ = 1 the rate of convergence in (1.11)
takes the following explicit form: for each l ≥ 2 there exist some constants
al+1, bl+1 ∈ R such that
(1.12) kχn
1 (l) n
l−1
2 = χn(l) n
l−1
2 = al+1 + bl+1 + o(1)√n for n → ∞
and
(1.13) sup
l≥2
l
√
|al|
lm < ∞, where m =
{
2 for g ⁄= 0,
1 for g = 0,
where g is given by (1.9).
Example 1.2. It is easy to check that for χreg from (1.3) all higher cumulants
vanish:
kχreg
ℓ (l1, . . . , lℓ) = 0 for ℓ ≥ 2
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 7
x
1 2 3 4 5
y
1
2
3
4
5
x
1 2 3
y
1
2
3
4
5
FIGURE 1. A Y oung diagram λ = (4 , 3, 1) shown in the
French convention (left) and a generalized Y oung diagram
T 1
2 , 3
2
λ (right) obtained by an anisotropic scaling. The dashed
lines indicate individual boxes.
and the ﬁrst cumulant takes a particularly simple form
kχreg
1 (l) = χreg(l) =
{
1 if l = 1,
0 otherwise.
It follows that that the sequence (χn) for which χn := χreg fulﬁlls the
enhanced approximate factorization property.
1.13. Drawing Y oung diagrams.
1.13.1. Anisotropic Young diagrams. The usual way of drawing Y oung di-
agrams is to represent each individual box as a unit square, s ee Figure 1
(left). However, when dealing with random Y oung diagrams related to Jack
polynomials it is more convenient to represent each box as a r ectangle with
width w > 0 and height h > 0 such that
(1.14) w
h = α.
A Y oung diagram viewed like this becomes a polygon contained in the
uppper-right quaterplane which will be denoted by Tw,hλ, see Figure 1
(right). We will refer to such polygons as anisotropic Young diagrams; they
have been ﬁrst considered by Kerov [Ker00].
1.13.2. Russian convention. Proﬁle of a Young diagram. We draw (aniso-
tropic) Y oung diagrams on the plane with the usual Cartesian coordinates
8 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
u
−3−2−1
1
2
3
v
1
2
3
4
5
6
x
1 2 3
y
1
2
3
4
5
u
−5 −4 −3 −2 −1 1 2 3
v
1
2
3
4
5
x
1
2
3
y
1
2
3
4
FIGURE 2. The anisotropic Y oung diagram from Figure 1
shown in the French and Russian conventions. The solid
line represents the proﬁle of the Y oung diagram. The coor-
dinate system (u, v) corresponding to the Russian conven-
tion and the coordinate system (x, y) corresponding to the
French convention are shown.
(x, y). However, it is also convenient to use the Russian coordinate system
(u, v) given by
u = x − y, v = x + y.
This new coordinate system gives rise to theRussian convention for drawing
(anisotropic) Y oung diagrams, see Figure 2.
The boundary of a Y oung diagram λ drawn in the Russian convention
(the solid zigzag line on the right-hand side of Figure 2) is a graph of a
function ωλ which will be called the proﬁle of λ. If the Y oung diagram is
replaced by an anisotropic Y oung diagram Tw,hλ we deﬁne in an analogous
way its proﬁle ωTw,hλ.
1.14. The ﬁrst main result: Law of Large Numbers. The following the-
orem is a generalization of the results of Biane [Bia01] who c onsidered the
special case α = 1 and the corresponding representations of the symmetric
groups.
Theorem 1.3 (Law of large numbers) . Assume that α = α(n) is such that
(1.9) holds true. Assume that χn : Pn → R is a reducible Jack character;
we denote by λn the corresponding random Young diagram with n boxes
distributed according to P(α)
χn . We assume also that the sequence (χn) of
characters fulﬁlls the enhanced approximate factorizatio n property.
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 9
Then there exists some deterministic function ωΛ ∞ : R → R with the
property that
(1.15) lim
n→∞
ωΛ n = ωΛ ∞,
where
(1.16) Λ n := T√
α
n ,
√ 1
αn
λn
and the convergence in (1.15) holds true with respect to the supremum
norm, in probability. In other words, for each ǫ > 0
lim
n→∞
P
(
‖ωΛ n − ωΛ ∞‖∞ > ǫ
)
= 0.
Remark 1.4. The concrete formula for the proﬁle ωΛ ∞ may be obtained by
computing the corresponding R-transform and Cauchy transform, see for
