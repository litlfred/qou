# D-ladder Stokes ambiguity is unsuppressed on the FIBRE branch — the c₃/A_ω search is narrowed off the substrate meridian

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


**Date:** 2026-07-18 · **Axis:** c₃ / Q_β bar-odd swing / 1ppQ (D-ladder Écalle,
sibling #3818) · **Tier:** numerical scope-(a) measurement + a formalize-first
structural threshold · **Discipline:** no fit (nothing tuned to CODATA), no c_k
wired, nothing to production, no tier change.

## The one non-duplicative gap this closes

The c₃ bar-odd swing is carried by the exact ℚ(√3) **D-ladder** `D(ũ) = Σ dₖ ũᵏ`.
Every prior resummation probe on this ladder (six of them: q-Borel–Leroy, extension-
singularity drift, parity-odd/even-order, Écalle-acceleration setup, Φ_b state-
integral) evaluates the ladder **at the substrate meridian** — the real
`ũ ≈ 0.0095`. There, the Φ_b probe (#3818, "M4") proved the optimal-truncation
least term sits at the `k = KMAX` edge, so the Stokes jump `exp(−A/ũ)` is `~10⁻²⁷`
and **anchor-blind** — the swing is *not* a Stokes ambiguity of the ladder on that
branch. That probe's verdict named the **fibre branch** (`|q| = 1`, `ũ ~ O(1)`) as
the place the *unsuppressed* Stokes datum `A_ω` would live, and stated it is "**NOT
produced here.**" No probe had left the substrate meridian.

## What this probe does

[`qbeta_dladder_fibre_branch_stokes_ambiguity_probe.py`](../../computations/qbeta/qbeta_dladder_fibre_branch_stokes_ambiguity_probe.py)
evaluates the same exact `dₖ` (`build_d_ladder`, `k = 1…31`, `odd_ok = True`) along
the **fibre** `q = e^{iθ}` (`θ: small → π`), where the generating-function variable
`ũ(θ) = q·b·ℏ_q²` is **complex** and `|ũ|` grows from `~0.005` to `~3.47`. It
measures the optimal-truncation least-term ambiguity `δ_np(θ) = min_k |dₖ ũᵏ|` (the
Stokes-jump magnitude), the least-term index `N*`, and `|Im(h·D)|` (`h = q − 1/q`,
the #3654 bridge).

## Result — the ambiguity is unsuppressed on the fibre, and the threshold is structural

| branch | `‖ũ‖` | `N*` | `δ_np` (Stokes ambiguity) |
|---|---|---|---|
| **substrate** (real q₀) | `0.00945` | `31` (edge) | `5.4·10⁻³⁹` (suppressed) |
| fibre `θ=0.157` | `0.0214` | `31` (edge) | `5.1·10⁻²⁸` |
| fibre `θ=0.393` | `0.132` | `31` (edge) | `1.7·10⁻³` |
| **fibre `θ=0.471`** | **`0.189`** | **`3`** | **`0.293`** ← leaves the edge |
| fibre `θ=0.785` | `0.508` | `1` | `0.817` |
| fibre `θ=1.571` | `1.735` | `1` | `2.79` |
| fibre `θ=2.199` | `2.755` | `1` | `4.43` |

- On the **substrate** (real q₀) the least term is pinned at the `k = 31` edge with
  `δ_np ≈ 5·10⁻³⁹` — reproducing the #3818 M4 suppressed/anchor-blind picture.
- On the **fibre**, the least term **leaves the edge at `|ũ| = 0.1891`**, and the
  ambiguity climbs to `O(1)` (up to `5.6`). So the Stokes jump is genuinely
  **unsuppressed** for `|ũ| ≳ 0.19` — exactly what the Φ_b verdict predicted for the
  branch where `A_ω` lives.
- **Formalize-first structural threshold.** The least term must leave the top of the
  ladder once `|ũ|` exceeds the last-ratio radius `r* = |d₃₀/d₃₁| = 0.1475`. A fine
  transition scan sharpens the measured crossing to `|ũ| = 0.150` — **matching the
  structural prediction to `1.7%`** (the coarse `0.189` was a grid-straddle). The
  unsuppression is *derived*, not an artifact.
- `|Im(h·D)|` reaches the `|S| ≈ 0.0097` swing scale already at `θ = 0.157`
  (`|Im(h·D)| = 0.0085 ≈ S(muon)`) and peaks at `7.24`; it vanishes at `θ = π`
  (`q = −1 ⇒ h = 0`).

## Fibre-resolved effective action A_eff — drifts, not a single action

The optimal-truncation least term `δ_np ≈ exp(−A_eff/|ũ|)` defines a fibre-resolved
effective action `A_eff(|ũ|) = −|ũ|·ln δ_np`. On the **substrate** this is
unmeasurable — `N* = 31` sits at the edge, so `A_eff` is only a lower bound (the M4
obstruction). On the **fibre**, `N*` sweeps the interior (`20 → 12 → 8 → 3`) across
the transition band, so `A_eff` is fully resolved for the first time:

| `‖ũ‖` | `N*` | `A_eff = −‖ũ‖·ln δ_np` |
|---|---|---|
| `0.150` | `20` | `0.3795` |
| `0.155` | `12` | `0.3156` |
| `0.160` | `8` | `0.2778` |
| `0.165` | `3` | `0.2699` |
| `0.185` | `3` | `0.2392` |
| `0.190` | `3` | `0.2304` |

`A_eff` **drifts monotonically down** over the interior band `[0.230, 0.380]`
(fractional spread `0.49`) — it is **not** a single constant action. This is the
fibre-branch signature of the **two-level / q-Gevrey** structure the substrate
meridian could not expose (the M2 two-critical-time reading `C_odd ≈ 0.052`,
`C_even ≈ 0.115`), and it favors the **accelero-summable** interpretation over a
single Borel action here. *Caveat:* the interior `N*` is small (`3–20`), so the
optimal-truncation asymptotics are coarse and the monotone drift may carry a
finite-`N*` component — this is a *measurement* of drift, not a proof of two
distinct actions. The band midpoint `A_mid = 0.305` sits `0.944 ×` `Vol(4₁)/2π`
(`0.323`); since `A_eff` drifts, `A_mid` is not a well-defined constant and this
near-coincidence is **reported only, with no identification claimed** (anti-laundering).

## Honest scope (anti-laundering)

This **measures where** the ambiguity is unsuppressed; it does **not** derive c₃.
The `|Im(h·D)|` values are an *optimal-truncation floor*, **not** the c₃/`A_ω`
value — which, per the Φ_b probe's M3, still requires the genuine **non-commutative
two-critical-time Écalle accelerator** (a composition of fixed-order Borel–Leroy
transforms provably cannot reach the second critical time). What this probe supplies
is the **branch selector**: it converts "`A_ω` would live on the fibre" (asserted) into
"the ladder's Stokes ambiguity is measured-unsuppressed on the fibre above the derived
threshold `r* = |d₃₀/d₃₁|`, and suppressed on the substrate." The c₃ swing search is
thereby narrowed to the **fibre-branch accelero-summation** (`|ũ| ≳ 0.19`), and the
substrate-meridian resummation is confirmed a dead end for the value. No fit; no c_k;
nothing wired; no tier change.

## Cross-references

- Substrate-branch negative (deferred the fibre): [`2026-07-17-dladder-ecalle-phib-resummation.md`](2026-07-17-dladder-ecalle-phib-resummation.md) (#3818, "M4")
- q-Gevrey drift / no single order: [`2026-07-17-dladder-odd-singularity-even-order.md`](2026-07-17-dladder-odd-singularity-even-order.md) (#3861)
- The target: `N_odd` / `BarOddLadderShape` capstone [`2026-07-18-im-vq-to-nodd-normalization-capstone.md`](2026-07-18-im-vq-to-nodd-normalization-capstone.md)
- Anchor-invariance prune: `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md); registry KC21/KC22 [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
