import Mathlib.Data.Real.Basic
import QOU.KnotTheory
import Mathlib.Tactic.NormNum

/-!
# QOU.KnotRegistry — Formal Knot Registry with Alexander-Briggs Indexing

A structured registry of all knots relevant to the Quantum Observable Universe
and Bring's Surface.  Each entry carries:

  1. **Alexander-Briggs index** (primary key, e.g. `"4_1"`)
  2. **Braid word** (from `QOU.KnotTheory`, Markov closure to recover the link)
  3. **Hyperbolic volume** with SnapPy-grade precision
  4. **QOU physical identity** (the particle the knot encodes)
  5. **Knot Atlas URL** for machine-readable external linkage

## Data Sources

- Braid words: The Knot Atlas / KnotInfo (converted from PD / Gauss code)
- Hyperbolic volumes: SnapPy census (Culler et al.)
- QOU identities: Manuscript Conjecture 4.25 and §5

## Convention

Every `def` or `theorem` involving a registered knot includes a docstring
with a persistent link to `http://katlas.org/wiki/<knot>`.
-/


open QOU.KnotTheory

namespace QOU.KnotRegistry

/-! ## QOU Physical Identity -/

/-- The physical particle a knot encodes in the QOU framework. -/
inductive QOUIdentity where
  /-- The neutrino — trivial knot, SU(2) vacuum baseline. -/
  | neutrino
  /-- The electron — Generation 1, B₃ monodromy source for Bring's Surface. -/
  | electron
  /-- The muon — Generation 2, cinquefoil T_{2,5} on Reeb divisor. -/
  | muon
  /-- The tau lepton — Generation 3, septafoil T_{2,7} on Reeb divisor. -/
  | tauLepton
  /-- The Higgs field / mass mechanism — figure-eight 4₁, amphichiral. -/
  | higgsField
  /-- The photon — background flux on the exceptional divisor. -/
  | photon
  /-- The strong force — Hopf link, internal binding energy. -/
  | strongForce
  /-- The nucleon — Borromean rings, color-exchange entanglement. -/
  | nucleon
  deriving DecidableEq, Repr

/-! ## Registry Entry -/

/-- A fully-specified knot registry entry.

    Each entry is the "settled type" for one knot in the QOU formalization:
    it pins the Alexander-Briggs name, braid word, computed volume,
    physical identity, and external reference URL. -/
structure KnotEntry where
  /-- Alexander-Briggs index, e.g. `"4_1"`. Primary key. -/
  ab_index : String
  /-- Braid word (Markov-closure encoding) from `QOU.KnotTheory`. -/
  braid : BraidWord
  /-- Hyperbolic volume of the knot complement (SnapPy). -/
  volume : HyperbolicVolume
  /-- The QOU particle this knot represents. -/
  identity : QOUIdentity
  /-- Persistent URL to The Knot Atlas wiki page. -/
  atlas_url : String

/-! ## The Registry — Primary Knot Definitions -/

/-- **Unknot (0₁)** — the trivial knot.
    QOU identity: **Neutrino**.  Represents the SU(2) vacuum state and
    the baseline vacuum drag with zero crossing number.

    Knot Atlas: <http://katlas.org/wiki/0_1>
    Hyperbolic volume: 0  (non-hyperbolic) -/
noncomputable def unknotEntry : KnotEntry where
  ab_index := "0_1"
  braid := unknot
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
  braid := trefoil
  volume := vol_trefoil
  identity := .electron
  atlas_url := "http://katlas.org/wiki/3_1"

/-- **Figure-Eight Knot (4₁)** — the simplest hyperbolic knot.
    QOU identity: **Higgs field (mass mechanism)**.  Its hyperbolic volume
    Vol(4₁) ≈ 2.02988321281931 is the numerator in the mass-ratio derivation
    `m_μ/m_e = Vol(4₁) / ℏ_q²`.  The figure-eight is amphichiral
    (4₁ = 4₁⁻¹), so the Higgs field is its own antiparticle.
    Exact: 3 · Cl₂(π/3) (OEIS A091518).

    Knot Atlas: <http://katlas.org/wiki/4_1>
    Hyperbolic volume: 2.02988321281931 ± 1×10⁻¹⁴  (SnapPy / Bloch-Wigner)
    Ref: [turaev2010] https://doi.org/10.1515/9783110221831 -/
