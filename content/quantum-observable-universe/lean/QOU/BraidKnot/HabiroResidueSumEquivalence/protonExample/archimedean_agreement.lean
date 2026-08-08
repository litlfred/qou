import Mathlib.Tactic
import QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement

/-!
# QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample.archimedean_agreement — conjectural class

**§3b-cond class axiomatisation** for content block
[`conj:gs-archimedean-agreement-residue`](../../../../../mass-theory/gs-archimedean-agreement-residue.md):
*Archimedean agreement (proton instance): degree-48 Habiro trace at $u_0$*.

This is a **dependent conjecture** (§3b-tax): the proton specialisation of the
generic `archimedean_agreement`, with the Gröbner–Shirshov target fixed to the
proton GB mass `𝔪_GB(𝔭, q₀) ≈ 2.1225825095`.  It carries **no instance** — the
honest open state.

## Field schema — content-bearing (bean `qou-ffwk`)

For the proton braid `T_w(Z = 1, N = 0)`, the degree-48 Markov-normalised
Habiro polynomial trace evaluated at `u₀ = √q₀` (`traceEval`) agrees with the
proton GB mass to within `ε ≥ 0`:

$$ \bigl| T_{\mathfrak p}(\sqrt{q_0}) - 2.1225825095 \bigr| \le \varepsilon. $$

Parameterising by `(traceEval, ε)` with the proton mass baked in makes this a
genuine specialisation (not a re-parameterised copy of the generic), and it is
**falsifiable** — `archimedean_agreement 0 0` is uninhabited.  The
`to_generic` instance is the derived §3b-tax dependency edge: a proton witness
supplies the generic `archimedean_agreement` bound at the proton's target.

§7c: `ℝ` is genuinely required — the claim is the archimedean evaluation
`T_𝔭(√q₀)`.
-/

namespace QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample

/-- **§3b-cond hypothesis class** for `conj:gs-archimedean-agreement-residue`.

    Proton specialisation: the degree-48 Habiro trace at `√q₀` (`traceEval`)
    agrees with the proton GB mass `≈ 2.1225825095` within a tolerance
    `ε ≥ 0`.

    Conjectural class — see
    [`conj:gs-archimedean-agreement-residue`](../../../../../mass-theory/gs-archimedean-agreement-residue.md). -/
class archimedean_agreement (traceEval ε : ℝ) : Prop where
  /-- The tolerance is non-negative. -/
  tol_nonneg : 0 ≤ ε
  /-- The proton Habiro trace agrees with the proton GB mass within `ε`. -/
  agree : |traceEval - 2.1225825095| ≤ ε

/-- **Derived specialisation edge** (§3b-tax dependent → generic): a proton
    agreement witness supplies the generic `archimedean_agreement` bound with
    the GB target fixed to the proton mass.  No fabrication — it consumes the
    proton hypothesis. -/
instance to_generic (traceEval ε : ℝ) [h : archimedean_agreement traceEval ε] :
    HabiroResidueSumEquivalence.archimedean_agreement traceEval 2.1225825095 ε :=
  ⟨h.tol_nonneg, h.agree⟩

/-! ## The proton carrier is content-bearing (falsifiability)

Theorems *about the class*, not instances of it — the proton conjecture
itself remains open (no instance below). -/

/-- **Exact agreement at zero tolerance**: at `ε = 0` the class pins the
    degree-48 Habiro trace to the proton GB mass exactly. -/
theorem eq_of_tol_zero {traceEval : ℝ}
    [h : archimedean_agreement traceEval 0] :
    traceEval = 2.1225825095 := by
  have := h.agree
  rw [abs_nonpos_iff, sub_eq_zero] at this
  exact this

/-- **The proton carrier is falsifiable**: `archimedean_agreement 0 0` is
    uninhabited, since the proton GB mass is nonzero.  (The replaced
    `residual = 0` schema was inhabited by `⟨0, rfl⟩` for every parameter.) -/
theorem not_agreement_zero_zero : ¬ archimedean_agreement 0 0 := by
  intro h
  have h0 : (0 : ℝ) = 2.1225825095 := @eq_of_tol_zero 0 h
  norm_num at h0

-- **No instance of `archimedean_agreement` is provided — the honest open
-- state** (AGENTS.md §3b-tax).  History: this file previously carried an
-- `axiom` + global `instance` (removed, PR #3793) and then a trivially
-- inhabited `residual = 0` placeholder; the schema is now refined to the
-- proton agreement bound (bean `qou-ffwk`).  A genuine instance requires a
-- derivation or a certified evaluation of the degree-48 trace, never
-- `⟨0, rfl⟩`.
end QOU.BraidKnot.HabiroResidueSumEquivalence.protonExample
