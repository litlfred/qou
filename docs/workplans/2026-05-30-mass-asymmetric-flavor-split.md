# Mass-asymmetric flavor-split workplan (m_n residual closure)

Date: 2026-05-30
Author: agent on `claude/meson-prod-wire-2026-05-29` (#1451)
Context: after `m-p-substrate-identity-50dps` witness regen, m_n
sits at **1.04 ppb** vs CODATA — at the 100× target it's 181×
off, but at experimental σ it's within 2σ_exp. The residual is
flavor-split-derived; this workplan concretises the categorical
closure.

## What's open

The production m_n formula:

```
m_n = m_p · (1 + X(q) / (1 − X(q)/2))
```

uses a Hecke-skein traffic invariant `X(q)` that depends only on
the topological u↔d flip in the baryon word. It's **flavor-blind**
— it doesn't see the empirical m_d ≈ 2.16 · m_u asymmetry. The
residual 1.04 ppb is essentially the gap between `X(q)` and a
mass-asymmetric `X(q, m_d/m_u)` derived from first principles.

## What's already evidence

- **PR #1445** scaffolds `class ColorFlavorCompatible` with a
  `weight : QuarkType → QuarkType → R → R` open class field
  (mass-asymmetric Bring color-tube weight). The 9-pair
  decomposition 2·(u,u) + 4·(u,d) + 1·(d,u) + 2·(d,d) from
  `p = uud × n = udd` is already in the Lean structure.
- **`probe_pn_flavor_asymmetry.py` Scheme 4** (per-sheet PL
  integration on Bring's surface) reproduces `Δm_{n-p}` to ≈0.14%
  of CODATA — empirical evidence the framework's bones support it.
- **`lambda_scale_refinement_h4_correction_bring.py`** evaluates
  `1/(1 − h_q · q^{10})` at the substrate; the `q^{10}` exponent
  is the Bring genus-class exponent that should generalise to
  `q^{10 + k_{12}}` with `k_{12}` the flavor-displacement.

## What needs to land (in order)

### Step 1 — derive `k_{12}` for each quark-type pair (open math)

`k_{12}(q_1, q_2)` for `q_i ∈ {u, d}` should fall out of:

- the Bring color-tube symmetry under quark-type permutation, OR
- the Hecke partition's branching by quark TYPE (a refinement of
  the Wenzl `y_λ` weighting to per-tableau weights `y_{λ,T}` that
  see the cell-by-cell U/D labeling)

Expected: `k_{uu} = k_{dd} = 0` (same-type, no flavor cost);
`k_{ud} = k_{du} ≠ 0` (mixed pair carries the m_d/m_u tension).
Anti-symmetry vs CPT: `k_{ud} = k_{du}` (bar-invariance) → one
free parameter.

**This is the load-bearing open math.** Without it, downstream
steps are blocked.

### Step 2 — connect `k_{ud}` to a categorical invariant

Must be one of:

- a Catalan / Lobachevsky integral over the Bring color-tube fibre
  of a u↔d face (so `k_{ud}` derives from hyperbolic geometry);
- a Hecke partition's mixed-symmetry character at H_2 (so
  `k_{ud} = χ_{(1,1)}(σ_1) / χ_{(2)}(σ_1)` or some such ratio);
- a Wenzl seed weight `y_{(1,1)} / y_{(2)}` at n=2 (operator-
  reduction down to the 2-body face).

The probe `probe_pn_flavor_asymmetry.py` Scheme 4 numerics gives
the **empirical** `k_{ud}` value; the open math is identifying
which categorical object it equals.

### Step 3 — compute `m_d / m_u` from the derived `k_{ud}`

The framework should predict `m_d / m_u` from `k_{ud}` and `q_0`
via a closed form along the lines of:

```
m_d / m_u = (1 − h_q · q^{10}) / (1 − h_q · q^{10 + k_{ud}})
```

(structurally; exact form depends on Step 2). Sanity check: does
this give 2.16(7) at the substrate? **No fitting.** If the answer
is 2.17 the framework wins; if it's 1.8 or 2.7 something is wrong
in Step 2's identification.

### Step 4 — recompute m_n with mass-asymmetric X

Replace the current `X(q)` in `m-p-substrate-identity-50dps.py`
with `X(q, m_d/m_u from Step 3)`. Expected: m_n drops from
1.04 ppb to ≤0.1 ppb (within the 100× target of 0.006 ppb if
no other residual is masking — likely there's a residual EM
correction also present).

### Step 5 — Lean-formalise the chain

