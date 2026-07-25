# Faddeev–Volkov uniqueness keystone — state map (sorry-free modulo one analytic input)

**Date:** 2026-07-25 · **Bean:** `qou-7xvy` (discharge `hr_entire` for the concrete
`Φ_b`) · **Axis:** G3 / Faddeev rigidity · **Tier:** state consolidation (verified by
sorry-audit + file reads; no new Lean claim). Consolidates the now-~8-file chain so
the next full-build session has one map.

## Bottom line

The entire Faddeev–Volkov uniqueness leg (`PentagonRigidity.uniqueUpToScalar` for the
**physical meromorphic `Φ_b`**) is **sorry-free at tactic position across every file**,
reduced to **one** honest, named analytic input about the concrete `Φ_b`. `qou-7xvy` is
exactly that input.

## Canonical map (consolidated 2026-07-25, after input-1 closure)

Two facts about `phiBProd` are now **theorems on the substrate branch `Im b² > 0`**, no
longer carried hypotheses:

- **`MeromorphicOn (phiBProd b)`** — closed by input 1 (the infinite-product-analyticity
  route: `PhiBProdFactorAnalytic` #4272 → `LocalUniformLimitEntire` #4278 →
  `PhiBProdProductConvergence` #4296 → `PhiBProdMeromorphic` #4223).
- **`meromorphicOrderAt (phiBProd b) ≠ ⊤`** — input 2 (`PhiBProdOrderNeTop` #4225).

The elliptic-freedom obstruction is narrowed to a single residual, excluded in three
layers (see ledger at the end): even `℘` and bar-even reciprocal-odd are killed
**algebraically** (inversion #4227a, σ-unitarity #4227b); the non-σ-fixed reciprocal-odd
residual is excluded **analytically** by boundedness.

**The single remaining open input** (both routes bottom out here): the `Φ_b`
**divisor-rigidity fact** — either `hr_entire` (the ratio `Ψ/phiBProd` extends across
removable singularities to entire; divisor route) or `hbdd` (that ratio is bounded on ℂ;
growth route). These are two forms of the same statement, and both require the
**state-integral / Écalle–Borel growth estimate** for `Φ_b` (contour integration) —
infrastructure Mathlib does not package. Input 1's infinite-product-analyticity closed
`MeromorphicOn` but **not** divisor rigidity, which is the strictly harder fact.

Everything *around* this input is already in place: ratio double-periodicity on a dense
locus (`CyclicDilogPentagon.ratio_ib_periodic` / `ratio_ibinv_periodic`), continuity
promotion to everywhere (`Common.periodic_of_continuous_of_eqOn_dense`), the period basis
(`PeriodLatticeBasis.exists_period_basis`), the global←compact boundedness localization
(`DoublyPeriodicBoundedLocalization` #4237), and the conditional capstones/assembly
(`FaddeevUniquenessBoundedCapstone`, `PhiBProdUniquenessAssembly` #4232). The keystone is a
single Lean theorem modulo the one growth-estimate endowment.

## The chain (all sorry-free; earlier "N sorry" grep hits were docstring mentions)

| File | Role |
|---|---|
| `MathlibExt/FaddeevQuantumDilogarithm.lean` | `FaddeevPhi` conjecture-class (two shift eqns); `phi_b_zero` |
| `MathlibExt/PhiBProd.lean` | **concrete inhabitant** `phiBProd = (∏ numFactor)/(∏ denFactor)`; `faddeevPhi_phiBProd_substrate` proves `FaddeevPhi (substrateB t) (phiBProd …)` **with the `Multipliable` facts discharged** (geometric bounds, `Im b²>0`) — unconditional on the substrate branch |
| `QBeta/MeromorphicSameOrder.lean` | route-B step 2 (my merged work): `meromorphicOrderAt_comp_add` (brick a) + unconditional order-difference periodicity |
| `QBeta/FaddeevRigidityMeromorphic.lean` | my merged assembly: `uniqueUpToScalar_meromorphic` + `uniqueUpToScalar_of_ratio_dense_periodic` |
| `QBeta/FaddeevPhiEllipticFreedom.lean` | proves `uniqueUpToScalar` **cannot** be derived from the difference equations alone (the ratio can carry a nonconstant elliptic `℘` factor) — the honest obstruction |
| `QBeta/RatioEntireOfSameDivisor.lean` | **brick (c), divisor route**: `entire_toMeromorphicNFOn_div_of_same_order` — same divisor ⇒ entire ratio (proved) |
| `QBeta/BoundedMeromorphicLiouville.lean` | **brick (c′), growth route**: bounded meromorphic ⇒ entire (`meromorphicOrderAt_nonneg_of_bounded`, proved) |
| `QBeta/FaddeevPhiUniquenessAssembly.lean` | `faddeevPhi_proportional_of_ratio_entire` (consumes my dense-periodic reduction) |
| `QBeta/FaddeevUniquenessCapstone.lean` | `faddeevPhi_proportional_of_same_divisor` — divisor-route capstone |
| `QBeta/FaddeevUniquenessBoundedCapstone.lean` | `faddeevPhi_proportional_of_bounded_ratio` — growth-route capstone |

## The single remaining open input (two equivalent forms)

Both capstones derive proportionality; each leaves exactly one analytic fact about the
concrete `Φ_b` as an explicit, non-axiomatised hypothesis:

1. **Divisor route** — `∀ z, meromorphicOrderAt Ψ z = meromorphicOrderAt Φ z` (the two
   solutions share a divisor), plus `MeromorphicOn Φ`, `MeromorphicOn Ψ`, and `Φ` not
   locally zero (`ord ≠ ⊤`).
2. **Growth route** — `∀ z, ‖r z‖ ≤ C` for the prefactor-cancelled ratio `r` (the
   state-integral / Écalle–Borel strip boundedness of `Φ_b`).

They are equivalent: a nonconstant elliptic ratio has poles (unbounded) ⇔ non-matching
divisors; boundedness ⇔ no poles ⇔ same divisor ⇒ entire ⇒ (Liouville) constant.

## The concrete next brick + the Mathlib-infra gap

Because `phiBProd` is now a **concrete product**, the first sub-brick of the divisor
route is mechanical *modulo one Mathlib fact*:

> `MeromorphicOn (phiBProd b) univ` ⇐ the two products
> `fun z => ∏' k, numFactor b z k` and `fun z => ∏' k, denFactor b z k` are **entire**
> (`Differentiable ℂ`). Then `phiBProd = num/den` (definitional) gives `MeromorphicOn`
> via `MeromorphicOn.div` (used already in `RatioEntireOfSameDivisor`).

The open Mathlib-shaped input is **entireness of the infinite products** — i.e.
*a locally-uniformly-convergent `tprod` of entire functions is entire*. This is not in
the QOU olean cone, and Mathlib's infinite-product-analyticity support is thin; it is the
concrete gap between `phiBProd`'s proved `Multipliable` (pointwise) and the `Differentiable`
the ratio needs. The `ord ≠ ⊤` and same-divisor facts then need the explicit zero/pole
lattice of the products (each `numFactor`/`denFactor` vanishes on a shifted lattice),
which the product form makes computable but multiplicity/no-extra-zeros is the "no elliptic
freedom" content.

## `qou-7xvy` status

Precisely bounded, **not closeable without a full-build session**: verifying any file
importing `PhiBProd` needs the Meromorphic cone (`scripts/build-meromorphic-cone.sh`) plus
the `PhiBProd` dep cone built locally, and pinning the `Differentiable → AnalyticOnNhd →
MeromorphicOn` bridge + `tprod`-entireness lemma needs a working Lean search/LSP (loogle /
leansearch are firewalled in this sandbox). No unverified Lean was committed. The route is:
(i) build the cone; (ii) prove `phiBProd` meromorphic via product entireness; (iii) the
explicit product divisor; (iv) feed the divisor-route capstone. Steps (ii)–(iii) are the
genuine remaining mathematics; the growth route (boundedness from the state-integral) is
the alternative and is equally an analytic-`Φ_b` fact, not a mathlib-only lemma.

## Session arc update (2026-07-25) — keystone sorry-free modulo one *localized* input

The concrete-`Φ_b` divisor/boundedness inputs mapped above were then discharged in a
sequence of verified (`lean`-direct exit 0, sorry-free) bricks:

| brick | file | PR |
|---|---|---|
| input 1: `MeromorphicOn phiBProd` ⇐ product analyticity | `QBeta/PhiBProdMeromorphic.lean` | #4223 |
| input 1 infra: factor/partial-product entire | `QBeta/PhiBProdFactorAnalytic.lean` | #4272 |
| input 1 infra: local-uniform limit of entire is entire | `QBeta/LocalUniformLimitEntire.lean` | #4278 |
| **input 1 CLOSED**: partial products converge locally uniformly ⇒ `phiBProd` meromorphic **unconditionally on `Im b² > 0`** | `QBeta/PhiBProdProductConvergence.lean` | (this) |
| input 2: `meromorphicOrderAt phiBProd ≠ ⊤` ⇐ products locally nonzero | `QBeta/PhiBProdOrderNeTop.lean` | #4225 |
| input 3a: inversion kills the **even** elliptic freedom (`℘`) | `QBeta/InversionKillsEvenElliptic.lean` | #4227 |
| input 3b: σ-unitarity (self-duality) kills the **bar-even reciprocal-odd** residual | (same file) | #4227 |
| assembly: concrete-`Φ_b` `uniqueUpToScalar` via the boundedness capstone | `QBeta/PhiBProdUniquenessAssembly.lean` | #4232 |
| `hbdd` localization: doubly-periodic global boundedness ⇐ compact-domain bound | `QBeta/DoublyPeriodicBoundedLocalization.lean` | (this) |

**Input 1 fully closed (2026-07-25, this brick).** `PhiBProdProductConvergence.lean`
supplies the local-uniform convergence of the `numFactor`/`denFactor` partial products
(Mathlib's `Summable.hasProdUniformlyOn_one_add` per-compact + geometric bound
`e^{M_K}(e^{Re c})^k`, glued by `hasProdLocallyUniformlyOn_of_forall_compact`). Feeding
`LocalUniformLimitEntire`, both `tprod`s are entire, so
`phiBProd_meromorphicOn`/`phiBProd_meromorphicOn_substrate` establish
`MeromorphicOn (phiBProd b) univ` with **no remaining analytic hypothesis** on the branch
`Im b² > 0`. Input 1 (`MeromorphicOn phiBProd`) is therefore no longer a carried hypothesis —
it is a theorem on the physical branch. The only remaining open input to the full keystone is
the **growth/boundedness** endowment `hbdd` below (equivalently the same-divisor premise).

**Net state.** The Faddeev–Volkov uniqueness leg for the physical `Φ_b` is sorry-free
modulo the single analytic endowment `hbdd` (strip boundedness of the ratio), and that
input is now **localized**: `bounded_of_doublyPeriodic_of_bounded_on_ball` reduces the
*global* `hbdd` to boundedness on **one compact fundamental parallelepiped**. The remaining
obligation is therefore "the elliptic ratio is pole-free (bounded) on one fundamental
domain" — equivalently the `Φ_b` divisor-rigidity fact — which needs the Écalle–Borel /
state-integral growth estimate or the infinite-product-analyticity infrastructure Mathlib
does not yet package. That is the honest floor; nothing downstream of it remains open.

**Elliptic-freedom ledger (what excludes the `e·Φ` factor, by route).**
- even `e` (`℘`): excluded **algebraically** by the inversion relation (input 3a).
- bar-even reciprocal-odd `e`: excluded **algebraically** by σ-unitarity (input 3b).
- non-σ-fixed reciprocal-odd `e`: excluded **analytically** — a nonconstant elliptic has
  poles in the fundamental domain, so it fails the (localized) boundedness — via the
  boundedness capstone + this localization.
