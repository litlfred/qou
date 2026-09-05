/-!
# QOU.BraidsAndKnots.WignerSu4FromSpinIsospin — vacuous duplicate; see the correction below

**Sibling-resolution stub** for content block
[`conj:wigner-su4-from-spin-isospin`](wigner-su4-from-spin-isospin.md): *D11 Wigner SU(4)*.

## 🛑 This header was wrong on three counts — corrected 2026-09-05

It previously said the axiomatisation *"lives at
`../lean/QOU/BraidsAndKnots/WignerSU4FromSpinIsospin.lean` … (file pending)"* and that
the `.ts` ref is `qou:QOU.BraidsAndKnots.WignerSU4FromSpinIsospin`. All three parts
were false, and they pointed in three different directions:

* **that path does not exist** anywhere in the tree;
* the `.ts` actually refs `qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin` —
  lower-case `u`, which is the class declared *below*, not the one the header named;
* the axiomatisation is **not pending**. A substantive D11 carrier already exists at
  [`../lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean`](../lean/QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean)
  (`namespace QOU`, imported at `QOU.lean:421`), carrying two real
  parameter-quantified fields — `dynamic_capacity_from_plancherel_weight`
  (`E_gate = E_0 · log (1 / W_λ)`) and `dynamic_occupancy_c_lambda`
  (`c_λ = B_AME / E_gate`) — alongside three `: True` fields that each carry an
  `opaque marker` docstring naming why they are unstatable.

**So the class below is a vacuous duplicate of a carrier that is not vacuous.** Do
**not** repair it by writing the conjecture's content into it, the way D9
(`IsospinFromCanonicalBowtie`, #6671) and D10 (`SpinFromSo3Fiber`, #6683) were
repaired — that would create a second D11 carrier competing with the real one. The
defect here is the **ref**, not the encoding.

Bean `qou-tsnp` lists this carrier among its twelve; that listing is correct about the
syntax and wrong about the required action, and is corrected there. The ref repoint
(and whether to align the library class's namespace so §0a candidate-2 resolution
works) is left as an author decision — measured blast radius is **zero consumers** on
both classes. Full finding:
[`docs/audits/2026-09-05-d11-is-a-mis-ref-not-a-vacuous-carrier.md`](../../../docs/audits/2026-09-05-d11-is-a-mis-ref-not-a-vacuous-carrier.md).

The class instance is the **conjectural witness** (sorry = conjecture per AGENTS.md
§3b), not a missing proof; downstream theorems take the carrier as an explicit
`[Instance]` hypothesis. This stub satisfies the lean-ref sibling-resolution rule
(AGENTS.md §0a step 1) for the `.ts` manifest's
`lean.ref = "qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin"`.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/wigner-su4-from-spin-isospin.ts
-/

namespace QOU.BraidsAndKnots

/-- **CONJECTURE.** Wigner $\\mathrm{SU}(4) = \\mathrm{SU}(2)_S \\times \\mathrm{SU}(2)_I$ as the categorical source for nuclear-shell binding (L3) -/
class WignerSu4FromSpinIsospin where
  holds : Prop
  -- Ref: [manuscript] conj:wigner-su4-from-spin-isospin

end QOU.BraidsAndKnots