Close the open `ColorFlavorCompatible` instance in `pn-averaging-
uniqueness.lean` (PR #1445) with the explicit `k_{ud}` from Step
1-2. Cross-link to a new prop `prop:mass-asymmetric-flavor-split`
that states the closed form derived in Step 3-4.

## Probes to write (in order)

| Order | Probe | Purpose |
|---|---|---|
| 1 | `pn_flavor_asymmetry_per_tableau_weight.py` | Compute Scheme-4 PL integration's `k_{ud}` precisely; tag as empirical baseline |
| 2 | `bring_color_tube_k_ud_categorical.py` | Test candidate Step-2 identifications against the empirical `k_{ud}` |
| 3 | `m_d_m_u_categorical_prediction.py` | Step 3 closed form; cross-check against PDG 2.16(7) |
| 4 | `m_n_path_d_mass_asymmetric.py` | Production candidate: m_n via mass-asymmetric X; report residual |

## Dependencies

- **Gates:** PR #1443 (operator-valued LR-branching) for the
  symmetric EM-channel companion direction (`baryon_em_sinh_
  operator_valued_probe.py`), and PR #1445 (`ColorFlavorCompatible`
  scaffold) for the Lean axiomatic layer. Probe 1 doesn't gate on
  either — it's data-side prep work that can start today.
