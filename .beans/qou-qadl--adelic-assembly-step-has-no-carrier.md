---
# qou-qadl
title: 'q-RH keystone: the adelic-assembly step is asserted in prose and carried nowhere'
status: completed
type: task
priority: high
created_at: 2026-08-29T17:00:00Z
updated_at: 2026-08-29T17:00:00Z
---

The arc's spine is

```
local q-zeta → Hasse–Weil → Re(ρ_i) = ½ at each place → [assembly] → classical RH
```

Steps 1–3 have blocks, Lean, and (as of `qou-hwax`) an honest conditional status.
**Step 4 has nothing.** `stochastic-mechanics/classical-riemann-hypothesis.md`
states it in a subordinate clause:

> The Hasse–Weil bound guarantees `Re(ρ) = 1/2` for each local geometry
> individually. The Riemann hypothesis asserts that this alignment survives the
> adelic assembly into the global zeta function.

No block, no conjecture, no Lean declaration states that implication.

## What is NOT the gap

`stochastic-mechanics/` does carry adelic infrastructure —
`prop:adelic-reeb-restricted-product` (sorry-free), `def:adelic-substrate`,
`rem:adelic-tate-squeeze`, `rem:adelic-tate-motivic-dual`,
`rem:classical-limit-adelic-assembly`. Do not read that as the step being
carried. The last one is a **remark** with `interprets:
def:classical-limit-functor`, and it is about the archimedean projection `ρ_∞`
of a motivic realization tower — the `q → 1` collapse of the local Reeb
infinitesimal. It says nothing about critical-line persistence.

Corpus-grep, all six paths: "adelic assembly" — 0 in `docs/audits`,
`docs/coordination`, `computations`, `library/INDEX.md`. "critical line" — 0 in
all four. The step is genuinely unstated.

## Why this is the keystone and not one gap among several

Hasse–Weil holds at **every** place, unconditionally, for curves over finite
fields — that is Weil's theorem, and it has been known since 1948 while RH has
stayed open. So local critical-line alignment at every place cannot by itself be
close to RH; the assembly step is carrying the entire distance. Any claim that
the arc "reduces RH to" the local statement is measuring the wrong leg.

Naming it is the whole first task, and it is cheap: a `conjecture` block stating
the implication, `uses` the local corollary, `sorry` + `-- Ref:` per §3b, a
primary conjecture per §3b-tax. That puts the arc's actual claim where it can be
read and attacked instead of inside a subordinate clause — and it makes the
distance visible rather than eliding it.

Sequencing note: `qou-qspc` (the spectral coordinate map) is upstream of this.
The assembly statement should quantify over the *Reeb* spectrum, so it wants that
map to exist first, or it will restate the same ambiguity one level up.

---

## RESOLVED 2026-08-29 — the step now has a carrier

`conj:adelic-critical-line-persistence`, a new block triple in
`stochastic-mechanics/`, registered in the chapter manifest between
`classical-riemann-hypothesis` and `macroscopic-stability-equivalence`.

**The statement.** If the local spectral exponents are critical-line aligned at
every place, then every non-trivial zero of `riemannZeta` has real part ½. The
antecedent is exactly the conclusion of `cor:spectral-half-line`; the consequent
is exactly `conj:classical-riemann-hypothesis`. Primary conjecture per §3b-tax —
its Lean class takes no other conjecture class as a hypothesis.

**Lean carrier**
`QOU.BraidKnot.AdelicCriticalLinePersistence`, content-bearing, **no instance**
(the honest open state). Plus one derived theorem:

```lean
theorem classicalRiemannHypothesis_of_persistence
    {P : Type*} (localSpectrum : P → Fin 8 → ℂ)
    [AdelicCriticalLinePersistence localSpectrum]
    (h_local : ∀ v i, (localSpectrum v i).re = 1 / 2) :
    ClassicalRiemannHypothesis
```

That is a genuine composition, not the projection of a single assumption: it
consumes the persistence class **and** a separate proof of local alignment, and
neither alone gives the conclusion. It states the arc's reduction precisely — and
makes visible that the reduction is only as strong as the open hypothesis.

**Vacuity hazard, recorded in the module docstring and the block's
`authorNotes`.** The class is an *implication*, so it is vacuously true on any
family that is not critical-line aligned. An instance on such a family would be
the `da-arity-conflation` failure mode — right shape, no content. An instance is
an advance only when it comes with a witness family satisfying the antecedent.
Whoever attacks this next should read that paragraph before writing an instance.

**Verification.** `lean`-direct: `ClassicalRiemannHypothesis.lean` built to olean
(exit 0), `AdelicCriticalLinePersistence.lean` exit 0 silent.
`run-validate content/quantum-observable-universe` exit 0, `✓ Valid` — the 13
reported issues are pre-existing and in other blocks, none in this one. Render-QA
grep battery on the `.md`: balanced delimiters, no `\operatorname`, no
align-family env, no non-ASCII.

**What this does and does not do.** It does not make the conjecture any more
likely, and it is not progress on RH. It converts a subordinate clause into an
object with a label, a type and a dependency edge, so the arc's actual claim can
be cited, attacked, and — importantly — *seen to be the whole difficulty* rather
than read as a small remaining step.
