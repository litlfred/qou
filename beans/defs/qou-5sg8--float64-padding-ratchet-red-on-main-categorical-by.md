---
# qou-5sg8
title: 'float64-padding ratchet RED on main: categorical-bypass-volmatch-demo carries 4 padded binary64 after the mpf lift'
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T02:03:14Z
updated_at: 2026-10-04T15:11:36Z
parent: qou-9nnz
---

Found 2026-08-16 running `scripts/precision-gates.sh` as the prepare-merge §4b
gate on PR #5165. NOT that branch's regression -- it has never touched this
producer or its witness.

## The red

    float64-padding ratchet: baseline 13 -> 17 occurrences, 4 NEW

All four are in `computations/categorical-bypass-volmatch-demo.witness.json`:

    data.rows[0].ratio_direct_to_AME
        claims  0.43313064724721211939950649139063898473978042602539...
        really  0.4331306472472121
    data.rows[1].B_AME_MeV
        claims  2.2245661999999999380861481768079102039337158203125...
        really  2.2245662
    data.rows[2].B_AME_MeV
        claims  8.4817961999999997857457856298424303531646728515625...
        really  8.4817962
    data.rows[3].B_AME_MeV
        claims  7.71804132000000020497054720181040465831756591796875...
        really  7.71804132

Those tails are the exact decimal expansions of the binary64 values -- the
signature of `mp.mpf(<float>)` serialized at full dps. This is fake precision
in the padding audit's precise sense: 50+ digits claimed, ~16 real.

## Cause: the mpf lift reached the constant but not this consumer

`git log` puts the last touch on this witness at `50cc629802`
("fix(precision): the binding-family producers crashed on mpf JSON; port them
properly"), 2026-08-15. That arc (qou-3wqg / qou-hqjf) lifted `codata_constants`
and `B_AME_MEV` to mpf. This producer takes those constants, and somewhere in
its path a value goes float -> `mp.mpf(<float>)` rather than being carried as
mpf or rebuilt from the decimal string. `mp.mpf(2.2245662)` binds the binary64
value; `mp.mpf("2.2245662")` binds the decimal one -- the distinction the
`B_AME_MEV` comment in `canonical_mass_table_extended.py` already spells out for
its own literals.

## Not fixed here, and why

Different arc's file, and the fix is a producer port, not a serialization tweak.
`qou-hqjf` is COMPLETED and covers a DIFFERENT defect in the neighbourhood -- the
`TypeError: Object of type mpf is not JSON serializable` crash. Its fix made
these producers run again; this bean is about what the now-running producer
writes. Do not close one against the other.

## What a fix looks like

1. Trace where the float enters `categorical_bypass_volmatch_demo.py` -- most
   likely a `float()` on a CODATA/AME constant, or a `knot_volumes` back-compat
   f64 alias, the same aliases `qou-hqjf` names as the root of its own bug.
2. Carry it as mpf from source (or rebuild via `mp.mpf("<decimal>")`) and
   serialize with `_precision.fmt`.
3. Re-run the producer and confirm `witness_float64_padding_audit.py --strict`
   drops back to the 13 baseline.

Do NOT rebaseline. Serializing a binary64 at 50 dps is exactly what the padding
ratchet exists to catch, and the baseline drains rather than grows.

## Wider check worth doing at the same time

`50cc629802` re-ran a family of producers. This one is the only NEW padding
offender the gate reports, but the same float -> `mp.mpf` shape could sit in a
sibling producer whose witness has not been regenerated yet, in which case it is
latent rather than absent. Worth a sweep of that commit's producer list before
closing.

---

## Step 1 done — the float enters at TWO places, not one (2026-08-16, PR #5163)

Traced while draining the same defect class on `claude/producer-audit-regression-y8hlxh`.
This is **not** one bug; the four offenders split into two causes with two
different fix sizes. Fixing only the obvious one leaves the ratchet red.

**(a) The three `B_AME_MeV` — one-line fix.**
[`categorical_bypass_volmatch_demo.py:194-197`](../computations/categorical_bypass_volmatch_demo.py):

```python
_bv = vm.get("B_pred_MeV")
B_volmatch = mp.mpf(_bv) if _bv is not None else None
_ba = vm.get("B_AME_MeV", ref_val)
B_AME = mp.mpf(_ba) if _ba is not None else None
```

`_ba` arrives as a **float** off the volmatch witness, so `mp.mpf(_ba)` binds
the binary64 and `str(B_AME)` writes its 50-digit expansion. Fix is
`mp.mpf(str(_ba))` (and the same for `_bv`), which is what
`_ame_binding_mev` already does internally.

Worth flagging to whoever owns that arc: the comment immediately above those
lines reads *"Lifting with mpf rather than float keeps the precision the port
created."* It does not. `mpf(a_float)` creates no precision — it re-expands a
value that only ever had 17 digits. That sentence is the bug, written down.

**(b) `rows[0].ratio_direct_to_AME` — the deeper one, and (a) does not fix it.**
The ratio is `B_pred_direct / B_AME`, and `B_pred_direct` is float64 in its own
right: line 90 reads the weight table as
`out[(n, partition)] = float(w["y_lambda_numeric"])`. So the whole `B_pred`
chain is float64 before any AME value is involved. This needs the y_λ read
lifted to mpf, not a serialization change. Expect the ratchet to still report
1 NEW after (a) alone.

## "Wider check worth doing" — measured, and the answer is yes

The bean asks whether the same float -> `mp.mpf` shape sits in a sibling
producer with a not-yet-regenerated witness. It does. `charge_symmetric_coulomb_binding.py`
carried the identical shape: `strong()` ended in `float(E0 * mp.fsum(...))`,
and `coulomb_energy_mev` returns mpf, so `b1 - ec` promoted the float64 back to
mpf and the witness serialized it at 50 dps:

    claimed  2.833754824119470328014358528889715671539306640625
    true     2.83375482411947010855370314674164655959009612888689...
                              ^ diverges at digit 17

Fixed on PR #5163 (drop the cast; also dropped `float(_ame_binding_mev(...))`
and `float(E0)` at the witness boundary). So this is a **family** defect, not a
single producer, and the `50cc629802` producer-list sweep the bean proposes is
worth running for real rather than as a precaution.

