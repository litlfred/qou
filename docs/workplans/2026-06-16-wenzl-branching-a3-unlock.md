# Wenzl operator-valued branching at A ≥ 3 — the ¹⁶O feasibility unlock (2026-06-16)

**Branch:** `claude/wenzl-branching-a3-2026-06-16`
**Picks up:** PR #2349 §C ([`docs/audits/2026-06-16-bsym-residual-16o-feasibility-wall.md`](../audits/2026-06-16-bsym-residual-16o-feasibility-wall.md))
— the explicit "genuine unlock for ¹⁶O" follow-up.
**Status:** scope + formalize-first pruning. **No compute landed** (this container
has no `numpy`/`mpmath`/`pyhecke_native`; empirical steps are deferred to an
environment with the stack installed — see §5).

## 1. Goal — and what is *not* the goal

The ¹⁶O magic-number test (PR #2349) is blocked by an **algorithmic feasibility
wall**, not a missing value. Two distinct things must not be conflated:

| | A ≥ 3 |
|---|---|
| **Value of `\|tr_M(β_atom)\|`** | **Already correct** — `compute_tr_m_via_branching` (`canonical_tr_m_via_branching.py:367`) routes A ≥ 3 through the lossless fine-Bratteli transfer `tr_m_atom_via_transfer.tr_m_atom_zn` (Σ_{λ⊢3A} y_λ χ^λ over **all** p(3A) partitions, agrees with full Hoefsmit to 4.7e-15). |
| **Speed** | **Walls at `p(3A)`** — ⁴He 0.09 s (p=77) → ¹²C ≈ 333 s (p=17 977) → ¹⁶O ≈ 1.5–3 h (p=147 273). Empirically ≈ `p(3A)^1.5`. |

**Goal:** make the A ≥ 3 trace *fast enough* for ¹⁶O (and the magic-number ladder
beyond) by activating the **operator-valued Wenzl branching recursion**
(`compute_chi_lambda_via_branching`, currently `return None` for A ≥ 3 —
`canonical_tr_m_via_branching.py:263`), whose cost is polynomial in A
(`Σ_level Σ_{ξ,ν} dim(ξ)·dim(ν)`) rather than `p(3A)`.

**Not the goal:** changing any production binding value, wiring to the canonical
chain, or fitting. This is a *speedup* to an already-validated value — exploratory
infrastructure, derive-or-refute, **not wired**.

## 2. Current state (grounded in the code)

- **A = 2 works end-to-end.** The deuteron runs the operator-valued branching via
  the **H₆ two-block interface extract** (`sublemma-2-1-A-operator-extract*.witness.json`),
  matching `markov_peel` to 7e-15. The H₆ extract **is full-rank**.
- **A ≥ 3 recursion returns `None`.** Root cause (verbatim from
  `canonical_tr_m_via_branching.py:232-243`): the H₉/H₁₂/H₁₅/H₁₈ interface
  extracts are produced by **least-squares fitting over a small set of H₃ test
  words** (`A_operator_extract_general.py`, `np.linalg.lstsq`). For every λ with
  `d_λ > 1` the bilinear system is **rank-deficient**:

  | λ ⊢ 9 | n_unknowns | n_equations | rank |
  |---|---|---|---|
  | `[8,1]` | 30 | 144 | 14 |
  | `[4,3,1,1]` | 3390 | — | 66 |

  The fitted `A` is the **min-norm solution for H₃ inner test-words**, not a
  universal interface operator; applied to an H₆ inner deuteron it gives the wrong
  χ^λ. Empirically A=3 (T/³He) differs from `markov_peel` by **21–42 %**.

## 3. Formalize-first pruning — kill the non-scaling path before coding

Per the repo's **formalize-first discipline**, the structural argument prunes the
hypothesis class *before* any wide numerical run:

- **Closure path (a) — regenerate full-rank extracts — is structurally refuted for
  high A.** To make the least-squares system full-rank for `[4,3,1,1] ⊢ 9` needs
  **≥ 3390 test words**; for `[3,3,3,3,3,3] ⊢ 18` the test-word count *explodes*
  combinatorially (already noted at `canonical_tr_m_via_branching.py:249-250`).
  So path (a) does **not** reach ¹⁶O. **Do not** invest in a bigger test-word
  panel as the ¹⁶O route. ✗
- **Closure path (c) — `markov_peel` / transfer fallback — is what A ≥ 3 already
  does.** Correct but `p(3A)`-bound; *is* the wall. Not an unlock. (Useful only as
  the cross-check oracle, §4 step 4.) ◯
- **Closure path (b) — operator-form recursion — is the only scalable route.** ✓

  **Structural claim to formalize (the crux).** The interface operator
  `A^λ_{ξν}(I)` is a **universal** object: it depends only on the interface type
  `I` and the partition data `(λ, ξ, ν)` via Littlewood–Richardson / fusion, **not
  on the inner braid word**. Therefore it should be computed **from the
  representation theory directly** (iterated branching / Clebsch–Gordan over the
  Bratteli diagram), making it **exact and full-rank by construction** — never
  least-squares-fitted. If this holds, the recursion peels one H₃ block at a time,
  carries `ρ_ξ` in **matrix (operator) form** between peels, and the rank-deficiency
  vanishes because no `H_{3A}` single-shot extract is ever formed.

  This claim is the gate: **prove/realize the universal `A^λ_{ξν}(I)` from
  branching data first**; only then run the A=3 cross-check. A small Lean lemma
  (or a rigorous symbolic check that the fusion-derived `A^λ_{ξν}` reproduces the
  full-rank H₆ extract for A=2) is the cheap pre-flight that decides whether to
  build the A≥3 layer at all.

## 4. Plan (ordered; each step gated on the previous)

0. **Env preflight.** Install `numpy`, `mpmath`, and build `pyhecke_native`
   (`maturin build` per #2349 commit). Confirm `tr_m_atom_via_transfer.tr_m_atom_zn`
   runs (A=2 deuteron ⇒ 0.388357).
1. **Realize the universal interface operator (§3 crux).** In
   `A_operator_extract_general.py` (or a new `a_operator/` module), derive
   `A^λ_{ξν}(I)` from the LR/fusion data (`lr_coefficients.lr_coef` already
   present) instead of `np.linalg.lstsq`. **Pre-flight check:** the fusion-derived
   operator must reproduce the full-rank **H₆** extract bit-for-bit (A=2 deuteron
   to 1e-14). If it cannot, path (b) has a hidden obstruction — stop and report.
2. **Operator-form recursion.** Replace the `A ≥ 3` `return None` branch
   (`canonical_tr_m_via_branching.py:225-263`) with the recursive `ρ_ξ(β_{A-1})`
   built in matrix form from step 1, peeling one nucleon per level.
3. **A = 3 cross-check (the decisive gate).** Tritium / ³He via the recursion must
   match `markov_peel.tr_M_atomic` (and the transfer) to ≤ 1e-12. This is the
   test the current rank-deficient extracts **fail at 21–42 %**; passing it is the
   proof the unlock works.
4. **Climb the ladder with the transfer as oracle.** ⁴He, ⁸Be, ¹²C must reproduce
   the §A residual-ladder values of #2349 (the transfer already has them) — now in
   seconds. Then **¹⁶O** (the new datum the wall blocked) and, if cheap, a
   magic-but-not-α-conjugate discriminator (⁴⁸Ca) per #2349 §A.
5. **Witness + audit.** Emit `*.witness.json` with the A=3..16 cross-checks
   (recursion vs transfer vs markov_peel), wall times, and the ¹⁶O magic-test
   result. Cross-link the #2349 wall audit and the #2343 low-isotope closed form.

## 5. Constraints / risks

- **Compute env.** None of this runs in the current container (no
  numpy/mpmath/pyhecke). Step 0 is mandatory and must use the
  `lake-cache`-style preserved-build discipline if a sandbox rebuild is needed.
- **Step 1 may fail.** If `A^λ_{ξν}(I)` is *not* word-independent in the way §3
  claims (e.g. a genuine dependence on the inner braid beyond `(ρ_ξ ⊗ ρ_ν)`), path
  (b) collapses to path (a) and ¹⁶O stays infeasible by this route. The §3
  pre-flight (reproduce H₆ exactly) is the early kill-switch.
- **Effort.** Multi-day. Step 1 (the representation-theory derivation) is the hard,
  unsolved piece; steps 2–4 are ≈ 200 lines + caching once step 1 lands.
- **Discipline.** Speedup only — the value is fixed by the transfer; the recursion
  must *match* it, never replace or re-tune it. No production-chain / MBA-appendix
  touch unless a value changes (it must not).

## 6. Prior art (do not re-derive)

- `a_operator/A_operator_extract_general.py` — generalized least-squares extract
  (the rank-deficient method; the thing step 1 replaces).
- `a_operator/A_operator_extract_{reduced,kron,at_level}.py`,
  `mass_tower_operator_valued.py` — earlier operator-form attempts.
- `sublemma_2_1_A_operator_extract*.py` + witnesses — the A=2 H₆ extract (full-rank
  reference for the step-1 pre-flight).
- [`docs/audits/2026-05-16-sublemma-2-1-h9-phase-1.md`](../audits/2026-05-16-sublemma-2-1-h9-phase-1.md)
  — H₉ phase-1 audit.
- [`docs/audits/2026-06-16-bsym-residual-16o-feasibility-wall.md`](../audits/2026-06-16-bsym-residual-16o-feasibility-wall.md)
  §C — the unlock framing this workplan executes.
