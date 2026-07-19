# Covariance-kernel epic (qou-x631) — kernel-SIGN structural narrowing + transpose-parity no-go (Lean)

**Date:** 2026-07-19 · **Branch:** `claude/deltalambda-kernel-sign-2026-07-19` · **Bean:** `qou-ogxc` ·
**Epic:** `qou-x631` · **Tier:** structural narrowing (exact) + sorry-free Lean no-go ·
**Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7). **Follows:**
#3998 (frontier + Lean infra), Phase 1 (routes 1,2 eliminated), Phase 2 / #4066 (RSK form + tilt
heuristic).

## The kernel (unchanged, still OPEN)

> `T₃ = Σ_{λ⊢k} (f^λ)² χ^λ(3-cycle) ≤ 0` ⇔ `cov(k) = Σ_{λ⊢k}(f^λ)³(Σ_□c² − C(k,2)) ≤ 0`
> ⇔ `Cov_Planch(f^λ, Σ_□c²) ≤ 0` ⇔ `Cov_Planch(f^λ, R₄) ≤ 0`.

Sole open input of the Δ_λ super-exponential growth bound (#3939, via the #3959 reduction).
Corpus-grep confirms it is still open: `YoungDiagramKernel.covariance_kernel_conjecture` carries an
honest §3b `sorry`; every prior route is a narrowing, none a closure. **The kernel remains open.**

## What this note adds

Two **decisive structural narrowings** of *how* a proof can go — each a scope-(a) exact fact, not a
numerical near-match — plus a **sorry-free Lean** formalization of the second. Neither closes the
kernel; together with Phase 1 they pin the sign as an *order-blind, parity-blind concentration
effect*, which is exactly the regime where elementary correlation-inequality machinery fails and the
tilted-limit-shape (Śniady genus / large-deviation) analysis is required.

### NARROWING A — FKG / correlation-inequality on the DOMINANCE lattice is DEAD

A Harris/FKG proof of `Cov_Planch(f^λ, Σc²) ≤ 0` on the partition **dominance** lattice needs `f^λ`
and `Σc²` to be **oppositely monotone** on that lattice (with a log-supermodular measure). Both
functions **fail monotonicity**:

- The two dominance extremes — the single row `(k)` (top) and single column `(1^k)` (bottom) — have
  **identical** `f = 1` and **identical** `Σc² = Σ_{j<k} j²` (transpose-equal). So both `f` and `Σc²`
  are extremal (`f` minimal, `Σc²` maximal) at **both** ends and opposite in the middle.
- Explicit covering-pair witnesses of **both** signs of `Δf` and `ΔΣc²` are emitted for every
  `k = 4..16`, e.g.
  - `k=6`: `(4,2) ⊵ (3,3)` gives `Δf = +4` (increasing) while `(6) ⊵ (5,1)` gives `Δf = −4`
    (decreasing) — `f` is provably not monotone.

So the anti-correlation is a **middle-vs-extremes** (concentration) effect, **not** an order-driven
one. This complements Phase 1's ruled-out **β-monotonicity**: neither the exponent order (`β`) nor
the partition order (dominance) drives the sign. Harris/FKG-on-dominance is therefore not a viable
route.

### NARROWING B — TRANSPOSE PARITY (route b) provably CANNOT sign `T₃`; it only kills `T₂`

Under conjugation `λ ↔ λ'` (content `c(i,j)=j−i` flips sign):

| quantity | transpose behavior | consequence |
|---|---|---|
| `f^λ` | `f^{λ'} = f^λ` (transpose of SYT) | invariant |
| `Σc(λ)` (linear content) | `Σc(λ') = −Σc(λ)` (**odd**) | `Σ_λ (f^λ)³ Σc = 0` ⇒ **`T₂ = 0`** |
| `Σc²(λ)` (content square) | `Σc²(λ') = Σc²(λ)` (**even** — squares kill the sign) | each cov summand invariant |

Hence **each** `cov(k)` summand `(f^λ)³(Σc² − C(k,2))` is **individually** conjugation-invariant: the
transpose involution is a **symmetry** of the kernel, contributing zero information about its sign.
This is the rigorous form of the Phase-2 "one candidate scope-(b)" remark: the transpose route
provably closes only the **odd** moment (`T₂`), never the **even** one (`T₃`). At self-conjugate
`λ = λ'` the odd quantity `Σc` vanishes, consistent with the pairing (verified `k ≤ 16`).

**Formalized sorry-free in Lean** — `YoungDiagramTranspose.lean`:

- an **abstract parity no-go** over a generic `CommRing`: an involution with an invariant weight and
  an odd quantity forces the odd moment to vanish (`sum_involution_weight_odd_eq_zero`), while an
  *even* quantity's weighted sum is fixed by the involution (`sum_weight_even_involution_invariant`)
  — so an involution *can* kill an odd moment but *never* signs an even one;
- the **concrete instances**: `contentSum` is transpose-odd (`content_sum_conj`) and `contentSq` is
  transpose-even (`content_sq_conj`) on the elementary `List ℕ` diagram machinery, hence each kernel
  summand is transpose-invariant (`kernel_summand_conj_invariant`).

## Formalize-first assessment

The invariant that would justify a scope-(b) closure **is** the open kernel `T₃ ≤ 0`; NARROWING B
proves the *only* clean involution available (transpose) is provably insufficient — a genuine
sorry-free structural result, not a fake scope-(b). NARROWING A rules out the natural
correlation-inequality lattice. No sorry smuggling, no axiomatized kernel, nothing wired.

## Verdict

Kernel **still OPEN**. Delivered: FKG-on-dominance no-go (NARROWING A, exact, with covering-pair
witnesses); transpose-parity-cannot-sign-`T₃` no-go (NARROWING B, exact + **Lean sorry-free**); a
re-anchor of `cov(k) ≤ 0` for `k ≤ 30`. The residual gap is unchanged and sharp: a large-deviation /
tilted-limit-shape bound on `E_{(f^λ)³}[Σc²] < C(k,2)` — order-blind and parity-blind, so genuinely
analytic. scope-(a); no fit; nothing wired; no `c_k`.

## Compute

- Structural probe: [`computations/deltalambda/fl_kernel_sign_structure.py`](../../computations/deltalambda/fl_kernel_sign_structure.py)
  (exit 0), witness `fl-kernel-sign-structure.witness.json`
- Lean (sorry-free): `QOU/BraidsAndKnots/YoungDiagramTranspose.lean`

## Cross-references

- Phase 2 (RSK + tilt): [`2026-07-19-deltalambda-covariance-epic-phase2-sniady-genus.md`](2026-07-19-deltalambda-covariance-epic-phase2-sniady-genus.md)
- Phase 1 (routes 1,2 eliminated): [`2026-07-18-covariance-kernel-proof-epic-phase1.md`](2026-07-18-covariance-kernel-proof-epic-phase1.md)
- Frontier + Lean infra (#3998): [`2026-07-18-deltalambda-covariance-kernel-frontier.md`](2026-07-18-deltalambda-covariance-kernel-frontier.md)
- Reduction to the kernel (#3959): [`2026-07-18-deltalambda-D-reduction-content-covariance.md`](2026-07-18-deltalambda-D-reduction-content-covariance.md)
- Lean: `QOU/BraidsAndKnots/DeltaLambdaDReduction.lean` (reduction, sorry-free),
  `QOU/BraidsAndKnots/YoungDiagramKernel.lean` (kernel conjecture),
  `QOU/BraidsAndKnots/YoungDiagramTranspose.lean` (transpose no-go, sorry-free)
- Literature: Śniady (PTRF 2006, arXiv:math/0305423), Biane (Adv. Math. 1998)
