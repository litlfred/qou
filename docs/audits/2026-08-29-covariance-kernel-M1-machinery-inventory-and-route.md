# Covariance-kernel epic (`qou-x631`) — M₁>0 analytic machinery: accurate inventory + route decision

**Date:** 2026-08-29 · **Branch:** `claude/m1-conditional-skeleton-and-machinery-2026-08-29` ·
**Tier:** infrastructure survey (corrects an earlier over-claim) + route decision · **Discipline:**
no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`; machinery epic
`qou-h315`.

## Why this exists — a corpus-grep correction

I earlier told the owner the closure needs *"Bessel/Debye/Euler–Maclaurin-remainder or
determinantal-CLT machinery that Mathlib does not have."* That is the exact failure the repo's
disciplines warn about: I checked **Mathlib** and not the **corpus**. Much of the machinery is
already in-repo, sorry-free. This audit records the accurate inventory so the remaining work is scoped
to what is genuinely missing.

## What already exists (sorry-free, in-repo)

| need | status | where |
|---|---|---|
| Euler–Maclaurin with **explicit remainder** | **built** (order 2, `\|R\| ≤ k·h⁵·M/720`) | `QOU/MathlibExt/CompositeEulerMaclaurin.lean` (`abs_integral_sub_composite_le`); one-cell rule `CorrectedTrapezoid.lean` (9 lemmas) |
| Gaussian tail / sum bounds (de-poissonization, edge) | **built** | `QOU/MathlibExt/GaussianTailBound.lean`, `GaussianSumBound.lean`, `GaussianThetaSum.lean`, `GaussianWindowSum.lean` |
| Lobachevsky / Clausen / dilog (limit-shape volume side) | **built** | `QOU/Archimedean/{BlochWignerLobachevsky,LobachevskyDerivative}.lean`, `QOU/Knot/Clausen.lean` |
| Mathlib Abel / Poisson summation | available | `Mathlib.NumberTheory.AbelSummation`, `Mathlib.Analysis.Fourier.PoissonSummation` |
| the reduction skeleton `[CS inputs] ⟹ M₁>0 ∀n` | **built this PR** | `YoungDiagramKernelCSMargin.m1_pos_all_of_cs_inputs` |

Shared with the c_σ arc: `qou-mlgp` names the identical Euler–Maclaurin-with-constant need (its item
(A)) and the same Gaussian/Lobachevsky infra — the two arcs share this machinery.

## What is genuinely missing — and two routes

The one open input is `hCS`: `σ_D(n) < ρ_P(n)·σ_A(n)` for `n ≥ N₀ ≤ 79`, i.e. explicit finite-n
bounds on the descent-DPP variance ingredients. Two routes:

**Route 1 — Kerov limit-shape + Euler–Maclaurin (uses existing `CompositeEulerMaclaurin`).**
Content statistics are integrals against the rotated profile; their variances, via the Kerov
fluctuation field, are smooth-integrand sums. Apply `abs_integral_sub_composite_le` to those
integrands to get the `θ^{−1}` correction with the explicit `M/720`-type constant. **Missing piece:**
the Kerov/VKLS limit shape and its fluctuation field as *analytic* objects in Lean (the `QOU`
tree has the `Sₙ` representation theory — Jucys–Murphy, Wedderburn — but not the analytic limit
shape). This route reuses the most existing infra.

**Route 2 — discrete Bessel kernel asymptotics (BOO).** Bound `V(g)=½Σ(g(x)−g(y))²J(x,y)²` directly
via the discrete Bessel kernel's uniform (Olver/Debye) asymptotics. **Missing piece:** `J_ν(2√θ)`
uniform asymptotics with explicit error — genuinely absent (Mathlib's only `bessel` is the
inner-product inequality; the repo's `QBessel*` files are the *algebraic* q-Bessel, not analytic
`J_ν`). This route needs the most new infrastructure.

**Route decision (`qou-2toh`): Route 1.** It reuses `CompositeEulerMaclaurin` (sorry-free, explicit
constant) and the Gaussian bounds; the kink already cancels (PR #5939), so the integrand is smooth and
the order-2 EM remainder is exactly the right tool. Route 2's Bessel-J asymptotics are a larger new
build with no other consumer in the corpus. The measured kink-cancellation (`c_{1/2}=0`, transpose
symmetry) is the structural fact that makes Route 1's smooth EM applicable.

## Decomposition (epic `qou-h315`)

- `qou-2toh` — route decision (**this audit: Route 1**).
- `qou-8quz` — rigorous transpose-symmetry proof `c_{1/2}=0` (finite substrate already Lean:
  `YoungDiagramTranspose.csq_transpose`, `YoungDiagramTransposeBridge.cells_conj`).
- `qou-tvok` — explicit `θ^{−1}` EM constant `C_A` for `Var(Σ|c|)` via `CompositeEulerMaclaurin`.
- `qou-po72` — the analogous `C_W`, `C_P`, `C_D` (smooth weights, easier than `C_A`).
- `qou-xs2c` — explicit de-poissonization `O(1/n)` constant (reuse `GaussianTailBound`/`GaussianSumBound`).
- `qou-jh3m` — ratio propagation `m = ρ_P − σ_D/σ_A → C →` verify `N₀ ≤ 78`, discharging `hCS`.

## Honest status

The closure is **not** done, but it is now accurately scoped: the reduction is Lean-proved
(`m1_pos_all_of_cs_inputs`), the kink is gone (`θ^{−1}`, PR #5939), and the analytic tools (EM with
explicit remainder, Gaussian bounds) **already exist sorry-free**. What remains is Route 1's
Kerov-profile layer + the constant assembly — a real but now well-scoped multi-piece build, tracked
under `qou-h315`. Gap `qou-k5r5` OPEN.

## Cross-references

- Reduction skeleton: `YoungDiagramKernelCSMargin.m1_pos_all_of_cs_inputs` (this PR).
- Kink cancellation: [`2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md`](2026-08-29-covariance-kernel-M1-debye-kink-cancellation.md)
- Shared machinery: bean `qou-mlgp` (c_σ arc, same EM/Gaussian/Lobachevsky need).
- Gap bean `qou-k5r5`; machinery epic `qou-h315`.
