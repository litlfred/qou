# Covariance-kernel epic (qou-x631) — literature assessment (7 arXiv papers)

**Date:** 2026-07-24 · **Branch:** `claude/deltalambda-covariance-epic-phase3-2026-07-24` ·
**Scope:** assess whether the uploaded literature closes the kernel `Cov_Planch(f^λ, Σc²) ≤ 0`.
**Verdict:** the literature supplies the *machinery* (Stein, Kerov CLT, Jack, genus) but **not a proof**;
the dimension-not-polynomial obstruction the epic named at the start is **confirmed** as the exact
barrier. No proof is claimed (anti-laundering).

## Papers read (owner-uploaded to `library/`, commit `03fa2a5b`)

| paper | what it gives | closes the kernel? |
|---|---|---|
| **Fulman, *Stein's Method and Plancherel Measure*** (`math/0305423`) | Stein's-method CLT **with error term `40.1·n^{−1/4}`** for the **transposition** (2-cycle) character ratio `n^{−1/2}χ^λ(12)/dim λ`; exchangeable pair from Bratteli-diagram harmonic functions; spectrum of the associated partition Markov chain (eigenvalues = character ratios, multiplicity `(dim λ)²`). | **No.** Our object is the **3-cycle** ratio `χ̂^λ(3-cyc) ∝ Σc²−C(k,2)` **jointly with dimension**. His exchangeable pair is transposition-specific; the marginal n^{−1/4} bound is not a joint covariance. |
| **Ivanov–Olshanski, *Kerov's CLT*** (`math/0304010`) | The joint asymptotic Gaussianity of the character ratios (`p#_k` / `Σ_μ` basis) with **explicit covariances**, all inside the algebra `A` of **polynomial functions on Young diagrams**; §10 = free cumulants + Biane. | **No.** Gives `Cov(Σ_2,Σ_3)` etc. exactly, but `f^λ ∉ A` (see obstruction). |
| **Dołęga–Féray, *Gaussian fluctuations … Jack characters*** (`1402.4615`) | Second-order asymptotics of the **α-Jack** measure `P^{(α)}(λ)=α^n n!/j^{(α)}_λ`; polynomiality of Jack-character structure constants; Gaussian-β-ensemble link. | **No** — and **not directly applicable**: the α-Jack family ≠ our `(f^λ)^β` family (they coincide **only** at Plancherel, α=1 = β=2). Resolves the Phase-3 caveat: the β-ensemble conjecture is *not* an α-Jack statement. |
| Śniady `math/0411647`; Biane `math/0006111`; Dołęga–Śniady `1704.02352`; Okounkov–Olshanski `q-alg/9608020` | genus expansion; character concentration / tensor-power multiplicities `(dim)^k`; Jack fluctuations; shifted-Jack content evaluations. | supporting; same obstruction. |

## The obstruction, literature-confirmed

Every rigorous framework above operates on the algebra **`A` of polynomial functions on Young
diagrams** — the character ratios `Σ_μ`. Writing `Cov_Planch(f^λ, Σc²) = 3·cov(k)/k!` and
`f^λ = √(k!·P(λ))`, one gets

> `Cov_Planch(f^λ, Σ_3) = √(k!) · Σ_λ P(λ)^{3/2} Σ_3(λ)`,

i.e. the observable is averaged against the **`P^{3/2}` (dimension-cubed) biased** measure. The
dimension `f^λ` is `exp` of an infinite series in the `Σ_μ` (the Kerov functional), so it is **not**
in `A`, and the `P^{3/2}` biasing is outside every framework's native (Plancherel, α-Jack) measure
class. This is exactly the obstruction recorded at epic start — now cross-checked against four
independent machineries.

## Realistic paths (honest)

1. **Effective Route 1 (only plausible *full* proof; multi-session research).** Extend Fulman's
   exchangeable pair from the transposition to the **3-cycle**, and upgrade his *marginal* `n^{−1/4}`
   bound to an **effective joint Berry–Esseen bound** on `(ln f^λ, Σ_3)`; then show the Stein
   transfer-factor error is smaller than the negative main term `E[f]·Cov(ln f, Σ_3) < 0` for all
   `k > k₀` (computable), closing the residue with exact enumeration (`k ≤ 40` done). Fulman himself
   only *conjectures* the sharp `n^{−1/2}` rate, and the joint-with-dimension version is **not** in the
   literature — this is genuine new work, not a citation.
2. **Accept as a well-supported conjecture with machinery cited.** The kernel is a Kerov-CLT-regime
   anti-correlation (verified `k ≤ 40`), reframed as the β-ensemble inequality `E_β[C₂] ≤ C(k,2)
   ∀β≥2` (Phase 3), with the Stein / genus route identified. This is the honest status for the paper;
   the Δ_λ growth chain stays Lean-proved **modulo** this named conjecture.

## What did NOT close it (do not retry)

- A citation. No paper states `Cov(dim, 3-cycle-ratio) ≤ 0` or the β=2-maximises-`E_β[C₂]` fact.
- The α-Jack literature (different deformation family).
- Fulman's transposition bound as-is (wrong central element, marginal not joint).

## Cross-references

- Phase 3 (β-ensemble reframing): [`2026-07-24-covariance-kernel-proof-epic-phase3.md`](2026-07-24-covariance-kernel-proof-epic-phase3.md)
- Phase 2 / Phase 1: [`…-phase2.md`](2026-07-24-covariance-kernel-proof-epic-phase2.md) / [`…-phase1.md`](2026-07-18-covariance-kernel-proof-epic-phase1.md)
- Papers: `library/{0305423v3,0304010v1,1402.4615v3,0411647v2,0006111v2,1704.02352v2,9608020v2}.pdf`
