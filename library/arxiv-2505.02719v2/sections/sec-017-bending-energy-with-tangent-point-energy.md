---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-017-bending-energy-with-tangent-point-energy
section_title: "Bending energy with tangent-point energy"
section_number: null
pages: 39-40
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
Theorem 5.3 Let 𝜃> 0, 𝑝∈(4, 5), z ∈R𝑛, and let U be an open subset of A2 or A2
z. Then
every critical point of T = 𝐸b + 𝜃TP(𝑝,2) on U is of class 𝐶∞(R/Z, R𝑛).
Proof. As in the proof of Theorem 5.1 we may focus on T |U-critical knots 𝛾for U ⊂A2.
The criticality equation is a minor modification of (5.2):
Δ2𝛾= 𝐹𝛾−𝑅𝛾−𝜃D(TP(𝑝,2))𝛾.
(5.5)
For 𝑡≥2 > (𝑝−1)/2 and 𝛾∈A𝑡[15, Proposition 4.3] implies 𝑅TP
𝛾
∈𝐻𝑡−1−𝑝/2−𝜀(R/Z, R𝑛)
for all 𝜀> 0, where 𝑅TP
𝛾
appears as a remainder term in (4.10). Combining this for 𝜀∈
(0, (𝑝−4)/2] with the first part of Lemma 4.6 and (4.10) leads to
D(TP(𝑝,2))𝛾∈𝐻𝑡−(𝑝−1)(R/Z, R𝑛).
Together with (5.3) and (5.4), we obtain
Δ2𝛾∈𝐻𝜎(𝑡−2,𝜀)−1(R/Z, R𝑛) ∩𝐻𝑡−(𝑝−1)(R/Z, R𝑛)
for all 𝜀> 0.
By elliptic regularity, [27, Theorem 6.33], we arrive at
𝛾∈𝐻𝜎(𝑡−2,𝜀)+3(R/Z, R𝑛) ∩𝐻𝑡−(𝑝−1)+4(R/Z, R𝑛).
Since 𝑝−1 < 4 and by choice of, say 𝜀= 1
4 as in the proof of Theorem 5.1, we gain the fixed
amount min{4 −(𝑝−1), 1
4} > 0 in regularity for each 𝑡≥2, and therefore conclude that 𝛾is
smooth.
□
The previous result in combination with Theorem 3.10 and Lemma 3.13 yields the following
corollary.
Corollary 5.4 (Critical knots under length constraint) Let z ∈R𝑛and M ∈{A2
z, A2}.
For any fixed 𝜃> 0 and 𝑝∈(4, 5) every critical knot 𝛾of the restricted energy T

M is critical
for T −𝜆L on the open subset 𝐻2
ir (R/Z, R𝑛) ⊂𝐻2 (R/Z, R𝑛) for some 𝜆∈R.
Remark 5.5 (Homogeneous total energies) One could add a different power of the knot en-
ergy (depending on its scaling behavior) to obtain a positively homogeneous total energy as
was done in [33, (1.4)]. Here, for example, one could consider S ≔𝐸b + 𝜃(TP(𝑝,2) ◦𝜄)4−𝑝
as a positively (−1)-homogeneous total energy, which implies by means of Theorem 3.10 that
39
𝜆= −S(𝛾) ≤−𝐸b(𝛾) ≤−(2𝜋)2. If 𝛾is non-trivially knotted, one even has 𝜆< −(4𝜋)2 due to
the Farý-Milnor theorem [44, Corollary 4.6]. Very recently, the sharp lower bound
TPmin ≔𝜋𝑝−3
∫𝜋
0
sin4−𝑝𝑧d𝑧
(5.6)
for TP(𝑝,2) has been established in [24], which leads to the improved upper bound −(2𝜋)2 −
𝜃TP1/(𝑝−4)
min
on 𝜆, or even the strict upper bound −(4𝜋)2 −𝜃TP1/(𝑝−4)
min
, if 𝛾is non-trivially
knotted.
