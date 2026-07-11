import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# Faddeev non-compact quantum dilogarithm `Φ_b` (modular double) — T3 scaffold

The **decay / bar-odd** face of the quantum dilogarithm, complementary to the
**compact** `Φ_q` (mass / bar-even) backbone formalized in
`QOU.MathlibExt.QuantumDilogarithm{,Infinite}` (T1).  This is the object the
open Q_β `c₃` bar-odd S-leak lives in (S ≈ `+0.00968` muon / `−0.03946` proton;
`docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`).

`Φ_b` is defined analytically by the contour integral
$$\Phi_b(z) = \exp\!\int_{\mathbb{R}+i0}
   \frac{e^{-2izw}}{4\sinh(wb)\,\sinh(w/b)}\,\frac{dw}{w},$$
which needs contour integration not available in Mathlib.  Per AGENTS.md §3b we
therefore **axiomatize `Φ_b` as a conjecture-class carrying its *real* defining
functional equations** (the existence of a function satisfying them is the open
input) and **derive consequences from those axioms** — nothing here constructs
`Φ_b`, and no numerical `c_k` value is produced or wired.

-- Ref: [faddeev1995] Faddeev, "Discrete Heisenberg–Weyl group and modular
--        group", Lett. Math. Phys. 34 (1995) 249. https://doi.org/10.1007/BF01872779
-- Ref: [faddeev1994] the quantum dilogarithm. https://doi.org/10.1007/BF02101594
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md
-/

namespace QOU.MathlibExt.FaddeevQuantumDilogarithm

open Complex

/-- **Faddeev `Φ_b` (conjecture-class, §3b).** `Φ : ℂ → ℂ` satisfies the two
modular-double `q`-difference equations of the non-compact quantum dilogarithm
at modular parameter `b > 0`:
$$\Phi_b(z - \tfrac{ib}{2}) = \bigl(1 + e^{2\pi b z}\bigr)\,\Phi_b(z + \tfrac{ib}{2}),
\qquad
\Phi_b(z - \tfrac{i}{2b}) = \bigl(1 + e^{2\pi z/b}\bigr)\,\Phi_b(z + \tfrac{i}{2b}).$$
The two relations are exchanged by `b ↔ 1/b`, encoding the **self-duality**
`Φ_b = Φ_{1/b}` — the structural feature the compact `Φ_q` (single relation)
lacks.  The `sorry`-free consequences below hold for *any* `Φ` in this class;
the open conjecture is that the integral `Φ_b` **is** such a `Φ`. -/
class FaddeevPhi (b : ℝ) (Φ : ℂ → ℂ) : Prop where
  /-- `b > 0`. -/
  hb : 0 < b
  /-- `b`-shift relation (the "compact half", same shape as `Φ_q`'s
  `q`-difference equation). -/
  shift_b : ∀ z : ℂ,
    Φ (z - I * (b / 2)) = (1 + Complex.exp (2 * (Real.pi : ℂ) * b * z)) * Φ (z + I * (b / 2))
  /-- `1/b`-shift relation (the **modular-dual** half, absent from compact `Φ_q`). -/
  shift_binv : ∀ z : ℂ,
    Φ (z - I / (2 * b)) = (1 + Complex.exp (2 * (Real.pi : ℂ) * z / b)) * Φ (z + I / (2 * b))

variable {b : ℝ} {Φ : ℂ → ℂ}

/-- **Derived zero locus (`b`-lattice).** From the `b`-shift axiom alone: wherever
the prefactor `1 + e^{2π b z}` vanishes, `Φ_b` has a zero.  This is the top edge
of `Φ_b`'s `b`-lattice of zeros — a genuine consequence of the functional
equation, not an assumption. -/
theorem phi_b_zero [h : FaddeevPhi b Φ] {z : ℂ}
    (hz : Complex.exp (2 * (Real.pi : ℂ) * b * z) = -1) :
    Φ (z - I * (b / 2)) = 0 := by
  rw [h.shift_b z, hz]; simp

/-- **Derived zero locus (`1/b`-lattice).** The modular-dual companion of
`phi_b_zero`, from the `1/b`-shift axiom. The two lattices together are the
`(mb + n/b)`-zero structure the compact `Φ_q` cannot reproduce. -/
theorem phi_binv_zero [h : FaddeevPhi b Φ] {z : ℂ}
    (hz : Complex.exp (2 * (Real.pi : ℂ) * z / b) = -1) :
    Φ (z - I / (2 * b)) = 0 := by
  rw [h.shift_binv z, hz]; simp

/-- **Ratio form of the `b`-shift** (where `Φ` does not vanish): the defining
quotient `Φ_b(z - ib/2) / Φ_b(z + ib/2) = 1 + e^{2π b z}`. -/
theorem phi_b_ratio [h : FaddeevPhi b Φ] (z : ℂ) (hne : Φ (z + I * (b / 2)) ≠ 0) :
    Φ (z - I * (b / 2)) / Φ (z + I * (b / 2)) = 1 + Complex.exp (2 * (Real.pi : ℂ) * b * z) := by
  rw [h.shift_b z, mul_div_assoc, div_self hne, mul_one]

