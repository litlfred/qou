# The cumulant→MeV map is a cluster expansion — linear (pair) + log (many-body)

**Date:** 2026-07-19 · **Branch:** `claude/cumulant-mev-map-normalization-2026-07-19`
(PR #4101, bean `qou-4uk9`) · **Axis:** Δ_λ binding magnitude — the cumulant→MeV map ·
**Tier:** structural reconciliation (scope-(a); no fit; nothing wired). Resolves the
load-bearing gap surfaced by merged #4093.

## 0. The gap (from #4093)

The b₄ pole-regulator wall (#4093) named its load-bearing gap as *"no established
cumulant→MeV map"*: the deuteron reeb-flow law `B(²H) = 5·g` is **linear** in the
magnitude `g`, while the He4-local cumulant `b_A = −ln det(I+g·S)` is **logarithmic**
(`5g/b₂ = 10.03`). The #4093 required-`Vol` back-out silently assumed a log map, which
the deuteron's linear law appeared to refute.

## 1. The resolution — different cluster ORDERS, not rival maps

The apparent inconsistency is a **category error**. The corpus already documents
(`2026-07-06-reeb-flow-…-provenance` §3) that `B=5g` is *"**NOT** the A=2 case of the
`b₄=−ln det(I+G)` form"*, and that the deuteron law's real shape is the pair-order

  `B(²H) = √5·E_unit·(1 − x/10 + 3x²/200 − ⋯)`,  `x = (v−v⁻¹)²`,

dimensionless core Lean-proved sorry-free, with `E_unit ≈ 0.9959 MeV` the one open
dimensional anchor. So the linear and log forms are **different orders of one cluster
(Mayer/cumulant) expansion** of the binding, carried in the same MeV unit:

  `B(K) = E_unit · [ Σ_pairs (linear pair term) + Σ_{k≥3} b_k (connected k-body cumulants) ]`.

- **Pair order** is **linear** in `g` — the deuteron (one pn bond) is `√5·E_unit·g·ladder`.
- **Many-body orders** are the connected cumulants `b_k = −ln det`-type; `b₄` is the
  He4-local 4-body piece of #4084 (log, near-critical at ⁴He).
- The leading term of `−ln det₂` is `g²` (**quadratic**) — a *different power* of `g`
  than the pair-order `5g` (**linear**). That different power is the machine-level
  signature that they are different orders, not a normalization mismatch.

## 2. Verifications (`cumulant_mev_cluster_expansion_probe.py`, 3/3)

| # | check | result |
|---|---|---|
| V1 | deuteron pair-order `√5·E_unit·ladder` | `2.2245668` MeV = AME `2.224566` (6 digits); the ladder fixes the +0.41% bare `5g=2.2336` carries |
| V2 | pair `5g` (linear) vs cumulant `−ln det₂ ~ g²` (quadratic) | different orders, ratio `10.03` — the #4093 category error |
| V3 | ⁴He cluster structure | 6 pair terms (`13.35` MeV) + connected many-body (`b₃+b₄ ≈ 14.95` MeV) = AME `28.30`; `ρ₄ obs 12.7 > 6` baseline, with `b₄` the #4084 near-pole enhancement |

## 3. Consequence + what stays open

- **Resolves** the #4093 normalization gap: "linear vs log" is cluster-**order**
  structure, one `E_unit` anchor across orders. The #4093 required-`Vol` diagnostic was
  ill-posed because it treated a pair term (`b₂`) and a 4-body cumulant (`b₄`) as the
  same map; corrected, ⁴He binding = 6 pair terms + the near-pole `b₄`.
- **Reframes Item 2** (`qou-6kgu`, the moduli `Vol`): the `b₄` term is a *many-body
  correction* in `E_unit` units, not the whole binding — so the moduli `Vol`/regulator
  is downstream of `E_unit` and of the pair-order sum, not a standalone determinant of
  `B(⁴He)`. (#4093 already walled the standalone-`Vol` back-out; this explains *why* it
  was the wrong object.)
- **Still open** (unchanged): `E_unit` itself — the dimensional anchor, which the
  provenance audit §2e records must come from a *structural* argument, not a scan
  (entropy bound) — and the `b₄` magnitude (#4084). This note fixes the **framework** the
  two live in; it does not derive either.

## 4. `E_unit` — attempted; it is a documented wall (exchange sector is scale-free)

The cluster expansion isolates `E_unit` as *the* remaining dimensional open. Attempting it
(bean `qou-6kgu`/`qou-4uk9` follow-up) resolves to the corpus's already-exhaustive record
(`2026-07-06-reeb-flow-…` §2f–§2i), **not** a new number — and a numerical search is
**forbidden** by the §2e entropy bound (a ~0.4% two-factor match carries no evidence). The
documented state:

- **The exchange sector is scale-free (§2h.2, Lean-motivated).** The amplitude `g` and the
  ceiling `√5` are dimensionless Hecke-operator data; `m_e` enters only downstream via the
  `τ`-functor. So `B = √5·E_unit` *requires* an **external** `E_unit`, and no internal QOU
  scale supplies `0.99594 MeV` to the law's precision — nearest is `2m_e` at **+2.6%**
  (6× the law's own +0.41% residual); `m_e[2]_v` +2.8%, `E_0/[2]_v²` +4.8%, `Q_β` −21%.
- **Single-factor `m_e × (bond q-integer)` is exhausted-negative** (§3d).
- **The counit-defect functional** supplies the sign but its magnitude explodes with `A`
  (scope-(a) negative *as normalized*; an `A`-flattened variant is not excluded).
- **Additive open+loop decomposition fails** (§2i, −36% to −64%): binding is collective.

**Cluster-expansion sharpening (the one thing this branch adds to the `E_unit` picture).**
Item 1 shows `E_unit` is the **single universal per-bond quantum shared across *all* cluster
orders** (the pair-linear term *and* the many-body cumulants carry the same `E_unit`). That
*explains* §2h.2 structurally: a quantity common to every order of the exchange-algebra
expansion cannot originate *inside* the (dimensionless, scale-free) exchange algebra — it
must be the one external `τ`-archimedean scale. So the two open routes narrow to: **(i)** an
external `~1 MeV` `τ`-sector scale the framework does not yet canonically contain, or
**(ii)** the `A`-flattened counit variant (§2f). This branch does **not** close either —
`E_unit` remains open, and per the anti-laundering rule no axiom/class carrying it counts as
a derivation.

Refs: probe `computations/deltalambda/cumulant_mev_cluster_expansion_probe.py`;
#4093 `docs/audits/2026-07-19-b4-collective-coordinate-regulator-wall.md`;
provenance `docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md`
§2e/§3; #4084 `B4CumulantBarEven.lean`.
