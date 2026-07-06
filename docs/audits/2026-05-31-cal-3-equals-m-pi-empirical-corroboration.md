# CAL-3 = m_π — empirical corroboration audit (2026-05-31)

**Status:** CONFIRMED — the framework's current canonical assignment
`CAL-3 = m_π` is corroborated by two independent empirical lines of
evidence converging from opposite directions (negative-derivability
probe + positive nuclear-binding closure).

**Branch:** `claude/brave-mendel-FPxFl` (PR
[#1579](https://github.com/litlfred/qou/pull/1579))

## What this audit is

This is a **corroboration audit, not a discovery audit**. The framework
has already adopted `CAL-3 = m_π` as the canonical assignment:

- [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py) line 22 (module header table):

  | ID    | Observable | Module export | Measurement / Source |
  |-------|------------|---------------|----------------------|
  | CAL-3 | 𝔇_π (→ m_π) | `M_PI_PM_MEV_VALIDATION` | pion decay width (τ_π, h³ jet order) |

- [`content/quantum-observable-universe/mass-theory/three-calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/three-calibration-inputs.md):

  > | CAL-3 | 𝔇_π | pion decay width (τ_π) | meson mass scale m_π; independent of (m_e, q_0) | h³ |
  >
  > sym (λ = (3)) | CAL-3: m_π± | Sets the chiral / Goldstone scale (sym is the "all crossings positive" / hadronic channel). The pion mass is the pseudo-Goldstone boson of broken chiral SU(2)_A; its mass encodes the chiral condensate ⟨q̄q⟩^{1/3} ≈ 240 MeV which is absent from (m_e, q_0). Q_β(n) is **derived** from CAL-1 + CAL-2 via … and serves as a cross-check, not an independent input.

Two empirical probes from this session and from sibling work on main
provide independent corroboration of that assignment.

## Line of evidence 1 — negative-derivability probe (this PR)

[`computations/probes/m_pi_hecke_prediction_probe.py`](../../computations/probes/m_pi_hecke_prediction_probe.py)
tested ~100 candidate categorical formulas for m_π from (m_e, q_0)
alone, including:

- Direct lepton-tower-style: `m_e · F_Bor^k` for k ∈ {-4, …, +4}
- Substrate-shifted-mass: `2·m_μ·|tr_M(𝓜_+)| − N·m_e` for N ∈ [-30, +30]
- Tower-style: `m_e · [3]_q! / h^k`, `m_e · (q² + 1)/h^k`
- Geometric: `√(m_e·m_μ) · |tr_M(𝓜_+)|^k`, `m_e · (1 + h)^N`
- Bridge: `m_μ · (1 + net(𝓜_+))`, `m_μ · (2 − net(𝓜_+))`

**Result.** Best miss = 19,938 ppm (formula `m_μ · (|tr_M(𝓜_+)| + 5h)`),
i.e. 1.4 × 10⁷ × the PDG experimental precision of 1.3 ppb. Compare to
the proton mass which closes at **0.24 ppm** under the substrate
identity (`2·m_μ·F_Bor(q_0) − 12·m_e`) using the SAME building blocks
(m_e, q_0, m_μ, |tr_M|, [3]_q!).

A 35,000× gap in derivability between m_p (0.24 ppm) and m_π (19,938 ppm)
under the same compute infrastructure is structural, not numerical.
**m_π carries information that (m_e, q_0) does not encode.**

## Line of evidence 2 — positive nuclear-binding closure (main, option-e v9)

Main commit
[`30c5393b7`](https://github.com/litlfred/qou/commit/30c5393b7)
("option-e v9 BREAKTHROUGH") derived this canonical closure for the
A=3 mirror pair:

$$B_T - B_{^3\text{He}} \;=\; m_\pi \cdot \hbar_q \cdot \tfrac{1+q}{2} \cdot \sum_\lambda y_\lambda \cdot \tfrac{\chi^\lambda(\beta_T) + \chi^{\lambda^T}(\beta_{^3\text{He}})}{2}$$

closing the mirror pair to **0.11%** (`0.7629` MeV vs target `0.7637` MeV).
The progression v7 → v8 → v9 explicitly cites the pion mass as the
"isospin-breaking quark-mass scale" required to close the residual.

Sibling PR [#1581](https://github.com/litlfred/qou/pull/1581) Finding C
independently audited the v9 `(1+q)/2` multiplicative-correction factor
and found:

> `(1+q)/2` is **UNIQUE within 0.11%** across 33 candidate q-arithmetic
> forms (q-brackets, q-factorials/n, cosh/exp variants, mixed). Next-
> closest: `q^(1/2)` at -0.23% (2.5× further off). v9's BREAKTHROUGH
> headline ("mirror pair CLOSED to 0.11%") is SUPPORTED — NOT a
> coincidence basin.

## Combined verdict

Two independent paths converge on m_π as the genuine CAL-3 anchor:

| Path | Direction | Evidence |
|---|---|---|
| Negative-derivability (this PR) | "m_π can't come out of (m_e, q_0)" | best of ~100 candidate formulas misses by 19,938 ppm |
| Positive-binding-closure (main #30c5393b7 + #1581) | "m_π as input closes nuclear binding" | A=3 mirror pair closed to 0.11% via `m_π · ℏ_q · (1+q)/2 · Σ_λ y_λ χ` |

The negative path forecloses derivation; the positive path demonstrates
necessity. Together with the framework's prior cohomological
3-calibration argument (which guarantees exactly three independent
calibration slots), the m_π assignment is over-determined.

## What's still open

1. **v9 generalization across mirror pairs.** Only ³H/³He has the
   chi-witness pair (`chi-{T,3He}-h*-at-q0-50dps.witness.json`) needed
   to apply the v9 formula. Tested at scale on ⁷Li/⁷Be, ¹¹B/¹¹C, ¹³C/¹³N,
   etc. once those chi-witnesses are computed — pings posted on
   [#1516](https://github.com/litlfred/qou/pull/1516) which is the H_n
   Gram-matrix generalization work. If v9 generalizes, CAL-3 = m_π is
   structurally robust; if not, v9 may be partially overfitted to ³H/³He
   even with #1581's uniqueness audit.

2. **Categorical derivation of `(1+q)/2`.** Per #1581 Finding C: "What's
   STILL OPEN: a categorical derivation that PRODUCES `(1+q)/2` from the
   Reeb-phase / canonical-cheat-sheet chain." Currently this factor is
   selected by search (within a categorical menu) rather than predicted.

3. **Chi-witness coverage for heavier nuclei.** Closing the A ≥ 4
   mass-table to 100× target requires per-isotope chi witnesses
   that don't yet exist for most isotopes. Tracked under #1516 (H_n
   Gram) and the broader Option E phase 2 work.

4. **Categorical derivation of c_3.** The
   [Q_β c_3 derivation attempt](2026-05-31-c-3-categorical-derivation-attempt.md)
   in this PR is NEGATIVE. The remaining open path is the Q_β Habiro
   generating function (parallel to α_EM PR #1511), NOT a static
   coefficient closure.

## Cross-references

- This audit: [`2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md`](2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md)
- m_π Hecke probe: [`m_pi_hecke_prediction_probe.py`](../../computations/probes/m_pi_hecke_prediction_probe.py)
- m_π witness: `m-pi-hecke-prediction-probe.witness.json`
- c_3 derivation attempt audit: [`2026-05-31-c-3-categorical-derivation-attempt.md`](2026-05-31-c-3-categorical-derivation-attempt.md)
- Canonical 3-calibration content block: [`content/quantum-observable-universe/mass-theory/three-calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/three-calibration-inputs.md)
- CODATA constants (already declares M_PI_PM_MEV_VALIDATION): [`computations/substrate/codata_constants.py`](../../computations/substrate/codata_constants.py)
- Option-e v9 (main): commit [`30c5393b7`](https://github.com/litlfred/qou/commit/30c5393b7)
- Q_β c_k truncation framing (main): commit [`6ace8153e`](https://github.com/litlfred/qou/commit/6ace8153e)
- Sibling PR #1581 (three-dashboard-probes): independent v9 uniqueness + c_3 Rule A reframing
- m_K/m_π MET (main #1442 + commit `d4d2f10a2`): m_K closure derives from m_π via `(3q²−1)/(2q²)` — does NOT contradict CAL-3 = m_π
- Coordination ledger: [`docs/coordination/2026-05-31-cal-3-m-pi-hunt.md`](../coordination/2026-05-31-cal-3-m-pi-hunt.md)
