---
# qou-o6ml
title: 'EM-linking invariant ATTACK (shared blocker: 3He residual 69% + m_d-m_u extraction): trichotomy of routes — (1) higher-order Milnor/third-order-helicity integrals (pairwise lk=0 in Brunnian B3 kills first-order Gauss), (2) Mobius/knot-energy class (nonzero for unlinked pairs; corpus MobiusEnergy.lean exists), (3) h-graded per-pair Hecke trace channel at H_2A with Hochschild-homology classification of trace functionals (Solleveld 1108.5286, uploaded). GATE: must reproduce kappa(A) profile 3.2->2.1-2.3 from em-linking-invariant-scoping witness; no tuned constant (CAL-4)'
status: todo
type: task
priority: normal
created_at: 2026-08-01T15:18:09Z
updated_at: 2026-08-30T13:25:47Z
---

**`qou-bn8e` merged in, 2026-08-30 — with two constraints on this bean's target.**

`qou-bn8e` ("intra-nucleon EM self-energy `E_EM` is not derived") is the same
object as this bean's two-like-charge EM-linking invariant. `qou-m3vl` said so
on 2026-08-01 — *"the intra-nucleon EM self-energy is the SAME open
two-like-charge EM-linking invariant that owns the ³He mirror residual; one
invariant blocks both"* — but that conclusion lives only in
`quark-mass-extraction-stage1.witness.json`, because `qou-m3vl`'s bean body is
empty, so a `.beans/` grep cannot find it.

**Constraint 1 — the coefficient is not free; the RATIO is a theorem.**
From the cheat sheet (§3 item 2, *"a theorem, not a fit"*) plus Lean:
`[n]_q = sinh(nλ)/sinh(λ)` with **cosh = strong, sinh = Coulomb**;
`h = 2 sinh(ln q)` (`QOU.Mass.MassVolDensity.h_crossing_eq_two_sinh_log`);
`[2]_q = 2 cosh(ln q)`. Hence the Coulomb-to-strong ratio is

    h / [2]_q = tanh(ln q)   →   tanh(ln q₀) = 0.10396371005241013891

derived, parameter-free. `quark-mass-extraction-stage1` independently names the
framework's only derived EM mechanism as **`tanh(ln q₀) × strong bond`**, and
`QOU.MassTheory.EmGermMomentVanishing.emMoment` (`−h/[2]_q`, reached from germ
curvature) is **algebraically identical** to `−tanh(ln q₀)` (checked to 3.3e-52
at 50 dps). So what this bean owes is **the bond `tanh(ln q₀)` multiplies**, not
a free coupling.

**Constraint 2 — `wᵢⱼ` must be EVEN in `μ̄₁₂₃`, which prunes route (1).**
Two proved facts compose:

* `mirror_split_s3_em_functional_probe.py` **(A3)**: for L6a4 (the Borromean
  link) every pairwise `lk_ij = 0`, so any nonzero `wᵢⱼ` is mediated by
  `μ̄(123)`, the triple channel.
* `QOU.BraidsAndKnots.MilnorTripleLinkingMagnus.odd_symmetric_functional_vanishes`
  (sorry-free): an **odd** `F` agreeing on the Borromean and swapped longitudes
  vanishes — hypothesis: exchange-symmetry of a two-like-charge Coulomb
  self-energy. Companion `linear_coefficient_must_vanish`: `E_EM = c·μ̄₁₂₃`
  forces `c = 0`.

⟹ **`wᵢⱼ` depends on `μ̄₁₂₃` evenly** (`μ̄²`, `|μ̄|`), never linearly. This bean's
route **(1)** (higher-order Milnor / third-order helicity) should not spend a
pass on a linear-in-`μ̄` ansatz; it is already excluded.

**What did NOT merge.** `bn8e`'s **self**-term question (`A·Σqᵢ²`). Probe axiom
(A1) derives `a = 0` for **binding energy** (`B = Z·m_p + N·m_n − M`) because
single-component self-energy lives in `m_p`, `m_n` — but `m_n − m_p` is a
difference of **free** masses, not a binding energy, so A1 does not touch it.
That stays in `bn8e`; this bean owns only the pairwise/linking channel.

Note `qou-17mq` (O2 neutrality obstruction) still reshapes this bean's
*statement*, independently of the above.


