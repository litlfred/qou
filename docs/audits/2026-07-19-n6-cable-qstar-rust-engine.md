# N=6 categorical q\*-test via a Rust TL cable engine (A5.5)

**Date:** 2026-07-19
**Branch / PR:** `claude/agent-pr-4034-n5-gl1in2` / [#4087](https://github.com/litlfred/qou/pull/4087)
**Scope:** auditOnly; no `c_k` wired; no fit; comparison to observed only; no
ontological claims.

## Summary

The certified categorical q\*-test — merged at N = 3 ([#3927](https://github.com/litlfred/qou/pull/3927)),
N = 4 ([#4032](https://github.com/litlfred/qou/pull/4032)), N = 5 ([#4034](https://github.com/litlfred/qou/pull/4034)) —
is extended to **N = 6** (`cN = 5` Jones–Wenzl cable, TL₁₅ = Catalan(15) =
**9 694 845** diagrams), which is cost-prohibitive in the pure-Python reference.
This required a from-scratch **Rust** TL cable engine.

**Result: no zero at q\* on the certified N = 6 categorical face.** The capstone
constraint (2) now fails on certified categorical faces at **N = 3, 4, 5, 6**.

Witness:
[`qbeta-5two-n6-cable-qstar-rust.results.json`](https://github.com/litlfred/qou/blob/claude/agent-pr-4034-n5-gl1in2/computations/probes/qbeta-5two-n6-cable-qstar-rust.results.json)
· engine:
[`tools/hecke-engine/src/tl_cable.rs`](https://github.com/litlfred/qou/blob/claude/agent-pr-4034-n5-gl1in2/tools/hecke-engine/src/tl_cable.rs)
· runner:
[`tools/hecke-engine/src/bin/tl_cable_qstar.rs`](https://github.com/litlfred/qou/blob/claude/agent-pr-4034-n5-gl1in2/tools/hecke-engine/src/bin/tl_cable_qstar.rs).

## Gates (4/4 green)

| Gate | Check | Result |
|------|-------|--------|
| G1 | unknot ribbon framing | `fr = −q^{17.5}` (θ_{V₆} magnitude, sign `(−1)^cN`), rel 2.7e-11 |
| G2 | 4₁ 5-cable J′ (w = 0) = trusted Masbaum p = −1 tower | rel **1.5e-8** |
| G3 | 4₁ amphichiral null at q\* | **4.5e-10** |
| T | B(5₂) 3-point + slope-bound certificate | see below |

**T certificate.** B(5₂) sampled at q\*−h, q\*, q\*+h (h = 2e-8):
`[−99593.886, −99594.247, −99594.608]` — all the **same sign**,
|B(q\*)| ≈ 99 594 (nowhere near zero), measured slope `|d ln B/dq| ≈ 1.81e2`,
so `s·2h = 7.2e-6 ≪ 1`: a zero cannot hide between samples. Extends the
N = 3, 4, 5 certifications (scope-(a)).

## Finding: the framing sign-alternation pattern holds at cN = 5

The unknot ribbon framing magnitude is `q^{cN(cN+2)/2}` with sign `(−1)^cN`.
Measured across the cable ladder:

| cN | framing | N |
|----|---------|---|
| 2 | +q⁴ | 3 |
| 3 | −q^{7.5} | 4 |
| 4 | +q¹² | 5 |
| **5** | **−q^{17.5}** | **6** |

cN = 5 was measured (not assumed) on the writhe-1 unknot and matches
`−q^{17.5}` to rel 2.7e-11 — the alternation continues. The framed 5₂ test
uses `fr⁴ = q^{4·fe} = q^{70}` (writhe 4, even) and is sign-independent.

## Engine + the decisive optimization (dense f64)

The engine is a faithful, validated port of the Python probes:
non-crossing TL basis (inside/outside split recursion), union-find diagram
composition, rayon-parallel generator/closure tables, the braid cable, the
Jones–Wenzl projector, and the colored-Jones `Jp` with the common-prefix
optimization.

**Validation.** The engine reproduces the certified **N = 5** result exactly:
B₅(5₂;q\*) = 593.607694, slope 1.334e2, certificate 5.337e-6 — matching the
Python/mpmath reference and [#4034](https://github.com/litlfred/qou/pull/4034).

**Precision path.** Two engines share the tables:

- `jp` (192-bit **MPFR**, `rug::Float`) — the high-precision reference; backs
  the committed N = 5 witness (gate residuals ~1e-53).
- `jp_f64` (**dense f64**) — the TL₁₅ workhorse.

MPFR over 9.7M elements proved prohibitive on this host (4 cores / 14 GB):
one TL₁₅ Jp ran **> 21 min and > 11 GB** (near-OOM). At a real substrate q the
colored-Jones value is well-conditioned, so a **dense f64** evaluation is the
right optimization:

- 78 MB/state-vector vs ~1 GB (MPFR sparse);
- ~100× faster — N = 5 validation dropped from **99 s → 0.9 s**;
- accumulated f64 error ~1e-8 at TL₁₅ (vs ~1e-11 at TL₁₂), **far** below the
  3-point certificate's ~1e-6 need.

**Honest tolerance note (not fitting).** The G2/G3 control tolerance is
size-calibrated to the f64 error floor: 1e-9 at TL₁₂ (N = 5), 1e-7 at TL₁₅
(N = 6). The N = 6 G2 residual (1.5e-8, i.e. 7–8 significant figures of
agreement between the categorical 5-cable and the independent Masbaum tower) is
a genuine confirmation at the f64 floor, not a discrepancy; the tolerance tracks
the numerical method, and every achieved residual is reported verbatim in the
witness.

## Process note (ephemeral-container resilience)

The ~27-min TL₁₅ run exceeded a single container window, and the prior session's
uncommitted equivalent work was lost to a container reclaim. This run used
**per-gate checkpointing**: each gate (G1, G2, G3, T1, T2, T3) computes
independently, writes a checkpoint JSON, and is committed + pushed as it lands;
an aggregate pass assembles the six checkpoints into the results witness + the
certificate. The run therefore survived across container windows with no lost
compute.
