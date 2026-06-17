# L1 1 ppQ certification gap — the live cross-check fails (2026-06-17)

**Branch:** `claude/l1-1ppq-certification-gap-audit-2026-06-17`

**Finding (critical-distance):** the headline claim in
[`docs/precision-goals.md`](../precision-goals.md) — *"L1. Compute precision …
**met** … 1 ppQ"* with the gate *"already tightened to 1 ppQ"* — is **overstated**
against the live compute. Running the canonical L1 cross-check on `main`
(`computations/cross_check_trM_1ppb.py`, commit at audit time) reports **4 of 6
atoms divergent** and writes the witness with a **FAILURES** assertion:

```
  atom            Hoefsmit         markov_peel         chi-cache            Habiro       |Δ|max  status
  deuteron  0.3882864240747888  0.3882864240747891  0.3882864240747888  0.3882864715594088  1.22e-7  DIVERGE
  helium-3  0.2065408170207396  0.2065408170207397  0.2065408170207396  0.2065408585724969  2.01e-7  DIVERGE
  helium-4       (no Hoefsmit)  0.0553483351637683      (no chi cache)  0.0553483458793373  1.94e-7  DIVERGE
  neutron   0.9232332299116371  0.9232332299116373  0.9232332299116371       (no Habiro)   2.03e-16  OK
  proton    1.0653061442544499  1.0653061442544502  1.0653061442544499       (no Habiro)   2.57e-16  OK
  tritium   0.1040521067420517  0.1040521067420515  0.1040521067420517  0.1040521186784656  1.15e-7  DIVERGE
  → atoms compared: 6, divergent: 4   (witness: FAILURES)
```

Two distinct defects, neither of which is "1 ppQ certified":

## Defect 1 — the peel witness is float64-limited (~2.5e-16), not 50-dps

For the atoms where the exact methods agree (proton, neutron), `|Δ|max` is
**2.5e-16 ≈ float64 ε**, not the ~1e-48 the doc claims ("agree to ~1e-48"). The
stored 50-char witness values reveal the cause — the `markov_peel` value carries
only ~16 significant digits, zero/garbage-padded to 50:

```
proton  Hoefsmit (mpf 50dps):  1.0653061442544499756666334037445034130528872534934
proton  markov_peel:           1.0653061442544502490648028469877317547798156738281
                                             └─ diverges at digit ~13 (2.5e-16)
```

`markov-peel-atomic-tr-m.witness.json` is therefore **stale**. The cross-check's
`TOLERANCE_PEEL = 1e-12` is the honest gate for the *current* witness — it is
**not** a "1 ppQ exact method." So the L1 claim rests on **two** float-clean
methods (Hoefsmit, chi-cache) agreeing at 2.5e-16, i.e. at the float64 floor —
that is **not** a 1 ppQ (1e-15) certification.

### Root cause — the peel producer is BROKEN (regressed), not just stale

Running the current producer `computations/markov/markov_peel_atomic_witness.py`
**cannot reproduce its own committed witness**:

```
proton  (A=1): tr_M(q₀) = 1.0653062286131667…  vs committed 1.0653061442544502…  |diff| 8.4e-8  MISMATCH
neutron (A=1): tr_M(q₀) = 0.9232332971861534…  vs committed 0.9232332299116373…  |diff| 6.7e-8  MISMATCH
deuteron/T/³He/⁴He: FAILED ValueError: unknown (c, d) crossing: d=-0.10445818939954299 (= −h(½−δ/4))
```

Two regressions, both downstream of recently-merged `main` changes:

1. **Nuclei crash.** `markov_peel.crossing_from_cd` only recognises the four
   templates `(1,0) → σ`, `(1,−h) → σ−h`, `(1,−h/2) → σ−h/2`, `(0,1) → 𝟙`. It was
   **never updated for the canonical color-weighted p-n crossing**
   `σ − h(½ − δ/4)·𝟙` (`atom_braid_word_3A`'s default
   `pn_convention="bring_color_weighted"`, owner directive 2026-06-01,
   δ = `_avg_color_delta()`). Every nucleus with a p-n bridge raises.

2. **proton/neutron 8.4e-8 mismatch.** The committed p/n values are
   float64-correct (match Hoefsmit at 2.5e-16) and were produced by an *earlier*
   correct producer; the current producer yields values 8.4e-8 off. The likely
   cause is the q-parameterised-braid-word core refactor
   (`nucleon_gen_chains(q=…)`, stages merged on `main` 2026-06-17) changing the
   intra-nucleon crossing constants, so `crossing_from_cd`'s **float-tolerance
   template matching** now silently maps a crossing to the wrong σ-template
   (no crash, wrong value).

So the committed peel witness is **doubly unreproducible**: the p/n entries
predate the q-param regression, and the nuclei entries predate the
color-weighting (the producer crashes on them now). This is why peel cannot be
"the 4th 1 ppQ method" — its producer must first be repaired to (a) recognise the
color-weighted crossing and (b) reproduce the correct p/n trace under the
q-param word, *then* be regenerated float-clean.

> Even Hoefsmit-vs-chi-cache at 2.5e-16 is at float ε; a genuine 1 ppQ
> certification needs the cross-method Δ resolved well below 1e-15 (the doc's own
> §"Infra requirement: true arbitrary precision end-to-end"). The current witness
> set does not demonstrate this for the atomic traces.

## Defect 2 — extended-Habiro nuclei values diverge by ~1e-7

The fourth path (cyclotomic Habiro via `habiro-coefficients-extended.witness.json`,
intended to cover A∈{2..6}) disagrees with the exact methods by **~1e-7 on every
nucleus** (D, T, ³He, ⁴He): e.g. deuteron Habiro `0.38828647…` vs exact
`0.38828642…`. This is a real value discrepancy (8th significant figure), not a
precision-floor artifact, and it is what flips the 4 atoms to DIVERGE. Either the
extended-Habiro coefficients for A≥2 are wrong/stale, or the consumer
(`term_6_via_habiro_coeffs_mp`) is mis-assembling them.

## Why this matters for "close 1 ppQ"

"Closing 1 ppQ" cannot mean tightening the L2 (per-observable) targets while the
**L1 certification itself is failing**. The honest precedence is:

1. **Re-establish L1** — regenerate the peel witness float-clean (so peel agrees
   with Hoefsmit/chi-cache at ≪ 1e-15), and resolve the extended-Habiro nuclei
   1e-7 divergence (fix or quarantine the A≥2 Habiro path). Then the cross-check
   passes and the gate can be honestly stated.
2. **Drive the cross-method Δ below 1e-15** on the atomic traces (not just the
   3-strand closed-form anchor, which already holds at 4e-50) — the actual
   1 ppQ certification.
3. Only then is L1 "met *and certified*," and L2 work (the σ_theory shell-order
   program) sits on a sound floor.

This audit corrects the `precision-goals.md` L1 status from "met / certified" to
"**met in principle (exact methods exist), NOT certified — live cross-check
fails**" pending the two repairs above.

## Reproduce

```bash
python3 computations/cross_check_trM_1ppb.py           # prints the table above
python3 computations/cross_check_trM_1ppb.py --strict  # exits non-zero (FAILURES)
```
