# Compute-pipeline deep analysis + accuracy wiring / optimization

**Branch:** `claude/compute-pipeline-audit-generalize-2026-06-10`
**Date:** 2026-06-10
**Mandate (owner):** generalized infra so a user can request any nuclide /
observable from the outset; wire up everything possible for accuracy and
optimize; **NO FLOAT64** on the canonical path; **NO FITTING** beyond the
three calibrations (CAL-1 m_e, CAL-2 q₀, CAL-3 m_π).

This document is the synthesis target for a four-axis deep audit of the
current compute pipeline. Each axis is produced by a dedicated pass; the
findings are merged here into a single prioritized work-plan.

## 0. Scope and method

Anchored on `docs/canonical-derivation-cheat-sheet.md`. The audit asks, for
every script under `folio-assistant/computations/` and `tools/**`:

1. Is it on the **canonical path** (feeds a production observable) or
   exploratory?
2. Does it violate **NO FLOAT64** (canonical math must be mpmath/MPFR ≥50 dps)?
3. Does it violate **NO FITTING** (only the 3 calibrations are inputs)? Are there
   hardcoded CODATA literals or duplicated magic values instead of importing from
   a central registry (`codata_constants` / `content/values/registry.ts`, using
   canonical validation aliases like `M_P_MEV_VALIDATION`)?
4. Is it **wired** (consumed by the mass/binding sweep + L1/L2 dashboards) or
   orphaned?
5. Can it be **optimized** without losing precision (Rust port, batched FFI,
   caching, closed form replacing sympy)? Do long-compute scripts (>5 min) adhere
   to the Long-compute logging discipline (units/sec, wall elapsed, ETA)?

## 1. Axis A — FLOAT64 violations (canonical path)

**Verdict: production observable chain is MPFR-clean** — `closed_form_tau_M` →
`hecke_characters.chi_lambda_braid(precision="mpfr_50dps")` → Rust `*_mpfr`
kernels → `mass_formula_6term_mpfr_50dps` / `binding_canonical` /
`markov_trace_canonical` → `mass_table_ppb` / dashboards. The `float()` there
are tolerance-dispatch keys, witness-emit, or display. **6 canonical-path
violations remain** (scripts computing χ^λ / tr_M / Gram in f64), plus a tier of
benign tolerance-dispatch f64.

| id | file | leak | fix | priority |
|----|------|------|-----|----------|
| **C6** | `tools/hecke-engine` (`gram.rs`, `seminormal.rs`, `geck_pfeiffer.rs`) + `pyhecke-native/src/lib.rs` f64 exports; dispatched by `hecke_characters.chi_lambda_braid` | two-tier design (f64 + mpfr); a producer that **omits `precision="mpfr_50dps"` silently gets f64** | **fail-closed**: default wrapper to mpfr_50dps (or raise for witness producers) + CI guard + rename f64 kernels `_f64` | **1 (highest leverage)** |
| **C4** | `mass_at_3A_proper.py:285-304` `atom_braid_word_3A` | canonical braid constructor emits f64 `(c,d)` flavor-split; color-weight `-h·(0.5-δ/4)` flows un-re-lifted into numeric consumers | return `(c,d)` as `Rational`/`mpf`; compute `_avg_color_delta` + color-weight in mpf | **2 (spine + cascades)** |
| **C2** | `wedderburn_jones_markov.py:327,382-389` | canonical Jones-Markov `tr_M=Σ y_λχ^λ` does `float(y)*float(chi)`, emits witness | route χ via `chi_lambda_braid(mpfr_50dps)`; accumulate mpf; serialize strings | 3 |
| **C3** | `tr_m_q_hecke_seminormal.py:69,109-118` | canonical tr_M at **30 dps** + f64 χ; emits witness | 50-dps mpf q from `Q_50_DIGIT_STR`; mpfr χ; mpf accumulate | 3 |
| **C1** | `hoefsmit_numpy.py:86-161` | entire χ^λ engine in numpy.float64 (`mp.mpf(float(np.trace))`); canonical-shaped, currently exploratory consumers | route consumers to `chi_lambda_braid(mpfr_50dps)` or `mpmath.matrix`; delete numpy engine | 4 |
| **C5** | `mass_at_3A_proper.py:337-348,478-495` | numeric `chi_lambda_of_word`/`per_generator_V_hat_3A` in numpy.f64 (some `[DEPRECATED]`) | deprecate→`chi_lambda_braid(mpfr_50dps)`; seed `BlockCache` from `Q_50_DIGIT_STR`; `mp.log` | 4 |

