# `C_knot` is non-universal with the pinned weight — the single-factor / single-scale route is refuted

**Date:** 2026-08-02 · **Branch:** `claude/c-knot-delta-lambda-derivation-2026-08-02` · **PR:** #4556
· **Bean:** `qou-3q7t` · **Axis:** Δ_λ / `C_knot` magnitude · **Tier:** scope-(a) refutation of
single-universal-`C_knot` + scope-(b) exclusion of any level-only rescale; **no fit**; nothing wired.

> ## 🛑 CORRECTION 2026-08-21 — every number below is CONVENTION-C-FRAME, and the ⁴He one is
> ## additionally ill-conditioned. The VERDICTS survive; the MAGNITUDES do not.
>
> **(i) The figures are stale.** This document records a run made under the Markov parameter
> `z = √q/(q+1)` (convention C). The producer was refreshed to the canonical convention D
> (`z = q³/(q²+1)`) on 2026-08-11 (`70d1ade383`, bean `qou-4jut`), and the committed witness
> [`c-knot-nonuniversal-pinned-weight.witness.json`](../../computations/deltalambda/c-knot-nonuniversal-pinned-weight.witness.json)
> now reads:
>
> | K | H_n | `\|S(K)\|` conv-C | `\|S(K)\|` conv-D | `C_knot` conv-C | `C_knot` conv-D |
> |---|---|---|---|---|---|
> | D | 6 | 0.7438 | 0.71745 | 5.853 | **6.0679** |
> | T | 9 | 3.7349 | 2.47514 | 4.444 | **6.7061** |
> | ³He | 9 | 4.5883 | 3.07899 | 3.292 | **4.9054** |
> | ⁴He | 12 | 5.9456 | 0.19094 | 9.313 | **290.007** |
> | | | | | spread **2.83×** | spread **59.12×** |
>
> The mirror ratio `C_knot(T)/C_knot(³He)` moves 1.35 → **1.3671**. **Do not quote "spread 2.83×" or
> "`C_knot ≈ 5.85`" — both are superseded.** The bean `qou-3q7t` body carried the same C-era numbers
> and is corrected in the same PR. Every *verdict* in this document is unaffected and in fact
> strengthens: non-universality, the dimension-convention scan (`f^λ` still tightest), the failure of
> any single scale, and the Lean mirror-pair exclusion all hold at the new magnitudes.
>
> **(ii) The 59.12× is dominated by one ill-conditioned denominator — read §2(a) with this in mind.**
> `S(K)` is an *alternating* sum, so `|S|` can sit far below the scale of its summands. The
> cancellation ratio `κ(K) = |S|/Σ_λ|t_λ|` is the reciprocal condition number of `|S|` under per-block
> relative perturbation (`‖δ‖_∞ ≤ ε ⇒ |S′−S| ≤ ε·Σ|t| = (ε/κ)|S|`). Measured under convention D:
> κ = 0.2911 (D) / 0.4137 (T) / 0.2944 (³He) / **0.0079548 (⁴He)**. **⁴He sits on a 126×
> near-cancellation**, its largest single block term being **52× the whole signed sum**, so a 0.8%
> per-block correction moves `C_knot(⁴He)` anywhere, sign included. Re-expressed per block, the
> minimum sup-norm relative correction `δ_min^∞ = |B_AME/m_e − S|/Σ|t|` is 1.475/2.361/1.150/2.299 —
> **spread 2.05×**, every isotope needing an order-unity correction.
>
> **This does NOT rescue universality** (`δ_min` is a *lower bound* on the missing structure, and equal
> `δ_min` does not mean equal correction *direction*), and it does **not** weaken the §3 Lean
> mirror-pair exclusion (T and ³He are both well-conditioned, κ ≈ 0.29–0.41). What it says is that the
> missing per-block magnitude is an **order-unity** relative correction uniformly across all four
> isotopes — reading the 59.12× as "⁴He is qualitatively harder" is reading a coordinate artifact.
> Corroborated independently by [`threerow_4he_completion_probe.py`](../../computations/deltalambda/threerow_4he_completion_probe.py)
> (bean `qou-prjo`), which already records a ⁴He **sign change in q** for the ℓ(λ)≥3 stratum of the
> same object — a sign change is a zero, hence κ = 0 on the physical interval.
>
> Producer: [`c_knot_cancellation_conditioning_probe.py`](../../computations/deltalambda/c_knot_cancellation_conditioning_probe.py)
> (0-fit, audit-only, convention D, proton pin). PR #5406, bean `qou-3q7t`.

