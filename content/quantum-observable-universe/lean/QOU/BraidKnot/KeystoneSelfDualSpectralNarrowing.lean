import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.Tactic

/-!
# Keystone value step, structural reframe: self-duality narrows the eigenfunction class

**Context (owner reframe, 2026-07-05).** The keystone value map needs the vector
`bwS0(λ) = d_q(λ)/D` (`BWVacuumRowIsHecke.lean`). The *geometric-realisation* program tried to
reproduce it by screening an off-the-shelf q-special-function family (Σ(2,3,5) WRT, colored
Lawrence–Rozansky, and the E_q(2) q-Bessel — Hahn–Exton/q-Hankel via Koornwinder–Swarttouw
arXiv:1208.2521, and the *big* q-Bessel / q-Laguerre of Ciccoli–Koelink–Koornwinder
arXiv:math/9805023). Every node-value screen was a **scope-(a)** refutation, and the big q-Bessel
route is not even a 0-dof test: its discrete orthogonality is supported on `{c·q^k : k∈ℤ}` for *any*
`c > 0` (math/9805023 §4), so its "nodes" carry a free scale.

The reframe **inverts the search**: instead of importing an orthogonal family and testing its values,
read off the orthogonality/eigen constraints the framework's *own* structure imposes, and let them
narrow the class. Three ingredients:

* **(A) Frobenius pairing.** The Markov trace `tr_M = Σ_λ y_λ χ_λ` is a Frobenius form; under it the
  characters `χ_λ` are orthogonal with the quantum-dimension (Plancherel) weight `μ(λ)=d_q(λ)²/D²`
  (`KeystoneVerlindeSMatrixBridge.verlindeMeasure_eq_plancherel`), and `d_q(λ)/D = χ_λ(1)/D` is the
  vacuum overlap. The orthogonal system is *supplied*, not imported.
* **(B) Categorical 𝐂-action / Verlinde.** `S` simultaneously diagonalises the fusion operators;
  `d_q` is the unique Perron–Frobenius-positive common eigenvector (Ocneanu; Wenzl — the corpus
  `y-lambda-closed-form-wenzl-bridge`).
* **(C) Self-duality.** The modular `S` is symmetric and squares to charge conjugation, `S² = C`
  (`C² = 1`). That is the categorical avatar of a **self-reciprocal** transform — the spectral
  duality the geometric program was not using.

**What this file proves (the (C) leg, sorry-free).** For any symmetric `S` with `S² = C` and
`C² = 1` (charge conjugation an involution):

* `sTransform_pow_four : S ^ 4 = 1` — `S` has order dividing 4: the categorical **self-reciprocality**
  (`𝓗_q⁴ = id`), matching the self-reciprocal q-Hankel transform of arXiv:1208.2521.
* `eigenvector_pow_four_fixed` — an eigenvector `v` with `S v = ζ v` satisfies `ζ⁴ • v = v` (any
  `CommRing`); and `eigenvalue_pow_four_eq_one` — over a **field**, on a **nonzero** `v`, this gives
  `ζ⁴ = 1`: every eigenvalue is a 4th root of unity. The eigenfunction class is narrowed to the four
  charge-conjugation phases (as ordinary Fourier self-duality forces `iⁿ` on the Hermite
  eigenfunctions). On the **self-dual** (`C`-fixed) sector
  `C = +1`, so `S² = +1` there and the real symmetric `S` has eigenvalues `±1`; the vacuum row lives
  in this sector (`vacuumRow_conj_invariant`) and is the `+1` / PF-positive ground state — this is
  where `d_q` is pinned by (A)+(B).

**Honest scope.** This is the **keystone** value step (s013), *not* Step-9b binding. The value step
already has its non-geometric answer (redirect iii = Markov/PF uniqueness); this leg supplies the
*narrowing* — the constraint any geometric realisation must satisfy, and the reason a free-scale
q-Bessel family cannot be it — not a new closure. The PF-selection (B) step that pins the specific
`+1`-eigenvector to `d_q` is cited (Ocneanu/Wenzl), not re-proved here.

Base ring (§7c): generic `{R : Type*} [CommRing R]` — the order-4 identity is pure matrix algebra; the
`ζ⁴=1` eigenvalue corollary needs only a nonzero test vector, no ordering or `Real.sqrt`.

Audit: `docs/audits/2026-07-05-keystone-selfduality-spectral-narrowing.md`.
Ledger: `docs/coordination/s5-so3-keystone.md`.

-- Ref: [bakalovkirillov2001] Lectures on Tensor Categories and Modular Functors (S-matrix, S²=C).
-- Ref: [koornwinderswarttouw1992] arXiv:1208.2521 — self-reciprocal q-Hankel transform on E_q(2).
-/

namespace QOU.BraidKnot.Keystone

open Matrix

variable {ι : Type*} [Fintype ι] [DecidableEq ι] {R : Type*} [CommRing R]

