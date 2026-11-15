---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-003-4-cayley-algebras
section_title: "Cayley algebras"
section_number: 4
pages: 15-19
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
will see in the next section.
Finally, for completeness, we include a slight generalisation of Proposition 3.7.
Proposition 3.9 Let kF G be an algebra that admits a strong diagonal involution σ(x) = s(x)x.
Then the non degenerate form n(x) = x · σ(x) makes kF G a composition algebra if and only if
i) s(xy)F(x, y)2F(xy, xy) = s(x)s(y)F(x, x)F(y, y), for all x, y ∈G.
ii) F(x, xz)F(y, yz)F(z, z)s(z) + F(x, yz)F(y, xz)F(xyz, xyz)s(xyz) = 0, for all x, y ∈G
with x̸ = y.
Proof
Let A be a quasialgebra kF G that admits a strong diagonal involution σ(x) = s(x)x
and let us consider the form n(x) = xσ(x). For all x, y ∈G if the form n(x) admits compo-
sition we have n(x · y) = n(x)n(y) and then n(x · y) = F 2(x, y)F(xy, xy)s(xy) = n(x)n(y) =
s(x)s(y)F(x, x)F(y, y). On the other hand for two elements of the algebra kF G, a = P
x∈G αxx
and b = P
y∈G βyy we have n(a) = P
x∈G α2
xs(x)F(x, x) and n(b) = P
y∈G β2
ys(y)F(y, y). But we
know that a·b = P
z∈G z(P
x∈G αxβxzF(x, xz)) so n(a·b) = P
z∈G[P
x∈G αxβxzF(x, xz)]2s(z)F(z, z) =
P
x,y,z∈G αxβxzF(x, xz)αyβyzF(y, yz)s(z)F(z, z), and like in the proof of Proposition 3.7 the re-
sult follows after comparing the last expression with
n(a)n(b) =
 X
x∈G
α2
xs(x)F(x, x)
! 
X
y∈G
β2
ys(y)F(y, y)

