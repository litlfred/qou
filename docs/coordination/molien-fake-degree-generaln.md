# Coordination ledger — general-n Molien / fake-degree q-hook normalisation

Goal: prove the general-`n` q-analogue `Σ_{λ⊢n} f^λ q^{−κ_λ} qDim(λ) = [n]_q!`
(equivalently the Jones–Markov / Schur-element normalisation over `⊢ n`), and the
Molien = Jones–Markov weight identification behind it.

## Scope map

| PR | Branch | Owns | Files | Relationship to #5948 |
|----|--------|------|-------|------------------------|
| **#5948** | `claude/borel-alien-calculus-n24484` | Molien = Jones–Markov weights (n=3,4 exact, Wenzl-independent); fake-degree reduction; induction → addable-box hook identity (B); GAP-2 He4 Milnor | `QOU/QBeta/MolienJonesMarkov{N3,N4}.lean`, `QOU/MathlibExt/MolienFakeDegree{,GeneralN,Induction}.lean`, `computations/qbeta/molien_*`, `gap2_he4_*` | — (this PR) |
| **#5970** | `claude/lean-qa-backlog-2h3f8d` | Macdonald hook **telescope** general-X: `Σ f^ν schurElement Q X ν = ((1−X)/(1−Q))^n` all X, sorry-free; `sum_dim_wenzlWeight_eq_one` | `QOU/MathlibExt/MacdonaldTelescopeGeneralX.lean` | **convergent** — same normalisation family, different route; may close #5948's `normalizedSum n q = 1` residual. Additive (no file overlap). |

## The convergence (open question, posted on #5970 2026-08-29)

Both PRs prove a general-`n` normalisation of the same shape (`Σ_{λ⊢n} f^λ · weight = 1`):
- #5948 route: **induction** on `n` → one-step recursion → the **addable-box hook
  identity (B)** `Σ_{b addable to μ} q^{−c(b)} qDim(μ+b)/qDim(μ) = [|μ|+1]_q`
  (verified `|μ|≤6`; `c(b)` a q-JM content; no rep theory / maj / q-RSK). Skeleton +
  conditional main theorem sorry-free (`MolienFakeDegreeInduction`).
- #5970 route: **Macdonald telescope** off the principal-specialisation locus, via
  `sum_dim_wenzlWeight_eq_one` + `Polynomial.eq_of_infinite_eval_eq`.

**Open ask to #5970:** does `telescope_generalX` + `sum_dim_wenzlWeight_eq_one`
imply `normalizedSum n q = 1` (the balanced-convention fake-degree identity)? If yes,
#5948's `qou-3quc` general-`n` gap is closed by #5970's route, and the induction/(B)
route re-scopes to an independent second proof (parallel-research rule — two routes
valuable). Conventions differ: #5948 balanced `[m]_q`, content `κ_λ`; #5970 Macdonald
`Q`, level `r`. Reconciling the two conventions is the first step if the implication holds.

## Sessions log

| Date | PR | Event |
|------|----|-------|
| 2026-08-29 | #5948 | n=3,4 full Molien=Jones–Markov identity (Wenzl-independent) Lean-proved; general-n reduced to addable-box hook identity (B) via induction (sorry-free skeleton); GAP-2 He4 = Milnor-indeterminacy exclusion. Convergence flagged to #5970. |

## RESOLVED 2026-08-29 — the telescope closes it

The convergence question is answered **YES**: #5970's `telescope_generalX` (all X) closes
`normalizedSum n q = 1` via the X=0 specialisation + the `(Q=q², X=0)` convention bridge
(exact `n≤5`, `fake_degree_via_telescope_probe.py`; audit
`2026-08-29-normalizedsum-closes-via-telescope.md`). `qou-3quc` is no longer open math —
only mechanical Lean bridging remains (per-cell brick `one_sub_qsq_pow_eq` landed sorry-free
in #5975). The induction/(B) route is now an independent second proof. Posted on #5970
(issuecomment-5461309188).
