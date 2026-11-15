---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
essentially need two diﬀerent ﬁltrations. Their purpose is to single out main terms
of asymptotics in diﬀerent regimes. One ﬁltration is responsible for the “law of
large numbers” while another serves the “central limit theorem”.
In §5, we start the study of the Plancherel measures Mn.
We introduce the
sequence of expectation functionals ⟨· ⟩n on A that corresponds to the sequence
{Mn}, and we remark that ⟨· ⟩n becomes very simple in the basis {p#
ρ }. Then we
prove the main result of the section — the law of large numbers, or convergence
to the curve Ω. Although the central limit theorem, established in §7, contains the
law of large numbers, we prefer to prove it independently, because this can be done
in a rather simple way. It is interesting to compare our simple algebraic argument
with the analytic approach of the pioneer works [LoS], [VeK1], [VeK3].
In §6, we examine the random variables p#
2
(n), p#
3
(n), . . ., where p#
k
(n) stands
for the restriction of the function p#
k ∈A to the ﬁnite probability space (Yn, Mn).
We show that, as n →∞, the variables p#
k
(n), suitably scaled, are asymptotically
independent Gaussians. This result is the ﬁrst version of the central limit theorem.
Its proof relies on the method of [IK]. A diﬀerent proof has been given by Hora
[Ho].
In §7, we obtain our main result: a description of the Gaussian ﬂuctuations
around the limit curve Ω. It is derived from the central limit theorem for the gen-
erators p#
k mentioned above. The proof is based on a formula that gives the highest
term of the polynomial expressing p#
k through the (centered and scaled versions of)
the generators epj. Here “highest term” refers to an appropriate ﬁltration of the
algebra A, which we call Kerov’s ﬁltration.
In §8, we get one more version of the central limit theorem. According to Vershik–
Kerov’s theory, to any Young diagram λ we attach a probability measure on R
(say, µλ), supported by a ﬁnite set. Viewing λ ∈Yn as the random element of the
probability space (Yn, Mn), we turn µλ into a random measure. For these random
measures we prove an asymptotic formula similar to (0.1), where, instead of the
limit curve Ω, we have the semi–circle distribution, and ∆(x) is replaced by another
generalized Gaussian process. We do not know if Kerov was aware of this result.
However, it perfectly ﬁts in the philosophy of his works.
In §9, we give comments to the results of §§7–8 and compare them with the
central limit theorem for random matrices.
In §10, we show that the highest terms of the elements p#
ρ in the “weight grading”
are closely related to the free cumulants. As an application, we get a simple proof
of Biane’s asymptotic formula for character values of large symmetric groups, [Bi1].
Acknowledgment. One of the authors (G. O.) is deeply grateful to Persi Diaconis
for discussions and an important critical remark, which was taken into account in
the ﬁnal version of the paper.
§1. The algebra of polynomial
functions on the set of Young diagrams
Recall ﬁrst the basic deﬁnitions and notation related to partitions and Young
diagrams, see [Ma].
A partition is an inﬁnite sequence λ = (λ1, λ2, . . .) of nonnegative integers such
that λ1 ≥λ2 ≥. . . and the number of nonzero λi’s is ﬁnite. The sum λ1 + λ2 + . . .
is denoted by |λ|, and usually we set |λ| = n.
5
