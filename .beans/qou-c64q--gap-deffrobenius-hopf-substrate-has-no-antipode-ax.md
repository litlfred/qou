---
# qou-c64q
title: 'GAP: def:frobenius-hopf-substrate has NO antipode axiom -- S is free data, so S^2 = id is independent (owner decision)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T18:01:40Z
updated_at: 2026-09-14T19:05:39Z
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


---

## 🟩 RESOLVED 2026-09-14 — owner chose A + C; B answered NO

Owner: **A yes** (add the standard Hopf antipode axiom), **C yes** (fix all
three holes), and asked B: *"can we derive S^2 = id from A?"*

### B: no, and the evidence is not mine

- **Mathlib's own theorem carries the hypothesis.**
  `CategoryTheory.HopfObj.antipode_antipode` is stated *"In a commutative Hopf
  algebra, the antipode squares to the identity"* and takes
  `comm : (beta_ A A).hom >> mu[A] = mu[A]` as an explicit argument. Re-exported
  as `QOU.antipode_sq_of_comm` so the dependence is visible from inside the
  corpus rather than asserted about it.
- **The counterexamples are q-deformations.** `U_q(g)`:
  `S^2(x) = K_{2rho} x K_{2rho}^{-1}`. Taft algebra of dim `n^2`: `S` has order
  `2n`.

Sharp for this framework: `comm` is close to the **negation** of q-deformation,
and `def:quantum-universe` specifies braided-monoidal-not-symmetric precisely to
keep the braiding non-trivial. `S^2 = id` is the wrong thing to want here.

### Scope was larger than the question described

The prose ALREADY asserted most of what was missing — axiom 1 "associative
unital algebra object", axiom 2 "coassociative counital coalgebra object" — and
**none** of assoc / 2 unit laws / coassoc / 2 counit laws was in either Lean
carrier. A+C is mostly the Lean catching up with its own block; only the
antipode condition is new mathematics.

### What landed (`f23b41ee0d`)

Eight law fields on both carriers, Mathlib field shapes. `.md` axiom 2 now
states the Hopf condition and keeps the old equation under its correct name
(counit multiplicativity). Two `authorNotes` on the `.ts`.

**Payoff:** `QOU.FrobeniusHopfData.antipode_unique_of_left` — the antipode is
**determined** by `(mu, eta, Delta, eps)`, no longer free data. Proof runs in
`CategoryTheory.Conv A A`, which is a monoid only given the six C laws — that
is why C was not optional.

**Blast radius, measured first: one constructor.** `TrivialWitness.unitFrobHopf`
(the unit object) is the only record literal in the corpus; all eight new laws
discharge there by `coherence`, so the definition stays inhabited.

**Scope correction to my own theorem:** `id_eq_zero_of_antipode_sq_eq_id`
substituted `g = 0` for the antipode and so needed free data. No longer
available. `AntipodeIndependence.lean` restated over a local
`FrobeniusHopfDataPreAxiom` so the record stays machine-checked.

### Still open, recorded not acted on

1. **No bialgebra axiom.** The bimonoid compatibility is absent, so the
   substrate is not a Hopf monoid in Mathlib's sense and `antipode_antipode`
   cannot be applied to it even given `comm`. **Owner's call**, as this was.
2. **Three structures named `FrobeniusHopfSubstrate`** with different field
   sets (content block 8 fields; `categorical-reeb-derivation` obj/mul/unit;
   `substrate-self-duality` obj/comul/frobeniusForm). The `markovZ` overload
   defect again. Needs its own bean.

Bean stays **in-progress** — item 1 is an open conjecture-adjacent decision
(rule 13a).
