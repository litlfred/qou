---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-125-1c1-the-classical-burgess-bound
section_title: "1C1. The classical Burgess bound"
section_number: null
pages: 249-250
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
|S(N, H)|≪ q1/2 log q (see [Pólya 1918; Vinogradov 1918] or for a modern treatment [Iwaniec and
Kowalski 2004, §12.4]). This provides a nontrivial upper bound for|S(N, H)| as long as H≫ q1/2+ε
for someε> 0. When H is shorter than this range, the sum is considered to be “short,” and obtaining an
o(H) bound is much more difﬁcult. Conjecturally, under the generalized Riemann hypothesis, a bound as
strong as|S(0, H)|≪ε H 1/2qε should hold for all ε> 0, thus leading to a nontrivial upper bound in any
range H≫ε q3ε (see, e.g., [Iwaniec and Kowalski 2004, Equation (12.54)], or [Friedlander et al. 2013,
Equation (9.6)]; see also the more general Conjecture Cn in [Friedlander et al. 2013, §9]).
Burgess [1957; 1962; 1963; 1986] showed that for χ a primitive character to a prime modulus q, for
all integers r≥ 1, the inequality (1-1) holds, with an implied constant uniform in N, yielding a nontrivial
bound for H≫ q1/4+κ, κ> 0. More generally, with log q replaced by qε for arbitrarily smallε, Burgess
proved that this bound also holds for cube-free moduli q for all r≥ 1, and for any integer q, for r≤ 3.
The q1/4+κ “threshold” of the Burgess bound remains essentially unimproved since its inception, despite
signiﬁcant interest, due to its applications.
As a consequence of (1-1), Burgess [1963] proved a landmark subconvexity bound
⏐⏐L
( 1
2+ it,χ
)⏐⏐≪t,ε q1/4−1/16+ε
for all ε> 0, with χ a nonprincipal Dirichlet character modulo q as above; there is a corresponding
hybrid subconvexity bound
⏐⏐L
( 1
2+ it,χ
)⏐⏐≪ε(|t|q)1/4−1/16+ε of Heath-Brown [1980]. This remains the
best bound known to hold for all Dirichlet L-functions. (Special cases of the modulus q in which a better
subconvexity bound is known include: smooth moduli [Graham and Ringrose 1990; Goldmakher 2010;
Chang 2014; Irving 2016]; prime-power moduli [Postnikov 1956; Barban et al. 1964; Gallagher 1972;
Mili´cevi´c 2016], or powerful moduli [Iwaniec 1974]. Most recently, Petrow and Young [2018] proved a
better Weyl-strength subconvex estimate of size q1/6 for all cube-free moduli q.1) There is great interest
in establishing bounds of at least the strength of a “Burgess exponent” for analogous bounds in higher
rank contexts. For example, in the GL(2) setting, the “Burgess bound” for an L-function of a Hecke cusp
form g twisted by a primitive Dirichlet characterχ modulo q is
⏐⏐L
( 1
2+ it, g⊗χ
)⏐⏐≪g,ε q1/2−1/8+ε for
allε> 0 (as has been obtained in [Bykovskii 1996; Blomer and Harcos 2008]). Reaching the Burgess
exponent in new settings, or even re-proving such Burgess bounds is currently an important proving
ground for new methods (e.g., [Munshi 2018] via a GL(2) delta method and subsequently [Aggarwal
et al. 2018] via a trivial delta method).
In another direction, the Burgess bound establishes an upper bound for the least quadratic non-
residue n(p) modulo a prime p. Vinogradov conjectured that n(p)≪ε pε for everyε> 0; Burgess’s
1After the writing of this paper, Petrow and Young [2019] posted a preprint proving a Weyl-strength subconvex estimate for
all Dirichlet L-functions, without a restriction on the modulus q. This breakthrough result also implies a small improvement on
the classical Burgess upper bound (1-1) for the cases r= 2, 3 but not for larger r.
1916 Lillian B. Pierce and Junyan Xu
bound (1-1) proves n(p)≪ε p(4√e)−1+ε for anyε> 0, which held the record from [Burgess 1957] until
the quantiﬁcation in [Banks and Guo 2017]. In this vein, there are continued efforts toward the goal
of improving the inequality (1 -1) directly, such as reducing the power of the logarithm (see [Iwaniec
and Kowalski 2004, Equation (12.58) and Remark p. 329; Kerr et al. 2019]), deducing improvements in
certain special cases from conjectural improvements on the Pólya–Vinogradov inequality [Fromm and
Goldmakher 2019], and making connections to the Elliott–Halberstam conjecture and “Type II sums” in
sieve methods [Tao 2015, Conjecture 1.5, Theorem 1.6, Remark 1.7].
