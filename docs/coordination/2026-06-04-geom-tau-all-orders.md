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

## Empirical test (next experiment)

The dichotomy becomes discriminating at order h⁶ once one imposes
the categorical constraint that each `T_{k,j}` has bounded
q-polynomial degree (otherwise the system is under-determined for
all finite K).

Concrete next step (estimated 1-2 hours of compute):

1. Extend `phi0_normalization_disproof.py` to extract `α_6, α_8` via
   `itertools.combinations` over the 6 Q₈ crossings (already
   parameterised by `order` in `alg_trace_h_coeff`).
2. Extend `markov_h_coeff` to k = 6, 8 via `mp.diff` of `trM_borromean`.
3. Attempt a 2×2, 3×3, 4×4 lower-triangular fit for `T` and check
   whether the fitted entries are:
   - q-rational of bounded degree (evidence for hypothesis 1), or
   - dimensionally erratic / fitted-only (evidence for hypothesis 2).

Output: a new witness `tau-all-orders-empirical-bridge.witness.json`
recording the fit residuals across K = 1..4.

## What does *not* settle this

Per CLAUDE.md "Before declaring 'open' math/questions/gaps", the
corpus was searched:

- `grep -rln "tau.*all.orders" docs/audits/` → empty
- `grep -rln "tau.*all.orders\|order.mixing.*tau" content/` → empty
- `grep -rln "tau_order_mixing\|alg_h.*kappa.*all_orders" folio-assistant/computations/` → empty
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
- Precedent disproof: [`phi0_normalization_disproof.py`](../../folio-assistant/computations/hecke/phi0_normalization_disproof.py)
- Anchor proposition: [`prop:crossed-module-euler-characteristic`](../../content/quantum-observable-universe/mass-theory/crossed-module-euler-characteristic.md)
- Upstream conjecture: [`conj:geom-universality`](../../content/quantum-observable-universe/particle-interactions/geom-universality.md)
- Status remark this sharpens: [`rem:geom-bridge-status`](../../content/quantum-observable-universe/mass-theory/geom-bridge-status.md)