/-- **Quasi-periodicity under the full `ib`-shift** (the `b`-shift applied at
`z + ib/2`):
$$\Phi_b(z) = \bigl(1 + q_b\,e^{2\pi b z}\bigr)\,\Phi_b(z + ib),
\qquad q_b := e^{i\pi b^2}.$$
This **surfaces the modular-double parameter `q_b = e^{iπ b²}`** — the T3↔T1
bridge datum: `q_b` is the `q` of the compact `Φ_q` (whose functional equation
`Φ_q(q²x) = (1+qx)Φ_q(x)` is the multiplicative shadow of this additive relation
under `x = e^{2πbz}`, `q² = q_b`). -/
theorem phi_b_quasiperiod [h : FaddeevPhi b Φ] (z : ℂ) :
    Φ z = (1 + Complex.exp (I * (Real.pi : ℂ) * (b : ℂ) ^ 2)
              * Complex.exp (2 * (Real.pi : ℂ) * b * z)) * Φ (z + I * b) := by
  have key := h.shift_b (z + I * (b / 2))
  have e1 : (z + I * ((b : ℂ) / 2)) - I * ((b : ℂ) / 2) = z := by ring
  have e2 : (z + I * ((b : ℂ) / 2)) + I * ((b : ℂ) / 2) = z + I * b := by ring
  have e3 : 2 * (Real.pi : ℂ) * b * (z + I * ((b : ℂ) / 2))
      = 2 * (Real.pi : ℂ) * b * z + I * (Real.pi : ℂ) * (b : ℂ) ^ 2 := by ring
  rw [e1, e2, e3, Complex.exp_add] at key
  rw [key]; ring

/-!
## The bar-odd source: chiral knot operators (Hopf-led) — argument-identification target

The bar involution `q ↦ q⁻¹` is the mirror/chirality operation
(`J_K(q⁻¹) = J_{mirror K}(q)`), so an operator's bar-ODD part is non-zero **iff it
is chiral** (parity ↔ chirality dictionary,
`docs/audits/2026-07-07-parity-chirality-dictionary-closed.md`):

* **amphichiral** operators (mirror-invariant, `CS = 0`) — e.g. the figure-8 `4₁`
  — have **zero** bar-odd part; they are the compact `Φ_q` **mass/bar-even** face
  (T1, the `−Vol(4₁)` datum).
* **chiral** operators — led by the **Hopf link** (2-crossing), and the torus
  knots `T(2,3) = 3₁` (electron), `T_{3,5}` (writhe mediator) — carry the bar-ODD
  part; they are the `Φ_b` **decay/bar-odd** face formalized here (T3).

The Hopf sector is the concrete carrier: the bar-odd datum collapses (in
`y = q² + q⁻²`) to `C_Hopf(y) = y³ − 6y² + 10y − 6`, discriminant `−76 < 0`
(complex-conjugate root pair), with `C_Hopf(2) = −2 = J_Hopf(q=1)` = the empirical
`c₃` near-match (`QOU.QBeta.HopfCubicOddCarrier`,
`content/.../mass-theory/qbeta-odd-carrier-hopf-cubic.md`).

**Caveat (Subgoal-2 boundary).** The Hopf **fibre** cubic is *anchor-invariant*
(cross-anchor swing `~10⁻⁸`), so the chiral operators supply the bar-odd
**carrier** but **not** the anchor-dependent `c₃` **S-leak**
(`S(muon) ≈ +0.00968`, `S(proton) ≈ −0.03946`;
`docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`). The remaining
keystone is to identify the `FaddeevPhi` argument whose archimedean evaluation at
each anchor reproduces `S` — i.e. to realize the chiral Hopf sector's
anchor-dependent leak through the `Φ_b` axioms above. That argument-identification
is **not** done here.

### Reconciliation with the landed algebraic/Gram results (2026-07-11)

A parallel line pins the same bar-odd carrier at the `H₃(q)` algebra level and
sharpens "chiral operators" to a **single algebraic mode**
(`docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`):

* The `σ`-parity (mass/decay) split of `e_k` is proved sorry-free in
  `QOU.QBeta.EkParitySplit` (`massProj` / `decayProj`); `S` is the `decayProj`
  (bar-odd) half.
* The Frobenius/Gram form `G_{ij} = tr_M(b_i b_j)` is **indefinite** (signature
  `5+, 1−`); the bar-odd `decayProj` lands **exactly** on the unique
  negative-norm **ghost mode `(L₊ − L₋)/√2`** (`|cos| = 1`), while the mass
  (bar-even) part sits in the positive/unitary cone.  So **decay ⊥ mass ⇒ decay
  = binding** (`Gram`-norm sign is the mass/binding split): this `Φ_b`/bar-odd
  face is the **binding** channel, an LP/SDP dual shadow-price mode, not a mass
  contribution.

So this analytic `Φ_b` axiomatization and the `H₃` Gram-ghost picture are two
faces of one object: `Φ_b` is the modular-double *analytic* carrier (with a
numerical evaluator validated vs Hikami), and `(L₊ − L₋)` is its `H₃`-algebraic
shadow.  The open link remains the same `z(q₀) → c_k` evaluation map that would
make either face reproduce the anchor-dependent `S`.
-/

end QOU.MathlibExt.FaddeevQuantumDilogarithm