## 0. BLUF

Now that the binding weight is **pinned to the derived Wenzl `y_λ`** (Markov trace, PR #4543 — the
earlier "41× convention spread" was right-weight-vs-wrong-weight, resolved), the honest universality
question for the deuteron deficit `C_knot` can finally be asked cleanly. It is asked here across the
four lightest isotopes, all 0-fit:

| K | H_n | `\|S(K)\|` ⚠conv-C | `C_knot(K) = B_AME/(m_e·\|S\|)` ⚠conv-C |
|---|---|---|---|
| D | 6 | 0.7438 | **5.853** |
| T | 9 | 3.7349 | **4.444** |
| ³He | 9 | 4.5883 | **3.292** |
| ⁴He | 12 | 5.9456 | **9.313** |

**`C_knot` is NON-UNIVERSAL (spread 2.83× — ⚠ CONVENTION-C; the canonical convention-D figure is
59.12×, and see the correction banner above for why that number is ill-conditioned).** "Derive
`C_knot ≈ 5.85` as one geometric/scale factor" is refuted. The Δ_λ magnitude derivation itself stays **OPEN** (`qou-3q7t`) — this narrows the attack,
it does not close the gate.

## 1. The master formula and the convention pin

`B(K) = m_e · |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|`, with `y_λ` the Wenzl Schur-principal
weight (`markov_weights_symbolic.solve_y_lambda`), normalized `Σ_λ y_λ f^λ = tr_M(1) = 1`. The probe
recomputes `y_λ` from the Wenzl closed form and asserts `Σ y_λ f^λ = 1` (verified 1.0000 for all four
isotopes), reproducing the committed deuteron sum `Σ = −0.7438` exactly. `χ^λ(β_K)` is read from the
interface-inclusive (`include_inter=True`) Rust Hoefsmit caches `atom-chi-rust-{d,t,3he,4he}`. `sgn` is
`(−1)^{n(λ)}` (Lean-proved). `f^λ` is the hook-length SYT dimension.

## 2. Three independent 0-fit kills of the single-factor hypothesis

**(a) Non-universal.** Spread 2.83× (min ³He 3.29, max ⁴He 9.31). Even `C_knot/A` (per nucleon:
2.93/1.48/1.10/2.33) and `C_knot/(A−1)` (per bond: 5.85/2.22/1.65/3.10) are non-constant, so no
extensive or per-bond rescale collapses them.

**(b) Dimension convention doesn't fix it.** `f^λ` (hook SYT) is already the **tightest** dim choice:

| dim in `Σ y_λ χ^λ sgn · [dim]` | cross-isotope spread | T/³He (same H₉) |
|---|---|---|
| `f^λ` (hook SYT, master) | **2.83×** | 1.35 |
| `d_q(λ)` (normalized quantum dim) | 116× | 1.29 |
| none (`Σ y_λ χ^λ sgn`) | 122× | 1.32 |

**(c) No scale fixes it.** The spread is invariant under any *global* scale (m_e→E₀/μ₀ — a constant
multiplies every `C_knot`), and `log C_knot / log A ∈ {2.55, 1.36, 1.09, 1.61}` is not a clean power.
Concretely, a **deuteron-pinned 0-fit scale** (`α = B_AME(²H)/|S(D)| = 2.99 MeV = 5.85 m_e`, a
legitimate CAL since `B(²H)` is CAL-adjacent) PREDICTS the other three:

| K | B_pred (α·\|S\|) | B_AME | error |
|---|---|---|---|
| T | 11.17 | 8.48 | **+31.7%** |
| ³He | 13.72 | 7.72 | **+77.8%** |
| ⁴He | 17.78 | 28.30 | **−37.2%** |

Errors of +32% / +78% / −37% are far outside the isospin **±8%** band (ROUTE 5,
[`2026-08-01-mu3-target-robustness-audit.md`](2026-08-01-mu3-target-robustness-audit.md)). The
deuteron-pinned-E₀ route — explicitly flagged as a candidate in the task and in the E₀-options audit —
therefore **fails the cross-isotope prediction test.** (And it does *not* silently absorb the
chirality cancellation into a scale — see §4 — so there is no hidden fit; it genuinely mispredicts.)

## 3. The Lean-provable invariant: `C_knot` is not a function of `(n, q₀)`

The triton `T` and helion `³He` sit at the **same** strand count `H₉`, so any *level-only* closure
`B(K) = g(n_K, q₀) · m_e · S(K)` would force the **same** `g(9, q₀)` to reproduce both bindings from
their `S` values. The measured pairs make that impossible:

