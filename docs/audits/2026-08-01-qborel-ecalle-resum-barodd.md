# q-Borel/Écalle resummation of the bar-odd D-ladder — the value at the substrate is precise but anchor-blind (2026-08-01)

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


**Branch:** `claude/qborel-ecalle-resum-barodd-2026-08-01` · **PR:** #4519 · **Bean:** `qou-dri7` (W9)
**Probe:** [`computations/qbeta/qbeta_dladder_barodd_borel_pade_laplace_probe.py`](../../computations/qbeta/qbeta_dladder_barodd_borel_pade_laplace_probe.py) (exit 0)
**Witness:** `computations/qbeta/qbeta-dladder-barodd-borel-pade-laplace.witness.json`
**Lean:** [`content/quantum-observable-universe/lean/QOU/QBeta/BarOddLadderEdgeSuppression.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BarOddLadderEdgeSuppression.lean) (sorry-free; hand-audited, machine-validation disk-blocked in this sandbox)
**Tier:** numerical scope-(a) + a sorry-free structural lemma · **Discipline:** no fit, no c_k wired, nothing to production, no tier change.
**Distinct angle vs sibling `qou-fgte`** (Stokes-3 extraction of A_ω from large-order growth, branch `claude/stokes3-identification-aomega-2026-08-01`): fgte *extracts the Stokes constant*; this probe *resums the series to a value* and adjudicates Borel-summability.

## The bar-odd D-ladder — what it is

`D(ũ) = Σ_k d_k ũ^k`, with `d_k = a_k + b_k√3 ∈ ℚ(√3)` exact (k = 1…21 at ORD 43;
canonical producer `qbeta_dladder_generating_function_structure_probe.build_d_ladder`).
It is the bar-**odd** part of the regularized neutron−proton net symbolic quantity,
extracted by the bar-involution parity projection `O = (logR − logR∘φ)/2` then divided
by `h = q − 1/q`. It carries the **c₃ bar-odd swing** of Q_β — the S-channel /
Im(deformed volume) / `sinh` partner of the bar-even (`cosh`) meson scale.
The generating variable `ũ = q·b·ℏ_q²` (`b = √(q⁴+q²+1)/(q²+1)`) evaluates to
**ũ₀ ≈ 0.00945** at the real substrate q₀ ≈ 1.10998.

## Current q-Borel corpus state (before this probe — very mature, ~180 commits)

The ladder is **super-exponentially divergent (radius → 0), q-Gevrey with a *drifting*
index** (log-fit C ≈ 0.06, Borel–Leroy s\* ≈ 0.20, local index C_k ≈ 0.63 falling —
no single Gevrey order). A dozen+ prior probes exist:

- **substrate meridian**: optimal-truncation least term pinned at the ladder **edge**,
  δ_np ≈ 5·10⁻²⁷…⁻³⁹ (suppressed, **anchor-blind**) — `qbeta-dladder-fibre-branch-stokes-ambiguity`.
- **fibre branch** (|q|=1, ũ~O(1)): Stokes ambiguity **unsuppressed** above `r* = |d₃₀/d₃₁| = 0.1475`;
  A_eff **drifts** ⇒ two-critical-time / accelero-summable, not single Borel.
- **odd-channel Borel–Leroy s-scan**: s-dependent pole (0.147→0.249), **no fixed-order clean action**
  (`qbeta-odd-channel-stokes-borel`); even-channel Vol/π method does **not** transfer.
- **single-instanton extraction**: growth FORM unresolved at k=41, (κ,A) length-blocked.
- **accelerator composition (Lean-proved)**: fixed-order Borel–Leroy composition adds orders
  (ℤ-multiples of the base) — can **never** reach an incommensurate critical time
  (`QOU.QBeta.DLadderAccelerationComposition`). A genuine non-commutative Écalle accelerator is necessary.
- **Borel–Padé Laplace to a VALUE** was done only for the **even** κ-tower
  (`qbeta-c3-borel-pade-resummation`: A = Vol(4₁)/π, Im 𝔙_b = 0.05545, off-axis ⇒ summable).

**The gap this probe fills:** the even-tower Borel–Padé→Laplace→value→on/off-axis-summability
treatment had **never** been carried out for the **odd** ladder.

## What this probe does (the odd-ladder analogue)

At the real substrate ũ₀ ≈ 0.00945:

1. **Direct superasymptotic value** — partial sums `S_N = Σ_{k≤N} d_k ũ₀^k`, optimal
   truncation N\*, least term δ_np.
2. **Classical Borel–Padé[m/m] + Laplace** — `B(ζ)=Σ d_k ζ^k/k!`, diagonal Padé,
   `V_B = ∫₀^∞ Padé(ũ₀ s) e^{-s} ds`, residual vs S_opt, nearest Borel pole ζ\* (on/off ℝ⁺),
   order stability m=2…5.
3. **q-Borel (theta kernel)** coefficient class `d_k/q₀^{k(k-1)/2}`.
4. **1ppQ verdict** + anchor-blindness cross-ref.
5. **Cross-check** `|Im(h₀·D(ũ₀))|` vs the swing S ≈ 0.0097.

## Results (scope-(a); exact ℚ(√3) rungs; mpmath 60 dps)

| quantity | value |
|---|---|
| resummed value `S_opt = Σ d_k ũ₀^k` | **−0.0166749175685** |
| least-term index N\* | **21 = edge** (anchor-blind) |
| Stokes ambiguity δ_np = |d₂₁ ũ₀²¹| | **4.92·10⁻²⁷** |
| Borel–Padé Laplace residual vs S_opt (m=2→5) | 2.9·10⁻⁶ → 9.5·10⁻⁸ → 1.7·10⁻¹¹ → **7.4·10⁻¹⁴** |
| value order-spread (top two m) | 1.73·10⁻¹¹ |
| nearest classical Padé pole ζ\* (m=2…5) | 0.663, 0.371, 1.05, 1.05 — mostly on ℝ⁺ but **|ζ\*| DRIFTS 0.65** |
| theta-kernel q-Borel `|d_k/q₀^{k(k-1)/2}|^{1/k}` | 3.74 → 2.08 (over-suppresses to entire) |
| `|Im(h₀·D)|` on the real meridian | **0** |

### 1. The value exists and is essentially unambiguous at the substrate
The classical Borel–Padé + Laplace **reproduces** the direct optimal-truncation value
`S_opt = −0.0166749175685` to residual **7.4·10⁻¹⁴** at m=5, converging order-by-order
(3e-6 → 7e-14). So the bar-odd ladder **is** summable-to-a-value at the substrate: the value
is real, single-valued, and unambiguous there.

### 2. …but 1ppQ-precise for a trivial, anchor-blind reason
The direct least term δ_np ≈ **4.9·10⁻²⁷** ≪ 1ppQ (10⁻¹⁵), and it sits at the **edge**
(N\*=21=KMAX). So the value is pinned far beyond 1ppQ by optimal truncation alone — but
because the least term is edge-pinned, the Stokes jump `exp(−A/ũ₀) ≈ δ_np ≈ 10⁻²⁷` is
**exponentially suppressed and carries no monodromy datum**. The resummed number is precise
and **anchor-blind**: it reproduces the perturbative sum but says nothing about the c₃ swing.
(The Borel–Padé cross-check is limited to ~11–14 digits by the 4 available Padé orders at 21
terms — it *confirms* the value, it is not the source of the 1ppQ precision, which is the
optimal truncation.)

### 3. Borel-summable or ambiguous? — no genuine on-axis obstruction; no single classical action
The classical Padé poles land near ℝ⁺ but **drift** across order (|ζ\*| spread 0.65,
0.37→1.05) — the **Froissart-spurious** signature of applying a classical (single-k!) kernel
to a sub-factorial q-Gevrey series. This is **not** a clean Stokes singularity, so the naive
"on-axis pole ⇒ ambiguous" reading would be an over-claim. The genuine, real-axis Stokes
ambiguity is δ_np = exp(−A/ũ₀) itself — real but exp-suppressed at the substrate, and O(1)
only on the fibre (|ũ|≳0.19, the corpus threshold `r*`). The **theta-kernel q-Borel** goes the
other way — it **over-suppresses** the coefficients to an entire function. So **neither** the
classical kernel (spurious drifting poles) **nor** the naive theta q-Borel (entire) isolates a
single instanton action, exactly matching the corpus verdict that a genuine **two-critical-time
Écalle accelerator** is required and that fixed-order transforms cannot reach it
(Lean-proved, `DLadderAccelerationComposition`).

### 4. Cross-check confirms the swing is fibre-borne
`|Im(h₀·D(ũ₀))| = 0` on the real substrate meridian (h₀, D both real there) — consistent
with the corpus: the c₃ swing is not carried on the real meridian; it lives on the fibre.

## Honest headline

- **The bar-odd D-ladder resums to a definite value at the substrate,** `S ≈ −0.0166749175685`,
  reproduced independently by direct optimal truncation and by Borel–Padé Laplace (residual
  7·10⁻¹⁴). **1ppQ is met at the substrate — but trivially and anchor-blindly** (δ_np ≈ 10⁻²⁷,
  edge-pinned). Resummation delivers no new physics *here*.
- **The ladder is not cleanly single-instanton Borel-summable.** Classical Borel–Padé gives
  Froissart-spurious drifting poles; theta q-Borel over-suppresses to entire. The genuine
  Stokes datum (c₃ swing / A_ω) is exp-suppressed on the substrate and unsuppressed only on the
  fibre, where a **two-critical-time accelerator** — provably unreachable by fixed-order
  transforms — is needed. This *confirms and quantifies* the standing corpus verdict, now with
  an explicit back-summed value + residual for the odd ladder for the first time.

This is the **honest negative** the owner asked for: the summation-to-a-value route succeeds
numerically at the substrate but is anchor-blind, so it is **not** an Option-1 path to a
*physically informative* 1ppQ c₃ — that still requires the fibre-branch accelerator (sibling
fgte's Stokes-extraction angle, converging on the same accelerator need).

## Formalize-first — the Lean lemma

`BarOddLadderEdgeSuppression.lean` (sorry-free, generic `[LinearOrderedField R]`) proves the
**structural reason** the value is anchor-blind:

- `barOdd_leastTerm_at_edge` — if `x` is below every rung-ratio radius (`c_{k+1}·x ≤ c_k`,
  k<n), the magnitudes `t_k = c_k x^k` are antitone on `[0,n]` and the minimum is the **edge n**;
  i.e. δ_np is the *smallest* rung, maximally suppressed.
- `barOdd_ratio_exceeded_of_not_edge` — the falsifiable converse: least-not-at-edge ⇒ a rung
  radius was crossed (`∃ k<n, c_k < c_{k+1}·x`), the substrate↔fibre transition (`r* = |d₃₀/d₃₁|`).

*Machine-validation note:* `lean-verify` (lean-direct) could **not** run in this sandbox — the
Mathlib olean cache restore hit ENOSPC (~4 GB free vs ~5 GB needed). The proofs are elementary
(`pow_nonneg`, `mul_le_mul_of_nonneg_right`, downward induction) and hand-audited, but were
**not machine-checked here**.

## Corpus-grep compliance

Prior art checked (`docs/audits/2026-07-{12,17,18}-dladder-*`, `qbeta-odd-channel-stokes-borel`,
`qbeta-dladder-{ecalle,jackson-qborel,single-instanton,parity-split}-*`,
`qbeta-c3-borel-pade-resummation`, `DLadderAccelerationComposition.lean`). The Borel–Padé→Laplace
value + residual + on/off-axis adjudication was present only for the **even** κ-tower; this is
its first execution on the **odd** ladder. No route re-opened, no refuted item re-declared open,
no c_k wired.
