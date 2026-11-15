---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-007-8-factors-of-the-jacobian
section_title: "Factors of the Jacobian"
section_number: 8
pages: 36-40
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
toc_source: inferred
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cover- ings of P1, highlighting their"
---
Factors of the Jacobian
In this section we elaborate some of the algebraic geometry underlying the
cases where ρq(Bn) is ﬁnite. In particular, we describe a basis of elliptic
diﬀerentials for the representative examples (n, d) = (3, 4) and (3, 6).
We begin by showing:
Theorem 8.1 The representation of the braid group ρq(Bn) at a primitive
dth root of unity is ﬁnite iﬀ
n = 3 and d = 3, 4, 6 or 10; or
n = 4 and d = 4 or 6; or
n = 5, 6 and d = 6.
Proof.
In the 8 cases given we ﬁnd, consulting Table 9, that H1(X)q is
deﬁnite for all primitive dth roots of unity q; hence U(Λn,q), and its subgroup
ρq(Bn), are both ﬁnite.
To see the list is complete for n = 3, note that if −q is a primitive
pth root of unity and p > 6, then ρq(Bn) maps onto the (2, 3, p) triangle
group (see §5) and hence it is inﬁnite. In particular, for q = −1 we have
ρq(Bn) ∼= SL2(Z).
To see the list is complete for n > 3, let
g = τ1τ −1
2 τ3τ −1
4
· · · τ ±1
n
and let A = ρq(g). Observe that ρq(Bn) contains a copy of ρq(Bn−1), so the
list of d for which ρq(Bn) is ﬁnite only gets shorter as n increases; and if
ρq(Bn) is ﬁnite, then the spectral radius r(A) must be 1.
For n = 4 we need only test d = 3, 4, 6 and 10. We have seen that d = 4
and 6 give ﬁnite groups, and we can rule out d = 3 and 10 by checking that
r(A) > 1 for q = ζ3 and q = ζ3
10. Similarly, for n = 5 we can rule out d = 4
by checking that r(A) > 1 at q = ζ4; and for n = 7 we can rule out d = 6
by checking that r(A) > 1 at q = ζ6. (Here we have used the fact that
the representations ρq at diﬀerent primitive dth roots of unity are all Galois
conjugate.)
Corollary 8.2 The image of the braid group ρq(Bn) is ﬁnite iﬀU(Λn,q) is
ﬁnite.
35
Jacobians. When ρq(Bn) is ﬁnite, the Hodge structure on the correspond-
ing part of the H1(X) is rigid; equivalently, we have an isogeny
Jac(X) →J(X) × A
where dim A > 0 and A is independent of X. We refer to A as a rigid factor
of the Jacobian of X.
Theorem 8.3 The Jacobian of the curve X deﬁned by
yd = (x −b1) · · · (x −bn)
(for n distinct points) has a rigid factor in the 8 cases shown in Table 10.
n
d
g(X)
Factor of Jac(X)
3
3
1
C/Z[ζ3]
3
4
3
(C/Z[ζ4])2
3
6
4
(C/Z[ζ3])2
3
10
9
(C2/Z[ζ5])2
n
d
g(X)
Factor of Jac(X)
4
4
3
(C/Z[ζ4])2
4
6
7
(C/Z[ζ3])3
5
6
10
(C/Z[ζ3])4
6
6
10
(C/Z[ζ3])4
Table 10. Rigid factors of the Jacobian.
In Table 10, g(X) indicates the genus of X, and the rigid factor listed
comes from L H1(X)q over the primitive dth roots of unity.
The factor C2/Z[ζ5], which occurs for (n, d) = (3, 10), denotes quotient
of C2 by the image of Z[ζ5] under x 7→(x, x′), where x 7→x′ is the Galois
automorphism satisfying ζ′
5 = ζ2
5. The other factors listed are elliptic curves
with automorphisms of orders 4 or 6.
Note that the cases (n, d) = (3, 4) and (4, 4) yield the same set of curves
X, as do the cases (5, 6) and (6, 6). Note also that curves of type (n, d) =
(3, 6) cover curves of type (3, 3), so they also have a second rigid factor
A′ ∼= C/Z[ζ3].
Proof of Theorem 8.3. Let S = L H1(X)q, where the sum is taken over
the primitive dth roots of unity. This subspace is deﬁned over Q, so it meets
H1(X, Z) in a lattice SZ of the same rank as dimC S.
For the 8 cases listed, the induced Hodge structure on S is given by
S = S1,0 ⊕S0,1 =

M
Im q>0
H1(X)q

⊕

M
Im q<0
H1(X)q

