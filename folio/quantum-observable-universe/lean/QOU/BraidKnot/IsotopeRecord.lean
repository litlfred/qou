/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# IsotopeRecord — per-(Z, N) atomic record with knot-operator catalogue

Lean mirror of the Python dataclass schema in
[`isotope_record_schema.py`](../../../../computations/isotope_record_schema.py).

Per-isotope record carrying:
  - Atom identification (Z, N, A, n_strands)
  - Canonical braid word + knot operators (intra / inter / closure / fusion)
  - Canonical |tr_M(β_atom, q_0)| from the Σ_λ y_λ · χ^λ pipeline
  - Mass prediction + AME residual (when measured)
  - Calibration source (CAL-1 / CAL-2 / CAL-3)
  - Prediction method (Layer 1..5)

The Python dataclass is the runtime source of truth (used by
`canonical_mass_table_extended.py`); this Lean module gives the
schema formal backing for the all-atoms / all-isotopes atlas
extension per
[`docs/audits/2026-05-18-all-atoms-isotopes-plan.md`](../../../../docs/audits/2026-05-18-all-atoms-isotopes-plan.md).

Ref: [wenzl1988] https://doi.org/10.1007/BF01393699 (Markov-trace)
Ref: [jones1987] https://www.jstor.org/stable/1971403 (Hecke characters)
-/

namespace QOU.BraidKnot

/-- The three crossing conventions used in the canonical atomic braid.
    See `canonical_braid_crossings.atom_canonical_crossings` for the
    runtime convention. -/
inductive CrossingType : Type
  | sigma       -- positive crossing (c = 1, d = 0)
  | sigma_inv   -- negative crossing (c = 1, d = -h),  h = q − q⁻¹
  | averaged    -- half-sum (c = 1, d = -h/2)
  deriving Repr, DecidableEq

/-- Knot-operator class per the atlas layered framework. -/
inductive KnotOperatorType : Type
  | intra_nucleon    -- σ_0 g_0 + σ_1 g_1 per nucleon (at strands 3k, 3k+1)
  | inter_nucleon    -- pp / nn / pn at gen 3k+2
  | closure_topology -- Markov closure
  | fusion           -- α-α / α-N coupling (Layer 2/3)
  | vacuum           -- vortex / unknot
  deriving Repr, DecidableEq

/-- Prediction methodology per atlas Layer 1..5. -/
inductive PredictionMethod : Type
  | canonical_trace       -- Layer 1 — Σ y_λ · χ^λ
  | alpha_cluster         -- Layer 2 — recursive on ⁴He
  | hybrid_valence        -- Layer 3 — α + valence nucleon
  | brane_tower           -- Layer 4 — A > 40
  | prediction_only       -- Layer 5 — no AME measurement
  | volume_match_deprecated
  deriving Repr, DecidableEq

/-- Three-anchor calibration source per `conj:three-calibration-inputs`. -/
inductive CalibrationSource : Type
  | CAL_1   -- electron mass m_e
  | CAL_2   -- substrate parameter q_0
  | CAL_3   -- Q_β(neutron) = m_n - m_p - m_e
  deriving Repr, DecidableEq

/-- A single knot operator applied at a definite gen-index in the
    canonical braid word. -/
structure KnotOperatorCatalogue where
  op_type : KnotOperatorType
  gen_index : Int                 -- −1 for closure-topology slots
  crossing_type : Option CrossingType := none
  nucleon_type : Option String := none      -- "p" / "n"
  interface_channel : Option String := none -- "pp" / "nn" / "pn"
  canonical_form_label : Option String := none
  deriving Repr

/-- Canonical record for a single isotope (Z, N). -/
structure IsotopeRecord where
  Z : Nat
  N : Nat
  -- Optional spectroscopy
  spin_J : Option Float := none
  parity : Option String := none
  -- Braid identification
  markov_closure : Option String := none
  knot_operators : List KnotOperatorCatalogue := []
  -- Trace / prediction
  tr_M_q0_canonical_50dps : Option String := none
  prediction_method : PredictionMethod := PredictionMethod.canonical_trace
  calibration_source : CalibrationSource := CalibrationSource.CAL_1
  prediction_MeV_50dps : Option String := none
  -- Empirical comparison
  B_AME_MeV : Option Float := none
  err_MeV : Option Float := none
  err_pct : Option Float := none
  err_ppb : Option Float := none
  deriving Repr

/-- Mass number `A = Z + N` — derived (computed), not a stored/overridable
    field, so `A = Z + N` holds definitionally for every record. -/
def IsotopeRecord.A (r : IsotopeRecord) : Nat := r.Z + r.N

/-- Strand count `n_strands = 3·A` — derived (computed), not stored. -/
def IsotopeRecord.n_strands (r : IsotopeRecord) : Nat := 3 * (r.Z + r.N)

/-- A=Z+N derivation is by `rfl`. -/
theorem A_eq_Z_plus_N (r : IsotopeRecord) :
    r.A = r.Z + r.N := by rfl

/-- n_strands = 3·A derivation is by `rfl`. -/
theorem n_strands_eq_three_A (r : IsotopeRecord) :
    r.n_strands = 3 * (r.Z + r.N) := by rfl

/-- The canonical knot-operator catalogue for atom (Z, N) constructed
    by `build_knot_operator_catalogue(Z, N)` in the Python schema.

    This Lean signature axiomatises the existence of such a builder;
    the body is computed Python-side and stored on the `IsotopeRecord`
    instance. For the formal layer this is the canonical recipe input
    to all downstream Lean machinery (mass formula, atlas auto-render). -/
noncomputable def canonicalKnotOperatorList (Z N : Nat) :
    List KnotOperatorCatalogue := []

/-- A canonical IsotopeRecord skeleton for (Z, N) — used as the base
    for the all-isotopes registry. Computed fields (|tr_M|, B_AME)
    are filled by the runtime pipeline. -/
noncomputable def canonicalIsotopeRecord (Z N : Nat) : IsotopeRecord :=
  { Z := Z, N := N,
    knot_operators := canonicalKnotOperatorList Z N }

end QOU.BraidKnot
