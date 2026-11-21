import QOU.MathlibExt.BraidedBlockShiftTrace
import QOU.Machinery.MarkovTraceOnHecke

/-!
# Exact traces of the interleaved nucleon words

Mass gap 6 (bean `qou-hu1f` reordering; factorisation bean `qou-5zl1`).

`QOU.Mass.AtomTraceFactorisation.tr_atomWord` proves, on every Markov trace on a
braided tower, that the atom word factorises **over blocks**:

    tr (W_atom) = (∏_bonds (z + d_k)) · P_p^Z · P_n^N,

with `P_p = tr (proton word)` and `P_n = tr (neutron word)` read on strands
`0, 1, 2`. That theorem leaves `P_p` and `P_n` as abstract traces. This file
evaluates them **exactly**, as polynomials in `h`, `z` and the averaged-letter
shift `a`, for the production words of `computations/mass_at_3A_proper.py`
(`intra_order = "borromean"`, the owner-ruled interleaved core):

    proton   σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ (σ₀+a) (σ₁+a) σ₀ σ₀
    neutron  σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ (σ₀+a) (σ₀+a) σ₁⁻¹ σ₀ σ₀

with `σ⁻¹ = σ − h` (the quadratic relation) and, in production, `a = −h/2`.

## Method

`H₃` is spanned by the six images of the `GB`-normal-form basis
`1, g₀, g₁, g₁g₀, g₀g₁, g₀g₁g₀`. `nfEmbed` sends a coordinate vector to that
combination, and `nfEmbed_mul_g0` / `nfEmbed_mul_g1` show that right
multiplication by `g₀`, `g₁` acts on coordinates exactly as
`QOU.Machinery.H3.mulσ₀` / `mulσ₁` (quadratic + braid relations only). The
Markov property gives the trace of each basis element, which is
`QOU.Machinery.H3.TRM`. So the trace of any word in `g₀, g₁` with affine
letters is `H3.trM` of a coordinate vector computed by a fold
(`tr_wordVal_eq_trM`), and for the two concrete words that vector is a
polynomial identity closed by `ring`.

## What is NOT claimed

* That `computations/mass_at_3A_proper.py` emits exactly these letters. The
  words are transcribed from `atom_canonical_crossings(1, 0)` and
  `atom_canonical_crossings(0, 1)` (2026-11-16); no Lean object reads the
  Python producer.
* Anything about `z`. The polynomial identities hold for every Markov trace on a
  braided tower; the convention-D rational functions are the specialisation
  `z = q³/(q²+1)`, `h = q − q⁻¹`, `a = −h/2`, in the field section at the end.
* Any binding energy.

Base ring: generic `[CommRing R]`, generic `R`-algebra `A`. The convention-D
section is over a generic `[Field K]`. No `ℝ`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [leitner2026] beans qou-5zl1 / qou-hu1f; computations/mass_at_3A_proper.py.
-/

namespace QOU.Mass.NucleonWordTraceClosedForm

open QOU.MathlibExt.OcneanuTrace QOU.MathlibExt.BraidedBlockShiftTrace
open QOU.Machinery.H3

section Words

variable {R : Type*} [CommRing R] (h : R)

/-- One affine letter `(i, s, b) ↦ s • 1 + b • g_i`, `i ≤ 1`, acting on coordinates. -/
def nfStep (v : Fin 6 → R) (l : ℕ × R × R) : Fin 6 → R :=
  l.2.1 • v + l.2.2 • (if l.1 = 0 then mulσ₀ h v else mulσ₁ h v)

/-! ## The production nucleon words -/

/-- The proton word, `intra_order = "borromean"`: letters `(generator, shift, 1)`,
with `σ⁻¹ = σ − h` and the averaged letter `σ + a`. -/
def protonWord (a : R) : List (ℕ × R × R) :=
  [(0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1),
   (0, a, 1), (1, a, 1), (0, 0, 1), (0, 0, 1)]

/-- The neutron word, `intra_order = "borromean"`. -/
def neutronWord (a : R) : List (ℕ × R × R) :=
  [(0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, a, 1),
   (0, a, 1), (1, -h, 1), (0, 0, 1), (0, 0, 1)]

