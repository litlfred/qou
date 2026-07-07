# c_k special-function candidate landscape: one wall, one surviving channel

**Date:** 2026-07-07 · **Axis:** z→c_k f-map keystone (candidate triage) ·
**Relates:** PR #3459 (channel-separation spec), PR #3458 (u-side / evaluation
map) · **Tier:** formalize-first triage (scope-(a)) · **Verdict:** three of four
named candidates excluded/negative; the survivor is in the phase channel

## One-line

Every special-function candidate that models the c_k as a **smooth real
function of q** (q-Hermite, q-Bessel, toroidal-Legendre) hits the **same q=1
cusp / PR #1821 smoothness wall** — the *magnitude channel* identified in the
[channel-separation spec](2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md).
The lone structurally-positive candidate (Wenzl–Pochhammer) lives in the
**root-of-unity / phase channel**, which is where PR #3458's evaluation map
operates. The candidate search has been looking in the wrong channel.

## The four candidates

| Candidate | Status | Evidence | Channel |
|---|---|---|---|
| **q-Hermite** | scope-(a) excluded (new, [`qbeta_c4_qhermite_entry_gate_probe.py`](../../computations/qbeta/qbeta_c4_qhermite_entry_gate_probe.py), 3/3) | gen func = product of compact `Φ_q` ⇒ correct **bar-even** face, but cumulants `κ_n = 2cos(nθ)/(1−q^n)` have a **q=1 pole**; can't equal the finite `c_2=−1` without a fitted q-dependent variable change; moments (Touchard–Riordan `1,1,3,15,…`) are positive-growing vs the small mixed-sign c_k | magnitude (fails) |
| **q-Bessel** | already refuted ([`qbeta-qbessel-crossanchor-smoothness-refutation`](../../computations/qbeta/qbeta-qbessel-crossanchor-smoothness-refutation.witness.json)) | substrate-fixed **real-x** `sinh(x·sinh η)` under-precise vs the cross-anchor `dc_3/dq₀≈4.66×10⁶` (PR #1821 wall) | magnitude (fails) |
| **Toroidal-Legendre** | already negative (sibling `claude/toroidal-harmonics-basis`) | toroidal-Legendre ↔ 2nd-order ODE in `w=z²` **proved**, but "nothing here makes any c_k exact"; the Δ_λ (A=4) scan is a flagged coincidence (fails 3-CAL + Δ_λ gate) | magnitude (fails) |
| **Wenzl–Pochhammer** | **structurally positive** ([`qbeta-habiro-phi8-squared-boundary-explained`](../../computations/qbeta/qbeta-habiro-phi8-squared-boundary-explained.witness.json)) | identifies the Habiro-tower **boundaries** as the **second Wenzl-tower annihilator at `[8]_q = 0`** (`M_first_Φ_8²` = 12 for D−n vs 15 for He pairs) — a **root-of-unity** structure, not a smooth real function | **phase** (survives) |

## The unifying invariant (why this is one wall, not four)

The c_k are **finite** Taylor coefficients at `q=1` (`c_2=−1` proved). Every
"smooth real function of q" candidate must therefore be finite and smooth at
`q=1`. But the natural q-special-function objects on the bar-even/Rogers face —
compact-q-dilog cumulants, q-Bessel of real argument, modular toroidal
harmonics (E₄,E₆) — all carry the `1/(1−q^n)` / cusp structure that **diverges
at `q=1`**. Reproducing a finite c_k then demands a q-dependent counter-term
whose only job is to cancel that pole: **a fit, not a derivation** (C14; the
PR #1805 entropy bound makes a 4–5-sig-fig fit to c_4 numerology).

This is precisely the **magnitude channel** of the
[channel-separation spec](2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md):
PR #1821's `dc_3/dq≈4.66×10⁶` impossibility is a bound on smooth **real**
functions. The bar-odd c_k source is the **phase channel**, on which the
magnitude/smoothness wall is silent.

## The surviving direction — Wenzl–Pochhammer (probed)

**Wenzl–Pochhammer is the one candidate in the right channel.** It does not
model c_k as a smooth real function; it locates the Habiro element's
**boundaries at roots of unity** (`[n]_q = 0`), which is the phase / root-of-
unity structure. Probe
[`qbeta_c4_wenzl_pochhammer_channel_probe.py`](../../computations/qbeta/qbeta_c4_wenzl_pochhammer_channel_probe.py)
(3/3) makes this concrete:

| gate | finding |
|---|---|
| **WP1** boundaries | `[4]_q = [8]_q = [12]_q = 0` exactly at `ζ₄, ζ₈, ζ₁₂` — the Wenzl-tower annihilators (`[4m]_q=0`, the `m∣k` vanishing) |
| **WP2** c_4 closed form? | the **exact** `c_4^even` (9fnm, ∈ ℚ(√3)=ℚ(ζ₁₂)⁺) has rational height `~2.5×10⁹` ⇒ a **generic ℚ(√3) element, NOT a low-complexity W-P value** — W-P gives no clean c_4 closed form |
| **WP3** c_8 boundary | the known c_k pattern-break at **c_8** (c6-c10 falsification) coincides with the **second** Wenzl boundary `[8]_q=0` at ζ₈ |

**Honest verdict (scope-(a)):** W-P is confirmed the correct **channel** (roots
of unity; `[4m]_q` boundaries; `c_8`-break ↔ `[8]_q`), but it does **not** hand
c_4 a closed form — the exact `c_4^even` is generic in ℚ(√3), and the canonical
c_4 (~4–5 sig figs, PR #1805) cannot be identified by a fit (C14). This is
consistent with — and feeds — PR #3458's evaluation-map program: the map
extracts a **phase** of the pure-phase fibre `Φ_b`, a Habiro element in the
**Wenzl–Pochhammer basis** whose `ζ_{4m}` boundaries generate the ladder, with
the near-singularity sought as a **root-of-unity accumulation** on `|q|=1`, *not*
a fitted real-q pole. **c_4 is determined by that evaluation map, not by a
special-function substitution.**

**Concrete continuation (non-fishing):** the q-Bessel refutation was against a
**real-x** ansatz (magnitude channel); the phase-channel reframe means a
**root-of-unity q-Bessel / Wenzl–Pochhammer boundary** form is *not* excluded by
that refutation. Reopening it would require a **derived** root-of-unity argument
(a Wenzl annihilator condition), not a real-x scan. That is #3458's territory;
this doc hands over the triage so the excluded three are not re-run.

## Discipline

Scope-(a) throughout. Nothing wired; no registry tier change; no c_4 value
proposed or fitted. q-Hermite is recorded as **excluded at the c_2 anchor**
(cite the invariant: q=1 pole of `1/(1−q^n)`), with the ingredient **not**
structurally forbidden in other variants — only the natural continuous route is
excluded. The three prior negatives (q-Bessel, toroidal) are cited, not re-run.

## Cross-references

- Channel-separation spec: [`2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md`](2026-07-07-qbeta-fmap-phi-b-channel-separation-spec.md)
- Wenzl boundary audit: [`docs/audits/2026-06-01-qbeta-habiro-phi8-squared-boundary-explained.md`](../audits/2026-06-01-qbeta-habiro-phi8-squared-boundary-explained.md)
- AGENTS.md §"Formalize-first probe discipline"; §"Before declaring refuted (a)/(b)"; §"Im(q) at fibre vs observable level"
- PR #3458 (z→c_k u-side / evaluation map); PR #1821 (real-q smoothness wall); PR #1805 (entropy bound)
