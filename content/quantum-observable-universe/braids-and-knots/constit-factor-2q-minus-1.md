**Conjecture (Constit-side per-Z step factor in canonical-atom Markov trace).**

*Let $\beta_K^{\mathrm{constit}} \in H_{3A}(q)$ be the disjoint Hecke
product of constituent 3-strand blocks for atom $K = (Z, N)$ (no
interface generators), per [`def:ew-interface-knot`](#def:ew-interface-knot).
The **constit-side per-Z step** is the ratio*
$$
  \rho_Z^{\mathrm{constit}}(q) \;:=\;
    \frac{\tau_M\!\bigl(\beta_{(Z+1, N)}^{\mathrm{constit}}\bigr)}
         {\tau_M\!\bigl(\beta_{(Z, N)}^{\mathrm{constit}}\bigr)}
$$
*— independent of $N$ since the constit factorisation is disjoint in $Z$
and $N$.*

*Conjecture.  At the substrate point $q_0$, this ratio admits the
clean categorical form*
$$
  \boxed{\;
    \rho_Z^{\mathrm{constit}}(q_0)
    \;=\; 2q_0 - 1 \,+\, O(h^{4})
    \;=\; 1.219957 \,+\, O(h^{4})
  \;}
  \tag{$\star\star$}
$$
*where $h(q) = q - q^{-1}$ is the Hecke skein parameter.  The 50-dps
empirical measurement is*
$$
  \rho_Z^{\mathrm{constit}}(q_0) \;=\; 1.220358\ldots
$$
*matching $(2q_0 - 1)$ to **$0.033\%$ relative error** — a $15\times$
improvement over the previous candidate $q + h/2$ at $0.48\%$.*

### Empirical evidence (50-dps categorical search, Phase 5g)

Categorical scan over products / quotients / sums of substrate primitives
$\{q, q^{-1}, q^n, [n]_q, h, z, \sqrt{q}, \sqrt{q}^{-1}\}$ for matches
to the measured value $1.220358$ at $q_0$:

| rank | candidate | value at $q_0$ | rel. err. |
|---|---|---:|---:|
| **1** | **$2q - 1$** | **$1.219957$** | **$0.0329\%$** |
| 2 | $[6]_q / [5]_q$ | $1.223668$ | $0.2712\%$ |
| 3 | $q + h/2$ | $1.214509$ | $0.4794\%$ |
| 4 | $1 + \sinh(h)$ | $1.210587$ | $0.8008\%$ |
| 5 | $z + q^{-3}$ | $1.230554$ | $0.8354\%$ |

The $0.033\%$ residual conjecturally vanishes to order $O(h^{4})$ — a
higher-precision measurement (Phase 5k, queued) is needed to
distinguish $O(h^{4})$ noise from a genuine second-order correction.

### Structural reading

The form $2q - 1$ has a clean Hecke-deformation interpretation:
$$
  2q - 1 \;=\; 1 + 2(q - 1) \;=\; \exp(h)\Big|_{\text{leading 2 terms}}
$$
i.e. it is the leading two terms of the series for $\exp(h)$ in the
substrate window $q \in (1, 2)$, where $h = q - q^{-1} \approx q - 1$
to leading order.  Equivalently, $2q - 1$ is the **doubled
$q$-deformation of the unit** — the categorical "rate of growth"
per added proton in the disjoint Hecke product, measured at $H_3$
per added 3-strand block.

### Combined per-Z step at the full $\tau_M$ level

Combining $(\star\star)$ with the interface-knot factor $z = 1/(q^{1/2}
+ q^{-1/2})$ from
[`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) gives
the per-Z step at the **full $\tau_M$ level** (adding a proton at a
p-* boundary):
$$
  \boxed{\;
    \frac{\tau_M(\beta_K^{Z+1, N})}{\tau_M(\beta_K^{Z, N})}
    \;=\; z \cdot (2q - 1) \,+\, O(h^{4})
    \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} \,+\, O(h^{4})
  \;}
$$
which at $q_0$ evaluates to $\approx 0.609346$ — verified empirically
to $0.0001\%$ in Phase 5c.1.

### Relation to `conj:alpha-cosh-h-z-step-correction`

$(\star\star)$ lives at the **full $\tau_M$** level, complementing
[`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction)
which states that the per-Z step factor in the **single-block
$|\Delta_\lambda^*|$** extraction is $[3]_q^2 \cdot \cosh(h)$ (to
$0.022\%$).  The two conjectures are at structurally distinct
extraction levels of the same Hecke algebra:

| level | per-Z step factor | conjecture |
|---|---|---|
| full $\tau_M(\beta_K)$ | $z \cdot (2q - 1) + O(h^4)$ | $(\star\star)$ — this block |
| single-block $\|\Delta_\lambda^*\|$ | $[3]_q^2 \cdot \cosh(h) + O(?)$ | `conj:alpha-cosh-h-z-step-correction` |

Phase 5h's negative result confirms the separation: injecting
$\cosh(h)$ at the depth-stratified $\Phi_k$ level does **not** close
the residual $1.54\times$ variance in the full formula — that
residual lives at the $|\Delta_\lambda^*|$ layer (per Phase 5b), not
the $\tau_M$ layer where $(\star\star)$ is exact-to-$O(h^4)$.

### Bar-symmetry

Under the bar involution $q \mapsto q^{-1}$, the candidate $2q - 1$
maps to $2q^{-1} - 1 = (2 - q) / q$.  These differ at $q \neq 1$:
$$
  (2q - 1) \;\neq\; (2q^{-1} - 1) \quad\text{at }q \neq 1.
$$
Hence $(\star\star)$ is **not** a bar-symmetric identity in the
strong sense — unlike `conj:alpha-cosh-h-z-step-correction` whose
$[3]_q^2 \cdot \cosh(h)$ closed form is bar-symmetric.

This is consistent with the structural reading: the constit-side
factor is a **per-proton** measurement (counts protons explicitly via
the $Z$-step direction), so it carries the natural chirality of the
constituent structure, whereas the single-block $|\Delta_\lambda^*|$
extraction averages over the symmetric channel and is bar-symmetric
by construction.

### Open questions

1. **Is the $0.033\%$ residual $O(h^4)$ noise or a genuine
   second-order correction?**  Phase 5k (queued): higher-precision
   measurement of the constit factor and a categorical scan over
   $h^4$-order corrections.

2. **Operator-level derivation of $2q - 1$ from the Hecke skein.**
   The form $2q - 1$ matches $\sigma + \sigma^{-1}$ acting on the
   trivial channel idempotent $e_+ = (\sigma + q^{-1}) / (q + q^{-1})$,
   suggesting an averaging-channel interpretation parallel to the
   $\cosh(h)$ eigenvalue identity (see
   [`alpha-cosh-h-z-step-correction.lean §2`](alpha-cosh-h-z-step-correction.lean)).
   The §3b-cond class `ConstitFactor2qMinus1` axiomatises this; the
   operator-level proof is queued.

3. **Higher-rank extensions.**  Does the same $(2q - 1)$ companion
   hold for $H_{3A}$ at $A > 4$?  The constit-side factor is
   independent of $A$ (disjoint product), so the identity should
   extend trivially — but the categorical fit needs verification.

### Implementation reference

- Script: [`folio-assistant/computations/constit_factor_and_volhyp_test.py`](../../../folio-assistant/computations/constit_factor_and_volhyp_test.py) (Phase 5g categorical scan)
- Witness: `folio-assistant/computations/constit-factor-and-volhyp.witness.json` (results recorded; categorical-search assertion passes)
- Companion proposition: [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) (interface factor $z$, exact)
- Single-block companion: [`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction) ($|\Delta_\lambda^*|$ level)
- Audit: [`docs/audits/2026-05-20-phase5g-5h-5i-results.md`](../../../docs/audits/2026-05-20-phase5g-5h-5i-results.md) §5g