/-- `P_p(h, z, a)`. -/
def protonPoly (z a : R) : R :=
  a ^ 2 * (-h ^ 8 * z + h ^ 7 * z ^ 2 - h ^ 7 - 3 * h ^ 6 * z + 3 * h ^ 5 * z ^ 2 - 3 * h ^ 5
      - h ^ 4 * z + h ^ 3 * z ^ 2 - h ^ 3 + h ^ 2 * z + h + z)
  + a * (-h ^ 9 * z + h ^ 8 * z ^ 2 - h ^ 8 - 4 * h ^ 7 * z + 4 * h ^ 6 * z ^ 2 - 4 * h ^ 6
      - 3 * h ^ 5 * z + 3 * h ^ 4 * z ^ 2 - 3 * h ^ 4 + 2 * h ^ 2 * z ^ 2 + 3 * h * z + z ^ 2 + 1)
  + (h ^ 6 * z - h ^ 5 * z ^ 2 + h ^ 5 + h ^ 4 * z + h ^ 3 + h ^ 2 * z + 2 * h * z ^ 2 + z)

/-- `P_n(h, z, a)`. -/
def neutronPoly (z a : R) : R :=
  a ^ 2 * (h ^ 8 * z - h ^ 7 * z ^ 2 + h ^ 7 + 3 * h ^ 6 * z - 3 * h ^ 5 * z ^ 2 + 3 * h ^ 5
      + 2 * h ^ 4 * z - 2 * h ^ 3 * z ^ 2 + 2 * h ^ 3 - h ^ 2 * z + h * z ^ 2 - h + z)
  + a * (2 * h ^ 9 * z - 2 * h ^ 8 * z ^ 2 + 2 * h ^ 8 + 6 * h ^ 7 * z - 6 * h ^ 6 * z ^ 2
      + 6 * h ^ 6 + 2 * h ^ 5 * z - 2 * h ^ 4 * z ^ 2 + 2 * h ^ 4 - 4 * h ^ 3 * z
      + 4 * h ^ 2 * z ^ 2 - 4 * h ^ 2 + 2 * z ^ 2)
  + (h ^ 10 * z - h ^ 9 * z ^ 2 + h ^ 9 + 4 * h ^ 8 * z - 4 * h ^ 7 * z ^ 2 + 4 * h ^ 7
      + 4 * h ^ 6 * z - 4 * h ^ 5 * z ^ 2 + 4 * h ^ 5 - h ^ 2 * z + 2 * h * z ^ 2 - h + z)

theorem nfStep_zero (x0 x1 x2 x3 x4 x5 s b : R) :
    nfStep h ![x0, x1, x2, x3, x4, x5] (0, s, b)
      = ![s * x0 + b * x1, s * x1 + b * (x0 + h * x1), s * x2 + b * x3,
          s * x3 + b * (x2 + h * x3), s * x4 + b * x5, s * x5 + b * (x4 + h * x5)] := by
  funext i
  fin_cases i <;> simp [nfStep, mulσ₀]

theorem nfStep_one (x0 x1 x2 x3 x4 x5 s b : R) :
    nfStep h ![x0, x1, x2, x3, x4, x5] (1, s, b)
      = ![s * x0 + b * x2, s * x1 + b * x4, s * x2 + b * (x0 + h * x2),
          s * x3 + b * x5, s * x4 + b * (x1 + h * x4), s * x5 + b * (x3 + h * x5)] := by
  funext i
  fin_cases i <;> simp [nfStep, mulσ₁]

theorem trM_vec (z x0 x1 x2 x3 x4 x5 : R) :
    trM z h ![x0, x1, x2, x3, x4, x5]
      = x0 + x1 * z + x2 * z + x3 * z ^ 2 + x4 * z ^ 2 + x5 * (h * z ^ 2 + z) := by
  simp [trM, TRM, Fin.sum_univ_six]

