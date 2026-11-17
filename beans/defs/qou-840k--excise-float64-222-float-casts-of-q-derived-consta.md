---
# qou-840k
title: 'EXCISE FLOAT64: 222 float()-casts of q-derived constants across 129 files; existing audit tier was too narrow and read clean'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:54:30Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-9nnz
---


Owner directive, restated: NO FLOAT64. Branch claude/anchor-followups-2026-08-08.

## Why this was not caught before

`computations/f64_into_mpmath_audit.py` reports **LAUNDERED — none**, and that
reading was used as assurance (a "117 -> 0" sweep earlier this session). Its
LAUNDERED tier is defined as `mpf(str(<f64 const>))` ONLY. It therefore misses
every other way an f64 enters a high-precision path:

  * `float(Q)` / `float(HA_VAL)` — a direct cast at a named source
  * `BlockCache(float(Q0), float(HA_VAL))` — seeding a cache with doubles
    (`mass_at_3A_proper.py:164`)
  * numpy kernels (`np.eye`, `np.trace`, `@`) run on q-derived matrices
  * `total = 0.0` accumulators in character sums

Widened detector (working copy: /tmp/f64scan.py) finds, excluding
`_deprecated/`, `node_modules/`, `.lake/`:

    129 files | 222 float()-casts of q-derived constants | 248 numpy ops beside them

## What is NOT affected — checked, not assumed

The canonical 2H chain is clean of float64:
  q0 (50 dps) -> atom_braid_word_3A (exact mpmath, fixed earlier this session)
  -> chi_all_lambda_reduced_block (mpmath transfer) -> y_lambda_at -> tr_M.

## BUT: a 30-digit cap in the production weights

`wedderburn_jones_markov.y_lambda_at` fast-path 2 returns

    {sh: sp.Float(_mp_inner.nstr(y, 30), 30) for sh, y in y_mp.items()}

i.e. the mpmath y_lambda are truncated to **30 digits** "for consumer
compatibility". Not float64, but it is the binding precision constraint on every
tr_M in the framework, and it explains a set of residuals I had been reading as
exact:

    Markov normalisation  SUM y_lam d_lam = 1     7.7e-31
    tr_free = tr_p * tr_n                          7.9e-31
    tr_atom = tr_free*(z+d)                        1.2e-31
    Markov  tr(W.sigma) = z*tr(W)                  9.1e-32

All ~1e-31 = the 30-digit cap, NOT 1e-50. Corpus claims of "~1e-50 agreement"
are about chi^lambda; once weighted by y_lambda the product is capped at 1e-30.
Harmless for a 75% binding gap and for 11.54 ppb anchor work, but it should be
documented and the "exact to 1e-50" phrasing corrected where it refers to tr_M.

Also `y_lambda_at:145` gates its witness cache on
`abs(float(q_val) - float(Q_0_FLOAT)) < 1e-12`, reading the f64 name `Q`.
Behaviourally harmless (Q vs Q_MP differ ~1e-17, far inside 1e-12, and float64
ulp at q~1.11 is 2.46e-16, far below the tolerance) but it is a directive
violation and should read `Q_MP`.

## Known f64 layer with production consumers

`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal` is float64 by
construction (`total = 0.0`, `float(y) * float(chi)`, numpy Hoefsmit) — its own
docstring says so and quotes 1e-13..1e-10 agreement. Consumers:
`delta_lambda_empirical_tabulation` (writes witnesses),
`delta_lambda_q_sweep_2row_dominance`, `delta_lambda_2row_stratum_analysis`,
`probes/rho_binding_constancy_probe`, `alpha/alpha_5_lp_dual_crystal`,
`term5_v2_chirality`. An mpmath seminormal builder ALREADY EXISTS —
`tr_m_wenzl_bridge_mpfr._build_seminormal_matrices_mpf` (used by
`deltalambda/he4_binding_k_stage2_probe.py:329`) — so this is a rewire, not new
mathematics.

## Plan

- [x] land the widened detector in-repo with self-tests, as new tiers on
      `f64_into_mpmath_audit.py` (F64_CAST, NUMPY_ON_Q) rather than a new script
      — done 2026-08-09; 23/23 self-tests, exit 0. See "Round 1" below.
- [x] tier the 222 by blast radius: canonical chain > witness-writing producers
      > probes > display-only — done; recount is 232 casts = 214 defects +
      18 display-only. See "Round 1" below, and its CORRECTIONS section.
- [ ] rewire `global_wedderburn_sum_q_hecke_seminormal` onto
      `_build_seminormal_matrices_mpf`
