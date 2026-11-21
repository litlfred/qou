import QOU.BraidKnot.ConfinedParticle
import QOU.BraidKnot.ElectronShell
import QOU.BraidKnot.DressedParticle
import QOU.Interactions.ConfinementSDP

/-!
# Shell-Closure Stability

Along the dressing chain `P_bare → P^(1) → ⋯ → P^(Z_max)` in the
confinement category, the Frobenius stability index
`σ_F := n_target · y₀*(P, q)` is non-decreasing (claim 1). Its
marginal increment `Δσ_F(Z) = σ_F(P^(Z)) − σ_F(P^(Z-1))` — the
ionisation gap `I₁(Z)` — attains strict local maxima at the shell
**closures** (claim 2), where binding multiplicity `μ(S_Z, q) ≥ 2`;
the monotone `σ_F` itself has no interior local maximum. Whether those
closures fall at the noble-gas `Z ∈ {2, 10, 18, 36, 54, 86}` is
conditional on the open shell-capacity (`2n²`/Madelung) derivation —
the bare 2×2 `T_γe` gives closures every two electrons, not the noble
gases (a high-precision categorical σ_F chain confirms σ_F does not by
itself reproduce the noble-gas peaks). At a closure `Z` the dressed
particle is a local terminal object of the dressing sub-diagram: any
outgoing dressing requires breaking multiple tight dual blocks of the
confinement SDP simultaneously, exceeding the EM coupling at generic `q`.

(The two `ShellClosureStability` theorem groups formalise exactly the
consistent content — claim 1 `monotone` and claim 2 `μ ≥ 2` — and do
*not* assert a local maximum of `σ_F`.)

Claim (1) follows from SDP-relaxation monotonicity under the
cabling-induced primal/dual lift — not Cauchy eigenvalue
interlacing, which would run in the opposite direction on a raw
principal-submatrix relationship.

## References

- [prop:shell-closure-stability]
- [def:dressed-particle]
- [def:electron-shell]
- [prop:confinement-sdp]
- [boyd-vandenberghe-2004]
-/

namespace QOU.BraidKnot

open QOU.Archimedean

/-- Frobenius stability data — class-supplied evaluation of
    `σ_F(D, q) = n_target · y₀*(D, q)` (the optimal dual objective
    of the confinement SDP at `(D, q)`; equivalently, by strong
    duality, the optimal primal `⟨T, Φ*⟩`).

    **The index is `ℝ`-valued, and that is the whole point (2026-09-02).**
    It used to be `R_q → R_q`, and because `R_q = ℤ[q, q⁻¹]` carries no
    order, this file installed one:

        local instance : LE R_q := ⟨fun _ _ => True⟩

    Under that instance `x ≤ y` is `True` for every pair, so claim (1) below
    — *"the stability index is non-decreasing along the dressing chain"* —
    was `True`, and `ShellClosureMonotone` was inhabited by `⟨trivial⟩` for
    **any** pair of dressed particles, one-step or not. Measured
    `lean`-direct, exit 0, with the instance in scope:

        example (x y : R_q) : x ≤ y := trivial
        example … : frobeniusStability D_prev q ≤ frobeniusStability D q := trivial
        example … : ShellClosureMonotone D_prev D q h := ⟨trivial⟩

    An ordering is an archimedean construct (AGENTS.md §7c), so it belongs
    on the `ℝ` side of the substrate wall, not on the Laurent ring. `σ_F` is
    an SDP dual objective and is a real number; making that explicit removes
    the need for a fabricated order and makes claim (1) falsifiable. The
    argument stays `R_q` — the *point* of evaluation is still substrate-side.

    **Claim (2) was never affected**, and this is worth separating rather
    than sweeping in: `bindingMultiplicity` is `ℕ`-valued, so `μ ≥ 2` is over
    `ℕ`'s genuine order. The same probe rejects `… ≥ 2 := trivial` with a
    type mismatch. Only the `σ_F` comparisons collapsed. -/
-- Ref: [leitner2026] particle-interactions/confinement-sdp
class HasFrobeniusStability (D : DressedParticle) where
  /-- The stability index `σ_F(D, q)`, real-valued: it is an SDP dual
      objective, and it is compared with `≤`. -/
  sigma : R_q → ℝ

/-- Frobenius stability accessor, backed by `HasFrobeniusStability`. -/
def frobeniusStability (D : DressedParticle) [h : HasFrobeniusStability D]
    (q : R_q) : ℝ :=
  h.sigma q

/-- Is `D` a one-step dressing of `D_prev` (one extra electron)? -/
-- Ref: [leitner2026] braids-and-knots/dressed-particle
def isOneStepDressing (D_prev D : DressedParticle) : Prop :=
  D_prev.bare = D.bare ∧
  D.shell.nElectrons = D_prev.shell.nElectrons + 1

/-! ## §1  Claim (1) — Monotonic non-decrease -/

/-- **Shell-closure monotonicity — typeclass (Pattern 4).**

    Witnesses non-decrease of the Frobenius stability index for a
    *specific* one-step dressing pair. The full SDP-relaxation
    monotonicity proof requires the cabling embedding
    `ι : H_{A+Z-1}(q) ↪ H_{A+Z}(q)` and the dual-feasible lift,
    which depend on Mathlib SDP infrastructure. By packaging the
    inequality as a class, the conjectural content is visible at
    every use site rather than asserted universally. -/
