---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-042-223-examples-and-computations
section_title: "Examples and computations"
section_number: 2.2.3
pages: 51-54
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
We give a relation between the torsion form as we deﬁned it above and the previous
work of J.Porti and then J.Dubois in [Por97, Dub06, DHY09]. As Dubois computed
50
explicit formulae in many cases, this will permit us to perform direct computations
in several examples.
Proposition 2.2.4 (see also Corollary 4.2 of [Por97]). Given a ﬁnite pointx in
a component of irreducible type ¯X of the augmented character variety, and v a
valuation corresponding tox, we ﬁxµ a class inπ1(∂M ). Then the following holds :
tor(M, Ad◦ρ)(v) = 1
τµ(M, Ad◦¯ρ)
2√
(Tr ¯ρ(µ))2− 4
dYµ
where τµ(M, Ad◦¯ρ) is the torsion in the sense of Porti-Dubois at the pointv, rela-
tively to the curveµ.
Remark 2.2.5.Here we use the convention of [Por97], that corresponds to ours. In
[Dub06] for instance, the torsion deﬁned is the inverse of the latter.
Remark 2.2.6. Notice thatτµ makes sense only whenv is not a critical point of
Yµ. If we pull-back this formula on the augmented variety by settingYµ =Zµ +Z−1
µ
then the formula becomes rational :tor(M, Ad◦ρ) = 2
τµ
dZµ
Zµ
.
Proof. The torsion in the sense of Porti-Dubois is deﬁned pointwise as a function on
a smooth open subsetU of the character varierty, and it is proved in [Por97] that it is
infactanalytic.For v∈U,pickanygenerator P ofH0(∂M, Ad◦¯ρ).Thenoneobtains
basis ofHi(M, Ad◦¯ρ),i = 1, 2, as follows : since we assumed that¯ρ is not a critical
point of the trace functionYµ, the restriction mapH1(M, Ad◦¯ρ)→H1(µ, Ad◦¯ρ) is
an isomorphism. The latter is identiﬁed tok viaH1(µ, Ad◦¯ρ)→k,f↦→ Tr(Pf (µ)),
and the composition of those maps is simply the diﬀerentialdYµ. Then the generator
of H1(M, Ad◦¯ρ) is ﬁxed to bedY−1
µ (1). For the generator ofH2(M, Ad◦¯ρ), pull-
back 1 via the isomorphismsH2(M, Ad◦¯ρ)→H2(∂M, Ad◦¯ρ)
φP
−→k, whereφP (f) =
f(P ). ButP appears both inH1 and inH2, hence the torsion does not depend on a
choice ofP. Finally, we have chosenH to be a generator ofH2(M, Ad◦ρ), and the
isomorphism H1(M, Ad◦ρ)→ Ωk(Y )/k provides a term¯ρ0(µ), we need to normalize
by
√
Tr(H2)
Tr(¯ρ0(µ)2), and the result follows.
Example 2.2.7 (The trefoil knot). Recall that the tautological representation of
the component of irreducible typeX⊂X(M) is given by the formulae :
ρ(a) =
(
t 1
−(t2 + 1) −t
)
,ρ (b) =
(
−j 0
0 −j2
)
51
In [Dub06], for any boundary curveµ,τµ(¯ρ) is a constant1/k that does not depend
on ¯ρ. Takeµ the meridianab−1, Yµ = (j−j2)t, Zµ =u, then
tor(M, Ad◦ρ) =kdu
u
It has no zeros, and two poles at zero and inﬁnity, as expected its divisor’s degree
is -2 because the smooth projective modelY of X is isomorphic toCP1.
Example 2.2.8(The ﬁgure-eight knot). Here we takeµ to be the longitude ofM,
denote its trace byYµ = x4− 5x2 + 2, then τµ(x,y ) = 5 − 2x2 and one obtains
tor(M, Ad◦ρ) = dZµ
(5−2x2)Zµ
. A careful examination shows that it has no poles, and
zeros only at inﬁnity : takex = 1/t a local coordinate, dZµ
Zµ
= dYµ√
Y 2µ−4≃ dt
t , hence
each of the four ideal points contribute as a zero of order 1. The divisor’s degree of
the torsion is4, that conﬁrms the fact that the Riemann surfaceY has genus 3.
Example2.2.9 (Theknot 52). Thisexamplearisesfrom[DHY09].Thefundamental
group is isomorphic toπ1(M) =⟨u,v| vw =wu⟩ where w =u−1v−1uvu−1v−1. The
component of irreducible type of the character variety is described by the Riley
polynomial φ(S,U ). In our setting, with x = Tr u = Tr v and y = Tr uv, then
x =S
1
2 +S− 1
2 and y =S +S−1−U, we obtain
X =Xirr(M) =
{
(x,y )∈k2| −x2(y− 1)(y− 2) +y3−y2− 2y + 1 = 0
}
This aﬃne curve compactiﬁes with two points at inﬁnity : an ordinary double point
corresponding to the two directionsx =∞,y = 1 or y = 2, and a simple point
x =y =∞. Apart from this, the variety is smooth. By the Noether-Plücker formula,
its genus is(d− 1)(d− 2)/2−δ, withd = 4 and δ = 1, henceg( ˆX) = 2.
The extensionα +α−1 =x gives a 2 : 1 map Y → ˆX, that ramiﬁes atx2 = 4. The
Hurewitz formula impliesχ(Y ) = 2χ( ˆX)− 6 =−10, henceY is a curve of genus 6.
From [DHY09] again, withµ a longitude,τµ = 5x4(y− 2)−x2(5y2 + 7y− 31) +
7(y2−y− 3), andYµ = (y3− 6y2 + 12y− 8)x10− (3y4− 10y3−y2− 68)x8 + 3(y5−
43y3 + 48y2 + 86y− 116)x6 + (y6 + 6y5− 23y4− 28y3 + 96y2 + 28y− 105)x4 + (2y6−
y5− 16y4 + 6y3 + 40y2− 9y− 34)x2 + 2.
As tor(M, Ad◦ρ) = dYµ
τµ
√
Y 2µ−4, we compute the vanishing order of the torsion at the
3 diﬀerent ideal points :
1. x∼ 1
t, y∼ 1 +t2, thenτµ∼ 1
t4, dYµ√
Y 2µ−4∼ dt
t and tor∼t3dt
2. x∼ 1
t, y∼ 2 + 3t, thenτµ∼ 1
t2, dYµ√
Y 2µ−4∼ dt
t and tor∼tdt
52
3. x∼ 1
t(1−2t2), y∼ 1
t2(1−2t2), then againτµ∼ 1
t2, dYµ√
Y 2µ−4∼ dt
t and tor∼tdt
Finally, notice thatY → ˆX does not ramify at inﬁnity, hence to each ideal point
of ˆX correspond 2 ideal points ofY, and the divisor’s degree oftor on Y is 10, as
expected.
Example 2.2.10(The knot61). This example arises from [DHY09] too. The funda-
mental group isπ1(M) =⟨u,v| vw =wu⟩ where w = (vu−1v−1u)2. The irreducible
type part of the character variety is
X ={(x,y )∈ C2|x4(y− 2)2−x2(y + 1)(y− 2)(2y− 3) + (y3− 3y− 1)(y− 1) = 0}
The two ideal points are non ordinary double points :
