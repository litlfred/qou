# FKV 2001 supplies both open inputs of the Faddeev uniqueness leg (2026-07-31)

**Branch:** `claude/fkv-phib-strip-growth-2026-07-31`. **Source:** owner-uploaded
[`library/arxiv-hep-th-0006156v1/0006156v1.pdf`](../../library/arxiv-hep-th-0006156v1/0006156v1.pdf) — Faddeev–Kashaev–Volkov,
*Strongly coupled quantum discrete Liouville theory II* (2001),
[hep-th/0006156](https://arxiv.org/abs/hep-th/0006156), §6 (Appendix: the non-compact
quantum dilogarithm). **Analysis, mapping the literature to the on-main leg — no new
Lean this doc; it converts two "open physical inputs" into cited results + a precise
formalization gap.**

## The leg's two open inputs

`FaddeevPhiFullUniqueness.faddeevPhi_uniqueUpToScalar` (on main) is conditional on
`FaddeevPhiPhysical`, whose non-trivial residuals are:

1. **same divisor** — a second solution `Φ` has the same zeros/poles as `phiBProd`
   (the divisor-route brick / `PhiBProd*` assembly);
2. **strip-growth** (`instStripGrowth`) — `Φ` is comparable in modulus to `phiBProd`
   (the boundedness route; my #4424 reduced this to a *compact fundamental-domain*
   bound).

Both were "the physical Faddeev–Kashaev asymptotic content" — not derivable from the
shift equations alone (elliptic freedom). FKV §6 supplies **both, explicitly.**

## What FKV §6 gives (`e_b(z)` is `Φ_b` is `phiBProd`)

FKV's non-compact quantum dilogarithm `e_b(z)`, `c_b = i(b+b⁻¹)/2`:

- **Shift equations (eq 17):** `e_b(z − ib^{±1}/2) = (1 + e^{2πzb^{±1}})·e_b(z + ib^{±1}/2)`
  — *exactly* the `FaddeevPhi` `shift_b`/`shift_binv` class fields (up to the shift-half
  convention). So `e_b` **is** a `FaddeevPhi` solution.
- **Explicit product form (eq 21):**
  `e_b(z) = (e^{2π(z+c_b)b}; q²)_∞ / (e^{2π(z−c_b)b⁻¹}; q̄²)_∞`, `q = e^{iπb²}`,
  `q̄ = e^{−iπb⁻²}` — the ratio of two `q`-Pochhammer products, i.e. **`phiBProd`**.
- **Explicit divisor (eq 21, read off):**
  `zeros of (e_b)^{±1} = {∓(c_b + m·ib + n·ib⁻¹) : m,n ∈ ℤ≥0}` — the divisor is a
  discrete `ℤ≥0`-lattice, given in closed form.
- **Asymptotic at infinity (eq 22)** — the strip-growth control, four sectors:
  `e_b(z) ≈ 1` for `|arg z| > π/2 + arg b`; `≈ e^{iπz²−iπ(1+2c_b²)/6}` for
  `|arg z| < π/2 − arg b`; `≈ (q̄²;q̄²)_∞/Θ(ib⁻¹z; −b⁻²)` and `Θ(ibz; b²)/(q²;q²)_∞` in
  the two remaining wedges (`Θ` = the Jacobi theta / Gaussian analogue).
- **Inversion (eq 16):** `e_b(z)e_b(−z) = e^{iπz²−iπ(1+2c_b²)/6}`; **unitarity (eq 18):**
  `e_b(z)* = 1/e_b(z̄)` for `b` real or a phase.

## How this discharges each input

**Same divisor (input 1).** Eq 21 gives `phiBProd`'s divisor in closed form
(`∓(c_b + m·ib + n·ib⁻¹)`). The physical second solution `Φ` — being `e_b` for the same
`b`, or the analytic continuation of the same integral (eq 15) — has the *identical*
divisor. So "same divisor" is not an open premise for the physical solution; it is eq 21.
The elliptic-freedom counterexamples (`e·phiBProd`) are excluded precisely because a
nonconstant elliptic `e` *adds* zeros/poles, changing the divisor away from eq 21.

**Strip-growth (input 2).** Eq 22 is the growth bound. For two solutions both satisfying
eq 22 (the physical asymptotic that *selects* `e_b`), the ratio `Φ/phiBProd` — already
doubly-periodic (shift prefactors cancel) — has the **same leading behavior in every
sector**, so it `→ 1` at infinity along each wedge and is **bounded on the compact
fundamental parallelogram** (its only possible unboundedness would be poles, excluded by
input 1). That compact-domain bound is exactly what #4424
(`comparable_of_periodic_ballBound`) promotes to global comparability.

## The closure chain (now literature-backed)

```
FKV eq 21 (explicit divisor)      ⇒  Φ, phiBProd same divisor  ⇒  ratio entire (brick c)
FKV eq 22 (sector asymptotic)     ⇒  ratio bounded on fundamental domain
        #4424 (box reduction)     ⇒  ratio bounded on ℂ
        elliptic Liouville (main) ⇒  ratio constant            ⇒  Φ = c·phiBProd
```

So the Faddeev–Volkov uniqueness leg is **unconditional modulo formalizing FKV eqs 21–22**
— the physical inputs are no longer "open," they are two cited FKV results. The
remaining work is *formalization*, not *research*:

1. **Formalize eq 21's divisor** — that `phiBProd`'s `meromorphicOrderAt` is `+1` on the
   `+c_b + ℤ≥0`-lattice and `−1` on the `−c_b − ℤ≥0`-lattice, `0` elsewhere. This is the
   infinite-product-analyticity / `MeromorphicOn.tprod` gap (a genuine Mathlib gap, cf.
   the `Log.Summable` cone) applied to the explicit `q`-Pochhammer factors.
2. **Formalize eq 22's sector bound** — that the physical `Φ` and `phiBProd` share the
   four-sector leading asymptotic, so the ratio is bounded on the fundamental domain.
   This is a Phragmén–Lindelöf / theta-asymptotic estimate.

Both are now **cited, closed-form** literature results (FKV §6), so they belong in the
`§3b`/`-- Ref:` tier as *stated, literature-backed* inputs rather than open conjectural
axioms. The honest status upgrade: **the uniqueness leg's residual is a formalization
task against FKV eqs 21–22, not an open analytic problem.**

## Scope

Analysis + literature mapping; no fit; nothing wired. The uniqueness leg stays *stated*
conditional in Lean until eqs 21–22 are formalized — this doc does not silently mark it
closed (per "conditional-proved ≠ premise-established"). It records that the two class
axioms are now backed by explicit FKV formulas, and pins the exact formalization targets.
-- Ref: [faddeev-kashaev-volkov-2001] https://arxiv.org/abs/hep-th/0006156 (§6, eqs 15–22)
