---
# qou-syit
title: 'unified_low_isotope_predictor: committed witness is 24.8x stale AND its refresh is blocked by the raw-float64 ratchet'
status: todo
pr: 8336
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T16:32:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
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


## MAIN CHANGED THE ANSWER, 2026-08-26 — the count fell 57 -> 36 without the arithmetic changing

Merged 124 commits of main and re-measured. **My conclusion above is now wrong
in type and right in substance, and the new state is arguably worse.**

`light_isotope_sweep.tr_M_at_q0` now returns an **`mpf`**. The file is
**byte-unchanged** — all 8 `float(` sites still there, no commit touched it —
so this is **import-cone drift**: main's `187aa0242d`
("chi_sym_alt_closed_form: 36 raw float64 fields -> 0") drained the character
closed forms, and `total = 0.0; total += y * chi` promotes the whole sum the
moment `chi` is an mpf.

### What that did to the witness

| | pre-merge | post-merge |
|---|--:|--:|
| raw float64 payload fields | 57 (33 LOCAL / 24 INHERITED) | **36** (21 / 15) |
| long numeric strings | 0 | **60** |

21 fields left the ratchet's count and became 50-digit strings — among them
`T1_descended`, `E_0_MeV_per_cat` and both `tr_M_*_at_q_0`, i.e. exactly the
INHERITED ones this bean was about.

### The arithmetic did not improve

Measured on the live objects: `w_lambda types = {'float'}` and
`chi types = {'float', 'mpf'}`. Both conventions produce a float weight —
plancherel `w = float(d_q_val**2/nfac)`, wenzl-schur
`y = float(w["y_lambda_numeric"])`. A float64 multiplicand caps the information
content of the product at ~53 bits however many digits mpmath then prints. That
is arithmetic, not an experiment.

**A correction to my own instrument, recorded because I nearly shipped it.** I
first tested this by running at dps 30/60/90 and checking digit stability. It
agreed to 31 digits and I read that as "the precision is real". **That test
cannot detect float64 contamination at all** — a float64 input is bit-identical
at every `mp.dps`, so a contaminated result is stably *wrong*. Do not use
dps-stability for this question.

### The corpus caught it, mechanically, and it is RED ON MAIN

`scripts/precision-gates.sh` goes **RED: float64-padding ratchet** — 59 padded
occurrences, 38 distinct values, 46 NEW-not-baselined. The named offender is
`computations/chi-sym-alt-closed-form.witness.json`, the witness that same drain
commit produced:

    assertions[2].computed
        claims  -1.0558397672668704547760398781974799931049346923828...
        really  -1.0558397672668705

**Verified as main's, not this branch's:** that witness is byte-identical to
`origin/main`, this branch does not touch it, and the audit run on a pristine
`origin/main` checkout reports the same 59 / 46. So the padding gate is red on
the base branch.

### The generalisable lesson

Draining `raw-float64` by promoting a float to `mpf` **without fixing the
arithmetic** moves fields from the raw-float64 ratchet into the *padding*
ratchet. If padding is not also checked, it looks like progress: the headline
count drops, the values gain 34 meaningless digits, and the ratchet that was
watching them goes quiet. Here the padding gate caught it — which is the gate
earning its keep, not a reason to relax it.

**Not fixed here.** `chi_sym_alt_closed_form` is `qou-l790`'s live file, merged
an hour before this measurement. Fixing it is at that producer (carry the
assertion values as strings/mpf at their true precision), and it is theirs.


## Progress Update (PR #8336)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`03d44f353473173a3c5099bb1c73d25e13571021` -> `ece176bc167f5646b3158b046f0540fa97d681a7`) in PR #8336.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8336, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
