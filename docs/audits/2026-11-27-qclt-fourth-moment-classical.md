# The q-CLT as pinned in `QCltCut` does not hold at `q ≠ 1`: the fourth moment goes to 3

Date: 2026-11-27. Beans `qou-e1uf` (q-CLT) and `qou-o8lo`. Carl: "Prove the conjecture …
and the related assertions." Probe: `computations/probes/qclt_fourth_moment_exact_probe.py`
(exact rational arithmetic, no floats, PASS).

## 1. The class as written cannot be proved honestly

`QOU.Observations.QCltCut.QCltCut K q` has two fields: `momentSequence : ℕ → ℕ → K` and
`momentConverges`. `momentSequence` is **free**. Nothing ties it to `tr_M(S_n^k)`, so the
constant sequence `fun _ k => evalAt q (qGaussMoment k)` satisfies the class. Writing that
instance would "prove" the conjecture while saying nothing about the Hecke algebra. That is the
empty-carrier case of AGENTS.md §3b-tax, and it is not done here. The related assertions
(`limit_eq`, `odd_moment_converges_zero`, `fourth_moment_converges` = `2 + q`) are sorry-free
consequences of the class. They are only as true as the class is for the real moment sequence.

## 2. For the real moment sequence the limit is the classical Gaussian

Exact model of the convention-D Markov trace: the `U_q(sl₂)` quantum trace on `V^{⊗n}`,
`ω(x) = Tr(μ^{⊗n} x)/Tr(μ)^n`, `μ = diag(1, q⁻²)`, with `σ_i` the R-matrix on factors
`(i, i+1)` (eigenvalues `q`, `−q⁻¹`). The probe checks `ω(σ₀) = q³/(q²+1) = z_D` exactly.

With `S = Σ_{i<n−1}(σ_i − z)` and `k = n − 1`:

| `q` | exact limit of `m₄/m₂²` | q-Gaussian pin `2 + q` |
|---|---|---|
| 11/10 | **3** | 31/10 |
| 3/2 | **3** | 7/2 |
| 2 | **3** | 4 |

For `n = 6…9` the ratio is exactly `a + b/k + c/k²`. It is solved from three exact points and
confirmed on the fourth, and `a = 3` at every `q` tested.

Why:
- `ω` is a product state.
- `σ_i` and `σ_j` with `|i − j| ≥ 2` act on disjoint tensor factors, so a crossing pairing
  factorises with weight `1`, not `q`.
- The Markov property gives `ω(σ_iσ_j) = z²`, so off-diagonal covariances vanish and `m₂` is
  constant in `k`.

So the centred generator sum obeys the **classical** CLT. The q-Gaussian moment `2 + q` is
reached only at `q = 1`.

**Scope.** This is a refutation of the pinned limit for the moment sequence `tr_M(S_n^k)`
under the R-matrix model of convention D. It is checked exactly at three rational `q`, with the
general mechanism stated above. It is not yet a Lean theorem. A Lean refutation needs the class
first tied to `tr_M(S_n^k)`.

## 3. Consequence for the isospin work

`qGaussMoment_two = 1` (used in the weight-multiplicity audit §6) still holds, and so does the
classical `−2T_z²/N` coefficient. The q-CLT never changed it. The q-Gaussian higher moments do
not describe this sum either.

## Restatement landed (owner pick "Do both", 2026-11-27)

`QOU/Observations/QCltCut.lean` is restated, lean-direct exit 0, axioms
`[propext, Classical.choice, Quot.sound]`:

- **Moments are no longer a free field.** The class carries a tracial normalised
  state `state : A →ₗ[K] K` (intended instance: `tr_M` on the Hecke tower), a sum
  sequence `sum : ℕ → A` and a variance `v ≠ 0`. The normalised even moment is
  `evenMoment = state (sum n ^ (2k)) / n ^ k`, pinned to `v^k · qGaussMoment (2k)` at `q`.
  Odd moments are dropped (normalising them needs `√n`).
- **`QCltCut.q_eq_one_of_fourth_limit`**: a fourth-moment limit of `3 v²` forces `q = 1`.
  `not_qCltCut_of_classical_fourth` is the contrapositive at `q ≠ 1`.
- **`ClassicalClt K A := QCltCut K A 1`**, with `ClassicalClt.fourth_moment_converges`
  (`→ 3 v²`).
- The bridge `toQCltCut` from `QOU.Transcendental.QCltNonCommutative` is removed: that
  class keeps its moments as a free field and cannot supply a state.

Still open (bean `qou-e1uf`): an instance of `ClassicalClt` for `tr_M`, i.e. the
Lean proof that the Markov trace's normalised moments converge. Lean has no
general-`n` Markov trace yet (`markovTraceH2/H3A/H4A` only). Proposed route: the
cumulant / additive-formal-group argument over `QOU/LiftingDescent/FormalGroupLaw.lean`,
with the Markov factorisation as the key lemma (owner card pending).

## Classical CLT for tr_M, step 1: the exact second moment (owner pick "cumulant route")

`QOU/Observations/QCltMarkovSecondMoment.lean`, lean-direct exit 0, standard axioms. For
**every** Markov trace `T : MarkovTower δ ε` on the Temperley–Lieb tower:

- `tau_e`: `τ_n(e_i) = ε`; `tau_e_mul_e`: `τ_n(e_i e_j) = ε²` for all `i ≠ j`, adjacent or not.
  The Markov property kills every off-diagonal covariance.
- `tau_S_sq`: `τ_n(S_n²) = n·(δε − ε²)` exactly, `S_n = Σ_i (e_i − ε)`.
- `secondMoment_converges`: `τ_n(S_n²)/n → v = δε − ε²` (`= 1 − δ⁻²` at `ε = δ⁻¹`, the spin
  chain of PR #9817).

This is the `k = 1` field of `QCltCut`, which holds for every `q` (the second q-Gaussian
moment is 1). Remaining for `ClassicalClt` (bean `qou-e1uf`):

1. cluster factorisation (locality of the product state) for words of `X_i`;
2. the leading-order pair count `(2k−1)!! v^k n^k` (nearest-neighbour pairs contribute 0 by
   step 1, so crossings weigh 1);
3. a bound `O(n^{k−1})` on the rest, and **`[Archimedean K]`**: the `k ≥ 2` moments carry
   `O(1/n)` corrections, and `b/n` is not a located-cut limit in a non-Archimedean field. So a
   `tr_M` instance of the class exists only over an Archimedean `K`; in a surreal or
   hyperreal field the statement is a standard-part one.
