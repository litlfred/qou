---
# qou-kyst
title: 'Discharging the keystone conjecture and its one vacuous premise'
status: todo
type: task
priority: medium
created_at: 2026-08-08T08:10:00Z
updated_at: 2026-08-08T08:10:00Z
---

The two things above the C1 chain that are open by nature rather than by
neglect. Beaned so they are not mistaken for oversights.

## 1. `conj:qdifference-kernel-prolongation-symbol` — class with no instance

`content/quantum-observable-universe/mass-theory/qdifference-kernel-prolongation-symbol.lean`
declares `class QDifferenceKernelIsProlongationSymbol (R) [CommRing R]` and
proves `kernel_is_prolongation_symbol` **from the class field**. There is no
instance anywhere. That is the honest open state for a `conjecture` block
(§3b-tax), not a defect — and `lean.validation: "validated"` is correct, since
the schema defines it as *"built and type-checked successfully"*, a build-status
field. (I flagged this as overstating on 2026-08-08 and retracted it; see
`qou-slpd`.)

**Discharging it means constructing an instance**, i.e. proving the kernel `R`
really is the jet-prolongation operator symbol. Per the block's own 2026-07-20
notes the GGM clause is already **refuted at module level** (Door-i), and the
owner re-scoping decision (F1 rewrite to R1 / F2 mark the GGM clause refuted /
F3 split) is **still open**. Nothing should be attempted on the Lean until that
framing call is made — otherwise the instance would be built against a statement
the corpus has already decided is wrong in part.

**Blocked on: an owner framing decision.** This is the one item in this cluster
that genuinely cannot be unblocked by reading a source.

## 2. `prop:mi-sw-abelianisation` — vacuous, and hard to fix

`QOU/BringsSurface.lean`:

```lean
theorem mi_sw_abelianisation (_bs) (n) (sw_period mi_integral : ℕ → ℝ)
    (fake_flat_abelian : ∀ k, mi_integral k = sw_period k) :
    mi_integral n = sw_period n := fake_flat_abelian n
```

Hypothesis is conclusion; the proof is a projection. Marked `validation:
"trivial"` on 2026-08-08 with an author note and a flag at the declaration.

Discharging it means proving the three steps of its own outline:

1. an SU(2) bundle over `S²` is trivial, so the connection abelianises to U(1);
2. fake-flatness `F_A = B` forces the 2-form datum into the Cartan subalgebra on
   the exceptional divisor `E_c`;
3. the MI integral then reduces to the classical contour integral of `λ_SW^(n)`.

**Realistic assessment: Mathlib cannot support this.** (1) needs principal
bundles and classifying spaces over `S²`; (2) needs nonabelian gauge theory and
Lie-algebra-valued 2-forms; (3) needs Yekutieli's nonabelian multiplicative
integration. None of that exists. The honest options are (a) leave it `trivial`
with the flag, which is where it is now, or (b) restate the block as a
*definition* or an explicit *premise* rather than a proposition, so the corpus
stops carrying a proposition whose Lean is a restatement. **(b) is an owner
call and is the cheap one.**

Relates: `qou-slpd`, `qou-c1ln`, `qou-c1wr`.
