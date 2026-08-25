---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-022-56-convergence-of-densities-in-probability
section_title: "Convergence of densities, in probability."
section_number: 5.6
pages: 39-41
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
sequence of random variables (S[n]
k )n converges (as n → ∞) to sk in prob-
ability; in other words for each ǫ > 0 and each integer k ≥ 0
(5.8) lim
n→∞
P
(⏐
⏐
⏐
⏐
∫
uk dPΛ n(u) −
∫
uk dPΛ ∞(u)
⏐
⏐
⏐
⏐ > ǫ
)
= 0;
in other words the sequence of random probability measures PΛ n converges
to the measure PΛ ∞ in moments, in probability .
The weak topology of probability measures can be metrized, f or exam-
ple by Lévy–Prokhorov distance π. Since the measure PΛ ∞ is uniquely
determined by its moments, convergence to PΛ ∞ in moments implies con-
vergence to the same limit in the weak topology of probability measures .
With the help of the distances d (cf. Section 5.3) and π, the latter statement
can be rephrased as follows: for each ε > 0 there exists δ > 0 such that for
any probability measure µ
d(µ, PΛ ∞) < δ =⇒ π(µ, PΛ ∞) < ε.
It follows that the sequence of random probability measures PΛ n converges
to the measure PΛ ∞ in the weak topology of probability measures, in prob-
ability, i.e. for each ε > 0
(5.9) lim
n→∞
P
(
π(PΛ n, PΛ ∞) > ε
)
= 0.
Let ǫ > 0; by adapting the proof of (5.6), we get that
(5.10)
⏐
⏐
⏐
⏐fΛ n(u0) −
∫
φǫ(u) d PΛ n(u)
⏐
⏐
⏐
⏐ ≤ ǫ.
40 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
Lévy–Prokhorov distance π metrizes the weak convergence of probability
measures; it follows that we can choose sufﬁciently small ε > 0 with the
property that for any probability measure µ on R
(5.11) π(µ, PΛ ∞) ≤ ε =⇒
⏐
⏐
⏐
⏐
∫
φǫ(u) dµ(u) −
∫
φǫ(u) dPΛ ∞(u)
⏐
⏐
⏐
⏐ < ǫ.
Equation (5.9) combined with (5.11) as well as (5.10) imply t herefore that
lim
n→∞
P
(⏐
⏐
⏐
⏐fΛ n(u0) −
∫
φǫ(u) dPΛ ∞(u)
⏐
⏐
⏐
⏐ > 2ǫ
)
= 0.
As ǫ ց 0, the integral
∫
φǫ(u) dPΛ ∞(u) converges to the density fΛ ∞(u0)
by an analogue of (5.6). In this way we proved that for each u0 the sequence
fΛ n(u0) converges to fΛ ∞(u0) in probability.
By the same type of argument as in (5.7) it follows that the sequence of
functions fΛ n converges uniformly to fΛ ∞ in probability, i.e. for each ǫ > 0
lim
n→∞
P
(
‖fΛ n − fΛ ∞‖∞ > ǫ
)
= 0
with respect to the supremum norm.
5.7. Back to Y oung diagrams. The function ωΛ ∞ which was promised in
the formulation of Theorem 1.3 is simply given by the relatio nship (5.1) for
the speciﬁc choice of fΛ := fΛ ∞, namely
ωΛ ∞(u) := 2fΛ ∞(u) + |u|.
We just ﬁnished the proof of the fact that ωΛ n converges to ωΛ ∞ in the
supremum norm as n → ∞ , in probability, thus the proof of Theorem 1.3
is completed.
6. C ENTRAL LIMIT THEOREM . P ROOF OF THEOREM 1.5
Proof of Theorem 1.5. In the light of Remark 1.6 we shall investigate the
cumulants of the form
κℓ
(
Yi1, . . . , Yiℓ
)
for the random variables (Yk) given by (1.18).
We start with the case ℓ ≥ 2. By (1.17), each Yk is equal (up to a deter-
ministic shift) to the random variable
Xk := √
n k − 1
2
∫
uk−2 ωΛ n(u) du = n− k−1
2 Sk(λn).
For ℓ ≥ 2 the cumulant κℓ is translation-invariant; it follows therefore that
(6.1)
κℓ
(
Yi1, . . . , Yiℓ
)
= κℓ
(
Xi1, . . . , Xiℓ
)
= κℓ
(
n− i1−1
2 Si1, . . . , n− iℓ−1
2 Siℓ
)
.
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 41
By Theorem 2.3( a) the approximate factorization property of (χn) is
equivalent to condition (C) which we apply in the special case when (x1, . . . , xℓ) :=
(Si1, . . . ,Siℓ). The latter implies that the right-hand side of (6.1) is of or der
O
(
n
2−ℓ
2
)
. This implies that for each ℓ ≥ 3
lim
n→∞
κℓ
(
Yi1, . . . , Yiℓ
)
= 0.
Consider now the case ℓ = 2 . If we adapt the above reasoning, we get
that the limit
lim
n→∞
κ2 (Yi1, Yi2)
exists and is ﬁnite.
We consider now the case ℓ = 1. By Theorem 2.3( b), enhanced approxi-
mate factorization property implies that for each k ≥ 2 there exist constants
a′′
k, b′′
k such that
n− k
2 ESk(λn) = a′′
k + b′′
k + o(1)
√n
as n → ∞. It follows that the cumulant
κ1(Yk) = EYk = √n
(
n− k
2 ESk(λn) − lim
m→∞
m− k
2 ESk(λm)
)
converges as n → ∞ to b′′
k (given explicitly by (3.24)).
Let us summarize the above discussion. We have proved that th e limit
lim
n→∞
κℓ
(
Yi1, . . . , Yiℓ
)
exists and is ﬁnite for any choice of ℓ ≥ 1 and i1, . . . , iℓ ≥ 2. In other words:
the joint distribution of the random variables (Yi) converges in moments as
n → ∞ to the joint distribution of an abstract family of random var iables
(Zi) with the property that all cumulants vanish: κℓ
(
Zi1, . . . , Ziℓ
)
= 0 ,
except for ℓ ≤ 2. The latter is the deﬁning property of the Gaussian distri-
bution. Since the Gaussian distribution is uniquely determ ined by its mo-
ments, it follows that (Yi) converges to (Zi) not only in moments but also
in the weak topology of probability measures, as required. □
