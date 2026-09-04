# Two `μ̄`s: the sorry-free one is a selector, the magnitude-typed one is trace-unreachable

**Date:** 2026-09-03
**Branch:** `claude/mubar-selector-vs-magnitude-2026-09-03`
**Bean:** `qou-brng`, arc `bk-crossing-mass-binding`
**Status:** scoping correction + a convergence. **No new compute; no new claim.** Every
value cited is already verified in a carrier on `main`.

---

## VERDICT (one line)

**The route "use `μ̄₁₂₃` to close the binding channel asymmetry" — which this arc
proposed after the rank bound closed the trace-subtraction route — is retired as
stated, because it names the wrong `μ̄`. The `μ̄` the SM side has proved sorry-free
is a `{0, ±1}`-valued *selector*, which cannot supply a real ratio of `33.7`; the
`μ̄` that carries a *magnitude* is the Markov-trace deficit coefficient, and
`cyclic_trace_kills_iterCommTower` already proves a cyclic trace cannot reach it.
That second fact is an independent corroboration of this arc's rank bound, reached
from a different direction with no shared machinery.**

---

## How this arose, and the mis-step it corrects

After `ocneanuFamily_finrank_le` (PR #6415) proved the Ocneanu/Markov trace family
spans at most `n` dimensions of a `p(n)`-dimensional space of trace functionals, the
arc recorded a next step in these words:

> chase the non-trace route the rank result leaves open — `μ̄₁₂₃`, the sorry-free
> triple-linking object the SM side already has.

That is a type error, and `SecondCrossingInvariant.lean` warns against it explicitly
in a section headed *"Symbol disambiguation — two `μ̄`s in the corpus (do not
conflate)"*. Reading the carriers before building the probe is what caught it.

## The two objects

| | carrier | type | values |
|---|---|---|---|
| **topological `μ̄₁₂₃`** | `QOU/StandardModel/SecondCrossingInvariant.lean` | integer, bounded | `±1` on the Borromean triple, `0` on a 2-tube meson |
| **`mubarMeasured`** | `QOU/MassTheory/MilnorExactCoefficient.lean` | `ℚ`, unbounded | `(3/4)·(−2)^{A−3}`: `3/4, −3/2, 3, −6, …` |

The second is the **trace-normalised leading coefficient of the A-component Brunnian
Markov-trace deficit `1 − τ_A`**, empirically extracted. Its values at `A = 3..6` are
proved as `example`s in its own file, so they are cited here rather than re-computed.

The carrier's own words: *"Same glyph, different objects and different
normalisations — per AGENTS.md §'Attributes do not transfer across overloaded
symbols', no property of either transfers to the other."*

## Why the type settles the route

The binding channel asymmetry is a **ratio of log-moduli** — a real number, measured
against nature's `2.224566 / 0.066 = 33.7055` (np ¹S₀ virtual state).

`μ̄₁₂₃ ∈ {0, ±1}` cannot supply it. It distinguishes baryon from meson; it does not
carry a magnitude. This is the *same* type failure the arc already hit once: the
`Δ₃,₃` exponents are integers, which is exactly why that ceiling is `9` and cannot be
tuned (`block_transposition_lift_probe`). An invariant valued in `{0, ±1}` is a
harder version of the same wall.

`mubarMeasured` has the right type — `ℚ`, unbounded, growing with `A`. But it is
defined *as* a Markov-trace deficit, which puts it on the wrong side of this arc's
own result.

## The convergence — two independent proofs that the trace cannot reach it

`MilnorExactCoefficient.lean` records:

> `cyclic_trace_kills_iterCommTower` proves a cyclic (Markov) trace annihilates the
> Lie iterated-commutator tower, so the leading coefficient is **not recoverable
> from that tower via a trace**.

Set beside this arc's result:

```
upstream (MassTheory):   a cyclic trace annihilates the iterated-commutator tower
                         => the deficit coefficient is not trace-recoverable
this arc  (SchurWeyl):   the Ocneanu family spans rank <= n of p(n) trace
                         functionals, and only the two 1-dimensional blocks are
                         individually recoverable
```

