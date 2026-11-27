# Pre-registration: mirror rule on V³, and coloured bond factors (2026-11-22)

Written before `np_mirror_and_bonds_probe.py` is run. Owner choice 2026-11-22: "Both". Algebra,
basis and trace exactly as in `np_yokonuma_coloured_probe.py`: Y_{2,3}(q), Juyumaya trace at
z = z_D = q³/(q²+1), x = 0. x = 0 is forced, since x = ±1 kills a colour sector (np-splitting §12).
The probe is exact over Q(q). Values at the proton q₀ are shown for display only, with mpmath. No
CODATA value selects anything.

## Probe A: u = trefoil, d = mirror, on the ruled V³ = (g₁g₂⁻¹)³
- Rule M (the §12 "Y1" rule, fixed): when both strands at a crossing are d, invert the written
  letter (g ↔ g⁻¹). Otherwise keep it. Strand positions are tracked through the word. Control: rule
  0, every letter as written.
- V³'s permutation is the identity, so every placement has a nonzero trace. Proton placements
  uud, udu, duu; neutron placements udd, dud, ddu. All six are reported. None is selected.
- Report: s_c = tr(π_c W)/tr(π_c) for each placement, the ratio s_n/s_p for each flip-paired
  pair, and ε = s_n − s_p. For display only, E₀^full·|ε|, with E₀^full = m_e/(q(q−1)(1−ℏ²)),
  ℏ = 1 − 1/q.
- Predictions:
  - **A1.** Under rule 0, s_n = s_p (the flip result, 21/21 in the earlier probe).
  - **A2.** Under rule M, the flip symmetry breaks and s_n ≠ s_p for at least one placement pair.
  - **A3.** The sign of s_n − s_p under rule M is not the same for every placement pair. If it is
    not, the sign depends on the placement, which is not derived for V³.

## Probe B: bond factors μ_pp, μ_nn, μ_pn (colour = nucleon isospin)
- μ_c(W) = tr(π_c W)/tr(π_c). B = −α·log μ, so μ < 1 binds. b₃ > 0 on a chain needs the unlike
  bond on the opposite side of 1 from both like bonds (`B3SignOneRoot.b3corpus_chain`, bean
  `qou-q8vl`).
- Candidate bond letters, fixed in advance:
  - **B1** g (two strands)
  - **B2** g² (two strands, the full twist)
  - **B3** the γγ bond G³ = (g₁g₂⁻¹)³ on three strands, with every colouring of the three strands
    by p/n. Like and unlike are read from the colour counts.
- Each is computed under rule 0 and under rule M (n–n crossings inverted).
- Predictions:
  - **B-a.** For B1, μ_pn = 0, because a mixed-colour single crossing permutes colours (tr = 0).
    No log exists there.
  - **B-b.** For B2 under rule 0, μ_pn = 1 exactly (on the mixed sector g² = 1), and μ_pp = μ_nn.
    Not sign-mixed: the pn bond is exactly unbound.
  - **B-c.** Under rule 0, μ_pp = μ_nn for every candidate (flip symmetry).
  - **B-d.** No candidate is asserted to pass. Whether any gives μ_pn < 1 < μ_pp, μ_nn is the
    measurement.
