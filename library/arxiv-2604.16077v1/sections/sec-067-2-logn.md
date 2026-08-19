---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-067-2-logn
section_title: "Log(N )"
section_number: 2
pages: 60-62
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
on→∞ (1/n|f ′(z0)|) = on→∞ (1/NLog(N )) in the asymptotic formula of Proposition 5.3 (ii).
Also Cl 2(s−
N ) ∼N →+∞ −s−
N Log(s−
N ), e− N
2iπ (s−
N )2
∼N →+∞ 1, and
ρ(is−
N )
−iLog|2 sin(s−
N/2)| ∼N →+∞
1
i ·e−
l′
1α−
2N
( Ni
α−π
) l′
0
2iπ + 1
2
· 1
Log( N
α−π ).
Therefore, taking the bounded sequence ( vN ) into account as explained above, from (144) we
get
∫
[is′
N,is−
N ]
gN (z)
N (l′
0+iπ)/2iπe
N
2π ℑ(f+(z))dz
∼N →+∞i
l′
0
2iπ + 3
2e
N
2π (α− π
N ·Log( N
α−π ))e−
l′
1α−
2N
( 1
α−π
) l′
0
2iπ + 1
2
vN · 1
Log( N
α−π ) · 1
N
∼N →+∞
i
l′
0
2iπ + 3
2
N 1− α−
2 Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
vN.(145)
We can now conclude. Consider the integral over C +−
a on the RHS of (143). As in (142) one
ﬁnds
⏐
⏐
⏐
⏐
∫
C+−
a
gN (z)e
N
2iπ L+(z,−2iπ,2iπ)dz
⏐
⏐
⏐
⏐ =ON →∞
( 1
N 1− α′
2
)
.
Since α′ <α −, it is a oN →+∞ of (145). From this and (140) we deduce
(146)
∫
C+
a
gN (z)e
N
2iπ L+(z,−2iπ,2iπ)dz
∼N →+∞i
l′
0
2iπ + 3
2 · N
l′
0
2iπ − 1
2 + α−
2
Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
vN.
This concludes Step 3.
Step 4: Deformed contour in case (a), integral IN,+(iπ).
Similarly, in the situation of Figure 3 we can deform C ±
N to the contour shown in the ﬁgure
except in the case R(Log(u0))> 0, where the contour must circumvent L1 in a small subarc
close to 0 and joining a point −υ′′, υ′′ > 0, to is−
N , if I(Log(u0)) < 0, or the contour
must circumvent L2 in a small subarc close to 2 iπ and joining −υ′′ + 2iπ to 2iπ −is+
N , if
I(Log(u0))> 0. Indeed, we can take such subarcs to be C +
a in the ﬁrst case, and ¯C +
a + 2iπ
in the second case, with C +
a deﬁned as in Step 3, and ¯C +
a the complex conjugate of C +
a but
with endpoint −is+
N instead of −is−
N .
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 61
Here we get the following horizontal derivative:
∂
∂x ℑ(f+(x +it)) = 2t − arg
(
1 −ex+it)
+π,
which is positive when t > 0. Thus the integrals of e
N
2π ℑ(f+(z)) over the subarcs C +
a or
¯C +
a + 2iπ will be dominated by a constant times the same integrals over the projections of
these sub-arcs on the vertical axis, where we know that ℑ(f+(z)) = Cl 2(t). By the same
arguments as in Step 3 for C +
a one proves that max ¯C+
a +2iπ
(
|gN (z)|
N (l′
0+iπ)/2iπ
)
< +∞. Then, the
same reasoning as from (140) to the inequality in (142) gives
⏐
⏐
⏐
⏐
∫
¯C+
a +2iπ
gN (z) e
N
2iπ L+(z,−2iπ,iπ)dz
⏐
⏐
⏐
≤N (l′
0+iπ)/2iπ max
¯C+
a +2iπ
( |gN (z)|
N (l′
0+iπ)/2iπ
)
·ON →∞(1) ·
∫ 2π
2π−sN
e
N
2π Cl2(t)dt
=N (l′
0+iπ)/2iπON →∞
( 1
N
)
.(147)
where the asymptotics of the last integral were obtained in S ection 4.3.1. On the other hand,
as in (146) we have:
(148)
∫
C+
a
gN (z)e
N
2iπ L+(z,−2iπ,iπ)dz ∼N →+∞i
l′
0
2iπ + 3
2 · N
l′
0
2iπ − 1
2 + α−
2
Log(N )
( 1
α−π
) l′
0
2iπ + 1
2 + α−
2
vN.
For future reference in Step 6, we note that (147) is negligib le with respect to (148), since
α− > 0 and ( vN ) is bounded from below by a constant > 0, and (148) tends to + ∞ as
N → +∞, since R( l′
0
2iπ − 1
2 )> 0 by our choice a0 ≥ 2.
Step 5: Checking the assumptions of Proposition 5.4 away fro m the ends is−
N , is+
N .
By Steps 2 to 4 the function gN (z)e
N
2iπ L±(z,−2iπ,ℓ) is holomorphic on a domain where we can
deform the contour C −
N or C +
N to those described in Step 2 (Figure 7 or [ is−
N,is +
N ]), Step 3
(Figure 8), and Step 4. By Cauchy’s theorem the integral IN,±(ℓ) is unchanged if one replaces
its contour by any of these ones.
By following the analysis of Sections 4.4–4.5 we now check th at the hypothesis of Proposition
5.4(ii) are satisﬁed by the integral IN,±(ℓ), restricted to subcontours that stay away from
the ends is−
N and is+
N in the situations of Figures 7 and 8, and by the integral IN,−(iπ) on
a subcontour of [ is−
N,is +
N ]. Namely, these subcontours go from 2 iπ −iη′ to −iη in Figure 8,
and from iη to 2iπ −iη′ in Figure 7, where η > s−
N , η′ > s+
N , and one deformes slightly the
contour near s−
N and 2iπ −is+
N so that it goes ﬁrst vertically to iη and ﬁnishes vertically from
2iπ −iη′ to 2iπ −is+
N , respectively. The subcontour goes from iη to 2iπ −iη′ vertically in
the situation of the integral IN,−(iπ).
Recall that the critical point z0 of L±(z, −2iπ,ℓ ), where ℓ = iπ or 2iπ, is: z0 = iπ
3 for
L−(z; −2iπ,iπ ), z0 = Log((
√
5 − 1)/2) for L+(z; −2iπ, 2iπ), and z0 = Log((
√
5 + 1)/2 +iπ
for L−(z; −2iπ, 2iπ).
In each case gN (z)e
N
2iπ L±(z,−2iπ,ℓ) is holomorphic in a neighborhood of z0, and by the formulas
(120) and (135) we see immediately that it is non vanishing at z = z0, since ρ(z0) ⁄= 0. In
Lemma 3.5 we proved that exp
(1
N Ψu0,N (z0)
)
converges uniformly to 1 on compact neigh-
borhoods of z0 inU , and from (130) and the deﬁning formula of Iu0,N (z) one ﬁnds easily an
62 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
upper bound for |RN (z)|, independent of N , in a suﬃciently small compact neighborhood of
z0. Hence the hypothesis of Proposition 5.4(ii) are satisﬁed i n each case.
Step 6: Comparing the asymptotics on subcontours, and concl usion.
Here we combine the Steps 1 to 5 to describe asymptotics of the integralsIN,±(ℓ).
Consider the integral IN,+(iπ). The analysis of Section 4.4.2 can be repeated verbatim for
the integral restricted to the subcontour from 2 iπ −υ′′ to −υ′′ in Step 4 (Figure 3). This
analysis shows again that this integral is a ON →+∞(1) summand of IN,+(iπ). By Step 4 the
integrals (147) and (148), along the arcs ¯C +
a + 2iπ andC +
a , have distinct growths, and (148)
dominates (147) and is not bounded. Then the integral (148) d ominates the asymptotics of
IN,+(iπ), which are therefore of the form stated in Lemma 5.5.
Consider the integral IN,−(iπ). By Step 5 and Proposition 5.4(ii) the analysis of Section
4.4.2 can be repeated verbatim for the integral restricted t o the subcontour [ iη, 2iπ −iη′].
This analysis shows again that this integral grows exponent ially, with growth rate equal to
1
