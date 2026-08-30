/-!
# Fusion process — strand-balanced rearrangement, with the D + T → ⁴He + n
# instance machine-checked

A *fusion process* is a rearrangement of nuclear subjects that conserves the
strand count (3 per nucleon), the proton number and the baryon number on the
subject side. It is a **process in the strong sector**, not a fourth
interaction: no bar-odd (weak) conversion occurs, and the energy release is a
difference of bar-even bindings.

This file proves, kernel-checked and sorry-free:

1. the D + T → ⁴He + n process is strand-, charge- and baryon-balanced;
2. β-decay (n → p) is NOT a rearrangement in this sense (charge moves), which
   is exactly what routes it to the weak (bar-odd) sector;
3. the Littlewood–Richardson **support-contraction** result of
   `computations/probes/fusion_process_lr_support_probe.py`: inducing the
   four subjects' SDP active sets (from the committed
   `nucleus-real-sdp-*.witness.json`, 2026-08-30) into the common frame
   `H_15`, the final support is strictly contained in the initial support.

The LR positivity used here is the standard skew-tableau ballot rule,
implemented executably (`lrPos`): a filling of ν/λ with content μ, rows
weakly increasing, columns strictly increasing, reverse reading word a
ballot sequence. The counts proved below (|S_init| = 79, |S_fin| = 23 of
the 176 partitions of 15) independently reproduce the Python probe's
figures, so the two implementations cross-validate.

Ref: docs/audits/2026-08-29-mass-provenance-breakdown-and-gap-map.md §4b.
-/

namespace QOU.Interactions.FusionProcessBlock

/-- A nuclear subject: `Z` protons, `N` neutrons. -/
structure Subject where
  Z : Nat
  N : Nat
deriving DecidableEq, Repr

/-- Nucleon count `A = Z + N`. -/
def Subject.nucleons (s : Subject) : Nat := s.Z + s.N

/-- Hecke strand count: three strands per nucleon (`H_{3A}`). -/
def Subject.strands (s : Subject) : Nat := 3 * s.nucleons

/-- A nuclear process: initial and final lists of subjects. -/
structure Process where
  initial : List Subject
  final : List Subject

def sumBy (f : Subject → Nat) (l : List Subject) : Nat :=
  (l.map f).foldr (· + ·) 0

/-- Strand conservation: the two sides live in the same total Hecke frame. -/
abbrev Process.strandBalanced (p : Process) : Prop :=
  sumBy Subject.strands p.initial = sumBy Subject.strands p.final

/-- Proton-number conservation on the subject side. -/
abbrev Process.chargeBalanced (p : Process) : Prop :=
  sumBy Subject.Z p.initial = sumBy Subject.Z p.final

/-- Baryon-number conservation. -/
abbrev Process.baryonBalanced (p : Process) : Prop :=
  sumBy Subject.nucleons p.initial = sumBy Subject.nucleons p.final

/-- A **fusion/rearrangement process** (strong sector): all three balances
hold. A process failing `chargeBalanced` while conserving baryon number is a
weak-sector conversion, not a rearrangement. -/
abbrev Process.isRearrangement (p : Process) : Prop :=
  p.strandBalanced ∧ p.chargeBalanced ∧ p.baryonBalanced

def deuteron : Subject := ⟨1, 1⟩
def tritium  : Subject := ⟨1, 2⟩
def helium4  : Subject := ⟨2, 2⟩
def neutron  : Subject := ⟨0, 1⟩
def proton   : Subject := ⟨1, 0⟩

/-- The D + T → ⁴He + n fusion process. -/
def dtFusion : Process := ⟨[deuteron, tritium], [helium4, neutron]⟩

/-- β-decay of the free neutron, subject side only (the lepton pair is not a
nuclear subject). -/
def betaDecay : Process := ⟨[neutron], [proton]⟩

theorem dtFusion_isRearrangement : dtFusion.isRearrangement := by decide

/-- The two sides of D + T → ⁴He + n share the frame `H_15`. -/
theorem dtFusion_strands_fifteen :
    sumBy Subject.strands dtFusion.initial = 15 ∧
    sumBy Subject.strands dtFusion.final = 15 := by decide

/-- β-decay is not a rearrangement: proton number moves. This is the
subject-side discriminator that routes it to the weak (bar-odd) sector. -/
theorem betaDecay_not_rearrangement : ¬ betaDecay.isRearrangement := by decide

/-! ## Littlewood–Richardson support -/

/-- A partition, as a weakly decreasing list of positive naturals. -/
abbrev Partition := List Nat

def weight (p : Partition) : Nat := p.foldr (· + ·) 0

/-- `part n maxPart`: all partitions of `n` with parts ≤ `maxPart`,
first-part-descending. Fuel = `n` suffices (each chosen part ≥ 1). -/
def partAux : Nat → Nat → Nat → List Partition
  | 0, n, _ => if n == 0 then [[]] else []
  | _ + 1, 0, _ => [[]]
  | fuel + 1, n + 1, maxPart =>
    (List.range maxPart).foldr (fun p0 acc =>
      let p := p0 + 1
      if p ≤ n + 1 then
        (partAux fuel (n + 1 - p) p).map (p :: ·) ++ acc
      else acc) []