- [x] `y_lambda_at`: read `Q_MP`, and reconsider the 30-digit `sp.Float` cap
      — DONE 2026-08-24 (PR #5641). See "Round 2" below.
- [ ] `mass_at_3A_proper.py:164` BlockCache f64 seeding
- [ ] correct "1e-50" claims that are actually about tr_M

SEQUENCING CONSTRAINT: wave 4 (163 producers) is running in this checkout. Do
NOT run any producer and do NOT edit modules producers import until it finishes
-- a mid-wave edit makes earlier and later producers disagree.


---

## Round 1 (2026-08-09, branch `claude/anchor-followups-2026-08-08`) — tooling + inventory only

Wave 4 (163 witness producers) was running in this checkout, so this round is
**analysis + tooling only**: no producer run, no `*.witness.json` written, and
no module a producer imports edited. Plan items 1 and 2 are done; items 3-6
carry precise edit notes below so they can be applied in one pass post-wave.

### Item 1 — widened detector landed on the existing script (DONE)

`computations/f64_into_mpmath_audit.py` now carries five tiers. No competing
script was created; `float64_entry_tracer.py` remains the complementary
*runtime* localizer (this one is static).

| tier | meaning | fails a run? |
|---|---|---|
| `LAUNDERED` | `mpf(str(<f64>))` | **yes** |
| `F64_CAST` | `float(<f64>)` in a **value position** | **yes** |
| `NUMPY_ON_Q` | numpy `eye/trace/array/zeros/dot/matmul` in a module holding an f64 q-name *and* using mpmath | no — circumstantial |
| `F64_DISPLAY` | `float(<f64>)` reaching only an f-string / `print` / `%` / `.format()` | no — **not a precision defect** |
| `F64_IMPORT` | imports an f64 constant + uses mpmath, no cast, no kernel | no — circumstantial |

Also widened, both of which turned out to matter (see corrections below):

* module pool now includes **`qou_substrate.constants`** — the canonical module
  behind the `q_parameter` shim. 11 modules import `Q` straight from it and
  were invisible to every previous sweep.
* casts read through a module alias (`float(gram.z)`) are caught, not just
  bare imported names.

`python3 computations/f64_into_mpmath_audit.py --self-test` → **23/23 passed,
exit 0**, including "the audit does not flag itself" (its prose quotes every
idiom it detects).

### CORRECTIONS to this bean's own claims — read before acting on it

1. **"LAUNDERED — none" was FALSE, not merely narrow.** With the
   `qou_substrate.constants` pool the audit finds **6 live LAUNDERED sites**,
   all `mpf(str(qou_substrate.constants.Q))`, all in witness-writing producers:
   `alpha_em_b2_hecke_s5_symmetry_probe.py:57`,
   `alpha_em_b2_period_intertwiner_probe.py:64`,
   `alpha_em_b2_scalar_c_probe.py:75`,
   `alpha_em_b2_tau_w_freedom_probe.py:61`,
   `alpha_em_b2_tits_deformation_probe.py:70`, `e0_lambda_tryall.py:57`.
   The earlier "117 → 0" sweep never covered these — they bypass the shim, so
   the module matcher never saw them. The clean reading was an artifact of the
   matcher, not of the tree.

2. **`y_lambda_at:145` is the `qou-mass` copy, not the production one.** The
   `computations/wedderburn_jones_markov.py` copy no longer reads `Q_0_FLOAT`;
   it was already fixed (anchor-convention change, 2026-08-07) and the gate is
   now `abs(float(q_val) - _Y_LAMBDA_AT_Q0_WITNESS_Q0) < 1e-12` at **L172-173**,
   comparing against the witness's *own recorded* q₀. The `float(Q_0_FLOAT)`
   form survives only at
   `qou-mass/src/qou_mass/_internal/wedderburn_jones_markov.py:144-145`. The two
   copies differ by 47 diff lines — the fix is to **sync the packaged copy**,
   not to patch its line 145 in isolation.

3. **`mass_at_3A_proper.py:164` is a no-op cast into a cache that is f64 by
   construction.** `Q0` / `HA_VAL` are *already* Python floats (`from
   q_parameter import Q as Q0, Q_INV as QI, HA as HA_VAL`, L63), so
   `float(Q0)` destroys nothing at that line. And `BlockCache`
   (`tools/pyhecke/python/pyhecke/syt_prefix_cache.py:31-62`) cannot hold mpf:
   `b = math.sqrt(abs(b_sq))` (L58) returns a Python float whatever it is fed,
   and the `abs(denom) > 1e-15` guards (L54, L56) are f64 thresholds. Passing
   mpf in changes nothing. **It is also not on the canonical chain** —
   `_ensure_block_cache` is reached only from `_cached_seminormal` (L232),
   which serves the legacy Hoefsmit path (`chi_lambda_of_word` L386-416, itself
   `np.eye` / `float(np.trace(...))`; `markov_trace_3A` L419, marked
   DEPRECATED). `tr_m_atom_zn` imports **only** `atom_braid_word_3A` from this
   module (`tr_m_atom_via_transfer.py:51`), the exact-mpmath path.

4. **Recount: 222 → 232 casts, of which 214 are defects.** The 18-cast
   difference between "casts" and "defects" is display-only formatting (see
   (d) below), and the +10 over the prototype is the widened pool
   (`qou_substrate` 5, `pyhecke.gram` module-attribute reads included in the
   17 pyhecke-origin casts). File count is 121 with ≥1 cast (the prototype's
   129 counted numpy-only modules in the same row set).

5. **The canonical chain claim HOLDS at the entry point** — verified, not
   assumed: `tr_m_atom_via_transfer.py:63` is `from q_parameter import Q_MP as
   Q0`, and the audit reports `tr_m_atom_via_transfer.py`,
   `reduced_block_kernel.py` and `computations/wedderburn_jones_markov.py` all
   tier `None`. The 30-digit cap claim also holds and is now traced end to end:
   `y_lambda_at` fast path 2 returns `sp.Float(nstr(y, 30), 30)` (L191) and
   `tr_m_atom_via_transfer.py:115` re-lifts it with `mp.mpf(str(v))`.
   **Sharpen one phrase:** the cap binds *whenever fast path 2 is taken*, not
   unconditionally — fast path 1 returns 50-digit values (L104). After the
   2026-08-07 anchor change a proton-anchored caller always misses the
   muon-pinned witness gate (11.54 ppb ≫ 1e-12) and falls to fast path 2, so
   for the default anchor it is indeed always 30 digits.

### Item 2 — tiered inventory by blast radius (DONE)

Bucket (a) is the **downstream import cone** of the four named entry points
(54 in-repo modules); (b) is anything containing `WitnessBuilder(` or
`json.dump`; (c) is the remainder. 244 modules are flagged at some tier.

| bucket | files flagged | files with a defect | LAUNDERED | F64_CAST | display-only | numpy ops |
|---|---:|---:|---:|---:|---:|---:|
| (a) canonical chain | 12 | 6 | 0 | 12 | 2 | 15 |
| (b) witness producers | 187 | 93 | 6 | 155 | 13 | 37 |
| (c) probes / analysis | 45 | 27 | 0 | 47 | 3 | 5 |
| **total** | **244** | **126** | **6** | **214** | **18** | **57** |

(numpy column counts modules whose *worst* tier is NUMPY_ON_Q; 254 such ops
corpus-wide, the rest sitting inside files already counted as a defect.)

**(a) canonical chain — all 12 defect sites, 6 files:**

```
F64_CAST  computations/hecke/hecke_character_symbolic.py:462        <- q_parameter.Q
F64_CAST  computations/markov/markov_trace_canonical.py:369         <- q_parameter.Q
F64_CAST  computations/mass_at_3A_proper.py:164                     <- q_parameter.Q, q_parameter.HA
F64_CAST  computations/mass_tower_operator_valued.py:174            <- q_parameter.Q
F64_CAST  computations/sublemma_2_1_A_operator_extract.py:52, 288   <- q_parameter.Q
F64_CAST  computations/sublemma_2_1_deuteron_branching.py:182,183,189,190,286
```

plus in-cone `NUMPY_ON_Q`: `hecke/hecke_characters.py` (7 ops),
`substrate/char_fast.py` (2), `pyhecke/atom.py` (2), `pyhecke/gram.py` (4).

*Scope caveat:* "reachable from" is read as **downstream** (what the entry
points import). Upstream *callers* are in (b)/(c) by construction — 41 direct
callers of the four entry points carry 64 defect sites, led by
`sublemma_2_1_deuteron_branching.py` (5), `probe_4f_h3_sigma_avg_asymmetry.py`
(4), `probe_4_li6_rectangular_python.py` (4), `canonical_tr_m_via_branching.py`
(4). `canonical_tr_m_via_branching` is a canonical consumer despite landing in
bucket (c); do not read (c) as "all disposable".

**(b) witness producers — 93 defect files, 161 sites.** Worst offenders:
`h2o_angle_gb_truncation_inverse.py` (25), `qbeta/qbeta_habiro_phase5q_dn_refactorize.py` (5),
`qbeta/qbeta_decay_sdp_solver.py` (5), `probe_4f_h3_sigma_avg_asymmetry.py` (4),
`probe_4_li6_rectangular_python.py` (4). All 6 LAUNDERED sites are here.
This bucket is the one that writes doubles into committed artifacts.

**(c) probes / analysis — 27 defect files, 47 sites.** Led by
`tools/pyhecke/tests/test_trace_formal.py` (4),
`canonical_tr_m_via_branching.py` (4), `atom_level_wedderburn_tower.py` (4).

**(d) display/formatting only — 18 sites in 18 files. NOT precision defects.**
A `float()` whose value reaches only an f-string, `print`, `%`-format or
`.format()` renders a number for a human; it destroys nothing the pipeline goes
on to use, and rewriting it to mpmath makes the output uglier and the numbers
no better. **Do not "fix" these, and do not count them in the defect total.**

```
computations/canonical_isospin_pyhecke.py:46
computations/d_density_derivation.py:134
computations/habiro/habiro_coefficients_atomic.py:313
computations/habiro/habiro_coefficients_interpolate.py:327
computations/probes/qbeta_braid_nf_sdp_offset_probe.py:139
computations/qbeta/qbeta_c3_barodd_knot_operator_gram_probe.py:60
computations/qbeta/qbeta_decay_sdp_solver.py:84
computations/sublemma_2_1_A_operator_extract.py:121        (in-cone)
computations/sublemma_2_1_A_operator_extract_h12_nn.py:196
computations/sublemma_2_1_A_operator_extract_h12_nn_streamed.py:330
computations/sublemma_2_1_A_operator_extract_h9.py:305
computations/sublemma_2_1_alpha_shift_extract.py:174
computations/sublemma_2_1_deuteron_branching.py:177        (in-cone)
computations/sublemma_2_1_h12_he4_branching.py:173
computations/sublemma_2_1_h9_branching_basis.py:425
computations/symmetrized_constituent_general.py:153
computations/wenzl_a3_combiner_end_to_end.py:80
computations/wenzl_a3_cross_check.py:123
```

One nuance the tier deliberately does **not** hide: `float(Q)` is idempotent —
`Q` is already a double — so a value-position cast destroys no precision *at
that line*. What `F64_CAST` gives is the **edit site**: the exact line where a
double enters a computation and therefore the line to rewrite onto `Q_MP`.

### Items 3-6 — NOT done this round; precise edit notes

**Item 3 — rewire `global_wedderburn_sum_q_hecke_seminormal` onto the mpf
seminormal builder.** All in `computations/wedderburn_jones_markov.py`:

* L339 `q_val: float` and L345 `-> tuple[float, list[dict]]` — widen to mpf.
* L353 docstring "χ^λ_q via Hoefsmit seminormal matrices at q_val (numerical,
  float64)" and L357-361 "agrees … to 1e-13 (A=1) — 1e-10 (A=2)" — both must be
  restated after the rewire, or they document a path that no longer exists.
* L365 `import numpy as np` is **dead already** (no `np.` use anywhere in the
  function body, L336-417) — delete it with the rewire.
* L367 `from hecke_characters import build_seminormal_matrices` →
  `from tr_m_wenzl_bridge_mpfr import _build_seminormal_matrices_mpf`
  (defined at `tr_m_wenzl_bridge_mpfr.py:144`). **Return shape differs**: the
  mpf builder returns `(sigmas, dim)`, the f64 one `(sigmas, dim, syts)` —
  L403 unpacks three.
* L370 `chi_lambda_of_word` (from `mass_at_3A_proper`, L386-416) is numpy-f64
  and must be swapped too or the rewire buys nothing. The drop-in is
  `_chi_lambda_of_word_mpf(sigmas, dim, word, q=q)` at
  `tr_m_wenzl_bridge_mpfr.py:262`; the reference call-site pairing both is
  `chi_at_q0_via_hoefsmit_mpfr.py:361-364`.
* L401 `total = 0.0` → `mp.mpf(0)`; L408 `contrib = float(y) * float(chi)` →
  keep mpf.
* L413-415 `"y_at_q0": float(y)`, `"chi_q_at_q0": float(chi)`,
  `"contribution": float(contrib)` — these land in witness JSON. Serialize as
  strings, following `chi_at_q0_via_hoefsmit_mpfr.py:383-386`
  (`"y_lambda": str(y_lam)`).
* Twin: apply the same to
  `qou-mass/src/qou_mass/_internal/wedderburn_jones_markov.py` (function at
  L309; L326 docstring, L374 `total = 0.0`, L381 `contrib`).
* Then re-run the consumers named above in this bean (all wave-gated).

**Item 4 — `y_lambda_at`.** Two separable halves:

* *`Q_MP`*: nothing to do in `computations/` (already fixed — see correction 2).
  The live edit is `qou-mass/src/qou_mass/_internal/wedderburn_jones_markov.py:144-145`,
  and the right fix is to sync that copy to the `computations/` one rather than
  patch the line.
* *30-digit cap*: `computations/wedderburn_jones_markov.py:191`
  `sp.Float(_mp_inner.nstr(y, 30), 30)` — both `30`s. 50 is already precedented
  in the same file at L104 (`sp.Float(r["y_at_q0_50dps"], 50)`), and the only
  canonical consumer immediately re-lifts through `mp.mpf(str(v))`
  (`tr_m_atom_via_transfer.py:115`), so raising it is cheap. Twin at
  `qou-mass/.../wedderburn_jones_markov.py:164`. Expect every ~1e-31 residual
  recorded in this bean to drop by ~20 orders; that changes witness values, so
  it is strictly post-wave and needs a producer re-run + witness refresh.

**Item 5 — `mass_at_3A_proper.py:164`.** Not the one-line fix the plan implies
(correction 3). The real work is an mpf-capable block cache — a `BlockCacheMpf`
beside `syt_prefix_cache.BlockCache`, or a numeric-backend parameter — and it
should ride with item 3, since the only consumer is the same legacy Hoefsmit
path. Note the module is f64 below `atom_braid_word_3A` regardless: L71
`h = HA_VAL`, L76 `Z_MARKOV = 1.0 / (Q0 ** 0.5 + QI ** 0.5)`, L90 / L123
`q: float = Q0` defaults. Lowest priority of the four — off the canonical chain.

**Item 6 — "1e-50" claims that are really about tr_M.** Targets, in order:

* `folio/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step03-markov-trace.md:92-95`
  — "The numerical mode at $q = q_0$ meets L1 to $10^{-50}$ by the precision
  discipline of `qou-substrate`." Any tr_M routed through `y_lambda_at` fast
  path 2 is capped at ~1e-30. Content block ⇒ needs the `.md` + `.ts` sibling,
  the render-QA gate, and `qa-sweep` on the touched criteria.
* `computations/wedderburn_jones_markov.py:180-183` — "Verified to ~10⁻⁵⁰ vs
  the cached witness for n ∈ {2..12}". True of the mpmath values *before* L191
  truncates them; the dict the function returns is 30-digit. Twin at
  `qou-mass/.../wedderburn_jones_markov.py:153-156`.
* `docs/audits/2026-06-28-audit-move-mass-endomorphism.md:74` — `10^{-50}` for
  `markov_trace_recursive`. That route does **not** pass through `y_lambda_at`,
  so verify before editing; do not blanket-rewrite every 1e-50 in the corpus.
