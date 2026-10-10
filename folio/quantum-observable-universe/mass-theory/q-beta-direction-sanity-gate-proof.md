## Proof

Write $q_0$ for the substrate modulus, $u = b(q)\,\hbar_q^2$ for the
ladder variable of the precision-ladder factorisation

$$
\mathfrak{Q}_\beta(q)
= Q_A(q)\cdot\cos\bigl(\alpha_{\text{eff}}(q)\bigr)
  \cdot\prod_{k \ge 2}\bigl(1 + c_k\,u^k\bigr)
$$

([$c_2$ structural identity](q-beta-c-2-eq-neg-one-structural.md)),
$u_0 \approx 8.517\times 10^{-3}$ for its substrate value, and $c_k$
for the pinned ladder coefficients. A candidate Habiro element $F(q)$
is a proposed closed form for the correction factor
$\mathfrak{Q}_\beta(q)/[Q_A(q)\cos(\alpha_{\text{eff}}(q))]$
([$c_k$ recursion](q-beta-c-k-recursion-from-habiro-q-difference.md)),
and the target magnitude is

$$
F_{\text{target}}(q_0)
:= \frac{\mathfrak{Q}_\beta^{\text{CODATA}}}
        {Q_A(q_0)\cdot\cos\bigl(\alpha_{\text{eff}}(q_0)\bigr)}
\approx 0.998 .
$$

**The gate.** $F$ *passes* when
$F_{\text{target}}(q_0)/10 \le |F(q_0)| \le 10\,F_{\text{target}}(q_0)$
(same order of magnitude, one decade each way) and is refuted
otherwise. The operational test
$|F(q_0) - F_{\text{target}}(q_0)|/F_{\text{target}}(q_0) > 10$ is a
sufficient condition for failure: it forces either
$|F(q_0)| > 11\,F_{\text{target}}(q_0)$ or a sign reversal, both
outside the window.

**Step 1 — the target has order of magnitude one.** Every ladder
factor satisfies $|c_k u_0^k| \le |c_2|\,u_0^2 \approx 7.3\times
10^{-5}$, with the sequence $|c_k|\,u_0^k$ decreasing to the flat
asymptote $\approx 2.1\times 10^{-13}$ established by the
[radius-of-convergence gate](q-beta-radius-of-convergence-gate.md).
Hence

$$
\Bigl\lvert \ln \prod_{k \ge 2}\bigl(1 + c_k u_0^k\bigr) \Bigr\rvert
\;\le\; 2\sum_{k \ge 2} |c_k|\,u_0^k
\;\lesssim\; 2\times 10^{-4}
\;\ll\; \ln 10 ,
$$

so the correction product lies within a factor $e^{\pm 2\times
10^{-4}}$ of unity: it cannot move the base value
$Q_A \cos\alpha_{\text{eff}}$ by even a fraction of a decade. The
empirical target evaluates to $F_{\text{target}}(q_0) \approx 0.998$
(gate witness), consistent with this bound. Order-of-magnitude
proximity to the target is therefore an invariant that every faithful
candidate for the correction factor must satisfy.

**Step 2 — soundness of rejection.** $F_{\text{target}}(q_0) > 0$,
and the true kernel — the element whose expansion generates the
canonical $c_k$ — evaluates at $q_0$ to the correction product of
Step 1, hence within $2\times 10^{-4}$ (in log) of order unity and,
up to the sub-percent accuracy of the ladder itself (negligible at a
decade threshold), to $F_{\text{target}}(q_0)$. Its window ratio is
$\approx 1 \ll 10$: the true kernel passes at any decade threshold,
so no false refutation is possible. Contrapositively, a candidate
whose magnitude falls outside the decade window has $F(q_0) \ne
F_{\text{true}}(q_0)$, and two fibre elements with distinct
archimedean evaluations at $q_0$ are distinct: the refuted candidate
is not the true kernel. Rejection is definitive; passage is only
necessary — a passing candidate still faces the exact $\S 4(c)$
integer shadows and the $\S 4(a)$ pole-location test.

**Step 3 — calibration of the $10\times$ threshold.** Two constraints
bound the admissible threshold window.

1. *Lower bound.* The gate must not refute legitimate fibre-level
   candidates whose archimedean evaluations swing between anchor
   pins: recorded cross-anchor swings reach $\approx 3.5\,\%$ at the
   $c_3$ level, while the substrate variable itself shifts by only
   $2.1\times 10^{-7}$ (210 ppb) under the proton–muon re-pin,
   moving the target through the ladder by
   $\bigl(\sum_k k\,|c_k|\,u_0^k\bigr)\cdot 2.1\times 10^{-7}
   \approx 3\times 10^{-11}$ in log — utterly negligible. Any
   threshold well above the few-percent near-match band therefore
   tests direction, not anchor choice or near-match precision.
2. *Upper bound.* The threshold must still catch the
   geometric-decay direction errors of Step 4, which escape only
   thresholds $\gtrsim 16$.

The decade convention $10\times$ sits inside this admissible window.
Finer discrimination is deliberately delegated to the complementary
gates, which admit no tolerance at all ($\S 4(c)$) or a $10^{-6}$
fibre-level tolerance ($\S 4(a)$).

**Step 4 — non-vacuity: the stabilisation direction obstruction.**
The canonical refuted precedent is the family of trace-level
candidates whose substrate magnitude is a power of the
positive-stabilisation weight $z = 1/(q^{1/2} + q^{-1/2})$. For every
$q > 1$ the AM–GM inequality gives $q^{1/2} + q^{-1/2} > 2$, hence
$0 < z < 1/2$; at the substrate, $z(q_0) \approx 0.4993$. A candidate
with $|F(q_0)| = z(q_0)^m$ after $m$ stabilisations therefore
satisfies

$$
\frac{F_{\text{target}}(q_0)}{|F(q_0)|}
\;>\; 0.998 \cdot 2^{\,m},
$$

which exceeds $10$ already at $m = 4$ (where $0.998 \cdot 16 \approx
16.0$). Repeated stabilisation can only shrink the magnitude — it can
never climb to a target of order unity, let alone to the
linking-weight scale $\approx 2.5$ of the precedent — so the entire
family fails the gate for every $m \ge 4$. $\blacksquare$
