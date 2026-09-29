---
# qou-lx7k
title: selection-rule c1/c2/c3 Lean proves arithmetic over hand-substituted literals, not the hook-length formula
status: completed
type: task
priority: high
created_at: 2026-08-29T16:46:36Z
updated_at: 2026-08-29T18:27:04Z
---

Found 2026-08-29 working qou-u8oy (the three inputs jet-filtration-binding-extensive
carries as hypotheses). Branch claude/sw-period-jet-filtration-inputs-2026-08-29.

THE CLAIM. content/quantum-observable-universe/climax-volume-mass/
selection-rule-anchors-c1-c3.md says of the per-component selection rule
lw(c) = (1/(c+1)) Sum_{lambda |- c+1} dim_q V_lambda:

  "This proposition Lean-formalises both identities. It grants the selection
   rule's two anchors derivation-tight status (they are not a fit; both follow
   from the q-deformed hook-length formula)."

and selection-rule-c2-prediction.md calls its c=2 case "derivation-tight (no fit,
zero free parameters)" and "the first testable prediction of the rule".

WHAT THE LEAN ACTUALLY PROVES, in full:

  selection_rule_c1_eq_one       ((1 : R) + 1) / 2 = 1
  selection_rule_c2_prediction   (1 + (q + q^-1) + 1) / 3 = (q+1)^2 / (3*q)
  selection_rule_c3_eq_family_a  (1 + (q^2+1+q^-2) + (q^2+q^-2) + (q^2+1+q^-2) + 1)/4
                                   = 5/2 + (3/4)(q - q^-1)^2

Every one is an arithmetic identity over literals typed in BY HAND. No partition,
no Young diagram, no hook length and no dim_q occurs in any STATEMENT. The
hook-length computation is done in a docstring and only its OUTPUT reaches the
Lean. The c=1 case is the clearest: `(1+1)/2 = 1` is a fact about the numeral 1,
and its own docstring concedes the q argument "is genuinely unused".

Both files are sorry-free, and both .ts carry validation: "not_checked".

This is the sorry-free != derived failure AGENTS.md legislates against, and
Strict Lean Discipline 8's test catches it: "could this be wrong?" No -- not
because the mathematics is sound, but because the statement does not mention the
objects it claims to be about. The mathematics IS sound; the formalisation does
not reach it.

FIXED, NOT ONLY REPORTED. content/quantum-observable-universe/lean/QOU/Mass/
QHookDimension.lean (this branch) supplies the missing half, sorry-free:

  qInt / qFact          balanced q-integer as an explicit zpow sum, matching
                        mass_at_3A_proper.qint, so [2]=q+q^-1 and [3]=q^2+1+q^-2
  conjugate / hookAt    Young-diagram transpose and arm+leg+1
  hooks                 the hook multiset, COMPUTED from the shape
  hooks_two_one etc.    hooks [2,1] = [3,1,1] and friends, by `decide`
  dimQ                  [n]_q! / prod of the hooks' q-integers
  dimQ_two_one          dim_q V_(2,1) = [2]_q, DERIVED
  selection_rule_c1_from_hooks / _c2_from_hooks    the sums over the real dimQ
  selection_rule_c1_real / _c2_real                same over an ordered field, 0<q

lean-direct exit 0; axioms [propext, Classical.choice, Quot.sound]; hooks_two_one
depends on none.

TWO THINGS THE WORK ITSELF TURNED UP.

1. The non-vanishing hypotheses are NOT decoration. dimQ divides by the product
   of the hooks' q-integers and Lean sends a zero denominator to 0, so at
   [2]_q = 0 (q^2 = -1) `dimQ q [2] = 1` is genuinely FALSE, not merely
   unproved. My first attempt tried to prove it over an arbitrary field without
   them and the by_cases branches were unprovable -- correctly. qInt_pos
   discharges them for every real q > 0, which is the regime the blocks use.
2. selection_rule_c1_from_hooks divides by 2, so over an arbitrary field it
   needs (2 : R) != 0: `2/2 = 1` is FALSE in characteristic 2. Same shape as the
   `two_ne` in markov_param_eq_half_h.

NOT DONE HERE, deliberately: the .md/.ts of the two blocks still describe their
literal-substituted theorems as "Lean-formalises ... derivation-tight", and their
lean.ref still points at those. Updating them is a content-block change needing
sidecar QA and is a different PR; QHookDimension.lean is standalone library Lean
with no sidecar. Follow-up: re-point the refs (or add uses[]) at the derived
theorems and soften the .md claim to match what each theorem states.

SCOPE. This says nothing about whether lw(c) is the RIGHT selection rule, nor
about a_D^(n) = lw(n-1) -- the identification that jet-filtration-binding-
extensive actually calls conjectural. It says the q-dimension arithmetic those
blocks rest on is now derived rather than asserted.

RESOLVED 2026-08-29, PR #6051, branch claude/selection-rule-refs-to-derived-2026-08-29.

QOU.Mass.QHookDimension extended to the partitions of 4, so all three cases (c=1, c=2, c=3) now derive from shape -> conjugate -> hook lengths -> dimQ rather than from hand-substituted literals. Derived theorems added to BOTH .lean siblings (not only the library) because AGENTS.md 0a resolves lean.ref to the sibling first -- a library-only target would have been shadowed. Both .ts retargeted, validation: validated.

The original identities are kept: they are true, and they are what the derived statements reduce to. What changed is that the hook-length step is now inside a statement instead of inside a docstring.
