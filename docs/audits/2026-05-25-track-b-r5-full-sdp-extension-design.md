# Track B — R5-full SDP extension to H_5 + H_12: design

**Date:** 2026-05-25
**Branch:** `claude/track-b-r5-full-sdp-design-2026-05-25`
**Track:** B (R5-full SDP at ⁴He via α-cluster cascade)
**Status:** design-only — no code changes; estimates the scope + value

## Premise

The audit body of PR #1257 highlighted the R5-full SDP solver for ⁴He
as *"the single highest-leverage mass-table fix"* — *"~5000 bps across
7 atoms via α-cluster cascade"*. This document is the design pass:
what code touches what, what new infrastructure is needed, and what
the headline observable would do.

## Current state (post PRs #1266, #1267, #1269)

### R5-full prototype scope

[`computations/r5_full_canonical_knot_solver.py`](../../computations/r5_full_canonical_knot_solver.py)
(860 LOC) currently covers exactly two atoms:

| atom | strands `n_0` | knot | status |
|---|---:|---|---|
| ²H deuteron | 3 (B_3 / H_3) | `6_2` | full R5-full search |
| ³He | 3 (B_3 / H_3) | `L6a4` | full R5-full search |
| ³H tritium | 5 (B_5 / H_5) | `8_11` | **DEFERRED** (Hoefsmit at H_5 not in prototype) |
| ⁴He | 12 (B_12 / H_12) | n/a | **NOT IN R5-FULL** — uses magic-A formula |

The H_3 Hoefsmit seminormal block matrices are hardcoded inline
([`hoefsmit_h3_blocks(q)`](../../computations/r5_full_canonical_knot_solver.py),
3 blocks: trivial (3), standard (2,1), sign (1,1,1) — 1+2+1 = 4 dims).

### ⁴He current formula

[`magic_A_formula.py`](../../computations/magic_A_formula.py)
implements the *magic-A* shell-closure rule:

```
B(⁴He) = ρ_F · m_e · A · 8G   (zero parameters; A=4; 8G = Vol(L6a4))
```

Current error: **+2.51%** vs AME (predicted 3438.466 MeV vs empirical
3451.144 MeV; per
`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`
line 101). Refined to **+0.37%** with the `cosh(h)` α-derivation correction.

### α-cluster cascade for ⁴He → 7 atoms

[`alpha_cluster_recursion.py`](../../computations/alpha/alpha_cluster_recursion.py)
extends ⁴He to six heavier α-chain atoms via:

```
B(nα) = n · B(⁴He) + C(n, 2) · c_αα,   n_α = A/4
```

Atoms in the cascade and α-cluster counts:

| atom | A | n_α | C(n_α, 2) |
|---|---:|---:|---:|
| ⁴He  | 4  | 1  | 0  |
| ⁸Be  | 8  | 2  | 1  |
| ¹²C  | 12 | 3  | 3  |
| ¹⁶O  | 16 | 4  | 6  |
| ²⁰Ne | 20 | 5  | 10 |
| ²⁴Mg | 24 | 6  | 15 |
| ⁴⁰Ca | 40 | 10 | 45 |

Closing the ⁴He systematic by `δ` ppm propagates approximately:

```
δ_per_atom(nα) ≈ n_α · δ(⁴He)
```

(The C(n_α,2) coefficient on c_αα is separate; this is the
n_α-multiplicative ⁴He propagation only.) For ⁴⁰Ca with n_α = 10,
a 50 ppm closure on ⁴He → 500 ppm closure on ⁴⁰Ca's predicted
binding. Across 7 atoms that's the "~5000 bps" headline.

## What R5-full extension would unlock

If R5-full could compute the canonical T_w for ⁴He (and tritium en
route), the cascade upgrades from a zero-parameter shell-closure
rule to a derived per-knot Markov-trace formula:

```
B(⁴He) = ρ_F · m_e · |tr_M(T_w(⁴He), q_0)|
```

This replaces the magic-A `A · 8G` ansatz with a categorical
quantity, removing the ~2.51% systematic at the source.

**Headline observable impact (estimate):**

| obs | current err | with R5-full ⁴He fix | improvement |
|---|---:|---:|---:|
| B(⁴He)  | +2.51% (25,100 ppm) | target ≤ 100 ppm | 250× |
| B(⁸Be)  | inherits +5% via 2·B(⁴He) | proportional |
| B(¹²C)  | inherits +7.5% via 3·B(⁴He) | proportional |
| B(¹⁶O)  | inherits +10% via 4·B(⁴He) | proportional |
| B(²⁰Ne) | inherits +12.5% via 5·B(⁴He) | proportional |
| B(²⁴Mg) | inherits +15% via 6·B(⁴He) | proportional |
| B(⁴⁰Ca) | inherits +25% via 10·B(⁴He) | proportional |

