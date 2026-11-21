import QOU.MathlibExt.FaddeevQuantumDilogarithm
import Mathlib.Tactic

/-!
# L4 — Cyclic-dilogarithm pentagon + Faddeev–Volkov uniqueness skeleton

Result **L4** of the Φ_b combinatorial (cyclotomic / tetraplectic) fibre workplan
(`docs/workplans/2026-07-13-phib-combinatorial-fibre-lean-workplan.md`, bean
`qou-evo7`). The pentagon / five-term relation is the standard functional
identity of the quantum dilogarithm; L4 uses it as the **uniqueness lever**:
*pentagon + inversion + unitarity + modular invariance pin `Φ_b` uniquely*
(Faddeev–Volkov rigidity), converting the keystone from an existence hunt into a
rigidity statement — the datum is *forced, not fitted*.

## Honest scope — outcome (B), with a fully-proved finite/lattice rigidity core

The **full operator pentagon** `Φ(𝗉)Φ(𝗊) = Φ(𝗊)Φ(𝗉+𝗊)Φ(𝗉)` is an identity in the
finite Weyl algebra at `ζ_N` (non-commuting `𝗉, 𝗊` with `𝗉𝗊 = ζ² 𝗊𝗉`); a genuine
scalar/commutative "pentagon" identity for `Φ : ℂ → ℂ` would be *false*, so this
file does **not** fabricate one. Instead it delivers, honestly:

* **(A-core, fully proved, sorry-free)** the *finite cyclic* Faddeev–Volkov
  rigidity — the finite-lattice heart of the uniqueness statement. A solution of
  the finite `N`-periodic multiplicative shift recursion (the cyclic quantum
  dilogarithm at `ζ_N`, `CyclotomicDilogCollapse`/L1 → `CyclicQuantumDilog`/L2)
  is **determined by its seed** (`solution_unique_of_seed`), equals the explicit
  partial product (`solution_eq_prod`), and — given the *pentagon closure*
  (`∏` over a full period `= 1`, the cyclotomic-collapse shadow of the pentagon,
  carried as an honest hypothesis in `PentagonClosure`) — is **`N`-periodic**
  (`PentagonClosure.solution_periodic`). No open input; pure finite algebra over
  a generic `CommRing`.

* **(A-core, fully proved)** the analytic *ambiguity is a periodic function*:
  the ratio of any two `FaddeevPhi` solutions is invariant under the full
  `ib`-shift (`ratio_ib_periodic`) — the concrete step showing the only freedom
  between two solutions is doubly-periodic, which is exactly what the pentagon's
  Liouville rigidity then kills.

* **(B, §3b-cond conditional theorem)** the *global* Faddeev–Volkov uniqueness.
  `PentagonRigidity` carries, as an **honest open hypothesis field**
  (`uniqueUpToScalar`), the analytic rigidity the pentagon buys per
  Faddeev–Kashaev — *every `FaddeevPhi` solution is a constant multiple of a
  fixed one* — which requires the doubly-periodic-⇒-constant (Liouville) step not
  available in Mathlib. `faddeevPhi_unique_of_pentagon` then **derives** genuine
  equality of two solutions from that hypothesis **plus a normalization point**
  (pinning the scalar). This is the §3b-cond pattern: the theorem proves the
  *implication* (rigidity-up-to-scalar + normalization ⇒ equality); the pentagon
  is honestly marked as the open input, not laundered as proved.

No `c_k` is produced or wired; registry untouched; scope-(a) throughout.

-- Ref: [faddeev_kashaev1994] Faddeev–Kashaev, "Quantum dilogarithm",
--        Mod. Phys. Lett. A 9 (1994) 427. https://doi.org/10.1142/S0217732394000447
-- Ref: [faddeev1995] Faddeev, "Discrete Heisenberg–Weyl group and modular group",
--        Lett. Math. Phys. 34 (1995) 249. https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] docs/workplans/2026-07-13-phib-combinatorial-fibre-lean-workplan.md (L4)
-/

namespace QOU.QBeta.CyclicDilogPentagon

