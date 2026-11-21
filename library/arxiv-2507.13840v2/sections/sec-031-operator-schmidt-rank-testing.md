---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-031-operator-schmidt-rank-testing
section_title: "Operator Schmidt rank testing"
section_number: null
pages: 38-39
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Operator Schmidt rank testing
Here, we present an efficient algorithm to test the operator Schmidt rank of a given mixed state.
Consider the operator Schmidt decomposition of a mixed n-qubit state ρ with respect to bipartition
A, B
ρ
q
tr(ρ2
A)
=
X
i
q
λO
i OA,i ⊗OB,i,
(123)
where {OA,i} and {OB,i} are a set of orthonormal operators in the subsystem A and B, λO
i ≥0 are the
operator Schmidt coefficients with λO
1 ≥· · · ≥λO
R, P
i λO
i = 1 and operator Schmidt rank R ≤4n. The
operator Schmidt decomposition can be obtained by vectorizing the normalized operator |ρ⟩=
ρ
√
tr(ρ2
A)
and performing the Schmidt decomposition in Eq. (120) on |ρ⟩. The maximum pure-state overlap of
|ρ⟩with the set of operators MO
r = {|O⟩:
O
√
tr(O2
A) = P
i
q
λO
i OA,i ⊗OB,i} whose operator Schmidt
rank is at most r is given by
FO
r (ρ) =
max
|O⟩∈MO
r
| ⟨O|ρ⟩|2 =
max
|O⟩∈MO
r
tr(ρO)2
tr(ρ2
A)tr(O2
A) .
(124)
Note that
q
FO
r (ρ) is equivalent to the mixed-state fidelity introduced in Ref. [111], which satisfies
Jozsa’s axioms for mixed-state fidelities [61] up to a normalization factor. Following the pure-state
case, we have
FO
r (ρ) =
r
X
i=1
λO
i .
(125)
Next, we recall that the purity of the state |ρ⟩is given by r4/r2
2. From Eq. (122), we thus have the
inequality
r4
r2
2
≤FO
r (ρ) ≤
s
rr4
r2
2
.
(126)
With this bound, we can now provide an efficient algorithm to test the operator Schmidt rank by
measuring r4 and r2.
Theorem K.1 (Efficient testing of operator Schmidt rank). Let ρ be an n-qubit state where it is
promised that
either
(a) FO
r (ρ) ≥ϵ1 ,
or
(b) FO
r (ρ) ≤ϵ2 ,
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
38
across a given bipartition, where it is assumed that tr(ρ2
A) = 1/poly(n) and (ϵ2
1/r −ϵ2) tr(ρ2
A)2 >
1/poly(n). Then, there exists an efficient quantum algorithm to distinguish case (a) and (b) using
O(r2) copies of |ψ⟩with high probability.
Proof. The algorithm works as follows: We measure r2
2 = tr(ρ2
A)2 using Bell measurements and r4
using the algorithm in Appendix B with L = O(ϵ−2 log(1/δ)) number of copies, such that |r2
2 −ˆr2| < ϵ
and |r4 −ˆr4| < ϵ, each with failure probability δ. The parameter ϵ will be fixed later. We then make
the following decision: if ˆr4/ˆr2 ≥ϵt, where ϵt is a parameter to be fixed later, then we output (a),
otherwise (b).
If we find ˆr4/ˆr2 ≥ϵt, we need that FO
r (ρ) > ϵ2. We have
FO
r (ρ) ≥r4
r2
2
> ˆr4 −ϵ
ˆr2 + ϵ ≥ϵt −ϵ/ˆr2
1 + ϵ/ˆr2
,
(127)
with failure probability δ2/4. We now impose the condition
ϵt −ϵ/ˆr2
1 + ϵ/ˆr2
> ϵ2.
(128)
Next, if we find ˆr4/ˆr2 < ϵt, we need that FO
r (ρ) < ϵ1. We have
FO
r (ρ) ≤
s
rr4
r2
2
<
s
r(ˆr4 + ϵ)
ˆr2 −ϵ
<
s
r(ϵt + ϵ/ˆr2)
1 −ϵ/ˆr2
,
(129)
with failure probability δ2/4. Here, we must have that ˆr2 −ϵ > 0. We further impose the condition
s
r(ϵt + ϵ/ˆr2)
1 −ϵ/ˆr2
< ϵ1.
(130)
Combining the two inequalities in Eq. (128) and Eq. (130), we obtain
ϵ
ˆr2
+ ϵ2(1 + ϵ
ˆr2
) < ϵt < ϵ2
1
r (1 −ϵ
ˆr2
) −ϵ
ˆr2
.
(131)
Therefore, assuming ϵ2
1/r > ϵ2, we can choose
ϵ <
ˆr2
2 + ϵ2
1/r + ϵ2
 
ϵ2
1
r −ϵ2
!
(132)
and
ϵt = 1
2
 
ϵ2
1
r + ϵ2
!
−
ϵ
2ˆr2
 
ϵ2
1
r −ϵ2
!
.
(133)
Therefore, the algorithm requires O(r2r−4
2 ϵ−4
1 ) number of copies, which is polynomial in n assuming
r2 = 1/poly(n).
L
