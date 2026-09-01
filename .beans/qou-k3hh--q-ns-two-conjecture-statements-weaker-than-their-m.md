---
# qou-k3hh
title: 'q-NS: two conjecture statements weaker than their .md (critical-exponent, ns-counterexample)'
status: completed
type: task
priority: normal
created_at: 2026-08-29T16:40:02Z
updated_at: 2026-08-30T09:05:51Z
---

**Verified** by `docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean`
(`lean`-direct, exit 0, no `sorryAx` on either witness).

Two carriers state strictly less than their `.md`:

- `p2-critical-exponent.lean` — `enstrophy_diverges : ∀ M, ∃ q ≠ 1, M < enstrophy q`
  omits the `q → 1` limit. Witness `regularAtOne` (`enstrophy q = max q 0`) is the
  identity near `q = 1` — regular there — and inhabits the class.
  Also: `criticalExponent` is unconstrained; the asymptotic `~ |q-1|^{-γ_c}` that
  defines it is never encoded.
- `p5-counterexample.lean` — `ns_counterexample_holds` omits the `t → T*⁻` limit.
  Witness `noSingularityAtT` (`velocityProfile t x = max (-t) 0`, `T* = 1`) tends to
  0 at `T*` — no finite-time singularity — and inhabits the class.

**This is NOT the `qou-hjf4` defect.** That one is vacuity (fields that cannot be
false, discharged by unconditional instances, in `QOU.AlgebraicSubstrate`). These
fields *can* be false and have no instance; they are conditional on the wrong
proposition. A zero-inhabitability detector cannot find them.

**Fix** (proposed in the audit, §"Proposed fix"): add the neighbourhood quantifier
to each field. One line each. **Blast radius nil** — neither class has an instance
anywhere, and `ConditionalCorollaries.lean` binds the same five *names* in the
`QOU.AlgebraicSubstrate` namespace, not these.

`conj:levi-degeneracy` recorded in the same audit as a lesser instance: `leviForm`
and `leviForm_symm` are inert, never related to `degeneracySet`.

**Follow-on audit complete (2026-08-29).** All 51 conditional classes / 345
fields in the chapter, via new `scripts/limit-claim-encoding-audit.py`
(--selftest pins both known true positives).

Corpus-wide: 11 candidates over 11,277 .lean files -> **1 genuine**, and it is
NOT in this chapter.

The six fluid-dynamics candidates are all FALSE POSITIVES: the limit is deferred
to an opaque predicate (`jet_diverges`, `is_NS_singular`, `obstruction`), not
missing -- the same device `q_ns_wellposedness` now uses for Smooth/IsSolution,
and the iff-pair form AGENTS.md 3b-cond item 5 names as sanctioned. **The p2/p5
defect does not recur in the q-NS chapter.**

Genuine hit, left for the mass-tower owner (outside this branch's chapter, and
the honest fix changes what the class demands):
`Archimedean/MassTowerOpenProblemsClasses.lean::ChiralityFactorClass.kauffman_derivation`
-- docstring claims `O(h^2)`, field bounds nothing, instance discharges it with
`error_term := fun _ _ _ => 0`. Disclosed, but NOT reachable by
`trivially-inhabiting-instance-census.py` (that keys on data fields; this is a
Prop existential). Fix would be `exists C, forall .., |error_term ..| <= C` near
h = 0, which the current instance would NOT discharge.

Two of my own measurements were wrong before correction, both recorded in the
audit: '53 classes / 2 zero-field carriers' (an enumerator that did not strip
block comments matched docstring PROSE -- real: 51 / 345 / 0), and '0 candidates
over 2000 files' (scope artifact; the corpus is 11,277).

COMPLETED. The two weaker-than-.md conjecture statements were strengthened in
PR #6041 (merged, 5999bdbdae): p2-critical-exponent's enstrophy_diverges became
one-sided, and p5-counterexample's ns_counterexample_holds gained the
singularityTime - eps < t conjunct that puts the blow-up AT the singularity
time rather than merely somewhere.
