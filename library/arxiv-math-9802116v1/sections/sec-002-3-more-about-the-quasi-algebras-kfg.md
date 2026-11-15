---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-002-3-more-about-the-quasi-algebras-kfg
section_title: "More about the quasi-algebras kFG"
section_number: 3
pages: 7-15
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
More about the quasi-algebras kFG
In this section, we will study further properties of the G-graded quasialgebras kF G beyond the
general ones arising from their categorical structure in the preceding section. We assume that
G is Abelian, that F is a 2-cochain and φ a 3-cocycle.
First of all, we note that kF G has a natural symmetric bilinear form whereby the basis of
group elements is orthonormal. In general, the associated quadratic function on kF G will not
be multiplicative (a quadratic character).
Proposition 3.1 If kF G admits a quadratic character then F 2 is a coboundary and φ2 = 1.
If the Euclidean norm quadratic function deﬁned by q(x) = 1 for all x ∈G is multiplicative
(making kF G a composition algebra) then F 2 = 1.
Proof
(For all discussions of quadratic forms we suppose that k has characteristic not 2).
Given a quadratic character q : kF G →k, we have q(x · y) = q(F(x, y)xy) = F 2(x, y)q(xy) =
q(x)q(y) on x, y ∈G, i.e. F 2(x, y) = q(x)q(y)/q(xy) is a coboundary in the group cohomology. In
general, if F 2 = ∂q we still need to specify a bilinear form with diagonal q, so the converse is not
automatic. If we take the canonical quadratic function associated to G as an orthonormal basis,
we will have q(x ·F y) = F 2(x, y) = F 2(x, y)q(x)q(y) for all x, y ∈G, so if this is multiplicative
then F 2 = 1. ⊔⊓
This will be the case for some of the Cayley algebras in the next section, as well as for many
other examples, and is the reason that F, φ typically have values ±1 in these cases.
Also, we already know from the construction in Corollary 2.4 that
(x · y) · z = x · (y · z)φ(x, y, z),
φ(x, y, z) = F(x, y)F(xy, z)
F(x, yz)F(y, z)
and hence that kFG is associative iﬀφ = 1. Also, recall that F(x, e) = F(e, x) = 1 (where e ∈G
is the group identity) is part of the cochain deﬁnition, and
φ(e, x, y) = φ(x, e, y) = φ(x, y, e) = 1
is part of the cocycle deﬁnition (the middle one implies the other two), in particular it holds for
our coboundary φ.
Likewise, we know from Proposition 2.5 that kF G is braided-commutative with respect the
braiding
Ψ(x ⊗y) = R(x, y)y ⊗x,
R = F(x, y)
F(y, x),
∀x, y ∈G.
Hence it is commutative in the usual sense iﬀF is symmetric. This is also clear from the form
of the product in kF G since G itself is Abelian. More interesting for us,
Deﬁnition 3.2 We say that kFG is altercommutative if Ψ is given by R of the form
R(x, y) =
 1
