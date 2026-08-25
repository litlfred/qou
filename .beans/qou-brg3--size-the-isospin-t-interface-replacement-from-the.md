---
# qou-brg3
title: size the isospin-T interface replacement from the deuteron's 27.34 percent one-bond miss
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T00:11:01Z
updated_at: 2026-08-16T13:57:06Z
---


## Arc status 2026-08-16 — Wenzl level 2 reframes the H₆ result

The selection principle this bean was looking for is supplied by the framework:
convention D **is** SU(2) Wenzl level 2, so `y_λ = 0` on every ≥3-row partition
and the two-nucleon trace sees **4 of 11 blocks**. Three of the four unbind in
all three systems. Details + the conjugate-pair consequence: `qou-8zjc`.

Corrections this forced on my own committed work, all landed:

* the "7 of 11 sign-flipped blocks are the deuteron's channel" obstruction —
  those blocks have `y = 0` and are not in the trace. Residue is one block,
  `(3,3)`, unexplained.
* a guard against reading "3 of 4 unbind" as "nearly unbound": the aggregate is a
  ratio of sums, not a mean of ratios, and the exact trace ratio is `1/μ` to
  `1e-30` — the diproton is still bound at +2.54 MeV.
* `μ±` verified to BE the n=2 Wedderburn weights (`0.7527021133`,
  `0.2472978867`), which I had asserted without checking.

Still open on this bean: the isospin-`T` sizing itself. It is better posed than
before — the surviving-block structure is now known and small — but no magnitude
statement is available until `qou-jtfo` (per-block reconstruction) closes.


## 2026-08-16 — CLOSED (route 4, the last one). The framing does not matter.

The bean asked to size the isospin-T interface replacement. Answer: **no T-odd
replacement exists**, and this is proved without ever deriving the framing `f`.

**The framing cancels.** A T-odd rescaling `(μ₊,μ₋) → (μ₊t, μ₋/t)` — the ribbon
twist is `t = q^f` — leaves `B(T=1)+B(T=0) = −α·log(μ₊μ₋)` unchanged, because
the two `log t` terms have opposite sign. Verified at `f = 0, 3, 10, −8.297`:
identical to 50 digits (spread 1.07e-50).

**The total is floored.** `μ₊+μ₋ = 1` (`InterfaceScalar.mu_sum_eq_one`) caps
`μ₊μ₋ ≤ 1/4` by AM–GM, so `B(T=1)+B(T=0) ≥ α·log 4` for EVERY convex pair.

    floor      α·log 4          = 5.8030 MeV
    substrate  −α·log(μ₊μ₋)     = 7.0377 MeV
    nature     B(3S1)+B(1S0)    = 2.2246 − 0.0736 = 2.1510 MeV

Substrate over-binds 3.27x; the **floor** over-binds 2.70x whatever the projector
scalars are. Robust to the virtual-state number: taking B(T=1)=0 exactly still
leaves 2.61x.

**This supersedes the 'f = 3 is a fit' honesty flag with something stronger —
there is no f to find.**

**The obvious escape is closed in the opposite direction.** 'The colour-only
fibre lacks a spin/spatial factor so the two channels carry only s < 1 of the
trace, dropping the floor' is BACKWARDS: the cap `μ₊μ₋ ≤ s²/4` shrinks with s,
so smaller normalisation binds HARDER. Reaching nature needs `s ≥ 1.5469 > 1`,
unavailable to a projector decomposition. More channels is also wrong-way: the
k-channel floor is `α·k·log k`, rising (k=2: 5.80, k=3: 13.80, k=4: 23.21 MeV).

**So the surviving direction is α, not the interface.** The issue is not whether
the colour-only fibre can host 3S1/1S0 — it is that the energy scale attached to
the interface is ~2.7x too large. Satisfying the floor needs α ≤ 1.5516 MeV
against E₀ = 4.1860. That re-points the sibling bean.

Lean: `QOU/QBeta/TwoChannelTotalBindingFloor.lean`, 7 declarations, sorry-free,
lean-direct exit 0, all [propext, Classical.choice, Quot.sound].
Probe: `computations/probes/two_channel_total_binding_floor_probe.py`.

Self-correction: an earlier revision of the probe asserted the escape as s < 1
(≈0.60). Wrong direction; caught before commit, and the corrected direction is
recorded in the Lean docstring because the wrong one is the intuitive one.