**Benign tolerance-dispatch f64** (markov_peel:109, closed_form_tau_M:352,
canonical_braid_marshalling:96/141, binding_canonical:99) — match exact symbolic
`HA` via tolerance; **C4's exact-(c,d) fix makes these disappear repo-wide.**

**Leverage existing infra:** `audits/float64_leak_audit.py` is the repo's I8
scanner but **banner-only** (misses C1/C5 which lack banners) — widen it to the
canonical-script list (cheat-sheet §2/§7) and wire as the C6 CI guard.
`cross_check_trM_1ppb.py` is the model for correctly demoting an f64 method to a
"1e-12 check, not 1 ppQ-certifying" tier.

## 2. Axis B — FITTING / numerology leaks  ✅ clean on production

**Verdict: 0 production-leak violations.** The NO-FITTING / 3-calibration
discipline holds on every live prediction path. Genuine fits all sit in
`_deprecated/`, `probe_*`, §3b-cond conjecture classes, or carry truth-in-naming
suffixes (`*_FITTED_FROM_CODATA`, `*_AUDIT_ONLY`). Repo has strong self-audit
infra (`cal4_disguise_hunt.py` scans 972 scripts). LP/SDP `scipy.optimize`
solves and `lstsq` *structure-diagnostics* are correctly not fits.

**3 REVIEW-tier fixes (label/kind only — none wired to a prediction):**

| id | item | file | fix |
|----|------|------|-----|
| R1 | `prop:term6-binding-density` is `kind: proposition` but embeds a 2-param AME fit (α≈339.4, β≈1.14 MeV; R²=0.84). Producer `term6_scaling_heavy.py` is in `_deprecated/`; production binding uses the open `B=m_e·Σ y_λ χ^λ Δ_λ`, does NOT consume α/β. Lean side already correct (§3b-cond `class`). | `mass-theory/term6-binding-density.{md,ts,lean}` | recategorize proposition→conjecture (or §3b-cond banner) + move α,β to `authorNotes` |
| R2 | `qbeta_physics.py` hardcodes `c_3=-2`, `c_4=b²+½` under comment "STRUCTURAL PREDICTIONS, not empirical fits" — contradicts settled near-match tiering. Only caller is a `_deprecated/` probe (dormant). | `folio-assistant/computations/qbeta/qbeta_physics.py:95-114` | comment → proved(`c_2`)/near-match(`c_3,c_4`) tiering, or move to `probes/` |
| R3 | a derivation `.md` calls `c_3=-2` "exactly … canonical" — overstates settled status (dashboard: Q_β misses 100× by 164×). | `stochastic-mechanics/q-beta-gamma-gamma-canonical-derivation.md:117-124` | soften to proved/near-match tiering |

These are documentation/kind corrections; no witness or dashboard number
changes. Scheduled in the synthesis as low-risk cleanups (R1 has content-kind
propagation implications — handle with care).

## 3. Axis C — Canonical-chain wiring map + orphans + gaps

**Chain is well-mapped** (steps 1-11 have canonical scripts; tree reorganized
into `markov/`, `hecke/`, `substrate/` — many cheat-sheet flat paths are stale).
The problem is **the accuracy story is orphaned from the dashboards**.

**ORPHANS (canonical content computed but consumed by no dashboard):**
1. **`binding_depth_stratified_rust.py`** — the declared canonical binding
   default (step 9b, appendix `alg:per-isotope-binding`). Witness has no
   `consumers`; **no dashboard reads it**. Entire 9b output invisible to L1/L2.
2. **`canonical-mass-table-242ppb.witness.json`** — named by the appendix; read
   by nothing.
