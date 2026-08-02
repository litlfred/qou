# Is "driver-14" (a Behrend-weighted DT moduli of the character variety) constructible from the QOU drivers? — independent cross-context verdict

**Date:** 2026-08-02 · **Branch:** `claude/driver-14-character-variety-dt-moduli-2026-08-02` · **PR #4601** ·
**Tier:** synthesis + formalize-first (independent parallel attack, per AGENTS.md
"Parallel exploration is valuable — cross-agent duplication is NOT waste").
**Scope (STRICT):** scope-(a) throughout; nothing fitted; nothing wired; no
bridge/DT-moduli axiomatized; L2 unchanged.

- Lean (new, machine-verified): [`QOU/QBeta/Driver14CharacterVarietyDTMenu.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/Driver14CharacterVarietyDTMenu.lean) — Mathlib-free core Lean, `lean`-direct **exit 0** (no olean dependency; fully machine-checked under the disk wall).

## The question

#4599 (`StokesDTCountExceedsRecursionOrder`, 2026-08-02) named the single missing
categorical input unifying the per-partition `Δ_λ` gap and the per-knot `A_ω`
gap: **"driver-14"** = a categorical construction, *from the substrate*, of the
**Behrend-weighted DT moduli of the character variety / BPS Hilbert space of
`T[K]`**. This note attacks the open-outcome question from an independent context:

> Can the QOU drivers (Hecke / Wedderburn / Frobenius / confinement-SDP /
> canonical-`T_w`) CONSTRUCT that moduli — or a usable fragment — even for the
> simplest case? Or is the Behrend weight / DT moduli irreducibly external?

**Verdict: irreducibly external.** Independent corpus-grep confirms the existing
negative from a second direction, sharpens *which* categorical input is missing
(a chirality-refined, set-valued count), and — the genuinely new result — shows
that the one partition-level fragment that *is* already derived does **not** move
the deuteron gate. Honest negative, as the owner expected.

## STEP 0 — what the corpus already establishes (grep, not reinvented)

The DT/character-variety obstruction is the *same* missing input at two levels,
and both levels are already sharply pinned on `main`:

| Level | object | QOU-derived | external (the residual) |
|---|---|---|---|
| **per-partition `Δ_λ`** | Springer fibre `𝓑_λ` DT | the **value** `Δ_λ = (-1)^{n(λ)}·dim V_λ` (sorry-free, all `n`: `DeltaLambdaDTIndexGeneralN`; `S5SO3FiberAction.deltaLambda = deltaSign·dim`, `deltaSign = (-1)^{nStat}`) | the **single-degree geometric concentration** `H^{2n(λ)}(𝓑_λ)=V_λ` — proved external Springer geometry (Rossmann-CC 2026-08-02): `y_λ` is the q-Plancherel measure, not a Green function; the substrate's only graded object is the *cancelling* fake degree (#4581) |
| **per-knot `A_ω`** | character variety `X(S³∖K)` / `T[K]` BPS | the spectral **curve** (`A_{4₁}`, proved `AJFigureEightAnnihilation`) and the Stokes-matrix **shape** (recursion order = `A`-poly `L`-degree) | the Behrend/BPS **count** (`3`; `{3,4}`) — geometric (exponential-network / triangulation), `> recursionOrder` (#4599) |

Three independent forcing routes at the partition level are PROVED-DEAD, unified
by #4581 under one **cancellation** mechanism: any graded substrate object that
realizes `Δ_λ` under signed-Euler is forced *cancellation-free* (single
grade-parity), but every algebraic grading the drivers produce (jet-order /
coinvariant / KLR-semisimple / Demazure) is a genuine two-parity multiplicity
space (the fake degree `f_λ(q)`), so `χ = f_λ(-1) ≠ Δ_λ`. Count (#4559), SDP
(#4570), valuation (#4574) all collapse to this. The one non-algebraic candidate
(Rossmann characteristic cycle, single-parity by construction) is gated on
**(IDENT)** — that `tr_M`'s archimedean evaluation is a Harish-Chandra invariant
eigendistribution whose Springer CC is single-parity — and the Green-function
corpus read proves (IDENT) is **not forceable** from the substrate weights.

At the knot level, the arc ledger
([`2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md))
records the literature verdict: KLW categorify the **colored Jones**, not the
3d-index / DT count; DGG give `{3,4}` from **triangulation**, not crystal/Hecke;
**no categorification of the q→0 DT count `{3,4}` from crystal/Hecke data appears
to exist.** It names the tractable, decidable, **still-UNCHECKED Route 1** as the
next probe: does a categorical count from Hecke/Bring reproduce `{3,4}`?

## The independent attack — Route 1, run to completion (formalize-first)

I ran Route 1 as a decidable cross-knot menu exclusion (the Lean file). The DT
datum is `4₁ ↦ 3`, `5₂ ↦ {3,4}` — where the `5₂` pair is **chirality-split**
(`4` in `S⁺(0)`, `3` in `S⁻(0)`; `FiveTwoDTSpectrumSplit`). Against it, the full
menu of natural knot integers:

| invariant (QOU-derivable unless noted) | `4₁` | `5₂` | hits DT? |
|---|---|---|---|
| Wedderburn block count (`H₃`, both 3-braids) | 3 | 3 | no |
| `|Σ_{λ⊢3} Δ_λ|` (partition Euler, #4599) | 2 | 2 | no |
| recursion order = AJ order = `A`-poly `L`-deg | 2 | 3 | no |
| crossing number *(classical control)* | 4 | 5 | no |
| knot determinant `|Δ_K(-1)|` *(classical)* | 5 | 7 | no |
| minimal ideal-tetrahedra *(classical)* | 2 | 3 | no |
| braid index *(classical)* | 3 | 3 | no |
| Seifert genus *(classical)* | 1 | 1 | no |
| **DT count (imported)** | **3** | **{3,4}** | — |

**Two machine-checked results** (`Driver14CharacterVarietyDTMenu.lean`, sorry-free):

1. `no_menu_invariant_hits_dt_vector` — no menu invariant has value-vector `(3,4)`
   over `(4₁,5₂)`. None of the natural scalar knot-integers reproduces the count.
2. `no_scalar_matches_chirality_split_datum` — **the deeper obstruction**: the
   `5₂` DT datum is a 2-element *set* (chirality-split), while every QOU scalar
   driver invariant is single-valued per knot; matching would force `4 = 3`.
   Hence the missing "driver-14" count is inherently a **chirality-refined,
   set-valued moduli count** — an object *outside the scalar-integer range of
   the 13 drivers*. This is the sharpened, formalized name of the missing input.

This is genuinely additive to prior work: #4599 tested 2 specific integers for
`4₁`; `FiveTwoDTSpectrumSplit` established the `5₂` chirality split; this file
runs the *whole menu* against the *cross-knot* datum and identifies the
obstruction as a **cardinality/chirality-refinement** mismatch, not merely a
per-knot numerical miss.

### The `dtMax = recursionOrder + 1` coincidence — recorded as a probe, NOT a law

The `dtMax` vector `(3,4)` equals `recursionOrder (2,3)` **plus 1** for both
knots. This is *not* asserted as a derivation and gets **no Lean theorem**:

- **2 knots always admit a linear fit** — the standing "single-knot
  count-matching is a trap" guard (#4534 audit) applies a fortiori to a
  two-point `y = x+1`.
- The `+1` has an *imported* geometric reading — the **abelian branch** of the
  character variety contributes one extra Behrend-signed point beyond the
  irreducible (geometric) components counted by the `A`-polynomial `L`-degree.
  That is exponential-network / DT geometry, **not** a QOU driver.
- **Decisive test (open):** a third knot. For `5₂` the *full* chirality-split
  datum is `{3,4} = {recursionOrder, recursionOrder+1}`, so a genuine law would
  have to predict *both* members and their chirality assignment — which
  `recursionOrder+1` alone does not. A `3₁` / `6₁` check is the honest next step;
  until then this is an unclaimed observation, mirroring #4599's treatment of the
  `−2` sandwich normalization.

## The 1ppq hook — derive-then-check on the deuteron (the new, useful negative)

**Expected value set BEFORE compute, from the already-derived fragment, no fit.**
The partition-level driver-14 fragment that *is* in hand is the Behrend-weighted
DT Euler characteristic itself: `Δ_λ = (-1)^{n(λ)}·dim V_λ`. Plugging the derived
`Δ_λ` (as `f^λ = dim V_λ`, chirality `sgn(w₀^{S_{λ'}})`) into the per-block
binding formula `B(K) = m_e·|Σ_λ y_λ χ^λ(β_K) Δ_λ|` gives, at the canonical q₀
([`binding_energy_categorical_deuteron.py`](../../computations/binding_energy_categorical_deuteron.py:15)):

    B(D) = 0.380 MeV  →  −82.9% vs AME (2.225 MeV).

The apparent "closure" needs `C_knot = B_AME/(m_e·|sum|) = 5.852`, which the
producer itself labels **FITTED, "not a derived geometric layer"**
([`:99`](../../computations/binding_energy_categorical_deuteron.py:99)).

**Consequence for driver-14.** Even the partition-level DT fragment that the
drivers *already* supply — the Behrend-weighted Euler characteristic `Δ_λ` — does
**not** move the deuteron gate: it is off by −82.9%, and the missing factor
`5.852` is a fitted deficit ratio, **not** any DT count (it is not `3`, not `{3,4}`,
not `recursionOrder`, not the Springer Euler total `−2`). So:

- A *constructed* driver-14 is **not established to close the deuteron** — the
  one derived fragment already fails it, and the residual is a different object.
- Conversely, the deuteron gap is **not** evidence that driver-14 is the missing
  binding ingredient. The Δ_λ-gate and the DT-count gap are *distinct* open
  problems that happen to share the "Behrend-weighted DT moduli" vocabulary.

This is a **scope-(a)** negative: `Δ_λ = (-1)^{n(λ)}dim V_λ` alone does not
reproduce `B(D)`; it does **not** exclude `Δ_λ` from a larger closure (a missing
multiplicative/interface term *re-weights* it — the standing "compositional object
is already many-body" caveat). Nothing is refuted structurally; the derived
value stands, it simply does not close the gate by itself.

## What IS internally derivable (the maximal QOU fragment — unchanged, restated)

1. `Δ_λ` **value** `= (-1)^{n(λ)}·dim V_λ` = per-partition DT/3d-index Euler
   characteristic (sorry-free, all `n`). A genuine categorical Behrend-signed
   count *value* from Wedderburn — but it does not close the deuteron (above).
2. The knot Stokes-matrix **shape** — recursion order = AJ annihilator order =
   `A`-poly `L`-degree (`4₁`: 2, proved; `5₂`: 3). Internally derived.
3. The sandwich **normalization** `−2 = Σ_{λ⊢3} Δ_λ` (single-knot, unclaimed).

## The irreducible residual (honest negative)

Driver-14 — the Behrend-weighted DT **moduli / count** of the character variety /
`T[K]` BPS Hilbert space — is **not constructible from the QOU scalar drivers**,
at either level:

- **partition level:** the missing input is the single-degree **concentration**
  (a variety's top cohomology), proved external Springer geometry, not reachable
  from the substrate's q-Plancherel measure + cancelling fake degree (Rossmann-CC,
  #4581, #4570, #4574).
- **knot level:** the missing input is a **chirality-refined, set-valued** DT
  count (`5₂: {3,4}` split across `S⁺/S⁻`), which no scalar Wedderburn Euler
  characteristic / recursion order / block count / classical knot integer supplies
  (this file, `no_scalar_matches_chirality_split_datum`). The count is the
  exponential-network / triangulation invariant of the spectral curve — geometric,
  not categorical-from-the-drivers.

**Named missing categorical input, sharpened:** a construction, *from the
substrate*, of a **chirality-graded moduli whose Behrend-weighted point count is
the character-variety DT spectrum** — the knot-level twin of the single-parity
Springer concentration Rossmann-CC proved external for `Δ_λ`. The DT/3d-index
*categorification* literature has not built this object (KLW categorify colored
Jones, not the 3d-index). It is a genuine literature frontier, not a QOU wiring
gap.

## Anti-laundering / honesty ledger

- **No DT moduli / bridge axiomatized.** No `Driver14`/`StokesDTBridge` class
  carrying a DT-count conclusion is landed. The output is the negative.
- **0 free parameters; nothing inverted; nothing wired.** DT counts `3`, `{3,4}`
  and all knot invariants are recorded imported/standard values, used only to
  prove the QOU scalars miss them. The deuteron `−82.9%` / `C_knot=5.852` are
  cited from the producer, which labels the fit as a fit.
- **`dtMax = recursionOrder+1` NOT wired, NOT a Lean theorem** — recorded as a
  2-point coincidence + imported-geometry reading needing a third-knot test.
- **Formalize-first honoured, machine-verified** (Mathlib-free core Lean,
  `lean`-direct exit 0 — no hand-audit needed; the file is deliberately
  olean-independent to clear the disk wall).
- **corpus-grep run before the "external" declaration** (Rossmann-CC / #4581 /
  #4570 / #4574 / option-e / the c₃-odd arc ledger / #4599 walked). Existing
  closed items not re-declared open; the negative is *confirmed and sharpened*,
  not manufactured.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring refuted"
  ((a)/(b) scoping used); §"Strict Lean Discipline"; §"Conditional-proved ≠
  premise-established" respected.

## Cross-references

- Unification / #4599: [`2026-08-02-stokes-dt-bridge-moduli-gap-unification.md`](2026-08-02-stokes-dt-bridge-moduli-gap-unification.md); [`StokesDTCountExceedsRecursionOrder.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesDTCountExceedsRecursionOrder.lean).
- Partition-level external verdict: [`2026-08-02-rossmann-cc-bridge-deltalambda-realization.md`](2026-08-02-rossmann-cc-bridge-deltalambda-realization.md); [`2026-08-02-deltalambda-graded-concentration-frontier.md`](2026-08-02-deltalambda-graded-concentration-frontier.md) (#4581).
- `5₂` chirality split: [`FiveTwoDTSpectrumSplit.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FiveTwoDTSpectrumSplit.lean); [`2026-08-02-fivetwo-crossknot-34-resolution.md`](2026-08-02-fivetwo-crossknot-34-resolution.md).
- Δ_λ value (proved): [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean); [`DeltaLambdaDTIndexGeneralN.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaDTIndexGeneralN.lean).
- Δ_λ gate / deuteron: [`option-e.md`](../coordination/option-e.md); [`binding_energy_categorical_deuteron.py`](../../computations/binding_energy_categorical_deuteron.py).
- Arc ledger (Route 1, literature verdict): [`2026-08-02-c3-odd-aomega-unification.md`](../coordination/2026-08-02-c3-odd-aomega-unification.md).