- **Companion direction:** baryon EM sinh-channel (#1443) is a
  separate residual contributing to the 1.04 ppb. Both directions
  may need to land for the 100× target; they're not exclusive.

## What this is NOT

- Not a one-session task — Step 2's identification is research-
  level open math.
- Not a fit — the discipline review will catch any "we tried 4
  candidate forms and picked the one closest to PDG" pattern.
  The Step-2 identification must be **derived**, not selected.
- Not a CAL-4. m_d / m_u is **predicted** from `q_0` and `k_{ud}`,
  not added as a fourth calibration input.

## Status pin

Tracking this workplan from the m_n row's source_witness in
[`per_observable_100x_status.py`](../../folio-assistant/computations/per_observable_100x_status.py)
and from PR #1445's `pn-averaging-uniqueness.md` `ColorFlavor
Compatible` open class.

---

## Full queued queue (m_n closure — full landscape)

This is the broader queue of work items for closing m_n past
the 100× experimental target. Items are ordered by:
(a) dependency (lower items may gate on higher ones),
(b) tractability (within "open math" tier; none are "rerun
    a script"),
(c) which sibling PR they couple with.

### Direction 1 — Δ-isospin breaking via Hecke EM channel (`gates: #1443`)

The same `(α_em/π)·(3q² − 1)/(2q²)` correction that closed the
meson sinh-channel ([`prop:meson-em-sinh-closed-form`](../../content/quantum-observable-universe/braids-and-knots/meson-em-sinh-closed-form.md))
should have a baryon analog via the **operator-valued LR-branching**
of [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/mass-endomorphism/hecke-branching-trace-decomposition.md)
(PR #1443).

| #  | Item | Status | Gates on |
|----|---|---|---|
| 1.1 | Probe stub `baryon_em_sinh_operator_valued_probe.py` | ✓ stubbed (this branch, audit-only) | — |
| 1.2 | Replace stub `I_EM` with operator-valued formula from #1443 | Queued | #1443 merge |
| 1.3 | Compute `A^{(2,1)}_{(1),(1,1)}(I_EM)` on Hoefsmit H_3 basis (entries already in `gram-matrix-h3-symbolic.lean`) | Queued | 1.2 |
| 1.4 | Cross-check candidate residual closure (target: reduce 1.04 ppb m_n by ≥ 50%) | Queued | 1.3 |
| 1.5 | Lean-formalise as `prop:baryon-em-sinh-closed-form` (companion to meson prop) | Queued | 1.4 |

### Direction 2 — Mass-asymmetric flavor-split (`gates: #1445`)

Extend the production `X(q)` (currently flavor-blind, q-rational)
to `X(q, m_d/m_u)` where the categorical mass ratio is **derived**
from the Wenzl-y partition weighting on `(udd)` vs `(uud)` (NOT
fitted to PDG). Closes the open `class ColorFlavorCompatible`
field from PR #1445.

| #  | Item | Status | Gates on |
|----|---|---|---|
| 2.1 | Probe `pn_flavor_asymmetry_per_tableau_weight.py` — empirical baseline `k_{ud}` from Scheme-4 PL integration | Queued | — (data-side prep, no sibling gate) |
| 2.2 | Derive `k_{ud}` from Bring color-tube symmetry (**geometric** — fibre symmetry on the u↔d face) | Queued (open math) | 2.1 |
| 2.3 | Connect `k_{ud}` to a categorical invariant — Hecke partition weight `y_{(1,1)} / y_{(2)}` candidate, OR Catalan / Lobachevsky integral over Bring's surface | Queued (open math) | 2.2 |
| 2.4 | Compute predicted `m_d / m_u` from closed-form `k_{ud}` | Queued | 2.3 |
| 2.5 | Verify `m_d / m_u` matches PDG 2.16(7) **without fitting** — if it lands wrong, Steps 2.2-2.3 wrong, do not adjust | Queued (discipline gate) | 2.4 |
| 2.6 | Production probe `m_n_path_d_mass_asymmetric.py` — m_n via mass-asymmetric X; expected residual ≤ 0.1 ppb | Queued | 2.5 |
| 2.7 | Close `ColorFlavorCompatible.weight` class field on PR #1445 with derived `k_{ud}` | Queued | 2.5 (math), #1445 merge (Lean) |
| 2.8 | New prop `prop:mass-asymmetric-flavor-split` capturing the closed form | Queued | 2.7 |

### Direction 3 — Brane-tower correction (CAUTION: prior fit retracted)

A higher-rung `h_q^k` term may contribute. **#1422 audit
explicitly retracted the fitted brane-tower** (`(1 + 46 u⁴)(1 + 4 u⁵)(1 − 29 u⁶)(1 − 8 u⁷)`)
as a CODATA fit, not a Taylor expansion. Genuine higher-order
must be **derived from first principles**.

| #  | Item | Status | Gates on |
|----|---|---|---|
| 3.1 | Identify the categorical source of the Habiro Taylor coefficients — should converge to the substrate value, not overshoot to CODATA | Queued (open math; do NOT propose new ansatz, the discipline review will catch it) | — |
| 3.2 | If derived, cross-check Taylor convergence direction | Queued | 3.1 |

### SnapPy witness migration (its own PR — companion to BorromeanVolumeCatalan close)

Per the architectural discussion: every SnapPy-computed knot
volume in the framework should follow the three-layer pattern
(producer witness + cross-check + Lean per-manifold axiom).
The `vol_borromean = 7.32772475341775` literal in
`_li_2_q_util.py` is the last in-codebase hardcode and should
migrate first.

| #  | Item | Status |
|----|---|---|
| S.1 | New `snappy_borromean_volume.py` producer script — emits witness with tiered precisions (15 / 50 / 100 / 1000 dps) | Queued |
| S.2 | New `borromean_volume_catalan_cross_check.py` — verifies SnapPy value ≈ 8·G to declared precision | Queued |
| S.3 | Edit `_li_2_q_util.py` to read `vol_borromean` from witness, drop the literal | Queued |
| S.4 | New Lean module `QOU.Archimedean.SnapPyAxioms` with `axiom snappy_L6a4_volume : ℝ` + `axiom snappy_L6a4_volume_eq_vol_B3` named after SnapPy manifold | Queued |
| S.5 | Edit `BorromeanVolumeCatalan.lean` to consume the axiom rather than the bare literal | Queued |
| S.6 | (Optional, future) extend producer to a batch `snappy_knot_volume_catalog.py` for T(2,3), T(2,5), T(2,7), T(3,5), Whitehead, etc. — all per-manifold axioms | Queued (later PR) |

### Other proof-gap closures (off m_n track but on /coordinate goal)

| #  | Item | Status | Gates on |
|----|---|---|---|
| P.1 | Close 4 sorries in `BorromeanVolumeCatalan.lean` (Lobachevsky def, Λ(π/4)=G/2, S_22 numerical bounds, vol_B3=8G) | Queued | S.4 + S.5 (axiom layer easier to consume than bare literal) |
| P.2 | Close 1 sorry in `gram-matrix-h3-symbolic.lean` (6×6 symbolic det) via row-by-row Schur reduction | Queued (heavy LSP work) | — |
| P.3 | Help close PR #1445 uniqueness scaffolds (item 2: SDP `T_w` Mathlib strict-complementarity) | Queued | #1445 merge |
| P.4 | Help close `em-coupling-chern-simons` Witten-κ sorry (un-conditions PR #1451's CLASS-A banner) | Queued (open math) | — |

### Coordination state (as of 2026-05-30)

| PR | Theme | Coupled queue items |
|---|---|---|
| #1451 (in-flight) | m_K/m_π production wire | Done; awaiting explicit merge |
| #1443 | Hecke operator-valued LR-branching | Gates Direction 1 entirely |
| #1444 | α_em Bring zero-mode shift | Reduces CLASS-A banner on #1451 to ≈4 ppm if landed (separate from Witten-κ) |
| #1445 | Uniqueness scaffolds (mass-theory) | Gates Direction 2.7 + P.3 |
| #1449 | q₀ cleanup tail | Surfaced the m_p witness staleness this branch caught; no further coupling |
| #1450 | Clarabel LP/SDP MPFR≡f64 validate | Independent infra |

