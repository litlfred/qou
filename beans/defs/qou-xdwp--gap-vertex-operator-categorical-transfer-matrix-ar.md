---
# qou-xdwp
title: 'GAP: vertex-operator + categorical-transfer-matrix — architectural blockers behind the parse errors'
status: completed
type: task
priority: normal
created_at: 2026-09-03T23:11:58Z
updated_at: 2026-09-13T18:05:00Z
---

Two of the four parse-failures from the sibling sweep (`qou-e7xv`). Both are
now much closer, and both stop at something structural rather than syntactic.

    categorical-transfer-matrix.lean   13 errors -> 3
    vertex-operator.lean                7 errors -> 1

## Fixed (mechanical, verified)

1. A `/-- … -/` docstring immediately followed by `noncomputable section`.
   A docstring must attach to a DECLARATION; `section` is not one. Moved the
   `section` above the docstring. (Both files, identical.)
2. `LaurentPolynomial` unknown — neither imported
   `Mathlib.Algebra.Polynomial.Laurent`, though both declare
   `abbrev R_q := LaurentPolynomial ℤ`.
3. An unclosed `noncomputable section`: both open `namespace QOU` then a
   section, and close only with `end QOU`. Pre-existing, and MASKED by defect
   1 — the parse error meant the section never opened, so the imbalance could
   not surface. Added the bare `end`.
4. `vertex-operator` wrote `-(q⁻¹)` with `q : R_q`. Same shape as the
   `Inv GroundRing.R_q` cluster, but here the file is genuinely categorical,
   so `⁻¹` is simply the wrong spelling — the file declares `q_inv_param`
   itself, three lines up. Now `-q_inv_param`.

## Still open — architectural, one each

**`vertex-operator.lean`, 1 error: `ReebBundle` is not in scope.**
It is declared in `mass-theory/reeb-bundle.lean` — ANOTHER CONTENT-BLOCK
SIBLING, which this file structurally cannot import: siblings live outside
the Lake globs (`globs = ["QOU", "QOU.+"]`, `srcDir = "."`), so there is no
module path to them. Options: promote `ReebBundle` into the Lake library
(same shape as the queued `VolumeConjecture` promotion), or re-declare it
locally. Note also a wall issue if promoted as-is: `structure ReebBundle
(q : ℝ)` is archimedean while `vertex-operator` is categorical (`q : R_q`).

**`categorical-transfer-matrix.lean`, 3 errors: an undetermined implicit.**
`CategoricalTransferMatrix q` has a field `base : ExceptionalDivisor` where
`ExceptionalDivisor` is not a parameter of the structure and cannot be
inferred at the use site, so `T₁.base = T₂.base` fails to elaborate. The
structure needs to be parameterised over it (or `ExceptionalDivisor` needs to
be a concrete type).

Worth flagging: the declaration this blocks is
`axiom transfer_matrix_level_independence`, and
`prop:transfer-matrix-level-independence` is one of the FOUR provable-kind
blocks whose Lean is a bare `axiom` (found earlier this session by
`scripts/provable-block-axiom-audit.ts`). So this file wants the axiom
question settled at the same time, not two passes.

No `sorry` was added anywhere (§Zero-sorry default).

## 🛠 RECOVERED 2026-09-26 — the note below was orphaned in a DUPLICATE file for 13 days

Everything from here to the end of this bean was written on 2026-09-13 by commit `e70d947d7c` ("close(cscb, qou-e7xv, qou-xdwp)") and landed in a SECOND file claiming this same id — `qou-xdwp--…-arch.md`, with **no front matter at all**, so it was a headless body fragment rather than a bean. The *status* change reached this file (it is `completed`); only the *body* went astray. `beans list` deduplicates by id, so the note was invisible there, and `check-beans.sh` reported it only as a duplicate id.

It is reunited here verbatim and the fragment file is deleted. Recovered while migrating `.beans/` → `beans/defs/` (bean `qou-utbr`).

**My own part in this, recorded because it made things worse before it made them better:** the 2026-09-26 status-vocabulary pass in this branch saw the fragment as a bean with status `''` and SYNTHESISED front matter onto it — `title: ""`, `status: todo`, `created_at: 2026-09-26T09:57:34Z`. That turned a headless fragment into a valid-looking live todo with an empty title which then SHADOWED this bean, because `beans update qou-xdwp` resolves the id to that file. The body below is therefore taken from `origin/main`, not from the working tree, so none of that fabricated front matter is carried over.

---



## 🟩 BOTH architectural blockers are resolved — verified at the files (2026-09-13, bean qou-g5sp)

Both files compile: `vertex-operator.lean` and `categorical-transfer-matrix.lean`
are `exit 0`, 0 errors in the 938-target content sweep on `main` `16ccc3f7e2`
([`2026-09-13-every-content-sibling-compiles-zero-red.md`](../docs/audits/2026-09-13-every-content-sibling-compiles-zero-red.md)).

**But this bean is explicit that a compile fix is not what it was tracking** —
it separates its four mechanical fixes from "still open — architectural, one
each". So the compile result alone would not close it. Both architectural items
were checked **in the source**, not taken from `qou-e7xv`'s account of having
fixed them; AGENTS.md: *"a sibling's bean is not a primary source either."*

**`vertex-operator.lean` — "`ReebBundle` is not in scope", declared in another
content-block sibling this file structurally cannot import.** Resolved by the
route this bean listed as an option, and by the safer one: `ReebBundle` is
carried as a **type parameter `B`**, not promoted into the Lake library. The
file's own docstring at lines 45–59 records exactly the hazard this bean
predicted would bite on a naive promotion — `structure ReebBundle (q : ℝ)` is
archimedean while this file is categorical over `R_q = ℤ[q, q⁻¹]` — and names
`B := ReebBundle q₀` as the instantiation *after* the τ functor. That is the §7c
wall respected rather than crossed.

Separately: `ope_is_skein` is a **`theorem`** at line 102. This bean recorded it
as a bare `axiom`.

**`categorical-transfer-matrix.lean` — "an undetermined implicit",
`base : ExceptionalDivisor` not a parameter of the structure.** Resolved the same
way, a type parameter `B`, with the rationale at lines 84–89.

**And the axiom question this bean asked to settle in the same pass, was.** Its
closing flag: *"the declaration this blocks is `axiom
transfer_matrix_level_independence` … so this file wants the axiom question
settled at the same time, not two passes."* The file now carries
`level_independence_false_as_stated` at line 153 — a **refutation**, the axiom
was FALSE as stated — and `transfer_matrix_level_independence` as a **`theorem`**
at line 183. One pass, as asked.

Both items closed, both verified at the source. Status → completed.
