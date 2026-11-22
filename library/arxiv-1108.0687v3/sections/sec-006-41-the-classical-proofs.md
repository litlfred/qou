---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-006-41-the-classical-proofs
section_title: "The classical proofs"
section_number: 4.1
pages: 9-10
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
The classical proofs
To prove bounds such as (1.1), one obtains an upper bound for EeλSn, and then applies Markov’s
inequality, choosing λ optimally. Underlying the bounds on EeλSn are corresponding bounds for
compensated increments.
Let ∆denote a variable with mean zero.
Three classical exponential
bounds are as follows.
|∆| ≤1
⇒
Eeλ∆≤eλ2/2
(4.10)
∆∈[r, s]
⇒
Eeλ∆≤eλ2(s−r)2/8
(4.11)
∆∈[r, s]
⇒
Eeλ∆≤exp

(eλ −1 −λ) |rs|

,
(4.12)
when |r−s| ≤1. These are used together with the following two special cases of Markov’s inequality.
EeλX ≤ecλ2/2
=⇒
P(X ≥a) ≤e−a2/(2c)
(4.13)
EeλX ≤eb (eλ−λ−1)
=⇒
P(X > a) ≤ea

b
a + b
a+b
≤exp

−
a2
2(a + b)

(4.14)
These inequalities have appeared many times in the literature. Inequalities (4.10) and (4.13)
8
constitute the classical Azuma-Hoeﬀding inequality and imply
Eeλ(Sn−µn)
≤
eλ2n/2 ;
(4.15)
P(Sn −µn ≥a)
≤
e−a2/(2n) .
(4.16)
This is valid for any martingale with diﬀerences bounded by 1; an exposition can be found in [AS08,
Theorem 7.2.1]. The improvement to (4.11) is present already in [Hoe63], though the exposition
in [McD89] is clearer (see Lemma 5.8 therein). When the increments of Sn −µn are compensated
Bernoullis, one may take b −a = 1 rather than 2, resulting in an improvement by a factor of 4 in
the exponent,
Eeλ(Sn−µn) ≤eλ2n/8 .
(4.17)
which together with (4.13) yields (1.1). Finally, (4.12) and induction yield
Eeλ(Sn−µn) ≤e(eλ−λ−1) Vn ≤e(eλ−λ−1) µn
(4.18)
where Vn := Pn
k=1 pk(1 −pk) is the variance of Sn; together with (4.14) this implies (1.3); these
results appear, for instance, in [Fre75, (1.3)–(1.6)].
To prove the generalization to Lipschitz functions, let
Mk := E (f(X1, . . . , Xn) | X1, . . . , Xk) −Ef(X1, . . . , Xn) .
It is immediate that {Mk} is a martingale and that conditional on X1, . . . , Xk−1, the two possible
values of Mk diﬀer by at most 1. Hence, conditional on X1, . . . , Xk−1, the increment ∆k := Mk −
Mk−1 is constrained to an interval of length at most 1. Applying (4.11) then yields (1.4).
The extension of inequalities (1.1)–(1.2) to negatively cylinder dependent random variables is
established by examining the power series for eλSn. This may be expanded into positive sums of
expectations of products of powers of the variables {Xj : 1 ≤j ≤n}. Negative cylinder dependence
implies that these are bounded from above by the corresponding products of expectations. There-
fore, (4.17) and (4.18) hold when the assumption of independence is replaced by negative cylinder
dependence, whence the probability inequalities (1.1) and (1.3) hold as well. This and more is shown
in [PS97, Theorem 3.4], specializing their more general negative cylinder property to λ = 1. We
remark that only the ﬁrst inequality (1.5) in the deﬁnition of negative cylinder dependence is used
to obtain bounds on EeλSn for λ > 0, which suﬃces for the upper tail bounds. Lower tail bounds
require these inequalities for λ < 0, for which the second inequality (1.6) is required.
4.2
