import QOU.Hecke.Algebra
import QOU.Hecke.MarkovTrace

/-!
# QOU.Shared.MarkovTraceClaim — shared context for Markov-trace claims

A *Markov-trace claim* is any proposition that bundles a substrate
parameter `q`, a strand count `n`, an Iwahori–Hecke algebra
`H_n(R, q)`, and a Markov-trace instance, and then asserts some
identity about `tr_M(x)` for `x : H_n(R, q)`.

Per `local/lean-substantive-pass`, ~40 blocks in the QOU package
share this shape (Hecke / Wenzl-bridge / mass-formula /
spectral-sequence content).  This typeclass extracts the shared
structure so per-block claims only need to specify the substantive
identity.

**Usage**:

```lean
class MyBlockClaim extends QOU.Shared.MarkovTraceContext where
  -- block-specific data (Hecke element, etc.)
  T_w : A
  -- block-specific assertion
  claim_identity : markovInst.trace T_w = ...
```

Then the per-block theorem proves directly from `claim_identity`:

```lean
theorem my_block [ctx : MyBlockClaim] :
    ctx.markovInst.trace ctx.T_w = ... :=
  ctx.claim_identity
```

-- Ref: [leitner2026] braids-and-knots/markov-trace.md (shared)
-/

namespace QOU.Shared

universe u

/-- Shared context for any block whose claim involves a Markov trace
    on the Iwahori–Hecke algebra `H_n(R, q)`.  Bundles the coefficient
    ring, substrate parameter, Hecke algebra, and Markov-trace
    instance. -/
class MarkovTraceContext where
  /-- The coefficient ring `R`. -/
  R : Type u
  /-- Commutative-ring structure on `R`. -/
  ringR : CommRing R
  /-- Inverse function on `R` (needed for `q^{1/2} + q^{-1/2}` in the
      Markov parameter). -/
  invR : Inv R
  /-- The substrate parameter `q : R`. -/
  q : R
  /-- The strand count `n`. -/
  n : ℕ
  /-- The Hecke-algebra carrier `A = H_n(R, q)`. -/
  A : Type u
  /-- Ring structure on `A`. -/
  ringA : Ring A
  /-- `R`-algebra structure on `A`. -/
  algebraA : @Algebra R A ringR.toCommSemiring ringA.toSemiring
  /-- The Hecke-algebra typeclass instance. -/
  heckeInst : @QOU.Hecke.HeckeAlgebra R n q A ringR invR ringA algebraA
  /-- The Markov-trace instance on `A`. -/
  markovInst :
    @QOU.Hecke.MarkovTrace R n q A ringR invR ringA algebraA heckeInst

end QOU.Shared
