# α_EM B2 lift — modular-family hypothesis killed; numerics exhausted (2026-07-18)

**Bean:** `qou-tq20`, tranche 7 — closes the parameter-free numerical
program on the τ-identification.

**Probe:** [`computations/alpha_em/alpha_em_modular_family_probe.py`](../../computations/alpha_em/alpha_em_modular_family_probe.py)
→ [`alpha-em-modular-family.witness.json`](../../computations/alpha_em/alpha-em-modular-family.witness.json)
— 4/4 PASS.

**Hypothesis label (owner question, 2026-07-18: "is modular family from the
lit or just made up?"):** the modular family was a **program inference**
(elimination after #4027 killed the heat family, plus nome-nativeness), not
a literature identification. Standard ingredients (moduli deformation;
`det′Δ(E_τ) = (Im τ)²|η|⁴`, Ray–Singer/OPS; the nome — also the corpus's B1
fibre dictionary); the identification claim itself is the open wall. This
tranche **tested** the hypothesis — and killed it.

**Scope guard (STRICT):** scope-(a) kills; zero free constants by
construction; no fit; nothing wired; `1/(8π)` stays phase-4.

## The test — exact dictionary, no freedom

For real q ∈ (0,1) the nome inverts exactly: `τ = i·|ln q|/(2π)` — every
comparison point is a prediction. Three canonical per-factor weight
families for the isotypic pair `(E_{5τ}³, E_τ)` vs the Markov ratio `r(q)`:

| Family | Behavior | Outcome |
|---|---|---|
| harmonic (`dim H^{1,0}`) | constant 3 | **killed** — fails pointwise (r(0.8) = 5.76) |
| area (`Im τ`) | constant 15 | **killed** — fails at the anchor (r(1) = 3) |
| `det′Δ` (`(Im τ)²\|η\|⁴`) | `~3·e^{4π/(15y)}` at the anchor (η functional equation) | **killed** — 1.1e45 at q = 0.95 vs r = 3.45 (~45 orders) |

## Synthesis — the wall is irreducibly categorical

With the prior tranches — endpoint-constants null (#4022), heat reciprocal
power-law dictionaries killed (#4027), and now all three nome-anchored
modular families dead — **every parameter-free numerical candidate for the
identification's dictionary is excluded.** This sharpens the corpus's
Im(q) fibre-vs-observable discipline: the nome is a *fibre-level*
dictionary, while the Markov weights at real q are *archimedean*
evaluations; the dictionary the identification needs **is the archimedean
τ-functor itself** — precisely the categorical content of the open lift
(`qou-tq20`). Further numerics cannot decide it.

## Where the wall stands (end of the numerical program)

```
Wall = the B2 lift's Reality-realization premise, open half:
  τ-identification of the canonical Markov channel weight with a real
  (Laplacian-derived) operator on H¹(Bring).
Proved free:      reality half (#3999 constructor).
Consistency:      (3,1) isotypic match (#4019) — survives.
Excluded:         endpoint dictionaries (#4022); heat-family reciprocal
                  power-laws (#4027); nome-anchored harmonic/area/det′Δ
                  modular families (this).
Remaining route:  categorical — construct the archimedean τ-functor's
                  action on the channel data (Mathlib CategoryTheory now
                  reachable via the lake-cache restore, #3985).
```
