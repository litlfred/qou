# Sign issues across the mass, binding and decay arcs, and the ordering they share

Issue #8960, branch `claude/he4-binding-breakdown-2026-11-21`. Owner, 2026-11-22: *"make a
table of where we have all of our sign issues and see if we can sort them out. I think there
are a couple of overlapping areas"*, and *"If we can come back to the first principles that
drove the ordering for the gerbner bases, hopefully that'll help to sort out the signs"*.

This is a record of where each sign comes from. It changes no producer, number or ruling.

## 1. The ordering principle

`prop:braiding-induced-ordering` (`quantum-observable-universes/braiding-induced-ordering.md`)
orders the positive words of `W_n` degree-lexicographically **after a total order on the
letters is fixed**, and says the letter order is a choice, so the ordering is not canonical.
The Gröbner–Shirshov normal form (`appendix-transfer-matrices/tm-gs-normal-form.md`,
`mba-step02-gs-reduction.md`) keeps positive letters as leading monomials and rewrites
`σ⁻¹ = σ − h`. Three facts follow, each checked or proved:

1. **The leading monomial does not see chirality.** `σ_iσ_{i+1}⁻¹ = σ_iσ_{i+1} − hσ_i` and its
   ι image `σ_i⁻¹σ_{i+1} = σ_iσ_{i+1} − hσ_{i+1}` (ι: `σ ↦ −σ⁻¹`) share the leading term with
   coefficient `+1`. They differ only in the correction term, by **which letter is inverted:
   the larger or the smaller in the letter order**. The ruled photon vertex inverts the larger.
2. **Strand reflection reverses the letter order.** `P: σ_i ↦ σ_{n−2−i}` sends
   `σ_iσ_{i+1}⁻¹` to `σ_{j+1}σ_j⁻¹`, a cyclic rotation of the ι image. The Markov trace at
   `z_D` is invariant under `P`: checked exactly on every bond word below
   (`he4_sign_conventions_probe.py`, check `reflection_invariance`). Not proved in Lean.
3. **The Markov property is one-sided.** `tr(xσ_m) = z·tr(x)` holds at the top generator, and the
   brane tower adds strands at the top (`ordering-jet-compatibility`: `ℓ_n` extends `≺_n`
   without changing old elements).

So **bond chirality, bond side and strand reflection are one convention**: the letter order.
Fixing it, and reading the photon ruling as "invert the larger letter", fixes the chirality.
Requiring that a bond added with a new nucleon use only generators at or above the
interface (fact 3) fixes the side: the bond enters the newer nucleon. That is the production
placement. This last step is a reading of the tower principle, not a theorem.

## 2. The ⁴He chain under each convention

Exact, proton pin, `z_D`; `he4_sign_conventions_probe.py`. The production row is the first.

| chirality | side | order | B chain (keV) |
|---|---|---|---|
| ruled `σσ⁻¹` | left (enters newer nucleon) | ppnn | −0.862 |
| ruled | left | nnpp | −1.032 |
| ruled | right (enters older nucleon) | ppnn | +16.020 |
| ruled | right | nnpp | +17.154 |
| ι image `σ⁻¹σ` | left | ppnn | +3.642 |
| ι image | left | nnpp | +3.778 |
| ι image | right | ppnn | −16.618 |
| ι image | right | nnpp | −18.102 |

The sign is the product of chirality and side. The p/n labels do not flip it. Observed:
+28.3 MeV. Even the binding rows are three orders of magnitude short.

## 3. All live sign issues

Read from `main`, the sibling branches and PRs named. "Measured" = probe or Lean; the rest is
stated in the source and was not re-checked here.

