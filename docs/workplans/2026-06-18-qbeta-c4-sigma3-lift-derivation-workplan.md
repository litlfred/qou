# Q_β c₄ Stage-C — derive the σ₃-lift Λ from the brane-tower map (workplan)

**Date:** 2026-06-18
**Branch:** `claude/qbeta-c4-stage-c-sigma3-lift-2026-06-18`
**Goal:** 1ppQ — Q_β; the `c₄` rung. Continues the merged #2465 (bridge + C13
+ H₄ preflight) and #2106 (Stage B). Owner directive: "start Stage-C σ₃-lift."

---

## 0. The open object (from #2465, now on main)

The merged preflight ([Stage-C scope](../scope/2026-06-18-qbeta-c4-h4-tower-stage-c-scope.md))
established, validated at 50 dps:

- H₄ Hoefsmit seminormal reps + the H₃⊂H₄ branching map are correct;
- **σ₃-gating**: a σ₃-free element carries no new H₄ DOF, so `c₄` is gated on a
  **length-4, σ₃-involving** element `Λ ∈ H₄(q)` lifting the decay operator
  `ΔT ∈ H₃(q)`.

The open question (the keystone of this branch):

> **Which `Λ` is the categorically-correct σ₃-lift of `ΔT`, such that its
> level-4 Markov-trace component yields `c₄`?**

## 1. STRICT discipline — derive, never fit

The refuted-class map + flip-flop guard forbid the obvious trap: enumerating
σ₃-extensions of `ΔT` until one's `c₄` matches the target. **That is fitting and
will be caught.** `Λ` must be **derived** from categorical content:

- **Source of `Λ`:** the brane-tower N→N+1 map (`prop:mass-endomorphism-tower`,
  generator `V̂_i`, the physical tower variable `z = |V̂_i|`). The decay
  operator's lift under adding one strand/cell is what specifies the σ₃ entry —
  not a free choice.
- **Anchor-stability gate (registry §8):** any `c₄` produced must pass
  proton+muon swing < 1%, else `empirical`, dead on arrival.
- **Bar-evenness + q=1 shadow** (refuted-class map §1 invariants) must hold.
- **Reduce to the #2465-validated H₄ machinery** (seminormal + branching).
- **Tiered reporting** (proved / near-match / fitted); no production wiring,
  no registry tier change unless a genuine, anchor-stable closure (→ owner
  escalation, not self-wire).

## 2. Coordinate — the Φ_q line is the same object

Commit `e451d436` (merged) wired the **Φ_q / z-Habiro** bridge and flagged the
identical split my #2465 synthesis hit: its N=0→Φ_q correction (9.36% at the
*representative* scale `z=ℏ_q²`) is **not** the production brane-tower `z`, and
*"pinning the production z and wiring it into the mass table is the next step."*
That production `z` is the **same `|V̂_i|`** the σ₃-lift must use. So Stage-C and
the Φ_q line share the open `z`; coordinate, do not duplicate.

## 3. Work plan (one principled step at a time)

1. **Identify the categorical specifier of `Λ`** — read
   `prop:mass-endomorphism-tower` + the N→N+1 map + the Φ_q `z` (research in
   flight). Output: the *derivation rule* for how σ₃ enters, with no free
   parameter. **If no rule exists, that is the finding** — `Λ` is genuinely
   underdetermined and Stage-C is blocked on new categorical content (report
   honestly, do not invent a rule).
2. **Construct the canonical lift candidate `Λ`** from that rule (if it exists).
3. **Compute its level-4 Markov-trace `c₄`** via the #2465 machinery; check the
   §1 invariants (anchor-stability first — kill early if it swings).
4. **Tier-report.** Closure (anchor-stable, derived) → owner. Near-match →
   refuted-class row. Underdetermined → state precisely what is missing.

## 4. Honest forecast

Closure odds this session are **modest** — this is the open keystone after ~12
refuted classes, and `Λ` may prove underdetermined by current categorical
content (in which case the honest deliverable is *that*, sharply stated, not a
fitted `Λ`). The value is a principled attempt that either closes `c₄` or pins
exactly what categorical input is missing.
