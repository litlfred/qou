# Two q-NS conjectures are satisfied by counterexamples to themselves

**Date:** 2026-08-29
**Probe:** [`2026-08-29-q-ns-conjecture-statement-strength-probe.lean`](2026-08-29-q-ns-conjecture-statement-strength-probe.lean)
(`lean`-direct, **exit 0**, `#print axioms` shows no `sorryAx` on either witness)
**Companion (different defect, already recorded):**
[`2026-08-24-shape-of-claim-is-not-content.md`](2026-08-24-shape-of-claim-is-not-content.md)

---

## The finding

Two conjecture carriers in `fluid-dynamics/` state a **strictly weaker**
proposition than the `.md` block they formalise. Not vacuous — each field is a
real, falsifiable claim — but the claim is missing the limit that carries all
the physics, and the docstring one line up asserts the limit anyway.

### 1. `conj:critical-exponent` — the `q → 1` limit is not encoded

[`p2-critical-exponent.lean`](../../content/quantum-observable-universe/fluid-dynamics/p2-critical-exponent.lean):

```lean
enstrophy_diverges : ∀ M : ℝ, ∃ q : ℝ, q ≠ 1 ∧ M < enstrophy q
```

The docstring reads *"The enstrophy diverges as `q → 1`"*. The field says only
that enstrophy is **unbounded somewhere off `q = 1`** — no neighbourhood of `1`
appears in it.

**Witness** (`regularAtOne`, verified): `enstrophy q = max q 0`. Near `q = 1`
this is the identity — bounded, continuous, no divergence of any order. It
inhabits the class.

A second gap in the same carrier: `criticalExponent` and its positivity are
declared, but the asymptotic `enstrophy(q) ~ |q-1|^{-γ_c}` that *defines* γ_c is
never encoded, so no field constrains γ_c at all. Any positive real is a legal
critical exponent.

### 2. `conj:ns-counterexample` — the `t → T*⁻` limit is not encoded

[`p5-counterexample.lean`](../../content/quantum-observable-universe/fluid-dynamics/p5-counterexample.lean):

```lean
ns_counterexample_holds :
  ∀ M : ℝ, ∃ t x : ℝ, t < singularityTime ∧ M < velocityProfile t x
```

The docstring reads *"The velocity is unbounded as `t → T*⁻`"*. The field says
only that the velocity is **unbounded on the whole half-line `t < T*`**.

**Witness** (`noSingularityAtT`, verified): `T* = 1`, `velocityProfile t x =
max (-t) 0`. This tends to `0` as `t → 1⁻` — it is perfectly regular *at the
alleged singularity time* — and is unbounded only as `t → -∞`. It inhabits the
class.

So the formal statement is satisfied by a flow that has no finite-time
singularity, which is the thing the block exists to claim.

### 3. `conj:levi-degeneracy` — `leviForm` is inert

[`levi-degeneracy-conjecture.lean`](../../content/quantum-observable-universe/fluid-dynamics/levi-degeneracy-conjecture.lean)
carries `leviForm`, `leviForm_symm` and `degeneracySet`, and asserts
`degeneracySet = {1/κ : κ ≥ 2}`. Nothing relates `degeneracySet` to `leviForm`,
though the docstring defines it as *"the locus on which the Levi form is not
positive-definite"*. The set equality is content-bearing; the Levi form is
decoration. Not probed here — recorded for completeness.

---

## Why this is a separate defect from `qou-hjf4`

[`2026-08-24-shape-of-claim-is-not-content.md`](2026-08-24-shape-of-claim-is-not-content.md)
covers the `QOU.AlgebraicSubstrate` family — carriers whose fields are
*theorems* (`∃ K, 0 ≤ K ∧ K ≤ 2E`), discharged by unconditional global
instances. That is **vacuity**: the field cannot be false.

These two are the opposite shape. The fields **can** be false, no instance
exists in the tree, and the conditional theorems above them are genuinely
conditional. The defect is that they are conditional on *the wrong proposition*
— one an unrelated flow satisfies. A detector keyed on "is this field
inhabitable by zero" does not fire, because these are not inhabitable by zero;
it takes a purpose-built counterexample, which is what the probe supplies.

Note the two `QOU.FluidDynamics`-namespace carriers `QAubinLions` and
`RegularityBreakdown` (`∃ q_thresh : ℝ, q_thresh > 0`) **are** the vacuity
shape and are already recorded in
[`vacuous-prop-carrier-baseline.json`](vacuous-prop-carrier-baseline.json);
independently re-verified today (exit 0, no `sorryAx`).

---

## Proposed fix — cheap, local, no new mathematics

Both are one-line strengthenings that make the statement say what the prose
already says. Neither requires progress on the underlying open problem; they
restore the gap to its honest size.

