> **Archimedean specialisation (AGENTS.md §7c).** The Lean encoding
> of this conjecture works over $\mathbb{R}$ — both the `q : ℝ`
> parameter and the `Real.sqrt` evaluation are archimedean-specific.
> The conjecture's structural content (the closed-form $\rho_Z(q)$
> shape) is a numerical claim at the substrate $q_0 \in \mathbb{R}$,
> not a generic-ring identity.
>
> **Resolved (Phase 5l, 2026-05-20): see
> [`prop:constit-factor-tau-M-proton-identity`](#prop:constit-factor-tau-M-proton-identity).**
> The correct closed form for the constit-side per-Z step factor
> is $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$, the
> proton's H_3 Markov trace — a structural identity derivable from
> Wenzl's disjoint Markov-trace multiplicativity (Wenzl 1988 §1.7),
> empirically verified at mpfr-50-dps precision ($\sim 10^{-50}$) across
> the substrate window in [Phase 5l](../../../computations/rho_constit_equals_tau_M_proton_phase5l.py).
>
> The $(2q - 1)$ form below is now understood as a numerical
> coincidence at $q_0$: $\mathrm{tr}_M^3(\mathcal{B}_p, q_0) \approx 1.2204$
> happens to be close to $2 q_0 - 1 = 1.2200$, but the two
> functions diverge away from $q_0$ (rel. err. 28% at $q = 1.05$
> and 33% at $q = 1.17$ — see Phase 5k.2 (this PR) for the
> varying-$q$ falsification table). The conjecture statement
> below is preserved as a record of Phase 5g's categorical-search
> result, but the **structural-form claim is superseded** by the
> Phase 5l proposition.
> ** Update 2026-05-20 (Phase 5k.2): GLOBAL FORM FALSIFIED.**
> Phase 5k.2 (this PR, [`constit_factor_varying_q_phase5k2.py`](../../../computations/constit_factor_varying_q_phase5k2.py))
> directly measured $\rho_Z^{\mathrm{constit}}(q)$ at five $q$-values
> across the substrate window using the same $y_\lambda$ / $\chi_\lambda$
> pipeline as PR #819's Phase 5c.1. Result:
>
> Main sweep (5 q-values, recorded in the witness JSON):
>
> | $q$ | $\rho_Z^{\mathrm{constit}}(q)$ | $(2q - 1)$ | rel. err. |
> |---|---:|---:|---:|
> | $1.050$ | $0.7928$ | $1.100$ | $27.9\%$ |
> | $1.080$ | $0.9933$ | $1.160$ | $14.4\%$ |
> | $\mathbf{1.10998 = q_0}$ | $\mathbf{1.2204}$ | $\mathbf{1.220}$ | $\mathbf{0.034\%}$ |
> | $1.130$ | $1.3905$ | $1.260$ | $10.4\%$ |
> | $1.170$ | $1.7858$ | $1.340$ | $33.3\%$ |
>
> Supplementary fine scan around $q_0$ (separate from the witness):
>
> | $q$ | $\rho_Z^{\mathrm{constit}}(q)$ | rel. err. vs $(2q-1)$ |
> |---|---:|---:|
> | $1.105$ | $1.1805$ | $2.44\%$ |
> | $1.108$ | $1.2044$ | $0.95\%$ |
> | $1.110$ | $1.2205$ | $0.04\%$ |
> | $1.111$ | $1.2287$ | $0.54\%$ |
> | $1.113$ | $1.2450$ | $1.55\%$ |
>
> The $0.033\%$ match at $q_0$ identified in Phase 5g is a
> **localised tangency**, not a structural identity — within
> $\pm 0.005$ of $q_0$ the relative error jumps by $\sim 28 \times$ (to $\sim 0.95\%$
> at $q = 1.108$) and by $\sim 70 \times$ at $q = 1.105$ (to $\sim 2.44\%$), per the
> fine-scan table above.
> The candidate $(2q - 1)$ is **NOT** the correct closed form for
> $\rho_Z^{\mathrm{constit}}(q)$ globally; Phase 5g's categorical
> search matched the *value* at $q_0$, not the *function*.
> Phase 5k.1's "unit-coefficient $h^5$" finding is consequently
> also a coincidence at $q_0$.
>
> The statement below is preserved as a record of the at-$q_0$
> tangency; the **claim that $(2q - 1)$ is the categorical form of
> $\rho_Z^{\mathrm{constit}}$ is empirically refuted**.

**Conjecture (Constit-side per-Z step factor in canonical-atom Markov trace).**

*Let $\mathcal{B}_K^{\mathrm{vac}} \in H_{3A}(q)$ be the disjoint Hecke
product of constituent 3-strand blocks for atom $K = (Z, N)$ (no
interface generators), per [`def:ew-interface-knot`](#def:ew-interface-knot).
The **constit-side per-Z step** is the ratio*
$$
  \rho_Z^{\mathrm{constit}}(q) \;:=\;
    \frac{\mathrm{tr}_M\!\bigl(\mathcal{B}_{(Z+1, N)}^{\mathrm{vac}}\bigr)}
         {\mathrm{tr}_M\!\bigl(\mathcal{B}_{(Z, N)}^{\mathrm{vac}}\bigr)}
$$
*— independent of $N$ since the constit factorisation is disjoint in $Z$
and $N$.*

*Conjecture. At the substrate point $q_0$, this ratio admits the
clean categorical form*
$$
  \boxed{\;
    \rho_Z^{\mathrm{constit}}(q_0)
    \;=\; 2q_0 - 1 \,+\, O(h^{4})
    \;=\; 1.219957 \,+\, O(h^{4})
  \;}
  \tag{$\star\star$}
$$
*where $h(q) = q - q^{-1}$ is the Hecke skein parameter. The 50-dps
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
to leading order. Equivalently, $2q - 1$ is the **doubled
$q$-deformation of the unit** — the categorical "rate of growth"
per added proton in the disjoint Hecke product, measured at $H_3$
per added 3-strand block.

### Combined per-Z step at the full $\mathrm{tr}_M$ level

Combining $(\star\star)$ with the interface-knot factor $z = 1/(q^{1/2}
+ q^{-1/2})$ from
[`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) gives
the per-Z step at the **full $\mathrm{tr}_M$ level** (adding a proton at a
p-* boundary):
$$
  \boxed{\;
    \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
    \;=\; z \cdot (2q - 1) \,+\, O(h^{4})
    \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} \,+\, O(h^{4})
  \;}
$$
which at $q_0$ evaluates to $\approx 0.609346$ — verified empirically
to $0.0001\%$ in Phase 5c.1.

### Relation to `conj:alpha-cosh-h-z-step-correction`

$(\star\star)$ lives at the **full $\mathrm{tr}_M$** level, complementing
[`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction)
which states that the per-Z step factor in the **single-block
$|\Delta_\lambda^*|$** extraction is $[3]_q^2 \cdot \cosh(h)$ (to
$0.022\%$). The two conjectures are at structurally distinct
extraction levels of the same Hecke algebra:

| level | per-Z step factor | conjecture |
|---|---|---|
| full $\mathrm{tr}_M(\mathcal{B}_K)$ | $z \cdot (2q - 1) + O(h^4)$ | $(\star\star)$ — this block |
| single-block $\|\Delta_\lambda^*\|$ | $[3]_q^2 \cdot \cosh(h) + O(?)$ | `conj:alpha-cosh-h-z-step-correction` |

Phase 5h's negative result confirms the separation: injecting
$\cosh(h)$ at the depth-stratified $\Phi_k$ level does **not** close
the residual $1.54\times$ variance in the full formula — that
residual lives at the $|\Delta_\lambda^*|$ layer (per Phase 5b), not
the $\mathrm{tr}_M$ layer where $(\star\star)$ is exact-to-$O(h^4)$.

### Bar-symmetry

Under the bar involution $q \mapsto q^{-1}$, the candidate $2q - 1$
maps to $2q^{-1} - 1 = (2 - q) / q$. These differ at $q \neq 1$:
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

### Phase 5k residual characterisation

Phase 5k.1 (PR #831) analyses the $0.033\%$ residual at $q_0$ across
powers of $h(q) = q - q^{-1}$:

| $k$ | $h^k(q_0)$ | residual$/h^k$ | $\|c\|$ |
|:-:|---:|---:|---:|
| 1 | $2.09 \times 10^{-1}$ | $+1.94 \times 10^{-3}$ | 0.002 |
| 2 | $4.37 \times 10^{-2}$ | $+9.28 \times 10^{-3}$ | 0.009 |
| 3 | $9.14 \times 10^{-3}$ | $+4.44 \times 10^{-2}$ | 0.044 |
| 4 | $1.91 \times 10^{-3}$ | $+2.12 \times 10^{-1}$ | 0.212 |
| **5** | $\mathbf{3.99 \times 10^{-4}}$ | $\mathbf{+1.02 \times 10^{0}}$ | **1.016** |
| 6 | $8.35 \times 10^{-5}$ | $+4.86 \times 10^{0}$ | 4.86 |
| 7 | $1.75 \times 10^{-5}$ | $+2.32 \times 10^{1}$ | 23.2 |

The best **unit-coefficient** fit is $k = 5$ with $c \approx 1.016$
(within $2\%$ of unity), suggesting the refined closed form
$$
  \boxed{\;
    \rho_Z^{\mathrm{constit}}(q_0)
    \;=\; (2q - 1) \,+\, h^5 \,+\, O(h^7)
  \;}
  \tag{$\star\star\star$}
$$
at the substrate point. Evaluated at $q_0$:

$$
  (2q_0 - 1) + h(q_0)^5 \;\approx\; 1.2203565
$$

versus the measured $\rho_Z^{\mathrm{constit}}(q_0) \approx 1.2203629$
— a residual of $6.3 \times 10^{-6}$ ($\mathbf{64\times}$ better than
$(2q - 1)$ alone).

### Open questions

1. ~~**Confirm the $O(h^5)$ form via varying-q measurement.**~~
 **Phase 5k.2: FALSIFIED** (see banner at top). The varying-$q$
 sweep showed that $\rho_Z^{\mathrm{constit}}(q)$ does NOT follow
 $(2q - 1) + h^5$; the $q_0$ match is a localised tangency, not
 a structural identity.

2. **What IS the closed form?** Open: identify the actual
 categorical structure of $\rho_Z^{\mathrm{constit}}(q)$. The
 measured ratio grows from $\rho(1.05) = 0.79$ to $\rho(1.17) = 1.79$
 — a factor of $2.26\times$ across only $0.12$ in $q$, much steeper
 than $(2q-1)$. **Phase 5l RESOLVED this**: the actual closed form
 is $\rho_Z^{\mathrm{constit}}(q) = \mathrm{tr}_M^3(\mathcal{B}_p, q)$ — exact,
 not "non-polynomial combination plus z-factors". See
 [`prop:constit-factor-tau-M-proton-identity`](#prop:constit-factor-tau-M-proton-identity)
 for the Wenzl-derivation and machine-precision verification.

3. **Operator-level derivation of $2q - 1$ from the Hecke skein.**
 The form $2q - 1$ matches $\sigma + \sigma^{-1}$ acting on the
 trivial channel idempotent $e_+ = (\sigma + q^{-1}) / (q + q^{-1})$,
 suggesting an averaging-channel interpretation parallel to the
 $\cosh(h)$ eigenvalue identity (see
 [`alpha-cosh-h-z-step-correction.lean §2`](alpha-cosh-h-z-step-correction.lean)).
 The §3b-cond class `ConstitFactor2qMinus1` axiomatises this; the
 operator-level proof is queued.

4. **Higher-rank extensions.** Does the same $(2q - 1)$ companion
 hold for $H_{3A}$ at $A > 4$? The constit-side factor is
 independent of $A$ (disjoint product), so the identity should
 extend by definition — but the categorical fit needs verification.

### Implementation reference

- Script: [`computations/constit_factor_and_volhyp_test.py`](../../../computations/constit_factor_and_volhyp_test.py) (Phase 5g categorical scan)
- Witness: `computations/constit-factor-and-volhyp.witness.json` (results recorded; categorical-search assertion passes)
- Companion proposition: [`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z) (interface factor $z$, exact)
- Single-block companion: [`conj:alpha-cosh-h-z-step-correction`](#conj:alpha-cosh-h-z-step-correction) ($|\Delta_\lambda^*|$ level)
- Audit: [`docs/audits/2026-05-20-phase5g-5h-5i-results.md`](../../../docs/audits/2026-05-20-phase5g-5h-5i-results.md) §5g
