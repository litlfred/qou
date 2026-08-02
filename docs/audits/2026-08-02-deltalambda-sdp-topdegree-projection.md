# Does the confinement SDP / canonical `T_w` FORCE the top-degree projection? (NO — sharply-bounded structural negative)

**Date:** 2026-08-02 · **Epic:** `qou-r2nh` · **Bean:** `qou-nmpr` ·
**Branch:** `claude/deltalambda-sdp-topdegree-projection-2026-08-01` · **PR #4570** ·
**Tier:** derivation / formalize-first (Lean, sorry-free) ·
**Scope:** (a) LIMITATIVE throughout; nothing fitted; nothing wired; no anchor inverted; L2 unchanged.

- Lean: [`QOU/BraidsAndKnots/DeltaLambdaTopDegreeConcentration.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/DeltaLambdaTopDegreeConcentration.lean) — sorry-free, `lean`-direct exit 0.
- Builds on: [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean) (`nStat`, `dim`, `deltaSign`, `deltaLambda`, `deltaSign_eq_nStat_parity`) — all on `main`.
- Direct parent: PR #4559 [`2026-08-01-deltalambda-dt-substrate-derivation.md`](2026-08-01-deltalambda-dt-substrate-derivation.md) (`qou-ylot`, moduli under-determined).
- Grandparent: PR #4553 [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md) (the single-degree `dtEuler` object).

## The question (the crux)

PR #4559 proved sorry-free a **limitative** result — matching the target
`Δ_λ = (-1)^{md}·count` under-determines the Springer moduli dimension (pins only
its parity mod 2 + the count `dim V_λ`) — and isolated the exact residual
obstruction:

> the **single-degree / TOP-cohomology concentration** is load-bearing. The
> substrate's natural coinvariant grading spreads `V_λ` across the fake-degree
> polynomial `f_λ(q)`, whose signed evaluation `f_λ(-1)` is generically **not**
> `Δ_λ` (e.g. `(2,1)`: `f = q+q²`, `f(-1)=0 ≠ -2 = Δ_{(2,1)}`). Only the top /
> lowest-fake-degree Springer piece `H^{top}(𝓑_λ) = V_λ` gives the clean
> `(-1)^{n(λ)}·dim`.

**THE question (`qou-nmpr`): does the confinement SDP / canonical `T_w` FORCE
that top-degree projection?**

## Corpus / sibling state (grep + coordinate)

- **Confinement SDP / canonical `T_w` — its actual data.** The SDP-as-solver
  (`tools/hecke-engine/src/sdp_solve_canonical_t_w.rs`) minimizes `‖c‖₁` over the
  Hecke coefficients `c_w` (GB-NF basis) subject to the block-PSD confinement
  constraints `ρ_λ(T(c)) ⪰ 0 ∀ λ ⊢ n` plus a linear anchor `L·c = b`; the
  representations `ρ_λ` are the *ungraded* seminormal (Hoefsmit) matrices at
  `q = q₀` (`seminormal_matrices`). The canonical-`T_w` uniqueness chain
  (`docs/coordination/2026-05-30-sdp-uniqueness-status.md`,
  `MathlibExt/SDPRankEquality.lean`) is a *strict-complementarity rank* argument
  on those same ungraded blocks. The Markov-trace anchor
  `tr_M = Σ_λ w_λ(q)·χ_λ` (`prop:operator-selection-lp`,
  `computations/lp_dual_solver.py`) is a weighted sum of *ungraded* Wedderburn
  characters. **Every ingredient factors through `⊕_λ End(V_λ)`.**
- **`Springer` / `fake degree` / `coinvariant` in the corpus.** No Springer-fibre
  *construction* from the drivers; `Behrend` / `nilpotent orbit` introduced only
  by #4553 (now merged) / the then-unlanded #4559. The fake-degree ceiling is flagged as
  convention-dependent hidden DOF (`docs/coordination/option-e.md`, 2026-06-28) —
  corroborating that the ungraded algebraic data does not pin a distinguished
  graded realization.
- **The grade `n(λ)` is separately corpus-derived** as the Gröbner–Shirshov
  jet-order fake-degree valuation (= Lusztig a-function = b-invariant;
  `option-e.md`, 2026-07-18 front (i)) — an **independent** substrate map, NOT
  produced by the SDP.
- **Sibling coordination.** Distinct-angle intent posted on **#4559** (parent,
  `qou-ylot`) and **#4554** (the `A_ω` mirror, `qou-qnnq`). #4554 independently
  reached "structurally-open — no QOU driver forces `3` by a short structural
  argument"; this result converges to the same honest verdict by a third
  direction (grading invisibility). #4558 (general-`n` DT lift) is the forward
  extension target.

## The test — result: NO, sharply bounded (formalize-first, sorry-free)

The confinement SDP / canonical `T_w` / `tr_M` are functionals of the **ungraded
Wedderburn dimension `dim V_λ`** (and the ungraded block matrices) alone. Formalize
the obstruction at `n = 5`: encode the single-degree Springer object `G_λ`
(`dim V_λ` in degree `n(λ)`) and the full fake-degree coinvariant object `H_λ`
(graded dims = coefficients of `f_λ(q)`).

| lemma | statement |
|---|---|
| `singleTotalDim_eq_dim` | `Σ_k (G_λ)_k = dim V_λ` |
| `fakeTotalDim_eq_dim` | `Σ_k (H_λ)_k = dim V_λ` (`= f_λ(1)`) — **same ungraded dimension** |
| `single_gradedEuler_eq_deltaLambda` | `χ(G_λ) = (-1)^{n(λ)}·dim V_λ = Δ_λ` |
| `fake_gradedEuler_ne_deltaLambda` | `χ(H_λ) = f_λ(-1) ≠ Δ_λ` for every `dim V_λ > 1` block |
| **`sdp_cannot_force_top_degree`** | **∃ two graded assignments with the SAME ungraded dimension at every block but DIFFERENT signed Euler characteristics (only the single-degree one `= Δ_λ`)** |

### Fake-degree data at `n = 5` (all non-trivial blocks fail `f_λ(-1)=Δ_λ`)

`f_λ(q) = q^{n(λ)}·[5]_q! / ∏_{cell}[h]_q`; graded dims are its coefficients.

| λ | `n(λ)` | `dim V_λ` | `f_λ(q)` | `f_λ(-1)` | `Δ_λ` | concentration load-bearing? |
|---|---|---|---|---|---|---|
| `(5)` | 0 | 1 | `1` | `1` | `+1` | (trivially single-degree) |
| `(4,1)` | 1 | 4 | `q[4]_q` | `0` | `-4` | **yes** |
| `(3,2)` | 2 | 5 | `q²[5]_q` | `1` | `+5` | **yes** |
| `(3,1,1)` | 3 | 6 | `q³[3]_q(1+q²)` | `-2` | `-6` | **yes** |
| `(2,2,1)` | 4 | 5 | `q⁴[5]_q` | `1` | `+5` | **yes** |
| `(2,1,1,1)` | 6 | 4 | `q⁶[4]_q` | `0` | `+4` | **yes** |
| `(1⁵)` | 10 | 1 | `q^{10}` | `1` | `+1` | (trivially single-degree) |

Every non-`dim`-1 block has `f_λ(-1) ≠ Δ_λ`: the single-degree concentration is
load-bearing at the entire `n=5` anchor (extends #4559's single `(2,1)` `n=3`
example). The two `dim`-1 blocks are monomials (trivially single-degree), so they
agree — hence the `dim ≠ 1` hypothesis.

**Reading.** `G_λ` and `H_λ` share the ungraded dimension `dim V_λ` (`f_λ(1)`),
the entire input the confinement SDP / canonical `T_w` / `tr_M` read, yet their
signed Euler characteristics differ. So the ungraded datum does **not** pin the
graded Euler characteristic; no functional of it can distinguish — and therefore
none can **force** — the single-degree (top-cohomology) object over the fully
coinvariant-graded one. The top-cohomology projection `H^{top}(𝓑_λ) = V_λ` is a
genuinely **independent** input.

## Proved / open split

- **PROVED (sorry-free, this file):** the confinement SDP / canonical `T_w` /
  Markov-trace data — a functional of the ungraded Wedderburn dimension
  `dim V_λ` — does **not** force the top-degree concentration (two graded objects,
  same ungraded dimension, different signed Euler characteristics; only the
  single-degree one is `Δ_λ`). The SDP, as constructed, does not reach top degree.
- **OPEN (unchanged, now precisely bounded one notch further):** whether an
  **independent graded substrate map** — the a-function = GS jet-order valuation
  that already supplies the *grade value* `n(λ)` algebraically — can be promoted
  to *select the single graded degree* (a genuine graded Springer/coinvariant
  structure forced by the drivers). That map, not the SDP, is where a genuine
  substrate-derivation must now be attempted.

## Verdict

**NO — the confinement SDP / canonical `T_w` does not force the top-degree
projection**, proved as a scope-(a) LIMITATIVE negative with a structural
backbone: the SDP / `T_w` / `tr_M` factor through the ungraded Wedderburn algebra
`⊕_λ End(V_λ)`, and the fake-degree grading is not a function of that algebra
(witnessed by `G_λ` vs `H_λ`). This is **not** a claim that top-degree is excluded
from every closure — an independent graded map (a-function / GS jet-order) remains
a live route and is the precise next obstruction. Third-direction convergence with
#4554 (`A_ω=3` structurally-open) and #4559 (moduli under-determined).

## Anti-fit / honesty ledger

- **0 free parameters**; `Δ_λ`, AME, CODATA, `q₀` never inverted; the fake-degree
  polynomials `f_λ(q)` are the standard coinvariant graded dimensions (hook-length
  formula, `f_λ(1) = dim V_λ` machine-checked).
- Formalize-first honoured: the limitative claim is a sorry-free Lean statement.
  No `sorry`, no `True`-conclusion, no `native_decide`/`decide`-laundering (the
  `decide`s discharge genuinely-finite concrete integer computations at `n=5`);
  base ring `ℤ`.
- **No instance of the open conjecture fabricated.** The proved content is a
  *limitative* fact (the ungraded datum does not force the concentration) — it does
  NOT close the open leg and does not launder it. "Axiomatization is NOT a proof",
  "sorry-free ≠ derived", "conditional-proved ≠ premise-established" respected.
- corpus-grep run before the "open"/"does-not-force" declaration (Springer /
  fake-degree / coinvariant / confinement-SDP paths walked; the SDP's ungraded
  data type confirmed from `sdp_solve_canonical_t_w.rs` + `prop:operator-selection-lp`).

## Cross-references

- Parent (moduli under-determined): PR #4559, [`2026-08-01-deltalambda-dt-substrate-derivation.md`](2026-08-01-deltalambda-dt-substrate-derivation.md).
- Grandparent (single-degree DT object): PR #4553, [`2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md`](2026-08-01-deltalambda-dt-3dindex-graded-euler-unification.md).
- `A_ω=3` mirror (`qou-qnnq`): PR #4554.
- General-`n` DT lift: PR #4558.
- SDP data + uniqueness: `tools/hecke-engine/src/sdp_solve_canonical_t_w.rs`; [`docs/coordination/2026-05-30-sdp-uniqueness-status.md`](../coordination/2026-05-30-sdp-uniqueness-status.md); `prop:operator-selection-lp`.
- a-function = GS jet-order valuation, fake-degree hidden-DOF: [`docs/coordination/option-e.md`](../coordination/option-e.md) (2026-07-18 front (i); 2026-06-28).
- Primary sources: Springer, *A construction of representations of Weyl groups*, Invent. Math. 44 (1978) 279–293, https://doi.org/10.1007/BF01403165 ; Behrend, *DT type invariants via microlocal geometry*, Ann. of Math. 170 (2009) 1307–1338, https://doi.org/10.4007/annals.2009.170.1307 ; James, `[james1984representation]`.
- AGENTS.md §"Axiomatization is NOT a Proof"; §"Before declaring open/refuted"; §"Strict Lean Discipline".