Two different arguments — one about a commutator tower, one about the polynomial
degree of the Ocneanu weight in `z` — with **no shared machinery**, both concluding
that the Markov trace cannot deliver the object. Neither was derived with the other
in view. That is corroboration of the kind AGENTS.md §"Parallel exploration"
describes as the point of the multi-agent workflow.

## What is retired, and what survives

**Retired:** "`μ̄₁₂₃` carries the binding asymmetry", as this arc stated it. The
sorry-free object is a selector.

**Survives, and is the honest weaker form:** `μ̄₁₂₃` may act as the **coefficient
selecting which** magnitude applies — baryon versus meson — with the magnitude
supplied by something else. That is a real role and it is consistent with its type.
Nothing here tests it.

**Untouched:** the rank bound's scope is unchanged. It excludes the Ocneanu/Markov
trace family parameterised by `N` and nothing else; a genuinely non-trace functional
remains open. What this note removes is the *specific* candidate the arc named, not
the class.

## Follow-up (same day): the selector role does NOT survive for isospin either

The paragraph above kept one thing alive: `μ̄₁₂₃` as *"the coefficient selecting which
magnitude applies"*. Checked against the carrier, that does not survive for the question this
arc is asking.

`SecondCrossingInvariant.lean` types the invariant on **single objects** — `B : S → ℚ`
(lines 100, 119) — and every object it is applied to is a single hadron: the confined triple,
the Borromean rings, the 2-tube meson, the baryon/vacuum pair. It is never evaluated on a
two-nucleon state.

The binding channel asymmetry compares **two two-baryon states**: the `T = 0` (³S₁) and
`T = 1` (¹S₀) channels of the same nucleon pair. `μ̄₁₂₃ = ±1` on every baryon, so it is `±1` on
both nucleons in both channels. **It is channel-blind.** It selects baryon-from-meson; it cannot
select `T = 0` from `T = 1`, because the two channels differ in how the nucleons are *exchanged*
(the `Δ₃,₃` operator of `block_transposition_lift_probe`), not in what each nucleon *is*.

So the weak form is retired too. What would be needed is an invariant of the **six-strand
two-nucleon link** that is sensitive to the exchange — a different object from the per-baryon
`μ̄₁₂₃`, and one this corpus does not currently carry. That is the honest residue.

Scope (a): established from the carrier's definition and its own list of applications. A
bounded corpus grep for any file pairing `μ̄₁₂₃` with an isospin channel was attempted and
**timed out before completing**; it is not cited as evidence either way.

## Follow-up (same day): the residue's *linking-data* half is closed, scope (b)

The section above ends by naming what would be needed: *"an invariant of the
six-strand two-nucleon link that is sensitive to the exchange — a different object
from the per-baryon `μ̄₁₂₃`, and one this corpus does not currently carry."*

A corpus sweep confirmed the object is genuinely absent on all six paths. But the
natural candidate class for it — the **linking data** of the six-component link,
i.e. pairwise linking numbers and the Milnor `μ̄` tower built on them — is dead,
and the reason is one line long once two facts already in the corpus are put
side by side. Probe:
[`computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py`](../../computations/probes/two_nucleon_linking_matrix_channel_blind_probe.py).

**(F1) The inter-nucleon linking number *is* the isospin projection.**
[`inter_nucleon_linked_channel.py`](../../computations/inter_nucleon_linked_channel.py)
derives the inter-nucleon arc as the minimal non-Brunnian 2-component link, the
Hopf link `T(2,2k)` — `pp → lk +1`, `nn → lk −1`, `pn → lk 0` — under a docstring
heading "DERIVATION OF THE BRAID WORD (provenance, NOT a fit)" that states *"NO
numeric is tuned."* `u1_hypercharge_assignment.py:336` names the same datum in
isospin terms: *"I_3 = writhe/2-of-inter-nucleon-arc carries the p/n split."*
Since `lk(T(2,2k)) = k = writhe/2`, those are one statement.