| # | quantity | sign now vs observed | turns on | fixed by the corpus? | source |
|---|---|---|---|---|---|
| A1 | m_n − m_p, any increasing trace→mass map | n lighter, wrong (measured, Lean) | p/n label; map | open | PR #8800, `NeutronHeavierSign.lean` |
| A2 | single flip K→K⁻¹ or u = e₂ | swaps n, p (proved) | p/n label | each single flip excluded; both together invariant | #8800 R5/R6 |
| A3 | coloured strands, u↔d mirror | n = p, Q_β = 0 | colour; knot assignment | open, owner call | #8800 O2/O3 |
| A4 | every E_n − E_p, PR #8804 §29–§40 | flips under p↔n | which bit is u | **reconciled in PR #8800 §21** (not re-checked here): reversing the letter order also flips the Markov weight, so u is the K = q vector in either order, given the definition "u passes over" | `LITERATURE-COMPARISON.md` §40; #8800 §21 |
| A5 | 𝒟² arm of m_n − m_p | +0.171 MeV, sign from ε³ term | A4 | open | §40 |
| A6 | α·S EM term | −2.30 MeV, QED sign | A4; c_q² reading | S sign ruled (ℒ ⊃ −α·S) | §41–§45 |
| B1 | Q_β and lepton pair, one-sided reading | one is negative for any monotone map | trace→energy map | **closed (b)**, `monotone_excluded` | `2026-11-21-qbeta-np-error-budget.md` |
| B2 | Q_β = \|ε\|·E₀ | sign put in by \|·\| | absolute value | not derived | #8800 R9 |
| C1 | hydrogen bond asymmetry S | sign = chirality × side | letter order (§1) | open in #8804; §1 here fixes it given the photon ruling | §42–§43 |
| C2 | capture braid S | ∓h²[3]_q/q², placements mirror | side | cancels between placements (Lean, unmerged) | §43, §46 |
| C3 | α_em functional | sign = extremal vs mixed sectors | ι | open | `2026-11-21-alpha-em-which-form-is-canonical.md` §13 |
| C4 | ⁴He, ²H, ³H, ³He on the γγ bond | all unbind (−0.86 keV chain, about −1.6 keV all pairs) | letter order (§1, §2) | production placement is the tower reading | this branch |
| C5 | Δ_pp mirror split ³H/³He | two carriers give opposite signs of log(1−h) | bond writhe | open, bean `qou-fi1p` | bean |
| E1 | Mayer b₃ | b₃ < 0 for every bond triple in (0,1) | needs a pn bond above 1 | **closed (b)** for bonds in (0,1) | `UrsellPartitionFunctionB3` |
| E2 | fusion Q (D+T) | −0.3 vs +17.6 MeV | follows C4, E1 | open | scorecard |
| F1 | GMO, Σ isospin split | sign follows u, d, s order | flavour order | order not derived | #8957 |

Not sign issues but they rescale MeV rows: the c_q² reading (bean `qou-91w7`, a factor 82.68)
and the −12 m_e coefficient.

## 4. Overlaps

- **One letter order (rows C1, C2, C3, C4, C5).** Chirality, side and reflection are the same
  choice by §1. The ι map that separates the two α_em sectors (C3) is the same map that
  separates the two bond chiralities. With the photon ruling read as "invert the larger letter"
  and the tower reading for the side, all five are fixed together. Hypothesis, untested: the
  flavour order F1 is the same letter order on more strands.
- **One p/n bit (rows A1–A6).** A single bit decides every n − p sign. The corpus contradicts
  itself on whether it is derived (A4). PR #8800 §21 reports (exact sympy) that the order of the basis
  vectors e₁, e₂ of V is the same choice as the letter order on the Hecke side, so the p/n bit
  joins the letter-order group. The remaining input is the definition "u passes over".
- **One map (rows A1, B1, B2).** Wherever a sign enters through \|·\| or a monotone map, two
  proved obstructions apply.
- **Downstream (rows E1, E2).** These follow from C4 and close only when a bond binds.

## 5. What would settle it

1. Prove `P`-invariance of `towerTr` in Lean (fact 2). Cheap.
2. Decide whether the photon ruling `σ₀σ₁⁻¹` is meant as "invert the larger letter". If yes,
   C1 and C4 are fixed and the ⁴He chain unbinds by −0.862 keV.
3. A4 is reconciled by PR #8800 §21, modulo the definition "u passes over".
4. Test the flavour-order hypothesis in §4 (F1) the same way.
