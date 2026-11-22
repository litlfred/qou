---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-033-223-examples-and-computations
section_title: "Examples and computations"
section_number: 2.2.3
pages: 51-54
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Examples and computations
We give a relation between the torsion form as we deﬁned it above and the previous
work of J.Porti and then J.Dubois in [Por97, Dub06, DHY09]. As Dubois computed
50
explicit formulae in many cases, this will permit us to perform direct computations
in several examples.
Proposition 2.2.4 (see also Corollary 4.2 of [Por97]). Given a ﬁnite point x in
a component of irreducible type ¯X of the augmented character variety, and v a
valuation corresponding to x, we ﬁx µ a class in π1(∂M). Then the following holds :
tor(M, Ad ◦ρ)(v) =
1
τµ(M, Ad ◦¯ρ)
2
p
(Tr ¯ρ(µ))2 −4
dYµ
where τµ(M, Ad ◦¯ρ) is the torsion in the sense of Porti-Dubois at the point v, rela-
tively to the curve µ.
Remark 2.2.5. Here we use the convention of [Por97], that corresponds to ours. In
[Dub06] for instance, the torsion deﬁned is the inverse of the latter.
Remark 2.2.6. Notice that τµ makes sense only when v is not a critical point of
Yµ. If we pull-back this formula on the augmented variety by setting Yµ = Zµ + Z−1
µ
then the formula becomes rational : tor(M, Ad ◦ρ) =
2
τµ
dZµ
Zµ .
Proof. The torsion in the sense of Porti-Dubois is deﬁned pointwise as a function on
a smooth open subset U of the character varierty, and it is proved in [Por97] that it is
in fact analytic. For v ∈U, pick any generator P of H0(∂M, Ad ◦¯ρ). Then one obtains
basis of Hi(M, Ad ◦¯ρ), i = 1, 2, as follows : since we assumed that ¯ρ is not a critical
point of the trace function Yµ, the restriction map H1(M, Ad ◦¯ρ) →H1(µ, Ad ◦¯ρ) is
an isomorphism. The latter is identiﬁed to k via H1(µ, Ad ◦¯ρ) →k, f 7→Tr(Pf(µ)),
and the composition of those maps is simply the diﬀerential dYµ. Then the generator
of H1(M, Ad ◦¯ρ) is ﬁxed to be dY −1
µ (1). For the generator of H2(M, Ad ◦¯ρ), pull-
back 1 via the isomorphisms H2(M, Ad ◦¯ρ) →H2(∂M, Ad ◦¯ρ)
φP
−→k, where φP(f) =
f(P). But P appears both in H1 and in H2, hence the torsion does not depend on a
choice of P. Finally, we have chosen H to be a generator of H2(M, Ad ◦ρ), and the
isomorphism H1(M, Ad ◦ρ) →Ωk(Y )/k provides a term ¯ρ0(µ), we need to normalize
by
q
Tr(H2)
Tr(¯ρ0(µ)2), and the result follows.
Example 2.2.7 (The trefoil knot). Recall that the tautological representation of
the component of irreducible type X ⊂X(M) is given by the formulae :
ρ(a) =
 
t
1
−(t2 + 1)
−t
!
, ρ(b) =
 
−j
0
0
−j2
!
51
In [Dub06], for any boundary curve µ, τµ(¯ρ) is a constant 1/k that does not depend
on ¯ρ. Take µ the meridian ab−1, Yµ = (j −j2)t, Zµ = u, then
tor(M, Ad ◦ρ) = kdu
u
It has no zeros, and two poles at zero and inﬁnity, as expected its divisor’s degree
is -2 because the smooth projective model Y of X is isomorphic to CP1.
Example 2.2.8 (The ﬁgure-eight knot). Here we take µ to be the longitude of M,
denote its trace by Yµ = x4 −5x2 + 2, then τµ(x, y) = 5 −2x2 and one obtains
tor(M, Ad ◦ρ) =
dZµ
(5−2x2)Zµ. A careful examination shows that it has no poles, and
zeros only at inﬁnity : take x = 1/t a local coordinate, dZµ
Zµ =
dYµ
√
Y 2
µ −4 ≃dt
t , hence
each of the four ideal points contribute as a zero of order 1. The divisor’s degree of
the torsion is 4, that conﬁrms the fact that the Riemann surface Y has genus 3.
Example 2.2.9 (The knot 52). This example arises from [DHY09]. The fundamental
group is isomorphic to π1(M) = ⟨u, v| vw = wu⟩where w = u−1v−1uvu−1v−1. The
component of irreducible type of the character variety is described by the Riley
polynomial φ(S, U). In our setting, with x = Tr u = Tr v and y = Tr uv, then
x = S
1
2 + S−1
2 and y = S + S−1 −U, we obtain
X = Xirr(M) =