[`QOU/MassTheory/CKnotNonUniversal.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/CKnotNonUniversal.lean)
(sorry-free, lean-direct exit 0, v4.24.0; no trivial-true / native_decide / axiom):

| lemma | content |
|---|---|
| `mirror_cross_ne` | `B_T · S_He ≠ B_He · S_T` (i.e. `C_knot(T) ≠ C_knot(³He)`) |
| `no_level_only_closure` | `¬ ∃ g, B_T = g·S_T ∧ B_He = g·S_He` — no level-`H₉` rescale closes both |
| `mirror_gap_exceeds_isospin_band` | `B_T·S_He > 1.1·(B_He·S_T)` — the gap (1.35×) exceeds the ±8% band |

So `C_knot` carries genuine per-knot (isospin / mirror) content, not captured by `(n, q₀)`. This is a
**scope-(b) structural exclusion of the level-only-rescale closure class** (cited invariant
`mirror_cross_ne`); it does **not** exclude a per-knot Δ_λ derivation.

### 3a. A second, independent structural reason: the chirality regime `(−1)^{C(3A,2)}`

The mirror inequality shows per-knot variation *within* a level. A cleaner *level-parity* reason
separates the deuteron from the heavier isotopes entirely. Under conjugation the `n`-statistic obeys
the Macdonald identity `n(λ) + n(λ') = C(n,2)` (verified numerically at `n = 6`: all five conjugate
pairs flip the binding sign, the self-conjugate `(3,2,1)` is fixed), so the binding sign
`sgn(λ) = (−1)^{n(λ)}` satisfies `sgn(λ') = (−1)^{C(n,2)} · sgn(λ)` — it *antisymmetrizes* conjugate
pairs iff `C(n,2)` is odd. With `n = 3A`:

| A | isotope | n = 3A | C(3A,2) | parity | chirality regime |
|---|---|---|---|---|---|
| 2 | D | 6 | 15 | **odd** | sgn antisymmetrizes (bar-odd-projected) |
| 3 | T, ³He | 9 | 36 | even | sgn preserved |
| 4 | ⁴He | 12 | 66 | even | sgn preserved |

The **deuteron sits in a different chirality regime than A ≥ 3** — its binding-sign structure is
qualitatively unlike the heavier isotopes, a structural reason `C_knot(D)` cannot lie on the same
universal curve, independent of the mirror inequality. Lean `sgn_conj` (the exponent law, sorry-free)
+ `deuteron_chirality_regime_differs` (the concrete parity split, `decide`). *(This split explains the
D-vs-rest gap; it does NOT explain the T/³He split at fixed n=9 — that is the isospin content of §3.
The two reasons are complementary: C_knot varies both across regimes AND within a regime.)* (Structural
identity contributed by a parallel session, formalized here.)

## 4. Parallel-check corroboration (attribution: a sibling session's read-only probes, folded in per
owner request — no separate PR)

Two independent parallel checks on the **deuteron alone** (from the cached per-λ H₆ data) reach the
same "not the culprit" conclusion for weight, dimension, and known-invariant, and add a useful
constraint on the residual:

- **Dimension-normalization ruled out (parallel).** `B_cat` under `f^λ` = 0.380 (5.85×), `d_q` = 0.487
  (4.57×), signed-no-dim = 0.052 (42.7×), plain `tr_M` = 0.198 (11.2×). Every principled dim swap
  undershoots 4.6–43×; `f^λ` is already near-best. *(The parallel `d_q` deficit 4.57× and this doc's
  normalized-`d_q` spread 116× differ only by the `d_q` normalization convention — both agree dim is
  not the culprit, and neither closes it; per the parallel note's own anti-fit caveat, `d_q`'s smaller
  4.57× is not a licence to switch to it.)*
- **Sgn-cancellation decomposition (parallel).** `|Σ y_λ f^λ χ^λ|` (no sgn) = 1.662 → 2.62× deficit;
  `|Σ y_λ sgn f^λ χ^λ|` (master) = 0.744 → 5.85×. The `sgn` (chirality, Lean-proved-correct, not
  droppable) **reduces** the magnitude 1.662→0.744, a 2.23× cancellation. So
  `C_knot(D) 5.85× ≈ [sgn-cancellation 2.23×, chirality-structural, NOT scale-fixable] × [intrinsic
  2.62×]`. A **global** scale multiplies the whole sum and thus **cannot** touch the 2.23×
  chirality-cancellation floor — consistent with §2(c). Data check: `Σ f^λ = 76`, `Σ sgn·f^λ = 16 = 2⁴`,
  `Σ (f^λ)² = 720 = 6!`.

