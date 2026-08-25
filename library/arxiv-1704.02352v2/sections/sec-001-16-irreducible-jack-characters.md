---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-001-16-irreducible-jack-characters
section_title: "Irreducible Jack characters"
section_number: 1.6
pages: 3-5
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
other, more general, family (χ(α)
λ ) of irreducible characters in (1.1). Our
starting point is the family of Jack polynomials J (α)
λ [Jac71] which can be
regarded as a deformation of the family of Schur polynomials ; a deforma-
tion that depends on the parameter α > 0. We use the normalization of Jack
polynomials from [Mac95, Section VI.10].
We expand Jack polynomial in the basis of power-sum symmetri c func-
tions:
(1.4) J (α)
λ =
∑
π
θ(α)
π (λ) pπ.
The above sum runs over partitions π such that |π| = |λ|. For a given
integer n ≥ 1, any Y oung diagram λ ∈ Yn and any partition π ∈ P n we
deﬁne the irreducible Jack character χ(α)
λ as
(1.5) χ(α)
λ (π) := α− ‖ π‖
2
zπ
n! θ(α)
π (λ).
Above,
‖π‖ := |π| − ℓ(π)
4 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
denotes the length of the partition π = (π1, . . . , πl), while ℓ(π) = l denotes
its number of parts . Also, the numerical factor zλ is deﬁned by
(1.6) zλ :=
∏
i≥1
mi(λ)! imi(λ),
where mi(λ) :=
⏐
⏐{k : λk = i}
⏐
⏐is the multiplicity of i in the partition λ.
It is worth pointing out that in the special case α = 1 the corresponding
Jack character χ(1)
λ (π) = χλ(π) coincides with the irreducible character
(1.2) of the symmetric group S(n), see [Las09, DF16].
1.7. Probability measures P(α)
χ . With χλ := χ(α)
λ given by the irreducible
Jack characters, (1.1) takes the following more speciﬁc for m
(1.7) χ =
∑
λ∈Yn
P(α)
χ (λ) χ(α)
λ .
If the coefﬁcients P(α)
χ (λ) ≥ 0 are non-negative, we will say that χ is a
reducible Jack character. The resulting probability measure P(α)
χ on Yn is
in the focus of the current paper.
In the simplest example of χ := χreg given by (1.3) the corresponding
probability measure P(α)
χreg turns out to be the celebrated Jack–Plancherel
measure [Sta89, Ful04, Mat08, DF16, BGG17, Mol15] which is a one-
parameter deformation of the Plancherel measure.
1.8. Random Y oung diagrams related to Thoma’s characters. An ad-
ditional motivation for considering this particular class of random Y oung
diagrams stems from the research related to the problem of ﬁn ding ex-
tremal characters of the inﬁnite symmetric group S(∞), solved by Thoma
[Tho64]. V ershik and Kerov [VK81] found an alternative, more conceptual
proof of Thoma’s result, which was based on the observation that characters
of S(∞) are in a natural bijective correspondence with certain sequ ences
(λ1 ր λ2 ր · · · ) of growing random Young diagrams.
The original Thoma’s problem can be equivalently formulate d as ﬁnding
all homomorphisms from the ring of symmetric functions to re al numbers
which are Schur-positive, i.e. which take non-negative values on all Schur
polynomials. In this formulation the problem naturally ask s for general-
izations in which Schur polynomials are replaced by another interesting
family of symmetric functions. Kerov, Okounkov and Olshans ki [KOO98]
considered the particular case of Jack polynomials and they proved that a
direct analogue of Thoma’s result holds true also in this cas e. The main
idea behind their proof was that the probabilistic viewpoin t from the above-
mentioned work of V ershik and Kerov [VK81] can be adapted to t he new
setting of Jack polynomials. Thus, a side product of the work of Kerov,
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 5
Okounkov and Olshanski is an interesting, natural class of r andom Y oung
diagrams which ﬁts into the framework which we consider in th e current
paper, see Section 1.16 and the forthcoming paper [D ´S18] for more details.
