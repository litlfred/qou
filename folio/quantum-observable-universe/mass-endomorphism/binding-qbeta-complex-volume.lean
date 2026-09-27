import Mathlib.Data.Complex.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
-- `evenStep` / `oddStep` / `rotation_step` and `AWDeformationPath` were relocated
-- to the Lake tree so the content-block resolver finds them; `evenStep_map` and
-- `AWDeformationPath.channel_ladders` below still use them.
import QOU.MassEndomorphism.rotation_step
import QOU.MassEndomorphism.AWDeformationPath

/-!
# QOU.MassEndomorphism.ComplexVolumeUnification

Complex-volume unification of mass-binding and β-decay
([binding-qbeta-complex-volume.md](binding-qbeta-complex-volume.md)).

Binding `𝔈_bind` and the β-decay `𝔔_β` are the real and imaginary parts of a
single complex fibre observable — the complexified mass-endomorphism
convolution-defect `𝔙 = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ` — the QOU analogue of the
Neumann–Zagier complex volume `Vol(K) + i·CS(K)`.

Per the owner's observation ("in many ways this is definitional"), the
unification is taken **definitionally**: `𝔙 := E₀·tr_M((Π_free−1)∘𝓜)` (𝓜 = mass endomorphism in 𝐂, Π_free = idempotent projector onto the factorized sub-object, tr_M = categorical Markov trace — no braid words),
`𝔈_bind := Re 𝔙`, `𝔔_β := Im 𝔙`.  Then the unification
`𝔈_bind + i·𝔔_β = 𝔙` is a **theorem** (`Complex.re_add_im`), sorry-free.
The only conjectural content is the *physical match*: that the measured
binding and Q_β equal these definitional Re/Im at one normalisation —
axiomatised as the class `ComplexVolumeMatch` (AGENTS.md §3b-cond).

Fibre-level caveat: `Im(q₀)=0` at the archimedean level
(`lusztig_q_0_imaginary_part_zero`); the complex structure is fibre-level
and `𝔈_bind, 𝔔_β` are real observable shadows under different archimedean
evaluations (real-q vs root-of-unity), exactly as `Vol` and `CS` are
separately real.

Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
Ref: [kashaev1997] https://doi.org/10.1007/BF00768318
-/

namespace QOU.MassEndomorphism

open Complex

/-! ## Bar-parity + descent over a CommRing with involution (§7c — NOT `ℂ`)

The *proofs* live over a commutative ring `R` with a ring **involution**
`σ` (the bar-involution `q ↦ q⁻¹`), **not** `ℂ`. `σ`-even `x + σx` is the
binding (bar-even / `cosh`) channel; `σ`-odd `x − σx` is the `𝔔_β`
(bar-odd / `sinh`) channel. `ℂ` with complex conjugation is just the
*archimedean realisation* (below). The `/2` (`cosh`/`sinh`) normalisation
is narrative; we use the division-free `x ± σx` forms, so everything
holds over any `CommRing`. -/
section BarParityInvolution
variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- `σ`-even + `σ`-odd reconstructs `2x` (`(x+σx) + (x−σx) = 2x`). -/
theorem barParity_sum (x : R) : (x + σ x) + (x - σ x) = 2 * x := by ring

/-- `σ`-even − `σ`-odd reconstructs `2·σx`. -/
theorem barParity_diff (x : R) : (x + σ x) - (x - σ x) = 2 * σ x := by ring

/-- **Involution descent.** One ring identity `x = w` yields BOTH the
    bar-even (binding) and bar-odd (`𝔔_β`) identities at once — the
    `[CommRing R]`-generic form of "prove on `𝔙` once, read off both
    channels" (no `ℂ`, no `/2`). -/
theorem invol_descent {x w : R} (h : x = w) :
    (x + σ x = w + σ w) ∧ (x - σ x = w - σ w) :=
  ⟨by rw [h], by rw [h]⟩

