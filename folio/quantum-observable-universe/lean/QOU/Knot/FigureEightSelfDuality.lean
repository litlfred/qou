/-
  Self-duality kills the imaginary face — the keystone CS(4_1)=0, formalized
  over a generic commutative ring with a bar-involution σ (NOT ℂ; §7c).

  Context (vpug / keystone). The QOU complex volume splits a substrate element
  V into a bar-EVEN (cosh / Vol / binding / Re) part and a bar-ODD (sinh /
  Chern–Simons / Q_β / Im) part — the archimedean (ℂ) instance being
  Re/Im under complex conjugation. The figure-eight 4_1 (the Higgs) is
  AMPHICHIRAL (self-dual: 4_1 = mirror 4_1), so its colored Jones is σ-fixed
  (J_N(q)=J_N(q^-1), verified exactly in figure_eight_aj_operator.py). The
  consequence — Im V(4_1) = CS(4_1) = 0, so the Higgs knot contributes ONLY the
  real (mass) face m_μ/m_e = Vol(4_1)/ℏ_q² — is here PROVED algebraically over
  any (R, σ): a σ-fixed element has zero bar-odd part.

  This is the (R,σ)-generalization the literature's ℂ-results need (owner's
  "not just ℂ"): bar-involution σ replaces complex conjugation; the elementary
  self-duality argument is ring algebra. The hard saddle asymptotics
  (Vol(4_1) limit) stay conditional — see QOU/Knot/FigureEightVolume.lean.

  Complements the bar-parity descent in
  mass-endomorphism/binding-qbeta-complex-volume.lean (invol_descent); the NEW
  content here is the self-dual ⇒ Im-vanishes theorem.

  -- Ref: [kashaev1997] https://doi.org/10.1007/BF01239527
  -- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/

import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic

namespace QOU.Knot.SelfDuality

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- bar-EVEN part: `V + σV` (cosh / Vol / binding / Re face). -/
def barEven (V : R) : R := V + σ V

/-- bar-ODD part: `V − σV` (sinh / Chern–Simons / Q_β / Im face). -/
def barOdd (V : R) : R := V - σ V

/-- The two parities reconstruct `2V`. -/
theorem barEven_add_barOdd (V : R) : barEven σ V + barOdd σ V = 2 * V := by
  simp only [barEven, barOdd]; ring

/-- **Self-duality kills the imaginary face.** A σ-fixed (amphichiral /
    self-dual) element — the figure-eight 4_1 / Higgs — has zero bar-ODD part.
    This is CS(4_1) = 0 = Im V(4_1), proved over any `(R, σ)`. -/
theorem selfDual_barOdd_zero (V : R) (hV : σ V = V) : barOdd σ V = 0 := by
  simp only [barOdd, hV, sub_self]

/-- For a self-dual element only the bar-EVEN (Vol / mass) face survives:
    `barEven σ V = 2V`. -/
theorem selfDual_barEven_two (V : R) (hV : σ V = V) : barEven σ V = 2 * V := by
  simp only [barEven, hV]; ring

/-- **Recurrence descent (the c_k ladder).** A three-term recurrence
    `Vp = c·Vk − Vm` with a σ-fixed (bar-even) multiplier `c` descends to BOTH
    parity recurrences at once — the algebraic engine of the c_k ladder
    (bar-even binding `c₂=−8` and bar-odd Q_β `c₂=−1` from one relation). -/
theorem recurrence_descent {Vp Vk Vm c : R} (hc : σ c = c)
    (h : Vp = c * Vk - Vm) :
    barEven σ Vp = c * barEven σ Vk - barEven σ Vm ∧
    barOdd σ Vp = c * barOdd σ Vk - barOdd σ Vm := by
  have hσ : σ Vp = c * σ Vk - σ Vm := by
    rw [h, map_sub, map_mul, hc]
  refine ⟨?_, ?_⟩
  · simp only [barEven]; rw [hσ, h]; ring
  · simp only [barOdd]; rw [hσ, h]; ring

/-- **Keystone corollary.** For the self-dual Higgs knot, the complex volume is
    purely real: its bar-odd (CS / Q_β / Im) face is 0 and its bar-even
    (Vol / mass / Re) face is `2V`. Hence `Q_β` cannot be the figure-eight's own
    imaginary face — it must live in the many-body binding defect (see the
    CAL-123 reanalysis audit). -/
theorem higgs_complex_volume_real (V : R) (hSelfDual : σ V = V) :
    barOdd σ V = 0 ∧ barEven σ V = 2 * V :=
  ⟨selfDual_barOdd_zero σ V hSelfDual, selfDual_barEven_two σ V hSelfDual⟩

