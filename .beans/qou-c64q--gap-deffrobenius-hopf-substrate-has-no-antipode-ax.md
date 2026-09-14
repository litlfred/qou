---
# qou-c64q
title: 'GAP: def:frobenius-hopf-substrate has NO antipode axiom -- S is free data, so S^2 = id is independent (owner decision)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T18:01:40Z
updated_at: 2026-09-14T18:02:32Z
---

## Measured 2026-09-14 (session: duality-sigma-hermitian-derivation)

Full write-up:
[`docs/audits/2026-09-14-antipode-is-free-data-s-squared-is-independent.md`](../docs/audits/2026-09-14-antipode-is-free-data-s-squared-is-independent.md).

### The finding

`def:frobenius-hopf-substrate` contains **no antipode axiom**. The Hopf
condition `mu . (S (x) id) . Delta = eta . eps` is absent from the block, from
both of its Lean carriers, and from everything downstream. `S` satisfies no
law, so no property of it is derivable and none is refutable.

`S^2 = id` is therefore **INDEPENDENT** of the definition -- not open, not
unproved, not false. Same for `unit` and `counit`, which are equally free.

### Evidence

- `scripts/lean-structure-field-law-audit.py` (new) strips docstrings and
  comments first, then counts each data field's name in the LAW field types.
  `FrobeniusHopfData` (library) and `FrobeniusHopfSubstrate` (content block)
  carry DIFFERENT law sets and give the IDENTICAL verdict: `unit`, `counit`,
  `antipode` -> 0 mentions.
- `QOU/QuantumObservableUniverse/AntipodeIndependence.lean` (new) --
  `lean`-direct exit 0, zero warnings, sorry-free, `#print axioms` clean
  (only `propext`, from `simp only`). Seven declarations; the decisive one is
  `id_eq_zero_of_antipode_sq_eq_id`: in any ambient category with zero
  morphisms, `S ≫ S = id` as a theorem forces `id_A = 0`, i.e. every
  Frobenius-Hopf object is a zero object. So `S^2 = id` cannot be made
  derivable by adding axioms that do not mention `S`.

### Not the discovery -- credit where due

The block's own QA sidecar already records it in prose:
`frobenius-hopf-substrate.qa.json`, criterion `trap-nonspeakable`, reviewer
`agent:d02` -- *"THE ANTIPODE IS UNCONSTRAINED ... so S is free data"*. What
is new here is the machine check, the same hole in the library carrier the
Lagrangian consumes, the `unit`/`counit` extension, and the cost theorems.

The corpus's one "proof" of `S^2 = id` --
`QOU.BraidKnot.antipode_involution`, `rfl` -- is vacuous because that file
defines `antipodeS := id`. Already in the vacuous class per
`docs/audits/2026-09-06-q-analysis-uniqueness-axioms-are-false.md`.

### OWNER DECISION -- not agent-actionable

Adding an antipode axiom is a change to a central definition. Per AGENTS.md
"ASK THE OWNER BEFORE CHANGING THINGS" it is outside both exemptions (it
neither increases precision nor is fixed by the corpus), and per
"Axiomatization is NOT a Proof" adding one to unblock a downstream consumer
is exactly the forbidden move. Precedent: `qou-t7mt`, same block, axioms 4-5,
held three weeks and resolved by owner pick.

Blast radius if added: `mass-theory/frobenius-antipode-unifies-chirality-and-tower`,
`mass-theory/frobenius-antipode-neutron-tower-closure`,
`braids-and-knots/frobenius-antipode-lean-stub.lean`.

Caution for whoever takes the decision: for `U_q(g)` the antipode satisfies
`S^2 =` conjugation by `K_{2rho}`, which is NOT the identity, and the QOU
ambient category is braided rather than symmetric. A genuinely q-deformed
substrate plausibly wants `S^2 != id`.
