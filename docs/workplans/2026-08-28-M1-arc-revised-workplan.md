# M₁ > 0 arc — revised workplan (2026-08-28)

**Epic:** `qou-x631` · **Gap:** `qou-k5r5` · **Branch:** `claude/m1-genus-source-unblock-2026-08-28`
(PR #5882) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged.

Revised after a 5-day gap in which main advanced ~29k commits. Goal of the arc: prove
`M₁ = Cov_Planch(Σ_□ h(□), Σ_□ c(□)²) > 0` for **all n** — the sole open input of the Δ_λ
super-exponential growth bound (`WstdSuperExpBound.lean`, via the `D_of_T3_nonpos` reduction).

## DONE (merged to main — do NOT re-derive)

- **`κ = 128/(225π²)` DERIVED** (IO Kerov-CLT Chebyshev-mode integral; PR #5428). `M₁ ~ κ n^{5/2}`.
- **Reduction to a one-sided bound:** `M₁>0 ∀n ⟸ (exact M₁>0 for n≤12) ∧ (κ_n ≥ κ for n≥13)`, where
  `κ_n = M₁/n^{5/2}`. Crossing pinned exactly at `n₀ = 13`. The `M₁=Cov(T,ω₃)` "Λ*-peeling"
  sub-result was **RETRACTED as vacuous**; the one-sided form is the live target.
- **`M₁ > 0` exact for n ≤ 67** (exact `Fraction`).
- **`M₁ > 0` Lean-proved for `3 ≤ k ≤ 8`** (`m1_pos_of_le_eight`, `decide`, sorry-free).
- **Fulman P−N reduction:** `M₁ = P − N`, `P=Cov(Σ|c|,ω₃)≥0`, `N=−Cov(ΣD²,ω₃)≥0`; `N/P → 0.6605 < 1`
  asymptotically (finite-n open).
- **Genus route UNBLOCKED (2026-08-28):** `pymupdf` extracts the in-repo Śniady source; Thm 4.13/4.14
  (§4.5) transcribed; target fixed as **`M₁ = Cov_Planch(Σh, R₄)`** (`ω₃ = R₄+R₂`, `R₂=n`
  deterministic). Genus applicability established (both legs polynomial-on-Young-diagrams — unlike the
  eliminated dim-tilt kernel). **Not executed.**
- **NEW general-n Lean substrate** (siblings, 2026-08-23/24): `PlancherelSnData` inhabited ∀n
  (`PlancherelSnDataGeneral.lean`); `secondMomentKernel_eq_zero (k)` ∀k
  (`SecondMomentKernelVanishes.lean` — the mean-zero identity `Σ_λ(f^λ)²ω₃=0`, was `decide` k≤20);
  `RSK_substrate_axiom` discharged to a theorem; `ContentSqSumBridge`. **First-moment / dim²-sum
  infra — it does NOT provide a Plancherel covariance, a free cumulant beyond `R₄=3ω₃−k`, or any
  second-order object.**

## THE OPEN NUB (unchanged)

Prove `κ_n − κ ≥ 0` for `n ≥ 13`, i.e. the **sign of the genus-1 second-order correction to
`Cov_Planch(Σh, R₄)`**. The order (`n^{-1/2}` bulk vs `n^{-2/3}` edge vs mix) is **undetermined** at
reachable n (measured effective exponent still rising, ≈0.25→0.36 over n=40..64). Empirically the sign
holds for every 13 ≤ n ≤ 67; the proof is a genuine second-order Plancherel-fluctuation problem.

## Revised plan — four tracks

### Track A (PRIMARY) — execute the genus-1 sign of `Cov(Σh, R₄)`

- **A1.** Express `Σh = ½(p₂(λ)+p₂(λ'))` in free cumulants `R_k` (the `p₂`-type Kerov polynomial;
  bounded, the R_k↔power-sum dictionary is standard). *Effort: low–med. Risk: low.*
- **A2.** Assemble the **joint second-order Plancherel structure** of the R_k entering `Cov(Σh, R₄)`.
  This is the crux: IO Kerov-CLT gives genus-0 (= the derived `κn^{5/2}`); the genus-1 correction needs
  the second-order fluctuation cumulants (Śniady Thm 4.14 is the *deterministic* character↔cumulant
  relation; the Plancherel averaging beyond leading order likely needs the Dołęga–Féray / Śniady
  second-order apparatus, not Thm 4.14 alone). *Effort: HIGH. Risk: HIGH — may stall; bean the gap
  honestly if it walls.*
- **A3.** Compose A1+A2 → **order + sign** of `κ_n − κ`. *Gated on A2.*

### Track B (PARALLEL, CHEAP) — sharpen the exact window to GUIDE Track A

- **B1.** Extend exact `κ_n` beyond n≤67 (direct Plancherel sum feasible to ~n≤85–90; `p(85)≈10⁸`
  partitions — bounded-but-slow, log per compute-audit discipline) to sharpen the effective-exponent
  measurement. This does **not** prove the sign but tells Track A which order to expect (de-risks A3).
  *Effort: low. Risk: none. NO float64 — exact Fraction.*

### Track C (LONGER-HORIZON, LEAN) — leverage the new general-n substrate

- **C1.** Assess whether `PlancherelSnDataGeneral` + `secondMomentKernel_eq_zero` can be extended to a
  **second-moment / covariance** statement (`Σ_λ (f^λ)² Σh·ω₃` general-n) — the Lean vehicle for M₁'s
  exact finite-n form. The substrate is first-moment today; a covariance extension is a real
  formalization project. *Lower priority — the analytic sign (Track A) is the blocker, not the Lean.
  Effort: high. Risk: med.*

### Track D (ALTERNATIVE to A2) — Fulman finite-n bound

- **D1.** Fulman (`arxiv-math-0305423`) exchangeable-pair / Stein gives finite-n error bounds. If Track
  A yields `κ_n≥κ` for n≥N₀, D1 (or the exact check B) closes `13≤n<N₀`. Independently, Fulman's Stein
  bound might give a self-contained finite-n positivity without the full genus derivation.
  *Effort: med–high. Risk: med. A genuine alternative if A2 walls.*

## Recommended sequencing

**A + B in parallel** (B guides A's order prediction), D held as the fallback if A2 walls, C as a
longer-horizon Lean consolidation. If A2 hits the "genuine analysis project" wall the bean already
names, the honest outcome is an explicit bean gap + the standing **"asymptotic (κ>0 derived) +
exact-finite-check (n≤67, extend via B)"** status — which is a defensible, non-laundered position, not
a failure.

## Honest scope

Nothing here claims the sign or order. The arc's *rigorous* content is: `κ>0` derived, `M₁>0` exact to
n≤67 + Lean k≤8, reduced to a one-sided second-order sign whose proof is the open nub. This plan makes
the nub concrete and sequenced; it does not pretend it is closed.
