---
# qou-u87j
title: 43 content-block .lean siblings redefine a library structure with a different field set, and mask it via lean.ref candidate 1
status: todo
type: task
created_at: 2026-08-23T07:55:37Z
updated_at: 2026-08-23T07:55:37Z
---


## Measured 2026-08-23, branch `claude/n1dj-volume-iso-reading-2026-08-22`

Found while doing `qou-n1dj` item 3, where **one** instance of this appeared:
`quantum-observable-universes/quantum-observable-universe.lean` turned out to be
a second definition of `QuantumObservableUniverse`, not a stub importing the
library one — and its field set had drifted, carrying a `volumeForm_epi` the
library never had. That looked like a one-off. It is not.

### The population

Over `content/quantum-observable-universe/**/*.lean`, comparing every
`structure`/`class` declared in a co-located sibling against a library
declaration of the **same name under the same namespace**:

| | count |
|---|---|
| same-namespace duplicate definitions (sibling mirrors library) | **167** |
| field lists identical — faithful mirrors | 117 |
| field lists **drifted** | **50** |
| distinct sibling *files* carrying at least one drifted mirror | **43** |
| of those, files that are a content-block sibling (`<stem>.ts` exists) | **43 — all of them** |

The last row is the finding. A co-located `<block>.lean` wins **candidate 1** of
`lean.ref` resolution in `walkBlocks`, unconditionally and before the Lake-tree
candidates. So for all 43, the block's checkers audit the drifted copy and never
look at the declaration `lake build` actually compiles.

### Mirroring is deliberate; drift is not

`su2-emergence.lean` states the reason in its own docstring: *"content-sibling
`.lean` files compile standalone and cannot import one another"*, so a sibling
that needs a library type restates it. 117 of the 167 do that faithfully. This
bean is about the 50 that no longer do.

### It is not cosmetic — worked example

`QOU.CRManifoldData`, library `lean/QOU/QuantumObservableUniverse/CRRealisation.lean`
vs siblings `c-quantum-observable-universe.lean` and `c-quantum-universe.lean`:

- **library only:** `n_pos : 0 < n`
- **sibling only:** `contact_nondeg : ∃ p, contactForm p ≠ 0`,
  `reeb_preserves_contact : ∀ p, contactForm (reebField p) = contactForm p`

Each side carries an anti-vacuity condition the other lacks. The library's
version admits a contact form that is identically zero; the sibling's admits
`n = 0`. Whichever one a reader or a checker happens to reach, it is not the
one the other half of the corpus is talking about.

Hand-verified against both files — this is not a parser artifact.

### Method and its limits

Regex scan (`structure|class` head, then indented `field :` lines until
dedent), namespace tracked via `namespace`/`end`. Limits, stated so the number
is not over-read:

- Fields whose type spans lines before the `:` are missed; a `where`-clause
  default on its own line is not counted as a field.
- Name+namespace collision is treated as "same declaration". Two genuinely
  unrelated declarations that happen to share a fully-qualified name would be
  counted as drift — but that is itself a defect worth the same bean.
- **117/167 identical is the control.** A parser that mis-read fields at random
  would not produce a 70 % exact-match rate, so the 50 are drift rather than
  noise.

### Notable entries

`quantum-universes/quantum-universe.lean` (`def:quantum-universe`),
`c-quantum-observable-universe.lean`, `c-quantum-universe.lean`,
`lifting-and-descent/motivic-galois-character.lean` (the class `qou-s0ip` is
about), `spin-labels.lean`, `substrate-parameter.lean`,
`quantum-observable-universes/quantum-gauge-group.lean`.

A **44th** existed on `main`: `quantum-observable-universes/quantum-observable-universe.lean`,
resynced by the `qou-n1dj` branch. Re-measure against `main` if that PR has not
landed.

### Relation to neighbouring beans

- **`cscb`** (epic, content-sibling compile breakage) and **`qou-lsib`** are
  about siblings that *do not compile*. These 43 compile fine. Different defect:
  a file can be green and still be the wrong definition.
- **`qou-cu0a`** / **`qou-2u26`** are about `lean.ref`s that resolve to the wrong
  place or nowhere. This is the inverse: the ref resolves *successfully*, to a
  file that disagrees with the library.

### Options, for an owner call

1. **Gate it.** A checker comparing each sibling mirror's field set against the
   same-named library declaration, erroring on drift. Cheapest durable fix, and
   it is the only one that stops the 117 faithful mirrors from becoming the next
   50. Belongs in folio-assistant next to `check-wall-side`.
2. **Reorder `lean.ref` resolution** so the Lake tree wins over a co-located
   sibling when both exist. Removes the masking outright, but changes resolution
   for every block in the corpus and would need its own measurement first.
3. **Resync the 50 by hand.** Fixes today and not tomorrow.
4. **Stop mirroring** — give siblings a way to import library modules. Addresses
   the root cause; much the largest change.

Options 1 and 2 are complementary, not alternatives. Not started.
