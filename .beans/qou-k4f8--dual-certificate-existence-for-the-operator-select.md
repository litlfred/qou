---
# qou-k4f8
title: 'Dual certificate existence for the operator-selection LP: formalize first, then symbolic'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T12:50:00Z
updated_at: 2026-08-16T13:05:56Z
---

Follows `k4ul` (#5216, theorem proved) and `0tjt` (#5231, box shown
non-binding by the paper's own text). Those establish that
`operator_selection_lp` holds **given** a dual certificate. This bean asks
whether one exists.

## The question, stated exactly

`k4ul`'s hypotheses require `s : Fin d → R` with

```
s ≥ 0        and        ∀ j,  t j = y_0_star + Σᵢ sᵢ · G i j
```

`G` is the Frobenius Gram matrix `Gᵢⱼ = tr_M(bᵢbⱼ)`, hence **symmetric**, so in
vector form the second condition is

```
t = y₀ · 𝟙 + G s ,      s ≥ 0
```

— `d` equations in `d + 1` unknowns `(y₀, s)` with a sign constraint. Existence
is **not** automatic: it asks whether `t` lies in the cone `{y₀𝟙 + Gs : s ≥ 0}`,
`y₀ ∈ ℝ`. That is a genuine Farkas-type question about the substrate data.

## Method: formalize first, then compute

Per AGENTS.md. Do not start from numerics.

1. **Lean, statement.** Define
   `DualCertificateExists (t G) : Prop := ∃ y₀ s, (∀ i, 0 ≤ s i) ∧ ∀ j, t j = y₀ + Σᵢ s i * G i j`
   and prove the two reductions that make it checkable:
   - if `G` is invertible, `s = G⁻¹(t − y₀𝟙)`, so existence reduces to
     `∃ y₀, ∀ i, 0 ≤ (G⁻¹(t − y₀𝟙))ᵢ` — a one-parameter sign condition;
   - the certificate, once exhibited, discharges `k4ul`'s fields directly.
   Both are elementary and need no Farkas — Farkas would only be needed for the
   *converse* (non-existence ⇒ something), which is not wanted here.
2. **Symbolic.** For `n = 2` (`d = 2`) and `n = 3` (`d = 6`), build the NF basis
   of `H_n(q)`, compute `tᵢ = tr_M(bᵢ)` and `Gᵢⱼ = tr_M(bᵢbⱼ)` **symbolically in
   `q`**, not at a pinned `q₀`. Then evaluate the sign condition from step 1.
3. **Instantiate.** If a certificate exists for those `n`, supply it as a
   `OperatorSelectionLpContext` instance — that turns `k4ul` from conditional
   into an unconditional statement about the small cases.

## Why symbolic before numeric

A numeric check at `q₀` cannot distinguish "the certificate exists" from "the
certificate exists at this `q₀`". The proposition is stated for general `q`, and
the sign condition can change across `q`. This corpus has a `q-usage` QA axis
precisely because pinning `q` early hides that.

## Starting points

- `computations/aK_via_lp_dual_hecke_basis.py` + its witness
  `a-K-via-lp-dual-hecke-basis.witness.json` — the closest existing artifact,
  and it is **live**, not deprecated. Read before writing anything new.
- `computations/alpha-k-jones-markov-h3.witness.json`,
  `alpha-k-jones-markov-h4.witness.json` — Markov traces for `H₃`, `H₄`
  already computed. These may already contain `t` for `n = 3, 4`.
- `computations/_deprecated/symbolic-lp.py` — deprecated; check what replaced it
  before reusing.

`pyhecke` is **not importable** in this sandbox as of 2026-08-16, so the Hecke
machinery has to come from the checked-in computations or be rebuilt.

## Stage 1 DONE (2026-08-16) — the Lean is in place, sorry-free

`operator_selection_lp.lean` now carries the whole reduction. Compiled clean
against the pinned mathlib (zero errors, zero warnings, hence no `sorry`).

**The algebra was factored out first.** `sum_cost_mul_eq` is the dual
decomposition `Σⱼ tⱼxⱼ = y₀·n_target + Σᵢ sᵢ(Gx)ᵢ` over *raw data* — no order
on `R`, no sign hypotheses. Everything else is a corollary, including the
optimality bound the main theorem used to inline.

**The two reductions this bean asked for:**

1. `dualCertificateExists_of_left_inverse` — given `K` with
   `Σᵢ K k i · G i j = δₖⱼ`, the dual equation *determines* `s`:
   `s i = Σₖ (t k − y₀)·K k i`. So existence collapses to: **does some single
   scalar `y₀` make all `d` entries non-negative?** A `d`-dimensional
   feasibility question becomes a one-parameter search.

   Deliberately phrased with a *given* left inverse rather than `G⁻¹`: no
   invertibility API, no determinant, no `Matrix` import (`Data/Matrix/Defs`
   is **not** in the olean cache, though `Basic`/`Mul`/`NonsingularInverse`
   are). The symbolic stage supplies `K` explicitly and `hK` is checked by
   multiplication.

2. `OperatorSelectionLpContext.ofCertificate` — builds the class from data
   plus four checkable facts (`s ≥ 0`, the dual equation, the net constraint,
   Frobenius positivity, per-index complementary slackness) and **derives**
   `zero_gap` via `zero_gap_of_complementary_slackness`.

   Deriving it is the point. `zero_gap` is the one field that looks like the
   block's own conclusion, and hand-supplying it is exactly where the
   §3b-cond self-assuming instance would creep back in — the defect `k4ul`
   was filed for. A raw-data lemma is required here: a lemma assuming the
   class could never supply one of its own fields.

**Complementary slackness is the whole content of the gap.**
`zero_gap_iff_complementary_slackness` shows that for feasible `x`, attaining
the dual bound is *equivalent* to `∀i, sᵢ(Gx)ᵢ = 0` — each Frobenius
constraint inactive (`sᵢ = 0`) or tight (`(Gx)ᵢ = 0`). One equation in the
whole data becomes `d` independent scalar equations. That is what makes the
certificate checkable rather than merely stateable.

## Stage 2 DONE (2026-08-16) — and the answer is not the expected one

`computations/operator_selection_lp_symbolic_qq.py`, exact in ℚ(q),
`fractions.Fraction` throughout, **no floating point anywhere**. 18/18 checks.
Stdlib only — deliberately: `numpy`/`mpmath`/`pyhecke` are all unimportable
here, but more to the point, the whole question turns on whether `det G` is
**zero**, not small, and `gram.py` documents at length that f64 cannot see the
difference (`|λ_min| = 3.9e-17` even at 60 dps through its NF path;
`np.linalg.inv` returns entries to 7.6e15 with `‖G·G⁻¹−I‖ = 1.64` and raises
nothing).

### The planned reduction does not apply — `G` is singular

`det G = 0` **identically in ℚ(q)** for `H₃`. Rank 5, nullity 1. So
`dualCertificateExists_of_left_inverse` has no left inverse to be given, and
the "invert `G`, search over `y₀`" plan this bean wrote in stage 1 is not the
right instrument. Independently confirmed what `gram.py` lines 100–155 assert.

The radical is `v = (−q³, q², q², −q, −q, 1) ∼ (−1/q)^len(wᵢ)` — the
q-antisymmetriser, matching `gram.py`'s `RADICAL` up to the scalar `−q³`.

### A certificate exists, trivially, and for a structural reason

`tⱼ = tr_M(bⱼ) = tr_M(b₀·bⱼ) = G₀ⱼ` — **the cost vector is row 0 of the Gram
matrix**, because the basis contains the identity. So `y₀ = 0`, `s = e₀` is a
dual certificate, for every `n`, with no computation. `DualCertificateExists`
is TRUE and the answer to this bean's headline question is "yes, vacuously".

Vacuously because of what it certifies: the bound is `Σⱼtⱼxⱼ ≥ 0` derived
from the constraint `(Gx)₀ ≥ 0`, and `(Gx)₀` **is** `Σⱼtⱼxⱼ`. The objective
is bounded below by one of its own constraints.

### `y₀* = 0` is forced — exactly, not numerically

Pair the dual equation with the radical: `⟨t,v⟩ = y₀⟨𝟙,v⟩ + sᵀGv = y₀⟨𝟙,v⟩`,
and `⟨t,v⟩ = (Gv)₀ = 0`. With `⟨𝟙,v⟩ = −(q−1)(q²−q+1)`, which vanishes only at
`q = 1` (the quadratic has no real root):

> **`y₀ = 0` for every dual-feasible `(y₀, s)`, at every `q ≠ 1`.**

No symmetry of `G`, no `s ≥ 0`, no primal feasibility needed. And for `q > 0`
the certificate is *unique*: `s = e₀ + λv` needs `λq² ≥ 0` and `−λq ≥ 0`, so
`λ = 0`.

The optimum is attained on the radical itself: `x* = c·v` with `c⟨𝟙,v⟩ =
n_target` is feasible with **every** Frobenius constraint tight, and objective
`0`. The LP selects the operator the Markov trace cannot see.

### `H₂` is the contrast

`det G = (q⁴+q²+1)/(q²+1)² ≠ 0`, nullity 0. Nothing forces `y₀`; there is a
one-parameter family. So the degeneracy is a fact about `H₃`, **not** an
artifact of the LP formulation — which is what the `aK_via_lp_dual_full.py`
→ `aK_via_lp_dual_hecke_basis.py` move assumed when it went to the full basis
to escape "degenerate duals (y_0^* = 0 for A ≥ 2)".

## Stage 3 DONE — the Lean instantiation is abstract, not hardcoded

Rather than embed a 6×6 ℚ(q) matrix in Lean, the three facts the computation
verifies are exactly the hypotheses of two new theorems:

- `dualCertificateExists_of_cost_eq_gram_row` (`ht`)
- `y_0_eq_zero_of_radical` (`ht`, `hv`, `hone`) — holds over any commutative
  ring without zero divisors; the `omit` on the order instances is deliberate
- `OperatorSelectionLpContext.ofRadical` (`ht`, `hv`, `hc`) — builds a full
  context whose `x*` is the scaled radical

Each check in the script names the Lean hypothesis it discharges, so the two
sides can be audited against each other.

## The content finding

The dual objective is `n_target · y₀`. With `y₀ = 0` forced, **the LP's
optimal value is 0 for every `n_target`** — so `y₀*` cannot be the shadow
price of the net constraint; it cannot respond to the constraint it prices.

`aK_via_lp_dual_hecke_basis.py` already guards `abs(u0) > 1e-12` and records
`a_K^chi_active` as undefined when it trips. **That guard is firing on a
structural identity, not on noise**, and `a_K^{dual_ratio} = y₀*_atom /
y₀*_free` is `0/0` symbolically. Needs a separate bean and an owner decision —
it questions `prop:mass-coefficient-shadow-price`, not just this block.

## Still open

- [x] Register the findings as a proper `*.witness.json` — **done 2026-08-22**,
      see below.
- [x] File the shadow-price finding against
      `prop:mass-coefficient-shadow-price` — done 2026-08-22 as a `caveat`
      authorNote, corrected for the wrong-LP error (`8na1`).

Farkas (`qou/kl8z`) was never needed here, and now demonstrably so: the
certificate is exhibited by hand.

## Blocker recheck 2026-08-21

Witness registration is still blocked, and not by choice: `numpy`, `mpmath`,
`sympy` and `scipy` are all unimportable in this container, so `WitnessBuilder`
(via `qou_substrate.precision` → `mpmath`) cannot run and `pyhecke` cannot
import either. The `.results.json` files remain deliberately outside the witness
namespace rather than hand-forged. Needs one run in an environment with the
numeric stack; the computation itself is exact and stdlib-only, so nothing about
the result depends on that environment.

## Correction 2026-08-22 — `pyhecke` IS importable, and the Gram is confirmed numerically

Two lines in this bean are wrong and have been carried forward since.

**"`pyhecke` is not importable in this sandbox as of 2026-08-16"** — it is. It
lives at `tools/pyhecke/python/pyhecke` and needs its siblings on the path:

```sh
PYTHONPATH=tools/pyhecke/python:tools/qou-substrate/python:computations/substrate:computations
```

The same shape of error as the numpy/mpmath blocker recorded further up: a
missing path read as a missing capability.

**"Register the findings as a proper `*.witness.json` (needs an environment
with `mpmath`)"** — `numpy`, `mpmath`, `sympy` and `scipy` all install from
PyPI here. Both blockers on this bean are stale.