(x, y) ∈k2| −x2(y −1)(y −2) + y3 −y2 −2y + 1 = 0
	
This aﬃne curve compactiﬁes with two points at inﬁnity : an ordinary double point
corresponding to the two directions x = ∞, y = 1 or y = 2, and a simple point
x = y = ∞. Apart from this, the variety is smooth. By the Noether-Plücker formula,
its genus is (d −1)(d −2)/2 −δ, with d = 4 and δ = 1, hence g( ˆX) = 2.
The extension α + α−1 = x gives a 2 : 1 map Y →ˆX, that ramiﬁes at x2 = 4. The
Hurewitz formula implies χ(Y ) = 2χ( ˆX) −6 = −10, hence Y is a curve of genus 6.
From [DHY09] again, with µ a longitude, τµ = 5x4(y −2) −x2(5y2 + 7y −31) +
7(y2 −y −3), and Yµ = (y3 −6y2 + 12y −8)x10 −(3y4 −10y3 −y2 −68)x8 + 3(y5 −
43y3 + 48y2 + 86y −116)x6 + (y6 + 6y5 −23y4 −28y3 + 96y2 + 28y −105)x4 + (2y6 −
y5 −16y4 + 6y3 + 40y2 −9y −34)x2 + 2.
As tor(M, Ad ◦ρ) =
dYµ
τµ√
Y 2
µ −4, we compute the vanishing order of the torsion at the
3 diﬀerent ideal points :
1. x ∼1
t, y ∼1 + t2, then τµ ∼1
t4,
dYµ
√
Y 2
µ −4 ∼dt
t and tor ∼t3dt
2. x ∼1
t, y ∼2 + 3t, then τµ ∼1
t2,
dYµ
√
Y 2
µ −4 ∼dt
t and tor ∼tdt
52
3. x ∼
1
t(1−2t2), y ∼
1
t2(1−2t2), then again τµ ∼1
t2,
dYµ
√
Y 2
µ −4 ∼dt
t and tor ∼tdt
Finally, notice that Y →ˆX does not ramify at inﬁnity, hence to each ideal point
of ˆX correspond 2 ideal points of Y , and the divisor’s degree of tor on Y is 10, as
expected.
Example 2.2.10 (The knot 61). This example arises from [DHY09] too. The funda-
mental group is π1(M) = ⟨u, v| vw = wu⟩where w = (vu−1v−1u)2. The irreducible
type part of the character variety is
X = {(x, y) ∈C2 |x4(y −2)2 −x2(y + 1)(y −2)(2y −3) + (y3 −3y −1)(y −1) = 0}
The two ideal points are non ordinary double points :
1. When y →2, x →∞, we have a double point of type ”y2−x6”, its δ-invariant
is 3.
2. When y, x →∞, we have a double point of type ”y2 −x8”, its δ-invariant is
4.
Hence g( ˆX) = (d −1)(d −2)/2 −P δi = 10 −3 −4 = 3. The covering map Y →ˆX
given by α + α−1 = x ramiﬁes in eight ﬁnite points, thus χ(Y ) = −16.
When desingularizing ˆX one obtains four ideal points, the same kind of computations
as in Example 2.2.9 are shortened as follows :
1. x ∼
1
t(1+at2), y ∼
2
1+at2 with a a root of 4a2 +6a+1 then in both cases τ ∼1
t2,
dλ
λ ∼dt
t and tor ∼tdt
2. x ∼
1
t(1−t2), y ∼
1
t2(1−t2), then τ ∼1
t6, dλ
λ ∼dt
t and tor ∼t5dt
3. x ∼
1
t(1−2t2+6t4−25t6), y ∼
1
t2(1−2t2+6t4−25t6), then τ ∼1, dλ
λ ∼tdt and tor ∼tdt
Then notice that Y →ˆX is not ramiﬁed at inﬁnity, thus the divisor’s degree of tor
is 16, as expected.
