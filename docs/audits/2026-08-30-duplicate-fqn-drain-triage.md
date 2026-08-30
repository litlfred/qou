# Draining the 26 duplicate-FQN collisions — per-pair triage

Measured 2026-08-30 on `main`. Companion to
[`scripts/lean-duplicate-fqn-audit.py`](../../scripts/lean-duplicate-fqn-audit.py)
and [`lean-duplicate-fqn-baseline.json`](lean-duplicate-fqn-baseline.json)
(PR #6191). Bean `qou-kfcl`.

## What holds the 26 apart today

**None of them is held apart by design.** `QOU.lean`, the root aggregator, has
1306 imports and reaches **1290 of the 2389 modules under `QOU/`** — so
**1099 modules (46 %) are not in the root build at all**.

Checked against the baseline: of the 26 confirmed pairs, **0 have both modules
reachable from `QOU.lean`**, 19 have exactly one, and 7 have neither. That is
the consistency test the whole story has to pass — if any pair had both sides
in the root build, `lean QOU.lean` could not exit 0, and it does. The worked
case is `QOU.Mathlib.addCell`: `YoungDiagramAddable` **is** imported by
`QOU.lean`, `YoungDiagramAddCell` is **not**. Add the missing import and the
root build breaks.

So the root build's silence about a collision is the aggregator's *omission*,
not evidence of separation. Two separate things follow, and they should not be
conflated:

- **`lean QOU.lean` exit 0 verifies 1290 modules, not 2389.** It is not a
  corpus-wide gate and must not be quoted as one.
- The corpus-wide sweep that *is* one is
  [`scripts/lean_cone_triage.py`](../../scripts/lean_cone_triage.py) over every
  module. Run 2026-08-30 after PR #6140 it reported 2128 up-to-date, 210 ok,
  **0 blocked**. That is the measurement behind "180 → 0", and it stands.

## How to drain

Per-name importer counts are direct importers under `QOU/`; they exclude
`QOU.lean` itself, which is counted separately above.

| verdict | names | what to do |
|---|---|---|
| one side has **zero** importers | 11 | rename the dead side; nothing to update |
| **both** sides have zero importers | 10 | both modules are unconsumed; rename either |
| both sides consumed | **3** | real judgement: `QOU.BraidKnot.writhe` (1/1), `QOU.Mathlib.addCell` (2/1), `QOU.Mathlib.IsAddableCell` (2/1) |

So 21 of 24 names are mechanical and 3 need a decision about which definition
is canonical. `addCell` / `IsAddableCell` are one decision, not two — same
module pair.

**A zero-importer module is not thereby dead code.** It means nothing under
`QOU/` imports it directly; a content-block `.lean` sibling or a downstream
paper may still resolve declarations from it. Check before deleting anything —
this triage recommends renaming, not deletion, for exactly that reason.

---

## `QOU.Archimedean.BraidWord` — bodies DIFFER

- `QOU.Archimedean.HeckeRep` — 10 importer(s)
  ```lean
  abbrev BraidWord (n : ℕ) := List (Fin (n - 1) × Bool)
  ```
- `QOU.Archimedean.NuclearGroebnerReduction` — 0 importer(s)
  ```lean
  abbrev BraidWord := List ℕ
  ```

## `QOU.Archimedean.T_nn` — bodies DIFFER

- `QOU.Archimedean.TransferMatrix` — 10 importer(s)
  ```lean
  noncomputable def T_nn : TMatrix :=
    transferMatrix 1 (-HA_t)
  ```
- `QOU.Archimedean.beta_decay_transfer_matrix` — 0 importer(s)
  ```lean
  noncomputable def T_nn (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
    betaTransfer q 1 (-(q - q⁻¹))
  ```

## `QOU.Archimedean.T_pp` — bodies DIFFER

- `QOU.Archimedean.TransferMatrix` — 10 importer(s)
  ```lean
  noncomputable def T_pp : TMatrix := transferMatrix 1 0
  ```
- `QOU.Archimedean.beta_decay_transfer_matrix` — 0 importer(s)
  ```lean
  noncomputable def T_pp (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ := betaTransfer q 1 0
  ```

## `QOU.BraidKnot.heckeH` — bodies DIFFER

- `QOU.BraidKnot.HoefsmitV21CosSymmetrization` — 1 importer(s)
  ```lean
  noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹
  ```
- `QOU.BraidKnot.chirality_frobenius_self_pairing` — 0 importer(s)
  ```lean
  def heckeH (q : Rˣ) : R := (q : R) - ((q⁻¹ : Rˣ) : R)
  ```

## `QOU.BraidKnot.qFact` — bodies DIFFER

- `QOU.BraidKnot.H3HeckeIdempotents` — 1 importer(s)
  ```lean
  noncomputable def qFact [DecidableEq R] (q : R) : ℕ → R
    | 0 => 1
    | (k+1) => qInt q (k+1) * qFact q k
  ```
- `QOU.BraidKnot.QBetaWenzlDecomposition` — 0 importer(s)
  ```lean
  noncomputable def qFact (n : ℕ) (q : ℝ) : ℝ :=
    if n = 0 then 1
    else (List.range n).foldl (fun acc i => acc * qInteger (i + 1) q) 1
  ```

## `QOU.BraidKnot.qInt` — bodies DIFFER

- `QOU.BraidKnot.ZeqNRhoCorrection` — 0 importer(s)
  ```lean
  noncomputable abbrev qInt (q : ℝ) (n : ℕ) : ℝ :=
    QOU.QInteger.qIntBalCl q n
  ```
- `QOU.BraidKnot.wedderburn_trace_identity` — 3 importer(s)
  ```lean
  abbrev qInt {R : Type*} [Field R] (q : R) (k : ℕ) : R :=
    QOU.QInteger.qIntGeo q k
  ```

## `QOU.BraidKnot.writhe` — bodies DIFFER

- `QOU.BraidKnot.AlphaShiftOneDimChannel` — 1 importer(s)
  ```lean
  def writhe : Word → Int
    | [] => 0
    | g :: rest => (if 0 < g then (1 : Int) else -1) + writhe rest
  ```
- `QOU.BraidKnot.DeltaLambdaExponentKeystone` — 1 importer(s)
  ```lean
  def writhe (Z N : Nat) : Nat := protonCrossings Z N - neutronCrossings Z N
  ```

## `QOU.BraidsAndKnots.chi21_borromean` — bodies DIFFER

- `QOU.BraidsAndKnots.BorromeanChiPerRep` — 1 importer(s)
  ```lean
  def chi21_borromean (h : R) : R := 2 - 3 * h^4 - h^6
  ```
- `QOU.BraidsAndKnots.BorromeanFrobeniusReconstruction` — 0 importer(s)
  ```lean
  def chi21_borromean (h : ℚ) : ℚ := 2 - 3 * h ^ 4 - h ^ 6
  ```

## `QOU.BraidsAndKnots.qFactorial` — bodies DIFFER

- `QOU.BraidsAndKnots.QSchurYLambdaClosedForm` — 0 importer(s)
  ```lean
  noncomputable def qFactorial : ℕ → ℝ → ℝ
    | 0, _ => 1
    | (n + 1), q => qBracket (n + 1) q * qFactorial n q
  ```
- `QOU.BraidsAndKnots.YLambdaQSchur` — 1 importer(s)
  ```lean
  noncomputable def qFactorial {R : Type*} [Field R] (q : R) : ℕ → R
    | 0 => 1
    | n + 1 => qInt q (n + 1) * qFactorial q n
  ```

## `QOU.BringsSurface.eulerChar` — bodies DIFFER

- `QOU.BringsSurface` — 0 importer(s)
  ```lean
  def eulerChar : ℤ := -6
  ```
- `QOU.BringsSurface.EulerCharacteristicSix` — 0 importer(s)
  ```lean
  def eulerChar (g : ℕ) : ℤ := 2 - 2 * (g : ℤ)
  ```

## `QOU.HyperellipticQuintic.HyperellipticQuintic` — IDENTICAL bodies

- `QOU.HyperellipticQuintic.ScratchZeta5` — 0 importer(s)
  ```lean
  def HyperellipticQuintic (p : ℂ × ℂ) : Prop :=
    p.2 ^ 2 = p.1 ^ 5 - 1
  ```
- `QOU.HyperellipticQuintic.zeta5_residue_monodromy` — 0 importer(s)
  ```lean
  def HyperellipticQuintic (p : ℂ × ℂ) : Prop :=
    p.2 ^ 2 = p.1 ^ 5 - 1
  ```

## `QOU.HyperellipticQuintic.gauss_sum_5` — IDENTICAL bodies

- `QOU.HyperellipticQuintic.ScratchZeta5` — 0 importer(s)
  ```lean
  noncomputable def gauss_sum_5 : ℂ :=
    zeta5^0 + zeta5^1 + zeta5^4 + zeta5^9 + zeta5^16
  ```
- `QOU.HyperellipticQuintic.zeta5_residue_monodromy` — 0 importer(s)
  ```lean
  noncomputable def gauss_sum_5 : ℂ :=
    zeta5^0 + zeta5^1 + zeta5^4 + zeta5^9 + zeta5^16
  ```

## `QOU.HyperellipticQuintic.zeta5` — IDENTICAL bodies

- `QOU.HyperellipticQuintic.ScratchZeta5` — 0 importer(s)
  ```lean
  noncomputable def zeta5 : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)
  ```
- `QOU.HyperellipticQuintic.zeta5_residue_monodromy` — 0 importer(s)
  ```lean
  noncomputable def zeta5 : ℂ := Complex.exp (2 * Real.pi * Complex.I / 5)
  ```

## `QOU.MassTheory.MagnitudeCloses` — bodies DIFFER

- `QOU.MassTheory.BorromeanMagnitudeLift` — 0 importer(s)
  ```lean
  def MagnitudeCloses (E0 h κ μ₃ : ℝ) : Prop := levelMagnitude E0 h κ = μ₃
  ```
- `QOU.MassTheory.BraneTowerLevelAmplitude` — 0 importer(s)
  ```lean
  def MagnitudeCloses (E0 h κFull μ₃ : ℝ) : Prop := levelMagnitude E0 h κFull = μ₃
  ```

## `QOU.MassTheory.heckeH` — IDENTICAL bodies

- `QOU.MassTheory.AveragedLetterSpectrum` — 1 importer(s)
  ```lean
  noncomputable def heckeH (q : K) : K := q - q⁻¹
  ```
- `QOU.MassTheory.PnInterfaceBarStructure` — 0 importer(s)
  ```lean
  noncomputable def heckeH (q : K) : K := q - q⁻¹
  ```

## `QOU.MassTheory.levelMagnitude` — bodies DIFFER

- `QOU.MassTheory.BorromeanMagnitudeLift` — 0 importer(s)
  ```lean
  noncomputable def levelMagnitude (E0 h κ : ℝ) : ℝ := E0 * (h ^ 4 * κ)
  ```
- `QOU.MassTheory.BraneTowerLevelAmplitude` — 0 importer(s)
  ```lean
  def levelMagnitude {R : Type*} [CommRing R] (E0 h κ : R) : R := E0 * (h ^ 4 * κ)
  ```

## `QOU.Mathlib.IsAddableCell` — bodies DIFFER

- `QOU.Mathlib.YoungDiagramAddCell` — 2 importer(s)
  ```lean
  def IsAddableCell (μ : YoungDiagram) (s : ℕ × ℕ) : Prop :=
    s ∉ μ ∧ (s.1 = 0 ∨ (s.1 - 1, s.2) ∈ μ) ∧ (s.2 = 0 ∨ (s.1, s.2 - 1) ∈ μ)
  ```
- `QOU.Mathlib.YoungDiagramAddable` — 1 importer(s)
  ```lean
  def IsAddableCell (μ : YoungDiagram) (c : ℕ × ℕ) : Prop :=
    c ∉ μ ∧ (c.1 = 0 ∨ (c.1 - 1, c.2) ∈ μ) ∧ (c.2 = 0 ∨ (c.1, c.2 - 1) ∈ μ)
  ```

## `QOU.Mathlib.addCell` — bodies DIFFER

- `QOU.Mathlib.YoungDiagramAddCell` — 2 importer(s)
  ```lean
  def addCell (μ : YoungDiagram) (s : ℕ × ℕ) (hs : IsAddableCell μ s) : YoungDiagram where
    cells := insert s μ.cells
    isLowerSet := by
      obtain ⟨hs0, hs1, hs2⟩ := hs
      intro a b hba ha
      simp only [Finset.coe_insert, Set.mem_insert_iff] at ha ⊢
  ```
- `QOU.Mathlib.YoungDiagramAddable` — 1 importer(s)
  ```lean
  def addCell (μ : YoungDiagram) (c : ℕ × ℕ) (hc : IsAddableCell μ c) : YoungDiagram where
    cells := insert c μ.cells
    isLowerSet := by
      obtain ⟨-, hup, hleft⟩ := hc
      intro a b hba ha
      simp only [Finset.coe_insert, Set.mem_insert_iff, Finset.mem_coe] at ha ⊢
  ```

## `QOU.QBeta.zC` — bodies DIFFER

- `QOU.QBeta.DecayLadderConventionDPositivity` — 0 importer(s)
  ```lean
  noncomputable def zC (q : ℝ) : ℝ := Real.sqrt q / (1 + q)
  ```
- `QOU.QBeta.LadderPhaseMirrorCovariance` — 1 importer(s)
  ```lean
  noncomputable def zC (s : F) : F := s / (1 + s ^ 2)
  ```

## `QOU.QBeta.zD` — bodies DIFFER

- `QOU.QBeta.DecayLadderConventionDPositivity` — 0 importer(s)
  ```lean
  noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)
  ```
- `QOU.QBeta.LadderParityReflection` — 0 importer(s)
  ```lean
  noncomputable def zD (q : ℂ) : ℂ := q ^ 3 / (q ^ 2 + 1)
  ```
- `QOU.QBeta.LadderPhaseMirrorCovariance` — 1 importer(s)
  ```lean
  noncomputable def zD (q : F) : F := q ^ 3 / (q ^ 2 + 1)
  ```

## `QOU.Substrate.ProtonMassSubstrateIdentity.m_e_codata` — IDENTICAL bodies

- `QOU.Substrate.ProtonMassSubstrateIdentity` — 0 importer(s)
  ```lean
  def m_e_codata : ℝ := 0.51099895069
  ```
- `QOU.scratch_pmass` — 0 importer(s)
  ```lean
  def m_e_codata : ℝ := 0.51099895069
  ```

## `QOU.Substrate.ProtonMassSubstrateIdentity.m_mu_codata` — IDENTICAL bodies

- `QOU.Substrate.ProtonMassSubstrateIdentity` — 0 importer(s)
  ```lean
  def m_mu_codata : ℝ := 105.6583755
  ```
- `QOU.scratch_pmass` — 0 importer(s)
  ```lean
  def m_mu_codata : ℝ := 105.6583755
  ```

## `QOU.Substrate.ProtonMassSubstrateIdentity.m_p_codata` — IDENTICAL bodies

- `QOU.Substrate.ProtonMassSubstrateIdentity` — 0 importer(s)
  ```lean
  def m_p_codata : ℝ := 938.27208943
  ```
- `QOU.scratch_pmass` — 0 importer(s)
  ```lean
  def m_p_codata : ℝ := 938.27208943
  ```

## `QOU.Substrate.ProtonMassSubstrateIdentity.m_p_predicted` — IDENTICAL bodies

- `QOU.Substrate.ProtonMassSubstrateIdentity` — 0 importer(s)
  ```lean
  def m_p_predicted (q_0 : ℝ) : ℝ :=
    2 * m_mu_codata * F_Bor q_0 - 12 * m_e_codata
  ```
- `QOU.scratch_pmass` — 0 importer(s)
  ```lean
  def m_p_predicted (q_0 : ℝ) : ℝ :=
    2 * m_mu_codata * F_Bor q_0 - 12 * m_e_codata
  ```

---

identical-body names (delete one, import the other): 8
differing-body names (rename; decide which is canonical): 16