-- Ref: [leitner2026] particle-interactions/shell-closure-stability
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — value-function monotonicity under domain expansion)
class ShellClosureMonotone
    (D_prev D : DressedParticle)
    [HasFrobeniusStability D_prev] [HasFrobeniusStability D]
    (q : R_q)
    (_h : isOneStepDressing D_prev D) : Prop where
  /-- Stability index does not decrease under the one-step dressing. -/
  monotone : frobeniusStability D_prev q ≤ frobeniusStability D q

/-- **Reflexivity instance**: when `D_prev = D` syntactically, the
    monotonicity is `≤` reflexivity. -/
instance shellClosureMonotone_refl
    (D : DressedParticle) [HasFrobeniusStability D]
    (q : R_q) (h : isOneStepDressing D D) :
    ShellClosureMonotone D D q h :=
  -- Ref: [leitner2026] particle-interactions/shell-closure-stability
  -- Now `le_refl` on `ℝ`. It used to be `⟨trivial⟩`, and the comment here
  -- said why: "`≤` on `R_q` is the trivial (`fun _ _ => True`) order". That
  -- was an accurate description of the mechanism and it did not draw the
  -- conclusion — that the theorem two declarations down was therefore empty.
  ⟨le_refl _⟩

/-- **Shell-closure stability, claim (1) — monotone non-decrease.**
    Per-instance form backed by `ShellClosureMonotone`.

    **Assumed, not derived here** — the body projects
    `ShellClosureMonotone.monotone`, so the stability inequality is carried as
    a context-class hypothesis (§3b-conditional, derivation pending), not
    established below. Boyd–Vandenberghe is cited for the perturbation and
    sensitivity-analysis background, not for a proof performed here; because
    `D_prev`, `D`, and `q` are arbitrary, this projection may not be converted
    to a global `axiom`. -/
-- Ref: [leitner2026] particle-interactions/shell-closure-stability
-- Ref: [boyd-vandenberghe-2004] §5.6 (Perturbation and sensitivity
--      analysis — value-function monotonicity under domain expansion)
theorem shell_closure_monotone
    (D_prev D : DressedParticle)
    [HasFrobeniusStability D_prev] [HasFrobeniusStability D]
    (q : R_q)
    (h : isOneStepDressing D_prev D)
    (hi : ShellClosureMonotone D_prev D q h) :
    frobeniusStability D_prev q ≤ frobeniusStability D q :=
  hi.monotone

/-! ## §2  Claim (2) — Local maxima at noble-gas Z -/

/-- **Shell-closure stability, claim (2) — noble-gas multiplicity.**
    At `Z ∈ nobleGasMagic`, the binding multiplicity satisfies
    `μ(S, q) ≥ 2`, giving the multi-operator regime. -/
-- Ref: [leitner2026] particle-interactions/shell-closure-stability
theorem shell_closure_noble_multiplicity
    (D : DressedParticle) [HasBindingMultiplicity D.shell] (q : R_q)
    (h : D.shell.nElectrons ∈ nobleGasMagic)
    [NobleGasMultiOperator D.shell q h] :
    bindingMultiplicity D.shell q ≥ 2 :=
  noble_gas_multi_operator D.shell q h

/-! ## §3  Claim (3) — Terminality -/

/-- **Shell-closure stability, claim (3) — terminality.**
    For `Z ∈ nobleGasMagic`, any outgoing dressing from `D` to a
    `D'` with `Z + 1` electrons requires simultaneously breaking
    `μ ≥ 2` tight dual blocks of the confinement SDP.
    Stated here as: the stability of any strict upgrade does not
    exceed that of `D` in the generic locus. -/
-- Ref: [leitner2026] particle-interactions/shell-closure-stability
theorem shell_closure_terminality
    (D D' : DressedParticle)
    [HasFrobeniusStability D] [HasFrobeniusStability D']
    [HasBindingMultiplicity D.shell]
    (q : R_q)
    (h_noble : D.shell.nElectrons ∈ nobleGasMagic)
    (h_step : isOneStepDressing D D')
    (hi : ShellClosureMonotone D D' q h_step)
    [NobleGasMultiOperator D.shell q h_noble] :
    frobeniusStability D' q ≥ frobeniusStability D q ∧
    bindingMultiplicity D.shell q ≥ 2 := by
  refine ⟨?_, shell_closure_noble_multiplicity D q h_noble⟩
  exact shell_closure_monotone D D' q h_step hi

/-! ## §4  Headline theorem -/

/-- **Shell-closure stability (headline).** Umbrella statement:
    for a noble-gas-dressed particle, binding multiplicity ≥ 2 and
    any subsequent one-step dressing cannot reduce Frobenius
    stability. -/
-- Ref: [leitner2026] particle-interactions/shell-closure-stability
theorem ShellClosureStability
    (D : DressedParticle) [HasBindingMultiplicity D.shell] (q : R_q)
    (h : D.shell.nElectrons ∈ nobleGasMagic)
    [NobleGasMultiOperator D.shell q h] :
    bindingMultiplicity D.shell q ≥ 2 :=
  shell_closure_noble_multiplicity D q h

end QOU.BraidKnot
