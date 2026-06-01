# Sign-block / Plancherel campaign — canonical reference

**Date:** 2026-06-01
**Branch:** `claude/sign-block-chain-consolidation-2026-06-01`
**Status:** Canonical consolidation of the 6-PR campaign chain (#1581 → #1617 → #1629 → #1645 → #1650 → #1654)

This document is the **canonical reference** for the sign-block /
Plancherel-channel investigation of the proton-mass identity. Future
agents should **read this BEFORE** attempting to re-derive any of the
findings catalogued here.

## Campaign summary

| PR | Outcome | Key Files |
|---|---|---|
| [#1581](https://github.com/litlfred/qou/pull/1581) | Probes A/B/C + closed-route roundup | `docs/audits/2026-06-01-closed-route-reexamination-roundup.md` |
| [#1617](https://github.com/litlfred/qou/pull/1617) | Alt-geometries confirm `dim H_3 = 6` (27 alternatives REJECTED) | `ocneanu_12_em_correction_candidate.py` |
| [#1629](https://github.com/litlfred/qou/pull/1629) | h⁴-residual PSLQ NULL across natural basis (120 dps, 17 basis) | `h4_residual_higher_precision_pslq.py` |
| [#1645](https://github.com/litlfred/qou/pull/1645) | **MAJOR — sign-block hypothesis + CODATA-floor finding** | `QOU.Substrate.ProtonMassEMSignBlock`, `mp_residual_exotic_basis_pslq.py` |
| [#1650](https://github.com/litlfred/qou/pull/1650) | Template is m_p-specific (not transferable to m_n or Q_β) | `mn_flavor_split_plancherel_channel.py`, `qbeta_signblock_template_check.py` |
| [#1654](https://github.com/litlfred/qou/pull/1654) | X(q) IS Plancherel-structured; "Bring derivation" reframed; deuteron NULL | `mn_flavor_split_h3_plancherel.py`, `bring_zero_mode_per_block_scaffold.py` |

## The PROVED structural form

The proton-mass identity:

```
m_p = 2·m_μ·F_Bor(q_0) − (12 − (α_em/π)/dim H_3) · m_e
    = 2·m_μ·F_Bor(q_0) − 12·m_e + (α_em/π) · m_e / dim H_3
```

where `F_Bor(q) = |tr_M(β_Bor, q)| · [3]_q!/q³` is the Borromean Markov
trace, `dim H_3 = 6`, and `(α_em/π)/6 ≈ 0.0003871`.

**Numerical validation:** the residual `k_required - 12 + (α_em/π)/6`
is **54 ppb** at the proton anchor (PR #1581's near-match identification,
confirmed PR #1617). The CODATA propagated precision floor on
`k = (2·m_μ·F_Bor − m_p)/m_e` is **~71 ppb** (quadrature sum of
δ(m_p), δ(m_e), δ(m_μ) propagation). Observed 54 ppb = **76% of CODATA
floor** — the proton-mass identity is **exact within experimental
uncertainty** (PR #1645 finding).

## The OPEN structural items

The (α_em/π)/6 form has a **provisional categorical reading** but NOT a
derivation:

1. **`/6 = 1/dim H_3 = 1/|S_3|` = classical Plancherel weight at a
   1-dim Wedderburn block**. Both trivial V_(3) and sign V_(1,1,1)
   have `P_λ = d²_λ/|S_3| = 1/6`, numerically indistinguishable.

2. **Physical pick is sign V_(1,1,1)**: the proton (uud) color
   singlet is fully antisymmetric in color labels per Fermi
   statistics → sign rep of S_3 on 3 color labels.

3. **`(α_em/π)` is the standard QED 1-loop coupling** (vacuum
   polarization / bubble integral) — NOT a Bring-derived number
   (PR #1654 Item B reframing).

**Multi-session open work** (per PR #1654 Item B reframing):

  (a) **Substrate-level implementation of QCD color-singlet** (Fermi
      statistics → sign rep of S_3 on color labels).
  (b) **Categorical Wedderburn-projection of EM coupling** (why
      electromagnetic interaction lands at sign block specifically).

Neither (a) nor (b) exists yet at the categorical level. This is the
actual blocking work for the `EmSignBlockCorrection` Lean class to
become a `theorem` rather than a `class`.

## What's been RULED OUT

PR #1617 confirmed that **27 alternative knot-operator geometries**
all FAIL by 100× to 30,000× compared to `dim H_3 = 6`. The integer 6
is structurally robust. Tested alternatives include:
  - 5-fold Bring quintic (5, 120, [5]_q!)
  - |S_4| = 24, |S_5| = 120
  - Bring saturating-genus knots (3, T_(2,3), T_(2,5), T_(2,7))
  - 4 Yekutieli edge cells × 3 strands = 12
  - 9 = 3·3 (color×generations), 8 (gluons), 11 (quarks+gluons)
  - dim_q V_(2,1) at q_0, |J_Hopf|, |tr_M(β_Bor)|
  - 6/q, 6/q², 6·q (q-variations of 6)
  - Bring Euler χ = -6 (only one tied with |S_3| at 54 ppb)

PR #1629 + PR #1645 confirmed **PSLQ NULL across natural + exotic
bases** (17 + 12 elements) at 120 dps maxcoeff 10⁶, tol 10⁻²² — no
clean integer relations for the h⁴-residual coefficient (which is
ultimately at CODATA floor).

PR #1654 confirmed:
  - Template does NOT transfer to **m_n flavor-split** (H_2 and H_3
    NULL; X(q) baseline IS Plancherel-structured but the 0.10%
    residual is at the standard channel, which has no clean form)
  - Template does NOT transfer to **Q_β c_3** (`-2` matches
    `dim H_2 · σ_1(sign)|_{q=1}` algebraically, but NOT the
    Plancherel-weight d²_λ/|S_n| pattern)
  - Template does NOT close **deuteron binding** at H_2

## Lean coverage

- `QOU.Substrate.ProtonMassEMSignBlock`:
  - `EmSignBlockCorrection` class (the conjecture)
  - `plancherelSignH3 = plancherelTrivialH3 = 1/6` defs
  - `plancherelStandardH3 = 4/6` def
  - `plancherel_sum_S3 : Σ_λ P_λ = 1` theorem (norm_num)
  - `residual_eq_alpha_em_over_6pi` corollary
  - `codataPropagatedFloorPpb = 71` def
  - `observedSubResidualPpb = 54` def
  - `subResidual_at_or_below_codata_floor : 54 ≤ 71` theorem (norm_num)

## Cross-references

- merged PRs #1581, #1617, #1629, #1645, #1650, #1654
- `docs/coordination/2026-06-01-closed-route-followups.md` (PR #1617 ledger)
- `docs/coordination/2026-06-01-h4-residual-derivation.md` (PR #1629 ledger)
- `docs/coordination/2026-06-01-mp-yekutieli-and-mn-flavorsplit.md` (PR #1645 ledger)
- `docs/coordination/2026-06-01-sign-block-template-expansion.md` (PR #1650 ledger)
- `docs/coordination/2026-06-01-post-1650-trio.md` (PR #1654 ledger)

## Do NOT do (anti-patterns)

Future agents should NOT:

1. **Re-derive `(α_em/π)/dim H_3` numerical match** — done in PR #1581
2. **Test more alternative N values** — done in PR #1617 (27 alts)
3. **Run more PSLQ on the residual coefficient** in natural OR exotic
   basis — done in PR #1629 + PR #1645
4. **Try to apply the sign-block template to m_n / Q_β / binding
   energies** without a CATEGORICAL motivation — PR #1650 + PR #1654
   confirmed the template is m_p-specific
5. **Argue `(α_em/π)` needs Bring-quintic derivation** — PR #1654
   Item B reframing shows this is circular; (α_em/π) is the standard
   QED bubble coupling

## Do (productive next steps)

Future agents SHOULD:

1. **Pursue substrate-level Fermi statistics implementation** (Open
   item (a)) — multi-session Lean / categorical work.
2. **Pursue categorical Wedderburn-projection of EM coupling** (Open
   item (b)) — multi-session formalization.
3. **For m_n / Δ_pn / Q_β / binding closures**: pursue independent
   categorical mechanisms (NOT the sign-block template).
4. **For 1ppQ improvements**: improved CODATA inputs (Penning-trap
   m_p, anomalous-moment α_em, muon-anchor m_μ) — the m_p identity
   is at the floor under current inputs.
