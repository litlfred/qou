---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-020-53-the-limiting-probability-measure-p
section_title: "The limiting probability measure P"
section_number: 5.3
pages: 37-38
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
mean value
(5.4) u ↦→EfΛ n(u)
exists, is ﬁnite, and fulﬁlls analogous bounds to (5.2). It i s the density of
the probability measure EPΛ n; the moments of this measure are given by∫
uk dEPΛ n(u) = 1
k + 1 EχnS[n]
k+2.
The topology on the set of probability measures (with all mom ents ﬁnite)
given by convergence of moments can be metrized; we denote by d the cor-
responding distance. Equation (5.3) implies that the seque nce of measures
(EPΛ n) is a Cauchy sequence in the metric space given by d; this sequence
converges therefore in moments to some probability measure which will be
denoted by PΛ ∞, in particular∫
uk dPΛ ∞(u) = 1
k + 1 sk+2.
In general, it might happen that the measure PΛ ∞ is not unique; it turns
out, however, that in the setup which we consider the measure PΛ ∞ is
uniquely determined by its moments ; we shall prove it in the following.
5.4. The measure PΛ ∞ is determined by its moments. By a minor mod-
iﬁcation of the proof of (4.10) we have
(5.5) lim
n→∞
1
n
k1+···+kℓ
2
Eχn
[
Sk1 · · · Skℓ
]
= sk1 · · · skℓ.
It follows that the relation between the families of real num bers (sk)k≥2 and
(rk)k≥2 (given by (4.7)) is given by an analogue of (3.7).
Proposition 4.4 states that there exists some constant C such that
|rk| ≤ C kkmk
for all positive integers k ≥ 2, where m is given by (1.13). Thus Lemma 4.2
gives us the following estimates for the moments of PΛ ∞:⏐
⏐
⏐
⏐
∫
uk dPΛ ∞(u)
⏐
⏐
⏐
⏐ =
⏐
⏐
⏐
⏐
1
k + 1 sk+2
⏐
⏐
⏐
⏐ ≤ C ′k+2(k + 2)m(k+2) ≤ C ′′kkmk
38 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
for some constants C ′, C′′.
We consider ﬁrst the case g = 0 . Lemma 4.1 implies immediately that
the measure PΛ ∞ is uniquely determined by its moments which concludes
the proof.
In the case g > 0 the height of each box constituting the anisotropic
Y oung diagram Λ n is equal to g + o(1) > c for some constant c > 0,
uniformly over n, cf. Section 1.11. By comparison of the areas it follows
that the length l of the bottom rectangle constituting Λ n fulﬁlls lc ≤ 1; in
particular it follows that the support of the measure PΛ n is contained in the
interval
(
−∞, 1
c
]
. It follows that an analogous inclusion holds true for the
support of the mean value EPΛ n; by passing to the limit the same is true for
PΛ ∞. It follows that Lemma 4.1 can be applied which concludes the proof.
The case g < 0 is fully analogous.
