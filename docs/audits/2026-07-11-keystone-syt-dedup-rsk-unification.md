# Keystone SYT de-duplication + RSK-target unification

**Date:** 2026-07-11 · **Axis:** s5-so3-keystone / Identity-I infra (P1–P5) ·
**Trigger:** owner "1 2" (start RSK Tier-2 + advance another keystone gate) ·
**Follow-up to** [#3580](https://github.com/litlfred/qou/pull/3580) ·
**No fit; no closure.**

## The corpus-grep catch (a duplicate I introduced in #3580)

#3580 added `QOU/BraidKnot/YoungTableauStandard.lean` with its own
`structure StandardYoungTableau (μ : YoungDiagram)` + `fDim := Nat.card (…)`.
I grepped **Mathlib** (correctly finding no `StandardYoungTableau` there) but
**not the QOU tree** — which already carries the canonical type:

| Canonical (pre-existing) | PR | What it is |
|---|---|---|
| `QOU.Mathlib.StandardYoungTableau` | [#2871](https://github.com/litlfred/qou/pull/2871) | SSYT-refinement (`toSsyt` + `bijOn` onto `{1,…,|μ|}`); proves `row_strict`, `injOn_cells`, **a `Finite` instance** |
| `QOU.Mathlib.numStandardYoungTableaux` | #2871 | `#SYT(μ) := Nat.card (StandardYoungTableau μ)` |
| `QOU.Mathlib.partitionShape` / `dimSYT` | [#2879](https://github.com/litlfred/qou/pull/2879) | `Nat.Partition n → YoungDiagram`; `dimSYT p := numStandardYoungTableaux (partitionShape p)` |
| `QOU.Mathlib.RSKBurnsideHolds n` | #2879 | `∑_{p⊢n} (dimSYT p)² = n!` — **axiom (i) of Identity I** as a fully-defined `Prop` |

The canonical is strictly better: it proves `Finite (StandardYoungTableau μ)`
via an injective encoding, so `numStandardYoungTableaux` counts a genuinely finite
type; my `fDim` relied on `Nat.card = 0` for infinite types (harmless here but
weaker). **Fix (this PR):** `YoungTableauStandard.lean` now *reuses*
`numStandardYoungTableaux` / `partitionShape` / `dimSYT`, deleting the duplicate
`StandardYoungTableau` / `fDim` / `ydOfPartition` / `entry_lt_card`. It keeps only
the genuinely-new parts (no canonical equivalent): `SkewStandardYoungTableau` /
`fDimSkew`, `mu21`, `involutionNumber_pos`, the C8 corollary `c8_superexp`, and the
three cited-`sorry` RSK-family identities.

This is the §2a "reuse pass" / corpus-grep discipline applied after the fact — the
duplicate should have been caught before #3580 landed.

## The unification: one RSK engine for both keystone frontiers

The keystone has two open representation-theory frontiers. They share a single
Tier-2 engine:

- **Identity-I axiom (i)** = `RSKBurnsideHolds n` : `∑_λ (#SYT λ)² = n!` — the RSK
  correspondence `S_n ≃ Σ_λ SYT(λ)²`.
- **C8's three sorries** (`branching_two_one`, `skew_le_straight`,
  `sum_dimSYT_eq_involution`) are sibling RSK-family facts over the **same**
  `numStandardYoungTableaux`: the branching rule, skew↪straight injection, and
  RSK-for-involutions `∑_λ #SYT λ = I(k)`.

All four are corollaries of the Schensted/RSK bijection, which the pinned Mathlib
lacks entirely (no `Combinatorics.RSK`; recon 2026-06-26). Proving
`RSKBurnsideHolds` discharges Identity-I axiom (i); the same machinery discharges
the C8 sorries. So the C8 super-exponential frontier and the Identity-I general-`n`
frontier are **one** multi-session build, scoped as the P1–P5 program
([`2026-06-24-identity-i-plancherel-snrep-infra-program.md`](../scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md)).

## Corrected stale status (keystone doc)

`docs/coordination/s5-so3-keystone.md` line 40 claimed Identity I is "held as a
`def twoM`, multi-session infra fill." **Stale.** Actual state on main:

- **conditional-proved sorry-free** ([#2709](https://github.com/litlfred/qou/pull/2709), `PlancherelSnData` class);
- **unconditional for `n=3..12`** ([#2760](https://github.com/litlfred/qou/pull/2760), `decide` instances) — covers deuteron `n=3`, keystone `n=5`, defect sign-flip `n=7`;
- `def twoM` **eliminated** (`n144C_eq_twelve_plancherel` / `defect_closedform_plancherel`);
- per-partition `Σh²=Σc²+n²` (`sumSqHooks_eq_sumSqContents_add_sq`, all `n`) + JM core (`jm_identity_coeff_two`) sorry-free.

Only the **general-`n`** discharge (axioms (i)/(ii) for all `n`) is open. The doc is
corrected to match.

## Scope (STRICT)

Removes a duplicate type + corrects a stale note + unifies the RSK target. **No
fit, no scale, no wiring, no physics.** The RSK/JM proofs (`RSKBurnsideHolds` and
the C8 sorries) remain the open P1–P5 program. `lean`-direct verified.
