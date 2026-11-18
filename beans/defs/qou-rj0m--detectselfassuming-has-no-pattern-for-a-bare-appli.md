---
# qou-rj0m
title: detectSelfAssuming has no pattern for a bare applied field projection (+27 CRITICAL)
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T21:07:51Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-5vkl
---

Split out of `qou-tmmt` on 2026-09-04. Measured, not proposed.

`detectSelfAssuming` in `content/pipeline/lean-vacuity-axiom-audit.ts` has four
projection patterns. `PROJECTION_BODY` (line 753) and `EXACT_PROJECTION` (756)
both anchor `\s*$` immediately after the field name, so they match
`inst.identity` and reject `inst.identity data`. `APPLIED_TUPLE_PROJECTION`
(773) handles applied projections but only inside a `⟨…⟩` tuple.

So a **bare applied field projection** — `inst.identity data`,
`h.bridge ν β`, `hmT.disjoint_product k n hk α β`, i.e. the commonest way to
consume a §3b-cond conditional class whose field takes arguments — matches no
pattern and is rejected at the pattern gate.

**Blast radius, measured** by adding an experimental pattern and re-running the
producer over all 3578 `.lean` files:

| | candidates | CRITICAL | EXEMPT |
|---|---|---|---|
| baseline | 78 | 41 | 36 |
| + bare applied-projection | 106 | 68 | 37 |

**+28 candidates, 27 CRITICAL.** That is a 66 % rise in the criterion's critical
count, so this is a widening that needs its own PR and its own triage pass — the
file's history is four *narrowings*, and landing 27 new criticals in a commit
that does anything else would be indefensible.

**It does not close `qou-tmmt`.** None of the eight adjudicated item-5
violations is caught by it: five of them move from the pattern gate to the
type-match gate and are rejected there instead, because
`projectionTypeMatchesConclusion` compares characters and a ∀-quantified field
is never character-identical to its own instantiation. See
`docs/audits/2026-09-04-item5-detector-gate-instrumented.md`.

**Next step:** add the pattern, run, and hand-triage all 27 new criticals before
proposing the change — a raw count is not evidence they are defects. Several are
likely the same honest-§3b-placeholder class the existing EXEMPT carve-out
covers, in which case the emission should be EXEMPT rather than CRITICAL and the
headline number falls.


---

## 2026-09-04 — the triage is DONE: 23 genuine, 4 false positives, and a refinement that separates them exactly

The bean above said "hand-triage all 27 new criticals before proposing the
change — a raw count is not evidence they are defects." Done. The experimental
pattern was applied, the producer run, the 27 new CRITICALs diffed against the
baseline, and each one's proof body read. Producer and audit JSON reverted; the
tree is clean.

### 23 genuine item-5 projections

Every one is a context- or instance-object field applied to arguments, and the
field name announces itself:

| body | file |
|---|---|
| `inst.cl_via_stpart_holds q hq` | `ClassicalLimitStpart:65` |
| `ctx.claim_descartes_terminal X` | `archimedean:42` |
| `ctx.claim_metallic_iff a` | `metallic_character_knot:43` |
| `a.claim_noble_iff_curls h_stable` | `noble_gas_characterization:60` |
| `inst.factorisation_holds q b` | `KnotFactorFrobeniusPairing:80` |
| `ctx.claim_universality G' h_add h_norm` | `geom_universality:68` |
| `ctx.claim_reducer_correct β` | `markovTraceRecursiveReducer:58` |
| `ctx.claim_energy_diverges M` | `non_self_intersection:44` |
| `ax.claim_equivariance n h_n_pos x k` | `lagrange_resolvent_transform:72` |
| `ctx.claim_cocycle_deviation n i j k` | `descent_cocycle_deviation:57` |
| `ctx.claim_cech_cocycle n i j k` | `descent_cocycle_deviation:68` |
| `ctx.exists_angleStructure hExp` | `AngleStructureFeasibility:173` |
| `ctx.claim_tr_trans_eq_Phi_q ϱ p` | `quantum_dilogarithm:60` |
| `ctx.claim_dq_squared α` | `dq_squared:51` |
| `ctx.claim_emergence_to_quantum_flat G' h` | `emergence_to_quantum_flat:50` |
| `ctx.claim_frobenius_relation x` | `frobenius_relation:63` |
| `ctx.claim_reeb_rotation Z` | `substrate_radial_coordinate:59` |
| `ctx.claim_rank_eq_two h_simple` | `volume_from_rigidity:51` |
| `lpd.complementary_slackness_holds lam` | `confinement-nf-partial-proof:133` |
| `inst.kvc_holds fourOneBraid` | `kashaev-volume-conjecture:144` |
| `inst.kvc_holds borromeanBraid` | `kashaev-volume-conjecture:154` |
| `hC.shadow_holds a rfl` | `mass-side-kernel-formalize-first-gates:137` |
| `hK.shadow_holds a rfl` | `mass-side-kernel-formalize-first-gates:247` |

### 4 false positives — and they share one cause

| body | file |
|---|---|
| `verticalReflectionIsom.dH_eq verticalReflection_involutive x y` | `HyperbolicIsometryReflection:87` |
| `hf.eqOn_of_preconnected_of_frequently_eq hg hU hz₀ …` | `KeystoneRootsToQ0Bridge:125` |
| `hf.eqOn_of_preconnected_of_frequently_eq hg …` | `ComplexDilogarithmUnique:147` |
| `h.scalar_eq (seminormalRep_jmPowSum …) (seminormalRep_jmPowSum …)` | `SeminormalInequivalence:144` |

These are ordinary term-mode proofs applying a lemma or a constructed object's
field to real arguments — a Mathlib idiom, not a self-assuming projection. They
reach CRITICAL because `CONCLUSION_FIELD` matches the **`_eq` suffix**, and
`foo_eq` applied to arguments is exactly how a great deal of Mathlib is written.

### The refinement, measured

**Exclude `_eq`-suffixed fields from the `applied-field-projection` pattern
only.** On the full population of 27:

- removes **4 of 4** false positives;
- loses **0 of 23** true positives — no genuine one ends in `_eq`
  (`claim_tr_trans_eq_Phi_q` and `claim_rank_eq_two` contain `_eq` but do not
  end in it);
- net **27 → 23** new candidates.

Caveat, since the sample is the whole population but is small: `_eq` is a
heuristic, and a future field named `claim_foo_eq` would be missed. It is
narrowing on the *suffix name*, which is the same kind of gate the file's
history shows going wrong. Prefer, if it can be made to work, keying on whether
the receiver is an **instance-binder name** — that is what actually separates
`ctx.claim_x` from `hf.lemma_eq`, and it does not depend on naming at all.

### Ready to propose

+23 CRITICAL, all hand-verified as genuine. Needs its own PR; do not land it
alongside unrelated work.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-5vkl`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.
