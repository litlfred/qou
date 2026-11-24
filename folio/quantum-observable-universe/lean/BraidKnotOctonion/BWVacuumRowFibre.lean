import Mathlib.Analysis.Normed.Field.Basic

/-!
# The surviving residue of the keystone gate: `‖bwS0Concrete‖²` realizes `W_λ` at the fibre `‖q‖ = 1`

`BWVacuumRowConcrete.lean` (#3662) de-opaqued the keystone gate `bwS0_eq_hecke` by replacing the free
gauge field `bwS0` with the **concrete** Reshetikhin–Turaev / Seifert vacuum row
`bwS0Concrete = S_{0λ}·θ_λ^{f}`, and proved it equals the modular datum `S_{0λ}` **iff** the framing
twist is trivial (`θ_λ^f = 1`).  At the *observable / archimedean* real `q₀ > 1` the twist
`θ_λ = q₀^{c(λ)}` is a real power `> 1` — **not** a root of unity — so for the forced Seifert framing
`f ≠ 0` and any non-self-conjugate block (`c(λ) ≠ 0`) the gate is **REFUTED** (a scope-(a) negative for
*this construction at real q₀*, sharpened by the transpose-symmetry invariant there).

This file formalizes the **surviving residue** of that refutation — sorry-free, no fit, no physics
claim.  The framing obstruction that breaks the gate at real `q₀` is **exactly `‖q‖ = 1`-removable**:
at the **fibre root of unity** `‖q‖ = 1` (the pre-`τ` categorical level; AGENTS.md fibre-vs-observable
`q`), the twist `θ_λ = q^{c(λ)}` is a **phase** (`‖θ_λ‖ = ‖q‖^{c(λ)} = 1`), so the framing **cancels in
the squared modulus**:

`‖bwS0Concrete‖² = ‖S_{0λ}·θ_λ^{f}‖² = ‖S_{0λ}‖²·‖θ_λ‖^{2f} = ‖S_{0λ}‖²` — the Verlinde measure
`W_λ = S_{0λ}² = d_q²/D²` (`KeystoneVerlindeSMatrixBridge.verlindeMeasure`).

So **the geometric squared-amplitude realizes `W_λ` at the fibre** (`‖q‖ = 1`, framing-cancelled).  The
residue does **NOT** close the gate: the open object is the **archimedean continuation** `‖q‖ = 1 → q₀ > 1`,
where the cancellation fails (the contrast lemma `bwS0N_norm_off_unit`: at `‖q‖ = r ≠ 1` the framing
factor `r^{c·f}` survives unless `c·f = 0`).  This restates `bwS0_eq_hecke` and precisely **locates the
frontier** — it states the residue, it does not derive the physics.  The root-of-unity value of
`S_{0λ}` / `d_q` is carried as the datum `s0`, not asserted.

## Base ring (§7c)

A **generic normed field** `{K : Type*} [NormedField K]`.  A norm `‖·‖` is genuinely required (the
whole statement is about the modulus at `‖q‖ = 1`), so `NormedField` is the correct home — it supplies
`norm_mul` and `norm_zpow` (`‖a^{n:ℤ}‖ = ‖a‖^n`) with no ordering / `Real.sqrt` machinery.  Fresh,
minimal analogues (`thetaN` / `bwS0N`) are defined over `K`; the ℝ-only `VerlindeModularData` /
`bwS0Concrete` are **not** reused — over `ℝ` the twist is never a phase (`q₀ > 1` is a real power), so
the modulus statement has no content there; it lives at the fibre `‖q‖ = 1`, which needs a base ring
that admits roots of unity (e.g. `ℂ`), hence the generic normed field.

Refs:
- [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (`S`, `T` modular data).
- [beasleywitten2005] https://doi.org/10.4310/jdg/1143593746 — non-abelian CS localization.
-/

namespace QOU.BraidKnot.Keystone

variable {K : Type*} [NormedField K]

/-! ## Fibre-level analogues of the concrete RT/Seifert vacuum row -/

/-- **The ribbon twist over a normed field** `θ = q^{c}`, with the block content sum `c : ℤ` carried
as the datum (avoids re-deriving `contentSum`).  A `zpow` (the content sum may be negative). -/
def thetaN (q : K) (c : ℤ) : K := q ^ c

/-- **The concrete RT / Seifert vacuum row over a normed field** `bwS0N = s0·(θ)^{f}`: the S-matrix
vacuum entry `s0` times the ribbon twist `θ = q^{c}` raised to the Seifert framing `f : ℤ`.  The
normed-field analogue of `BWVacuumRowConcrete.bwS0Concrete`, at the fibre variable `q`. -/
def bwS0N (s0 : K) (q : K) (c : ℤ) (f : ℤ) : K := s0 * (thetaN q c) ^ f

/-! ## The twist is a phase at the fibre root of unity `‖q‖ = 1` -/

/-- **The twist is a phase at the fibre root of unity.**  If `‖q‖ = 1` then `‖θ_λ‖ = ‖q^{c}‖ =
‖q‖^{c} = 1`.  This is the fibre-level statement `Im q ≠ 0` (AGENTS.md fibre-vs-observable `q`): at
`‖q‖ = 1` the twist carries no modulus, only a phase. -/
theorem thetaN_norm_one {q : K} (c : ℤ) (hq : ‖q‖ = 1) : ‖thetaN q c‖ = 1 := by
  unfold thetaN
  rw [norm_zpow, hq, one_zpow]

/-- **The framing cancels in the modulus at the fibre root of unity.**  `‖bwS0N‖ = ‖s0·(θ)^f‖ =
‖s0‖·‖θ‖^{f} = ‖s0‖·1^{f} = ‖s0‖`: at `‖q‖ = 1` the framing `θ^f` is a phase, so the modulus of the
concrete vacuum row is exactly the modulus of the S-matrix entry `s0` — the framing dependence drops
out. -/
theorem bwS0N_norm_eq {s0 q : K} (c f : ℤ) (hq : ‖q‖ = 1) :
    ‖bwS0N s0 q c f‖ = ‖s0‖ := by
  unfold bwS0N
  rw [norm_mul, norm_zpow, thetaN_norm_one c hq, one_zpow, mul_one]

/-- **Capstone: the squared modulus of the geometric vacuum row realizes the Verlinde measure `W_λ` at
the fibre.**  `‖bwS0N‖² = ‖s0‖²` — independent of the framing `f`.  With `s0 = S_{0λ} = d_q/D` this is
`W_λ = S_{0λ}² = d_q²/D²` (`KeystoneVerlindeSMatrixBridge.verlindeMeasure`).  So at the fibre root of
unity `‖q‖ = 1` the geometric squared-amplitude **is** the Verlinde measure, framing-cancelled — the
surviving residue of the #3662 refutation.  This does not close the gate; it states precisely what
survives at `‖q‖ = 1`. -/
theorem bwS0N_normSq_eq_verlinde {s0 q : K} (c f : ℤ) (hq : ‖q‖ = 1) :
    ‖bwS0N s0 q c f‖ ^ 2 = ‖s0‖ ^ 2 := by
  rw [bwS0N_norm_eq c f hq]

/-! ## The residue's frontier: off the fibre root of unity the framing does NOT cancel -/

/-- **Contrast lemma — the open object, made explicit.**  Off the fibre root of unity, at `‖q‖ = r`,
the modulus of the concrete row is `‖s0‖·r^{c·f}`: the framing factor `r^{c·f}` survives and does
**NOT** cancel unless `c·f = 0`.  At the observable archimedean `q₀ > 1` (`r = q₀ > 1`) this restates
the #3662 refutation — for the forced Seifert framing `f ≠ 0` and a non-self-conjugate block
(`c ≠ 0`), `r^{c·f} ≠ 1`, so `‖bwS0N‖ ≠ ‖s0‖`.  The open residue is precisely the continuation
`r = 1 → r = q₀`; this lemma locates that frontier and asserts no physics beyond it. -/
theorem bwS0N_norm_off_unit (s0 q : K) (c f : ℤ) :
    ‖bwS0N s0 q c f‖ = ‖s0‖ * ‖q‖ ^ (c * f) := by
  unfold bwS0N thetaN
  rw [norm_mul, norm_zpow, norm_zpow, ← zpow_mul]

end QOU.BraidKnot.Keystone
