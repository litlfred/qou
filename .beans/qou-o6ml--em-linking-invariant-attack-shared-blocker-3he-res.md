---
# qou-o6ml
title: 'EM-linking invariant ATTACK (shared blocker: 3He residual 69% + m_d-m_u extraction): trichotomy of routes — (1) higher-order Milnor/third-order-helicity integrals (pairwise lk=0 in Brunnian B3 kills first-order Gauss), (2) Mobius/knot-energy class (nonzero for unlinked pairs; corpus MobiusEnergy.lean exists), (3) h-graded per-pair Hecke trace channel at H_2A with Hochschild-homology classification of trace functionals (Solleveld 1108.5286, uploaded). GATE: must reproduce kappa(A) profile 3.2->2.1-2.3 from em-linking-invariant-scoping witness; no tuned constant (CAL-4)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-01T15:18:09Z
updated_at: 2026-08-30T14:39:21Z
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


## ROUTE (3) RESHAPED 2026-08-30 — it inherits a blocker this bean does not name, and "h-graded" misdescribes what the theorem offers

Formalize-first pass before probing, per AGENTS.md §"Formalize-first probe
discipline". Four findings; **none refutes the route**, and one of them is prior
art this bean should have linked from the start.

### 1. Prior art: `qou-siin` already worked this apparatus, and found the wall

`qou-siin` ("Pull through Solleveld") and its probe
[`computations/probes/solleveld_form_degree_vs_body_order_probe.py`](../computations/probes/solleveld_form_degree_vs_body_order_probe.py)
attacked the same Solleveld theorem for a **different target** — the body-order
series of `conj:binding-manybody-eq-jet-filtration`, not the EM per-pair weight.
Its OBSERVATION 3 is this route's blocker verbatim:

> Solleveld's theorem is about the **affine** Hecke algebra. The corpus's atom
> word lives in the **finite** `H_{3A}(q)`, which is semisimple at generic q —
> so for it the whole grading **collapses to degree 0** and none of the above
> exists. Using any of this requires the inductive limit, and
> `markov-trace-inductive-limit.lean` says of exactly that: *"The full
> operator-theoretic construction (von Neumann inductive limit on the
> infinite-dim affine Hecke algebra) is the open R&D content."*

**So route (3) is NOT the blocker-free route.** It waits on the same
inductive-limit bridge the corpus has already marked open. That is a correction
to this bean's own framing and to my ROAST entry above, which called (3) *"the
only live route with no known structural blocker"* — **retracted**; I had
grepped this bean's routes, not the apparatus they cite.

### 2. "h-graded" is not what the theorem supplies

Solleveld's Theorem 2 (introduction, p. 3): `HH_*(H(R,q^ε)) ≅ Ω^*(T̃)^W`, and

> the Hochschild homology of `H(R,q^ε)` is **independent of the parameters
> `q^ε`** and can be expressed in terms of `T` and `W`. Only the action of the
> centre depends on `q^ε`, but in a simple way.

The grading index is the **de Rham form degree** `j`, and `qou-siin`'s probe
computes its ranks as pure combinatorics — `rank HH_j = Σ_{λ⊢n} C(#parts(λ)−1, j)`
— with no `q` anywhere. So there is no grading of the trace space by powers of
`h = ℏ_q` to find: **`h` enters only through the centre's action** (the
`c_{w,i}(q)` shifts of Theorem 1.c), which is a *finite discrete datum*, not a
grading. Restate the route as "the form-degree channel, with `h` entering
through the central character" or it will be searched for the wrong object.

The `c_{w,i}` being finite and explicit is the encouraging half: it is exactly
the no-tuned-constant shape this bean's GATE demands.

### 3. On the FINITE algebra the route's search space is small, and already searched

Degree 0 is all that survives finiteness, and `HH_0` of `H_n(q)` at generic `q`
is `span{χ_λ}`, `p(n)`-dimensional — i.e. **the Frobenius pairing
`tr_M = Σ_λ y_λ χ_λ` the canonical chain already uses.** Route (3) on the finite
algebra is therefore not a new channel; it is a re-search of that span with
different `y_λ`.

And convention D cuts it much further. `deuteron_real_sdp.py:342`: *"Convention D
zeroes `y_lambda` for `ell(lambda) > 2`"* — so the live sub-space is the
**two-row** partitions only:

| A | n = 3A | p(n) | ℓ(λ) ≤ 2 | pairs C(A,2) |
|---|---|---|---|---|
| 2 | 6 | 11 | **4** | 1 |
| 3 | 9 | 30 | 5 | 3 |
| 4 | 12 | 77 | 7 | 6 |
| 6 | 18 | 385 | 10 | 15 |
| 8 | 24 | 1575 | 13 | 28 |

**Not claimed:** that ⌊3A/2⌋+1 < C(A,2) is a counting obstruction. It is not —
the trace is *evaluated* at each pair's sub-braid, so a low-dimensional space of
functionals still yields many distinct values. The dimension is a fact about the
search space, not a bound on the weights.

