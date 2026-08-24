---
# qou-geqa
title: '24 producers on main cannot complete: 14 crash, 10 exceed 240s'
status: todo
type: task
created_at: 2026-08-23T20:16:11Z
updated_at: 2026-08-23T20:16:11Z
---



## What was measured

Found while running the substantive census (PR #5577): a git-baselined sweep of
all **152** producers behind self-stale witnesses. 128 completed. The other
**24 (16 %) could not run to completion at all** and were excluded from the rate.

This is a stronger defect class than a drifted number. A producer that cannot
run can never regenerate its witness, so that witness is frozen at whatever it
last emitted — and nothing in the corpus currently surfaces the condition. The
staleness audits read witnesses; they never execute producers.

## CRASHED (14) — non-zero exit

    computations/alpha_em_b2_bring_period_matrix_probe.py
    computations/hadron_knot_table.py
    computations/lepton_tower_probe_1_cinquefoil_muon.py
    computations/low_isotope_mass_table.py
    computations/per_irrep_pole_atom.py
    computations/probes/h6_deuteron_free_word_chi_lambda_probe.py
    computations/probes/pentagon_rt_torus_knot_higgs_probe.py
    computations/probes/per_knot_density_borromean_q_locality_probe.py
    computations/probes/qbeta_braid_nf_sdp_offset_probe.py
    computations/probes/qbeta_habiro_element_probe.py
    computations/probes/su4_1111_markov_trace_probe.py
    computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py
    computations/rho_k_h3a_refinement.py
    computations/substrate/lever1_habiro_element_fit.py

## TIMEOUT (10) — exceeded 240 s

    computations/atom_mass_derived.py
    computations/bar_pairing_binding_observable.py
    computations/binding_depth_stratified.py
    computations/chi_4he_binding_lossless.py
    computations/chi_at_q_inv_via_native_mpfr.py
    computations/delta_lambda_v_hat_z_transfer_phase5d_4.py
    computations/gram_transfer_quadratic.py
    computations/probes/ground_state_ordering_a3_probe.py
    computations/probes/ksel2id_sw_identification_probe.py
    computations/qbeta/qbeta_c4even_exact_sseries_probe.py

Timeout is a budget artifact, not necessarily a defect: some of these are
legitimately long-compute (`qou-mnrd` records one producer that ran two hours
without finishing). Re-run them with a real budget before calling any of them
broken. The 14 crashes are the actionable half.

## Next step

`computations/witness_producer_executes_audit.py` (on main via #4960) is the
right tool — it exists precisely for "can this producer still produce its
witness?". This bean hands it 14 concrete instances rather than a sweep to
discover them.

## Do not

Do not "fix" a crash by regenerating its witness in this container. Several of
these touch the q0 anchor machinery, and an environment-stamped regeneration is
how a container fingerprint gets written into the corpus — see the reverted
witnesses in #5333.


## 2026-08-23 — diagnosed, and the count corrects DOWN to 12

Re-ran all 14 crashers with the harness defects fixed. **Two were my own
harness, not defects:**

  * `h6_deuteron_free_word_chi_lambda_probe.py` — exits **0** once
    `computations/` is on `PYTHONPATH`. My runner used `cwd=<producer dir>`
    and supplied no path.
  * `per_irrep_pole_atom.py` — declares required positionals
    (`atoms [atoms ...]`). Running it bare is operator error.

So the honest figure is **12 broken of 152**, not 14. Same failure mode as the
census itself: the harness was measuring itself. Caught before reporting this
time, not after.

## The 12, by root cause

**mpf-formatting (3) — known class, known fix, do these first.** AGENTS.md
already documents it: a float64 drain makes constants `mpmath.mpf`, and an
untouched `print(f"{k:.7f}")` becomes a hard `TypeError` because `mpf` has no
`__format__`. The producer then dies *before* `json.dump`, so its witness can
never be regenerated.

    lepton_tower_probe_1_cinquefoil_muon.py    Object of type mpf is not JSON serializable
    pentagon_rt_torus_knot_higgs_probe.py      unsupported format string passed to mpf.__format__
    per_knot_density_borromean_q_locality_probe.py   same

Fix per AGENTS.md: `float(x)` is permitted **inside an f-string for display
only**, or prefer `mp.nstr`. Do not widen a gate to make it pass.

**Silent death (2)** — non-zero exit, no stderr at all. Worse than a traceback:
nothing to grep for.

    low_isotope_mass_table.py
    qbeta_braid_nf_sdp_offset_probe.py

**Environment / input (2)**

    alpha_em_b2_bring_period_matrix_probe.py   its own environment guard fires
    lever1_habiro_element_fit.py               FileNotFoundError on an input

**Genuine import defect (1)** — unlike the two artifacts above, this one still
fails *with* `PYTHONPATH` set:

    rho_k_h3a_refinement.py                    from codata_constants import ...

**Library/dtype (2)**

    hadron_knot_table.py       no supported conversion (dtype float64 vs object)
    su4_1111_markov_trace_probe.py   scipy.sparse does not support dtype object

**Domain errors (2)** — these may be correct refusals rather than bugs; check
the invariant before "fixing" either:

    qbeta_habiro_element_probe.py         NoneType not subscriptable
    qbeta_habiro_phase5q_dn_refactorize.py  AmDifferenceInvalid: D - n

## Do not

Do not regenerate any of these witnesses in an agent container. Several touch
q0/anchor machinery, and an environment-stamped regeneration writes a container
fingerprint into the corpus — see the reverted witnesses in #5333. Fix the
producer, and let the witness be regenerated where the environment is right.

## 2026-08-24 — DEFINITIVE: 8 broken, not 14. Four were the harness.

The census reported 14 crashes. Re-tested properly, **8 are real**. The count
corrected downward four times, and each correction was a different defect in my
own runner — that taxonomy is worth more than the number:

| artifact | producer | why the census was wrong |
|---|---|---|
| missing `PYTHONPATH` | `h6_deuteron_free_word_chi_lambda_probe` | needs `computations/` importable; exits 0 with it |
| required CLI args | `per_irrep_pole_atom` | declares positionals; a bare run is operator error |
| sweep order-dependence | `lepton_tower_probe_1_cinquefoil_muon` | exits 0 **in isolation**; a sweep that already set PYTHONPATH still called it broken |
| wrong cwd convention | `lever1_habiro_element_fit` | uses REPO-ROOT-relative paths; exits 0 from root, fails from its own dir |

**A producer-runner is only trustworthy if it does all four:** sets
`PYTHONPATH` to `computations/` and `computations/substrate/`; skips producers
declaring required positionals; cleans the tree **before** each run as well as
after; and tries **both** `cwd=<producer dir>` and `cwd=<repo root>` before
calling anything broken.

Fixed this session (PR #5615, both now exit 0 either way):

    per_knot_density_borromean_q_locality_probe.py   mpf f-string x5, numerics unchanged
    pentagon_rt_torus_knot_higgs_probe.py            mpf f-string + _fmt_deep serializer

## The 8 genuinely broken

    alpha_em_b2_bring_period_matrix_probe.py    its own environment guard fires
    hadron_knot_table.py                        dtype float64 vs object
    su4_1111_markov_trace_probe.py              scipy.sparse rejects dtype object
    low_isotope_mass_table.py                   exit 2, NO stderr
    qbeta_braid_nf_sdp_offset_probe.py          exit 2, NO stderr
    rho_k_h3a_refinement.py                     import fails even with PYTHONPATH
    qbeta_habiro_element_probe.py               NoneType not subscriptable
    qbeta_habiro_phase5q_dn_refactorize.py      AmDifferenceInvalid: D - n

The two `exit 2, no stderr` cases are the worst to inherit: nothing to grep for.
The last two may be **correct refusals** rather than bugs — check the invariant
each is asserting before "fixing" either.

## 2026-08-24, second correction — 4 broken, not 8, and not 14

Two more of the "8" turned out to be guards, and two more had already succeeded.
**A non-zero exit is not a defect.** The classifier has to look for a traceback.

**Deliberate refusals — working correctly:**

    low_isotope_mass_table.py            refuses: precision below committed target_dps
                                         (names its own --allow-precision-downgrade flag)
    qbeta_braid_nf_sdp_offset_probe.py   refuses: mp.lu_solve would NOT raise, returns
                                         ~1e50 entries at ~1e-3 residual; running on
                                         "would publish laundered numbers"

Both print their reason to **stdout**. My harness captured stderr only, so it saw
"(no stderr)" and filed them as mysterious crashes. They are the anti-laundering
discipline functioning exactly as designed.

**Succeeded, then exited non-zero:**

    alpha_em_b2_bring_period_matrix_probe.py   writes its witness, then flags an
                                               environment check
    rho_k_h3a_refinement.py                    writes rho-k-h3a-refinement.witness.json
                                               (11275 B, closure error 0.0 MeV), then
                                               exits 2 on DeprecationWarnings

**The 4 genuinely broken — all carry tracebacks:**

    hadron_knot_table.py                     TypeError: dtype float64 vs object
    su4_1111_markov_trace_probe.py           ValueError: scipy.sparse rejects dtype object
    qbeta_habiro_element_probe.py            TypeError: NoneType not subscriptable
    qbeta_habiro_phase5q_dn_refactorize.py   AmDifferenceInvalid: D - n

The last two may still be correct refusals raised as exceptions rather than clean
exits — check the invariant each asserts before "fixing" either.

## The full unwind: 14 -> 4

    4  harness artifacts   PYTHONPATH x2, sweep order-dependence, cwd convention
    4  non-zero by design  2 guards + 2 that wrote their witness first
    2  real, now fixed     mpf-formatting (PR #5615)
    4  real, outstanding   tracebacks, listed above

Six requirements for a trustworthy producer-runner, each bought by one of the
above: set PYTHONPATH; skip scripts with required positionals; clean the tree
BEFORE each run as well as after; try both cwd=<producer dir> and cwd=<repo
root>; capture stdout as well as stderr; and check for a traceback rather than
trusting the exit code.

## 2026-08-24 — re-verified against main: 2 broken, not 4

Rebased onto main (+368) and re-ran all four names on the current tree.

| producer | verdict now |
|---|---|
| `hadron_knot_table` | **fixed on main** by the sibling `qou-n7ue` arc (`46dcfc62a57`). Runs; slow — the "honest cost" that bean records. Not mine to touch. |
| `qbeta_habiro_phase5q_dn_refactorize` | **NOT a defect.** Raises `AmDifferenceInvalid`, a `ValueError` subclass `habiro/habiro_coefficients_atomic.py:488` defines for "when a_m-differencing would silently build the wrong object". Names the correct route and beans `qou-0ndb` / `qou-lnog`. Same class as `qbeta_braid_nf_sdp_offset_probe`'s refusal — a guard, working. |
| `su4_1111_markov_trace_probe` | real. `ValueError: scipy.sparse does not support dtype object` — an `mpf` reaching a sparse matrix. |
| `qbeta_habiro_element_probe` | real. `TypeError: 'NoneType' object is not subscriptable` at `main()`. |

### The sixth harness defect — my own checklist misfired

The five-item checklist I committed said "check for a **traceback** rather than
trusting the exit code". That rule is what put `phase5q_dn_refactorize` on the
broken list: **a traceback is not proof of a defect either.** A refusal
implemented as a raised domain exception is indistinguishable from a crash by
shape alone. The discriminator is whether the exception type is one the
producer's own import cone defines — a seventh item, now in AGENTS.md.

Worth naming plainly: this is the *fourth* consecutive downward correction to
this count (14 → 12 → 8 → 4 → 2), and every one of them was my measurement, not
the corpus. The rate of false "broken" verdicts from a naive runner is roughly
6 in 7.

### Overlap

`qou-n7ue` is actively draining this same backlog and covered five producers
(`hadron_knot_table`, `parabolic_cylinder_channel_mixing_probe`,
`vhat_per_crossing_chain`, `derivation_chain_validator`,
`habiro_interpolate_cross_validator`). Only `hadron_knot_table` overlapped mine.
The two remaining real defects above are **not** in that arc's scope.
