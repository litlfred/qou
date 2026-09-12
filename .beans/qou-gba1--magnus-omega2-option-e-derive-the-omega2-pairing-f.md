---
# qou-gba1
title: 'Magnus Omega2 option E: derive the Omega2 pairing from what Omega2 is'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T11:44:24Z
updated_at: 2026-09-12T12:23:09Z
---

# The only option that ANSWERS the question rather than choosing

Derive the correct contraction from what Ω₂ is, instead of picking a weight
family and defending it.

## For

Ω₂ = ½ Σ_{i<j} [A_i, A_j] is a curvature-like object built from germs
`A_g = q(∂_q σ_g)σ_g⁻¹`. The right pairing should fall out of whatever
variational principle produces a binding energy — and if it does, it settles the
row-cap objection to option A **on principle** rather than by convention, which
no other option can do.

## Against

Open-ended research with no bounded cost. The arc already has a usable sign
result, and the sign does not depend on the choice, so this blocks nothing.

## Work

- [ ] Identify the functional whose stationarity gives the binding correction.
- [ ] Read off the induced pairing on `H_n(q)` and compare with both families.
- [ ] Should NOT block option A; if it lands, it supersedes whichever was chosen.

Option from the decision analysis in [`docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md`](../docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md).
Parent question: `qou-za3q`. Sibling options: `qou-q2q7` (A), `qou-94yt` (B),
`qou-smvw` (C), `qou-ia4w` (D), `qou-gba1` (E).

**Shared measured context** (none of this is fitted):

- `tr(1) = Σ_λ w(λ)·d_λ` — Wenzl gives exactly **1.0** at n = 6, 9, 12;
  Plancherel gives **11.139 / 184.233 / 6751.541**. Plancherel is not a
  normalised trace and its scale grows ~600× from A=2 to A=4.
- Plancherel puts **81.8 %** of its H₆ mass on ≥3-row shapes; the Wenzl row cap
  (level r = 2, `qou-fq0f`) puts **0 %** there. **62.4 %** of the Plancherel
  |contribution| at A=2 comes from shapes Wenzl annihilates.
- The **sign is robust**: P_total < 0 under both, on all three atoms — and not
  trivially, since the per-λ traces are mixed-sign (+4/−5, +13/−15, +26/−49).
- **Magnitude is not robust** and not monotone: deuteron −15.1 → −6.9, triton
  −108.1 → −60.0, but ⁴He −57.8 → **−100.8**.
- The probes' stated control (`ρ=I ⇒ tr(Ω₂)=0`) holds **blockwise** — every
  per-λ control trace is exactly 0 — so it is weight-blind and provides no
  evidence either way.

No published conclusion depends on the choice, so this is a correctness-of-object
question, not an emergency.


## 🟧 PROMOTED 2026-09-12 by owner ruling — this is now the live route

Owner, verbatim: *"qou-za3q formalize and derive first.  probably adopt wenzl"*.

Option E (this bean) is the **derive** half and is now the priority. The
Formalize-first policy applies in full: Lean structure before any Python.

**The target.** Derive the Omega2 pairing weight family from the
characterisation of the Markov trace, with the Markov parameter already fixed:

    (i)   cyclicity            tr(ab) = tr(ba)
    (ii)  Markov property     tr_{n+1}(x sigma_n) = z * tr_n(x),  x in H_n
    (iii) normalisation       tr(1) = 1
    (iv)  z = z_D = q^3/(q^2+1)   ALREADY FIXED (owner ruling 2026-08-15, R1)

If (i)-(iv) force the family, the pairing is derived from a ruling the corpus
already holds rather than chosen, and `qou-q2q7`'s Wenzl adoption becomes a
conclusion instead of a premise. That is the whole point of doing it this way.

**What the existing evidence can and cannot do.** The probes' `rho = I` control
is **weight-blind**: `tr(Omega2_lambda) = 0` for each lambda separately by
cyclicity, so `Sum_lambda w(lambda) * 0 = 0` for ANY `w`. It tests cyclicity and
says nothing about the weight. Two facts do bear on it, both already measured:
Wenzl's `tr(1)` is exactly `1.0` at n = 6, 9, 12, and the Plancherel measure
gives `11.139 / 184.233 / 6751.541`, failing (iii) and drifting ~600x across A.

