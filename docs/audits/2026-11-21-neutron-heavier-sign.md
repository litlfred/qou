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
