---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-016-37-the-spectral-action-and-the-asymptotic-expans
section_title: "The spectral action and the asymptotic expansion"
section_number: 3.7
pages: 30-34
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
In this section we compute the spectral action for the inner ﬂuctuations of the product
geometry M × F.
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
31
Theorem 3.13. The spectral action is given by
S
=
1
π2 (48 f4 Λ4 −f2 Λ2 c + f0
4 d)
Z √g d4x
(3.41)
+
96 f2 Λ2 −f0 c
24π2
Z
R √g d4x
+
f0
10 π2
Z
(11
6 R∗R∗−3 Cµνρσ Cµνρσ) √g d4x
+
(−2 a f2 Λ2 + e f0)
π2
Z
|ϕ|2 √g d4x
+
f0
2 π2
Z
a |Dµϕ|2 √g d4x
−
f0
12 π2
Z
a R |ϕ|2 √g d4x
+
f0
2 π2
Z
(g2
3 Gi
µν Gµνi + g2
2 F α
µν F µνα + 5
3 g2
1 Bµν Bµν) √g d4x
+
f0
2 π2
Z
b |ϕ|4 √g d4x
where
R∗R∗= 1
4ǫµνρσǫαβγδRαβ
µν Rγδ
ρσ
is the topological term that integrates to the Euler characteristic. The coeﬃcients (a, b, c, d, e)
are deﬁned in (3.16) and Dµϕ is deﬁned in (3.36).
Proof. To prove Theorem 3.13 we use (3.33) and we apply Gilkey’s theorem (see Theorem 6.1
below) to compute the spectral action. By Remark 6.2 below, the relevant term is −1
6R + E,
which is the sum
E′ = −R
6 id + E = ( R
12id −14 ⊗(D0,1)2) −
X
µ<ν
γµγν ⊗Fµν + i γ5 γµ ⊗M(Dµ ϕ).
(3.42)
We need to compute the sum
Σ = f2
8 π2 Λ2Tr(E′) +
f0
32 π2 Tr((E′)2).
(3.43)
Lemma 3.14. The term Σ in (3.43) is given by
Σ
=
4 f2
π2 Λ2 R −f2
2 π2 Λ2 Tr((D0,1)2) +
f0
8 π2 Tr(M(Dµ ϕ)2)
(3.44)
+
f0
8 π2 Tr(( R
12 −(D0,1)2)2) +
f0
16 π2 Tr(FµνFµν).
Proof. The contribution of Tr(E′) is only coming from the ﬁrst term of (3.42), since the trace
of the two others vanishes due to the Cliﬀord algebra terms. The coeﬃcient of f2 Λ2
π2 R is
1
8 · 1
12 · 4 · 96 = 4. To get the contribution of Tr((E′)2), notice that the three terms of the sum
(3.42) are pairwise orthogonal in the Cliﬀord algebra, so that the trace of the square is just
the sum of the three contributions from each of these terms. Again the factor of 4 comes
from the dimension of spinors and the summation on all indices µν gives a factor of two in
the denominator for
f0
16 π2.
32
CHAMSEDDINE, CONNES, AND MARCOLLI
Notice also that the curvature Ωµν of the connection ∇is independent of the additional term
D(0,1). We now explain the detailed computation of the various terms of the spectral action.
3.7.1. Λ4-terms.
The presence of the additional oﬀ-diagonal term in the Dirac operator of the ﬁnite geometry
adds two contributions to the cosmological term of [8]. Thus while the dimension N = 96
contributes by the term
48
π2 f4 Λ4
Z √g d4x ,
we get the additional coeﬃcients
−f2
π2 Λ2 Tr(Y ∗
RYR) = −c f2
π2 Λ2,
which are obtained from the second term of (3.44), using (3.14). Finally, we also get
f0
4 π2 Tr((Y ∗
RYR)2) = d f0
4 π2 ,
which comes from the ﬁfth term in (3.44). Thus, the cosmological term gives
1
π2 (48 f4 Λ4 −f2 Λ2 Tr(Y ∗
RYR) + f0
4 Tr((Y ∗
RYR)2))
Z √g d4x .
(3.45)
3.7.2. Riemannian curvature terms.
The computation of the terms that only depend upon the Riemann curvature tensor is the
same as in [8]. It gives the additive contribution
1
π2
Z
(4 f2 Λ2 R −3
10 f0 Cµνρσ Cµνρσ)√g d4x ,
(3.46)
together with topological terms. Ignoring boundary terms, the latter is of the form
11 f0
60 π2
Z
R∗R∗√g d4x.
(3.47)
There is, however, an additional contribution from the fourth term of (3.44). Using (3.14),
this gives
−f0
48 π2 R Tr((D0,1)2) = −f0
12 π2 a R |ϕ|2 −
f0
24 π2 c R .
(3.48)
Notice the presence of the terms in R |ϕ|2 (cf. [23] equation 10.3.3).
3.7.3. Scalar minimal coupling.
These terms are given by
f0
8 π2 Tr(M(Dµ ϕ)2) =
f0
2 π2 a |Dµ ϕ|2
(3.49)
using (3.32) and (3.44).
Notice that there is a slight change of notation with respect to [7] since we are using the
Higgs doublet ˜H instead of H with the notations of [7].
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
33
3.7.4. Scalar mass terms.
There are two contributions with opposite signs. The second term in (3.44) i.e.
−f2
2 π2 Λ2 Tr((D0,1)2)
gives, using (3.14), a term in
−2 f2
π2 Λ2 a |ϕ|2 .
The fourth term in (3.44) gives, using (3.15),
f0
8 π2 8 e |ϕ|2 = e f0
π2 |ϕ|2.
Thus, the mass term gives
1
π2 (−2 a f2 Λ2 + e f0) |ϕ|2 .
(3.50)
3.7.5. Scalar quartic potential.
The only contribution, in this case, comes from the fourth term in (3.44) i.e. from the term
f0
8 π2 Tr((D0,1)4).
Using (3.15), this gives
f0
2 π2 b |ϕ|4 .
(3.51)
3.7.6. Yang-Mills terms.
For the Yang-Mills terms the computation is the same as in [8]. Thus, we get the coeﬃcient
f0
24π2 in front of the trace of the square of the curvature. For the gluons, i.e. the term Gi
µν Gµνi,
we get the additional coeﬃcient 3 · 4 · 2 = 24, since there are three generations, 4 quarks per
generation (uR, dR, uL, dL), and a factor of two coming from the sectors Hf and H ¯f. In other
words, because of the coeﬃcient g3
2 , we get
f0 g2
3
4π2 Tr(Gµν Gµν) = 2 f0 g2
3
4π2 Gi
µν Gµν
i
= f0 g2
3
2π2 Gi
µν Gµν
i ,
where we use (3.26). For the weak interaction bosons W α we get the additional coeﬃcient
3 · 4 · 2 = 24 with the 3 for 3 generations, the 4 for the 3 colors of quarks and 1 lepton per
isodoublet and per generation (ujL, djL, νL, eL), and the factor of 2 from the sectors Hf and
H ¯f. Thus, using Tr(σaσb) = 2δab, we obtain the similar term
f0 g2
2
4π2 Tr(Fµν F µν) = 2 f0 g2
2
4π2 F a
µν F µν
a
= f0 g2
2
2π2 F a
µν F µν
a .
For the hypercharge generator Bµ we get the additional coeﬃcient
2 · (((4
3)2 + (2
3)2 + 2 (1
3)2) · 3 + (22 + 2)) · 3 = 80,
which gives an additional coeﬃcient of 10
3 in the corresponding term
10
3
f0 g2
1
4π2 Bµν Bµν = 5
3
f0 g2
1
2π2 Bµν Bµν.
34
CHAMSEDDINE, CONNES, AND MARCOLLI
This completes the proof of Theorem 3.13.