**(F2) Milnor's indeterminacy theorem**, already load-bearing in this corpus as
the scope-(b) exclusion of the Milnor route for ⁴He
([`2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md`](2026-08-29-gap2-he4-milnor-indeterminacy-exclusion.md)):
`μ̄` is well-defined only modulo the gcd of the lower invariants, so one
Hopf-linked pair sends the whole higher tower to `ℤ/1 = 0`.

**Composed.** The `³S₁` (T=0) and `¹S₀` (T=1) np channels have the *same flavour
content* — one proton, one neutron — so `I₃ = 0` in both. By (F1) their linking
matrices are therefore identical, verified entry by entry on all 15 pairs, under
both the corpus's literal single-arc reading and the maximal all-nine-pairs
reading, so the verdict does not rest on that modelling choice. Every function of
the linking data consequently takes **equal values on the two channels**: the
achievable asymmetry is exactly `1`, against the `33.7055` required. This is not a
bound a better choice inside the class might beat — the two inputs are the same
matrix.

**Where the tower is even alive**, as a by-product of (F2): `gcd = 1` on `pp`/`nn`
(indeterminacy `ℤ/1`, no content) and `gcd = 0` on `np` (indeterminacy `ℤ/0 = ℤ`,
genuine invariant). So the Milnor tower survives across the interface *only* on
the np line — where **both** channels sit. Surviving is exactly what does not help.

**Scope.** (b), structural, cited invariant. It excludes invariants that are
functions of the pairwise linking data. It does **not** exclude an invariant
reading the braid word beyond its linking data — the `Δ₃,₃` exchange spectrum is
such an object, and is capped at `9` by the separate integer-exponent argument —
nor a non-Milnor super-pairwise object, nor anything carrying **spin**, which is
what actually separates the channels.

**Convergence, and its limit.** Bean `qou-7zob` records from the flavour side that
*"a flavour-only interface CANNOT split ³S₁ from ¹S₀ … NO map from strand position
to orbital angular momentum anywhere in the corpus"*, and the `t7qv` arc's
`det T = −1` caps the channel-asymmetry ratio at `1`. This gives a *reason* those
ratios are `1` rather than merely small: the objects compared are functions of
`I₃`, and both channels have `I₃ = 0`. That is corroboration rather than a fourth
independent measurement — these routes share the assignment (F1), so they are not
structurally independent the way the two proofs in the section above are.

## What this does NOT claim

* **NOT** that `mubarMeasured` and `μ̄₁₂₃` are unrelated — only that no property
  transfers between them without proof, which is the carrier's own statement. The
  upstream file is explicit that the identification is *open* (*"that is the open
  Milnor μ̄(12…A) content, Route A"*).
* **NOT** a refutation of either object. Both stand as recorded.
* **NOT** a new measurement. Every number here is cited from a verified carrier;
  this note adds a scope correction and an observation, and running a probe to
  re-derive `3/4` would be redundant work.
* **NOT** a claim that the binding gap is closed or closable. It is not.

## References

- `content/quantum-observable-universe/lean/QOU/StandardModel/SecondCrossingInvariant.lean`
  — topological `μ̄₁₂₃`; the disambiguation section; `Y = a·w + b·B` as an open
  primary-conjecture class with no instance.
- `content/quantum-observable-universe/lean/QOU/MassTheory/MilnorExactCoefficient.lean`
  — `mubarMeasured`, its values at `A = 3..6`, and `cyclic_trace_kills_iterCommTower`.
- `content/quantum-observable-universe/lean/QOU/SchurWeyl/OcneanuWeight.lean`
  — `ocneanuFamily_finrank_le` and the degree chain beneath it (PR #6415).
- `computations/probes/block_transposition_lift_probe.py` — the integer-exponent
  ceiling of 9, the first instance of this type wall in the arc.
- `docs/audits/2026-08-02-hypercharge-second-invariant-milnor.md` — the SM-side
  selection of `μ̄₁₂₃` as the second crossing invariant.
