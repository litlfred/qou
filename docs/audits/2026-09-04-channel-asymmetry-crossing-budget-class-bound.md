# The channel asymmetry is capped by the crossing budget — and the budget is s² = 9, forced

**Date:** 2026-09-04 · **Bean:** `qou-brng`, arc `bk-crossing-mass-binding`
**Type:** class bound. **scope-(b) conditional** on two cited facts (H1, H2),
neither derived here. No fit, no search, no selection, no production change.
**Does not close the binding gap.**

## VERDICT (one line)

**The two-nucleon channel asymmetry achievable by any single block-exchange
braid carrier is capped at `R ≤ 9`, because the inter-nucleon crossing budget is
`c = s² = 9` forced by the 3-strands-per-nucleon layout — against nature's
`33.7055`. The ceiling of 9 previously reported for `Δ₃,₃` is therefore not a
property of that operator: it is `s²`.**

## What was already closed, and what was not

Four routes to the asymmetry had closed, each excluding **one object**:

| route | result |
|---|---|
| `isospin_channel_R_is_one_everywhere_probe` | a single crossing gives `R = 1` exactly, every rep, every dimension (minimal polynomial: `spec(ρ(σ)) ⊆ {q, −1/q}`) |
| `block_transposition_lift_probe` | the 9-crossing `Δ₃,₃` gives a discrete asymmetry set with **ceiling 9** |
| `markov_trace_family_rank_probe` / `ocneanuFamily_finrank_le` | the Ocneanu/Markov family has rank `n`; trace subtraction cannot isolate a block |
| `two_nucleon_linking_matrix_channel_blind_probe` | the linking class is `I₃`-valued, hence channel-blind (scope-(b)) |

None of them bounds the **class**. `block_transposition_lift_probe` is explicit
about its own scope — *"over all 11 blocks of `H₆`, for **this** operator, the
ceiling is 9"* — and the arc's stated residue was *"an invariant of the
six-strand two-nucleon link that is sensitive to the exchange"*, i.e. keep
looking for another object. This note asks the class question instead: **what is
the largest asymmetry any braid carrier on the physical strand layout can
produce?**

## The two cited facts

- **(H1) Quantisation with a crossing cap.** In the seminormal reps of `H_n(q)`,
  every eigenvalue of a braid word `w` has `log|λ| = k·log q` with `k ∈ ℤ` and
  `|k| ≤ c(w)`, the crossing count — and the extremes are **attained**.
  Measured in `block_transposition_lift_probe` (`k` integral to `1.8e-22` at
  90 dps; its line 148: *"a 9-crossing word must give `k = +9` and `k = −9`.
  Both hit exactly."*). The cap direction is elementary — each generator
  contributes one factor of modulus `q^{±1}`.
- **(H2) The strand layout is forced.** Each nucleon carries exactly `s = 3`
  strands — `QOU.Mass.StrandLayoutForcesChain` / bean `qou-gwr9` (*"The chain
  bond set is FORCED by the 3-strands-per-nucleon layout, not chosen"*).

## The argument (three lines)

A two-nucleon channel operator is an exchange of the two nucleon blocks. With
`s` strands per nucleon, exchanging the blocks crosses each strand of one past
each strand of the other exactly once:

```
c_inter = s · s = 9          (s = 3 by H2 — and this IS Δ₃,₃)
```

By H1 the two channel log-moduli are `k_T·log q` with `|k_T| ≤ c_inter`, and a
non-degenerate channel has `|k| ≥ 1` (a `k = 0` eigenvalue has `|λ| = 1`, giving
`B = 0`). Hence

```
R = |k₀ / k₁|  ≤  c_inter / 1  =  9
```

Nature needs `R = 2.224566 / 0.066 = 33.7055`, which is **3.745× over budget**.
Inverting: reaching it needs `c ≥ 34` inter-nucleon crossings, i.e.
`s ≥ ⌈√34⌉ = 6` strands per nucleon — contradicting the forced `s = 3`.

Probe: [`channel_asymmetry_crossing_budget_bound_probe.py`](../../computations/probes/channel_asymmetry_crossing_budget_bound_probe.py)
(4/4 assertions; integer arithmetic for the budget).

## Why this is more than a restatement

It **explains** the ceiling rather than recording it. Before this note, "9" was
a measured property of one operator and it was reasonable to hope a different
six-strand operator would do better. It cannot: 9 is `s²`, and `s` is forced. The
four point-exclusions above become corollaries of a single budget — the single
crossing (`c = 1 ⇒ R ≤ 1`, matching the exact `R = 1`) and `Δ₃,₃`
(`c = 9 ⇒ R ≤ 9`, matching the measured ceiling) are the two endpoints of the
same bound.

## Scope — what this does NOT exclude

- **Repeated exchanges.** `Δ^m` has `c = 9m` and would lift the cap. The
  physical carrier is the *minimal* braid representing the two-nucleon link
  (owner ruling 2026-08-29, canonical braid closure), so `m = 1`; if a
  derivation ever justifies `m ≥ 4`, this bound does not apply to it. Stated as
  a limitation, not waved away.
- **Non-braid carriers.** Any channel object that is not a braid word in the
  nucleon strands is untouched by H1 — that remains the arc's honest residue.
- **The binding gap.** Not closed, and nothing here licenses a fit.

## Consequence for the arc

The asymmetry is not merely *unexplained* by the braid channel objects tried so
far — on the forced layout it is **out of reach of the whole single-exchange
braid class by a factor of 3.7**. A closure must therefore come from outside
that class (a non-braid carrier, or a derivation that justifies a larger
crossing budget), not from a better choice of braid invariant. That redirects
the search rather than merely narrowing it.

## Cross-references

- [`2026-09-03-two-mubars-selector-vs-magnitude.md`](2026-09-03-two-mubars-selector-vs-magnitude.md) — the residue this addresses.
- [`block_transposition_lift_probe.py`](../../computations/probes/block_transposition_lift_probe.py) — H1, ceiling 9, `k` integrality.
- [`isospin_channel_R_is_one_everywhere_probe.py`](../../computations/probes/isospin_channel_R_is_one_everywhere_probe.py) — `R = 1` for a single crossing.
- [`two_nucleon_linking_matrix_channel_blind_probe.py`](../../computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py) — the linking class.
- [`StrandLayoutForcesChain.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/StrandLayoutForcesChain.lean) — H2.
