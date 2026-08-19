---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-063-452-case-b-integral-in-from-the-formula-fz-lz-2π
section_title: "Case (b), integral In,−. From the formula f−(z) = L−(z; −2πi, 2iπ) = Li 2(ez) +z2 −"
section_number: 4.5.2
pages: 45-47
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
2iπz we compute
ℑ(f−(z)) = ℑ(Li2(ez)) + 2ℜ(z)ℑ(z) − 2πℜ(z),
(f−)′(z) = 2z − Log(1 −ez) − 2iπ,
(f−)′′(z) = 2 + ez
1 −ez = 1 + 1
1 −ez,
f−(x +it) = Li 2(ex+it) + (x +it)2 − 2iπ(x +it),
∂
∂x ℑ(f−(x +it)) = ℑ
(∂
∂xf−(x +it)
)
= 2(t −π) − ℑ
(
Log(1 −ex+it)
)
= 2(t −π) − arg
(
1 −ex+it)
,
∂
∂t ℑ(f−(x +it)) = ℑ
(∂
∂tf−(x +it)
)
= 2x − ℜ
(
Log(1 −ex+it)
)
= 2x − Log|1 −ex+it|.
One can easily compute that ( f−)′(z0) = 0 if and only if
z0 =b +iπ := Log((1 +
√
5)/2) +iπ ≈ 0.48 +iπ.
As in the previous section, we will deform the contour i[s−
N, 2π −s+
N ] (in blue in Figure 5) to a
new contour C ′ (in dotted blue in Figure 5). In Figure 5, red dots and lines ar e points where
one can easily prove that ℑ(f−) = 0, and the red dotted curve is suggested by Mathematica.
We construct C ′ in ﬁve parts:
• C ′
1 is horizontal, going from is−
N to 1 + is−
N .
• C ′
2 is vertical, going from 1 + is−
N to 1 + i(π −ǫ), where ǫ> 0 is small enough.
• C ′
3 is almost horizontal, going from 1 + i(π −ǫ) to the saddle point b +iπ.
• C ′
4 is almost horizontal, going from the saddle point b +iπ to i(π +ǫ).
• C ′
5 is vertical, going from i(π +ǫ) to 2iπ −is+
N .
ℑf−< 0
ℑf−< 0
ℑf−> 0
ℑf−> 0
Cut
Cut
b +iπ
0
is−
N
iπ
2iπ −is+
N
2iπ
1 +is−
N
1 +i(π −ǫ)
i(π +ǫ)
Figure 5. The deformed contour C ′
Asymptotics on C ′
1: On the horizontal line of altitude s−
N , for all x /greaterorequalslant0, we have
∂
∂x ℑ(f−(x +is−
N )) = 2s−
N − 2π − arg
(
1 −ex+is−
N
)
< −π
2,
46 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
where the last inequality comes from | arg | ⩽ π and the fact that s−
N is small. Thus for all
x> 0 we have
ℑ(f−(x +is−
N ))< ℑ(f−(0 +is−
N )) −π
2x = Cl 2(s−
N ) − π
2x.
Since Cl 2(s−
N )< Cl2(π/3) ≈ 1.10149, it follows that for all x /greaterorequalslant1 we have ℑ(f−(x +is−
N )) ⩽
ℑ(f−(1 +is−
N ))< 0. Moreover, on C ′
1 = [is−
N, 1 +is−
N ] we have:
⏐
⏐
⏐
⏐
⏐
∫
C′
1
e
N
2iπf−(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽
∫ 1
0
e
N
2π ℑ(f−(x+is−
N ))dx
⩽
∫ 1
0
e
N
2π (Cl2(s−
N )− π
2x)dx
=e
N
2π Cl2(s−
N ) ·
∫ 1
0
e
N
2π (− π
2x)dx
=e
N
2π Cl2(s−
N ) · 4
N
(
1 −e− N
4
)
=oN →∞
( 1√
N
)
,
where the last asymptotics comes from s−
Ne
N
2π Cl2(s−
N ) =oN →∞(1/
√
N ) established in Section
4.3.2.
Asymptotics on C ′
3 ∪C ′
4:
We proceed similarly as we did in the previous section for C ′
3,
constructing this time two almost horizontal curves C ′
3,C ′
4, going respectively from 1 + iπ −iǫ
tob +iπ and from b +iπ toiπ +iǫ. For this we construct a small disk Dx around each point
x +iπ of [iπ, 1 + iπ], where ℑ(f−) is negative on the bottom half-disk and positive on the
upper half-disk if x>b , and conversely if x<b . This is possible, because for any x /greaterorequalslant0 the
vertical derivative at x +iπ is
∂
∂t ℑ(f−(x +it))|t=π = 2x − Log|1 −ex+iπ| = 2x − Log(1 +ex).
The reader will recognize the golden ratio, and agree that 2 x − Log(1 +ex)< 0 for x ∈ [0,b )
and 2x − Log(1 +ex)> 0 for x>b . This justiﬁes the location of the zones of signs of ℑ(f−)
in Figure 5 (the valleys and the hills of f− at b), whence the construction of the disks Dx.
By compacity we can reduce to a ﬁnite family of such disks whic h cover [iπ, 1 +iπ]; they are
drawn in grey in Figure 5. Then we deﬁne ǫ >0 small enough to be smaller than the radii
of all grey disks.
Finally, in order to apply the saddle point method of Proposi tion 4.2 for the contour λ =
C ′
3 ∪C ′
4, with g = 1, f = f−, and z0 = b +iπ, we only need to check that f ′′(z0) ⁄= 0. We
have
(f−)′′(b +iπ) = 1 + 1
1 −eb+iπ = 1 + 1
1 + 1+
√
5
2
= 5 −
√
5
2 = 1.38... ⁄= 0
so we are good to go. For the sake of completeness, we can compu te f−(b +iπ) = 9π2/10,
once again from the special values of the dilogarithm. Hence we get∫
C′
3∪C′
4
e
N
2iπf−(z)dz = Constant−√
N
(eir−N +oN →∞(1)),
where Constant − ∈ C∗ has modulus 2π
(
5 −
√
5
2
) − 1
2
= 5.34... and r− = − 9π
20 ∈ R.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 47
Asymptotics on C ′
2: Now that ǫ> 0 has been ﬁxed, we deﬁne C ′
2 as the vertical contour from
1 +is−
N to 1 +iπ −iǫ. To see that ℑ(f−) is strictly increasing on C ′
2 going upwards, one can
for example prove that the vertical derivative is positive:
∂
∂t ℑ(f−(x +it))|x=1 = 2 − Log|1 −e1+it| /greaterorequalslant2 − Log(1 +e)> 0,
where the last inequality stems from the fact that 1 > b. Hence the negative number
ℑ (f− (1 +iπ −iǫ)) is an upper bound for ℑ(f−) on C ′
2, and
⏐
⏐
⏐
⏐
⏐
∫
C′
2
e
N
2iπf−(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽ π ·e
N
2π ℑ(f−(c+iπ−iǫ)) =oN →∞
( 1√
N
)
.
Asymptotics on C ′
5: We deﬁne C ′
5 :=i[π +ǫ, 2π −s+
N ], oriented upwards. From Section 4.3,
since i[π +ǫ, 2π −s+
N ] ⊂ [π, 2π], we have:
⏐
⏐
⏐
⏐
⏐
∫
C′
5
e
N
2iπf−(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽
∫ 2π−s+
N
π+ǫ
e
N
2π ℑ(f−(it))dt =
∫ 2π−s+
N
π+ǫ
e
N
2π Cl2(t)dt =oN →∞
( 1√
N
)
.
This concludes the construction of the new contour C ′, and by summing the integrals on each
part, we obtain
In,− =
∫
C′
e
N
2iπf−(z)dz = Constant−√
N
(eir−N +oN →∞(1)),
where
(118) |Constant−| = 2π
(
5 −
√
5
2
) − 1
2
= 5.34..., r− = − 9π
20 ∈ R.