.
⊔⊓
4
Cayley algebras
In this section, we show that the ‘complex number’ algebra, the quaternion algebra, the octonion
algebra and the higher Cayley algebras are all G-graded quasialgebras the form kF G for suitable
G and F, which we construct. We recall that these algebras can be constructed inductively
by the Cayley-Dickson process; we show that this process is compatible with our quasialgebra
approach to nonassociative algebras.
Let A be ﬁnite-dimensional (not necessarily associative) algebra with identity element 1 and
a strong involution σ, i.e. an involution such that a + σ(a), a · σ(a) ∈k1 for all a ∈A. We have
studied this condition in the context of our quasialgebras kFG in Proposition 3.5. The Cayley
Dickson process says that we can obtain a new algebra ¯A = A ⊕vA of twice the dimension (i.e.
elements are denoted a, va for a ∈A) and multiplication deﬁned by
(a + vb) · (c + vd) = (a · c + αd · σ(b)) + v(σ(a) · d + c · b)
and with a new strong involution ¯σ
¯σ(a + vb) = σ(a) −vb.
The symbol v here is a notation device to label the second copy of A in ¯A. However, v · v = α1
according to the stated product, so one should think of the construction as a generalisation of
the idea of complexiﬁcation when α = −1. If A = k and α = −1 then ¯A = k[v] modulo the
relation v2 = −1 will be called the ‘complex number algebra’ over a general ﬁeld k. As in the
preceding section, we suppose k has characteristic not 2.
We start with the cochain version of the Cayley-Dickson construction, motivated by the
formulae above.
Proposition 4.1 Let G be a ﬁnite Abelian group F a cochain on it (so kF G is a G-graded
quasialgebra). For any s : G →k∗with s(e) = 1 we deﬁne ¯G = G × Z2 and on it the cochain ¯F
and function ¯s,
¯F(x, y) = F(x, y),
¯F(x, vy) = s(x)F(x, y),
¯F(vx, y) = F(y, x)
¯F(vx, vy) = αs(x)F(y, x),
¯s(x) = s(x),
¯s(vx) = −1
for all x, y ∈G. Here x ≡(x, e) and vx ≡(x, ν) denote elements of ¯G, where Z2 = {e, ν} with
product ν2 = e.
If σ(x) = s(x)x is a strong involution, then k ¯F ¯G is the Cayley-Dickson process applied to
kF G.
Proof
The only features to be checked for a cochain are that ¯F should be pointwise invertible
(which is clear from invertibility of s, F) and ¯F(e, vx) = s(e)F(e, x) = 1 and ¯F(vx, e) = F(e, x) =
1. Hence we have a new quasi-algebra k ¯F ¯G.
This reproduces the product · of the Cayley-Dickson process with respect to σ(x) = s(x)x,
since that is
vx · y = v(y · x) = vF(y, x)yx
vx · vy = αys(x) · x = αs(x)F(y, x)yx
x · vy = vs(x)x · y = s(x)F(x, y)xvy
in terms of the product of ¯G on the right. Moreover, ¯s on ¯G clearly reproduces the ¯σ in the
Cayley-Dickson precedure as well. ⊔⊓
This provides a cochain approach to the Cayley-Dickson process. The last proposition also
makes evident that all composition algebras with identity element, over a ﬁeld of characteristic
diﬀerent from two, are in fact quasialgebras kF G. We know that if we start by a ﬁeld k with
characteristic diﬀerent from 2 we can construct the sequence of algebras k(ν) (the Cayley-
Dickson extension of k with α = ν), (k(ν), β) (the Cayley-Dickson extension of k(ν) with
α = β) and ((k(ν), β), γ) (the Cayley-Dickson extension of (k(ν), β) with α = γ), in all cases
admitting a strong diagonal involution such that the associated form admits composition. If
A is a composition algebra with identity, over a ﬁeld of characteristic diﬀerent from two, it is
isomorphic to one of these 4 classes of algebras. This proves too that the last proposition of the
section 3 is a complete characterization of all composition algebras kFG with identity, in terms
of its cochain F. We also know from Proposition 3.5 that all these algebras with strong diagonal
involution are altercommutative.
As in Section 3, we are particularly interested in the canonical involution deﬁned by s(x) =
F(x, x) and in the Cayley Dickson extension with α = −1. In that case ¯F is determined from
F alone. Let us call this choice the standard Cayley-Dickson process in our cochain approach.
Proposition 4.2 If F(x, x) = −1 for all x ∈G and x̸ = e then the same holds for ¯F under the
standard Cayley-Dickson process. Moreover, in this case,
(i) ¯s has the standard form on ¯G.
(ii) If F 2 = 1 then ¯F 2 = 1 as well.
(iii) If kF G is altercommutative then so is k ¯F ¯G.
Proof
We have
¯σ(x) = ¯F(x, x)x = F(x, x)x = σ(x),
¯σ(vx) = ¯F(vx, vx)vx = −F(x, x)2vx = −vx
since F 2(x, x) = 1. The ﬁrst two parts are then immediate. The third part is
¯R(x, vy) =
¯F(x, vy)
¯F(vy, x) = F(x, x),
¯R(vx, y) = F(y, y)−1
¯R(vx, vy) =
¯F(vx, vy)
F(vy, vx) = F(x, x)
F(y, y) R(x, y)
has the altercommutative form in Deﬁnition 3.2 when R does and when F(x, x) = −1 for x̸ = e.
⊔⊓
In particular, the standard complex, quaternion, octonion etc algebras are all of this form
given by iterating the standard Cayley-Dickson process. To describe their cochains, we consider
the special case where G = (Z2)n and F is of the form
F(x, y) = (−1)f(x,y)
for some Z2-valued function f on G × G (which is a natural supposition for the class with
F 2 = 1).
Corollary 4.3 If G = (Z2)n and F = (−1)f then the standard Cayley-Dickson process has
¯G = (Z2)n+1 and ¯F = (−1) ¯f.
We use a vector notation⃗x = (x1, · · · , xn) ∈(Z2)n where
xi ∈{0, 1} (and the group Z2 is now written additively). Then
¯f((⃗x, xn+1), (⃗y, yn+1)) = f(⃗x,⃗y)(1 −xn+1) + f(⃗y,⃗x)xn+1 + yn+1f(⃗x,⃗x) + xn+1yn+1.
Proof
¿From the above, we have clearly
¯f(x, y) = f(x, y),
¯f(x, vy) = f(x, y) + f(x, x),
¯f(vx, y) = f(y, x),
¯f(vx, vy) = 1 + f(x, x) + f(y, x).
We then convert this to a vector notation where each copy of Z2 in G is the additive group of
Z2. We then make use of the product in Z2 to express whether a term is included or not (thus
xn+1yn+1 contributes 1 iﬀboth xn+1 = 1 and yn+1 = 1, etc.).
⊔⊓
Iterating this now generates the f for the quaternions, octonions etc.:
Proposition 4.4 i) The ‘complex number’ algebra has this form with
G = Z2,
f(x, y) = xy,
x, y ∈Z2
where we identify G as the additive group Z2 but also make use of its product.
