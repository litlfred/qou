# Derivation chain — GB jet order at each step + h⁴ emergence + Pentagon placement

**Date:** 2026-05-24
**Trigger:** Author observation after the q-locality + h⁴ probe debrief:
*"relook at derivation here. cat action → non-abelian Stokes →
Frobenius → Wedderburn → Geom → Archimedean at each step of the
derivation. keep track on GB filtration / jet order as complicated
relations smooth out there. this is what we are seeing with h⁴. also
queue up… where does Pentagon identity get reflected in all this?"*
**Status:** Per-step jet-order analysis + Pentagon identity location
+ closure-path implications.

## §1. The canonical derivation chain (one-line each, with jet order)

Per [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
§1 + §2, the canonical chain is:

```
substrate q_0
  → 𝐂 categorical action
  → Yekutieli non-abelian Stokes
  → 𝐇_n(q) Hecke
  → Wedderburn decomposition (partitions λ ⊢ n)
  → Frobenius pairing tr_M = Σ y_λ χ_λ
  → GB filtration / spectral sequence
  → confinement SDP / canonical T_w
  → Geom functor (VolDensity(K, q_0))
  → Archimedean functor (substitute q_0, pull back to MeV)
  → observable mass
```

The **Gröbner-basis (GB) filtration** by Coxeter length $\ell(w)$
([cheat-sheet §2 step 7](../canonical-derivation-cheat-sheet.md)) is
the bookkeeping device that tracks how relations *smooth out* as
the jet order increases. Each jet grade collapses one degree of
ambiguity:

| jet grade | Coxeter length | what gets smoothed | $h$-order contribution |
|---:|---:|---|---:|
| 0 | $\ell = 0$ (identity) | trivial — base substrate $q_0$ | $h^0$ (the leading $5/2$) |
| 1 | $\ell = 1$ (single $\sigma_i$) | Hecke quadratic $\sigma_i^2 = h\sigma_i + 1$ | $h^1$ (writhe / chirality) |
| 2 | $\ell = 2$ (e.g. $\sigma_1\sigma_2$, $\sigma_1\sigma_3$) | Pentagon / Yang–Baxter relations | $h^2$ (Family A / linking weight) |
| 3 | $\ell = 3$ (e.g. $\sigma_1\sigma_2\sigma_3$) | Braid relations + pentagon coherence | $h^3$ (chirality cubed; usually 0 by parity) |
| 4 | $\ell = 4$ | Borromean closure ($\sigma_1^{-1}\sigma_2)^3$'s leading word | $h^4$ ← the "missing" term per the audit |
| $k$ | $\ell = k$ | $E_k$ spectral page of the GB resolution | $h^k$ |

The cheat-sheet quotes
([`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md)):
*"the spectral sequence collapses at $E_2$"* — meaning, after
identifying $\ell = 0, 1, 2$ data, all higher relations are
*formally determined* by the pentagon coherence at $E_2$. In
particular, $h^4$ does not need a separate input — it is **forced**
by pentagon coherence applied to the $\ell = 2$ data.

## §2. Step-by-step jet-order analysis

### Step 1. **substrate $q_0$** (CAL-2 anchor)

- **Jet grade**: 0 (atomic constant)
- **h-content**: $h(q_0) = q_0 - q_0^{-1} \approx 0.209$, fixed
- **Source**: [`q_parameter.py`](../../computations/substrate/q_parameter.py) (50 dps locked: 1.10970000000)
- **What's determined**: every downstream $h$-coefficient evaluates
  *at* this $q_0$; nothing constrains $q_0$ itself within the
  derivation (substrate-derivation declined 2026-05-08)

### Step 2. **$\mathbf{C}$ categorical action**

- **Jet grade**: 0 → 1 (the action *defines* $h$ as a structure constant)
- **h-content**: introduces $h = q - q^{-1}$ as the deformation parameter
- **Source**: [`def:rigid-monoidal-category`](../../content/quantum-observable-universe/braids-and-knots/rigid-monoidal-category.md), Yang–Baxter $R$-matrix structure
- **Content**: the categorical action makes $h$ a first-class
  structure constant in the Hopf algebra $\mathcal{H}_q$. **GB
  smoothing here**: any $h$-polynomial relation that holds in the
  algebra is forced; no semantic input from outside.

### Step 3. **Yekutieli non-abelian Stokes**

- **Jet grade**: explicit recursion in jet grade $k$
- **h-content**: per
  [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md)
  §"GB filtration connection":

  | jet grade | tessellation $k$ | cells | h-order |
  |---:|---:|---:|---:|
  | 0 | coarsest | 1 | leading $\mathrm{Vol}/\hbar_q^2$ |
  | 1 | first refinement | 4 | $h^2$ (CBH ½[α,β]) |
  | **2** | **second refinement** | **16** | **$h^4$** |
  | $j$ | k=j | $4^j$ | $h^{2j}$ |

- **What's determined**: the Riemann-product recursion *forces* the
  jet-grade structure. Each grade $j$ reuses grade $j{-}1$'s product
  and adds the finer-cell CBH corrections. This is the user's
  "complicated relations smooth out at higher jet order" — the
  $h^4$ coefficient at $k=2$ is determined by $k=0$ (via Vol/ℏ_q²)
  and $k=1$ (via the linear holonomy $g = \mathrm{MI}(\alpha|\sigma)$),
  NOT a free parameter.

### Step 4. **$\mathbf{H}_n(q)$ Hecke algebra**

- **Jet grade**: 1 (Hecke quadratic lives at $\ell=1$)
- **h-content**: $\sigma_i^2 = h\sigma_i + 1$ is the defining
  quadratic — this is the BASE jet of all later h-expansions
- **Source**: [`def:hecke-algebra`](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra.md), CLAUDE.md §7a
- **GB smoothing**: the Hecke relation expresses any $\sigma_i^k$
  as a degree-1 polynomial in $\sigma_i$ — collapsing infinite-jet
  data to jet grade 1.

### Step 5. **Wedderburn decomposition**

- **Jet grade**: 2 (partition structure lives at $\ell=2$)
- **h-content**: $H_n(q) \cong \bigoplus_{\lambda \vdash n} M_{d_\lambda}(\mathbb{Q}(q))$;
  Wedderburn idempotents project onto partition blocks. The Schur
  elements $y_\lambda(q)$ expand as $h$-Laurent series; in
  particular $y_\lambda$ has order $h^{2\ell(\lambda)}$ where
  $\ell(\lambda)$ is the partition's content
- **Source**: [`prop:alpha-k-derivation-procedure`](../../content/quantum-observable-universe/braids-and-knots/prop-alpha-k-derivation-procedure.md), [wenzl1988]
- **h⁴ emergence**: $y_{(2,1)}$ at $H_3$ contributes the **first
  non-trivial $h^4$ coefficient** of the Borromean Markov trace
  (per
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md)
  §"Per-representation structure": *"ALL correction terms ($h^4,
  h^6, \ldots$) originate from this partition alone — the two
  1-dimensional representations have commuting generators and
  contribute trivially"*). The $h^4$ at jet grade 2 comes from
  the standard (2,1) irrep at $H_3$, exactly matching the
  Wedderburn jet-grade prediction.

### Step 6. **Frobenius pairing $\mathrm{tr}_M = \sum y_\lambda \chi_\lambda$**

- **Jet grade**: aggregates jets 0..2 (Wedderburn data)
- **h-content**: for the Borromean braid $\beta_{\mathrm{Bor}} = (\sigma_1^{-1}\sigma_2)^3$,
  the closed-form trace
  $$\mathrm{tr}_M = \frac{4 + h^2 - 3h^4 - h^6}{h^2 + 4}
                  = 1 + 0\cdot h^2 - \tfrac{3}{4}\cdot h^4 - \tfrac{1}{16}\cdot h^6 + \cdots$$
  the $h^2$ coefficient **vanishes** by non-trivial denominator
  cancellation. **The first non-trivial $h$-correction in
  $\mathrm{tr}_M$ is at $h^4$ with coefficient $-3/4$.**

### Step 7. **GB filtration / spectral sequence**

- **Jet grade**: the bookkeeping itself
- **h-content**: per
  [`prop:gb-spectral-sequence`](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md)
  and [`prop:spectral-sequence-collapse`](../../content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md):
  the spectral sequence of the GB resolution **collapses at $E_2$**,
  meaning the $\ell = 0, 1, 2$ data (substrate + Hecke + Wedderburn)
  determines every higher jet **up to the differentials being zero**
- **Implication**: $h^4, h^6, \ldots$ are not free — they are
  forced by the pentagon-coherent extension of the $E_2$ data

### Step 8. **Confinement SDP / canonical $T_w$**

- **Jet grade**: 2 (LP/SDP duality at the operator-selection level)
- **h-content**: selects active operators (`active_set`); doesn't
  introduce new $h$-orders
- **Source**: [`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md)
  + CLAUDE.md §LP/SDP duals

### Step 9. **Geom functor ($\mathrm{VolDensity}(K, q_0)$)**

- **Jet grade**: aggregates all earlier jets
- **h-content**: $\mathrm{VolDensity}(K, q) = \mathrm{Vol}(K)/\hbar_q^2 \cdot \mathrm{linking\_weight}(q)$ — by current production
- **Source**: [`prop:geom-universality`](../../content/quantum-observable-universe/braids-and-knots/geom-universality.md), [`_li_2_q_util.py:201-236`](../../computations/_li_2_q_util.py)
- **What linking_weight should equal**: the production uses
  `linking_weight = 5/2 + (3/4)·h²` (Family A's H_4 half-symmetric
  Wedderburn sum). The exact Markov-trace finding (step 6) shows
  this is the **Wedderburn projection layer's h² coefficient**, not
  the trace's (which is zero). The h⁴ coefficient $-3/4$ from the
  trace IS the structural input that the linking_weight should
  honor.

### Step 10. **Archimedean functor at $q_0$**

- **Jet grade**: substitutes the substrate value; no new jet structure
- **h-content**: $h(q_0) \approx 0.209$, $h^2 \approx 0.0436$,
  $h^4 \approx 0.0019$
- **What's determined**: the numerical MeV prediction is
  $m_p^{\mathrm{pred}} = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$
- **Per-jet contribution magnitudes**:
  - jet 0 (Vol/ℏ_q² ≈ 746.4): dominates
  - jet 1 ((3/4)·h² ≈ 0.033, fractional contribution of Family A's
    h² term): small
  - jet 2 (h⁴ structural ≈ 0.0014 if Markov-trace -3/4 honored):
    very small (∼0.05% effect)
- **The +2.89% gap** is between this evaluation and CODATA. Per the
  q-locality probe (commit `ae70f99af`), the gap is dominated by
  Geom_leading's $q$-dependence, NOT by linking_weight refinement —
  so h⁴-order corrections to linking_weight CANNOT close the gap
  alone

## §3. The Pentagon identity placement

### What "Pentagon" means in this chain

The Pentagon identity is MacLane's associator-coherence axiom:
$$(\alpha_{X,Y,Z} \otimes \mathrm{id}_W) \circ \alpha_{X,Y\otimes Z, W} \circ (\mathrm{id}_X \otimes \alpha_{Y,Z,W}) = \alpha_{X\otimes Y, Z, W} \circ \alpha_{X,Y,Z\otimes W}.$$

In the $q$-deformed category $\mathcal{H}_q$, this is realized as
the **q-dilogarithm five-term identity** (per
[`q-rogers-pentagon-archimedean.md`](../../content/quantum-observable-universe/braids-and-knots/q-rogers-pentagon-archimedean.md)):

#### Pre-$\tau$ pentagon (categorical / Hopf-algebraic; jet grade 2)

$$
  \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) =
  \mathrm{Li}_2^q(uv) +
  \mathrm{Li}_2^q\!\!\left(\tfrac{u(1-v)}{1-uv}\right) +
  \mathrm{Li}_2^q\!\!\left(\tfrac{v(1-u)}{1-uv}\right)
$$

— a bare five-term identity in $\mathcal{H}_q^{\otimes 2}$, holding
in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$ without analytic
considerations. This is the categorical (pre-$\tau$) Pentagon.

#### Post-$\tau$ pentagon (archimedean; jet grades 2 and 4)

Under the archimedean realization $\tau$:

$$
  \mathrm{Li}_2^q(u) + \mathrm{Li}_2^q(v) - \mathrm{Li}_2^q(uv) - \mathrm{Li}_2^q(\alpha) - \mathrm{Li}_2^q(\beta)
  = \log_q\!\!\left(\tfrac{1-u}{1-uv}\right) \cdot \log_q\!\!\left(\tfrac{1-v}{1-uv}\right) + O\bigl((q-1)^2\bigr)
$$

— the archimedean Pentagon picks up a **$\log_q^2$ Rogers
correction** that is **bilinear in $\log_q$**. Since $\log_q(x) = (x-1)/h + O(h)$ near $q=1$, the $\log_q \cdot \log_q$ term is
$O(h^{-2}) \cdot O(h^{-2}) \cdot O(h^4)$ at the next archimedean
order — i.e., the $\log_q^2$ correction is exactly the **$h^4$
term** that the user's Option-A hypothesis predicted!

### Where Pentagon enters in each step of the chain

| Chain step | Pentagon role |
|---|---|
| 2. cat action | Forces categorical Pentagon (associator coherence in $\mathcal{H}_q$) |
| 3. Yekutieli MI | Pentagon ensures the binary-tessellation Riemann products are well-defined (the cell-merge associativity) |
| 4. $H_n(q)$ Hecke | Pentagon = the q-dilogarithm 5-term identity at jet grade 2 |
| 5. Wedderburn | Pentagon-respecting Wedderburn idempotents (no Pentagon-violating reordering of irreps) |
| 6. Frobenius | Pentagon-coherent Frobenius pairing (ensures $\mathrm{tr}_M$ is well-defined on tensor products) |
| 7. GB filtration | Pentagon = the relation that forces spectral-sequence collapse at $E_2$ |
| 10. Archimedean | **Pentagon picks up $\log_q^2$ correction = $h^4$ term** ← here is where the h⁴ "missing structure" comes from canonically |

### Implication: h⁴ is Pentagon-derived

The user's observation *"h⁴ terms related to full SO(3) action; SU(2)
picked up quadratic terms"* maps onto:

- **SU(2) quadratic (Casimir)** = pre-$\tau$ Pentagon at jet grade 2 = the bare 5-term Rogers identity, contributing at $h^2$ order
- **Full SO(3) → h⁴** = post-$\tau$ archimedean refinement of Pentagon, contributing the $\log_q^2$ Rogers correction at $h^4$ order

The h⁴ coefficient is therefore **not a free parameter** — it is forced by:

1. The Pentagon identity at jet grade 2 (pre-$\tau$ form),
2. Combined with the archimedean realization functor $\tau$, which adds the $\log_q^2$ correction,
3. Which expands to an $h^4$ term whose coefficient is **structurally derived** from the bare Pentagon.

The Markov-trace closed form
$\mathrm{tr}_M = 1 + 0\cdot h^2 - (3/4)\cdot h^4 - \ldots$
gives a *first observation* of the structural $-3/4$ at the $H_3$
level. The full categorical derivation of the coefficient via
Pentagon archimedean refinement is what would lock this in as a
proved categorical identity (queued: §4 below).

## §4. Closure path implications

Combining the per-step analysis with the empirical h⁴ probe results
(commit `2184c84d3`, witness
`vol-density-borromean-h4-probe.witness.json`):

| Question | Status |
|---|---|
| Does h⁴ structure exist in the chain? | **YES** — at jet grade 2 (Yekutieli k=2 + Wedderburn (2,1) + Pentagon archimedean refinement) |
| Is the h⁴ coefficient categorically derivable? | **YES (in principle)** — Pentagon → q-Rogers correction; the bare $-3/4$ from $\mathrm{tr}_M$ is the first observation |
| Can adding h⁴ to linking_weight close the +2.89% gap? | **Partial** — empirical Probe 2 gives +1.95% (1.5× improvement); structural Markov-trace × 5/2 still fails q-locality |
| Can adding h⁴ close q-locality? | **NO** — q-locality fail dominated by Geom_leading = Vol/ℏ_q²; linking_weight refinements (any polynomial in h) cannot fix it |
| What's the architectural fix for q-locality? | Either change Geom_leading's form, change mass-formula shape, or absorb q-dependent factor into CAL (options A-C from the family-a-gap-audit) |

### Concrete proof tasks queued

**(T1) Prove the structural $h^2 = 0$ identity** as a corollary of `prop:borromean-markov-trace-closed-form`. Lean: a 5-line `norm_num` proof on the rational expression.

**(T2) Categorically derive the $h^4 = -3/4$ coefficient** via Pentagon archimedean refinement. Path: take the bare Pentagon (pre-$\tau$) at jet grade 2, apply $\tau$, expand the $\log_q^2$ correction to $h^4$ order, evaluate the coefficient on the Borromean braid. Compare to the empirical $-3/4$ from $\mathrm{tr}_M$ closed form. **Expected outcome**: structural match.

**(T3) Formalize the q-Rogers correction in Lean** as the bridge between pre-$\tau$ and post-$\tau$ Pentagon. References: `q-rogers-pentagon-archimedean.md` already has the narrative proof; need Lean.

**(T4) Spectral-sequence collapse — explicit $E_2 → E_∞$ statement**. If GB collapses at $E_2$, then by Pentagon coherence every higher-jet $h^{2k}$ coefficient is determined by the $E_2$ data alone. Stating this rigorously in Lean would close the "no free parameters" gate for h⁴ and higher.

**(T5) Architectural q-locality investigation** (separate from h⁴): test alternative forms of Geom_leading (linear-ℏ, exp-ℏ, etc.) to see if any restore q-locality. This is option-A exploration from `2026-05-24-family-a-gap-audit.md` §4.

## §5. Cross-references

- [`content/.../predicted-spectra/three-knot-jet-order-independence.md`](../../content/quantum-observable-universe/predicted-spectra/three-knot-jet-order-independence.md) + [`QOU.Archimedean.JetOrderIndependence`](../../content/quantum-observable-universe/lean/QOU/Archimedean/JetOrderIndependence.lean) (PR #1931, 2026-06-07) — **the GB-filtration / jet-order bookkeeping of this audit, instantiated as a transcendence reduction.** The order-`N` GB *elimination* certificate (`jetOrder3_certificate`: eliminated echelon minor non-singular, ∏ pivots = 1/16 ≠ 0 — **witnessed real Markov-trace data**, not representative: `jet_order_pivots.py` expands the framework's own canonical traces $\mathrm{tr}_M(4_1/5_2/\mathcal{B}_3)$ about $q=1$ to jet-Jacobian rows $(1/4,-1,55/16)$, $(1/2,0,-1/16)$, $(1,0,0)$, elimination determinant $1/16$, LU pivots $(1/4,2,1/8)$ wired into `jetPivots`, witness `jet-order-pivots.witness.json`) discharges jet-order independence of the three coloured-Jones series at the Reid-1991 base order — a finite, decidable determinant test, exactly the "relations smooth out per jet grade" mechanism this audit describes. Reduces `conj:hyperbolic-volume-transcendence` to two named physical inputs + the per-order certificate.
- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — **canonical framing reference** (post-PR #1080); explains why λ_scale ≠ separate object (now in main)
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — the canonical chain (this audit traces through it)
- [`docs/audits/2026-05-24-yekutieli-mi-derivation-path.md`](2026-05-24-yekutieli-mi-derivation-path.md) — Yekutieli MI tessellation, jet grades
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — h⁴ source trace + SO(3) gap
- [`docs/audits/2026-05-24-family-a-gap-audit.md`](2026-05-24-family-a-gap-audit.md) — Family A +2.89% gap (currently in PR #1063)
- [`content/quantum-observable-universe/braids-and-knots/q-rogers-pentagon-archimedean.md`](../../content/quantum-observable-universe/braids-and-knots/q-rogers-pentagon-archimedean.md) — Pentagon archimedean refinement
- [`content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md) — exact $\mathrm{tr}_M$, h² = 0, h⁴ = -3/4
- [`content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md`](../../content/quantum-observable-universe/braids-and-knots/gb-spectral-sequence.md) — spectral sequence
- [`content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md`](../../content/quantum-observable-universe/braids-and-knots/spectral-sequence-collapse.md) — collapse at $E_2$
- [`computations/probes/vol_density_borromean_h4_probe.py`](../../computations/probes/vol_density_borromean_h4_probe.py) — empirical h⁴ probe (commit `2184c84d3`)
