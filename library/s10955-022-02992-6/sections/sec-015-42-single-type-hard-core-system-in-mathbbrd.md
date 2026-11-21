---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-015-42-single-type-hard-core-system-in-mathbbrd
section_title: "Single-Type Hard-Core System in mathbbRd"
section_number: 4.2
pages: 27-30
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Consider a bounded convex shape S ⊂Rd which is non-empty, regular closed and balanced
(recall: A set S ⊂Rd is called regular closed if and only if it equals the closure of its interior,
i.e., S◦= S, and it is called balanced if and only if αS ⊂S for all |α| ≤1). We investigate
the special case of the hard-core setup in the continuum from Sect. 2.3 where X consists of
all translates x + S = {x + y | y ∈S}. Let us further assume that both the activity and
the reference measure λ are translationally invariant. Then we may identify X with Rd, the
reference measure λ with the Lebesgue measure, and the activity function with a positive
scalar, z(x) ≡z > 0.
For an integrable function h : X →R we write

X
h(Z)λ(dZ) =

Rd h(x + S)dx.
Write |S| for the Lebesgue volume of the shape S and deﬁne for Borel sets D ⊂Rd
V (D) :=

Rd 1l{(x+S)∩D̸=∅}dx.
(4.6)
Notice V ({y}) = |S|,whichispositiveandﬁnitebyourassumptionson S,and V(S) = |S⊕S|
with A ⊕B := {a + b | a ∈A, b ∈B} the Minkowski sum. The latter identity holds
since we assumed the set S to be balanced which implies {(x + S) ∩S̸ = ∅} = S ⊕S.
Moreover, notice that V —as a function on Dε with the convention V (∅) = 0—satisﬁes the
measurability assumption from Theorem 2.6 by the same argument as formulated on p. 22
for ˜T .
Werefertosuchsystemsassingle-typehard-coresystemsinthecontinuum.Inthelanguage
of stochastic geometry (see [28, Sects. 3,4]), the associated Gibbs measure is a hard-core
germ–grain model with deterministic grain S (the germs are the positions x).
Theorem 4.2 Assume there exists α > 0 such that
|S|eαV (S)z < eα|S| −1.
(4.7)
Then the activity expansions ρn(x1, . . . , xn; z) converge absolutely for all n ∈N and all
(x1, . . . , xn) ∈Xn.
Remark 4.2 Again, notice that while Theorem 4.2—just as its discrete analogue Theo-
rem 4.1)—improves on the Kotecký–Preiss condition, it is in all the cases we considered
as examples weaker than Fernández–Procacci (e.g., for systems of hard spheres the bounds
on the radius of convergence obtained in [9, 22] are slightly better). However, the advantage
of our criterion is that an explicit bound is provided directly, with no need for numerical
computation regardless of the dimension.
Example 4.2 (Hard spheres) If S = BR(0) is the closed ball of radius R > 0 around the
origin, condition (4.7) becomes
z ≤sup
α>0
exp(α|BR(0)|) −1
|BR(0)| exp(α|B2R(0)|).
Carrying out the optimization over α yields the condition
|B2R(0)| z ≤

1 −1
2d
	2d−1
.
33
Page 28 of 47
S. Jansen, L. Kolesnikov
In the limit d →∞at ﬁxed R > 0, the right-hand side converges from above to the familiar
bound 1/e.
Proof Let α > 0 satisfy condition (4.7). Set a(D) := αV (D) for D ∈Dε, choose some
chopping map C and let D ∈Dε (the snippet-size ε > 0 will be speciﬁed later in the
proof). For the simplest selection rule s choosing always the ﬁrst snippet E1, condition (i) in
Theorem 2.6 reads
∞

k=1
zk
k!