**Not fixed here** for the same reason the bean gives — different arc's file,
actively in flight. The trace above is offered so the owner does not have to
redo it.

## FIXED (2026-08-16, PR #5204) -- and the bean named only half the cause

    float64-padding ratchet   NEW 4 -> 0, baseline 13 unchanged, exit 0
    raw-float64 (same file)   69 -> 50, drained as a side effect

The four fields split into TWO causes needing OPPOSITE fixes. This bean, written
from the audit output alone, described only the first.

### Cause 1 (3 fields) -- lift it

B_AME_MeV read from mass-table-ppb.witness.json, which carries it as a JSON
float. mp.mpf(<float>) binds the binary64; str() prints the expansion. Fixed by
sourcing the constants from codata_constants directly.

Root confirmed as this bean guessed: mass_table_ppb.py imports the mpf AME
constants and wraps each in float(). NOT fixed there -- that flips B_AME_MeV
from float to string in a witness EIGHT producers read. Still the right wider
change, still belongs to the qou-3wqg arc, still open.

### Cause 2 (1 field) -- do the OPPOSITE, stop lifting

ratio_direct_to_AME on the electron row is B_pred_direct/1.0, and
B_pred_direct = M_E_MEV * rho * tr_M. joint-tower-sdp-rust.witness.json stores
matrix_at_q_0_sym_eigvals as JSON FLOATS, so chi enters at binary64 and caps
everything downstream. y_lambda IS available at 50 digits -- and load_y_lambda()
was discarding 34 of them with a float() -- but no amount of lifting raises a cap
set elsewhere.

So those digits were never real. Fix is to stop claiming 50: the ratios now
serialize at 17 sig digits, the audit's own second remedy ('or serialize at its
true precision'). Had I only applied Cause 1's fix, this field would have stayed
red and the obvious next move -- lift y_lambda too -- would have been wasted
work.

### Lesson worth keeping

'Fix at the producer' does not always mean 'carry more precision'. When the
input floor is float64, the honest fix is to EMIT LESS. Diagnose the floor
before choosing which direction to move: here the two directions were needed in
the same file, four lines apart.

### Still open on this bean

  1. the wider mass_table_ppb.py float() drop + 8-consumer audit (qou-3wqg arc)
  2. load_y_lambda()'s float() discards 34 real digits -- harmless while chi caps
     at f64, live the moment the SDP witness carries better eigenvalues

### Correction to the PR #5163 trace above, on cause (b)

The #5163 trace and mine agree there are two causes and agree on (a). We
disagree on (b), and the disagreement is worth recording because the
prescription there would have made the ratchet green while leaving the digits
fake.