3. **`mass_table_comprehensive.py`** (65-isotope sweep) — self-referential;
   L2 predicts m_p/m_n from standalone borromean witnesses, **not** this table,
   so full-table accuracy never reaches the headline.
4. **`derived_chi_catalogue_sweep.py`** — exact q-Laurent χ^λ(β_K) catalogue,
   demo-only. **Prime wire-in: the exact step-5 χ cache** per-knot mass/binding
   needs (no float64, fast).

**GAPS:**
1. **9a per-knot VolDensity (wiring gap — biggest safe accuracy win).**
   Production uses **uniform `vol_density_borromean(q)` for all atoms**
   (`mass_table_comprehensive.py:208`); per-knot `vol_density_per_block` infra
   **exists** but the 65-isotope sweep never migrated (12 scripts uniform / 7
   per-knot). Error tracks the approximation: +2.89% (m_p) → +3.73% (¹²C). Not
   a fit, not new code — a migration. See
   `docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md` (read before
   migrating — confirm why it was deferred).
2. **9b Δ_λ closure — genuinely open gate** (the binding blocker;
   `canonical-with-empirical-assignment`). NO FITTING ⇒ stays categorical-only
   (GAP-A-3/4 / Option-E); do **not** wire the empirical α_k assignment as if
   derived.
3. **11 Q_β c_k near-match tier** — `qbeta-ck-cache` consumed at
   `per_observable_100x_status.py:325` (labeled DERIVED-tier, not credited).

**Dashboards** are read-only aggregators over a narrow witness set. L2 = 3/7
pass (m_p, m_e, m_K/m_π); misses m_μ 963×, Q_β 164×, Δ_pn 163×, m_n 185×.

**Generalized infra (`qou-mass`):** a vendored-shard **reader**, not a live
`predict(Z,N)`. Lookup generalizes (120 Z-shards); **computation does not** —
`compute_tr_M`/`canonical_braid` cover only 8 nuclides (p..⁶Li), `q≠q₀` raises,
no Rust backend wired, dashboards don't call `qou_mass.predict`. For true live
`predict(Z,N)`: PyO3-bind/vendor `markov_peel` + `atom_braid_word_3A` +
`hecke_core` (or route through the **merged scalable transfer-χ** for any A),
wire the Rust backend, implement `q≠q₀`, wire `derived_chi_catalogue` as the
χ cache. Appendix `alg:` blocks point `computation.script` at `api.py` but the
named witnesses are produced in-repo — contract is aspirational.

### 3a. Generalized-infra (`qou-mass`) state

**Finding (facade read, `qou-mass/src/qou_mass/api.py`):** the public
`predict(atom, observable)` is live but **reads vendored pre-computed shards**
(`canonical-isotope-witness-Z<NN>.witness.json`), described in-code as
**"current: f64 precision"** — a float64 leak at the facade layer. The live /
exact paths are stubbed:

| API | current state | gap |
|-----|---------------|-----|
| `predict(atom, q=…)` | `NotImplementedError` for `q != q_0` | no custom-q |
| `predict(..., method="rust_canonical_chi")` | declared in `Method` literal, not implemented | **the hook for the merged scalable χ** |
| `compute_tr_M(Z,N)` | reads vendored `canonical-mass-table-extended.witness.json`; raises outside vendored range | no live recompute |
| `canonical_braid(Z,N)` | explicit word only p..⁶Li; else empty generators | no live word for arbitrary A |

