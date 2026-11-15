---
doc_id: arxiv-math-0203160v3
doc_title: "arXiv:math/0203160v3 [math.QA] 28 Oct 2002"
section_id: sec-003-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 8-13
source_pdf: 0203160v3.pdf
source_sha256: a84f478d72d40af2
toc_source: inferred
---
We would like to thank Yu. Manin for his interest in our work, and for informa-
tion that our results could be useful in number theory (Yu. Manin has explained
the relation of our results to number theory in his recent preprint [11]). One of
authors (A. Sch.) appreciates the hospitality of IHES and ESI where a part of
this work was done.
References
[1] A. Connes. C∗–alg`ebres et g´eom´etrie diﬀ´erentielle. C. R. Acad. Sci. Paris,
290:599–604, 1980.
[2] A. Connes. Noncommutative Geometry. Academic Press, 1994.
[3] A. Connes and M. Rieﬀel. Yang–Mills for noncommutative two–tori. Con-
temporary Math., 66:237–266, 1987.
8
[4] A. Connes, M. Douglas, and A. Schwarz. Noncommutative geometry and
matrix theory: Compactiﬁcation on tori. J. High Energy Phys., (2), 1998.
[5] A. Konechny and A. Schwarz. BPS states on noncommutative tori and
duality. Nucl. Phys., B(550):561–584, 1999.
[6] A. Konechny and A. Schwarz. Moduli spaces of maximally supersymmetric
solutions on noncommutative tori and noncommutative orbifolds. JHEP,
09:1–23, 2000.
[7] A. Konechny and A. Schwarz. Introduction to M(atrix) theory and non-
commutative geometry. arXiv:hep-th/0012145.
[8] Yu. Manin. Quantized theta–functions, volume 102. Common trends in
Mathematics and Quantum Field Theories, 1990.
[9] Yu. Manin.
Mirror symmetry and quantization of abelian varieties.
arXiv:math.AG/0005143.
[10] Yu. Manin. Theta functions, quantum tori and Heisenberg groups. Lett.
Math. Phys., 56, June 2001.
[11] Yu.
Manin.
Real
multiplication
and
noncommutative
geometry.
arXiv:math.AG/0202109.
[12] D. Mumford. Tata Lectures on Theta I. Birkh¨auser, 1983.
[13] D. Mumford. Tata Lectures on Theta III (with M. Nori and P. Norman).
Birkh¨auser, 1991.
[14] M. Rieﬀel. Projective modules over higher–dimensional noncommutative
tori. Can. J. Math., XL(2):257–338, 1988.
[15] M. Rieﬀel and A. Schwarz. Morita equivalence of multidimensional non-
commutative tori. Intl. J. of Math., 10(2):289–299, 1999.
[16] A. Schwarz. Gauge theories on noncommutative spaces. ICMP lecture,
arXiv:hep–th/0011261.
[17] A. Schwarz. Morita equivalence and duality. Nucl. Phys., B(534):720–738,
1998.
[18] A. Schwarz. Theta–functions on noncommutative tori. Lett. Math. Phys.,
58(1):81–90, 2001.
9
4
Appendix
Our candidate function h(z, ∆) for the map (1) is given by :
h(z, ∆) =
X
q∈Z

f((n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)∆, −q + a ∆)
·g((n + m θ)z + k −l θ
l
q −
k −l θ
n l + m k ∆, q)

For reference, let us recall all the actions we will need. If f(x, µ) ∈En,m(θ),
and g(y, ν) ∈E′
k,l(θ), then:
U1 f(x, µ) = f(x −n + m θ
m
, µ −1)
U2 f(x, µ) = e2 π i(x−µ n/m) f(x, µ)
U1 g(y, ν) = g(y −k −l θ
l
, ν −1)
U2 g(y, ν) = e2 π i(y−ν k/l) g(y, ν)
Z1 f(x, µ) = f(x −1
m, µ −a)
Z2 f(x, µ) = e2 π i(x/(n+m θ)−µ/m) f(x, µ)
Let us start by checking the identiﬁcations. Replacing f with U1 f in the deﬁ-
nition of h we obtain:
X
q∈Z

f((n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)∆−n + m θ
m
, −q + a ∆−1)
·g((n + m θ)z + k −l θ
l
q −
k −l θ
n l + m k∆, q)

Letting q →q −1 gives:
=
X
q∈Z

f((n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)∆, −q + a ∆)
·g((n + m θ)z + k −l θ
l
q −
k −l θ
n l + m k∆−k −l θ
l
, q −1)

This means that the map (1) is compatible with the identiﬁcation
(U1 f) ⊗g ∼f ⊗(U1 g)
Similarly, replacing f with U2 f in (1) we get:
10
X
q∈Z
exp

2 π i

(n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)∆−n(−q + a ∆)
m

f · g
=
X
q∈Z
exp

2 π i

(n + m θ)z −θ q +
l(n + m θ)
m(n l + m k)∆−a n ∆
m

f · g
using the relation a n = 1 + b m gives:
=
X
q∈Z
exp

2 π i

(n + m θ)z + k −l θ
l
q +
k −l θ
n l + m k ∆−k
l q

f · g
This means that the map (1) is compatible with the identiﬁcation
(U2 f) ⊗g ∼f ⊗(U2 g)
So the map (1) that was deﬁned originally as a map of the tensor product
En,m ⊗C E′
k,l descends to a map of En,m ⊗Tθ E′
k,l.
Next, we need to check that the new product module is in fact E′
a k+b l,n l+m k(θ′).
That is, we ﬁrst need to show that the shift ∆→∆+ n l + m k leaves h(z, ∆)
invariant; therefore we can consider ∆as an element of Zn l+m k:
h(z, ∆+ n l + m k) =
X
q∈Z

f((n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)(∆+ n l + m k), −q + a (∆+ n l + m k))
·g((n + m θ)z + k −l θ
l
q −
k −l θ
n l + m k(∆+ n l + m k), q)

Let q →q + l. Then the extra terms in the ﬁrst argument of f are:
−n + m θ
m
l +
l(n + m θ)
m(n l + m k)(n l + m k) = 0
The extra terms in the second argument of f are:
−l + a n l + a m k ≡−l −a n l
(mod m)
≡l (a n −1)
(mod m)
≡l b m
(mod m)
≡0
(mod m)
Similarly, the extra terms in the arguments of g are respectively:
11
(k −l θ) −(k −l θ) = 0
and
l ≡0
(mod l)
It follows that:
h(z, ∆+ n l + m k) = h(z, ∆)
as required. Finally we need to check that the action of the endomorphism
algebra generators Z1, Z2 on h(z, ∆) induced by the action of Z1 and Z2 on f
describe the standard module E′
a k+b l,n l+m k(θ′):
Z1 h(z, ∆)
=
X
q∈Z

f((n + m θ)z −n + m θ
m
q +
l(n + m θ)
m(n l + m k)∆−1
m, −q + a ∆−a)
·g((n + m θ)z + k −l θ
l
q −
k −l θ
n l + m k∆, q)

=
X
q∈Z

f((n + m θ) (z + α) −n + m θ
m
q +
l(n + m θ)
m(n l + m k)(∆−1), −q + a (∆−1))
·g((n + m θ)(z + β) + k −l θ
l
q −
k −l θ
n l + m k (∆−1), q)

where
α =
1
n + m θ
 l(n + m θ)
m(n l + m k) −1
m

= −
k −l θ
(n + m θ)(n l + m k)
= β
and can be rewritten in a simpler way using the relation a n −b m = 1:
= −a k + b l
n l + m k + b + a θ
n + m θ
= −a k + b l
n l + m k + ˆθ
Therefore:
Z1 h(z, ∆) = Z1 h(z −a k + b l
n l + m k + ˆθ, ∆−1)
12
as required for E′
a k+b l,n l+m k(θ′). Similarly:
Z2 h(z, ∆)
=
X
q∈Z
exp

2 π i

z −q
m +
l
m(n l + m k)∆−1
m(−q + a ∆)

f · g
=
X
q∈Z
exp

2 π i

z + l(1 −a n) −a m k
m(n l + m k)
∆

f · g
substituting −b m in for 1 −a n gives:
=
X
q∈Z
exp

2 π i

z −a k + b l
n l + m k∆

f · g
= exp

2 π i

z −a k + b l
n l + m k∆

h(z, ∆)
also as required.
Our considerations prove that the formula (1) speciﬁes a map from En,m(θ)⊗
Tθ
E′
k,l(θ) into E′
a,k+b l,n l+m k(θ′) and this map is compatible with the structure
of Tθ′ right modules on these objects. It is easy to check that this map is an
isomorphism (either directly or using the general result about tensor products
of modules over noncommutative tori).
One can use also the technique suggested in [17]; the latter approach has the
advantage that it gives a regular way to obtain (1). Namely we can start with
the description of the linear space that is dual to the tensor product En,m(θ) ⊗
Tθ
E′
k,l(θ). We notice that a continuous linear functional on the tensor product of
En,m(θ) and E′
k,l(θ) over C is speciﬁed by a generalized function (a distribution)
ϕ(x, µ, y, ν) where x, y ∈R, µ ∈Zm, ν ∈Zl; it transforms f ⊗g into:
X
µ∈Zm
X
ν∈Zl
Z
f(x, µ) g(y, ν) ϕ(x, µ, y, ν) d x d y
This functional descends to the tensor product over Tθ if:
ϕ(x, µ, y, ν) · e2 π i(x−µ n/m) = ϕ(x, µ, y, ν) · e2 π i(y−ν k/l)
and
ϕ(x + n
m + θ, µ + 1, y, ν) = ϕ(x, µ, y + k
l −θ, ν + 1)
Solving this system of equations for ϕ, we arrive at a description of the space
that is dual to the tensor product we are interested in. Using this description,
it is easy to obtain (1).
13
