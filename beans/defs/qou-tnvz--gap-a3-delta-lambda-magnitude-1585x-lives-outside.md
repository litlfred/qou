---
# qou-tnvz
title: 'GAP: A=3 Delta_lambda magnitude 1.585x lives OUTSIDE the finite-type filtration of the single Borromean deficit'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:13:32Z
updated_at: 2026-10-04T15:19:40Z
parent: qou-v2om
---

## What is open

The A=3 triton 3-body magnitude factor `r* = μ₃/c₃ ≈ 1.585` (μ₃=+0.4708 #4320 ÷ c₃=+0.297
Hecke H₉ near-miss #4364) is bracketed out of every Hecke-level AND finite-type ingredient:

- LEVEL / geometric W_λ / coordination-EDGE / exact-order μ̄_A — walls #4364/#4376/#4392/#4472/#4480.
- **Vassiliev WEIGHT of the single Borromean deficit — REFUTED here (scope-b).** The proved
  deficit `1−τ_Borr = h⁴(3+h²)/(h²+4)`; its leading finite-type weight `(3/4)h⁴` is ≤ the full
  deficit for ALL h, so weight/Hecke ≤ 1 (measured 0.9964; whole tower correction +0.36 %, not
  the +58.5 % needed). The finite-type filtration re-expands the same Markov trace the Hecke
  level sums — no truncation exceeds it. Lean `VassilievMagnitudeA3.lean`, audit
  `2026-08-01-deltalambda-a3-beyond-hecke-vassiliev-magnitude.md`.

## Next honest step

The `1.585×` requires structure OUTSIDE the finite-type filtration of the single Borromean
deficit. Untested candidates (NOT excluded): a per-isotope **operator-valued cross-channel
combiner** summing over multiple Wedderburn blocks (each block a distinct deficit, so the total
is not a truncation of one `1−τ_Borr`); a **cross-cluster interface term** (the A=4 PROBE-2
interface operator restricted to A=3); or the μ₃ target being a **sum of ≥2 finite-type objects**
of comparable size (the +0.36 % single-deficit tower measures the size of the MISSING higher
term, per the "compositional object is already many-body" discipline). Do NOT re-probe a single
weight of `1−τ_Borr` — that route is closed. Anti-fit still gates: a Δ_λ obtained by inverting
μ₃ is a fit, not a derivation.

### Progress (Round 72 — PR litlfred/qou#8311)
- Formalized in PR `litlfred/qou#8311` (`feat/round72-su4gate-markovzd-interface-vassiliev-lever1-43c1`, Commit 1 `120f8595e20646e98de0e5ba129245b973aa1574`, Head `be2282b84c903a928b1e78fc59abcd496c8ceea5`, `scriptHash: 3cfc48bf2b24`).
