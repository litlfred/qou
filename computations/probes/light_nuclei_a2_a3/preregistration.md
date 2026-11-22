# Pre-registration: ²H, ³H, ³He on the ruled γγ bond

Issue #9039. Written before any A = 2 or A = 3 binding number of this probe is computed.

## Rulings used (`docs/coordination/owner-rulings.md`)

- Photon vertex at strands `(i, i+1)` is `σ_iσ_{i+1}⁻¹` (reading A); closure on the right, so a
  bond enters the newer nucleon (2026-11-22). In the chain this is the "left entry"
  placement of `he4_sign_conventions_probe.py`: the bond `V³ = (σ_{3j−1}σ_{3j}⁻¹)³` sits on the
  last strand of nucleon `j − 1` and the first two strands of nucleon `j`.
- Nucleon blocks: the production proton and neutron words (`hecke_exact.Ring.proton/neutron`,
  identical to `atom_braid_word_3A` blocks).
- Trace: Ocneanu/Markov trace at `z_D = q³/(q² + 1)`, exact over ℚ(q).
- Binding forms, both reported, neither chosen: `B_diff = E₀(tr_free − tr_atom)` and
  `B_log = E₀ ln(tr_free/tr_atom)`, with `E₀` the value recorded in
  `he4-gg-all-pairs.witness.json`. `E₀` is a scale only; it never changes a sign.

## What is already known before this probe

The symbolic factorisation (exact ℚ(q), computed before any binding number) gives the
bond factor ratios `μ_x = tr(V³ · x↑¹)/tr(x)` for `x ∈ {p, n}` in closed form. With
`y = q² − 1`, `μ_p − 1` and `μ_n − 1` are `y⁴` resp. `y⁵` times ratios of polynomials whose
coefficients in `y` are all positive. By the chain law (`towerTr_ggChain`, proved)
`tr_atom = tr(N₀) · ∏_{j≥1} μ_{N_j} tr(N_j)`.

## Predictions

- **P1 (structural, every q > 1).** For every nucleon order and every A ≥ 2, `tr_atom > tr_free`,
  so `B_diff < 0` and `B_log < 0`: every γγ chain unbinds. It binds at no q > 1, and the
  binding vanishes at q = 1 to order `y⁴` (first bond entering a proton) or `y⁵` (neutron).
- **P2 (control).** ²H in order p n reproduces §6c of
  `docs/audits/2026-11-21-he4-binding-breakdown.md`: `B_diff = −0.77 keV`, `B_log = −2.58 keV`
  (to the digits printed there); ⁴He ppnn reproduces `−0.862 keV`.
- **P3 (orders).** For ²H (pn, np), ³H (pnn, npn, nnp), ³He (ppn, pnp, npp) every row is
  reported. No order is selected; the owner ruled order must be derived (2026-11-21), and this
  probe does not derive it.
- **P4 (mirror).** No prediction for the sign of `B(³He) − B(³H)`. Reported as found.

## Comparison (audit only)

AME2020 B: ²H 2224.6, ³H 8481.8, ³He 7718.0 keV. These enter the audit doc and the witness
as comparison fields only, never Lean and never any choice.

## Not covered

All-pairs bonding at A = 3 (non-neighbour transport): on record in §6c (mpmath), not
re-derived here. Many-body γγ vertices. A non-trace energy map.
