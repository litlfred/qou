---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-018-tangent-point-energy
section_title: "Tangent-point energy"
section_number: null
pages: 40-41
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
Theorem 5.6 Let 𝑝∈(4, 5), 𝑠= 𝑠(𝑝) = (𝑝−3)/2, and z ∈R𝑛. Let U be an open subset of the
manifolds A1+𝑠or A1+𝑠
z
. Then every critical knot 𝛾of TP(𝑝,2) on U is of class 𝐶∞(R/Z, R𝑛).
Proof. By substituting the splitting (4.10) into (5.1) for E = TP(𝑝,2), we get the following
criticality equation:
2𝑄TP(𝛾, ℎ) = 𝐹𝛾ℎ−𝑅TP
𝛾ℎ
for all ℎ∈𝐻1+𝑠(R/Z, R𝑛),
where
𝐹𝛾ℎ≔D(TP(𝑝,2))𝛾𝑌𝛾⟨𝛾′, ℎ′⟩.
Now suppose that we know already that 𝛾∈𝐻𝑡(R/Z, R𝑛) for some 𝑡≥1 + 𝑠. Then [15,
Proposition 4.3] shows that
𝑅TP
𝛾
∈𝐻𝑡−1−𝑝/2−𝜀(R/Z, R𝑛)
for all 𝜀> 0.
Moreover, by Lemma 4.7,
𝐹𝛾∈𝐻𝑡−1−𝑝/2−𝜀(R/Z, R𝑛)
for all 𝜀> 0.
Combining this, we see that
𝑄TP(𝛾, ·) ∈𝐻𝑡−1−𝑝/2−𝜀(R/Z, R𝑛) for all 𝜀> 0.
By elliptic regularity (see the second part of Lemma 4.6), 𝛾must have 𝑝−1 derivatives more
than QTP(𝛾, ·), thus
𝛾∈𝐻𝑡−1−𝑝/2−𝜀+(𝑝−1)(R/Z, R𝑛) = 𝐻𝑡+(𝑝−4)/2−𝜀(R/Z, R𝑛)
for all 𝜀> 0.
Since 𝑝∈(4, 5), we may fix 𝜀such that 0 < 𝜀< (𝑝−4)/2, e.g., 𝜀= (𝑝−4)/4, and get a
strict increase in regularity. Starting at 𝑡= 1 + 𝑠and iterating this, we obtain
𝛾∈
Ù
𝑡≥1+𝑠
𝐻𝑡(R/Z, R𝑛) = 𝐶∞(R/Z, R𝑛).
□
40
Since TP(𝑝,2) is positively (4 −𝑝)-homogeneous we obtain length-constrained critical knots as
before, with an explicit bound on the scalar Lagrange multiplier.
Corollary 5.7 (TP( 𝒑,2) critical knots) Let z ∈R𝑛and M ∈{A1+𝑠, A1+𝑠
z
}.
Any critical
knot 𝛾of the restricted energy TP(𝑝,2) 

M is critical for TP(𝑝,2) −𝜆L on the open subset
𝐻1+𝑠
ir
(R/Z, R𝑛) ⊂𝐻1+𝑠(R/Z, R𝑛) for 𝜆= (4 −𝑝) TP(𝑝,2)(𝛾) ≤(4 −𝑝) TPmin, where TPmin is
defined in (5.6).
Remark 5.8 In [63, Corollary 1.3] it was shown that critical points of integral Menger cur-
vature intM(𝑝,2) for 𝑝∈( 3
7, 8
7) under a fixed-length constraint are even real-analytic. The
technique of that proof, however, does not seem to carry over to arclength-constrained critical
knots, but it relies on a splitting of the differential D intM(𝑝,2) provided in [17, Section 4].
This splitting is of the same kind as that of D TP(𝑝,2), 𝑝∈(4, 5), see (4.10), that we frequently
used in the present paper. Thus, the same method applies to the tangent-point energies. As
a consequence, length constrained TP(𝑝,2)-critical knots, and therefore by Corollary 5.7 also
TP(𝑝,2) |M-critical knots, are real-analytic for M ∈{A1+𝑠, A1+𝑠
z
} for any z ∈R𝑛, where
𝑠= 𝑠(𝑝) = (𝑝−3)/2 𝑝∈(4, 5).
