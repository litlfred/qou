#!/usr/bin/env python3
"""Generate QOU/AtomicMass.lean from the canonical data table.

The atomic-mass audit file is *generated*, not hand-written: the CODATA
2022 / AME2020 constants and the 118-element binding-energy table live in
``atomic_mass_data.json`` (exact decimal strings, with provenance), and the
Lean proofs are emitted uniformly from a single template.  This keeps the
data auditable in one place and the proofs uniform, and lets CI guard
against drift (a hand-edit of the generated ``.lean`` that the data table no
longer reproduces).

Usage
-----
    python3 gen_atomic_mass.py            # regenerate AtomicMass.lean (write)
    python3 gen_atomic_mass.py --check    # CI drift gate: exit 1 if stale

Both modes are path-independent (resolved relative to this script), so the
same invocation works locally and in CI.
"""
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "atomic_mass_data.json"
OUT_PATH = SCRIPT_DIR.parent / "QOU" / "AtomicMass.lean"

BANNER = """\
-- ╔═══════════════════════════════════════════════════════════════════╗
-- ║  GENERATED FILE — DO NOT EDIT BY HAND.                              ║
-- ║  Source of truth: scripts/atomic_mass_data.json (data) +           ║
-- ║                   scripts/gen_atomic_mass.py    (template).         ║
-- ║  Regenerate:  python3 scripts/gen_atomic_mass.py                    ║
-- ║  CI drift gate (atomic-mass-gen-check.yml) fails on any divergence. ║
-- ╚═══════════════════════════════════════════════════════════════════╝
"""

