# Q_β is derived, not fitted — the honest tier map of the ladder

**Date:** 2026-07-04
**Branch:** `claude/mu-p-tension-closure-uua4os`
**Probe:** [`docs/audits/scripts/qbeta_derived_ladder_tiers_probe.py`](scripts/qbeta_derived_ladder_tiers_probe.py) (self-contained, exit 0)
**Companion:** [`2026-07-04-c4-mu-p-tension-pin-dependence.md`](2026-07-04-c4-mu-p-tension-pin-dependence.md) (the m_p side — a fit that was dropped)

## Task

> "derive Q_β."

## Answer: it already **is** derived — cleanly, to 1.28 ppm, with no fit

Unlike the m_p `(1 + 46u⁴)…` Habiro tower (a CODATA fit, dropped in PR #3280),
the production Q_β ladder (`computations/derived_masses.py::q_beta_kashiwara_n2_mev`)
is built **entirely from derived or proved categorical objects**. Factored
into its tiers, at the proton-pinned q₀:

| step | tier | provenance | Q_β error |
|---|---|---|---|
| `Q_A = m_e·\|q²−2q−1\|(q+1)/(2q³)` | **derived** | `prop:neutron-qvalue-symbolic` (net Hecke-channel cancellation Δ(net)=h(h−2)/2) | +1677.6 ppm |
| `× cos(α − b·ℏ_q²/2)` | **derived** | c_1 = b = Hoefsmit b; α = (z−1)h/2, z = 1/(√q+1/√q) — Kashiwara crystal edge weight | +73.8 ppm |
| `× (1 − b²ℏ_q⁴) = (1 − u²)` | **PROVED** | c_2 = −1, `prop:q-beta-c-2-eq-neg-one-structural` | **+1.28 ppm** |

with `h = q−q⁻¹`, `ℏ_q = (q−1)/q`, `u = b·ℏ_q² ≈ 0.00852`. Each tier strictly
improves the prediction (1677 → 74 → 1.28 ppm), and the last factor is
*exactly* `(1 − u²)` — i.e. the **proved** `c_2 = −1`, not a fitted number
(verified in the probe: `(1−u²) = Q_N2/Q_N1` to 10⁻⁴⁰).

**Production correctly stops at the proved c_2.** There is no fit to remove.

## Why it still misses the L2 100× target — and why that is honest

The L2 target for Q_β is 7.8 ppb; the derived value is 1.28 ppm, a **~164×
miss**. But — and this is the key contrast with m_p — the miss is because
**the derivation stops at the proved c_2**, not because a fit was stripped.
The m_p 3/7→2/7 drop (PR #3280) removed a *fit* that had been masking the
true error; the Q_β 164× has always been the honest derived residual.

## The next order is the settled, gated frontier — not re-attempted here

Reaching below 1.28 ppm needs `c_3`. The corpus value `c_3 = −2 = J_Hopf(q=1)`
is a **near-match**, recovered to 3 ppm by the *proved* O(u₀²) bias-correction
identity ([`q-beta-c-k-leading-bias-correction-identity-proof`](../../content/quantum-observable-universe/mass-theory/q-beta-c-k-leading-bias-correction-identity-proof.md):
`ĉ_k^corr = c_k^alg − c_{k+2}^alg·u₀²`), **not** a clean derivation. It is the
**settled**, s5bb-gated frontier:

- 6-entry wire/un-wire flip-flop history in [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md);
- PR #1580 settled `c_3` as **non-wireable** to production;
- per the AGENTS.md anti-flip-flop and formalize-first disciplines, this
  probe does **not** re-open it. Deriving `c_3` from first principles is the
  same open Habiro-element / s5-so3 keystone (`beans s5bb`) as the mass-sector
  `c_4`.

## Verdict

Q_β is the **honest counterpoint to m_p**: a fully-derived observable whose
1.28 ppm accuracy comes from a proved base (`Q_A`) times a derived Kashiwara
edge (`c_1 = b`) times a proved structural coefficient (`c_2 = −1`). "Deriving
Q_β" further — below the proved-c_2 floor — is gated on the s5bb keystone and
must not be pursued via the refuted `c_3` fit classes.
