---
# qou-1lb8
title: main is RED at QOU.Mathlib.Summary — triv_hecke/triv_wedderburn demoted to def, inferInstance left behind
status: completed
type: bug
created_at: 2026-08-24T15:00:40Z
updated_at: 2026-09-13T17:10:00Z
---

`lake build QOU` fails on origin/main (8367fafb26) at QOU/Mathlib/Summary.lean:100 — `failed to synthesize IwahoriHeckeAlgebra R 2 q`. Surfaced by /prepare-merge on claude/fivetwo-level7-ladder-numerators; inherited, not merge damage.

## The finding

`lake build QOU` **fails on `origin/main`** (8367fafb26):

```
✖ [5791/5797] Building QOU.Mathlib.Summary (4.0s)
error: QOU/Mathlib/Summary.lean:100:21: failed to synthesize
  IwahoriHeckeAlgebra R 2 q
```

Line 100 is inside `inventory_check`, whose proof term is
`⟨⟨inferInstance⟩, ⟨inferInstance⟩, ⟨inferInstance⟩, …⟩`.

## Cause

Commit **9a41a7ca57** — *"lean(HeckeAlgebra): demote triv_hecke and triv_wedderburn to `def` —
they discharged two chain steps globally"* — removed the two instances that those
`inferInstance` calls resolved against. `Summary.lean` was not updated in the same commit.

⚠ **Do not fix by handing `inventory_check` the trivial witnesses explicitly.** That would
reinstate precisely what 9a41a7ca57 removed, and it removed them for a stated reason: they
"discharged two chain steps globally", i.e. they were a vacuity. `inventory_check`'s
`Nonempty (IwahoriHeckeAlgebra R 2 q)` conjunct is asserting that a Hecke algebra structure
*exists* for arbitrary `R`, `q` — which, with the trivial instance gone, may simply no longer
be true at that generality. The right repair is a decision about what `inventory_check` should
claim, and it belongs to whoever owns the Hecke work, not to a passing branch.

## How it was found, and that it is inherited

Surfaced by `/prepare-merge` on `claude/fivetwo-level7-ladder-numerators` (the Roth arc), after
merging `origin/main` (420 commits). Confirmed inherited rather than merge damage:

- `Summary.lean` and `HeckeAlgebra.lean` are **byte-identical to `origin/main`** on the merged
  branch (`git diff origin/main -- <both>` empty);
- `Summary.lean`'s **82-module transitive QOU import closure has zero overlap** with the
  branch's seven changed `.lean` files (all Roth/Wronskian modules);
- `Summary.lean` itself did not change in `dd6565ba51..origin/main`, so the breakage arrived
  through its dependency.

## Why this keeps happening

Same shape as `qou-mnrd` (main red on its own float64 ratchet) and as the `lean-orphan-gate`
header's story of 37 modules silently ceasing to compile: **every workflow in this repo is
`workflow_dispatch`-only**, so nothing builds `main` unless a human or an agent asks. A
demotion from `instance` to `def` is exactly the change that breaks a distant `inferInstance`
and nothing local, which is what an unrun build is worst at catching.

The branch that found it is green in its own modules: all seven rebuilt with `.olean`s deleted,
exit 0, no errors, no warnings.


## 🟩 STALE — re-measured 2026-09-13, `QOU.Mathlib.Summary` COMPILES (bean qou-g5sp)

This bean has stood `in-progress` as a `bug` since 2026-08-24 asserting that
`main` is RED at `QOU.Mathlib.Summary`. It is not, and has not been for some
time.

**Measured**, on `main` `16ccc3f7e2`, quiesced container, `lean`-direct via
`scripts/lean-library-sweep.py --all --only-exact QOU.Mathlib.Summary`:

```
=== library sweep: 54 ok, 0 RED, 0 TIMEOUT + 0 UNVERIFIED, 0 skipped, 337s ===
  [54/54] ok   QOU.Mathlib.Summary
```