```lean
-- p2-critical-exponent.lean  (one-sided: the md says q → 1⁺, and the
-- substrate regime is q > 1)
enstrophy_diverges :
  ∀ M : ℝ, ∀ ε : ℝ, 0 < ε → ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < enstrophy q

-- p5-counterexample.lean
ns_counterexample_holds :
  ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
    ∃ t x : ℝ, singularityTime - ε < t ∧ t < singularityTime ∧
               M < velocityProfile t x
```

Both witnesses above are then refuted, which is the point of making the change —
and the probe now proves that refutation rather than asserting it.

**What the fix does not reach.** `p2`'s md asserts a *power law*,
`Ω_max(q) ~ (q-1)^{-α}`. The strengthened field asserts unboundedness on every
right-neighbourhood of 1, which is what makes the conjecture non-vacuous, but
it is not the rate. So `criticalExponent` (γ_c) remains unconstrained by any
field even after this change: the class still admits any positive real as the
critical exponent. Encoding the asymptotic rate is separate, open work, and is
noted in the carrier's docstring rather than silently left to look finished.

**Blast radius.** Neither class has an instance anywhere in the tree, and the
`QOU.FluidDynamics` carriers are not the ones `ConditionalCorollaries.lean`
consumes (that module binds the same five *names* in `QOU.AlgebraicSubstrate` —
the collision is catalogued as kind B in
[`2026-08-24-divergent-duplicate-class-review.md`](2026-08-24-divergent-duplicate-class-review.md)).
So strengthening these fields cannot break a downstream proof: there is nothing
downstream that builds a witness.

---

## Also observed — `q_ns_wellposedness` prose contradicted its own code (**FIXED, same session**)

[`lean/QOU/FluidDynamics/q_ns_wellposedness.lean`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean)
carries a "Disposition (integrity)" section stating that the self-assuming
encoding was removed, that the theorem "is `sorry`'d", and that *"Nothing in
`QNsWellposednessContext` assumes any part of this conclusion."*

Measured against the file as it stands on `main` today, all three are false:

- there is **no `sorry`** in the file;
- the class carries `wellposedness_holds`, whose type is **verbatim the
  theorem's conclusion** (its own field docstring says `Missing input: global
  regularity of the q-NS system`);
- the proof is `ctx.wellposedness_holds` — a bare projection.

The defect itself is already adjudicated: `lean-vacuity-review-ledger.json`
records this declaration under `proof-no-self-assuming-projection` with verdict
`genuine`. What is not recorded is that **the file's prose denies it**, and that
the two beans tracking it (`qou-t28w`, `qou-7aj0`) both describe a `sorry` at
line 109 that no longer exists — so an agent triaging from the beans looks for
the honest disposition and finds the forbidden one.

The history is shallow-cloned here, so which encoding came first is **not
established** and is not claimed.

### Fix applied

Rather than restore the `sorry`, the file was **de-abstracted**: the single
conclusion-typed field was split by what each conjunct actually needs.

Two of the block's three properties do not require any q-NS-specific
infrastructure — given the evolution's own differential inequalities they are
Grönwall comparisons. They are now proved, in
[`q_ns_energy_and_decay.lean`](../../content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_energy_and_decay.lean):

| block property | before | after |
|---|---|---|
| existence + uniqueness | assumed (inside the monolith) | `existence_uniqueness` — **assumed**, and now visibly the only substantive input |
| (i) smoothness | assumed | `smooth_of_isSolution` — **assumed** |
| (ii) energy inequality | assumed | `q_ns_energy_inequality` — **proved** from the pointwise balance `E' + 2ν_q D ≤ 0` |
| (iii) `Δ_q`-spectral decay | assumed | `q_ns_spectral_decay` — **proved** from `d/dt|v̂_k| ≤ −ν_q [k]_q² |v̂_k|` |

Both lemmas are stated for a bare real trajectory, so they carry no q-NS
commitments and cannot reintroduce the conclusion: the hypothesis is the
pointwise *rate* statement (about the equations), the conclusion is the
*integrated* bound (what the block claims). Built on Mathlib's
`le_gronwallBound_of_liminf_deriv_right_le` and `gronwallBound_ε0`.

Verified `lean`-direct, exit 0; `#print axioms` on all five new/changed
declarations shows only `propext`, `Classical.choice`, `Quot.sound` — no
`sorryAx`. No field of the class is or implies either derived conclusion, and
`grep` finds no consumer of the removed field anywhere in `content/` or
`docs/`, so the blast radius was nil.

What is still assumed is exactly the open problem and no more: that a solution
exists, is unique, and is smooth. `qou-t28w` (tier B, infra-blocked) therefore
narrows from "the whole theorem" to "global existence, uniqueness and
regularity" — the Millennium-adjacent core, which is untouched and remains
open.
