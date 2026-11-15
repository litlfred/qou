import QOU.BraidKnot.BringWPlaneMonodromy

/-!
# Fibre→observable passage as a Stokes / Gauss–Manin monodromy action (Riemann–Hilbert)

**Follow-up to** #3662 (gate de-opaqued) + #3677 (fibre residue); see
[`docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md`](../../../../../../docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md)
§1 (Riemann–Hilbert / Stokes) and §"three carriers" (3). **No fit, no physics claim.**

## What this file states

The passage that #3677 pinned — the colored-WRT vacuum row `bwS0Concrete = S_{0λ}·θ_λ^{f}` realizing the
Verlinde measure `W_λ = ‖S_{0λ}‖²` at the fibre root of unity `‖q‖=1`, versus its value at the
observable substrate `q₀>1` — is naively read as **analytic continuation** of a `q`-series from `‖q‖=1`
to `q₀`. That reading is wrong for this framework. The correct categorical framing (audit §1) is the
**Riemann–Hilbert / Stokes** one: the analytic continuation of the solutions of a linear `q`-difference
connection *is* its **monodromy** — "continue to `q₀`" becomes "apply the monodromy operator", a morphism
in a category, with no limits taken.

Concretely, the ribbon twist `θ_λ = q^{c(λ)}` (the framing datum that distinguishes fibre from
observable; #3662/#3677 twist, `KeystoneModularTwist.theta`) is a **monodromy eigenvalue** of the
Gauss–Manin connection whose unimodular `2×2` monodromy `M` is `BringWPlaneMonodromy.M`, with
characteristic (Cayley–Hamilton) relation the depth-2 recurrence kernel `x² − (tr M)·x + 1`
(`unimodular_two_recurrence`, `τ = tr M`). This file axiomatizes that single structural residue as a
content-bearing §3b class and derives its sorry-free consequences.

## Honest scope (§"Axiomatization is NOT a Proof"; §3b-tax)

This file **reframes** the fibre→observable passage in monodromy language and ties three corpus objects
into one eigenvalue picture:

* the #3662/#3677 twist `θ_λ` (here `theta`),
* its transpose / chirality law `θ_{λ'} = θ_λ⁻¹` (`KeystoneModularTwist.theta_conjugate`), recovered
  here as *"the other monodromy eigenvalue is `θ⁻¹`"* (unimodular ⇒ eigenvalue product `= 1`), and
* the `BringWPlaneMonodromy` trace `τ = tr M`, recovered here as `θ + θ⁻¹ = τ` (sum of eigenvalues
  = trace).

It does **not** prove the geometric identification — that `θ_λ` is an eigenvalue of the *actual* Seifert
Gauss–Manin `M` of `E = Bring/S₄` along the `S³/2I` fibration — which remains the open, owner-gated §3b
conjecture (`BringWPlaneMonodromy.is_seifert_gauss_manin`; narrow Subgoal-2 reversal #2503/#2524, now
under the general 2026-07-11 reversal). It **closes nothing**: it restates the surviving residue as the
Riemann–Hilbert statement *"continuation = the monodromy acts"*. The content-bearing class field `eigen`
is a genuine parameter-quantified polynomial equation in the *shape* of the claim (the characteristic
relation), not an empty marker or `: True`; the `τ` value is carried as the monodromy datum `tr M`, never
asserted equal to any specific number. §7c: base ring `ℝ` — this is the archimedean / observable side,
where `τ`, `θ` are real.

Refs:
- audit `2026-07-12-fibre-observable-categorical-not-analytic.md` (RH/Stokes framing of the passage).
- [deligne1970] Équations différentielles à points singuliers réguliers (Riemann–Hilbert / monodromy).
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (ribbon twist `θ_λ`).
-/

namespace QOU.BraidKnot.Keystone

/-- **The fibre↔observable passage as a Stokes / Gauss–Manin monodromy action (§3b class).**

CONTENT: the ribbon twist `θ_λ` — the framing that distinguishes the fibre value (`‖q‖=1`) from the
observable value (`q₀>1`) — is an **eigenvalue** of the unimodular monodromy `M`, i.e. it satisfies `M`'s
characteristic (Cayley–Hamilton) relation `x² − (tr M)·x + 1 = 0` with `τ = tr M`. This is the
Riemann–Hilbert statement that "continuation to `q₀`" *is* "apply the monodromy", not an analytic limit.

The single field `eigen` carries the residue as a parameter-quantified polynomial equation in the shape
of the characteristic relation of `unimodular_two_recurrence` — genuine content, discharged for a
concrete shape-witness but **open** for the actual Seifert `M` (`BringWPlaneMonodromy`). -/
class StokesMonodromyFraming (τ : ℝ) where
  /-- The `λ`-graded ribbon twist eigenvalue `θ_λ` carried on this block (the framing datum). -/
  theta : ℝ
  /-- **CONTENT.** `θ` solves the unimodular monodromy's characteristic polynomial
      `x² − τ·x + 1 = 0` (`τ = tr M`) — i.e. `θ` is a monodromy eigenvalue. This is the Cayley–Hamilton
      residue of `unimodular_two_recurrence`, evaluated on the eigenvalue `θ` rather than the operator. -/
  eigen : theta ^ 2 - τ * theta + 1 = 0

namespace StokesMonodromyFraming

variable {τ : ℝ}

/-- **The twist eigenvalue is nonzero.** From `eigen`: if `θ = 0` the characteristic relation collapses
to `1 = 0`. (Unimodularity forbids a zero eigenvalue — the eigenvalue product is the constant term `1`.) -/
theorem theta_ne_zero (self : StokesMonodromyFraming τ) : self.theta ≠ 0 := by
  intro h
  have he := self.eigen
  rw [h] at he
  norm_num at he

/-- **The other monodromy eigenvalue is `θ⁻¹`** — `θ⁻¹` solves the *same* characteristic polynomial.
Multiply `eigen` by `θ⁻²` and use `θ ≠ 0`: the two roots of the unimodular `x² − τx + 1` are `θ, θ⁻¹`
(product `= 1`). This is the Riemann–Hilbert incarnation of the transpose / chirality law
`θ_{λ'} = θ_λ⁻¹` (`KeystoneModularTwist.theta_conjugate`, #3662): **the transpose `λ ↦ λ'` supplies the
second monodromy eigenvalue.** -/
theorem theta_inv_eigen (self : StokesMonodromyFraming τ) :
    (self.theta)⁻¹ ^ 2 - τ * (self.theta)⁻¹ + 1 = 0 := by
  have hne := self.theta_ne_zero
  have he := self.eigen
  field_simp
  linear_combination he

/-- **The fibre/observable twist pair reconstructs the monodromy trace: `θ + θ⁻¹ = τ`.** Sum of the two
eigenvalues `θ, θ⁻¹` equals `tr M = τ`. From `eigen` + `θ ≠ 0`. This is the genuine, sorry-free bridge:
the twist pair `(θ_λ, θ_{λ'}) = (θ, θ⁻¹)` reconstructs the `BringWPlaneMonodromy` trace scalar `τ`. -/
theorem theta_add_inv_eq_tau (self : StokesMonodromyFraming τ) :
    self.theta + (self.theta)⁻¹ = τ := by
  have hne := self.theta_ne_zero
  have he := self.eigen
  field_simp
  linear_combination he

/-- **The eigenvalue product is `1`** (unimodularity at the eigenvalue level): `θ · θ⁻¹ = 1`. The
constant term `1` of the characteristic polynomial is `det M = 1` — the symplectic structure of `H¹(E)`
read off the roots. -/
theorem theta_mul_inv_eq_one (self : StokesMonodromyFraming τ) :
    self.theta * (self.theta)⁻¹ = 1 :=
  mul_inv_cancel₀ self.theta_ne_zero

end StokesMonodromyFraming

/-- **Bridge to the actual Gauss–Manin monodromy trace.** For any `BringWPlaneMonodromy` instance `mon`
(carrying the unimodular Seifert operator `M`, `tr M = τ`), a `StokesMonodromyFraming` at `τ = tr M`
reconstructs that trace from its twist pair: `θ + θ⁻¹ = tr M`. This states the fibre→observable passage
in monodromy language against the corpus's actual `M` — the categorical "`continuation = M acts`",
modulo the open geometric identification `mon.is_seifert_gauss_manin`. -/
theorem framing_reconstructs_monodromy_trace
    {is_seifert_gauss_manin : Prop}
    [mon : QOU.BraidKnot.BringWPlaneMonodromy is_seifert_gauss_manin]
    (self : StokesMonodromyFraming mon.M.trace) :
    self.theta + (self.theta)⁻¹ = mon.M.trace :=
  self.theta_add_inv_eq_tau

/-- **Non-vacuity — the shape-witness.** `τ = 5/2`, `θ = 2`: `2² − (5/2)·2 + 1 = 4 − 5 + 1 = 0`, so `θ = 2`
is a genuine root of the characteristic polynomial (its partner is `θ⁻¹ = 1/2`, and `2 + 1/2 = 5/2 = τ`).
This witnesses the *shape* of the class — it is **not** a claim that the actual Seifert `M` has trace
`5/2` (`τ ≈ 2.6424` is never fitted; the geometric identification is the open owner-gated object). -/
instance shapeWitness : StokesMonodromyFraming (5 / 2) where
  theta := 2
  eigen := by norm_num

end QOU.BraidKnot.Keystone
