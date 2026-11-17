import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Module
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# The nucleon–nucleon interface is a single scalar

**The interface collapses to one number, and that number is bounded.**

> The title and subtitle here used to read "…and it has a floor" / "Why no
> crossing convention can bind the deuteron". Both are **withdrawn** (2026-08-09):
> the floor is convention-**C** specific and the deuteron IS reachable under the
> production convention **D**. See the retraction below.

In the `H_{3A}` atom word (`computations/mass_at_3A_proper.atom_braid_word_3A`)
the generator `σ₂` is the *only* one joining strand 2 — nucleon `k`'s last quark
— to strand 3, nucleon `k+1`'s first. So "the inter-nucleon sector" is literally
the word placed at that one generator, and the binding functional
`B = α·ln(tr_free/tr_atom)` reads it through the Markov trace alone.

Two facts collapse that sector to a single number.

* The Hecke quadratic `σ² = h·σ + 1` closes `span{1, σ}` under multiplication
  (`interface_mul`), so **every** word at `σ₂`, of any length, is `a•σ + b•1`.
* The Markov property `tr(W·σ) = z·tr(W)` plus linearity then gives
  `tr(W·(a•σ + b•1)) = (a·z + b)·tr(W)` (`interface_scalar`).

Hence the whole interface enters through `μ = a·z + b`, and the per-bond
log-suppression is `L = −ln μ`. The framework's four whitelisted crossings are
the `a = 1` cases at `d ∈ {0, −h(½−δ/4), −h/2, −h}`, i.e. `μ ∈ [z−h, z]`.

Four consequences are recorded here.

`mu_mem_Icc` — the admissible `μ` lies in `[z−h, z]`, so with `−ln` decreasing
the binding is confined to `[α·ln(1/z), α·ln(1/(z−h))]`. `mu_unreachable` is the
formal statement that a target above `z` is not attained by any admissible
offset. Both are conditional theorems and remain true as stated.

> **RETRACTION 2026-08-09 — the deuteron IS reachable, and the impossibility
> narrative that used to stand here is withdrawn.** This paragraph read
> "Numerically that is `[2.907195, 5.177967]` MeV, while `B_AME(²H) =
> 2.2245662`: **below the floor by 30.69 %** … no crossing sign, colour weight,
> or multiplicity reaches the deuteron." Those numbers are convention **C**
> (`z = 1/(√q+1/√q) = 0.4993`), which was excised. Under the production
> convention **D** (`z = q³/(q²+1) = 0.6127`) the admissible band is
> `[2.0507, 3.7978]` MeV and **contains** `B_AME(²H) = 2.224566`. Solving for
> the required offset gives `d = −0.024973 = −0.11945·h`, **inside** the Hecke
> range `[−h, 0]`, where under C it was `+0.4230·h` and outside. The theorems
> are untouched; only the claim that they *bind here* was wrong. What remains
> open is that the derived colour weight `t = ½ − δ/4 = 0.499656` does not equal
> the required `t = 0.119453` — a derivation gap, not an impossibility.
> Audit: `docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`;
> bean `qou-kj4v`.

`bond_energy_floor` — a `z`-form-specific bound. **`z = 1/(q^{1/2} + q^{-1/2})`
is convention C and is NO LONGER the production Markov parameter** (production
is D, `z = q³/(q²+1)`); this paragraph used to call it "the production Markov
parameter" and to bill this as "the stronger, q-independent form, which
supersedes `mu_unreachable` as the headline". Both withdrawn. For a `z` of the
C form, AM-GM (`two_le_add_inv`,
`markov_param_le_half`) gives `z ≤ 1/2` for *every* `q`. With `d ≤ 0` that
forces `μ ≤ 1/2` (`mu_le_half`) and hence

    B_bond = −α·log μ  ≥  α·log 2  =  2.90150117984 MeV,

against `B_AME(²H) = 2.224566` — **30.43 % below**. This holds for every `q`,
every crossing convention, and every multiplicity — **but only for a `z` of the
form `1/(x + x⁻¹)`**, which is where AM-GM bites.

> **SCOPE CORRECTION 2026-08-09.** This paragraph previously added "and every
> `N` in an `SU(N)` choice of `z` (larger `N` shrinks `z` and *increases* the
> floor)". **That is false**, and it mattered. It assumed the `SU(N)` family is
> `z = 1/[N]`, which it is not — the `SU(N)` weights are quantum dimensions
> (hook-content), and the `SU(2)` member is registry convention **D** at
> `z = q³/(q²+1) = 0.6126880 > 1/2`. `markov_param_le_half` does not apply to
> it, so neither does the floor. Measured under D the admissible band is
> `[2.0507, 3.7978] MeV` and `B_AME(²H) = 2.224566` lies **inside** it, with the
> required offset `d = −0.1192·h` admissible. The impossibility below is
> therefore specific to convention **C**, the production binding trace, not a
> statement about Markov traces in general. See `computations/y_lambda_su_n.py`
> and `docs/coordination/trace-convention-registry.md`.

Within convention C it stands — and only there. Contrapositively
(`alpha_upper_bound`), under C the deuteron would be reachable only if

    α  ≤  B_AME(²H)/log 2  =  3.2093703 MeV,

while the derived `α = m_e/(q₀(q₀−1)) = 4.1859814` exceeds that by 30.43 %.
Pursued in bean `qou-qlma`.

`charge_independence_iff` — the strong force is charge independent, so a bond
model must give `L_pp = L_nn`. With `d_pp = 0` (σ) and `d_nn = −h` (σ⁻¹) that
demands `z = z − h`, i.e. `h = 0`, i.e. `q = 1`: the classical limit, where the
Hecke structure is gone. Measured under C, `α(L_nn − L_pp) = 2.27077 MeV`; under D with the derived
writhe term wired it is **0.76532 MeV** (the writhe factor `(1−h)^(Δe/2)` shifts
pp and nn equally and oppositely, removing 56.19 % of the asymmetry). Either way
the splitting is an artifact of the σ/σ⁻¹ charge assignment, not an isospin
effect — charge symmetry demands the *strong* mirror split be small, and the
flavour parameter δ cancels out of it entirely by `mirror_split_eq_L_diff`.
Nature's 0.7638 MeV is mostly Coulomb (uniform-sphere E_C alone gives 0.9984),
so the strong sector should supply only the small Nolen–Schiffer residual, not
the whole split. Beans `qou-4waf`, `qou-usft`.

`proj_add_eq_one` / `proj_mul_eq_zero` — the same quadratic supplies the isospin
decomposition for free. `P₊ = (σ + q⁻¹)/(q + q⁻¹)` and `P₋ = (q − σ)/(q + q⁻¹)`
are complementary orthogonal idempotents, and for two nucleons `T=1` is the
isospin-symmetric channel, `T=0` the antisymmetric one. Their interface scalars
are `μ₊ = (z + q⁻¹)/(q + q⁻¹)` and `μ₋ = (q − z)/(q + q⁻¹)`, with `μ₊ + μ₋ = 1`.

Base ring: **generic** (§7c). The algebra `A` is a plain `[Ring A]` over a
commutative `[CommRing R]` of scalars, so nothing here assumes the Hecke algebra
is commutative; the ordered results take `[Field R] [LinearOrder R]
`[IsStrictOrderedRing R]` because they
are about the *scalar* `μ`, never about `A`.

