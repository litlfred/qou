# Which reading of trace → mass makes the neutron heavier? (2026-11-21)

Thread "Settle the neutron-heavier sign", bean `qou-99qc`. Sign left open by owner ruling D2
(2026-11-20; np-splitting audit §23). Lean: `QOU/QBeta/NeutronHeavierSign.lean`. Probe:
`computations/probes/np_splitting/np_sign_readings_probe.py`, pre-registered in
`np_sign_readings_preregistration.md` (commit `b49b8067a`, before the run).

Framework used (owner rulings on main 845e2f820): photon γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹;
nucleon V³ = (σ₀σ₁⁻¹)³ = γ(0,0,qh)·γ(0,0,−q⁻¹h); electron σ₀σ₁σ₀ ∈ B₃ (Hopf closure); up quark
an unknot strand, u = e₁; two-term Lagrangian trace with the quantum trace Tr(K^{⊗3}·)/[2]³.

## 1. Result

**No corpus reading derives m_n > m_p.** The reason is one invariant. For every element X of the
braid-group algebra, the plain traces on the proton weight space W_p = (2,1) and the neutron
weight space W_n = (1,2) are equal (the intertwiner P(q)). The flavour content is then only the
Cartan weight: ε_p = q·t/[2]³ and ε_n = q⁻¹·t/[2]³ with one common t. So ε_n = q⁻²·ε_p, and
above the wall (q > 1) |ε_n| < |ε_p| for every X with t ≠ 0.

| reading (corpus source) | m_n > m_p? | Lean |
|---|---|---|
| R1 signed linear m ∝ ε | iff t < 0. On V³ t > 0, so no | `signed_reading_iff`, `V3_signed_reading_neutron_lighter` |
| R2 any increasing f of the absolute sector trace (production m_p identity uses \|tr_M\|; Q_β uses \|ε\|) | **never** | `increasing_reading_neutron_lighter`, `word_…`, `V3_…` |
| R3 any decreasing f ("more negative Φ is more confinement", old n–p proof block) | always | `antitone_reading_neutron_heavier` |
| R4 bar side 0 < q < 1 | reverses R2 | `bar_side_reverses` |
| R5 one flip only: K ↦ K⁻¹, or u = e₂ | swaps p and n | `single_flip_swaps` |
| R6 both flips (Cartan involution) | same as R2 | `cartan_involution_invariant` |
| R7 two-term static charge term c·Q_pair or c·Q_self | flips only if c < −3(q − q⁻¹) | `twoTerm_flip_iff`, `twoTerm_neutron_lighter` |
| R8 electron as a spectator factor (its trace q³(q⁴+1)/(q²+1)² > 0) | same as R2 | `spectator_preserves` |
| R9 kinematic m_n − m_p = Q_β + m_e, Q_β = \|ε\|·E₀ | yes, but the same for ε and −ε | `kinematic_reading_sign_blind` |

Every reading that gives a heavier neutron has a named defect:

- **R3** is one sentence in `observations/neutron-proton-mass-splitting-proof.md` and
  `mass-theory/neutron-proton-splitting.md`. It flips the orientation "rather than reduced
  binding, as occurs at the nuclear level". It is applied to Φ, which is not a braid trace
  (§19 of the np-splitting audit), and it is the opposite orientation to the production m_p
  identity, which increases with |tr_M|. Using one orientation for m_p and the other for m_n
  would be two maps, which is a choice.
- **R4** evaluates below the wall. Every corpus anchor is at q₀ ≈ 1.11.
- **R5** each single flip is excluded by a proved theorem: K⁻¹ is not a Markov trace
  (`OverStrandWeight.ptr_other_not_scalar`, `MarkovOrientationForced`), and u = e₂ contradicts
  the over/under rule (`OverStrandWeight`, merged #7971).
- **R1 with t < 0**: 114 of 1364 signed words of length ≤ 5 have t < 0 at q = 111/100. The
  ruled element V³ is not one of them. Choosing such a word for the neutron would be selection.
- **R7**: the ruled covariant term (all pairs, connected) is 0 on V³ (`deltaT_allPairs_connected_eq_zero`).
  The static terms push the same way as the Cartan term for c ≥ 0. That is the familiar fact
  that the Coulomb term makes the proton heavier (`MassTheory/NeutronProtonEMSign`). A flip
  needs c < −3h ≈ −0.63 at q₀; no derived c has that sign.
- **R9**: the sign is supplied by |·| and by kinematics, not by the trace.
- Not formalised here: FE inserted alone (np-splitting §22) gives t_n > t_p, but FE versus EF
  is a choice; FE + EF gives q⁻² exactly (`trace_twoTerm_with_secondOrder_eq`).

Independent confirmation, sibling thread "m_n by its own identity": under "the mass is the
nucleon's own T³ component" Lean gives F⁽ⁿ⁾ = q⁻² F⁽ᵖ⁾ (`NeutronOwnIdentity.sector_ratio`), so
m_n − m_p = 2m_μF_Bor(q⁻² − 1) < 0. That is R2 with f linear.

## 2. Scope

- **Structural, scope (b), for R2.** Invariant: equal plain traces on W_p, W_n plus q⁻¹ < q.
  It holds for the whole braid-group algebra, so no choice of word, photon weights or electron
  insertion on the three strands changes it.
- **Scope (a) for the rest.** This file does not exclude a mass map that is not a function of
  the sector trace (for example one that reads more than the flavour weight space), or a
  derivation of R3's orientation. If a derivation of a decreasing map appears, R3 becomes the
  answer, and it would then have to be reconciled with the m_p identity.
- What would change the verdict: an element that acts differently on W_p and W_n (not in the
  braid-group algebra), a derived negative static charge coupling, or a derived reason for the
  sector-decreasing orientation.

## 3. Verification

- Lean: `lean -DautoImplicit=false -s 65536 QOU/QBeta/NeutronHeavierSign.lean` exit 0, no
  warnings, no `sorry`. The four imported modules were rebuilt from this branch's source into a
  private olean directory first (all exit 0). `#print axioms` on the ten headline theorems:
  `propext, Classical.choice, Quot.sound`.
- Probe (sympy over ℚ(q), decisions at q = 111/100 and 100/111, no float): P1 1364/1364,
  P2 1364/1364, P4 1364/1364, P5 1364/1364, P6 1364/1364; V³, Δ₃·V³, the symbolic photon
  product and γ(0,0,qh)γ(0,0,−h/q) all give ε_n/ε_p = q⁻². P3 (reported, not predicted):
  114/1364 words have t < 0.
- Precision gates (`--changed`): the red gates (q0-anchor flip, refill, reference-literal,
  q0-value drift) are tree-wide and name no file of this branch; the audit witnesses they
  rewrote were reverted, not committed.
- Corpus search: paths 1–4 (docs/audits, folio, computations, docs/coordination) for
  "neutron heavier/lighter", "mass ordering", "wrong sign"; read MirrorAsymmetrySign,
  NeutronProtonEMSign, the np-splitting audit §13–§23, FlavourWeightSplit, DecayConjectures,
  NucleonWeightSpaceTwoTerm, OverStrandWeight, PR #8734 (MirrorTraceBar, open). Not run:
  corpus_search step 0, the library tiers and the beans mount. So the verdict is about the
  readings listed here, found in those paths.
