---
doc_id: arxiv-1705.01853v2
doc_title: "Line Operators in the Standard Model David Tong"
section_id: sec-010-31-theta-angles
section_title: "Theta Angles"
section_number: 3.1
pages: 11-13
source_pdf: 1705.01853v2.pdf
source_sha256: 895e0b22c93bca1b
doc_brief: "Line Operators in the Standard Model David Tong — There is an ambiguity in the gauge group of the Standard Model."
---
We can now ask how the spectrum of line operators changes as we va ry the θ-angles.
A priori, there are three such angles, one for each factor of the g auge group. We call
these θ˜Y , θ2 and θ3. Within the framework discussed in this paper it makes sense to
ask how the line operators vary under each of these.
Before we proceed, it is worth reviewing the role of theta angles in th e Standard
Model. The most discussed is the QCD theta angle, θ3. Bounds on strong CP violation
restrict θ3 ≲ 10−10. (The value θ3 = π also preserves CP but the meson spectrum
derived from the chiral Lagrangian diﬀers from the observed value s [14, 15].)
It is usually stated that the weak theta angle, θ2, can be rotated away in the Standard
Model . This follows from the existence of an anomalous global symme try B +L → ZNf
where Nf = 3 is the number of generations. We will revisit this below.
Finally, there is very little, if any, discussion of the theta angle for hy percharge
θ˜Y . This changes neither the spectrum nor correlation functions of lo cal operators.
Nonetheless, it can play a role in the presence of magnetic monopoles or boundaries of
space. Correspondingly, it also changes the spectrum of line opera tors.
Here we start by ignoring the eﬀects of global anomalies and focus o n the spectrum
of line operators and the Witten eﬀect. As reviewed in Section 2, for simple gauge
groups, a quotient by the centre has the eﬀect of extending the r ange of θ. In the
present context, the quotient Γ = Zp extends the range of the Abelian theta angle
only4. We have
θ2, θ 3 ∈ [0, 2π) and θ˜Y ∈ [0, 2πp 2) (3.2)
This is simplest to see for the case of Z2 and Z3 where the gauge group is G = U(2) ×
SU (3) and G = SU (2) × U(3) respectively. Here
U(N) = U(1) × SU (N)
ZN
We denote the U(1) gauge ﬁeld as ˜a, the SU (N) gauge ﬁeld as a and their corresponding
ﬁeld strengths as ˜f and f . The theta terms for the U(1) × SU (N) theory are
Sθ = θN
16π 2
∫
tr (f ⋆f ) +
˜θ
16π 2
∫
˜f ⋆˜f
4For the hypercharge with normalisation Y = ˜Y / 6, the range is 36 θY ∈ [0, 2πp 2), so θY ∈ [0, 2π )
when Γ = Z6.
10
To describe the U(N) theory, we introduce the canonically normalised gauge ﬁeld
b = a + ˜a1N
with corresponding ﬁeld strength g. The theta terms can then be written as
Sθ = θN
16π 2
∫
tr (g ⋆g) +
˜θ − N θN
16π 2N 2
∫
(tr g) ⋆(tr g) (3.3)
We see that θN ∈ [0, 2π) while ˜θ ∈ [0, 2πN 2).
Similarly, for the Z6 quotient, one can check that the spectrum of line operators is
invariant under the identiﬁcation (3.2), with ˜θ ∈ [0, 72π).
(Some examples with the Z6 quotient: the theory with θ2 = 0, θ3 = 2π and Abelian
theta angle ˜θ has the same spectrum of line operators as the theory with θ2 = θ3 = 0
and Abelian theta angle ˜θ′ = ˜θ + 48π; the theory with θ2 = 2 π, θ3 = 0 and Abelian
theta angle ˜θ has the same spectrum of line operators as the theory with θ2 = θ3 = 0
and Abelian theta angle ˜θ′ = ˜θ + 36π.)
Time Reversal Invariant States
It is interesting to ask: for which values of the θ angles does the theory respect time
reversal invariance or, equivalently, CP? There are eight possibilities, two for each factor
of the gauge group.
Γ = 1:
All theta angles have periodicity 2 π. It is well known that θ2, θ 3 and ˜θ can
each take values 0 or π.
Γ = Z2: Here ˜θ ∈ [0, 8π). The values θ3 = 0 and π are both time reversal invariant.
We can read oﬀ the U(2) θ angles from (3.3). When θ2 = 0, ˜θ = 0 or 4 π; when θ2 = π
then ˜θ = 2π or 6 π.
Γ = Z3: Here ˜θ ∈ [0, 18π). The values θ2 = 0 and π are both time reversal invariant.
The U(3) theta angles can be θ3 = 0 and ˜θ = 0 or 9 π. Alternatively, we can have
θ3 = π and ˜θ = 3π or 12 π.
Γ = Z6: We have ˜θ ∈ [0, 72π). The time reversal invariant theories have
• θ2 = 0 and θ3 = 0 and ˜θ = 0 or 36 π.
• θ2 = 0 and θ3 = π and ˜θ = 12π or 48 π.
• θ2 = π and θ3 = 0 and ˜θ = 18π or 54 π.
• θ2 = π and θ3 = π and ˜θ = 30π or 66 π.
11
The Eﬀect of Global Anomalies
The chiral nature of the Standard Model means that the theta an gle θ2 can be rotated
away. Here we review this argument. In fact, as we will see, a more c areful statement
is that a linear combination of θ2 and ˜θ can be removed.
In general, theta angles can be rotated away if the theory admits a continuous global
symmetry which suﬀers a mixed anomaly with the gauge symmetry. Th is arises most
naturally in the presence of a massless chiral fermion. (For example , a massless up
quark provides an elegant solution to the strong CP problem, albeit o ne that appears
not to be favoured by Nature). However, even with non-vanishing Yukawa couplings, so
that all fermions have a mass, the Standard Model still admits two g lobal symmetries:
these are lepton and baryon number:
lL qL eR uR dR νR
L +1 0 +1 0 0 +1
B 0 + 1
3 0 + 1
3 + 1
3 0
where, for once, we have bowed to tradition and employed the non- integer normalisation
of the baryon current. Both L and B suﬀer mixed anomalies with both SU (2) and
U(1) ˜Y . They are
∑
L SU (2)2 =
∑
B SU (2)2 = −1 and
∑
L ˜Y 2 =
∑
B ˜Y 2 = +18
We recover the well known fact that the combination B − L is non-anomalous. Mean-
while, under a transformation of L, parameterised by α L, we have
L : θ2 → θ2 − α L , ˜θ → ˜θ + 18α L
The linear combination ˜θ + 18θ2 is physical and cannot be rotated away. We will see
the interpretation of this shortly.