Companion audit: `docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`.
Beans `qou-c6gx`, `qou-h7mh`.

**Scope.** This is a structural result about the *interface* — it collapses to
one scalar, and that scalar is bounded by the Hecke range. It is **not** an
impossibility result for the deuteron; that reading was C-specific and is
retracted above. It is conditional in one place: `interface_scalar` takes the Markov property as a
hypothesis, because in this corpus that property is an `axiom` carrying a
`sorry` (`jones-markov-trace.lean`, standing in for Jones 1987) rather than a
theorem. Nothing here proves the trace exists.

It also does **not** claim the interface is where the ²H error lives. Note the
premise of that argument has itself been retracted: an admissible `μ` **does**
reach AME under convention D (see the retraction above). The per-bond
sign-change evidence (audit §4) was also computed under C and needs re-running
before it is cited. The two
positive routes suggested by `proj_*` — a derived Clebsch weighting, and
charge independence imposed with Coulomb carrying the mirror split — are
neither formalised nor wired here.

The `Li₂^q` product form of audit §8 is not in this file; it needs a Fubini
argument on a doubly-indexed sum and is tracked separately (bean `qou-cw27`).
-/

namespace QOU.QBeta.InterfaceScalar

section Algebra

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The interface subalgebra is two-dimensional.** The Hecke quadratic
`σ² = h•σ + 1` closes `span{1, σ}` under multiplication, so a word of *any*
length at the single inter-nucleon generator is again `a•σ + b•1`. This is what
forbids "adding more knot operations" at the interface: there is nowhere for
them to go. -/
theorem interface_mul (σ : A) (h a b c d : R) (hq : σ * σ = h • σ + 1) :
    (a • σ + b • (1 : A)) * (c • σ + d • (1 : A))
      = (a * c * h + a * d + b * c) • σ + (a * c + b * d) • (1 : A) := by
  have expand :
      (a • σ + b • (1 : A)) * (c • σ + d • (1 : A))
        = (a * c) • (σ * σ) + (a * d + b * c) • σ + (b * d) • (1 : A) := by
    simp [add_mul, mul_add, smul_smul, add_smul]
    module
  rw [expand, hq]
  module

/-- **The interface collapses to one scalar.** Markov stabilisation
`tr(W·σ) = z·tr(W)` plus linearity of the trace send every interface element
`a•σ + b•1` to the single number `μ = a·z + b`.

The Markov property is a hypothesis, not a theorem: in this corpus it is an
axiom standing in for Jones (1987). -/
theorem interface_scalar (tr : A → R) (W σ : A) (z a b : R)
    (hadd : ∀ x y : A, tr (x + y) = tr x + tr y)
    (hsmul : ∀ (c : R) (x : A), tr (c • x) = c * tr x)
    (hmarkov : tr (W * σ) = z * tr W) :
    tr (W * (a • σ + b • (1 : A))) = (a * z + b) * tr W := by
  have expand : W * (a • σ + b • (1 : A)) = a • (W * σ) + b • W := by
    simp [mul_add]
  rw [expand, hadd, hsmul, hsmul, hmarkov]
  ring

end Algebra

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Charge independence forces the classical limit.** The framework assigns
`d_pp = 0` (σ) and `d_nn = −h` (σ⁻¹), so the p-p and n-n interface scalars agree
only when `h = 0`, i.e. `q = 1`. Since the strong force *is* charge independent,
the σ/σ⁻¹ assignment cannot be right at `q ≠ 1`. -/
theorem charge_independence_iff (z h : R) : z + 0 = z + -h ↔ h = 0 := by
  constructor
  · intro hyp
    have : (0 : R) = -h := by linarith
    linarith
  · intro hyp; rw [hyp]; ring

/-- The admissible interface offsets `d ∈ [−h, 0]` — σ⁻¹ at one end, σ at the
other — put `μ = z + d` in `[z − h, z]`. -/
theorem mu_mem_Icc (z h d : R) (hd_lo : -h ≤ d) (hd_hi : d ≤ 0) :
    z - h ≤ z + d ∧ z + d ≤ z := by
  constructor <;> linarith

