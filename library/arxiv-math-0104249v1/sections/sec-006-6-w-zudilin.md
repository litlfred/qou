---
doc_id: arxiv-math-0104249v1
doc_title: "IRRA TIONALITY OF V ALUES OF ZET A-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive pr"
section_id: sec-006-6-w-zudilin
section_title: "W. ZUDILIN"
section_number: 6
pages: 6-7
source_pdf: 0104249v1.pdf
source_sha256: c2fcdefc73b8df24
doc_brief: "IRRATIONALITY OF VALUES OF ZETA-FUNCTION W. Zudilin 1. Introduction. The irrationality of values of the zeta-function ζ(s) at odd integers s ≥ 3 is one of the most attractive problems in number theory"
---
Lemma 4. Suppose the root µ1 ∈ (c, +∞) of the polynomial (18) satisﬁes the
condition
µ1 ≤c + c2 − 1
4 · min
{ b
2(a +b), 1
3c
}
. (19)
Then all solutions of equation (17) in the domain ℜ(τ ) > 0 are exhausted by the
following list :
(a) the “real” solution µ1 ±i0 for λ = ±b, where a sign ‘ +’ (a sign ‘ −’) in the
record ±i0 coinsides with the sign of λ and corresponds to upper (respectively,
lower ) bank of the cut [c, +∞);
(b) a real solution µ0 ∈ (1,c ) for λ = 0;
(c) a complex solution τλ ∈ (1,c ) for 0 < |λ| < b; in addition , the sign of ℑ(τλ )
coinsides with the sign of λ, and τλ =τ−λ .
The set of solutions of (17) generates a smooth closed curve
ℜ(f ′(τ )) = log |τ +c|b|τ − 1|a+b
|τ −c|b|τ + 1|a+b = 0 (20)
in the domain ℜ(τ )> 0; this curve is contained between two circles centered at τ =c of
radii (µ1 −c)/2, (c−µ0)/2; there holds ℜ(f ′(τ ))> 0 inside the curve and ℜ(f ′(τ ))< 0
outside it.
Proof of the claim leans on a geometric interpretation of the funct ion ℑ(f ′(τ ))
and on a description of all solutions of (17) in the whole cut τ -plane (and not only in
the domain ℜ(τ )> 0).
With the use of Lemma 4 we choose the countour Mλ to calculate asymptotics
of Jn,λ as n → ∞ in the following way. If λ >0 then the countour Mλ consists of
the vertical ray ( µ0 −i∞,µ 0], of the segment [ µ0,µ 0 +eiθ√
µ2
0 − 1 ] passing through
the saddle point τλ , and of the horizontal ray [ µ0 +eiθ √
µ2
0 − 1,e iθ√
µ2
0 − 1 + ∞];
in the case λ < 0 the contour Mλ is symmetric to M−λ with respect to real axis;
lastly, the contour M0 remains the vertical line ( µ0 −i∞,µ 0 +i∞). This choice of
the contour Mλ and an application of Laplace’s method (see, e.g., [B], § 5.7) yield
the following claim.
Lemma 5. Letλ ∈ R, |λ| ≤ b, and let τλ be the (unique) solution of equation (17)
in the domain ℜ(τ )> 0. Then there holds the asymptotic formula
|Jn,λ | = enℜ(f0(τλ ))|g(τλ )|
(2πn|f ′′(τλ )|)1/ 2 ·
(
1 +O(n−1)
)
as n → ∞,
where
f0(τ ) := f (τ ) −f ′(τ )τ = (a +b −bc)2 log 2 +bc log(τ +c) +bc log(−τ +c)
− (a +b) log(τ + 1) − (a +b) log(τ − 1).
IRRATIONALITY OF ZETA-V ALUES 7
Lemma 6. Suppose condition (19) is satisﬁed. Then for the linear forms (5) there
holds the limit relation
κ := lim sup
n→∞
log |In|
n = ℜ(f0(µ)) = log 22(a+b−bc)|µ +c|bc|µ −c|bc
|µ + 1|a+b|µ − 1|a+b , (21)
whereµ is a real root (i.e., µ1) of the polynomial (18) from the interval (c, +∞) for
b = 1, or a root of this polynomial in the domain ℑ(τ ) > 0 with a maximal possible
part ℜ(µ) for b >1. In the case b = 1 the limit superior in (21) can be replaced by
the ordinary one.
Proof. All solutions of (17) in the domain ℜ(τ ) > 0 for odd values λ = k are
simultaneously roots of the polynomial (18). A routine test shows that condition (19)
provides the increase of the function ℜ(f0(τ )) viewed as a function of ℜ(τ ) (or, equiv-
alently, as a function of λ) on the curve (20) in the domain ℜ(τ )> 0, ℑ(τ ) ≥ 0; hence
only asymptotics of Jn, ±1 ifb = 1 and of Jn, ±(b−2) ifb> 1 inﬂuence on asymptotics of
the integral (15). The application of Lemmas 5 and 3 yields th e desired relation (21).
