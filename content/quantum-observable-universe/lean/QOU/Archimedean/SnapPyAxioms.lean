/-
  # QOU.Archimedean.SnapPyAxioms

  Per-manifold axiomatic boundary for hyperbolic-volume constants
  computed externally by SnapPy (Goerner-Hoffman-Weeks).

  ## Why axioms

  SnapPy is a Python library; Lean cannot call it. The framework's
  production code (Python / mpmath at 50 dps) reads hyperbolic
  volumes from witness sidecars produced by
  `folio-assistant/computations/snappy_*.py` scripts. To bring
  those values into Lean rigorously, we introduce **one axiom per
  manifold**, named after the SnapPy manifold notation. Each
  axiom declares the existence of the volume as a real number;
  its closed-form characterisation (e.g. `Vol(L6a4) = 8·G`) lives
  in a separate theorem file where the categorical identity is
  formalised (e.g. `BorromeanVolumeCatalan.lean`).

  This pattern keeps Lean's formal layer **free of bare numerical
  literals** for SnapPy-computed values — downstream theorems
  refer to `snappy_<manifold>_volume` symbolically, not
  `7.327724…`.

  ## Naming convention

  - `snappy_<manifold_name>_volume : ℝ` — the canonical volume of
    the named manifold. The Lean-name uses the SnapPy notation
    lowercased and with underscores replacing hyphens. Examples:
    `L6a4`, `figure_eight` (= 4₁), `three_twist` (= 5₂).

  ## Witnesses producing these constants

  | Lean axiom | Producer script |
  |---|---|
  | `snappy_L6a4_volume` | `snappy_borromean_volume.py` |
  | `snappy_figure_eight_volume` | (TODO future migration) |
  | `snappy_three_twist_volume` | (TODO future migration) |

  Currently only L6a4 is migrated. Other per-manifold axioms can
  be added in follow-up commits as their producer scripts land.

  Ref: [adams1985hyperbolic] Adams, C.C. (1985), Proc. Amer. Math. Soc.
       100, 601-606.
  Ref: [culler2024] Goerner-Hoffman-Weeks SnapPy manifold census.
-/

import Mathlib.Data.Real.Basic

namespace QOU.Archimedean.SnapPyAxioms

/-- Hyperbolic volume of the SnapPy manifold `L6a4` — the
    Borromean rings complement, denoted `𝓑₃` in the QOU framework.

    Producer witness:
    `folio-assistant/computations/snappy-borromean-volume.witness.json`.
    Records the canonical value (Adams 1985: `Vol(L6a4) = 8·G`
    where G is Catalan's constant) at multiple precision tiers
    (15 / 30 / 50 / 100 / 200 dps). Independent cross-check via
    `folio-assistant/computations/borromean_volume_100dps.py`
    (Lobachevsky integration at 100 dps).

    The closed-form characterisation `snappy_L6a4_volume = 8·G`
    is the content of [`BorromeanVolumeCatalan.lean`'s
    `vol_B3_eq_8_catalan` theorem](./BorromeanVolumeCatalan.lean);
    when that theorem closes, this axiom becomes a named
    constant whose value is `8·G`.

    -- Ref: [culler2024] snappy-borromean-volume.witness.json
    -- Ref: [adams1985hyperbolic] Adams 1985, Proc. Amer. Math. Soc. 100, 601-606
-/
axiom snappy_L6a4_volume : ℝ

/-- The hyperbolic volume of L6a4 is positive. -/
-- Ref: [adams1985hyperbolic] hyperbolic structure non-degenerate
axiom snappy_L6a4_volume_pos : 0 < snappy_L6a4_volume

end QOU.Archimedean.SnapPyAxioms
