---
# qou-840k
title: 'EXCISE FLOAT64: 222 float()-casts of q-derived constants across 129 files; existing audit tier was too narrow and read clean'
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T23:54:30Z
updated_at: 2026-08-09T00:16:16Z
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

* `content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step03-markov-trace.md:92-95`
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
