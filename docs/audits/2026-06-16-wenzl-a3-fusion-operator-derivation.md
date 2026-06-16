# Path-(b) fusion derivation of the interface operator `A^λ_{μν}(I)` (2026-06-16)

**Branch:** `claude/wenzl-a3-fusion-operator-2026-06-16`
**Executes:** step 1 (the §3 crux) of the Wenzl A≥3 workplan
[`docs/workplans/2026-06-16-wenzl-branching-a3-unlock.md`](../workplans/2026-06-16-wenzl-branching-a3-unlock.md).
**Goal:** replace the rank-deficient least-squares extraction of `A^λ_{μν}(I)`
with a **representation-theoretic derivation** — exact and full-rank by
construction — so the operator-valued branching recursion works at A ≥ 3
(the ¹⁶O unlock).

## 1. The object

The refined Sub-lemma 2.1 defining relation
([`sublemma_2_1_A_operator_extract.py`](../../computations/sublemma_2_1_A_operator_extract.py)):
for the parabolic split `n = n_1 + n_2`, an interface element
`I ∈ H_n` (the coupling generator `I = c·σ_{n_1} + d·1`), and arbitrary
`β_1 ∈ H_{n_1}`, `β_2 ∈ H_{n_2}` (shifted),

$$
\chi^\lambda(\beta_1\,I\,\beta_2)
  = \sum_{\mu\vdash n_1,\ \nu\vdash n_2} c^\lambda_{\mu\nu}\;
    \mathrm{Tr}_{V_\mu\otimes V_\nu}\!\Big(
      A^\lambda_{\mu\nu}(I)\,\big(\rho_\mu(\beta_1)\otimes\rho_\nu(\beta_2)\big)
    \Big).
\tag{1}
$$

The current code **fits** `A^λ_{μν}(I)` from a panel of `K·K` test-word
pairs by `np.linalg.lstsq`. That system is full-rank at H₆ (A=2) but
**rank-deficient at H₉+** (e.g. `[4,3,1,1]⊢9`: 3390 unknowns, rank 66), so
the fitted `A` is a min-norm artifact that gives wrong `χ^λ` when the inner
braid is a multi-nucleon block rather than an H₃ test word — the 21–42 %
A=3 error documented at `canonical_tr_m_via_branching.py:232-243`.

## 2. The derivation (closed form, no fitting)

**Branching.** Over a field where `H_n(q)` is semisimple (generic `q`, and
`q₀` is generic),
$$
V_\lambda \big\downarrow_{H_{n_1}\otimes H_{n_2}}
  \;=\; \bigoplus_{\mu,\nu}\,(V_\mu\otimes V_\nu)^{\oplus c^\lambda_{\mu\nu}},
\tag{2}
$$
with `c^λ_{μν}` the Littlewood–Richardson coefficients
([`substrate/lr_coefficients.py::lr_coef`](../../computations/substrate/lr_coefficients.py)).

**Commuting factors.** `H_{n_1} = ⟨σ_1,…,σ_{n_1-1}⟩` and
`H_{n_2} = ⟨σ_{n_1+1},…,σ_{n-1}⟩` **commute**: they share no generator and
are non-adjacent (the only bridge, `σ_{n_1}`, lies in neither). Hence on each
block `W_{μνt} ≅ V_μ⊗V_ν` (`t = 1,…,c^λ_{μν}` the multiplicity index),
$$
\rho_\lambda(\beta_1)\big|_{W_{\mu\nu t}} = \rho_\mu(\beta_1)\otimes \mathrm{id}_\nu,
\qquad
\rho_\lambda(\beta_2)\big|_{W_{\mu\nu t}} = \mathrm{id}_\mu\otimes \rho_\nu(\beta_2),
\tag{3}
$$
independently of `ν,t` (resp. `μ,t`).

**Trace.** Write `ρ_λ(I)` in the branching-adapted basis of (2). Then
$$
\chi^\lambda(\beta_1 I \beta_2)
  = \mathrm{Tr}_{V_\lambda}\!\big[\rho_\lambda(\beta_1)\,\rho_\lambda(I)\,\rho_\lambda(\beta_2)\big].
$$
`ρ_λ(β_1)` and `ρ_λ(β_2)` are **block-diagonal** w.r.t. (2) by (3), so only
the **diagonal** `(μνt)→(μνt)` blocks of `ρ_λ(I)` survive the trace:
$$
\chi^\lambda(\beta_1 I \beta_2)
  = \sum_{\mu,\nu}\sum_{t=1}^{c^\lambda_{\mu\nu}}
    \mathrm{Tr}_{V_\mu\otimes V_\nu}\!\Big[
      (\rho_\mu(\beta_1)\otimes\mathrm{id})\,[\rho_\lambda(I)]^{(\mu\nu t)}_{\mathrm{diag}}\,(\mathrm{id}\otimes\rho_\nu(\beta_2))
    \Big].