/-- **Recurrence descent — the `c_k`-ladder mechanism, generic.** A
    three-term recurrence `𝔙ₚ = c·𝔙ₖ − 𝔙ₘ` with a **bar-even** multiplier
    `c` (`σ c = c`, the `2cosh η` analogue) yields the binding (`σ`-even)
    AND `𝔔_β` (`σ`-odd) recurrences from the *single* ring proof. -/
theorem recurrence_invol_descent {Vp Vk Vm c : R} (hc : σ c = c)
    (h : Vp = c * Vk - Vm) :
    ((Vp + σ Vp) = c * (Vk + σ Vk) - (Vm + σ Vm)) ∧
    ((Vp - σ Vp) = c * (Vk - σ Vk) - (Vm - σ Vm)) := by
  have key : σ Vp = c * σ Vk - σ Vm := by
    simp only [h, map_sub, map_mul, hc]
  exact ⟨by rw [key, h]; ring, by rw [key, h]; ring⟩

end BarParityInvolution

/-! ## Archimedean realisation (`ℂ`, `σ =` complex conjugation) -/

/-- The complex fibre observable `𝔙 = E₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`. -/
noncomputable def fibreDefect (E0 : ℝ) (trDefect : ℂ) : ℂ := (E0 : ℂ) * trDefect

/-- Binding `𝔈_bind := Re 𝔙` — the bar-even / volume channel. -/
noncomputable def binding (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).re
/-- β-decay `𝔔_β := Im 𝔙` — the bar-odd / Chern–Simons channel. -/
noncomputable def Qbeta (E0 : ℝ) (trDefect : ℂ) : ℝ := (fibreDefect E0 trDefect).im

/-- **The complex-volume unification (definitional, PROVED, sorry-free).**
    Binding (Re) and β-decay (Im) reconstruct the one complex fibre
    object `𝔙`: `𝔈_bind + i·𝔔_β = 𝔙`.  Mass and binding are no longer two
    stories — they are the two parities of one complex volume. -/
theorem complex_volume_unification (E0 : ℝ) (trDefect : ℂ) :
    (binding E0 trDefect : ℂ) + (Qbeta E0 trDefect : ℂ) * Complex.I
      = fibreDefect E0 trDefect := by
  unfold binding Qbeta
  exact Complex.re_add_im _

/-! ## Descent — one proof on `𝔙` covers binding AND `𝔔_β`

The "prove once, read off both channels" payoff is the **generic**
`invol_descent` / `recurrence_invol_descent` above (over `[CommRing R]`
with the bar-involution `σ`). The `ℂ` Re/Im descent is simply their
**archimedean instance** with `σ =` complex conjugation: `Re z = (z+σz)/2`
(bar-even / binding) and `Im z` carried by `(z−σz)/2` (bar-odd / `𝔔_β`).
No separate `ℂ`-only lemma is needed — the proofs live over the ring with
involution, per AGENTS.md §7c. -/

/-! ## Physical-match conjecture (the only open content) -/

/-- The physical-match conjecture (AGENTS.md §3b-cond class): the
    *measured* complex volume of a composite `K` — the **single** observable
    `𝔙_obs = 𝔈_bind^obs + i·𝔔_β^obs` — equals `𝔙(K)` at a single
    normalisation.  One hypothesis (`volume_match`), not two parallel arms:
    binding and `Q_β` are the Re/Im of *one* measured object, matched to the
    Re/Im of *one* fibre object.  This is the conjectural input; the
    unification theorem above is proved unconditionally. -/
class ComplexVolumeMatch (K : Type*) where
  /-- substrate energy scale `E₀`. -/
  E0 : ℝ
  /-- the complexified convolution-defect `tr_M((Π_free−1)∘𝓜)(K) ∈ ℂ` (fibre-level). -/
  trDefect : ℂ
  /-- the **measured complex volume** `𝔙_obs = 𝔈_bind^obs + i·𝔔_β^obs ∈ ℂ`
      (binding as Re, β-decay Q-value as Im — one observable, two shadows). -/
  measured_volume : ℂ
  /-- the single physical-match hypothesis: `𝔙_obs = E₀·(defect)`. -/
  volume_match : measured_volume = fibreDefect E0 trDefect

