---
# qou-840k
title: 'EXCISE FLOAT64: 222 float()-casts of q-derived constants across 129 files; existing audit tier was too narrow and read clean'
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T23:54:30Z
updated_at: 2026-09-07T04:44:03Z
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
- [x] rewire `global_wedderburn_sum_q_hecke_seminormal` onto
      `_build_seminormal_matrices_mpf`
- [x] `y_lambda_at`: read `Q_MP`, and reconsider the 30-digit `sp.Float` cap
      — DONE 2026-08-24 (PR #5641). See "Round 2" below.
- [ ] `mass_at_3A_proper.py:164` BlockCache f64 seeding
- [x] correct "1e-50" claims that are actually about tr_M — RE-CHECKED 2026-08-30: no edit needed, see Round 3

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


## Round 3 (2026-08-30, branch `claude/anchor-followups-2026-08-08`) — ITEM 3 DONE

Every line number in the Round-1 plan had drifted, exactly as the "VERIFY THE
LINE NUMBERS FIRST" note warned: the function is at **470-551**, not 339-417.
The mpf helpers moved too — `_build_seminormal_matrices_mpf` is at
`tr_m_wenzl_bridge_mpfr.py:188` (plan said 144), `_chi_lambda_of_word_mpf` at
**306** (plan said 262). Everything else in the plan held.

### The trap the plan named, and it is worse than it reads

    f64:  chi_lambda_of_word(sigmas, dim, word, n_gens_required: int)
    mpf:  _chi_lambda_of_word_mpf(sigmas, dim, word, q=None)

The call site passed **four positional arguments**. A literal swap would have
bound `n_gens_required` (here `8`) to `q` — computing the character at q=8 and
returning a number, silently. Passing `q=` by keyword is not style, it is the
whole safety of this edit. Checked that dropping the argument loses nothing:
`n_gens_required` has **zero uses** in the f64 body (AST-counted, not grepped);
it is vestigial. The range-check above the loop still uses it.

### A second downcast the plan did not mention

`y_lambda_at` returns `sp.Float(..., 50)`. `mp.mpf(sp.Float(...))` rounds
through a C double, so the conversion must go through `str()`. Written that
way, with the reason in-line — this would have capped the rewire at ~15 digits
while looking correct.

### The consumer had to move in the same commit

`delta_lambda_empirical_tabulation.py` did

    q0_float = float(Q_MP)                                  # :403
    ... q_val=q0_float                                      # :405
    "contribution": fmt(term["y_at_q0"] * term["chi_q_at_q0"])   # :413

The first is this bean's own defect class — an f64 cast of the pin — and would
have discarded the entire benefit at the entry point. The third does
**arithmetic on the breakdown fields**, which are now strings; left alone it
breaks. Both fixed here. Three other readers (`:457-458` `mp.mpf(...)`,
`q_sweep_2row_dominance:56` `float(...)`, `binding_row_length_stratification:106`
`Decimal(...)`) all lift from strings already and are unaffected — checked, not
assumed.

### Verified by A/B, not by inspection

    A=1 (proton), q = Q_MP
      new (mpf)          1.14575969245730086968908159577
      old f64 path       1.1457596924573032
      relative difference  2.07e-15

Float64 epsilon. That is the signature of a correct precision upgrade: the same
mathematics, resolved further. A materially different number would have meant
the rewire was wrong. Return type is `mpf` and the three breakdown fields are
`str`, both confirmed by running it; the fixed consumer reproduces the same
total.

### The docstring's accuracy claim is REMOVED, not restated

It quoted agreement with `markov_trace_recursive` of 1e-13 (A=1) to 1e-10
(A=2). Those figures measured the f64 path. They are not re-quoted as mpf
figures, because nobody has measured this path against `markov_trace_recursive`
— asserting an improved bound I had not tested would be the same error as the
label/value mislabels in `qou-fd0e`. The docstring now says to re-measure.

### The twin CANNOT follow, and that is now recorded in the twin

`qou-mass/src/qou_mass/_internal/wedderburn_jones_markov.py` stays float64:
**`tr_m_wenzl_bridge_mpfr` does not exist under `qou-mass/`**, so mirroring the
edit raises ImportError. A note in that copy's docstring records the divergence
and, more importantly, that the two now differ in **return type and field
types**, not merely precision — callers must not treat them as interchangeable.
Closing it needs the bridge vendored or the function re-homed.

### Witness refresh NOT run — deliberately

Per this bean's standing rule and `qou-jjge`: the six named consumers now return
values that differ in the last ~20 digits, so their committed witnesses are
stale. Not regenerated here — in this corpus a producer IS its side effect, and
a precision fix must not carry a multi-producer regeneration.

### Also this round: `he_nu_sdp_psd_count_test` is NOT a violation

`qou-fd0e` had me note it as forbidden float64. Re-checked: it runs on **numpy**
throughout (`hoefsmit_matrices_numpy`, `np.linalg.eigvalsh`) and its witness
records `"engine": "numpy"`. An mpf `Q0` would be downcast at the first call.
It belongs to this bean's **67 f64-by-construction** files, not the 49 fixable
ones. My earlier note overstated it; corrected there.

`docs/audits/scripts/keystone_wrt_schurweyl_plancherel_4count_probe.py` is pure
Python and genuinely fixable — still open, and it also holds a **superseded
vintage** (B, while the canonical pin is now C), which is a second decision.


## Item 6 — RE-CHECKED 2026-08-30. The answer is DO NOT EDIT, and here is the evidence

Round 2 warned that item 6's premise had inverted and that acting on the
original instruction would introduce the error item 6 exists to remove. Checked
rather than taken on trust, because the first thing I found appeared to
contradict it.

### The apparent contradiction, and its resolution

The 30-digit cap **is still in the file** — `sp.Float(_mp_inner.nstr(y, 30), 30)`,
both `30`s, and in the `qou-mass` twin too. That reads like Round 2's note was
wrong.

It is not. That cap is at **`:315`, inside
`_y_lambda_at_convention_C_HISTORICAL`**. The live `y_lambda_at` is at 118-212
and its conversion is **`:201  sp.Float(_mp.nstr(v, 50), 50)`** — 50, with a
comment at `:179` explaining the change from 30. Round 2 raised the live path
and left the historical one, which is correct.

Verified the historical path is genuinely dead: the live function's own
docstring says so at `:151`, and every other reference in the tree is a
docstring or an audit — no runtime caller.

### Measured, not read

    mp.dps = 70
    y(3,)   = 0.50540422650393080318755870324047227566035119774981   (50 sig digits)
    y(2,1)  = 0.24729788674803459840622064837976386216982440112509   (50 sig digits)

The live path returns 50 significant digits. The cap is gone where it matters.

*(One near-miss worth recording: I checked `sum(y) - 1` as a normalisation
residual and got `-0.2473`, which looks alarming. It is not a precision result —
the two-row Wenzl cap makes `y_(1³) = 0`, so these weights do not sum to 1 in
this convention. My assumption was wrong, not the numbers. Do not re-derive that
scare.)*

### The target claim is TRUE as written

`content/…/mba-step03-markov-trace.md:94`:

> The numerical mode at $q = q_0$ meets L1 to $10^{-50}$ by the precision
> discipline of `qou-substrate`.

With the live conversion at 50 digits this holds. **Rewriting it to $10^{-30}$
would make a true statement false** — precisely what Round 2 predicted. **No
edit made to any of item 6's three targets.**

### But it only became true for ONE path today

Worth stating because it ties item 6 to item 3: the claim covers "the numerical
mode". Until this round, a reader following the numerical mode through
`global_wedderburn_sum_q_hecke_seminormal` got a **float64** kernel — ~1e-15,
not 1e-50. Item 3's rewire (same branch, previous commit) is what makes the
sentence true along that route as well. Before it, the claim was true of the
symbolic and mpf paths and false of the Hecke-seminormal numerical one, and
nothing said which path a reader was on.

### One annotation added, no behaviour changed

The historical function's comment quotes *"Verified to ~10⁻⁵⁰"* immediately
above a conversion that returns 30. Both statements are accurate — the closed
form is that good, and the conversion then discards it — but read together they
invite copying the wrong half, which is plausibly how the cap propagated in the
first place. A note now records the split, that the live path uses 50, and that
30 is kept **deliberately**: a historical path should reproduce its history, not
be quietly improved.


## Item 5 — RE-SCOPED 2026-08-30. The blocker was never the cache, and it was not cost

Item 5 read: *"the real work is an mpf-capable block cache — a `BlockCacheMpf`
beside `syt_prefix_cache.BlockCache` … lowest priority of the four."* Both
halves are out of date, and the second is misleading.

### The cache exists, and so does the whole mpf path

`BlockCacheMP` is at **`computations/hoefsmit_mpmath.py:33`** (sibling branch
`claude/sparse-mpf-character-2026-08-24`), and its docstring says it *"mirrors
`pyhecke.syt_prefix_cache.BlockCache` exactly"* — same `__init__(q, h)`, same
`get(rho) -> (a, a', b)`. More than that: `mass_at_3A_proper` **already carries
a full mpf path behind `QOU_H3A_MPF`** (`:234`), gating `_q_pair`, the
`V_hat` accumulator (`:874`) and the trace (`:949`), *off by default and
deliberately so*. So item 5 was never "build the cache"; the cache and the
wiring were both already there.

### First measurement was wrong — recording it

I measured `markov_trace_3A` and found the flag changed nothing: the total came
back `float` either way, differing only in the last digit, with no time penalty.
That would have supported "the flag does nothing". **It is the wrong function** —
`markov_trace_3A` is marked `[DEPRECATED — Plancherel-weighted form]` and its
`total = 0.0` is not gated at all. The gated function is
`per_generator_V_hat_3A`, and there the flag is unmistakable:

    QOU_H3A_MPF=0   'full': 0.6713858243916997                        float
    QOU_H3A_MPF=1   'full': mpf('0.671385824391699572753287986942…')  mpf

### The actual blocker: a hard failure, not a slow path

    A=1  flag on: fine        A=2  flag on: fine (0.013s vs 0.007s — 1.9x, not 642x)
    A=4  flag on: ValueError: scipy.sparse does not support dtype object

`build_seminormal_matrices_cached` switches to a scipy sparse representation
once **`dim > 500`** (`tools/pyhecke/python/pyhecke/syt_prefix_cache.py:154`),
and scipy.sparse cannot hold a non-numeric dtype. Under the flag the entries are
mpmath objects, so it raises. **A ≤ 2 never crosses dim > 500**, which is why
every size the flag had been exercised at looked healthy.

This is the same failure the *symbolic* branch already anticipated —
`mass_at_3A_proper.py:335` forces `sparse=False` with a comment saying scipy
"cannot hold sympy expressions". The mpf path hits the identical wall and was
never given the identical treatment. Fixed by mirroring it at `:408`;
`sparse=None` keeps the dim-based default for float64.

A/B on one shape, which is the proof:

    (4,3,2,1)  sparse=None  (old default)  -> ValueError: scipy.sparse … dtype object
    (4,3,2,1)  sparse=False (the fix)      -> ok, dim=768

### Where the cost actually is — NOT in the seminormal build

Under the flag, with the fix, shapes well past the threshold build fast:

    (4,3,2,1)  dim=768   0.2s
    (5,4,3)    dim=2112  2.0s

So the 642x is not construction. A full `per_generator_V_hat_3A(2,2)` under the
flag **did not finish in 850s**, against **75.6s** for float64 — so the A=4 cost
is **>11x and still unmeasured**; the earlier "642x at dim=162" figure is not
reproduced here and should not be quoted as if it were. The expense is in the
character multiplication over object-dtype arrays, not in building the matrices.

### What is left, and it is a decision

The blocker is gone; the flag now works above dim > 500. Remaining:
- **measure A=4 to completion** under the flag (needs a long run; the mpf disk
  cache also grew ~3 GB and had to be cleared twice during this work);
- then the standing choice this flag exists to inform — flip the default, or
  declare a float64 tier — which changes every value for ~20 consumers and is
  explicitly not a change to make silently.


## 2026-08-30 — OPTIMISATION: the mpf character kernel does ~2.2x more matrix work than it needs

Asked whether the Hecke seminormal path can be made faster. It can, exactly, and
the reason is algebraic rather than a micro-optimisation.

### The easy win was already taken

`mpmath 1.4.1` is running on the **`gmpy` backend** with `gmpy2 2.3.1`
installed, so the usual "install gmpy2" advice does not apply — it is already
the fast path. `python-flint` is NOT installed and would be the next big lever
(C-backed arbitrary-precision matrices), but that is a dependency decision.

### Where the time actually goes

Measured earlier: the seminormal BUILD is not the bottleneck — dim=768 in 0.2s,
dim=2112 in 2.0s under mpf. The cost is the character kernel
`_chi_lambda_of_word_mpf`, which multiplies a dense d x d accumulator by one
sparse factor per word letter. The A=4 atom word has **47 letters**.

### The word is runs of a repeated generator

    gens = [0x7, 1x4, 2x1, 3x7, 4x4, 5x1, 6x7, 7x4, 8x1, 9x7, 10x4]

and grouping by the full `(c, d, g)` triple gives runs of length up to 4.

### The Hoefsmit matrices satisfy the Hecke quadratic — verified, not assumed

    max |sigma^2 - (h*sigma + I)| = 3.6e-71        h = q - 1/q
    max |sigma^2 - (h*sigma - I)| = 2.0            (the other sign, for contrast)

at dps=70. So every polynomial in a single sigma is again linear in it:

    (c*sigma + d*I)^k = a_k*sigma + b_k*I
        a_{k+1} = a_k*(c*h + d) + b_k*c
        b_{k+1} = a_k*c + b_k*d

A run of k identical factors therefore collapses to **one** factor by a scalar
recurrence — zero matrix work.

    A=2   23 factors -> 10 runs   2.30x fewer matrix products
    A=4   47 factors -> 21 runs   2.24x fewer

### Implemented as PREPROCESSING, so the hot loop is untouched

The collapsed run has the same `(c, d, g)` shape as an ordinary letter, so the
optimisation is a shorter word handed to the existing loop. Nothing about the
multiplication changed. Only consecutive IDENTICAL triples collapse; different
generators do not commute and nothing is reordered.

### Correctness, three ways

- the quadratic itself, above;
- the recurrence against direct powers: `M**k` vs `a*sigma + b*I` agrees to
  3.6e-71 for k = 2, 3, 4 and 1.8e-70 for k = 7;
- the kernel against an **independent** explicit mpmath matrix product at
  dim=16: `-1.972272446151549689048234878` from both, differing by 2.5e-70.

### WALL CLOCK, measured 2026-08-30 — the op count holds up

The first two A/B attempts were both killed at 600s: their "collapse off" arm at
dim ~2000 IS the slow case, so the experiment could not finish for the same
reason the optimisation exists. Re-run at sizes where **both** arms complete:

    shape        dim   off      on       speedup   |diff|
    (3,2,1)      16    0.012s   0.005s   2.40x     5.1e-70
    (2,2,1,1)     9    0.004s   0.002s   2.09x     6.2e-70
    (4,1,1)      10    0.005s   0.002s   2.14x     1.5e-70

**2.09x - 2.40x measured**, against a predicted operation count of 2.30x at
A=2 — so the saving is real time, not just fewer calls, and the results are
identical to machine zero in every case. The earlier "operation count, not a
timing" caveat is now discharged.

### What is measured and what is not

The **factor-count** reduction is exact and measured (47 -> 21). The
**wall-clock** A/B at dim ~2000 has not returned — the "collapse off" arm is
precisely the slow case, and it exceeded 600s. So the 2.24x is an operation
count, and the speedup should track it but is NOT yet a timing I can quote.
Do not repeat it as a measured runtime until that A/B lands.

### Also this round

`term5_v2_chirality` is in this bean's list of six consumers to re-run. It has
**no `main`, no `__main__` guard and zero write operations** — it is a library
module, not a producer, and emits no witness. It needs no regeneration and the
list of six is really five.


## 2026-08-30 — python-flint: implemented, verified CORRECT, measured SLOWER, reverted

Both remaining levers were approved: add python-flint, and flip the
`QOU_H3A_MPF` default. Flint went first, because whether it makes A=4 tractable
decides whether flipping the default is safe. **It does not.**

### The headline benchmark was real and did not transfer

    dense 200x200 multiply @ ~70 digits
      mpmath   8.736s
      flint    0.013s      660x, results agreeing

That is a true measurement of the wrong thing. This kernel multiplies dense x
**SPARSE** at O(d*nnz) with nnz ~ 2d; `arb_mat` is dense at O(d^3). At d=768
that is ~380x more arithmetic, and 660x of speed does not cover it.

    shape         dim    mpmath     flint      speedup
    (3,3)           5     0.001s     0.001s     1.41x
    (4,2)           9     0.002s     0.002s     0.91x
    (4,3,2,1)     768    12.668s    32.151s     0.39x   <- 2.6x SLOWER

**Reverted.** The implementation was correct — it agreed with the mpmath path to
1e-70..1e-68 on every shape tested — and it is still a net loss where it counts.
Correct and slower is not worth shipping, and keeping it "for large dim" would
be worse: large dim is exactly where it loses.

Two structural reasons, for whoever revisits this:
1. `arb_mat` is dense-only, so the sparsity that makes the mpmath path viable
   has to be thrown away to use it.
2. Building the matrix costs O(d^2) **Python** object constructions — 590k arb
   objects at d=768, 4M at d=2000 — before FLINT does any arithmetic. An
   n=12 shape did not even finish.

A flint path could still win, but only via a sparse representation or a C-level
matrix build. That is a different piece of work, not a dependency swap.

**mpmath 1.4.1 has no flint backend** (`BACKEND: gmpy`, zero flint hooks), so
installing python-flint changes nothing on its own — the earlier note calling it
"the next big lever" was too optimistic and is corrected here.

### One bug worth recording, because the test that missed it looked fine

`_mpf_to_arb` used mpmath's `man_exp`, whose mantissa is **UNSIGNED**. The sign
lives elsewhere in the mpf, so every negative value converted to its absolute
value: sigma's -0.900918 diagonal came back +0.900918 and chi was 5.13 instead
of 1.53. My conversion test had checked `mpf(3)/7` — positive — and reported
"delta: 0.0". **A conversion test that never passes a negative number is not a
conversion test.**

### The default flip is NOT done, and should not be

`QOU_H3A_MPF=1` still cannot complete A=4: the run was killed at 850s against
75.6s for float64, and flint does not rescue it. Flipping the default would
hand ~20 consumers a path that does not finish at the sizes they use. The
approval was given on my statement that flint might make A=4 tractable; it does
not, so the premise for flipping is gone.

**What would unblock it:** a completed A=4 measurement under the flag. That is
one long unattended run, and it is the only thing standing between here and the
flip.


## 2026-08-30 — BOTTLENECK ANALYSIS: how to make A=4 tractable

Profiled the mpf character kernel at a size that completes (dim=768, the A=2
word, 23 letters -> 10 after collapse) rather than guessing from the A=4 hang.

    ncalls     tottime  function
    8,735,905    7.118  mpmath ctx_mp_python.__mul__
    8,732,967    6.952  mpmath ctx_mp_python.__add__
    8,732,968    6.495  mpmath libmp.mpf_add
            1    5.867  _chi_lambda_of_word_mpf itself
    8,735,905    3.541  mpmath libmp.mpf_mul
   17,468,917    2.661  built-in __new__
   17,468,936    1.443  built-in hasattr

### The arithmetic is NOT the bottleneck

    real arithmetic   mpf_add 6.5s + mpf_mul 3.5s        = 10.0s   ~29%
    object protocol   __mul__/__add__ wrappers, __new__,
                      hasattr                            = 18.2s   ~55%

**17.5 million object allocations and 17.5 million `hasattr` calls** — one of
each per elementary operation. gmpy2 is already doing the mantissa work
efficiently; what costs is wrapping every intermediate in a Python `mpf`.

This also explains the flint result. Flint attacked the 29%, and paid for it by
discarding sparsity — hence 0.39x. The 55% is the part worth attacking, and it
does not require giving up the sparse structure.

### Measured: fixed-point integers remove it

Same multiply-add workload at ~70 digits, 200k operations:

    mpmath mpf objects   0.294s
    gmpy2 fixed-point    0.045s      **6.58x**

Values here are O(1) in magnitude and the precision is fixed, so a scaled
integer `round(x * 2^240)` is a faithful representation: multiply is an mpz
multiply plus a shift, add is an mpz add. gmpy2's mpz is a thin C object with
no per-operation precision bookkeeping and no `hasattr` dispatch.

### The route to A=4

    run-collapse (landed)          2.24x   measured
    fixed-point kernel             6.58x   measured on the primitive
    combined                     ~14.7x    projection

A=4 under the flag did not finish in 850s; float64 does it in 75.6s. A ~15x cut
puts the mpf path in the same order as float64 rather than two orders above it.
**That is a projection from a primitive benchmark, not a measured A=4 run** —
the projection is what makes the work worth doing, and only a completed A=4 run
settles it.

### What NOT to try, with reasons

- **python-flint** — measured 0.39x at dim=768. Dense-only, so it costs the
  sparsity. Recorded above.
- **Trace-only propagation** — computing `tr(prod)` by propagating d basis
  vectors is O(d * k * nnz), identical to maintaining the d x d accumulator.
  No win, and it looks like one.
- **Lower working precision** — 70 -> 55 dps is maybe 15%, against 658% from
  the representation change. Not where the money is.

### Implementation risk, stated up front

A fixed-point kernel means owning rounding and sign handling by hand. The flint
attempt is the cautionary case: it was *correct-looking*, agreed to 1e-70 on
three shapes, and still had a sign bug that a positive-only conversion test
missed. Any fixed-point kernel must be A/B'd against the mpf path on values of
BOTH signs before it is trusted.

## 2026-08-30 — issue fixed: `rho_binding_constancy_probe`

The raw-float64 guard fired on 6 fields. Unlike `per_atom_audit_witnesses`
(Rust backend, structural) this one has **no numpy, scipy or native backend** —
it consumes `global_wedderburn_sum_q_hecke_seminormal`, which this bean made an
mpf kernel, and then threw the precision away:

    Q0 = 1.10997859555733471                      # float64, 17-digit truncation
    "ratios_B_over_trM": {k: float(v) ...}        # mpf -> float64
    "relative_spread": float(spread)

Fixed: `Q0` is the full 50-digit value as an mpf, and the payload serializes
through `_precision.fmt`. Order matters — `fmt` on a float64 renders 53 bits out
to 50 digits, which `_precision.py` warns about, so the literal had to be fixed
first.

    raw float64 fields   6 -> 0
    verdicts             identical
    relative_spread      1.65683393513255664717432155596311  (was float64)

Vintage deliberately unchanged: the canonical pin moved A -> C, this is still A,
and the payload calls it "muon (computations-layer canonical)" — re-pinning is a
convention decision, not a precision fix.


## 2026-08-30 — A=4 IS NOW TRACTABLE. Fixed-point kernel: 31.7x measured

Implemented the fixed-point route the bottleneck analysis identified. It beat
its own projection.

    shape         dim     mpf        fixed      speedup   rel.err
    (2,2,1,1)       9     0.002s     0.001s      2.31x     1.8e-71
    (4,1,1)        10     0.002s     0.001s      2.66x     4.5e-72
    (3,2,1)        16     0.005s     0.001s      4.16x     5.5e-71
    (4,3,2,1)     768    11.857s     0.374s     **31.73x** 5.9e-70

The projection was 6.58x, from a primitive benchmark. The realised figure grows
with dimension because the per-operation object overhead is a larger share of a
bigger problem — 6.58x was the floor, not the ceiling.

**Signs are covered, and deliberately so.** chi for `(3,2,1)` is NEGATIVE
(-1.9722...) and matches to 5.5e-71. `_to_fixed` applies the sign by hand
because mpmath's `man_exp` mantissa is unsigned — the exact bug that made the
flint attempt return 5.13 instead of 1.53, whose test used only positives.

Sparsity is retained, which is why this wins where `arb_mat` lost: dense flint
was 0.39x at this same dim=768.

### Why A=4 still did not finish in my tests — measured, not guessed

    partitions of 12: 77     max dim 7700     sum dim^2 = 4.79e8

    (6,3,2,1)   dim=5632   build 13.03s   chi 69.91s
    (4,3,3,2)   dim=2970   build  3.55s   chi 17.57s
    (5,4,3)     dim=2112   build  1.93s   chi  8.62s
    (4,4,4)     dim= 462   build  0.15s   chi  0.37s

chi is ~84% of the cost; the seminormal build is only 16%. Extrapolating on
dim^2 from two independent calibration points:

    calibrated on dim=5632   total chi ~ 1056s = 17.6 min
    calibrated on dim=2112   total chi ~  926s = 15.4 min

**~15-18 minutes.** Before this change it was ~31x that: **8-9 hours**, which is
why it never finished and why "did not complete in 850s" kept being the only
observation available. **My 850s command timeout is 14 minutes — A=4 was
finishing just outside the window I was measuring in.**

### What this means for the default flip

The blocker was "A=4 does not complete". That is now false: it completes in
~15-18 minutes. But that is per A=4 producer, against 75.6s for float64, so
flipping `QOU_H3A_MPF` on for ~20 consumers is a **~12-14x wall-clock cost**,
not a hang. That is a real decision with a real number behind it now, rather
than a blocker — and it is still the owner's call, not mine, because it changes
every value those consumers emit.

### Remaining headroom, if it is ever wanted

chi is O(sum_lambda dim_lambda^2) and that sum is 4.79e8 for n=12. The
fixed-point kernel removed the constant-factor waste; what is left is the
algorithm. Real further gains would need to avoid computing every irrep
separately — a different piece of mathematics, not a faster inner loop.
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
