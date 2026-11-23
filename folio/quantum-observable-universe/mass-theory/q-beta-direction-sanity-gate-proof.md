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
(same order of magnitude, one decade each way) and is screened out
otherwise. The additive test
$|F(q_0) - F_{\text{target}}(q_0)|/F_{\text{target}}(q_0) > 10$ is
**not** a sufficient condition for failure when $F(q_0)$ may be
negative: $F_{\text{target}}=1$, $F(q_0)=-19/2$ passes the window but
fails the additive test. For $F(q_0)\ge0$ it is sufficient, but it
never rejects a too-small magnitude
([The order-of-magnitude screen $\mathrm{Scr}_\lambda(t,x)$](#prop:order-of-magnitude-screen), item 6).

**Step 1 — the target has order of magnitude one.** Every ladder
factor satisfies $|c_k u_0^k| \le |c_2|\,u_0^2 \approx 7.3\times
10^{-5}$, with the sequence $|c_k|\,u_0^k$ decreasing to the flat
asymptote $\approx 2.1\times 10^{-13}$ measured on the window
$c_2, \ldots, c_{10}$ (radius-of-convergence gate computation).
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
$\approx 1 \ll 10$: *granted that ladder comparison*, the true kernel
passes at any decade threshold, so the screen raises no false refutation. Contrapositively, *if* the true kernel passes, a candidate whose
magnitude falls outside the decade window has $F(q_0) \ne
F_{\text{true}}(q_0)$ ([The order-of-magnitude screen $\mathrm{Scr}_\lambda(t,x)$](#prop:order-of-magnitude-screen), item 2).
That premise rests on the comparison of the ladder with
$\mathfrak{Q}_\beta^{\text{CODATA}}$ and on the infinite ladder
bound, whose convergence is not proved, so rejection is conditional,
not definitive. Passage is only
necessary — a passing candidate still faces the exact $\S 4(c)$
integer shadows and the $\S 4(a)$ pole-location test, which is
conditional on the [radius-of-convergence conjecture](q-beta-radius-of-convergence-gate.md).

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
   geometric-decay direction errors of Step 4, which for $m \ge 5$
   escape only thresholds $\gtrsim 11.6$.

The decade convention $10\times$ sits inside this admissible window.
Finer discrimination is deliberately delegated to the complementary
gates, which admit no tolerance at all ($\S 4(c)$) or a $10^{-6}$
fibre-level tolerance ($\S 4(a)$).

**Step 4 — non-vacuity: the stabilisation direction obstruction.**
The canonical refuted precedent is the family of trace-level
candidates whose substrate magnitude is a power of the
positive-stabilisation weight, at the canonical value
$z = q^3/(q^2+1)$. This satisfies $z < 1$ exactly when
$q^3 - q^2 - 1 < 0$, that is for $1 < q < \psi \approx 1.4656$ (the
real root of $x^3 = x^2 + 1$); the substrate lies in that range, with
$z(q_0) \approx 0.6127$. A candidate with $|F(q_0)| = z(q_0)^m$ after
$m$ stabilisations therefore satisfies

$$
\frac{F_{\text{target}}(q_0)}{|F(q_0)|}
\;\approx\; 0.998 \cdot 1.632^{\,m},
$$

which, at the retired $z = 1$ base target $\approx 0.998$, exceeds
$10$ first at $m = 5$ (where it is $\approx 11.6$; at $m = 4$ it is
$\approx 7.1$). The first rejected $m$ depends on the target: it is
$m = 4$ at the convention-D target $\approx 1.76$. Repeated stabilisation can only
shrink the magnitude — it can never climb to a target of order unity,
let alone to the linking-weight scale $\approx 2.5$ of the precedent —
and, at that target, the gate screens out every member with $m \ge 5$
([The order-of-magnitude screen $\mathrm{Scr}_\lambda(t,x)$](#prop:order-of-magnitude-screen), item 5). The members with
$m \le 4$ are not caught by the decade threshold; their exclusion
rests on the direction argument itself, not on this gate.
$\blacksquare$

Under the alternative Convention-C weight
$z = 1/(q^{1/2} + q^{-1/2})$. That weight satisfies $0 < z < 1/2$ for
every $q > 1$ by AM–GM, which made the obstruction hold at all $q > 1$
with first exceedance at $m = 4$ (ratio $\approx 16$). Neither holds
at the canonical weight.
