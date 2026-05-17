# Coordination ledger: 1 ppb categorical-chain frontier

Tracking PRs working toward the 1 ppb $Q_\beta$ / mass-table goal.

## Scope map (2026-05-17)

| PR | Branch | Author | Role |
|---|---|---|---|
| [#665](https://github.com/litlfred/qou/pull/665) | `claude/knot-volumes-review-Pgt8o` | claude (this session) | N=4 + σ_1 + n-strand foundation + scaffolds |
| [#672](https://github.com/litlfred/qou/pull/672) | `claude/post-665-open-rd-hoefsmit-matrices` | claude (this session) | R&D inventory + YB d_1↔d_2 finding |
| [#664](https://github.com/litlfred/qou/pull/664) | `claude/post-662-c3-chain-anti-staleness` | claude (other session) | `prop:hopf-jones-c3-categorical` (alternate c_3 = −2 proof) |
| [#671](https://github.com/litlfred/qou/pull/671) | `claude/post-670-story-b-mp-c5-c6` | claude (other session) | Story B forced audit + m_p chain closure gap |
| [#663](https://github.com/litlfred/qou/pull/663) | `claude/isotope-mass-witness-data-x5lCh` | claude (other session) | isotope-mass-table + anti-staleness infra |

## Classification

| pair | overlap | dependency | cherry-pick |
|---|---|---|---|
| #665 ↔ #672 | HIGH (#672 follows #665) | #672 depends on #665 | — |
| #665 ↔ #664 | HIGH (same c_3 = −2, different proof paths) | independent | none planned; cross-ref both after merge |
| #665 ↔ #671 | MEDIUM (same Story B framing) | independent | none |
| #665 ↔ #663 | LOW (different files, different topic) | #663 consumes substrate Q_β; could swap to N=4 once #665 lands | none |
| #672 ↔ #664 | MEDIUM (#672 documents YB anomaly; #664 may implicitly need YB) | independent | none |

## Coordination comments posted

- [#664 — coordination from #665+#672](https://github.com/litlfred/qou/pull/664#issuecomment-4469105688)
- [#671 — coordination from #665+#672](https://github.com/litlfred/qou/pull/671#issuecomment-4469149330)
- [#663 — Q_β substrate swap opportunity](https://github.com/litlfred/qou/pull/663#issuecomment-4468003754) (earlier)

## Cross-PR findings affecting siblings

### YB cubic d_1↔d_2 anomaly (PR #672)

Symbolic computation shows the chapter `hoefsmit_sigma1` matrices
fail YB cubic with `σ_0 = diag(q, −q⁻¹)`. Analytical fix: swap
`hoefsmit_d1` and `hoefsmit_d2` in
`hoefsmit-V21-cos-symmetrization.lean`. Zero downstream regressions
(basis-permutation preserves all scalar invariants).

**Implications for siblings**:
- #664: Step 2 ("Frobenius selection picks V_(2,2,2) at order h⁶")
  may or may not depend on YB-compatible σ_1 conventions. Coordination
  comment posted asking; awaiting response.
- #665: cross-PR fix commit `df5621609` removes the vacuous
  `yangBaxter_H3 := ⟨0, rfl⟩` instance to avoid asserting a falsehood
  under current conventions.

## Open questions for the author

1. **Q_β substrate swap on #663**: ship #663 as-is with `form_a_cos`
   (residual +306 ppm), or wait for #665 to land then swap to the
   N=4 ladder (residual ~7e-6 ppm)?
2. **c_3 cross-references**: after #665 and #664 both land, should
   `prop:q-beta-c3-hopf-three-fold-markov` (#665) cite
   `prop:hopf-jones-c3-categorical` (#664) as upstream, or vice-versa?

## Next concrete task (non-overlapping)

Await Gemini/Copilot review responses on #665 and #672; address as
they come in. R&D items 1-5 (from #672's inventory) are queued for
follow-up branches; none touch sibling PR scopes.