`--all` means **nothing is trusted**: every one of the 54 modules in the
closure was rebuilt from source into a hardlinked shadow, so this is not a
stale-olean green. The whole-corpus run the same day
(`docs/audits/2026-09-13-every-library-module-compiles-zero-defects.md`) reaches
the same verdict from the other direction — 2836 of 2836 modules judged, 0 RED,
`QOU.Mathlib.Summary` among them.

**The closure is 54 modules, not the 82 quoted above.** Different measure or
different date; recorded so the next reader does not treat the mismatch as a
missed module.

## The repair was the one this bean asked for, and someone made it

The bean's ⚠ said: do **not** fix by handing `inventory_check` the trivial
witnesses explicitly, because 9a41a7ca57 removed them as a vacuity; the right
repair is a decision about what `inventory_check` should claim.

`QOU/Mathlib/Summary.lean`'s own docstring now records exactly that decision:

> Conditional on `[IwahoriHeckeAlgebra R 2 q]` (§3b-cond): the trivial global
> `IwahoriHeckeAlgebra` instance was deliberately removed on 2026-08-23
> (anti-laundering — a content-free `carrier = PUnit` instance must not be
> fabricated to close it), so `Nonempty (IwahoriHeckeAlgebra R 2 q)` is honestly
> available only *given* the class.

So the `inferInstance` was not re-satisfied by refabricating the instance; the
claim was weakened to a conditional and the hypothesis moved into the signature.
That is the §3b-cond pattern, and it is the honest disposition.

The same docstring goes further than this bean asked, flagging
`GBFiltrationCollapsesAtE2 R` as the *remaining* instance of the same shape — an
unconditional instance whose only model is the trivial spectral sequence, so
`[GBFiltrationCollapsesAtE2 R]` would be free for every `R` and every downstream
result taking it as a hypothesis unconditional on a collapse nobody proved.

**🛑 And that paragraph of Summary.lean is itself STALE — I repeated it before
checking, which is the error this bean is about, one file over.** Measured on
`main` `16ccc3f7e2`:

- `QOU/Mathlib/SpectralSequence.lean:136` declares `def canonicalTrivial`, not
  `instance`. It was demoted on **2026-08-24** (bean `qou-fngs`), and its
  docstring says why in terms: *"that is exactly why this is a `def` and not an
  `instance` … it must now be supplied by hand."*
- A tree-wide grep for `instance.*GBFiltrationCollapsesAtE2` and
  `: GBFiltrationCollapsesAtE2` finds **no instance anywhere** — only the class
  declaration and that `def`.
- `inventory_check`'s own proof term is the demonstration: it discharges the
  `GBFiltrationCollapsesAtE2` conjunct with `⟨canonicalTrivial R⟩`, applied
  explicitly, while the `WedderburnIsomorphism` conjunct beside it still uses
  `inferInstance`.

So the vacuity was fixed three weeks before this bean was re-measured, and
Summary.lean's docstring — which even says *"Recorded rather than fixed here …
a scoped change and not a merge-time edit"* — was never updated when the scoped
change landed. The code below it was. Corrected in the same PR as this append.

This is worth more than the compile result. The stale reading is not merely out
of date, it is wrong in the direction that destroys work: it tells a reader that
live §3b-cond conditional results are unconditional-and-vacuous, which invites
deleting or weakening them.

## Why this bean outlived its subject

Its own "Why this keeps happening" section names the cause and it applies to the
bean as well as to the breakage: **every workflow in this repo is
`workflow_dispatch`-only**, so nothing re-runs the build that would have said
"this is green now" any more than it said "this went red". A bug bean whose
subject is a compile error has no closing signal in a repo with no automatic
build — it closes only when an agent happens to re-measure.

Status → completed. The `GBFiltrationCollapsesAtE2` vacuity noted above is a
separate subject and should get its own bean if it does not already have one.