/-- **A self-dual S-transform** on a finite fusion-label type.  Bundles the modular data used by the
narrowing: a symmetric matrix `S`, a charge-conjugation matrix `C` that is an involution, and the
self-duality relation `S² = C`.  (In a modular tensor category `S` is symmetric and `S² = C` is the
standard modular relation; `C` is the charge-conjugation permutation, `C² = 1`.) -/
structure SelfDualSTransform (ι R : Type*) [Fintype ι] [DecidableEq ι] [CommRing R] where
  /-- The modular S-matrix. -/
  S : Matrix ι ι R
  /-- The charge-conjugation matrix. -/
  C : Matrix ι ι R
  /-- `S` is symmetric (Frobenius self-duality of the pairing). -/
  S_symm : S.transpose = S
  /-- **Self-duality** `S² = C`. -/
  S_sq : S * S = C
  /-- Charge conjugation is an involution `C² = 1`. -/
  C_invol : C * C = 1

namespace SelfDualSTransform

variable (T : SelfDualSTransform ι R)

/-- **Spectral self-reciprocality: `S⁴ = 1`.**  From `S² = C` and `C² = 1` the transform has order
dividing 4 — the categorical avatar of a self-reciprocal (q-Hankel–type) transform `𝓗⁴ = id`.  This
is the *structural* fact the value-map program should have been matching against, in place of screening
node values of an imported q-Bessel family. -/
theorem sTransform_pow_four : T.S ^ 4 = 1 := by
  rw [show (4 : ℕ) = 2 + 2 from rfl, pow_add]
  simp only [pow_two, T.S_sq]
  rw [T.C_invol]

/-- `S² * S² = 1` (the two-step form of self-reciprocality, `C² = 1`). -/
theorem sSq_mul_sSq : (T.S * T.S) * (T.S * T.S) = 1 := by
  rw [T.S_sq, T.C_invol]

/-- **Eigenvector action of `S⁴`: `ζ⁴ • v = v`.**  From `S⁴ = 1`, an eigenvector `v` with
`S v = ζ v` satisfies `ζ⁴ • v = v` (over any `CommRing`, no nonzero hypothesis).  The scalar
consequence `ζ⁴ = 1` needs a nonzero `v` over a field — see `eigenvalue_pow_four_eq_one`. -/
theorem eigenvector_pow_four_fixed {v : ι → R}
    (ζ : R) (heig : T.S.mulVec v = ζ • v) : ζ ^ 4 • v = v := by
  have hpow : (T.S ^ 4).mulVec v = ζ ^ 4 • v := by
    have step : ∀ n : ℕ, (T.S ^ n).mulVec v = ζ ^ n • v := by
      intro n
      induction n with
      | zero => simp
      | succ k ih =>
          rw [pow_succ, ← Matrix.mulVec_mulVec, heig, Matrix.mulVec_smul, ih,
            smul_smul, pow_succ, mul_comm]
    exact step 4
  rw [T.sTransform_pow_four, Matrix.one_mulVec] at hpow
  exact hpow.symm

end SelfDualSTransform

/-- **Eigenvalue narrowing: `ζ⁴ = 1`.**  Over a **field**, any eigenvalue `ζ` of `S` on a **nonzero**
vector `v` is a 4th root of unity.  So the eigenfunctions the framework needs are not an arbitrary
orthogonal family: their eigenvalues are the four charge-conjugation phases (as ordinary self-dual
Fourier forces `iⁿ` on Hermite functions).  On the self-dual (`C`-fixed) sector this tightens to
`ζ = ±1`, and the PF-positive `+1` ground state is `d_q` (input (A)+(B), Ocneanu/Wenzl). -/
theorem eigenvalue_pow_four_eq_one {ι R : Type*} [Fintype ι] [DecidableEq ι] [Field R]
    (T : SelfDualSTransform ι R) {v : ι → R} (hv : v ≠ 0)
    (ζ : R) (heig : T.S.mulVec v = ζ • v) : ζ ^ 4 = 1 := by
  have hfix : ζ ^ 4 • v = v := T.eigenvector_pow_four_fixed ζ heig
  obtain ⟨i, hi⟩ := Function.ne_iff.mp hv
  rw [Pi.zero_apply] at hi
  have hcomp : ζ ^ 4 * v i = v i := by
    have := congrFun hfix i; simpa [Pi.smul_apply, smul_eq_mul] using this
  have hz : (ζ ^ 4 - 1) * v i = 0 := by rw [sub_mul, one_mul, hcomp, sub_self]
  rcases mul_eq_zero.mp hz with h | h
  · exact sub_eq_zero.mp h
  · exact absurd h hi

/-! ## The vacuum row lives in the self-dual sector -/

/-- **The vacuum row is charge-conjugation invariant.**  Because the quantum dimensions are self-dual
(`d_q(λ′) = d_q(λ)`, corpus `qDim_conj`), the vacuum S-matrix row `S_{0λ} = d_q(λ)/D` is fixed by the
transpose involution `λ ↦ λ′`.  So the value-map target lives in the `C = +1` (self-dual) sector,
where `S² = +1` and the real symmetric `S` has eigenvalues `±1` — the sector in which the PF-positive
`+1` ground state is `d_q`.  (Restates, at the vacuum row, the sector the narrowing selects.) -/
theorem vacuumRow_conj_invariant {ι R : Type*} [Field R]
    (d : ι → R) (D : R) (conj : ι → ι)
    (d_conj : ∀ lam, d (conj lam) = d lam) (lam : ι) :
    (fun μ => d μ / D) (conj lam) = (fun μ => d μ / D) lam := by
  simp only [d_conj]

end QOU.BraidKnot.Keystone
