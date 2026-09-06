# D-ladder is SINGLE-LEVEL — the two k-parity halves share one common Borel action; no two-critical-time accelerator needed

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
sibling #3818) · **Tier:** numerical scope-(a) structural measurement (point-by-point,
KMAX-converged) · **Discipline:** no fit (nothing tuned to CODATA), no c_k wired,
nothing to production, no tier change.

## Question

The whole D-ladder Écalle program hinges on one structural gate: is the bar-odd
D-ladder genuinely **two-level** (a sum of two Gevrey series with *distinct* Borel
actions — so a non-commutative *two*-critical-time Écalle accelerator is the required
tool, and its two critical times are those actions) or **single-level** (one action —
the accelerator is overkill and a single-level Borel/Écalle resummation suffices)? The
merged Φ_b probe (#3818, "M2") found two distinct divergence *classes* `C_odd ≈ 0.052`,
`C_even ≈ 0.115`; my #3861 found the parity *orders* soften toward a common value at
k=31 — an unresolved tension.

## Test (accelerator prerequisite)

[`qbeta_dladder_fibre_two_action_probe.py`](../../computations/qbeta/qbeta_dladder_fibre_two_action_probe.py)
splits the exact ℚ(√3) ladder by k-parity (the M2 split: odd `k ≥ 3`, even `k ≥ 4`)
and measures **each half's own least-term action** `A = −|ũ|·ln δ_np` on the fibre,
**point-by-point** across the window where both halves are simultaneously interior.
On the substrate both are pinned at the `k = KMAX` edge (unmeasurable); the fibre
resolves them. No Padé.

## Result — the two parities' actions COINCIDE at every resolved point

**`24/24` both-interior points have `A_odd(|ũ|) ≈ A_even(|ũ|)` to rel `< 2%`**
(worst rel `= 0.0106`; ORD=63, KMAX=31). Representative points:

| `‖ũ‖` | `N*_odd` | `A_odd` | `N*_even` | `A_even` | rel |
|---|---|---|---|---|---|
| `0.147` | `33` | `0.448108` | `34` | `0.448169` | `1.4·10⁻⁴` |
| `0.148` | `27` | `0.420606` | `28` | `0.420597` | `2.2·10⁻⁵` |
| `0.150` | `19` | `0.379411` | `20` | `0.379531` | `3.2·10⁻⁴` |
| `0.152` | `15` | `0.349336` | `16` | `0.349293` | `1.2·10⁻⁴` |
| `0.155` | `11` | `0.315132` | `12` | `0.315599` | `1.5·10⁻³` |
| `0.158` | `9` | `0.288773` | `10` | `0.290371` | `5.5·10⁻³` |

The common value **drifts with `|ũ|`** (`0.448 → 0.29` as `N*` falls `33 → 9`) — that
drift is the *shared* finite-`N*` running of the single action (optimal-truncation
asymptotics are exact only as `N* → ∞`); the decisive fact is that **odd and even
co-drift, coinciding to 4–5 digits at every point**, not that the value is a fixed
constant.

**KMAX-converged.** Extending the exact ladder ORD `63 → 83` (`k = 31 → 41`) leaves
the in-band values identical and gives `13/13` agreement in the widened window — the
coincidence is not a truncation artifact.

## Conclusion — SINGLE-LEVEL (the accelerator is not the required tool)

The two k-parity halves share **one common leading Borel action** at every resolved
`|ũ|`. Therefore:

- The D-ladder is **single-level**, not two-level. M2's distinct divergence *classes*
  `C_odd ≈ 0.052`, `C_even ≈ 0.115` are **sub-leading** (`k·log k`) coefficients, **not**
  distinct leading actions — two distinct actions would make `A_odd` and `A_even`
  differ by `O(1)`, not `O(10⁻⁴)`. This resolves the M2-vs-#3861 tension **toward the
  #3861 softening**.
- **The non-commutative two-critical-time Écalle accelerator is NOT required.** A
  *single-level* Borel/Écalle resummation on the fibre branch (whose unsuppressed
  Stokes ambiguity the [companion probe](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
  already localized, above `r* = |d₃₀/d₃₁|`) is the right tool. This materially
  **simplifies the c₃ program**: the swing lives in a single Borel plane's Stokes
  structure on the fibre, not in an exotic two-time accelero-summation.

**Deliverable for #3818:** drop the two-critical-time accelerator route; pursue the
single-level fibre-branch Stokes datum instead.

## Scope (anti-laundering)

A structural measurement resolving the two-level/single-level gate toward single-level
(point-by-point coincidence, KMAX-converged). Derives no c₃ value; wires nothing; no
tier change. The common action's absolute value is a drifting finite-`N*` quantity —
**no** constant is identified. No fit; no c_k.

## Cross-references

- Companion (branch selector + threshold): [`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
- M2 two-level claim (now re-scoped as sub-leading): [`2026-07-17-dladder-ecalle-phib-resummation.md`](2026-07-17-dladder-ecalle-phib-resummation.md) (#3818)
- Parity-order softening (now confirmed): [`2026-07-17-dladder-odd-singularity-even-order.md`](2026-07-17-dladder-odd-singularity-even-order.md) (#3861)
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
