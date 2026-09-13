---
# qou-bxw4
title: 'EPIC: close sn_isotypic_specht_split — the last OV-cone gap'
status: completed
type: milestone
priority: normal
created_at: 2026-08-15T14:41:43Z
updated_at: 2026-09-08T05:16:01Z
---

---

## CLOSED 2026-09-08 — the class is INHABITED by a real generic construction, not assumed.

This EPIC's body is empty, so its title is the whole spec: *close
`sn_isotypic_specht_split` — the last OV-cone gap*. A class with no instance is
the honest representation of an open gap (AGENTS.md §3b-tax); an instance built
from a construction closes it. There is one.

`QOU/BraidKnot/SnIsotypicSpechtSplitInstance.lean:86`:

```lean
instance instSnIsotypicSpechtSplit :
    QOU.BraidKnot.SnWedderburnPartitionBridge.SnIsotypicSpechtSplit k where
  exists_split n := ⟨matrixSplit (k := k) n, matrixSplit_centralC2 (k := k) n⟩
```

- **Generic in `k`**, not specialised to `ℚ`. Its own docstring: *"The class's use
  sites are all at `ℚ`, but nothing in the construction is: the split, the matrix
  form and the `C₂` alignment are all generic, so the instance is stated where it
  actually holds."*
- Both ingredients — `matrixSplit` (:59) and `matrixSplit_centralC2` (:68) — are
  **in that same file**, so the instance is not deferring to something unread.
- That file has **zero** `sorry` under both a term-shaped and a token-shaped
  match, and **zero** `axiom` declarations. Two of its three `QOU` imports
  (`SpechtCentralC2Scalar`, `SpechtWedderburnGeneral`) are likewise zero under
  both.

### The downstream evidence, which is stronger than mine

`QOU/BraidKnot/BurnsideDischarge.lean:35-42` records a dated correction by
someone who ran Lean:

> *"`sn_rational_specht_split`'s `sorry` was replaced by the class
> `SnIsotypicSpechtSplit`, which is now **inhabited**
> (`SnIsotypicSpechtSplitInstance`, from the RSK correspondence rather than from
> any assumption). Measured: `#print axioms` on `burnside_proved` reports
> `[propext, Classical.choice, Quot.sound]`."*

`burnside_proved` consumes this class, so a clean axiom report on it is a
statement about the instance's whole cone — which a grep cannot give.

### 🛑 What I did NOT verify, so a reviewer can overturn this in one command

**I did not run Lean.** The axiom claim above is the corpus's recorded
measurement, not mine, and I could not reproduce it here. My own evidence is
textual, and this session established twice that text matching cannot certify
sorry-freeness in this corpus — `SnWedderburnPartitionBridge.lean` (the file
declaring the class) returns 1 hit under one pattern and 4 under another, and
**all of them are prose**: `by sorry-free` at line 27, and backtick-quoted
`` `sorry` `` at 24 / 76 / 330 describing a gap in a *different* file. A term and
a mention are lexically identical here.

So the disposition rests on: a real construction, a generic instance, zero hits
of any kind in the constructing file, and a recorded `#print axioms`. If
`lean`-direct on `SnIsotypicSpechtSplitInstance` disagrees, reopen this.

### What this does NOT close

`qou-3c2j` stays **`in-progress`**, correctly. Its W1 — building
`Fin N ≃ PartitionIndex n` from the abstract Wedderburn split — is a *different
route to a different statement*, and `StandardYoungCountInstance.lean:30-32` says
so explicitly: the class *"has an instance for every characteristic-zero field …
but it is a different route and its binder is what makes the two look
different."* Closing this EPIC does not close W1.
