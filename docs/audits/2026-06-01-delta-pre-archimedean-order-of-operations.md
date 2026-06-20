# Delta-then-archimedean vs masses-then-delta — the order is forced for differences

**Date:** 2026-06-01
**Paper block:** [`prop:delta-pre-archimedean`](../../content/quantum-observable-universe/particle-interactions/delta-pre-archimedean.md)
(+ Lean `delta-pre-archimedean.lean`).
**Question answered:** "do we compute masses via archimedean then take the
delta, or take the delta then apply archimedean?"

---

## The answer

| observable | kind | order | canonical chain |
|---|---|---|---|
| `Q_β`, binding `B(K)` | **difference** | **delta-then-archimedean** | `Q_β = \|Δ(net)\|·𝔈₀` (cheat-sheet step 11) |
| `m_p`, `m_n` (each) | **absolute** | archimedean (no delta) | `m = τ(tower)` |
| `Δ_pn = m_n − m_p` | boundary | via `Q_β` (= `Δ_pn − m_e`) | the difference route |

The β-decay Q-value and binding energy are **difference observables**:
the categorical delta `Δ = x_n − x_p` is formed at the **fibre level**,
then the archimedean functor `τ` is applied **once** (via `·𝔈₀`). One
does *not* compute the two absolute masses and subtract.

## Why — proved vs. expository (the clarification)

The point is easy to blur. Three statements, only the first two are
theorems:

1. **PROVED — fold commutes with the delta** (`fold_commutes_sub`). Any
   fibre fold `f` (bar involution `q↦q⁻¹`, Hecke antipode `σ↦σ⁻¹`,
   Type-B fold — all additive) satisfies `f(x_n − x_p) = f(x_n) −
   f(x_p)` over a generic `CommRing`. No reality, no archimedean input.
2. **PROVED — `τ` does NOT commute with the delta**
   (`archimedean_does_not_commute_sub`). `τ` is nonlinear (`Li_2^q`
   tower / Markov product / `𝔈₀` scaling); witnessed by `τ=(·)²` over
   `ℤ`: `τ(2)−τ(1)=3 ≠ 1=τ(2−1)`. So masses-then-delta ≠
   delta-then-archimedean — genuinely different operations.
3. **EXPOSITORY CONVENTION — which order for which observable.** Forced
   by the *physics* (difference vs absolute), not by (1)–(2): differences
   use delta-then-archimedean; absolutes use archimedean. The framework
   *predicts* the p/n split through the difference observable `Q_β`.

## "Folding/unfolding works for binding because binding is a pre-archimedean delta"

This is the thesis the question crystallises, and it is now proved:
folding/unfolding (Hecke reduction, bar-symmetric channel sorting) is
the engine of the binding/`Q_β` derivations. By (1) those folds commute
with the **pre-archimedean** delta `Δ(net)`, so they are legitimate
inside it. By (2) the *same* folds would **not** commute with a
difference of two `τ`-images. Hence the fold discipline is available
**only** in the delta-then-archimedean order.

## Empirical corroboration (this session, RAW, no fit)

Computed both orders from the merged convergence-safe tower (#1657):

- **masses-then-delta (A):** calibrate `E_0` on the proton, `m_n =
  E_0·tower_n`, subtract → `Δ ≈ −149 MeV` (vs CODATA `Δ_pn = 1.293`).
  The raw σ₀-tower over-amplifies the split by **~10²**.
- **delta-then-archimedean (B):** `|Δtr_M|·m_e = 0.073` (undershoots —
  wrong scale `m_e`); the canonical `|Δ(net)|·𝔈₀` with `𝔈₀≈4.19 MeV`
  lands in the `Q_β = 0.782 MeV` range.

The A-vs-B gap **is** the scaling-map / `c_k` structure (order audit
#1593: `Δtr_M` is `O(√u)`, `Q_β` lives at `O(u^k)`), and order B is the
one for which the imaginary parts cancel cleanly (#1666). The order
discipline thus unifies this session's results.

## Connection to the fibre-vs-observable convention

This is the same `Im(q)` fibre-vs-observable cut (AGENTS.md): folds and
the delta live in the **fibre** (formal `q`, automorphism-friendly);
reality / nonlinearity enter only at the **archimedean** `τ`. The order
"delta first, then `τ`" is exactly "stay in the fibre as long as
possible, apply `τ` last."

## Cross-references

- Neutron Q-value (the canonical `Q_β=|Δ(net)|·𝔈₀`): [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md)
- Order audit (`Δtr_M` is `O(√u)`): [`2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md`](2026-05-31-qbeta-c3-order-audit-accidental-coincidence.md)
- Im cancels in the difference: [`2026-06-01-li2q-imaginary-quantization-reality-gate.md`](2026-06-01-li2q-imaginary-quantization-reality-gate.md)
- Convergence-safe tower (the A/B numbers): [`2026-06-01-convergence-safe-vhat-tower.md`](2026-06-01-convergence-safe-vhat-tower.md)