noncomputable def figureEightEntry : KnotEntry where
  ab_index := "4_1"
  braid := figureEight
  volume := vol_figure_eight
  identity := .higgsField
  atlas_url := "http://katlas.org/wiki/4_1"

/-- **Empty Knot (photon background)** — the identity braid
    $\mathbf{1}$ with zero crossings.
    QOU identity: **Photon**.  Represents the background flux on the
    exceptional divisor.  The closure of the identity braid is a
    disjoint union of unknots; the entry is distinguished from the
    single-component unknot ($0_1$, the neutrino) by carrying no
    strand at all in its bare presentation.  Both have Jones
    polynomial $1$, so transfer-matrix arithmetic coincides, but the
    physical roles differ: photon (empty knot, $\varnothing$) vs.
    neutrino (unknot, $0_1$).  This entry records only the **bare**
    photon; the genuine photon is the four-term Hecke element
    `PhotonHeckeElement` defined below.

    Knot Atlas (closest entry, single-strand limit):
    <http://katlas.org/wiki/0_1> -/
noncomputable def photonEntry : KnotEntry where
  -- Unique key (not "0_1") so `lookup` can distinguish the photon
  -- (empty knot ∅, identity braid) from the neutrino (unknot 0_1).
  -- Both have Jones polynomial 1 and zero volume; the entry reuses
  -- the `unknot` braid word as a single-component placeholder
  -- because `BraidWord` does not yet model a genuinely empty
  -- Markov closure (zero components).
  ab_index := "empty"
  braid := unknot
  volume := {
    value := 0
    error_bound := 0
    error_nonneg := le_refl 0
  }
  identity := .photon
  atlas_url := "http://katlas.org/wiki/0_1"

/-! ## The Photon as a Four-Term Hecke Element

The registry's `photonEntry` records the photon's **bare** limit — the
identity braid `𝟙` — because `KnotEntry` carries a single `BraidWord`,
not a Hecke-algebra superposition.  The genuine photon is a four-term
element of `H₃(q)`, `γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹` (`def:photon`; the last
term is the chiral pair-production vertex by owner ruling 2026-11-18, bean
`qou-99qc`). Since `σ₀σ₁⁻¹ = σ₀σ₁ − h·σ₀`, its support in the normal-form basis is
the four words `{𝟙, σ₀, σ₁, σ₀σ₁}`.  It is therefore
**not** the unknot `0₁` (which is the neutrino): its support has four
words, and its two-photon products generate the full operator basis
(see the `gamma-gamma-generates-particles` proposition). -/

/-- The photon as a four-term element of the Hecke algebra `H₃(q)`:
    `γ = 𝟙 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁⁻¹`.  The colour weights are formal,
    so this is stated over a generic commutative ring (no `q₀`). -/
structure PhotonHeckeElement (R : Type*) [CommRing R] where
  /-- Colour weight of `σ₀`. -/
  phi0 : R
  /-- Colour weight of `σ₁`. -/
  phi1 : R
  /-- Colour weight of the chiral vertex `σ₀σ₁⁻¹`. -/
  phi01 : R

/-- The four normal-form basis words carrying the photon, as `σ`-index
    sequences: `𝟙 = []`, `σ₀ = [0]`, `σ₁ = [1]`, `σ₀σ₁ = [0,1]` (the vertex
    `σ₀σ₁⁻¹ = σ₀σ₁ − hσ₀` lies in their span). -/
def photonSupportWords : List (List ℕ) := [[], [0], [1], [0, 1]]

/-- The photon is a **four-term** element: its support has four basis
    words, distinguishing it from the single-component unknot `0₁`
    (the neutrino). -/
theorem photonSupportWords_length : photonSupportWords.length = 4 := by
  decide

