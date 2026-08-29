---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-018-62-a-precise-upper-bound
section_title: "A precise upper bound"
section_number: 6.2
pages: 46-47
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
Theorem 6.3. Let B be a Borelian subset of R.
(1) If B is admissible, then
lim sup
n→∞
(√
2πtn exp(tnF(B)) P[Xn∈ tnB]
)
≤



∑a∈Bmin
ψ(h(a))
(1−e−|h(a)|)
√
η′′(h(a))
∑a∈Bmin
ψ(h(a))
|h(a)|
√
η′′(h(a))
the distinction of cases corresponding to φ lattice or non-lattice distributed. The sum
on the right-hand side consists in one or two terms — it is considered inﬁnite if a =
η′(0)∈ Bmin.
(2) If B is not admissible, then for any positive real number M,
lim
n→∞
(
exp(tnM) P[Xn∈ tnB]
)
= 0.
Proof. For the second part, one knows that ϕn(x) exp(−tnη(x)) converges to ψ(x)
which does not vanish on the real line, so by taking the logarithms,
lim
n→∞
log ϕn(x)
tn
= η(x).
Then, Ellis-Gärtner theorem holds since F is supposed essentially smooth. So,
lim sup
n→∞
log P[Xn∈ tnB]
tn
≤− F(B),
and if B is not admissible, then the right-hand side is−∞ and (2) follows immediately.
For the ﬁrst part, suppose for instance φ non-lattice distributed. Take C a closed
admissible subset, and assume η′(0) /∈ C — otherwise the upper bound in (1) is +∞
and the inequality is trivially satisﬁed. Since Cc is an open set, there is an open interval
(a, b)⊂ Cc containing η′(0), and which we can suppose maximal. Then a and b are in
C as soon as they are ﬁnite, and C⊂ (−∞, a]⊔ [b, +∞). Moreover, by strict convexity
of F, the minimal value F(C) is necessarily attained at a or b. Suppose for instance
F(a) = F(b) = F(C) — the other situations are entirely similar. Then,
P[Xn∈ tnC]≤ P[Xn≤ tna] + P[Xn≥ tnb]
≲ exp(−tnF(C))
(
ψ(h(a))
−h(a)
√
2πtnη′′(h(a)) + ψ(h(b))
h(b)
√
2πtnη′′(h(b))
)
by using Theorem 4.3 for P[Xn≥ tnb], and also for P[Xn≤ tna] = P[−Xn≥− tna] —
the random variables−Xn satisfy the same hypotheses as the Xn’s withη(x) replaced
by η(−x), ψ(x) replaced by ψ(−x), etc. This proves the upper bound when B is closed,
and since F(B) = F(B) by lower semi-continuity of F and Bmin = ( B)min, the result
extends immediately to arbitrary admissible Borelian subsets. □
MOD-φ CONVERGENCE, I 47
