/-!
# Interaction-sector taxonomy

The framework's three interaction sectors, with their corpus
identifications: the bar-involution parity channel each sector's primary
observable lives in, the calibration it anchors to, and its coupling
object. *Processes* (fusion, capture, decay) are not sectors: a fusion
process is a strand-balanced rearrangement inside the strong sector
(`fusion-process.lean`), while β-decay moves proton number and is thereby
routed to the weak sector.

Bar parity is recorded only where the corpus establishes it: binding /
volume observables are bar-even (cosh channel) and Q_β / decay widths are
bar-odd (sinh channel) per `conj:binding-qbeta-complex-volume`; no
bar-parity assignment for the electromagnetic sector's primary observable
is established in the corpus, and none is invented here.

Sorry-free; the theorems are kernel-checked finite facts about the
taxonomy (weak is the unique bar-odd-assigned sector; sector data is
total; the three sectors are pairwise distinct).
-/

namespace QOU.Interactions.SectorTaxonomy

/-- Bar-involution (`q ↦ q⁻¹`) parity channel. -/
inductive BarParity where
  | even  -- cosh channel: binding / volume / retained energy
  | odd   -- sinh channel: Q_β / Chern–Simons / emitted energy
deriving DecidableEq, Repr

/-- The three interaction sectors of the framework. -/
inductive Sector where
  | strong
  | electromagnetic
  | weak
deriving DecidableEq, Repr

/-- The calibration each sector's scale anchors to (CAL index 1–3):
strong binding is priced in `E₀ = m_e/(q₀(q₀−1))` off CAL-1/CAL-2; the
electromagnetic Hartree scale is `α_EM²·m_e c²` off CAL-1 with the derived
`α_EM`; the weak sector is CAL-2 itself (`𝔇_β`, proxy `m_μ/m_e`). -/
def calAnchor : Sector → Nat
  | .strong => 2
  | .electromagnetic => 1
  | .weak => 2

/-- Bar parity of the sector's primary observable, where a PURE channel
exists (strong: binding, bar-even; weak: Q_β, bar-odd). For the
electromagnetic sector `none` is itself a theorem-backed verdict: the EM
coupling is provably neither bar-even nor bar-odd under nondegeneracy
(`QOU.Interactions.EmCouplingBarParity.emCouplingBare_not_bar_even/odd`) —
the sector admits no pure-parity assignment. -/
def parity : Sector → Option BarParity
  | .strong => some .even
  | .electromagnetic => none
  | .weak => some .odd

/-- The coupling object each sector reads its strength from, named by the
corpus construction (documentation-level: the strings name the canonical
compute/Lean carriers). -/
def couplingObject : Sector → String
  | .strong => "Borromean Markov trace tr_M(β_Bor) / confinement SDP duals"
  | .electromagnetic => "α_EM⁻¹ = q₀·[9]_q·[10]_q × CS tower (pyhecke.alpha_em_inv_mp)"
  | .weak => "bar-odd channel: Q_β Kashiwara b², decay widths 𝔇_β"

/-- Weak is the unique sector whose established parity is bar-odd. -/
theorem weak_unique_bar_odd :
    ∀ s : Sector, parity s = some .odd ↔ s = .weak := by
    intro s; cases s <;> decide

/-- Strong is the unique sector whose established parity is bar-even. -/
theorem strong_unique_bar_even :
    ∀ s : Sector, parity s = some .even ↔ s = .strong := by
    intro s; cases s <;> decide

/-- The electromagnetic sector is exactly the one with no pure bar-parity
assignment (and provably cannot have one — see the library module
`QOU.Interactions.EmCouplingBarParity`). -/
theorem em_no_pure_parity :
    ∀ s : Sector, parity s = none ↔ s = .electromagnetic := by
    intro s; cases s <;> decide

/-- The three sectors are pairwise distinct. -/
theorem sectors_distinct :
    Sector.strong ≠ Sector.electromagnetic ∧
    Sector.electromagnetic ≠ Sector.weak ∧
    Sector.strong ≠ Sector.weak := by decide

end QOU.Interactions.SectorTaxonomy
