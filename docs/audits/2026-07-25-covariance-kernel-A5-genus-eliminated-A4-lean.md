# Covariance-kernel epic (qou-x631) — A5 (genus) ELIMINATED + A4 (Lean scaffold) landed

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-attack-a4-lean-2026-07-25` ·
**Tier:** route-elimination (A5) + sorry-free Lean (A4) · **Discipline:** scope-(a); no fit; nothing
wired; no `c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`, attacks `qou-9clc` (A5), `qou-q8g5` (A4).

## A5 — Śniady genus expansion: ELIMINATED (route #11), with a valuable reframing

A paper-mining agent read Śniady (`0411647`), Dołęga–Śniady (`1704.02352`), Ivanov–Olshanski
(`0304010`). Verdict: **A5 is not viable** — but the *why* sharpens the problem.

**The mechanism.** Śniady's genus grading lives on the algebra `A` of polynomial functions on Young
diagrams (spanned by the central characters `Σ_k = p#_k`). `ω₃ = Σ₃ = R₄+R₂ ∈ A` (degree 4) is fine.
The **obstruction is the dimension weight.** Using `ω₃ = n↓3·χ^λ(σ₃)/dim λ` (IO Def 3.1) and IO
Prop 5.1 (`⟨p#_ρ⟩_Planch = n↓ʳ·δ_{ρ=(1ʳ)}`):

> `cov(n) = Σ_λ (dim λ)³ ω₃(λ) = n↓3 · Σ_λ (dim λ)² χ^λ(σ₃) = n!·Cov_Planch(dim, ω₃)`.

The summand `(dim)²·χ^λ(σ₃)` carries **one surplus `dim`** beyond what column-orthogonality absorbs
(`dim³/dim = dim²`); and `dim λ ∉ A` (it grows super-polynomially). So `dim·ω₃` has **no degree, no
genus**, and Śniady's expansion structurally cannot represent it — there is no "genus-0 leading term"
whose sign to read.

**The sharp diagnostic (now Lean-encoded, see A4).** Replace the tilt `dim³ → dim²`: then
`Σ_λ (dim)² ω₃ = n!·E_Planch[ω₃] = 0` **exactly** (Prop 5.1, since `(3) ≠ (1ʳ)`). So the entire
negative value of `cov(n)` is the **first-order response to the extra `dim`** — a genuine covariance
`Cov_Planch(dim, ω₃)` of the one functional (`dim`) the genus machinery cannot touch. Distinct cycle
lengths even *decorrelate* at leading order (IO Thm 6.1: `p#_k/n^{k/2} → √k ξ_k`, independent), and
we verified `Cov_Planch(Σc, ω₃) = 0` exactly.

**Consequence for the plan.** The first lemma any viable route must supply is an **expansion of the
non-polynomial functional `dim λ` (or `ln dim λ`) against Plancherel** — a Schur-measure / hook-content
generating function or the Vershik–Kerov `ln dim` functional — **not** a `Σ_k` genus grading. Neither
Śniady nor Dołęga–Śniady provides it (the latter deforms the *measure*, α-Jack, keeping a `dim²`-type
normalization — not an extra power of `dim`). A5 is a dead end *for the sign*; this redirects effort.

## A4 — Lean scaffold: 5 sorry-free theorems landed

Extending [`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean)
(lean-direct exit 0; the only `sorry` remains the open `covariance_kernel_conjecture`):

| theorem | content |
|---|---|
| `secondMomentKernel_eq_zero_of_le_seven` | **`Σ_{λ⊢k} (f^λ)² ω₃(λ) = 0`** for `3≤k≤7` — encodes A5's reframing: the dim²-sum vanishes, so the kernel is the pure `dim`-tilt `k!·Cov_Planch(f^λ,ω₃)` |
| `kernelValue_base_values` | exact `kernelValue k` for `k=3..7` (`−4,−16,−320,−10400,−163520`), Lean-kernel-`decide`d |
| `kernelValue_nonpos_of_le_seven` | the **conjecture Lean-verified** for `3≤k≤7` (was Python-only) |
| `contentSq_conj_invariant_of_le_six` | `contentSq (conj λ) = contentSq λ` for all `λ⊢k`, `k≤6` — the transpose symmetry behind ω₃'s U-shape (why no monotone certificate works) |
| `omega3_conj_invariant_of_le_six` | `ω₃(conj λ) = ω₃(λ)` (conjugate-pairing of the kernel summands) |

**Scope honesty.** These are `decide`-verified *instance* results (bounded `k`). The general
statements need representation theory beyond this elementary List file: `Var_P(ω₃)=n(n−1)(n−2)/3` and
the `τ₃=3/n` eigenvalue need character theory / the group algebra; the general (`∀` sorted `l`)
conjugation-invariance needs a sorted-List transpose bijection
`cellSum (conj l) f = cellSum l (fun i j => f j i)` (via `len(conj l)=l.headD 0`,
`(conj l).getD r 0 = #{i : l.getD i 0 > r}`, staircase `c<(conj l).getD r 0 ↔ r<l.getD c 0`) — infra
not built here (~150 lines; it hardens a scaffold fact but does not advance the open kernel).

## Net

A5 eliminated (route #11); A4 scaffold landed (5 sorry-free theorems, including the Lean-encoded
`dim²`-vanishing that pins the kernel as a `dim`-tilt covariance). The kernel stays open; the honest
open core is now sharpened: **an expansion of the non-polynomial `dim`/`ln dim` functional against
Plancherel** (not the character-algebra `Σ_k` machinery).

## Compute / Lean

- Lean: [`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean) (lean-direct exit 0; 5 new sorry-free theorems)

## Cross-references

- Attack plan: bean `qou-v8t7`; A5 `qou-9clc`, A4 `qou-q8g5`
- A3 (CM refuted): [`2026-07-25-covariance-kernel-complete-monotonicity-target.md`](2026-07-25-covariance-kernel-complete-monotonicity-target.md)
- Śniady `0411647`, Dołęga–Śniady `1704.02352`, Ivanov–Olshanski `0304010` (in `library/`)