/-- **The floor theorem.** A target strictly above `z` is attained by no
admissible interface element. With `z = 1/(√q₀ + 1/√q₀)` this says
`B ≥ α·ln(1/z) = 2.907195 MeV` for every crossing convention, while
`B_AME(²H) = 2.2245662`. **Retracted as a physical claim 2026-08-09**: those are
convention-C numbers, and under production convention D the deuteron IS
reachable at `d = −0.11945·h`. The theorem below is a true conditional and is
unaffected; only its application to ²H was wrong. -/
theorem mu_unreachable (z d μ_req : R) (hd_hi : d ≤ 0) (htarget : z < μ_req) :
    z + d ≠ μ_req := by
  intro hcontra
  have : z + d ≤ z := by linarith
  linarith [hcontra ▸ this]

/-- Stacking crossings does not escape the interval either: `σ²  = h•σ + 1`
sends `(a, b) = (1, 0)` to `(h, 1)`, whose scalar `h·z + 1` exceeds `1` whenever
`h` and `z` are positive — i.e. the two-crossing bond is *anti*-bound
(`μ > 1 ⟹ L < 0`). Measured: `μ = 1.1044`, `B = −0.416 MeV`. -/
theorem stacked_crossing_gt_one (z h : R) (hz : 0 < z) (hh : 0 < h) :
    1 < h * z + 1 := by nlinarith

/-- **AM-GM on the Markov parameter.** `2 ≤ x + x⁻¹` for every `x > 0`, since
`x + x⁻¹ - 2 = (x-1)²/x ≥ 0`. -/
theorem two_le_add_inv (x : R) (hx : 0 < x) : 2 ≤ x + x⁻¹ := by
  have key : x + x⁻¹ - 2 = (x - 1) ^ 2 / x := by field_simp; ring
  have hnn : 0 ≤ (x - 1) ^ 2 / x := by positivity
  linarith [key ▸ hnn]

/-- **`z ≤ 1/2` for every q.** The production Markov parameter is
`z_m = 1/(q^{1/2} + q^{-1/2})`; with `x = √q₀` that is `(x + x⁻¹)⁻¹`, bounded by
`1/2` unconditionally. Wenzl positivity (`q^{1/2} + q^{-1/2} > 2`, already
required by the corpus) makes it strict. -/
theorem markov_param_le_half (x : R) (hx : 0 < x) : (x + x⁻¹)⁻¹ ≤ 1 / 2 := by
  have h2 : (2 : R) ≤ x + x⁻¹ := two_le_add_inv x hx
  have hpos : (0 : R) < x + x⁻¹ := by positivity
  rw [inv_eq_one_div]
  exact one_div_le_one_div_of_le (by norm_num) h2

/-- Every admissible interface scalar is at most `1/2`: `d ≤ 0` from the Hecke
range, `z ≤ 1/2` from AM-GM. -/
theorem mu_le_half (z d : R) (hz : z ≤ 1 / 2) (hd : d ≤ 0) : z + d ≤ 1 / 2 := by
  linarith

end Ordered

section EnergyFloor

/-- **The universal binding floor.** Combining `mu_le_half` with the fact that
`-log` is decreasing: for any admissible interface scalar,

    B_bond = -α·log μ  ≥  α·log 2.

Numerically `α·log 2 = 2.90150117984 MeV` while `B_AME(²H) = 2.224566`, which is
**30.43% below the floor**. Unlike `mu_unreachable`, which was stated at the
actual `z`, this holds for *every* `q`, every crossing convention, every
multiplicity, and every `N` in an `SU(N)` choice of `z` — so it is a statement
about **α**, not about the interface.

Contrapositive, and the reason bean `qou-qlma` exists: the deuteron is reachable
at all only if `α ≤ B_AME(²H)/log 2 = 3.2093703 MeV`. The derived
`α = m_e/(q₀(q₀−1)) = 4.1859814` exceeds that by 30.43%.

Stated over `ℝ` rather than a generic ordered field because `Real.log` is
genuinely required here — this is not a gratuitous `ℝ` in the sense of §7c. -/
theorem bond_energy_floor (a mu : ℝ) (ha : 0 < a) (hmu : 0 < mu)
    (h : mu ≤ 1 / 2) : a * Real.log 2 ≤ -a * Real.log mu := by
  have hlog : Real.log mu ≤ Real.log (1 / 2) := Real.log_le_log hmu h
  have hhalf : Real.log (1 / 2) = -Real.log 2 := by
    rw [one_div, Real.log_inv]
  nlinarith [hlog, hhalf]

/-- The contrapositive as a bound on the energy scale: if the observed bond
energy is below `α·log 2`, then `α` is too large to be the interface scale. -/
theorem alpha_upper_bound (a mu B : ℝ) (ha : 0 < a) (hmu : 0 < mu)
    (h : mu ≤ 1 / 2) (hB : -a * Real.log mu = B) : a * Real.log 2 ≤ B := by
  rw [← hB]; exact bond_energy_floor a mu ha hmu h

end EnergyFloor

section FunctionalIsTheLog

/-! ### Which functional carries a multiplicative trace to an additive energy

