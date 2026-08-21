---
# qou-j47t
title: derived-chi-catalogue holds 2 stale y_lambda_at_zero cells its own builder no longer emits — and the builder cannot refresh them (add() raises on duplicate)
status: completed
type: task
priority: normal
created_at: 2026-08-21T15:35:44Z
updated_at: 2026-08-21T16:46:33Z
---

Split out of `qou-cdh3` (regenerate the convention-C witnesses). After that
tranche's regenerations, `derived-chi-catalogue.witness.json` is the **last
structural hit** in `scripts/convention-c-witness-audit.py`, at 2 entries. It is
NOT a regeneration item, which is why it is its own bean.

## The two entries

```
(1,1,1)  borromean     / borromean-baryon   y_lambda_at_zero = "1"   k_lambda=2
(1,1,1)  figure-eight  / higgs-pion-half    y_lambda_at_zero = "1"   k_lambda=2
```

Both are three-row blocks, which convention D annihilates
(`WenzlWeightVanishing.lean`, all n), so a nonzero Markov weight there is exactly
what the detector exists to catch.

## Why the detector is right to look, and why it is still not decisive

`y_lambda_at_zero` is **not** a name collision with `y_lambda`. It is documented
in `derived_chi_catalogue.py:124-128` as the *"leading Markov-normalisation
weight y_λ(0) … derived via T18 template (Markov axioms on the Wedderburn
block)"* — the same family of object the convention test is about.

What is genuinely ambiguous is `y_λ(0)`: **evaluated at q = 0**, or **the leading
(zeroth) coefficient** of an expansion. Under D, `y_λ = 0` identically in q for
`ℓ(λ) ≥ 3`, so on the first reading `"1"` contradicts D; on the second it may be
a normalisation index carrying no convention content. The cells also record
`q_convention: "kauffman"`, a different variable convention from the Hecke `q`
the test assumes. **Not resolved here** — deciding it is a mathematical
judgement, and clearing a detector on a guess is the `qou-emyt` trap.

## The concrete defect, which does not depend on that question

**The committed catalogue is stale against its own builder.**
`derived_chi_catalogue_build.py:324-331` now emits

```python
partition=(1, 1, 1),
...
y_lambda_at_zero="?",     # NOT COMPUTED — see above
```