omit [CommRing R] in
/-- Componentwise equality of six-vectors. -/
theorem vec6_ext {a0 a1 a2 a3 a4 a5 b0 b1 b2 b3 b4 b5 : R} (e0 : a0 = b0) (e1 : a1 = b1)
    (e2 : a2 = b2) (e3 : a3 = b3) (e4 : a4 = b4) (e5 : a5 = b5) :
    (![a0, a1, a2, a3, a4, a5] : Fin 6 → R) = ![b0, b1, b2, b3, b4, b5] := by
  subst e0 e1 e2 e3 e4 e5; rfl

-- The heartbeat bump pays for elaborating the explicit step statements.
set_option maxHeartbeats 1000000 in
/-- The proton word, folded: each step is checked by `ring` on explicit coordinates. -/
theorem trM_protonWord (z a : R) :
    trM z h ((protonWord h a).foldl (nfStep h) ![1, 0, 0, 0, 0, 0]) = protonPoly h z a := by
  simp only [protonWord, List.foldl_cons, List.foldl_nil]
  have s0 : nfStep h ![1, 0, 0, 0, 0, 0] (0, 0, 1) =
      ![0, 1, 0, 0, 0, 0] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s1 : nfStep h ![0, 1, 0, 0, 0, 0] (1, -h, 1) =
      ![0, -h, 0, 0, 1, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s2 : nfStep h ![0, -h, 0, 0, 1, 0] (0, 0, 1) =
      ![-h, -h^2, 0, 0, 0, 1] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s3 : nfStep h ![-h, -h^2, 0, 0, 0, 1] (1, -h, 1) =
      ![h^2, h^3, -h, 1, -h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s4 : nfStep h ![h^2, h^3, -h, 1, -h^2, 0] (0, 0, 1) =
      ![h^3, h^4 + h^2, 1, 0, 0, -h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s5 : nfStep h ![h^3, h^4 + h^2, 1, 0, 0, -h^2] (1, -h, 1) =
      ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s6 : nfStep h ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] (0, 0, 1) =
      ![-h^5 - h^3, -h^6 - 2*h^4 + 1, -h^2, 0, 0, h^4 + h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s7 : nfStep h ![-h^5 - h^3, -h^6 - 2*h^4 + 1, -h^2, 0, 0, h^4 + h^2] (0, a, 1) =
      ![-a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, -a*h^6 - 2*a*h^4 + a - h^7 - 3*h^5 - h^3 + h, -a*h^2, -h^2, h^4 + h^2, a*h^4 + a*h^2 + h^5 + h^3] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s8 : nfStep h ![-a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, -a*h^6 - 2*a*h^4 + a - h^7 - 3*h^5 - h^3 + h, -a*h^2, -h^2, h^4 + h^2, a*h^4 + a*h^2 + h^5 + h^3] (1, a, 1) =
      ![-a^2*h^5 - a^2*h^3 - a*h^6 - 2*a*h^4 - a*h^2 + a, -a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^2 - a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a*h^4 + h^5 + h^3, -a*h^6 - a*h^4 + a*h^2 + a - h^7 - 2*h^5 + h, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s9 : nfStep h ![-a^2*h^5 - a^2*h^3 - a*h^6 - 2*a*h^4 - a*h^2 + a, -a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^2 - a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a*h^4 + h^5 + h^3, -a*h^6 - a*h^4 + a*h^2 + a - h^7 - 2*h^5 + h, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2] (0, 0, 1) =
      ![-a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^7 - 3*a^2*h^5 - a^2*h^3 + a^2*h - a*h^8 - 4*a*h^6 - 3*a*h^4 + a + h^5 + h^3, a*h^4 + h^5 + h^3, -a^2*h^2 - 2*a*h^3 - h^4 + 1, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2, a^2*h^5 + a^2*h^3 + a*h^6 + a*h^4 + a*h^2 + a - h^5 - h^3 + h] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s10 : nfStep h ![-a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^7 - 3*a^2*h^5 - a^2*h^3 + a^2*h - a*h^8 - 4*a*h^6 - 3*a*h^4 + a + h^5 + h^3, a*h^4 + h^5 + h^3, -a^2*h^2 - 2*a*h^3 - h^4 + 1, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2, a^2*h^5 + a^2*h^3 + a*h^6 + a*h^4 + a*h^2 + a - h^5 - h^3 + h] (0, 0, 1) =
      ![-a^2*h^7 - 3*a^2*h^5 - a^2*h^3 + a^2*h - a*h^8 - 4*a*h^6 - 3*a*h^4 + a + h^5 + h^3, -a^2*h^8 - 4*a^2*h^6 - 3*a^2*h^4 + a^2*h^2 + a^2 - a*h^9 - 5*a*h^7 - 6*a*h^5 - a*h^3 + 2*a*h + h^6 + 2*h^4 + h^2, -a^2*h^2 - 2*a*h^3 - h^4 + 1, -a^2*h^3 - a*h^4 + h^3 + h, a^2*h^5 + a^2*h^3 + a*h^6 + a*h^4 + a*h^2 + a - h^5 - h^3 + h, a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + a*h^7 + 3*a*h^5 + 3*a*h^3 + a*h] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  rw [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, trM_vec, protonPoly]
  ring

set_option maxHeartbeats 1000000 in
/-- The neutron word, folded step by step. -/
theorem trM_neutronWord (z a : R) :
    trM z h ((neutronWord h a).foldl (nfStep h) ![1, 0, 0, 0, 0, 0]) = neutronPoly h z a := by
  simp only [neutronWord, List.foldl_cons, List.foldl_nil]
  have s0 : nfStep h ![1, 0, 0, 0, 0, 0] (0, 0, 1) =
      ![0, 1, 0, 0, 0, 0] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s1 : nfStep h ![0, 1, 0, 0, 0, 0] (1, -h, 1) =
      ![0, -h, 0, 0, 1, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s2 : nfStep h ![0, -h, 0, 0, 1, 0] (0, 0, 1) =
      ![-h, -h^2, 0, 0, 0, 1] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s3 : nfStep h ![-h, -h^2, 0, 0, 0, 1] (1, -h, 1) =
      ![h^2, h^3, -h, 1, -h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s4 : nfStep h ![h^2, h^3, -h, 1, -h^2, 0] (0, 0, 1) =
      ![h^3, h^4 + h^2, 1, 0, 0, -h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s5 : nfStep h ![h^3, h^4 + h^2, 1, 0, 0, -h^2] (1, -h, 1) =
      ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s6 : nfStep h ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] (0, a, 1) =
      ![-a*h^4 + a - h^5 - h^3, -a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, a*h^3 - h^2, -a*h^2, a*h^4 + a*h^2, h^4 + h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s7 : nfStep h ![-a*h^4 + a - h^5 - h^3, -a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, a*h^3 - h^2, -a*h^2, a*h^4 + a*h^2, h^4 + h^2] (0, a, 1) =
      ![-a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, a^2*h^3 - 2*a*h^2, -a^2*h^2 - h^2, a^2*h^4 + a^2*h^2 + h^4 + h^2, 2*a*h^4 + 2*a*h^2 + h^5 + h^3] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s8 : nfStep h ![-a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, a^2*h^3 - 2*a*h^2, -a^2*h^2 - h^2, a^2*h^4 + a^2*h^2 + h^4 + h^2, 2*a*h^4 + 2*a*h^2 + h^5 + h^3] (1, -h, 1) =
      ![a^2*h^5 + a^2*h^3 - a^2*h + 2*a*h^6 + 2*a*h^4 - 2*a*h^2 + h^7 + 2*h^5 - h, a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, -a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, -a^2*h^2 - h^2] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s9 : nfStep h ![a^2*h^5 + a^2*h^3 - a^2*h + 2*a*h^6 + 2*a*h^4 - 2*a*h^2 + h^7 + 2*h^5 - h, a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, -a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, -a^2*h^2 - h^2] (0, 0, 1) =
      ![a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, a^2*h^7 + 3*a^2*h^5 + 2*a^2*h^3 - a^2*h + 2*a*h^8 + 6*a*h^6 + 2*a*h^4 - 4*a*h^2 + h^9 + 4*h^7 + 4*h^5 - h, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, a^2 + 1, -a^2*h^2 - h^2, -a^2*h^5 - 2*a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - 2*h^3 + h] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s10 : nfStep h ![a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, a^2*h^7 + 3*a^2*h^5 + 2*a^2*h^3 - a^2*h + 2*a*h^8 + 6*a*h^6 + 2*a*h^4 - 4*a*h^2 + h^9 + 4*h^7 + 4*h^5 - h, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, a^2 + 1, -a^2*h^2 - h^2, -a^2*h^5 - 2*a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - 2*h^3 + h] (0, 0, 1) =
      ![a^2*h^7 + 3*a^2*h^5 + 2*a^2*h^3 - a^2*h + 2*a*h^8 + 6*a*h^6 + 2*a*h^4 - 4*a*h^2 + h^9 + 4*h^7 + 4*h^5 - h, a^2*h^8 + 4*a^2*h^6 + 4*a^2*h^4 + 2*a*h^9 + 8*a*h^7 + 6*a*h^5 - 4*a*h^3 - 2*a*h + h^10 + 5*h^8 + 7*h^6 + 2*h^4 - h^2, a^2 + 1, a^2*h^3 + a^2*h + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3 + h, -a^2*h^5 - 2*a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - 2*h^3 + h, -a^2*h^6 - 2*a^2*h^4 - a^2*h^2 - 2*a*h^7 - 4*a*h^5 + 2*a*h - h^8 - 3*h^6 - 2*h^4] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  rw [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, trM_vec, neutronPoly]
  ring


end Words

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
  (T : MarkovTrace R A) (h : R)

/-- The `H₃` normal-form basis `1, g₀, g₁, g₁g₀, g₀g₁, g₀g₁g₀`, as elements of `A`. -/
def nfBasis : Fin 6 → A :=
  ![1, T.g 0, T.g 1, T.g 1 * T.g 0, T.g 0 * T.g 1, T.g 0 * T.g 1 * T.g 0]

/-- A coordinate vector, read as an element of `A`. -/
def nfEmbed (v : Fin 6 → R) : A := ∑ i, v i • nfBasis T i

theorem nfEmbed_unit : nfEmbed T (![1, 0, 0, 0, 0, 0] : Fin 6 → R) = 1 := by
  simp [nfEmbed, nfBasis, Fin.sum_univ_six]

theorem nfEmbed_add (u v : Fin 6 → R) : nfEmbed T (u + v) = nfEmbed T u + nfEmbed T v := by
  simp only [nfEmbed, Pi.add_apply, add_smul, Finset.sum_add_distrib]

theorem nfEmbed_smul (c : R) (v : Fin 6 → R) : nfEmbed T (c • v) = c • nfEmbed T v := by
  simp only [nfEmbed, Pi.smul_apply, smul_eq_mul, mul_smul, Finset.smul_sum]

section Relations

variable (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1)
  (hbr : T.g 1 * T.g 0 * T.g 1 = T.g 0 * T.g 1 * T.g 0)

include hq0 in
/-- Right multiplication by `g₀` is `mulσ₀` on coordinates. -/
theorem nfEmbed_mul_g0 (v : Fin 6 → R) :
    nfEmbed T v * T.g 0 = nfEmbed T (mulσ₀ h v) := by
  have e1 : T.g 1 * T.g 0 * T.g 0 = h • (T.g 1 * T.g 0) + T.g 1 := by
    rw [mul_assoc, hq0, mul_add, mul_smul_comm, mul_one]
  have e2 : T.g 0 * T.g 1 * T.g 0 * T.g 0 = h • (T.g 0 * T.g 1 * T.g 0) + T.g 0 * T.g 1 := by
    rw [mul_assoc, hq0, mul_add, mul_smul_comm, mul_one]
  simp only [nfEmbed, nfBasis, Fin.sum_univ_six, mulσ₀, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val, add_mul, smul_mul_assoc, one_mul,
    hq0, e1, e2, smul_add, add_smul, smul_smul]
  module

include hq1 hbr in
/-- Right multiplication by `g₁` is `mulσ₁` on coordinates (uses the braid relation). -/
theorem nfEmbed_mul_g1 (v : Fin 6 → R) :
    nfEmbed T v * T.g 1 = nfEmbed T (mulσ₁ h v) := by
  have e1 : T.g 0 * T.g 1 * T.g 1 = h • (T.g 0 * T.g 1) + T.g 0 := by
    rw [mul_assoc, hq1, mul_add, mul_smul_comm, mul_one]
  have e2 : T.g 0 * T.g 1 * T.g 0 * T.g 1 = h • (T.g 0 * T.g 1 * T.g 0) + T.g 1 * T.g 0 := by
    rw [← hbr, mul_assoc (T.g 1 * T.g 0) (T.g 1) (T.g 1), hq1, mul_add, mul_smul_comm,
      mul_one, hbr]
  simp only [nfEmbed, nfBasis, Fin.sum_univ_six, mulσ₁, Matrix.cons_val_zero,
    Matrix.cons_val_one, Matrix.cons_val, add_mul, smul_mul_assoc, one_mul,
    hq1, e1, e2, hbr, smul_add, add_smul, smul_smul]
  module

include hq0 hq1 hbr in
theorem nfEmbed_mul_letter (v : Fin 6 → R) (l : ℕ × R × R) (hl : l.1 ≤ 1) :
    nfEmbed T v * letterVal T 0 l = nfEmbed T (nfStep h v l) := by
  obtain ⟨i, s, b⟩ := l
  simp only [letterVal, zero_add, mul_add, mul_smul_comm, mul_one, nfStep, nfEmbed_add,
    nfEmbed_smul]
  rcases Nat.le_one_iff_eq_zero_or_eq_one.mp hl with rfl | rfl
  · simp [nfEmbed_mul_g0 T h hq0]
  · simp [nfEmbed_mul_g1 T h hq1 hbr]

include hq0 hq1 hbr in
theorem nfEmbed_mul_wordVal (w : List (ℕ × R × R)) (hw : ∀ l ∈ w, l.1 ≤ 1) :
    ∀ v : Fin 6 → R, nfEmbed T v * wordVal T 0 w = nfEmbed T (w.foldl (nfStep h) v) := by
  induction w with
  | nil => intro v; simp [wordVal]
  | cons l w ih =>
      intro v
      have hl := hw l (List.mem_cons_self ..)
      have hw' : ∀ l' ∈ w, l'.1 ≤ 1 := fun l' hl' => hw l' (List.mem_cons_of_mem _ hl')
      rw [show wordVal T 0 (l :: w) = letterVal T 0 l * wordVal T 0 w by
        simp [wordVal, List.map_cons, List.prod_cons], ← mul_assoc,
        nfEmbed_mul_letter T h hq0 hq1 hbr v l hl, ih hw', List.foldl_cons]

end Relations

/-- The Markov trace of the normal-form basis is `TRM`. -/
theorem tr_nfBasis (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) (i : Fin 6) :
    T.tr (nfBasis T i) = TRM T.z h i := by
  have t0 : T.tr (T.g 0) = T.z := by
    simpa using T.markov 0 1 (Subalgebra.one_mem _)
  have t1 : T.tr (T.g 1) = T.z := by
    simpa using T.markov 1 1 (Subalgebra.one_mem _)
  have t01 : T.tr (T.g 0 * T.g 1) = T.z ^ 2 := by
    rw [T.markov 1 (T.g 0) (T.g_mem 0), t0, sq]
  have t10 : T.tr (T.g 1 * T.g 0) = T.z ^ 2 := by rw [T.tr_mul_comm, t01]
  have t010 : T.tr (T.g 0 * T.g 1 * T.g 0) = h * T.z ^ 2 + T.z := by
    have hmem : h • T.g 0 + 1 ∈ T.H 1 :=
      Subalgebra.add_mem _ (Subalgebra.smul_mem _ (T.g_mem 0) h) (Subalgebra.one_mem _)
    rw [T.tr_mul_comm, ← mul_assoc, hq0, T.markov 1 _ hmem, map_add, map_smul, t0, T.tr_one,
      smul_eq_mul]
    ring
  fin_cases i <;> simp [nfBasis, TRM, T.tr_one, t0, t1, t01, t10, t010]

theorem tr_nfEmbed (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) (v : Fin 6 → R) :
    T.tr (nfEmbed T v) = trM T.z h v := by
  simp only [nfEmbed, map_sum, map_smul, smul_eq_mul, tr_nfBasis T h hq0, trM]

/-- **Trace of any `H₃` word with affine letters**: the trace of the fold. -/
theorem tr_wordVal_eq_trM (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1)
    (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1) (hbr : T.g 1 * T.g 0 * T.g 1 = T.g 0 * T.g 1 * T.g 0)
    (w : List (ℕ × R × R)) (hw : ∀ l ∈ w, l.1 ≤ 1) :
    T.tr (wordVal T 0 w) = trM T.z h (w.foldl (nfStep h) ![1, 0, 0, 0, 0, 0]) := by
  rw [← tr_nfEmbed T h hq0, ← nfEmbed_mul_wordVal T h hq0 hq1 hbr w hw, nfEmbed_unit, one_mul]

section Exact

variable (hq0 : T.g 0 * T.g 0 = h • T.g 0 + 1) (hq1 : T.g 1 * T.g 1 = h • T.g 1 + 1)
  (hbr : T.g 1 * T.g 0 * T.g 1 = T.g 0 * T.g 1 * T.g 0)

include hq0 hq1 hbr

/-- **`P_p` exactly**, on every Markov trace on a tower whose first two generators
satisfy the quadratic relation with scalar `h` and the braid relation. -/
theorem tr_protonWord (a : R) : T.tr (wordVal T 0 (protonWord h a)) = protonPoly h T.z a := by
  rw [tr_wordVal_eq_trM T h hq0 hq1 hbr _ (by simp [protonWord]), trM_protonWord]

/-- **`P_n` exactly.** -/
theorem tr_neutronWord (a : R) : T.tr (wordVal T 0 (neutronWord h a)) = neutronPoly h T.z a := by
  rw [tr_wordVal_eq_trM T h hq0 hq1 hbr _ (by simp [neutronWord]), trM_neutronWord]

end Exact

/-! ## Convention D: the rational functions of `q` -/

section ConventionD

variable {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0)

include hq hq2 h2

/-- At `h = q − q⁻¹`, `z = q³/(q²+1)`, `a = −h/2`:
`P_p = (q⁴+1)(q¹⁸ − 3q¹⁶ + 7q¹⁴ − 8q¹² + 10q¹⁰ − 9q⁸ + 10q⁶ − 6q⁴ + 3q² − 1) / (4q⁹(q²+1)²)`. -/
theorem protonPoly_conventionD :
    protonPoly (q - q⁻¹) (q ^ 3 / (q ^ 2 + 1)) (-(q - q⁻¹) / 2)
      = (q ^ 4 + 1) * (q ^ 18 - 3 * q ^ 16 + 7 * q ^ 14 - 8 * q ^ 12 + 10 * q ^ 10
          - 9 * q ^ 8 + 10 * q ^ 6 - 6 * q ^ 4 + 3 * q ^ 2 - 1) / (4 * q ^ 9 * (q ^ 2 + 1) ^ 2) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold protonPoly
  field_simp
  ring

/-- At convention D: `P_n = (q⁴+1)(q¹⁴ − 3q¹² + 4q¹⁰ − 4q⁸ + 5q⁶ − 4q⁴ + 3q² − 1) / (4q⁹)`. -/
theorem neutronPoly_conventionD :
    neutronPoly (q - q⁻¹) (q ^ 3 / (q ^ 2 + 1)) (-(q - q⁻¹) / 2)
      = (q ^ 4 + 1) * (q ^ 14 - 3 * q ^ 12 + 4 * q ^ 10 - 4 * q ^ 8 + 5 * q ^ 6
          - 4 * q ^ 4 + 3 * q ^ 2 - 1) / (4 * q ^ 9) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold neutronPoly
  field_simp
  ring

end ConventionD

end QOU.Mass.NucleonWordTraceClosedForm