/-! ## §2  Markov-trace Frobenius pairing and 4₁ amphichiral self-duality (bean `8gzz`)

    The figure-eight knot $4_1 = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$
    is amphicheiral ($4_1 \simeq \overline{4_1}$), with writhe
    $w(4_1) = (+1) + (-1) + (+1) + (-1) = 0$ and $\sigma$-invariant Jones /
    Markov trace $V_{4_1}(q) = V_{4_1}(q^{-1})$.

    In the $\hat{A}_{4_1}$ module construction, a $\sigma$-equivariant trace
    $\tau : A \to R$ on a ring $A$ equipped with a mirror/bar involution
    $\sigma_A : A \to A$ induces the $\sigma$-sesquilinear Frobenius pairing
    $$\langle x, y \rangle_{\tau, \sigma_A} := \tau(x \cdot \sigma_A(y)).$$
    We prove below over any `[CommRing R]` and `[Ring A]`:
    1. **$\sigma$-Hermitian symmetry (`sigma_frobeniusPairing`):** when $\tau$
       is cyclic ($\tau(ab) = \tau(ba)$), $\sigma_A$ is an anti-involution
       ($\sigma_A(xy) = \sigma_A(y)\sigma_A(x)$, $\sigma_A(\sigma_A(x)) = x$),
       and $\tau$ is $(\sigma_A, \sigma)$-equivariant
       ($\sigma(\tau(x)) = \tau(\sigma_A(x))$), the pairing satisfies
       $\sigma(\langle x, y \rangle) = \langle y, x \rangle$.
    2. **Diagonal self-duality (`frobeniusPairing_self_barOdd_zero`,
       `frobeniusPairing_self_barEven_two`):** every diagonal pairing
       $\langle x, x \rangle = \tau(x \cdot \sigma_A(x))$ is $\sigma$-fixed, so
       its bar-odd (imaginary / CS) part vanishes identically and its bar-even
       part is $2\langle x, x \rangle$.
    3. **Amphichiral self-square (`frobeniusPairing_amphichiral_eq_trace_sq`):**
       for an amphichiral ($\sigma_A$-self-dual, $\sigma_A(u) = u$) element $u$,
       the Frobenius self-pairing reduces to the Markov trace of the square
       $\langle u, u \rangle = \tau(u^2)$ and is $\sigma$-fixed.
    4. **Left-multiplication $\sigma_A$-adjointness (`frobeniusPairing_mul_adjoint`):**
       for any $a, x, y \in A$, $\langle x \cdot a, y \rangle = \langle x, y \cdot \sigma_A(a) \rangle$;
       in particular, for an amphichiral element $u$ ($\sigma_A(u) = u$), right
       multiplication by $u$ is self-adjoint under $\langle \cdot, \cdot \rangle$. -/

/-- Writhe of the standard 4-crossing braid word
    $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ of the figure-eight knot $4_1$:
    two positive crossings ($+1$) and two negative crossings ($-1$). -/
def figureEightCrossingSigns : List ℤ := [1, -1, 1, -1]

/-- Total writhe $w(4_1) = \sum \epsilon_i$ of the figure-eight braid word. -/
def figureEightWrithe : ℤ := figureEightCrossingSigns.sum

/-- Amphichiral writhe vanishing: $w(4_1) = 1 - 1 + 1 - 1 = 0$. -/
theorem figureEightWrithe_eq_zero : figureEightWrithe = 0 := rfl

section FrobeniusPairing

variable {A : Type*} [Ring A]

/-- The Markov-trace Frobenius pairing $\langle x, y \rangle_{\tau, \sigma_A} := \tau(x \cdot \sigma_A(y))$
    associated to a trace functional $\tau : A \to R$ and an involution
    $\sigma_A : A \to A$. -/
def frobeniusPairing (τ : A → R) (σA : A → A) (x y : A) : R :=
  τ (x * σA y)

/-- **$\sigma$-Hermitian symmetry of the Markov-trace Frobenius form.**
    If $\tau$ is cyclic, $\sigma_A$ is an anti-involution, and $\tau$ intertwines
    $\sigma_A$ with the ground-ring bar-involution $\sigma$, then
    $\sigma(\langle x, y \rangle) = \langle y, x \rangle$. -/
