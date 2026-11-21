/-
  Milnor-indeterminacy gate — invariant I3 of
  docs/audits/2026-07-13-alpha-activation-brunnian-derive-or-refute.md.

  Model (honest formalizable core; the Magnus expansion / Milnor invariant
  itself is NOT re-derived here, matching the modeling stance of the sibling
  `MilnorSignRepObstruction.lean`):

    * A 3-component sub-link of a cluster arrangement is carried abstractly
      as its three pairwise linking numbers `(l12, l13, l23 : ℤ)`
      (`ClusterTriple`).
    * By Milnor's well-definedness theorem, the triple invariant μ̄(ijs) is
      well-defined only modulo Δ(ijs) = gcd of the pairwise linking numbers
      of the three components (μ̄ of the proper sub-links).  That literature
      input is carried as the MODELING CHOICE that the residue of μ̄ lives in
      `ZMod (indeterminacy l12 l13 l23)` — it is the type of the invariant,
      not a Lean axiom.  What IS proved here is the pure number theory the
      audit's gate rests on:

      (a) `gate_kills_hopf_spectator` — if any pair of the triple is
          Hopf-linked (|lk| = 1, the always-on light-spectator channel), the
          gcd is 1 and `ZMod 1` is a subsingleton: the residue class of
          μ̄(ijs) carries NO invariant content.  Audit-shaped corollary:
          `ClusterTriple.residue_trivial_of_hopfSpectator`.

      (b) `gate_open_iff_brunnian` — the gcd vanishes iff ALL pairwise
          linkings vanish (the Brunnian/Borromean pattern); then the residue
          space is `ZMod 0 = ℤ` (`residue_eq_int_of_brunnian`) and integer
          casts stay distinct (`intCast_injective_of_brunnian`): full
          ℤ-valued μ̄ content.  This is the α-only gate: only a
          pairwise-unlinked third α can activate an α·α triple channel.

  Everything is stated over ℤ / ℕ / `ZMod` — linking numbers ARE integers,
  so no gratuitous ℝ appears (AGENTS.md §7c); `decide`-free, sorry-free.

  -- Ref: [leitner2026] docs/audits/2026-07-13-alpha-activation-brunnian-derive-or-refute.md §I3
  -- Ref: [milnor1954] https://doi.org/10.2307/1969685  (Milnor, "Link groups",
  --      Ann. of Math. 59 (1954): μ̄ is defined modulo the gcd of the
  --      lower-order linking invariants of the sub-links)
-/

import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

namespace QOU.Mass.MilnorIndeterminacyGate

/-! ### The Milnor indeterminacy Δ(ijs) -/

/-- The Milnor indeterminacy `Δ(ijs)` of a 3-component sub-link with pairwise
    linking numbers `l12, l13, l23`: the gcd of the three pairwise linking
    numbers.  Milnor 1954: μ̄(ijs) is a well-defined residue only modulo this
    gcd (the lower-order invariants of the proper sub-links of a 3-component
    link are exactly the pairwise linking numbers).  Computed on `ℤ.natAbs`
    since the gcd of integers is a natural number and `ZMod` is indexed by
    `ℕ`; this agrees with `Int.gcd`. -/
def indeterminacy (l12 l13 l23 : ℤ) : ℕ :=
  Nat.gcd l12.natAbs (Nat.gcd l13.natAbs l23.natAbs)

/-- The natAbs-gcd of the definition agrees with the iterated `Int.gcd`. -/
theorem indeterminacy_eq_int_gcd (l12 l13 l23 : ℤ) :
    indeterminacy l12 l13 l23 = l12.gcd ((l13.gcd l23 : ℕ) : ℤ) := by
  simp [indeterminacy, Int.gcd]

/-- If any pair of the triple has `|lk| = 1` (a Hopf-linked pair), the
    indeterminacy is total: `Δ(ijs) = 1`. -/
theorem indeterminacy_eq_one_of_unit_pair {l12 l13 l23 : ℤ}
    (h : l12.natAbs = 1 ∨ l13.natAbs = 1 ∨ l23.natAbs = 1) :
    indeterminacy l12 l13 l23 = 1 := by
  rcases h with h | h | h <;>
    simp [indeterminacy, h, Nat.gcd_one_right, Nat.gcd_comm]

/-! ### (a) The gate closes on a Hopf-linked spectator -/

/-- **Gate kills the Hopf spectator (audit I3(a)).**  If any pair in the
    triple is Hopf-linked (`|lk| = 1` — the always-on light-spectator
    channel), the Milnor residue space `ZMod Δ(ijs) = ZMod 1` is a
    subsingleton: the residue class of μ̄(ijs) is trivial and carries no
    invariant triple content. -/
theorem gate_kills_hopf_spectator {l12 l13 l23 : ℤ}
    (h : l12.natAbs = 1 ∨ l13.natAbs = 1 ∨ l23.natAbs = 1) :
    Subsingleton (ZMod (indeterminacy l12 l13 l23)) := by
  rw [indeterminacy_eq_one_of_unit_pair h]
  infer_instance

/-! ### (b) The gate is open exactly in the Brunnian case -/

/-- **Gate open iff Brunnian (audit I3(b)).**  The indeterminacy vanishes —
    equivalently, the residue space is `ZMod 0 = ℤ`, full integer μ̄
    content — iff ALL pairwise linking numbers vanish: the
    Brunnian/Borromean pattern. -/
theorem gate_open_iff_brunnian {l12 l13 l23 : ℤ} :
    indeterminacy l12 l13 l23 = 0 ↔ l12 = 0 ∧ l13 = 0 ∧ l23 = 0 := by
  simp [indeterminacy, Nat.gcd_eq_zero_iff, Int.natAbs_eq_zero]

