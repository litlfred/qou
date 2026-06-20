# Δ_λ exponent `10A−5`: jet-grade / GB-normal-form reframe (formalize-first)

**Status:** formalize-first **HYPOTHESIS** (not derived, not wired). Item 1 of
[PR #2483](https://github.com/litlfred/qou/pull/2483). Companion to the scope doc
[`docs/scope/2026-06-18-qbeta-habiro-pde-binding-jet-exponent-scope.md`](../scope/2026-06-18-qbeta-habiro-pde-binding-jet-exponent-scope.md).

## Context

The binding Δ_λ residual is `Δ_λ(K) ≈ q₀^(10A−5) = q₀^(5(2A−1))`
([2026-06-14 second-kind audit](2026-06-14-qlommel-delta-lambda-second-kind-derived-b.md)).
The crossing-count derivation
([`delta_lambda_exponent_from_crossings.py`](../../computations/delta_lambda_exponent_from_crossings.py))
establishes the **slope** (`σ+σ⁻¹ = 10A−2`, with the Z,N dependence cancelling —
DERIVED, verified D,T,³He,⁴He) but **asserts** the two structural constants: the
per-site `5` (= Bring quintic) and the per-nucleon `9` (= intra-𝓑₃). The
per-site-`q₀⁵` mechanism is the open keystone
([2026-06-15 start](2026-06-15-delta-lambda-q5-per-site-mechanism-start.md)).

**Finding (PR #2483, item 1).** The current derivation is a **raw braid-word
crossing count** — it does **not** use the GB normal form (Step 7), the jet-prefix
order (Step 8), or the confinement SDP (Step 10). Confinement enters only the
binding *magnitude* / operator selection, never the exponent.

## Hypothesis (formalize-first targets)

**H1 (per-site = jet grade).** In the jet-prefix filtration (Step 8) each
**chain-site** of the atom word — a nucleon or an inter-nucleon bond — contributes
exactly jet-grade `5` to the Δ_λ q₀-exponent, so
`exponent = 5 · #sites = 5·(A + (A−1)) = 5(2A−1) = 10A−5`,
with **no `−3` offset** (the `−3` was an artifact of counting crossings, `10A−2`,
rather than sites). The `5` is the degree of the Bring quintic (genus-4 Bring
surface, Aut = S₅) — the same `5,7` family as the categorical Weinberg ratio
`cosh(5η₀)/cosh(7η₀)`.

**H2 (per-nucleon = GB-normal-form crossings).** The Gröbner–Shirshov normal
form of a single nucleon's 𝓑₃ braid carries exactly `9` non-bar-symmetric
crossings, so the per-nucleon increment of `σ+σ⁻¹` is `9` (intra) `+ 1`
(interface) `= 10` — a **GB-NF** count, not a raw-word count.

## Why this is the right cut

If H1/H2 hold, the exponent stops being a numerology of raw crossing counts and
becomes a **graded statement**: per-site jet grade (Step 8) × site count, with the
per-nucleon `9` fixed by the GB normal form (Step 7). That converts "why 5? why
9?" from asserted integers into **filtration invariants** — the formalize-first
prune the q-Lommel second-kind audit flagged as the remaining open piece.

## Decisive tests (no fit — each confirms or refutes)

1. **H2 is directly decidable now (cheap compute, next step):** GB-reduce a single
   nucleon 𝓑₃ word (`_PROTON_G0/_G1`, `_NEUTRON_G0/_G1` in
   [`hecke_core.py`](../../computations/hecke_core.py)) via the Laurent engine and
   count the non-bar-symmetric crossings in the normal form. `= 9` confirms; `≠ 9`
   refutes H2 (and the raw-count `9` is then a coincidence of the un-reduced word).
2. **H1 needs the jet-prefix grading (Step 8)** applied per site; a Lean lemma over
   the jet filtration stating `jetGrade(site) = 5` is the target. Gated on the
   brane-tower per-site jet machinery (shares the H≥6 typed-braid bottleneck — the
   PR #2483 unifying finding).

## Tier

HYPOTHESIS. H2 is a cheap decidable compute (immediate next step); H1 is a Lean
formalize-first target gated on the jet/tower machinery. Neither is wired; no fit
is introduced. Per the Δ_λ gate this is a structural prune, **not** a seventh
closure ansatz.