# Everything between the constants block and the dataset table is static
# (the algebra does not depend on the numeric values), so it lives here as a
# template with three injection points: the constants, the two data-source
# URLs, and the nuclide table.
TEMPLATE = r'''import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.AtomicMass.MagicNumbersFromQ

/-!
  QOU Atomic Mass Predictions — CODATA 2022 vs AME2020 Audit

  Two independent mass sources are compared for each element:
  - **CODATA 2022** constituent masses (m_p, m_n, m_e)
  - **AME2020** atomic mass unit (u) and mass excesses (Δ_H, Δ_n)

  For an element with `Z` protons and `N` neutrons (`A = Z + N`) the
  CODATA path is `Z·m_p + N·m_n + Z·m_e − A·(B/A)` and the AME path is
  `A·u + Z·Δ_H + N·Δ_n − A·(B/A)`.  Their difference is the *structural
  offset*

      codataMass − ameMass = Z·offset_Z + N·offset_N            (1)

  with
  - `offset_Z = (m_p + m_e) − (u + Δ_H) ≈ 1.546 × 10⁻⁵ MeV` — the
    H-atom electron binding energy, absent from the free `m_p + m_e`
    but present in `M_H`; and
  - `offset_N = m_n − (u + Δ_n) ≈ 1.46 × 10⁻⁶ MeV` — the residual
    CODATA-2022 vs AME2020 neutron-mass discrepancy.

  Both offsets are tiny.  Identity (1) (`codata_minus_ame_offset`) and
  the resulting per-element bound (`deviation_uniform`) are proved
  **generically** for every `ElementDatum`, subsuming what were 118
  copy-pasted per-element theorems.  The curated 118-element AME2020
  dataset (Z = 1…118) is retained as `elements`.

  Correction note: the historical per-Z-only form `… = Z·offset_Z`
  is *false* — the `N·offset_N` term does not cancel against the
  `B/A` binding term (that would require `m_n = u + Δ_n`, which fails
  by ≈ 1.46 eV).  Identity (1) is the corrected statement.
-/

namespace QOU.AtomicMass

/-! ## CODATA 2022 Constituent Masses
Source: NIST CODATA 2022, __CODATA_URL__ -/

__CODATA_CONSTANTS__

/-! ## AME2020 Constants
Source: Atomic Mass Evaluation 2020 (Wang et al., Chinese Physics C 45,
030003), __AME_URL__ -/

__AME_CONSTANTS__

/-! ## Mass computation functions -/

/-- CODATA path: `M = Z·m_p + N·m_n + Z·m_e − A·(B/A)`. -/
noncomputable def codata_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  (Z : ℝ) * codata_m_p + (N : ℝ) * codata_m_n + (Z : ℝ) * codata_m_e
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- AME2020 path: `M = A·u + Z·Δ_H + N·Δ_n − A·(B/A)`. -/
noncomputable def ame2020_atomic_mass (Z N : ℕ) (BperA : ℝ) : ℝ :=
  ((Z : ℝ) + (N : ℝ)) * ame_u + (Z : ℝ) * ame_delta_H + (N : ℝ) * ame_delta_n
    - ((Z : ℝ) + (N : ℝ)) * BperA

/-- Element data: atomic number, neutron number, AME2020 B/A (MeV). -/
structure ElementDatum where
  /-- Atomic number. -/
  Z : ℕ
  /-- Neutron number. -/
  N : ℕ
  /-- Binding energy per nucleon from AME2020 (MeV). -/
  BperA : ℝ

/-- CODATA-derived atomic mass for an element. -/
noncomputable def ElementDatum.codataMass (d : ElementDatum) : ℝ :=
  codata_atomic_mass d.Z d.N d.BperA

/-- AME2020-derived atomic mass for an element. -/
noncomputable def ElementDatum.ameMass (d : ElementDatum) : ℝ :=
  ame2020_atomic_mass d.Z d.N d.BperA

/-! ## Structural offsets -/

/-- Per-proton CODATA−AME2020 offset: `(m_p + m_e) − (u + Δ_H)`
    ≈ 1.546 × 10⁻⁵ MeV (H-atom electron binding energy). -/
noncomputable def codata_ame_offset_per_Z : ℝ :=
  (codata_m_p + codata_m_e) - (ame_u + ame_delta_H)

/-- Per-neutron CODATA−AME2020 offset: `m_n − (u + Δ_n)`
    ≈ 1.46 × 10⁻⁶ MeV (residual CODATA-2022 vs AME2020 neutron-mass
    discrepancy).  Nonzero — this is the term the historical
    `= Z·offset_Z` lemma wrongly dropped. -/
noncomputable def codata_ame_offset_per_N : ℝ :=
  codata_m_n - (ame_u + ame_delta_n)

/-- **Structural identity.**  For any element datum the CODATA−AME2020
    mass difference is `Z·offset_Z + N·offset_N`.  The `A·(B/A)`
    binding terms cancel; the proton and neutron offsets do not. -/
theorem ElementDatum.codata_minus_ame_offset (e : ElementDatum) :
    e.codataMass - e.ameMass
      = (e.Z : ℝ) * codata_ame_offset_per_Z
        + (e.N : ℝ) * codata_ame_offset_per_N := by
  unfold ElementDatum.codataMass ElementDatum.ameMass
    codata_atomic_mass ame2020_atomic_mass
    codata_ame_offset_per_Z codata_ame_offset_per_N
  ring

/-- The per-proton offset is below 2 × 10⁻⁵ MeV. -/
theorem codata_ame_offset_per_Z_bound : |codata_ame_offset_per_Z| < 0.00002 := by
  unfold codata_ame_offset_per_Z codata_m_p codata_m_e ame_u ame_delta_H
  rw [abs_lt]; constructor <;> norm_num

/-- The per-neutron offset is below 2 × 10⁻⁶ MeV. -/
theorem codata_ame_offset_per_N_bound : |codata_ame_offset_per_N| < 0.000002 := by
  unfold codata_ame_offset_per_N codata_m_n ame_u ame_delta_n
  rw [abs_lt]; constructor <;> norm_num

/-- **Uniform per-element deviation bound.**  For any element datum,
    `|codataMass − ameMass| ≤ Z·|offset_Z| + N·|offset_N|`.  This
    single generic statement subsumes the per-element numerical checks
    (the offsets are bounded by `codata_ame_offset_per_{Z,N}_bound`). -/
theorem ElementDatum.deviation_uniform (e : ElementDatum) :
    |e.codataMass - e.ameMass|
      ≤ (e.Z : ℝ) * |codata_ame_offset_per_Z|
        + (e.N : ℝ) * |codata_ame_offset_per_N| := by
  rw [ElementDatum.codata_minus_ame_offset]
  have hZ : (0 : ℝ) ≤ (e.Z : ℝ) := Nat.cast_nonneg _
  have hN : (0 : ℝ) ≤ (e.N : ℝ) := Nat.cast_nonneg _
  calc |(e.Z : ℝ) * codata_ame_offset_per_Z + (e.N : ℝ) * codata_ame_offset_per_N|
      ≤ |(e.Z : ℝ) * codata_ame_offset_per_Z|
          + |(e.N : ℝ) * codata_ame_offset_per_N| := abs_add_le _ _
    _ = (e.Z : ℝ) * |codata_ame_offset_per_Z|
          + (e.N : ℝ) * |codata_ame_offset_per_N| := by
        rw [abs_mul, abs_mul, abs_of_nonneg hZ, abs_of_nonneg hN]

/-! ## Headline numerical checks (concrete instances of the bound) -/

/-- Hydrogen (Z=1, N=0). -/
noncomputable def hydrogen : ElementDatum := ⟨1, 0, 0.0⟩
/-- Iron-56 (Z=26, N=30): peak binding energy per nucleon. -/
noncomputable def iron56 : ElementDatum := ⟨26, 30, 8.7903⟩
/-- Oganesson-294 (Z=118, N=176): heaviest tabulated element. -/
noncomputable def oganesson : ElementDatum := ⟨118, 176, 6.972⟩

example : |hydrogen.codataMass - hydrogen.ameMass| < 0.0001 := by
  simp only [hydrogen, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

example : |iron56.codataMass - iron56.ameMass| < 0.0008 := by
  simp only [iron56, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

example : |oganesson.codataMass - oganesson.ameMass| < 0.0032 := by
  simp only [oganesson, ElementDatum.codataMass, ElementDatum.ameMass,
    codata_atomic_mass, ame2020_atomic_mass,
    codata_m_p, codata_m_n, codata_m_e, ame_u, ame_delta_H, ame_delta_n]
  rw [abs_lt]; constructor <;> norm_num

/-! ## AME2020 dataset (Z = 1…118)

Curated `(symbol, ⟨Z, N, B/A⟩)` table.  Every entry satisfies
`deviation_uniform`; B/A values are AME2020 binding energy per
nucleon in MeV.  Source: __AME_URL__ -/

/-- The 118 tabulated elements with their AME2020 binding energies. -/
noncomputable def elements : List (String × ElementDatum) :=
  [
__TABLE__
  ]

end QOU.AtomicMass
'''


