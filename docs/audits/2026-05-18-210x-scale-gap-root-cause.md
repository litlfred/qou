# 210× scale-gap root cause: `ρ_K · m_e` vs `E_0^(N=0)` are different scales

> **Status (2026-05-18, this branch):** investigates the 210× scale
> gap surfaced when `probe_neutron_gap_round2.py` adopted the
> non-tautological pattern `E_0 = m_p / |tr_M(p)|`. The gap is
> NOT a missing normalisation — it's a category-error between three
> distinct "energy scale" notions the framework uses, only one of
> which equals `m_p / |tr_M(p)|`.

## TL;DR

The setup:

| quantity | value | derivation |
|---|---|---|
| `tr_M(p, q_0)` (Habiro) | ≈ 1.065 | rational function in q evaluated at q_0 |
| `m_e / (q_0·(q_0-1))` (= E_0^(N=0)) | 4.186 MeV | substrate Planck-tick (CAL-1 + CAL-2) |
| `m_p / \|tr_M(p)\|` (= E_0_calibrated) | 880.8 MeV | divide m_p_CODATA by Habiro tr_M |
| `E_0_full` (Li_2^q tower) | 4.227 MeV | full brane-tower sum |

The 210× gap = 880.8 / 4.186 = 880.8 / 4.227 (essentially the same
since E_0^full / E_0^(N=0) ≈ 1.01x at q_0).

## What the production framework actually does

The production mass formula is **not** `m = |tr_M| · E_0` (single
constant). Per
[`atomic_mass_via_rho_k.py:363`](../../folio-assistant/computations/atomic_mass_via_rho_k.py):

```python
# M(K) = ρ_K · m_e · |tr_M(K)|
def rho_K_leading_order(Z, N, abs_tr_M):
    """ρ_K^{LO}(Z, N) = (Z·m_p + N·m_n) / (m_e·|tr_M(K)|)."""
    return (Z * M_P_MEV + N * M_N_MEV) / (M_E_MEV * abs_tr_M)
```

So:
- `M_pred(Z, N) = ρ_K · m_e · |tr_M|`
- `ρ_K` is a **per-atom** categorical-density factor
- At leading order this is tautological (`M_pred ≡ Z·m_p + N·m_n`)
- The framework's structural goal is **deriving ρ_K from substrate**,
  not calibrating a single E_0

For the proton specifically:

```
ρ_K^{LO}(1, 0) = m_p / (m_e · |tr_M(p)|)
               = 938.272 / (0.511 · 1.065)
               ≈ 1722.5

⇒ ρ_K · m_e = m_p / |tr_M(p)| ≈ 880.8 MeV
            = E_0_calibrated  ← what round-2 named E_0
```

So `E_0_calibrated = ρ_K^{LO} · m_e`, which is **(Z, N)-dependent**.
The categorical-mass-markov prop's narrative — `m = |tr_M| · E_0`
with "a single calibration constant E_0" — is **incomplete** as
stated; the actual framework needs ρ_K as the structural factor.

## Three distinct "energy scales" the framework uses

| name | formula | at q_0 | meaning |
|---|---|---|---|
| **`E_0^(N=0)`** | `m_e / (q_0·(q_0-1))` | 4.186 MeV | leading-order substrate Planck-tick (one brane unit; geometric series leading term) |
| **`E_0^full`** | `e_0_full_mev()` Li_2^q tower | 4.227 MeV | full brane-tower N→∞ sum; +1% over N=0 (NOT 210×) |
| **`ρ_K^{LO} · m_e`** | `(Z·m_p + N·m_n) / \|tr_M\|` | varies per atom | per-atom categorical-density × electron mass; FOR PROTON = 880.8 MeV |

The 210× ratio is between `E_0^(N=0)` (substrate Planck-tick) and
`ρ_K · m_e` (per-atom calibration). These are NOT the same thing
and were never supposed to be equal.

## Why the round-2 script's setup was misleading

`probe_neutron_gap_round2.py:96-100`:

```python
E0 = mp.mpf(str(M_P_MEV)) / mp.fabs(tr_p)
mp_pred = float(mp.fabs(tr_p) * E0)  # exact by construction
mn_pred = float(mp.fabs(tr_n) * E0)
```

The variable named `E0` here is **not** the substrate Planck-tick
`E_0^(N=0)`. It's actually `ρ_K^{LO}(1, 0) · m_e`, computed
specifically from the proton's CODATA mass and the Habiro tr_M(p).

Then using this `E0` for the **neutron** prediction:

```
mn_pred = |tr_M(n)| · (m_p / |tr_M(p)|)
        = m_p · |tr_M(n)| / |tr_M(p)|
```

This is **NOT** an independent neutron prediction — it's a ratio
prediction that bakes in m_p_CODATA as a CAL anchor. The "single-
point calibration" framing hides the fact that the proton ρ_K is
being used to define a per-particle "E_0" that doesn't generalize.