**What IS claimed:** the corpus has already run an SDP over exactly this space at
A = 2 (`deuteron_real_sdp.py`, H₆, 11 partitions restricted to the support) and
AGENTS.md records the outcome as a scope-(a) negative — *"the diagonal Gram SDP
is degenerate and 0 of 6 off-diagonal encodings derive the binding; the only
non-zero result (2.22456607) is the AME value fed in as the constraint
(circular)"*. So the finite-algebra reading of route (3) is not merely small, it
is **tested and empty at the one A where it has been tried**.

### 4. Convention trap, carried forward from `qou-siin`

**Solleveld's `q` is the corpus's `q²`.** His Hecke relation is
`(N_s − q(s)^{1/2})(N_s + q(s)^{-1/2}) = 0` against the corpus's
`(σ_i − q)(σ_i + q^{-1}) = 0` (AGENTS.md §7a). At the anchor,
`q_Sol = q₀² ≈ 1.23206`, **not** 1.10998. Any numeric transfer that skips this
is off by a square root.

### Where route (3) actually stands

Not refuted — scope (a) throughout, and the affine object genuinely has the
higher-degree structure the finite one lacks. But it is **gated on the
inductive-limit bridge**, and that bridge is the corpus's own open R&D item, not
a step this bean can take. Ranking (2) against (3) on "which has no blocker" was
wrong: **both** are gated on infrastructure. The difference is the *kind* —
route (2) needs an ambient metric on `KnotEmbedding` (bounded, known right
answer); route (3) needs the von Neumann inductive limit (open R&D).

**On that comparison route (2) is the cheaper front**, and I am reversing my
earlier ranking accordingly.


## ROUTE (2) — the positive half of the μ̄ prune, PROVED 2026-08-30

The prune I contributed from `qou-bn8e` (route (1)'s linear ansatz dies:
`odd_symmetric_functional_vanishes`) said what `E_EM` may **not** be. Route (2)
needs the complementary statement, and it was missing — "the map must be even"
is half an instruction.

Three lemmas added to
[`MilnorTripleLinkingMagnus.lean`](../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/MilnorTripleLinkingMagnus.lean),
`lean`-direct exit 0, sorry-free; two of them depend on **no axioms at all**.

1. **`even_functional_is_symmetric`** — an even `F` satisfies the exchange-
   symmetry hypothesis *automatically*. So evenness is not an extra condition
   route (2) must meet; it is the condition under which the symmetry is free.
2. **`even_symmetric_functional_can_be_nonzero`** — witness `F m = m²`. Without
   this the prune pair would have been consistent with *every* admissible
   functional vanishing, which would kill route (2) rather than narrow it.
3. **`exchange_symmetry_forces_agreement_on_pm_one`** — the sharper reading, and
   the one that actually constrains route (2). Exchange symmetry **alone**, with
   no parity assumption, forces `F(1) = F(−1)`.

### What (3) means for route (2), stated carefully

Since the Borromean longitude and its component-swapped partner are separated by
`μ̄₁₂₃ = 1` against `μ̄₁₂₃ = −1`, **the sign of `μ̄₁₂₃` is invisible to any
exchange-symmetric `E_EM`**: on that pair such a functional sees at most
`|μ̄₁₂₃|`. That is strictly stronger than "odd functionals vanish", which is the
special case `F(−m) = −F(m)`.

**Consequence for route (2):** the triple-linking channel can supply a
*magnitude* to the EM weight but never a *chirality*. Any construction whose EM
content is carried by the **sign** of `μ̄₁₂₃` is excluded before it is built.
Scope: (b) on sign-carrying constructions — the invariant cited is
`mubar_swap_eq_neg`, computed by `decide`, not assumed. Scope (a) on nothing
else; the magnitude channel is untouched.

This matters because it is the *same* obstruction shape as the PROBE-4 KL-
positivity prune recorded in AGENTS.md for Δ_λ — a channel that supplies
magnitude but not chirality sign. Two independent fronts, same failure mode.
Worth checking whether that is a coincidence or a common cause.

### Retracted before it was written down

I began this by arguing that the Möbius energy is even in `μ̄₁₂₃` because it is
built from distances, hence **mirror-invariant**, and `μ̄₁₂₃` negates under
mirror image. **The last step is a transformation law I was quoting from
memory and did not verify** — the Borromean rings' amphichirality points the
other way, and I could not settle it from the corpus. It is not needed: the
prune's hypothesis is *exchange* symmetry, not mirror symmetry, and a functional
of the unlabelled geometry is exchange-symmetric by construction with no
transformation law required. Recorded so the mirror route is not re-attempted
as though it had been checked. If someone does want it, the open question is the
sign of `μ̄₁₂₃` under mirror image — worth a `library/` read, not a memory.
