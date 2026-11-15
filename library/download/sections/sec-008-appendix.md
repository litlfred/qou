---
doc_id: download
doc_title: "Concentration of empirical distribution functions with applications to non-i.i.d. models"
section_id: sec-008-appendix
section_title: "Appendix"
section_number: null
pages: 26-28
source_pdf: Download.pdf
source_sha256: ca9639465b08d34c
toc_source: outline
doc_brief: "Concentration of empirical distribution functions with applications to non-i.i.d. models — 12 sections: Front matter; Introduction; Empirical Poincaré inequalities"
---
Here we recall some facts about Poincaré-type and log-Sobolev inequalities. While Lemmas 2.2
and 5.3 list some of their consequences, one might wonder which measures actually satisfy these
analytic inequalities. Many interesting examples can be constructed with the help of the following
elementary proposition.
Proposition A1. Let μ1,...,μN be probability measures on R satisfying PI(σ 2) (resp.,
LSI(σ 2)). The image μ of the product measure μ1 ⊗··· ⊗μN under any map T :RN →Rn
with ﬁnite Lipschitz seminorm satisﬁes PI(σ 2∥T ∥2
Lip) (resp., LSI(σ 2∥T ∥2
Lip)).
On the real line, disregarding the problem of optimal constants, Poincaré-type inequalities
may be reduced to Hardy-type inequalities with weights. Necessary and sufﬁcient conditions for
a measure on the positive half-axis to satisfy a Hardy-type inequality with general weights were
found in the late 1950s in the work of Kac and Krein [27]. We refer the interested reader to [35]
and [34] for a full characterization and an account of the history; here, we just recall the principal
result (see also [7]).
Let μ be a probability measure on the line with median m, that is, μ(−∞,m) ≤1
2 and
μ(m,+∞) ≤1
2. Deﬁne the quantities
A0(μ) = sup
x<m

μ(−∞,x)
 x
−∞
dt
pμ(t)

,
A1(μ) = sup
x>m

μ(x,+∞)
 +∞
x
dt
pμ(t)

,
where pμ denotes the density of the absolutely continuous component of μ (with respect
to Lebesgue measure) and where we set A0 = 0 (resp., A1 = 0) if μ(−∞,m) = 0 (resp.,
μ(m,+∞) = 0). We then have the following proposition.
Proposition A2. The measure μ on R satisﬁes PI(σ 2) with some ﬁnite constant if and only if
both A0(μ) and A1(μ) are ﬁnite. Moreover, the optimal value of σ 2 satisﬁes
c0

A0(μ) + A1(μ)

≤σ 2 ≤c1

A0(μ) + A1(μ)

,
where c0 and c1 are positive universal constants.
Necessarily, μ must have a non-trivial absolutely continuous part with density which is posi-
tive almost everywhere on the supporting interval.
For example, the two-sided exponential measure μ0, with density 1
2e−|x|, satisﬁes PI(σ 2)
with σ 2 = 4. Therefore, any Lipschitz transform μ = μ0T −1 of μ0 satisﬁes PI(σ 2) with
σ 2 = 4∥T ∥2
Lip. The latter property may be expressed analytically in terms of the reciprocal to
the so-called isoperimetric constant,
H(μ) = essinf
x
pμ(x)
min{Fμ(x),1 −Fμ(x)},
where Fμ(x) = μ(−∞,x] denotes the distribution function of μ and pμ the density of its ab-
solutely continuous component. Namely, as a variant of the Mazya–Cheeger theorem, we have
that PI(σ 2) is valid with σ 2 = 4/H(μ)2; see [9], Theorem 1.3.
To roughly describe the class of measures in the case, where μ is absolutely continuous and
has a positive, continuous well-behaving density, one may note that H(μ) and the Poincaré
constant are ﬁnite, provided that the measure has a ﬁnite exponential moment. In particular,
any probability measure with a logarithmically concave density satisﬁes PI(σ 2) with a ﬁnite σ;
see [4].
As for logarithmic Sobolev inequalities, we have a similar picture, where the standard
Gaussian measure represents a basic example and plays a similar role as the two-sided expo-
nential distribution for Poincaré-type inequalities. A full description on the real line, resembling
Proposition A2, was given in [6]. Namely, for one-dimensional probability measure μ, with pre-
vious notation, we deﬁne the quantities
B0(μ) = sup
x<m

μ(−∞,x)log
1
μ(−∞,x)
 x
−∞
dt
pμ(t)

,
B1(μ) = sup
x>m

μ(x,+∞)log
1
μ(x,+∞)
 +∞
x
dt
pμ(t)

.
We then have the following proposition.
Proposition A3. The measure μ on R satisﬁes LSI(σ 2) with some ﬁnite constant if and only if
B0(μ) and B1(μ) are ﬁnite. Moreover, the optimal value of σ 2 satisﬁes
c0

B0(μ) + B1(μ)

≤σ 2 ≤c1

B0(μ) + B1(μ)

,
where c0 and c1 are positive universal constants.
In particular, if μ has a log-concave density, then LSI(σ 2) is satisﬁed with some ﬁnite constant
if and only if μ has sub-Gaussian tails.