## What was hidden by the tautology

The old script form `E_0 = m_p / |tr_M(p)|` followed immediately by
`m_p_pred = |tr_M(p)| · E_0` gave `m_p_pred ≡ m_p` exactly. This
hides the 210× scale gap by absorbing it into the calibration
step. The CORRECT setup surfaces this:

- If you ask "what's the substrate-derived energy unit?" → 4.186 MeV
- If you ask "what's the calibrated mass-per-tr_M unit for the
  proton?" → 880.8 MeV
- These are different by 210× because **the Habiro `|tr_M|`
  computes a dimensionless Markov-trace value, not a mass-shaped
  quantity**

## Why `E_0^full` doesn't close the gap either

`derived_masses.e_0_full_mev()` computes the brane-tower-summed
Planck-tick — the Li_2^q sum is the geometric extension of
E_0^(N=0):

```
E_0^full = e_0_n0 · (1 + ℏ_q² · G + …)
```

At q_0: `E_0^full / E_0^(N=0) ≈ 1.01x` (the +1% the docstring
comments document). The tower amplification is ~1%, not 210×. So
the gap is NOT in the brane-tower truncation.

The gap lives in the **`ρ_K` factor**, which is per-atom and is
the structural object the framework derives — not a free calibration.

## How PR #708 (Borromean tower) addresses this

Per the [v6-refreshed workplan](2026-05-18-1ppb-workplan-v6-refreshed.md):

> **Borromean tower formula closes the m_p 1700× scale gap to 0.25 ppm**
> (commit `dc3a85500`).

The Borromean tower derivation **provides a substrate formula for
ρ_K at the proton** (or equivalently, for m_p in terms of m_e and
q_0 alone). When that closes, the proton ρ_K is no longer a free
parameter calibrated against m_p_CODATA — it's predicted from
substrate. At that point the 210× gap is no longer a gap because
`ρ_K · m_e ≈ 880.8 MeV` becomes a derivation result, not a calibration.

The "1700×" in #708's gap-closure refers to a different baseline
(`m_e` vs `m_p`, i.e. 938.272 / 0.511 ≈ 1836). The 210× I see here
is the same family of structural gap (per-atom ρ_K factor vs
substrate Planck-tick).

## The fix for the rewire pattern

For scripts in Bucket D (`probe_neutron_gap_round2`, round 3-5,
`d_from_scratch`, etc.) that pair Habiro `|tr_M|` with an energy
scale, **stop calling `m_p / |tr_M(p)|` an "E_0"**. The correct
pattern is:

### Wrong (the round-2 pattern)
```python
E0 = m_p / |tr_M(p)|          # actually ρ_K^{LO}(1,0) · m_e, not E_0
mp_pred = |tr_M(p)| · E0       # tautology
mn_pred = |tr_M(n)| · E0       # = m_p · tr_n / tr_p — not independent
```

### Correct (per the production framework)
```python
from atomic_mass_via_rho_k import predict_mass
M_pred_p, rho_K_p = predict_mass(1, 0, abs(tr_p))
M_pred_n, rho_K_n = predict_mass(0, 1, abs(tr_n))
# At LO: M_pred_p = m_p, M_pred_n = m_n — tautological by design.
# The structural prediction is *the ρ_K values*, not the M_pred values.
```

### For substrate-anchored predictions (the v6 goal)
```python
# Substitute ρ_K with a substrate-derived form.
# Per PR #708's Borromean tower:
rho_K_p_substrate = borromean_tower_rho_K(1, 0, q_0)  # from substrate
M_pred_p_substrate = rho_K_p_substrate · m_e · abs(tr_p)
err = (M_pred_p_substrate - m_p_CODATA) / m_p_CODATA
# This is the HONEST residual the framework needs to drive to 1ppb.
```

## Files modified

- [`docs/audits/2026-05-18-210x-scale-gap-root-cause.md`](2026-05-18-210x-scale-gap-root-cause.md)
  (this file)

## Cross-references

- [`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md)
- [`prop:atomic-mass-via-rho-k`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-via-rho-k.md)
- [`derived_masses.py`](../../folio-assistant/computations/derived_masses.py)
  `e_0_n0_mev`, `e_0_full_mev` definitions
- [`atomic_mass_via_rho_k.py`](../../folio-assistant/computations/atomic_mass_via_rho_k.py)
  `rho_K_leading_order` + `predict_mass`
- [`probe_neutron_gap_round2.py`](../../folio-assistant/computations/probe_neutron_gap_round2.py)
  the tautological setup that surfaces the gap
- [`2026-05-18-1ppb-workplan-v6-refreshed.md`](2026-05-18-1ppb-workplan-v6-refreshed.md)
  (sibling: m_p closure via Borromean tower)
