import QOU.MassTheory.TransverseSurfaceCurvature

/-!
# QOU.MassTheory.GermConnectionGaugeCovariance

**The germ `q`-curvature `F_q = ⟦δq_i, δq_j⟧` is NOT gauge-covariant, and the
transverse NA-Stokes pairing `Ω₂` inherits that failure exactly. The covariant
second-order object built from the germ is the cup square, and it is
*identically a coboundary* — hence zero in `H²`.**

Bean `qou-prjo`. Companion to
[`GermRootVectorGaugeFixing`](GermRootVectorGaugeFixing.lean) (single-generator
scope-(b)) and
[`TransversePairingClusterDecomposition`](TransversePairingClusterDecomposition.lean)
(the bilinear cluster decomposition).

## The question this file answers

[PR #4849](https://github.com/litlfred/qou/pull/4849) §2.3 recorded that the
germ `δq = q (∂_q ρ) ρ⁻¹` transforms **inhomogeneously** — like a connection,
not like a tensor — under a `q`-dependent change of representation basis, and
left open whether the pairing `Ω₂` is nevertheless covariant. It is not.

## What is proved (sorry-free, generic `Ring R`)

Everything is stated for a bare **derivation** `D` of a ring `R` and **units**
of `R`. The substrate reading is `D = q ∂_q`, `R` = the matrix algebra of a
Hecke representation, `u = ρ(σ_i)`, `b = B(q)` the `q`-dependent basis change;
but no such interpretation is needed for the algebra.

| § | Result |
|---|---|
| 1 | `IsDeriv.map_one`, `IsDeriv.inv` — derivation basics |
| 2 | `germ_mul` — the germ is a **1-cocycle**: `α(uv) = α(u) + Ad(u) α(v)` |
| 3 | **`germ_conj`** — the **connection law**: `α ↦ Ad(b)(α + (1 − Ad u)Θ)`, `Θ = b⁻¹ D b` |
| 4 | **`germCurvature_conj`**, **`germCurvature_covariant_iff`** — covariance holds **iff** the defect vanishes |
| 5 | `listPairing_map_adAct`, `transversePairing_covariant_iff_curvature` — the pairing is covariant *given* covariant inputs, so **all** of the failure sits in `F_q` |
| 6 | **`gaugeDefect_witness`, `germCurvature_not_covariant`** — a concrete derivation, ring, and units where the defect is `!![X², −2X; 0, −X²] ≠ 0` |
| 7 | **`cupSq_eq_neg_coboundary`** — the cup square `⟦α(u), Ad(u)α(v)⟧` is *exactly* `−∂β` with the explicit primitive `β = D ∘ α` |
| 8 | `trace_germ_conj` — `τ(α(u))` **is** gauge-invariant for any cyclic trace `τ` |

## How to read the verdict

* §4 + §6: `F_q` is **not a tensor**. There is no basis-independent `‖Ω₂‖`, so
  the `0 … 897` spread of [#4798](https://github.com/litlfred/qou/pull/4798) and
  the `16.4×` germ-observer spread of #4849 are not merely *unchosen* — there is
  nothing to choose *between*, because the object has no invariant value.
* §7: the correct covariant second-order object exists and is the cup square in
  `H²(G; R_{Ad ρ})`. It vanishes identically — with an explicit primitive — so
  the *covariant* version of the order-2 transverse content is **zero**. The
  reason is structural: `D` is a derivation in a **single** direction (`q`), and
  a curvature needs two independent base directions; the generator indices
  `i, j` are group elements, not base directions.
* §8: the surviving gauge-invariant linear functional of the germ is
  `τ(α(u)) = D log det ρ(u)`, which sees only the abelianisation — i.e. exactly
  the writhe/framing datum already walled by `no_writhe_only_framing`.

## What is NOT proved — read before citing

* **`sorry-free ≠ derived`.** No binding energy, no `Δ_λ`, no magnitude, no
  `q₀`, no AME comparison appears in this file. Nothing is wired.
* §6 exhibits **one** ring/derivation/unit triple with a nonzero defect. That
  refutes "the defect vanishes identically"; it does not compute the defect for
  the Hecke germ (the probe
  `computations/probes/nastokes_germ_gauge_covariance_probe.py` does that,
  exactly over `ℚ(q)`).
* §7 shows the canonical covariant *second-order* object vanishes. It does
  **not** show that no nonzero gauge-invariant functional of the germ exists —
  §8 exhibits one (an abelian one). Classifying all of them is open.

**Base ring (§7c).** Generic non-commutative `Ring R` throughout §§1–5, 7–8.
§6's witness ring is `Matrix (Fin 2) (Fin 2) (Polynomial ℚ)` — a concrete
counterexample carrier, not an archimedean specialisation: no `ℝ`, no ordering,
no `Real.*` anywhere in the file.

## References
- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian multiplicative
  integration and Stokes' theorem on surfaces.
- Ref: [leitner2026] `docs/audits/2026-08-09-germ-gauge-covariance-verdict.md`
-/

namespace QOU.MassTheory.GermConnectionGauge

open QOU.MassTheory.TransverseSurfaceCurvature

variable {R : Type*} [Ring R]

/-! ## 1. Derivations -/

/-- A derivation of a ring, as a bare predicate on a function (no module or
    algebra structure required). The substrate reading is `D = q ∂_q`. -/
structure IsDeriv (D : R → R) : Prop where
  map_add : ∀ x y, D (x + y) = D x + D y
  leibniz : ∀ x y, D (x * y) = D x * y + x * D y

namespace IsDeriv

variable {D : R → R}

theorem map_zero (hD : IsDeriv D) : D 0 = 0 := by
  have h := hD.map_add 0 0
  rw [add_zero] at h
  exact self_eq_add_left.mp h

theorem map_one (hD : IsDeriv D) : D 1 = 0 := by
  have h := hD.leibniz 1 1
  simp only [one_mul, mul_one] at h
  exact self_eq_add_left.mp h

/-- Leibniz forces the inverse rule `D(u⁻¹) = −u⁻¹ (D u) u⁻¹`. -/
theorem inv (hD : IsDeriv D) (u : Rˣ) :
    D ((u⁻¹ : Rˣ) : R) = -(((u⁻¹ : Rˣ) : R) * D (u : R) * ((u⁻¹ : Rˣ) : R)) := by
  have h := hD.leibniz ((u : R)) (((u⁻¹ : Rˣ) : R))
  rw [Units.mul_inv, hD.map_one] at h
  have h3 : (u : R) * D ((u⁻¹ : Rˣ) : R) = -(D (u : R) * ((u⁻¹ : Rˣ) : R)) :=
    eq_neg_of_add_eq_zero_right h.symm
  calc D ((u⁻¹ : Rˣ) : R)
      = ((u⁻¹ : Rˣ) : R) * ((u : R) * D ((u⁻¹ : Rˣ) : R)) := by
        rw [← mul_assoc, Units.inv_mul, one_mul]
    _ = ((u⁻¹ : Rˣ) : R) * (-(D (u : R) * ((u⁻¹ : Rˣ) : R))) := by rw [h3]
    _ = -(((u⁻¹ : Rˣ) : R) * D (u : R) * ((u⁻¹ : Rˣ) : R)) := by
        rw [mul_neg, ← mul_assoc]

end IsDeriv

/-! ## 2. The germ is a 1-cocycle for the adjoint action -/

/-- The adjoint action of a unit. -/
def adAct (u : Rˣ) (x : R) : R := (u : R) * x * ((u⁻¹ : Rˣ) : R)

theorem adAct_add (u : Rˣ) (x y : R) : adAct u (x + y) = adAct u x + adAct u y := by
  simp only [adAct, mul_add, add_mul]

theorem adAct_sub (u : Rˣ) (x y : R) : adAct u (x - y) = adAct u x - adAct u y := by
  simp only [adAct, mul_sub, sub_mul]

theorem adAct_mul (u : Rˣ) (x y : R) : adAct u (x * y) = adAct u x * adAct u y := by
  have h : ((u⁻¹ : Rˣ) : R) * (u : R) = 1 := Units.inv_mul u
  simp only [adAct]
  calc (u : R) * (x * y) * ((u⁻¹ : Rˣ) : R)
      = (u : R) * x * ((((u⁻¹ : Rˣ) : R) * (u : R)) * y) * ((u⁻¹ : Rˣ) : R) := by
        rw [h]; noncomm_ring
    _ = ((u : R) * x * ((u⁻¹ : Rˣ) : R)) * ((u : R) * y * ((u⁻¹ : Rˣ) : R)) := by
        noncomm_ring

theorem adAct_curvComm (u : Rˣ) (x y : R) :
    adAct u (curvComm x y) = curvComm (adAct u x) (adAct u y) := by
  simp only [curvComm, adAct_sub, adAct_mul]

theorem adAct_neg (u : Rˣ) (x : R) : adAct u (-x) = -adAct u x := by
  simp only [adAct, neg_mul, mul_neg]

theorem adAct_one (x : R) : adAct (1 : Rˣ) x = x := by
  simp [adAct]

theorem adAct_comp (b u : Rˣ) (x : R) : adAct (b * u) x = adAct b (adAct u x) := by
  have hval : ((b * u : Rˣ) : R) = (b : R) * (u : R) := rfl
  have hinv : (((b * u)⁻¹ : Rˣ) : R) = ((u⁻¹ : Rˣ) : R) * ((b⁻¹ : Rˣ) : R) := by
    rw [mul_inv_rev]; rfl
  simp only [adAct, hval, hinv]
  noncomm_ring

theorem adAct_inv_adAct (b : Rˣ) (x : R) : adAct b⁻¹ (adAct b x) = x := by
  rw [← adAct_comp, inv_mul_cancel, adAct_one]

/-- Conjugation is injective, so an identity of conjugates descends. -/
theorem adAct_injective (b : Rˣ) {x y : R} (h : adAct b x = adAct b y) : x = y := by
  have h' := congrArg (adAct b⁻¹) h
  rwa [adAct_inv_adAct, adAct_inv_adAct] at h'

/-- The **germ** (right logarithmic derivative) of a unit:
    `α(u) = (D u) u⁻¹`. Substrate reading: `δq_i = q (∂_q ρ(σ_i)) ρ(σ_i)⁻¹`. -/
def germ (D : R → R) (u : Rˣ) : R := D (u : R) * ((u⁻¹ : Rˣ) : R)

/-- **The germ is a 1-cocycle**: `α(uv) = α(u) + Ad(u) α(v)`. This is the
    statement that `α` represents a class in `H¹(G; R_{Ad})` once one quotients
    by coboundaries — which §3 shows is exactly the gauge freedom. -/
theorem germ_mul {D : R → R} (hD : IsDeriv D) (u v : Rˣ) :
    germ D (u * v) = germ D u + adAct u (germ D v) := by
  have hval : ((u * v : Rˣ) : R) = (u : R) * (v : R) := rfl
  have hinv : (((u * v)⁻¹ : Rˣ) : R) = ((v⁻¹ : Rˣ) : R) * ((u⁻¹ : Rˣ) : R) := by
    rw [mul_inv_rev]; rfl
  have hv : (v : R) * ((v⁻¹ : Rˣ) : R) = 1 := Units.mul_inv v
  simp only [germ, adAct, hval, hinv, hD.leibniz]
  calc (D (u : R) * (v : R) + (u : R) * D (v : R)) *
        (((v⁻¹ : Rˣ) : R) * ((u⁻¹ : Rˣ) : R))
      = D (u : R) * ((v : R) * ((v⁻¹ : Rˣ) : R)) * ((u⁻¹ : Rˣ) : R)
        + (u : R) * (D (v : R) * ((v⁻¹ : Rˣ) : R)) * ((u⁻¹ : Rˣ) : R) := by
        noncomm_ring
    _ = D (u : R) * ((u⁻¹ : Rˣ) : R)
        + (u : R) * (D (v : R) * ((v⁻¹ : Rˣ) : R)) * ((u⁻¹ : Rˣ) : R) := by
        rw [hv, mul_one]

/-! ## 3. The gauge law — the germ transforms as a CONNECTION -/

/-- The gauge potential of a `q`-dependent basis change `b`: `Θ = b⁻¹ (D b)`. -/
def gaugePotential (D : R → R) (b : Rˣ) : R := ((b⁻¹ : Rˣ) : R) * D (b : R)

/-- The inhomogeneous shift `(1 − Ad u) Θ` picked up by the germ at `u`. -/
def gaugeShift (D : R → R) (b u : Rˣ) : R :=
    gaugePotential D b - adAct u (gaugePotential D b)

/-- `α(b) = Ad(b) Θ` — the germ of the gauge element is its own potential,
    conjugated. -/
theorem germ_eq_adAct_gaugePotential {D : R → R} (b : Rˣ) :
    germ D b = adAct b (gaugePotential D b) := by
  simp only [germ, adAct, gaugePotential]
  rw [← mul_assoc, Units.mul_inv, one_mul]

/-- `α(b⁻¹) = −Θ`. -/
theorem germ_inv {D : R → R} (hD : IsDeriv D) (b : Rˣ) :
    germ D b⁻¹ = -gaugePotential D b := by
  simp only [germ, gaugePotential, hD.inv b, inv_inv]
  rw [neg_mul, mul_assoc, Units.inv_mul, mul_one]

/-- **THE CONNECTION LAW.**

    Under the change of trivialisation `u ↦ b u b⁻¹` (a `q`-dependent change of
    representation basis, `b = B(q)`), the germ transforms **inhomogeneously**:

      `α(u) ↦ Ad(b) ( α(u) + (1 − Ad u) Θ )`,   `Θ = b⁻¹ (D b)`.

    The extra term vanishes exactly when `D b = 0`, i.e. when the basis change
    is `q`-independent. The Hoefsmit seminormal basis and the reduced-Burau
    basis are both `q`-dependent, and differ by such a `b`. -/
theorem germ_conj {D : R → R} (hD : IsDeriv D) (b u : Rˣ) :
    germ D (b * u * b⁻¹) = adAct b (germ D u + gaugeShift D b u) := by
  rw [germ_mul hD (b * u) b⁻¹, germ_mul hD b u, germ_inv hD b, adAct_comp,
    germ_eq_adAct_gaugePotential (D := D) b, gaugeShift]
  simp only [adAct_neg, adAct_add, adAct_sub]
  abel

/-! ## 4. The germ curvature is NOT a tensor -/

/-- The germ `q`-curvature at two observers: `F_q = ⟦α(u), α(v)⟧`. -/
def germCurvature (D : R → R) (u v : Rˣ) : R := curvComm (germ D u) (germ D v)

/-- The obstruction to covariance of `germCurvature` under the gauge `b`. -/
def gaugeDefect (D : R → R) (b u v : Rˣ) : R :=
    curvComm (germ D u) (gaugeShift D b v)
      + curvComm (gaugeShift D b u) (germ D v)
      + curvComm (gaugeShift D b u) (gaugeShift D b v)

/-- **The transformation law of the germ curvature.** It picks up the defect
    additively *inside* the conjugation: `F ↦ Ad(b)(F + Δ)`. -/
theorem germCurvature_conj {D : R → R} (hD : IsDeriv D) (b u v : Rˣ) :
    germCurvature D (b * u * b⁻¹) (b * v * b⁻¹)
      = adAct b (germCurvature D u v + gaugeDefect D b u v) := by
  simp only [germCurvature, gaugeDefect, germ_conj hD, ← adAct_curvComm, ← adAct_add]
  congr 1
  simp only [curvComm]
  noncomm_ring

/-- **COVARIANCE HOLDS IFF THE DEFECT VANISHES.** `germCurvature` is a tensor
    for the gauge `b` exactly when `gaugeDefect D b u v = 0`. §6 exhibits a
    concrete triple where it does not. -/
theorem germCurvature_covariant_iff {D : R → R} (hD : IsDeriv D) (b u v : Rˣ) :
    germCurvature D (b * u * b⁻¹) (b * v * b⁻¹) = adAct b (germCurvature D u v)
      ↔ gaugeDefect D b u v = 0 := by
  rw [germCurvature_conj hD]
  constructor
  · intro h; exact add_eq_left.mp (adAct_injective b h)
  · intro h; rw [h, add_zero]

/-! ## 5. The pairing inherits the failure exactly -/

/-- Conjugation commutes with the ordered transverse pairing. So the pairing is
    covariant **given** covariant inputs: every failure of covariance of `Ω₂`
    comes from the curvature `F_q`, none of it from the transports (which are
    products of `ρ`'s, hence genuinely tensorial) or from the pairing itself. -/
theorem listPairing_map_adAct (b : Rˣ) (l : List R) :
    listPairing (l.map (adAct b)) = adAct b (listPairing l) := by
  induction l with
  | nil => simp [listPairing, adAct]
  | cons c t ih =>
    have hrow : ∀ (c : R) (t : List R),
        rowPairing (adAct b c) (t.map (adAct b)) = adAct b (rowPairing c t) := by
      intro c t
      induction t with
      | nil => simp [rowPairing, adAct]
      | cons y ys ih2 =>
        simp only [List.map_cons, rowPairing, ih2, ← adAct_curvComm, ← adAct_add]
    simp only [List.map_cons, listPairing, ih, hrow, ← adAct_add]

/-- **The transverse pairing `Ω₂` is covariant iff the transported curvatures
    are unchanged.** Combined with §4 + §6: they are not, so `Ω₂` has no
    basis-independent value, and neither does any norm of it. -/
theorem transversePairing_covariant_iff (b : Rˣ) (l l' : List R) :
    listPairing (l'.map (adAct b)) = adAct b (listPairing l)
      ↔ listPairing l' = listPairing l := by
  rw [listPairing_map_adAct]
  exact ⟨fun h => adAct_injective b h, fun h => by rw [h]⟩

/-! ## 6. The defect is not identically zero — a concrete witness -/

section Witness

open Polynomial

/-- The witness ring: `2 × 2` matrices over `ℚ[X]`. Concrete counterexample
    carrier only — no archimedean content (§7c). -/
abbrev W : Type := Matrix (Fin 2) (Fin 2) (Polynomial ℚ)

/-- The witness derivation: entrywise `d/dX`. Substrate reading: `q ∂_q`. -/
noncomputable def dW (A : W) : W := A.map (Polynomial.derivative (R := ℚ))

theorem isDeriv_dW : IsDeriv dW := by
  constructor
  · intro A B
    ext i j
    simp [dW, Matrix.map_apply]
  · intro A B
    ext i j
    simp only [dW, Matrix.map_apply, Matrix.mul_apply, Matrix.add_apply,
      map_sum, Polynomial.derivative_mul]
    rw [Finset.sum_add_distrib]

/-- `u = !![1, X; 0, 1]`, a unipotent unit; `α(u) = E`. -/
noncomputable def uW : Wˣ :=
  ⟨!![1, X; 0, 1], !![1, -X; 0, 1], by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring, by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring⟩

/-- `v = !![1, 0; X, 1]`, the opposite unipotent unit; `α(v) = F`. -/
noncomputable def vW : Wˣ :=
  ⟨!![1, 0; X, 1], !![1, 0; -X, 1], by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring, by
      ext i j; fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_two] <;> ring⟩

theorem germ_uW : germ dW uW = !![0, 1; 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [germ, uW, dW, Matrix.map_apply, Matrix.mul_apply, Fin.sum_univ_two]

theorem germ_vW : germ dW vW = !![0, 0; 1, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [germ, vW, dW, Matrix.map_apply, Matrix.mul_apply, Fin.sum_univ_two]

theorem gaugePotential_uW : gaugePotential dW uW = !![0, 1; 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [gaugePotential, uW, dW, Matrix.map_apply, Matrix.mul_apply, Fin.sum_univ_two]

theorem gaugeShift_uW_uW : gaugeShift dW uW uW = 0 := by
  simp only [gaugeShift, gaugePotential_uW, adAct]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [uW, Matrix.mul_apply, Fin.sum_univ_two]

theorem gaugeShift_uW_vW : gaugeShift dW uW vW = !![X, 0; X * X, -X] := by
  simp only [gaugeShift, gaugePotential_uW, adAct]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [vW, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **THE WITNESS.** With the gauge `b = u` (a genuinely `X`-dependent basis
    change: `D b ≠ 0`), the covariance defect of the germ curvature is the
    explicit nonzero matrix `!![X², −2X; 0, −X²]`. -/
theorem gaugeDefect_witness :
    gaugeDefect dW uW uW vW = !![X * X, -(2 * X); 0, -(X * X)] := by
  simp only [gaugeDefect, gaugeShift_uW_uW, gaugeShift_uW_vW, germ_uW, germ_vW]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [curvComm, Matrix.mul_apply, Fin.sum_univ_two] <;> ring

/-- **`germCurvature` IS NOT GAUGE-COVARIANT.** There is a ring, a derivation,
    and units for which the defect is nonzero — hence, by
    `germCurvature_covariant_iff`, the curvature is not a tensor.

    This is the route-closing negative for the transverse NA-Stokes programme:
    `F_q = ⟦δq_i, δq_j⟧` has no basis-independent value, so neither does
    `Ω₂ = Σ J ⟦𝓕, 𝓕⟧` nor any norm of it. -/
theorem gaugeDefect_ne_zero : gaugeDefect dW uW uW vW ≠ 0 := by
  rw [gaugeDefect_witness]
  intro h
  have h00 := congrFun (congrFun h 0) 0
  simp at h00

theorem germCurvature_not_covariant :
    germCurvature dW (uW * uW * uW⁻¹) (uW * vW * uW⁻¹)
      ≠ adAct uW (germCurvature dW uW vW) := fun h =>
  gaugeDefect_ne_zero ((germCurvature_covariant_iff isDeriv_dW uW uW vW).mp h)

end Witness

/-! ## 7. The covariant object: the cup square is exactly a coboundary -/

/-- The bracket cup square of the germ 1-cocycle with itself:
    `(α ∪ α)(u,v) = ⟦α(u), Ad(u) α(v)⟧`. This — not `⟦α(u), α(v)⟧` — is the
    canonical second-order object attached to a 1-cocycle, and it descends to
    cohomology classes. -/
def cupSq (D : R → R) (u v : Rˣ) : R := curvComm (germ D u) (adAct u (germ D v))

/-- The group coboundary of a 1-cochain `β`. -/
def coboundary (β : Rˣ → R) (u v : Rˣ) : R := adAct u (β v) - β (u * v) + β u

/-- The **second germ** `β = D ∘ α`. Substrate reading: `q ∂_q (q ∂_q ρ · ρ⁻¹)`. -/
def secondGerm (D : R → R) (u : Rˣ) : R := D (germ D u)

/-- **A derivation fails to commute with the adjoint action by exactly one
    bracket against the germ**: `D(Ad_u x) = Ad_u(D x) + ⟦α(u), Ad_u x⟧`. This
    single identity is what makes the cup square a coboundary. -/
theorem D_adAct {D : R → R} (hD : IsDeriv D) (u : Rˣ) (x : R) :
    D (adAct u x) = adAct u (D x) + curvComm (germ D u) (adAct u x) := by
  have hu : ((u⁻¹ : Rˣ) : R) * (u : R) = 1 := Units.inv_mul u
  simp only [adAct, curvComm, germ]
  rw [hD.leibniz, hD.leibniz, hD.inv u]
  rw [show (D (u : R) * ((u⁻¹ : Rˣ) : R)) *
        ((u : R) * x * ((u⁻¹ : Rˣ) : R))
      = D (u : R) * x * ((u⁻¹ : Rˣ) : R) from by
      rw [show (D (u : R) * ((u⁻¹ : Rˣ) : R)) * ((u : R) * x * ((u⁻¹ : Rˣ) : R))
          = D (u : R) * (((u⁻¹ : Rˣ) : R) * (u : R)) * x * ((u⁻¹ : Rˣ) : R) from by
          noncomm_ring, hu, mul_one]]
  noncomm_ring

/-- The second germ fails the cocycle law by exactly the cup square. -/
theorem secondGerm_mul {D : R → R} (hD : IsDeriv D) (u v : Rˣ) :
    secondGerm D (u * v)
      = secondGerm D u + adAct u (secondGerm D v) + cupSq D u v := by
  calc secondGerm D (u * v) = D (germ D u + adAct u (germ D v)) := by
        rw [secondGerm, germ_mul hD]
    _ = D (germ D u) + D (adAct u (germ D v)) := hD.map_add _ _
    _ = D (germ D u)
          + (adAct u (D (germ D v)) + curvComm (germ D u) (adAct u (germ D v))) := by
        rw [D_adAct hD]
    _ = secondGerm D u + adAct u (secondGerm D v) + cupSq D u v := by
        simp only [secondGerm, cupSq]; abel

/-- **THE COVARIANT SECOND-ORDER OBJECT IS A COBOUNDARY.**

    `α ∪ α = −∂β` with the **explicit** primitive `β = D ∘ α`. Hence the class
    `[α] ∪ [α] ∈ H²(G; R_{Ad})` — the canonical gauge-invariant second-order
    object built from the germ — is **identically zero**, in every gauge and for
    every representation.

    **Reading.** `D` differentiates in a *single* direction; a curvature needs
    two independent base directions, and the generator indices `i, j` of
    `⟦δq_i, δq_j⟧` are group elements, not directions. So the transverse
    NA-Stokes construction has no nonvanishing covariant order-2 content: the
    naive `⟦δq_i, δq_j⟧` is not covariant (§4, §6), and the covariant
    replacement vanishes. -/
theorem cupSq_eq_neg_coboundary {D : R → R} (hD : IsDeriv D) (u v : Rˣ) :
    cupSq D u v = -coboundary (secondGerm D) u v := by
  rw [coboundary, secondGerm_mul hD]
  abel

/-! ## 8. What *is* gauge-invariant: the trace of the germ -/

/-- A cyclic trace is invariant under the adjoint action. -/
theorem trace_adAct {A : Type*} [AddCommGroup A] (τ : R →+ A)
    (hcyc : ∀ x y : R, τ (x * y) = τ (y * x)) (u : Rˣ) (x : R) :
    τ (adAct u x) = τ x := by
  simp only [adAct]
  rw [hcyc, ← mul_assoc, Units.inv_mul, one_mul]

/-- **The trace of the germ IS gauge-invariant.** `τ(α(u))` survives the
    connection law because the inhomogeneous term `(1 − Ad u) Θ` is
    trace-annihilated.

    Substrate reading: `τ(δq(w)) = q ∂_q log det ρ(w)`, which sees only
    `det ρ` — i.e. the abelianisation of the braid group, i.e. the writhe /
    framing. That is precisely the datum already walled by
    `no_writhe_only_framing`, so the surviving invariant linear functional of
    the germ carries no new information. -/
theorem trace_germ_conj {A : Type*} [AddCommGroup A] (τ : R →+ A)
    (hcyc : ∀ x y : R, τ (x * y) = τ (y * x)) {D : R → R} (hD : IsDeriv D)
    (b u : Rˣ) : τ (germ D (b * u * b⁻¹)) = τ (germ D u) := by
  rw [germ_conj hD, trace_adAct τ hcyc, gaugeShift, map_add, map_sub,
    trace_adAct τ hcyc, sub_self, add_zero]

end QOU.MassTheory.GermConnectionGauge