namespace ComplexVolumeMatch
variable {K : Type*} [c : ComplexVolumeMatch K]

/-- Measured binding `𝔈_bind^obs := Re 𝔙_obs`. -/
def binding_measured : ℝ := c.measured_volume.re
/-- Measured β-decay Q-value `𝔔_β^obs := Im 𝔙_obs`. -/
def qbeta_measured : ℝ := c.measured_volume.im

/-- Measured binding matches `Re 𝔙` (derived from the single `volume_match`). -/
theorem binding_match : (binding_measured (K := K)) = binding c.E0 c.trDefect := by
  unfold binding_measured binding; rw [c.volume_match]
/-- Measured Q-value matches `Im 𝔙`. -/
theorem qbeta_match : (qbeta_measured (K := K)) = Qbeta c.E0 c.trDefect := by
  unfold qbeta_measured Qbeta; rw [c.volume_match]

end ComplexVolumeMatch

/-- Under the physical-match class, the measured observables reconstruct
    the complex defect: `𝔈_bind^obs + i·𝔔_β^obs = 𝔙`.  Now immediate from the
    single `volume_match` + the definitional unification. -/
theorem measured_complex_volume {K : Type*} [c : ComplexVolumeMatch K] :
    (ComplexVolumeMatch.binding_measured (K := K) : ℂ)
        + (ComplexVolumeMatch.qbeta_measured (K := K) : ℂ) * Complex.I
      = fibreDefect c.E0 c.trDefect := by
  rw [ComplexVolumeMatch.binding_match, ComplexVolumeMatch.qbeta_match]
  exact complex_volume_unification _ _

/-! ## Channel three-term recurrences over categorical `R` (§7c — fibre level, pre-τ)

The even (compact / binding / continuous q-Hermite) and odd (non-compact /
`𝔔_β` / Askey `q > 1` a.k.a. Ismail–Masson `q⁻¹`-Hermite) channel recurrences,
stated over a generic `[CommRing R]` — **not** `ℝ` or `ℂ`.  The "complex
rotation" between the two channels is a *formal* rotation element `ι` with
`ι * ι = -1` living in the fibre ring; `Complex.I` is only one archimedean
instance, reached downstream of the archimedean realisation τ.  Nothing in this
section uses an ordering, `cosh`, a metric, or a real/complex embedding.

Division-free conventions: the bar involution is carried by the hypothesis
`σ q * q = 1` (never `q⁻¹`), and the odd recurrence is multiplied through by
`q ^ (n+1)`.

Ref: [askey1989qhermite] R. Askey, *Continuous q-Hermite polynomials when
q > 1* (q-Series and Partitions, IMA Vol. 18, 1989) — the `q > 1` channel.
Ref: [ismail-masson1994] DOI 10.1090/S0002-9947-1994-1264148-6 — the
`q⁻¹`-Hermite rotation identity `h_n(x|q) = i^{-n} H_n(ix|q^{-1})`. -/
section ChannelRecurrences
variable {R : Type*} [CommRing R]

/-- The bar involution transports an even step to an even step at the
    conjugated data (`σ` a ring hom: coefficients map through). -/
theorem evenStep_map (σ : R →+* R) {q x : R} {n : ℕ} {H0 H1 H2 : R}
    (h : evenStep q x n H0 H1 H2) :
    evenStep (σ q) (σ x) n (σ H0) (σ H1) (σ H2) := by
  unfold evenStep at h ⊢
  have := congrArg σ h
  simpa [map_sub, map_mul, map_add, map_pow, map_one, map_ofNat] using this

end ChannelRecurrences

/-! ## Leonard pair / overlap coefficients — the rotation matrix, categorical

