# The T4 anchor round-trip: `A_ω = 3` has no internal support, and ϑ_K is not independently determined

**Date:** 2026-08-01 · **Axis:** ϑ_K gap (`qou-qnnq`) / T4–T5 channel · **Tier:** scope correction.
**Nothing retracted numerically — every number below is correct. What is corrected is what those numbers *establish*.**

New audit axis introduced alongside this note:
[`folio/pipeline/circular-anchor-audit.ts`](../../folio/pipeline/circular-anchor-audit.ts)
(mechanical) + [`circular-anchor-review-ledger.json`](../audits/circular-anchor-review-ledger.json)
(agentic).

## The round-trip

[`qbeta_t4_stokes3_crux_probe.py`](../../computations/qbeta/qbeta_t4_stokes3_crux_probe.py) fixes the constant and inverts the channel:

```python
A_omega = 3
coeff = A_omega * kappa
theta2_muon   = ln2_q0 - S_muon   / coeff
theta2_proton = ln2_q0 - S_proton / coeff
```

`ϑ` is therefore **defined** by `A = 3` together with the measured `S`. Recovering
`A` from `(ϑ, S)` inverts exactly that and returns 3 by construction. The
"both anchors give A ≈ 3.00, 0.6 % apart" reading — which this session cited twice
before catching it — is **rounding in the 8-digit ϑ values**, not independent
agreement between two anchors.

The circularity closes across probes:
[`qbeta_t3_multiknot_binding_probe.py`](../../computations/qbeta/qbeta_t3_multiknot_binding_probe.py)
takes those ϑ (annotated `# T4-inverted`) and **recomputes** `S`:

```python
theta_muon_T4 = 0.05894648  # T4-inverted
S_muon_T4 = A_omega_41 * kappa_41 * (ln_q0**2 - theta_muon_T4**2)
```

`S → ϑ → S`. Any agreement reported there is definitional.

## Both reported checks are weaker than they read

T4's verdict is *"both anchors yield real ϑ_K, with correct boost/spin dominance"*.
Formalizing the channel ([`ThetaRealityBound.lean`](../../folio/quantum-observable-universe/lean/QOU/QBeta/ThetaRealityBound.lean),
sorry-free) shows what each check is worth:

| reported check | what it actually is |
|---|---|
| **diagonal crossed** (`ϑ_μ < ln q₀ < ϑ_p`) | **an identity.** `S > 0 ⇒ ϑ² < ln²q₀` and `S < 0 ⇒ ϑ² > ln²q₀` hold for **every** `A, κ > 0` (`diagonal_crossed`). It is equivalent to the measured sign flip of `S` and is independent of `A`. It supports **no** value of `A`. In the probe it is additionally a hardcoded `"diagonal_crossed": True`. |
| **both ϑ real** | **a one-sided lower bound.** `ϑ² ≥ 0 ⟺ A ≥ S/(κ·ln²q₀)` (`thetaSq_nonneg_iff`), binding only at the `S > 0` anchor; the `S < 0` anchor is real for any positive `A` (`thetaSq_pos_of_neg`). Numerically `A ≥ 2.054`, monotone upward (`thetaSq_nonneg_mono`). |

`"S_sign_correct": True` is likewise a hardcoded literal, not a computed comparison.

## Consequence: one degree of freedom, not two

The channel `S_K = A_ω·κ·(ln²q₀ − ϑ_K²)` gives **two equations** (two anchors) in
**three unknowns** (`A_ω`, `ϑ_μ`, `ϑ_p`) when `A_ω` is shared. The system is
**underdetermined by one**. Fixing `A_ω = 3` from the literature makes it solvable —
but nothing internal pins it, and the only internal constraint is the one-sided
`A ≥ 2.054`.

So **`A_ω` and `ϑ_K` are not two independent gaps — they are one degree of freedom.**
Fixing either determines the other. This is why successive rounds of Stokes
refinement (`qou-awpk`, `qou-3bp8`) produced real infrastructure without moving
`qou-qnnq`: the blocker was never precision.

**What `A_ω = 3` still rests on:** GGM's literature value (the classical q→0
Stokes datum), plus — for 4₁ specifically — the exact q-series identity
`S₁₂ + S₂₁ = 3·S₁₁` certified in #4447. That identity is real; what it is *not* is
a determination of the physical channel coefficient, and its q-independence is
rank-2-specific (see [`2026-08-01-aomega-three-test-illposed.md`](2026-08-01-aomega-three-test-illposed.md) Addendum 2).

**What this does NOT say.** It does not say `A_ω = 3` is wrong — the literature
value is unaffected, and the reality bound admits it. It says the T4/T5 chain
provides no *independent* evidence for it, and that ϑ_K values derived through it
are `A`-conditioned and must be labelled as such wherever reused.

## Actionable consequences

1. **ϑ values from T4 are conditioned.** Any downstream use (including the qou-3bp8
   W2 sheet evaluations, which inherit them) must carry "conditional on `A_ω = 3`".
2. **The arc needs an independent leg.** The highest-value routes are the ones that
   determine `ϑ_K` *without* `A_ω`: `qou-offl` (cone-manifold / generalized Dehn
   filling) and `qou-rdmr` (Rademacher braid-word → winding). Two independent ϑ
   determinations that agreed would be the first genuine constraint in this arc.
3. **The pattern is now audited.** See below.

## The new audit axis (mechanical + agentic)

`circular-anchor-audit.ts` is the candidate-finder; an agent adjudicates into a
committed ledger keyed by file sha, so a verdict goes stale the moment the file
changes — the same shape as `lean-vacuity-axiom-audit.ts`.

| criterion | fires on |
|---|---|
| `circ-vacuous-check` | a results-dict key shaped like a check (`*_correct`, `*_ok`, `*_crossed`, …) bound to a **literal** `True`/`False`. The check cannot fail. |
| `circ-anchor-inverted-roundtrip` | a module-level constant inverted to define a derived quantity, with confirmation language reported about either. |
| `circ-derived-used-as-input` | a hardcoded literal annotated as derived (`# T4-inverted`, `back-solved`, …) consumed as an input without the conditioning carried. |

First sweep over `computations/` (3032 files): **18 candidates** — 6 adjudicated
`genuine` (the four T4 entries, the two T3 entries), 1 `legit` (a false positive on
a loop bound in this session's own awpk probe), 11 awaiting agent review.

Two calibration notes recorded from building it: an initial `key = True` detector
produced **314** false positives on the ordinary accumulator idiom
(`ok = True` … `if bad: ok = False`) and was narrowed to dict-literal keys only; and
a `\s*(?!True)` lookahead backtracked to zero width and silently exempted the very
case that motivated the axis — caught only by asserting T4 must appear in the output.

## Cross-references

- Beans: `qou-qnnq` (the gap), `qou-offl` / `qou-rdmr` (independent-ϑ routes).
- [`2026-08-01-3bp8-entirety-and-channel-correctness.md`](../audits/2026-08-01-3bp8-entirety-and-channel-correctness.md)
  (the channel gap; §3's discriminator table).
- AGENTS.md §"Axiomatization is NOT a Proof"; §anti-fit; §"Before declaring refuted".
