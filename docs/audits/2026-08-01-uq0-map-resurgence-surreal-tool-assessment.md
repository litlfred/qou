# The q₀→m argument map: convergence synthesis + alien-calculus / surreal tool assessment (2026-08-01)

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Axis:** Q_β c₃ (bar-odd `S`) — the single open link `u(q₀)` (`qou-82w7`). **Distinct-angle
synthesis** (overlap with the S-channel / one-instanton / Habiro sessions is authorised and
deliberate). **No c_k wired; no fit; registry untouched.** This doc does NOT close the map;
it consolidates the ~10 angles onto one object and honestly assesses the two tools proposed
for it (alien calculus, surreal grading), including one honest negative.

## 1. All angles reduce to one open object

The value of c₃ (equivalently: the argument map `u(q₀)` / `q₀→m`, the S-channel
`S = Im 𝔙(u(q₀))`, the magnitude) is the **same single open object** across every route:

| Angle (this session + prior) | Structural result (proved) | Reduces to |
|---|---|---|
| C1↔SW keystone | W1 S₃/no-branch; W2 exponents, ∞ q-Gevrey formal solution | `q_cubic = C1` value |
| Berezinian super-DM | c₃ = cross-term alone (diagonal drops out, #4469) | `q_cubic = C1` value |
| tetraplectic → CS 3-form (Reeb) | Cartan-contraction 3-form = CS face = `S=Im 𝔙` | `u(q₀)` value |
| SDeformedVolumeChannel | `V₄₁(u)=Vol+i(√3/4)u²` concrete; boost `Re u=ln q₀` fixed | spin part of `u(q₀)` |
| one-instanton resurgence | CS-phase `sin(Im𝔙/πℏ)` supplies the zero-crossing | multi-instanton magnitude |
| Q_β Habiro element (1ppQ ledger) | `c_2` Taylor-exact; `c_{≥3}` near-match | fibre-level `F(q)` search |

The object is: the **Q_β Habiro element `F(q)`** = the **resurgent trans-series normalization**
of the 4₁ complex-volume phase at the substrate `q₀` = the **spin/imaginary part of the
meridian holonomy** (the boost→spin transition). One object, many faces.

## 2. Alien calculus / resurgence — already the one-instanton route (done, quantitatively open)

The alien-calculus attack **is** `OneInstantonNormalization.lean` (PR #4246) + audit
[`2026-07-25-aomega-one-instanton-magnitude-probe.md`](2026-07-25-aomega-one-instanton-magnitude-probe.md).
Form `N_odd(q) = 𝒜·e^{−Re𝔙/(πℏ)}·sin(Im𝔙/(πℏ))`, `ℏ=log q`. Honest result:

- **Structurally necessary ✓** — the CS-phase oscillation `sin(Im𝔙/πℏ)` is the *only*
  census object producing a zero-crossing of `N_odd` at all (the raw `Im(ι₁₃)` form is
  monotone). So the Stokes/resurgent structure is confirmed *required*.
- **Quantitatively open ✗ (parameter-free)** — zero-location off by ~10⁶× the anchor gap;
  slope 4.28 orders short; prefactor ~1.8 orders large. The `1/u³` lever **cancels** in the
  `S=A/u³` slope ratio (retracted over-claim). The residual is the **multi-instanton /
  median resummation** — the full state-integral resurgence, not the leading saddle.

So the resurgence route has the right *structure* and an open *magnitude*; today's
`schannel` audit adds `κ_n ≠ c_k` and `saddle ≠ 4.075` (two more honest negatives on the
saddle/κ routes to that magnitude).

## 3. Surreal grading — honest negative for leverage (with the one caveat)

Proposed use: manage the transcendental growth via the blow-up calculus
(`AppendixSurreals/BlowupCalculus`, `SurrealLimitTransfer`). Assessment:

- **The obstruction quantities are finite (archimedean grade-0):** `dc₃/dq ≈ 4.7×10⁶`, the
  4.28-order slope gap, the 10⁶ zero-location miss are all **large finite** numbers, not
  `ω`-graded infinities/infinitesimals. The surreal blow-up calculus manages *infinite and
  infinitesimal* grades (`ord_ω ≠ 0`); a hypersensitive-but-finite archimedean map is
  grade-0 throughout, so surreal grading supplies **no new leverage on the map itself**.
- **The one caveat (where it *would* apply):** near the root-of-unity Stokes line `q*`
  (where `e^{−Action/ℏ_q} → O(1)` and the trans-series stops decaying) the map genuinely
  *does* acquire divergent grade, and the blow-up calculus would track the approach
  `u(q₀) = u(q*) + (blow-up)`. **But locating `q*` and its blow-up grade is the open
  problem** — so this is circular, not a new tool. Honest verdict: surreal grading is a
  correct *bookkeeping* for the resurgence boundary, not a *lever* that closes it.

## 4. Honest bottom line

The q₀→m map is the framework's single central open research object. The alien-calculus
route is done-and-structurally-confirmed but quantitatively open (multi-instanton
resummation residual); the surreal tool does not add leverage (finite-grade problem, modulo
the circular `q*` caveat). No fit closes it; the anti-fit rule forbids fitting it. The
precise open computation is unchanged: **the Q_β Habiro element `F(q)` / the median
resummation of the 4₁ state integral at `q₀`** (1ppQ ledger PROBE-NEW; `qou-82w7`). This
doc does not close it — it consolidates the reduction and rules the surreal tool out as a
lever, which narrows the search.

-- Ref: [manuscript] docs/coordination/keystone-sdeformedvolume-channel-attack.md
-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md (PROBE-NEW Habiro element search)
-- Ref: [manuscript] docs/audits/2026-07-25-aomega-one-instanton-magnitude-probe.md
-- Ref: [manuscript] docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md (qou-82w7)
