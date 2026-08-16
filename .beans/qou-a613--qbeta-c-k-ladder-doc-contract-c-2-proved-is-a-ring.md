---
# qou-a613
title: 'qbeta c_k ladder doc contract: c_2 ''PROVED'' is a ring tautology, ladder terminates at k=3, N=4/5 cites a rung removed in #1416'
status: todo
type: task
created_at: 2026-08-16T16:47:05Z
updated_at: 2026-08-16T16:47:05Z
---

Verification of a sibling's defect report on PR #5124 (comment 5308056155,
`AGENTS.md:1062`). Both reported counts CONFIRMED; a third defect found while
checking them. **No file was edited** — see "Why unclaimed" below.

## F1 — "`c_2 = -1` is PROVED Taylor-exact": the Lean is a `ring` tautology

`content/quantum-observable-universe/mass-theory/q-beta-c-2-eq-neg-one-structural.lean`
contains three theorems, each `by ring`, over an arbitrary `CommRing R` with
arbitrary `b hbar : R`:

```lean
theorem c_2_eq_neg_one_structural {R} [CommRing R] (b hbar : R) :
    (1:R) - b^2 * hbar^4 = 1 - (b * hbar^2)^2 := by ring
```

This is the substitution `u := b·ℏ_q²` written on both sides. It holds for every
`b` and every `hbar` in every commutative ring, so it carries no information
about Q_β specifically.

The load-bearing claim — that the operator-valued N=2 correction to Q_β **is**
the factor `(1 − b²·ℏ_q⁴)` (the Kashiwara `f̃₁²` geometric-tail identification) —
appears only as docstring prose citing PRs #1602/#1769/#1786. It is not a
theorem in this file. So "PROVED" attaches to the trivial half of the argument:
*given* the factor, reading off the `u²` coefficient is `ring`; *establishing*
the factor is the open part.

Not necessarily wrong to call `c_2 = -1` established — but "Lean-PROVED
Taylor-exact" overstates what the Lean file contains, and it is the one rung
`qbeta_ck_cache.py` labels `tier: "derived"` and wires to the L2 dashboard
headline.

## F2 — the ladder does not converge, it closes: exactly one rung after c_2

`computations/qbeta/qbeta_ck_cache.py` extracts `c_k` by residual inversion:

```python
ck_extracted = ratio_m1 / u ** k                 # ratio_m1 = Q_codata/Q_prev − 1
Q_next       = Q_prev * (1 + ck_extracted * u ** k)
```

Substituting: `Q_next = Q_prev · (Q_codata/Q_prev) = Q_codata`, **identically**.
So after the k=3 pass the residual is exactly zero, and the loop's guard

```python
EPS_RESIDUAL = mpf("1e-30")
if abs(ratio_m1) < EPS_RESIDUAL: break   # prints "ladder converged"
```

fires at k=4 **for any inputs whatsoever**. It reads as a convergence test; it is
a tautology. Consequences, all checked:

- `structural_candidates` for k = 4,5,6,7 (the `c_3·b⁴`, `−(b²+½)`, `4·b²`, `−8`
  forms) is unreachable dead code.
- The producer prints `Q_N7 = …` while `Q_prev` is `Q_N3`.
- `qbeta-ck-cache.witness.json` confirms it: `rows` holds k=2 and k=3 only,
  `discipline/cal_anchored_tier_count = 1`, `Q_beta_tiers/cal_anchored/
  err_ppb_vs_codata = 0.0` (zero because it was *defined* to be zero).

Replicated standalone (arithmetic only, no producer run, no witness written):
residual at k=4 is `0.0`, `break`, one rung extracted. The conclusion is
input-independent — it follows from the algebra, not from the constants.

So the `AGENTS.md:1062` framing "**convergent series**; `N` is the truncation
order chosen by target precision (`N ≥ log₁₀(1/ε)/2.07 − 1`)" does not describe
this producer. There is no free `N`: there is c_2, then one calibrated rung that
absorbs the entire remaining residual by construction.

## F3 — NEW: "N=4 → N=5 non-monotonicity" cites a rung removed in #1416

`AGENTS.md:1062` offers "the N=4 → N=5 non-monotonicity as the experimental
signature", and `appendix-mass-binding-algorithms/mba-sidecar-ck-truncation-ladder.md`
carries the same text in its `k ≥ 4` tier row. But `docs/precision-goals.md`
says the N=5 ladder was a **fit, removed in #1416**, and marks the claims that
rested on it:

> **Superseded (do not restore).** Prior text claimed "Q_β N=5 categorical meets
> Subgoal-1 (5.7 ppb)" … Both relied on the CODATA-fitted N=5 Q_β ladder removed
> in #1416.

Two canonical docs therefore disagree: one cites N=4/N=5 as live evidence, the
other says do not restore it.

Compounding this, the sidecar's own contract is unsatisfied. It names
`computations/q_beta_predicted.py` as "Canonical compute … which records each
`c_k` with its tier in the witness JSON", and states "**Witness contract:** …
**Must** record each `c_k` alongside its tier". Checked directly:
`q_beta_predicted.py` has no `c_k` logic at all (it computes the base
`Q_β = m_e·|q₀²−2q₀−1|·(q₀+1)/(2q₀³)`), and `q-beta-predicted.witness.json`
contains no `c_2`, no `c_3`, no `c_k`, and no `tier` key. The actual c_k producer
is `qbeta_ck_cache.py`, which the sidecar never names.

This matters more than an ordinary stale pointer because the sidecar sits under
the STRICT Mass-and-Binding-Algorithms appendix-sync banner — the maintenance
contract whose entire job is keeping propositions ↔ Python API in sync. The
contract has drifted from its own compute.

## Why unclaimed / nothing edited

The sibling flagged rather than edited, for owner sign-off, because this is a
STRICT banner on a channel with a documented six-entry flip-flop history
(`docs/coordination/1ppq-qbeta.md`). That restraint is right and applies equally
here, so no file was touched. All three findings are **evidence for an owner
call**, not repairs an agent should make unilaterally.

Deliberately left `todo` rather than claimed: the verification is finished and
the remaining step is owner-gated, so marking it `in-progress` would block a
sibling from picking it up without anything actually being in flight.

Note the interaction with `qou-cds1` (re-derive the ladder under convention D,
ACTIVE with a sibling — do not claim): F2 means the D re-derivation cannot be a
z-swap *or* a re-truncation, because there is no truncation to re-do. The C-frame
`c_3 = -2.0693` in the cache is a single calibrated residual absorber, and its D-
frame replacement will be too, unless the N=2 factor itself is re-derived.

Related: `qou-7hfy` (bare auto-generated stub for the
`qbeta_ck_truncation_canonical_conjecture` Lean open conjecture) — adjacent, not
the same thing; this bean is about the documentation contract.