Xk I(E1; D′; Y1, . . . , Yk) eα[V (D′∪(∪k
i=1Yi))−V (D′)]λk(dY)
≤eα[V (D′∪E1)−V (D′)] −1,
(4.8)
where D′ = D\E1.
Notice that—unlike in the discrete case—terms of order higher than one in z do not
necessarily vanish in the series in (4.8). Inspired by the proof of Theorem 4.7, we try ﬁrst
to bound the exponent on the left-hand side of (4.8), seeking a bound that separates Y :=
Y1 ∪· · · ∪Yk from E1 and D′. If the constraint were that E1 ⊂Y, we would conclude with
strong subadditivity applied to B := Y and C := D′ ∪E1 that V (E1) + V (D′ ∪Y) ≤
V (Y) + V (D′ ∪E1). For the weaker constraint E1 ∩Y̸ = ∅, this is no longer true. Let
Z ∈X. A straightforward case distinction reveals that under the indicator I, the inequality
1l{Z∩E1̸=∅} + 1l{Z∩(D′∪Y)}̸=∅} ≤1l{Z∩Y̸ =∅} + 1l{Z∩(D′∪E1)̸=∅}
is correct for all possible values of the left-hand side except possibly 1 + 1. Indeed it may
happen that Z intersects both E1 and D′ ∪Y, hence a fortiori D′ ∪E1, but not Y, so that
the right-hand side becomes 0 + 1. This happens precisely when Z intersects D′ and E1 but
not Y. The inequality becomes correct if we add the indicator of this event to the right-hand
side. Integrating over Z, we obtain
V (E1) + V (D′ ∪Y) ≤V (Y) + V (D′ ∪E1) +

X
1l{Z∩E1̸=∅, Z∩Y=∅, Z∩D′̸=∅}λ(dZ).
Moreover, there exists a constant C = C(S, d) > 0 that depends only on the dimension d
and the shape S such that if k = 1 and Y = Y1 ∈X is a translate of S, then

X
1l{Z∩E1̸=∅, Z∩Y=∅, Z∩D′̸=∅}λ(dZ) ≤Cε.
Indeed, on the left side we may drop the indicator that Z intersects D′ and see that it is
sufﬁcient to check

X
1l{Z∩E1̸=∅, Z∩Y=∅}λ(dZ) ≤Cε.
(4.9)
To see that such an estimate holds let Bε(c) be a closed ball of radius ε around some c ∈Rd
containing the snippet E1 and let x ∈Y ∩E1 (by assumption this intersection is non-empty).
Then x ∈Bε(c) and the inequality
1l{Z∩E1̸=∅, Z∩Y=∅} ≤1l{Z∩Bε(c)̸=∅, x /∈Z}
holds pointwise in Z, thus also

X
1l{Z∩E1̸=∅, Z∩Y=∅}λ(dZ) ≤

X
1l{Z∩Bε(c)̸=∅, x /∈Z}λ(dZ).
Cluster Expansions: Necessary...
Page 29 of 47
33
Notice that

