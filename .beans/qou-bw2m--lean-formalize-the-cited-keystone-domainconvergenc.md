---
# qou-bw2m
title: 'Lean: formalize the cited keystone domain/convergence results'
status: completed
type: task
priority: normal
created_at: 2026-08-10T19:52:01Z
updated_at: 2026-08-10T23:29:33Z
parent: qou-i85j
---

BUILT rather than beaned, per .agents/rules/lean-infra-rule.md item 3. New file QOU/BraidKnot/HabiroDomainVanishing.lean, sorry-free, generic CommRing (§7c): qPochSelf, qPochSelf_zero, qPochSelf_eq_zero_of_pow_eq_one (the vanishing mechanism), qPochSelf_eventually_zero, qPochSelf_ne_zero_of_no_root_of_unity. Verified lean-direct exit 0 against the real import cone; #print axioms = [propext, Classical.choice, Quot.sound] on all four, no sorryAx. The last two together ARE the keystone obstruction in algebraic form: termination at roots of unity, non-termination at q0. NOT formalized, and per rule item 4 these are not beans either - they are CITED published results whose formalization needs theory Mathlib does not have (no Faddeev quantum dilogarithm, no Habiro ring): the Beliakova-Le domain theorem, GK state-integral convergence, and the GK closed form. Verified numerically instead (1.1e-19 by quadrature). Reopen only if the keystone advances to the point where one of them must be machine-checked.