## ROAST 2026-08-30 — route (2)'s corpus asset does not exist; the route is untouched

Four defects in `content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean`,
the file this bean cites as *"corpus MobiusEnergy.lean exists"*. All four are
**machine-verified against the committed declarations** (lean-direct, exit 0,
`#print axioms` clean), and all four were invisible to every detector: none
carries a `sorry`, an `axiom`, or a tautological *conclusion*, and a library
`.lean` has no `.qa.json` sidecar.

**1. `NonSelfIntersection M` was UNINHABITABLE for every `M`.** Its
`energyDivergence` field read `∀ E₀ : ℝ, ∃ ε : ℝ, ε > 0 ∧ (∀ _s _t : ℝ,
cme.energy > E₀)`. The `_s _t` binders are unused, so the inner `∀` is a
constant and the field reduces to `∀ E₀, cme.energy > E₀`. Instantiate at
`E₀ := cme.energy`. Proved: `IsEmpty (NonSelfIntersection M)`. So the entire
"quantum exclusion zone / knot-theoretic Pauli principle" corollary — the part
of this file route (2) actually wants — was **vacuous**, not weak.

**2. `qRepulsionKernel_singular` concluded the kernel is ZERO** at the radius
its own name and docstring call a divergence, by `div_zero` — Lean's `x/0 = 0`
junk value. Name said singular, docstring said "diverges at `r = ℏ_q`",
statement said `= 0`.

**3. `ClassicalMobiusEnergy.unknot_iff` read `value = 4 ↔ True`.** `P ↔ True`
is `P`, so it forced `value = 4` for *every* instance (`c.unknot_iff.mpr
trivial : c.value = 4`). That is not a weakened Freedman–He–Wang; it is the
negation of its content — it makes the classical Möbius energy blind to the
knot.

**4. Consequence, proved: `E_cat = 1 + const` for every knot.** Through
`CategoricalMobiusEnergy.classicalLimit` the categorical energy inherits the
blindness. A knot-energy route needs a functional that *separates* knots; this
encoding provably does not.

Worth naming the near-miss: bean `qou-u87j` inspected this file and cited
`unknot_iff`'s presence as evidence the library encoding was **stronger** than
its content-block sibling. The field was seen and not read. `qou-lo1t` repaired
the *projection* defect in the same file (batch 4, via the Möbius orbit) and
left these four. Fixed 2026-08-30 in this branch.

### What this does NOT say

The route is **not** refuted — scope (a), and narrowly: it is a negative about
an encoding, not about knot energy. Two things point the other way:

- **The literature Möbius/O'Hara energy is exactly the shape `qou-17mq`'s O2
  obstruction demands.** Its integrand is `1/|γ(s)−γ(t)|² − 1/D(γ(s),γ(t))²`
  — **subtracted by construction**. 17mq excluded the unsubtracted `coth`
  kernel because an admissible pair kernel must be zero-mean; a functional
  whose regularising subtraction is intrinsic is not vulnerable to that
  argument. So O2 is a reason to prefer route (2) over route (1)'s kernel,
  not a reason to drop it.
- The `-- Ref: [freedman1994]` and `[ohara1991]` citations are real and the
  classical object is standard.

### The concrete blocker, and it is a missing primitive not a missing proof

`KnotEmbedding` carries `curve : ℝ → M`, `arcLengthDist : ℝ → ℝ → ℝ` and two
symmetry/non-negativity fields. **There is no ambient distance on `M`.** So
the Möbius integrand — which is a function of `|γ(s) − γ(t)|`, the *ambient*
separation, minus the intrinsic one — **cannot be written in this encoding at
all**. That is also why defect 1 had no proximity hypothesis to condition on:
there was nothing to condition on. The fix carries a `separation` field on
`NonSelfIntersection` as a stopgap and says so.

**Next for route (2), in order:** (i) give `KnotEmbedding` an ambient metric
(or land it on a `MetricSpace M`); (ii) write the O'Hara integrand with its
intrinsic subtraction; (iii) only then ask whether it reproduces `κ(A)`. Steps
(i)–(ii) are infrastructure with a known right answer, not research — which
makes route (2) cheaper than it looks, but not yet startable.

**Route (3) (h-graded Hecke trace channel) is untouched by all of this** and is
now the only live route with no known structural blocker.
