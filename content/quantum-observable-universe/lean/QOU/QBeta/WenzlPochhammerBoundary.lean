import Mathlib.RingTheory.RootsOfUnity.Basic
import Mathlib.Tactic

/-!
# Wenzl–Pochhammer boundaries — quantum integers vanishing at roots of unity

Fibre-side infrastructure for the z→c_k evaluation-map program (PR #3458).
The Wenzl–Pochhammer / Habiro-tower **annihilator boundaries** are the roots of
unity at which the quantum integer `[n]_q = (q^n − 1)/(q − 1)` vanishes: at a
primitive `m`-th root of unity `ζ` (with `m > 1`), `[n]_ζ = 0` exactly when
`m ∣ n`. In particular `[4m]_q = 0` at `ζ_{4m}` are the boundaries at which the
Habiro tower truncates (`[4]_q=0` at ζ₄, `[8]_q=0` at ζ₈ — the second boundary
that the c_8 pattern-break aligns with; see
`docs/scope/2026-07-07-qbeta-ck-special-function-candidate-landscape.md`).

These are the **phase-channel** structure identified in the candidate triage:
the c_k live at root-of-unity boundaries, not on the smooth real-q axis (the
excluded magnitude channel).

The f-map is now established (main `a5bb64f3`) to be a **resurgence connection**,
not a coefficient map: the colored-Jones / Ohtsuki *geometric-connection* series
is divergent (essential singularity at `q=1`, Kashaev `~ e^{N·Vol/2π}`) while the
`Q_β = ∏(1+c_k u^k)` *trivial-connection* series is regular, so no analytic
change of variables links them — the c_k ↔ κ_k relation is Stokes data
(Garoufalidis–Gu–Mariño). The boundary fact below is a pure algebraic truth that
is agnostic to that: it pins **where** the geometric-connection singularities sit
(the roots of unity `[4m]_q=0`), which is the input to the Stokes/resurgence
analysis, independent of the connection being resurgent rather than a coefficient
re-basing.
-/

namespace QOU.QBeta

/-- The quantum integer `[n]_q = (q^n − 1)/(q − 1)` vanishes at a primitive
`m`-th root of unity `ζ` (with `m > 1`) exactly when `m ∣ n`. This is the
Wenzl–Pochhammer boundary structure: the roots of unity at which the Habiro
tower truncates. -/
theorem qInt_root_vanishes_iff_dvd {ζ : ℂ} {m : ℕ} (hm : 1 < m)
    (hζ : IsPrimitiveRoot ζ m) (n : ℕ) :
    (ζ ^ n - 1) / (ζ - 1) = 0 ↔ m ∣ n := by
  have hζ1 : ζ ≠ 1 := hζ.ne_one hm
  have hsub : ζ - 1 ≠ 0 := sub_ne_zero.mpr hζ1
  rw [div_eq_zero_iff]
  simp only [hsub, or_false, sub_eq_zero]
  exact hζ.pow_eq_one_iff_dvd n

/-- The Habiro-tower boundaries `[4m]_q = 0` at `ζ_{4m}` (the `[4]_q=0` /
`[8]_q=0` / … annihilators): a primitive `4m`-th root of unity kills `[4m]_q`. -/
theorem qInt_fourm_vanishes_at_zeta_fourm {ζ : ℂ} {m : ℕ} (hm : 0 < m)
    (hζ : IsPrimitiveRoot ζ (4 * m)) :
    (ζ ^ (4 * m) - 1) / (ζ - 1) = 0 := by
  have h1 : 1 < 4 * m := by omega
  exact (qInt_root_vanishes_iff_dvd h1 hζ (4 * m)).mpr dvd_rfl

end QOU.QBeta