for exactly these cells. The committed witness carries `"1"` from an earlier
build. The builder's own selftest-visible convention is that `"?"` clears the
audit (`convention-c-witness-audit.py` selftest: *"placeholder '?' -> clear
(unknown, not convention C)"*). So the live artefact asserts a value its producer
has since withdrawn.

Note the `derivation_ref` carry-forward note *"y_lambda_at_zero from
main@b6c23f2053 (T18 Markov-normalisation)"* is **not** a mechanism and does not
apply here — it annotates only the borromean **(2,1)** cell, whose value is
`"1/4"`.

## Why it cannot simply be regenerated

`DerivedChiCatalogue.add` (`derived_chi_catalogue.py:172-180`) raises on a
duplicate key:

```python
key = (cell.knot, cell.partition, cell.atom)
if key in self._index:
    raise ValueError(f"duplicate catalogue cell {key}; re-derive or update the "
                     "existing record explicitly.")
```

and `derived_chi_catalogue_build.py` **merges into** the existing catalogue
(`load_catalogue()` then `cat.add(c)`) rather than replacing it. Verified
read-only against the committed witness (342 cells): both
`('borromean', (1,1,1), 'borromean-baryon')` and
`('figure-eight', (1,1,1), 'higgs-pion-half')` are already in `_index`, so a
re-run raises on the first duplicate add.

So the builder is **not idempotent against a populated catalogue**. There is no
update path — the error message says "update the existing record explicitly" and
nothing implements that. Deleting the witness and rebuilding is not an option
either: the builder emits 12 cells and the committed catalogue has **342**, so a
fresh build would drop 330 (the Phase-3 Rust production cells the merge exists to
preserve).

## What this needs

1. Decide what `y_λ(0)` means for `ℓ(λ) ≥ 3` under D — a real answer, not a
   detector change.
2. Give the catalogue an explicit **update** path (the one `add`'s own error
   message tells the caller to use), so a stale cell can be refreshed without
   dropping the 330 cells that only exist in the committed artefact.

Until (2) exists, this witness cannot be brought in line with its builder by any
supported operation. That is the part worth fixing regardless of how (1) is
answered.

## Scope

No file edited. `qou-cdh3` records this as its one remaining structural hit and
does not count it as convention-C-confirmed.

---

## Summary of Changes (2026-08-21) — RESOLVED

Both open items closed. The semantics question turned out to have a clean answer
in the data, and it made the defect **larger and less alarming** than filed: not
a convention error at all.

### 1. `y_λ(0)` means the ZERO-DEFORMATION point q = 1, and the `1`s are dimensions

The catalogue itself pins the reading. Of 342 cells only **11** carried a
non-placeholder value:

| value | cells | `mu_eigenvalues` |
|---|---|---|
| `1` | **10** | every one `['1']` — i.e. every **1-dimensional** rep |
| `1/4` | 1 | `['?','?']` — the only **2-dimensional** rep |

The single genuine value decides it. Under convention D the H₃ weights are
`y_(3) = (q⁴+1)/(q²+1)²`, `y_(2,1) = q²/(q²+1)²`, `y_(1³) = 0`, and at **q = 1**
that gives `1/2, 1/4, 0` (sum check `y_(3) + 2y_(2,1) = 1` ✓). The stored
borromean `(2,1) = 1/4` **matches convention D at q = 1 exactly** — convention C
gives `0` there. So `at_zero` is `h = q − 1/q = 0`, i.e. **q = 1**, not q = 0,
and the one computed cell is already a D value.

The `1`s are then unambiguous: under D at q = 1, `y_(3) = 1/2` and `y_(1³) = 0`,
yet **both** are stored as `1` — they cannot both be weights under any
convention, and every cell holding `1` is a 1-dimensional rep. The field holds
the **representation's dimension**, in a slot documented to hold a Markov weight.

**So the audit's "convention C" label was a misdiagnosis.** The value is wrong,
but it is neither C nor D — it is a field-semantics error. Filing this as a
convention-C item (which is how it reached `qou-cdh3`) was reasonable from the
detector output and wrong on the merits.

**And the detector sees only 2 of the 10.** Its structural screen only inspects
`ℓ(λ) ≥ 3` blocks, because that is a *convention* test. Eight of the ten sit on
1- and 2-row partitions — `(3)`, `(2)`, `(1,1)` — and are invisible to it. Worth
a taxonomy row: **a convention detector catches only the subset of a
field-semantics bug that happens to land on a dead block**; the bug is uniform,
the detection is not.

### 2. The builder was already right; the artefact was stale

`derived_chi_catalogue_build.py` emits `y_lambda_at_zero="?"` (*"NOT COMPUTED"*)
for **all ten** of those cells today, and keeps `1/4` only for the borromean
`(2,1)` it genuinely derived via T18. So nothing needed computing and no witness
number needed writing — the producer had already withdrawn the values and the
committed artefact had not caught up.

### 3. The missing update path — implemented

`DerivedChiCatalogue` gains **`update()`** (replace in place by
`(knot, partition, atom)`; raises if absent) and **`upsert()`** (update-or-add,
returns whether it replaced). `add()` is **unchanged** and still raises on a
duplicate — its error message told callers to "update the existing record
explicitly", and that method now exists.

Deliberately separate methods rather than `add(..., replace=True)`: replacing a
derived cell is a different act from recording one, and it should not be
reachable by adding an argument to the call every producer already makes.

`derived_chi_catalogue_build.py` gains **`--refresh`**, which swaps `cat.add` for
`cat.upsert` so the script can re-run over a populated catalogue and bring its
own 12 cells back in line. Default behaviour unchanged.

### 4. Verified

Snapshotted the 342-cell catalogue first, then ran `--refresh`:

- **342 cells before, 342 after**, key set identical — the 330 Phase-3 cells that
  exist only in the artefact are untouched. (This is what a delete-and-rebuild
  would have destroyed: the builder emits 12.)
- **Exactly 10 cells changed**, every one `y_lambda_at_zero: '1' → '?'`, and **no
  other field on any cell** differs.
- The genuine `1/4` is **preserved**.
- `convention-c-witness-audit.py`: the catalogue's 2 structural entries are
  **gone**. The remaining structural hit is helium-4 alone (`qou-cdh3`,
  infeasible on its producer), and the symbolic hit is the telescope's proved
  identically-zero weights.
- Semantics checked directly: `update()` raises on an absent key, `add()` still
  raises on a duplicate, `update()` leaves the count unchanged, `upsert()`
  returns `True` replacing / `False` adding.

### Deliberately not done

Computing the **real** `y_λ(q=1)` values (`1/2` and `0` at n=3 under D) rather
than leaving `"?"`. The builder's own comment marks the T18-template extension as
a follow-up, so `"?"` is the honest state: it says *not computed*, which is true,
instead of asserting a number nobody derived. Filling them in is a small,
well-posed follow-up — the D weights are known in closed form — but it is new
derivation, not this repair.