With those, the ℚ(q) result is confirmed numerically at the substrate `q₀`:

```
NF_NAMES     ['γ', 'σ₀', 'σ₁', 'L₊', 'L₋', 'e⁻']
max|G - Gᵀ|  0.0
eigenvalues  [-0.75270211, 0.0, 0.75270211, 0.75270211, 0.75270211, 4.23033923]
rank 5   det 4.0e-17   min|eig| 1.85e-16
t == G row 0   True, max diff 0.0
```

Rank 5, one exact zero eigenvalue, and the cost vector is row 0 of the Gram
**to the last bit** — the two facts this bean established symbolically, now
from the other direction.

Worth noting which of the two does the work downstream. `dualCertificateExists_of_cost_eq_gram_row`
needs only `t = G e₀`, and that alone produces `y₀ = 0`, `y = e₀` and optimal
value `0`. The radical is what upgrades "attained" to "forced". Twelve of the
fourteen committed LP/SDP witnesses carrying a `y0_star` show the `e₀`
certificate — including `frobenius-repose`, whose Gram is **invertible**
(`gram_rank 6`). So the identity, not the radical, is the widespread mechanism.
See `qou/augu`.


## 2026-08-22 — witness registered, and the block now cites it

`computations/operator-selection-lp-symbolic-qq.witness.json`, 18/18
assertions, `allPassed: true`. The `.results.json` is deleted; nothing read it
but this script.