**Conclusion → top Phase-2 item.** The merged scalable transfer-matrix χ +
`tr_m_atom_via_transfer` (#2097, `270801d6`) produce **50-dps mpmath** `χ^λ`
and canonical `tr_M(atom/free)` for **any A** with no float64. Wiring that as
the live `compute_tr_M` / `rust_canonical_chi` method (and a live
`canonical_braid` via `atom_braid_word_3A`) makes `predict(Z,N)` answer for an
**arbitrary nuclide from the outset at exact precision** — simultaneously
closing the generalized-infra goal AND the facade-layer float64 leak. This is
the spine of the whole tranche.

## 4. Axis D — Performance hotspots + FFI roundtrips

FFI roundtrip catalogue (2026-05-29) re-confirmed RESOLVED on the mass/binding
path. The new wins:

| P | item | cost now → after | NO-float64 |
|---|------|------------------|-----------|
| **P1** | **wire transfer-χ → canonical tr_M (`canonical_tr_m_via_branching.py:421`, currently O(L·d_λ²) MPFR = 3.6 yr @⁶Li) + binding (`binding_depth_stratified_lr/_rust` ingests f64 χ from `compute_atom_chi_rust.py`)** | **years → seconds; any-A** | ✅ removes f64 χ |
| P2 | Rust port of transfer kernel (`chi_all_lambda` α/β + edge sweep → `hecke-engine` + PyO3, rayon) | ⁹Be 10s→sub-s; ¹⁰B 138s→s | ✅ MPFR |
| P3a | 1-line `py.allow_threads` on 6 PyO3 funcs (`chi_lambda_braid`/`chi_q_via_gp`/`chi_q_atomic`/`*_all_partitions_mpfr`/`tr_m_atomic_mpfr`/`mn_chi_q`) | threaded callers 0×→N× | ✅ orthogonal |
| P3b | rayon `par_iter` over partition loop in MPFR batches | ~N-core | ✅ |
| P4 | flip `binding_canonical.py:139` default `use_closed_form=True` | A=4 minutes→sub-s | ✅ |
| P5 | wire `derived_chi_catalogue` lookup into `closed_form_tau_M.py` (demo-certified ≡) | GP-reduce→dict lookup | ✅ exact q-Laurent |
| P6 | delete/guard `canonical_tr_m_via_branching.py:104` np.complex-f64 A=2 path (dead after P1) | — | ✅ removes f64 |

## 5. Synthesis — prioritized work-plan

NO-FITTING is **already clean** (Axis B) → no numeric work, 3 label fixes only.
The action is NO-FLOAT64 (Axis A) + wiring-for-accuracy (Axis C) + optimize
(Axis D), and **they converge**: P1 is simultaneously the top float64 fix
(removes f64 χ ingestion — A's C-consumers), the top wiring fix (un-orphans the
transfer + binding — C's orphan #1/#4), the top perf fix (D's P1), and the
generalized-infra engine (any-A χ for `predict(Z,N)` — §3a).

**Execution order (safety × value; sandbox runs Python + `bun validate`, not
Lean/CI):**

| # | task | axes | risk |
|---|------|------|------|
| 1 | **C6 CI guard** — widen `audits/float64_leak_audit.py` to canonical-script list + flag witness-producers calling `chi_lambda_braid`/`gram`/`nf_tr` without `mpfr` tag | A | low (audit tool, additive) |
| 2 | **R2/R3 label fixes** (c_3=-2 tiering) | B | low (doc) |
| 3 | **P4** flip `use_closed_form` default | D | low (1 caller, diag-only) |
| 4 | **P1** wire transfer-χ → canonical tr_M + binding (verify ≡ old within precision, run scripts) | A·C·D | med (math-affecting; equiv pre-certified) |
| 5 | **C2/C3** re-lift canonical tr_M producers to mpf | A | med (witness values f64→exact) |
| 6 | **C4** exact `(c,d)` in `atom_braid_word_3A` (cascades to dispatchers) | A | med |
| 7 | **C1/C5** route/deprecate numpy χ engines | A | med |
| 8 | **generalized `predict(Z,N)`** — wire transfer as live `compute_tr_M`/`canonical_braid` for any nuclide | C·§3a | med-high |
| 9 | **P3a** allow_threads (Rust rebuild) | D | low logic / needs maturin |
| 10 | **GAP#1 per-knot VolDensity** migration (headline-moving — read 2026-06-02 audit, report Δ, owner-surface) | C | high (moves numbers) |
| 11 | **R1** term6 proposition→conjecture (content-kind propagation) | B | med |

Δ_λ closure (GAP#2) stays out — NO FITTING; categorical route only.

## 6. Execution log

_(commits referenced here as the plan is worked)_