open scoped BigOperators

/-! ## 1. Finite cyclic recursion rigidity (fully proved, generic `CommRing`)

Model a solution of the finite cyclic quantum dilogarithm on the shift lattice as
`f : ℕ → R` obeying the first-order multiplicative recursion `f (k+1) = w k · f k`
with shift multipliers `w : ℕ → R` (at `ζ_N` these are the `N`-periodic factor
family `1 + ζ^{2k+1} x`). The recursion determines `f` from its seed `f 0`, so two
solutions agreeing at the seed agree everywhere — the finite Faddeev–Volkov
rigidity. -/

variable {R : Type*} [CommRing R]

/-- **Explicit product form.** A solution of the multiplicative shift recursion is
its seed times the partial product of the multipliers. -/
theorem solution_eq_prod {w : ℕ → R} {f : ℕ → R}
    (hf : ∀ k, f (k + 1) = w k * f k) (k : ℕ) :
    f k = (∏ j ∈ Finset.range k, w j) * f 0 := by
  induction k with
  | zero => simp
  | succ n ih =>
      rw [hf n, ih, Finset.prod_range_succ]; ring

/-- **Shifted product form.** `f (k + m)` is `f k` times the product of the `m`
multipliers starting at `k`. -/
theorem solution_shift {w : ℕ → R} {f : ℕ → R}
    (hf : ∀ k, f (k + 1) = w k * f k) (k m : ℕ) :
    f (k + m) = (∏ j ∈ Finset.range m, w (k + j)) * f k := by
  induction m with
  | zero => simp
  | succ n ih =>
      have hkm : k + (n + 1) = (k + n) + 1 := by ring
      rw [hkm, hf (k + n), ih, Finset.prod_range_succ]; ring

/-- **Finite cyclic Faddeev–Volkov rigidity (seed uniqueness).** Two solutions of
the same finite multiplicative shift recursion that agree at the seed agree
everywhere. This is the finite-lattice heart of the uniqueness statement — no
open input. -/
theorem solution_unique_of_seed {w : ℕ → R} {f g : ℕ → R}
    (hf : ∀ k, f (k + 1) = w k * f k) (hg : ∀ k, g (k + 1) = w k * g k)
    (h0 : f 0 = g 0) : ∀ k, f k = g k := by
  intro k
  rw [solution_eq_prod hf, solution_eq_prod hg, h0]

/-! ## 2. Pentagon closure ⇒ cyclic periodicity (finite pentagon shadow, used)

At `q = ζ_N` the multiplier family is `N`-periodic and the product over a full
period trivialises (`= 1`) — the finite (cyclotomic-collapse) shadow of the
pentagon / five-term relation. The full operator pentagon is **not** proved
(open input, §3b); `PentagonClosure` carries its finite consequence as an honest
hypothesis, which is genuinely *used* to derive `N`-periodicity of any solution. -/

