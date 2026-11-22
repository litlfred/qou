---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-042
section_title: "Page 42"
section_number: null
pages: 42-42
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Or, equivalently,
R[x] ∋v =
X
i
cixi
←→
bv =
X
i
cigi ∈Aext.
In particular, for v = tk we get from (8.5)
btk =
[k/2]
X
j=0
(−1)j
k
k −j
k −j
j

gk−2j ,
k = 3, 4, . . . .
Recall also that bt0 = bt1 = bt2 = 0.
Comparing this with (8.11) we see that
btk =
p#
k−1
(p#
1 )(k−1)/2 + Rk−1 ,
Rk−1 ∈Aext,
deg1(Rk−1) < 0,
k = 3, 4, . . . .
Or by the deﬁnition of the elements ηk, see (6.5),
btk =
√
k −1ηk−1 + Rk−1,
k = 3, 4, . . .,
so that
t(n)
k
=
√
k −1η(n)
k−1 + R(n)
k−1 ,
k = 3, 4, . . . .
Then the proof is completed as at the end of §7.
□
§9. Discussion
Recall that a generalized Gaussian process is a Gaussian measure in a space F′
of distributions (=generalized functions); F′ is supposed to be the dual to a space
F of test functions. Given a test function ϕ ∈F, the result of its pairing with the
random distribution deﬁned by the process is a random Gaussian variable. See,
e.g., Gelfand–Vilenkin [GV], Simon [Si].
We shall deﬁne Gaussian processes via expansions in some orthogonal systems
of functions with random coeﬃcients (a useful general reference on such random
series is Kahane’s book [Ka]). Consider the random series
∆(x) =
∞
X
k=1
ξk+1uk(x)
√
4 −x2
2π
√
k + 1
,
−2 ≤x ≤2.
(9.1)
Here, as above, ξ2, ξ3, . . . are independent standard Gaussian random variables
and u1, u2, . . . are modiﬁed Chebyshev’s polynomials of the second kind (see (7.3),
(7.4)). The series (9.1) correctly deﬁnes a generalized Gaussian process, where as
F′ we take the space (C∞(R))′ of compactly supported distributions on the real
line. But the process actually lives on the subspace of distributions concentrated
on [−2, 2]). For any test function ϕ ∈F = C∞(R),
⟨ϕ, ∆⟩=
Z 2
−2
ϕ(x)∆(x)dx =
∞
X
k=1
ξk+1
2π
√
k + 1
Z 2
−2
ϕ(x)uk(x)
p
4 −x2dx
42
