# Q_β residue A — KLR / Kashiwara crystal infra scope (2026-06-03)

> Long-term infrastructural roadmap for promoting `c_3` from
> `cal-anchored` to `derived` via composite Kashiwara operator
> structures. Companion to the acceptance doc
> [`docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md`](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md).
>
> **Status**: scoping only. NO implementation in this PR. Owner direction
> required before any of the items below proceed.

## Current state — Mathlib coverage

| Feature | Mathlib coverage (2026-06) | Sufficient for residue A? |
|---|---|---|
| Young diagrams | `Mathlib.Combinatorics.Young.YoungDiagram` | Yes — combinatorial foundation |
| Semistandard Young tableaux | `Mathlib.Combinatorics.Young.SemistandardTableau` | Yes — combinatorial foundation |
| Standard Young tableaux + major index | Limited — major index not directly available | Partial |
| Symmetric polynomials (mv-polynomials) | `Mathlib.RingTheory.MvPolynomial.Symmetric` | Partial — Schur polynomials / full symmetric-functions algebra may still be a gap depending on residue A's exact need |
| Demazure modules / characters | **None** | **Gap** |
| Kashiwara crystal graphs | **None** | **Gap** |
| KLR algebra structure | **None** | **Gap** |
| q-Pochhammer symbols `(q;q)_n` / infinite product `(q;q)_∞` | **None** | **Gap** |
| Hecke algebra H_n(q) | Partial (basic definition in `Mathlib.Combinatorics.HeckeAlgebra`) | Partial — no Wenzl, no Markov trace |
| Markov trace on Hecke algebras | **None** | **Gap** |
| Jones-Wenzl projector | **None** | **Gap** |
| Bloch-Wigner dilogarithm | Limited (real Li_2 yes, BW form no) | Partial |
| Type-B folded crystals | **None** | **Gap** |

**Net**: Mathlib has the combinatorial foundation (Young diagrams,
tableaux, Schur polynomials) but NO crystal-graph, KLR, or
Demazure-module machinery, and NO Markov trace on Hecke algebras.

## What residue A needs (composite operator)

Per the 4-search NEGATIVE bracket
([acceptance doc](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md)),
residue A lives in a **composite Kashiwara operator structure**.
Concrete composite candidates that need infrastructure:

### Composite 1: Demazure × q-Pochhammer mixed trace

`F(u) = Σ_w D_w(λ) · (q;q)_{ℓ(w)} · u^{ℓ(w)}`

where `D_w(λ)` is the Demazure character at element w of S_n, and
`(q;q)_k` is the finite q-Pochhammer. **Needs**:
- Lean: `Demazure` namespace with character `D_w(λ) : ℝ`
- Python: Demazure-character evaluator at q₀

### Composite 2: KLR canonical-basis-weighted Markov trace

`F(u) = Σ_{b ∈ KLR canonical basis} τ(b) · q^{deg(b)} · u^{|b|}`

where `τ` is the Markov trace and `deg(b)` is the KLR grading.
**Needs**:
- Lean: KLR algebra `KLR(Γ)` with canonical basis enumeration
- Python: `KLR canonical basis` Python module + Markov trace
  linear extension

### Composite 3: Type-B folded crystal sum

`F(u) = Σ_{T ∈ B_{Type-B fold}(λ)} q^{c(T)} · u^{|T|}`

where `B_{Type-B fold}(λ)` is the Type-B-folded Kashiwara crystal of
the highest-weight rep V(λ), per AGENTS.md §7b authoring guidance.
**Needs**:
- Lean: Type-B Cartan datum + crystal folding
- Python: crystal-graph node enumeration + content statistic

### Composite 4: Wenzl-projector tower with q-Pochhammer modulation

`F(u) = Π_{k=2}^{∞} (1 + tr_M(p_k^{JW}) · (q;q)_k · u^k)`

Combines Family α (Wenzl projector Markov trace, NEGATIVE alone)
with Family β (Kashaev q-Pochhammer, NEGATIVE alone) — symmetric
combination not tested in Chain 1 first-tests.
**Needs**:
- Lean: Wenzl projector definition + p_k^{JW} construction
- Python: linear-combination `tr_M` extension in `pyhecke`

## Estimated effort per composite

| Composite | Lean infra cost | Python infra cost | Test cost | Total |
|---|---|---|---|---|
| 1 (Demazure × q-Poch) | 3-5 sessions | 1 session | 1 session | **5-7 sessions** |
| 2 (KLR canonical basis) | 5-8 sessions | 2-3 sessions | 1 session | **8-12 sessions** |
| 3 (Type-B folded crystal) | 8-12 sessions | 3-4 sessions | 1 session | **12-17 sessions** |
| 4 (Wenzl × q-Poch) | 2-3 sessions | 2 sessions | 1 session | **5-6 sessions** |

**Cheapest first-attempt**: Composite 4 (Wenzl × q-Pochhammer). Cost
roughly half a small paper's infrastructure. Probability of landing
within 10 ppm at both anchors: research-grade unknown.

**Most principled**: Composite 3 (Type-B folded crystal). Aligns with
AGENTS.md §7b authoring guidance about Type-B folding for chirality /
matter-antimatter. But highest cost.

## Recommended next-action options (owner direction needed)

| Option | Action | Trade-off |
|---|---|---|
| **A. Stop chasing c_3 promotion** | Accept residue A as inherently CAL-3-anchored permanently. Focus future work on the OTHER 6 L2-failing observables (m_μ 963.6×, m_n 185.4×, Δ_pn 163.3×, plus 100× still-active ladder for m_⁴He / Q_α) | Lowest cost; preserves the 4-of-7 L2 met state without infrastructural investment |
| **B. Composite 4 (Wenzl × q-Pochhammer)** | Cheapest composite — 5-6 sessions of infrastructure to add Wenzl projector + linear `tr_M` to `pyhecke`, then test the composite at q₀ | Moderate cost; probability of residue A unknown but at least tests a NEW combinator |
| **C. Composite 1 (Demazure × q-Pochhammer)** | 5-7 sessions; Demazure infra is genuinely useful beyond Q_β (mass-formula crystal-multiplicity work would also benefit) | Moderate cost; infrastructure benefits multiple goals |
| **D. Composite 3 (Type-B folded crystal)** | 12-17 sessions; aligns with §7b authoring guidance + matter-antimatter structural framework | Highest cost; highest theoretical value if landed |

The Δ_λ gate forbids me picking the option without explicit owner direction. This doc is the scope artifact for that decision.

## Cross-refs

- [4-search acceptance doc](../audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md)
- [1ppQ Q_β master ledger](../coordination/1ppq-qbeta.md)
- [Chain 1 scope (closed)](../coordination/2026-06-03-qbeta-habiro-chain-1-scope.md)
- [Q_β truncation-order audit](../audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- AGENTS.md §"Precision goals" — L2 status
- AGENTS.md §7b — symmetric-crystal authoring guidance