* Leave the χ^λ claims alone (`docs/audits/2026-06-29-…:25`,
  `2026-07-13-…:74`) — they are about characters, which genuinely reach 50 dps;
  the cap is introduced by the y_λ weighting, downstream of them.


---

## Round 2 (2026-08-24, PR #5641, branch `claude/stalled-agent-prs-ir8t3p`) — item 4 closed

### Item 4 — DONE, and the cap was worse than this bean estimated

**The `Q_MP` half needed nothing.** Correction 2 in Round 1 already established
the `computations/` copy was fixed on 2026-08-07 and only the packaged twin
carried `float(Q_0_FLOAT)`. Re-verified: `sync-qou-mass-vendor.py --apply`
regenerates the twin from the fixed source, so the sync IS the fix. Do not
hand-patch `_internal/`.

**The 30-digit cap half is closed, at a NEW line.** Round 1 pointed at
`wedderburn_jones_markov.py:191`. That line is now inside
`_y_lambda_at_convention_C_HISTORICAL`, which is DEAD — the convention-C
excision of 2026-08-09 moved the live code. **The cap survived the excision
unchanged on the live convention-D path**, at what is now L160:

    return {sh: sp.Float(_mp.nstr(v, 30), 30) for sh, v in _y.items()}

i.e. anyone following Round 1's line reference would have edited dead code and
believed the item closed. Raised to 50/50 there.

### The measurement Round 1 predicted, now actually run

Round 1 said "expect every ~1e-31 residual to drop by ~20 orders". Measured on
the Markov normalisation `Σ y_λ f^λ = 1` at the proton q₀ — it holds:

| n | raw from `y_lambda_su_n` | capped at 30 | after |
|---|---|---|---|
| 3 | 0.0 | 0.0 | 1.069e-50 |
| 4 | 1.336e-51 | **1.0e-30** | 2.673e-51 |
| 5 | 0.0 | **5.0e-31** | 1.069e-50 |
| 6 | — | **1.0e-31** | 1.336e-51 |

The truncation artefact is visible directly in the returned weights — every
one was zero-padded past digit 30:

    (2,1) before  0.2472978867480345984062206483799999999999999999999999
    (2,1) after   0.2472978867480345984062206483797638621698244011250899

Two cautions for anyone re-measuring: n=3's before-residual of exactly `0.0`
is an ARTEFACT (both weights truncated to values that happen to sum exactly),
not evidence the cap was harmless there; and `1e-50` after is round-off at 50
digits, not a regression from `0.0`.

### Item 6's PREMISE HAS INVERTED — re-check before editing

Item 6 was "correct the corpus's 1e-50 claims that are really about tr_M,
because the cap makes them false". As of this round **the cap is gone and
those claims are true as written.** The listed targets (`mba-step03-markov-
trace.md:92-95`, `wedderburn_jones_markov.py` docstring, the audit doc) should
be RE-CHECKED, not edited to say 1e-30. Editing them now would introduce the
error item 6 was written to remove.

### Not done — witness refresh

The change moves returned values for ~155 consumers, so committed witnesses
downstream are stale in their last ~20 digits. Tracked separately as
**`qou-jjge`**, deliberately NOT run inside #5641: a two-token precision fix
must not carry a ~155-producer regeneration as a side effect, and in this
corpus a producer IS its side effect (it writes sibling witnesses).

### Item 2's inventory, re-cut by fixability

Of the 116 F64_CAST files, **49 use no f64 engine** (numpy / BlockCache /
scipy / pyhecke.gram / solvers) and are the genuinely fixable set. The other
67 are f64 by construction — `atom_level_wedderburn_tower.py` carries a
comment saying exactly that and explicitly declining to claim high precision.
**The drain target is 49, not 116.** Round 1's "one nuance the tier
deliberately does not hide" paragraph now also prints when the audit runs, so
the next agent does not re-derive it from the detector (I did, having read the
detector and the print block but not the header).

### Items 3, 5, 6 remain open

Item 3 (rewire `global_wedderburn_sum_q_hecke_seminormal` onto
`_build_seminormal_matrices_mpf`) is the next-largest precision win and its
Round 1 edit notes are still accurate — but VERIFY THE LINE NUMBERS FIRST.
Round 1's item-4 references had drifted by a whole function in two weeks.


## 2026-09-06 — re-measured: the widened detector LANDED, and it is the largest live tier

Found by `scripts/bean-staleness-triage.py` (21st of 291 artifact beans), and
reached from the other end the same day: `qou-b7cf`'s LAUNDERED drain ran into
exactly the boundary this bean names.

### The good half — the detector is no longer a working copy

This bean's widened scan lived in `/tmp/f64scan.py`, which would have been lost.
It **did land** in the canonical audit, as the `F64_CAST` tier —
`computations/f64_into_mpmath_audit.py:635` still carries the attribution
comment *"the tier the LAUNDERED-only reading missed (qou-840k)"* — along with
`NUMPY_ON_Q`, `F64_ENGINE_ENTRY`, `F64_DISPLAY` and `F64_IMPORT`. So the
measurement is reproducible by anyone, which was this bean's real deliverable.

### The count, and it has barely moved

| | bean (2026-08-09) | measured 2026-09-06 |
|---|---|---|
| files | 129 | **105** |
| `float()`-casts in a value position | 222 | **188** |

`F64_CAST` is **the largest defect tier in the audit** — LAUNDERED is now 0
(`qou-b7cf`, four sites fixed today) while this one stands at 188. The
circumstantial tiers underneath it are larger still: `NUMPY_ON_Q` 283 ops
corpus-wide, `F64_ENGINE_ENTRY` 70 sites, `F64_IMPORT` 138 files — all marked
*review, do not bulk-edit*.

### 🛑 A caution bought today, and it is this bean's own failure mode one level up

`--tier` **filters the rows before the report is built** (`main()`:844-846), so
`--tier LAUNDERED` prints `F64_CAST — none.` on a tree carrying 188 of them. I
read that as a corpus fact and wrote "F64_CAST 195 → none" into a commit
message and a bean before catching it; the correction is on `qou-b7cf`.

That is the same shape this bean was opened about — *"`LAUNDERED — none` … and
that reading was used as assurance"* — except that there the detector was too
narrow, and here the detector is right and the **invocation** narrowed it.
Either way a `— none.` line was read as an all-clear. **Run the audit
unfiltered when quoting any tier's count**; use `--tier` only to list sites
within a tier you have already sized.

### Not attempted here

Draining 188 sites is a tranche, not an idle pass, and the tiers below it are
explicitly not bulk-editable. `qou-b7cf`'s scope note applies verbatim: fixing
the `mpf(str(f64))` entry point does not de-float a probe body, and the two
probes fixed today still carry `HF, DPN = float(_H), float(D_PN)` — they are 2
of the 105.


## 2026-09-06 — the 188 are now ENUMERABLE; the tier listing was capped at 40

Found while trying to scope this bean's drain: I asked for the 188 `F64_CAST`
sites and got 40, under a message reading *"… and more; re-run with `--tier`
for the full list"* — while already running `--tier`.

`_print_sites` carried an unconditional `cap = 40`, and `--tier` is passed to
`_iter_rows(a.tier)`, which filters the **rows** and never the cap. So the
escape hatch the message advertised did nothing. Two sibling listings (lines
910, 998 — `numpy`, `imports`) had the same `[:40]` shape; those at least named
the hidden count, the `F64_CAST` one did not.

Fixed all three: `_cap = 10 ** 6 if a.tier else 40`, set once from the flag.

    overview (no --tier)   40, and now names what is hidden ("… and 148 more")
    --tier F64_CAST        188 == headline
    --tier F64_IMPORT      138 == headline
    --tier NUMPY_ON_Q       21 == headline

**Display only** — `--self-test` 36/36, exit contract unchanged (1 on
LAUNDERED 0 + F64_CAST 188). Commit on PR #6930.

**Why it matters for this bean specifically:** the drain cannot be scoped from
a 40-site sample. The full list is now obtainable in one command, which is the
precondition for anyone — owner or agent — deciding how to stage 188 sites
across 105 files.

    python3 computations/f64_into_mpmath_audit.py --tier F64_CAST


## 2026-09-06 — the 188 CHARACTERISED, so the drain can be staged rather than swept

Measurement only; nothing edited. Now that `--tier F64_CAST` lists all 188 (the
cap fix above), the tranche has a shape.

### 74 % of it is ONE constant, so there is one repair pattern, not 188

    139   q_parameter.Q            <- the same origin as every LAUNDERED site
     20   q_parameter.HA
     13   pyhecke.gram.z
      6   qou_substrate.constants.Q
      4   q_parameter.Q_INV
      3   qou_substrate.constants.HA
      3   pyhecke.gram.q0
    ---
    188

`q_parameter.Q` is exactly what `qou-b7cf` repaired today with
`q_at(mp.mp.dps)` — the established, already-reviewed pattern. So 139 of 188
have a known fix, and the remaining 49 split over six origins, of which `HA`
(23) and `pyhecke.gram.z`/`q0` (16) are the only groups above single digits.

### The risk axis: does fixing a file MOVE a published number?

Of the 105 files:

    61   own a committed witness   -> the fix moves published numbers; each
                                      needs a producer re-run and a before/after
    41   own no witness            -> probe / consumer / library; the fix is
                                      local and verifiable in place
     3   qou-mass/src/…            -> 🛑 GENERATED mirror. NEVER hand-edit.
                                      Fix at the computations/ source, then
                                      scripts/sync-qou-mass-vendor.py --apply

### Concentration worth knowing before staging

`computations/h2o_angle_gb_truncation_inverse.py` alone carries **25 sites** —
**13 % of the whole tranche in one file.** Three more carry 4 each. So a
first batch of ~5 files reaches roughly a quarter of the sites.

### A suggested staging, offered for scoping — NOT started

1. **The 41 witness-free files.** Local, verifiable in place, no published
   number moves. This is the safe majority of the *files* even though not of
   the sites.
2. **`h2o_angle_gb_truncation_inverse.py`** on its own — 25 sites, one
   before/after.
3. **The 61 witness-owning files**, in producer-cost order, each with the
   before/after `qou-b7cf` used. This is the expensive part and the one that
   wants owner sign-off, because it re-publishes numbers.
4. **The 3 generated mirrors last**, via the sync script, never by hand.

**Not begun.** Under the AGENTS.md precision rules a fix here is *fix at the
producer and re-run*, and 61 producer re-runs is a tranche with real compute
cost — it is a scoping decision, not an idle pass. The list, the counts and the
staging are the deliverable of this pass.

