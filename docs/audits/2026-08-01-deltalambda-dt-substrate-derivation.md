# Δ_λ = DT-count of the Springer fibre — does the substrate FORCE the moduli? (OPEN, precisely bounded)

**Date:** 2026-08-01 · **Epic:** `qou-r2nh` · **Bean:** `qou-ylot` ·
**Branch:** `claude/deltalambda-dt-substrate-derivation-2026-08-01` ·
**Tier:** derivation / formalize-first (Lean, sorry-free) ·
**Scope:** (a) throughout; nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/BraidsAndKnots/DeltaLambdaDTModuliUnderdetermined.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTModuliUnderdetermined.lean) — sorry-free, `lean`-direct exit 0.
- Builds on: [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (`nStat`, `deltaSign`, `deltaLambda`, `deltaSign_eq_nStat_parity`, `binding_magnitude_eq_dim`) — all on `main`.
- Parent result: [`DeltaLambdaDTIndex.lean`](https://github.com/litlfred/qou/blob/claude/resurgent-bridge-deltalambda-dt-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndex.lean) (PR #4553) + its audit [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md).

## The question (the open crux)

The DT / 3d-index unification (PR #4553) proved sorry-free that the per-partition
binding factor is the Behrend-signed Donaldson–Thomas count of the Springer fibre
`𝓑_λ`:

> `Δ_λ = (-1)^{n(λ)} · dim V_λ = DT(𝓑_λ)`,

with the a-function grade `n(λ) = dim_ℂ 𝓑_λ` the Behrend `(-1)^{dim moduli}` sign
and the Wedderburn dimension `dim V_λ` the virtual count. That file honestly
carries the OPEN leg as a content-bearing primary conjecture
`DeltaLambdaDTRealization` (NO instance): **does the QOU substrate FORCE the DT
moduli `𝓑_λ` from the 13 categorical drivers, so that `Δ_λ` is its DT invariant —
or is the `(n(λ), dim V_λ)` data merely READ OFF `Δ_λ` after the fact?**

This is `bean qou-ylot`, the exact mirror of `qou-ujmw`/`qou-qnnq` for the
figure-eight Stokes integer `A_ω = 3` (PR #4534/#4554): "the DT-count
identification is established; the internal derivation from the drivers is the
open leg."

## Corpus / sibling state (grep + coordinate)

- **`Behrend` / `nilpotent orbit`**: absent from `content/`, `docs/`,
  `computations/` on `main` — introduced only by the unlanded PR #4553. No prior
  substrate-derivation attempt exists to duplicate.
- **`Springer`**: appears in the corpus only as incidental (publisher in
  `references.ts`; unrelated Lean file names). No Springer-fibre *construction*
  from the drivers exists.
- **Both numerical inputs are already substrate-derived** per the option-e ledger:
  the grade `n(λ)` is the **Gröbner–Shirshov jet-order fake-degree valuation**
  (= Lusztig a-function = b-invariant; `docs/coordination/option-e.md`, 2026-07-18
  front (i), "sign fully derived"), and `dim V_λ` is the `H_n(q) → Wedderburn`
  block dimension of the canonical chain. What is NOT derived is the geometric
  *moduli object* `𝓑_λ`.
- **Fake-degree q-dimension = hidden DOF** (option-e, 2026-06-28): the fake-degree
  ceiling is "wildly convention-dependent" (⁴He spans 0.41→5.62) — magnitude via a
  q-dim convention is NOT a derivation. Corroborates that the algebraic data does
  not pin a distinguished geometric realization.
- **Sibling coordination.** Distinct-angle intent posted on PR #4553 (parent) and
  PR #4554 (the `A_ω` mirror, `qou-qnnq`). #4554 independently reached
  "structurally-open — no QOU driver forces `3` by a short structural argument";
  this Δ_λ result converges to the same honest verdict by a different route (moduli
  under-determination), a second-direction confirmation.

## The derivation attempt — result: OPEN, sharply bounded

Attacking the crux as a structural argument yields a precise **limitative**
result: the `Δ_λ = DT-count` identification, *taken alone*, cannot force the
Springer moduli. Work with the realization predicate abstractly,

> `IsDTRealization md vc := ∀ λ, (-1)^{md λ} · vc λ = Δ_λ`

(`(md, vc)` = a (moduli-dimension, virtual-count) assignment reproducing `Δ_λ` as
a Behrend-signed DT count). Two sorry-free facts:

| lemma | statement |
|---|---|
| `canonical_dt_realization` | `(md, vc) = (n(λ), dim V_λ)` realizes `Δ_λ` (the Springer/toy reading) |
| `shifted_dt_realization` | `(md, vc) = (n(λ)+2, dim V_λ)` ALSO realizes `Δ_λ` — same Behrend sign |
| `dt_moduliDim_sign_forced` | with `vc = dim V_λ`, the Behrend sign `(-1)^{md λ}` is pinned to `(-1)^{n(λ)}` |
| **`dt_moduliDim_underdetermined`** | **two DISTINCT moduli dimensions (`n(λ)` and `n(λ)+2`) both realize `Δ_λ`** |

**Reading.** Matching `Δ_λ` constrains the moduli dimension **only mod 2** (its
Behrend-sign parity) and the count to `dim V_λ` — it never singles out the
Springer value `n(λ) = dim_ℂ 𝓑_λ`. So the `Δ_λ = DT-count` identity is a correct
categorical *home* but does **not** force the fibre `𝓑_λ`. The Springer dimension
`n(λ)` must therefore enter from an **independent** substrate map (the a-function /
GS jet-order valuation — separately corpus-derived), not from the DT-count
identification; and the geometric moduli object itself (a variety carrying a
Behrend function / symmetric obstruction theory) is **not** produced by the 13
drivers at all — only its numerical shadow `(n(λ), dim V_λ)` is.

### Why the geometric moduli is not needed for the value (reduction)

The landed `dtEuler_eq_deltaLambda` computes `Δ_λ` as the graded Euler
characteristic of the **algebraic** graded object `G_λ = V_λ` concentrated in
degree `n(λ)`. This is a graded vector space, not a moduli space — the Springer
fibre is one geometric *avatar* (Springer 1978: `H^top(𝓑_λ) = V_λ`), but the
alternating sign is supplied algebraically by the a-graded object. So "force the
DT moduli `𝓑_λ`" is the wrong target for the value; the right (weaker) target is
"force the single-degree graded object `G_λ`".

### The residual obstruction (what a genuine derivation still needs)

Even granting `V_λ` (Wedderburn, forced) and the grade `n(λ)` (a-function =
GS jet-order, separately corpus-derived), the **single-degree concentration** is
extra structure. The substrate's natural coinvariant grading spreads `V_λ` across
degrees `[n(λ), …]` per the fake-degree polynomial `f_λ(q)`, whose *signed*
evaluation is generically **not** `Δ_λ` — e.g. `λ=(2,1)`: `f_λ(q)=q+q²`,
`f_λ(-1)=0 ≠ -2 = Δ_{(2,1)}`. Getting `χ = Δ_λ` requires selecting **only** the
top / lowest-fake-degree piece (Springer's "top cohomology" choice). Whether the
confinement SDP / canonical `T_w` forces that top-degree selection is the precise
open sub-question. (Not formalized here — it needs the `n=5` fake-degree data;
carried as the next honest step, below.)

## Proved / open split

- **PROVED (sorry-free, this file):** the `Δ_λ = Behrend-signed DT-count` target
  under-determines the moduli dimension (forces only its parity + the count
  `dim V_λ`); the geometric fibre `𝓑_λ` is not singled out by matching `Δ_λ`.
- **OPEN (unchanged, now precisely bounded):** the internal derivation
  `DeltaLambdaDTRealization` — that the 13 drivers *force* a moduli `𝓑_λ` of
  dimension exactly `n(λ)` with Behrend count `dim V_λ`. The DT identity does not
  supply it; the a-function derivation supplies the *dimension* algebraically but
  not the *space*; the single-degree concentration (top-cohomology selection) is
  the residual structural ingredient the substrate has not been shown to force.

## Verdict

**OPEN, sharply bounded — not closed, not a read-off passed as derivation.** The
`Δ_λ = DT-count` identification is the right categorical home but is *limitatively*
insufficient to force the Springer moduli: it constrains the moduli only to
parity + count (proved). A genuine substrate-derivation would need (i) an
independent driver-map to the a-function grade `n(λ)` (partially in hand:
GS jet-order valuation) AND (ii) a substrate-forced single-degree concentration /
top-cohomology selection (open) — or, more ambitiously, a driver-internal
construction of a space with a symmetric obstruction theory whose Behrend-weighted
count is `Δ_λ` (absent). This mirrors, from a second direction, the `A_ω = 3`
"structurally-open" verdict (#4554).

## Anti-fit / honesty ledger

- **0 free parameters**; `Δ_λ`, AME, CODATA, `q₀` never inverted; no word or
  dimension chosen to hit a target. `(n(λ), dim V_λ)` is the established
  Springer/Wedderburn datum.
- Formalize-first honoured: the limitative claim is a sorry-free Lean statement.
  No `sorry`, no `True`-conclusion, no `native_decide`-laundering; base ring ℤ.
- **No instance of the open conjecture fabricated.** The proved content is a
  *limitative* fact (the target under-determines the moduli) — it does NOT close
  the open leg and does not launder it. "Axiomatization is NOT a proof" respected.
- corpus-grep run before the "open" declaration (all four paths empty modulo the
  originating PR #4553). "sorry-free ≠ derived" and "conditional-proved ≠
  premise-established" respected: the DT identity proves the *implication shape*,
  not the substrate premise.

## Next honest step (beaned under `qou-ylot`)

Formalize the concentration obstruction at `n=5`: encode the fake-degree
polynomials `f_λ(q)`, prove `Σ_λ`-level that the *full* coinvariant-graded signed
Euler characteristic `f_λ(-1)` differs from `Δ_λ` (so the single-degree selection
is load-bearing), then test whether the confinement SDP / canonical `T_w` forces
the top-degree projection. If it does → the derivation closes; if not → the
substrate under-determines the realization and the DT home stays an avatar.

## Cross-references

- Parent DT unification: PR #4553, [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md).
- `A_ω = 3` mirror (`qou-ujmw`/`qou-qnnq`): PR #4534 / PR #4554; [`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md).
- a-function = GS jet-order valuation, fake-degree hidden-DOF: [`docs/coordination/option-e.md`](../coordination/option-e.md) (2026-07-18 front (i); 2026-06-28).
- s5-so3 keystone (geometric `W_λ`, distinct from the Springer/DT route): [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).
- Primary sources: Springer, *A construction of representations of Weyl groups*, Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165 ; Behrend, *DT type invariants via microlocal geometry*, Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307 ; James, *The Representation Theory of the Symmetric Groups*, `[james1984representation]`.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring open"; §"Strict Lean Discipline".
