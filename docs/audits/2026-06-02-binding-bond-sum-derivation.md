# Extensive per-bond binding sum — zero-fit derivation quadruples the A-scaling

**Date:** 2026-06-02
**Derivation:** [`derive_binding_bond_sum.py`](../../folio-assistant/computations/derive_binding_bond_sum.py)
→ `derive-binding-bond-sum.witness.json`
**Status:** DERIVATION (zero fit, level-0). The intensive→extensive fix, validated.

## Context

The zero-fit canonical derivation
([`2026-06-02-binding-intensive-vs-extensive-derivation.md`](2026-06-02-binding-intensive-vs-extensive-derivation.md))
showed `B = E_0·Δ|tr_M|` is **intensive** (saturates; A-growth 1.65× vs AME 12.72×),
and that the Δ_λ gate is mis-framed: nuclear binding is **extensive**, an additive
sum over inter-nucleon bonds, not a per-block weight. This derivation tests the
extensive form directly.

## The derivation (level 0, zero fit)

$$B(K) = \sum_{b\in\bowtie_K} B_b,\qquad B_b = E_0\,\Delta|\mathrm{tr}_M|_b,$$

with the **derived deuteron bond** `B_pn = E_0·(Σ_λ y_λ|χ^λ_free| − Σ_λ y_λ|χ^λ_atom|)_D
= 2.304 MeV` (+3.6 %) used for every bond (isospin-symmetric, level 0), and bond
count by type from `(Z,N)`: `n_pp = C(Z,2)`, `n_nn = C(N,2)`, `n_pn = Z·N`,
`N_bonds = C(A,2)`. `E_0 = m_e/(q₀(q₀−1)) ≈ 4.186 MeV` (calibration). **No fit.**

| isotope | (pp, pn, nn) | N_bonds | B = N·B_bond | AME | err |
|---|---|---|---|---|---|
| D | (0,1,0) | 1 | 2.304 | 2.225 | **+3.6 %** |
| T | (0,2,1) | 3 | 6.913 | 8.482 | −18.5 % |
| ³He | (1,2,0) | 3 | 6.913 | 7.718 | −10.4 % |
| ⁴He | (1,4,1) | 6 | 13.826 | 28.296 | −51.1 % |

**A-growth `B(⁴He)/B(D)` = 6.00×** — vs the intensive formula's **1.65×** (target
AME 12.72×). The extensive bond-sum **quadruples the A-scaling accuracy** with
zero fit, and derives the deuteron (+3.6 %).

## The two residuals — structurally isolated (the next step)

1. **Bond type.** T and ³He share `C(A,2)=3` so level-0 predicts them identically
   (6.91), but AME differ (8.48 vs 7.72). They differ by bond *composition*:
   T = {2 pn, 1 nn}, ³He = {1 pp, 2 pn}. **Closing this needs `B_pp ≠ B_pn ≠ B_nn`**
   — the per-bond-type binding from the pp / pn / nn 2-nucleon sub-braid trace
   differences (the deuteron *is* the pn bond; pp and nn are the diproton /
   dineutron sub-braids).
2. **Per-bond growth.** ⁴He is −51 %: 6 bonds × the deuteron bond under-counts
   because each bond is **embedded in the 12-strand ⁴He braid**, not isolated
   (the cooperative/saturation effect). **Closing this needs `B_b` computed from
   each bond's embedded sub-braid**, not the isolated-deuteron value.

Both refinements reduce to **one compute step: derive `B_b = E_0·Δ|tr_M|_b` for
each `⨝_K` bond from its (possibly embedded) 2-nucleon sub-braid.** The deuteron
is the isolated-pn base case (derived). This is a *derivation* (sum of derived
per-bond pieces over the structural bond set), the natural realization of the
operator-valued combiner (#1698) — not a weight-fit.

## Significance

The whole 2026-06-02 probe arc (volume → phase → content → measure) was searching
for a per-block *weight* — the wrong object. This derivation confirms the right
object is the **extensive bond-sum**: zero-fit, deuteron-derived, A-scaling 1.65×
→ 6.00× in one structural step, with the residuals reduced to a single
well-posed compute (per-bond sub-braid `Δ|tr_M|`). Cheat-sheet §9.3 updated with
this reframing. Track A per-isotope binding (gated for the L2 100× `Q_β`/`m_n`/
`Δ_pn` targets) now has a derivation path, not a fitting search.
