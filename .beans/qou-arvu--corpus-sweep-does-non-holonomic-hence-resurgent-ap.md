---
# qou-arvu
title: "Corpus sweep: does 'non-holonomic hence resurgent' appear elsewhere?"
status: todo
type: task
created_at: 2026-08-14T20:02:00Z
updated_at: 2026-08-14T20:02:00Z
---

Spun out of `qou-tdp0` step 1 (owner-directed, 2026-08-14).

## The inference, and why it is invalid

Found in `docs/coordination/1ppq-qbeta.md` (framing bullet, corrected in place
2026-08-14):

> the odd channel … has no quantum-A-polynomial recurrence, **hence the
> resurgent/Écalle route**

**Non-holonomic does not imply divergent, and only a divergent series can be
resurgent.** The counterexample is the object under discussion: KC22's own
closed form

    D(w) = φ(w)·log(1 − w/ρ) + ψ(w),   φ, ψ algebraic over a degree-12 field

is **convergent** (`ρ = 0.1428`, `κ = 0`) *and* provably not low-order P-finite.
KC22 even says so in as many words — "a convergent series need not be
holonomic … exactly the sort of element that is not low-order P-finite" — so
the corpus already carries the refutation next to the bad inference.

This is a **separate defect** from the 2026-08-09 convergence correction. That
correction withdrew a conclusion drawn *from a divergence that turned out to be
absent*. This is a step that would have been invalid **even if the ladder had
diverged**: the premise (no holonomic recurrence) simply does not deliver the
conclusion (resurgent).

## Work

1. Grep the corpus — `docs/`, `content/`, `computations/`, `.beans/`, Lean
   docstrings — for the *step*, not the words. Patterns: "not holonomic" /
   "no P-finite" / "no A-polynomial recurrence" / "non-holonomic" appearing
   within a sentence or two of "hence"/"so"/"therefore" + "resurgent" /
   "transseries" / "Borel" / "Écalle" / "divergent".
2. For each hit, classify:
   - **(a) the invalid step** — asserts resurgence/divergence *from*
     non-holonomicity ⇒ correct it, citing the `φ·log + ψ` counterexample;
   - **(b) independently grounded** — the object is *separately* known to
     diverge (e.g. the Ohtsuki κ-tower: Gevrey-1, ratios 1.32→3.63→4.93, Borel
     singularity `A ≈ 0.7`) ⇒ leave; the conclusion is right even though this
     particular route to it would not be;
   - **(c) technique** — Écalle median / M-dictionary as a normalization
     scheme ⇒ leave.
3. Check the **converse** while in there: any claim that convergence implies
   holonomicity, or that holonomicity implies convergence. Both are also false
   and the same `φ·log + ψ` object refutes the first.

## Scope discipline

Scope-(a): this is "an inference step does not license its conclusion", **not**
"these objects are not resurgent". Several corpus objects *are* genuinely
divergent and resurgent — the κ-tower above, and C1 at `∞` (irregular, slope
`½`, the live `qou-vkg5`). Correcting the *route* must not be read as
withdrawing those. Do not convert any hit into a scope-(b) exclusion without a
proved invariant.

## Why it is worth a sweep

The corpus's recurring failure mode is a correct finding restated one step too
strongly, then relied on downstream. This one is cheap to check and, unlike the
convergence correction, does not depend on any numerical result — it is a
logical step that can be audited by reading.
