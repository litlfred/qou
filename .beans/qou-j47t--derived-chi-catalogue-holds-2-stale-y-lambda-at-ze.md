---
# qou-j47t
title: derived-chi-catalogue holds 2 stale y_lambda_at_zero cells its own builder no longer emits — and the builder cannot refresh them (add() raises on duplicate)
status: todo
type: task
created_at: 2026-08-21T15:35:44Z
updated_at: 2026-08-21T15:35:44Z
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
