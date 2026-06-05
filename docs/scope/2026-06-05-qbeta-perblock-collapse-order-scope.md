# Q_β residue-A — the per-block collapse-order test (S2 + S3): research scope (2026-06-05)

## Status: owner-authorized exploration (strategy S2 + S3)

Owner directed exploration of the canonical-derivation cheat-sheet **§9.2
"unused lever"**: the scalar Markov trace

$$\mathrm{tr}_M \;=\; \sum_{\lambda \vdash n} y_\lambda\,\chi^\lambda$$

**collapses the per-block content at step 5 — *before* the archimedean functor
`τ` at step 9.** The cheat-sheet's guiding principle is *"stay in the fibre as
long as possible, observe last."* This doc scopes the **unique, non-duplicative**
test of that lever for the Q_β `c_3` residue-A. It is **scope only** — no result
claim, no fit; the compute is for a focused session.

## What the active siblings already settled (build on, don't repeat)

| Sibling | Established | Consequence for this test |
|---|---|---|
| **#1887** (Reeb-sinh parity) | **Lean-proved**: `cosh(kη)` bar-EVEN, `sinh(kη)` bar-ODD ⇒ only the `sinh` term can source the first bar-antisymmetric coefficient `c_3` (S3). The scalar Reeb-`sinh` matches `c_3`'s **sign** but is `O(1)` vs `dc_3/dη ≈ 4.26e6`. **f-map `sinh(ℓη)/u^k` REFUTED**: the swing-lock identity ⇒ no fixed-ℓ closed-form f-map absorbs the `c_3` cross-anchor swing. | S3 (bar-odd localization) is **done**. The scalar amplifier is **refuted**. The amplification is *not* a closed-form scalar f-map. |
| **#1742** (bar-pairing binding) | The archimedean **observation stays `\|χ^λ(q₀)\|`** (Im(q₀)=0), **not** the mirror bar-pairing (which underbinds −70%). **~half the Wedderburn channels are *growth* channels** (`χ(q₀)·χ(q₀⁻¹) < 0`, the arccosh/hyperbolic regime). The bar is a **fibre-only** tool. | The per-λ structure carries a **rotation/growth sign split** that the scalar `Σ_λ` mixes. Observe-last must use `\|χ^λ(q₀)\|` per block — never bar-ify the observation. |
| **#1839** (residue-A kernel) | **C-finite recurrence** engine for the `c_k` (Lean, sorry-free): `c_n = -(q₀)⁻¹ Σ_j …`. | The per-λ generating structure should reproduce this constant-recursion; a per-λ source must be consistent with it. |
| **#1521** (α_EM Habiro) | `[2]_q·(1−h²α)` **is** a closed fermion-loop in the fundamental rep — a fibre-level Habiro element. | The residue-A element is the analogous **bar-odd** fibre object; `α_EM` is the bar-even template. |

**Net:** S3 is proved, the scalar f-map is refuted, the observation is pinned to
`|χ^λ(q₀)|`, and the per-λ channels carry a rotation/growth sign split. The one
thing **no sibling has tested** is whether the **collapse itself** is the source
of the order gap.

## The unique test — does `Σ_λ` *cancel* the `c_3`-carrying order?

PR #1593's ε-order gap: the scalar per-block `Δtr_M` sits at `O(√u)·ε¹`, the
ladder `c_3` at `u³·ε⁶`. #1887 showed the bridge is **not** a closed-form scalar
f-map. The §9.2 lever proposes a different origin for the gap entirely:

> **Hypothesis (falsifiable).** The per-λ summands
> `y_λ·[χ^λ(𝓑_n) − χ^λ(𝓑_p)]` contain order-`u³` (ε⁶) components that **cancel
> in the scalar sum** `Σ_λ` — because the rotation channels and growth channels
> (per #1742's sign split) carry opposite-sign higher-order terms — but
> **survive** if `τ` acts **per block** (via the per-λ q-Reeb phase
> `θ_λ = arccos(χ^λ/d_λ)`, or per-block `|χ^λ(q₀)|`), summed *after* the
> nonlinear step.

- **If the `u³ε⁶` component exists per-λ and cancels in `Σ_λ`:** the collapse
  **is** the artifact. Observe-last (per-λ `θ_λ` or `|χ^λ|`, then sum) recovers
  `c_3` at the right order **with no fitted amplifier** — a genuine mechanism,
  and exactly the "observe last" the cheat-sheet predicts.
- **If no per-λ `u³` component exists:** S2 is **refuted** as the order-gap
  source; the amplification is genuinely elsewhere (consistent with #1887's
  brane-tower refutation). A clean negative that closes the lever.

Either branch is a *derive-or-refute* structural result, not a curve fit.

## Probe design (for a focused compute session)

1. **Per-λ data over ℚ(q)** for the canonical proton `𝓑_p` and neutron `𝓑_n`
   braids, `λ ⊢ 3` = {(3), (2,1), (1,1,1)}: `y_λ(q)`, `χ^λ(𝓑_p)`, `χ^λ(𝓑_n)`,
   `d_λ`, `θ_λ = arccos(χ^λ/d_λ)`, and the rotation/growth label `sign(χ^λ(q₀)·χ^λ(q₀⁻¹))`.
   Sources: `y_lambda_wenzl_bridge.py`, `hecke_characters.chi_lambda_braid`,
   the Phase-5l.1 closed-form `χ^λ` Laurent rationals.
2. **Order expansion** of each per-λ summand in `u = b·ℏ_q²` to `O(u³)`; record
   the `u^k` coefficient **per λ** and per channel.
3. **Cancellation test:** scalar `Σ_λ y_λ Δχ^λ` order structure vs the per-λ
   structure — does a `u³` term exist per-λ that **cancels** in the sum?
4. **Observe-last variants:** `Σ_λ y_λ |χ^λ(q₀)|` and `θ_λ`-weighted forms;
   compare their `u`-order + cross-anchor swing to `c_3`.
5. **Swing-lock cross-check (vs #1887):** proton vs muon `q₀` — does an
   observe-last form carry the `0.02375` `c_3` swing **structurally**, without a
   fitted `ℓ`? (If yes, it evades #1887's fixed-ℓ refutation precisely because
   the per-λ collapse, not a scalar f-map, is the mechanism.)

## Discipline gates

- **3-calibration; NO 7th fit** — this is a structural derive-or-refute test.
- **Fibre vs observation (the whole point):** per-λ `θ_λ` / bar lives in the
  **fibre**; the observation is `|χ^λ(q₀)|` at `Im(q₀)=0` (per #1742). Collapse
  **last**; never bar-ify the observation.
- **Im(q) / regime discipline:** growth channels are `arccosh` (imaginary
  `arccos`) — keep the rotation/growth split explicit, never silently `.real`.
- **Report TIERED** (proved / near-match / fitted); nothing wired to production;
  `c_3` stays cal-anchored.

## Cross-refs

- Cheat sheet **§9.2** (the lever), **§4** (`Φ_q`/`Li_2^q` bar-parity), steps 5/6/9.
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — residue A ≈ 1.804e-15.
- [`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`](2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md) — parent strategy menu (this is S2+S3).
- PRs: **#1887** (bar-odd source + f-map refutation), **#1742** (observation = `|χ(q₀)|`, growth-channel split), **#1839** (C-finite `c_k`), **#1521** (α_EM Habiro), #1593 (ε-order gap), #1739 (f-map keystone).
