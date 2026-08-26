---
# qou-syit
title: 'unified_low_isotope_predictor: committed witness is 24.8x stale AND its refresh is blocked by the raw-float64 ratchet'
status: todo
type: task
priority: normal
created_at: 2026-08-26T16:32:15Z
updated_at: 2026-08-26T17:27:59Z
---

Measured 2026-08-26 while answering "are all witnesses and their dependencies
updated?" on the low-isotope dashboard. Tree was clean before and after; every
re-run below was restored with `git checkout -- computations/`.

## The finding

`computations/unified-low-isotope-predictor.witness.json` is self-stale
(`scriptHash eba70b193ab6 -> a84f7373d484`), computed 2026-07-05, and its
recorded `commitSha 6949424f7a` resolves to nothing — bucket `rewritten` in
`witness_staleness_triage.py`, so "diff the producer first" is unrunnable and a
re-run is the only way to decide it.

Re-ran it. **It moves, hard.** Masked leaf diff (volatile keys removed:
computedAt/timestamp/durationMs/commitSha/scriptHash/environment/...):
**49 of 148 fields moved.**

    .data.isotopes[0].B_pred_MeV   -10570.825368453634 -> -261780.8500515504
    .data.isotopes[0].err_pct      -475285.92          -> -11767825.77
    .data.isotopes[1].B_pred_MeV   -14509.157577614    -> -340647.044194764

That is a **24.8x** move on the headline predicted binding. (Both values are
already nonsense as physics — a binding energy of -10 GeV — so this producer is
exploratory whatever its state; the point is that the committed witness does not
describe the committed producer.)

## Why it cannot simply be refreshed

The re-run emits, on stdout, a live gate warning:

    raw-float64: unified-low-isotope-predictor.witness.json: 70 raw float64
    field(s) would enter the witness -- .parameters.q_0, .parameters.m_e_MeV,
    .parameters.Q_beta_n_MeV, .parameters.E_0_MeV_per_cat,
    .parameters.tr_M_proton_at_q_0, .parameters.tr_M_neutron_at_q_0,
    .data.isotopes[0].T1_descended, .data.isotopes[0].T4_frobenius ...

So refreshing this witness would land **70 raw float64 fields** on `main`, which
the NO-FLOAT64 ratchet forbids and which `scripts/precommit-precision-warn.sh`
would flag on the commit. Note `q_0`, `m_e_MeV` and both `tr_M` values are in
that list: the *inputs* are float64, so per AGENTS.md rule 3 ("a float64 input
poisons the whole result") the payload resolves to ~1e-16 regardless.

**Do not fix this by rebaselining.** The fix is at the producer: carry
`mpmath.mpf` from the source and serialize with `_precision.fmt`. Baselines
drain, never grow.

Sibling beans on the same class (this one is the specific blocked refresh, not a
duplicate of the drain): `qou-5lw7` (1712 payload sites), `qou-xwjs`,
`qou-kn46`, `qou-7q56`, `qou-7kq3`.

## Two neighbours measured in the same pass, recorded so they are not re-measured

- **`low_isotope_mass_table` REFUSES, by design.** Exit 2 after 35.8 s with
  *"Re-run at >= the committed target_dps, or pass
  --allow-precision-downgrade if the downgrade is intended"* (bean `qou-7e1t`).
  Wrote nothing. This is a guard working correctly — a non-zero exit here is not
  a defect, and `--allow-precision-downgrade` would launder a downgrade into a
  refresh. Its witness stays stale until the precision is available.
- **`low_isotopes_binding_sweep` refreshes cleanly and moves a little.** Exit 0,
  35 of 134 masked fields move, at ~1e-8 relative on `Delta_lambda` and
  `B_pred_canonical_MeV` (7th-8th significant figure — small, but real at 60 dps,
  not noise). This one is a safe refresh whenever someone wants it.

## Not in scope of this bean

Whether `B_pred_MeV = -261780 MeV` is meaningful at all. It is not, but that is
the producer's physics, not its precision hygiene.


## MEASURED 2026-08-26 — the split is 33 LOCAL / 24 INHERITED, and the 33 were deliberately NOT converted

Re-ran the producer and classified every raw-float64 payload field by origin.
**57 payload fields, not 70** — the 70 in the gate's warning includes assertion
metadata.

| bucket | n | examples |
|---|---|---|
| **LOCAL** — fixable in this producer | 33 | `.parameters.q_0`, `.parameters.m_e_MeV`, `.parameters.Q_beta_n_MeV`, `.data.isotopes[*].T6_habiro`, `.data.isotopes[*].delta_m_shell` |
| **INHERITED** from `light_isotope_sweep` | 24 | `.parameters.E_0_MeV_per_cat`, `.parameters.tr_M_proton_at_q_0`, `.parameters.tr_M_neutron_at_q_0`, `.data.isotopes[*].T1_descended`, `.data.isotopes[*].T5_BW_chirality` |

### Why converting the 33 would have been the wrong fix

`B_pred_MeV = T1 + T4 + T5 + T6 + Tk3 + Δm_shell`, and `T1_descended` is
inherited. So **every headline number in this witness is float64-derived no
matter what this producer does locally.** Dressing the 33 survivors in `mpf`
would lower the ratchet count and leave the arithmetic exactly as accurate as
it is now — the "note it as a limitation and ship" move AGENTS.md rule 3 bans
("a float64 input poisons the whole result").

**What WAS done, on separate grounds:** the two provenance parameters with
exact sources are now recorded exactly — `q_0` from `Q_50_DIGIT_STR` and
`m_e_MeV` from `experimental_constants._M_E_MEV`. That is a *provenance* defect
independent of precision: at 16 digits a reader cannot tell which q₀ pin the run
used. `Q_NEUTRON_MEV` has no exact private sibling and stays the float64 it is.
The computed parameters stay float64 **and stay unserialised as strings**,
because stringifying them is precisely the laundering the gates flag. Ratchet
count 70 → 55; the witness still reports dirty, correctly.

### The real scope

`light_isotope_sweep.tr_M_at_q0` is float64 by construction, not by a few stray
casts:

    71:  H_VAL = float(Q0 - 1.0 / Q0)
    72:  _BLOCK_CACHE = BlockCache(float(Q0), H_VAL)
    96:  d_for = {c: float(d_for_ctype(c, H_VAL)) for c in CTYPES}
    107: float(product.diagonal().sum()) if is_sparse
    108: else float(np.trace(product))
    145: wenzl_y = {tuple(w["partition"]): float(w["y_lambda_numeric"])
    176: w = float(d_q_val ** 2 / nfac)
    221: E_0 = float(Q_NEUTRON_MEV) / abs(Q_cat)

A numpy + `BlockCache` pipeline end to end. Porting it to mpmath is a real
tranche with a performance consequence, not a drive-by.

**Blast radius: 3 module-importers, NOT 118.** A bare-name grep for
`tr_M_at_q0` returns 118 files, but that name is defined in several modules
(`pyhecke.trace`, `markov_trace_recursive`, `hecke_characters`, …). By actual
`import light_isotope_sweep` the count is **3**. Recording this explicitly
because the bare-name-grep overcount is the error class that has already cost
this session twice (`\bmarkovZ\b` across five namespaces; `head -8` of a
`dim_q` grep sorted `_deprecated` first).

### Still true, and the reason this may not be worth the tranche

`B_pred_MeV(D) = −261780 MeV`. The producer's physics is broken independently
of its precision — that is the k≥3 tail, not term 4 and not float64. Fixing
`light_isotope_sweep` would make this witness honest, not correct.
