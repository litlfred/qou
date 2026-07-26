# Meromorphic infra build + the elliptic-freedom obstruction (2026-07-24)

**Axis:** A_ω / Faddeev–Volkov rigidity uniqueness leg (`qou-q95i` / `qou-2cvs`).
**PR:** #4155. **Branch:** `claude/aomega-uniqueness-dual-lattice-density-2026-07-24`.

Two results this session: (1) built the Mathlib `Meromorphic` olean cone from
source, unblocking the previously-"multi-week/environmentally-blocked" brick (c);
(2) with brick (c) proved, identified and **proved** the genuine remaining wall —
the `FaddeevPhi` class underdetermines the divisor (elliptic freedom), so the
same-divisor premise is not derivable from it.

## 1. Meromorphic infra build (unblocks brick (c))

Per [`2026-07-18-endowment-scope-meromorphic-wall.md` §3](2026-07-18-endowment-scope-meromorphic-wall.md),
route (B) needed `Mathlib.Analysis.Meromorphic.{Order,Divisor,NormalForm,…}`,
which are **absent from the `lake-cache/qou-v4-24-0` olean cache** (the QOU library
never imports them) and were reported unbuildable in-sandbox.

Resolved: github egress works (only the release-server olean cache / `lake exe
cache get` are firewalled), so mathlib **source** clones at the pinned rev. A BFS
over imports found the missing-olean set is exactly **10 modules**; compiling them
`lean`-direct against the restored oleans took ~2 min (no `lake` rebuild storm):

```
Mathlib.Analysis.Analytic.Order
Mathlib.Analysis.Meromorphic.Basic
Mathlib.Algebra.Order.WithTop.Untop0
Mathlib.Analysis.Meromorphic.Order
Mathlib.Analysis.Meromorphic.TrailingCoefficient
Mathlib.Topology.LocallyFinsupp
Mathlib.Analysis.Meromorphic.Divisor
Mathlib.Analysis.Meromorphic.NormalForm
Mathlib.Analysis.Meromorphic.IsolatedZeros
Mathlib.Analysis.Meromorphic.FactorizedRational
```

Reproducible recipe: [`scripts/build-meromorphic-cone.sh`](../../scripts/build-meromorphic-cone.sh)
(idempotent; clones source + builds the 10 modules). The oleans live under
`.lake/` (gitignored, container-ephemeral); re-run the script after a container
recycle. CI has full Mathlib and is unaffected.

## 2. Brick (c) — same divisor ⇒ entire ratio (PROVED)

[`QOU/QBeta/RatioEntireOfSameDivisor.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/RatioEntireOfSameDivisor.lean)
`entire_toMeromorphicNFOn_div_of_same_order`, sorry-free `lean`-direct exit 0.

The `0/0` junk at shared zeros is dissolved by Mathlib's meromorphic **normal
form**: `r = toMeromorphicNFOn (Ψ/Φ)` has `meromorphicOrderAt r = ord Ψ − ord Φ =
0` everywhere (same divisor), and a normal-form function of order `≥ 0` is analytic
(`MeromorphicNFAt.meromorphicOrderAt_nonneg_iff_analyticAt`). So `r` is entire.
This is the analytic content of `hr_entire`, previously the wall.

## 3. The genuine remaining wall — elliptic freedom (PROVED obstruction)

With brick (c) reducing the leg to the **same-divisor premise**, the question is
whether two `FaddeevPhi` solutions share a divisor. **They need not.**

The class (`QOU.MathlibExt.FaddeevQuantumDilogarithm.FaddeevPhi`) has exactly three
fields — `hb : 0 < b.re`, `shift_b`, `shift_binv` — all quasi-periodicity, with
**no analyticity/growth/divisor condition** on `Φ`. So an **elliptic** `e`
(periodic w.r.t. the lattice `⟨ib, i/b⟩`) cancels in both quasi-period prefactors,
and `e · Φ` is **again a `FaddeevPhi` solution**:

- [`QOU/QBeta/FaddeevPhiEllipticFreedom.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/FaddeevPhiEllipticFreedom.lean)
  `faddeevPhi_mul_elliptic` — sorry-free `lean`-direct exit 0.

A nonconstant such `e` (a Weierstrass `℘` for the lattice) has its own zeros/poles,
so `e · Φ` has a **different divisor** from `Φ`. Therefore:

> **Scope-(b), proved:** the same-divisor premise — and hence
> `PentagonRigidity.uniqueUpToScalar` (`Φ₁ = c·Φ₂`) — **cannot** be derived from the
> `FaddeevPhi` class as axiomatised.

This is a **missing hypothesis on the class**, not a gap in the reduction. The
genuine Faddeev–Volkov rigidity requires a strengthening that excludes the elliptic
factor: analyticity / bounded growth in a fundamental horizontal strip (a `℘` has
poles there), or the explicit `PhiBProd` product characterisation
(`QOU.MathlibExt.PhiBProd`, which pins the divisor to simple zeros on the `b`-lattice
and simple poles on the `1/b`-lattice).

## Net state of the uniqueness leg

| Piece | Status |
|-------|--------|
| Prefactor-lattice density pair (`dense_{dual,primary}Pole_compl`) | proved |
| Concrete `Φ_b` reduction to `hr_entire` (`faddeevPhi_proportional_of_ratio_entire`) | proved |
| Brick (c): same divisor ⇒ entire ratio | **proved** (needs Meromorphic infra) |
| Same-divisor premise from the class alone | **impossible** (elliptic freedom, proved) |
| The actual close | needs a class strengthening (strip-growth / `PhiBProd` divisor) |

The analytic wall is down; the remaining wall is a **characterisation** wall —
strengthen `FaddeevPhi` (or use `PhiBProd`) so the elliptic factor is excluded.
Nothing fitted, nothing axiomatised; `conj:algebraic-geometric-dilog-equivalence`
stays open, now with the obstruction precisely located.

---

## Toolbox note from the 4₁ saddle program (2026-07-26, sibling session, bean qou-ja69)

For the remaining **strip-growth / `PhiBProd` divisor** leg: the volume-conjecture
discharge landed reusable product-growth mechanics on main —
`Analysis`-free sum-vs-integral comparisons for `log`-products of unimodal factors
(`QOU/Knot/Clausen.lean`: monotone/antitone Riemann bounds, the all-k uniform
deviation `abs_deviation_le` with vanishing master error `tendsto_master_error`,
and the `log Σ ≤ log N + log max` step `log_kashaev_le_log_add`), plus the
Clausen/Lobachevsky primitive fully machine-proved (`hasDerivAt_clausen`,
series↔integral bridge). If the `PhiBProd` strip-growth estimate can be phrased as
a product over a 1D sub-lattice with a unimodal log-factor profile, these bricks
give the growth rate without contour integration — the same move that made the 4₁
and (feasibility-confirmed) Borromean Kashaev sums elementary
(`docs/audits/2026-07-26-borromean-kashaev-positive-sum-feasibility.md`).
Measured overlap note only; no claim that the 2D lattice case reduces — flag to
qou-jpwy if it does.