Reproduce any of it with:

    python3 computations/f64_into_mpmath_audit.py --tier F64_CAST


## 🛑 2026-09-06 (correction to my own staging, made BEFORE acting on it)

The plan above says stage 1 is *"the 41 witness-free files — local, verifiable
in place, no published number moves."* **That is wrong, and it is wrong in the
exact way AGENTS.md's import-cone note warns about**: a file can own no witness
and still be *imported by* producers that do, so a float cast fixed there
propagates into their numbers. `binding_canonical` is the corpus's own worked
case — source-stable while `tr_M_atom` moved 48 % because a module it *calls*
changed.

Measured before touching anything. Of the 41:

    12  imported by another computations/ or tools/ module
    29  imported by nobody -> genuinely cannot move a published number

And the 12 are not marginal. Three are high-fan-in library modules:

    hecke_core_legacy.py       imported by 17
    per_irrep_pole_atom.py     imported by 14
    schur_weyl_mpmath.py       imported by 12
    canonical_tr_m_via_branching.py, term5_v2_chirality.py   3 each
    canonical_brane_tower.py, probe_4_li6_rectangular_python.py, …

A cast fixed in `hecke_core_legacy` reaches seventeen consumers, several of
which publish witnesses. Those belong **with** the witness-owning group, behind
the same sign-off, not ahead of it.

### Corrected staging

1. **29 isolated files / 46 sites** — witness-free *and* imported by nobody.
   This is the real no-risk batch. Smaller than it looked: 46 of 188 sites
   (25 %), not the 41 files I implied.
2. `h2o_angle_gb_truncation_inverse.py` — 25 sites, one before/after.
3. **61 witness-owners + the 12 imported ones = 73 files** — each moves
   published numbers, directly or through its consumers. Producer re-run and
   before/after each. This is the part that wants owner sign-off.
4. The 3 generated `qou-mass` mirrors, via `sync-qou-mass-vendor.py`, never by
   hand.

**Still not begun.** Recording the correction is the point: the difference
between the two versions is 12 files that would have been edited as "no risk"
while feeding up to seventeen consumers each.


## 🛑 2026-09-07 — THE STAGE PLAN IS WITHDRAWN. F64_CAST is 105 ports, not one pattern.

PR #6977, `docs/audits/2026-09-07-f64cast-is-not-a-drain.md`. Opened a branch to
drain stage 1 (29 isolated files / 46 sites) and **drained nothing**, because
checking the fix before applying it showed the fix does not exist.

### The claim that was wrong

This bean said 74 % of the tranche shares one origin (`q_parameter.Q`) and
therefore **one repair pattern** — `_Q = q_at(mp.mp.dps)`, the fix `qou-b7cf`
established. The isolation analysis holds. The repair claim does not:
**LAUNDERED and F64_CAST are inverse operations.**

    LAUNDERED   mpf(str(Q))     an mpf CONSTRUCTED from a float64
    F64_CAST    float(Q)        an mpf DESTROYED into a float64

LAUNDERED's float64 is an accident of construction — the code around it is
already mpmath, so `q_at(dps)` fixes it in place and nothing else moves.
F64_CAST's cast is **deliberate and load-bearing**: it sits at the boundary of a
float64 kernel that cannot take an `mpf`. Of the 46 isolated sites, **38 rebind
the name to float** and **11 pass `float(…)` into a call**; **17 of the 29 files**
use numpy or a float-typed signature, and `build_seminormal_fast` is declared
`(shape, q: float)`.

Substituting `q_at(mp.mp.dps)` there raises the precision of nothing. Each site
is a **port of the kernel behind it** — the job `qou-b7cf` scoped out. That is
105 ports.

It also explains the rates, which looked inconsistent: LAUNDERED **34 → 0 in a
day**, F64_CAST **222 → 188 in a month**. Same corpus, same discipline, different
defect.

### Second finding: 12 of the 29 are fit-search scripts

`derive_b2.py` reads the AME deuteron binding as `target`, casts everything to
float, and loops products of `quaternion_quantum = 2.277455`, `kashiwara = 1/32`,
`E0`, `me`, `g8` looking for one that lands on it. Twelve of 29 match that shape.
Under 🟥 NO FITTING they want a **disposition**, not better arithmetic — raising
the precision of a search for a coincidence does not make it less of one.

### Corrected disposition

1. Stage plan **withdrawn**. It staged by *risk*; the axis that decides the work
   is **what sits behind the cast**.
2. Re-stage by **kernel** if at all — mpmath-capable receivers are small,
   numpy/float-typed receivers are ports.
3. Triage the 12 fit-search files on the **anti-fit** axis, separately.
4. **Do not quote "74 % share one repair pattern."** They share one origin
   constant; the repair is a property of the receiver.

### Why nothing was edited

A 29-file PR applying `q_at(mp.mp.dps)` would have compiled, **passed the
F64_CAST gate by removing the matched shape, and changed no result**. A green
gate over an unchanged defect is precisely what this gate family exists to
prevent.


---

## 🛑 The 30-digit cap is DEAD CODE, and this bean's instruction would now INTRODUCE errors (measured 2026-09-26, from `qou-ejfy`; status NOT changed)

This bean's §"BUT: a 30-digit cap in the production weights" says the
`sp.Float(_mp_inner.nstr(y, 30), 30)` truncation "is the binding precision
constraint on every tr_M in the framework", lists four residuals at ~1e-31, and
concludes that **"corpus claims of '~1e-50 agreement' ... should be documented
and the 'exact to 1e-50' phrasing corrected where it refers to tr_M."**

**Acting on that today would replace correct 1e-50 statements with wrong 1e-30
ones.** The cap is unreachable.

### Structural: zero call sites

Line 314 (the cap) is inside **`_y_lambda_at_convention_C_HISTORICAL()`**, lines
214-339 (AST-resolved, not grepped). That name occurs at exactly **two** lines in
the file — **150**, a mention inside `y_lambda_at`'s own docstring, and **214**,
its `def`. **It is never called.** The live `y_lambda_at` (from line 117) is six
statements and routes to `y_lambda_su_n` / `y_lambda_su_n_symbolic` with no
truncation anywhere.

### Executed: 60 digits, and the normalisation closes at 1e-50

`y_lambda_at(3, sp.Rational(Q_50_DIGIT_STR))` at the proton pin:

    y_(3,)       ~60 sig digits   0.505404226503930803187558703240472275660351197749810143
    y_(2, 1)     ~60 sig digits   0.247297886748034598406220648379763862169824401125089916
    y_(1, 1, 1)                   0            (row cap — this IS convention D)

The cap would force **exactly 30** and no more. Against this bean's own first
residual:

    Sum y_lam * f^lam = 1      recorded here 7.7e-31   ->   MEASURED 1.06911e-50

### Why it went stale, and it was one day