(Rough estimates; actual cascade involves c_αα corrections per the
recursion formula.)

## What the extension requires

### Phase B-1 — replace inline Hoefsmit with upstream Rust (H_3 → H_n generic)

The inline
[`hoefsmit_h3_blocks(q)`](../../computations/r5_full_canonical_knot_solver.py)
returns numpy arrays for 3 hardcoded blocks. Replace with calls
to `pyhecke_native`:

  - `pn.partitions_of(n)` — enumerate Wedderburn blocks
  - `pn.chi_lambda_braid(λ, word, q)` — character on a braid word
  - `pn.trace_weights_n(n, q)` — Wenzl JM (current convention)
  - or `pn.trace_weights_n_q_schur(n, q)` — q-Schur (closed form)

After PR #1263 (just merged), the common `markov_trace_for_knot`
infra is also available — could be the unified entry point.

**Scope:** ~200 LOC refactor; no new Rust needed. Mechanical.

### Phase B-2 — R5-full for tritium (H_5)

7 partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1⁵)
— 7 blocks. Hook-length dimensions: d_(5)=1, d_(4,1)=4, d_(3,2)=5,
d_(3,1,1)=6, d_(2,2,1)=5, d_(2,1,1,1)=4, d_(1⁵)=1. Max d_λ = 6 (at
partition (3,1,1)); total Wedderburn dimension Σ d_λ² = 120 = 5!.

**Scope:** Tritium added to `R5_FULL_SUBSTRATE_REGISTRY`. Search over
B_5 braid words length ≤ 8 (more candidates than B_3 — `4^L` vs `2^L`
sign choices, plus 4 generators vs 2). After Phase B-1 the seminormal
matrices come from pyhecke_native automatically.

**Performance:** B_5 search space at L=8 has 4 generators × 2 sign
choices per crossing, so the raw enumeration is `(4·2)^8 = 8^8 =
16,777,216` words. After the same adjacent-cancellation + canonical-
basis dedup pruning used at B_3 (which reduces 13,088 raw words to
2,556 evaluated candidates — a ~5× reduction factor), expected
evaluated candidates at B_5 are ~3.4M. Wall time with pyhecke_native
chi_lambda_braid in the back end: ~30 min – 2 hr per nucleon at
50 dps. Manageable but no longer "minutes-scale" — Rust kernel
parallelisation likely needed for joint deuteron + ³He + ³H sweep.

### Phase B-3 — R5-full for ⁴He (H_12)

77 partitions of 12. Hook-length-formula dimensions (verified via
sympy; the value `d_λ = n! / ∏ hooks(c)` over cells `c` of the
Young diagram):

```
d_(6,6)       = 132
d_(7,5)       = 297
d_(8,4)       = 275
d_(6,3,3)     = 1650
d_(4,4,4)     = 462
d_(5,3,2,1,1) = 7700    ← true max d_λ across all 77 partitions
```

Total Wedderburn dimension Σ d_λ² = 12! = 479,001,600 (Schur-Weyl
identity for S_12). Too big for inline numpy; must use the Rust
kernel (each block's chi_lambda_braid evaluation is O(d_λ² · word
length) per call — at max d_λ = 7700, one call is ~10^8 mpfr-ops
even before stacking 77 of them per candidate braid).

**Bottleneck — closed_form_tau_M reuse.** PR #1269 just landed the
`atomic_tr_m_helium4_canonical.py` path which gives ⁴He tr_M at
**0.32 s** via the Phase 5q closed form
(`compute_tau_M_nucleon_H3 → closed_form_tau_M`). Critically, this
**bypasses H_12 entirely** — only computes tau_p, tau_n at H_3 and
applies an interface decomposition.

This changes the R5-full ⁴He design:

- **Option α (full H_12 search):** B_12 braid words length ≤ L_max
  searched per candidate; each candidate evaluated via 77-block
  Hoefsmit. Even at L_max = 6 the search space is ~22^6 ≈ 113M words
  — needs Rust execution + caching. Multi-day to multi-week.

- **Option β (canonical-word-only via closed form):** Take the
  CANONICAL atom_braid_word_3A(2, 2) word (47 crossings, 3 interfaces)
  and evaluate via `closed_form_tau_M`. The "search" becomes
  selection of the canonical word + cross-validation vs the magic-A
  predicate. ~0.3s per atom. **This is essentially already done by
  PR #1269.**

- **Option γ (joint α-cluster R5):** Parametrise the α-cluster
  recursion's `c_αα` derivation through R5-full at H_3 on `7²_1`
  (Whitehead link). Currently `c_αα = m_e · Vol(7²_1) ≈ 2.4269 MeV`
  is a literature value. R5-full at H_3 for `7²_1` would give a
  categorical derivation. Doesn't need H_12.