/-- The bare (free) photon: all colour weights vanish, leaving the
    identity term `𝟙` alone — the limit recorded by `photonEntry`. -/
def barePhoton (R : Type*) [CommRing R] : PhotonHeckeElement R := ⟨0, 0, 0⟩

/-- **Hopf Link (L2a1)** — the simplest non-trivial link (2 components).
    QOU identity: **Strong Force**.  The Hopf link represents the
    internal binding energy between quarks; invisible to the ℂP¹ base.

    Knot Atlas: <http://katlas.org/wiki/Hopf_Link>
    Hyperbolic volume: 0  (torus link — non-hyperbolic)
    Components: 2 -/
noncomputable def hopfLinkEntry : KnotEntry where
  ab_index := "L2a1"
  braid := hopfLink
  volume := {
    value := 0
    error_bound := 0
    error_nonneg := le_refl 0
  }
  identity := .strongForce
  atlas_url := "http://katlas.org/wiki/Hopf_Link"

/-- **Borromean Rings (6₂³)** — three mutually linked rings, no two
    of which are linked pairwise.
    QOU identity: **Nucleon**.  The Borromean topology encodes the
    color-exchange entanglement of three quark tubes (uud or udd).

    Mathematical value (exact, transcendental): `8 · G` where
    `G` = Catalan's constant (OEIS A006752).  The `volume.value`
    field below is the 50-dps decimal *approximation* to that exact
    value — the EXACT symbol lives in `QOU.Archimedean.vol_B3`
    (defined as `8 · catalan_G`).

    Knot Atlas: <http://katlas.org/wiki/L6a4>
    Hyperbolic volume (catalog literal): 50 dps,
    `7.32772475341775212043682811945907288619319499425336`
    `± 1×10⁻⁵⁰`.  Bumped 2026-06-07 from the previous 15-dps
    literal `7.32772475341775 ± 1×10⁻¹⁴` to match the project's
    standard working serialization precision (50 dps per
    `computations/_precision.py`).
    Source: **mpmath `mp.catalan` at `mp.dps = 50`, evaluated as
    `8 * mp.catalan`** — a closed-form-derived decimal (computed
    from the exact identity `Vol(L6a4) = 8·G`), NOT a SnapPy
    numerical measurement. The numerical value agrees with SnapPy's
    `M = SnapPy.Manifold("L6a4"); M.volume()` to 15+ digits (and
    with the proof of Adams (1985) that the two are equal), but
    the literal stored here is computed from the closed form so
    its precision is bounded by `mp.dps`, not by SnapPy's `f64`
    convergence floor. (Copilot review #1978: previous docstring
    conflated the two provenances.)
    Components: 3

    Note: this `value` field is a data-catalog decimal kept for
    downstream consumers that want a literal rather than the
    symbolic form. The categorical `QOU.Archimedean.vol_B3` is
    the EXACT transcendental (`8 · catalan_G`) — use it in
    proofs and as the canonical Borromean volume reference. -/
noncomputable def borromeanRingsEntry : KnotEntry where
  ab_index := "L6a4"
  braid := borromeanRings
  volume := {
    value := 7.32772475341775212043682811945907288619319499425336
    error_bound := 1e-50
    error_nonneg := by norm_num
  }
  identity := .nucleon
  atlas_url := "http://katlas.org/wiki/L6a4"

/-! ## Registry Collection -/

/-- The complete knot registry: all knots with settled types in the QOU
    formalization.  Ordered by Alexander-Briggs crossing number. -/
noncomputable def registry : List KnotEntry :=
  [unknotEntry, trefoilEntry, figureEightEntry, photonEntry,
   hopfLinkEntry, borromeanRingsEntry]

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
    unknotEntry.braid.crossingCount = 0 := by
  rfl

/-- The trefoil has 3 crossings. -/
theorem trefoil_crossing_count :
    trefoilEntry.braid.crossingCount = 3 := by
  rfl

/-- The figure-eight knot has 4 crossings. -/
theorem figureEight_crossing_count :
    figureEightEntry.braid.crossingCount = 4 := by
  rfl

end QOU.KnotRegistry
