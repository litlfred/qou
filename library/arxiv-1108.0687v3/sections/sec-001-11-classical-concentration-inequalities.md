---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-001-11-classical-concentration-inequalities
section_title: "Classical concentration inequalities"
section_number: 1.1
pages: 2-3
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
---
Let {Xn : n ≥ 1} be independent Bernoulli random variables with respective means {pn}. Let
Sn := ∑ n
k=1Xk denote the partial sums, µn := ESn = ∑ n
k=1pk denote the means and Vn :=∑ n
k=1pk(1 −pk) denote the variance of Sn. The simple and well known one-sided tail estimate for
Sn is the classical Gaussian bound
P(Sn −µn ≥a) ≤ exp
(
− 2a2
n
)
. (1.1)
Replacing Xn with 1 −Xn gives the two-sided bound
P(|Sn −µn| ≥ a) ≤ 2 exp
(
− 2a2
n
)
. (1.2)
The bound (1.1) may be found, among other places, in [McD89, Corolla ry 5.2]. The references given
there include [Hoe63, (2.3)] as well as [Che52], which proves the resu lt for identically distributed
variables.
Whenpn and 1 −pn are bounded away from zero, the variance of Sn is of order n and this kind
of bound is the best one can expect. However, when n ≫ µn, one might hope for uniformity in n
via bounds in which the exponent depends on µn and not on n. For example, if max j≤npj is small
then Sn is well approximated by a Poisson variable with mean µn. The upper tail of a Poisson is
not as thin as a Gaussian, being exp[ −Θ(a log(a/µ))] rather than exp[ −Θ(a2/µ)]. The bound
P(Sn ≥a +µ) ≤ea
( µ
a +µ
) a+µ
≤ exp
[
− a2
2(a +µ)
]
(1.3)
is proved in [Hoe63, Theorem 1] and asymptotically matches the Poiss onian upper tail.
1