def render(data: dict) -> str:
    consts = data["constants"]
    sources = data["sources"]

    def const_block(prefix: str) -> str:
        lines = []
        for name, c in consts.items():
            if not name.startswith(prefix):
                continue
            lines.append(f"/-- {c['lean_doc']} -/")
            lines.append(f"noncomputable def {name} : ℝ := {c['value']}")
            lines.append("")
        return "\n".join(lines).rstrip()

    rows = []
    for nuc in data["nuclides"]:
        sym, z, n, b = nuc["sym"], nuc["Z"], nuc["N"], nuc["BperA"]
        rows.append(f'    ("{sym}", ⟨{z}, {n}, {b}⟩),')
    rows[-1] = rows[-1].rstrip(",")  # no trailing comma on the last list entry
    table = "\n".join(rows)

    body = (TEMPLATE
            .replace("__CODATA_URL__", sources["codata2022"])
            .replace("__AME_URL__", sources["ame2020"])
            .replace("__CODATA_CONSTANTS__", const_block("codata_"))
            .replace("__AME_CONSTANTS__", const_block("ame_"))
            .replace("__TABLE__", table))
    return BANNER + body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 (with a diff) if the committed file is stale")
    args = ap.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    rendered = render(data)

    if args.check:
        current = OUT_PATH.read_text(encoding="utf-8") if OUT_PATH.exists() else ""
        if current == rendered:
            print(f"OK — {OUT_PATH.name} is in sync with {DATA_PATH.name}")
            return 0
        sys.stderr.write(
            f"::error::{OUT_PATH} is stale — regenerate with "
            f"`python3 {Path(__file__).name}`.\n")
        diff = difflib.unified_diff(
            current.splitlines(keepends=True), rendered.splitlines(keepends=True),
            fromfile="committed", tofile="generated", n=2)
        sys.stderr.writelines(list(diff)[:80])
        return 1

    OUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({rendered.count(chr(10)) + 1} lines, "
          f"{len(data['nuclides'])} nuclides, {len(data['constants'])} constants)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
