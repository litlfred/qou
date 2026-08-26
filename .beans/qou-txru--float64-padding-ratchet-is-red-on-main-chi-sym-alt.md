---
# qou-txru
title: 'float64-padding ratchet is RED ON MAIN: chi_sym_alt_closed_form substitutes a float64 q then evaluates at 60 dps'
status: todo
type: task
priority: normal
created_at: 2026-08-26T18:08:04Z
updated_at: 2026-08-26T18:09:23Z
---

Found 2026-08-26 while merging 124 commits of main into PR #5843. **Not that
branch's regression** — established below.

## The red

`scripts/precision-gates.sh` → **RED: float64-padding ratchet**

    padded occurrences : 59
    distinct values    : 38
    baseline           : 13
    NEW (not baselined): 46

Offender is `computations/chi-sym-alt-closed-form.witness.json`:

    assertions[2].computed
        claims  -1.0558397672668704547760398781974799931049346923828...
        really  -1.0558397672668705

That tail is the exact decimal expansion of the binary64 value — 50 digits
claimed, ~17 real.

## Established as main's, not the PR's

- The witness is **byte-identical to `origin/main`**.
- PR #5843 does not touch it (`git diff --name-only origin/main...HEAD` → 0 hits).
- Run on a **pristine `origin/main` checkout**: same 59 padded / 46 NEW.

Last touched by `187aa0242d` — *"chi_sym_alt_closed_form: 36 raw float64 fields
→ 0, and the noise was ours"* — main's own float64 drain, ~1 h before this
measurement.

## Root cause, traced to the line

`computations/chi_sym_alt_closed_form.py:148`, inside `chi_in_shape`:

    M[i, j] = mp.mpmathify(sp.N(e.subs(q_sym, Q0), dps))

`Q0` is imported at line 59 as `from q_parameter import Q as Q0` — **the
float64**. So a float64 `q` is substituted into the symbolic seminormal entry,
`sp.N(..., dps)` then evaluates *that* to 60 dps, and `fmt()` faithfully prints
all 50 digits of a value carrying ~17. The producer's own docstring at 125–132
says the numpy→mpmath port was done and the float64 "was introduced HERE, not
inherited" — correct diagnosis, incomplete fix: the matrix product moved to
mpmath, the *anchor* did not.

**The obvious one-line fix does NOT work, and I checked before editing.** Line
134 uses a different name, `Q0_PROTON` from `mass_at_3A_proper`, so `Q0` →
`Q0_PROTON` looks like a one-identifier repair. Measured at runtime:

    Q0_PROTON: float 1.1099785827513808
    Q0       : float 1.1099785827513808

**Both are float64.** The file has no exact anchor available under any name, so
the fix must introduce `mp.mpf(Q_50_DIGIT_STR)` and thread it through
`mass_at_3A_proper` (which also feeds `_cached_seminormal`). That is a shared
module, so this is a tranche, not a drive-by — which is why this bean records
the diagnosis instead of a patch.

## Not a duplicate of `qou-5sg8` — same class, different instance

`qou-5sg8` (in-progress since **2026-08-16**) is the identical mechanism on
`categorical-bypass-volmatch-demo.witness.json`, 4 padded fields, traced to the
same `mp.mpf(<float>)`-serialised-at-full-dps signature. Ten days open, and the
class has produced a fresh 46-field instance in the meantime.

**The generalisable point, worth more than either instance:** draining
`raw-float64` by promoting a float to `mpf` *without fixing the arithmetic*
moves fields out of the raw-float64 ratchet and into the **padding** ratchet.
Measured on the neighbouring `unified-low-isotope-predictor` in the same pass:
raw float64 payload fields **57 → 36**, long numeric strings **0 → 60**. If
padding is not also checked, that reads as progress — the headline count drops,
the values gain 34 meaningless digits, and the gate that was watching goes
quiet. Here the padding gate caught it, which is the gate earning its keep.

**A method caution from the same investigation.** I first tested whether the
promoted values carried real precision by running at dps 30/60/90 and checking
digit agreement. They agreed to 31 digits and I read that as "the precision is
real". **That test cannot detect float64 contamination at all** — a float64
input is bit-identical at every `mp.dps`, so a contaminated result is stably
*wrong*. Do not use dps-stability for this question; use the padding audit, or
check the type of every multiplicand.