This bean is dated **2026-08-08**. The convention-D cascade of **2026-08-09**
made the three C fast paths dead — `y_lambda_at`'s docstring states it outright
("THE THREE C FAST PATHS BELOW ARE NOW DEAD ... the D result returns before any
of them is reached"), and the AST and the execution both confirm it. The
measurement here was correct the day it was taken and was superseded the next.

### Scope of this correction — deliberately narrow

I re-measured **one** of the four residuals. I am **not** asserting specific new
values for the other three (`tr_free = tr_p*tr_n`, `tr_atom = tr_free*(z+d)`,
`tr(W.sigma) = z*tr(W)`); they need their own runs. What IS established is their
**cause**: this bean attributes all four to the 30-digit cap on `y_lambda`, and
`y_lambda` now carries 60 digits from a code path that never reaches the cap. So
the stated explanation no longer holds for any of them, whatever they now measure.

### Independent corroboration from the other direction

`qou-ejfy` measured the canonical `tr_M` witness against an exact symbolic
recompute over ℚ(q) at the exact-rational 50-digit pin: agreement to **1.4e-50**
(proton) / **5.8e-50** (neutron), stable from 60 to 90 dps. Under a live 30-digit
cap those two independent routes could not have agreed past ~1e-30. The two
findings confirm each other and were reached from opposite ends.

### What is NOT retracted

The bean's main subject — **222 `float()`-casts of q-derived constants across 129
files** — is untouched by this. Only §"a 30-digit cap in the production weights"
is stale.


### Where the withdrawn claim propagated — 2 carriers, not 8

A figure-grep for the four residuals returns eight files. **Four are substring
artifacts of scientific notation** and are unrelated — worth naming, because the
over-match is the same detector-blindness class running the other way:

| file | matched | actually |
|---|---|---|
| `all-nuclides-sdp-admissibility-mp.witness.json` | `7.9e-31` | inside `y0_star_str = 3.53127756391210122990490434350523013712148691057*49e-31*` — an LP dual |
| `probes/awzero-asymptotics.witness.json` | `7.9e-31` | `tail_bound_at_b = 2.51709e-31*1*` — a different exponent entirely |
| `qbeta/gram-convention-d-singularity-structural.witness.json` | `9.1e-32` | `min\|eig\| under D = 4.33951e-32` — a Gram eigenvalue |
| `.beans/qou-cds2` | `9.1e-32` | the same Gram row |

**The genuine carriers are two, and they are NOT equally bad:**

1. **`docs/audits/2026-08-09-canonical-chain-walk-gaps-marked.md` (lines 161-165)
   — this is the one that misleads.** It states the cap as fact in a durable
   audit doc, gives it as the *cause* of all four residuals, and concludes:
   *"Corpus claims of '1e-50 agreement' are about χ^λ, not tr_M."* That last
   sentence is now measurably false — `qou-ejfy` measured the canonical tr_M
   witness against an exact symbolic recompute at **1.4e-50**. An agent citing
   this doc would "correct" a right number into a wrong one.

2. `docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
   (lines 277-280) and `.beans/qou-d5e8` cite 7.9e-31 / 1.2e-31 as
   **verification that tr_M is multiplicative**. That use is benign: the
   verification stands, only its precision was understated. No causal claim
   about the cap, no instruction to edit anything.

Also distinct, despite matching: `.beans/t7qv` records `G[3,2] = z·G[2,2]`
residual `1.2e-31` **"at 40 dps"** — self-explained by its own compute
precision, not by the y_λ cap. Same family of check, different and stated cause.

**Not edited.** Both audit docs are dated records, and this repo's standing
practice (`qou-3nva`) is to leave those as historical rather than sweep them.
The 08-09 doc is the one where that practice and the risk actually collide;
raised for the owner rather than acted on.


### Residual 2 re-measured: `tr_free = tr_p · tr_n` is EXACT, not 7.9e-31

Computed on the exact symbolic route (`markov_weights_symbolic.tr_M_canonical`,
rational functions over ℚ(q)), evaluated at the exact-rational 50-digit pin:

    tr_free   @q0  = 0.29901501718464007670216042677098383227494947439701665190
    tr_p*tr_n @q0  = 0.29901501718464007670216042677098383227494947439701665190
    RELATIVE RESIDUAL = 0

**Stated precisely:** the two sides agree to **all 60 digits evaluated**. That is
not a proof of symbolic identity — I deliberately did not run `sp.simplify` on
the H_6 difference (see below) — but at the precision measured there is no
residual at all. The recorded **7.9e-31 was entirely the cap artifact**, and the
cap is dead.

This **strengthens** the benign citation in
`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
(lines 277-280), which offers 7.9e-31 as verification that tr_M is
multiplicative over independent subsystems. The verification is better than it
claims.

### Residual 3 NOT measured, and the reason is structural

`tr_atom / tr_free` needs the **atom** word, which carries an
`averaged_weighted` letter — `σ_i − h(1/2 − δ/4)·𝟙` (`markov_peel.py:187`). That
makes tr_M(atom) a rational function over **ℚ(q, δ, h)**, not ℚ(q). Measured
cost at the same n=6: **>13 min with no result**, against **193 s** for the free
word. Killed rather than run to timeout. Residual 3 and residual 4
(`tr(W·σ) = z·tr(W)`) are therefore still open; their stated CAUSE is withdrawn
either way, per the correction above.

### Method note, because it cost the first attempt

The first probe put `sp.simplify(tr_free - tr_p*tr_n)` **before** the numeric
evaluation it was guarding. On an H_6 rational function that is the expensive
step, and it gated the cheap answer behind it. Evaluating at the pin with
`sp.cancel` only — no `simplify` — returns in 199 s total. If you extend this to
residual 3, substitute q, δ and h numerically *before* taking the trace rather
than after.


### Residual 4 re-measured: `tr_M(W·σ) = z·tr_M(W)` is EXACT too — in 1.7 s

W = the canonical proton word on 3 strands (generators {0,1}); `W·σ₃` appends
`(2, 'sigma')` and is evaluated at H_4. `M.Z_MARK` verified `= q³/(q²+1)`,
i.e. convention D.

    tr_M(W·σ₃)  @q0 = 0.38558198346622944847005289495935556822269309959149640845
    z·tr_M(W)   @q0 = 0.38558198346622944847005289495935556822269309959149640845
    RELATIVE RESIDUAL = 0

**1.7 seconds**, against the >13 min that residual 3 failed in. The difference is
structural and worth keeping: H_4 has 5 partitions and the word carries **no
extra free symbols**, whereas the atom word's `averaged_weighted` letter drags in
δ and h.

### The corrected table

| residual | recorded 2026-08-08 | measured 2026-09-26 | route |
|---|---|---|---|
| `Σ y_λ f^λ = 1` | 7.7e-31 | **1.06911e-50** | numeric accessor `y_lambda_at` |
| `tr_free = tr_p·tr_n` | 7.9e-31 | **0** (60 digits) | symbolic over ℚ(q) |
| `tr_atom = tr_free·(z+d)` | 1.2e-31 | *not measured* | needs ℚ(q,δ,h) |
| `tr(W·σ) = z·tr(W)` | 9.1e-32 | **0** (60 digits) | symbolic over ℚ(q) |

**Why residual 1 is 1e-50 and not 0, while 2 and 4 are 0.** Not an
inconsistency — they are measured on different routes. `y_lambda_at` computes
*numerically* (`y_lambda_su_n(n, mpf(str(q)), 2)`), so its residual is the
mpmath working-precision floor at the 70/60 dps default. Residuals 2 and 4 are
rational-function identities evaluated on the *symbolic* route, so they close to
every digit evaluated. Both readings are the honest one for their own route.

**All four were recorded at ~1e-31 and attributed to the 30-digit cap. Three are
now re-measured and none of them is 1e-31.** The fourth is untractable here, but
its stated cause is withdrawn on the same evidence as the others: the cap has
zero call sites.


### 🛑 Correcting myself: residual 3 is NOT ℚ(q,δ,h). It is ℚ(q), same as the others

Two entries above I recorded, as the structural reason residual 3 could not be
measured:

> the atom word carries an `averaged_weighted` letter — `σ_i − h(1/2 − δ/4)·𝟙`
> — so `tr_M(atom)` is a rational function over **ℚ(q, δ, h)**, not ℚ(q)

**Measured, and it is wrong.** Calling the live symbolic character on a
one-letter word with that ctype:

    ctype='sigma'             free symbols {q}   Float present? No   (q²−1)/q
    ctype='averaged'          free symbols {}    Float present? No   0
    ctype='averaged_weighted' free symbols {q}   Float present? No
        (q⁸ − 2q⁷ + 2q⁵ − 2q⁴ + 2q³ − 2q + 1) / (6q⁵)

One symbol, no Float. δ and h are resolved to closed forms in q before they ever
reach the expression, so the atom trace lives in **ℚ(q)** exactly like the free
one. The real cost is *size*: a single `averaged_weighted` letter contributes a
degree-8 numerator over `6q⁵`, so the rational functions balloon through a
23-letter product in a way the free word's letters do not. Slow, not
structurally harder — an important difference, because slow has a workaround and
"more symbols" does not.

### And a second suspicion of mine that did NOT hold

I expected to find a **layer straddle**. `d_for_ctype`'s own docstring warns that
a q-symbolic caller taking the default `delta=None` gets `_avg_color_delta()`
evaluated at the numeric `q_parameter.Q`, *"an ideal/experimental mix inside one
quantity, which AGENTS.md rules out regardless of its size"* — and
`hoefsmit_symbolic.chi_lambda_symbolic` takes **no** `delta` parameter and
documents its ctype domain as only `{'sigma', 'sigma_inv', 'averaged'}`, with
`averaged_weighted` absent. That reads exactly like an unguarded path.

**It is not one.** The Float check above is the test, and it comes back clean on
the very ctype in question. Recorded because the inference was reasonable, the
documentation genuinely points that way, and the measurement says otherwise —
which is the only thing that settles it.


### Residual 3 measured: `tr_atom = tr_free·(z + d)` holds to 1.34e-51

Method that worked, after the symbolic route failed twice: substitute the
exact-rational pin into `q_character_on_braid_word` **before** the matrix
product, so every χ^λ is an exact rational number rather than a ballooning
rational function. 201 s, against >13 min with no result symbolically.

    tr_free @q0 = 0.29901501718464007670216042677098383227494947439701665190
    tr_atom @q0 = 0.15196833920423160759266569775106614127124096465525819935
    ratio       = 0.50822978937673896257799579765589360389830839091656702154

    d_for_ctype("averaged_weighted", h) @q0 = -0.1044582477697262890178340662900
    z_D + d                                 =  0.50822978937673896257799579765589
    ratio − (z_D + d)                       =  1.3363824e-51     <- residual 3

Against the recorded **1.2e-31**. 1.3e-51 is the 50-digit pin's own floor, so
the identity is exact at the precision available.

**The comparison discriminates, which is worth more than the residual.** Using
the *unweighted* `averaged` d instead gives `ratio − (z+d) = 7.19e-5` — five
orders worse. So this identity picks out the **colour-weighted** interface
specifically, an independent confirmation that `bring_color_weighted`
(convention D, ruling R3) is the constant the canonical word actually uses.

### The complete table — all four re-measured, none of them 1e-31

| residual | recorded 2026-08-08 | measured 2026-09-26 | route |
|---|---|---|---|
| `Σ y_λ f^λ = 1` | 7.7e-31 | **1.06911e-50** | numeric accessor |
| `tr_free = tr_p·tr_n` | 7.9e-31 | **0** (60 digits) | symbolic ℚ(q) |
| `tr_atom = tr_free·(z+d)` | 1.2e-31 | **1.3363824e-51** | exact-rational at the pin |
| `tr(W·σ) = z·tr(W)` | 9.1e-32 | **0** (60 digits) | symbolic ℚ(q) |

The 30-digit cap explained all four and has zero call sites. Every replacement
is 20 orders tighter or exact.

### Unplanned, and the most valuable thing this run produced

`tr_M(atom)` for the deuteron was recomputed here **entirely from scratch** — a
different route from anything in `qou-ejfy`, going through
`q_character_on_braid_word` at an exact rational rather than reading any
witness. Against the committed `markov-trace-assembly-deuteron.derivation.json`
`target_value`:

    stored     0.1519683392042316075926656977510661412712409646552611513103
    recomputed 0.15196833920423160759266569775106614127124096465525819935
    common prefix: 51 chars = ~49 significant digits

So the stored deuteron value is confirmed to **~49 digits by a third
independent route**. `qou-ejfy` had the nucleon values at 1.4e-50 / 5.8e-50 by
exact symbolic recompute and the weights at 60 digits; this adds the full
*atom* trace. The claim that these witnesses carry ~16 real digits is now
refuted three ways over.


## 2026-09-27 — RESOLVED as a currency note; the cap was already lifted

Owner instruction "resolve issues". The audit doc
`docs/audits/2026-08-09-canonical-chain-walk-gaps-marked.md` §Step 6 concluded
*"Corpus claims of '1e-50 agreement' are about χ^λ, not tr_M."* That is now
FALSE, and the paragraph's own diagnosis is what fixed it.

The live `y_lambda_at` returns **50 digits, not 30** — `wedderburn_jones_markov.py`,
the `q_val is not None and not _symbolic` early-return, whose in-source comment
records the change and the reason: `y_lambda_su_n` runs at `COMPUTE_DPS` (70), so
the cap threw digits 31–50 away for a "consumer compatibility" no canonical
consumer needed (`tr_m_atom_via_transfer.py` re-lifts through `mp.mpf(str(v))`).

RE-MEASURED live, proton q₀, `|Σ_λ y_λ f^λ − 1|`:

    n=3  1.06911e-50      n=5  1.06911e-50
    n=4  2.67276e-51      n=6  1.33638e-51

19–20 orders below the ~1e-31 the doc records.

**Stated as a FLOOR, not an agreement.** The returned values are themselves
truncated at 50 decimals, so 1e-50/1e-51 is the serialization floor of the
arithmetic — it marks where the cap stops binding, not how exact the mathematics
is. The in-source comment's own figures (0.0 / 1.336e-51 / 0.0 for n=3/4/5)
differ from mine by less than that floor, so the two do not disagree; both say
"at the floor".

**A second 30-digit cap survives and is HARMLESS — do not "fix" it.** The literal
`sp.Float(nstr(y, 30), 30)` is inside `_y_lambda_at_convention_C_HISTORICAL`
(convention C, excised 2026-08-09, dead), unreachable on the D path because the
live early-return fires for every numeric `q_val`. It is the exact string the
audit doc quotes, which is why it still looks live.

The dated analysis is KEPT per the `qou-3nva` precedent (a dated audit doc is a
record of its own session); added as a currency note, not a rewrite. Step 7's
four ~1e-31 rows get a pointer; its `4.1e-15` transfer-kernel row is a different
route, unaffected by the cap, and remains the only genuinely independent one.

Commit `b2909d503f`.


## F64_IMPORT re-measured 2026-09-14: 119 -> 173, and a measured case where the advisory tier hid a real defect

Re-ran `f64_into_mpmath_audit.py --tier F64_IMPORT` on
`claude/raw-float64-drain-2026-09-13` (rebased on main `8b7b663b566`):

    LAUNDERED        34      <- NOT zero; qou-tj98 closed on "exits 0"
    F64_CAST        225
    F64_ENGINE_ENTRY 45
    F64_IMPORT      173      <- qou-tj98 recorded 119

**qou-tj98 is `completed` on the acceptance test `--tier LAUNDERED` exits 0,
and that tier now lists 34.** Not re-opening it here — recording that its
acceptance no longer holds, so it must not be cited as evidence the laundering
class is closed.

### The measured case

`computations/probes/casimir_grid_sweep_probe.py` sat in F64_IMPORT — the tier
whose own footer says it "never fail[s] a run" — while carrying

    from q_parameter import Q        # float(_d["q"]), a float64 constant
    q = mpf(Q)                       # round-trip: the whole sweep at ~17 digits

Fixed to `Q_MP` (commit 3c1317dea45). Every field diffed against the committed
witness, 183 in / 183 out / 0 lost / 0 gained:

    rel_residue fields   n= 26   ALL moved   max 4.26e-13   median 1.9e-14
    every other numeric  n=112    55 moved   max 6.67e-16   median 6.9e-17

The residues are the probe's HEADLINE quantity and they were good to ~13
digits, not 16. `rel_res = |val - pi_sq_720| / pi_sq_720` with `val` within
0.04 % of the target cancels ~3.4 digits and amplifies the 1e-16 cap.

### The control, and the discriminator it gives

`casimir_phi_q_markov_probe.py` — same tier, same import, same `q = mpf(Q)`,
same edit (commit 0b92461054b). Its 26 residue fields moved **4.13e-15**, a
factor ~100 less, because it is a NULL RESULT: nothing is near the target, so
nothing cancels.

So F64_IMPORT is a genuinely MIXED bucket and qou-tj98's "review individually,
do not bulk-edit" is right. The discriminator this pair supplies:

  **does the file form a difference of near-equal quantities?**

If yes the f64 cap is amplified into the reported digits; if no it stays at
f64 epsilon and is harmless. Unfortunately that ranks the probes that FIND
something above the ones that do not — i.e. the dangerous cases are exactly
the ones whose conclusion someone will quote.

### Still live in this bucket, same `q = mpf(Q)` shape

  computations/probes/casimir_carlitz_q_bernoulli_probe.py:127
  computations/probes/casimir_macdonald_probe.py:209

and `mp.mpf(HBAR_Q)` in `probes/c4_two_nucleon_probe.py:71`,
`probes/c4_a3_a4_long_compute_probe.py:85`, `probes/c3_he4_long_compute_probe.py:113`,
`probes/c3_borromean_all_cases_probe.py:80`.

### Correction to my own commit message

Commit 0b92461054b says the tier finding is "raised as bean qou-lz8f". That is
the wrong bean — `qou-lz8f` is the mpf/json destructive-write class — and the
finding is not new besides: this bucket has been tracked here (qou-840k) and
in qou-tj98 since 2026-08-08. What is new is the re-measured count and the
grid-sweep/phi-q pair above.

Not proposing a tier re-ranking: re-severity-ing a live gate is an owner call.


### CORRECTION, same hour — I COUNTED LINES, NOT FINDINGS. Four of the five numbers above are wrong, and one inverts its own conclusion.

The table above came from `grep -c ""` on each `--tier` run's stdout, i.e. the
LINE COUNT of the output file. `--tier X` prints all six tier headers plus ~30
lines of explanatory boilerplate every time, so the count is dominated by
prose. Re-read from the tier header lines themselves:

    tier              I WROTE   ACTUALLY                        fails a run?
    LAUNDERED           34      **none**                        yes
    F64_CAST           225      104 file(s), 184 site(s)        yes
    F64_ENGINE_ENTRY    45      0 file(s), 0 site(s)            no
    F64_IMPORT         173      139 file(s)                     no

**The inverted one is LAUNDERED.** I wrote that qou-tj98 "is `completed` on the
acceptance test `--tier LAUNDERED` exits 0, and that tier now lists 34 ...
must not be cited as evidence the laundering class is closed." The tier prints
the literal string `LAUNDERED — none.` **qou-tj98's acceptance HOLDS.** Strike
that paragraph; it was an accusation manufactured entirely by my own
miscount, against a bean that is correct.

**F64_IMPORT is 119 -> 139, growth of 20, not 119 -> 173.** Of the 139, 129 are
under `computations/`; the rest are `qou-mass/src/qou_mass/_internal/` (the
GENERATED mirror — never hand-edit, see AGENTS.md), `tools/pyhecke`, and one
`tools/qou-substrate` test. No truncation in the listing; the 129/139 gap is
those ten paths, not a cap.

**The live failing number for this bean is F64_CAST: 104 files, 184 sites**,
and the audit's own text calls them "defects" rather than circumstantial.
That is the figure to work, and it is the one my table buried.

**What survives unchanged.** The grid-sweep / phi-q pair is a direct
measurement of two witnesses and does not depend on any tier count: 4.26e-13
vs 4.13e-15 on the same edit, and the near-cancellation discriminator. Both
commits' witness diffs stand.

**Contaminated elsewhere:** commit `0b92461054b` (pushed, PR #7318) says
"Measured: 173 files sit in F64_IMPORT". Read 139. The rest of that message —
the two witness diffs, the tier's advisory status, the two named live
`q = mpf(Q)` files — is unaffected.


## Casimir family drained, 2026-09-14 (branch claude/raw-float64-drain-2026-09-13)

Nine producers, unmodified-first baseline on every one before editing.

| producer | before | after | why the after is what it is |
|---|---|---|---|
| casimir_grid_sweep | 81 | 0 | serializer + a genuine `mpf(Q)` cap |
| casimir_phi_q_markov | 80 | 0 | serializer + cap (control for the above) |
| casimir_q_factorial | 54 | 0 | serializer |
| casimir_carlitz_q_bernoulli | 33 | 0 | serializer |
| casimir_jet_order_derivation | 20 | 0 | serializer + a 1e-40 test made real |
| casimir_hoefsmit_additivity | 20 | 0 | serializer + TWO gates retightened |
| casimir_n_unknot_construction | 17 | 0 | serializer + a 1e-40 test made real |
| casimir_xi_2_dig_deeper | 18 | **16** | 16 are the CORRECT record — see below |
| casimir_d6_qcorrection | 5 | **1** | 1 is the CORRECT record — see below |
| casimir_epsilon_vacuum | 12 | 0 | was running at `mp.dps = 15` (`qou-0p2h`) |

Ratchet throughout: NEW 1 / REGRESSED 0 (the inherited
`computations/audits/braid-encoding-audit.witness.json`). Padding ratchet: 61 NEW
before and after, none of them a casimir witness, and this branch touches none of
the 11 files it reports.

## Finding 1 — THE DIRTY COUNT IS NOT A MEASURE OF REMAINING DEBT

Two files cannot reach 0 without making the corpus WORSE, and this is the
opposite of every blind spot in the detector-blindness taxonomy: the ratchet here
sees too MUCH, by design.

- `casimir_xi_2_dig_deeper`, 16 survivors. All in
  `finding_B3_survey_numbers_not_reproducible`: 8 are CITED survey values
  (0.9946, 0.9839, 0.9680, 0.7510, recorded twice each), 4 decimals and no more;
  8 are derived from them and deliberately `round(..., 4)` because 4 is what the
  input justifies.
- `casimir_d6_qcorrection`, 1 survivor. `rows[5].vol = 2.82812` is Vol(5_2), a
  cited SnapPy value with no closed form available here. Measured what `fmt`
  would do:
  `fmt(mpf("2.82812")) = 2.82812000000000000000000000000000000000000000000000000000000`
  — 60 significant figures claimed for a 6-figure datum. That is the padding
  defect with the sign flipped (padding a SHORT source rather than a binary64
  one), and the padding audit does not flag it BECAUSE THE ZEROS ARE REAL, which
  makes it the more dangerous form.

An agent draining by count will eventually reach a file where the only way to
move the number down is to overstate a citation. At that point the number is the
wrong target.

## Finding 2 — A TOLERANCE SIZED TO A FLOAT64 CAST, and the obligation that
## comes with removing the cast

`casimir_hoefsmit_additivity_probe` had two assertions that read their own
recorded values back and whose tolerances were EXPLICITLY sized to the float64
the recording introduced. The witness said so in its own `source` strings:

    "gate 1e-15 is the float64 the table is serialised through, not a chosen band"
    "gate 1e-9 covers the float64 the table stores at N = 1000"

Both honest as written; both FALSE the moment the cast goes. Carrying mpf through
collapsed the gaps:

    disjoint_union_volumes_are_additive      6.29520766772e-16  ->  0.0 EXACTLY
    geom_epsilon_coefficient_is_linear_in_N  1.69196699728e-11  ->  2.1365027428e-65

i.e. the float64 was not merely *covered by* the gates, it was their ENTIRE
CONTENT. Retightened 1e-15 -> 1e-58 and 1e-9 -> 1e-54, both from the
SERIALIZATION ROUND-TRIP BOUND (largest value x 1e-60) and NOT from the observed
gap — sizing a gate to its own measurement is the fit defect AGENTS.md names.
Left alone, 1e-9 would have been 56 orders of slack on a quantity now known to
1e-65.

**So a `float()` -> `fmt()` change is not always local.** If any assertion,
threshold or tolerance downstream was sized to that cast, removing it obliges
retightening, and the witness's own justification text becomes a false statement
that must be rewritten. Grep the file for `tolerance=` before calling a drain
done.

## Finding 3 — three 1e-40 thresholds that could not fail

`casimir_n_unknot_construction` (`n_stable`), `casimir_jet_order_derivation`
(`matches_textbook`), and by the same shape `_spread` in the former: a threshold
of 1e-40 applied to float64 quantities of order 0.1-1e5 is satisfiable only by
landing on EXACTLY 0.0, which two identical double expressions always do. Each
gave the right answer for the wrong reason. All three now mpf on both sides.

Verdicts unchanged in every case, and checked rather than assumed:
`bare_count_is_uniquely_n_stable` computed '1', n-stable set `['bare_count']`;
`q_independence`/`matches_textbook`/`derivation_works` all True. What changed is
that jet-order's test is now NON-TRIVIALLY satisfied — the rows compute
`pi_sq * (1/120) / 6` against a `pi_sq / 720` target, which round differently:
`a - b = 1.414949856e-73` (rel 1.032e-71), one ulp, clearing 1e-40 by ~31 orders.
Under float64 the two were the same bit pattern.

## Finding 4 — the DISCRIMINATOR for whether a float64 cast matters

Two files in this family both moved ZERO recorded fields when their cast was
removed, and the two facts mean opposite things:

- `xi-2`: the cast sat 14 orders BELOW the input noise (4-decimal survey values).
  A discipline fix; it could not have changed anything.
- `n-unknot`: the cast sat ABOVE the tolerance the code tests against. It made a
  test undecidable. A correctness fix that happens to leave today's answer alone.

So the discriminator is not the SIZE of the cast but its size RELATIVE TO THE
TOLERANCE THE CODE COMPARES AGAINST. Read the comparison, not the cast.

## Finding 5 — the builder's guard counts more than the ratchet does

`qou_substrate.witness._check_raw_float64` has no integral carve-out, so four
`vol: 0.0` rows are raw float64 to it and invisible to the corpus ratchet (9 vs 5
on the d6 witness). It is the better LOCATOR — it prints exact JSON paths at the
producer — but it only fires when the witness is actually WRITTEN: `save()`
short-circuits an unchanged payload and skips the guard with it. An unmodified
re-run printing no warning is NOT an all-clear, and a witness that does not appear
in `git status` after a re-run has PASSED the baseline check, not failed to write.

## Also learned

`round()` on an mpf returns an mpf that is not exactly rounded —
`round(mpf('-0.12345678901234567890'), 4) = -0.1234999999...9998` — so where a
4-decimal record is wanted the cast must come FIRST, `round(float(x), 4)`.

`min()` on float64 keys HIDES TIES. In `casimir_q_factorial`,
`best_classical_ok` flipped from `pi^2/(6*[5]_q!_sym)` to
`pi^2/(6*([5]_q!+[5]_{q^-1}!)/2)` — two MATHEMATICALLY IDENTICAL expressions
(`[k]_q` is invariant under q -> 1/q), differing by 5.6e-71, i.e. one ulp at dps
70. `float(r1) == float(r5)` was True, so `min()` used to return the first;
now the second wins. Residue 8.6154% either way and the conclusion is untouched,
but the tie-break is arbitrary and is now VISIBLE where float64 rounding hid it.
Not fixed — making it deterministic is a tidy, not a precision fix.


## 🛑 "LOCAL (drainable now)" OVERSTATES BY 22 % — the partition models only the
## UPSTREAM direction (measured 2026-09-14)

`computations/audits/drain_queue_relay_partition.py` asks *"does this producer
READ another witness?"*. It does not ask *"does another producer read THIS
witness?"* — so an **upstream** witness lands in LOCAL, labelled "drainable
without touching an upstream", and draining it breaks its consumers.

Measured with the partition's OWN criterion and regex:

```
partition LOCAL:              287 witnesses,  4368 fields
of those, READ downstream:     25 witnesses,   945 fields   (22 % of LOCAL fields)
```

Top five, all currently advertised as drainable now:

| fields | witness | readers |
|---:|---|---:|
| 452 | `hadron-knot-table` | 2 |
| 78 | `deltalambda/alpha-cluster-volume-additivity` | **3** |
| 72 | `bw-chirality-isotopes` | 2 |
| 67 | `symmetrized-constituent-general` | 2 |
| 42 | `probes/rho-k-markov-multiplicativity` | 1 |

`hadron-knot-table` is already excluded for runtime (>50 min per bound atom), so
the live figure is **24 witnesses / 493 fields**. The genuinely safe remainder is
**262 witnesses / 3,423 fields** — still the right queue, just 22 % smaller than
advertised.

### Demonstrated on the 78-field case, and it breaks 5 of 6 consumption patterns

`alpha-cluster-volume-additivity.witness.json` is read by three producers.
Serializing its fields with `fmt` (the drain) turns floats into strings, and
their consumption splits two ways:

```
inter_cluster:172   float(b_ame - b_add) - row['deficit_MeV']   TypeError: float - str
inter_cluster:223   rows[i]['deficit_MeV'] / rows[i]['H1_...']  TypeError: str / str
inter_cluster:225   rows[i]['deficit_MeV'] > 7                  TypeError: str > int
mixed_multibond:183 r['deficit_MeV'] - r['pred_deficit_MeV']    TypeError: str - str
mixed_multibond:196 f"{c['deficit_MeV']:8.4f}"                  ValueError: format 'f' on str
alpha_activation:161 mp.mpf(str(ADD['12C']['deficit_MeV']))     ok  <- the only safe form
```

Five of six break. The one that survives is `mp.mpf(str(...))`, which is
string-agnostic — so a codebase that used it uniformly would be drain-safe, and
this one does not.

**Severity, stated precisely rather than dramatised.** All three relays write via
the destructive shape this arc already documents —
`json.dump(wit, open(out, "w"), indent=1)` at lines 456 / 535 / 445 — where
`open(..., "w")` truncates before `json.dump` can raise. But every failing site
above sits in the ANALYSIS section, upstream of those lines, so the crash happens
before the write and **the downstream witnesses survive**. Three crashing
producers, not three destroyed witnesses. I checked the line ordering rather than
assuming the worse case.

### I nearly filed a false blind spot against the partition script — third time
### this session

My first two re-scans returned 26 / 882 and 100 / 5,272 and BOTH were wrong,
because I matched witness names with a bare `grep -oE '[\w./-]+\.witness\.json'`.
The committed script uses

```python
WIT_READ = re.compile(r"""["'][^"']*\.witness\.json["']""")
```

— a **quoted literal whose closing quote is immediately after `.witness.json`** —
and that is the better discriminator, because it separates *opening* a file from
*citing* one in prose. The worked case: `alpha_cluster_volume_additivity_probe.py`
mentions `binding-link-volumes.witness.json` three times, and all three are prose
— one comment, and two `"source": "binding-link-volumes.witness.json (deprecated
volume-search ID)"` provenance strings, whose trailing text defeats the regex by
design. My grep called it a RELAY; the script correctly calls it LOCAL.

So: **the tool is sound in the direction it measures, and its label is the
overclaim.** The reusable rule is the one this session keeps re-learning from the
other side — *the audit reads bindings, grep reads spellings* — here as **an
audit's stricter regex beat my looser one, and the stricter one was right.**

### Options

- **A — record it and drain only the 262 safe witnesses.** Free; the 24 stay
  listed as drainable and the next agent can hit the same rake. *This is what I
  did, absent authorisation for B.*
- **B — add a downstream column to the partition script**, so a LOCAL entry with
  readers is flagged and its readers named. ~20 lines, changes no published
  number, only the queue's advice. Not taken: it adds a capability rather than
  making code agree with the corpus, so it is not clearly inside either
  2026-09-07 exemption.
- **C — drain the 24 together with their readers**, porting each reader to
  `mp.mpf(str(...))` in the same commit. Correct and much larger; the reader
  edits touch producers in other arcs.

**My judgement: B then A.** The flag is cheap and it is the difference between a
queue and a trap; C is real work that should be scoped per-witness.


## The LOCAL queue splits THREE ways by `fmt` usage, and 12 of them are abandoned
## drains (measured 2026-09-14)

Correcting a claim I made in PR #7318's own body. It states the clean class is
filtered on *"producer exists, calls `set_compute_dps()`, no numpy, not an
orphan, **`fmt(` count zero**"*. **There is no `fmt` filter.**
`grep -n fmt computations/audits/drain_queue_relay_partition.py` returns nothing;
the script's only producer-side tests are

```python
if "set_compute_dps" not in src or "import numpy" in src:
    continue
```

So the queue silently mixes producers at three different stages, with three
different costs:

| class | producers | dirty fields |
|---|---:|---:|
| `fmt` **called** — partial drain | 34 | 444 |
| `fmt` **imported, NEVER called** | **12** | **200** |
| no `fmt` anywhere | 239 | 3600 |

### Why the middle class is worth naming

Twelve producers import `fmt` and call it **zero** times while making `float()`
calls. That is not a style variation, it is the fingerprint of a drain that was
started and abandoned — someone added the import, meaning they had decided the
mpf-to-string move was correct here, and then the calls never landed. They are
the cheapest targets in the whole queue: the import is present, the intent is
documented by its own presence, and the only work is at the recording sites.

```
   57  computations/alpha/alpha-5-jucys-murphy-central.witness.json      fmt=0  float=24
   39  computations/probes/brane-tower-two-avenues-probe.witness.json
   37  computations/entanglement-orders.witness.json
   26  computations/probes/khovanov-klr-rank-cohomology-probe.witness.json
   10  computations/q-beta-predicted.witness.json
    9  computations/q-beta-form-a-n1-extension.witness.json
    9  computations/chirality-avg-content-chiral.witness.json
    6  computations/sdp-gamma-gamma-to-qqbar.witness.json
```

`alpha_5_jucys_murphy_central` is the extreme case: `from _precision import
set_compute_dps, fmt` on line 61, **0** `fmt(` calls, **24** `float(` calls.

### Why the partial-drain class is worth naming separately

A partial drain is lower-risk than a virgin producer for a different reason: the
author already made the per-field judgement for some fields, so the remaining
`float()` sites are usually the ones missed rather than the ones deliberately
kept. Note that both kinds of deliberate keep exist in this corpus and must not
be "finished" blindly — `casimir_d6_qcorrection` keeps one float on purpose
(a 6-figure SnapPy citation) and `casimir_xi_2_dig_deeper` keeps sixteen (cited
4-decimal survey values). So a `fmt`-calling producer with float()s left is a
*candidate*, never a to-do.

High fields-per-float is the signal to rank on, not raw field count — it means
each remaining cast sits inside a loop and one edit clears many fields:

```
   90 fields  fmt=1  float=2    brane-tower-isospin-diagnosis    (WITHHELD — other arcs' drift)
   27 fields  fmt=1  float=10   binding-bring-enhancement-compare (mine, this session, 39 -> 27)
   21 fields  fmt=1  float=3    sweeps/low-isotope-binding-sweep  (mine, 102 -> 21)
   33 fields  fmt=2  float=1    qbeta/qbeta-cosh-q-sinh-q-candidate-scan
```

### Option

Adding a `fmt`-usage column to the partition script is the same shape as the
downstream-column proposal above (option B there): ~10 lines, no published number
moves, and it turns the queue from one list into three ranked by cost. Same
reason for not doing it unasked — it adds a capability rather than making code
agree with the corpus. Bundling both columns into one patch would be the
efficient version if the author wants either.

**Correction count for this session: this is the fifth claim of mine to need
fixing** — after the qou-840k tier line counts, the three casimir "float64 caps"
that were not caps, the qou-0p2h remedy, and the two wrong downstream re-scans.
Four of the five were a detector or filter I described without reading its source.


## A FOURTH reason a LOCAL witness is not drainable: its INPUTS are float64 at source (2026-09-14)

The partition script's LOCAL bucket means "this producer reads no other
witness". It does **not** mean the producer's numbers are mpf. Nine of the 284
LOCAL producers take their substrate constants from `computations/substrate/hecke_core.py`,
whose module-level `h` and `z` are **plain Python floats** — verified by import,
not inferred:

```
h  float  0.20906029879563937
z  float  0.6126880371464652
```

So `mp.mpf(str(float(h_val)))` — which is literally what
`probes/brane_tower_two_avenues_probe.py` writes — is a **no-op**: the value was
already a double, the cast lifts the double's binary expansion, and `fmt` then
writes ~45 further characters of binary64 tail. The raw-float64 ratchet would
read 0 for that file while every recorded value stayed float64-derived. That is
laundering, and it is the one outcome this whole arc exists to prevent.

**Screened and deliberately NOT drained: `probes/brane_tower_two_avenues_probe.py`
(39 fields).** It looked like the ideal next target — no downstream readers,
reads only its own witness, `fmt` already imported with 0 calls, 23 `float()`
sites, so one edit clears many fields. The `hecke_core` import is what
disqualifies it.

### Measured populations (post-rebase onto `main` f580bec78cf, 2026-09-14T19:2xZ)

Same predicates as `drain_queue_relay_partition.py`, imported rather than
re-spelled, so the LOCAL set here IS that script's LOCAL set:

```
LOCAL total                284 producers  4187 fields
  hecke_core (capped)        9 producers   698 fields
  bare Q, no Q_MP (capped)   9 producers   231 fields
  genuinely drainable      266 producers  3258 fields
```

`hecke_core` bucket, by field count:

```
  452  hadron-knot-table                          (also >50 min per bound atom — excluded twice over)
   90  brane-tower-isospin-diagnosis              (also WITHHELD: other arcs' drift)
   39  probes/brane-tower-two-avenues-probe
   37  entanglement-orders                        (also has a downstream reader: unified_low_isotope_predictor.py)
   34  catalan-binding
   25  deltalambda/he4-stage2-ranking-seminormal-xcheck
   12  probes/b-pred-mirror-slope-closed-form
    7  binding-multibond-wenzl
    2  rho-k-graded-atomic-mass
```

`bare Q` bucket (imports `Q` with no `Q_MP`; `q_parameter.Q = float(_d["q"])`,
so the substrate pin is capped at ~17 digits before the producer starts):

```
   67  symmetrized-constituent-general
   42  probes/rho-k-markov-multiplicativity
   41  per-atom-rho-deviation
   35  m-p-m-e-li2q
   20  probes/binding-depth-stratified-derived-alpha-probe
   18  probes/gg-production-bond-probe
    4  binding-depth-stratified
    2  probes/probe-convention-d-vs-c-borromean
    2  proton-wedderburn-block-diagnostic
```

**The `bare Q` bucket is the cheap one and is a genuine precision fix, not a
launder** — unlike `hecke_core`, `q_parameter` carries `Q_MP = mpf(_d["q"])`, the
full pin, one import away. The ordering rule from earlier in this bean applies:
`Q -> Q_MP` **first**, `fmt` after. Draining these nine in the other order is
exactly the laundering case.

**`hecke_core` is the expensive one and its fix is upstream, in `hecke_core`
itself** — the module would have to serve `h` and `z` as mpf (or add `_MP`
siblings, matching `q_parameter`'s own convention). That touches 9 producers'
recorded numbers at once and is not this branch's scope. Filing it as the
finding, not doing it.

### Figure that moved, so do not quote the old one

An earlier measurement this session read **8 producers / 673 fields** for
`hecke_core` and **267 / 3283** clean. The delta is exactly the 25 fields of
`deltalambda/he4-stage2-ranking-seminormal-xcheck`, and the LOCAL total moved
287 -> 284 / 4368 -> 4187 across the same rebase (54 main commits). Re-measure
with the script rather than quoting either figure.


## A FIFTH class, and it is invisible to the partition script by construction: the double-precision CHARACTER path (2026-09-14)

Found by draining `probes/rho_k_markov_multiplicativity_probe.py` (42 -> 0), where
the fix was not serialization at all. `computations/substrate/char_fast.py`
exposes two character evaluators:

```
chi_lambda_fast(shape, word, q_val=None, precision="double") -> complex
    sp.lambdify(..., modules=["numpy"]);  np.asarray(fn(q_val), dtype=complex)
    prod = prod @ (complex(c)*sigmas_num[g] + complex(d)*I)

chi_lambda_fast_mp(shape, word, q_val) -> mpmath.mpc
    sp.lambdify(..., modules=["mpmath"]);  mp.matrix arithmetic
```

The first is **complex128 whatever `q_val` you hand it** — the σ_i matrices are
built `dtype=complex` and the products are numpy. So a producer can pass the
50-digit pin, set `mp.dps = 70`, and still be capped at ~1e-16, which is exactly
what happened: the rho_k probe reported max branching residue `1.60e-14`, its own
prose called that "machine precision", and its assertion was NAMED
`wenzl_branching_identity_machine_precision` with a 1e-12 gate. On the mpmath
sibling the same identity verifies at **3.02e-70** — 56 orders lower.

**Why the partition script cannot see this.** Its producer test is
`"set_compute_dps" in src and "import numpy" not in src`. The numpy is in
`char_fast`, not in the caller, so a double-path caller passes the filter and
lands in LOCAL looking drainable. In the rho_k case that verdict was *right* —
the file WAS drainable, just not by removing casts — but the filter reached it by
luck rather than by seeing the cap. Nothing in the queue distinguishes
"drainable by serializing" from "drainable only by changing the arithmetic" from
"not drainable at all". Candidate row 48 for
[`docs/audits/2026-08-15-detector-blindness-taxonomy.md`](docs/audits/2026-08-15-detector-blindness-taxonomy.md)
— same family as rows 17-21 (a cap the detector is structurally unable to reach),
but one import hop further out than any of them.

### Measured surface

Live (non-`_deprecated`) callers of the double path, and the dirty fields behind
them:

```
   28  computations/probes/poly-q-proof.witness.json                      <- probes/poly_q_proof_probe.py (5 double calls)
   62  computations/sublemma-2-1-h9-tritium-verify.witness.json           <- sublemma_2_1_h9_tritium_verify.py (2)
   95  computations/sublemma-2-1-A-operator-extract-h12-nn.witness.json   <- sublemma_2_1_A_operator_extract_h12_nn.py (1)
  ---
  185  fields, 3 witnesses, CONFIRMED behind the double path
```

Six further callers exist and their status is **undetermined, not clean** —
`sublemma_2_1_h9_branching_basis`, `sublemma_2_1_h12_he4_branching`,
`sublemma_2_1_A_operator_extract_h9`,
`sublemma_2_1_A_operator_extract_h12_nn_streamed`,
`a_operator/A_operator_extract_at_level`, and `nuclide_braid_pipeline`. The first
five are library/pipeline modules whose witness `producer_for` does not resolve by
name, so "no dirty witness resolved to it" is an artifact of the resolver, not a
measurement. Do not read that line as an all-clear.

**`nuclide_braid_pipeline.py` is the one to look at first** — it calls the double
path once and the mpmath path twice, i.e. it is a candidate *layer straddle
inside one producer*, mixing complex128 characters with 70-dps ones. That is the
shape AGENTS.md's "never straddle the two layers inside one quantity" rule exists
for, one level down from the q₀ pin it was written about. Not measured here.

Also `computations/_deprecated/rho_k_markov_multiplicativity_probe.py` is a
3-double-call copy of the file drained today; the live one is under `probes/`.

### Two caveats on the fix, both recorded at the site

- The mpmath path is ~10x slower (its own docstring). Fine at H₆ (Specht dims
  ≤ 16); the H₉/H₁₂ A-operator extracts in the list above are already named in
  AGENTS.md as long-compute, so switching those is a cost decision, not a free
  precision win.
- **Retighten the gate from the SERIALIZATION ROUND-TRIP bound, never from the new
  residue.** rho_k went 1e-12 -> 1e-58, derived as (largest serialized character
  2.813) x 10^-OUTPUT_DPS ~= 2.8e-60 with a decade of headroom. Sizing it to
  3e-70 would be a bound sized to its own miss.

### One downstream artifact left deliberately stale, and it UNDERSTATES

`folio/quantum-observable-universe/mass-endomorphism/rho-k-graded-expansion.md`
line 43 cites the verification as *"machine precision ($3.2 \times 10^{-14}$)"*.
That is now 56 orders pessimistic. The block belongs to the mass-endomorphism
arc, so it was not edited — rewriting another arc's published figure is an owner
call and not a side effect of a float64 drain. It understates rather than
overstates, so nothing downstream is inflated by leaving it; the discrepancy is
recorded in the producer docstring and the witness description so a reader
comparing the two is not misled.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
