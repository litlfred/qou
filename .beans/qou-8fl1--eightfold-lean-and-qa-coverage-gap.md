---
# qou-8fl1
title: 'Eightfold chapter: Lean + QA coverage gap after the honesty pass'
status: todo
type: task
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-08-06T00:00:00Z
---

## Context

Honesty pass landed (see the `content(eightfold)` commit). Overclaims withdrawn,
four wrong meson weight rows fixed, corner-label error fixed, invalid Hurwitz
inference withdrawn. What remains is coverage, not accuracy.

## Open items

1. **QA sidecars.** 11 `.qa.json` files carrying `"criteria": {}` were removed —
   zero criteria had ever been evaluated, but populated `source_hashes` made the
   staleness check report them current, so they actively suppressed QA. The
   chapter now has **no** sidecar coverage. Needs a real `qa-sweep` run, which
   needs the `folio-assistant` pipeline
   (`scripts/setup-folio-assistant.sh`) — not available in the sandbox this pass.
   Same defect still live in `appendix-standard-model/strand-twist-datum.qa.json`
   and 6 `section-title-audit.qa.json` files across 5 papers.

2. **Lean coverage.** Three `proposition` blocks have no Lean backing:
   `prop:schur-weyl-eightfold` (ref removed — pointed at a module proving a
   different statement), `prop:meson-octet-decomposition`,
   `prop:borromean-decuplet`. Under AGENTS.md these warn rather than fail, but a
   proposition chapter with 1 real Lean module is thin.

3. **`Sym2Gate.lean` is vacuous.** Its declarations reduce to
   `6 = 6 ∧ 0 = 0` and `1 + 5 = 6 ∧ 1 > 0` — arithmetic tautologies whose
   representation-theoretic content lives in the *statement names*, not the
   proofs. Under "Strict Lean Discipline" item 5 this is a review failure. The
   prose now says "not excluded by the Sym² gate" rather than "passed", but the
   file should either encode a real decomposition claim or be demoted.

4. **Chapter `.ts` TODOs** (3, all research-gated): `a2-root-system-proof` +
   `hexagonal-weight-lattice` (§1), `color-tube-coords-intro` (§5),
   `thurston-relaxation` (§6).

5. **New open problems added to §8** and needing owners: the
   spin–flavour–colour selection rule (the decuplet identification currently
   matches dimensions and weights only), and Gell-Mann–Okubo (asserted as a
   consequence, not derived; the one cross-check gives ≈6% vs ≈3.3%).
