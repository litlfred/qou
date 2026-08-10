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

## RETRACTED: this was reported as an LP degeneration. It is not.

`rho-k-h3a-gg-trajectory.witness.json` is the only witness with values past 1e13:

```
.data.nucleons.n.lp_dual.y_star[2]   47.232917966806724 -> 999999999999998.8
.data.nucleons.p.lp_dual.y_star[2]   58.496430716462120 -> 999999999999998.8
```

**I first wrote this up as "a dual variable has run to infinity — the LP has
degenerated under convention D, exactly as `MarkovGramDegenerate` predicts."
That was wrong**, and it is corrected here rather than quietly dropped because
it reached a commit message and a pull-request body before I checked the
producer.

`999999999999998.8` is not a solver bound. It is the producer's own sentinel.
`rho_k_h3a_gg_trajectory.py` builds the LP cost as

```python
_yc_floor = 1e-15
t_arr = [1.0 / (dim_q[lam] * max(y_chi_abs[lam], _yc_floor)) for lam in parts]
```

with the comment *"Guard against near-zero |y_λ χ^λ| (set to a large finite cost
so the LP naturally avoids that channel)."* Under convention D,
`y_(1^3) = 0` exactly, so `max(0, 1e-15)` selects the floor and the cost becomes
`1/(dim_q · 1e-15) ≈ 1e15` — `dim_q((1,1,1)) ≈ 1`, which reproduces the observed
`999999999999998.8` to the digit.

So the actual chain is: the antisymmetric weight vanishes under D (correct, and
the point of the convention) → the guard prices that channel out of the program
(by design) → the LP avoids it → the dual of an unused channel equals its cost
(ordinary LP behaviour). **Nothing degenerated.** `feasible: true` is accurate.

What is genuinely true, and was true before this regeneration, is the *structural*
statement: `det G = 0` under D, so the Markov–Gram is singular and the LP posed
over all `n!` basis elements has a corank-dimensional space of optima. That is
proved (`gram_det_eq_zero_of_radical_combination`) and written into
`prf:operator-selection-lp`. But **this witness is not evidence for it.** The
producer sidesteps the singularity with a cost floor rather than running into it,
and I mistook the sentinel for the symptom.

The remaining defect here is cosmetic but real: a witness that publishes `1e15`
as a dual variable invites exactly the misreading I made. Better to record the
channel as excluded than to price it at a sentinel — tracked in `qou-y6h7`.

### The one genuine large mover

`rho-k-h3a-wenzl-bridge.witness.json`: `max_observed_offset` 0.0080 → 31614.6,
and `Delta_minus_delta_rho` entries moving from ~1e-7 to O(10). No sentinel
involved. A model whose residuals were tuned against convention-C weights does
not survive those weights moving tens of percent. That is information about the
model, not an error in the migration.

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
