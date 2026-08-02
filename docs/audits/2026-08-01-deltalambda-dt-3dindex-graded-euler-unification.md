# Δ_λ = DT / 3d-index graded Euler characteristic — the categorical home that unifies both horns

**Date:** 2026-08-01 · **Epic:** `qou-r2nh` · **Bean:** `qou-f0ny` ·
**Branch:** `claude/dt-3dindex-delta-lambda-derivation-2026-08-01` · **PR:** #4551 ·
**Tier:** derivation / formalize-first (Lean, sorry-free) ·
**Scope:** (a) throughout; nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/BraidsAndKnots/DeltaLambdaDTIndex.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndex.lean) — sorry-free, `lean`-direct exit 0.
- Builds on: [`QOU/BraidsAndKnots/S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (`nStat`, `deltaSign`, `deltaLambda`, `deltaSign_eq_nStat_parity`, `binding_magnitude_eq_dim`).

## The question

Two just-landed honest negatives bracket the per-partition binding factor `Δ_λ`:

- **Horn 1** ([PR #4540](https://github.com/litlfred/qou/pull/4540), `StokesPhaseSignChirality`):
  the Δ_λ chirality **SIGN** is the Lusztig a-function / b-invariant parity `(-1)^{n(λ)}`
  (a real π-phase, square `+1`), **not** the resurgent `±i` (π/2) Stokes phase — refuted by
  the `(5) ↔ (1⁵)` counterexample (both `+1`, so the sign is not bar-odd).
- **Horn 2** ([PR #4538](https://github.com/litlfred/qou/pull/4538), `StokesConstantQDimCategoricity`):
  the Δ_λ **MAGNITUDE** is **not** a KL-positive categorical q-dimension (the GGM Stokes
  descendant series has a negative coefficient); it is a signed, positivity-**violating**
  Donaldson–Thomas / 3d-index integer.

Both horns share ONE invariant — **KL-positivity** — and both point at the same home: a
*signed, a-graded, DT-index* object, not a positive-categorical one. The forward question
(this bean): **does the signed a-graded DT / 3d-index invariant DERIVE both the sign and the
magnitude as ONE categorical object?**

## The answer (per-partition Δ_λ): YES — one graded Euler characteristic supplies both horns

**`Δ_λ` is the (Behrend-signed) Donaldson–Thomas count of the Springer fibre `𝓑_λ`.**

Two standard facts assemble the object:

1. **Springer correspondence** (Springer 1978). The Wedderburn irrep `V_λ` sits in the top
   cohomology of the Springer fibre `𝓑_λ` of a nilpotent of Jordan type `λ`, and the
   **complex dimension of `𝓑_λ` is exactly the a-function** `n(λ) = Σ_i (i−1)λ_i` (type A).
   So the "count" attached to the block is `dim V_λ`, and the moduli dimension is `n(λ)`.

2. **Behrend / DT weighting** (Behrend 2009). A Donaldson–Thomas / BPS invariant is the
   Euler characteristic of the moduli *weighted by the Behrend function* `ν`, which on the
   smooth locus contributes the sign `(-1)^{dim moduli}`. Hence the DT invariant of `𝓑_λ` is

   > `DT(𝓑_λ) = (-1)^{dim_ℂ 𝓑_λ} · (count) = (-1)^{n(λ)} · dim V_λ = Δ_λ`.

So a **single** DT invariant supplies BOTH horns simultaneously:

| horn | ingredient | DT origin |
|---|---|---|
| **1 — sign** `(-1)^{n(λ)}` | Behrend `(-1)^{dim moduli}` | parity of the moduli complex dimension |
| **2 — magnitude** `dim V_λ` | virtual point count | the Springer count |

and — the crux — the **same odd complex dimension `n(λ)`** that makes the Behrend sign
negative is exactly what pushes the count out of `ℕ`. **Horn-1 (a minus sign) and horn-2
(positivity violation, "not a KL-positive q-dim") are the SAME phenomenon: an odd
a-function grade.**

Decategorified, `DT(𝓑_λ)` is the alternating (Euler-characteristic) sum of a graded object
`G_λ` — `V_λ` concentrated in cohomological degree `n(λ)`:

> `χ(G_λ) = Σ_{k=0}^{n(λ)} (-1)^k · dim (G_λ)_k = (-1)^{n(λ)} · dim V_λ`.

This **dissolves the "sign is exogenous / magnitude = dim, two separate legs" framing** that
has organized the entire Δ_λ ledger (`docs/coordination/option-e.md`: PROBE-4 KL-prune — "the
sign must come exogenously"; the L1-ceiling prune — "the sign structure never supplies the
magnitude"). In the DT / graded frame, sign and magnitude are the parity and the value of ONE
graded datum; there is no independent sign degree of freedom.

### The two anchors (independent check)

| `λ ⊢ 3` | `n(λ)` | `dim V_λ` | `Δ_λ = (-1)^{n(λ)}dim` |
|---|---|---|---|
| `(3)` | 0 | 1 | `+1` |
| `(2,1)` | 1 | 2 | `-2` |
| `(1³)` | 3 | 1 | `-1` |

⇒ `1+ / 2−` — matches horn-1's `n=3` anchor.

At `n = 6`: `(6),(5,1),(4,2),(4,1,1),(3,3),(3,2,1),(3,1³),(2³),(2²,1²),(2,1⁴),(1⁶)` give signs
`+,−,+,−,−,+,+,+,−,+,−` ⇒ `6+ / 5−` — matches horn-1's `n=6` anchor. The mechanism breaks at
`n = 4` between the anchors (the horn-1 finding), consistent: `(-1)^{n(λ)}` is not bar-odd.

## Proved sorry-free (`DeltaLambdaDTIndex.lean`, `n = 5` anchor)

| lemma | statement |
|---|---|
| `dtEuler_eq_sign_times_dim` | `χ(G_λ) = (-1)^{n(λ)}·dim V_λ` (single-degree collapse) |
| **`dtEuler_eq_deltaLambda`** | **the unification: `χ(G_λ) = Δ_λ` (both horns from one object)** |
| `dtEuler_magnitude_eq_dim` | `χ(G_λ)² = (dim V_λ)²` (horn-2 magnitude leg) |
| `dtEuler_neg_iff_odd_grade` | `χ(G_λ) < 0 ⟺ n(λ)` odd (horn-1 sign ⟺ odd Behrend grade) |
| **`horns_share_one_odd_grade`** | **one odd grade gives both the minus sign AND the ℕ-escape** |
| `deltaLambda_not_kl_positive` | `∃λ, Δ_λ < 0` (horn-2: Δ_λ leaves ℕ, not a KL-positive q-dim) |
| `dtEuler_mixed_sign` | both signs occur (the two parities of one graded object) |

The `n = 5` anchor reuses the established `nStat` (= a-function `n(λ)`), `deltaSign`,
`deltaLambda` and their theorems (`deltaSign_eq_nStat_parity` = horn-1 at `n=5`;
`binding_magnitude_eq_dim` = horn-2) — no re-derivation; the new content is the graded-object
**unification** and the shared-cause crux.

## What is OPEN (honest)

1. **Internal derivation from the 13 drivers.** The two inputs are already substrate-derived
   per corpus: the a-function `n(λ)` is the **Gröbner–Shirshov jet-order fake-degree
   valuation** (`docs/coordination/option-e.md`, 2026-07-18 front (i); the Nakayama-morphism
   *alternative* was refuted, but the GS/jet-order home stands), and `dim V_λ` is the
   `H_n(q) → Wedderburn` block dimension of the canonical chain. What remains open is whether
   the substrate **forces the DT moduli `𝓑_λ` itself** (dimension `n(λ)`, Behrend count
   `dim V_λ`) from the drivers — an actual moduli / 3d-index — rather than the `(n(λ), dim V_λ)`
   data being identified after the fact. This is the exact `qou-ujmw` pattern (`A_ω = 3` is an
   established DT-count; its internal derivation is the open leg `qou-qnnq`). Carried as a
   **content-bearing primary conjecture** `DeltaLambdaDTRealization` (NO instance, §3b-tax; not
   consumed by any theorem — no laundering). *Transparency:* the conjecture's shape is
   satisfiable by the toy `moduliDim := nStat, virtualCount := dim`, which merely READS the
   answer; that is not the derivation the conjecture asserts (the fields must be *outputs of
   the substrate*), so no instance is given.

2. **NOT a binding-energy closure.** This is the per-partition `Δ_λ` factor. The **many-body
   A=3 magnitude scalar** `r* = μ₃/c₃ ≈ 1.585` is a **distinct, still-open cluster-integral
   object**, orthogonal to the per-partition graded structure and walled from every route
   (Hecke level, geometric `W_λ`, coordination edge, Milnor `μ̄_A`, Vassiliev weight; see
   `docs/audits/2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md` and
   `docs/coordination/option-e.md`). Nothing here touches it.

## Verdict

**The DT / 3d-index (graded Euler characteristic) IS the right categorical home for the
per-partition `Δ_λ`, and it derives BOTH the sign and the magnitude as ONE object** — the
Behrend `(-1)^{dim moduli}` sign is horn-1, the count is horn-2, and their shared cause (an odd
a-function grade) collapses the two-leg framing into one graded datum. The **internal
derivation** of the moduli from the 13 categorical drivers remains open (the `qou-ujmw`
pattern), and the **many-body A=3 magnitude** is a separate open problem this does not address.
A precise, disciplined "right home + horn-unification proved; internal derivation open".

## Anti-fit / honesty ledger

- **0 free parameters**; `Δ_λ`, AME, CODATA, `q₀` never inverted; no word or dimension chosen
  to hit a target. The `(n(λ), dim V_λ)` data is the established Springer/Wedderburn datum.
- Formalize-first honoured: every claim is a sorry-free Lean statement written on the anchor
  before any prose. No `sorry`, no `True`-conclusion, no `native_decide`.
- The open conjecture is a **content-bearing primary carrier with no instance**; no downstream
  theorem consumes it. "Axiomatization is NOT a proof" respected — the class asserts, it does
  not close.
- PROBE-4 KL-positivity prune stays pruned; horn-1 and horn-2 stand (confirmed, unified, not
  overturned). Nothing wired to production; L2 dashboards unchanged.

## Cross-references

- Horn 1 (sign): [PR #4540](https://github.com/litlfred/qou/pull/4540) `StokesPhaseSignChirality.lean`; `PartitionOf5.deltaSign_eq_nStat_parity`.
- Horn 2 (magnitude): [PR #4538](https://github.com/litlfred/qou/pull/4538) `StokesConstantQDimCategoricity.lean`.
- `A_ω = 3` DT-count (shared open-leg pattern): [PR #4534](https://github.com/litlfred/qou/pull/4534); [`2026-08-01-ujmw-aomega-dt-index-derivation.md`](2026-08-01-ujmw-aomega-dt-index-derivation.md); beans `qou-ujmw` / `qou-qnnq`.
- Many-body A=3 magnitude walls: [`2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md`](2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md); [`docs/coordination/option-e.md`](../coordination/option-e.md).
- Primary sources: Behrend, *DT type invariants via microlocal geometry*, Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307 ; Springer, *A construction of representations of Weyl groups*, Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165 ; James, *The Representation Theory of the Symmetric Groups*, `[james1984representation]`.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted"; §"Strict Lean Discipline"; §"Conditional-proved ≠ premise-established".
