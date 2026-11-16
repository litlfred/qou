---
# qou-g94g
title: 'per_irrep_pole_atom_crystal: pole_u off by exactly one at the first atom'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:15:38Z
updated_at: 2026-11-16T19:43:00Z
parent: qou-trd0
---

Surfaced by the qou-hu1f regeneration pass. Pre-existing: fails identically under both intra orderings.

## Measured

    proton (Z=1, N=0, n=3, |word|=11, |partitions|=3)
      ord_min  = -18    (λ_min = (2,1))
      pole_u   = 18     expected = 19     MISMATCH

**Off by exactly one, at the very first atom**, and the probe stops there
(`--continue-on-mismatch` overrides). An off-by-one at the first case usually
means an index convention rather than a numerical drift, which is worth
checking before anything more expensive.

## NOT the intra-ordering ruling

`asserted_atoms_match_closed_form_shift` fails **identically under grouped and
borromean**. Established at assertion level, because a witness-environment gate
fires under both orderings and masks the exit code.

## Also carried by this producer

  * `⚠ raw-float64: 4 fields` — `.assertions[0].{computed,expected,tolerance}`
    and `.data.atoms[0].elapsed_sec`.
  * `⚠ environment: downgraded python 3.12.3 → 3.11.15` in this container. The
    witness on disk was produced under 3.12.3; regenerating here would weaken
    its provenance record, so it was NOT committed by the pass that found this.

- [x] Check the `pole_u` vs `ord_min` index convention before assuming a
      numerical cause — it is NOT an index convention; see below.
- [x] Drain the 4 raw-float64 witness fields.
- [ ] OWNER CALL: which law is right — `18Z+21N+1` or the measured
      `16Z+20N+2`? This probe cannot adjudicate it.

---

## 2026-09-07 — it is not an off-by-one, and my own framing above was wrong

### Run every atom, and the gap grows

The bean reasoned from the first atom: *"off by exactly one, at the very first
atom ... usually means an index convention rather than a numerical drift."*
That inference does not survive `--continue-on-mismatch`:

    atom       Z  N  measured  18Z+21N+1  gap
    proton     1  0        18         19    1
    neutron    0  1        18         22    4     <- A=1 anomaly, asserted=False
    deuteron   1  1        38         40    2
    tritium    1  2        58         61    3
    helium-3   2  1        54         58    4
    helium-4   2  2        74         79    5

The gap is 1, 2, 3, 4, 5 — not a constant. So it is not an index convention,
and checking that before anything more expensive (which the bean rightly
advised) cost one flag.

### The measured values fit a clean law of their own

Solving the four A ≥ 2 atoms exactly gives

    measured = 16*Z + 20*N + 2

and that law **also reproduces the proton** (16 + 0 + 2 = 18) without being
fitted to it. Five of six atoms, exactly. The gap to the asserted law is then
exactly `2Z + N − 1` on all five.

The sixth is the A=1 neutron, and it is anomalous under **both** laws — both
predict 22, measured is 18. It is already `asserted=False` per
`rem:crystal-bases-path-a` §"A=1 anomaly", so the fit is clean on every atom
the gate actually covers.

**NOT settled: which law is correct.** That is `prop:per-nucleon-shift-additive-linearity`
against the crystal Path A derivation, and this probe cannot adjudicate it —
it can only report that they disagree by `2Z + N − 1`. Recorded in the witness
under `measured_law_fit` so the next reader starts from the fit rather than
from "off by one".

### Two smaller things fixed

**Lithium-5 / Lithium-6 crashed with `ERROR '15'` / `ERROR '18'`** — a bare
`KeyError` from `w["tables_by_n"][str(n)]`. Neither the symbolic witness
(n = 2..12) nor the pole-order cache (n = 3, 6, 9, 12) covers n = 15 or 18, so
those atoms are simply outside the available data. It now says so, and names
the two ways to extend it, instead of printing a bare number that reads like a
crash.

**raw-float64 drained.** The assertion triple is a 0/1 indicator, now carried
as `"1"`/`"0"` strings; `elapsed_sec` is diagnostic wall-clock, now a
millisecond string. Zero raw float64 fields remain. (The bean said 4; it is 9
once every atom runs rather than stopping at the first mismatch.)

The top-level assertion still fails, correctly — the two laws do disagree.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 47 Execution Update (2026-11-16, PR #8152)

- **PR:** https://github.com/litlfred/qou/pull/8152 (`d0d9e522bf023310f599b4d6724b0703e39ccbd4`)
- **Verification & self-test:**
  - Confirmed the 2026-09-07 updates (`measured_law_fit` `16Z + 20N + 2` vs `18Z + 21N + 1` with gap `2Z + N - 1`, `n=15, 18` `KeyError` diagnostics, and string-formatted `elapsed_sec` / `computed`) are live on `main`.
  - Added `--self-test` / `--selftest` to `computations/per_irrep_pole_atom_crystal.py` verifying proton (`pole_u = 18` vs `19`) and deuteron (`pole_u = 38` vs `40`) without overwriting the witness.
- **Status:** Kept `in-progress` pending PR #8152 merge and owner decision on the `16Z + 20N + 2` vs `18Z + 21N + 1` convention.
