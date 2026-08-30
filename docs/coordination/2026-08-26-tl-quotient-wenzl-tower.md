# TL quotient / Wenzl tower — coordination ledger

**Goal.** Discharge `QOU.Machinery.HeckeTower.WenzlTowerStep` at the Markov
trace, over the Temperley–Lieb quotient rather than over `H_n` — the route
opened when `qou-vndn` was refuted.

Bean: `qou-s7z2`. Predecessor: `qou-vndn` (**scrapped**, refuted). Sibling
theme: `qou-kzjl` (**completed**, retracted mid-flight).

## Session 2026-08-26 — bricks 1–4

All merged to `main`. Sorry-free, axiom-clean, guard rc=0 on 105 verified on
`main` as a whole after the fourth landed.

| brick | PR | commit | result |
|---|---|---|---|
| 1 | #5850 | `a65aeb1187` | the quotient exists as an **object** — `TwoSidedIdeal`, quotient ring, descended trace, nondegeneracy in `WenzlTowerStep`'s shape |
| 2 | #5852 | `ed17762163` | the braided presentation descends to the quotient |
| 3 | #5853 | `6f77b79f16` | the tower inclusion **detects** the radical ⇒ `TL_n ↪ TL_{n+1}` |
| 4 | #5855 | `7c50a8e917` | **negative** — a nondegenerate cyclic trace does **not** imply semisimplicity |

Notes worth carrying forward:

- **Brick 1's gap was concrete.** `traceRadical` was a `Set A` carrying only
  *multiplicative* closure. The three **additive** closures were absent because
  `TemperleyLiebTower` states the radical for a bare `tr : A → R` with `[Zero R]`
  — no addition on the target to close under. So `H_n / rad τ ≅ TL_n(δ)`, a
  phrase the corpus uses in several places, had **no referent in Lean**.
- **Brick 3 gave more than preservation.** Reflection holds too, because `ε`
  retracts `ι` and is therefore surjective. Preservation alone gives a *map* of
  quotients; reflection makes it **injective**, which is what makes the
  quotients a tower. Preservation spends `bimodule`, reflection spends
  `retract` — both fields of `HeckeConditionalExpectation` are load-bearing.
- **Brick 4 is the constraint on the sequel.** Brick 1 makes the class's
  nondegeneracy hypothesis *free* on the quotient, which looked like it should
  make the class easy. It does not: `ℚ[ε]/(ε²)` with `τ(a+bε) = b` is linear,
  cyclic, non-degenerate and not semisimple, and
  `traceRadical_epsCoeff_eq_bot` shows its radical is already `{0}` — so the
  quotient cannot repair it. Only the **regular** trace form `trace(L_{xy})`
  carries semisimplicity.
- **Conditionality.** Everything touching `HeckeConditionalExpectation` is
  §3b-cond: the class has **no instance**. Implications proved, premise not
  established.

## Open, and now the binding constraint

`HeckeGramFactorial`'s own open input — the general `T_w`-basis Gram
determinant, the classical Schur-element product formula. `n = 2` is done
(`H2CompanionRep.h2GramFromRep_det`). Bricks 1–4 moved this from a distant
obstacle to *the* obstacle.

**Blocked on a decision** (`qou-6a7w`, #5857): the content-block copy of the
Schur-element machinery is hollow — `wenzlSchurElement ≡ 0`,
`yLambdaWenzlBridge ≡ 0`, `hookDim` discards its partition argument — and it
**shadows** the real `QOU/MathlibExt/WenzlSchurElement.lean` via §0a candidate-1
resolution, under a `prop:` block. The general-`n` work must be built on the
library module, not the sibling.

## Scope map (2026-08-26 `/coordinate`)

| PR | relationship | posted |
|---|---|---|
| #5856 borrowed-name audit | **direct** — `qou-6a7w` is a worked instance of their detector shape; offered it as a fixture, plus two candidate detector rows (docstring-states-the-evasion; docstring/code disagreement) | [comment](https://github.com/litlfred/qou/pull/5856#issuecomment-5430187450) |
| #5826 zero-weight sector = TL ideal | **convergent, independent** — same object from the algebra side; brick 4 constrains their sequel | [comment](https://github.com/litlfred/qou/pull/5826#issuecomment-5430191054) |
| #5352 TL-arc proved/assumed ledger | **dependency** — their ledger moved in both directions since `9c6e9834cb` | [comment](https://github.com/litlfred/qou/pull/5352#issuecomment-5430194177) |
| #5337 Wenzl two-row cap under D | **adjacent** — offered the source-free convention test, flagged the scrapped-bean citation | [comment](https://github.com/litlfred/qou/pull/5337#issuecomment-5430196684) |

No §6 escalations: no sibling finding contradicts anything here.

## A reusable determinant fact

The closed-form `n = 3` Markov Gram determinant carries the factor
`((q²+1)z − q³)`, which **is the convention-D pin rearranged**. So D did not
perturb that determinant — it selected precisely its root. This is a complete
convention test needing no `z` grep, no `y_λ` input and no anchor.

## Two process failures this session, both recorded because they recur

1. **`qou-kzjl` duplicated a corpus theorem.** I greped *Mathlib* exhaustively
   and treated "Mathlib lacks it" as "the corpus lacks it". Checklist path 2 is
   `grep -rln <topic> content/` and I never ran it. A rigorous search of the
   wrong corpus produces *more* false confidence than a sloppy one.
2. **Overloaded names inflated a blast radius.** `hookDim` is defined in three
   files and `wenzlSchurElement` in two; two apparent consumers of the hollow
   stubs define their own real versions. A self-contained vacuity looked like
   spreading corruption until each was resolved to its declaration.
