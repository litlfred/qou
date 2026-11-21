---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER"
section_id: sec-009-3-asymptotics-of-distances-for-a-general-scheme
section_title: "Asymptotics of distances for a general scheme of approximation"
section_number: 3
pages: 23-24
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
toc_source: outline
doc_brief: "ANNALES DE L’INSTITUT FOURIER — 27 sections: Front matter; Introduction; Poisson approximation of lattice-v"
---
approximation
We now consider a general scheme of approximation of a sequence of
Z-valued random variables (Xn)n∈N by a sequence of laws (νn)n∈N, with
c
µn(ξ) = E[eiξXn] = eλnφ(ξ) ψn(ξ) ,
c
νn(ξ) = eλnφ(ξ) χn(ξ) ,
limn→∞ψn(ξ) = ψ(ξ) and limn→∞χn(ξ) = χ(ξ) as in Deﬁnition 1.10. We
can immediately deduce from Theorem 2.3:
Proposition 3.1. — Consider a general scheme of approximation such
that the convergences ψn →ψ and χn →χ occur in C 1(T). Then, one has
dTV(µn, νn) →0, and as well for dL(µn, νn) and dK(µn, νn).
Proof. — Taking r = 0 in Theorem 2.3, we have
dTV(µn, νn) = ∥µn −νn∥A = O

1
(λn)
1
4

,
where the constant in the O( · ) depends on ∥ψn −χn∥A and ∥ψn −χn∥C 1.
By Proposition 2.1, both quantities are bounded by a function of ∥ψn −
χn∥C 1, which is itself bounded since ψn −χn →ψ −χ in C 1(T). For the
other distances, we use the inequality dL ⩽2 dK ⩽dTV.
□
If we want to improve on the rate of convergence of the distances to 0,
then we need an additional assumption similar to the hypothesis of Theo-
rem 2.3, namely:
(H1)
∀n ∈N, ψn(ξ) −χn(ξ) = βn (iξ)r+1 (1 + oξ(1))
and
ψ(ξ) −χ(ξ) = β (iξ)r+1 (1 + oξ(1))
with limn→∞βn = β, and the oξ(1) that converges to 0 as ξ goes to 0,
uniformly in n. We denote this condition by (H1). It is satisﬁed if, for in-
stance, the convergences ψn →ψ and χn →χ occur in C r+1(T), and if
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES
1137
the scheme of approximation is the scheme of order r as deﬁned in Exam-
ple 1.11. However, this new condition (H1) is a bit more general, as we do
not assume that the residues χn and χ are Laurent polynomials of degree
r in eiξ.
In Section 3.1, Section 3.2 and Section 3.3, we shall consider the setting
described above, and we shall establish some exact asymptotic formulas
for dL(µn, νn), dK(µn, νn) and dTV(µn, νn). These formulas generally follow
from an application of the Laplace method to an integral representation of
the distance, but we shall also use Theorem 2.3 in order to get rid of certain
non dominant terms in the asymptotics. In Section 3.4, we introduce the
notion of derived approximation schemes which involve simpler residues,
and under appropriate assumptions, we extend the results of Sections 3.1-
3.3 to these approximation schemes.
