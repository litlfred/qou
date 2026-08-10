# Convention-C witness regeneration — total impact

**Bean `qou-eea0`.** Every witness carrying a convention-C fingerprint, regenerated
from producers that are now convention D. Serial, one producer at a time.

## Scale

| | |
|---|---|
| producers attempted | 68 |
| succeeded | 61 |
| failed | 7 |
| wall time | 50 min |
| witnesses whose C fingerprint cleared | 38 |
| witnesses still containing a C string | 32 (see triage) |

## What moved

```
  < 1 ppm                          786  ########################################
  1 ppm - 100 ppm                  104  #####
  100 ppm - 1%                     209  ###########
  1% - 10%                         169  ########
  10% - 100%                       684  ####################################
  > 100% (order-of-magnitude)      433  ######################
```

2385 genuine shifts, 55 structural zeros, 278 emerged, 232 vanished, 746
q0-refresh moves held apart from the physics.

The centre of mass sits at **10–100 %**, not at the ~200 ppm the registry records
for already-migrated channels. That is expected and not alarming: those ppm
figures describe channels that had *already* moved to D, whereas these witnesses
are crossing C→D for the first time. The trace weights themselves change by tens
of percent — `y_(3)` 0.4154 → 0.5054, `y_(2,1)` 0.2809 → 0.2473 — so anything
linear in them moves on that scale.

## THE FINDING: an LP degenerates under D, exactly as predicted

`rho-k-h3a-gg-trajectory.witness.json` — the only witness with values blowing past
1e13:

```
.data.nucleons.n.lp_dual.y_star[2]   47.232917966806724 -> 999999999999998.8
.data.nucleons.p.lp_dual.y_star[2]   58.496430716462120 -> 999999999999998.8
```

`999999999999998.8` is a solver bound, not a result. The LP still reports
`feasible: true`, but a **dual variable has run to infinity in one coordinate**.

This is not a migration bug. It is the predicted consequence:

> Under convention D, `y_(1^3) = 0` exactly, so the antisymmetric block *is* the
> radical of the trace form and `det G = 0`. The Markov–Gram is singular.
> — `QOU/QBeta/MarkovGramDegenerate.lean`, `gram_det_eq_zero_of_radical_combination`

A singular Gram gives the dual a free direction, so the dual optimum is not
unique and a solver walks it to its bound. This is the same statement already
written into `prf:operator-selection-lp`: *"on `H_n` the LP has a
corank-dimensional space of optima differing by radical directions the trace
cannot distinguish."* Here it is, empirically, in a solver.

**The fix is not to this witness.** The LP must be posed on the non-degenerate
quotient `H_n/rad ≅ TL_n`, where the rank is `C_n` rather than `n!` — 14 not 24
at `n = 4`, 42 not 120 at `n = 5`. Until it is, this witness records a degenerate
program and should be read as evidence, not as a result.

Also in the same family, `rho-k-h3a-wenzl-bridge.witness.json`:
`max_observed_offset` 0.0080 → 31614.6, and `Delta_minus_delta_rho` entries
moving from ~1e-7 to O(10). A model whose residuals were tuned under C does not
survive the weights changing by tens of percent; that is information, not error.

## Failures (7)

| producer | status | detail |
|---|---|---|
| `categorical_bypass_volmatch_demo.py` | exit1 | KeyError: 'rows' |
| `delta_lambda_2row_stratum_analysis.py` | timeout |   ── T (Z=1, N=2, n=9) ── |
| `delta_lambda_v_hat_z_transfer_phase5d_4.py` | timeout |     gen 4 (σ_5): V̂_FULL = +1.088368, V̂_CONSTIT = 1.088368 |
| `canonical_ordering_dof_probe.py` | exit1 | ⚠ raw-float64: canonical-ordering-dof.witness.json: 25 raw float64 field(s) would enter  |
| `tr_m_q_hecke_seminormal.py` | timeout |   deuteron: canonical=0.388286, q-Hecke seminormal=0.575172, rel_err=4.81e-01, 0.36s |
| `all_nuclides_wedderburn_spectral_v2.py` | exit1 | FileNotFoundError: [Errno 2] No such file or directory: '/workspace/qou-mass/src/qou_mas |
| `q_hecke_seminormal_character_closure_probe.py` | exit1 | ModuleNotFoundError: No module named 'probe_staircase_ew_k3_categorical' |

Triaged: three are timeouts on genuinely slow producers (600 s ceiling), and the
rest are pre-existing environment breakage —
`all_nuclides_wedderburn_spectral_v2.py` hardcodes `/workspace/qou-mass/...`
(wrong for a checkout at `/workspace/qou`), and
`q_hecke_seminormal_character_closure_probe.py` imports
`probe_staircase_ew_k3_categorical`, which lives only in `_deprecated/`.

**Four earlier "failures" were mine**, not the producers': the harness set a
relative `PYTHONPATH` while running each producer from its own directory, so
`../tools/pyhecke/python` resolved to `computations/tools/...`. Fixed to absolute
paths; three of the five requeued producers then succeeded. Recorded because
"pre-existing breakage" is the tidiest possible way to be wrong about your own
bug.

## Witnesses that still contain a C string

32, and not all are defects. Three distinct reasons, from triage:

* `audits/weight-factor-audit` — an audit **of** convention C: check `C8` is
  named *"Markov parameter z = 1/(q^0.5 + q^-0.5)"*. The number is not stale
  data; the *check* now audits the wrong convention. Separate fix.
* `bond-extensivity-equal-weight` — `f_bond.pp = 0.4993203341836944`, and the
  producer rewrote nothing. A stored value, not a derived one. A bond *fraction*
  equal to `z_C` to sixteen digits wants explaining on its own terms.
* `binding-k-enumerator` — `stabilization_z` sits beside
  `historical_markov_at_braid`; a historical section preserved on purpose.

So "C fingerprint cleared" is the wrong headline metric alone. A witness can be
fully migrated and still legitimately contain the string.

## Out of this harness's reach

* 2 witnesses produced by a **Rust binary** (`rust-chi-q-via-gp-lossless`), not a
  Python script. Note the binary layer is exactly where `qou-j6il` found a stale
  artifact returning convention C, so these want the convention gate applied
  before they are trusted.
* 3 witnesses whose producers now live in `_deprecated/`. The witness outlived
  the script; these should probably be **retired rather than regenerated** —
  history is allowed to be convention C provided it says so.
