---
# qou-37y0
title: 'GAP: m_d - m_u extraction claimed ''no new inputs'' — needs the underived EM coupling k, and does not cite the existing substrate split'
status: in-progress
pr: 8185
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-08-08T08:11:57Z
updated_at: 2026-10-10T07:15:51Z
parent: qou-8lxd
---

Surfaced 2026-08-08 while surveying the new `eightfold-way/` +
`appendix-standard-model/` chapters (landed `e1d58ced`, 2026-08-07) for L2
attack vectors. Recorded as a **caution on a proposed programme**, not a
refutation of anything wired — the block wires nothing.

## The claim

[`appendix-standard-model/sm-params-quark-masses.md`](../folio/quantum-observable-universe/appendix-standard-model/sm-params-quark-masses.md)
reframes the six quark masses as scheme quantities of the observer's inversion
procedure rather than numbers the framework owes, and argues that the cleanest
extractable one is the isospin difference `m_d − m_u`:

> "its experimental source is the neutron–proton splitting Δ_pn after removing
> the electromagnetic self-energy, and the framework derives both Δ_pn *and* its
> own electromagnetic–strong decomposition […] so an extraction of '`m_d − m_u`
> in the framework scheme' is well-posed **with no new inputs**."

The reframing is good and the `m_u + m_d` circularity it flags (source is
`m_π²`, and `m_π` is CAL-3) is correct and worth keeping. The **"no new
inputs"** clause is what does not hold up.

## Two problems

**1. The EM subtraction needs a coupling the corpus does not derive.**
[`docs/audits/2026-07-11-np-splitting-L2-em-sign-prune.md`](../docs/audits/2026-07-11-np-splitting-L2-em-sign-prune.md)
derives the EM self-energy **sign** parameter-free from the pairwise Coulomb
charge structure (`Σqq(p) − Σqq(n) = +1/3 > 0` ⇒ EM makes the proton heavier ⇒
the correction to `Δm` is negative). But that audit is explicit that the
magnitude is *not* derived:

> "The EM coupling `k` is not derived from the 13 categorical drivers, so
> **nothing is wired into production** (anti-laundering rule)."

and that magnitude alone cannot even separate EM from a q-term
(`|r−1| = 0.634%`, `α_EM = 0.730%`, but `ℏ_q² = 0.982%` is the same size). So
"remove the electromagnetic self-energy" currently requires `k`, which is a new
input. Doing the subtraction with a `k` back-solved from `Δ_pn` would be a fit —
exactly what the Δ_λ "no seventh fit-based ansatz" and anti-laundering rules
forbid.

**2. The block does not cite the substrate split the corpus already has.**
Two existing blocks already derive isospin-splitting content from `q₀`:

- [`observations/flavor-split-substrate.md`](../folio/quantum-observable-universe/observations/flavor-split-substrate.md)
  — `(m_n − m_p)/M_N ≈ (q−1)²(1−q⁻⁴)/3 = ℏ_q²·h_q·[2]_q`, depending only on
  `q₀` and `M_N`, matching CODATA to **−0.10 %**.
- [`mass-theory/flavor-dressed-mass-from-substrate-split.md`](../folio/quantum-observable-universe/mass-theory/flavor-dressed-mass-from-substrate-split.md)
  — recovers the dressed difference `μ_d − μ_u ≈ 1.288 MeV` as a derived
  consequence; [`observations/terminal-resolution-proof.md`](../folio/quantum-observable-universe/observations/terminal-resolution-proof.md)
  reports `μ_u ≈ 311.10`, `μ_d ≈ 312.39 MeV` with a **−0.53 %** residual on
  `m_n − m_p`.

`sm-params-quark-masses.md` gestures at "a constituent-level density […] exists
at the baryon level" but names none of these, so the appendix now proposes a
second, uncoordinated route into the same isospin-splitting structure.

**Nuance to preserve:** dressed/constituent `μ_d − μ_u` is **not** the same
object as current-quark `m_d − m_u`, so this is a coordination gap, not a
duplicate derivation. That distinction is precisely what the block should state
and currently does not.

## What would close this

1. Amend `sm-params-quark-masses.md` to (a) drop or qualify "no new inputs",
   naming `k` as the missing input and citing the EM-sign prune, and (b) cite
   the two substrate-split blocks, stating explicitly how current-quark
   `m_d − m_u` relates to (or differs from) the derived dressed
   `μ_d − μ_u ≈ 1.288 MeV`.
2. *Or*, if the extraction really is input-free, derive `k` from the categorical
   `α_EM = [2]_q·(1 − h²α)` (PR #1511) and show `−k·(1/3)` reproduces the
   `−0.634 %` residual — the charge-odd scan the EM-sign audit names as the
   productive next step. That would be a genuine result, and it would also
   discharge this bean.

## Explicitly NOT claimed

No L2 movement either way. Production `Δ_pn` is dashboard Path C (`Q_β + m_e`)
and its L2 gap is **Q_β-driven**, not EM — see
[`2026-07-11-trio-shared-root-qbeta-bottleneck.md`](../docs/audits/2026-07-11-trio-shared-root-qbeta-bottleneck.md).
This bean is about the honesty of a programme statement, not about closing a
precision target.

## Progress Update (Round 55 — PR #8185)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity advisories across all 6 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ColourConjugationGMODeviationAndAsymmetry.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/colour_conjugation_gmo_deviation_and_asymmetry_probe.py` and 2-commit stamped witness `computations/probes/colour-conjugation-gmo-deviation-and-asymmetry.witness.json` (`scriptCommitSha: dc490df3193b70802e4608a98cc9402380f4dbcd`, `HEAD: ea791bb906663eb37105b3486abd6e07818699ed`).
- [x] Opened `litlfred/qou#8185` (status kept at `in-progress` per no-unilateral-closure policy).
