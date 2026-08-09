---
# dsm1
title: 'GAP: docstring-claims-a-sorry queue — DRAINED (13 → 1, and that 1 is a known FP)'
status: completed
type: task
priority: high
tags:
    - lean
    - vacuity
    - proof-integrity
created_at: 2026-08-08T21:00:00Z
updated_at: 2026-08-08T21:00:00Z
---

Queue produced by the new `proof-docstring-sorry-mismatch` detector
(`content/pipeline/lean-vacuity-axiom-audit.ts`), added the same day. Each entry
is a **candidate**; the legit-vs-genuine call is an agent's, per the ledger.

## Why the detector exists

`detectSelfAssuming` gates on the projected **field name** (`CONCLUSION_FIELD`:
`claim_`, `_holds`, `_eq`, …). A class field named outside that convention is
invisible to it however plainly it posits the conclusion. Two live cases found by
hand on 2026-08-08 were missed for exactly that reason, both named `*_ident`:
`confinement_categorical` (`exact ctx.confinement_ident`) and
`nucleon_ordering_factorization` (`exact ctx.factorization_ident`). Both are now
fixed; the detector fires on both pre-fix versions, which is how it was validated.

The new criterion reads only the doc block and the body, so no naming choice can
dodge it.

## The queue — 9 on `main` @ 2026-08-09 (was 13 when first run)

| file (under `content/quantum-observable-universe/lean/`) | declaration |
|---|---|
| `QOU/AlgebraicSubstrate/JointGaloisBraidFigure8.lean:134` | `kappa_commutes_bar` |
| `QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean:90` | `kappa_vanishes_iff_chi` |
| `QOU/BraidKnot/OVTopAssembly.lean:203` | `identityB_general` |
| `QOU/BraidsKnots/mobius_frobenius_kernel.lean:78` | `mobius_frobenius_kernel` |
| `QOU/BraidsKnots/nsi_q_deformed_kernel.lean:159` | `nsi_q_kernel_identification` |
| `QOU/BraidsKnots/skein_mass_from_linking.lean:93` | `skein_mass_from_linking` |
| `QOU/Interactions/ConfinementSDP.lean:141` | `ConfinementSDP` |
| `QOU/Molecular/shell_filling_rule.lean:145` | `shell_filling_rule` |
| `QOU/ParticleInteractions/mass_categorical_descent.lean:75` | `mass_categorical_descent` |

**Four dropped between the first run and the rebase** — `volume_perturbation`,
`markov_identification`, `four_term_pair_nucleon`, `neutron_proton_splitting` —
fixed on `main` by other sessions in the intervening ~78 commits.

`volume_perturbation` was one of the three I had confirmed by reading, and it was
resolved independently. That is corroboration of the verdict, not a false
positive retracted.

**This list is a snapshot and will go stale the same way.** Re-run the detector
rather than working from this table:

```
bun run content/pipeline/lean-vacuity-axiom-audit.ts content/quantum-observable-universe/lean
```

## Three were spot-checked; all three were true positives

Two of them assert the **precise opposite** of their own code:

- **`volume_perturbation`** — *"Stated with `sorry` + citation per AGENTS.md §1a
  disposition 2 — **no conclusion field on the class hands this back**."* The body
  is `exact ctx.volume_perturbation_claim`, and the class field is commented
  `(conclusion)`.
- **`shell_filling_rule`** — *"the unproved ones carry honest `sorry`s in their
  named sub-theorems …, **not projected conclusion fields**."* Both named
  sub-theorems are `exact ctx.inner_shells_fill` and `exact ctx.hund_rule`, and
  neither carries a `sorry`.
- **`kappa_vanishes_iff_chi`** — *"inherits that lemma's single honest `sorry`."*
  `qou_obstruction_reduction.lean` contains **no `sorry` in code at all**; the
  cited `obstruction_trace_gap` is `exact ⟨ctx.kappa0_eq_chi_A,
  ctx.phi_1_image_eq_chi_A⟩`.

The remaining entries are **unread**. Do not assume they follow the same pattern.

## This one touches live work

