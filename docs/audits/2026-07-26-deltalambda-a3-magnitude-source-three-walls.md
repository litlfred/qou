# Δ_λ A=3 magnitude source — three independent 0-fit routes, three honest walls

**Date:** 2026-07-26
**Branch:** `claude/deltalambda-a3-magnitude-source-walls-2026-07-26`
**Supersedes the tangle:** consolidates the three route branches
`claude/deltalambda-{s5so3-wlambda-lift,cable-width-brane-tower,a4-helium-cluster}-2026-07-26`
(PRs #4370 / #4371 / #4374) after a shared-working-tree collision cross-contaminated
their commits. Each route's Lean was re-extracted, **re-verified sorry-free by
lean-direct (exit 0)**, and landed here on one clean branch. The three draft PRs are
closed in favour of this one (per AGENTS.md "combine related work into one branch / one PR").

## The gap being attacked

`#4364` (`BorromeanMagnitudeLift`, merged) lifted the derived A=3 3-body cluster
magnitude to the `H₉` joint-trace level via width-3 cabling, reaching
**`c₃ = +0.297 MeV = 0.63× μ₃`** (`μ₃ = +0.4708`, `AdditiveResidualSimplex` #4320) —
a `~1.6×` **near-miss**, 0 fit, `O(h⁴)` confirmed. `lift_is_coefficient_ratio` proved
the residual is a **coefficient** question (a lift/re-weight rescales `κ`, the shared
`h⁴` cancels — it can never change the leading `h`-order). Three routes were dispatched
to ask whether a **substrate-derived** coefficient closes the `1.6×` at **0 fit** — or
whether the source is genuinely open.

All three ran forward, 0 free parameters, `μ₃`/AME/CODATA never inverted, nothing wired.

## Route 1 — s5-so3 keystone `W_λ` re-weight → WALL (scope-a), overshoots 33×

`ρ_F` normalizes the Wedderburn blocks `λ ⊢ 9` with the **production** weight `y_λ`
(Wenzl principal specialization). The s5-so3 keystone posits the geometric
Ocneanu / q-Plancherel weight `W_λ = d_q(λ)² / [n]_q!` (`Σ_λ W_λ = 1`). Re-weighting
`y_λ → W_λ` on the **identical** `H₉` cabled-Borromean word `(Δ_A·Δ_B⁻¹)³`, same `E₀`,
same `|χ_λ|` (only the weight system changes) is a coefficient rescale
`r = κ_W/κ_y`; the route closes iff the derived `r = μ₃/v_y ≈ 1.585`.

| weight | `c₃` (MeV) | vs `μ₃` |
|--------|-----------|---------|
| `y_λ` (production, #4364) | +0.297 | 0.63× |
| **`W_λ` (q-Plancherel keystone)** | **+15.63** | **33.2×** |

Derived ratio **`r = 52.6`** vs needed `r* = 1.585`. `W_λ` **massively overshoots** —
the wrong order, not the missing `1.585×`. A closing coefficient always exists
mathematically (`κ★ = μ₃/(E₀h⁴)`), but it is neither `y_λ`'s nor `W_λ`'s derived value.

- **Verdict: WALL(scope-a)** — `W_λ` re-weight ≠ target order; magnitude source open, 0-fit.
- Lean: `QOU.MassTheory` `S5So3WLambdaLift.lean` (sorry-free) — `reweight_is_coefficient_ratio`,
  `clusterMagnitude_reweight`, `route1_closes_iff_ratio_eq` (closure = the coefficient
  identity `r = μ₃/v_y`). RESULT (`r=52.6`) in the witness.
- Witness: `computations/deltalambda/s5so3-wlambda-borromean-lift.witness.json`
  (`r_derived=52.62`, `r_needed=1.585`, `closes=false`, `free_parameters=0`).

## Route 2 — derived cable width / brane-tower level → WALL (scope-a), width-3 is derived but is the near-miss

Is the per-nucleon cable width `w` (hence the level `H_{A·w}`) **derived**, and does the
derived level close the residual 0-fit? The derived width of a nucleon is **`w = 3`** —
the `SU(3)_color` / three-quark strand count (`n₀ = 3A` atomic-braid rule). That is
**exactly** `#4364`'s width, so the derived level is `H₉` and the derived magnitude is
`0.297 ≠ μ₃`. **The derived width does not close the residual** — but it also confirms
`#4364`'s width-3 was *principled*, not chosen to hit a target.

The one corpus candidate for a derived level `≠ 9` — the brane-tower rule
`n★ = ℓ·n₀ + k` (`conj:brane-level-selection`, GAP-A-3) — is a deprecated internal
negative (2026-05-09 `probe_phiq_n_star_rule.py`, diverges `10⁵–10⁷ %`), and its failure
direction is **overshoot** (deeper levels blow the magnitude up, as
`lift_is_coefficient_ratio` predicts). So no derived rule that *raises* the level helps.

- **Verdict: WALL(scope-a)** — the derived (color) width gives the near-miss; closing
  needs a strictly larger `h⁴`-coefficient (`ratio μ₃/0.297 > 1`, proved) which no
  substrate rule supplies; selecting a width to hit `μ₃` is a fit, declined.
- Lean: `QOU.MassTheory.CableWidthBraneTower` `CableWidthBraneTowerLift.lean` (sorry-free)
  — `derived_level_A3`/`level_is_H9_of_rule` (width-3 ⇒ H₉ derived), `derived_width_not_closes`,
  `closing_needs_larger_coefficient` (`κc/κ₉ = μ₃/0.297 > 1`), `cable_width_wall`.
  Cites `#4364`'s already-witnessed `0.297`; no new witness.

## Route 3 — A=4 (⁴He) extension → WALL (scope-b, conditional on τ≤1): the A=3→A=4 sign SWAP

Does the same 0-fit Borromean-lift recipe reproduce the ⁴He 4-body residual? The derived
A=4 target (forward AME − model, `AdditiveResidualSimplex` #4320) is
**`μ₄ = −4.591 < 0`** — the closed `[1⁴]` SU(4) supermultiplet / α-cluster **saturation**
signature (`μ₄ = s₄ − g₄`, the graded reference's `g₄ = +8.37` over-subtracts). It is
**negative**, unlike `μ₃ = +0.4708 > 0`.

The A=4 Brunnian analog realized the SAME way — a trace deficit against the unlink
`c₄ = E₀·(1 − τ_L₄)` — is a **binding** object: whenever `τ_L₄ ≤ 1` (the invariant #4360
proved for the bare Borromean, `1 − τ_Borr = h⁴(3+h²)/(h²+4) ≥ 0`) the cluster is
`c₄ ≥ 0`. But the derived target is `μ₄ < 0`. Hence a non-negative Brunnian deficit
`≠` the derived `μ₄ < 0` — the recipe **walls on SIGN at A=4**.

Read with #4354 (`μ₃>0` excludes the `≤0` multiplicative cluster) this is a **sign SWAP**:

| residual | derived sign | Brunnian deficit (≥0) | multiplicative cluster (≤0) |
|----------|:---:|:---:|:---:|
| μ₃ (3-body) | **+** | ✓ (#4360) | ✗ (#4354) |
| μ₄ (4-body) | **−** | ✗ **(this route)** | ✓ (#4354) |

No single sign mechanism reproduces both isotopes: the Brunnian (binding) operator
selects A=3, the multiplicative (saturation) operator selects A=4. The A=4 α-cluster
residual is a structurally **different** object — a saturation term, not an
irreducible-binding term.

- **Verdict: WALL(scope-b, conditional on `τ_L₄ ≤ 1`)** — a *proved* sign exclusion
  citing the #4360 non-negativity invariant. The A=3 → A=4 step changes the residual's
  *sign*, so the derived Borromean-deficit recipe does not carry across it.
- Lean: `QOU.MassTheory` `HeliumFourBodyCluster.lean` (sorry-free) — `mu4Residual_neg`,
  `brunnian4Cluster_nonneg`, `mu4_ne_brunnian4Cluster` (the sign wall),
  `sign_swap_a3_a4` (capstone), `lift_is_coefficient_ratio_order` (the Milnor order rises
  to `h⁶ = 2(4−1)` for a 4-component link).
- Companion probe `computations/deltalambda/helium_four_body_cluster_probe.py`
  forward-derives `μ₄ = −4.591` and validates the A=3 machinery (deficit +, order 4.053).
  **Open companion input:** measuring `τ_L₄` for a width-3 cabled 4-component Brunnian
  word at `H₁₂` is compute-heavy and the word is non-unique (the antecedent of the
  scope-(b) wall); this is why the Lean wall is stated *conditional on* `τ_L₄ ≤ 1`
  rather than unconditionally.

## Net for the Δ_λ A=3 magnitude source

Three independent substrate-derived coefficient routes, **all 0-fit, all honest walls**:

1. the geometric q-Plancherel weight `W_λ` **overshoots** (33×);
2. the derived color cable width is exactly `#4364`'s (`w=3`, `H₉`) and gives the
   near-miss — no derived level closes it, the one alternate rule is refuted (overshoots);
3. the recipe **does not extend to A=4** — the residual's sign swaps (`μ₄<0`), so the
   A=4 term is a different (saturation) object entirely.

**Nothing wired. δ_λ A=3 exact closure remains open**, and is now bracketed: the missing
`1.585×` is a genuine coefficient with **no** derived substrate value among the weight
system (`y_λ`/`W_λ`), the cable width (`w=3`), or the brane-tower level (`n★` refuted).
This is a *scope-(a)* open, not a hard exclusion — a closing coefficient exists
mathematically; it is simply not any of the three derived quantities probed. The A=4
sign-swap (Route 3) is the strongest structural finding: it says the per-isotope residual
is **not** a single mechanism, consistent with the μ₃(binding)/μ₄(saturation) split.

## Anti-fit / honesty ledger

- **0 free parameters** in every route; `μ₃`, `μ₄`, AME, CODATA never inverted.
- Every durable claim classified: Routes 1–2 **WALL(scope-a)**, Route 3
  **WALL(scope-b, conditional on the cited τ≤1 invariant)**. No FIT, no closure claimed.
- "No seventh fit-based ansatz" + PROBE-4 KL-prune stand. Nothing wired to production.
- Formalize-first honoured: each route's claim is a sorry-free Lean statement
  (lean-direct exit 0), verified in this session by the parent before landing.
