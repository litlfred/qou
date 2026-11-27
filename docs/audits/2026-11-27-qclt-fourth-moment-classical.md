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
