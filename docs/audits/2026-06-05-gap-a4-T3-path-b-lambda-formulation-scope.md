# GAP-A-4 Task T3 — Path-B-specific λ(K) formulation (scope)

**Date:** 2026-06-05
**Audit type:** research-grade scope; no probe in this PR
**Status:** **scope only** — names what "Path-B-specific λ(K)" means
precisely and identifies the cheapest formalize-first probe direction.
**Owners:** PR chain — T1 ([#1886](https://github.com/litlfred/qou/pull/1886) merged),
T2 ([#1891](https://github.com/litlfred/qou/pull/1891) merged); both closed
NEGATIVE and pointed at T3 as the productive remaining direction.
**Cross-axis hub:** [`2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md)
(PR [#1871](https://github.com/litlfred/qou/pull/1871)) — the additive
many-body binding axis. T3 is its **per-atom mass-multiplier sibling**.

---

## §1. What "Path-B-specific" means after T1 + T2

The 1ppQ roadmap's Path B formula

```
m(K) = m_e · Vol(K) / ℏ_q² · λ(K) + S(K)
```

asks how `λ(K)` — the per-atom mass multiplier — is determined. This
session's chain closed three structural derivation routes for `λ(K)`:

| Route | Refutation | PR |
|---|---|---|
| **R1** Phase-4 carrier transplant — `λ(K) = f(A_Phase-4(K))` for any rational form | L1a/b/c REFUTED across light series | [#1874](https://github.com/litlfred/qou/pull/1874) |
| **R2** Vol(K) convention choice — `λ(K)` becomes near-constant under the "right" Vol | T2 REFUTED for all 3 conventions (best swing +132 %) | [#1891](https://github.com/litlfred/qou/pull/1891) |
| **R3** Additive `S(K)` sub-leading under uniform-λ — `S(K)` factors cleanly while `λ = 2.53` is held fixed | T1 REFUTED (100× swing) | [#1886](https://github.com/litlfred/qou/pull/1886) |

What R1-R3 share: each treats `λ(K)` as a **transplant** of a quantity
that lives at a different layer of the framework (Phase-4 lives on the
binding-energy amplitude; Vol(K) lives on the per-knot hyperbolic
geometry; uniform-λ lives on the global Wedderburn count). None of
these layers can derive a per-atom mass multiplier directly because
**they were never derived to be per-atom mass multipliers**.

**"Path-B-specific"** means: derive `λ(K)` from a structural object
that is **native to the Path B mass equation itself** — not transplanted
from elsewhere.

## §2. The native objects of Path B

Path B's `m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` is the mass-side
identity of the same q-difference family that appears in #1871's
binding closure. Its native objects are:

| Object | Role | Where it lives |
|---|---|---|
| **The per-atom braid β_K** in `H_{3·A}` | the algebraic representation of K | `mass_at_3A_proper.atom_braid_word_3A` |
| **The atomic Markov trace `tr_M(β_K, q₀)`** | scalar invariant of β_K | `canonical_tr_m_via_chi_cache.py` (chi-cache witnesses) |
| **The per-atom hyperbolic volume `Vol_hyp(β_K)`** | the SnapPy JSJ value of β_K's closure (= Phase-4's Vol) | `2026-05-19-delta-lambda-phase4-z4N-closure.md` §"Phase 3" |
| **The Path-B-native q-difference kernel** | `λ(K) = G(q₀; β_K) / Z_norm(q₀)` where G is determined by a q-difference recursion on K's atomic braid | **NOT YET CONSTRUCTED** (this is what T3 needs to define) |

The first three already exist. The fourth — a Path-B-native q-difference
kernel on the per-atom mass multiplier — is what's missing.

## §3. The structural pivot

Following [#1871's §4.A P4](https://github.com/litlfred/qou/blob/main/docs/workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md)
load-bearing identification — *"the per-order terms and the open scale
rule `ρ·A` are determined by a q-difference equation on the binding
generating function"* — apply the same machinery to the **mass**
generating function. Define

```
M(x; q) = Σ_K m(K) · x^A(K)
```

(formal power series in `x` over atoms K with mass weight, summed by
atomic number A). Per the Habiro / Garoufalidis–Zagier framework
already adapted to QOU in [`habiro-pochhammer-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/habiro-pochhammer-bridge.md),
`M(x; q)` is a candidate for satisfying a fibre-level q-difference
equation

```
M(qx; q) = R_mass(q, x) · M(x; q)
```

with `R_mass(q, x)` derived from the bar-symmetric q-Pochhammer
structure of the atomic braid words. **Conjecture (T3 core)**:

> `λ(K)` is the coefficient of `x^A(K)` in the q-difference solution
> of `R_mass(q, x)`, divided by the per-atom geometric factor
> `m_e · Vol(K) / ℏ_q²`.

This is the **Path-B-native** formulation: `λ(K)` becomes an output of
a q-difference recursion on `R_mass`, not a transplant of any other
layer's quantity.

## §4. Cheap formalize-first probe (NOT in this PR)

Before writing T3's probe, the formalize-first discipline (PR #1826)
requires identifying a **structural invariant** that pre-narrows the
search. Two candidates:

**Invariant I1 — bar-symmetry of `R_mass`.** Any Habiro-derived kernel
on the atomic braid words is **bar-symmetric** (`q ↔ q⁻¹` invariant)
when the braid word itself is bar-symmetric. The per-atom braids in
`atom_braid_word_3A` are bar-symmetric by construction (every `σ_i`
intra-nucleon crossing is paired with its inverse via the
flavor-averaged interface convention). Therefore `R_mass` must satisfy
`R_mass(q, x) = R_mass(q⁻¹, x)`. Predicts: any `λ(K)` solution must
have a definite parity in `h = (q − q⁻¹) / q^{1/2}`.

**Invariant I2 — proton-row exact match.** The proton row is the
calibration anchor: `m(p) = m_p_codata` by definition under CAL-1
(`m_e`). So at K=p, T3's formulation must produce
`λ(p) = m_p / (m_e · Vol(p) / ℏ_q²) = 2.4600...` (T2 verified; `Vol(p)` is the proton's per-atom volume, which under every convention tested in T2 evaluates to `Vol(𝓑₃) = 8·G`).
Predicts: any `R_mass` candidate must have a proton root at exactly
that value; any candidate that doesn't is REFUTED before any
numerical probe runs.

**Cheap probe (T3 follow-up; not this PR):**

1. Compute `m(K) / m(p)` ratios across the light series — these are the
   target ratios `R_mass` must reproduce on the proton-normalised
   coordinates.
2. Compute the bar-symmetric q-Pochhammer products of each `β_K`
   directly (no fitting), exploit I1 to restrict the candidate space.
3. Test whether ANY closed-form Path-B-native q-Pochhammer combination
   reproduces all six target ratios to a substrate-derivable precision
   (≤ 5 % first, then ≤ 1 %).
4. If none works, the conclusion is structural: **Path B's `λ(K)` is
   not a Habiro-bar-symmetric q-Pochhammer combination** — the
   formulation needs deeper categorical input (e.g. an explicit
   `τ`-image identification with a Dirac/SW PDE, per #1871's P4).

## §5. What T3 does NOT do

- **Does not propose a 7th fit ansatz.** Per AGENTS.md, no per-partition
  closure. The candidate space (Habiro-bar-symmetric q-Pochhammer
  combinations) is closed by I1 + I2 before any probe runs.
- **Does not touch production.** All work is exploratory.
- **Does not duplicate #1871's binding workplan.** #1871's q-difference
  kernel is on `B(K)`; T3's is on `m(K)`. Different generating functions,
  same machinery. Both ledgers' tasks T3 (mine) and §4.A P4 / L3
  (theirs) point at the same q-difference theory but from opposite
  sides of the additive identity `m(K) = m_e·Vol(K)/ℏ_q²·λ(K) + S(K)`.

## §6. Coordination

- **PR #1871 step-9 binding closure** — sibling axis. T3 ↔ §4.A P4 / L3.
- **PR #1762 1ppQ roadmap** — parent. T3 closes the remaining open box
  on the per-atom mass multiplier side; both Option A and Option D
  axes route through it.
- **GAP-A ledger** (`gap-a-path-b-lambda.md`) — T3 is the final open task;
  T1 + T2 closed in this session.

## §7. Honest expected outcome

The structural difficulty: bar-symmetric q-Pochhammer combinations form
a finite-dimensional space at any fixed order. Per I1 + I2, that space
is further restricted. **If the restricted space is empty** (no
combination reproduces all 6 target ratios), the conclusion is that
`λ(K)` requires deeper categorical input than the Habiro-Pochhammer
layer can supply — specifically, the **`τ`-image identification with a
Dirac/SW PDE** that #1871's workplan §4.A names as L3's load-bearing
claim. That would close T3 in the same direction #1871's binding
workplan points.

**If the space is non-empty**, the closure is *jointly* derivable
across both ledgers: my T3 supplies the mass-side q-difference solution;
#1871's L3 supplies the binding-side. The Path B identity then becomes
an algebraic identity between two derived q-Pochhammer combinations,
not an open conjecture.

Either way, T3's *scope* (this doc) defines the question precisely;
the follow-up *probe* in a separate PR resolves the verdict.

## §8. Cross-references

- [`gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) — GAP-A ledger; T3 entry
- [`2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md) — sibling-axis ledger (#1871)
- [`2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md) — #1871's binding workplan; §4.A P4 / L3 is T3's mirror
- [`2026-06-04-gap-a4-L1-retrospective.md`](./2026-06-04-gap-a4-L1-retrospective.md) — PR #1876 retrospective that first named the "Path-B-specific" requirement (O2)
- [`habiro-pochhammer-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/habiro-pochhammer-bridge.md) — the Habiro-Pochhammer infrastructure T3's probe would use
- T1 [#1886](https://github.com/litlfred/qou/pull/1886) — additive S(K) REFUTED
- T2 [#1891](https://github.com/litlfred/qou/pull/1891) — per-knot Vol(K) REFUTED