if x = e or y = e or x = y
−1
otherwise
for all x, y ∈G.
Note that R(x, x) = R(x, e) = R(e, x) = 1 for any kF G, so the content here is the value
−1 in the remaining ‘otherwise’ case. Also note that an altercommutative kF G can never be
commutative unless G = Z2. The condition is somewhat similar to the notion of a ‘supercom-
mutative’ algebra. One also has (more familiar) cases for the breakdown of associativity, such
as the notion of an alternative algebra. We have,
Proposition 3.3 kF G is an alternative algebra if and only if
φ−1(y, x, z) + R(x, y)φ−1(x, y, z) = 1 + R(x, y)
φ(x, y, z) + R(z, y)φ(x, z, y) = 1 + R(z, y)
for all x, y, z ∈G. In this case,
φ(x, x, y) = φ(x, y, y) = φ(x, y, x) = 1
for all x, y ∈G.
Proof
It is enough to consider the conditions of an alternative algebra on our basis elements,
x, y, z ∈G, i.e.
(x · y) · z −x · (y · z) + (y · x) · z −y · (x · z) = 0
(x · y) · z −x · (y · z) + (x · z) · y −x · (z · y) = 0.
This translates at once into the two equations
F(x, y)F(xy, z) + F(y, x)F(yx, z) = F(y, z)F(x, yz) + F(x, z)F(y, xz)
F(x, z)F(xz, y) + F(x, y)F(xy, z) = F(z, y)F(x, zy) + F(y, z)F(x, yz)
for all x, y, z ∈G when we put the product of kF G in terms of the associative product in G.
Dividing through then gives the equations in terms of φ, R as stated.
Also, setting x = y in the ﬁrst equation gives us (for characteristic of k not 2) φ(x, x, z) = 1.
Setting y = z in the second equation likewise gives us φ(x, y, y) = 1. Given these, setting x = z
in either gives φ(x, y, x) = 1. Actually, it is known that the condition of being an alternating
algebra is equivalent to
(a · a) · b = a · (a · b),
(a · b) · b = a · (b · b)
for all a, b in the algebra, which more immediately implies φ(x, x, y) = φ(x, y, y) = 1 on basis
elements. (Given these, the same two equations applied to a = x + y, b = z in the ﬁrst case and
a = x, b = y + z in the second case provide the full equations for an alternating algebra on basis
elements x, y, z, and hence imply that (a · b) · a = a · (b · a) holds as well, as usual.) ⊔⊓
Next we consider involutions. Since we have a special basis of kF G it is natural to consider
involutions diagonal in this basis.
Lemma 3.4 kF G admits an involution which is diagonal in the basis G iﬀR = ∂s (a group
coboundary) for some 1-cochain s : G →k∗with s2 = 1. In this case, one has R(x, y) = R(y, x)
and φ(x, y, z) = φ(z, y, x)−1 for all x, y, z ∈G.
Proof
Consider the endomorphism σ of the vector space kF G of the form
σ(x) = s(x)x,
∀x ∈G,
extended linearly, for some function s : G →k. For an involution we need σ2 = id, s(1) = 1 and
σ(a · b) = σ(b)σ(a), ∀a, b in our algebra. It is enough to consider these on the basis elements.
Then clearly the ﬁrst two correspond to
i) s(e) = 1 and s2(x) = 1 for all x ∈G.
For the second condition,
σ(x · y) = s(xy)x · y = s(xy)F(x, y)xy
while,
σ(y) · σ(x) = s(y)y · s(x)x = s(x)s(y)F(y, x)xy.
Equality for all x, y corresponds to
ii) s(x)s(y)
s(xy)
= F (x,y)
F (y,x) for all x, y ∈G.
We interpret this as stated, where the right hand side is R corresponding to the braiding Ψ. In
view of i), it implies that R2(x, y) = 1 and hence that R is symmetric. It also implies that ∂R = 1
in the group cohomology, which is the condition on φ stated since R(x, y) = F(x, y)/F(y, x) for
all x, y ∈G. ⊔⊓
In fact, we will be particularly interested in involutions with the property,
a + σ(a), a · σ(a) ∈k1
(a multiple of the identity) for all a in the algebra. Let us call this a strong involution.
Proposition 3.5 kF G admits a diagonal strong involution σ if and only if
i) G ≃(Z2)n for some n,
ii) σ(e) = e, σ(x) = −x for all x̸ = e,
iii) kF G is altercommutative in the sense of Deﬁnition 3.2.
Proof
Consider an endomorphism of the diagonal form σ(x) = s(x)x.
A general element
a = P
x∈G αxx, we have of course
σ(a) =
X
x∈G
αxs(x)x,
hence
a + σ(a) =
X
x∈G
αx(1 + s(x))x ∈k1
for all coeﬃcients αx if and only if s(x) = −1 for all x̸ = e. Here the group identity e ∈G is
the basis element 1 ∈kF G. Since we also need σ(1) = 1 for an involution, these two conditions
hold iﬀ
ii’) s(e) = 1 and s(x) = −1 for all x̸ = e.
Next, consider a basis element x ∈G, then
x · φ(x) = s(x)x · x = s(x)F(x, x)x2 ∈k1
implies that x2 = e, i.e. every element of G has order 2. Hence G (which is a ﬁnite Abelian
group) is isomorphic to (Z2)n for some n. Next, consider x + y for basis elements x̸ = y. Then
(x + y) · φ(x + y) = (x + y) · (s(x)x + s(y)y)
= (s(x)F(x, x) + s(y)F(y, y))e + (s(x)F(x, y) + s(y)F(y, x))xy ∈k1
tells us that
iii’) s(x)F(y, x) + s(y)F(x, y) = 0 for all x̸ = y.
When x = e or y = e this is empty. Otherwise, given ii’) it is equivalent to R(x, y) = −1 for
all x̸ = y, x̸ = e and y̸ = e, which is the altercommutativity condition.
Conversely, given these facts, a general element a = P
x∈G αxx obeys
a · σ(a) =
X
x,y∈G
αxαys(y)x · y =
X
x,y∈G
αxαyF(x, y)s(y)xy
=
X
z∈G
z

