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

## Coloured strands (owner choice 2026-11-21: "Coloured / Yokonuma strands")

Question from the owner: the strands carried no flavour of their own. Above, flavour lives only in
the choice of weight space and the K weight, and the braid acts identically on W_p and W_n. This
section puts flavour on the strands as a colour, in the two-colour Yokonuma–Hecke algebra Y₂,₃.

Prior work: np-splitting audit §12 (2026-11-15) already did this for the half and full twist and
found n − p = 0 at x = 0, where x = 0 is forced (x = ±1 kills a colour sector).
`np_yokonuma_coloured_probe.py` re-run 2026-11-21, reproduces.

New, pre-registered (`np_yokonuma_flip_preregistration.md`, commit 711b82f418), probe
`np_yokonuma_flip_probe.py`, exact over Q(q, z, x, φ's), output in `.out.txt`:

- **Y1.** The colour flip φ: t ↦ −t, g ↦ g is an algebra automorphism: 0 failures in 2304 basis
  products.
- **Y2.** The Juyumaya trace is φ-invariant at x = 0 (0/48 failures), and tr(φb)(x) = tr(b)(−x)
  (0/48).
- **Y3.** At x = 0, n = p for the ruled V³ = (g₁g₂⁻¹)³, both ruled photon factors, their product,
  the generic photon with symbolic φ's, the half twist and the full twist, in all three
  flip-paired placements (21/21). So under coloured strands **no reading of trace → mass orders n and
  p at all**: the neutron is neither heavier nor lighter.
- **Y4.** For symbolic x, tr_n(x) = tr_p(−x) (21/21). n − p = x(x−1)(x+1)/4 for every word except
  the half twist (0). It is word-independent (it is the difference of the bare projector traces),
  odd in x, and zero at all three E-system values. A sign would need a chosen sign of x off the
  E-system; that would be a fit.
- **Unexpected.** In Y₂,₃ the ruled photon factorisation V³ = γ(0,0,qh)·γ(0,0,−q⁻¹h) does
  **not** hold as an element (the probe prints `product == V3 : False`). The reason is that
  g⁻¹ = g − h·e in Yokonuma, against g⁻¹ = g − h in Hecke. The trace values agree here. The identity
  `borromeanV3A_eq_switched_photon_product` is a one-colour (Hecke) fact and does not lift to
  coloured strands unchanged.

Lean (`NeutronHeavierSign.lean`, section Coloured): `flip_sector_eq` (a φ-invariant trace gives the
flipped sector the same value on every φ-fixed element), `coloured_no_order`, `colouredDiff_odd`
and `colouredDiff_eSystem`. Y1 and Y2 enter as hypotheses checked by the probe, not as Lean facts.
Formalising Y₂,₃ itself in Lean is not done.

Verdict, scope (a): coloured strands put flavour on the strands, and the u ↔ d flip is then an
exact symmetry of the algebra and of the forced trace. The neutron-heavier question has no sign to
settle there. A mass ordering needs a u/d asymmetry that is not in Y₂,₃ with x = 0. Candidates are
the knot assignment u = T(2,3), d = mirror (§14), or a charge term. Either would be an added input.

## Options for a u/d asymmetry, and what each does downstream (2026-11-22, owner: "explore options and figure out the implications")

Nothing new was computed for this section. Each row cites the result it rests on. The downstream
objects checked: the ruled Q_β (D1 = A, 2026-11-20: Q_β = |t_n − t_p|·E₀^full = 0.3254 MeV), the
kinematic identity m_n − m_p = Q_β + m_e, the ruled photon and V³ (γγ selection, `qou-ales`), the
b₃ / isospin bond pattern (`qou-q8vl`), and the anti-fit rule.

| option | where u ≠ d enters | n vs p | ruled Q_β | photon / V³ | binding bonds | fit risk |
|---|---|---|---|---|---|---|
| O1 weight space + K (current) | K weight q on W_p, q⁻¹ on W_n | ε_n = q⁻²ε_p | **is** the ruled Q_β | compatible | none (bonds flavour-blind) | none; u = e₁ is derived (§16) |
| O2 coloured strands (Yokonuma, x = 0) | strand colour | n = p exactly | **forces Q_β = 0**, contradicts D1 | V³ = γγ product fails as an element | pn crossing (involution) ≠ pp, nn (Hecke) | none, but kills a ruling |
| O3 knot assignment u = T(2,3), d = mirror | d–d crossings inverted | nonzero (§12 Y1: −45.8 % half, +35.2 % full) | changes it; not re-scored | rewrites letters of the γγ word | not computed | second selection rule on top of γγ: owner call |
| O4 quark charges in the matter term | e_u, e_d | p: Σe = 1, n: 0 | adds an EM piece | compatible | Coulomb pp only | hypercharge Y is open (flavor-charge-assignments), so e_u, e_d are inputs; α_em conditional on a sorry |
| O5 FE or EF alone (§22) | order of the weak insertion | flips sign with FE | changes it | compatible | — | choosing FE over EF is a choice; the state-dependent order gives q⁻² (Addendum B) |
| O6 x ≠ 0 off the E-system | trace fugacity | n − p = x(x²−1)/4 | — | — | — | sign of x is chosen: a fit |
| O7 kinematic reading | none: m_n − m_p := Q_β + m_e | neutron heavier by construction | consistent with D1 (gives 0.8364 MeV, −35.3 %) | compatible | — | none, but the sign is assumed, not derived |

Implications.

1. **O2 conflicts with D1.** If flavour is a strand colour with the forced trace, then ε_flavour(V³)
   = 0, and the ruled Q_β becomes 0. Coloured strands and the ruled Q_β cannot both stand as the
   flavour carrier. Coloured strands could still be used for bonds only (pn vs pp/nn), where they
   separate the unlike pair. That matches the sign-mixed pattern b₃ > 0 needs (`qou-q8vl`), but
   whether μ_pn > 1 there has not been computed.
2. **O1 + O7 is the consistent pair now on record.** O1 supplies Q_β, and O7 reads the mass gap from
   kinematics. The cost is explicit: under O7 the neutron-heavier sign is assumed, and "mass ∝
   trace" (R1/R2) is excluded as a reading (scope a). No ruling is touched.
3. **O3 is the only option that derives a nonzero sign from strand data**, and it touches the γγ
   ruling. Its numbers in §12 come from the old chirality table, on the half and full twist, not on
   V³. It needs a pre-registered V³ run and an owner decision on whether a mirror rule may act on a
   γγ-selected word.
4. **O4 and O5 import a choice** (hypercharge; E/F order), so they are not derivations today.

## Mirror rule on V³ and coloured bond factors (2026-11-22, owner: "Both")

Pre-registered: `np_mirror_and_bonds_preregistration.md`, commit 51776331e6c. Probe
`np_mirror_and_bonds_probe.py`, output in `.out.txt`. Exact over Q(q), x = 0, z = z_D, 20 s.

**Probe A, u = trefoil and d = mirror on V³.** Rule M inverts every crossing whose two strands are
both d.
- A1 holds: under rule 0, ε = 0 in all three flip pairs.
- **A2 is refuted.** Under rule M, too, s_p = s_n = 1 in all six placements. For every mixed
  placement, V³ has normalised sector trace exactly 1 under both rules. So the mirror rule has
  nothing to act on, and the knot assignment gives n = p on the ruled nucleon. The §12 numbers
  (−45.8 %, +35.2 %) were on the half and full twist and do not carry over to V³.
- A3 does not arise.

**Probe B, bonds with colour = nucleon isospin** (μ < 1 binds):

| letter | rule | μ_pp | μ_nn | μ_pn |
|---|---|---|---|---|
| g | 0 | 2q³/(q²+1) = 1.2254 | same | 0 (no log) |
| g | M | 1.2254 | (q⁴+1)/(q(q²+1)) = 1.0163 | 0 |
| g² | 0 | (2q⁴−q²+1)/(q²+1) = 1.2562 | same | **1** |
| g² | M | 1.2562 | 0.7875 | **1** |
| G³ | 0, M | 1.000469 (ppp) | 1.000469 (nnn) | **1** (every mixed colouring) |

Predictions B-a, B-b and B-c hold. **B-d: no candidate is sign-mixed.** μ_pn is exactly 1 whenever
it has a log. The reason is that a mixed-colour crossing is an involution, ((1−e)g)² = 1−e
(`YokonumaColourSplit.mixedColour_involution`), so pure braids cancel on the unlike pair. The pn bond
is exactly unbound: the deuteron gets B = 0. Lean (`coloured_unlike_unit_b3_zero`): with both unlike
pairs at f = 1, b₃ = 0 whatever the like bond is. So coloured bonds give b₃ = 0, not b₃ > 0.

**The full braid with electrons (siblings, not re-run here).**
- "Derive m_n by its own identity", PR #8804 §46, builds hydrogen from photons on four strands:
  W = γ(0,0,qh)·γ(0,0,−q⁻¹h)·g·K, with K the electron capture. The photons multiply exactly to V³ in
  the weight-space model.
- The p/n asymmetry factorises onto the capture braid: S(W) = χ₍₃₎(nucleon)·S(capture).
- The mirror identity O₊(right) = −O₋(left) holds exactly, so placement fixes the sign and no photon
  weight or gluon fixes it.
- Lean for the capture: branch `claude/hydrogen-capture-lean-2026-11-22`, `S(W_L) = −h²[3]_q/q²`,
  `S(W_L) + S(W_R) = 0`.
- This is the strand-level version of the mirror option. Its mirror swaps the sign rather than
  selecting one.
- Separately, the "Photon norm 1" thread finds the electron itself as a two-photon product in the
  six-strand neutral sector.

**Combined reading, scope (a).** Three strand-level carriers of u ≠ d all give no derived
ordering:
- colour (n = p, μ_pn = 1);
- mirror on the nucleon (n = p on V³);
- mirror on the electron capture (the sign follows placement and cancels between the two
  placements).

Still open: a γγ-derived electron placement on the six-strand neutral sector, which would fix the
capture's side. That belongs to the photon-norm and m_n threads.

## The ruled flavour split on the siblings' four-strand hydrogen element (2026-11-22, owner: "use their work")

Pre-registered: `np_hydrogen_flavour_split_preregistration.md`, commit bb861be97f2, with an honesty
clause. The probe is `np_hydrogen_flavour_split_probe.py`, and its output is in `.out.txt`. It is
exact over Q(q).

**The coincidence that prompted this, recorded and not adopted.** E₀^full·(ε(V³) + |S_B1|) =
0.78189 MeV, against CODATA Q_β 0.78233 (−0.057 %). That sum adds two different functionals: the
ruled K-weighted quantum trace and the sibling's T³-weighted B1. It also needs the placement whose
sign makes them add. It is selection against the target.

**What the single ruled functional gives.** E_c(W) = Tr(K^{⊗4}Π_c W)/[2]⁴, ε = E_p − E_n.

| element | ε at q₀ | E₀^full·\|ε\| (MeV) | t_n/t_p | ε − ε(V³) |
|---|---|---|---|---|
| W0 = V³ (electron spectator) | 0.0769805 | 0.32543 | q⁻² | 0 (H1 holds) |
| W_L, cabled capture | 0.0584529 | 0.24711 | q⁻² | −0.018528, O(h²) |
| W_R, cabled capture | 0.0457499 | 0.19341 | not q⁻² | −0.031231, O(h²) |
| W_adj,L | 0.0704847 | 0.29797 | q⁻² | −0.006496, O(h²) |
| W_adj,R | 0.0651658 | 0.27549 | not q⁻² | −0.011815, O(h²) |

Exact forms are in the output. For example, ε(W_L) = −h·N₁₆(q)/(q⁷(q²+1)⁴) with
N₁₆ = q¹⁶ − 3q¹⁴ + 3q¹² − 7q¹⁰ + 6q⁸ − 7q⁶ + 3q⁴ − 3q² + 1.

**Implications.**
1. **The 0.782 coincidence does not survive one functional.** On the ruled functional, the electron
   capture is a negative O(h²) correction. It moves the scored Q_β away from CODATA, to −68 % to
   −75 % depending on the arm, against −58.4 % for bare V³.
2. **Sign unchanged.** ε > 0 in every arm, so under "mass ∝ trace" the neutron is still lighter.
   The capture does not flip it.
3. **H3 is half refuted.** Proton-left placements keep t_n/t_p = q⁻² exactly. Proton-right
   placements break it. Under this functional the two placements are not mirror images, unlike the
   sibling's S, which is exactly antisymmetric. The reason is that K and u = e₁ are not
   mirror-invariant.
4. **Owner rule 2026-11-21 (keep derivable small corrections).** The capture term ε(W) − ε(V³) is
   exact and derivable once the element is fixed. It is a correction to keep. But the element is
   not fixed:
   - the cabling (cabled vs adjacent) is the sibling's labelled choice;
   - the placement (left vs right) is not derived;
   - the gluon (step 4) is owner-unresolved.
   So no single correction can be scored yet. If Q_β is ever scored on the hydrogen element instead
   of bare V³, it moves from 0.3254 MeV to 0.193–0.298 MeV.
5. Not formalised in Lean. The left-placement q⁻² ratio would follow from a K-weighted version of the
   sibling's intertwiner (`HydrogenCaptureWeightSpace.lean`). That is the natural next lemma.

## §21 Reconciling "u = e₁ is derived" with #8804 §40 "nothing fixes which bit is u"

Both statements are true, about different things. Exact sympy check (scratch, 2026-11-22):

| R-matrix | weight on factor 2 | partial trace |
|---|---|---|
| Ř (h on e₂e₁, σᵢ = strand i over i+1) | K = (q, q⁻¹) | q²·1, Markov |
| Ř | K⁻¹ | not scalar |
| XŘX (letter order reversed, h on e₁e₂) | K | not scalar |
| XŘX | K⁻¹ | q²·1, Markov |

So the Markov weight moves with the letter order. In either order, the over strand that keeps its
label is the K = q vector (`over_e1_iff_pure`, `ptr_markov`, `ptr_other_not_scalar`, #7971).

- What is derived (#8800): u is the K = q vector. This follows from def:down-quark (u passes over)
  and convention D, and it does not depend on the basis labels. A full relabel (X on R, K and the
  sectors together) leaves every ε unchanged.
- What #8804 §40 shows: if you swap which bit is u while keeping Ř and K, every E_n − E_p changes
  sign. That swap pairs u with the K = q⁻¹ vector. With Ř that weight is not a Markov trace, and
  under the over/under rule u would not be the over strand. So the swap is a coherent relabel only
  if Ř is conjugated too, and then nothing changes.
- What is still an input: the definition "u passes over". The photon form and the Borromean core
  do not fix it. §40 is right that nothing derived from those alone fixes the bit.

This confirms the sign table's idea (PR #8969): the e₁/e₂ order and the flavour order are one
letter-order convention. They cannot be flipped independently without breaking the Markov trace
or the over/under rule.

## §22 Lean: the left placement keeps q⁻² for every four-strand word

`QOU/QBeta/HydrogenFlavourSplit.lean` is sorry-free; axioms are propext, Classical.choice, Quot.sound only. It is lean-direct with `-DautoImplicit=false`, about 4 min. Everything is over a generic field with `q ≠ 0` and `q² + 1 ≠ 0`. The functional is the ruled `E_c = Tr(K^{⊗4}Π_c W)/[2]⁴`.

- `left_ratio`: put the nucleon on strands 0–2. Then `E_n = q⁻²·E_p` for every braid word on four strands, not only the capture words.
  - Proof: two explicit intertwiners between the weight blocks commute with every letter, `P32 : z=3 → z=2` and `P21 : z=2 → z=1`.
  - The functional `tn − q⁻²tp` is `Σ_z tr(M_z W_z)` with `M = (P21N21, P32N32 − N21P21, −N32P32)`. That sum cancels by trace cyclicity.
  - Reading: the K-weighted trace over the last strand is the Markov one (`OverStrandWeight.ptr_markov`). So an extra strand on the right never changes the flavour ratio.
- Closed forms of the ruled split:
  - `wL_eps`: `ε = (1 − q²)·(q¹⁶ − 3q¹⁴ + 3q¹² − 7q¹⁰ + 6q⁸ − 7q⁶ + 3q⁴ − 3q² + 1)/(q⁸(q² + 1)⁴)`, which is 0.0584528858 at the proton q₀.
  - `wAL_eps`: the corresponding closed form for the adjacent capture.
- `wR_defect`: put the nucleon on strands 1–3 with the reflected capture `wR`. Then `E_n − q⁻²E_p = −h²q²(q² + 1)·P(q)/q¹²`, nonzero. Here `P(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1` is the polynomial in `ε(V³)`.
  - `wR` is the strand reflection of `wL`. `towerTr_reflect` keeps the full trace, but the sector split is not reflection invariant: 0.0585 against 0.0457.
- The letter order of the vertex, `(σ₀σ₁⁻¹)³` against `(σ₁σ₀⁻¹)³`, does not change ε at three strands or in either four-strand placement (checked in exact sympy, 2026-11-22). Only the side of the extra strand matters.

The generator is in `computations/probes/np_splitting/lean_gen/`.

## §23 The capture is a conditional expectation; the sign at the Markov end for every word (2026-11-22, owner: "options 2 and 3")

Pre-registered: `np_capture_conditional_expectation_preregistration.md` (commit 057cd44e7ac, pushed
before the run; its honesty clause records that the adjacent-capture ratio was checked by hand
first). Probe: `np_capture_conditional_expectation_probe.py`, output in `.out.txt`. Lean:
`QOU/QBeta/HydrogenCaptureFactor.lean`. All five predictions hold.

**Placement.** Owner ruling 2026-11-22 (reading A, right-hand closure) puts a newly added strand on
the right, where the K-weighted partial trace is Markov. That is the nucleon-on-strands-0–2
placement of §22. This is the reading of the ruling used below; the ruling names bonds and
vertices, and its application to the electron strand is my reading, not a separate ruling.

**Option 3: the neutron is never heavier at the Markov end.**
- Lean, four strands, every word (`HydrogenCaptureFactor`):
  - `eps_eq_one_sub_mul_tp`: `ε = (1 − q⁻²)·t_p`, so ε has the sign of t_p.
  - `left_abs_tn_lt`, `left_increasing_reading_neutron_lighter`: for 1 < q, |t_n| < |t_p| whenever
    t_p ≠ 0, so every strictly increasing reading of the absolute sector trace (R2) makes the
    neutron lighter, whatever the capture or gluon word.
  - `left_signed_reading_iff`: under the signed reading (R1) the neutron is heavier iff t_p < 0.
- More strands (P1, exact at q = 111/100 and 7/5): every word of length ≤ 4 on 5 strands (4681)
  and ≤ 3 on 6 strands (1111) keeps E_n = q⁻²E_p, with zero failures.
- Why, for every n (argument, not formalised): let E be the K-weighted partial trace over the
  last strand divided by [2]. It maps the braid image on n strands into the image on n−1, because
  H_n = H_{n−1} + H_{n−1}σ_{n−1}H_{n−1} [jones1985] and E(σ_{n−1}) is a scalar
  (`OverStrandWeight.ptr_markov`). Π_c acts on strands 0–2 only, so the n-strand functional is the
  three-strand one on E^{n−3}(W), where the ratio is q⁻² (§1). Only the n = 4 case is in Lean.
- P2: with the nucleon not at the left end the ratio fails for about half of all short words
  (268/585 and 272/585 on 5 strands). The Markov end is what makes the result hold.

So under the ruled functional, with reading A, no capture or gluon word on the right makes the
neutron heavier by R1 with t_p > 0 or by any R2 reading. The sign question is then entirely the
choice of reading (§1 table), not of element.

**Option 2: the capture correction to Q_β.** At the Markov end, ε(V³·C) = ε₃(V³·E(C)) for any
capture word C on the new strand. For both capture words E(C) is central in the three-strand
image, so the capture only reweights the two isotypic blocks of ε(V³):

| capture | E(C) | ε(W)/ε(V³) at q₀ | Lean |
|---|---|---|---|
| adjacent σ₂⁻² | scalar c_adj = (q⁴+1)/(q²(q²+1)) = 1 + h² − hq²/[2] | 0.915617464418 | `wAL_eps_eq_factor` |
| cabled (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹, the inverse Jucys–Murphy element of strand 3 | c₃ = (q⁸+1)/(q⁶(q²+1)) on (3), c₂₁ = (q⁴+1)/(q⁴(q²+1)) on (2,1) | 0.759320340517 | `wL_eps_eq_blocks` |

The blocks of ε(V³) are ε₍₃₎ = q²(q²−1)/(q²+1)³ (V³ acts as 1 on the symmetric block, so this is
h/[2]³) and ε₍₂,₁₎ = −(q²−1)(q⁴−q²+1)(q⁸−2q⁶−2q²+1)/(q⁴(q²+1)³); they sum to ε(V³)
(`blocks_sum`). Both block dimensions are 4.

Implications:
1. The capture correction is exact and has a closed form once the capture word is fixed. It
   multiplies the ruled Q_β cell (0.3254 MeV, −58.4 %) by 0.9156 (adjacent, 0.2980 MeV) or 0.7593
   (cabled, 0.2471 MeV). Both move away from CODATA. Under the owner rule of 2026-11-21 (keep
   derivable small corrections) it is a correction to keep; it is not small (−8 % or −24 %).
2. What is still a choice: cabled versus adjacent capture (the sibling's labelled choice), and the
   gluon letter (owner-unresolved). The placement is now fixed by reading A. The formula
   ε₃(V³·E(C)) covers any future choice, including a gluon letter on the new strand; if E(C) is
   not central it is no longer a pure block reweighting.
3. No number here was compared with CODATA for selection (P5).

## §24 Q_β for the light isotopes under the current rulings (2026-11-22, owner: "Q_β for low isotopes")

At A ≤ 4 only the free neutron and ³H → ³He are β-emitters. With atomic masses,
Q_β(³H) = Q_β(n) + B(³He) − B(³H). The free-neutron term is the ruled cell, E₀·|ε(V³)| = 325.43 keV.
The binding energies are the γγ-chain values of `docs/audits/2026-11-22-light-nuclei-a2-a3-gg-chain.md`
§2 (branch `claude/project-thread-4ieh97`, proton pin, `B_diff`), reused, not recomputed. The
nucleon order is not fixed by the rulings, so every order is reported. Values in keV.

| ³H order | ³He order | B(³He) − B(³H) | Q_β(³H) |
|---|---|---:|---:|
| pnn | ppn / pnp | −0.594 | 324.84 |
| npn / nnp | ppn / pnp | −0.325 | 325.11 |
| pnn | npp | −0.950 | 324.48 |
| npn / nnp | npp | −0.681 | 324.75 |

Comparison only: observed Q_β(³H) = 18.59 keV and Q_β(n) = 782.3 keV.

- The chain binds each nucleus by about 1 keV and the two differ by less than 1 keV. So the model's
  Q_β(³H) is the free-neutron term. Experiment needs B(³H) − B(³He) = 763.8 keV, most of it the
  Coulomb energy of ³He. Nothing in the chain is of that size, and the miss is about 17×.
- The §23 capture factors scale the neutron term to 298.0 keV (adjacent) or 247.1 keV (cabled).
  That shifts every row by the same amount and does not close the gap.
- With `B_log` instead of `B_diff`, B(³He) − B(³H) lies between −3.8 and 0 keV. The conclusion is
  the same.
- No A = 6 or A = 8 binding values exist yet, so ⁶He and ⁸Li are not given.

## §25 The Coulomb energy, and the ³H row with it (2026-11-22, owner: "we're missing the coulomb energy")

The §24 chain binds by about 1 keV and carries no electromagnetic term. The repo's Coulomb term is
`computations/coulomb_energy.py`:

E_C(Z, A) = (3/5)·Z(Z−1)·α_EM·ℏc / R,  R = λ̄_π·A^{1/3}.

**Status of each input.**

| input | status | why |
|---|---|---|
| Z(Z−1) | derived | pair count of Z discrete charges; `CoulombFromCrossingCounts` rewrites it as (n₊−n₋)(n₊−n₋−4)/16 |
| α_EM = 1/(q[9]_q[10]_q·tower) | conditional | bare value is −0.155 %; the tower needs the Gram matrix Gq, which is a parameter with no instance of `ChernSimonsCorrectionConjecture` (beans qou-gbsa, qou-aemx) |
| ℏc | external | unit conversion |
| coefficient 1 on λ̄_π | selection | the data want 0.985 ± 0.069; no derivation fixes it |
| A^{1/3} | assumption | liquid-drop scaling; the A = 3 data want exponents 0.43 (³H) and 0.53 (³He) |
| 3/5 | imported | uniform-ball self-energy; nothing in the braid picture gives a charge density |

So E_C is a standard-physics estimate with one derived-but-conditional input, not a derivation.
At A = 3 it gives E_C(³He) = 0.847 MeV against the 0.764 MeV the masses require (+10.95 %).

**³H with E_C.** B(³He) loses E_C, so every §24 row moves by −847.4 keV:

| ³H order | ³He order | Q_β(³H), chain only | Q_β(³H), chain + E_C |
|---|---|---:|---:|
| pnn | ppn / pnp | 324.84 | −522.56 |
| npn / nnp | ppn / pnp | 325.11 | −522.29 |
| pnn | npp | 324.48 | −522.92 |
| npn / nnp | npp | 324.75 | −522.65 |

Comparison only: observed 18.59 keV.

- The sign is now wrong: ³H would be stable and ³He would decay.
- The cause is the neutron term, not the Coulomb term. With the observed Q_β(n) = 782.3 keV the
  same formula gives 782.3 − 763.8 = 18.5 keV. The model's 325.43 keV is short by 457 keV, and E_C
  is only 84 keV high. Fixing the Coulomb inputs cannot rescue this row.

**What is proved in Lean about Coulomb.**

- `QOU.Hecke.BoundedDegreeCoulomb`: a bounded-degree bond graph cannot carry a Z(Z−1) term. Coulomb
  must come from a long-range pair sum, not from the nearest-neighbour bonds the γγ chain uses.
- `QOU.MassTheory.CoulombFromCrossingCounts`: with n₊ − n₋ = 4Z, 16·Z(Z−1) = (n₊−n₋)(n₊−n₋−4).
  This is arithmetic. That the half-writhe *is* the charge is the open identification in
  `def:coulomb-charge`.
- `QOU.MassTheory.NeutronProtonEMSign`: Σ_{i<j} QᵢQⱼ is 0 for uud and −1/3 for udd, so a pair
  term ∝ QᵢQⱼ lowers m_n − m_p.

**What is missing, and the next target.** No result derives a pair term ∝ Q_A·Q_B between two
separate nucleon blocks from the ruled photon. That is the physics the formula above imports.
§26 pre-registers the test: exchange the ruled photon between two V³ blocks and decompose the result
by charge.

## §26 Photon exchange between two nucleon blocks is not a charge–charge term (2026-11-22, owner: "Do 1 2")

Pre-registration: `computations/probes/np_splitting/np_two_block_photon_exchange_preregistration.md`
(committed before the probe). Probe and output: `np_two_block_photon_exchange_probe.py` and
`.out.txt` in the same directory. Exact over Q(q); checked at q = 111/100 and 7/5.

Six strands, ruled core V³ = (σ_iσ_{i+1}⁻¹)³ on block A (strands 0–2) and block B (3–5).
Block charge Q = (u bits on the block) − 1. Pair shift ΔE_X(a, b) = T_X(a, b)/T_1(a, b) with
T_X = Tr(K^{⊗6}(Π_a ⊗ Π_b)V_A³V_B³X), for the photon monomials that touch both blocks.

**Result: outcome O4 for all six insertions** (σ₂, σ₂⁻¹, σ₁σ₂⁻¹, σ₂σ₃⁻¹, σ₂², σ₂⁻²), symbolically
and at both rational checks. Over the 16 charge pairs the shift is not of the form
c + αQ_a + βQ_b + κQ_aQ_b, so it is neither Coulomb (O1) nor isospin (O2).

Nucleon pairs at the proton q₀ (display only; I = pp − pn − np + nn):

| X | pp | pn | np | nn | (pp − nn)/I | (pn − np)/I |
|---|---:|---:|---:|---:|---:|---:|
| σ₂ | 0.66264 | 0.51652 | 0.58629 | 0.66352 | −0.0039 | −0.312 |
| σ₂⁻¹ | 0.45358 | 0.30746 | 0.37723 | 0.45446 | −0.0039 | −0.312 |
| σ₁σ₂⁻¹ | 0.23290 | 0.08273 | 0.15559 | 0.23156 | +0.0059 | −0.322 |
| σ₂σ₃⁻¹ | 0.17550 | 0.05587 | 0.11494 | 0.17817 | −0.0146 | −0.323 |

- The pattern is the opposite of Coulomb. Like pairs (pp, nn) agree to within 0.4–1.5 % of the
  interaction, and unlike pairs differ from them. Coulomb would single out pp and leave
  pn = np = nn.
- pn ≠ np by about 31 % of the interaction: the shift depends on which block is on the left.
- σ₂ and σ₂⁻¹ give the same I, because σ₂ − σ₂⁻¹ = h shifts every ΔE by the same constant. The
  squares scale I by h, because σ₂² = hσ₂ + 1.

**Lean.** `QOU/QBeta/TwoBlockExchangeNotCoulomb.lean` (sorry-free) computes the traces exactly in ℤ
at q = 2, where 2Ř, 2Ř⁻¹ and 2K are integral, and proves `not_coulomb_*` and `not_isospin_*` for
σ₂, σ₂⁻¹, σ₁σ₂⁻¹ and σ₂σ₃⁻¹. A form that held identically in q would hold at q = 2, so these refute
both identities. They do not measure the miss at q₀; the table does that.

**Scope.** This is a scope-(a) negative: single photon monomials between two V³ blocks, with the
ruled trace and sector projectors. It does not exclude a Coulomb term from longer exchanges
(photon ladders), other placements, a different readout of charge, or a reading in which the
electromagnetic pair term comes from the q-deformation of the trace rather than from the braid.
The su(2)-type braiding couples weights, and weights are nearly charge symmetric here; a Q·Q
term needs something that tells u from d beyond the weight, which is the role the U(1) photon
is meant to play. None of the six monomials does that.

**Consequence for §25.** The import list there stands: no part of E_C is derived from the ruled
photon yet.

## §27 No braid element gives Coulomb; spectators are invisible (2026-11-22, owner: "Do both … plank length for distance")

Pre-registration: `computations/probes/np_splitting/np_charge_vertex_search_preregistration.md`.
Probe and output: `np_charge_vertex_search_probe.py` and `.out.txt`. Exact Fraction arithmetic at
q = 111/100 and q = 7/5.

**A. The whole six-strand braid image.** The image of H_6 on (C²)^{⊗6} has dimension 132 (rank modulo
2³¹ − 1, at both q). Over all 720 reduced words, the sector vectors (T_X(a, b)) on the 16 charge pairs
span only 10 dimensions. Because T_X is linear in X, that covers every element, and with it every
order in φ at n = 6.

- Coulomb form c + κQ_aQ_b with κ ≠ 0: **not reachable** by any element.
- Isospin form c + κW_aW_b: not reachable either.
- An affine-bilinear form is reachable, and on a single ray:
  ΔE = c + κ·(Q_aQ_b − αQ_a − βQ_b) with **α + β = 1 exactly** at both q
  (q = 111/100: α = 0.656, β = 0.344; q = 7/5: α = 1.054, β = −0.054).
  Equivalently, ΔE = c' + κ(Q_a − β)(Q_b − α). The centres add up to one charge unit. At α = β = ½
  this is the isospin form W_aW_b/4. Coulomb would need α = β = 0, which the constraint α + β = 1
  forbids.
- On the four nucleon sectors alone the span is all of R⁴, so pp, pn, np and nn can each be set
  freely. Any pattern there, Coulomb included, is a choice of element rather than a derivation. The
  charge structure only becomes a constraint once the Δ sectors (Q = −1, 2) are included.

Reading, as a hypothesis: the braid image sees weight (T₃) and not charge. The zero of every reachable
pair term sits between p and n, not at n. Moving it to n needs Q = T₃ + B/2, that is, a baryon-number
(hypercharge) ingredient. The level-2 braiding has none.

**B. All orders in φ for a single crossing (Lean).** `QOU/QBeta/HeckeSeriesCollapse.lean` (sorry-free)
proves:
- `pow_eq_affine` and `sum_pow_eq_affine`: from σ² = hσ + 1, every power of σ, and every finite
  truncation of a series in σ, is a + bσ.
- `coulomb_of_affine`: if a + b·ΔE_σ has a Coulomb shape and b ≠ 0, then so does ΔE_σ.

With `not_coulomb_s2`, no finite order of the single-crossing photon gives a Coulomb term. Part A
already covers every element at n = 6.

**C. Distance (spectators).** With d = 0, 1, 2, 3 spectator strands between the blocks and the band
generator joining strand 2 to strand 3 + d, all four nucleon shifts are **exactly identical** for every
d, at both q. The braid carries no distance: an exchange across spectators is the same as an adjacent
one. A 1/r cannot come from counting strands. It needs a metric ingredient, and the braid and trace
supply none.

On the Planck length: `planck-length-share-vs-total` normalises ℓ_P = ħ_q·t_P = 1. That is a
dimensionless circuit, not a distance between particles, and C shows that strand counting does not
supply one either. The length in E_C is λ̄_π, which comes from the CAL-3 calibration.

**Scope.** Scope-(a) negatives. A and C are computed at n = 6 and n ≤ 9 at two rational q, not proved for
all q or all n. The α + β = 1 identity was measured exactly at two q; it holds over Q(q) at n = 6 (`docs/audits/2026-11-22-coulomb-all-q-and-nucleon-writhe.md`). Tower status:
A covers every element at n = 6 (all orders in φ there). The tower in n is open.

## §28 Gaudin / KZ coupling on the surface: isospin, not Coulomb; what Coulomb needs (2026-11-22, owner: "Yes, go ahead" on the Bring-surface test)

Pre-registration: `computations/probes/np_splitting/np_gaudin_pair_charge_preregistration.md`
(commit `a608acfa1dd`, before the probe). Probe and output:
`np_gaudin_pair_charge_probe.py`, `.out.txt`. Lean:
`QOU/QBeta/WeylSymmetricPairNotCoulomb.lean` (sorry-free, lean-direct exit 0, axioms
`propext`, `Classical.choice`, `Quot.sound`).

**Set-up.** The two blocks sit at points z_A, z_B of a local chart of Bring's surface. The KZ
connection is ħ·Ω_AB·d log(z_A − z_B) and the Gaudin term is Ω_AB/(z_A − z_B). Their coordinate
dependence is the two-dimensional Coulomb law: on a surface the potential is log|z|, and 1/|z|
needs three dimensions. So the only question is whether the **charge factor** Ω_AB reads Q_A·Q_B.
Readout as §26: ΔE_X = T_X/T_1, sector projectors, V = σ₀σ₁⁻¹ on each block, K = diag(q, q⁻¹).
Exact Fractions at q = 111/100, 7/5, 2 and at the proton q₀ (exact rational of the 50-digit pin).

| X | all 16 sectors | nucleons pp, pn, np, nn | as registered |
|---|---|---|---|
| G-sl2: Σ(½h_ih_j + e_if_j + f_ie_j) | O2 isospin, κ_W = ½, every q | ½, −½, −½, ½ | yes (1) |
| G-gl2: Σ P_ij | O2 isospin (+ constant 9/2) | 5, 4, 4, 5 | yes (1) |
| G-cartan: Σ h_ih_j (trigonometric diagonal) | O2 isospin | 1, −1, −1, 1 | yes (1) |
| G-q: U_q pair Casimir, coproduct compatible with Ř | O4 | **pp = nn exactly**, pn ≠ np, pp − pn − np + nn = q + q⁻¹ | yes (3): not O1 |
| G-q, opposite coproduct (control; does not commute with Ř) | O4 | pp ≠ nn | control |
| M: KZ monodromy β_AB² in H_6(q) | O4 | pp = nn exactly | yes (4) |
| QQ: Σ q_iq_j, q = diag(2/3, −1/3) | O1 Coulomb, κ = 1 | 1, 0, 0, 0 | yes (5): the readout sees Coulomb when it is put in |

Which coproduct commutes with the Jimbo Ř is decided by the probe, not assumed:
Δe = e⊗K + 1⊗e, Δf = f⊗1 + K⁻¹⊗f does; its opposite does not. The q-Casimir is central for both.

**Why every invariant coupling fails (proved).** e and f change the weight, so they have zero trace
against the sector projectors; the Cartan part of any gl(2)-invariant symmetric form
a·tr(XY) + b·tr X·tr Y, summed over strand pairs, is a(n_An_B + d_Ad_B) + 9b with d = 3 − n. It is
symmetric under the Weyl reflection u ↔ d, which swaps the proton and neutron blocks, so pp = nn
(`invCartan_pp_eq_nn`). A Coulomb shape c + κQ_AQ_B with pp = nn has κ = 0
(`coulomb_kappa_zero_of_pp_eq_nn`, `invCartan_not_coulomb`). The u(1) of gl(2) is the identity on
V: it is baryon number and adds the same constant for p and n. The q-deformed Casimir is not Weyl
symmetric in its coproduct, yet the Ř-compatible one still gives pp = nn at all four q measured, and
its interaction is the q-number [2]_q = q + q⁻¹ where the classical one gives 2. That is a q-deformed
isospin coupling with an ordering asymmetry pn ≠ np. pp = nn for G-q and M now holds identically
in q: `np_gaudin_generic_q_probe.py` computes every trace in ℤ[q, q⁻¹] (the Casimir scaled by h² to
clear its denominator) and finds pp = nn, pp − pn − np + nn = [2]_q, and pp = nn for M, each with
residual exactly 0 as a Laurent polynomial. The reason is visible in the output: for 1, G-q and M
alike, the pp sector trace is exactly q⁴ times the nn sector trace, so the ratio dE is equal.

**What Coulomb needs.** The Coulomb operator is Q⊗Q with strand charge Q = T₃ + B/2, B = 1/3 per
strand: u ↦ 2/3, d ↦ −1/3, block charge n − 1 (`blockCharge_eq`). Written in gl(2),
Q = ½h + ⅙·1, so Q⊗Q contains the cross term (h⊗1 + 1⊗h)/12, which no invariant form has, and it
gives pp ≠ nn (`coulombPair_pp_ne_nn`). So the missing ingredient is exactly the Gell-Mann–Nishijima
mixing of T₃ with baryon number: a choice of which U(1) is gauged. That is electroweak symmetry
breaking to U(1)_em. The braid, the Hecke algebra, the Markov trace and the KZ/Gaudin coupling all
respect the Weyl reflection on the nucleon sectors, so none of them makes that choice.

**The helon ribbon twist (Gresnigt, Bilson-Thompson; prior-art review on PR #9095).** In the helon
model, electric charge is the number of ribbon twists (B₂ ≅ ℤ), assigned to the strands so the
charges come out right. In a ribbon category the twist on a simple object is a scalar, θ_V = q^{C(V)}.
Here u and d are two basis vectors of the one object V, so the twist cannot tell them apart. For twist
to carry charge, u and d must be different simple objects, i.e. V must be tensored with U(1) lines
L_k whose label is the electric charge. The double braiding of two U(1) lines is q^{2k_Ak_B}. Its log
is exactly κ·k_A·k_B: a Coulomb charge factor with its zero at charge 0. So the helon twist does
supply the U(1) charge factor, but only by attaching the charge label by hand, which is the same
Gell-Mann–Nishijima input. It is a carrier for the missing ingredient, not a derivation of it. Not
computed beyond this argument.

**Scope.** Scope-(b) for the invariant classical forms: the Weyl-symmetry step is proved in
`WeylSymmetricPairNotCoulomb.lean`, and the off-diagonal zero trace and the Cartan readout are proved
for every q and every weight-preserving core in `WeightShiftZeroTrace.lean`
(`sectorTrace_eq_zero_of_shift`, `sectorTrace_diag`, `gaudin_readout`; that the Jimbo Ř preserves
the u-count entrywise is `jimbo_weight_preserving`). For M, pp = nn is proved at q = 2 in Lean
(`dE_M_pp_eq_nn`, `M_coulomb_kappa_zero` in `TwoBlockExchangeNotCoulomb.lean`, kernel `decide`).
For G-q and M, pp = nn at generic q is an exact symbolic computation over ℤ[q, q⁻¹] (2026-11-22),
and its algebraic core is proved in Lean at generic q over any field
(`QCasimirPairGenericQ.lean`: `pairReadout_pp_eq_nn_of_blockData`, `pairDE_pp_eq_nn_of_blockData`,
`pairDE_interaction_of_blockData`, sorry-free). The Lean takes the block data as hypotheses: the
block traces are a(n) = k(n)·τ and h²c(n) = k(n)·(μ − (q k(n) + (q k(n))⁻¹)·τ), with k(2) = q,
k(1) = q⁻¹. That is, the core commutes with U_q on each block and the Casimir is a scalar on each
irreducible summand. Under them, pp = nn and pp − pn − np + nn = h²[2]_q hold for every τ and μ, so
for every U_q-commuting core, not only V = σ₀σ₁⁻¹. The hypotheses themselves are standard U_q(sl₂)
representation theory and are not proved in the file. For M, pp = nn at generic q is the symbolic
computation only. Both G-q and M are invariant under the map
u ↔ d together with i ↦ 5 − i (checked exactly at q = 7/5); a general proof of pp = nn from that
symmetry is open. Both pp = nn identities, and the §27A identity α + β = 1, hold exactly over Q(q) at n = 6: `docs/audits/2026-11-22-coulomb-all-q-and-nucleon-writhe.md` (computer algebra, pre-registered). Tower status: n = 6 only; the tower in n is open. No empirical
input, no fit.

**Owner decision this raises (not taken).** Whether the model adds a U(1)_em grading (strand charge
T₃ + B/2) as an explicit structural input, or looks for a mechanism inside the corpus that breaks
the Weyl reflection. The default, if nothing is decided, is that E_C stays an import (§25).

## §29 Where the U(1) charge lines come in (2026-11-22, owner: "Search for a mechanism first"; "where the U1 charge lines come in … do we need another paper?")

Lean: `QOU/QBeta/NeutralExchangeSplit.lean` (sorry-free, lean-direct exit 0).

**The corpus already holds the question.** `eightfold-way/flavor-charge-assignments.md` records
the electric charge as Gell-Mann–Nishijima `Q = I₃ + Y/2`, with I₃ derived (writhe coordinate) and
**hypercharge Y open**. Its candidate, the helon ribbon twist, is shown there to be a free label
(the battery reduces to T = 3Q), and the canonical ribbon twist (content sum) is refuted at n ≤ 8
because it gives only integer charges. `coulomb-charge.md` says the halved writhe is not
established as an electric charge. `weinberg-angle-categorical` is a conjecture whose evaluated form
misses (cot θ_W = q⁻⁴ ≈ 0.659 against 1.823). §28 is consistent with all three.

**Where the U(1) lines are.** They are already in the braiding. The Jimbo Ř is the U_q(gl(2))
R-matrix; its Cartan torus is U(1)_{T₃} × U(1)_B, and its Cartan factor
q^{E₁₁⊗E₁₁ + E₂₂⊗E₂₂} = q^{½h⊗h + ½·1⊗1} couples T₃ to T₃ and B to B, with no cross term. That is
the shape of the **unbroken** neutral exchange, W³ with coupling g and B with coupling g′:
g²·T₃T₃′ + g′²·(Y/2)(Y′/2). On three-quark blocks (Y = B = 1) this is isospin, pp = nn
(`nucleon_unbroken_isospin`), which is what §28 measured.

**What turns it into Coulomb.** `neutralExchange_split` proves, over any field,

    g²T₃T₃′ + g′²(Y/2)(Y′/2) = e²·QQ′ + g_Z²·(T₃ − s²Q)(T₃′ − s²Q′),
    e² = g²g′²/(g²+g′²),  s² = g′²/(g²+g′²),  g_Z² = g²+g′²,  Q = T₃ + Y/2.

The first term is the Coulomb factor, zero whenever a neutron is involved
(`nucleon_photon_coulomb`). So Coulomb is the unbroken exchange **minus the Z exchange**, and in the
Standard Model the Z drops out at long distance because it is massive. The §28 negative is
therefore what the physics predicts: an invariant (unbroken) coupling cannot be Coulomb. Two things
are needed and neither is derived in the corpus:
1. the mixing angle s² = sin²θ_W (the corpus conjecture `weinberg-angle-categorical`, currently off);
2. a Z mass scale that removes the second term at nuclear distance (no derivation found).
The u ↔ d asymmetry of Q = T₃ + B/2 itself is not a third input: with B = 1/3 per strand it is fixed
once a nucleon is a three-strand block (`blockCharge_eq`, §28).

**Do we need another paper?** Not for the mathematics: the identity above is elementary, and the
held Furey thesis (`furey2016`, `library/arxiv-1611.09182v1`) already derives U(1)_em as the
unique unbroken symmetry, generated by Q = N/3 with N a number operator, which is the u-counting
operator Σ E₁₁ here up to the baryon shift. The standard electroweak references (Glashow 1961,
Weinberg 1967, Salam 1968) are not registered; only `colemanglashow1961` is. They would be cited, not
used to derive anything. The open content is the Weinberg angle and the Z scale, which are corpus
problems, not literature gaps.

**Scope.** Algebraic identity, proved. Nothing here fixes s² or the Z mass; no number is claimed.
Tower status: not a tower computation.

## §30 Colour on the strand does not move the p/n readout (2026-11-22, owner: "Merge and continue")

The lead: if colour travels with the strand, the baryon trace of a word is the colour-singlet
twist of the flavour trace, and that twist could flip a sign in the p/n split. On colour singlets
there are two ways to write the strand letter (PR #9107, `ColourSingletSignTwist`,
`coideal_mul_tensor`):

- **Tensor route, raw letter.** X = −q⁻¹·b. Every letter is multiplied by the same scalar, so a fixed
  word of length L has every sector trace multiplied by (−q⁻¹)^L. The ratio T_X/T_1 in each sector
  is unchanged, so pp, pn, np and nn are exactly the flavour values. The owner ruling on #9107 makes
  b = −q·X the bond letter, which removes even the scalar.
- **gl₆ coideal route (the Hecke mirror).** s = −b⁻¹. This is not a scalar. But the mirrored core
  still commutes with U_q on each block, since an inverse of a commuting operator commutes, so the
  Lean result of §28 (`pairReadout_pp_eq_nn_of_blockData`, every U_q-commuting core) already gives
  pp = nn for the q-Casimir coupling. `np_gaudin_colour_mirror_probe.py` recomputes the q-Casimir
  and the KZ monodromy M with b ↦ −b⁻¹ in ℤ[q, q⁻¹], and both give pp = nn identically in q.

So neither colour route breaks the u ↔ d reflection, and colour cannot supply the Coulomb ordering
p < n through these couplings. The missing ingredient is still the U(1)_em grading of §28–§29.

**Scope.** Scope-(a) for M under the mirror (exact symbolic computation, not Lean). The tensor-route
statement is the scalar-cancellation argument above. Tower status: n = 6 only. No empirical input.

## §31 Where the U(1)_em lines can sit (2026-11-22, owner: "Both" — labelled input now, derivation open)

**Not on the strands.** Put the most general strand-symmetric charge phase on the Jimbo braiding,
Ř′ = Ř·diag(a, b, b, c) on uu, ud, du, dd. Yang–Baxter on three strands has exactly two nonzero
defect entries, −b(a − b)(q² − 1)(aq² + b)/q and the same with c (`u1_em_twist_ybe_probe.py`, exact
sympy). So a and c must each equal b or −b/q². The em charge line t^{9QQ′} has (a, b, c) = (t⁴, t⁻², t).
Its only solutions are t a cube root of unity, where the phase is the scalar Z₃ centre and invisible.
Over the reals with q > 1 it is t = 1, zero coupling (`ChargePhaseYangBaxterObstruction.lean`:
`ybe_entry`, `ybe_forces`, `charge_phase_trivial`, sorry-free). The cause is the Hecke term h: it
sends du to itself, which a braiding of two different U(1) objects cannot do. With h removed the
phase works for every t. The same argument applies to the gl₃ colour Jimbo braiding. And p and n
share the colour singlet ε, so a charge read off the colour factor cannot tell them apart either
(checked against PR #9107: its Lean carries no charge, and its Furey gl₈ route fails at q ≠ 1).

**On whole hadrons.** Tensor each nucleon block with one U(1) line L_Q, Q = n − 1, so p and n are
distinct charged objects. Lines braid by t^{QQ′}·swap, which satisfies Yang–Baxter for every t
(`lineBraid_ybe`). Passing A once round B gives t^{2Q_AQ_B} (`monodromy_eq`). Its log is
2 log t · Q_AQ_B: the Coulomb shape with κ = 2 log t, zero whenever a neutron is involved
(`em_coulombOnNucleons`). Added to the isospin-symmetric flavour readout (§28), the pair split is
pp − nn = 2 log t, nonzero iff t ≠ 1 (`total_pp_sub_nn`, `split_ne_zero_iff`;
`HadronChargeLineCoulomb.lean`, sorry-free).

**What this commits to.** Charge is a hadron-level label, an input (Gell-Mann–Nishijima), not a
derived feature of the strand braid. That is consistent with physics: U(1)_em appears only after
the electroweak symmetry is broken, and the strand-level Hecke braiding is the unbroken stage.
The coupling t is open, to come from the corpus α_EM, and is not fitted. The derivation route
(sin²θ_W, Z scale; §29) stays open.

**Scope.** Scope-(b) for the strand-level exclusion (Lean invariant: the Yang–Baxter entry). The
hadron-level construction is a labelled input. Tower status: two blocks, n = 6. No empirical input.

## §32 The block-data hypotheses of §28, discharged (2026-11-22, owner: "Fill gaps")

§28's generic-q theorem (`QCasimirPairGenericQ.lean`) took two hypotheses about one nucleon block:
its K-weighted core trace is k·τ and its Casimir-inserted trace is k·(μ − (qk + (qk)⁻¹)·τ), with the
same τ and μ on the proton sector (two u) and the neutron sector (one u). Those are now proved, for
any word in σ₀^{±1}, σ₁^{±1} on the block's three strands, over any field with q ≠ 0
(`BlockChargeSectorTrace.lean`, sorry-free, axioms propext / Classical.choice / Quot.sound only).

- **The sector matrices.** On the one-u sector (udd, dud, ddu) the Jimbo braiding gives σ₀ ↦ A0,
  σ₁ ↦ A1, with A0 = [[0,1,0],[1,h,0],[0,0,q]] and A1 = [[q,0,0],[0,0,1],[0,1,h]]. On the two-u
  sector the roles swap: σ₀ ↦ A1, σ₁ ↦ A0 (`block_sector_matrices_probe.py`, exact sympy).
- **Why the traces agree.** Δ = A0·A1·A0 intertwines the two letters, A1·Δ = Δ·A0 and A0·Δ = Δ·A1,
  and det Δ = −q³ ≠ 0. So every word on the two-u sector is Δ times the same word on the one-u
  sector times Δ⁻¹, and the traces are equal (`intertwine`, `det_Δ`, `sectorTrace_eq`). This is the
  braid-group Garside element acting as the u ↔ d swap.
- **The Casimir.** h²C restricted to either sector is one 3×3 matrix G, checked against the 6-site
  Casimir of the §28 probe (`block_sector_matrices_probe.py`). G commutes with A0 and A1, hence with
  Δ, so the Casimir-inserted traces agree too (`G_comm_A0`, `G_comm_A1`, `G_comm_Δ`,
  `casimirTrace_eq`). With fe inserted, h²fe = G − (qk + (qk)⁻¹) on the sector of K-value k, which is
  the second hypothesis with μ = tr(ρ(w)·G) (`feTrace_eq`).

**What is still outside Lean.** The step from the 64-dimensional two-block readout to these per-block
3×3 traces (the block tensor factorisation and the K-weighting of §28) is checked by exact computation
in `np_gaudin_generic_q_probe.py`, not proved. So §28's pp = nn is now Lean-proved from the block
level up, and computed below it.

**Scope.** Exact identities, no empirical input, no fitting. Tower status: one block, n = 3; the pair
statement is n = 6.

## §33 The two-block readout reduces to per-block traces (2026-11-22)

`PairReadoutTensorReduction.lean` (sorry-free; axioms propext / Classical.choice / Quot.sound) proves
the step §32 left to computation, in abstract form. Each block carries `e, f, K, K⁻¹`, a core `W` and
a charge-sector projector `P`, with the sector conditions: `P² = P`; `P` commutes with `K`, `K⁻¹`, `W`;
`K` and `K⁻¹` act on the sector as the scalars `k`, `k⁻¹`; `PeP = PfP = 0`. The pair operator is
`h²·Δf·Δe + qK_AK_B + q⁻¹K_A⁻¹K_B⁻¹ − C_A ⊗ 1 − 1 ⊗ C_B` with the `Ř`-compatible coproduct. Then
`tr((P_A ⊗ P_B)(K_A ⊗ K_B)(W_A ⊗ W_B)·X)` equals `QCasimirPairGenericQ.pairReadout` with
`a = tr(PKW)` and `c = h²·tr(PKW·fe)` per block (`readout_eq_pairReadout`). The charge-moving terms
`f_A ⊗ e_B` and `K_A⁻¹e_A ⊗ f_BK_B` drop out because each has a factor with `PYP = 0`
(`trace_shift`, `shift_mul_left`, `shift_mul_right`).

**Chain now.** Two-block readout → per-block `a`, `c` (§33, Lean) → equal `τ`, `μ` on the proton and
neutron sectors of a three-strand block (§32, Lean, on 3×3 sector matrices) → pp = nn and the
interaction `h²[2]_q` (§28, Lean). The one link still checked only by computation is that the 8×8
block operators, restricted to the two charge sectors, are the 3×3 matrices `A0`, `A1`, `G` of §32
(`block_sector_matrices_probe.py`, exact sympy).

**Scope.** Exact algebra over any field. No empirical input. Tower status: two blocks, n = 6.

## §34 pp = nn, end to end in Lean (2026-11-22)

`BlockSectorRestriction.lean` (sorry-free; `readout_pp_eq_nn` depends only on propext /
Classical.choice / Quot.sound) closes the last link of §33. On the 8-dimensional space of one block
(`u = 0`) it defines the Jimbo letters σ₀^{±1}, σ₁^{±1}, the operators `e, f, K, K⁻¹` with the
`Ř`-compatible coproduct, and the projectors onto the one-u and two-u sectors. It proves:

- every letter, and so every word, preserves the u-count, and restricted to the two sectors in the
  bases of §32 it is the 3 × 3 letter matrix (`letter_restrict`, `word_restrict`);
- `h²·fe` restricted to either sector is `G − (qk + (qk)⁻¹)` (`cas_restrict`);
- the sector conditions of §33 hold for these operators, any word, and `k = q⁻¹` (one u) or `k = q`
  (two u) (`sector`).

Composing §33, §32 and §28: for every three-strand core word `w` in both nucleon blocks, the
two-nucleon q-Casimir readout divided by the identity readout is the same in the pp and nn sectors
(`readout_pp_eq_nn`, stated cross-multiplied), over any field with `q ≠ 0`.

**What it does not cover.** Cores that braid strands of one nucleon with strands of the other (the
core here sits inside the blocks, as in the §28 probe); different core words in the two blocks; the
tower beyond n = 6. The conclusion is the same as §28: this coupling cannot make the neutron heavier,
and a Coulomb shape from it has κ = 0. That is now a theorem, not a computation.

**Scope.** Exact algebra, no empirical input, no fitting. Scope-(b) for this coupling class.

## §35 Cores that braid across the two nucleons break pp = nn (2026-11-22, pre-registered)

Pre-registered in `np_cross_core_probe.py` (committed before the run, fixed list of five cores,
decision rule: d = TX[pp]·T1[nn] − TX[nn]·T1[pp] in ℤ[q, q⁻¹]). Same readout and pair operator as §28;
the core is the §28 in-block core times a word that crosses strand 2 (block A) with strand 3 (block B).

| core (× in-block base) | pp = nn identically in q | ΔE_pp − ΔE_nn at q₀ (proton pin) |
|---|---|---|
| (a) σ₂ | no | +1.290e-4 |
| (b) σ₂⁻¹ | no | +2.154e-4 |
| (c) σ₂² (pure braid: strands return to their nucleon) | no | +1.142e-5 |
| (d) σ₂σ₃σ₁σ₂ | no | +6.095e-5 |
| (e) β_AB² full twist (control) | **yes** | 0 |

(mpmath 50 dps; exact polynomials in `np_cross_core_probe.out.txt`.)

**What this shows.** §34's restriction to in-block cores is load-bearing. The full twist β_AB² (central
on the pair) keeps pp = nn, but a single linking of one strand of each nucleon, σ₂², does not, and it
still returns every strand to its own nucleon, so the pp and nn labels stay meaningful. Cores (a), (b),
(d) move a strand between nucleons, so their sector readouts are diagonal restrictions of a
charge-moving operator and are harder to read physically; (c) is the clean case.

**Shape.** For core (c) the split is not Coulomb-shaped. pn and np sit well below nn (at q₀:
ΔE_pn − ΔE_nn = −0.0572, ΔE_np − ΔE_nn = −0.0287), pn ≠ np because the core is not A ↔ B symmetric,
and pp − nn is small and positive. The sign of pp − nn is positive at q = 1.01, 1.05, q₀, 1.3, 2, 3. It
is not definite on q > 1: T1 has real zeros at 1.502, 1.668 (pp) and 1.544, 1.613 (nn), and the ratio
changes sign in that window.

**Scope.** Scope-(a): these cores, alone, with this coupling. No empirical input, no fitting. The core list
was fixed in advance and was not chosen for the sign. Whether a cross-nucleon linking is physically the
right core is not decided here: it would be the first coupling on record with pp ≠ nn at generic q from the
braid alone. Tower status: n = 6.
