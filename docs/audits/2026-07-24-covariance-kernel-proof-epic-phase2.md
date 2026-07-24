# Covariance-kernel proof epic (qou-x631) — Phase 2: two more routes eliminated + R₄ affine

**Date:** 2026-07-24 · **Branch:** `claude/deltalambda-covariance-epic-phase2-2026-07-24` ·
**Tier:** route-elimination (exact) + sorry-free Lean · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`. **Follows:** #4008 (Phase 1).

## The epic (recap)

Prove the sole open input of the Δ_λ super-exponential growth bound (#3939, via the #3959
reduction):

> **`cov(k) := Σ_{λ⊢k} (f^λ)³ (Σ_□ c(□)² − C(k,2)) ≤ 0`**  (equivalently `T₃(k) := Σ_λ (f^λ)² χ^λ(3-cyc) ≤ 0`,
> `Cov_Planch(f^λ, Σ_□c(□)²) ≤ 0`).  Note `cov(k) = k(k−1)(k−2)/3 · T₃(k)`.

Phase 0 (#3939/#3959/#3998): reduction + free-cumulant framing + sorry-free Lean reduction, verified
`k ≤ 40`. Phase 1 (#4008): ruled out (1) holonomic recurrence and (2) β-monotonicity. This is Phase 2.

## Finding A — the R₄ reframing is **exactly affine** (not a new lever)

The 4th free cumulant of the transition measure, in Biane's normalisation `Σ̂₃ = R₄ + R₂` with
`R₂ = k`, is

> **`R₄(λ) = 3·(Σ_□c(□)² − C(k,2)) − k = 3·ω₃(λ) − k`**,

where `ω₃(λ) = Σc² − C(k,2)` is the eigenvalue of the 3-cycle class sum on the irrep λ. Since `k` is
**constant** across `λ ⊢ k`, the `−k` shift washes out of any covariance:
`Cov_Planch(f^λ, R₄) = 3·Cov_Planch(f^λ, ω₃)`. So "prove `Cov(f^λ,R₄) ≤ 0`" is **literally the same
inequality** as the content covariance — R₄ gives no independent handle. Cross-checked
`E_Planch[R₄] = −k` for all `k ≤ 8` (consistent with #3998).

This affine relation is now **Lean-carried, sorry-free**
([`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean)):
`r4WeightedSum_eq : Σ_λ (f^λ)³ R₄(λ) = 3·kernelValue(k) − k·cubeSum(k)` (via the inductive list
linearity `r4_sum_affine_list`). It exhibits how the shift enters at the summed level and why only the
*covariance*, not the raw sum, is shift-invariant.

## Finding B — Route 3 (sub-family / truncation sign-definiteness). **RULED OUT.**

If any natural sub-family of shapes summed to a sign-definite partial `cov`, one could try to bound the
remainder. It does not. The two-row truncation `Σ_{λ=(k−j,j)}` flips **positive at k = 6**
(`−160 → +1040`); the hook truncation `Σ_{λ=(k−j,1^j)}` flips **positive at k = 4** (`−4 → +16`). The
sign is a **global cancellation**: negative mass from balanced/typical shapes (ω₃ < 0, large f^λ)
outweighs positive mass from extreme shapes (ω₃ > 0, small f^λ), with `|cov⁻| ≈ 1.5–2× cov⁺`
consistently (k = 3..7: 2.00, 2.00, 1.47, 1.86, 1.74). No term-by-term or truncation bound works.

## Finding C — Route 4 (Murnaghan–Nakayama peeling). **RULED OUT.**

MN gives `χ^λ(3,1^{k−3}) = Σ_{ξ⊂λ, |ξ|=3 border strip} (−1)^{ht(ξ)} f^{λ∖ξ}`, hence

> `T₃(k) = Σ_{ν⊢k−3} f^ν · B(ν)`,   `B(ν) := Σ_{λ: λ/ν = BS₃} (−1)^{ht(λ/ν)} (f^λ)²`.

If `B(ν) ≤ 0` for every ν, the sign would follow from `f^ν ≥ 0`. It does **not**: `B(ν) ≤ 0` through
`k ≤ 8` but **first goes positive at k = 9** (`ν ⊢ 6`), and the offender is exactly the **self-conjugate
staircase** `ν = (3,2,1)`, `B = +6174` (peel-sum matches direct `T₃` exactly, so the enumeration is
sound). `B(ν)` is conjugation-symmetric, so the ± cancellation begins **precisely at the self-conjugate
shape** — a structurally telling place, consistent with the global-cancellation picture of Finding B.

## Finding D — no tabulated closed form (Route 5, informational)

An OEIS lookup of both positive sequences returns **no match**:

| k = 3..18 | sequence |
|---|---|
| `\|T₃(k)\|` | 2, 2, 16, 260, 2336, 28792, 632972, 19676288, 536156728, 15073599368, 506810488304, 22172234503696, 1192602485739392, 66317362326945680, 3739005858421579852, 221652176124179610176 |
| `\|cov(k)\|` | 4, 16, 320, 10400, 163520, 3224704, 106339296, 4722309120, 176931720240, 6632383721920, 289895599309888, 16141386718690688, 1085268262022846720, 74275445806179161600, 5085047967453348598720, 361736351434661123807232 |

Neither is in OEIS. Combined with the Phase-1 non-holonomicity, this makes a clean closed-form /
product evaluation unlikely — reinforcing that the sign is a genuine analytic fact, not a
combinatorial identity waiting to be spotted.

## Net + Phase-3 target

Five natural certificates are now excluded across Phases 1–2: (1) holonomic recurrence, (2) β-monotone
family, (3) sub-family sign-definiteness, (4) MN-peeling sign-definiteness, (5) tabulated closed form;
plus the R₄ reframing is an affine relabelling (no new lever). The kernel is a genuinely **global
analytic anti-correlation** with no local / inductive sign-certificate. The sole remaining route is
**Śniady's genus expansion** of the joint character cumulants on the `(f^λ)³`-biased measure — the
obstruction, unchanged, being that `f^λ = χ^λ(e)` is the exponentially-large **dimension**, not a
bounded character ratio, so standard Kerov-CLT / Ivanov–Olshanski machinery does not directly apply to
the dimension-cubed-biased average. Phase 3 attacks this via the RSK form
`T₃(k) = Σ_{w∈S_k} χ^{sh(w)}(3-cycle)`, coordinating with the Specht/S_n Lean epic `sp00`.

## Compute + Lean

- Probe: [`computations/deltalambda/wlambda_covariance_epic_phase2.py`](../../computations/deltalambda/wlambda_covariance_epic_phase2.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-phase2.witness.json`
- Lean (sorry-free additions): [`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean) — `omega3`, `r4Value`, `cubeSum`, `r4WeightedSum`, `r4_sum_affine_list`, `r4WeightedSum_eq` (lean-direct exit 0; only `sorry` is the honest open `covariance_kernel_conjecture`).

## Cross-references

- Phase 1 (routes 1–2): [`2026-07-18-covariance-kernel-proof-epic-phase1.md`](2026-07-18-covariance-kernel-proof-epic-phase1.md) (#4008)
- Kernel + framing + Lean infra: [`2026-07-18-deltalambda-covariance-kernel-frontier.md`](2026-07-18-deltalambda-covariance-kernel-frontier.md) (#3998)
- Reduction to the kernel: [`2026-07-18-deltalambda-D-reduction-content-covariance.md`](2026-07-18-deltalambda-D-reduction-content-covariance.md) (#3959)
- Literature: Śniady (PTRF 2006, arXiv:math/0305423), Biane (Adv. Math. 1998), Ivanov–Olshanski