`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
§10a argues the binding functional is *derived* rather than chosen: `tr_M` is
multiplicative over independent subsystems (`tr_atom = tr_free * Prod_bonds mu_k`,
measured there to 1.2e-31) and energy is extensive, so the map from trace to
energy satisfies Cauchy's `f(xy) = f(x) + f(y)` and the log form is forced.

That argument lived only in audit prose. The five-path grep in
`docs/audits/2026-08-25-deuteron-attack-c-convergence.md` recorded **"Lean:
nothing"**, and that part was correct. This section supplies the half that is
mechanically checkable.

**What is proved here, and what is not.** The *comparison* the corpus actually
runs — log versus linear, the two candidates §10a weighs — is proved: the log
form is extensive, the linear form is not, its failure has an exact closed form,
and it carries a ceiling that kills it above A = 2 independently of extensivity.
The *uniqueness* step ("the only continuous solutions of Cauchy's equation on
`(R_+, x)` are `c log x`") is a classical theorem that is **not** formalised
here, so "forced" still rests on it. Do not cite this section as a formalisation
of §10a's uniqueness claim. -/

/-- **The log form is extensive.** A product of bond scalars becomes a sum of
bond energies — the property §10a requires of the trace-to-energy map. -/
theorem logForm_extensive (a x y : ℝ) (hx : 0 < x) (hy : 0 < y) :
    -a * Real.log (x * y) = -a * Real.log x + -a * Real.log y := by
  rw [Real.log_mul (ne_of_gt hx) (ne_of_gt hy)]
  ring

/-- **The linear form's extensivity defect, in closed form.** For the rival
candidate `B = a(1 - t)` the failure is exactly `-a(1-x)(1-y)` — an identity, so
it needs no positivity hypothesis and no anchor.

This sharpens §10a, which reports the defect as a single measured number. That
number is **convention-C frame**: the audit is dated one day before the
2026-08-09 convention-D excision. Re-measured at the proton pin with
`mu_pp = z`, `mu_nn = z - h`:

    convention C   z = sqrt(q)/(q+1)   defect = 1.487498   <- the audit's 1.4875
    convention D   z = q^3/(q^2+1)     defect = 0.966887

The conclusion is unaffected in either convention — the closed form vanishes only
when `x = 1` or `y = 1` — but the quoted figure needs the scope. -/
theorem linearForm_extensivity_defect (a x y : ℝ) :
    a * (1 - x * y) - (a * (1 - x) + a * (1 - y)) = -(a * ((1 - x) * (1 - y))) := by
  ring

/-- **The linear form is not extensive**, whenever neither bond scalar is
trivial. `x = 1` or `y = 1` is the degenerate case of a bond that contributes
nothing, so on any bond that binds at all the linear form fails. -/
theorem linearForm_not_extensive (a x y : ℝ) (ha : a ≠ 0) (hx : x ≠ 1) (hy : y ≠ 1) :
    a * (1 - x * y) - (a * (1 - x) + a * (1 - y)) ≠ 0 := by
  rw [linearForm_extensivity_defect]
  simp only [neg_ne_zero]
  exact mul_ne_zero ha (mul_ne_zero (sub_ne_zero.mpr (Ne.symm hx))
    (sub_ne_zero.mpr (Ne.symm hy)))

/-- **The linear form's ceiling.** Because the atom trace is positive,
`B_lin = a(t_free - t_atom)` is strictly bounded by `a * t_free` — no choice of
word or convention escapes it.

§10a's table is this bound in the open: with `t_free ~ 1` at every `A`, the
ceiling sits near `a ~ 4.19 MeV`, so `B_AME` at ³H (8.48), ⁴He (28.30) and ⁷Li
(39.24) is unreachable. That is a second, independent reason to reject the linear
form, and unlike extensivity it does not depend on the convention. -/
theorem linearForm_ceiling (a t_free t_atom : ℝ) (ha : 0 < a) (ht : 0 < t_atom) :
    a * (t_free - t_atom) < a * t_free := by
  nlinarith [mul_pos ha ht]

end FunctionalIsTheLog

section WeightsDetermineZ

variable {R : Type*} [Field R]

/-- **The Markov parameter is not a free choice — the weights fix it.**

At `n = 2` the two irreps are `(2)` and `(1,1)`, both one-dimensional, with
`χ^{(2)}(σ) = q` and `χ^{(1,1)}(σ) = −q⁻¹`. Given only the Markov normalisation
`Σ_λ y_λ d_λ = 1` (here `y₂ + y₁₁ = 1`) and the pairing
`tr_M(σ) = Σ_λ y_λ χ^λ(σ)`, the parameter `z := tr_M(σ)` is a *function of the
weights*:

    z = y₂·(q + q⁻¹) − q⁻¹.

`y_lambda_at(n, q)` takes only `q` — there is no `z` argument — so `z` is a
consequence of the Jones–Markov hook-length weights, not an input beside them.
Checked numerically at q₀: `tr_M(σ)` from `y_λ` equals `1/(√q + 1/√q)` to
7.3e-31 (the 30-digit `y_λ` cap). Consequently z **cannot be retuned** to close
²H without contradicting `y_λ`. -/
theorem markov_param_determined (q y₂ y₁₁ z : R)
    (hnorm : y₂ + y₁₁ = 1)
    (htr : y₂ * q + y₁₁ * (-q⁻¹) = z) :
    z = y₂ * (q + q⁻¹) - q⁻¹ := by
  have hy : y₁₁ = 1 - y₂ := by linear_combination hnorm
  rw [← htr, hy]; ring

/-- **…and inverting it reproduces the isospin projector scalar.** Solving
`markov_param_determined` for `y₂` gives exactly `μ₊ = (z + q⁻¹)/(q + q⁻¹)`, the
symmetric-channel interface scalar from `proj_add_eq_one`. So the eightfold-way
projector weights and the `n = 2` Wedderburn weights are the *same object*, not
two constructions that happen to agree numerically (they match to 3.6e-31). -/
theorem weight_eq_proj_scalar (q y₂ z : R) (hs : q + q⁻¹ ≠ 0)
    (h : z = y₂ * (q + q⁻¹) - q⁻¹) :
    y₂ = (z + q⁻¹) / (q + q⁻¹) := by
  rw [eq_div_iff hs]
  linear_combination -h

end WeightsDetermineZ

section Mirror

/-- **The mirror splitting sees only `L_nn − L_pp`; the p–n bond cancels.**

On the chain topology ³H = `pnn` carries bonds `{pn, nn}` and ³He = `ppn`
carries `{pp, pn}`, so the predicted splitting is `α(L_nn − L_pp)` regardless of
what the p–n bond is. Combined with `charge_independence_iff` (`L_pp = L_nn ⟺
h = 0`) this says the model's mirror splitting is nonzero **precisely because**
the σ/σ⁻¹ templates are charge-assigned — it is an artifact, not isospin
physics. Measured: `α(L_nn − L_pp) = 2.27077 MeV` against nature's 0.7638, which
is mostly Coulomb. Giving all three bonds the same template sends it to zero. -/
theorem mirror_split_eq_L_diff {R : Type*} [CommRing R] (a L_pp L_pn L_nn : R) :
    a * (L_pn + L_nn) - a * (L_pp + L_pn) = a * (L_nn - L_pp) := by ring

/-- **The nucleon identity cancels out of the binding.** Since
`tr_atom = tr_free · μ`, the binding `−α·log tr_atom − (−α·log tr_free)` is
`−α·log μ`: `tr_free`, and with it `tr_M(p)` and `tr_M(n)`, drops out entirely.

This is why *all* isospin physics must live in the interface — nothing else
survives the difference. In particular any assignment with `d_pp = d_nn` gives
identically zero mirror splitting no matter how the proton and neutron words
differ, which is what `mirror_split_eq_L_diff` sees from the other side. -/
theorem binding_indep_of_free_trace (a trf mu : ℝ) (hf : 0 < trf) (hm : 0 < mu) :
    -a * Real.log (trf * mu) - -a * Real.log trf = -a * Real.log mu := by
  rw [Real.log_mul (ne_of_gt hf) (ne_of_gt hm)]; ring

end Mirror

section FlavourTilt

/-- **The flavour tilt is an additive shift on μ, of size `h·δ/4`.**

The p–n template is `d = −h(½ − δ/4)`, which is exactly the colour-blind
`−h/2` displaced by `h·δ/4`. So the tilt's whole effect on the interface scalar
is that shift — there is no other channel through which δ enters the trace. -/
theorem tilt_is_additive_shift {R : Type*} [Field R] (h δ : R) :
    -(h * (1 / 2 - δ / 4)) = -(h / 2) + h * δ / 4 := by ring

/-- **…so the binding it induces depends only on the ratio `t/μ₀`.**

With `μ₀` the colour-blind scalar and `t = h·δ/4` the shift, the change in
`B = −α·log μ` is `−α·log(1 + t/μ₀)` exactly. That is what makes the two roles
of δ separable: at q₀, `t = 7.19e-5` and `μ₀ = 0.394790`, so `t/μ₀ = 1.82e-4`
and the entire tilt is worth `7.6e-4 MeV` on `B(²H)` — while the
leading-vs-subleading disagreement inside δ is a further 1e-3 of *that*.

Role (a) (δ as the physical `Δm/M_N`, gated at 1000 ppm against CODATA) and
role (b) (δ as this tilt) therefore cannot disturb one another, and can be
given separate names and separate derivations. Bean `qou-nbx7`. -/
theorem tilt_log_shift (a mu0 t : ℝ) (h0 : 0 < mu0) (ht : 0 < mu0 + t) :
    -a * Real.log (mu0 + t) - -a * Real.log mu0 = -a * Real.log (1 + t / mu0) := by
  have hpos : 0 < 1 + t / mu0 := by
    have hr : 1 + t / mu0 = (mu0 + t) / mu0 := by field_simp
    rw [hr]; exact div_pos ht h0
  have hfac : mu0 + t = mu0 * (1 + t / mu0) := by field_simp
  rw [hfac, Real.log_mul (ne_of_gt h0) (ne_of_gt hpos)]
  ring

end FlavourTilt

section Projectors

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **The isospin projectors are complementary.** Writing `s = (q + q⁻¹)⁻¹`,
`P₊ = s•(σ + q⁻¹•1)` and `P₋ = s•(q•1 − σ)` sum to `1`. For two nucleons `T=1`
is the symmetric channel and `T=0` the antisymmetric one, so the eightfold-way
decomposition is already present in the Hecke quadratic — no new parameter. -/
theorem proj_add_eq_one (σ : A) (q qi s : R) (hs : s * (q + qi) = 1) :
    s • (σ + qi • (1 : A)) + s • (q • (1 : A) - σ) = 1 := by
  have expand : s • (σ + qi • (1 : A)) + s • (q • (1 : A) - σ)
      = (s * (q + qi)) • (1 : A) := by
    module
  rw [expand, hs, one_smul]

/-- **…and orthogonal.** `P₊ · P₋ = 0` follows from the quadratic together with
`h = q − q⁻¹`, which is exactly the Hecke parametrisation. -/
theorem proj_mul_eq_zero (σ : A) (q qi s h : R)
    (hq : σ * σ = h • σ + 1) (hh : h = q - qi) (hqi : q * qi = 1) :
    (s • (σ + qi • (1 : A))) * (s • (q • (1 : A) - σ)) = 0 := by
  have key : (σ + qi • (1 : A)) * (q • (1 : A) - σ) = 0 := by
    have expand : (σ + qi • (1 : A)) * (q • (1 : A) - σ)
        = q • σ + (q * qi) • (1 : A) - (σ * σ + qi • σ) := by
      simp [mul_sub, add_mul, smul_smul]
    rw [expand, hq, hqi, hh]
    module
  calc (s • (σ + qi • (1 : A))) * (s • (q • (1 : A) - σ))
      = (s * s) • ((σ + qi • (1 : A)) * (q • (1 : A) - σ)) := by
        rw [smul_mul_smul_comm]
    _ = 0 := by rw [key, smul_zero]

end Projectors

section IsospinOrdering

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **Convention D makes `2z − h` a manifest positive.** With the
Temperley–Lieb / SU(2) Markov parameter `z = q³/(q²+1)` and the Hecke
parameter `h = q − q⁻¹`,

    2z − h = (q⁴ + 1) / (q(q² + 1)),

an identity, not an estimate. Every factor on the right is positive for
`q > 0`, so the sign needs no numerical input. -/
theorem two_z_sub_h_conventionD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    2 * (q ^ 3 / (q ^ 2 + 1)) - (q - q⁻¹) = (q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by
  field_simp
  ring

/-- **…hence `h < 2z` for every `q > 0`.** -/
theorem h_lt_two_z_conventionD (q : R) (hq : 0 < q) :
    q - q⁻¹ < 2 * (q ^ 3 / (q ^ 2 + 1)) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hq2 : (0 : R) < q ^ 2 + 1 := by positivity
  have hid := two_z_sub_h_conventionD q hq0 (ne_of_gt hq2)
  have hpos : (0 : R) < (q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by positivity
  linarith [hid ▸ hpos]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- **The two isospin channels partition the free trace.** The scalar shadow of
`proj_add_eq_one`: `μ₊ + μ₋ = 1` exactly. Projecting onto a channel can only
*remove* trace weight, so `μ_T < 1` and `B_T = −α·log μ_T > 0` for both `T` —
which is why the projector decomposition alone can never produce an unbound
channel. Unbinding needs `μ > 1`, and that requires leaving the convex
decomposition of `1`, e.g. `stacked_crossing_gt_one`. -/
theorem mu_sum_eq_one (q z : R) (hs : q + q⁻¹ ≠ 0) :
    (z + q⁻¹) / (q + q⁻¹) + (q - z) / (q + q⁻¹) = 1 := by
  rw [← add_div, div_eq_one_iff_eq hs]
  ring

/-- **THE ORDERING IS FORCED — no fit, no multiplicity, every `q`.**

`μ₊` is the `T = 1` (isospin-symmetric) interface scalar and `μ₋` the `T = 0`
(antisymmetric) one. Under convention D,

    μ₋ < μ₊   for every  q > 0,

because the difference is `μ₊ − μ₋ = (2z − h)/(q + q⁻¹)` and
`h_lt_two_z_conventionD` makes the numerator positive. With `B = −α·log μ`
decreasing in `μ`, the **isospin singlet is always the more strongly bound
channel**. Nature agrees: of the four two-nucleon channels — pp, nn, pn(¹S₀)
all `T = 1`, pn(³S₁) the deuteron at `T = 0` — exactly the `T = 0` one binds.

This is the replacement for the crossing-multiplicity story. The channel is
selected by a representation label, not by a count of crossings, so there is
no `m_pp` / `m_nn` to tune (cf. bean `qou-h7mh`: "DO NOT JUST FIT m_*"). -/
theorem mu_singlet_lt_mu_triplet (q z : R) (hq : 0 < q)
    (hz : z = q ^ 3 / (q ^ 2 + 1)) :
    (q - z) / (q + q⁻¹) < (z + q⁻¹) / (q + q⁻¹) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hinv : 0 < q⁻¹ := by positivity
  have hs : 0 < q + q⁻¹ := by linarith
  have hnum : q - z < z + q⁻¹ := by
    have := h_lt_two_z_conventionD q hq
    rw [hz]; linarith
  exact (div_lt_div_iff_of_pos_right hs).mpr hnum

/-- **…and therefore the singlet binds harder.** `−log` is decreasing, so
`μ₋ < μ₊` transports to `B₊ < B₋` for any positive scale `α`. Stated over `ℝ`
because `Real.log` is. -/
theorem singlet_binds_more (α μp μm : ℝ) (hα : 0 < α) (hm : 0 < μm)
    (hlt : μm < μp) : -α * Real.log μp < -α * Real.log μm := by
  have hlog : Real.log μm < Real.log μp := Real.log_lt_log hm hlt
  nlinarith

end IsospinOrdering

section ChannelSelection

/-- **Any interface keyed on nucleon CONTENT is refuted by the two pn channels.**

The proposal "identical nucleons take two crossings" — and every variant of it —
assigns the interface from the unordered pair of nucleon species, i.e. it
factors through `content : Channel → Content`. But nature's two pn channels
have the *same* content and *opposite* boundness: pn(³S₁) is the deuteron at
`+2.224566 MeV`, pn(¹S₀) is unbound (a virtual state at `−0.066 MeV`). A
function of the content alone must give them the same energy.

So the refutation is logical, not numerical: no choice of `m_pp`, `m_nn`,
`m_pn` can succeed, because the failure is in what the multiplicities are
allowed to depend on. `mu_singlet_lt_mu_triplet` supplies the variable that
does work — the isospin label `T`, which separates the two pn channels. -/
theorem content_keyed_interface_refuted
    {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    {Channel Content : Type*} (content : Channel → Content) (B : Content → R)
    (pn_triplet pn_singlet : Channel)
    (hsame : content pn_triplet = content pn_singlet)
    (hbound : 0 < B (content pn_triplet))
    (hunbound : B (content pn_singlet) ≤ 0) : False := by
  rw [hsame] at hbound
  linarith

end ChannelSelection

section SpaceIndexSeparability

/-! ### Can a space index break the pn degeneracy?

Bean `qou-vbyi` proposes a **space index** on the interface as *"the only route
past the proved flavour-only degeneracy"*, on the strength of `qou-kj4v`'s
observation that in the Standard Model the ³S₁/¹S₀ split is the tensor force —
a spin-**space** coupling — and that *"the Hecke interface has one index (the
strand) and no space index to carry it."*

The reading of that as "add a space factor" does not survive a check, and the
reason is in `qou-kj4v`'s own sentence: *"In S-wave Pauli LOCKS spin to isospin
(**space symmetric** ⇒ spin and isospin symmetry opposite)."* **Both pn channels
are S-wave**, `L = 0` — ³S₁ and ¹S₀ are both `S` in `²ᴹ⁺¹L_J`. So a factor keyed
on `L` takes the *same* value on both, and a common factor cannot separate what
was already equal.

The theorem below states this for an arbitrary separable interface, so it covers
any space index entering multiplicatively, keyed on anything constant across the
two channels — not merely `L`. -/

variable {R : Type*} [CommMonoid R]

/-- **A separable interface stays degenerate on the two pn channels, whatever
space index it carries.**

The hypotheses encode the Pauli lock exactly as `qou-kj4v` states it: the
triplet is `(S = 1, T = 0)` and the singlet `(S = 0, T = 1)`, and the *same* two
projector scalars `μ₊`, `μ₋` appear in each SU(2) with the roles exchanged. The
space factor is applied at one and the same `ell`, which is the physical input —
both channels are S-wave.

The conclusion holds for **every** `fSpace`, so no choice of space index rescues
a separable interface. What the tensor force does in the Standard Model is
*couple* spin to space; a product of a spin function and a space function is
precisely what a coupling is not. -/
theorem separable_interface_degenerate
    {Sp Is Sp3 : Type*} (fSpin : Sp → R) (fIso : Is → R) (fSpace : Sp3 → R)
    (s1 s0 : Sp) (t1 t0 : Is) (ell : Sp3)
    (hplus : fSpin s1 = fIso t1) (hminus : fSpin s0 = fIso t0) :
    fSpin s1 * fIso t0 * fSpace ell = fSpin s0 * fIso t1 * fSpace ell := by
  rw [hplus, hminus, mul_comm (fIso t1) (fIso t0)]

/-- The bare form: a factor common to both channels cannot break a degeneracy
that already holds. Stated separately because it is what makes the theorem above
independent of *why* the space factor is common. -/
theorem common_factor_preserves_degeneracy (x y g : R) (h : x = y) :
    x * g = y * g := by rw [h]

end SpaceIndexSeparability

section ConjugationInvariance

variable {A : Type*} [Ring A] {K : Type*}

/-- **A conjugated interface has the same trace value.**

The attack that dies here: `chi_monotone_transfer.word_to_mpfr` rejects
non-monotone braid words, so a bond joining strands `1 ↔ 3` must be written
`σ₁σ₂σ₁⁻¹` and is currently unreachable. The proposed remedy was to lift that
restriction and thereby enlarge the set of attainable interface values.

It attains nothing new. Cyclicity of the Markov trace, `tr (ab) = tr (ba)`,
gives conjugation invariance for free:

    tr (u b u⁻¹) = tr (u⁻¹ u b) = tr b.

Every conjugate of `σ₂` carries `σ₂`'s value exactly. Lifting the monotone-word
restriction changes which *words* are admissible but not which *numbers* are
reachable, so the colour-weight blocker — that `span{1, σ₂}` is a 2-plane
inside the 4-dimensional `V_(2,1)` block — survives untouched. The refutation
is by derivation, not by measurement.

Stated for a bare `u : Aˣ` and an arbitrary codomain `K`: no order, no
topology, no algebraic structure on the target is used. Cyclicity alone is the
whole hypothesis. -/
theorem trace_conj_eq (tr : A → K) (hcyc : ∀ a b : A, tr (a * b) = tr (b * a))
    (u : Aˣ) (b : A) : tr ((u : A) * b * (↑u⁻¹ : A)) = tr b := by
  rw [hcyc ((u : A) * b) (↑u⁻¹ : A), ← mul_assoc]
  simp

/-- **…so conjugation enlarges no reachable set.** Packaging of the above for
the reachability question: if `S` is the set of interface values attainable by
monotone words and `tr b ∈ S`, then `tr (u b u⁻¹) ∈ S` as well. No `S` can grow
by admitting conjugates. -/
theorem conjugation_reaches_no_new_values (tr : A → K)
    (hcyc : ∀ a b : A, tr (a * b) = tr (b * a))
    (u : Aˣ) (b : A) (S : Set K) (hb : tr b ∈ S) :
    tr ((u : A) * b * (↑u⁻¹ : A)) ∈ S := by
  rw [trace_conj_eq tr hcyc u b]; exact hb

/-- **The ordering-dependence of the nuclear chain is NOT a trace defect.**

Bean `qou-c6gx` recorded that the dashboard's binding energy depends on the
hard-coded nucleon ordering (³He: `ppn` 6.7969 MeV vs `pnp` 7.7794 MeV) and read
it as a possible violation of trace invariance. It is not one. `ppn` carries the
bond multiset `{pp, pn}`; `pnp` carries `{pn, pn}`. Different multisets are
genuinely different links — *not* conjugates of one another — so different
traces are the correct answer.

Formally: an energy keyed on the bond multiset is automatically well defined on
any two orderings that induce the *same* multiset. When they induce different
ones, the values may legitimately differ, and the ill-posedness lies in the
*input* — a nucleus has no ordering — not in the trace.

That is evidence against the chain as a nuclear model (`qou-h7mh`), which is a
strictly different complaint from the one `qou-c6gx` filed. -/
theorem multiset_keyed_energy_well_defined
    {Ordering Bonds : Type*} (bonds : Ordering → Bonds) (E : Bonds → K)
    (o₁ o₂ : Ordering) (hsame : bonds o₁ = bonds o₂) :
    E (bonds o₁) = E (bonds o₂) := by
  rw [hsame]

end ConjugationInvariance

section MarkovRepeat

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- **Markov stabilisation on a REPEATED generator forces `z² = h·z + 1`.**

`interface_scalar` above takes `tr (W * σ) = z * tr W` as a hypothesis — its own
docstring flags this as an axiom standing in for Jones (1987), not a theorem. The
question this answers is *when that hypothesis may be assumed*, which the corpus
had not pinned down.

Take the word `W = σ` itself, i.e. the interface generator already occurring once
in the word it is being appended to. The Hecke quadratic then evaluates the
left-hand side outright, and stabilisation becomes an equation on `z` alone.

So stabilisation is not free: on a repeated generator it *forces* the Markov
parameter to be a root of `x² - h·x - 1`. Whether that root condition holds is a
property of the convention, settled for convention D below. -/
theorem markov_repeat_forces_quadratic
    (tr : A → R) (σ : A) (z h : R)
    (hadd : ∀ x y : A, tr (x + y) = tr x + tr y)
    (hsmul : ∀ (c : R) (x : A), tr (c • x) = c * tr x)
    (hq : σ * σ = h • σ + 1)
    (hone : tr (1 : A) = 1)
    (hσ : tr σ = z)
    (hrepeat : tr (σ * σ) = z * tr σ) :
    z * z = h * z + 1 := by
  have hlhs : tr (σ * σ) = h * tr σ + tr (1 : A) := by
    rw [hq, hadd, hsmul]
  rw [hrepeat, hσ, hone] at hlhs
  exact hlhs

end MarkovRepeat

section MarkovRepeatConventionD

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The convention-D defect `z² - h·z - 1` in closed form, with
`z = q³/(q²+1)` and `h = q - q⁻¹`.

Both quadratic factors are positive-definite over any linear ordered field
(`q² ± q + 1 = (q ± 1/2)² + 3/4`), so the defect is a *strictly negative* rational
function of `q` — it has no zero to be found by tuning the pin. -/
theorem conventionD_markov_defect (q : R) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1)) * (q ^ 3 / (q ^ 2 + 1))
        - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) - 1
      = -((q ^ 2 - q + 1) * (q ^ 2 + q + 1)) / (q ^ 2 + 1) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **The convention-D Markov parameter is never a root of `x² - h·x - 1`.**
The defect is strictly negative for every `q > 0`, so the equation
`markov_repeat_forces_quadratic` extracts can never be satisfied. -/
theorem conventionD_markov_defect_neg (q : R) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1)) * (q ^ 3 / (q ^ 2 + 1))
        - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) - 1 < 0 := by
  rw [conventionD_markov_defect q hq]
  apply div_neg_of_neg_of_pos
  · have h1 : 0 < q ^ 2 - q + 1 := by nlinarith [sq_nonneg (2 * q - 1)]
    have h2 : 0 < q ^ 2 + q + 1 := by positivity
    nlinarith [mul_pos h1 h2]
  · positivity

/-- **The once-only-occurrence condition is NECESSARY, for every `q`.**

Combining the two: if the interface generator already occurs in the word, Markov
stabilisation would force `z² = h·z + 1`, and convention D's `z` misses that by a
strictly negative amount at every `q > 0`. So `interface_scalar`'s hypothesis
**cannot** be assumed on a repeated generator — the collapse of the interface to
the single scalar `μ = a·z + b` is available only when the generator occurs once.

This is a scope-(b) structural exclusion and the invariant is cited: the defect's
closed form `-(q²-q+1)(q²+q+1)/(q²+1)²`, whose factors are positive-definite. It
is not a numerical near-miss at one pin.

Measured counterpart: `computations/probes/colour_weighting_markov_universality_probe.py`
(PR #6319) fits `k` in `tr_M ∝ (d + k)` from the traces alone and finds `k = z_D` to
`1e-48` on four canonical nuclear words — each of which uses its interface generator
exactly once — and finds the identity **breaks** (`k - z_D = 1.2285`) on the same
deuteron word with one extra `σ` on that generator. The Lean says why the control
had to come out that way. -/
theorem markov_stabilisation_fails_on_repeat
    {A : Type*} [Ring A] [Algebra R A]
    (tr : A → R) (σ : A) (q : R) (hq : 0 < q)
    (hadd : ∀ x y : A, tr (x + y) = tr x + tr y)
    (hsmul : ∀ (c : R) (x : A), tr (c • x) = c * tr x)
    (hhecke : σ * σ = (q - q⁻¹) • σ + 1)
    (hone : tr (1 : A) = 1)
    (hσ : tr σ = q ^ 3 / (q ^ 2 + 1)) :
    tr (σ * σ) ≠ (q ^ 3 / (q ^ 2 + 1)) * tr σ := by
  intro hrepeat
  have hquad := markov_repeat_forces_quadratic tr σ (q ^ 3 / (q ^ 2 + 1))
    (q - q⁻¹) hadd hsmul hhecke hone hσ hrepeat
  have hneg := conventionD_markov_defect_neg q hq
  linarith [hquad, hneg]

/-- **Closed form of the convention-D singlet (`T = 0`) projector weight (`qou-5d6k`).**
With `z = q³/(q² + 1)`, the antisymmetric projector trace `(q - z)/(q + q⁻¹)` simplifies
identically to `q²/(q² + 1)²`. -/
theorem mu_singlet_closed_form_conventionD (q : R) (hq : 0 < q) :
    (q - q ^ 3 / (q ^ 2 + 1)) / (q + q⁻¹) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  have hsum : q + q⁻¹ ≠ 0 := by
    have : 0 < q + q⁻¹ := by positivity
    exact ne_of_gt this
  field_simp
  ring

/-- **Closed form of the convention-D triplet (`T = 1`) projector weight (`qou-5d6k`).**
With `z = q³/(q² + 1)`, the symmetric projector trace `(z + q⁻¹)/(q + q⁻¹)` simplifies
identically to `(q⁴ + q² + 1)/(q² + 1)²`. -/
theorem mu_triplet_closed_form_conventionD (q : R) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1) + q⁻¹) / (q + q⁻¹) = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  have hsum : q + q⁻¹ ≠ 0 := by
    have : 0 < q + q⁻¹ := by positivity
    exact ne_of_gt this
  field_simp
  ring

/-- **Closed form of the convention-D stacked-crossing trace `h·z + 1` (`qou-5d6k`).**
With `h = q - q⁻¹` and `z = q³/(q² + 1)`, the stacked crossing `σ² = h·σ + 1` has
Markov trace `(q⁴ + 1)/(q² + 1)`. -/
theorem stacked_crossing_trace_conventionD (q : R) (hq : 0 < q) :
    (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) + 1 = (q ^ 4 + 1) / (q ^ 2 + 1) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hden : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

end MarkovRepeatConventionD

end QOU.QBeta.InterfaceScalar