- **Framing / writhe ruled out (parallel hypothesis, tested here).** The Markov trace is a *framed*-
  link invariant; the ambient Jones/HOMFLY invariant differs by a writhe-dependent framing factor
  `~ q₀^{c·w}`, which the master formula omits — a legitimate *word-specific* (not scale) deficit
  candidate. Writhe `w(K) = #σ − #σ⁻¹` of the canonical word (averaged interface crossings are
  writhe-neutral): **`w(D) = 11−7 = 4 = 16−12 = w(T)`** and **`w(³He) = 18−10 = 8 = 23−15 = w(⁴He)`**.
  But `C_knot` differs in BOTH equal-writhe pairs (D 5.85 vs T 4.44; ³He 3.29 vs ⁴He 9.31), and the
  required exponent `c = ln C_knot/(w·ln q₀) ∈ {4.23, 3.57, 1.43, 2.67}` varies 3×. So **no writhe-only
  framing factor closes the deficit** (Lean `no_writhe_only_framing`, sorry-free). The `q₀^17 ≈ 5.85`
  numerology is a coincidence — `w(D)=4` needs a non-framing `c≈4.23`, and that same `c` fails `T`
  (flagged and ruled out per the parallel note's own anti-numerology caveat).

**Net across all checks:** the binding **weight** (`y_λ`, Markov — #4543), the **dimension** (`f^λ`),
any **single scale** (this doc §2c/§3), any **simple known invariant** (parallel), and any
**writhe/framing factor** (parallel) are ALL ruled out. The 2.83× cross-isotope residual (and the
5.85× deuteron deficit) is irreducibly **per-knot Δ_λ magnitude**, sitting in the χ^λ-magnitude / word
content, with a hard chirality-cancellation floor.

## 5. Verdict + what stays open

- **scope-(a):** the single-universal-`C_knot` / single-scale derivation route is **REFUTED** with the
  pinned weight. Confirms + sharpens
  [`2026-06-01-e0-lambda-substrate-derivation-options.md`](2026-06-01-e0-lambda-substrate-derivation-options.md):
  the χ^λ→M_λ absolute per-block scale is not a single derivable object.
- **scope-(b) (narrow):** the level-only rescale class `g(n, q₀)·m_e·S(K)` is structurally excluded by
  the T/³He mirror inequality (Lean `mirror_cross_ne`).
- **OPEN (`qou-3q7t`):** a genuine per-knot Δ_λ magnitude derivation. Surviving direction (per §4): the
  residual lives in the **per-knot χ^λ-magnitude / word content**, above a chirality-cancellation
  floor, and is **not** reachable by any weight / dimension / global-or-level scale choice. Candidate
  #1 from the E₀-options audit (per-vertex seminormal eigenphase / q-Reeb `Δθ_λ`, the only object
  provably NOT a function of `(χ_λ, y_λ)`) remains the one non-circular opening — but it too has to
  date closed only *differences*, not absolute magnitude.

## 6. Anti-fit ledger

| statement | status |
|---|---|
| `C_knot` non-universal (2.83× spread, pinned weight, best dim) | **measured, 0-fit** |
| no 0-fit dim convention restores universality (`f^λ` tightest) | **measured, 0-fit** |
| no global / A-power / level-only scale closes it | **measured + Lean** |
| deuteron-pinned scale mispredicts T/³He/⁴He (+32/+78/−37%) | **measured, 0-fit** |
| `C_knot(T) ≠ C_knot(³He)` (level-only rescale excluded) | **Lean sorry-free** |
| per-knot Δ_λ magnitude derivation | **OPEN** (`qou-3q7t`) |

`y_λ` derived (Wenzl, `Σ y_λ f^λ = 1` asserted); `χ^λ` from committed caches; `B_AME` used **only** as
a diagnostic ratio, **never** inverted into a canonical weight; `free_parameters = 0`; nothing wired;
exact mpmath (50 dps).

**Refs:** probe
[`c_knot_nonuniversal_pinned_weight_probe.py`](../../computations/deltalambda/c_knot_nonuniversal_pinned_weight_probe.py)
(+ witness); supersedes
[`c_knot_not_universal_probe.py`](../../computations/deltalambda/c_knot_not_universal_probe.py) (whose
41× was right-vs-wrong weight); PR #4543 (weight pinned); PR #4491 (`C_knot` gate).
