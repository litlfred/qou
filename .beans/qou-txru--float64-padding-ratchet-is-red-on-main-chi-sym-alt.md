---
# qou-txru
title: 'float64-padding ratchet is RED ON MAIN: chi_sym_alt_closed_form substitutes a float64 q then evaluates at 60 dps'
status: todo
type: task
priority: normal
created_at: 2026-08-26T18:08:04Z
updated_at: 2026-08-26T18:35:44Z
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


## FIXED 2026-08-26 — and my own root-cause diagnosis above was WRONG

**46 NEW → 0. Padding occurrences 59 → 13, exactly the baseline.**
`chi-sym-alt-closed-form.witness.json` is no longer flagged;
`scripts/precision-gates.sh --changed` reports **all blocking gates green**.

### Retraction: line 148 was a contributor, not the cause

Everything above diagnoses the defect as
`chi_sym_alt_closed_form.py:148` substituting the float64 `Q0` into the
symbolic seminormal entry. That is a real defect and is fixed here too — but it
is **not** why the witness was padded, and I only found the real cause because
patching line 148 changed **nothing**: the regenerated values were byte-identical
to the old ones.

The actual cause:

    from _precision import fmt, set_compute_dps   # line 61

`set_compute_dps` was **imported and never called.** `mp.dps` stayed at
mpmath's default **15** for the entire run while `fmt()` serialised at 50. With
the working precision at 15, the anchor was irrelevant — every value was
15-digit whatever `q` it was computed from. Measured at import:

    mp.dps after import: 15
    Q0_EXACT           : 1.10997858275138        <- truncated at definition time

That last line is the second half of it: an mpmath constant built *before* the
dps raise is truncated when it is created, so the `set_compute_dps(60)` call
has to sit above the constants, not merely somewhere in the file.

### The evidence the fix is real, not cosmetic

    old  -1.05583976726687045477603987819747999310493469238281250000000
    new  -1.05583976726687183085942112763449928432331975561507218

They diverge at **digit 15** — the old tail was the binary64 expansion, the new
one carries real precision. `parameters.q` is now the exact 50-digit pin rather
than the float64's decimal expansion. All 16 assertions still pass.

### Why the existing gates missed it

The `mp.dps no-op` gate reports *"clean — no no-op precision assignments in
gated paths"*: it looks for an assignment that has no effect, not for a producer
that **never assigns at all**. `computations/never_raises_dps_audit.py` exists
for exactly that second case, so the check is written — this producer is simply
not in its gated set. That gap is worth closing and is not done here.

### Method note, which is the reusable part

I had a specific, well-evidenced, traced-to-the-line root cause that was wrong,
and the only reason I did not ship it is that I **re-ran the producer and
compared the serialised output** instead of trusting that a plausible fix had
worked. A patch that changes nothing is data.


## The detector gap is closed, 2026-08-26

The audit written for exactly this case reported the file **clean throughout**.
Found the clause, in `raises_precision()`:

    if isinstance(node, ast.ImportFrom):
        if any(a.name in RAISERS for a in node.names):
            return True

**Importing a raiser counted as raising precision.** `chi_sym_alt_closed_form.py`
has `from _precision import fmt, set_compute_dps` at line 61 and never calls it,
so it scored clean while computing its entire run at 15 dps.

The module docstring's imported-helper exemption is real — `mp.dps` is global
state, so a library legitimately inherits its caller's precision — but that is
enforced by `is_runnable()` (condition 3), which already exempts any file with
no `__main__` block. The `ImportFrom` clause was never needed for it, and it
silently widened the exemption from "helpers" to "anything that mentions a
raiser in an import". The selftest had **no case** covering it.

**Removed, and pinned.** New selftest case *"FLAGS a producer that IMPORTS a
raiser but never CALLS it"*; battery 8 → 9, all passing.

**Verified in both directions, which is the part that matters:**

    fixed detector vs PRE-FIX producer :  NEW 1  — 23  chi_sym_alt_closed_form.py
    fixed detector vs FIXED producer   :  NEW 0, REGRESSED 0

**Cost: zero baseline growth.** Measured before applying — removing the clause
surfaced no other findings on the current tree, because the one file it was
hiding is the one already fixed. The correction is free.


## CORRECTION 2026-08-26 — a sibling landed the same fix on main first

The "FIXED" section above is written as though I fixed this. During the
prepare-merge rebase, `computations/chi_sym_alt_closed_form.py` conflicted with
**`18bb011854` on main — "fix(chi-sym-alt): the padding red was a producer that
never raised its precision"**. Same diagnosis, same root cause, same
`set_compute_dps()` call.

**Resolved by taking main's version wholesale**, and my code change was then
*fully superseded* — the replayed commit reduced to this bean file alone, 0
lines of Python.

**Theirs is better than mine in a way worth recording.** I hardcoded
`set_compute_dps(60)` and `sp.Float(Q_50_DIGIT_STR, 60)`. They used the bare
idempotent `set_compute_dps()` and `Q0 = mp.mpf(Q_50_DIGIT_STR)`, noting that
`Q_50_DIGIT_STR` is **anchor-adaptive** — `q_parameter` rebinds it from the
anchor witness under `QOU_Q0_ANCHOR=ideal` — so the swap fixes the precision
*without pinning the producer to the proton pin*. My version would have pinned
it. That is a real defect in my patch that theirs does not have.

**What survives from this session on this bean is the detector fix**, which is
in a different file and is not duplicated: `never_raises_dps_audit.py` counted
an `ImportFrom` naming a raiser as raising precision, so it reported this exact
producer clean throughout. That is why the defect reached main at all, and
removing the clause is what stops the class recurring.

Two independent agents converging on the same root cause within hours is the
parallel-exploration policy working as intended (AGENTS.md §"Parallel
exploration is valuable"). Recorded rather than quietly dropped, because the
bean above reads as a solo finding and is not one.