X
x,y∈G
δxy,zαxαys(y)F(x, y)

∈k1
since the terms with z̸ = e have contribution only when x̸ = y, and in this case the terms cancel
pairwise due to condition iii’). Hence if these conditions hold, we have the stated properties for
σ. They clearly imply the ones in the preceding lemma as well. ⊔⊓
On the other hand, given kF G we have a natural function s(x) = F(x, x) and consider now
the particular endomorphism corresponding to this.
Proposition 3.6 If σ(x) = F(x, x)x for all x ∈G deﬁnes a strong involution and |G|̸ = 2 in
k, then the algebra kFG is simple.
Proof
Let I be an ideal of kF G diﬀerent from kF G, and a = P
x∈G αxx an element of I. Then
for each y̸ = e ∈G,
a · y =
X
x∈G
αxF(x, y)xy ∈I,
y · a =
X
x∈G
αxF(y, x)xy ∈I.
Adding these together and using Proposition 3.5 in the form of the conditions ii’) and iii’), we
see that
a · y + y · a =
X
x̸=y
αx(F(y, x) + F(x, y))xy + αy2F(y, y)e = 2αey −2αye ∈I.
Then (a · y + y · a) · y = −2(αee + αyy) ∈I as well.
Since this is for all y̸ = e, we have
P
y̸=e αyy + (|G| −1)αee ∈I and hence αee ∈I provided |G| −2̸ = 0 in k. In this case αe = 0
and −αye + αey = −αye ∈I tells us that αy = 0 for all y, i.e. a = 0. Hence I = {0}. ⊔⊓
We also see from Proposition 3.5 that σ a strong involution restricts us to G∼=(Z2)n. In this
context we have a partial converse to Proposition 3.1.
Proposition 3.7 If G∼=(Z2)n then the Euclidean norm quadratic function deﬁned by q(x) = 1
for all x ∈G makes kFG a composition algebra if and only if
i) F 2(x, y) = 1 for all x, y ∈G
ii) F(x, xz)F(y, yz) + F(x, yz)F(y, xz) = 0, for all x, y, z ∈G with x̸ = y.
In this case the conditions in the Proposition 3.6 hold, i.e. σ(x) = F(x, x)x for all x ∈G is
a strong involution and kF G is simple if |G|̸ = 2. Moreover, kF G is alternative.
Proof
Suppose that q is multiplicative. q(x · y) = q(x)q(y) on all basis elements x, y ∈G is
F 2 = 1, as we know already from Proposition 3.1. The next case q((x + y) · z) = q(x + y)q(z) on
basis elements x, y, z ∈G with x̸ = y does not yield any new condition (both sides are 2). Now
consider the elements x, y, z, w ∈G with x̸ = y, z̸ = w but xz = yw. Because every element of
G is of order 2, this also means xw = yz. Because G is a group, xz̸ = xw, however. Hence
q((x + y) · (z + w)) = q(xz(F(x, z) + F(y, t)) + xw(F(x, w) + F(y, z)))
= (F(x, z) + F(y, w))2 + (F(x, w) + F(y, z))2 = 4 + 2(F(x, z)F(y, w) + F(x, w)F(y, z))
while q(x + y)q(z + w) = 4. This is the second condition stated after writing w = xyz and
renaming xz to z.
Conversely, assuming these conditions and given a = P
x αxx and b = P
y βyy, we have
a · b =
X
z∈G
z
 X
