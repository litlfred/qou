# Φ_8 universality across all 10 pair-differences — PROTON-CONDITIONAL (2026-06-01)

> Tests whether the universal M_first_Φ_8 = 7 boundary (PR #1625
> Tracks 1 + 2) extends from the 3 atomic-step pairs to all 10
> pair-differences among {p, n, D, ³He, ⁴He}.
>
> Branch: `claude/qbeta-habiro-phi8-interference-2026-06-01` (PR #1625).
> Probe: [`computations/qbeta/qbeta_habiro_all_10_pairs_phi8_universality.py`](../../computations/qbeta/qbeta_habiro_all_10_pairs_phi8_universality.py)
> Witness: [`computations/qbeta/qbeta-habiro-all-10-pairs-phi8-universality.witness.json`](../../computations/qbeta/qbeta-habiro-all-10-pairs-phi8-universality.witness.json)

## TL;DR

**The M_first_Φ_8 = 7 universal cancellation is PROTON-CONDITIONAL.**

| Pair | Contains p? | M_first_Φ_8 |
|---|---|---|
| n − p | ✓ | **None** (no Φ_8 in partial sums) |
| D − p | ✓ | **None** |
| ³He − p | ✓ | **None** |
| ⁴He − p | ✓ | **None** |
| D − n | ✗ | **7** ✓ |
| ³He − n | ✗ | **7** ✓ |
| ³He − D | ✗ | **7** ✓ |
| ⁴He − n | ✗ | **7** ✓ |
| ⁴He − D | ✗ | **7** ✓ |
| ⁴He − ³He | ✗ | **7** ✓ |

**Pattern:** `M_first_Φ_8 = 7 ⟺ proton ∉ pair`. The proton acts as a structural "absorber" of the Φ_8 cancellation — pairs containing p never pick up Φ_8 in their partial sums.

The 6 non-p pairs all show M_first_Φ_8 = 7, validating the level-2 SU(2) Wenzl framework for those.

## The proton asymmetry

The 4 p-containing pairs share a structural feature: in PR #1579's Δa_m factorization of (n − p), we proved `Δa_7 = Δa_8 = 0` — proton and neutron share their top-two Habiro coefficients exactly. **This Δa_7 = 0 vanishing is what suppresses Φ_8 in (n−p) partial sums** (the M=7 marginal contribution is `Δa_7·(u;u)_7 = 0·(u;u)_7 = 0`, so no cancellation force at M=7).

For (D−p), (³He−p), (⁴He−p), the marginal `Δa_7·(u;u)_7` is generically non-zero, yet still no Φ_8 emerges. This is a stronger statement: the cancellation `S_6(ζ_8) + Δa_7(ζ_8)·8 = 0` that works for non-p pairs **does NOT hold** when p is one of the pair members.

## Two interpretations

**Interpretation 1 — Proton is "calibration anchor"**: The proton canonical braid `β_p` may be the reference against which the y_λ · χ_λ Wenzl decomposition is normalised. Differences against p would then carry the un-cancelled normalisation residue rather than the Wenzl-annihilator-forced cancellation. This is consistent with `_PROTON_G0`, `_PROTON_G1` being the FIRST chain in `hecke_core.py` and the proton mass being CAL-1's anchor (electron mass) under the substrate-identity formula.

**Interpretation 2 — Proton braid has special Wenzl block content**: `β_p` may live entirely in a Wenzl-surviving block (first-column ≤ 3) at q = ζ_8, so the Wenzl annihilator constraint vanishes trivially on `tr_M(β_p)`. The constraint then doesn't propagate to (X − p) differences for any X.

The Hecke eigenvalue spectrum probe (in-flight) should distinguish these.

## Connection to (n − p) isospin Φ_1·Φ_2 prefactor

The (n − p) Habiro element factors as `−u^15·(u−1)(u+1)·P_8` per PR #1579 — with `(u−1)(u+1) = Φ_1·Φ_2` the isospin classical-limit kill. This is a DIFFERENT cyclotomic from Φ_8:

| Pair signature | Cyclotomic | Mechanism |
|---|---|---|
| n − p (isospin doublet) | `Φ_1·Φ_2 = u² − 1` | Classical-limit kill (q=1 vanishing) |
| Atomic-step (no p) | `Φ_8 = u^4 + 1` (at M=7) | Wenzl annihilator at q^4 = −1 |

The two prefactors are orthogonal: n−p shows Φ_1·Φ_2 but NOT Φ_8; D−n shows Φ_8 but NOT Φ_1·Φ_2 (in its Σ_m Δa_m·(u;u)_m form). The proton-containing pairs show NEITHER (no Wenzl-cancellation, no classical-limit-kill at the partial-sum level).

## Implications for the keystone Q_β Habiro element

If interpretation 1 holds (proton is calibration anchor), then the canonical Q_β Habiro element formula should express:

   `Q_β-Habiro(X) = (Wenzl factor) · (pair-specific Δ from p, n)`

where the "pair-specific Δ from p" is the un-cancelled residue and the Wenzl factor encodes the level-2 SU(2) annihilator. This is consistent with the calibration-discipline framing of CAL-1 (m_e via proton substrate identity) + CAL-2 (Q_β via neutron β-decay) + CAL-3 (m_π pion).

## Open follow-up

The Hecke eigenvalue spectrum at ζ_8 (a parallel probe, [`afb17bcb...`](https://github.com/litlfred/qou/pull/1625) — agent truncated, needs retry) would directly test interpretation 2 (does β_p land in surviving Wenzl blocks?).

## Cross-references

- Universal M=7 boundary on atomic-step pairs: [Δa_m partial-sum scan](2026-06-01-qbeta-habiro-delta-am-partial-sum-scan.md)
- Level-2 SU(2) categorical witness: [ζ_8 categorical witness](2026-06-01-qbeta-habiro-zeta8-categorical-witness.md)
- Wenzl tower at higher ζ_n FALSIFIED: [Wenzl tower probe](2026-06-01-qbeta-habiro-wenzl-tower-zeta-n.md)
- n−p isospin signature `Φ_1·Φ_2`: [Δa_m factorization (PR #1579)](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
