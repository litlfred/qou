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

## Addendum, 2026-11-22: all-pairs bonds at A = 3

Owner choice (thread, 2026-11-22): extend the result to all-pairs bonds at A = 3 on the same branch.

**Disclosure.** Before this addendum was written, one cell was computed, ³H in order p n n with
over transport, as a timing test. In it `tr_atom/tr_free − 1 = −y⁵(q⁴+q²+1)·P₃₆(q)/(q¹⁰(q²+1)²Dn²)`
with `P₃₆(1) = −6`, and the exact trace is negative at `q = 2`. So the chain theorem does
**not** carry over unchanged, and nothing below predicts a sign at every q.

Objects: bonds on pairs (0,1), (1,2), (0,2), each `V³` placed as in the chain. The
non-neighbour bond (0,2) is transported by `σ₂σ₃σ₄ · V³ · (σ₄σ₃σ₂)⁻¹` ("over") or by the
reverse crossing signs ("under"), as in `he4_gg_all_pairs_probe.py`. Exact ℚ(q) on 9 strands.

- **P5 (control).** At the proton pin, ³H p n n and ³He p p n in both variants reproduce the
  all-pairs rows of `he4-gg-all-pairs.witness.json` (mpmath) to its printed digits, and unbind.
- **P6 (no prediction).** For every order (³H: pnn, npn, nnp; ³He: ppn, pnp, npp) and both
  variants, the factored closed form, the real roots of its sign-determining factor in
  `q > 1`, and the q-intervals where `tr_atom < tr_free` (binding) are all reported. None is selected.
- **P7 (control).** "Appended" and "arranged" placements give the same trace exactly
  (in the mpmath witness they agree to 0 and 1.9e−62).

No fit, no choice of order or variant, and AME is still comparison only.

## Addendum 2, 2026-11-22: ⁴He with all six pairs bonded

Owner, after #9053 merged: "Merge and continue". This addendum is written before any ⁴He
all-pairs trace of this probe. What was run beforehand: a timing test of the word expansion
(297 000 terms at q = 2), with no trace value printed, and a speed check of a flint-based
exact trace on the ³H pnn over cell, which reproduces the Fraction trace at q = 2 exactly.

Objects: the four formation routes of `he4_all_pairs_formation` (D+D pairing a, D+D pairing
b, ³H+p, ³He+n), with over and under transport, gives 8 cells. Bonds are placed as in
`he4_gg_all_pairs` (each after block max(j), in route order), in the production order p p n n.
The γγ chain is the control. Reduction: everything after the first nucleon uses generators
σ₂, σ₃, …, so `towerTr_disjoint` (proved) gives `tr_atom = tr N₀ · tr(tail)`, and the trace
runs on 10 strands.

- **P8 (control).** At the proton pin, every cell reproduces the ⁴He rows of
  `he4-gg-all-pairs.witness.json` to below 1e−28, and the chain reproduces −0.862 keV.
- **P9 (control).** At A = 3, tr N₀ · tr(tail on 7 strands) equals the 9-strand trace
  exactly, in every cell of the first addendum.
- **P10 (no prediction).** Report for each cell the factored `ratio − 1`, the leading order at
  q = 1, the sign pattern of its sign factor in y = q² − 1, and every crossing in q > 1. The
  A = 3 pattern (exactly one crossing) is **not** assumed.

No fit, no choice of route or variant, and AME is comparison only.
