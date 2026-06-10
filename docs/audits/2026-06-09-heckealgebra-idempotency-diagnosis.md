# HeckeAlgebra H₃(q) Wedderburn idempotency — root-cause diagnosis (LSP-verified)

**Date:** 2026-06-09. **Context:** the `Mathlib/HeckeAlgebra.lean` module was
repaired from 100+ errors to a residual proof tail in PR #2083 (structural /
import / timeout / namespace bitrot all fixed). This doc records the
**LSP-verified** diagnosis of the remaining `unsolved goals`, obtained after
unblocking the Lean LSP (toolchain linked under elan's pinned name; the
`release.lean-lang.org` firewall workaround per
`lean-environment-setup.md`).

## The remaining errors are a genuine math bug, not a mechanical gap

`H3WedderburnIdempotency_canonical` proves each Wedderburn projector is
idempotent via `unfold …; refine Prod.ext …; all_goals (field_simp; ring)`.
`field_simp` clears the `/qFactorial q 3` denominators (via `h_zne`) and the
`q⁻¹` denominators (via the newly-added `q ≠ 0`); `ring` then faces a
polynomial identity. The LSP goal states show those identities are **false**:

| component | goal after `field_simp` |
|-----------|-------------------------|
| `sym3` (0,0) | `1 + 2q² + 2q⁴ + q⁶ = qFactorial q 3` |
| `alt3` (0,0) | `1 + 2q² + 2q⁴ + q⁶ = q⁶ · qFactorial q 3` |

These two are **mutually contradictory** for a single value of
`qFactorial q 3`, yet `H3.blockSym3` and `H3.blockAlt3` divide by the **same**
`let z := qFactorial q 3`. So the two projectors cannot both be idempotent as
written.

### Two compounding convention errors

1. **balanced vs unbalanced `qFactorial`.** `sym3` idempotency requires
   `qFactorial q 3 = 1 + 2q² + 2q⁴ + q⁶ = (1+q²)(1+q²+q⁴)` — the **unbalanced
   Kauffman** factorial in `t = q²`. But the `qFactorial` the module resolves
   to (`QOU.MathlibExt.QPartitionCombinatorics.qFactorial`) is the **balanced**
   one, `[k] = (qᵏ−q⁻ᵏ)/(q−q⁻¹)`, giving `qFactorial q 3 = q³+2q+2q⁻¹+q⁻³ ≠
   1+2q²+2q⁴+q⁶`. So even `sym3` alone is false against this `qFactorial`.
   (Note: the original source referenced a bare `QOU.qFactorial` that **never
   existed** in namespace `QOU` — every `qFactorial` def lives in a
   sub-namespace — so the projectors were never checked against any concrete
   `qFactorial`.)

2. **`sym3`/`alt3` normalizer asymmetry.** `blockSym3` has q-power numerators
   `(1, q, q, q², q², q³)` and correctly wants `qFactorial(q)`; `blockAlt3` has
   q⁻¹-power numerators `(1, −q⁻¹, −q⁻¹, q⁻², q⁻², −q⁻³)` and needs
   `qFactorial(q⁻¹)` (the `q⁶·z` factor in its goal is exactly the `q ↦ q⁻¹`
   rescaling). Both currently divide by `qFactorial(q)`.

## Recommended fix (mathematical reconstruction — NOT a tactic tweak)

The correct H₃(q) Wedderburn idempotents need:
- a concrete **unbalanced Kauffman** `qFactorial` (`∏ (1 + q² + … + q^{2(k−1)})`,
  i.e. the q-factorial in `t = q²`) as the normalizer — defined in bare
  namespace `QOU` so both `HeckeAlgebra` and `WenzlBridgeConcrete` (which also
  references `QOU.qFactorial`) resolve it;
- `blockAlt3` normalized by that factorial **at `q⁻¹`** (or equivalently
  rescaled numerators);
- per-component **value lemmas** (`qFactorial q 3 = 1+2q²+2q⁴+q⁶`, …) rewritten
  in before `ring`, since `ring` treats `qFactorial` as opaque.

This is genuine representation-theory formalization (getting the idempotents
mathematically right), and the convention choice (Kauffman `t=q²` vs balanced)
is an authoring decision. **Deliberately not hacked to a green build** — forcing
`ring` to close by inlining whatever polynomial makes it pass would bake in
unverified idempotents.

## What landed alongside this doc
- `q ≠ 0` added to `H3WedderburnIdempotency_canonical` (genuinely required —
  closed the `1 − q·q⁻¹ = 0` component; it is also implied by `h_zne` since
  `qFactorial 0 3 = 0`).

## Separate residual (not part of the idempotency bug)
- `:1435` — an `H_4` Markov-trace `tr(β) = Σ …` identity (`mul_HnC4_tailored` /
  `embed_HnC3_to_HnC4`) that doesn't close; distinct from the idempotents.
- two `No goals` (`:387`, `:1133`) — trailing tactics after a closing `simp`.

## Resolution (2026-06-10, PR #2091)

Implemented on `claude/awesome-sagan-br883o`; `lake build
QOU.Mathlib.HeckeAlgebra` exit 0 (3088 jobs). All five errors above
are cleared.

- **Normalizer chosen: the S₃ Poincaré polynomial** `H3.poincare`,
  `P(q) = Σ_{w∈S₃} q^{2ℓ(w)} = 1 + 2q² + 2q⁴ + q⁶ = (1+q²)(1+q²+q⁴)`
  — equivalent to (and cleaner than) the "unbalanced Kauffman
  factorial in t = q²" recommended above, and related to the balanced
  factorial by `P(q) = q^{ℓ(w₀)}·[3]_q!` with `ℓ(w₀) = 3`. The
  rescaling `P(q)/P(q⁻¹) = q⁶` is exactly the `q⁶·z` factor in the
  alt3 goal. `blockSym3` divides by `P(q)`, `blockAlt3` by `P(q⁻¹)`.
- `P(q) ≥ 1 > 0` for all real `q` (`H3.poincare_pos`), so `h_zne` is
  dropped everywhere; only `q ≠ 0` survives (it clears the `q − q⁻¹`
  structure constants in `mulSigma`).
- Idempotency + orthogonality landed as four standalone theorems
  (`H3.blockSym3_sq`, `H3.blockAlt3_sq`, `H3.blockMixed21_sq`,
  `H3.blockSym3_blockAlt3_orthogonal`), each with its own heartbeat
  budget; `H3WedderburnIdempotency_canonical` just references them.
  (The original single `instance … where` shared one heartbeat budget
  across all 24 component proofs, which is what timed out.)
- The two `No goals` and the H₄ witness are also fixed — the latter
  was `simp` normalising the index to the `Fin` literal `6` while
  `h_six_one` was stated at `⟨6, ⋯⟩` (defeq bridge added).
- Tactic gotcha recorded: sequential `unfold A B C` does **not**
  revisit occurrences exposed by later entries in the list (this bit
  both `blockSum_first_component` and `blockMixed21_sq`, whose bodies
  re-expose `H3.add`/`H3.smul`); `simp only [defs]` unfolds to
  fixpoint and is order-independent.
