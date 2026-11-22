---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-055-appendix-b22-the-proper-calculation-of-the-footb
section_title: "Appendix B.2.2 The proper calculation of the football in time-ordered perturbation theory"
section_number: null
pages: 70-71
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
We will explain now the reason for the discrepancy between Eqs. (B.44) and (B.45). In covariant PT
theory one assumes for the interaction Hamiltonian density HI = −LI. This is strictly speaking not correct
for derivative coupling, because in that case one has HI = −LI + additional noncovariant terms.
For
relatively simple cases of derivative coupling, the additional terms are of the contact type. Now, in covariant
PT, there are also noncovariant contributions to the propagator, and it has been shown that for certain
interactions with derivative coupling these two groups of additional terms cancel. So, as a procedural matter,
in covariant PT, one can use HI = −LI and the usual covariant Feynman propagators, and everything comes
out right (cf. e. g., Ref. [225], pp. 318-323 therein).
In TOPT the story is diﬀerent. Propagators are just non-covariant energy denominators, which cancel
nothing. Therefore, the full interaction Hamiltonian including all additional terms has to be use to obtain
the same result as in covariant PT. However, in Ref. [54] HI = −LI is assumed in conjunction with TOPT.
Thus, the contributions from the additional contact terms in the Hamiltonian are missing in the calculation
of Ref. [54] and that is the reason for the discrepancy with the covariant calculation, as we will show now.
Using the notation of Ref. [225], the time-component of the current associated with the Lagrangian
density Eq. (A.43) reads
J0
b
=
1
4f 2π
¯Nτ cNϵabcπa
(B.46)
and the additional term in the interaction Hamiltonian is [cf. Eq. (12) of Ref. [51]]
Hadd
I
(t)
=
Z
d3x 1
2 (J0
b )(J0
b ) =
Z
d3x 1
2
1
16f 4π
¯Nτ cNϵabcπa ¯Nτ c′Nϵa′bc′πa′ .
(B.47)
This generates the following leading contribution to the S-matrix
⟨p′
1p′
2|S|p1p2⟩
=
(−i)
Z
dt Hadd
I
(t) = −i
Z
d4x
1
16f 4π
1
2ϵabcϵa′bc′⟨p′
1p′
2| ¯Nτ cNπa ¯Nτ c′Nπa′|p1p2⟩
=
−i
(2π)6
Z
d4x 2
1
16f 4π
1
2ϵabcϵa′bc′τ c
1τ c′
2 ei(p′
1+p′
2−p1−p2)x⟨0|πaπa′|0⟩,
(B.48)
where the factor of 2 comes from the permutation of the nucleon ﬁelds and the exchange term is left out.
For the pion ﬁelds, we obtain
⟨0|πaπa′|0⟩
=
1
(2π)3
Z
d3kd3k′
1
√4ωkωk′ ⟨0|

aa(⃗k)e−ikx + a†
a(⃗k)eikx 
aa′(⃗k′)e−ik′x + a†
a′(⃗k′)eik′x
|0⟩
=
1
(2π)3
Z
d3kd3k′
1
√4ωkωk′ δ3(⃗k −⃗k′)δaa′ =
Z
d3k
(2π)3
1
2ωk
δaa′ .
(B.49)
Hence,
⟨p′
1p′
2|S|p1p2⟩
=
−i
(2π)6
Z
d4x
1
16f 4π
ϵabcϵa′bc′τ c
1τ c′
2 ei(p′
1+p′
2−p1−p2)x
Z
d3k
(2π)3
1
2ωk
δaa′
=
−i(2π)4δ4(p′
1 + p′
2 −p1 −p2)
1
(2π)6
1
16f 4π
ϵabcϵa′bc′τ c
1τ c′
2
Z
d3k
(2π)3
1
2ωk
δaa′
=
−i(2π)4δ4(p′
1 + p′
2 −p1 −p2)
1
(2π)6
1
8f 4π
τ 1 · τ 2
Z
d3k
(2π)3
1
2
q⃗
k2 + m2π
=
−i(2π)4δ4(p′
1 + p′
2 −p1 −p2)
1
(2π)6
1
32f 4π
τ 1 · τ 2
Z
d3l
(2π)3
1
2
q⃗
l2 + 4m2π
,
(B.50)
70
where⃗k =⃗l/2 and ϵabcϵabc′τ c
1τ c′
2 = 2 τ 1 · τ 2 . From the last equation, one can read oﬀthe contribution to
the T-matrix [cf. Eqs. (A.36) and (A.35)], which is
V add = τ 1 · τ 2
1
32f 4π
Z
d3l
(2π)3
1
2
q⃗
l2 + 4m2π
(B.51)
Obviously, this additional term doesn’t depend on external momenta, only on mπ.
For the amplitude, calculated in TOPT and including all terms, we now get
V
=
VORK + V add
(B.52)
=
VORK + τ 1 · τ 2
1
32f 4π
Z
d3l
(2π)3
1
2
q⃗
l2 + 4m2π
(B.53)
=
VORK + τ 1 · τ 2
1
32f 4π
Z
d3l′
(2π)3
1
2ω+
(B.54)
=
VORK + τ 1 · τ 2
1
32f 4π
Z
d3l′
(2π)3
 1
4ω+
+
1
4ω−

(B.55)
=
VORK + τ 1 · τ 2
1
32f 4π
Z
d3l′
(2π)3
(ω+ + ω−)2
ω+ + ω−
1
4ω+ω−
(B.56)
=
τ 1 · τ 2
1
32f 4π
Z
d3l′
(2π)3
1
ω+ + ω−
(B.57)
where we used the transformations⃗l =⃗l′ +⃗q and⃗l′ 7→−⃗l′. This result is now identical to the one obtained
using covariant PT, Eq. (B.44), as it should. We note that the term, Eq. (B.51), left out in the calculation
of Ref. [54], is a contact term ∝m2
π, which aﬀects the mπ-dependence of the 2PE potential. Such terms are
relevant for the charge-dependence of the nuclear force [188] and for considerations of the chiral limit [129].
If these more subtle aspects are not of interest, then omitting the contact Eq. (B.51) is acceptable, since
contact terms with adjustable parameters are added to the theory anyhow (cf. Section 2.3).
