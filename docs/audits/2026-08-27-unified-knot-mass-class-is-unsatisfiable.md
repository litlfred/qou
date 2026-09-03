# The `UnifiedKnotMass` class is pinned to its own stubs, and one of its theorems is vacuous

**Date:** 2026-08-27 · **Bean:** `qou-0avp` · **Status:** machine-checked (`lean` exit 0)
**Subject:** [`content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean`](../../content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean)
**Reproduce:** [`scripts/lean/probes/unified-knot-mass-satisfiability.lean`](../../scripts/lean/probes/unified-knot-mass-satisfiability.lean)

## Summary

`class UnifiedKnotMass` carries the three-term mass identity
`total_mass = descended + tower + frobenius_correction`. Two of its fields tie
`descended` and `tower` to **stub definitions that are identically zero**, so
every instance of the class is forced to have those two terms vanish. The file's
`trivial_vortex_vacuum_mass` then assumes `U.descended = 1`, which contradicts
the class it quantifies over: its hypotheses are inconsistent and its conclusion
follows from `False`.

Four claims, all verified (`lean` exit 0 against the real file, no stubbed
harness):

| Claim | Verified statement |
|---|---|
| `descended` is forced to 0 | `(U : UnifiedKnotMass) → U.descended = 0` |
| `tower` is forced to 0 | `(U : UnifiedKnotMass) → U.tower = 0` |
| the hypotheses are contradictory | `(U : UnifiedKnotMass) → U.descended = 1 → False` |
| so the theorem is vacuous | the same hypotheses yield `U.total_mass = 12345` |

## What is *not* wrong

Stating this precisely matters, because the file does several things right and a
blunter reading would condemn them.

- **The stubs are disclosed.** `descendedMarkov` and `braneTower` carry the
  docstring *"Concrete model: each component returns 0; the genuine constructions
  live downstream in dedicated files"*, and name those files
  (`prop:categorical-mass-markov`, `prop:mass-endomorphism-tower`).
- **No instance is ever constructed.** Every use in the corpus is
  `(U : UnifiedKnotMass)` as a hypothesis. Nothing is claimed unconditionally,
  and the framework does not assert that any nucleon has zero descended mass.
- **The conditional-class pattern itself is the sanctioned one** (AGENTS.md
  §3b-cond).

## What is wrong

The defect is one level in, and is not a stub problem:

> **The class fields point at the stubs, not at the constructions they name.**

`descended_is_markov` does not say *"`descended` is whatever
`prop:categorical-mass-markov` yields"*. It says `descended = |descendedMarkov q braid|`,
and `descendedMarkov q _braid := 0 * q`. So the antecedent `U : UnifiedKnotMass`
is one that **no intended model can satisfy** — an instance carrying a real
Markov descent could not exist, because the field equation would refute it.

This fails AGENTS.md §3b-cond item 5, the non-degeneracy requirement: a
conditional class must axiomatise the *hypotheses* so the theorem can derive its
conclusion from them. Here the hypotheses are pinned to constants, so the
"conditional" results are conditional on an empty antecedent. It is also the
failure mode §"Conditional-proved ≠ premise-established" describes, in its
sharpest form: not merely that the premise is unestablished, but that it is
**unestablishable as written**.

`trivial_vortex_vacuum_mass` makes the collapse visible because it adds a second
hypothesis the class contradicts:

```lean
theorem trivial_vortex_vacuum_mass (U : UnifiedKnotMass)
    (h_desc : U.descended = 1) (h_tower : U.tower = 0) :
    U.total_mass = 1 + electronMass * frobeniusCoCasimirTrace U.q U.n
```

Its docstring explains `h_desc` as *"the descended trace evaluates to 1 (the
trace of the identity element of `H_n(q)`)"* — a correct piece of mathematics,
and exactly the reason the class's pinning is wrong. `tr(1) = 1`, not 0. The
author knew the right value; the class forbids it.

Note that `h_tower : U.tower = 0` is *redundant* rather than contradictory (the
class already forces it), which is the tell: one of the two hypotheses restates
what the class says and the other refutes it.

## Two further findings in the same file

Independent of the above; found in the same read and recorded in the vacuity
ledger.

