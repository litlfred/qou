# c₃ direction 2: leading geometric channel identity — honest null + direction-4 confirmation (2026-08-01)

**Axis:** Q_β c₃ bar-odd `S` — direction 2 (reproduce the smooth target `S = Im 𝔙₄₁(u(q₀))`
geometrically). **No c_k wired; no fit; registry untouched.** Honest **null** on the
canonical anchor, plus a clean confirmation of the direction-4 extraction picture.

## Setup

After the #4509 reframe, the well-posed target is the **smooth** `S = c₃ + Vol(4₁) =
Im 𝔙₄₁(u(q₀))`, not the `1/u³`-amplified `|S_p/S_m|`. The leading geometric prediction
(boost `Re u = ln q₀`, `Im u = 0`) is `geom(q) = (√3/4)(ln q₀)²`. Probe:
[`qbeta_c3_geometric_channel_q0star_probe.py`](../../computations/qbeta/qbeta_c3_geometric_channel_q0star_probe.py).

## Results

**(1) Direction-4 confirmation — geom FLAT, S STEEP.** Across the muon/proton anchor
gap, `geom(q)` changes by `Δgeom ≈ 1.0×10⁻⁹` while the ladder `S(q)` sweeps
`ΔS ≈ 0.049` — ratio `ΔS/Δgeom ≈ 4.7×10⁷`. The geometric object is smooth; the S
hypersensitivity is the `1/u³` extraction artifact. Independent confirmation of #4509.

**(2) Honest null — the identity fails at both canonical pins.**
`geom ≈ 0.004714` is `2.054×` below `S(muon) = 0.009683` (the known `A ≈ 2.05`
boost-enhancement / spin-part gap) and has the **wrong sign** vs `S(proton) = −0.039459`.
So the smooth target is **not** reproduced by the leading form + pure `ln q₀` boost at
either canonical anchor. The `A ≈ 2.05` gap persists (open, `qou-iyj5`).

**(3) The `q₀*` crossing is IVT-trivial.** There is a `q₀* = 1.10997859426` in the gap
with `S(q*) = geom(q*) = 0.004714`, at ~90% of the way from the proton to the muon pin.
But its existence is **IVT-trivial** — the steep amplified `S` curve must cross the flat
geometric line exactly once in the gap — so it is **not independent evidence** for the
identity. Recorded only as a datum.

## Net

Direction 2 does **not** close the gap: the leading geometric channel identity
undershoots the smooth target by the `A ≈ 2.05` factor at the canonical anchor (the
boost-enhancement / spin part remains open). What it *does* add is a second, independent
confirmation of the direction-4 picture (smooth geometry vs `1/u³`-amplified S), and it
rules out the naive reading that the `q*` crossing validates the identity (it is
IVT-trivial). The honest open target is unchanged: derive the `A ≈ 2.05`
boost-enhancement / spin part of `u(q₀)` (`qou-iyj5`), now known to be **smooth /
geometric** (radius `2 log φ`, #4508), **not** an on-anchor singularity, and **not** the
amplified `|S_p/S_m|` ratio.

-- Ref: [manuscript] docs/audits/2026-08-01-c3-hypersensitivity-is-u3-extraction-artifact.md (#4509)
-- Ref: [manuscript] docs/audits/2026-08-01-c3-uq0-radius-golden-ratio-on-anchor-singularity-refuted.md (#4508)
-- Ref: [manuscript] .beans/qou-iyj5 (the surviving open target: boost-enhancement A≈2.05)
