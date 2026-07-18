# q* re-pinned with the extended k=31 D-ladder — a scope-(a) negative: the ladder does not sharpen q*

**Date:** 2026-07-18 · **Branch:** `claude/c3-qstar-k31-repin-2026-07-18` ·
**Probe:** [`computations/qbeta/qbeta_c3_qstar_k31_repin_probe.py`](../../computations/qbeta/qbeta_c3_qstar_k31_repin_probe.py)
· **Witness:** `computations/qbeta/qbeta-c3-qstar-k31-repin.witness.json`
· **Tier:** scope-(a) measurement; C14; no `c_k` wired; no fit; no tier change;
`q₀` stays CAL-2 calibrated (`q*` is a cross-check determination, not a new pin).

## Question

The decay-sector determination `q*` — the `S = 0` (`ε = 0`, pure bar-even)
point, the third leg of the μ-p-`Q_β` trio (capstone
[`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md))
— was root-found at **k ≤ 21-era** ladder precision
([`qbeta_c3_imq_qstar_ladder_amplification_probe.py`](../../computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py),
`q* ≈ 1.10997859303152`). Merged **#3821**
([`qbeta_dladder_extension_singularity_probe.py`](../../computations/qbeta/qbeta_dladder_extension_singularity_probe.py))
extended the exact ℚ(√3) bar-odd D-ladder to **k = 31**. Does the extra ladder
data sharpen `q*` and its experimental sensitivity `dq*/dQ_β`?

## The two objects, kept distinct

The capstone records the schematic decomposition `S = h·D(u)`, `h = q − 1/q` the
anchor-blind bar-odd carrier. The exact bar-odd carrier is
`O(q) = h(q)·Σ_k d_k ũ(q)^k`, `ũ = q·b·ℏ_q²` the bar-even ladder variable
([`qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py):
`log R = E(ũ) + h·D(ũ)`); the `d_k` are exactly the coefficients #3821 extended.

`q*`, however, is the zero of the **empirical extractor**
`S(q) = c3_target_at(q, Q_β, m_e) + Vol(4₁)`, which inverts through the **N = 2
rung only** (`c₂ = −1` Lean-proved) and reads `c₃ = (Q_β/Q_{N2} − 1)/u³` against
the experimental neutron `Q_β`. **The extractor carries no `d_k`.**

## Findings (all measured in the probe; exact ladder core REUSED, not re-derived)

1. **`q*` is reproduced to full precision and is ladder-order-INDEPENDENT.**
   `q* = 1.10997859303152328840…` (matches the committed k ≤ 21-era witness to
   > 20 digits). Because `S = c3_target_at + Vol(4₁)` contains no `d_k`, `q*` is
   a property of the N = 2 inversion against the experimental `Q_β` — extending
   the ladder to k = 31 cannot move it.

2. **The bar-odd carrier `O_K(q*)` SATURATES by k ≈ 12**, far inside the
   pre-existing k = 21 data. At `ũ(q*) ≈ 0.009454`, `h(q*) ≈ 0.20906`, the
   per-term magnitudes `|d_k ũ^k|` fall as
   `k=1: 1.5e−2 · k=2: 1.4e−3 · k=3: 3.7e−5 · k=6: 7.9e−9 · k=9: 1.6e−12 ·
   k=12: 3.5e−16 · k=20: 7.8e−26`, and `O_K(q*)` is constant at 60+ dps from
   k ≈ 12 onward. The extra terms **k = 22…31 change `O(q*)` by `|O_31 − O_21| ≈`
   `6.94e−29`** — nothing at the physical substrate point.
   (Consistent with #3821: the q-Gevrey divergence is a growth *class* that only
   overtakes `ũ^k` when `C·log k > |log ũ|`, i.e. `k ≳ e^{|log ũ|/C} ≈ 10^{33}`
   at `ũ ≈ 0.0095, C ≈ 0.06` — so at k ≤ 31 the carrier is, in practice,
   saturated.)

3. **`q*` is experimental-`Q_β`-limited, by ≳ 20 orders over the ladder tail.**
   `dq*/dQ_β ≈ −0.539` (matches the committed value). For any realistic neutron-
   `Q_β` uncertainty `σ`, `q*` moves by `|−0.539|·σ` — e.g. `σ = 1e−9 MeV` gives
   a floor `≈ 5e−10`, still ~17 orders above the `~1e−27` ladder tail. And, more
   sharply, the carrier does **not enter the `q*` determination at all**.

4. **The bar-odd carrier is anchor-blind** — `O_31(proton) ≈ O_31(muon) ≈`
   `O_31(q*) ≈ −0.003486` (spread `~1e−9`) — so it does **not** reproduce the
   swinging empirical `S` (`S(proton) = −0.0395`, `S(muon) = +0.0097`). The
   capstone's `S = h·D(u)` is therefore a **schematic** decomposition (`S`
   bar-odd = `h` × a bar-even function), **not** a tight numerical identity with
   these `d_k`; the `S` swing lives in the `1/u³` extractor, per the merged
   **#3636** recalibration.

## Verdict (scope-(a) negative, informative)

The extended **k = 31** D-ladder does **not** sharpen `q*` or `dq*/dQ_β`. `q*`
remains pinned by the experimental neutron `Q_β` (`dq*/dQ_β ≈ −0.539`), exactly
as the k ≤ 21-era determination found; the bar-odd carrier the ladder refines
saturates by k ≈ 12 and does not feed `q*`. The k = 31 extension's value
(#3821) is to the **divergence-class / resummation program** — which manifests
only at astronomically high k — not to this finite-order pin. This closes the
"more ladder terms will sharpen `q*`" hypothesis **with a number**.

`conj:im-q-physical-role` stays a conjecture; `q₀` stays CAL-2 calibrated.

## What NOT to re-chase

- Do **not** re-pin `q*` off the D-ladder: the extractor is `d_k`-free and the
  carrier saturates by k ≈ 12. A sharper `q*` needs a sharper neutron `Q_β`
  (result 3), not more ladder terms.
- Do **not** read `S = h·D(u)` as a tight identity — it is schematic (result 4);
  the empirical `S` swing is the `1/u³` extractor (#3636), not the carrier.

## Cross-references

- k ≤ 21-era `q*`: [`qbeta_c3_imq_qstar_ladder_amplification_probe.py`](../../computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py); capstone [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md).
- k = 31 ladder: #3821 [`qbeta_dladder_extension_singularity_probe.py`](../../computations/qbeta/qbeta_dladder_extension_singularity_probe.py); [`2026-07-17-dladder-extension-qgevrey-drift-confirmed.md`](2026-07-17-dladder-extension-qgevrey-drift-confirmed.md).
- `S = h·D(u)` bar-split: [`qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py).
- `1/u³` extractor recalibration: [`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md) (#3636).