`collatz_contact_boundary` derives `obstruction_removable_of_even_chi` through
`kappa_vanishes_iff_chi`, so its own docstring's *"derived from the universal
obstruction-reduction … no independent assumption"* bottoms out in an assumed
class field rather than a proof. The §7c base-ring port of that file (same PR) is
unaffected — it was about the coefficient ring — but the **derivation** claim
should be re-scoped when this bean is worked.

## Do NOT soften the regex

The obvious refinement — skip when the doc delegates the `sorry` to a sub-theorem
or an inherited lemma ("in their named sub-theorems", "inherits … `sorry`") —
would have suppressed **two of the three confirmed true positives**. Delegation is
precisely where the claim goes unchecked. Keep it high-recall; keep the call with
the agent.

## Honest disposition per item (AGENTS.md §1a)

1. **Prove it** — discharge the goal.
2. **Queue it** — delete the conclusion-bearing class field and restore a real
   `sorry` + `-- Ref:`, so the docstring becomes true. This is what was done for
   `confinement_categorical` and `nucleon_ordering_factorization`.
3. **Fix the prose** — if the projection is a legitimate §3b-cond composition,
   the docstring is simply wrong and should stop claiming a `sorry`.

Whichever is chosen, the outcome is that the prose and `#print axioms` agree.

---

## DRAINED 2026-08-09 — 13 → 1

**Eight fixed** by the honest disposition (delete the conclusion-bearing class
field, restore a real `sorry` + `-- Ref:`, so prose and `#print axioms` agree):

| declaration | field deleted |
|---|---|
| `kappa_commutes_bar` | `kappa_commutes_bar_field` |
| `mobius_frobenius_kernel` | `classical_limit` |
| `nsi_q_kernel_identification` | `kernel_ident` (its doc said "conclusion") |
| `skein_mass_from_linking` | `skein_mass_ident` |
| `mass_categorical_descent` | `descent_ident` |
| `obstruction_trace_gap` | `kappa0_eq_chi_A`, `phi_1_image_eq_chi_A` |
| `shell_filling_inner_shells` / `_hund_rule` / `_lp_strong_duality` | `inner_shells_fill`, `hund_rule`, `lp_strong_duality` |
| `ConfinementSDP` | `HasConfinementSDPData.strong_duality` |

Four more were fixed on `main` by other sessions while this ran
(`volume_perturbation` — via an explicit `Revert "prove volume_perturbation via
context enrichment"` — plus `markov_identification`, `four_term_pair_nucleon`,
`neutron_proton_splitting`).

## The detector was refined by what the drain taught, not by taste

The first version deliberately did **not** exempt delegated `sorry`s, because
five declarations delegated in exactly that language while the delegated-to
declaration had no `sorry` either.

After the drain, the three survivors were all cases where the delegation had
become **true**. So the exemption is now gated on *evidence*, not wording:
`DOC_DELEGATES_SORRY` (wording) **and** `fileHasSorryCode` (a real `sorry`
somewhere in the file, read from comment-free bodies). Wording alone never
exempts.

Regression-tested: the two founding cases (`confinement_categorical`,
`nucleon_ordering_factorization`) still fire **CRITICAL** against their pre-fix
sources. Recall on the defect class is unchanged.

## Known residual false positive — `identityB_general`

`OVTopAssembly.lean:203` still reports CRITICAL. Its docstring truthfully places
the `sorry`s in "the bricks", which are in **other files**, and the exemption's
evidence check is file-local. Fixing it properly means resolving the delegation
target across the import cone — a real improvement, not attempted here, because
a cross-file `sorry` search is a different (and much more expensive) query than
the one this detector is built on.

**Do not silence it by widening the wording rule.** That is the mistake the
drain already disproved.

## Also found, not mine, not fixed

`QOU/SkeinResolutionObstruction.lean:41` does not compile **on `main`** —
`Invalid field 'obstruction_class'`, a field that exists in no version of
`QouObstructionReductionContext`. Confirmed pre-existing by stashing and
rebuilding against clean `main`. Unrelated to this bean; filed here so it is not
lost.

