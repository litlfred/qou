# Milnor / Brunnian deficit arc — coordination ledger (qou-v7ro)

**Opened:** 2026-08-30 · **Bean:** `qou-v7ro` · **Goal:** close the ∀A nonvanishing of
`MilnorExactOrderConjecture` via the convention-D Brunnian trace-deficit recursion, and record how
`D_A` is consumed downstream.

## State

- **`D_{A+1}=−h²(h²+2)D_A` is PROVED ∀A** (merged #6217, `4540e25a35`) by TL structural induction —
  probe `computations/deltalambda/milnor_recursion_forall_A_proof_probe.py` (`all_verified: true`),
  audit `docs/audits/2026-08-30-milnor-recursion-forall-A-PROVED.md`. Closed form
  `D_A = (−1)^{A−3} h^{2(A−1)} (h²+2)^{A−3} (h²+3)/(h²+4)`, leading coeff `(3/4)(−2)^{A−3}`.
- **Field-algebra core Lean-formalized** (this branch): `QOU.MassTheory.DeficitRecursionReduction`
  proves `(I) + Q-recursion ⇒ D-recursion` sorry-free over a generic field.
- **`BrunnianDeficitRecursion` instance still NOT created** — the remaining Lean obligation is the
  two TL facts (identity (I) + the Q-recursion) for the concrete Markov trace; not fabricated.
- **Cap-cup weight correction that others must not miss:** the TL cap-cup contraction is `μ⁻¹`
  (`ptr_{μ⁻¹}(e)=1`; `ptr_μ(e)=diag(q⁻²,q²)`). Any TL Markov-trace compute in this arc should use it.

## How `D_A` is used downstream — two channels

1. **Mathematical (knot invariant) — now CLOSED.** `D_A`'s leading coefficient `(3/4)(−2)^{A−3}` is
   the length-A Milnor μ̄ order marker; the recursion ⇒ nonvanishing ∀A ⇒ `MilnorExactOrderConjecture`
   (via the merged `tight_slice_of_recursion`). Lean cone is small and self-contained:
   `BrunnianDeficitRecursion.lean` → `BorromeanA4TightSlice.lean` → `MilnorOrderLawGeneral.lean`.
   Siblings on the Milnor-order / Vassiliev-grading side (`MilnorVassilievGrading`,
   `MilnorParitySignLaw`, `MilnorWeightParityConvergence`) inherit a *proved* order law.

2. **Physical (many-body binding) — GATED, not a `D_A` consumer yet.** `D_A` is the convention-D
   Brunnian trace deficit of the A-body nucleon knot `w_A`. It supplies **structure** (which Milnor
   order, sign/parity), **not the binding magnitude**. A MeV number sourced from `D_A` would be a fit
   (open Δ_λ gate; the extensive-term frontier is `qou-brng`). So the mass/binding content blocks that
   mention "deficit" mostly mean the *binding-energy* deficit (negative-debt confinement), a different
   object — not `D_A`. **No live sibling directly consumes `D_A` as a numerical input.**

   **MEASURED, 2026-08-30 (`milnor_deficit_vs_binding_magnitude_probe.py`, mpmath dps=50, no
   float64, scope-(a)) — the "structure not magnitude" claim is now quantified, not asserted.** At
   the proton q₀ the deficit and the binding fraction have **opposite A-dependence**:
   - `|D_A|` **falls geometrically** — `D_3=1.44e-3, D_4=1.28e-4, …, D_8=8.2e-9` — by exactly the
     recursion factor `−h²(h²+2) = −0.0893226497` at *every* step (an independent reconfirmation of
     the proved recursion at the physical anchor), with sign alternating `(−1)^{A−3}`.
   - The empirical binding fraction `B/A/m_N` **rises** with A over the light range
     (`0.767 → 0.954·ℏ_q²`, ⁴He → ⁵⁶Fe) via the coordination count `z=A−1` (`qou-brng`,
     `binding=−log I`).

   Opposite trends ⇒ `D_A` cannot be the binding magnitude; it is the rapidly-decaying, sign-carrying
   Milnor order/parity marker. The magnitude lives in the `qou-brng` coordination free energy (proved:
   type question #6125, coordination coefficient + `binding=−log I` via `ArchimedeanTraceBridge`),
   whose only open pieces are two named modelling inputs (Markov-trace-as-amplitude; the
   `m=m_e·Vol·lw/ℏ_q²` dressing) — **the exact ℏ_q² saturated fraction is confirmed numerology**
   (`2026-08-30-brng-residuals-worked.md`), so it is not wired and not forced.

## Sibling coordination

- **#6183** (`claude/he4-magnus-a4-sign-sparse-2026-08-30`, A=4 ⁴He Magnus Ω₂ sign) — same Thread-A
  arc (deuteron A=2 `qou-dp32`, triton A=3 #6107). Works the **Magnus pairing** `Σ y_λ tr(ρΩ₂)`, a
  *different* functional from `D_A`. Posted one intent comment
  ([#6183 comment](https://github.com/litlfred/qou/pull/6183#issuecomment-5469086382)): D_A recursion
  is proved+available; flagged the two sign structures side by side (deficit alternates `(−2)^{A−3}`;
  their P is negative at A=2,3) **without** claiming a forced match. No file/method overlap; no action
  required on their side. **Not** added to my scope (parallel leg, not a dependency).

## Next (non-overlapping)

- Land the `DeficitRecursionReduction` Lean lemma (this branch).
- The genuinely-open remaining piece stays `qou-v7ro`: formalize the two TL premises in Lean
  (quantum trace + cap-cup + Markov) to discharge the instance. Large, mechanical; not started.
