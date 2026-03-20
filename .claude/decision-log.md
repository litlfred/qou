# Editorial Decision Log

Decisions made during editorial review sessions. Entries are append-only.

---

## 2026-03-20 — Definition tightness review (all chapters)

**Session**: `claude/review-categorical-spec-kEy1l`
**Commit**: `b02a331`

### Standing editorial rules (from user)

1. **Definitions must be tight.** Explication belongs in remarks.
2. **Don't combine many definitions in one.** Reused concepts (T, [2]_q, etc.) should be defined first separately.
3. **Can bullet a few things together as a conceptual package** (e.g. QOU), but do not derive sub-definitions inside a definition.
4. **Each definition should be followed by a concrete realisation** so a non-expert reader feels comfortable.
5. **Archimedean realisations inside definitions → move to example/remark.**
6. **"where" blocks listing notation → put in a preceding remark** (before the definition, to keep Lean label compatibility).
7. **Variational equations derived from an action → proposition**, not part of the definition.
8. **Duplicative remarks → condense now**, don't defer with TODOs.
9. **Overlong remarks with multiple sub-sections → split into separate remarks.**
10. **If a remark defines something (e.g. a functional), promote it to a definition.**

### Decisions applied

| # | File | What | Decision |
|---|------|------|----------|
| 1 | qou | `def:quantum-universe` embedded gauge group + q note | Moved to `rem:quantum-universe-explication` |
| 2 | qou | `def:quantum-observable-universe` "restated for emphasis" | Removed |
| 3 | qou | `def:projective-line-object` archimedean realisation | Moved to `ex:projective-line-archimedean` |
| 4 | qou | `def:categorical-connection` combined 3 concepts | Split q-Hodge star to `def:q-hodge-star` |
| 5 | qou | `def:categorical-action` "where" block | Moved to preceding `rem:categorical-action-notation` |
| 6 | qou | `def:categorical-action` variational equations | Moved to `prop:variational-equations` + `rem:variational-archimedean` |
| 7 | qou | `def:observation` archimedean explication | Moved to `rem:observation-archimedean` |
| 8 | torsion | Yekutieli definition order | Reordered: lifting condition before characteristic classes |
| 9 | qou | `rem:gr-substrate-geometry` defines S_q | Promoted to `def:q-yang-mills-levi` |
| 10 | elab | `rem:vanishing-explication` + `rem:jet-bundle` overlap | Merged into single remark |
| 11 | elab | `rem:q-harmonic-physical` duplicates `rem:reeb-physical` | Condensed to cross-reference |
| 12 | qou | `rem:heisenberg-commutator` 3 sub-sections | Split into 3 remarks |
| 13 | qou | `rem:c-substrate-via-levi` exponential discussion | Split to `rem:substrate-exponential` |

### Labels preserved

All original `\label{}` tags kept for Lean compatibility. New labels added; none removed.

---

## 2026-03-20 — Merge upstream main

**Session**: `claude/review-categorical-spec-kEy1l`
**Commit**: `8491980`

### Upstream changes (7 commits)

| Commit | Summary |
|--------|---------|
| `4d75023` | Clarify topological formulas in Ch. 11: narrative proofs, reformulate q |
| `043c5ae` | chore: update proof-objects.json and glossary |
| `a2e4473` | Extract crystal-lattice paragraph from proof into remark |
| `5044894` | Add explicit Skein recursion formulas and tables for proton/neutron |
| `8b3fda5` | Add pair Skein mass decomposition to Lean formalization |
| `8f314a1` | Merge PR #105 (clarify-topological-formulas) |
| `3ac0d29` | chore: update proof-objects.json and glossary from Lean build |

### Conflict resolution

| File | Conflict | Resolution |
|------|----------|------------|
| `experimental-evidence.tex` (×2) | Our branch had `\begin{observation}`; upstream promoted to `\begin{proposition}` and added narrative paragraph + proof | Took upstream: `observation` → `proposition` consistent with editorial rule #7 (derived results are propositions). Added narrative proofs from upstream. |
