# The Sym² gate cannot separate flavour from colour — item 4's conclusion withdrawn

**Bean:** `qou-8pl3` gap (ii), under epic `qou-8lxd`.
**Date:** 2026-08-26.
**Lean:** `QOU/Eightfold/Sym2GateFSTrichotomy.lean` (sorry-free, `lean`-direct exit 0).

## What was claimed

[`eightfold-open-problems.md`](../../content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md) item 4, before this correction:

> The obstruction audit ([the colour-algebra section](#sec:color-algebra)) shows
> that they *cannot* both come from the same construction: the $\mathrm{Sym}^2$
> gate excludes the icosahedral colour triple $T_1$, while the $G_2$ route
> passes it.

Two defects, one of citation and one of inference.

## 1. The citation is dead

Item 4 attributes the argument to `sec:color-algebra`. That section, per
[`eightfold-way.ts`](../../content/quantum-observable-universe/eightfold-way/eightfold-way.ts),
contains exactly one block — `color-su3-from-g2` — and that block does not
mention $T_1$ or the icosahedral triple at all.

The $T_1$ comparison is in
[`schur-weyl-eightfold.md`](../../content/quantum-observable-universe/eightfold-way/schur-weyl-eightfold.md),
a different section, and **that source is markedly more careful than item 4**:

> What that file *proves* is only the arithmetic … So the correct reading is:
> the octonionic $\mathbf{3}$ is *not excluded* by the $\mathrm{Sym}^2$ gate, on
> a decomposition taken from the literature. It is not a machine-checked pass,
> and the file should not be cited as one.

Item 4 upgraded "not excluded, on a literature decomposition, not
machine-checked" into "the $G_2$ route passes it", and then built a **cannot**
on top of that.

## 2. The inference does not go through

The premise concerns **two different objects**: $T_1$ (icosahedral) fails the
gate; the octonionic $\mathbf{3}$ is not excluded by it. That establishes those
two objects differ.

The conclusion is about **one construction supplying two roles** — flavour and
colour. Nothing in the premise involves a single construction being asked for
both. The comparison never tests the proposition it is offered as proof of.

Under `AGENTS.md` §*Before declaring "refuted" / "ruled out"*, this is a
scope-limited negative (a) presented as a structural exclusion (b), and no
invariant is cited that would license (b).

## 3. The failure is structural, not a repairable gap

The interesting part is that no strengthening of the premise rescues the
argument, because the gate is provably blind to the distinction.

`gate_forces_complex_of_dim_three` proves that at dimension three, passing the
$\mathrm{Sym}^2$ gate is equivalent to carrying a complex-type irrep — real
multiplicities are forced to zero and quaternionic dimensions are even, so the
total is even and cannot be $3$.

Therefore **any** two three-dimensional objects that both pass are both complex
type, and the gate has returned the same verdict for each.
`gate_does_not_separate_two_triples` exhibits two distinct such objects
explicitly. A flavour triple and a colour triple that each pass are, to this
gate, indistinguishable.

This is the second tool in the arc found blind to the flavour/colour question.
The first was the $\mathbb{Z}/3$ grading:
`TrialitySelectionRule.identification_invisible_to_selection_rule` shows that
identifying the groups doubles each quark's triality, and that $2$ is a unit in
$\mathbb{Z}/3$, so every verdict is unchanged. Both of the obvious invariants
see nothing.

## 4. What the gate does establish

Not nothing — and the surviving content is stronger than the withdrawn claim in
one respect. It is a **class** exclusion rather than a two-example comparison:

> No real or quaternionic construction whatever reaches dimension three through
> this gate.

So $T_1$'s failure is a consequence of its Frobenius–Schur type — it is a
rotation representation of $A_5 \subset SO(3)$, hence real — and not a fact
about the icosahedron. `real_triple_fails_gate` is that half in one line, with
no appeal to icosahedral geometry.

## 5. Status after this correction

* Item 4 stays **open**, as it was. Nothing here decides whether flavour and
  colour SU(3) are the same, different, or groupoid-dual.
* What is removed is a *false* piece of support for one answer.
* What is added is a proved reason not to look here again: the gate and the
  grading are both blind, so a discriminator must be found elsewhere.

## 6. Scope

Per the (a)/(b) discipline:

* **(b), invariant named.** *The $\mathrm{Sym}^2$ gate cannot distinguish two
  three-dimensional objects that both pass.* The invariant is the
  dimension/parity bound behind `gate_forces_complex_of_dim_three`. This is a
  structural exclusion of the gate **as a discriminator**, with a witness.
* **(a) only, NOT (b).** Nothing here excludes any construction from supplying
  both roles, nor establishes that one does. Item 4's question is untouched.
