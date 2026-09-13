---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais–Smale condition in geometric knot theory"
section_id: sec-016-bending-energy-with-tangent-point-energy
section_title: "Bending energy with tangent-point energy"
section_number: null
pages: 39-41
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
doc_brief: "On the Palais–Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy"
---
Theorem 5.3Let𝜃 >0,𝑝∈(4,5),z∈R 𝑛, and letUbe an open subset ofA2 orA 2
z. Then
every critical point ofT=𝐸 b+𝜃TP (𝑝,2) onUis of class𝐶∞(R/Z,R𝑛).
Proof.As in the proof of Theorem 5.1 we may focus onT|U-critical knots𝛾forU⊂A 2.
The criticality equation is a minor modification of (5.2):
Δ2𝛾=𝐹 𝛾−𝑅 𝛾−𝜃D(TP (𝑝,2))𝛾.(5.5)
For𝑡≥2>(𝑝−1)/2and𝛾∈A 𝑡 [15, Proposition 4.3] implies𝑅TP
𝛾 ∈𝐻 𝑡−1−𝑝/2−𝜀(R/Z,R𝑛)
for all𝜀 >0, where𝑅 TP
𝛾 appears as a remainder term in (4.10). Combining this for𝜀∈
(0,(𝑝−4)/2]with the first part of Lemma 4.6 and (4.10) leads to
D(TP(𝑝,2))𝛾∈𝐻 𝑡−(𝑝−1)(R/Z,R𝑛).
Together with (5.3) and (5.4), we obtain
Δ2𝛾∈𝐻 𝜎(𝑡−2,𝜀)−1(R/Z,R𝑛)∩𝐻 𝑡−(𝑝−1)(R/Z,R𝑛)for all𝜀>0.
By elliptic regularity, [27, Theorem 6.33], we arrive at
𝛾∈𝐻 𝜎(𝑡−2,𝜀)+3(R/Z,R𝑛)∩𝐻 𝑡−(𝑝−1)+4(R/Z,R𝑛).
Since𝑝−1<4and by choice of, say𝜀= 1
4 as in the proof of Theorem 5.1, we gain the fixed
amountmin{4−(𝑝−1), 1
4}>0in regularity for each𝑡≥2, and therefore conclude that𝛾is
smooth. □
ThepreviousresultincombinationwithTheorem3.10andLemma3.13yieldsthefollowing
corollary.
Corollary 5.4 (Critical knots under length constraint)Letz∈R 𝑛 andM ∈ {A2
z,A 2}.
Foranyfixed𝜃 >0and𝑝∈(4,5)everycriticalknot𝛾oftherestrictedenergyT

