# 1 ppQ deep analysis — traced step-by-step through the canonical derivation chain

**Date:** 2026-07-13 · **Branch:** `claude/onepq-deep-analysis-2026-07-13` ·
**Owner directive:** "how can we close 1ppq — do deep analysis, look at canonical
derivation cheat sheet; (a) (b) (c) NO FLOAT." · **Tier:** strategic analysis +
one live L1 measurement + one coordination-hub staleness fix. No c_k wired; no
calibration change; scope-(a) throughout.

## 0. The governing structural fact

**A prediction cannot beat the calibration input it rides on.** Everything below
follows from tracing *which chain step injects the calibration* into each
observable:

- Steps 1–8 live in `ℚ(q)` — **exact, no precision cost** (the pre-Archimedean
  chain has no floats and no experimental inputs by construction).
- Step 9 (Archimedean realization at `q₀`) is where CAL-1/2/3 enter. An
  observable that keeps a CAL scale is **floor-limited** (~780 ppb, CAL-2); an
  observable where the calibration **cancels** (dimensionless, pure-q₀) has floor
  ≈ q₀'s own precision (~0.06 ppb) — **1 ppQ-capable**.

So "closing 1 ppQ" decomposes into exactly three strands (the owner's a/b/c):

## a) More calibration-cancelling dimensionless predictions — flagship α_EM

- **Where it sits in the chain:** α_EM is *not* one of the step-11 observables —
  it is derived off the same fibre data via the Rogers–Turaev / Bring-measure
  program, and the calibration cancels. Floor ~0.06 ppb < σ_α = 0.15 ppb ⇒
  1 ppQ-capable.
- **Live state:** proton anchor + *derived* Schwinger `(1−h²α)` → residual
  **+0.313 ppb ≈ 2.1× σ_α** (#3625) — the closest not-yet-met observable to its
  target in the entire framework.
- **The gap is a derivation gap, not a wall:** the missing 2-loop
  `c₂ = resid/α² ≈ 8.1e-4` is uncomputed (and ≠ Ohtsuki κ₁ — the form-ladder
  caveats apply; it must be *derived*, not plugged).
- **Verdict:** the single highest-value tractable 1 ppQ move in the corpus.
  Deriving `c₂` from the RT phase-4 program closes the fine-structure constant
  structurally. Second candidates in the same class: further meson ratios
  (m_K/m_π already met), m_μ/m_e (pure-q₀ but currently the 9.5σ μ–p tension
  carrier — a *physics* question, not a precision one).

## b) The two deep enablers (long game)

1. **Substrate derivation of q₀** (Subgoal-2, open-for-all since 2026-07-11).
   Only this removes the ~780 ppb CAL-2 floor under **absolute** masses
   (m_p 437×, m_n 416×, Q_β 160×, Δ_pn 159× — all floor-limited; the dashboard's
   5 misses are *structural*, not derivation laziness). Route: the s5-so3
   keystone geometric `W_λ` build (steps: fibre residue #3677, categorical
   fibre→observable explication #3681 — both landed this window).
2. **The volume conjecture** (`conj:kashaev-volume-conjecture`). The binding
   scale is `m_e·Vol` ([ledger](../coordination/binding-scale-is-hyperbolic-volume.md));
   until the conjecture is proved (or the identification is derived another way)
   every binding prediction is **conditional** — 1 ppQ binding numbers cannot be
   *certified* on a conjectural scale. (Chain steps 9b/10; the θ_λ-contraction
   unification #3748 makes this the single scale question.)

## c) NO FLOAT — the L1 certification leg (measured live today)

Ran `cross_check_trM_1ppb.py` on this branch (2026-07-13):

| object | methods | |Δ|max | status |
|---|---|---|---|
| proton | Hoefsmit / peel / chi-cache | **9.3e-50** | ✅ 1 ppQ certified |
| neutron | same 3 | **3.3e-50** | ✅ 1 ppQ certified |
| D, T, ³He | + Habiro | 1.8e-4 | "OK (cb≠)" — **color-blind legs**, convention not float |
| ⁴He | (no Hoefsmit) | — | **UNCERTIFIED** |

**The float64 era is over on the atomic path:** the 2026-06-29 peel fix removed
the last float64-q₀ substitution; single-nucleon traces now cross-certify at
~1e-49 (three independent methods). What remains is **not** float:

> **Correction (same day, on closer read of the script):** the nuclei are in
> better shape than the table's "cb≠" reads. The TWO color-weighted exact
> methods (peel + chi-cache) already agree at ~1e-50 on D/T/³He — both build
> the `bring_color_weighted` trace as exact sympy evaluated at the 50-digit q₀
> — so **D/T/³He are 2-method 1 ppQ-certified on the canonical convention.**
> The 1.8e-4 is only the *informational* gap vs the color-blind Hoefsmit/Habiro
> legs (`TOLERANCE_PEEL`, expected, not gated).

1. **Third-method independence (defense in depth):** peel + chi-cache share the
   `Σ y_λ χ^λ` definition (a common χ-engine error would be invisible; the
   closed-form character anchor covers the χ engine) — a genuinely independent
   color-weighted third method (color-weighted Hoefsmit-mpfr) would harden it.
2. **⁴He:** genuinely UNCERTIFIED — chi-cache partial, no H₁₂ Hoefsmit; needs
   the H₁₂ run (compute cost + Rust kernel, not float).
3. **Sandbox note:** the script's final closed-form anchor stage requires
   `pyhecke_native` (Rust), absent here — the certification of that stage runs
   in CI/dev envs, not this sandbox.

**NO-FLOAT rule going forward** (per owner): any new hot-path compute for L1/L2
work uses exact ℚ(q)/sympy or mpf(≥50 dps) end-to-end — `_precision.py` default;
float64 only in non-witness diagnostics. (The compute-author skill already
mandates this; today's measurement confirms the stack complies on atoms.)

## The chain, annotated for 1 ppQ (steps 1–11)

| step | 1 ppQ relevance |
|---|---|
| 1–8 (`ℚ(q)` fibre) | exact; no action. Lean debt only (step 3 axioms cited; step 8 `conj:` classical limit) |
| 9a absolute mass | **floor-limited** (CAL-2 ~780 ppb) → strand (b1) only |
| 9b binding | scale conditional on volume conjecture → strand (b2); honest core = bond-count (Lean-proved) + Vol; **coordination-hub row was STALE** (still advertised the refuted CKRecursion "sub-1ppq" — fixed this PR) |
| 10 SDP | exact selection; LP-dual infra in place |
| 11 Q_β | rides CAL-2 (floor 780 ppb → experimental lever: σ(Q_β) 0.024 eV would arbitrate μ–p, #3691 route 3) |
| off-chain dimensionless (α_EM, ratios) | **the 1 ppQ frontier** → strand (a) |

## Staleness fix included in this PR

The §0 9b row still claimed the NA-Stokes/CKRecursion closure "🟢 derived
(mathematically closed) … sub-1ppq" — contradicting merged main (#3723
adversarial review: measured split relabeled as "SU(4) differential", Lean
self-marked vacuous; `r_res ≠ 5/2`; `c_3=10/3` glyph collision). Row updated to
the honest state (bond-count core + θ_λ unification + open items). Per §0's own
rule: "update the relevant row — do not fork a parallel status doc."

## Priority order (recommendation)

1. **α_EM 2-loop `c₂`** (strand a) — 2.1× σ away; pure derivation gap; highest
   value per effort. 1 ppQ-capable *now*.
2. **L1 nuclei legs** (strand c) — color-weighted mpf variants + ⁴He H₁₂ run;
   mechanical, unblocks certifying any future nuclear 1 ppQ claim.
3. **Volume conjecture / scale derivation** (strand b2) — converts every binding
   result from conditional to certified.
4. **Substrate q₀** (strand b1) — the only path under the absolute-mass floor;
   hardest; s5-so3 keystone is the active route.
