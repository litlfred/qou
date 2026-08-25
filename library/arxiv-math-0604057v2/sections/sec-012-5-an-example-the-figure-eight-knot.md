---
doc_id: arxiv-math-0604057v2
doc_title: "VOLUME CONJECTURE, REGULA TOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT"
section_id: sec-012-5-an-example-the-figure-eight-knot
section_title: "An Example: The Figure Eight Knot"
section_number: 5
pages: 12-18
source_pdf: 0604057v2.pdf
source_sha256: 649fad141dc34eb9
doc_brief: "VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER VARIETY OF A KNOT — In this paper, by using the regulator map of Beilinson-Delig ne, we show that the quan- tization condition posed by Gukov is true"
---
Throughout this section, we shall denote by M the complement of the ﬁgure-eight knot in S3.
we compute its character variety and give some applications .
It is well-known that π1(M ) is given by two generators and one relation:
(5.1) π1(M ) =< α, β|R(α, β) >, R (α, β) = β−1α−1βαβ −1αβα−1β−1α,
VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT 13
where α, β are meridians, and they are conjugate to each other β = δαδ−1 with δ = α−1βαβ −1.
Set τ = αβ−1α−1β, we have a peripheral subgroup π1(∂M )
(5.2) π1(∂M ) =< α, λ > ; λ = τ −1δ = β−1αβα−1α−1βαβ −1,
where α is the meridian and λ is the longitude. Note in this section, we use α for the meridian
instead of µ.
Let us consider its character variety X(M ). We use (5.1) for the presentation of π1(M ). For
a SL2(C)-representation ρ ∈ R(M ), its character χ is determined by χ(α), χ(β), and χ(αβ). We
have the morphism t : R(M ) → C3, t(ρ) = ( χ(α), χ(β), χ(αβ)) and X(M ) is the image t(R(M )).
Let ( x, y, z) be the aﬃne coordinate for C3.
Proposition 5.1. The aﬃne variety X(M ) ⊂ C3 is deﬁned by the following equations:
(5.3) x = y,
(5.4) ( x2 − z − 2)(z2 − (1 + x2)z + 2x2 − 1) = 0 .
In particular, we can identify X(M ) with the aﬃne plane curve {(x, z) ∈ C2|(x2 − z − 2)(z2 − (1 +
x2)z + 2x2 − 1) = 0 }. It has two irreducible components.
Proof. Since α is conjugate to β, x = χ(α) = χ(β) = y. Hence (5.3) follows. For the second equa-
tion, by [Wh, Theorem 1], the factor x2 − z − 2 corresponds to characters of abelian representations,
and the other one corresponds to the characters of non-abeli an representations. □
By the preceding proposition, the component deﬁned by the eq uation z2 − (1 +x2)z + 2x2 − 1 = 0
consists of the characters of non-abelian representations , in particular, it contains the discrete
faithful representations of the complete hyperbolic metri c of M . We denote this component X0.
Hence we have :
Corollary 5.2. The component X0 is an irreducible smooth curve in C2 with the deﬁning equation:
(5.5) z2 − (1 + x2)z + 2x2 − 1 = 0 .
Proof. We only need to check that (5.5) deﬁnes a smooth curve. Let f (x, z) = z2−(1+x2)z+2x2−1.
Then ∂f
∂x = −2xz + 4x and ∂f
∂z = 2z − 1 − x2. It is straightforward to check that their is no common
solution to the equations ∂f
∂x = ∂f
∂z = f (x, z) = 0. Hence, the curve is smooth. □
Corollary 5.3. There are exactly two reducible characters on X0 and they correspond to the points
(±
√
5, 3).
Proof. Let ρ be a reducible representation whose character lies on X0. Let m be the eigenvalue
of ρ(α). By [CCGLS, Proposition 6.2], m2 must be a root of the Alexander polynomial ∆( t) =
t2 − 3t + 1 of the ﬁgure-eight knot. Thus,
m = ±
√
3 ±
√
5
2 = ±
√
5 ± 1
2 ; and x = σ(ρ(α)) = m + m−1 = ±
√
5.
Plug in (5.5), we get z = 3 with multiplicity two. Now it is easy to check that ( ±
√
5, 3) are
exactly the intersection points of X0 and the component x2 − z − 2 = 0. Since the latter component
consists of abelian characters, the result follows. □
Remark. Two inequivalent reducible representations may have the sam e character. The points
(±
√
5, 3) above are such examples. They are the characters of both some a belian representation and
non-abelian reducible representation which are clearly no t equivalent.
14 WEIPING LI AND QINGXUE W ANG
Proposition 5.4. Suppose that χ ∈ X0 and χ(α) = ±2. Then χ is the character of a discrete
faithful representation.
Proof. Plug x = ±2 in (5.5), we get z2 − 5z + 7 = 0 and hence z = 5±√
−3
2 . The following
representation θ : π1(M ) → P SL2(C) was given in [Ril2]:
θ(α) = ±
[
1 1
0 1
]
, θ (β) = ±
[
1 0
−ω 1
]
;
where ω = −1+√
−3
2 is a primitive cube root of unity. By [Ril2, Theorem 1], θ is an isomorphism.
Thus, θ is a discrete faithful representation of π1(M ). Let θ be the complex conjugation of θ. It is
straightforward to check that the four points ( ±2, 5±√−3
2 ) correspond to the SL2(C) characters of
the lifts of θ and θ. The result follows. □
Denote by CP2 the complex projective plane. We use [ X : Y : Z] to represent its homogenous
coordinates. We will identify C2 with the open subset {[x : 1 : z]|(x, z) ∈ C2}. Note this is diﬀerent
from the standard notation.
Let ~X0 be a smooth projective model of X0. We have the following explicit description of ~X0 in
CP2.
Proposition 5.5. ~X0 is an elliptic curve and deﬁned by the equation in CP2:
(5.6) Y Z 2 − Y 2Z − X 2Z + 2X 2Y − Y 3 = 0.
Proof. Equation (5.5) is the deﬁning equation of X0. Substitute x = X
Y , z = Z
Y , and we get
(5.6). That is, it is the projective closure of X0 in CP2. It suﬃces to show that it is smooth. Let
F (X, Y, Z) be the left-hand side of (5.6). It is elementary to check tha t except (0 , 0, 0), there is no
common solution to the equations ∂F
∂X = ∂F
∂Y = ∂F
∂Z = 0. Hence, it is smooth. Since (5.6) is a cubic
equation in CP2, ~X0 has genus 1. □
Corollary 5.6. X0 has exactly two ideal points [1 : 0 : 0] and [0 : 0 : 1] .
Proof. The ideal points correspond to Y = 0. This gives X 2Z = 0. Thus, X = 0 or Z = 0. □
Next, we explicitly construct the restriction map r : X0 → X(∂M ) induced by the inclusion
i : π1(∂M ) → π1(M ).
Theorem 5.7. The map r : X0 → X(∂M ) ∈ C3 is given by the formulas:
r(x, z) = ( x, F (x, z), G(x, z));
where F (x, z) = x4 −5x2 +2 is the trace of the longitude λ, and G(x, z) = (4 x−x3)z +(x5 −4x3 −x)
is the trace of αλ.
We will postpone the proof of Theorem 5.7 to the end of this sec tion. Instead, we ﬁrst discuss its
applications. The reason is that the proof itself is element ary and lengthy, and probably is known
to the experts. However, we can not ﬁnd it in the literature. S o we include here for completeness.
Denote by x0 = [0 : 0 : 1] and x1 = [1 : 0 : 0]. By Corollary 5.6, they are the only ideal points of
X0.
Lemma 5.8. (1) Both x0 and x1 are poles of the meromorphic functions fα and fλ . Their orders
are: vx0(fα ) = vx1(fα ) = 2 , and vx0(fλ ) = vx1(fλ ) = 8 .
(2) The Culler-Shalen norm |(1, 0)| = 4 and |(0, 1)| = 16.
Proof. (1) By Theorem 5.7, for χ = (x, z) ∈ X0, Iα (x, z) = x and Iλ (x, z) = F (x, z) = x4 − 5x2 + 2.
Since fα = I 2
α − 4 and fλ = I 2
λ − 4, it is suﬃcient to show that vx0(Iα ) = vx1(Iα ) = 1, and
vx0(Iλ ) = vx1(Iλ ) = 4.
VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT 15
On ~X0, substitute x = X
Y , z = Z
Y , we get for [ X : Y : Z] ∈ ~X0,
Iα ([X : Y : Z]) = X
Y , and Iλ ([X : Y : Z]) = X 4 − 5X 2Y 2 + 2Y 4
Y 4 .
First, we consider x0 = [0 : 0 : 1]. Let U3 = {[X : Y : Z]|Z ⁄= 0 }. Then it is an open subset
containing x0. U3 is identiﬁed with C2 via x = X
Z and y = Y
Z , where ( x, y) are aﬃne coordinates of
C2. Dividing by Z 3 the both sides of the equation (5.6) of ~X0 and substituting x = X
Z and y = Y
Z ,
we get the aﬃne equation in U3 = C2:
g(x, y) = y − y2 − x2 + 2x2y − y3 = 0.
Under this identiﬁcation, x0 is the origin (0 , 0), Iα (x, y) = x
y and Iλ (x, y) = ( x
y )4 − 5( x
y )2 + 2. Since
∂g
∂y = 1 − 2y + 2x2 − 3y2 and ∂g
∂y (0, 0) ⁄= 0, the function x is a local parameter of the local ring of
regular functions at (0 , 0). Solve g(x, y) = 0, we get
Iα (x, y) = x
y = x−1u(x, y), where u(x, y) = y2 + y − 1
2y − 1 , u (0, 0) ⁄= 0;
and
Iλ (x, y) = x−4w(x, y), where w(x, y) = u4 − 5x2u2 + 2x4, w (0, 0) ⁄= 0.
Therefore, x0 is a pole of Iα of order 1, and it is a pole of Iλ of order 4.
For x1 = [1 : 0 : 0]. Let U1 = {[X : Y : Z]|X ⁄= 0}. U1 is identiﬁed with C2 via y = Y
X and z = Z
X ,
where ( y, z) are aﬃne coordinates of C2. Similarly, we obtain the aﬃne equation in U1 = C2:
h(x, y) = yz 2 − y2z − z + 2y − y3 = 0.
Now x0 is the origin (0 , 0), Iα (x, y) = y−1 and Iλ (x, y) = y−4 − 5y−1 + 2. Since ∂h
∂z (0, 0) ⁄= 0, the
function y is a local parameter of the local ring of regular functions at (0, 0). Thus, x0 is a pole of
Iα of order 1, and it is a pole of Iλ of order 4.
(2) By deﬁnition, |(1, 0)| = deg fα = vx0(fα ) + vx1(fα ), by (1), |(1, 0)| = 2 + 2 = 4. Similarly,
|(0, 1)| = 8 + 8 = 16. □
Use this lemma, we can compute the Culler-Shalen norm |(p, q)| for any γ = pα+qλ ∈ H1(∂M, Z).
Proposition 5.9. For each γ = pα + qλ ∈ H1(∂M, Z), the Culler-Shalen norm |γ| = |(p, q)| =
2(|p + 4q| + |p − 4q|).
Proof. By Lemma [CGLS, 1.4.1, 1.4.2], for each ideal point x, there is a homomorphism φx :
H1(∂M, Z) → Z, such that, for each γ = pα + qλ,
vx(fγ ) = |φx(γ)|, and |γ| =
∑
x: ideal point
|φx(γ)|;
where vx(fγ ) denotes the order of pole of fγ at x. For our case, we have two ideal points x0 and
x1. By Lemma 5.8, we get |φx0(α)| = 2, |φx0(λ)| = 8, |φx1(α)| = 2 and |φx1(λ)| = 8. Since φxi are
homomorphisms, we obtain that |φxi(γ)| = | ± 2p ± 8q|, i = 1, 2. Therefore, we obtain that either
|φx0(γ)| + |φx1(γ)| = |2p + 8q| + |2p + 8q|,
or
|φx0(γ)| + |φx1(γ)| = |2p + 8q| + |2p − 8q|.
We claim that the ﬁrst case can not happen. Suppose not. Take γ = −4α + λ, then |γ| =
|φx0(γ)| + |φx1 (γ)| = 0. Hence deg fγ = |γ| = 0. This is impossible because fγ is not constant. Thus
the claim is proved and |γ| = |(p, q)| = 2(|p + 4q| + |p − 4q|). □
Next let M (0) be the closed 3-manifold obtained by the Dehn surgery of M along the longitude
λ. It is known that M (0) admits an essential torus [Boy, Page 200]. By Theorem 5.7 , we show that
M (0) has non-abelian inﬁnite fundamental group.
16 WEIPING LI AND QINGXUE W ANG
Proposition 5.10. The fundamental group π1(M (0)) is a non-abelian, inﬁnite group.
Proof. Suppose that ρ ∈ R(M ) with the property that its trace σ(ρ(λ)) = 2. Now by Proposition
5.7, we have:
x4 − 5x2 + 2 = 2
where x = σ(ρ(α)). Solve this equation, we get x = 0 or x = ±
√
5. By Proposition 5.1, there exists
ρ0 ∈ R(M ), such that σ(ρ0(α)) = 0 and σ(ρ0(λ)) = 2. In particular the eigenvalues of ρ0(α) is ±i.
By [CCGLS, Proposition 6.2], ρ0 is an irreducible representation. On the other hand, since ρ0(α)
and ρ0(λ) commute and ρ0(α) is not parabolic, ρ0(λ) must be the identity matrix. Hence ρ0 induce
a representation of π1(M (0)). The irreducibility of ρ0 implies that π1(M (0)) is not abelian.
Similarly, let ρ√
5 ∈ R(M ), such that σ(ρ√
5(α)) =
√
5 and σ(ρ√
5(λ)) = 2. By the same reason,
ρ√
5(λ) equals the identity matrix. Hence ρ√
5 induces a representation of π1(M (0)). We can check
that the image of ρ√
5 in SL2(C) is torsion-free. Therefore, π1(M (0)) is not ﬁnite. □
Remark. We know that M (0) is not a hyperbolic manifold. 0/1 is the one of the ten exceptional
surgery slopes of the ﬁgure-eight knot. It is interesting to k now that we can prove its fundamental
group is non-cyclic, non-abelian and inﬁnite just from the e lementary computations.
Let M (3) be the closed 3-manifold obtained by the Dehn surgery of M along the simple closed
curve γ = 3α + λ.
Lemma 5.11. M (3) has exactly three irreducible SL2(C) characters.
Proof. Since π1(M (3)) = ⟨π1(M )|α3λ = 1⟩, we have an embedding of character varieties X(M (3))֒→
X(M ). On the other hand, X0 is the only component of X(M ) containing characters of non-abelian
representations. Thus, the irreducible characters of M (3) are contained in the set S = {χ|χ ∈
X0, χ(α3λ) = 2 }. By (5.13), we have
(5.7) χ(α2λ) = χ(α)χ(αλ) − χ(λ),
and
(5.8)
χ(α3λ) =χ(α)χ(α2λ) − χ(αλ)
=(χ(α)2 − 1)χ(αλ) − χ(α)χ(λ).
By Theorem 5.7, we obtain
(5.9) ( x2 − 1)[(4x − x3)z + x5 − 4x3 − x] − x(x4 − 5x2 + 2) = 2 .
It is clear that the set S is exactly the common solutions to equations (5.9) and (5.5) . Note when
x = 1, (5.9) holds and is independent of the values of z. From (5.5), when x = 1, z = 1. So
(1, 1) ∈ S.
We solve z in terms of x from (5.9), then plug in (5.5) and simplify the expression, w e get
(5.10) C(x) = x4 − 4x3 + 2x2 + 4x + 1 = ( x2 − 2x − 1)2 = 0.
It has two solutions x = 1 ±
√
2. Hence the set S has three elements. They are not equal to ±2 or
±
√
5. By Corollary 5.3, x ⁄= ±
√
5 implies that each one is an irreducible character. By Propo sition
5.4 and 4.6, x ⁄= ±2 means that each one is also a character of M (3). The result follows. □
Let sl2(C) be the Lie algebra of SL2(C). Then we have the adjoint representation Ad : SL2(C) →
Aut(sl2(C)). For a representation ρ : π1(M (3)) → SL2(C), let H 1(M (3); sl2(C)ρ) be the ﬁrst
cohomology group with coeﬃcients in sl2(C) twisted by the composition Ad ◦ ρ.
Proposition 5.12. Suppose that ρ : π1(M (3)) → SL2(C) is irreducible.
Then H 1(M (3); sl2(C)ρ) = 0 .
VOLUME CONJECTURE, REGULATOR AND SL2(C)-CHARACTER V ARIETY OF A KNOT 17
Proof. By [BW, Theorem 1.1], M (3) is not toroidal. Since H1(M (3); Z) is ﬁnite, M (3) is a small
Seifeit ﬁbered space. By the preceding Lemma 5.11, M (3) has irreducible representations, so
π1(M (3)) is not cyclic. By [BZ1, Proposition 7], H 1(M (3); sl2(C)ρ) = 0. □
Remark. For the other eight exceptional surgery slopes ±1, ±2, ±3, ±4, we also have the explicit
irreducible representations with inﬁnite images. Hence th eir fundamental groups are all non-abelian
and inﬁnite. We omit the details here. Hence, Proposition 5. 12 holds also for M (±1), M (±2) and
M (−3).
Now we turn to the proof of Theorem 5.7. We need to ﬁnd explicit expressions of the traces
F (x, z), G(x, z) of ρ(λ) and ρ(αλ) respectively in terms of traces of ρ(α) and ρ(αβ).
We need some preliminary lemmas. For A, B, C ∈ SL2(C)), we have the following identities on
their traces [Wh]:
(5.11) σ(AB) = σ(BA);
(5.12) σ(A) = σ(A−1);
(5.13) σ(AB) = σ(A)σ(B) − σ(AB−1);
(5.14) σ(ABC ) = σ(A)σ(BC ) + σ(B)σ(AC) + σ(C)σ(AB) − σ(A)σ(B)σ(C) − σ(ACB );
(5.15) For m ≥ 2, σ(Am) = σ(Am−1)σ(A) − σ(Am−2).
Notice that (5.11) is true for any n × n matrices. It is easy to see that (5.14) and (5.15) follow
from (5.13). Equations (5.12) and (5.13) can be checked by di rect computations.
Now for ρ ∈ R(M ), set a = ρ(α), b = ρ(β), x = σ(a) = σ(b) and z = σ(ab) = σ(ρ(αβ)).
Lemma 5.13. (i) σ(a2) = x2 − 2.
(ii) σ(a−1b) = σ(ba−1) = σ(b−1a) = σ(ab−1) = x2 − z.
(iii) σ(b−1aba−1) = σ(a−1bab−1) = z2 − x2z + 2x2 − 2.
Proof. (i) By (5.15), σ(a2) = σ(a)2 − σ(I), where I is the 2 × 2 identity matrix.
(ii) By (5.11), σ(a−1b) = σ(ba−1) and σ(b−1a) = σ(ab−1) ; by (5.12), σ(ab−1) = σ(ba−1); by
(5.13), σ(ab−1) = x2 − z.
(iii) By the subdivision ( b−1a)ba−1 and (5.14), we have
σ(b−1aba−1) = σ(b−1a)σ(ba−1) + σ(b)σ(b−1) + σ(a−1)σ(b−1ab) − σ(b−1a)σ(b)σ(a−1) − σ(I).
Therefore,
σ(b−1aba−1) = ( x2 − z)2 + x2 + x2 − (x2 − z)x2 − 2 = z2 − x2z + 2x2 − 2.
The proof for σ(a−1bab−1) is the same by the subdivision ( a−1b)ab−1, and we omit it. □
Lemma 5.14. (i) σ(a−1a−1b) = x(x2 − z) − x;
(ii) σ(ba−1a−1b) = x4 − zx2 − 2x2 + 2;
(iii) σ(ba−1a−1bab−1) = x2 − z.
18 WEIPING LI AND QINGXUE W ANG
Proof. (i) By (5.13), we have
σ(a−1(a−1b)) = σ(a−1)σ(a−1b) − σ(a−1b−1a)
By Lemma 5.13, each term of the right-hand side is known. Henc e,
σ(a−1a−1b) = x(x2 − z) − x.
(ii) By (5.13),
σ(b(a−1a−1b)) = σ(b)σ(a−1a−1b) − σ(bb−1aa) = σ(b)σ(a−1a−1b) − σ(a2)
The formula follows.
(iii) By (5.14), we have
σ((ba−1)(a−1b)(ab−1)) = σ(ba−1)σ(a−1bab−1) + σ(a−1b)σ(1) + σ(ab−1)σ(ba−1a−1b)−
σ(ba−1)σ(a−1b)σ(ab−1) − σ(a−1b)
Plug in what we know on the right-hand side and simplify, we ob tain the formula. □
Lemma 5.15. (i) σ(ab−1a) = σ(aab−1) = x3 − zx − x;
(ii) σ(aab) = xz − x;
(iii) σ(ab−1aba−1) = x
Proof. (i) σ(a(b−1a)) = σ(a)σ(b−1a) − σ(b), and σ(a(ab−1)) = σ(a)σ(ab−1) − σ(aba−1);
(ii) σ(a(ab)) = σ(a)σ(ab) − σ(ab−1a−1)
(iii) σ(a(b−1aba−1)) = σ((b−1aba−1)a) = σ(b−1ab) = x. □
Proof of Theorem 5.7. First, let us compute F (x, z) = σ(ρ(λ)), the trace of ρ(λ). By (5.14), we
have
σ((b−1a)(ba−1)(a−1bab−1)) = σ(b−1a)σ(ba−1a−1bab−1) + σ(ba−1)σ(ab−1)+
σ(a−1bab−1)σ(b−1aba−1) − σ(b−1a)σ(ba−1)σ(a−1bab−1) − σ(I)
By Lemmas 5.13 and 5.14, we know all the terms on the right-han d side. Notice that ( x, z) ∈ X0,
hence z2 − (1 + x2)z + 2x2 − 1 = 0. Now divide the right-hand side by z2 − (1 + x2)z + 2x2 − 1, the
remainder is F (x, z). we calculate that F (x, z) = x4 − 5x2 + 2.
For the trace of ρ(αλ), we have
σ((ab−1a)(ba−1)(a−1bab−1)) = σ(ab−1a)σ(ba−1a−1bab−1) + σ(ba−1)σ(aab−1)+
σ(a−1bab−1)σ(ab−1aba−1) − σ(ab−1a)σ(ba−1)σ(a−1bab−1) − σ(a).
By Lemmas 5.13, 5.14 and 5.15, we have all the terms on the righ t-hand side. Then we divide
the result of the right-hand side by the polynomial z2 − (1 + x2)z + 2x2 − 1 = 0 and G(x, z) equals
the remainder. We calculate that it is (4 x − x3)z + (x5 − 4x3 − x). □
