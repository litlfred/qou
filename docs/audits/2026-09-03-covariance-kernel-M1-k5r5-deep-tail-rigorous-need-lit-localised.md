# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the far tail is rigorous corpus-free; the need-lit is localised to one bounded band

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-attack-2026-09-03` · **Tier:** a rigorous
corpus-free sub-bound + a precise "need lit?" localisation (after reviewing the ~2400-commit main
advance) · **Discipline:** no fit; nothing wired; no `c_k`; L2 unchanged; a vacuous first bound was
caught and fixed, not shipped. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Where the gap actually stands (main review, 2026-09-03)

Since this branch's session-of-origin, a large parallel effort landed the whole reduction on `main`:

- **Reduction Lean-proved.** `YoungDiagramKernelCSMargin.m1_pos_of_cs_margin` /
  `m1_pos_all_of_cs_inputs` (sorry-free): the Cauchy–Schwarz core derives `M₁>0` from the (CS)
  analytic inputs `σ_A, σ_D, ρ_P` carried as hypotheses (§3b-cond, non-degenerate).
- **Leading order derived.** `m_∞ = ρ_P^∞ − √(V_D/V_A) = 0.30019 > 0` is *derived* (rigorous modulo
  the published Ivanov–Olshanski CLT, cited not re-proved); its two byproduct constants `0.9798`,
  `0.6796` match the exact finite-n data (audit `…io-leading-order-CS-derived.md`).
- **Finite part certified.** `M₁>0` exact (`Fraction`, no rounding) for **n ≤ 78**; the exact (CS)
  margin `>0` for `n ≤ 42`.
- **Route decided.** Route 1 (Kerov limit shape + `CompositeEulerMaclaurin` with explicit remainder,
  both sorry-free in-repo) over Route 2 (Bessel-J uniform asymptotics).

So the **entire remaining gap** is one rigorous finite-n bound `|m(n) − m_∞| ≤ C·n^{−1/2}` with
`N₀ = ⌈(C/m_∞)²⌉ ≤ 78`, i.e. **`C ≤ m_∞·√78 = 2.65`**. Empirically `C_emp ≈ 0.087` and *decreasing*
(audit `…constant-C-and-N0.md`) — **~30× headroom**: any rigorous `C ≤ 2.65` closes `M₁>0` for all n.
The binding sub-constant is **`C_A`** (the `Var(Σ|c|)` kink ingredient, the slowest at `n^{−1/2}`);
tail, sine-truncation, de-poissonization and ratio-propagation are all pinnable from published bounds.

## "Need lit?" — YES, and this note localises it to one bounded band

The three-region split of `C_A` is: (1) tail `|x| > 2√θ`, (2) oscillatory bulk (Bessel→sine error),
(3) Airy edge. Region (2) needs an **explicit uniform Bessel remainder** for `J_ν(2√θ)`. Corpus-grep
(paths 1–6, incl. `library/*/sections/`): the corpus holds BOO, BDJ, IO, Charlier–Claeys, Tracy–Widom,
`CompositeEulerMaclaurin`, Gaussian bounds — but **not** Olver's error-bounded uniform asymptotic
(DLMF §10.19/§10.20 + Olver 1997 Ch. 10). That is the one missing published input.

This note sharpens *which part* of `C_A` needs it, by disposing of the far tail with corpus-free
elementary bounds.

### The far tail is rigorously negligible without Olver (this note)

Two standard, corpus-free bounds hold for integer `x` and real argument:

- **DLMF 10.14.4** (real argument): `|J_x(2√θ)| ≤ θ^{x/2}/x!` — tight only in the deep tail
  `x > e√θ`, exponentially loose in the bulk.
- **Universal**: `|J_n(z)| ≤ 1` for integer `n`, real `z`.

Their **minimum** `Jb(x) := min(θ^{x/2}/x!, 1)` is a valid bound everywhere.
[`wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py)
(exit 0; `mpmath` 50 dps; NO float64) uses it to bound the far-tail share of
`V_A = ½Σ(g(x)−g(y))²J(x,y;θ)²` (`J(x,y)=√θ(J_xJ_{y+1}−J_{x+1}J_y)/(x−y)`, `g=G_A`), taking the cutoff
`X*` where `θ^{X*/2}/X* ! < 10^{−20}`:

| θ | edge `2√θ` | `X*` | far-tail `V_A` share (rigorous ≤) |
|---|---|---|---|
| 100 | 20.0 | 58 | `1.6×10⁻³⁸` |
| 256 | 32.0 | 77 | `1.5×10⁻³⁸` |
| 640 | 50.6 | 104 | `1.0×10⁻³⁷` |

(sanity: `max |besselj|/Jb ≤ 0.47` across the grid — the bound is valid). So the contribution from
`|x| > X*` is **rigorously** below `10⁻³⁷·V_A` with **no** uniform-asymptotic input.

### What remains genuinely Olver-dependent

The elementary bounds cannot resolve `x ∈ (2√θ, X*]` — a band of width `~O(√θ)` (measured 38, 45, 53
for θ=100, 256, 640) — because there `|J| ≤ 1` is far too crude to expose the `O(θ^{−1/2})`
Bessel→sine **cancellation** that actually sets `C_A`. That band (edge + transition + outer-bulk),
together with the bulk oscillatory error itself, is exactly and only where Olver's explicit uniform
remainder is required.

### A caught error (discipline note)

The first version of the majorant used only `θ^{x/2}/x!` and coupled tail indices to **bulk** indices,
where that factor is exponentially large — giving a "bound" of `10⁸`–`10¹⁵ × V_A`, i.e. **vacuous**.
That was *not* shipped; the fix (take `min(·,1)` per index, push `X*` to where the factor `< 10⁻²⁰`)
is what makes the far-tail bound genuine. Recorded because the loose version *looks* like a rigorous
tail bound and is not.

## Honest status

Gap `qou-k5r5` **OPEN**, now with the need-lit pinned to a single bounded band. Rigorous corpus-free
this note: the far tail `|x| > X*` (`X* ~ e√θ + O(√θ)`) is `< 10⁻³⁷·V_A`. Everything else in the
closure is either already rigorous (reduction Lean-proved; `m_∞` derived; `n≤78` exact) or pinnable
from published bounds — **except** the `C_A` bulk band `x ≤ X*`, which needs Olver's uniform Bessel
remainder (not in corpus). The next honest step is to ingest that reference and carry it through the
`x²`-weighted band to a verified `C_A ≤ 2.65` — a well-scoped multi-page estimate with ~30× headroom,
not a new idea, and **not** to be faked without the bound in hand.

## Compute + sources

- [`wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py)
  (exit 0; NO float64; far-tail `< 10⁻³⁷·V_A` rigorous corpus-free).
- Elementary bounds: DLMF 10.14.4 (`|J_ν(z)| ≤ (z/2)^ν/Γ(ν+1)`), `|J_n(real)| ≤ 1`.
- Missing input (region `x ≤ X*`): Olver, *Asymptotics and Special Functions* (1997) Ch. 10 error
  bounds / DLMF §10.19–§10.20 — **not in corpus**.

## Cross-references

- Route + inventory: [`2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`](2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md)
- Constant `C` / `N₀`: [`2026-08-29-covariance-kernel-M1-constant-C-and-N0.md`](2026-08-29-covariance-kernel-M1-constant-C-and-N0.md)
- Rigorous finite-n bound: [`2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md)
- Epic `qou-x631`; gap `qou-k5r5`.