**Recommended path:** Option γ → Option β → defer Option α.

  - **γ first** — closes the c_αα derivation gap in `alpha_cluster_recursion.py`
    using existing H_3 infrastructure. ~1 day.
  - **β second** — formal R5-full registration for ⁴He using the
    Phase 5q closed form (essentially wrapping PR #1269's compute).
    ~half a day.
  - **α deferred** — full H_12 search is multi-week and brings little
    additional value once γ + β land (since the categorical T_w for
    ⁴He routes through the Phase 5l canonical-word structure).

### Phase B-4 — α-cluster recursion derived c_αα

Currently `c_αα = m_e · Vol(7²_1)` uses the Whitehead-link
hyperbolic volume as a fixed literature constant. R5-full at H_3
applied to the `7²_1` braid would yield:

```
c_αα = m_e · |tr_M(T_w(⁷²₁), q_0)|
```

— giving a Markov-trace-derived `c_αα` that participates fully in
the substrate calibration chain.

**Scope:** Add `7²_1` to `R5_FULL_SUBSTRATE_REGISTRY` (still at
H_3). The braid word `(σ_1⁻¹ σ_2 σ_1⁻¹ σ_2² σ_1⁻¹ σ_2²)` is already
catalogued in
[`knot_braid_database.py`](../../computations/knot_braid_database.py)
(PR #1263).

## Estimated headline outcomes

If Phases B-1, B-2, B-3 (Option γ + β), B-4 all land:

| outcome | now | post-design-execution |
|---|---|---|
| R5-full atoms | 2 (²H, ³He) | 5 (+ ³H, ⁴He, c_αα) |
| ⁴He err | +2.51% (magic-A) | ≤ +100 ppm target (via closed form + categorical c_αα) |
| ⁴⁰Ca err | inherits ~25% | inherits ≤ ~1000 ppm |
| Total mass-table closure | — | ~5000 bps across 7 α-chain atoms |
| Infra | inline H_3 numpy | pyhecke_native upstream |

## What this design does NOT propose

- Does NOT propose a new Rust kernel beyond what
  pyhecke_native already exposes. The H_3 → H_5 → H_n
  generalisation is already in upstream Rust (per PR #1263
  cataloguing).
- Does NOT propose a full B_12 brute-force search (Option α);
  the Phase 5q closed form route (Option β) makes this
  unnecessary.
- Does NOT touch the substrate calibration discipline (CAL-1/2/3
  acknowledged anchors are preserved).

## Execution order if owner approves

1. **Phase B-1** (3–4 hours): refactor `r5_full_canonical_knot_solver.py`
   to use `pyhecke_native` instead of `hoefsmit_h3_blocks` inline.
   Single PR, mechanical, no behavior change.

2. **Phase B-4** (1 day): add `7²_1` to R5-full registry at H_3.
   Derive `c_αα` from R5-full output and substitute in
   `alpha_cluster_recursion.py`. Quantify ⁸Be/¹²C/¹⁶O/²⁰Ne/²⁴Mg/⁴⁰Ca
   prediction shift.

3. **Phase B-2** (1 day): add ³H tritium (B_5 / 8_11) to R5-full.
   Verify against the existing H_3-restricted prediction (8_11 has
   B_5 canonical representative but might admit a B_3 representative
   too).

4. **Phase B-3 (Option β)** (half day): register ⁴He as R5-full atom
   via the Phase 5q closed form (per PR #1269). Cross-validate against
   the magic-A formula prediction; quantify the gap.

5. **Phase B-3 (Option γ)** is subsumed by B-4 above.

**Total: ~3 days serial, less if parallelised across PRs.**

## Cross-references

- [`computations/r5_full_canonical_knot_solver.py`](../../computations/r5_full_canonical_knot_solver.py)
- [`computations/magic_A_formula.py`](../../computations/magic_A_formula.py)
- [`computations/alpha/alpha_cluster_recursion.py`](../../computations/alpha/alpha_cluster_recursion.py)
- [`docs/audits/2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md`](2026-05-19-delta-lambda-phase5-alpha-derivation-progress.md) (the cosh(h) refinement)
- [`docs/audits/2026-05-25-phase5q-closed-form-reconciliation.md`](2026-05-25-phase5q-closed-form-reconciliation.md) (closed-form path that subsumes Option α)
- [`computations/atomic_tr_m_helium4_canonical.py`](../../computations/atomic_tr_m_helium4_canonical.py) (Option β realisation, PR #1269)
- [`computations/knot_braid_database.py`](../../computations/knot_braid_database.py) (7²_1 catalogue, PR #1263)