**1. `frobenius_codim_trace_n2/n3/n4/n5` — an axiom relocated, not discharged.**
The `frobeniusCoCasimirTrace` docstring states the mechanism itself:

> *"The previous formulation declared `frobeniusCoCasimirTrace` as
> `noncomputable opaque` and used three axioms (`frobenius_codim_trace_n2/n3/n4`)
> to bridge to the explicit values. Giving the function a partial `def` with
> `match n` discharges those axioms — they are now **theorems**."*

Nothing was discharged. The axioms' content moved into `match` arms, where the
theorems read it back by `rfl`. That is **strictly worse than the axioms it
replaced**, because `#print axioms` reported them and cannot see a `def` arm
(AGENTS.md §1a). The `rfl` has zero verification power: any value typed into an
arm passes.

**Narrow scope.** The *values* are separately derived in
[`frobenius-codim-universal.lean`](../../content/quantum-observable-universe/mass-theory/frobenius-codim-universal.lean)
— `hecke_n{3,4,5}_frobenius_codim` are genuine `Fin.sum_univ` + `ring`
evaluations of `Σ_λ 1/dim_q(λ)`. The mathematics is not fabricated. The defect is
that **nothing in Lean links an arm to its companion theorem**: the
cross-validation is by human eye across two files, so a mistyped arm is
undetectable.

*Fix:* state `frobeniusCoCasimirTrace q n = ∑ i, 1/heckeH{n}DimQ q i` and
discharge it against the companion. That is a real link and it catches a typo.

*Caveat on the n=2 companion:* `heckeH2DimQ (_q) (_i) := 1` discards both
arguments, so `hecke_n2_frobenius_codim` is `1 + 1 = 2` and cannot detect a wrong
q-dimension. The claim is true and disclosed; the check is weak. Recorded
advisory. Its n=3/4/5 siblings are genuine and are not flagged.

**2. `frobeniusCoCasimirTraceFallback` — the docstring contradicts the body.**
The docstring ends *"Concrete model: returns 0 for every n ≥ 6"*. The body is
`def frobeniusCoCasimirTraceFallback (_q : ℝ) (n : ℕ) : ℝ := (n : ℝ)`, which
returns 6 at n = 6. This term carries the Frobenius correction for every nucleus
past the smallest, so a reader trusting the docstring reads that contribution as
absent when it is `m_e · n`.

**3. A self-certifying audit string.** `def s3_bridge_audit_status : String :=
"n=2 PROVED (rfl); n=3 PROVED (rfl); n=4 PROVED (rfl); n=5 PROVED (rfl); …"`
asserts its own audit verdict as a string literal, where the proof is `rfl`
against a def arm. Any status tooling that greps the tree will read it as a
result.

## Disposition

Findings only — **no Lean is changed here.** The fix (re-pointing the class
fields at the downstream constructions, or replacing them with genuine
hypotheses) is a content change to a mass-theory block and belongs to its own
bean with its own review. Recording it as an audit doc plus a reproducible probe
is the honest exit per AGENTS.md §"When you can't close it — bean the gap".

The probe is deliberately kept **outside** the source file, as an appendable
fragment with a recipe in its header, so it can never be mistaken for a claim
the paper makes. The recipe was run verbatim from the committed file before this
doc was written; it exits 0.

## Method note

This came out of the `major` tier of the borrowed-name audit
(`scripts/lean-borrowed-name-audit.py`, bean `qou-0avp`), not from the CRITICAL
tier — `descendedMarkov` and `braneTower` were already CRITICAL and already
adjudicated `genuine`/`placeholder-disclosed` on 2026-08-26. **That earlier
verdict was right about the stubs and stopped one step short**: it recorded that
the two defs are zero and disclosed, without asking what the class *does* with
them. The `major`-tier entries for `frobenius_codim_trace_*` are what sent me
back into the file.

One correction to my own ledger fell out of the same read: I had recorded
`frobenius_codim_trace_n5` as `legit` on the evidence *"same family as the
`hecke_nX_frobenius_codim` group"*. It is not the same family — the latter
evaluates the sum, the former restates a def arm. I assimilated one to the other
by name similarity, which is the arity/identity conflation AGENTS.md §"Grep the
claim SHAPE" warns about, committed while building a detector for that class.
Revised to `genuine`.
