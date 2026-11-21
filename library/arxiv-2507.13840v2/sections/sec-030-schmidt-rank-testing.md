---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-030-schmidt-rank-testing
section_title: "Schmidt rank testing"
section_number: null
pages: 37-38
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Schmidt rank testing
Here, we present an efficient algorithm to test the Schmidt rank of a given pure state. Consider the
Schmidt decomposition of a pure n-qubit state |ψ⟩with respect to bipartition A, B
|ψ⟩=
R
X
i=1
p
λi |ϕi⟩A ⊗|ϕi⟩B ,
(120)
where |ϕi⟩A and |ϕi⟩B are normalized states on subsystem A and B, λi ≥0 are the Schmidt coefficients
with λ1 ≥· · · ≥λR, P
i λi = 1 and Schmidt rank R ≤2n. The maximum overlap of |ψ⟩with the
set of states Mr = {|η⟩: |η⟩= Pr
i=1
√λi |ϕi⟩A ⊗|ϕi⟩B} of at most Schmidt rank r is given by the
Eckart-Young theorem: [35]
Fr(|ψ⟩) = max
|η⟩∈Mr | ⟨η|ψ⟩|2 =
r
X
i=1
λi .
(121)
Next, we prove the following inequality
tr(ρ2
A) ≤Fr(|ψ⟩) ≤
q
rtr(ρ2
A).
(122)
The lower bound follows from tr(ρ2
A) ≤F1(|ψ⟩) ≤Fr(|ψ⟩). For the upper bound, we use the Jensen’s
inequality (Pr
i=1 λi)2/r ≤Pr
i=1 λ2
i ≤PR
i=1 λ2
i . With this bound, we can now provide an efficient
algorithm to test the Schmidt rank by measuring the purity tr(ρ2
A).
Theorem J.1 (Efficient testing of Schmidt rank). Let |ψ⟩be an n-qubit state where it is promised
that
either
(a) Fr(|ψ⟩) ≥ϵ1 ,
or
(b) Fr(|ψ⟩) ≤ϵ2 ,
across a given bipartition, where it is assumed that ϵ2
1/r > ϵ2+2ϵ. Assuming ϵ = 1/poly(n), there exists
an efficient quantum algorithm to distinguish case (a) and (b) using O(r2) two-copy measurements of
|ψ⟩with high probability.
Proof. We set ϵ < 1
2(ϵ2
1
r −ϵ2) and ϵt = 1
2(ϵ2
1
r +ϵ2). By Hoeffding’s inequality, the purity p2 = tr(ρ2
A) can
be measured efficiently using SWAP test or Bell measurement with L ≤2
ϵ2 ln

2
δ

number of samples,
such that |p2 −ˆp2| < ϵ with failure probability δ. We then make the following decision: if ˆp2 ≥ϵt then
we output (a), otherwise (b).
If we are in case (a), then the upper bound in Eq. (122) implies √rp2 ≥Fr(|ψ⟩) ≥ϵ1, so that
p2 ≥ϵ2
1/r. If ˆp2 < ϵt then p2 −ˆp2 > ϵ2
1
r −ϵt > ϵ, which occurs with probability at most δ/2. If
we are in case (b), then the lower bound in Eq. (122) implies p2 ≤Fr(|ψ⟩) ≤ϵ2. If ˆp2 ≥ϵt then
ˆp2 −p2 ≥ϵt −ϵ2 > ϵ, which occurs with probability at most δ/2. Therefore, the algorithm efficiently
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
37
distinguishes case (a) and (b) with probability 1 −δ/2. Since ϵ < ϵ2
1
r , the algorithm requires O(r2ϵ−4
1 )
number of copies.
A few remarks are in order.
First, since the Schmidt rank of a pure state is equivalent to the
rank of the reduced density matrix, our algorithm can also be used to test the rank of a mixed state.
Second, we note that our algorithm imposes non-trivial condition on ϵ1 and ϵ2, thus it only works in
certain parameter regimes. Nevertheless, it requires only two-copy measurements of the state, which
is an essential advantage for practical applications. Previously, an algorithm to test the rank in the
one-sided error setting (i.e. ϵ1 = 1) was proposed in Ref. [81] using O(r2) copies. This test used a
technique known as weak Schur sampling [26], which requires entangled measurements on many copies
of the state. Subsequently, Ref. [69] proposed a test with (r + 1)-copy measurements using Θ((r + 1)!)
copies, again in the setting of one-sided error.