/-- In the Brunnian case the residue space IS the integers:
    `ZMod Δ = ZMod 0 = ℤ` (definitional once the gcd is rewritten to 0). -/
theorem residue_eq_int_of_zero_linkings {l12 l13 l23 : ℤ}
    (h12 : l12 = 0) (h13 : l13 = 0) (h23 : l23 = 0) :
    ZMod (indeterminacy l12 l13 l23) = ℤ := by
  rw [gate_open_iff_brunnian.mpr ⟨h12, h13, h23⟩]
  rfl

/-! ### The physical gate: cluster triples -/

/-- A 3-component sub-link of a cluster arrangement, carried abstractly by
    its pairwise linking data `l12 = lk(i,j)`, `l13 = lk(i,s)`,
    `l23 = lk(j,s)`.  Modeling input (Milnor 1954, carried here as the type
    of the residue, not as an axiom): the triple invariant μ̄(ijs) of the
    sub-link is a well-defined element of `ZMod (indeterminacy l12 l13 l23)`
    only — any integer representative is meaningful only through its residue
    class modulo the gcd of the pairwise linkings. -/
structure ClusterTriple where
  /-- Pairwise linking number of components i, j. -/
  l12 : ℤ
  /-- Pairwise linking number of components i, s. -/
  l13 : ℤ
  /-- Pairwise linking number of components j, s. -/
  l23 : ℤ

namespace ClusterTriple

/-- The Milnor indeterminacy of the triple. -/
def indeterminacy (t : ClusterTriple) : ℕ :=
  MilnorIndeterminacyGate.indeterminacy t.l12 t.l13 t.l23

/-- The residue space in which μ̄(ijs) is well-defined (Milnor 1954).
    `abbrev` so that the `ZMod` ring instances are found on it. -/
abbrev Residue (t : ClusterTriple) : Type := ZMod t.indeterminacy

/-- The triple contains a Hopf-linked pair (`|lk| = 1`): the audit's
    light-spectator configuration (n/d/t pairwise Hopf-linked to an α). -/
def HopfSpectator (t : ClusterTriple) : Prop :=
  t.l12.natAbs = 1 ∨ t.l13.natAbs = 1 ∨ t.l23.natAbs = 1

/-- All pairwise linkings vanish: the Brunnian/Borromean pattern
    (a pure-α triple).

    **This is TIER 2 — strictly weaker than true Brunnian-ness** (every proper
    sub-link is the unlink), which it does not imply: the Whitehead link has
    linking number `0` and is not the unlink.  Tier table for the four things this corpus calls `Brunnian`, and which implications hold: `QOU.Mass.BrunnianTierDisambiguation`. -/
def Brunnian (t : ClusterTriple) : Prop :=
  t.l12 = 0 ∧ t.l13 = 0 ∧ t.l23 = 0

/-- **Audit corollary, Hopf side.**  In a cluster arrangement where a light
    spectator is Hopf-linked into the triple, the triple channel is trivial:
    ALL residues of μ̄(ijs) coincide — in particular every two integer
    candidate values of μ̄ become equal in the residue space, so the triple
    invariant distinguishes nothing. -/
theorem residue_trivial_of_hopfSpectator (t : ClusterTriple)
    (h : t.HopfSpectator) (x y : t.Residue) : x = y := by
  haveI : Subsingleton t.Residue := gate_kills_hopf_spectator h
  exact Subsingleton.elim x y

/-- Restatement on integer representatives: with a Hopf-linked pair present,
    any two integer values of μ̄ have the same residue — no invariant triple
    content survives the indeterminacy. -/
theorem intCast_residue_collapse_of_hopfSpectator (t : ClusterTriple)
    (h : t.HopfSpectator) (m n : ℤ) :
    ((m : ℤ) : t.Residue) = ((n : ℤ) : t.Residue) :=
  t.residue_trivial_of_hopfSpectator h _ _

/-- **Audit corollary, Brunnian side.**  For a pure-α triple (all pairwise
    linkings zero) the integer content of μ̄ is fully preserved: the cast
    `ℤ → Residue = ZMod 0` is injective, so distinct integer values of
    μ̄(ijs) stay distinct — the α-only gate is open. -/
theorem intCast_injective_of_brunnian (t : ClusterTriple)
    (h : t.Brunnian) :
    Function.Injective (fun m : ℤ => ((m : ℤ) : t.Residue)) := by
  intro a b hab
  have hz : t.indeterminacy = 0 := gate_open_iff_brunnian.mpr h
  have hmod : a ≡ b [ZMOD t.indeterminacy] :=
    (ZMod.intCast_eq_intCast_iff a b t.indeterminacy).mp hab
  rw [hz] at hmod
  simpa [Int.ModEq] using hmod

/-- The residue space of a Brunnian (pure-α) triple is the integers. -/
theorem residue_eq_int_of_brunnian (t : ClusterTriple) (h : t.Brunnian) :
    t.Residue = ℤ :=
  residue_eq_int_of_zero_linkings h.1 h.2.1 h.2.2

/-- The Brunnian residue space is nontrivial — the exact opposite of the
    Hopf-spectator collapse: the open gate carries information. -/
theorem residue_nontrivial_of_brunnian (t : ClusterTriple)
    (h : t.Brunnian) : Nontrivial t.Residue := by
  refine ⟨((0 : ℤ) : t.Residue), ((1 : ℤ) : t.Residue), fun hc => ?_⟩
  exact zero_ne_one (t.intCast_injective_of_brunnian h hc)

end ClusterTriple

end QOU.Mass.MilnorIndeterminacyGate