M iscritical
forT−𝜆Lon the open subset𝐻 2
ir(R/Z,R𝑛)⊂𝐻 2(R/Z,R𝑛) for some𝜆∈R.
Remark 5.5 (Homogeneous total energies)One could add a different power of the knot en-
ergy (depending on its scaling behavior) to obtain a positively homogeneous total energy as
was done in [33, (1.4)]. Here, for example, one could considerS≔𝐸b+𝜃(TP (𝑝,2)◦𝜄)4−𝑝
as a positively(−1)-homogeneous total energy, which implies by means of Theorem 3.10 that
39
𝜆=−S(𝛾)≤−𝐸 b(𝛾)≤−(2𝜋) 2.If𝛾isnon-triviallyknotted,oneevenhas𝜆<−(4𝜋) 2 dueto
the Farý-Milnor theorem [44, Corollary 4.6]. Very recently, the sharp lower bound
TPmin≔𝜋 𝑝−3
∫ 𝜋
0
sin4−𝑝𝑧d𝑧 (5.6)
forTP(𝑝,2) has been established in [24], which leads to the improved upper bound−(2𝜋)2−
𝜃TP 1/(𝑝−4)
min on𝜆, or even the strict upper bound−(4𝜋)2−𝜃TP 1/(𝑝−4)
min , if𝛾is non-trivially
knotted.
5.3. Tangent-point energy
Theorem 5.6Let𝑝∈(4,5),𝑠=𝑠(𝑝)=(𝑝−3)/2,andz∈R 𝑛. LetUbeanopensubsetofthe
manifoldsA 1+𝑠 orA 1+𝑠
z . Then every critical knot𝛾ofTP(𝑝,2) onUis of class𝐶∞(R/Z,R𝑛).
Proof.By substituting the splitting (4.10) into (5.1) forE=TP (𝑝,2), we get the following
criticality equation:
2𝑄TP(𝛾,ℎ)=𝐹 𝛾ℎ−𝑅 TP
𝛾 ℎfor allℎ∈𝐻 1+𝑠(R/Z,R𝑛),
where
𝐹𝛾ℎ≔D(TP (𝑝,2))𝛾𝑌𝛾⟨𝛾′,ℎ′⟩.
Now suppose that we know already that𝛾∈𝐻 𝑡(R/Z,R𝑛)for some𝑡≥1+𝑠. Then [15,
Proposition 4.3] shows that
𝑅TP
𝛾 ∈𝐻 𝑡−1−𝑝/2−𝜀(R/Z,R𝑛)for all𝜀>0.
Moreover, by Lemma 4.7,
𝐹𝛾∈𝐻 𝑡−1−𝑝/2−𝜀(R/Z,R𝑛)for all𝜀>0.
Combining this, we see that
𝑄TP(𝛾,·)∈𝐻 𝑡−1−𝑝/2−𝜀(R/Z,R𝑛)for all𝜀>0.
By elliptic regularity (see the second part of Lemma 4.6),𝛾must have𝑝−1derivatives more
thanQ TP(𝛾,·), thus
𝛾∈𝐻 𝑡−1−𝑝/2−𝜀+(𝑝−1)(R/Z,R𝑛)=𝐻 𝑡+(𝑝−4)/2−𝜀(R/Z,R𝑛)for all𝜀>0.
Since𝑝∈(4,5), we may fix𝜀such that0< 𝜀 <(𝑝−4)/2, e.g.,𝜀=(𝑝−4)/4, and get a
strict increase in regularity. Starting at𝑡=1+𝑠and iterating this, we obtain
𝛾∈
Ù
𝑡≥1+𝑠
𝐻𝑡(R/Z,R𝑛)=𝐶 ∞(R/Z,R𝑛).
□
40
SinceTP(𝑝,2) ispositively(4−𝑝)-homogeneousweobtainlength-constrainedcriticalknotsas
before, with an explicit bound on the scalar Lagrange multiplier.
Corollary 5.7 (TP( 𝒑,2) critical knots)Letz∈R 𝑛 andM ∈ {A1+𝑠,A 1+𝑠
z }. Any critical
knot𝛾of the restricted energyTP (𝑝,2) 

M is critical forTP(𝑝,2)−𝜆Lon the open subset
𝐻1+𝑠
ir (R/Z,R𝑛)⊂𝐻 1+𝑠(R/Z,R𝑛) for𝜆=(4−𝑝)TP (𝑝,2)(𝛾)≤(4−𝑝)TP min,whereTP min is
defined in(5.6).
Remark 5.8In [63, Corollary 1.3] it was shown that critical points of integral Menger cur-
vatureintM (𝑝,2) for𝑝∈ ( 3
7, 8
7)under a fixed-length constraint are even real-analytic. The
technique of that proof, however, does not seem to carry over to arclength-constrained critical
knots, but it relies on a splitting of the differentialD intM(𝑝,2) provided in [17, Section 4].
ThissplittingisofthesamekindasthatofD TP (𝑝,2),𝑝∈(4,5),see(4.10),thatwefrequently
used in the present paper. Thus, the same method applies to the tangent-point energies. As
a consequence, length constrainedTP(𝑝,2)-critical knots, and therefore by Corollary 5.7also
TP(𝑝,2)|M-critical knots, are real-analytic forM ∈ {A1+𝑠,A 1+𝑠
z }for anyz∈R 𝑛, where
𝑠=𝑠(𝑝)=(𝑝−3)/2𝑝∈(4,5).