#5163 says of `rows[0].ratio_direct_to_AME`:

> This needs the y_λ read lifted to mpf, not a serialization change.

It does not, and lifting y_λ alone cannot work. That trace found ONE float
entry point and missed the second:

    y-lambda-wenzl-witness.json      y_lambda_numeric  -> str, 50 digits
    joint-tower-sdp-rust.witness.json
                                     matrix_at_q_0_sym_eigvals -> FLOAT

χ_λ is `chi_lambda_from_block`, a sum of those eigenvalues, so χ enters at
binary64 no matter how y_λ is read. `tr_M = Σ y_λ·χ_λ` is therefore capped at
~17 digits at the χ factor. Verified against the deuteron block: the eigenvalue
arrives as the Python float `1.231434090000003`.

Lifting y_λ would make `tr_M` an mpf carrying f64 noise past digit 17 — and
because such a product generally does NOT round-trip through its own float64
truncation, the padding audit's heuristic would likely stop flagging it. Green
ratchet, same fake digits. That is the outcome the ratchet exists to prevent.

So (b)'s honest fix is the serialization change: emit at the true 17 digits.
Applied in PR #5204.

`load_y_lambda`'s `float()` cast is still a real defect — it discards 34
available digits — but it is currently *masked* by the χ cap, and fixing it
alone changes no digit of the output. It goes live the moment the SDP witness
carries better eigenvalues. Left in place, recorded as follow-up 2 below.

### Follow-up 2 re-scoped: the χ floor is the Rust engine's f64 typing (2026-08-16)

I wrote above that `load_y_lambda`'s `float()` cast "goes live the moment the
SDP witness carries better eigenvalues", and named lifting χ as the higher-value
next item. Both understated the size of that job. Traced it:

    joint-tower-sdp-rust.witness.json
      scriptFile : joint_tower_sdp.rs
      engine     : hecke-engine 0.8.0 (rust)

    tools/hecke-engine/src/wedderburn_psd.rs:96
      fn symmetric_eigenvalues(m_in: &[Vec<f64>]) -> Vec<f64>

The eigensolve is f64-in / f64-out **in the engine**, and `joint_tower_sdp.rs`
types q0, min/max_eigenvalue and b_ame_mev as `f64` throughout. So χ is not
float64 because of a serialization choice that a producer edit could fix -- it
is float64 because the compute that produces it is f64.

Consequences, all of which cut AGAINST doing more work here:

  1. The 17-digit serialization applied in PR #5204 is the PERMANENTLY correct
     answer for these fields, not a stopgap pending a better witness.
  2. `load_y_lambda`'s float() cast is masked INDEFINITELY, not "for now". It
     still discards 34 available digits and is still worth fixing for hygiene,
     but fixing it changes no digit of any current output. Low priority.
  3. Raising the χ floor means porting the engine's linear algebra to arbitrary
     precision (nalgebra f64 -> rug/MPFR or equivalent), which is an engine
     project, not a producer fix -- and it would change no published number
     unless a downstream consumer actually needs > 17 digits of tr_M. Nothing
     currently does: the L1 target is cross-method agreement at 1 ppQ (1e-15),
     which 17 digits meets.

Scope note per the refuted/ruled-out discipline: this is a scope-(a) statement
about the CURRENT implementation -- the engine is f64-typed today -- not a
structural impossibility claim. An arbitrary-precision port is possible; it is
just far larger than "lift the read", and no present consumer justifies it.

Recommendation: do NOT open the engine port off the back of this bean. If a
future consumer genuinely needs tr_M past 17 digits, that consumer is the
justification and should carry it.



## A second live instance of this class, 2026-08-26 (bean `qou-txru`)

The same mechanism produced **46 NEW padded fields** in
`computations/chi-sym-alt-closed-form.witness.json`, from main's own drain
commit `187aa0242d`. Root cause traced to
`chi_sym_alt_closed_form.py:148` — a float64 `Q0` substituted into the
symbolic seminormal entry and *then* evaluated at 60 dps. Both anchors
available in that file (`Q0`, `Q0_PROTON`) are float64, so the fix needs
`mp.mpf(Q_50_DIGIT_STR)` threaded through `mass_at_3A_proper`.

Recording it here because this bean has been open since 2026-08-16 and the
class is still minting instances: the padding ratchet is red on main again,
now at 59 occurrences / 46 NEW against a baseline of 13.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