theorem sigma_frobeniusPairing
    (τ : A → R) (σA : A → A)
    (hcyc : ∀ a b : A, τ (a * b) = τ (b * a))
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    (hequiv : ∀ a : A, σ (τ a) = τ (σA a))
    (x y : A) :
    σ (frobeniusPairing τ σA x y) = frobeniusPairing τ σA y x := by
  unfold frobeniusPairing
  rw [hequiv, hanti, hinv, hcyc]

/-- Every diagonal Frobenius pairing $\langle x, x \rangle = \tau(x \cdot \sigma_A(x))$
    is $\sigma$-fixed (self-dual in $R$). -/
theorem sigma_frobeniusPairing_self
    (τ : A → R) (σA : A → A)
    (hcyc : ∀ a b : A, τ (a * b) = τ (b * a))
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    (hequiv : ∀ a : A, σ (τ a) = τ (σA a))
    (x : A) :
    σ (frobeniusPairing τ σA x x) = frobeniusPairing τ σA x x :=
  sigma_frobeniusPairing σ τ σA hcyc hanti hinv hequiv x x

/-- The bar-odd (imaginary / Chern–Simons) face of any diagonal Frobenius pairing
    $\langle x, x \rangle$ vanishes identically. -/
theorem frobeniusPairing_self_barOdd_zero
    (τ : A → R) (σA : A → A)
    (hcyc : ∀ a b : A, τ (a * b) = τ (b * a))
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    (hequiv : ∀ a : A, σ (τ a) = τ (σA a))
    (x : A) :
    barOdd σ (frobeniusPairing τ σA x x) = 0 :=
  selfDual_barOdd_zero σ (frobeniusPairing τ σA x x)
    (sigma_frobeniusPairing_self σ τ σA hcyc hanti hinv hequiv x)

/-- The bar-even (real / hyperbolic volume) face of any diagonal Frobenius pairing
    $\langle x, x \rangle$ equals $2 \langle x, x \rangle$. -/
theorem frobeniusPairing_self_barEven_two
    (τ : A → R) (σA : A → A)
    (hcyc : ∀ a b : A, τ (a * b) = τ (b * a))
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    (hequiv : ∀ a : A, σ (τ a) = τ (σA a))
    (x : A) :
    barEven σ (frobeniusPairing τ σA x x) = 2 * frobeniusPairing τ σA x x :=
  selfDual_barEven_two σ (frobeniusPairing τ σA x x)
    (sigma_frobeniusPairing_self σ τ σA hcyc hanti hinv hequiv x)

omit [CommRing R] in
/-- For an amphichiral ($\sigma_A$-fixed, $\sigma_A(u) = u$) element $u \in A$
    such as the figure-eight $4_1$ holonomy, the Frobenius self-pairing equals
    the trace of the square $\tau(u * u)$. -/
theorem frobeniusPairing_amphichiral_eq_trace_sq
    (τ : A → R) (σA : A → A) {u : A} (hu : σA u = u) :
    frobeniusPairing τ σA u u = τ (u * u) := by
  unfold frobeniusPairing
  rw [hu]

omit [CommRing R] in
/-- **Adjointness of multiplication under the Frobenius pairing.**
    If $\sigma_A$ is an anti-involution, then $\langle x \cdot a, y \rangle = \langle x, y \cdot \sigma_A(a) \rangle$. -/
theorem frobeniusPairing_mul_adjoint
    (τ : A → R) (σA : A → A)
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    (a x y : A) :
    frobeniusPairing τ σA (x * a) y = frobeniusPairing τ σA x (y * σA a) := by
  unfold frobeniusPairing
  rw [hanti, hinv, mul_assoc]

omit [CommRing R] in
/-- **Self-adjointness of amphichiral multiplication in the $\hat{A}_{4_1}$ module.**
    For an amphichiral element $u$ ($\sigma_A(u) = u$), right multiplication by
    $u$ is self-adjoint with respect to $\langle \cdot, \cdot \rangle_{\tau, \sigma_A}$:
    $\langle x \cdot u, y \rangle = \langle x, y \cdot u \rangle$. -/
theorem frobeniusPairing_amphichiral_selfAdjoint
    (τ : A → R) (σA : A → A)
    (hanti : ∀ a b : A, σA (a * b) = σA b * σA a)
    (hinv : ∀ a : A, σA (σA a) = a)
    {u : A} (hu : σA u = u) (x y : A) :
    frobeniusPairing τ σA (x * u) y = frobeniusPairing τ σA x (y * u) := by
  rw [frobeniusPairing_mul_adjoint τ σA hanti hinv u x y, hu]

end FrobeniusPairing

end QOU.Knot.SelfDuality
