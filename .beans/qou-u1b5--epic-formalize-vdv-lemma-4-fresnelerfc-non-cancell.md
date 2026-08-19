---
# qou-u1b5
title: 'EPIC: formalize vdV Lemma 4 (Fresnel/erfc non-cancellation) — discharge VdVWhiteheadLemma4'
status: todo
type: epic
created_at: 2026-08-11T00:36:10Z
updated_at: 2026-08-11T00:36:10Z
---

EPIC RE-SCOPE 2026-08-19 -- remaining bricks go from BUILD to ASSEMBLE.

The epic's TARGET is still genuinely open: VdVWhiteheadLemma4 has no instance
anywhere in the corpus, and main's 18-file Kashaev* lane is 4_1 (kashaevProd is
defined in FigureEightVolume.lean), not the Whitehead link.  So this epic is
NOT redundant.

But its MACHINERY is already on main, generically, in QOU/MathlibExt/: six
Gaussian* files, CompositeEulerMaclaurin, CorrectedTrapezoid, TrapezoidRule.
qou-shrp learned this the expensive way -- it rebuilt a weaker first-order
Euler-Maclaurin rule nine days after the composite one landed, and the lane had
ALREADY applied it to the same function (logSinc = phi - log 2).

STANDING RULE for every remaining brick, before writing a line:
  grep -rln "<topic>" content/quantum-observable-universe/lean/QOU/MathlibExt/ \
                      content/quantum-observable-universe/lean/QOU/Knot/
"I checked what landed since my fork point" is NOT the corpus-grep checklist --
it cannot see a file that has been on main for nine days.
Audit: docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md
