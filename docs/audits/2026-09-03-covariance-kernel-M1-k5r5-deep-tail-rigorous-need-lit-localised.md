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

Their **minimum** `Jb(x) := min(θ^{|x|/2}/|x|!, 1)` is a valid bound everywhere (bound (i) alone
*exceeds 1* in the bulk, so the `min` is what makes it usable there).
[`wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py)
(exit 0; `mpmath` 50 dps; NO float64) bounds the far tail of
`V_A = ½Σ(g(x)−g(y))²J(x,y;θ)²` (`J(x,y)=√θ(J_xJ_{y+1}−J_{x+1}J_y)/(x−y)`, `g=G_A`), with cutoff `X*`
the first index where the (i)-factor `θ^{X*/2}/X*! < 10^{−20}`.

The **share** is made rigorous by bounding `V_A` from *below* as well: every term of `V_A` is a
product of two squares, hence non-negative, so any windowed partial sum is a valid lower bound.

| θ | edge `2√θ` | `X*` | far-tail **absolute** bound ≤ | rigorous `V_A ≥` | rigorous share ≤ |
|---|---|---|---|---|---|
| 100 | 20.0 | 58 | `1.26×10⁻³⁴` | `7.02×10³` | `1.8×10⁻³⁸` |
| 256 | 32.0 | 77 | `7.63×10⁻³⁴` | `4.71×10⁴` | `1.6×10⁻³⁸` |
| 640 | 50.6 | 104 | `3.29×10⁻³²` | `3.07×10⁵` | `1.1×10⁻³⁷` |

(sanity: `max |besselj|/Jb ≤ 0.42` across the grid — the bound is valid). So the contribution from
`|x| > X*` is **rigorously** below `1.1×10⁻³⁷·V_A` with **no** uniform-asymptotic input — both the
numerator (majorant) and the denominator (non-negative partial sum) being rigorous bounds in the
correct directions.

> **Correction (Copilot review, same day).** The first version of this table divided the rigorous
> absolute bound by the *measured* reference scale `0.8106·θ²` and labelled the quotient a rigorous
> share. That overstated rigor: a rigorous ratio needs a proven **lower** bound on `V_A`. Fixed above
> by the non-negative-partial-sum lower bound; the numbers moved only in the 2nd digit
> (`1.6→1.7×10⁻³⁸`), so the conclusion is unchanged — but the claim is now actually proved.

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

## 🛑 CORRECTION (same day): acquiring Olver's bound would NOT close it — the pointwise route fails

The section above, and my own recommendation to the owner ("fetch Olver, then track `C_A`"), assumed
that an explicit **pointwise** remainder `|J − S| ≤ ε ~ K·θ^{−1/2}` could be carried through the
weighted sum to give `C_A`. **Measured: it cannot, for any constant `K`.**

Write `J = S + E`. Then `V_A(J) − V_A(S) = ½Σ w·E·(2S + E)`, so *any* pointwise bound gives at best
`|ΔV| ≤ ε·U + …` with `U := Σ w |S|`, against `V := ½Σ w S² = V_A`. The relevant quantity is `U/V`.
[`wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py)
(exit 0; NO float64) computes both from the **exact** discrete Bessel kernel:

| θ | 64 | 78 | 128 | 256 | 512 |
|---|---|---|---|---|---|
| `U/V` | 42.78 | **45.65** | 53.87 | 70.71 | 91.91 |

`U/V` grows without bound (`d log(U/V)/d log θ` = 0.33→0.39, still drifting; growth is *sub*-`√θ` —
the normalised `(U/V)/√θ` decreases 5.35→4.06, so **do not quote "`U/V ~ √θ`"**; the exponent is not
pinned and the conclusion does not need it).

**The decisive number is a direct measurement, not an extrapolation.** At `θ = 78` — the largest `n`
the exact `Fraction` table reaches, hence exactly where the asymptotic must take over — `U/V = 45.65`,
so a pointwise `ε = K·θ^{−1/2}` gives a *relative* error on `V_A` of `≈ 5.17·K`. Keeping that below
`m_∞ = 0.3002` forces

> **`K < 0.058`**, whereas the leading Debye/Olver remainder coefficient is `O(1)` — short by ~17×.

So a sharper **pointwise-magnitude** bound cannot close `N₀ ≤ 78` however good its constant. The
**oscillatory cancellation** in `Σ w·S·E` (summation by parts / stationary phase) is load-bearing, not
a refinement.

**Consequences, stated plainly:**

1. **My "need lit? → fetch Olver" recommendation is retracted.** Acquiring DLMF §10.19/§10.20 or
   Olver 1997 would not, by itself, pin `C_A`. (Moot in any case: `arxiv.org` and `dlmf.nist.gov` are
   both blocked by org egress policy — 403 on CONNECT — so this agent cannot fetch them; per the proxy
   rules that is reported, not routed around.)
2. **This *reinforces* the corpus's own Route-1 decision.** Route 1 (Kerov limit shape +
   `CompositeEulerMaclaurin`) never forms the pointwise `|J − S|` difference at all — it works with
   the smooth limit-shape integrands, where EM's explicit remainder *is* the constant. Route 2 (the
   Bessel route this note started down) is the one that needs the cancellation.
3. **Route 1's missing piece is not literature.** It is the Kerov/VKLS limit shape and its
   fluctuation field as *analytic* objects (per the inventory audit) — a build, with the underlying
   theorems (Kerov CLT, IO) already published and IO already in corpus.

## Honest status

Gap `qou-k5r5` **OPEN**. Two results, one positive and one negative, both rigorous/measured:

- **Positive (corpus-free):** the far tail `|x| > X*` (`X* ~ e√θ + O(√θ)`) contributes
  `≤ 1.1×10⁻³⁷·V_A`, by elementary bounds alone (majorant above, non-negative-partial-sum lower bound
  on `V_A` below).
- **Negative (decisive):** the **pointwise** Bessel-remainder route to `C_A` cannot work — at `θ=78`
  it demands a remainder constant `K < 0.058` against an `O(1)` Debye coefficient. So "get Olver's
  bound" is *not* the next step, and the answer to **"need lit?" is NO** for the chosen route.

The live route is unchanged and is **Route 1** (Kerov limit shape + `CompositeEulerMaclaurin`), whose
missing piece is an analytic build (the VKLS limit shape and Kerov fluctuation field as analytic
objects, feeding the EM remainder), not a citation. Everything else is already rigorous: reduction
Lean-proved, `m_∞ = 0.30019` derived, `M₁>0` exact for `n ≤ 78`, far tail as above.

## Compute + sources

- [`wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_deep_tail_rigorous_majorant.py)
  (exit 0; NO float64; far-tail `≤ 1.1×10⁻³⁷·V_A`, rigorous corpus-free in both directions).
- Elementary bounds: DLMF 10.14.4 (`|J_ν(z)| ≤ (z/2)^ν/Γ(ν+1)`), `|J_n(real)| ≤ 1`.
- Missing input (region `x ≤ X*`): Olver, *Asymptotics and Special Functions* (1997) Ch. 10 error
  bounds / DLMF §10.19–§10.20 — **not in corpus**.

## Cross-references

- Route + inventory: [`2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`](2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md)
- Constant `C` / `N₀`: [`2026-08-29-covariance-kernel-M1-constant-C-and-N0.md`](2026-08-29-covariance-kernel-M1-constant-C-and-N0.md)
- Rigorous finite-n bound: [`2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md)
- Epic `qou-x631`; gap `qou-k5r5`.