x∈G
αxβxzF(x, xz)
!
since every element of G has order 2. Hence
q(ab) =
X
z
 X
x
αxβxzF(x, xz)
!2
=
X
z
X
x
X
y
αxαyβxzβyzF(x, xz)F(y, yz).
In this sum the diagonal part where x = y contributes
X
z
X
x
α2
xβ2
xz = q(a)q(b)
since F 2 = 1, while the remaining contribution from x̸ = y is
X
z
X
x̸=y
αxαyβxzβyzF(x, xz)F(y, yz),
(∗)
By condition ii) this is equal to
−
X
x̸=y
X
z
αxαyβxzβyzF(x, yz)F(y, xz) = −
X
x̸=y
X
w
αxαyβywβxwF(x, xw)F(y, yw)
where we change the order of summation and change variables to w = xyz. But this has the
same form as our original expression for (*) but with a minus sign, hence this is zero.
Next, we observe that the condition ii) can be broken down equivalently as the conditions
ii.a) F(x, xy) + F(x, y) = 0 for all x, y ∈G with x̸ = e.
ii.b) F(x, yz)F(y, xz) + F(x, z)F(y, z) = 0 for all x, y, z ∈G with x̸ = e, y̸ = e and x̸ = y.
The ﬁrst of these is ii) in either of the cases x = e, y̸ = e or x̸ = e, y = e (followed by a
relabeling), while the second is the remaining case x̸ = e, y̸ = e, x̸ = y after making use of ii.a)
to substitute F(x, xz) and F(y, yz).
In this case, ii.a) implies the condition ii’) of Proposition 3.6. On the other hand, z = e in
the original form of the present condition ii) gives us
F(x, x)F(y, y) + F(x, y)F(y, x) = 0,
∀x̸ = y
which, given F 2 = 1, implies the condition iii’) of Proposition 3.6. Hence φ is strongly involutive.
Finally, also in this case, the equations of an alternative algebra in terms of F (see the proof
of Proposition 3.3) reduce to the following.
If x = e or y = e, the ﬁrst equation is trivial.
Otherwise, the case x̸ = e, y̸ = e, x = y reduces to φ(x, x, z) = 1, which in our present case
where G∼=(Z2)n reduces to
F(x, x) = F(x, xz)F(x, z).
This holds because the left hand side is -1 by the condition ii’) of Proposition 3.6 and the right
hand side is −F(x, z)2 = −1 by ii.a) and F 2 = 1. The remaining case is x̸ = e, y̸ = e and x̸ = y.
In this case the altercommutativity property in Proposition 3.6 reduces the ﬁrst equation for an
alternative algebra to
F(y, z)F(x, yz) + F(x, z)F(y, xz) = 0.
Since F 2 = 1, this is equivalent to ii.b)
On the other hand, under the assumptions of Proposition 3.6, the conditions ii.a)-ii.b) are
equivalent to
ii.c) F(x, y) + F(xy, y) = 0 for all x, y ∈G with y̸ = e
ii.d) F(x, y)F(x, z) + F(xy, z)F(xz, y) = 0 for all x, y, z ∈G with y̸ = e, z̸ = e and y̸ = z
(or one can obtain them directly from our original condition ii)). We use these versions
in a similar analysis for the content of the second of the conditions in Proposition 3.3 for an
alternative algebra. ⊔⊓
We have written the proof of the last part of the proposition in a reversible way. Hence we
also conclude,
Corollary 3.8 If σ(x) = F(x, x)x for all x ∈G is a strong involution, and F 2 = 1, then the
following are equivalent,
i) kF G is an alternative algebra,
ii) kF G is a composition algebra.
The conditions in Proposition 3.7 and the corollary are evidently highly restrictive, because
if k has characteristic diﬀerent from 2 it is known that we have only the following composition
algebras with the Euclidean norm: k, the algebra with basis 1, v, v2 = −1, the algebra over
k with the product of quaternions and the algebra over k with the product of octonions. If
k is algebraically closed these algebras are isomorphic to k, k ⊕k, M2(k) (2 × 2 matrices)
and Zorn’s algebra of vectorial matrices [8]. Equivalently, one knows that these are the only
simple alternative algebras. On the other hand, the diagonal strong involution conditions in