X
1l{Z∩Bε(c)̸=∅, x /∈Z}λ(dZ) = |{y ∈Rd|(y + S) ∩Bε(0)̸ = ∅, ˜x /∈y + S}|,
where Bε(0) is the closed ball of radius ε around 0 and ˜x := x −c. For the set on the
right-hand side of that equation, the identity
{y ∈Rd|(y + S) ∩Bε(0)̸ = ∅, ˜x /∈y + S} = (S ⊕Bε(0)) \(˜x + S),
holds since S being balanced directly implies
{y ∈Rd|(y + S) ∩Bε(0)̸ = ∅} = S ⊕Bε(0)
and
{y ∈Rd|˜x ∈y + S} = ˜x + S.
Furthermore, observe that the inclusion
(S ⊕Bε(0)) \(˜x + S) ⊂((S ⊕Bε(0)) \S) ∪((S ⊕Bε(˜x)) \(˜x + S))
holds since ˜x ∈Bε(0) and S is balanced set. Moreover, (S ⊕Bε(˜x)) \(˜x + S) is the translate
of (S ⊕Bε(0)) \S by ˜x, hence it has the same Lebesgue volume and
| (S ⊕Bε(0)) \(˜x + S)| ≤| (S ⊕Bε(0)) \S| + | (S ⊕Bε(˜x)) \(˜x + S)|
=2| (S ⊕Bε(0)) \S|
=2 (|S ⊕Bε(0)| −|S|) .
Finally, by Steiner’s formula for compact convex sets (see [28]), |S ⊕Bε(0)| −|S| is given
by a non-constant polynomial in ε, which yields a bound of the form given by the right-hand
side of (4.9) (where the constant C > 0 can be expressed in terms of the intrinsic volumes
of S following the formula).
Consequently, we obtain the bound
V (E1) + V (D′ ∪Y) ≤V (Y) + V (D′ ∪E1) + Cε
(4.10)
which corresponds to the bound (4.4) in the proof of Theorem 4.1.
The inequality (4.10) immediately yields the following upper bound for the left-hand side
of (4.8):
eαCε eα[V (D′∪E1)−V (D′)−V (E1)]
∞

k=1
zk
k!

Xk I(E1; D′; Y1, . . . , Yk) eαV (Y)λk(dY).
The summand for k = 1 is equal to
z eαV (S)

X
1{Y1∩E1̸=∅,Y1∩D′=∅}λ(dY1) = z[V (D′ ∪E1) −V (D′)]eαV (S).
For k ≥2, we bound V (Y) ≤k
i=1 V (Yi) = kV (S), drop the indicator that the Yi’s do not
intersect D′, and get the upper bound
zkeαkV (S)

Xk
k
i=1
1l{Yi∩E1̸=∅}1l{Y1,...,Yk disjoint}λk(dY).
Notice that there exists N ∈N such that for all k ≥N + 1 the integral vanishes. To see
this, assume that there are inﬁnitely many disjoint objects Y ∈X intersecting the snippet E1
33
Page 30 of 47
S. Jansen, L. Kolesnikov
(and therefore some open ε-ball Bε in which the snippet is contained). Since all the objects
Y are translates of S, we can choose the same radius r > 0 for all of the inﬁnitely many
disjoint objects Y intersecting E1 such that Y = x + S ⊂Br(x). Naturally, every such
r-ball must intersect Bε and therefore their union is again a bounded Borel subset of Rd. But
— by our assumptions on the shape S—every Y ∈X has the same ﬁxed, strictly positive
Lebesgue measure, thus their disjoint union must have inﬁnite Lebesgue measure, which is
a contradiction to its boundedness.
For k ≤N, we drop the indicator that Y3, . . . , Yk are disjoint and ﬁnd that the integral is
bounded by
V (E1)k−2

X
1l{Y1∩E1̸=∅}

X
1l{Y2∩E1̸=∅, Y2∩Y1=∅}λz(dY2)
	
λz(dY1).
The inner integral is bounded by Cε because of (4.9), the outer integral gives an additional
factor V (E1). Altogether, the left-hand side of (4.8) is bounded by
eαCε eα[V (D′∪E1)−V (D′)−V (E1)]
z[V (D′ ∪E1) −V (D′)]eαV (S)
+Cε
N

k=2
zkV (E1)k−1eαkV (S)	
.
Proceeding as in the proof of Theorem 4.2, but taking into account the strict inequality from
assumption (4.7), we ﬁnd that there exist α > 0 such that
eα[V (D′∪E1)−V (D′)−V (E1)]z[V (D′ ∪E1) −V (D′)]eαV (S) < eα[V (D′∪E1)−V (D)] −1,
compare to (4.5). Therefore, picking ε small enough, we see that (4.8), hence also condition
(i) in Theorem 2.6 is satisﬁed and all T (D; z), D ∈Dε, are absolutely convergent. The claim
of the theorem follows immediately.
⊓⊔
