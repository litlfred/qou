# The q-NS conditional classes, audited — one new hit, and it is not in this chapter

**Date:** 2026-08-29 · **Beans:** `qou-k3hh`
**Tool:** [`scripts/limit-claim-encoding-audit.py`](../../scripts/limit-claim-encoding-audit.py) (`--selftest`)
**Predecessor:** [`2026-08-29-q-ns-conjecture-statement-strength.md`](2026-08-29-q-ns-conjecture-statement-strength.md)

Follow-on to the two carriers fixed there. The question: is the
"documented as a limit, stated without one" defect a pattern, or were those
two isolated?

## Scope, measured

`fluid-dynamics/` + `lean/QOU/FluidDynamics/`: **51 classes/structures, 345
fields, 0 zero-field carriers.**

Quote those numbers, not the first pass. A naive enumerator that does not strip
block comments reports **53 classes and 2 zero-field carriers**, because
`^(class|structure)\s` matches *prose* — the phrases "structure itself." and
"class is, or implies, either conclusion." inside docstrings. Both phantom
"critical `proof-no-empty-prop-carrier` hits" were sentences, one of them
written in this same session's own fix. The real count of zero-field carriers is
zero.

## The detector

Neither shipped criterion can find this defect class. The field is **not**
vacuous — it can be false — and **not** a self-assuming projection — nothing
projects it. It is simply weaker than its own prose, so a detector keyed on
inhabitability-by-zero is structurally blind to it.

`limit-claim-encoding-audit.py` flags a class field whose **docstring** promises
a limit ("diverges as `q → 1`", "unbounded as `t → T*⁻`", "asymptotically",
"blow-up") while its **statement** contains no device that localises one (`ε`,
`Tendsto`, `𝓝`, `|x - a| < ·`, an interval). `--selftest` pins both known true
positives in their pre-fix form, so a future narrowing cannot silently report a
clean tree.

It is high-recall by design: **a hit is a candidate to read, never a verdict.**
The triage below is why that wording matters.

## Result — 11 candidates over 11,277 files, 1 genuine

| candidate | verdict |
|---|---|
| `ns_obstruction_computation::jet_diverges_of_delta` / `::delta_of_jet_diverges` | **false positive** |
| `ns_obstruction_tower::obstruction_forces_singular` / `::singular_exhibits_obstruction` | **false positive** |
| `yekutieli_obstruction_level::obstruction_iff_exceeds` | **false positive** |
| `vorticity_lower_bound::impl_lower_bound` | **false positive** |
| `AppendixSurreals/SpectralNormalForm::not_finite_iff_Ow_pos` | **false positive** |
| `MathlibExt/QPlancherel::bound` | **false positive** |
| `ConditionalClasses::exists_singularity_time` / `::exists_blowup_rate` | already known — `qou-hjf4` |
| `Archimedean/MassTowerOpenProblemsClasses::kauffman_derivation` | **genuine, new** |

**The six in this chapter are all false positives, and for one reason:** the
limit is *deferred to an opaque predicate*, not missing. `jet_diverges : ℕ →
Prop`, `is_NS_singular : Prop` and `obstruction : ℕ → Prop` are opaque fields
whose meaning fixes what "diverges"/"singular" denote; the class then relates
them to concrete data. That is the same device `q_ns_wellposedness` now uses for
`Smooth` and `IsSolution`, and AGENTS.md §3b-cond item 5 names the iff-pair form
explicitly as the *sanctioned* pattern ("carry the two directions of an iff as
hypotheses, derive it by `Iff.intro`"). `impl_lower_bound` carries its
localisation inside `d : ℝ → ℝ`; `SpectralNormalForm` and `QPlancherel` state
explicit quantitative bounds, which are stronger than a limit, not weaker.

**So the p2/p5 defect does not recur in the q-NS chapter.** A clean negative,
which is the useful answer to the question that was asked.

Two of the eleven are the already-adjudicated vacuous carriers from `qou-hjf4`,
which is a precision signal: the detector's hits overlap the known defect set
rather than wandering.

## The one genuine hit

[`MassTowerOpenProblemsClasses.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean),
`ChiralityFactorClass::kauffman_derivation`:

```lean
kauffman_derivation :
  ∃ (a_K error_term : ℝ → ℤ → ℝ → ℝ), ∀ h writhe avg_content,
    a_K h writhe avg_content
      = chirality_factor_first_order h writhe avg_content
        + error_term h writhe avg_content * h^2
```

The docstring says `a_K` "is asymptotically `1 + w · ⟨c⟩ · h + O(h²)`". The
field says only that *some* pair of functions differs by *something* times `h²`.
Nothing bounds `error_term`, so the `O(h²)` — the entire asymptotic claim — is
unencoded, and the instance discharges it with `error_term := fun _ _ _ => 0`,
closed by `ring`.

**It is disclosed**, in the instance's own docstring: *"Our class field merely
demands existence of `chirality_factor_first_order h writhe = 1 + writhe · h`,
which is closed by `rfl`. The substantive structural content … lives upstream in
the .md narrative."* As with `ConditionalClasses.lean`, the defect is not
concealment; it is that a reader of `chirality_factor_structural` sees a
sorry-free theorem named for a Kauffman derivation whose content is `x = x + 0`.

**Not covered by the existing census.**
`scripts/trivially-inhabiting-instance-census.py` keys on *data* fields filled
with constant content; this is a `Prop` field whose existential is satisfied by a
zero error term. Different shape, so `qou-hjf4` does not reach it.

Fixing it means bounding the error term — `∃ C, ∀ …, |error_term …| ≤ C` on a
neighbourhood of `h = 0` — which is a real strengthening and, unlike the two
q-NS carriers, would **not** be discharged by the current instance. It is
therefore left as a finding for the mass-tower owner rather than patched here:
it is outside this branch's chapter, and the honest fix changes what the class
demands.