**`q0Anchor: "independent"`.** `resolve_q0_anchor` cannot infer that from a
manifest — a producer has to declare it — and it is the substantive claim of
stage 2: the computation never reads `q_0`, so a result at a pinned `q_0`
cannot be mistaken for it. Everything is exact in ℚ(q).

**Zero raw float64 values in the emitted JSON**, checked. Each of the 18
assertions carries the Lean hypothesis it discharges in its `lean` field, so
`operator_selection_lp.lean` and the witness audit against each other — which
is what this script was written for.

The arithmetic stays stdlib-only. Only the *reporting* imports
`WitnessBuilder`, which is a JSON writer and touches no number computed here;
the `fractions.Fraction` path is unchanged, so `== 0` is still a decision
rather than a threshold.

**`prop:operator-selection-lp` now carries a `computation` field** pointing at
script and witness (`status: "verified"`), plus a `status` authorNote stating
the finding and routing the content consequence to `8na1` for an owner ruling.
The block had no `computation` field at all before; a witness nothing points at
is only half-registered.

**Not flagged by `lp_dual_witness_validator.py`, correctly.** That validator
requires the six LP-dual fields only of witnesses whose sibling script imports
an actual solver (`linprog`, `cvxpy`, `lp_dual_solver`); its own comment
excludes "SYMBOLIC certificate witnesses", which is exactly what this is. It
does surface a pre-existing failure — `binding-sdp-bondgraph-degenerate.witness.json`
missing all six — recorded in `qou/augu`, since a sweep keyed on `y0_star`
cannot see a witness that omits it.

### Both blockers on this bean were false

Recorded 2026-08-16 as "`pyhecke` is not importable" and "needs an environment
with `mpmath`", rechecked and reaffirmed on 2026-08-21. Neither was true:
`numpy`, `mpmath`, `sympy` and `scipy` install from PyPI, and `pyhecke` imports
given `PYTHONPATH=tools/pyhecke/python:tools/qou-substrate/python:computations/substrate:computations`.
Six days on a missing path read as a missing capability, and the same pattern
turned up a third time the same day in `lp_dual_witness_validator.py`, which
dies on import without that path. Worth generalising: **before recording a
capability as absent, check whether it is merely unrouted.**
