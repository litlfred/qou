/-!
# QOU.KnotRegistry — Formal Knot Registry with Alexander-Briggs Indexing

A structured registry of all knots relevant to the Quantum Observable Universe
and Bring's Surface.  Each entry carries:

  1. **Alexander-Briggs index** (primary key, e.g. `"4_1"`)
  2. **Planar Diagram code** (from `QOU.KnotTheory`)
  3. **Hyperbolic volume** with SnapPy-grade precision
  4. **QOU physical identity** (the particle the knot encodes)
  5. **Knot Atlas URL** for machine-readable external linkage

## Data Sources

- Planar diagram codes: The Knot Atlas / KnotInfo
- Hyperbolic volumes: SnapPy census (Culler et al.)
- QOU identities: Manuscript Conjecture 4.25 and §5

## Convention

Every `def` or `theorem` involving a registered knot includes a docstring
with a persistent link to `http://katlas.org/wiki/<knot>`.
-/

import Mathlib.Data.Real.Basic
import QOU.KnotTheory

open QOU.KnotTheory

namespace QOU.KnotRegistry

/-! ## QOU Physical Identity -/

/-- The physical particle a knot encodes in the QOU framework. -/
inductive QOUIdentity where
  /-- The neutrino — trivial knot, SU(2) vacuum baseline. -/
  | neutrino
  /-- The electron — Generation 1, B₃ monodromy source for Bring's Surface. -/
  | electron
  /-- The muon — Generation 2, hyperbolic volume residue for mass derivation. -/
  | muon
  /-- The photon — background flux on the exceptional divisor. -/
  | photon
  deriving DecidableEq, Repr

/-! ## Registry Entry -/

/-- A fully-specified knot registry entry.

    Each entry is the "settled type" for one knot in the QOU formalization:
    it pins the Alexander-Briggs name, combinatorial PD code, computed
    volume, physical identity, and external reference URL. -/
structure KnotEntry where
  /-- Alexander-Briggs index, e.g. `"4_1"`. Primary key. -/
  ab_index : String
  /-- Planar diagram (PD code) from `QOU.KnotTheory`. -/
  diagram : PlanarDiagram
  /-- Hyperbolic volume of the knot complement (SnapPy). -/
  volume : HyperbolicVolume
  /-- The QOU particle this knot represents. -/
  identity : QOUIdentity
  /-- Persistent URL to The Knot Atlas wiki page. -/
  atlas_url : String
  deriving Repr

/-! ## The Registry — Primary Knot Definitions -/

/-- **Unknot (0₁)** — the trivial knot.
    QOU identity: **Neutrino**.  Represents the SU(2) vacuum state and
    the baseline vacuum drag with zero crossing number.

    Knot Atlas: <http://katlas.org/wiki/0_1>
    Hyperbolic volume: 0  (non-hyperbolic) -/
noncomputable def unknotEntry : KnotEntry where
  ab_index := "0_1"
  diagram := unknot
  volume := {
    value := 0
    error_bound := 0
    error_nonneg := le_refl 0
  }
  identity := .neutrino
  atlas_url := "http://katlas.org/wiki/0_1"

/-- **Trefoil (3₁)** — the simplest non-trivial knot.
    QOU identity: **Electron** (Generation 1).  The trefoil's braid group
    B₃ monodromy generates the branching structure of Bring's Surface.

    Knot Atlas: <http://katlas.org/wiki/3_1>
    Hyperbolic volume: 0  (torus knot — non-hyperbolic)
    Jones polynomial: −t⁻⁴ + t⁻³ + t⁻¹ -/
noncomputable def trefoilEntry : KnotEntry where
  ab_index := "3_1"
  diagram := trefoil
  volume := vol_trefoil
  identity := .electron
  atlas_url := "http://katlas.org/wiki/3_1"

/-- **Figure-Eight Knot (4₁)** — the simplest hyperbolic knot.
    QOU identity: **Muon** (Generation 2).  Its hyperbolic volume
    Vol(4₁) ≈ 2.0298832128 is the numerator in the mass-ratio derivation
    `m_μ/m_e = Vol(4₁) / ℏ_q²`.

    Knot Atlas: <http://katlas.org/wiki/4_1>
    Hyperbolic volume: 2.0298832128 ± 1×10⁻¹⁰  (SnapPy / Bloch-Wigner)
    Ref: [turaev2010] https://doi.org/10.1515/9783110221831 -/
noncomputable def figureEightEntry : KnotEntry where
  ab_index := "4_1"
  diagram := figureEight
  volume := vol_figure_eight
  identity := .muon
  atlas_url := "http://katlas.org/wiki/4_1"

/-- **Trivial Knot (unknot alias)** — the photon background.
    QOU identity: **Photon**.  Represents the background flux on the
    exceptional divisor; topologically equivalent to the unknot but
    distinguished by its physical role in the QOU gauge field.

    Knot Atlas: <http://katlas.org/wiki/0_1> -/
noncomputable def photonEntry : KnotEntry where
  ab_index := "0_1"
  diagram := unknot
  volume := {
    value := 0
    error_bound := 0
    error_nonneg := le_refl 0
  }
  identity := .photon
  atlas_url := "http://katlas.org/wiki/0_1"

/-! ## Registry Collection -/

/-- The complete knot registry: all knots with settled types in the QOU
    formalization.  Ordered by Alexander-Briggs crossing number. -/
noncomputable def registry : List KnotEntry :=
  [unknotEntry, trefoilEntry, figureEightEntry, photonEntry]

/-! ## Registry Queries -/

/-- Look up a knot entry by its Alexander-Briggs index. -/
noncomputable def lookup (ab : String) : Option KnotEntry :=
  registry.find? (fun e => e.ab_index == ab)

/-- Look up a knot entry by its QOU physical identity. -/
noncomputable def lookupByIdentity (id : QOUIdentity) : Option KnotEntry :=
  registry.find? (fun e => e.identity == id)

/-! ## Volume Extraction -/

/-- Extract the hyperbolic volume value from a registry entry. -/
noncomputable def KnotEntry.volumeValue (e : KnotEntry) : ℝ :=
  e.volume.value

/-- The figure-eight volume extracted from the registry matches the
    constant used in `MassDerivation`. -/
-- Ref: [turaev2010] https://doi.org/10.1515/9783110221831 — Vol(4₁) via SnapPy
theorem figureEight_volume_consistent :
    figureEightEntry.volumeValue = vol_figure_eight.value := by
  rfl

/-- The trefoil (torus knot) has zero hyperbolic volume. -/
theorem trefoil_volume_zero :
    trefoilEntry.volumeValue = 0 := by
  rfl

/-- The unknot has zero hyperbolic volume. -/
theorem unknot_volume_zero :
    unknotEntry.volumeValue = 0 := by
  rfl

/-! ## Crossing Number Properties -/

/-- The unknot has 0 crossings. -/
theorem unknot_crossing_count :
    unknotEntry.diagram.crossingCount = 0 := by
  rfl

/-- The trefoil has 3 crossings. -/
theorem trefoil_crossing_count :
    trefoilEntry.diagram.crossingCount = 3 := by
  rfl

/-- The figure-eight knot has 4 crossings. -/
theorem figureEight_crossing_count :
    figureEightEntry.diagram.crossingCount = 4 := by
  rfl

end QOU.KnotRegistry