**NOT yet claimed:** that (i)-(iv) are jointly sufficient, or that the forced
family is the row-capped Wenzl one. Both are to be proved. Classical
Markov-trace uniqueness is Jones/Ocneanu, so part of this may be a CITATION
rather than a derivation — a corpus-grep is establishing which, because
re-deriving a held result would be waste and passing a citation off as a
derivation would be worse.


## 🟩 ALREADY PROVED — 2026-09-12. Cite it; do NOT re-derive. And two of my own framings were WRONG.

Corpus-grep (all six paths) before writing any Lean, per formalize-first. The
derivation this bean was promoted to perform **already exists in the corpus,
sorry-free**, and the classical source is held too. Verified from the primary
files, not from the agent report.

### The citation

`QOU.SchurWeyl.HeckeCoset.markovTrace_unique` —
`content/quantum-observable-universe/lean/QOU/SchurWeyl/MarkovTraceUnique.lean:103`

    theorem markovTrace_unique (T S : MarkovTraceFamily K q qi z) :
        ∀ (n : ℕ) (x : Hecke K q qi n), T.tr n x = S.tr n x

`QOU.SchurWeyl.SeminormalRep.eq_wtrace_of_markov` —
`.../QOU/SchurWeyl/MarkovTraceInstance.lean:191`, which carries **z_D in its
own type** and proves *every* Markov trace at that parameter is the
Ocneanu-weighted seminormal trace:

    theorem eq_wtrace_of_markov (q : ℝ) (hq0 : q ≠ 0) … 
        (T : HeckeCoset.MarkovTraceFamily ℝ q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
        (n : ℕ) (x : Hecke ℝ q q⁻¹ n) : T.tr n x = wtrace q hq0 hq2 n x :=
      HeckeCoset.markovTrace_unique T (ocneanuMarkovTrace q hq0 hq2 hq21 hgen) n x

and `wtrace` IS the Frobenius decomposition,
`Σ_ν ocneanuWeight q (q^3/(q^2+1)) ν · (seminormalRep … ν x).trace`.

**Classical source HELD:** Chlouveraki HDR **Theorem 6.20**,
`library/hdr/sections/sec-025-knot-invariants.md` lines 24-37, key
`[chlouveraki2016-hdr]`. Quoted verbatim from the file: *"There exists a unique
linear Markov trace … (1) tr(ab) = tr(ba) (2) tr(1) = 1 (3) tr(ag_n) = z tr(a)
(Markov property) … **For d = 1** … it is the Ocneanu trace on the
Iwahori-Hecke algebra H_n(q) ≅ Y_{1,n}(q)."* So this is a **citation**, not a
derivation — which is exactly what the grep was for.

Level-r sibling, if wanted: `eq_wenzlWtrace_of_markov`,
`.../WenzlMarkovTraceInstance.lean:249`.

### 🛑 CORRECTION 1 — my hypothesis set was INCOMPLETE

I wrote the target as four conditions: cyclicity, Markov property, tr(1)=1, and
z fixed. **That is not what is proved.** Read from the structure
(`MarkovTraceUnique.lean:75-81`), it is **five**:

    tr        : (n : ℕ) → Hecke K q qi n →ₗ[K] K      ← LINEAR, not any function
    tr_one    : ∀ n, tr n 1 = 1
    tr_cyclic : ∀ n x y, tr n (x * y) = tr n (y * x)
    tr_incl   : ∀ n x, tr (n+1) (heckeIncl … x) = tr n x   ← TOWER CONSISTENCY
    tr_markov : ∀ n x, tr (n+1) (heckeIncl … x * σ …) = z * tr n x

**`tr_incl` is the one I missed**, and linearity I did not state at all. The
file says the induction uses all four Prop fields and dropping any one breaks
it. HDR carries the consistency implicitly — its trace is *"defined
inductively"* on the union — so the Lean encoding is faithful; my *statement*
of it was not. Anyone citing this must say **five**.

### 🛑 CORRECTION 2 — "Plancherel is not a Markov trace" is WRONG

I wrote that the Plancherel measure fails normalisation and is therefore not a
normalised trace. The sharper and correct statement: **it IS a Markov trace —
at z = 0.**

Two independent carriers agree. `q_plancherel_vs_y_lambda_probe.py` computes
`z = tr(σ₁) = y_(2)·q + y_(1,1)·(−q⁻¹)` for the q-Plancherel weights and gets
**exactly 0, symbolically, for every q**, because that measure decomposes the
REGULAR trace and `τ_q(T_σ) = 0` for σ ≠ id. And HDR **Remark 6.21**, one line
below Thm 6.20: *"The canonical symmetrising form … coincides with the Markov
trace with parameters z = x₁ = ⋯ = 0."*

This is **stronger** than what I claimed, not weaker: Plancherel is not a
malformed trace, it is the *right kind of object at the wrong parameter*. So
uniqueness at z_D excludes it with no extra argument — the exclusion follows
from the convention-D ruling alone.

### What this means for the arc

Chain, every link already held:

    owner ruling 2026-08-15 (R1)  fixes  z = z_D = q³/(q²+1)
    eq_wtrace_of_markov (sorry-free)  ⇒  the Markov trace at z_D IS the
                                         Ocneanu/Wenzl weight family
    ⇒ the Ω₂ pairing's weight family is FORCED, not chosen

So `qou-q2q7`'s Wenzl adoption is now a **derived conclusion**, and the owner's
*"probably"* is discharged. The Plancherel arm the probes aggregate with is the
z = 0 trace — i.e. the wrong parameter for a corpus committed to convention D.

### Scope — what is NOT settled

* The Ω₂ pairing is `tr_M(ρ·Ω₂)`, the Markov trace evaluated at an algebra
  element. The uniqueness fixes the *weights*; it says nothing about whether
  `ρ·Ω₂` is the right element, which is a separate question.
* Two uniqueness questions exist and neither implies the other (`qou-4a68`):
  *trace given parameter* (= this) and *level given parameter*
  (`level_unique_of_markovParameter`). Do not cite one for the other.
* HDR proves it for `z` an **indeterminate** over C(q); the corpus wants the
  **specialised** value z_D. The Lean proves the specialised case outright, so
  nothing is missing — but they are formally distinct statements.
* ~~**No fresh `lean`-direct run.**~~ **DISCHARGED 2026-09-12 — see
  §DISCHARGED at the foot of this bean.** Both declarations have since been
  rebuilt from source (`lean-library-sweep.py`, 95 ok / 0 RED) and their axioms
  re-measured sorry-free. Superseded text: *the lean-lsp MCP failed to connect
  this session; I verified the declarations and the structure by reading the
  files; the exit-0 / `#print axioms` record is `qou-4a68` (2026-08-24,
  PR #5705), quoted as a dated record, NOT re-measured.*
* Genericity `q²` not-a-root-of-unity is **vacuous over ℝ** beyond `q² ≠ 1`
  (`qou-4a68`), so `q₀` is in scope.

### 🛑 DECOYS — three declarations that look like the answer and are not

A name-grep in `content/**` finds these first. Do not cite any of them:

* `wenzl_bridge_unique_definitional` / `_categorical` / `wenzl_bridge_unique`
  (`y-lambda-closed-form-wenzl-bridge.lean:241,272,293`) — all three conclude
  the same `wenzlQ q = q^2 ∧ wenzlZ q = q * jonesMarkovZ q` and all three are
  `refine ⟨rfl, rfl⟩`. About the *convention shift*, not the weights.
* `y_lambda_unique_in_qou` (`wenzl-bridge-applicability-qou.lean:126`) — its
  conclusion is verbatim the `unique` field of the class it takes as a
  hypothesis, discharged by `exact U.unique …`. The §3b-cond rule-5
  self-assuming projection. That class's `unique : True`, and **no instance of
  it exists anywhere**.

The real theorem sits in a **library** file with no `.qa.json` sidecar, and
`thm:markov-trace-unique` appears in no `.md`/`.ts` block — which is exactly
why a content-tree grep returns the decoys and misses it.

### Fixed on the way

`jonesMarkovZ`'s docstring read `z = 1/(q^(1/2) + q^(-1/2))` — convention **C**
— above a body computing `q^3/(q^2+1)`, convention **D**. Name and docstring
agreed with each other and both disagreed with the body; only the body was
right. Corrected.


---

## 🟩 DERIVED AND VERIFIED 2026-09-12 — the control is weight-BLIND, proved

Two additions to
`content/quantum-observable-universe/lean/QOU/MassTheory/MagnusCurvatureCommutator.lean`
(a **library** file — no `.qa.json` sidecar, so nothing but the agent checks it):

```lean
theorem trace_commSum_eq_zero (tr : A →ₗ[R] R)
    (hcyc : ∀ x y : A, tr (x * y) = tr (y * x)) (σ : ℕ → A) (m : ℕ) :
    tr (commSum σ m) = 0

theorem trace_commSum_indep_of_cyclic (tr₁ tr₂ : A →ₗ[R] R)
    (h₁ : ∀ x y : A, tr₁ (x * y) = tr₁ (y * x))
    (h₂ : ∀ x y : A, tr₂ (x * y) = tr₂ (y * x)) (σ : ℕ → A) (m : ℕ) :
    tr₁ (commSum σ m) = tr₂ (commSum σ m)
```

Both generic over `{R} [CommRing R] {A} [Ring A] [Algebra R A]` (§7c — no `ℝ`,
no ordering, no `Real.sqrt`). The first is `ρ = 1` in the pre-existing
`trace_mul_commSum_eq_zero_of_commute`; the second is two applications of it.

### What it establishes, and why it is the thing worth proving here

The three Magnus-Ω₂ sign probes each report a `ρ = I` control confirming
`tr(Ω₂) = 0`, and read it — correctly — as *"any nonzero sign REQUIRES the
density"*. **`trace_commSum_indep_of_cyclic` refutes the tempting next step**:
a passing control is NOT evidence that the aggregation measure is the right one.
It passes for the quantum Plancherel weight, for the Ocneanu/Wenzl family, and
for **any** cyclic linear functional whatever — including ones nobody would
propose. So decision 1 of `qou-za3q` cannot be settled on the control's
strength, from either side.

Scope, precisely: this says the control cannot **discriminate**. It does not say
the control is worthless — a control that *failed* would mean the germ or the
trace was broken, which is exactly how the probes use it.

What fixes the weight family is therefore the Markov-trace characterisation
recorded above, and nothing else on the probe side.

### Verification — fresh this session, not a quoted record

`scripts/lean-library-sweep.py` (library file ⇒ not `lean-content-sweep.sh`;
not bare `lean`-direct, which is snapshot-conditional per `qou-56qy`):

* `--all --only-exact QOU.MassTheory.MagnusCurvatureCommutator` → **1 ok, 0 RED**, 7 s.
* `#print axioms` on both new theorems →
  `[propext, Classical.choice, Quot.sound]`. **No `sorryAx`.**
* `lean` invoked with `-DautoImplicit=false -s 65536` throughout, per `qou-56qy`
  — a bare `lean` is a strictly weaker check than the lakefile's options.

### The "No fresh `lean`-direct run" caveat above is now DISCHARGED

That scope item said the two cited uniqueness declarations were verified by
*reading*, with the exit-0 record quoted from `qou-4a68` (2026-08-24). Both have
now been **rebuilt from source** and re-measured:

`lean-library-sweep.py --package QOU --only QOU.SchurWeyl.MarkovTrace` →
**95 ok, 0 RED, 0 TIMEOUT, 0 skipped**, 296 s. Both `QOU.SchurWeyl.MarkovTraceUnique`
and `QOU.SchurWeyl.MarkovTraceInstance` were in the dirty closure and were
rebuilt (confirmed by the absence of a hardlinked `.olean.hash` beside them in
the shadow, which the snapshot copies carry). `#print axioms` against those
freshly-built oleans:

* `QOU.SchurWeyl.HeckeCoset.markovTrace_unique` → `[propext, Classical.choice, Quot.sound]`
* `QOU.SchurWeyl.SeminormalRep.eq_wtrace_of_markov` → `[propext, Classical.choice, Quot.sound]`

So the forcing argument rests on a **re-measured** sorry-free pair, not on a
three-week-old record. Every other scope item above stands unchanged.