,
36
where again the sum is over the primitive dth roots of unity (see Corollary
3.2). That is, the Hodge structure is reﬁned by the eigenspace decomposition
of T|S, which is independent of the complex structure on X; and hence the
complex torus A = S1,0/SZ is a rigid factor of Jac(X). The dimension of A
is determined by Corollary 3.3, and the CM-type of the endomorphism T|A
(see [Shi, §5.5A]) is determined by the condition Im q > 0. This information
determines A itself, up to isogeny, yielding Table 10.
Genus 3 curves branched over 4 points.
For added perspective we
describe some details in one of the simplest cases, namely genus 3 curves X
of the form
y4 = (x −b1)(x −b2)(x −b3).
1.
Eigenspaces.
The most interesting eigenspace here is H1(X)q for
q = √−1 = ζ−3
4 . This eigenspace satisﬁes H1(X)q ∼= H1,0(X)q; its signature
is (2, 0), and it is spanned by the holomorphic 1-forms dx/y3 and x dx/y3.
2. Factors of Jac(X). By Theorem 8.3 we have an isogeny
Jac(X) →E × A × A,
(8.1)
where A ∼= C/Z[ζ4] is the square torus and E is an elliptic curve that depends
on X. Composing with the inclusion X →Jac(X), we obtain a dominant
map p0 : X →E and a pair of dominant maps pi : X →A, i = 1, 2.
3.
Elliptic diﬀerentials.
These maps can be seen directly as follows.
First, observe that X is branched over B′ = B∪{∞}, and that Aut(bC, B′) ∼=
Z/2 × Z/2. Applying a M¨obius transformation to B′, we can normalize so
that its symmetry group is generated by x 7→−x and x 7→1/x; then the
deﬁning equation for X takes the form
X : y4 = x4 + bx2 + 1.
(8.2)
Now consider the elliptic curves and holomorphic 1-forms deﬁned by
E : z2 = x4 + bx2 + 1,
ωE = dx/z,
and
A : y4 = u2 + bu + 1,
ωA = du/y3.
Since A has an order 4 automorphism (u, y) 7→(u, √−1y), it is evidently
a square torus. Setting z = y2 and u = x2, we obtain degree two maps
p0 : X →E and p1 : X →A. Composing with an automorphism of X, we
deﬁne p2(x, y) = p1(1/x, y/x).
37
We claim the triple of maps (p0, p1, p2) induces the desired isogeny (8.1).
To see this, just note that the pullbacks of the forms (ωE, ωA, ωA) under
(p0, p1, p2) respectively yield a basis
= (dx/y2, dx/y3, −x dx/y3)
for Ω(X) consisting of elliptic diﬀerentials.
4.
Action of the braid group.
The braid group acts on PH1(X)q as
the octahedral group Γ ∼= S4 ⊂PU(2), preserving the spherical metric.
The generating twists τ1, τ2 act by rotations R1, R2 ∈Γ of order 4 about
orthogonal axes, corresponding to a pair of elliptic diﬀerentials as above.
5. The period map. The period map determines an embedding
fq : M∗
0,3 →(H2,0 ∼= P1)/S4
whose image omits just one point.
The domain is the (2, 3, ∞) orbifold
and the target is the (2, 3, 4) orbifold; and fq sends the cusp to the cone
point of order 4. These facts can be veriﬁed by showing the metric comple-
tion of M0,4 in the induced spherical metric is an orbifold; or by explicitly
computing the period map, using the elliptic forms above.
Remark: Shimura–Teichm¨uller curves. Equation (8.2) determines a
remarkable curve V ⊂M3 (parameterized by b). M¨oller shows V is the only
subvariety of any moduli space Mg, g ≥2 which is both a Shimura curve
and a Teichm¨uller curve [Mo].
Irregular covers of elliptic curves. The preceding example was partic-
ularly simple because the maps pi : X →A were Galois coverings. To give
the ﬂavor of a more typical example, we describe a map p : X →A in the
case (n, d) = (3, 6).
In this case X is a genus 4 curve, presented as a covering of bC branched
over 4 points. We can change the x-coordinate by a M¨obius transformation
so the deﬁning equation for X becomes
X : y6 = (x3 −3x −b)(x −2)3
for some b ∈C (because the cross-ratio of the roots of the polynomial on the
right takes on all possible values). Now consider the elliptic curve deﬁned
by
A : z6 = (b −2)4w(w −1)3.
Because of its order 6 symmetry S(w, z) = (w, ζ6z), we have A ∼= C/Z[ζ3];
and the formula
(w, z) =
x3 −3x −b
2 −b
, y(x + 1)

(8.3)
38
deﬁnes an irregular, degree 3 map p : X →A. This map shows A occurs as
one of the rigid factors of Jac(X).
This calculation is motivated by the observation that the desired map
p : X →A induces a map
p : X/⟨T⟩→A/⟨S⟩
between a pair of orbifolds with signatures (2, 6, 6, 6) and (2, 3, 6) respec-
tively. Since both orbifolds have genus zero, we can regard p as a rational
map of the form w = p(x). The signatures of these orbifolds suggest there
exists such a map with deg(p) = 3, sending the 3 points of order 6 in the
domain to the unique point of order 6 in the range. Any such map would be
totally ramiﬁed over the singular point of order 3, so in suitable coordinates
it would be a cubic polynomial; and we are led to formula (8.3).
Remark.
In the case (n, d) = (3, 10), the projection to the rigid fac-
tor Jac(X) →A ∼= C2/Z[ζ5] is not induced by a map p : X →Y with
Jac(Y ) ∼= A. This can be established by showing there is no map from the
(10, 10, 10, 10) orbifold to the (2, 5, 10) orbifold which lifts to the required
Z/10 covering spaces. (It is, however, induced by a correspondence.)
