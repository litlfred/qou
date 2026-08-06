---
# qou-mmz7
title: 'GAP: is the tanh(ln q0) Coulomb/strong shortfall a missing constant or missing scale-dependence? (channel-sweep discriminator)'
status: todo
type: task
created_at: 2026-08-06T22:45:27Z
updated_at: 2026-08-06T22:45:27Z
---

## What is established (do not re-derive)

`tanh(ln q₀) ≈ 0.10396` is **derived, parameter-free, and q₀-only** — it is
not a fit and not a suggestive coincidence:

- `def:coulomb-charge` ([`climax-volume-mass/coulomb-charge.md`](../content/quantum-observable-universe/climax-volume-mass/coulomb-charge.md))
- derivation: [`docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md`](../docs/audits/2026-06-03-charge-coulomb-tn3he-derived.md)
- identity `E_asym/E_sym = tanh(ln q)` is Lean-proved sorry-free
  (`QOU.Braiding.em_strong_ratio_tanh`), and after PR #4407 it carries the
  correct positive-braid hypothesis (`ratio_positive_braid`); the general
  case picks up a multiplicity factor `(p+m)/(p−m)` (`ratio_general`).

It is described in the corpus as "the only derived Coulomb/strong ratio"
([`2026-07-13-mirror-split-one-third-mechanism-probe.md` §S3](../docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md)).

## The gap

Used as a Coulomb/strong coefficient it **underdelivers by roughly 3×**.
From [`2026-06-22-he3-pairknot-clambda-coulomb-probe.md` Finding 2](../docs/audits/2026-06-22-he3-pairknot-clambda-coulomb-probe.md),
against the AME ³H−³He split of 0.764 MeV:

| quantity | MeV | vs split | fitted? |
|---|---|---|---|
| `C_λ·Z(Z−1)·m_e` | 0.034 | 4.4% (far under) | no |
| **derived pp-Coulomb `tanh(ln q₀)·B_pp`** | **0.238** | **31% (under)** | **no** |
| AME ³H−³He split (target) | 0.764 | — | experimental |
| Skein `a_C·Z(Z−1)/A^{1/3}` | 0.967 | 127% (over) | `a_C` is the empirical BW value — **not adopted** |

The target is *bracketed* by two parameter-free estimates, so the missing
object is bounded, not unbounded.

## The question this bean adds (not asked elsewhere)

`tanh(ln q₀)` is a function of `q₀` alone, hence **scale-free and
channel-independent by construction**. But a Coulomb/strong ratio is
physically a *running* quantity — α runs slowly, α_s runs fast — and no
renormalisation scale is attached to the substrate anchor anywhere in the
corpus.

So the shortfall admits two structurally different explanations, and they
are **experimentally distinguishable from data already in the corpus**:

- **(A) Missing constant.** The shortfall factor (~3.2× on ³He) is
  approximately *the same* across channels and mass numbers. Then the
  missing object is a single derived constant multiplying the ratio, and
  the scale-free form is fine.
- **(B) Missing scale/channel dependence.** The shortfall factor *varies*
  systematically with A, Z, or channel type. Then a scale-free coefficient
  is the wrong shape and no constant will close it — the ratio needs a
  running or channel-graded partner.

A scale-free coefficient landing at a consistent ~31% is the signature of
(A); drift across the sweep is the signature of (B).

## Concrete next step

Sweep the shortfall factor `split_measured / (tanh(ln q₀)·B_pp)` across
every channel where both sides are already computable — ²H, ³H−³He, ⁴He,
⁶Li, ⁷Li at minimum — and plot/tabulate it against A and Z.

- Factor flat within ~10% ⇒ **(A)**, and the bean becomes "identify the
  constant" (a derivation target, not a fit — the anti-fit discipline
  applies; inverting the AME anchors to get it is a fit and must be
  labelled one).
- Factor drifting monotonically with A or Z ⇒ **(B)**, which would be a
  scope-(a) negative against the scale-free form and would redirect the
  Coulomb work toward a graded/running partner. Record it as such;
  **do not** write "tanh(ln q₀) is refuted" — the identity is proved and
  the ratio stays valid as the bar-odd channel ratio. Only its adequacy
  *alone* as the Coulomb/strong coefficient would be at issue (scope (a),
  per AGENTS.md §"Before declaring refuted").

## Prior work — completed, different scope (do not redo)

- `uwpg` (completed) — ρ-normalisation isolating the sinh/Coulomb channel ρ
  for the ³H−³He mirror split; residual 18%, no fit.
- `vr1r` (completed) — ³He pair-knot/Coulomb corpus-grep #2478; LP-dual
  degenerate, Coulomb 31% forbidden-to-fit; `C_λ·S_λ` route assessed.

Both are scoped to the ³H−³He mirror split specifically. Neither poses the
cross-channel constant-vs-scale-dependence discriminator above.

The S3 gate in [`2026-07-13-mirror-split-one-third-mechanism-probe.md`](../docs/audits/2026-07-13-mirror-split-one-third-mechanism-probe.md)
notes the `tanh(ln q₀)` coefficient would have to be *superseded* at the
triple channel — outcome (B) would explain why, and outcome (A) would say
what supersedes it.

## Origin

Surfaced in PR #4407 (Einstein asymmetric-metric comparison,
[`docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md`](../docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md) §4.1).
That PR softened the "EM/strong ratio at the Skein scale" wording in
`rem:crossing-energy-interpretation` to a channel-weight ratio with no
scale attached — a presentation fix that made the open question visible
rather than answering it. This bean is the question.
