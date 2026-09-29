---
# qou-ulxr
title: ylambda-sign-content-threshold witness asserts PASS on main; the producer now returns FAIL
status: completed
type: task
priority: normal
created_at: 2026-08-25T12:15:31Z
updated_at: 2026-08-25T19:18:19Z
---

CONFIRMED 2026-08-25, measured on main. Audit:
docs/audits/2026-08-25-ylambda-threerow-frame-audit.md (state 3)

COMMITTED on main, computations/deltalambda/ylambda-sign-content-threshold.witness.json:

    rule_holds_all_partitions   computed 1  expected 1  passed TRUE
    no_threshold_degeneracy     computed 1  expected 1  passed TRUE
    by_n n_negative_y = 0, 0, 1, 1, 3, 4, 8, 10   (n = 2..9)

RE-RUN on main today, same producer, nothing changed:

    rule_holds_all_partitions   computed 0  expected 1  passed FALSE
    no_threshold_degeneracy     computed 0  expected 1  passed FALSE
    RESULT: FAILED -- the rule as stated is wrong.

Every mismatch reads `predicted=1 measured=-1 y=0.0`: the "measured sign" is
taken of a value that is EXACTLY ZERO.

WHY. The probe's thesis -- sign(y_lambda) is a content-threshold parity -- is a
statement about a sign structure convention D removed. Under D the Wenzl level
is r = 2, so y_lambda = 0 for every partition with three or more rows: 25 of the
30 partitions of 9, and NONE negative. The committed `10 negative at n=9` is
exactly the convention-C count.

WHY IT MATTERS MORE THAN THE OTHER INSTANCES. A passing assertion is what the QA
pipeline reads as evidence. main currently carries a green assertion for a claim
its own producer refutes, and nothing marks the committed numbers as C-frame.

NOT REPAIRED HERE, deliberately. The honest repair is a judgement about what the
probe was FOR, not a regeneration: re-running lands a witness recording FAILED,
which is truthful but leaves a dead probe asserting a dead rule. Either

  1. retire it and record that the content-threshold parity was a C-frame
     phenomenon, or
  2. restate the rule for the two-row stratum where sign(y_lambda) still has
     content, and re-derive.

Sibling instances of the same class, separate beans: qou-qdtk
(threerow_qcross_trend_probe -- D arithmetic under a C narrative), qou-58w3
(he4-two-row-dominance pins a C-era 866/1000).

Related but NOT this: threerow-sign-crossing and threerow-4he-completion are
state 2 -- stale C records whose producers now return zero, verdict INVERTS
(committed: deuteron crosses sign at q = 1.0537; live: object identically zero,
no crossing). Their re-run assertions all PASS, because they check internal
consistency rather than whether the object is nonzero, so a naive regeneration
lands a green witness with vacuous content. Whoever drains those should decide
between re-running and retiring, not default to re-running.


## RESOLVED 2026-08-25 — PR #5780 (pending merge)

Both dispositions were evaluated by measurement rather than judgement, and option 2
(restate for the two-row stratum) **does not exist**. Two independent reasons:

1. **The threshold lands exactly ON the content lattice under D** — the reason this bean
   did not have, and logically prior to the `y_λ = 0` one. `r = 2` ⇒ `Q^r = Q²` ⇒
   `c* = −2` EXACTLY, an attainable content (row 3, col 1 of every `ℓ ≥ 3` diagram), where
   `Q²·Q^{−2} = 1` exactly. Measured margin **0.0, not small**, at every `n = 3..12`. That
   is `wenzl_sign`'s `hnd` hypothesis failing — its docstring: *"without which the parity
   is genuinely undefined, not merely hard to prove."* Under C, `c* ≈ −2.5995` is off-lattice
   and the rule is well-posed.
2. **Vacuous where still well-posed** — min content on `ℓ ≤ 2` is `−1`, threshold needs
   `≤ −3`: 0 deep cells at every `n = 2..12`, all survivors positive. The discriminating
   power required `ℓ ≥ 4` (58 of 70 annihilated blocks at n=12 have `P > 0`; 0 of 7
   survivors).

Producer rewritten as a retirement record — asserts the four D-frame facts, keeps the
C measurement in `convention_c_record` rather than deleting it. Witness regenerated;
main no longer carries a false green.

**Lean untouched, not refuted**: generic in `Q`/`QR`, sorry-free, premise unsatisfiable
under D. Two docstring scope corrections only, no proof change.

Correction to my own work here: the partition total for `n = 2..12` is **270**, not the
240 I first wrote in the producer docstring.
