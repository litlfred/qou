---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-005-34-isoperimetric-constant
section_title: "Isoperimetric constant"
section_number: 3.4
pages: 20-21
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
---
Let us complete this section about some functional inequalities linked to the Stein kernel by studying
the isoperimetric constant. Recall that for a measure ν on Rd, an isoperimetric inequality is an
inequality of the form
ν+ (A) ≥c min {ν (A), 1 −ν (A)} , (41)
where c > 0, A is an arbitrary measurable set in Rd and ν+ (A) stands for the ν-perimeter of A,
deﬁned to be
ν+ (A) = lim inf
r→0+
ν (Ar) −ν (A)
r ,
withAr =
{
x ∈ Rd : ∃a ∈A, |x −a|<r
}
ther-neighborhood of A. The optimal value of c =Is (ν)
in (41) is referred to as the isoperimetric constant of ν.
The next proposition shows that existence of a uniformly bou nded Stein kernel is essentially
suﬃcient for guaranteeing existence of a positive isoperim etric constant.
Proposition 12 Assume that the probability measure ν has a connected support, ﬁnite ﬁrst moment
and continuous density p with respect to the Lebesgue measure. Assume also that its St ein kernel
τν is uniformly bounded on I (ν), ‖τν ‖∞ < +∞. Then ν admits a positive isoperimetric constant
Is (ν)> 0.
More precisely, from the proof of Proposition 12 (see below) , we can extract a quantitative
estimate of the isoperimetric constant. Indeed, under the a ssumptions of Proposition 12, denote by
qβ the quantile of order β ∈ (0, 1) of the measure ν and byµ its mean. Then, for any α ∈ (0, 1) such
that qα <µ<q 1−α , we have
Is (ν) ≥ min
{
α −1 min
x∈[qα ,q 1− α ]
{p (x)}, min {µ −qα,q 1−α −µ }
‖τν ‖∞
}
.
Measures having a uniformly bounded Stein kernel include st rongly log-concave measures - as
proved in Section 2 above -, but also smooth perturbations of the normal distribution that are
Lipschitz and bounded from below by a positive constant (see Remark 2.9 in [LNP15]). In addition,
bounded perturbations of measures having a bounded Stein kernel given by formula (6) and a density
that is bounded away from zero around its mean also have a boun ded Stein kernel. Indeed, take
κ a measure having a density pκ with connected support [ a,b ] ⊂ ¯R, a <0 < b, mean zero and a
ﬁnite ﬁrst moment so that its Stein kernel τκ is unique - up to sets of Lebesgue measure zero - and
given by formula (6). Assume also that the density pκ is bounded away from zero around zero, that
is there exists L,δ > 0 such that [ −δ,δ ] ⊂ (a,b ) and inf x∈[−δ,δ ]pκ (x) ≥ L > 0. Now, consider a
functionρ on R such thatC −1 ≤ρ (x) ≤C for anyx ∈ (a,b ) and for some constantC >0, such that
p (x) = ρ (x)pκ (x) is the density of a probability measure ν with support [a,b ]. As ν has a ﬁnite
ﬁrst moment, it also admits a Stein kernel τν, given by formula (6). Furthermore, τν is uniformly
bounded and easy computations using the formula (6) give
‖τν ‖∞ ≤C 2
(
‖τκ ‖∞ + |µ | max
{ 1
L, ‖τκ ‖∞
δ
})
,
where µ is the mean of ν.
It would be interesting to know if Proposition 12 also holds in higher dimension, but this question
remains open. A further natural question would be: does a mea sure having a Stein kernel satisfy a
weighted isoperimetric-type inequality, with a weight related to the Stein kernel? So far, we couldn’t
20
give an answer to this question. Note that Bobkov and Ledoux [BL09a, BL09b] proved some weighted
Cheeger and weighted isoperimetric-type inequalities for the generalized Cauchy and for κ-concave
distributions.
Proof. LetF be the cumulative distribution function of ν,µ be its mean and let ε> 0 be such that
[µ −ε,µ +ε] ⊂I (ν). Recall ([BH97], Theorem 1.3) that the isoperimetric cons tant associated to ν
satisﬁes
Is (ν) = ess inf
a<x<b
p (x)
min {F (x), 1 −F (x)} ,
where a<b are the edges of the support of ν. Take x ∈I (ν) such that x −µ ≥ε/ 2, then
τv (x) = 1
p (x)
∫ ∞
x
(y −µ)p (y)dy
≥ ε1 −F (x)
2p (x) ≥ ε
2
min {F (x), 1 −F (x)}
p (x) .
The same estimate holds for x ≤µ −ε/ 2 since τv (x) =p (x)−1∫ x
−∞ (µ −y)p (y)dy . Hence,
ess inf
x∈I(ν), |x−µ |≥ε/ 2
p (x)
min {F (x), 1 −F (x)} ≥ 2
ε ‖τν ‖∞
> 0 . (42)
Furthermore, we have
inf
|x−µ |≤ε/ 2
p (x)
min {F (x), 1 −F (x)} ≥ inf|x−µ |≤ε/ 2p (x)
min {F (µ −ε/ 2), 1 −F (µ +ε/ 2)} > 0 . (43)
The conclusion now follows from combining (42) and (43).