def partitionsOf (n : Nat) : List Partition := partAux n n n

def getD (l : List Nat) (i d : Nat) : Nat := (l[i]?).getD d

/-- λ ⊆ ν as Young diagrams (pointwise with zero padding). -/
def subShape (lam nu : Partition) : Bool :=
  decide (lam.length ≤ nu.length) &&
  (List.range nu.length).all fun i => decide (getD lam i 0 ≤ getD nu i 0)

/-- Increment index `e-1` of the counts vector. -/
def bump (counts : List Nat) (e : Nat) : List Nat :=
  counts.mapIdx fun i c => if i + 1 == e then c + 1 else c

/-- Fill one skew row right-to-left (columns `lo + k - 1` down to `lo`).
`acc` accumulates the row **left-to-right** (each placement is one column
further left and is prepended). `next` receives the finished row and updated
counts. Constraints per placement, in reverse-reading-word order: entry
capacity (`counts e < μ e`), incremental ballot (`counts e < counts (e-1)`),
weak increase along the row (`e ≤ rightBound`), strict increase down the
column (`e > entry above`, when the cell above lies in the skew shape). -/
def fillRow (m : Nat) (mu : List Nat) (prevLo : Nat) (prevRow : List Nat)
    (lo : Nat) :
    Nat → List Nat → Nat → List Nat → (List Nat → List Nat → Bool) → Bool
  | 0, counts, _, acc, next => next acc counts
  | k + 1, counts, rightBound, acc, next =>
    let col := lo + k
    let above : Option Nat :=
      if col ≥ prevLo ∧ col < prevLo + prevRow.length then
        some (getD prevRow (col - prevLo) 0)
      else none
    (List.range m).any fun e0 =>
      let e := e0 + 1
      decide (e ≤ rightBound) &&
      decide (getD counts (e - 1) 0 < getD mu (e - 1) 0) &&
      (decide (e == 1) || decide (getD counts (e - 1) 0 < getD counts (e - 2) 0)) &&
      (match above with | none => true | some a => decide (a < e)) &&
      fillRow m mu prevLo prevRow lo k (bump counts e) e (e :: acc) next

/-- Search all rows (paired `(λ_i, ν_i)`, top to bottom). Fuel is the row
list itself (structural). -/
def searchRows (m : Nat) (mu : List Nat) :
    List (Nat × Nat) → Nat → List Nat → List Nat → Bool
  | [], _, _, counts => counts == mu
  | (l, n) :: rest, prevLo, prevRow, counts =>
    fillRow m mu prevLo prevRow l (n - l) counts m []
      (fun row counts' => searchRows m mu rest l row counts')

/-- LR positivity `c^ν_{λμ} > 0`, by skew ballot-tableau search. -/
def lrPos (lam mu nu : Partition) : Bool :=
  weight lam + weight mu == weight nu &&
  subShape lam nu &&
  searchRows mu.length mu
    ((List.range nu.length).map fun i => (getD lam i 0, getD nu i 0))
    0 [] (mu.map fun _ => 0)

/-! ### The measured process instance

Active sets from the committed LP-dual witnesses
(`nucleus-real-sdp-{deuteron,tritium,he4,neutron}.witness.json`,
`positive_norm_subspace_solve.active_blocks`, read 2026-08-30 AFTER the
deuteron staleness adjudication of the same day — the deuteron witness was
regenerated from the live trace (tr_M 0.38836 → 0.57517), collapsing its
active set from seven blocks to three; the containment below survives the
re-measurement, at |S_init| = 47 (was 79 against the stale set): -/

def act2H : List Partition := [[4, 2], [5, 1], [6]]
def act3H : List Partition := [[6, 3], [7, 2], [8, 1], [9]]
def act4He : List Partition :=
  [[6, 6], [7, 5], [8, 4], [9, 3], [10, 2], [11, 1]]
def actN : List Partition := [[3]]

def pairsInit : List (Partition × Partition) :=
  act2H.foldr (fun l acc => act3H.map (fun m => (l, m)) ++ acc) []
def pairsFin : List (Partition × Partition) :=
  act4He.foldr (fun l acc => actN.map (fun m => (l, m)) ++ acc) []

def inSupport (pairs : List (Partition × Partition)) (nu : Partition) : Bool :=
  pairs.any fun lm => lrPos lm.1 lm.2 nu

def sInit : List Partition := (partitionsOf 15).filter (inSupport pairsInit)
def sFin : List Partition := (partitionsOf 15).filter (inSupport pairsFin)

/-- **Support contraction.** Every `H_15` Wedderburn block reachable by LR
induction from the final state's active sets (⁴He × n) is already reachable
from the initial state's (²H × ³H): `S_fin ⊆ S_init`. Machine-checked over
all 176 partitions of 15. -/
theorem support_contraction : sFin.all (fun nu => sInit.contains nu) = true := by
  decide

/-- The containment is strict: the sizes are 23 and 47, independently
reproducing `fusion_process_lr_support_probe.py`. -/
theorem support_sizes : sFin.length = 23 ∧ sInit.length = 47 := by decide

theorem support_strict : sFin.length < sInit.length := by decide

end QOU.Interactions.FusionProcessBlock
