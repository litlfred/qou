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