$$
Cyclicity plus `(\mathrm{id}\otimes B_2)(B_1\otimes\mathrm{id}) = B_1\otimes B_2`:
$$
\chi^\lambda(\beta_1 I \beta_2)
  = \sum_{\mu,\nu}\mathrm{Tr}\Big[
      \underbrace{\Big(\textstyle\sum_{t} [\rho_\lambda(I)]^{(\mu\nu t)}_{\mathrm{diag}}\Big)}_{\text{matches (1)}}
      \,\big(\rho_\mu(\beta_1)\otimes\rho_\nu(\beta_2)\big)
    \Big].
\tag{4}
$$

**Result.** Matching (4) against (1) (in the code's convention, where the
multiplicity `c^λ_{μν}` is absorbed into the extracted matrix — the
`sublemma_2_1` comment "do NOT multiply by c again"):
$$
\boxed{\;A^\lambda_{\mu\nu}(I) \;=\; \sum_{t=1}^{c^\lambda_{\mu\nu}}
   \big[\rho_\lambda(I)\big]^{(\mu\nu t)}_{\mathrm{diag}}\;}
\tag{5}
$$
— the sum of the diagonal multiplicity-blocks of the **single interface
generator** `ρ_λ(I)`, read off in the branching-adapted basis. (The
multiplicity-averaged operator is `(1/c^λ_{μν})·`(5).)

### Consequences

- **Word-independent / universal.** (5) depends only on `(λ,μ,ν,I)` — never
  on `β_1,β_2`. This is the property the least-squares fit only approximates;
  here it is exact by construction. The workplan §3 crux is **confirmed**.
- **Full-rank by construction.** No bilinear system, no rank condition. The
  rank-deficiency that blocks A≥3 (`[4,3,1,1]` needing ≥3390 test words)
  disappears: (5) reads `A` directly off `ρ_λ(I)` (a single
  `dim V_λ × dim V_λ` matrix).
- **A≥3 needs no `H_{3A}` extract panel.** The recursion peels one nucleon
  (one H₃ block) per level; at every peel the interface is the H₃↔(rest)
  generator, and (5) supplies its operator from the seminormal `ρ_λ(I)` — the
  inner `ρ_ξ` is carried in matrix form from the previous peel (the workplan
  step-2 recursion).

## 3. The one remaining computational ingredient

(5) requires the **branching-adapted basis** of (2): the change of basis from
the `H_n` seminormal basis of `V_λ` (indexed by `SYT(λ)`) to
`⊕_{μ,ν,t} (V_μ⊗V_ν)`. Two sub-steps:

1. **μ-grading is free.** The seminormal basis is adapted to the chain
   `H_1 ⊂ … ⊂ H_n`, so a `T ∈ SYT(λ)` has a definite `μ = shape_{n_1}(T)`
   (the shape of cells `1..n_1`). `ρ_λ(β_1)` is already
   `ρ_μ(β_1)⊗id`-block-diagonal in this grading.
2. **ν-grading is NOT free.** The span of `{T : shape_{n_1}(T)=μ}` is the
   skew module `V_{λ/μ} = ⊕_ν V_ν^{⊕c^λ_{μν}}`; extracting the straight-irrep
   `ν`-blocks requires the **skew→straight change of basis** (the sub-algebra
   `H_{n_2}` JM elements `L''_k = Σ_{n_1<i<k}(i,k)` are *not* diagonal in the
   global seminormal basis). This CoB is the concrete engineering task —
   computable per `(λ,μ)` by diagonalising the `H_{n_2}` action / building the
   `ν` central idempotents from `σ_{n_1+1},…,σ_{n-1}` (all available as
   seminormal matrices via `char_fast._compiled_sigmas`).

## 4. Pre-flight gate (the kill-switch)

Per the workplan, the multi-day A≥3 build is gated on a **cheap H₆ check**:
construct the H₃⊗H₃ branching CoB, apply (5) to the deuteron interface
`I = σ_3 − h/2`, and verify the resulting `A^λ_{μν}(I)` reproduces the
full-rank least-squares extract
([`sublemma-2-1-A-operator-extract.witness.json`](../../computations/sublemma-2-1-A-operator-extract.witness.json))
to ≤ 1e-12 (modulo a per-block unitary on the multiplicity space, so compare
the **basis-independent** invariants: the block trace `Tr A^λ_{μν}`, the
Frobenius norm `‖A^λ_{μν}‖_F`, and — the decisive test — that (5) reproduces
`χ^λ(β_1 I β_2)` on the existing test-word panel to 1e-12 via (1)).

If the invariants match → implement the skew CoB at H₉/H₁₂ and run step 3
(the A=3 cross-check vs `markov_peel`). If they do **not** match → (5) has a
convention/normalisation error to resolve before any A≥3 work. The
`χ^λ`-reproduction test in (4) is convention-free and is the primary gate.

## 5. Discipline

This is a **speedup derivation** for an already-validated value (the A≥3 trace
is correct via the transfer; this makes it fast). No production value changes;
no fitting; no fourth calibration. Exact arithmetic / mpmath at the 50-dps
floor for the eventual compute (the H₆ pre-flight may run at f64 first as a
cross-check, then 50-dps for the committed witness). Not wired to the canonical
chain. Per compute-author §3 the structural identity (5) is **proven above**
before any wide numerical run — formalize-first, as the workplan demanded.