Zhedanov's AW(3) picture, in its generically provable form: for a
tridiagonal ("channel-basis") operator, **any eigencolumn is the
orthogonal-polynomial column evaluated at its eigenvalue** — i.e. the
change-of-basis ("rotation") matrix between the channel basis and the
spectral basis has entries `p_n(θ_m)`, the three-term-recurrence
polynomials (Askey–Wilson at the top of the q-scheme).  This is
`eigencolumn_eq_overlap`, sorry-free over any `CommRing`.

What is *not* provable generically — that the QOU channel pair carries a
second (dual) operator making the overlap matrix self-dual
(`p_n(θ_m) = p*_m(θ*_n)`, a Leonard/tridiagonal pair, forcing AW/q-Racah
type by Terwilliger's classification) — is carried honestly as the
conjecture class `ChannelLeonardDuality` (§3b).

Ref: [zhedanov1991] DOI 10.1007/BF01015906 — "Hidden symmetry of
Askey–Wilson polynomials" (AW(3)).
Ref: [terwilliger2001] DOI 10.1016/S0024-3795(01)00242-7 — Leonard-pair
classification. -/
section LeonardOverlap
variable {R : Type*} [CommRing R]

/-- The overlap ("rotation-matrix") column: the orthogonal-polynomial
    sequence of the tridiagonal data `(a, b, c)` evaluated at the spectral
    value `θ`.  Super-diagonal entries `a` are units so the recursion is
    division-free-normalisable. -/
def overlapColumn (a : ℕ → Rˣ) (b c : ℕ → R) (θ : R) : ℕ → R
  | 0 => 1
  | 1 => ((a 0)⁻¹ : Rˣ) * (θ - b 0)
  | n + 2 =>
      ((a (n + 1))⁻¹ : Rˣ) *
        ((θ - b (n + 1)) * overlapColumn a b c θ (n + 1)
          - c (n + 1) * overlapColumn a b c θ n)

/-- `v` is a `θ`-eigencolumn of the tridiagonal (channel-basis) operator
    with sub/diag/super data `(c, b, a)`: the seed row plus the generic
    three-term row. -/
def IsEigencolumn (a : ℕ → Rˣ) (b c : ℕ → R) (θ : R) (v : ℕ → R) : Prop :=
  ((a 0 : R) * v 1 + b 0 * v 0 = θ * v 0) ∧
    ∀ n, (a (n + 1) : R) * v (n + 2) + b (n + 1) * v (n + 1)
        + c (n + 1) * v n = θ * v (n + 1)

/-- **Overlap coefficients are the orthogonal polynomials (rotation-matrix
    theorem), sorry-free.**  Any `θ`-eigencolumn of the tridiagonal channel
    operator is `v 0 · p_n(θ)`: the intertwiner between the channel basis
    and the spectral basis is *forced* to have orthogonal-polynomial
    entries.  This is the provable half of "the AW polynomials are the
    rotation between the two channels". -/
theorem eigencolumn_eq_overlap {a : ℕ → Rˣ} {b c : ℕ → R} {θ : R}
    {v : ℕ → R} (hv : IsEigencolumn a b c θ v) :
    ∀ n, v n = v 0 * overlapColumn a b c θ n := by
  have key : ∀ n, v n = v 0 * overlapColumn a b c θ n
      ∧ v (n + 1) = v 0 * overlapColumn a b c θ (n + 1) := by
    intro n
    induction n with
    | zero =>
      refine ⟨by simp [overlapColumn], ?_⟩
      -- seed row: a₀·v₁ = (θ − b₀)·v₀
      have h0 := hv.1
      have : (a 0 : R) * v 1 = (a 0 : R) * (v 0 * overlapColumn a b c θ 1) := by
        have : (a 0 : R) * (v 0 * overlapColumn a b c θ 1)
            = v 0 * (θ - b 0) := by
          show (a 0 : R) * (v 0 * (((a 0)⁻¹ : Rˣ) * (θ - b 0))) = v 0 * (θ - b 0)
          rw [show (a 0 : R) * (v 0 * (((a 0)⁻¹ : Rˣ) * (θ - b 0)))
              = ((a 0 : R) * ((a 0)⁻¹ : Rˣ)) * (v 0 * (θ - b 0)) by ring,
            Units.mul_inv, one_mul]
        rw [this]
        linear_combination h0
      exact (Units.mul_right_inj (a 0)).mp this
    | succ k ih =>
      refine ⟨ih.2, ?_⟩
      -- generic row: a_{k+1}·v_{k+2} = (θ − b_{k+1})·v_{k+1} − c_{k+1}·v_k
      have hrow := hv.2 k
      have hval : (a (k + 1) : R) * v (k + 2)
          = (a (k + 1) : R) * (v 0 * overlapColumn a b c θ (k + 2)) := by
        have hrhs : (a (k + 1) : R) * (v 0 * overlapColumn a b c θ (k + 2))
            = v 0 * ((θ - b (k + 1)) * overlapColumn a b c θ (k + 1)
                - c (k + 1) * overlapColumn a b c θ k) := by
          show (a (k + 1) : R) * (v 0 * (((a (k + 1))⁻¹ : Rˣ) *
              ((θ - b (k + 1)) * overlapColumn a b c θ (k + 1)
                - c (k + 1) * overlapColumn a b c θ k)))
            = v 0 * ((θ - b (k + 1)) * overlapColumn a b c θ (k + 1)
                - c (k + 1) * overlapColumn a b c θ k)
          rw [show ∀ u : R, (a (k + 1) : R) * (v 0 * (((a (k + 1))⁻¹ : Rˣ) * u))
              = ((a (k + 1) : R) * ((a (k + 1))⁻¹ : Rˣ)) * (v 0 * u) from
            fun u => by ring, Units.mul_inv, one_mul]
        rw [hrhs]
        linear_combination hrow + (θ - b (k + 1)) * ih.2 - c (k + 1) * ih.1
      exact (Units.mul_right_inj (a (k + 1))).mp hval
  exact fun n => (key n).1

/-- **Leonard-duality conjecture for the channel pair (§3b class;
    conjecture — no instance is provided).**  The overlap matrix of the
    channel tridiagonal data is *self-dual*: there exist dual tridiagonal
    data and dual eigenvalues with `p_n(θ_m) = p*_m(θ*_n)` — the defining
    property of a Leonard / tridiagonal pair.  By Terwilliger's
    classification this forces the overlap coefficients into the
    Askey–Wilson (q-Racah) family: *the two channels are a Leonard pair
    and the AW polynomials are the rotation between them.*  Fields carry
    the conjecture's inputs (the dual data and the quantified duality),
    per §3b-tax content rules. -/
class ChannelLeonardDuality (a : ℕ → Rˣ) (b c : ℕ → R) (θ : ℕ → R) where
  /-- dual super-diagonal (units). -/
  dualA : ℕ → Rˣ
  /-- dual diagonal. -/
  dualB : ℕ → R
  /-- dual sub-diagonal. -/
  dualC : ℕ → R
  /-- dual eigenvalue sequence. -/
  θstar : ℕ → R
  /-- Leonard self-duality of the overlap matrix: `p_n(θ_m) = p*_m(θ*_n)`. -/
  duality : ∀ n m,
    overlapColumn a b c (θ m) n = overlapColumn dualA dualB dualC (θstar n) m

/-- Derived (proved, conditional on the class): the **rows** of the overlap
    matrix satisfy the dual three-term recurrence — the second
    tridiagonalisation that makes the pair "Leonard".  One proof serves
    both channels, per `recurrence_invol_descent`. -/
theorem ChannelLeonardDuality.row_three_term
    {a : ℕ → Rˣ} {b c : ℕ → R} {θ : ℕ → R}
    [L : ChannelLeonardDuality a b c θ] (n m : ℕ) :
    (L.dualA (m + 1) : R) * overlapColumn a b c (θ (m + 2)) n
      = (L.θstar n - L.dualB (m + 1)) * overlapColumn a b c (θ (m + 1)) n
        - L.dualC (m + 1) * overlapColumn a b c (θ m) n := by
  rw [L.duality n (m + 2), L.duality n (m + 1), L.duality n m]
  show (L.dualA (m + 1) : R) * (((L.dualA (m + 1))⁻¹ : Rˣ) *
      ((L.θstar n - L.dualB (m + 1))
          * overlapColumn L.dualA L.dualB L.dualC (L.θstar n) (m + 1)
        - L.dualC (m + 1)
          * overlapColumn L.dualA L.dualB L.dualC (L.θstar n) m)) = _
  rw [← mul_assoc, Units.mul_inv, one_mul]

end LeonardOverlap

/-! ## AW deformation path — bound ↔ free, the character-variety reading

The free projection `Π_free` (inter-constituent crossings dropped) is the
**abelian** representation; the bound object is the full braiding (the
discrete-faithful side).  Neumann–Zagier reads the complex volume as the
integral of a holomorphic 1-form along the **path in the character variety
from the abelian to the discrete-faithful representation** — so the
"rotation interpolating bound and free" is the deformation path itself,
and the σ-odd (`𝔔_β` / CS) channel is the *holonomy picked up along it*.

Categorically (pre-τ, §7c): the path lives in the deformation parameter
`t : R` of ONE Askey–Wilson tridiagonal family — `t = 0` the q-Hermite
bottom of the scheme (all AW parameters off; its orthogonality measure is
the q-Plancherel `W_λ`, the *free* side), `t = 1` the bound channel data.
The class below carries exactly these inputs; the two-channel descent is
then **derived** (not assumed) via `recurrence_invol_descent`, so the
class is non-degenerate per §3b-cond rule 5.

Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7 -/
section AWDeformation
variable {R : Type*} [CommRing R]

/-- Derived (proved, conditional on the class): the σ-even (binding) and
    σ-odd (`𝔔_β`) ladders each satisfy the SAME three-term recurrence —
    the two channels are the two parities of the one deformation-path
    ladder.  Direct application of `recurrence_invol_descent`. -/
theorem AWDeformationPath.channel_ladders (σ : R →+* R)
    [P : AWDeformationPath σ] (n : ℕ) :
    ((P.ladder (n + 2) + σ (P.ladder (n + 2)))
        = P.multiplier * (P.ladder (n + 1) + σ (P.ladder (n + 1)))
          - (P.ladder n + σ (P.ladder n)))
      ∧ ((P.ladder (n + 2) - σ (P.ladder (n + 2)))
        = P.multiplier * (P.ladder (n + 1) - σ (P.ladder (n + 1)))
          - (P.ladder n - σ (P.ladder n))) :=
  recurrence_invol_descent σ P.multiplier_bar_even (P.ladder_recurrence n)

end AWDeformation

/-! ## Concrete AW(3) relations at the q-Hermite bottom — the channel operators

Zhedanov's AW(3) algebra, realized concretely for the channel pair.  At the
q-Hermite bottom of the scheme (all Askey–Wilson parameters off — the *free*
endpoint of `AWDeformationPath`) the algebra degenerates to the
**q-oscillator relations**, and these are *provable* over generic
`[CommRing R]`, division-free, coordinatewise on sequence space `ℕ → R`.

The channel tridiagonal operator (multiplication by `2x` in the q-Hermite
basis, transposed to coefficient columns) splits as `M = L + R`:

- `chR` (raising): `(R v) 0 = 0`, `(R v) (n+1) = v n` — the sub-diagonal;
- `chL` (lowering): `(L v) n = (1 − q^{n+1}) · v (n+1)` — the super-diagonal
  with the even-channel coefficient;
- `chQ` (grading): `(Q v) n = q^n · v n` — the diagonal q-power operator.

The proved relations (`chQR_rel`, `chLQ_rel`, `chLR_comm`) are the
degenerate-AW(3) presentation: the first two are the q-commutation of the
grading with the shifts, the third — `L∘R − R∘L = (1−q)·Q` — is the
q-oscillator commutator that generates the whole ladder.  The bar-conjugated
(odd-channel) operators are the same definitions at `σ q`, so every relation
descends to both channels by instantiation (`q := σ q`) — no second proof.

This realizes the algebra side of `ChannelLeonardDuality` at the free
endpoint; the four-parameter AW deformation of these relations (the bound
endpoint) remains the conjecture class.

Ref: [zhedanov1991] DOI 10.1007/BF01015906. -/
section AW3Concrete
variable {R : Type*} [CommRing R]

/-- Raising (sub-diagonal) channel operator: `(R v) 0 = 0`, `(R v)(n+1) = v n`. -/
def chR (v : ℕ → R) : ℕ → R
  | 0 => 0
  | n + 1 => v n

/-- Lowering (super-diagonal) channel operator with the even-channel
    coefficient: `(L v) n = (1 − q^{n+1}) · v (n+1)`. -/
def chL (q : R) (v : ℕ → R) : ℕ → R :=
  fun n => (1 - q ^ (n + 1)) * v (n + 1)

/-- Grading (diagonal) operator: `(Q v) n = q^n · v n`. -/
def chQ (q : R) (v : ℕ → R) : ℕ → R :=
  fun n => q ^ n * v n

/-- The channel tridiagonal operator at the q-Hermite bottom:
    multiplication by `2x` in the channel basis is `M = L + R`
    (diagonal term zero — the free endpoint of `AWDeformationPath`). -/
def chM (q : R) (v : ℕ → R) : ℕ → R :=
  fun n => chL q v n + chR v n

/-- **q-commutation of grading with raising**: `Q ∘ R = q · (R ∘ Q)`. -/
theorem chQR_rel (q : R) (v : ℕ → R) :
    ∀ n, chQ q (chR v) n = q * chR (chQ q v) n := by
  intro n
  cases n with
  | zero => simp [chQ, chR]
  | succ k =>
    show q ^ (k + 1) * v k = q * (q ^ k * v k)
    ring

/-- **q-commutation of lowering with grading**: `L ∘ Q = q · (Q ∘ L)`. -/
theorem chLQ_rel (q : R) (v : ℕ → R) :
    ∀ n, chL q (chQ q v) n = q * chQ q (chL q v) n := by
  intro n
  show (1 - q ^ (n + 1)) * (q ^ (n + 1) * v (n + 1))
      = q * (q ^ n * ((1 - q ^ (n + 1)) * v (n + 1)))
  ring

/-- **The q-oscillator commutator (degenerate AW(3), proved):**
    `L ∘ R − R ∘ L = (1 − q) · Q`.  This is the concrete channel-operator
    form of Zhedanov's algebra at the q-Hermite bottom; the odd channel
    satisfies the same relation at `σ q` by instantiation. -/
theorem chLR_comm (q : R) (v : ℕ → R) :
    ∀ n, chL q (chR v) n - chR (chL q v) n = (1 - q) * chQ q v n := by
  intro n
  cases n with
  | zero =>
    show (1 - q ^ (0 + 1)) * chR v (0 + 1) - 0 = (1 - q) * (q ^ 0 * v 0)
    show (1 - q ^ (0 + 1)) * v 0 - 0 = (1 - q) * (q ^ 0 * v 0)
    ring
  | succ k =>
    show (1 - q ^ (k + 2)) * chR v (k + 2) - chL q v k
        = (1 - q) * (q ^ (k + 1) * v (k + 1))
    show (1 - q ^ (k + 2)) * v (k + 1) - (1 - q ^ (k + 1)) * v (k + 1)
        = (1 - q) * (q ^ (k + 1) * v (k + 1))
    ring

/-- The channel operator is the shift-split sum (definitional). -/
theorem chM_eq_L_add_R (q : R) (v : ℕ → R) (n : ℕ) :
    chM q v n = chL q v n + chR v n := rfl

/-- **Eigencolumns of the free-endpoint channel operator are exactly the
    q-Hermite three-term rows**: `(M v) n = θ·v n` unfolds to the seed row
    `(1−q)·v 1 = θ·v 0` and the generic row
    `(1−q^{n+2})·v_{n+2} + v_n = θ·v_{n+1}` — the `evenStep` shape with
    diagonal off.  Connects `chM` to `IsEigencolumn`/`overlapColumn`
    without a unit assumption on the super-diagonal. -/
theorem chM_eigencolumn_iff (q θ : R) (v : ℕ → R) :
    (∀ n, chM q v n = θ * v n)
      ↔ ((1 - q) * v 1 = θ * v 0
          ∧ ∀ n, (1 - q ^ (n + 2)) * v (n + 2) + v n = θ * v (n + 1)) := by
  constructor
  · intro h
    refine ⟨?_, fun n => h (n + 1)⟩
    have h0 : (1 - q ^ 1) * v 1 + 0 = θ * v 0 := h 0
    rw [pow_one, add_zero] at h0
    exact h0
  · rintro ⟨h0, hrow⟩ n
    cases n with
    | zero =>
      show (1 - q ^ 1) * v 1 + 0 = θ * v 0
      rw [pow_one, add_zero]
      exact h0
    | succ k => exact hrow k

end AW3Concrete

/-! ## Casoratian descent — the mechanism of the W-sign test

The 1jrh prune (docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
pins the decisive physical experiment: if the binding and `𝔔_β` ladders solve
ONE three-term recurrence, they span its 2-dimensional solution space and
their **Casoratian** (discrete Wronskian) `W_k` transports by
`W_{k+1} = −B_{k+1}·W_k` — the AW form of `B_k` then forces a parameter-free
sign pattern.  With the `c₃^even` rung now measured exactly
(`qbeta-c3even-exact-sseries`, `c₃^even = 841/144 + 604739·√3/12960`), the
remaining gate is the Stage-C `c₄` pair; the *mechanism* is proved here so
the eventual test is one line of arithmetic on trusted rungs. -/
section Casoratian
variable {R : Type*} [CommRing R]

/-- **Casoratian descent (proved).**  If two sequences satisfy the SAME
    three-term step `X₂ = A·X₁ + B·X₀`, their Casoratian
    `W = X₀·Y₁ − X₁·Y₀` transports by one step as `W' = −B·W`.
    No hypothesis on `A` is needed — the multiplier cancels. -/
theorem casoratian_step {A B X0 X1 X2 Y0 Y1 Y2 : R}
    (hX : X2 = A * X1 + B * X0) (hY : Y2 = A * Y1 + B * Y0) :
    X1 * Y2 - X2 * Y1 = -B * (X0 * Y1 - X1 * Y0) := by
  subst hX; subst hY; ring

/-- **Channel-Casoratian invariance (proved).**  Along a `recurrence_invol_descent`
    ladder — one three-term recurrence `V₂ = c·V₁ − V₀` with a bar-even
    multiplier — the Casoratian of the two parity channels (bar-even/binding
    against bar-odd/`𝔔_β`) is *invariant*: constant multiplier ⇒ `B = −1` ⇒
    `W' = W`.  A measured drift of the physical channel Casoratian therefore
    reads directly as the `k`-dependence of the AW coefficient `B_k`. -/
theorem channel_casoratian_const (σ : R →+* R) {c V0 V1 V2 : R}
    (hc : σ c = c) (h : V2 = c * V1 - V0) :
    (V1 + σ V1) * (V2 - σ V2) - (V2 + σ V2) * (V1 - σ V1)
      = (V0 + σ V0) * (V1 - σ V1) - (V1 + σ V1) * (V0 - σ V0) := by
  obtain ⟨hE, hO⟩ := recurrence_invol_descent σ hc h
  have hstep := casoratian_step (A := c) (B := (-1 : R))
      (X0 := V0 + σ V0) (X1 := V1 + σ V1) (X2 := V2 + σ V2)
      (Y0 := V0 - σ V0) (Y1 := V1 - σ V1) (Y2 := V2 - σ V2)
      (by linear_combination hE) (by linear_combination hO)
  linear_combination hstep

end Casoratian


end QOU.MassEndomorphism