/-- **Pentagon closure datum.** The finite consequence of the pentagon at `ζ_N`:
`N`-periodic multipliers whose full-period product is `1`. Honest open
hypothesis (the operator pentagon itself is not formalised here). -/
structure PentagonClosure (R : Type*) [CommRing R] where
  /-- Cyclic order (the `N` of `ζ_N`; `N = 5` is Bring's tetraplectic modulus). -/
  N : ℕ
  /-- Shift multipliers of the finite cyclic quantum dilogarithm. -/
  w : ℕ → R
  /-- `N`-periodicity of the multiplier family. -/
  period : ∀ k, w (k + N) = w k
  /-- Full-period product trivialises — the cyclotomic-collapse / pentagon
  closure. -/
  closure : ∀ k, (∏ j ∈ Finset.range N, w (k + j)) = 1

/-- **Cyclic periodicity of a solution.** Given the pentagon closure, any solution
of the recursion is `N`-periodic — it descends to a genuine function on the
cyclic lattice `ℤ/N`. Uses `closure` essentially. -/
theorem solution_periodic (P : PentagonClosure R) {f : ℕ → R}
    (hf : ∀ k, f (k + 1) = P.w k * f k) (k : ℕ) :
    f (k + P.N) = f k := by
  rw [solution_shift hf k P.N, P.closure k, one_mul]

/-! ## 3. Analytic ambiguity is `ib`-periodic (fully proved)

The concrete analytic step underlying Faddeev–Volkov rigidity: two `FaddeevPhi`
solutions at the same modular parameter `b` solve the *same* first-order
quasi-period recursion `Ψ z = P z · Ψ (z + ib)` (`phi_b_quasiperiod`), so the
shared prefactor `P` cancels in the ratio and `Φ₁/Φ₂` is `ib`-periodic. The only
freedom is thus a doubly-periodic function; the pentagon's Liouville rigidity
(§4) is exactly what forces it constant. -/

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm

/-- **Ratio `ib`-periodicity.** For two `FaddeevPhi` solutions at the same `b`,
the ratio `Φ₁/Φ₂` is invariant under the full `ib`-shift wherever the shared
quasi-period prefactor is nonzero. -/
theorem ratio_ib_periodic {b : ℂ} {Φ₁ Φ₂ : ℂ → ℂ}
    [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂] (z : ℂ)
    (hP : (1 : ℂ) + Complex.exp (I * (Real.pi : ℂ) * (b : ℂ) ^ 2)
            * Complex.exp (2 * (Real.pi : ℂ) * b * z) ≠ 0) :
    Φ₁ z / Φ₂ z = Φ₁ (z + I * b) / Φ₂ (z + I * b) := by
  rw [phi_b_quasiperiod (b := b) (Φ := Φ₁) z, phi_b_quasiperiod (b := b) (Φ := Φ₂) z,
    mul_div_mul_left _ _ hP]

/-- **Dual quasi-periodicity under the full `i/b`-shift** (the `1/b`-shift applied
at `z + i/(2b)`), guarded off the dual pole lattice — the modular-dual companion
of `phi_b_quasiperiod`:
`Φ_b(z) = (1 + e^{2π(z + i/(2b))/b})·Φ_b(z + i/b)`. -/
theorem phi_binv_quasiperiod {b : ℂ} {Φ : ℂ → ℂ} [h : FaddeevPhi b Φ] (z : ℂ)
    (hpre : (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0) :
    Φ z = (1 + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b)) * Φ (z + I / b) := by
  have key := h.shift_binv (z + I / (2 * b)) hpre
  have e1 : (z + I / (2 * b)) - I / (2 * b) = z := by ring
  have e2 : (z + I / (2 * b)) + I / (2 * b) = z + I / b := by ring
  rw [e1, e2] at key
  exact key

/-- **Dual ratio `i/b`-periodicity** (modular-dual companion of
`ratio_ib_periodic`). For two `FaddeevPhi` solutions at the same `b`, the ratio
`Φ₁/Φ₂` is invariant under the full `i/b`-shift wherever the shared dual
quasi-period prefactor is nonzero.

Together with `ratio_ib_periodic` (invariance under `ib`) this proves the
inter-solution ambiguity `Φ₁/Φ₂` is **doubly periodic** for the lattice
`⟨ib, i/b⟩` — the exact structural input the Faddeev–Volkov (Liouville) step
consumes to force `uniqueUpToScalar`. This sharpens `PentagonRigidity`'s open
field: the remaining gap is *precisely* "doubly-periodic ⇒ constant", which
additionally needs holomorphicity/continuity of the ratio (NOT carried by the
`FaddeevPhi` conjecture-class, which axiomatizes only the difference equations)
and Mathlib's absent elliptic-function boundedness — see §4. Nothing here
closes that gap; this only makes the double-periodicity explicit and proved. -/
theorem ratio_ibinv_periodic {b : ℂ} {Φ₁ Φ₂ : ℂ → ℂ}
    [FaddeevPhi b Φ₁] [FaddeevPhi b Φ₂] (z : ℂ)
    (hpre : (1 : ℂ) + Complex.exp (2 * (Real.pi : ℂ) * (z + I / (2 * b)) / b) ≠ 0) :
    Φ₁ z / Φ₂ z = Φ₁ (z + I / b) / Φ₂ (z + I / b) := by
  rw [phi_binv_quasiperiod (b := b) (Φ := Φ₁) z hpre,
    phi_binv_quasiperiod (b := b) (Φ := Φ₂) z hpre,
    mul_div_mul_left _ _ hpre]

/-! ## 4. Conditional global Faddeev–Volkov uniqueness (§3b-cond)

`PentagonRigidity` carries the analytic rigidity the pentagon buys per
Faddeev–Kashaev — *every `FaddeevPhi` solution is a scalar multiple of a fixed
one* — as an **honest open hypothesis** (`uniqueUpToScalar`; it needs the
doubly-periodic-⇒-constant Liouville step not in Mathlib). The theorem then
**derives** genuine equality of two solutions from that hypothesis plus a
normalization point, which pins the scalar. Proves the *implication*; marks the
pentagon as the open input. -/

/-- **Pentagon-rigidity datum (§3b, open input).** For a fixed nowhere-zero
`FaddeevPhi` reference solution `Φ` at `b`, the field `uniqueUpToScalar` records
Faddeev–Volkov rigidity: any `FaddeevPhi` solution is a *constant* multiple of
`Φ`. This is the analytic content the pentagon / five-term relation supplies
(Faddeev–Kashaev); it is **not** proved here — the Liouville step is the open
input. -/
structure PentagonRigidity (b : ℂ) (Φ : ℂ → ℂ) : Prop where
  /-- `Re b > 0`. -/
  hb : 0 < b.re
  /-- The reference solution is nowhere zero. -/
  nonzero : ∀ z, Φ z ≠ 0
  /-- **Rigidity up to scalar** — the pentagon's Faddeev–Volkov content (open). -/
  uniqueUpToScalar : ∀ Ψ : ℂ → ℂ, FaddeevPhi b Ψ → (∀ z, Ψ z ≠ 0) →
      ∃ c : ℂ, ∀ z, Ψ z = c * Φ z

/-- **Conditional Faddeev–Volkov uniqueness.** Assuming pentagon rigidity
(`PentagonRigidity`, the open input) for a reference `Φ`, any two nowhere-zero
`FaddeevPhi` solutions that agree at a single normalization point `z₀` are
**equal** everywhere. Genuine derivation: rigidity gives `Φ₁ = c₁·Φ`, `Φ₂ = c₂·Φ`;
the normalization at `z₀` (with `Φ z₀ ≠ 0`) forces `c₁ = c₂`; hence `Φ₁ = Φ₂`.

This proves the *implication* — the pentagon (via `uniqueUpToScalar`) is an
explicit hypothesis, not a proved fact. It converts the keystone into rigidity:
the datum is forced by pentagon + normalization, not fitted. -/
theorem faddeevPhi_unique_of_pentagon {b : ℂ} {Φ Φ₁ Φ₂ : ℂ → ℂ}
    (hR : PentagonRigidity b Φ)
    (h₁ : FaddeevPhi b Φ₁) (h₂ : FaddeevPhi b Φ₂)
    (hn₁ : ∀ z, Φ₁ z ≠ 0) (hn₂ : ∀ z, Φ₂ z ≠ 0)
    {z₀ : ℂ} (hnorm : Φ₁ z₀ = Φ₂ z₀) :
    Φ₁ = Φ₂ := by
  obtain ⟨c₁, hc₁⟩ := hR.uniqueUpToScalar Φ₁ h₁ hn₁
  obtain ⟨c₂, hc₂⟩ := hR.uniqueUpToScalar Φ₂ h₂ hn₂
  have hz₀ : c₁ * Φ z₀ = c₂ * Φ z₀ := by rw [← hc₁ z₀, ← hc₂ z₀]; exact hnorm
  have hceq : c₁ = c₂ := mul_right_cancel₀ (hR.nonzero z₀) hz₀
  funext z
  rw [hc₁ z, hc₂ z, hceq]

end QOU.QBeta.CyclicDilogPentagon
