---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-006-41-hyperbolic-volumes-twisted-torsion-and-large
section_title: "Hyperbolic volumes, twisted torsion, and large N"
section_number: 4.1
pages: 13-15
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
The most fundamental relation between complex Chern-Simons theory and hyperbolic ge-
ometry has been understood for a long time, and concerns the semi-classical asymptotic
expansion of partition functions [3] (see also [25, 67]). It is easiest to formulate it ﬁrst in
7This very same symmetry played a central role in deﬁning reﬁned (compact) Chern-Simons theory on
Seifert-ﬁbered manifolds [66].
13
terms of the “holomorphic blocks”Bα, ~Bα appearing in (3.1), labelled by ﬂat connections α :
as k +is→∞ or q
1
2 =e
2πi
k+is→ 1, Bα(q
1
2 )∼
√
4π3
τ(α)e
i(k+is)
8π SCS (α) ;
as k−is→∞ or ˜q
1
2 =e
2πi
k−is→ 1, ~Bα(˜q
1
2 )∼
√
4π3
τ(α)∗e
i(k−is)
8π SCS (α)∗
;
(4.1)
whereSCS(α) is the classical Chern-Simons action evaluated on a particular ﬂat connection
andτ(α) is the analytic Ray-Singer torsion twisted by the ﬂat connection α [68]. This is the
standard result expected from Chern-Simons perturbation theory [69]. In the presence of
a boundary, the classical action and torsion on the RHS depend on the choice of boundary
conditions (boundary holonomies) for α. From (3.1), it then follows that if both k +is→∞
and k−is→∞
Z[M]k,s∼
∑
ﬂat α
1
|Stab(α)|
4π3
|τ(α)|e
ik
4π ReSCS (α)−is
4π ImSCS (α). (4.2)
The formula is particularly meaningful if s is analytically continued to (say) positive imag-
inary values. Then each term in (4.2) shows exponential growth or decay at large |s|,
controlled by ImSCS(α).
Now suppose that M is hyperbolic, meaning that it admits a hyperbolic metric. The
hyperbolic metric is unique (given suitable boundary conditions) and is a topological in-
variant of M [58, 59]. Moreover, the vielbein and spin connection of the hyperbolic met-
ric can be rewritten as a ﬂat SL(2, C) connection αhyp = w +ie, with the property that
ImSCS(αhyp) = Vol(M) is the hyperbolic volume ofM. The real part ReSCS(αhyp) is known
as the Chern-Simons invariant of the hyperbolic structure, and provides a natural complex-
iﬁcation of the hyperbolic volume [70, 71]. It is also useful to note that the connection αhyp
necessarily has a trivial stabilizer – the connection is fundamentally non-abelian.
Therefore, if the gauge group is SL(2, C) and M is hyperbolic, the sum (4.2) contains
a term that is controlled by the hyperbolic volume of M. Typically, Im SCS(αhyp) is larger
than the “volume” of any other ﬂat connection, and the entire sum (4.2) is dominated by
the hyperbolic volume. (It is expected that Im SCS(αhyp) always dominates, but no general
result of this type has been proven.)
It is often useful to strip oﬀ the holomorphic part of the asymptotic expansion. This can
be done by taking a singular limit: we ﬁx k = 1, analytically continues to imaginary values,
and send s→−ik =−i. This has the eﬀect of sending q→ 1 but ˜q→ 0, which trivializes
the anti-holomorphic blocks, ~Bα(˜q
1
2 )→ 1. In this singular limit, we expect
Z[M]1,s∼
∑
ﬂat α
1
|Stab(α)|
√
4π3
τ(α)e− 1
ℏSCS (α) as ℏ = 2πi 1−is
1 +is→ 0. (4.3)
This sort of limit played a major role in early analyses of partition functions for complex
Chern-Simons theory [72, 49], though it was not realized at the time that the partition
functions (derived from quantum Teichm¨ uller theory) being analyzed had ﬁxed levelk = 1.
14
The fact that the perturbative expansion of complex Chern-Simons theory (or individual
holomorphic blocks, as in (4.1)) contains geometric invariants of M played a major role
in providing a physical justiﬁcation for the Volume Conjecture, and generalizing it. The
original Volume Conjecture [26, 27] claims that a particular double-scaling limit of colored
Jones polynomials of a knotK⊂S3 leads to exponential growth, controlled by the hyperbolic
volume of the knot complement Vol(S3\K). This was justiﬁed in [25] by embedding SU (2)
Chern-Simons theory (which computes colored Jones polynomials) into a holomorphic sector
of SL(2, C) Chern-Simons theory, and arguing that the asymptotic expansions of SU (2)
and (holomorphic) SL(2, C) theories should coincide. The argument immediately led to
generalizations, involving higher-order terms in the asymptotic expansion and a dependence
on boundary conditions, which have been carefully checked in many computations, cf. [67,
49, 73].
It is also interesting to consider “large- N” limits in complex Chern-Simons theory, tak-
ing the gauge group to be SL(N, C) and sending N → ∞. Physically, such limits are
most conveniently studied by realizing Chern-Simons theory on a stack of N M5 branes
(Section 3.1), and using AdS/CFT or large- N duality. A study of the ﬁve-brane system
[74, 75, 76] predicts that the leading asymptotic growth of the partition function Z[M]k,s as
in (4.2) is scales as N 3Vol(M) at large N [38]. This is not surprising: the hyperbolic ﬂat
SL(2, C) connection can be embedded intoSL(N, C) by using theN-dimensional representa-
tionρN :SL(2, C)→SL(N, C), and the Chern-Simons functional evaluates to∼N 3Vol(M)
on ρN(αhyp), cf. [77]. As long as (4.2) is dominated by the ﬂat connection ρN(αhyp) for any
N, one quickly recovers the scaling prediction. Much more non-trivially, the M-theory anal-
ysis predicts that the logarithm of the torsion τ(ρN(αhyp)) will grow as N 3Vol(M) [78, 79]
at large N as well. This latter result was recently proved by Porti and Menal-Ferrer [80].
