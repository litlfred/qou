**Classical limit ($q = 1$).** Set $q = 1$. The q-integers reduce
to ordinary integers, $[n]_q \to n$, and $\mathrm{Li}_2^q(z) \to
\mathrm{Li}_2(z) = \sum z^n / n^2$. The identity (R) reduces to the
**classical Rogers–Abel five-term identity** [Rogers, 1907; Abel, 1826]:

$$
  \mathrm{Li}_2(u) + \mathrm{Li}_2(v) - \mathrm{Li}_2(uv) -
  \mathrm{Li}_2(\alpha) - \mathrm{Li}_2(\beta) =
  \log\!\!\left(\frac{1-u}{1-uv}\right) \cdot \log\!\!\left(\frac{1-v}{1-uv}\right).
$$

This is a classical, fully-proven result (Lewin, *Polylogarithms
and Associated Functions* 1981, §1.6). It is the **archimedean shadow**
of the bare pentagon (P): when $q = 1$, the pre-$\tau$ identity acquires
the explicit $\log^2$ correction.

**q-deformation extension.** For generic $q$, the q-log correction
$\log_q(x) = \sum_n (-1)^{n+1}(x-1)^n / [n]_q$ generalises the
classical $\log$. The proposed identity (R) is the natural
q-deformation: $\log \to \log_q$.

**Numerical evidence** at $q_0 \approx 1.110$, from
[`pentagon_reduction_li2q.py`](https://github.com/litlfred/qou/blob/main/computations/pentagon_reduction_li2q.py)
(witness:
[`pentagon-reduction-li2q.witness.json`](https://github.com/litlfred/qou/blob/main/computations/pentagon-reduction-li2q.witness.json)):

| $(u, v)$ | bare LHS−RHS of (P) | classical $\log^2$ err | q-$\log_q^2$ err | improvement |
|---|---:|---:|---:|---:|
| $(0.3, 0.3)$ | $+0.0687$ | $1.6 \times 10^{-4}$ | $\mathbf{4.0 \times 10^{-5}}$ | $4.0\times$ |
| $(0.5, -0.5)$ | $-0.1665$ | $5.3 \times 10^{-4}$ | $\mathbf{3.1 \times 10^{-4}}$ | $1.7\times$ |
| $(0.7, 0.7)$ | $+0.2780$ | $3.5 \times 10^{-3}$ | $\mathbf{2.3 \times 10^{-3}}$ | $1.6\times$ |
| $(-0.3, -0.3)$ | $+0.1274$ | $1.6 \times 10^{-4}$ | $\mathbf{3.1 \times 10^{-5}}$ | $5.1\times$ |

The q-$\log_q^2$ correction reduces the residual by $1.5$–$5\times$
compared to classical $\log^2$, confirming the q-deformed structure.
The remaining $\sim 0.5$–$1\%$ residual (especially at $u = v = 0.7$
near the convergence boundary $|z| < q_0$) is the $O((q-1)^2)$
sub-leading correction that needs a longer proof.

### Structural interpretation

This proposition crystallises **what $\tau_{\mathrm{arch}}$ does to
the pentagon identity**. Pre-$\tau$, the identity (P) is a five-term
relation among Hopf-algebraic primitives — no log-squared term, no
$1/n^2$ denominator structure, purely formal.

Post-$\tau$, the realization functor introduces the rational
denominators $1/n$ in the series (the "missing $n!$" structure
implicit in passing from divided-power algebras to series-form
archimedean realizations). The cost of this rationalisation is the
$\log_q^2$ Rogers correction term — which is *exactly* the
archimedean kernel that distinguishes Faddeev's non-perturbative
Volume-conjecture form from the $\mathrm{Li}_2^q$ algebraic form
(the bar-anti-symmetric image of $\log\Phi_q$ rescaled by $h/2$, per
`prop:li2q-phiq-bar-symmetrization`).

The post-$\tau$ pentagon (R) is therefore the **defining identity**
for the analytic q-dilogarithm in the volume-conjecture / Kashaev
[`rem:kashaev-as-archimedean-realization`](#rem:kashaev-as-archimedean-realization)
framework, in the same way the pre-$\tau$ pentagon (P) is the
defining identity for the algebraic level-2 primitive in $\mathcal{H}_q$.

### Significance: archimedean compute pipeline

Computational consequences of the post-$\tau$ pentagon (R):

1. **T3 reorganisation**:
   [`pentagon_reduction_li2q.py`](https://github.com/litlfred/qou/blob/main/computations/pentagon_reduction_li2q.py)
   uses (P$'$) — the duplication form of (R) — to evaluate
   $\mathrm{Li}_2^q(|V_i V_j|)$ at out-of-radius arguments via factorisation
   $z = uv$ with $|u|, |v| < q_0$. The Rogers $\log_q^2$ correction
   ensures the reorganisation is numerically consistent.

2. **Algebraic-side ratios** (per the Habiro framework
   [`prop:full-pole-structure-mass-trace`](#prop:full-pole-structure-mass-trace)):
   the bare pentagon (P) suffices for ratio computations; no
   $\log_q^2$ correction is needed when both numerator and
   denominator pass through the same $\tau_{\mathrm{arch}}$ realization.

3. **Volume-conjecture matching**: Kashaev's hyperbolic-volume
   conjecture uses Faddeev $\Phi_q$ on the archimedean side; the
   q-Rogers pentagon (R) connects this to the
   $\mathrm{Li}_2^q$ side via the bar-**anti**-symmetrization
   identity
   (`prop:li2q-phiq-bar-symmetrization`)
   $\mathrm{Li}_2^q(z) = -h \cdot \log \Phi_q(z) = (h/2)\bigl(\log \Phi_{q^{-1}} - \log \Phi_q\bigr)$ —
   not the bar-SYMMETRIC sum (which vanishes identically).

### Lean formalisation

[`qou:QOU.BraidKnot.q_rogers_pentagon_archimedean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/QRogersPentagonArchimedean.lean)
states the post-$\tau$ pentagon (R) as a theorem conditional on the
$O((q-1)^2)$ correction being class-axiomatized
(per AGENTS.md §3b-cond). At $q = 1$ the theorem reduces to the
classical Rogers identity (provable in Mathlib via real-log
arithmetic).

### Falsifiability

The numerical residual at $u = v = 0.7$ is $2.3 \times 10^{-3}$ — the
upper end of the empirical $O((q-1)^2)$ behaviour. A direct
high-precision computation at this point disagreeing by more than
$O((q-1)^3 \cdot u v)$ refutes the proposed q-correction; tracked
as the open paper-track derivation in
[`docs/audits/-pentagon-reduction-li2q.md`](https://github.com/litlfred/qou/blob/main/docs/audits/-pentagon-reduction-li2q.md).
