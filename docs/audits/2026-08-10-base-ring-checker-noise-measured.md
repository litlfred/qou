# `wall-base-ring-minimal` — 32 % of the axis is checker noise, measured

**Date:** 2026-08-10
**Branch:** `claude/agent-4886-completion-1ejh60` (follow-up to
[PR #4886](https://github.com/litlfred/qou/pull/4886))
**Bean:** `qou-z8m9`

## Result

The `wall-base-ring-minimal` axis reads **146 warn files / 563 hits** on the
current corpus. Two checker defects — both *identified* in PR #4886 but never
*quantified* — account for **43 files / 181 hits (32.1 % of all hits)**. The
real worklist is **103 files / 381 hits**.

| scoring | files | hits | skipped as archimedean |
|---|---|---|---|
| current checker | 146 | 563 | 0 |
| + fix 1 (gate bare-`⁻¹` on `ALGEBRAIC_LEAN_RE`) | 117 | 435 | 0 |
| + fix 2 (broad `ARCHIMEDEAN_TYPE_RE` for the skip) | 114 | 443 | 32 |
| **both fixes** | **103** | **381** | **32** |

Attribution of the 181 dropped hits:

| defect | files | hits |
|---|---|---|
| bare-`⁻¹` matched on a **group** inverse in a file with no ring | 11 | 61 |
| ℝ-typed file **not** skipped because it avoids `Real.*` | 32 | 120 |

The two largest entries on the axis are both noise, which is why this was worth
measuring before dispatching a swarm:

| was | file | why it is not work |
|---|---|---|
| 29 | `lean/QOU/Machinery/CoxeterReflectionCocycle.lean` | `Inv` on a Coxeter group / `Equiv.Perm`, ℤ/2-valued group cohomology, **no ring in the file at all** (`FIELD=0`) |
| 25 | `predicted-spectra/bloch-group-quotient-construction.lean` | ℝ-typed, but avoids `Real.*`, so the archimedean skip never fires |
| 14 | `predicted-spectra/bar-apply-transfer.lean` | same — all 14 hits are this one cause |
| 10 | `lean/QOU/BraidsKnots/RamifiedDiscFusion.lean` | group inverse |
|  9 | `lean/QOU/AppendixSurreals/BlowupCalculus.lean` | ℝ-typed, no `Real.*` |

## The two defects

Both live in `folio-assistant/content/pipeline/qa-checkers-voice.ts`.

### 1. `RING_INV_RE` matches group inverses

```ts
const RING_INV_RE = /⁻¹/;
```

The call site excludes `↑` / `Rˣ` / `Units` (the target division-free pattern),
but nothing distinguishes a **ring** inverse from a **group** inverse. In a
group-cohomology file `g⁻¹` is not a division at all, and there is no base ring
to minimise.

Minimal fix: gate the bare-`⁻¹` branch on `ALGEBRAIC_LEAN_RE`, which is already
defined in the same module —

```ts
const ALGEBRAIC_LEAN_RE = /\b(CommRing|Field|GroupWithZero|\{R : Type\*\}|\(R := |variable \{R\b)/;
```

— and is already `false` on `CoxeterReflectionCocycle` / `true` on
`bloch-group`. Measured effect: **−61 hits across 11 files**, no survivor loses
a genuine hit (every dropped file goes to exactly 0).

### 2. The archimedean skip uses the narrow regex

```ts
const ARCHIMEDEAN_LEAN_RE =
  /\b(Real\.sqrt|…|\(ℝ\)|: ℝ\b|: Real\b|LinearOrderedField)\b/;   // used by checkBaseRingMinimal
const ARCHIMEDEAN_TYPE_RE = /ℝ|\bReal\b|LinearOrderedField/;      // used by checkWallSide
```

`\b` adjacent to the non-word character `ℝ` cannot fire on the common spaced
Lean forms (`(x : ℝ)`, `→ ℝ`, `ℝ³`), so an ℝ-typed file that happens not to
call `Real.*` is scored on an axis it should be **skipped** on — §7c is explicit
that a field is legitimate post-wall.

The corrected `ARCHIMEDEAN_TYPE_RE` already exists in the same module and is
already used by the sibling checker `checkWallSide`. So the two wall checkers
currently **disagree about what "archimedean side" means** — that disagreement
is the defect, not the regex in isolation. Measured effect: **32 files skip,
−120 hits**.

## Why this was measured before the swarm, not after

AGENTS.md §"Formalize-first probe discipline" asks for a structural prune before
a wide search. Dispatching agents across all 146 files would have spent roughly
a third of the swarm's budget on files where **there is nothing to fix** — and
worse, an agent under instruction to reduce a hit count on
`CoxeterReflectionCocycle` would have been pushed toward inventing a ring
structure for a group-cohomology file to satisfy a regex. That is the failure
mode the anti-laundering rules exist to prevent, arrived at honestly.

The prune cost one re-scoring pass. It removed 181 hits of false work.

## Status of the fix

`folio-assistant` is a **separate repository**; this session's GitHub scope is
`litlfred/qou` only, so the checker fix cannot be pushed from here. Both fixes
are one-line, both reuse constants already defined in the same module, and the
numbers above give the expected delta to verify against.

Reproduce with [`scripts/check-base-ring.ts`](../../scripts/check-base-ring.ts):

```bash
bun run scripts/check-base-ring.ts --sweep content/quantum-observable-universe \
  --json /tmp/base_ring_worklist.json
```

Note the sidecars record only a verdict, never a hit count, so the axis could
be *read* before this script existed but not *worked*: there was no way to get
a prioritised list or to confirm a de-specialisation moved the number.

## Outcome of the round the prune enabled

The 8-agent swarm ran against the 103-file worklist, not the 146-file one:

| | files | hits |
|---|---|---|
| worklist in | 103 | 381 |
| worklist out | 48 warn (55 cleared) | **132** |

−65 % of hits, 55 files fully to zero. Per batch, summing exactly to 132:

| B7 | B6 | B4 | B2 | B5 | B8 | B3 | B1 |
|---|---|---|---|---|---|---|---|
| 47→2 | 47→8 | 48→10 | 48→14 | 48→17 | 47→18 | 48→23 | 48→40 |

The change is one shape throughout: `[Field R]` → `[CommRing R]` with the
inverted element carried as a unit (`q : Rˣ`, `↑q⁻¹`), `field_simp`
replaced by `linear_combination` or an explicit `Units.inv_mul` witness,
and `/2` by `⅟(2:R)` under `[Invertible (2:R)]`. Several results came out
**strictly stronger**: non-vanishing hypotheses disappear into the types
rather than being assumed.

**Two batches returned counterexamples instead of edits**, which is worth
more than the hits they would have cleared:

- `partialProduct_succ` cleared to `(1 − xqⁿ)·Φ_{n+1} = Φ_n` is **false**
  without a non-vanishing hypothesis — at `1 − xqⁿ = 0` the LHS is `0`
  while the RHS need not be. Clearing it would have *added* a hypothesis
  to satisfy a regex.
- `toroidal_locus_forced` over bare `CommRing` fails in `ℤ[1/2] × ℤ[1/2]`
  at `α = (−1/2,−1/2)`, `β = (−3/2,1/2)`. `IsDomain` is the honest floor;
  the same shape (`ZMod 6`, `q = 5`) pins it in `categorical-dq-squared`
  and `yekutieli_leading_coefficient`.

Both are recorded in the files' own docstrings so a later agent does not
retry them.

A **fourth** checker defect surfaced during the round and is worth adding
to the list above, though its blast radius on this axis is small:
`ARCHIMEDEAN_LEAN_RE` still tests for the token `LinearOrderedField`,
which is no longer a Mathlib class — the modern spelling is
`[Field R] [LinearOrder R] [IsStrictOrderedRing R]`. 271 `.lean` files in
`content/` use `IsStrictOrderedRing`, but only **3 files / 4 hits** of the
true worklist are affected, because most such files already trip the
narrow regex via `Real.*` and skip anyway. (An agent initially reported
this as "39 content files"; that figure is corpus-wide, not axis-relevant.)

## A third finding, incidental

`resolveCanonicalLean` accepts an optional `LakeTreeCache` "for bulk" callers.
Without it, the basename map and decl→file scan of the whole Lake tree are
rebuilt **per block**. The first sweep was killed at 15 minutes having emitted
nothing; with one shared cache it completes in well under a minute.

`scripts/check-wall-side.ts --sweep` also omits the cache and will have the same
problem at corpus scale.
