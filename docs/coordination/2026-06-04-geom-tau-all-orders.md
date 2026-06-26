# Geom bridge: τ at all orders (open research direction)

**Status**: open. Not gated on any active branch; documented as a
research direction for whoever picks it up next.

## What's settled (recap)

The algebraic → geometric → boundary chain (per
[`rem:geom-bridge-status`](../../content/quantum-observable-universe/mass-theory/geom-bridge-status.md)):

| Link | Statement | Status |
|---|---|---|
| 1 | `tr(h²-curvature) = dim(V)·χ(Σ₄) = -12` | **PROVED** (`prop:crossed-module-euler-characteristic`, Lean `native_decide` over Gaussian integers) |
| 2 | `2G/3 = Vol(B₃)/(dim(V)·|χ|) = 8G/12` | **PROVED** (arithmetic) |
| 3 | `Vol(B₃) = 8G` | **PROVED** (Adams 1985, 8 ideal octahedra) |
| 4 | `-12 / (-64) = 3/16 = κ` (the −64 normalisation as **structural**) | **DISPROVED** (PR #1819 follow-up `phi0_normalization_disproof.py`: at h⁴, α₄/κ₄ = +7.92 ≠ -64) |
| 5 | `τ` carries algebraic −12 to geometric −8G categorically | **CONJECTURAL** (the genuine open link) |

## The sharpened open question

`conj:tau-all-orders-bridge` (added with this doc): does the fibre
functor τ relate the algebraic and Markov-trace h-expansions at all
orders, and if so, as what kind of map?

The h⁴ disproof of −64 rules out **τ as a constant**. Two
categorically-meaningful possibilities remain:

1. **τ is an order-mixing linear map** — a lower-triangular real
   matrix `T_{k,j}` with `κ_{2k} = Σ_{j ≤ k} T_{k,j} · α_{2j}`. The
   h⁴ disagreement is then absorbed into the off-diagonal entries.
2. **τ does not exist at all orders** — the algebraic and
   Markov-trace sides measure genuinely different categorical
   invariants of the Borromean braid that share only h²
   (the categorical Euler characteristic on both sides via the
   trivial-strand expansion).

The conjecture proper is the **dichotomy** of (1) vs (2), since
both are categorically plausible.

## Empirical test — RUN (2026-06-04), refines the conjecture

The h⁶,h⁸ extension was implemented in
`computations/probes/tau_all_orders_h6_empirical.py`
(witness `tau-all-orders-empirical-bridge.witness.json`). It does NOT
resolve the dichotomy — instead it sharpens it and corrects the
"discriminating at h⁶" expectation above:

| order | α (Q₈ alg) | κ (Markov) | α/κ |
|---|---|---|---|
| h² | −12 | 3/16 | −64 |
| h⁴ | −6 | −0.7578… | +7.92 |
| h⁶ | **0** | −0.2024… | 0 |
| h⁸ | **0** | 0.00967… | — |

Two findings:

1. **α is degree-4 in h** (α₆ = α₈ = 0, despite 6 crossings — the
   order-6 full product is traceless). The algebraic side carries
   nonzero data at only TWO orders (−12, −6); the Markov κ-series is
   infinite. A 2-vs-∞ structural asymmetry — concrete evidence the
   two sides are different invariants.
2. **The number-level fit is non-discriminating.** At fixed q₀ both
   sequences are q-independent constants; a non-diagonal
   lower-triangular T trivially solves the under-determined system
   (row k: κ_{2k} = T_{k,1}·α₂ + T_{k,2}·α₄, 1 eq / 2 unknowns). So
   hypothesis (1) is trivially inhabited at the number level — the
   naive fit cannot discriminate (1) vs (2). (Contrary to the
   pre-run "discriminating at h⁶" expectation: there is no q-degree
   leverage because α is q-independent.)

**Refinement (the real next step).** The dichotomy is only non-trivial
if `TauOrderMixingMap` additionally requires T to be **natural** —
independent of the truncation K and arising from the single fibre
functor τ — not an ad-hoc per-truncation solve. Adding that
naturality / bounded-q-degree constraint to the Lean class is the
genuine open formalisation task; without it `tau_all_orders_bridge`
collapses to excluded middle. This is recorded in the conjecture's
`.md` "Empirical test" section.

## What does *not* settle this

Per AGENTS.md "Before declaring 'open' math/questions/gaps", the
corpus was searched:

- `grep -rln "tau.*all.orders" docs/audits/` → empty
- `grep -rln "tau.*all.orders\|order.mixing.*tau" content/` → empty
- `grep -rln "tau_order_mixing\|alg_h.*kappa.*all_orders" computations/` → empty
- Coordination ledgers: no prior closure of this specific question.

The four greps returning empty modulo this branch confirm the
sharpened conjecture is a genuine new statement. The proved Links
1-3 above and the disproved Link 4 do not settle it.

## Why this is *not* a CAL-4 / numerology trap

The dichotomy is intentionally **not a fitted constant**. The
DISCIPLINE check from `production-vs-exploratory-discipline.md`:

- It does not claim a fixed numerical scale (the h²-only −1/64 is
  proved from the −12 + 3/16 identities, both independently derived).
- It does not pin a new observable to substrate q₀ via a free
  parameter (no new CAL inputs; T_{k,j} are derived, not pinned).
- It explicitly states an empirical falsification test (the K ≥ 4
  fit residuals) before claiming hypothesis (1).
- It includes hypothesis (2) — "no map exists" — as a genuine
  branch of the dichotomy, with equal categorical weight.

The disproof of −64 (which was itself an attempt to read T_{1,1}
*as a structural constant*) is the precedent this conjecture is
built around: T at all orders cannot be a constant; the question is
whether the non-constant form is meaningful.

## What this doc is *not*

- Not a workplan: nobody is committed to running the h⁶ extension.
- Not a CI gate: no audit assertion depends on this.
- Not a proposition: no claim is provable from the current state.

It is a coordination doc so the next session/agent doesn't redo the
analysis or restate the question as if it were open in a less
sharpened form. If picked up: branch off
`claude/tau-all-orders-h6-empirical-<date>` and start with the
`phi0_normalization_disproof.py` extension.

## Cross-links

- Content block: [`conj:tau-all-orders-bridge`](../../content/quantum-observable-universe/mass-theory/tau-all-orders-bridge.md)
- Lean class skeleton: `content/quantum-observable-universe/mass-theory/tau-all-orders-bridge.lean` (declares `TauOrderMixingMap` + `TauDistinctInvariants` classes, no instances — honest open state)
- Precedent disproof: [`phi0_normalization_disproof.py`](../../computations/hecke/phi0_normalization_disproof.py)
- Anchor proposition: [`prop:crossed-module-euler-characteristic`](../../content/quantum-observable-universe/mass-theory/crossed-module-euler-characteristic.md)
- Upstream conjecture: [`conj:geom-universality`](../../content/quantum-observable-universe/particle-interactions/geom-universality.md)
- Status remark this sharpens: [`rem:geom-bridge-status`](../../content/quantum-observable-universe/mass-theory/geom-bridge-status.md)

## Update 2026-06-26 — the a_D^(n) fork settled + 3-layer recursive structure (lever-1, bean z2bn)

PR #2795 (`sw-lambda-jet-prolongation`) settled the structural fork for the
prolongation period `a_D^(n) = ∮ λ_SW^(n)`: the γ-loop encircles a √-branch of
the color cubic ⇒ `X^(n) ~ (z−z_k)^{1/2−n}`, falling-factorial `(1/2)_n`, so the
**global** `a_D^(n) = lw(n−1)` (#1765) is **super-exponential**; the depth-2 SL₂
trace `τ` is only the **n≤4 effective fit** (it caps at λ₊≈2.18 while the lw
ratio grows 1.9→3.1).

Two PRs this session formalize + confirm that:

- **#2800** (`lever1-keystone-na-stokes-3b`) — Lean. States the keystone
  `a_D^(n)=lw(n−1)` as a §3b class (`ProlongationPeriodMeanQuantumDim`), proves
  the conditional `τ = 3(3[2]²+2)/(4([2]+2))` (`NaStokesKeystone`), and maps the
  3-layer recursive structure: hyperbolic cosh/sinh (`BindingHyperbolicRecurrence`,
  reuses the Reeb growth tower), q-Bessel (`BindingQBesselKernel`, §3b class
  `BindingFollowsQBessel` = z2bn), Rogers–Szegő (`BindingQHermiteOscillator`,
  q-oscillator even/odd parity). na-Stokes bridge made explicit. Also a
  **robustness fix** to `QBesselContiguityRecurrence.lean` (was silently broken
  on main — brittle `mul_div_assoc`; → `div_mul_eq_mul_div`).
- **#2808** (`lever1-qbessel-period-compute`) — compute. Probe
  `sw_period_lw_sl2_qbessel_probe.py` reproduces the #2795 table with the
  **canonical q-hook dim_q** (independent confirmation): SL₂ diverges from lw by
  n=5/6; lw super-exp. Records the Hahn–Exton q-Bessel coefficients honestly
  (scope-(a), no fit): they shrink, so the super-exp growth lives in the
  **period/partial-sum**, not the coefficient — pins where the open z2bn
  correspondence sits.

**Still open** (z2bn): the geometric↔algebraic identification `a_D^(n)=lw(n−1)`
itself (#1765), and the exact q-Bessel⇒period correspondence.

**Sibling scope map + intent posted** (2026-06-26): #2795 (verdict — confirmed
w/ canonical dim_q), #2722 (`tr B=f([2]_q)` — flagged Lean-overlap vs
`tau_in_stokes_eigenvalue_gap`), #2325 (q-Bessel-2nd-kind binding — broadcast the
`QBesselContiguityRecurrence` fix, which affects any q-Bessel consumer), #2807
(q-binomial infra — reuse opportunity for `BindingQHermiteOscillator`, noted not
posted). #2793 is the same author's `[2]_q` τ-assembly (complementary).
