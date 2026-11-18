---
# qou-o6ml
title: 'EM-linking invariant ATTACK (shared blocker: 3He residual 69% + m_d-m_u extraction): trichotomy of routes — (1) higher-order Milnor/third-order-helicity integrals (pairwise lk=0 in Brunnian B3 kills first-order Gauss), (2) Mobius/knot-energy class (nonzero for unlinked pairs; corpus MobiusEnergy.lean exists), (3) h-graded per-pair Hecke trace channel at H_2A with Hochschild-homology classification of trace functionals (Solleveld 1108.5286, uploaded). GATE: must reproduce kappa(A) profile 3.2->2.1-2.3 from em-linking-invariant-scoping witness; no tuned constant (CAL-4)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T15:18:09Z
updated_at: 2026-10-04T15:12:27Z
parent: qou-5vkl
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

Four defects in `folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean`,
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


## ROUTE (1) [was mis-headed ROUTE (2)] — the positive half of the μ̄ prune, PROVED 2026-08-30

> **Heading corrected 2026-09-14.** This read *"ROUTE (2)"* and the body says "route (2)" throughout. **The object is route (1)'s.** These three lemmas live in `MilnorTripleLinkingMagnus.lean` and constrain functionals of `μ̄₁₂₃`, a Milnor invariant — route (1)'s apparatus. Route (2) is the Möbius/knot-energy class, whose object is a conformally-invariant integral, not a Milnor invariant. The misfiling made route (1) read as pruned-and-abandoned while its **positive half was credited to a different route**, which is how a live branch goes missing. Body text left as written (it is the dated record); only the heading and this note are new.

The prune I contributed from `qou-bn8e` (route (1)'s linear ansatz dies:
`odd_symmetric_functional_vanishes`) said what `E_EM` may **not** be. Route (2)
needs the complementary statement, and it was missing — "the map must be even"
is half an instruction.

Three lemmas added to
[`MilnorTripleLinkingMagnus.lean`](../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MilnorTripleLinkingMagnus.lean),
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


## SCOPE AUDIT of the chirality obstruction, same day — it is REAL but INERT for this bean's target

Immediately after recording `exchange_symmetry_forces_agreement_on_pm_one` above
I checked the one thing that decides whether it constrains 4-B at all: **does the
`κ(A)` target need a sign?**

Measured, from the committed witnesses rather than from the beans:

| source | statistic | value |
|---|---|---|
| `em-linking-mirror-series.witness.json` | 31 `κ` values | min **1.4020251**, max **3.2135068** |
| — | any negative | **no** |
| — | any zero | **no** |
| `em-linking-invariant-scoping.witness.json` | `kappa_min` / `kappa_max` | 2.1057468712 / 3.21350728299 |
| — | `kappa_a3` / `kappa_high_A_mean` | 3.21350728299 / 2.24616992054 |

(The two series are different populations and must not be conflated — the
scoping one is the `3.2 → 2.1–2.3` profile this bean's GATE names, and its
`kappa_a3` / `kappa_high_A_mean` reproduce that profile exactly. The mirror
series runs lower, to 1.40. **Both are strictly positive throughout.**)

**So the target is single-signed, and a channel that cannot carry a chirality
loses nothing it was being asked for.** The obstruction I proved this morning
stands as stated — it *is* a scope-(b) exclusion of sign-carrying constructions
— but it does **not** narrow route (2)'s access to `κ(A)`. Recorded because a
(b)-scope exclusion left in the corpus without this check reads as a live
constraint on the front, and it is not one. That is the over-narrowing failure
AGENTS.md §"Before declaring refuted" exists to prevent, and I nearly committed
it against my own result.

### Two places it still bites, so it is not merely decorative

1. **Signed intermediates.** The endpoint being positive does not make the
   *construction* sign-free. The ³He mirror residual is a **difference**, and
   `E_EM = Σ_{i<j} q_i q_j w_ij` carries signed charge products for p–n pairs.
   Any route through such an intermediate is still subject to the theorem;
   only the two-like-charge sector is manifestly positive.
2. **The inversion, which is the useful reading.** Since the channel cannot
   supply a sign, **`κ`'s uniform positivity across all 31 measured points is
   not explained by the μ̄₁₂₃ channel.** It has to be automatic, or come from
   elsewhere. That is a real question this bean did not previously have: *what
   makes κ > 1 everywhere?* — and it is now known that the answer is not in the
   triple-linking sign.

**Net:** route (2)'s ranking is unchanged; the obstruction narrows *how* it may
be built, not *whether* it can reach the target.


## ROUTE (2) UNBLOCKED 2026-08-30 — the O'Hara integrand is now writable, and its positivity is derived

The blocker recorded in this bean's ROAST — *"`KnotEmbedding` has `arcLengthDist`
and **no ambient distance**, so the Möbius integrand cannot be written at all"* —
is closed. `lean`-direct exit 0, sorry-free.

`QOU.KnotEmbedding` gains four fields: `ambientDist`, `ambient_symm`,
`ambient_nonneg`, and **`chord_le_arc : ∀ s t, ambientDist s t ≤ arcLengthDist s t`**.
Carried as fields rather than taken from a `MetricSpace M` instance, matching how
`arcLengthDist` was already carried — `M` is the fibre of the realisation functor
and the rest of the file keeps it a bare `Type*`, so a metric instance would
constrain every use site for one definition. Safe to extend: `KnotEmbedding`
has exactly **one** use in the tree (the `knot` field of
`CategoricalMobiusEnergy`) and **no constructor anywhere**, so no call site
breaks. (`genus_from_hecke_completeness.lean` matches a grep for the name only
through the unrelated `torusKnotEmbeddingCount`.)

Then:

- **`oharaIntegrand`** — `1/|γ(s)−γ(t)|² − 1/D(s,t)²`, the actual O'Hara/Möbius
  integrand, definable for the first time.
- **`oharaIntegrand_nonneg`** — pointwise non-negative off the diagonal,
  **derived from `chord_le_arc`**, not assumed.
- **`oharaIntegrand_symm`** — symmetric in `(s,t)`, from the two distance
  symmetries.

### Why the positivity lemma is worth more than it looks

`ClassicalMobiusEnergy.nonneg` is a structure **field** — the positivity of the
energy is *carried as a hypothesis*, because that structure had no integrand to
derive it from. `oharaIntegrand_nonneg` supplies the pointwise half of the
derivation. Stated honestly in the docstring: the remaining step is that the
integral of a non-negative function is non-negative, which needs integration
theory this file does not set up. So this **does not** discharge the field yet —
it reduces an assumption to one standard missing step, which is a different and
weaker claim than closing it.

### And it is the structural reason route (2) survives O2

The subtracted term is not decoration. `qou-17mq`'s O2 obstruction excludes pair
kernels that are not zero-mean; `oharaIntegrand`'s regularisation is **intrinsic
to its definition** rather than imposed by hand, so the argument that excluded
route (1)'s unsubtracted `coth` has nothing to bite on here. That was recorded
above as a literature fact; it is now a fact about a definition in this corpus.

### What is still needed before the GATE can be attempted

Writing the integrand is not evaluating it. Reproducing `κ(A)` needs actual
geometric embeddings of the nuclear links, and `qou-17mq` finding 3 established
that **no per-isotope hyperbolic geometry beyond A = 3 exists** in the corpus
(`binding-link-volumes.witness.json` holds A = 2 and 3 only). So the next
blocker on route (2) is *data*, not formalisation — and it is the same data gap
that stopped the kernel contest from being adjudicable.


## SCOPING THE DATA GAP 2026-08-30 — two corrections, one of them to my own last entry

I closed the previous entry saying the next step was to *"scope what it would
take to get per-isotope link geometry past A = 3"*, on the grounds that it is
the shared blocker. Scoped it. **Both halves of that framing were wrong**, and
the second is the useful one.

### Correction 1 — the volume endomorphism has ZERO supporting rows, not one

`computations/binding-link-volumes.witness.json` records
`B = m_e · Vol(K_bind) · Δtr` against AME:

| isotope | link | Vol | vol_eff used | err |
|---|---|---|---|---|
| ²H | Hopf (L2a1) | **0** (Seifert-fibred) | **7.3277** (= Vol(𝓑₃) = 8G) | −6.32 % |
| ³H | 8₁₁ | 8.2863 | 8.2863 | −55.64 % |
| ³He | L6a4 | 7.3277 | 7.3277 | −56.68 % |

The producer is scrupulous about this — the substitution is labelled at every
appearance (`binding_link_volumes.py:150`, `v_eff = v if
vols[iso]["hyperbolic"] else VOL_B3`), the docstring calls it *"the Hopf →
Vol(𝓑₃) substitution, since Vol(Hopf) = 0"*, and the file even carries the
**Lean-backed** fact that the vanishing is identical rather than numerical
(`QOU.Knot.FlatTet.BlochWigner_lob_ofReal`). Nothing is hidden.

**What changed is the ruling, not the code.** Owner Ruling A —
*"the deuteron binding is **NOT** a hyperbolic-volume term (Bloch volume leg
proved 0)"* — landed in
`docs/audits/2026-08-29-deuteron-knot-owner-decision.md` at **2026-08-30
02:29:49 UTC**. The producer was last touched at **2026-08-29 17:32 UTC**, ~9 h
earlier. It could not have known, and this is staleness created downstream, not
an authoring defect.

But the consequence is real: under the ruling, the ²H row assigns the deuteron a
hyperbolic volume it does not have, so **the −6.32 % is not a result about the
deuteron.** The endomorphism's score is therefore **0 supporting rows out of 3**,
not 1-of-3. That strengthens the producer's own "HONEST NEGATIVE" rather than
contradicting it — and the witness has **8 consumers** (`he4_vol4_prediction_test_probe`,
`alpha_cluster_volume_additivity_probe`, `bk_crossing_coordination`,
`theta_wn_jetfilt_linkvolume`, `theta_mn_multiplicity`,
`binding_volume_difference_probe`, `he4_link_volume_braid_closure`, and the
producer), so the 1-of-3 reading can propagate.

### Correction 2 — closing the volume gap would NOT unblock route (2), and my last entry implied it would

Route (2) does not want *a single binding-link volume*; it wants the **pairwise**
O'Hara energy, which is a double integral decomposed over component pairs. Those
are different objects and they need different data:

- the volume route needs **one hyperbolic volume per isotope** — a number per A;
- route (2) needs **ambient pairwise distances along the components** — an
  *embedding* per isotope, from which the integrand
  `1/|γ(s)−γ(t)|² − 1/D(s,t)²` is evaluated.

**So route (2)'s data requirement is strictly larger than the volume gap, not a
subset of it.** Getting `Vol` past A = 3 would not help it at all. I stated the
opposite last entry; that is retracted.

### The one genuinely encouraging thing, and it is in the producer's own text

`binding_link_volumes.py` names what the failure needs:

> closing A ≥ 3 needs additional structure (**per-pair sum over the JSJ
> decomposition**, or a different trace object) — NOT a rescaling of Δtr by
> hand-chosen factors (cf. retracted PR #1383).

**A per-pair sum is exactly what route (2) is.** So the witness that records the
single-volume negative also names route (2)'s shape as the structure that would
close it. That is a corpus endorsement written before this front was framed, and
it was not previously connected to 4-B.

**Net for the front:** route (2) is the right *shape* by the corpus's own
reckoning and is now formalisable, but its data requirement is an embedding per
isotope, which nothing in the corpus supplies at any A. That is the real blocker
and it should be stated at that size rather than as "geometry past A = 3".


## 2026-08-31 — THE DATA BLOCKER IS MUCH WEAKER THAN I STATED, and my own integrand was the wrong term

I closed the previous entry saying route (2) *"needs an embedding per isotope,
which nothing in the corpus supplies at **any** A"*, and offered as next steps
(a) find such embeddings or (b) ask whether the energy is computable from link
invariants alone. Took (b). The answer reshapes the blocker and corrects the
Lean I added yesterday.

### 1. Route (2) wants the MUTUAL term, and I formalised the SELF term

`oharaIntegrand` — `1/|γ(s)−γ(t)|² − 1/D(s,t)²` — is the **self**-energy of one
curve, and its subtraction exists to tame the diagonal singularity as `t → s`.
That is not what a per-pair EM weight is.

For two **distinct** components the subtracted term is `1/D(s,t)²` with `D` the
arc-length distance *along the curve*, and between different components **there
is no path along the curve at all**, so `D = ∞` and the term vanishes
identically. The mutual energy is the **unsubtracted** integral
`∫∫ 1/|γ_i(s) − γ_j(t)|²`, and the regularisation question does not arise:
distinct components are disjoint, so there is no diagonal to be singular on.

Formalised (`lean`-direct exit 0):

- **`mutualIntegrand`** — the unsubtracted cross-integrand.
- **`mutualIntegrand_pos`** — strictly positive wherever the components do not
  touch, **with no hypothesis beyond that**. Contrast `oharaIntegrand_nonneg`,
  which needs `chord_le_arc` and yields only `0 ≤`. Unconditional positivity is
  exactly what this bean asks of route (2) — *"nonzero for unlinked pairs"* —
  and on the Borromean carrier every pairwise `lk_ij = 0` ((A3) of
  `mirror_split_s3_em_functional_probe.py`), so a linking-number weight vanishes
  there while this one cannot.
- **`mutualIntegrand_eq_ohara_without_subtraction`** — the algebraic identity
  that makes the two comparable, so the relationship is in the file rather than
  in a docstring.

### 2. So the data requirement is a MINIMISATION ON THREE NAMED LINKS, not nuclear geometry

The mutual integrand is scale-invariant (length²/length², dimensionless) and
Möbius-invariant, and the **minimum of the energy over an isotopy class is an
invariant of the link type** — that is the content of Freedman–He–Wang, whose
`E(unknot) = 4` this file already cites. So route (2) does **not** need the
actual configuration of a nucleus. It needs the energy-minimising embedding of
each *named carrier link* — and the carriers are named: Hopf (L2a1), 8₁₁,
L6a4/Borromean.

**That drops the blocker from "per-isotope geometry the corpus has at no A" to
"run an energy minimisation on three links whose types are already fixed."**
Retracting the previous entry's framing accordingly.

**What is NOT claimed:** that there is a closed form from link invariants. There
is not — the energy of a knot type is defined by a minimisation and is computed
numerically by gradient flow, not read off a polynomial. So this is a *tractable
computation*, not a formula, and it is still work.

### 3. The real remaining gap, correctly sized

`KnotEmbedding` carries a single `curve : ℝ → M` and **cannot express a
multi-component link at all**. That is why `mutualIntegrand` is stated over a
bare separation function rather than through the structure. A multi-component
carrier is the next formalisation step, and it is bounded.

### 4. Acquisition gap

`freedman1994` and `ohara1991` are both registered in
`content/schema/references.ts` and **neither appears in `library/INDEX.md`** —
the corpus cites them and does not hold them. Same shape as `qou-bn8e`'s
Cottingham gap. Anyone taking route (2) forward should drop both into
`uploads/` and migrate, because the minimiser values and the link-energy
conventions are in those papers and are being reasoned about from structure
here.


## 2026-08-31 — `LinkEmbedding`: the mutual term now goes THROUGH the encoding, and its positivity is free

The last formalisation step named in the previous entry. `lean`-direct exit 0;
`#print axioms` clean on all four new results.

**`LinkEmbedding M n`** — `n` components, each a `KnotEmbedding`, plus a
link-level `sep i s j t` giving the ambient distance between a point on
component `i` and a point on component `j`. The separation is carried at link
level rather than assembled from components, because `KnotEmbedding.ambientDist`
relates two points on *the same* curve and nothing in that structure relates two
curves.

Five fields, and one of them is doing the work: **`disjoint : ∀ i j, i ≠ j → ∀
s t, 0 < sep i s j t`** — distinct components never meet, which is what makes
the configuration a *link* rather than a singular map.

| result | content |
|---|---|
| `mutualIntegrand` | the unsubtracted cross term, stated through the structure |
| **`mutualIntegrand_pos_of_ne`** | **positive with no hypothesis beyond `i ≠ j`** |
| `mutualIntegrand_symm` | symmetric under exchanging (component, parameter) pairs |
| `mutualIntegrand_self` | on the diagonal it is the *unsubtracted* part of that component's own O'Hara integrand — the two integrands are one object at different index pairs |
| `selfIntegrand` | the O'Hara term, so `Σᵢ self` and `Σ_{i<j} mutual` are both expressible here |
| `mutualIntegrand_smul` | rescaling every separation by `c` scales the integrand by `c⁻²` |

**Why `mutualIntegrand_pos_of_ne` is the point.** Yesterday's bare-function
version needed `0 < sep s t` supplied as a hypothesis. Here it is *discharged
from `disjoint`*. A per-pair EM weight built this way is positive **because the
carrier is a link**, not because positivity was assumed of it — which is the
difference between a derivation and an axiomatisation, and this file's own
history is full of the latter.

**Two things named rather than claimed.** `mutualIntegrand_smul` is the
*pointwise half* of scale invariance; the energy's invariance also needs the
`ds dt` measure to scale by `c²`, which requires the integral this file does not
build. And `selfIntegrand` makes both halves expressible but not summable —
only the summation and integration are missing, and they want measure theory.

### I checked my own structure for the defect I fixed here yesterday

`NonSelfIntersection` carried `∀ E₀, energy > E₀` and was therefore
**uninhabitable for every `M`** — sorry-free, seen by no detector, and every
result conditional on it vacuous. A new structure with five interacting fields
earns the same scrutiny, so **`nonempty_linkEmbedding`** exhibits an inhabitant
rather than asserting consistency: components with all distances `0`, and a
separation that is the component's own `ambientDist` on the diagonal and `1` off
it. Deliberately degenerate — it establishes that the field set is *consistent*,
not that this is a link anyone wants.

### Where route (2) now stands

The formalisation chain is complete end to end: a multi-component carrier, the
mutual term through it, unconditional positivity, and the self/mutual
relationship. What remains is **not** formalisation — it is the numerical
minimisation on the three named carriers (Hopf, 8₁₁, L6a4/Borromean), plus the
integration theory to turn pointwise statements into an energy.


## 2026-08-31 — 🛑 CORRECTING MY OWN CLAIM: pointwise positivity is NOT "nonzero for unlinked pairs"

Went to acquire `freedman1994` / `ohara1991` after `paper-search-mcp` reconnected.
It could not be done (see below), but the literature check that replaced it
found a defect in what I wrote here two entries ago.

### What the literature says, and it confirms the formalisation

The **Möbius cross energy** of a two-component link is

  `E(γ₁,γ₂) = ∫∫ |γ₁'(s)| |γ₂'(t)| / |γ₁(s) − γ₂(t)|² ds dt`

— **unsubtracted**, exactly as `mutualIntegrand` encodes it, and conformally
invariant. So the self/mutual split recorded here is the standard one, not a
reconstruction. Two hard facts arrive with it:

- **`E(standard Hopf link) = 2π²`** — a value for one of the three carriers.
- **Freedman–He–Wang conjectured** the Hopf link minimises cross energy among
  nontrivial links; **Agol–Marques–Neves proved it** (`arXiv:1205.0825`,
  *Min-max theory and the energy of links*): if `lk(C₁,C₂) = ±1` then
  `E ≥ 2π²`, with equality iff the pair is a Möbius image of the standard Hopf
  link.

### 🛑 The correction

The AMN bound is conditioned on **`lk = ±1`**. Our carriers are not uniformly
that: Hopf (²H) has `lk = ±1`, but on **L6a4/Borromean every pairwise
`lk_ij = 0`** ((A3) of `mirror_split_s3_em_functional_probe.py`) — which is the
whole reason this front picked a Brunnian carrier.

And for an unlinked pair the **infimum of the cross energy is 0**. The energy is
invariant under scaling *both* components, but shrinking one alone by `ε` scales
the numerator by `ε` and leaves the denominator, so `E → 0`. Nothing forbids
that isotopy for a pair considered on its own.

**So my entry above overstated `mutualIntegrand_pos`.** I wrote that its
unconditional positivity is *"exactly what this bean asks of route (2) — nonzero
for unlinked pairs"*. It is not. **Pointwise positivity of the integrand is
strictly weaker than a positive lower bound on the energy**, and it is the
second that route (2) needs. The Lean is correct; the gloss on it was not.
`mutualIntegrand_pos_of_ne` and `mutualIntegrand_pos` stand as stated — they
just do not carry the weight I gave them.

### What survives, and it is the sharper recipe

The Borromean link is **Brunnian**: no two components are linked, yet the whole
is not splittable. So while each *pairwise* term can be driven to 0 in
isolation, the **total** energy cannot — shrinking one component forces the
other two through a smaller region, raising their mutual term. The minimum of
the total is nontrivial and the minimising configuration distributes energy
across pairs.

**Therefore `w_ij` must be the pairwise cross energy evaluated AT THE MINIMISER
OF THE TOTAL LINK ENERGY — not the minimum of the pairwise energy over that
pair's own isotopy class, which is 0.** That is a joint minimisation over the
whole carrier, not three independent ones. My previous entry said *"minimise on
three named links"*, which is right per link and wrong if read per pair; this
sharpens it.

**Not claimed:** that the total minimum is positive for the Borromean carrier.
That is the standard reading of Brunnian non-splittability, but I have not
verified it against a source and the AMN theorem does not cover `lk = 0`.
Whether a positive lower bound is known for Brunnian links is an open question
for this front and is worth a targeted look before the minimisation is coded.

### Acquisition: still blocked, and my last entry was wrong about that too

`paper-search-mcp` **reconnected** this session and I reported that as making
the gap closable. It does not. Measured: `search_arxiv("knot")` — a query that
cannot legitimately return nothing — gives `[]`, as does `search_crossref`.
Direct `curl` confirms the cause rather than inferring it from the empty result:

```
arxiv:    CONNECT tunnel failed, response 403
crossref: CONNECT tunnel failed, response 403
```

and the agent proxy's own status reports `connect_rejected — gateway answered
403 to CONNECT (policy denial)`.

**TRAP for the next agent: an MCP server reconnecting is not its backend
becoming reachable.** The tools load and return `[]`, which reads as "no
results" rather than "blocked". The discriminator is a maximally-broad query
plus a direct `curl`, and it costs two calls. **WebSearch remains the open
out-of-band lane** — everything in this entry came through it — but it cannot
put a PDF into `uploads/`, so the acquisition gap stands.

New acquisition target, higher priority than the two originals because it is the
one that actually bounds things: **`arXiv:1205.0825`** (Agol–Marques–Neves).


## 2026-08-31 — Route (2) survives the `lk = 0` problem, and the literature's open route IS this front's construction

Chased the load-bearing question from the previous entry: is the total energy
bounded below for a **Brunnian** carrier, where AMN's `lk = ±1` does not reach?

### 1. The qualitative fact route (2) needed — zero linking number does NOT force zero energy

> the Möbius energy is constrained from below by the absolute Gauss linking
> number, but **links such as the Whitehead link and Borromean rings have
> nonzero Möbius energy despite zero linking number**

So the worry raised in the previous entry — that the pairwise infimum is 0 for
unlinked pairs and might drag the carrier's energy to nothing — **does not
happen on the Borromean rings.** The `lk`-based bound is vacuous there, and the
energy is nonzero anyway. Route (2)'s carrier is not degenerate.

### 2. A candidate value, flagged as unverified

The same source refers to **"the `20π²` Möbius energy of Borromean links"**,
against `2π²` for the standard Hopf link. If that holds it is a value for the
second of the three carriers.

**Not verified.** It reaches me through a WebSearch summary of
`arXiv:2507.20903` (*Geometric considerations for energy minimization of
topological links and chainmail networks*), and **WebFetch is egress-blocked in
this sandbox**, so I have not read the paper. Do not cite `20π²` in a content
block on the strength of this entry — it is a lead with a named source, not a
figure this corpus has checked.

### 3. The Brunnian lower bound is OPEN, and my previous "not claimed" was right

> Analogous lower bounds **could perhaps** be derived from **Milnor invariants**
> and imply a minimum energy that depends on the degree of "Brunnian-ness" of
> the link.

*Could perhaps.* So there is **no proved positive lower bound on Möbius energy
for Brunnian links** — it is an open suggestion in the literature. The previous
entry declined to claim one; that restraint was correct and is now sourced
rather than merely cautious.

Note also a scope subtlety worth keeping straight: the FHW **conjecture** is
stated over *all non-split links*, while what AMN **proved** is the `lk = ±1`
case. Those are different statements and the search results use both phrasings.
Do not upgrade the conjecture to a theorem for the Borromean carrier.

### 4. 🟧 The convergence, and it is the substantive find

The literature's own open route to a Brunnian lower bound is *"lower bounds
derived from **Milnor invariants**"*. **`μ̄₁₂₃` is a Milnor invariant**, and the
Borromean carrier's non-triviality is exactly `μ̄₁₂₃ = 1`
(`mubar_borromean_eq_one`, by `decide`). So the open problem the energy
literature names is the same object this front has been building on
independently.

**And this corpus already constrains its shape.**
`exchange_symmetry_forces_agreement_on_pm_one` (proved here 2026-08-30, no
axioms) says any *exchange-symmetric* functional satisfies `F(1) = F(−1)` — it
sees at most `|μ̄₁₂₃|`. The Möbius energy is a sum over **unordered** pairs of a
label-independent geometric quantity, so it is exchange-symmetric and the
theorem applies to it.

**Therefore: any Milnor-invariant lower bound on Möbius energy must depend on
`|μ̄₁₂₃|`, never on `μ̄₁₂₃` itself.** That is a falsifiable prediction about an
open question in the energy literature, derived from a sorry-free result in this
corpus, and it costs nothing to state. Scope (b) on the sign-carrying form —
invariant cited, `mubar_swap_eq_neg`.

### Where the front stands

| step | state |
|---|---|
| carrier is non-degenerate at `lk = 0` | **established** (literature) |
| formalisation chain | **complete** (`LinkEmbedding`, mutual/self, positivity, inhabitant) |
| `E(Hopf) = 2π²` | established (literature) |
| `E(Borromean) = 20π²` | **lead only** — unread source, do not cite |
| positive lower bound for Brunnian | **OPEN in the literature**, not just here |
| shape of any such bound | **constrained to `|μ̄₁₂₃|`** by this corpus |

The remaining blocker is unchanged and now correctly attributed: it is not a gap
in this corpus's reasoning, it is **an open problem in the field**. That is a
materially different thing to report, and it means the numerical minimisation —
not a derivation — is the only route to `w_ij` currently available.


## 2026-08-31 — THE INTEGRATOR IS CALIBRATED against a proved value, and it caught the front's own degeneracy in my code

Producer: [`computations/mobius_cross_energy_hopf_calibration.py`](../computations/mobius_cross_energy_hopf_calibration.py)
Witness: `mobius-cross-energy-hopf-calibration.witness.json` — 4 assertions, all
passed. mpmath end to end, no `float()` anywhere including in the search.

Before any Borromean number is worth anything, the integrator has to reproduce a
value the literature has **proved**. It does.

| quantity | value |
|---|---|
| target `2π²` (Agol–Marques–Neves) | `19.739208802178717238` |
| "obvious" Hopf config (R=1, c=1) | `21.183763721862556325` — **+7.318 %** |
| constrained minimum over the *linked* family | `19.739209340362215055` at R≈1.515, c≈1.815 |
| relative excess over `2π²` | **`2.7264695e-8`**, and **from above** |

So an independent 2-parameter numerical minimisation reproduces AMN to **8
significant figures**, approaching from above exactly as the theorem requires.
The integrator is trustworthy.

### Two substantive by-products

**1. The picture everyone draws is not the minimiser.** Two orthogonal unit
circles each through the other's centre — the standard illustration of the Hopf
link — sits **7.3 % above** the minimum. Anyone tempted to evaluate a "nice"
configuration instead of minimising will be wrong by that much, and on the
Borromean carrier there is no proved bound to catch them.

**2. The minimiser location is grid-limited; only the energy is converged.**
R and c are refined on a 1/200 grid, so `1.515 / 1.815` are grid points and not
the true minimiser. The *energy* is nonetheless good to 2.7e-8 because the
functional is quadratic near a minimum — a 0.005 offset costs ~1e-8, which is
what is seen. Do not quote the location as a result.

### 🛑 I hit the front's own degeneracy inside the tool built to study it

The first version of this scan guarded only against the components **touching**
(`d² ≤ 0`) and never against their becoming **unlinked**. It "minimised" to
`E = 3.1219` at `(R, c) = (0.4, 2.5)` — **far below the proved bound**, which is
impossible for a Hopf link. The configuration is a **split** link, where the
cross energy has infimum 0: shrink one component and the numerator carries
`|γ₂'| ~ R` while the denominator does not.

That is the *same* degeneracy this bean recorded two entries ago as the reason
`w_ij` cannot be a per-pair minimum — met from the inside, in my own code, within
an hour of writing it down. It is now **assertion 4**, a measurement rather than
a caution, so the next person to build a search here inherits the guard instead
of the lesson. The linking test is cheap: `γ₂` punctures `γ₁`'s plane at
`x = c ± R`, and the pair is linked iff exactly one puncture lies inside the
unit disk.

### One threshold corrected, and how

`quadrature_converges_spectrally` initially failed. The cause was **my own
threshold**, not the method: I set `1e-12` aspirationally without measuring, and
the N=32↔N=64 gap is `9.93e-11`. Renamed to
`quadrature_converged_far_below_the_comparison_tolerance` and set to `1e-8` —
principled because that is two orders below the `1e-6` at which the `2π²`
comparison is made, so quadrature error cannot be what that assertion measures.
The source records the original value and why it moved. **Not a drained
baseline**: it is a threshold invented minutes earlier, corrected to what the
method delivers.

### What this unlocks

The Hopf carrier (²H) is done: `E = 2π²`, reproduced. The remaining two carriers
(8₁₁ for ³H, L6a4/Borromean for ³He) need a real minimiser over a
multi-component configuration space rather than a 2-parameter family — but the
integrand, the guard, and the calibration are now in hand, and the `20π²`
Borromean lead recorded above has something to be checked against.


**Corpus-grep note for whoever greps this next.** There is **no prior
Möbius-energy compute** in `computations/` or `tools/` — checked before
committing the calibration. But a grep for `ohara` returns two files that are
**substring false positives**, and both are real names in this corpus:
`Ding-I**ohara**-Miki` (`probes/pentagon_multipair_borromean_h4_probe.py`) and
`Man**ohara**n` (`bk_alpha_geometry_selection.py`). Neither computes an energy.
Search for `cross_energy` or `Möbius energy` instead.


## 2026-08-31 — the Borromean carrier, measured — and a tidy answer REFUTED

Producer: [`computations/mobius_cross_energy_borromean.py`](../computations/mobius_cross_energy_borromean.py)
Witness: `mobius-cross-energy-borromean.witness.json` — 5 assertions, all passed.
Uses the integrator calibrated against the proved `E(Hopf) = 2π²`.

Classical realisation: three mutually orthogonal ellipses, semi-axes `a`, `b`,
cyclic in the coordinates so `E_total = 3·E₁₂`. Unordered-pair convention — the
one in which AMN state `2π²` and in which the calibration reproduces it.

| quantity | value |
|---|---|
| `E_total` at the golden ratio `a/b = φ` | **`98.701819678652718428`** |
| `10π²` | `98.696044010893586188` |
| ratio | **`1.0000585197494`** |
| quadrature converged to (N=96 vs 128) | **`2.792e-15`** |
| family minimum over `a/b ∈ [1.5, 2.1]` | `97.583276794340978666` at `a/b = 1.817` |
| equal circles `a = b`, min separation² | `1.67e-143` — **they touch** |

### 🛑 It is NOT `10π²`, and this is the interesting part

At N=64 and four decimals the ratio reads `1.0000`. It would have been written
down as an identity. It is not one: converged, the discrepancy is **`5.85e-5`**
against a quadrature error of **`2.79e-15`** — **ten orders of magnitude**
apart. A genuine near-miss, refuted rather than reported.

This also settles the `20π²` lead recorded above. `2 × 98.7018 = 197.4036`
against `20π² = 197.3921` — the *same* `5.85e-5`. So that figure is the
**ordered-pair** convention applied to the golden-ratio configuration, and it
carries the same near-miss. The convention question I flagged as "reasoning from
structure without the papers" is now answered from the arithmetic: **the source's
`20π²` is `2 ×` this value, not a different quantity.**

### The golden ratio is not the minimiser either

The family minimum is `1.13 %` **below** the golden-ratio value. Same shape as
the Hopf calibration, where the standard picture sat `7.3 %` above the minimum.
The classical, prettiest configuration is not the energy-minimising one in
either carrier.

### 🛑 What I did NOT verify, recorded as a deliberate failing-shaped assertion

`TOPOLOGY_NOT_VERIFIED_across_the_scan` is a **deliberate zero** in the witness.
Nothing checks that the configuration stays *Borromean* as `a/b` varies — only
that the components do not touch. That is the **identical trap** the Hopf
calibration's assertion 4 records, where a scan guarded only against touching
walked into a split link and "minimised" below a proved bound.

Two reasons it is less likely here — the energy **rises on both sides** of the
interior minimum (`142.6` at `a/b = 1.1`, `149.5` at `6.0`) rather than running
away, and pairwise linking number is `0` by construction for a Brunnian carrier
so there is no linking-number guard to write. **Less likely is not verified.**
The family minimum must **not** be cited as the Borromean energy minimum until
the topology is checked.

### Where route (2) stands

Two of three carriers now have numbers from a calibrated instrument. What is
still missing for a `κ(A)` comparison is the third (8₁₁, a knot rather than a
link, so its self-energy is the relevant object and the machinery differs), a
topology guard for the Brunnian scan, and the per-pair decomposition at the
minimiser rather than the total.


## 2026-08-31 — the TOPOLOGY gap is closed, and the obvious closed form is a low-end coincidence

Producer: [`computations/mobius_borromean_topology_guard.py`](../computations/mobius_borromean_topology_guard.py)
Witness: `mobius-borromean-topology-guard.witness.json` — 5 assertions, all passed.

The previous entry left `TOPOLOGY_NOT_VERIFIED_across_the_scan` as a deliberate
zero: nothing checked the three-ellipse configuration stays *Borromean* as `a/b`
varies, so its family minimum could not be cited.

**The argument is cheaper than computing `μ̄₁₂₃` geometrically.** Link type is an
isotopy invariant, and each component is an ellipse, hence embedded for any
`a, b > 0` — no self-intersection to check. So if no two components meet
anywhere along the path, the deformation is an ambient isotopy and the link type
is **constant** across the range.

| measurement | value |
|---|---|
| worst pairwise separation over `a/b ∈ [1.5, 2.1]` | **`0.5`** at `a/b = 1.5`, pair 01 |
| max pairwise Gauss linking number, all 3 pairs, 4 sample ratios | **`5.79e-71`** |
| `a = b` degenerate boundary, min separation² | `4.93e-142` |

Half a unit of clearance, not a near miss. And all three Gauss linking integrals
vanish to `1e-71`, which is necessary for Brunnian and rules out the pair-linked
alternatives the isotopy argument alone would permit.

**So `a/b = 1.817` (the family minimum) and `a/b = φ` are the same link**, and
the earlier probe's minimum may now be cited.

### 🛑 The tempting closed form is wrong past the low end

The worst case is `0.5` at `a/b = 1.5`, which is exactly `a − b`. It also matches
exactly at `a/b = 1.1` (`0.1`). **It does not hold generally**: at `a/b = 1.8`
the separation is `0.74415` against `a − b = 0.8`, and by `a/b = 4` it is
`0.96657` against `3` — the minimising pair of points on the two ellipses
changes. Recorded in the witness as `closed_form_check` because it is the
obvious wrong generalisation to draw from the worst-case row, and I drew it
myself before testing it.

### What actually disposes of the grid-sampling caveat

Not the closed form — **monotonicity**. The separation increases across the
sampled profile (`0.1, 0.5, 0.744, 0.817, 0.900, 0.937, 0.967` for
`a/b = 1.1 … 4.0`), so the minimum over any interval sits at its **left
endpoint**, which is independently where the step-0.01 grid scan found it.
Monotonicity is read off seven points, not proved, so the honest claim is a
strong statement about the sampled profile rather than a theorem.

### Still not established

That the type **is** the Borromean rings. That rests on the classical
three-mutually-orthogonal-golden-rectangles construction, taken here as the
definition of the `a/b = φ` point. What this probe adds is that the rest of the
family **inherits** it.


## 2026-08-31 — 🛑 SCOPING STOP: route (2) can reach ONE κ point, and the blocker is upstream of everything I have built

Before building the per-pair decomposition I checked what carriers exist to
decompose. The answer changes what "next" means on this front.

### The corpus names binding-link carriers for TWO isotopes, both at A = 3

From `he4-link-volume-braid-closure.witness.json`:

| isotope | binding link | components | Vol |
|---|---|---|---|
| ³H | `8₁₁` | 1 | 8.286316817806593 |
| ³He | `L6a4` = Borromean | 3 | 7.327724753417752 |

Plus ²H → Hopf (`Vol = 0`) from `binding-link-volumes.witness.json` — and Owner
Ruling A says the deuteron binding is **not** a hyperbolic-volume term, so that
row is not a carrier for this purpose.

**⁴He has no identified carrier at all.** Its `he4_vol4.bondcount_backout =
8.046` is described in the witness's own text as *"an unverified bond-count
back-out gated on the SDP/canonical-knot-ID (conj #604) at A=4"*, and it
disagrees with the alternative `doubly_magic_provisional = 14.655` by a factor
**1.82**.

### 🛑 And the route to DERIVE carriers fails where the answer is known

The same witness records a Markov-closure attempt to produce carriers from the
canonical operator-valued atomic braid word:

| | components | geometric | Vol | vs the known carrier |
|---|---|---|---|---|
| proton | 2 | no | 0 | — |
| neutron | 2 | no | 0 | — |
| ³H | 4 | no | 0 | **8₁₁ has 1** |
| ³He | 4 | no | 0 | **Borromean has 3** |
| ⁴He | 5 | no | 0 | (none to compare) |

This is not "the derivation has not been extended past A = 3". It is **refuted
at the two isotopes where the answer is checkable** — wrong component count,
non-geometric, zero volume, at both.

### What that means for route (2)

`κ(A)` spans **A = 3…63** (31 points, from the mirror series). Route (2) can
supply an EM weight for exactly the **A = 3 mirror pair** (³H / ³He), because
that is the only A where the corpus names carriers for both members. **One
point.**

I said "two points (A = 3, 4)" would be reachable in the previous turn's
hand-off. That was wrong — ⁴He has no carrier, only a gated back-out. And one
point is worse than two against a standard this corpus set for itself last week:
`qou-ebs6` records *"one parameter, two points, zero out-of-sample support"* as
the reason `b_αα` **is not closable**. Route (2) as it stands is a weaker
instance of the same shape.

### The honest consequence — stop building energy machinery

The formalisation is complete (`LinkEmbedding`, mutual/self, positivity), the
integrator is calibrated against a proved value to 8 figures, and the topology
guard is closed. **None of that is the blocker.** The gate is **carrier
identification**, it sits upstream of every piece of it, and the corpus's own
derivation route for carriers is refuted at A = 3.

So the next question on this front is not "compute more energies". It is: **is
there any route to a binding-link carrier at A ≥ 4 that is not the refuted
Markov closure?** Until that has an answer, more energy machinery has nothing
to consume it.

**Not claimed:** that route (2) is dead. Its A = 3 number is computable and
would be a genuine, if single, comparison — and the machinery is built and
verified, so it costs nothing further to use if a carrier route appears. Scope
(a) on the reachability, not on the route.


## 2026-08-31 — 🛑 ANSWERED, by a sibling three hours before I asked: the carriers are an ADMITTED FIT, so route (2) cannot meet this bean's own GATE

I closed the previous entry asking *"is there any route to a binding-link
carrier at A ≥ 4 that is not the refuted Markov closure?"* — and framed it as
needing an owner steer. **It did not: `qou-5vhf` answers it, created
2026-08-31T03:00Z and completed 03:22Z, roughly three hours before I asked.**
PR #6327. That is the corpus-grep discipline catching me one step late, on a
bean younger than the session.

### The answer, and it is worse than my scoping stop

> The obvious form of "extend the nucleus→link map past A=4" is a fit. The
> A≤4 assignments are an admitted AME-driven census search
> (`jsj_verification.py` keeps volumes near `B_AME/(ρ·m_e)`), and the
> 2026-07-13 C1–C9 table already excludes the constructed alternatives at A≥5
> from the other side.

and on whether the substrate supplies a selector instead:

> **`n_0 = 3A` IS derived** … the canonical atom word's max generator index is
> exactly `3A−2` on all eight isotopes tested.
> **`n_braid` is NOT derived.** It equals `1 + max|generator|` of the **assigned**
> knot's own SnapPy braid word — `6₂ → 3`, `8₁₁ → 5`, `L6a4 → 3`, all three
> exact. It is a **readout**, not a selector.

Supporting audit: `docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`.

### What that does to route (2), stated carefully

Two things, and only the second is fatal.

1. **Not strict circularity.** The carriers were selected to match **total**
   binding `B_AME`, whereas route (2) computes the **EM** weight — a small
   correction, not the quantity the selection targeted. So an A = 3 number
   would not be trivially circular.

2. **But it fails this bean's own GATE.** The GATE in this bean's title reads
   *"no tuned constant (CAL-4)"*. A carrier chosen by census search against AME
   data **is** a hidden fit — a much larger one than a tuned constant, since it
   selects the geometry the whole computation runs on. So a `κ(A)` reproduction
   built on these carriers could not be reported as parameter-free, whatever the
   energy machinery does.

**Combined with the previous entry** — carriers exist at A = 3 only, and the
closure derivation is refuted at A = 3 — route (2) reaches **one κ point, on a
fitted carrier**. That is not a front that more energy machinery improves.

### What this branch's work is still worth

The machinery is sound and independently useful, and none of it depended on the
carrier question: `LinkEmbedding` with mutual positivity discharged from
disjointness; the integrator calibrated against the **proved** `E(Hopf) = 2π²` to
8 significant figures; the Borromean value with `10π²` **refuted** at ten orders
of confidence; the topology guard closing the isotopy question. Those stand as
results about Möbius energy in this corpus regardless of what 4-B does with
them.

**Scope (a)** on route (2)'s reachability — a negative about the available
carriers, not about knot energy as an EM mechanism. If a *derived* carrier
assignment ever appears, every piece above is waiting for it.


## 2026-09-02 — the fourth route (`qou-0hdx`) is closed too, so route (2) has no successor

`qou-0hdx` was opened 2026-08-01 as this bean's successor: the Freedman–He
**asymptotic crossing number**, advertised as clearing every obstruction that killed
the trichotomy's routes — symmetric in the pair (O1-proof), unsigned so nonzero at
`lk = 0` (Brunnian-proof), `Flux^2` rather than `Flux^3`, and carrying an explicit
`Vol^{-1/3}` factor claimed to *converge* with the empirical `A^{-1/3}` κ-null. It
sat at `todo` with `updated_at == created_at` for a month.

It is now **scrapped**, on two corrections verified against the primary source
(`library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216`, Komendarczyk
eq. 43) rather than taken from the audit trail:

1. The bound's invariant is `ac(L_k, L)` — one component against the whole link,
   summed over `n` **components**. The per-pair object the bean proposed to derive
   **does not exist** in either source. Structural, scope-(b).
2. The prefactor is `(pi/16)^{1/4}`, a pure constant with **no volume factor**. The
   `Vol^{-1/3}` is Khesin Thm 3.6's *single-knotted-torus* bound, misapplied. The
   advertised convergence was one route and a misattribution, not two independent
   ones — retracted (Round 5, `docs/audits/2026-08-01-em-linking-reads-round1.md`).

**And it does not escape this bean's blocker.** Eq. (43) is indexed on an
n-component link `L` in `R^3`, so evaluating `ac(L_k, L)` for a nucleus requires
first saying which link the nucleus **is** — the same carrier assignment that
`qou-5vhf` establishes is an admitted AME-driven census search. Route (2)'s failure
of this bean's own no-tuned-constant (CAL-4) gate therefore applies to the successor
verbatim.

Net: the trichotomy's route (2) is closed and its one named successor is closed with
it. The **one live positive target** the arc leaves behind is not a crossing number
at all — eq. (43)'s topological factor is A-independent for a fixed local
configuration, so it *relocates* κ(A) into the flux: κ falls by 2.099 across
A = 3…41, requiring the per-component flux to fall by 1.449. Independently derivable
from the corpus braid geometry; not derived; nothing wired.


## 2026-09-02 — the flux leg, explored: the bound is CHARGE-BLIND, and the recorded obligation has the wrong sign

Taking up the one live successor `qou-0hdx` left behind. The obligation was
stated as *"derive the per-component flux law"*; it is not one function of A, and
the shape it must have is the opposite of the one recorded.

**The structural point.** Every factor on the right of Komendarczyk eq. (43) is
either link topology (`ac`) or flux — **nothing in it distinguishes a proton from
a neutron.** But κ(A) is built from the mirror-pair binding split, which is pure
charge. So charge can enter at exactly one place: the flux must differ between
proton and neutron components. The obligation was never `Flux(A)`; it is the pair
`(Φ_p, Φ_n)`.

**And that is not enough.** For a vertex-transitive carrier (`ac(L_k,L) = a` for
every k — true of the Borromean rings, S₃-symmetric, and of every carrier this arc
has used), assign flux by charge and swap Z↔N. Mirror partners share A, the link,
and `min_k|Flux|`; the swap only relabels. Then

    E₁ = C·a·(Z·Φ_p + N·Φ_n)·m ,  E₂ = C·a·(N·Φ_p + Z·Φ_n)·m
    ΔE = C·a·m·(Z − N)·(Φ_p − Φ_n)

For the whole `d = |Z−N| = 1` ladder — the entire `A = 2Z−1` series the arc scores
against — this is **one constant, independent of the nucleus**. Sorry-free in Lean,
`lean`-direct exit 0, `#print axioms` = `[propext, Quot.sound]` on all five decls
(no `Classical.choice`, no `sorryAx`):
`folio/quantum-observable-universe/lean/QOU/Mass/FreedmanHeMirrorSplitChargeBlind.lean`
— `mirrorSplit_eq`, `mirrorSplit_succ_const`, `mirrorSplit_succ_eq_of_ne`,
`mirrorSplit_eq_zero_of_flux_eq`, `mirrorSplit_add_eq`.

The AME ladder is **not** constant: the split grows **13.63×** from A=3 to A=63.
So constant charge-fluxes are refuted, and the required `Φ_p − Φ_n` must **GROW**
by that factor.

**This contradicts what the corpus records, in sign.** `em-linking-fh-link-bound-correction.witness.json`
records the obligation as a per-component flux **DECLINE of 1.4487357**. That is
`√(κ(3)/κ(41))`, read off κ. But **κ is not an energy**: measured here,
`κ := split/(n_pairs·u)` with `u` constant to **5.042e-8** across all 31 rows and
`n_pairs = Z−1` exactly, so the pp-pair count is already divided out. Eq. (43)
bounds an ENERGY; the observable to confront it with is the split. Reading the
obligation off κ silently asks the bound to explain a per-pair ratio. Opposite in
sign, **9.41×** in magnitude. Both corpus figures are reproduced exactly in the new
witness before being disputed (2.098835 and 1.4487357, to 1e-6).

**And the framework defines no flux.** Measured, not recalled: `Flux` occurs
nowhere in `folio/quantum-observable-universe/lean/` as a quantity. The grep hits
are a photon docstring (`KnotRegistry.lean:48`), meson colour tubes
(`MesonFluxTubeReduction.lean`), and the English idiom *"in flux in Mathlib's
CoxeterSystem API"* (`Tw.lean:56`, `Defn.lean:114`, `Quotient.lean:62,136`). So
supplying `(Φ_p, Φ_n)` is not reading off an existing structure — it is introducing
one, which is where CAL-4 pressure would land.

**Scope — (a) on a model class, not on eq. (43).** Excluded:
`{vertex-transitive carrier} × {flux depending only on charge} × {saturation}`.
Three escapes survive and are NOT refuted: a carrier that is not vertex-transitive;
an `ac` that depends on the charge assignment; an unsaturated bound — eq. (43) is
an inequality, and using it as an equality is an assumption **nothing in this corpus
establishes**. Each is a further thing to derive, not a thing the sources supply.

Artifacts: `computations/em_linking_fh_mirror_split_charge_blindness.py`,
`computations/em-linking-fh-mirror-split-charge-blindness.witness.json` (5/5).
Nothing wired.


## 2026-09-03 — SATURATION IS PRIOR, not one escape of three: a lower bound cannot constrain a DIFFERENCE

Correcting my own scoping from the entry above. That entry closed by naming three
surviving escapes from the charge-blindness result — a non-vertex-transitive
carrier, a charge-dependent `ac`, and an unsaturated bound — and presented them as
parallel. **They are not parallel.** The third is prior to the other two, and the
reason is elementary once stated.

**Eq. (43) is an inequality**, `E_{3/2}(X) ≥ B(L, Φ)`. The arc's observable is a
mirror-pair **split** — a *difference* of two such energies, `(Z,N)` against
`(N,Z)`. From `B₁ ≤ E₁` and `B₂ ≤ E₂`, **nothing at all follows about `E₁ − E₂`**:
for any target value `t` whatsoever there are energies meeting both bounds whose
difference is exactly `t`. Take `E₂ = max(B₂, B₁ − t)` and `E₁ = E₂ + t`.

So eq. (43) does not merely fail to *predict* κ(A) — it fails to **constrain** it,
in either direction. Whatever the AME ladder had turned out to be (constant,
growing, falling, alternating), the bound would have been consistent with it.

**Why that reorders the escapes.** Escapes 1 and 2 concern the *shape* of `B`. The
shape of `B` only matters once `B` is being read as the energy — i.e. once
saturation is assumed. Without it there is nothing for a carrier or an `ac` to be
the shape *of*. Every κ-scoring result in this arc inherits the assumption.

**What would restore a constraint is an UPPER bound**, which eq. (43) does not
supply. With `B₁ ≤ E₁ ≤ U₁` and `B₂ ≤ E₂ ≤ U₂` the difference is pinned to
`[B₁ − U₂, U₁ − B₂]`, and that interval collapses to a point exactly when both
bounds are tight — so saturation is the *extreme* case of the two-sided situation,
not a mild simplification of it. Naming the missing ingredient precisely: not more
topology, but an **upper bound on the energy of a knotted flux configuration**.

Sorry-free in Lean, `lean`-direct exit 0 no warnings, over the weakest structure
that admits the statements (`[AddCommGroup R] [LinearOrder R]
[IsOrderedAddMonoid R]` — an ordering is genuinely required here, unlike the
sibling file's generic `CommRing`; note `LinearOrderedAddCommGroup` is deprecated
in this Mathlib and is no longer a class at all, so it cannot be used as a binder):
`folio/quantum-observable-universe/lean/QOU/Mass/LowerBoundCannotConstrainADifference.lean`
— `diff_unconstrained`, `no_split_value_is_excluded`, `diff_of_saturated`,
`diff_bounded_of_upper`, `diff_bounded_collapses_iff_saturated`. `#print axioms`:
four carry `[propext, Classical.choice, Quot.sound]` (Classical.choice enters via
`max`), and `diff_of_saturated` depends on **no axioms at all**.

**Corpus-grep before claiming novelty.** `saturat` has many hits, all other
subjects (Δ_λ saturation, coth-saturation, channel saturation). The closest prior
remark is `docs/audits/2026-08-01-em-linking-reads-round1.md:281` — *"the
inequality itself is vacuous for our tubes"* — but that is about **Khesin Thm
3.6** having a `2·genus−1` factor that vanishes on unknot components, a different
statement about a different inequality. No prior instance of the
difference-of-lower-bounds argument in `docs/`, `computations/`, `content/` or
`.beans/`.

**NOT measured, and worth saying rather than leaving implicit.** One might hope to
show saturation is *implausible* by computing how far `B` sits below the observed
energies. That cannot be done here: evaluating `B` needs a per-nucleus carrier
link, and `qou-5vhf` establishes the `A ≤ 4` assignments are an admitted
AME-driven census search. The slack is **unmeasured**, not measured-and-small.

Nothing wired.


## 2026-09-03 — the UPPER-BOUND route dies on PRECISION, not availability

The entry above named the missing ingredient: an energy **upper** bound, since a
lower bound alone cannot constrain a difference. The obvious next move is to go
acquire one. That move is wrong, and the reason needs no carrier, no flux value
and no acquisition.

**The arithmetic.** With two-sided bounds `B_i ≤ E_i ≤ U_i` the difference is
pinned to `[B₁ − U₂, U₁ − B₂]`, an interval of width exactly `(U₁ − B₁) +
(U₂ − B₂)` — the **sum of the two slacks**. For that to be narrower than the split
it is meant to explain, the combined slack must beat the split. But the mirror
split is a **difference of two large, nearly equal energies**. Under the arc's own
model (`ΔE = c(Φp − Φn)` against `E = c(Z·Φp + N·Φn)`), if the two fluxes lie
within a factor `r`,

    ΔE / E  ≤  (r − 1) / A

**and the budget FALLS with A** — it sharpens 21-fold across the ladder
(`63/3`), so the requirement is hardest exactly where the data is best. At
`A = 63` with a generous factor-2 flux ratio it is **1.5873016 %**. Freedman–He-type
bounds are order-of-magnitude estimates; nothing in that literature is tight to a
percent. So an upper bound of the available quality cannot narrow the interval
below the observable, whatever it is.

**And the library holds nothing anyway** — but that is the weaker half of the
finding, not the point. Measured by a **live scan** in the probe (not a
remembered grep): **zero** files matching `ropelength|ideal knot` across `docs/`,
`computations/`, `content/` and `library/` — both the `sections/` and `ocr/`
tiers, all library directories. Asserted so that a future acquisition **flips the
assertion** and prompts a revisit, rather than the probe asserting a stale
absence. The precision argument does not depend on it.

Lean, sorry-free, `lean`-direct exit 0 no warnings:
`folio/quantum-observable-universe/lean/QOU/Mass/MirrorSplitIsASmallFractionOfTheEnergy.lean`
— `split_fraction_bound`, `interval_width`, `interval_narrower_than_split_iff`.
`#print axioms`: `interval_width` is `[propext, Quot.sound]`; the other two add
`Classical.choice`. Zero `sorry`/`axiom`.

**A fourth declaration was written and REMOVED rather than shipped.** A
`budget_tightens_with_A` had two hypotheses that did no work and a proof that was
just `split_fraction_bound` applied at the larger indices — it asserted nothing
the main bound does not already say, and the disjunction it stated was satisfied
by its right branch regardless of the growth hypothesis. That is a trivial-true
dressed as monotonicity, and the `1/A` is already visible in the main bound. Noted
in the file header so the removal is on the record.

Probe: `computations/em_linking_upper_bound_precision_budget.py` + witness, 4/4.

**SCOPE — scope-(a), and one escape is explicitly NOT closed.** The fraction bound
assumes the two fluxes are comparable (`Φn ≤ Φp ≤ r·Φn`, `r` finite). A model with
**`Φn → 0`** — neutron components carrying no flux at all — has unbounded `r` and
escapes this entirely. It is not refuted here. Eq. (43) itself remains untouched;
it is a true lower bound throughout.

Nothing wired.


## 2026-09-03 (later) — the `Φn → 0` "escape" is NOT one; correcting my own entry above

The entry above closed by leaving one escape open: *"a model with `Φn → 0` —
neutron components carrying no flux at all — has unbounded `r` and escapes the
fraction bound entirely. Not refuted here."* **That was wrong, and it was my
error, not an open question.**

What is true is only that the *hypothesis* fails: the bound is stated with
`Φn ≤ Φp ≤ r·Φn` and `Φn > 0`, so as `Φn → 0` the ratio `r` is unbounded and the
theorem does not apply. **A failing hypothesis is not a failing conclusion**, and
here the conclusion survives by direct computation:

- **The split is still constant.** With `Φn = 0`, `ΔE = c·Φp·(Z − N)`, which on
  the `d = 1` ladder is `c·Φp` — independent of `A`, exactly as before. This was
  never in doubt: `mirrorSplit_eq` (merged in #6423) assumes nothing about
  comparability.
- **The fraction is exactly `1/Z`.** The energy is `c·Z·Φp` and the split is
  `c·Φp`, so `Z·split = energy` — an identity, not an estimate. On the ladder
  `Z = (A+1)/2`, so the fraction is `2/(A+1)`.
- **Which is the `r = 3` case of the very bound it was meant to evade.** The
  general bound gives `(r−1)/A`; `r = 3` gives `2/A`. So the limit that looked
  like an escape sits *inside* the excluded regime, not outside it.

Both proved, sorry-free, `lean`-direct exit 0 no warnings, in
`folio/quantum-observable-universe/lean/QOU/Mass/MirrorSplitIsASmallFractionOfTheEnergy.lean`
— `zero_neutron_flux_is_the_r_eq_three_case` (needs `N ≤ Z`, true throughout the
`A = 2Z−1` ladder where `N = Z−1`) and
`zero_neutron_flux_fraction_is_exactly_one_over_Z`. `#print axioms`: the first
carries `[propext, Classical.choice, Quot.sound]`, the second **`[propext]`
alone**.

**Consequence for the arc: there is no surviving escape on this front that I
know of.** Route (2) and its successor `qou-0hdx` are closed; the flux leg is
closed (charge-blindness); saturation is closed (a lower bound cannot constrain a
difference); the upper-bound repair is closed (precision, not availability); and
the last named escape turns out to be inside the excluded regime. That is a
stronger statement than any single entry above, and it is stated as **scope-(a)
throughout** — eq. (43) itself is untouched and remains a true lower bound.

**What I am NOT claiming.** The two escapes that remain formally open from the
charge-blindness entry — a non-vertex-transitive carrier, and an `ac` that
depends on the charge assignment — are *not* closed by anything here. They were
shown to be posterior to saturation, which is closed; but posterior is not the
same as refuted, and neither has been tested on its own terms.

Also worth recording as a method note, because it nearly went the other way: I
flagged `Φn → 0` as an escape from the *shape of the hypothesis*, without
computing the case. One line of arithmetic settled it. Check the limit before
recording it as open.


## 2026-09-03 (later still) — the last two escapes are ONE, and it is the carrier blocker again

Taking up the two escapes left formally open by the merged #6423 and #6485: (1) a
carrier link that is **not vertex-transitive**, so `ac(L_k, L)` differs between
components; (2) an `ac` that **depends on the charge assignment**. They are one
escape, not two.

**(2) is a category error, not a model choice.** `ac(L_k, L)` is Freedman–He's
asymptotic crossing number of one component against the whole link — a topological
invariant of `L` alone. It takes no charge input, and neither Komendarczyk
(arXiv:0808.1533v1 eq. 43) nor Khesin defines any such refinement. Making it
charge-dependent is not a weaker reading of eq. (43); it is a **different
functional, for which no bound is in evidence**. Nothing here refutes such a
functional — there is simply no theorem to appeal to, so it cannot be cited as an
escape *from one*.

**(1) is a real generalisation, and it relocates rather than frees.** Give each
component its own weight `a k` and let the proton set be an arbitrary `Finset`.
The split factorises exactly:

    ΔE = C·m·(φp − φn)·( Σ_{k ∈ P} a k − Σ_{k ∈ Q} a k )

with `P`, `Q` the two partners' proton sets. **The total weight `Σ_k a k` cancels
entirely**, so every ingredient except that last bracket is A-independent — and
therefore *all* the A-dependence the split can possibly have is carried by it. A
non-vertex-transitive carrier does not manufacture A-dependence; it moves the
obligation onto a purely topological quantity of the carrier and the charge
assignment, which **cannot be evaluated without saying which link the nucleus is**.
`qou-5vhf` establishes the `A ≤ 4` carrier assignments are an admitted AME-driven
census search. So escape (1) is not independent of the blocker that ended route
(2) — it *is* that blocker, reached from a different direction.

Sharpest form: if the two proton sets happen to carry **equal total weight**, the
predicted split is exactly **zero**, whatever the fluxes
(`mirrorSplit_eq_zero_of_equal_weight`). The bracket is not merely where the
A-dependence lives; it is the only thing standing between this model and a
vanishing prediction.

The uniform case is recovered as a corollary — the bracket collapses to
`a·(|P| − |Q|)`, reproducing the merged `mirrorSplit_eq`, constant on the `d = 1`
ladder where `|P| − |Q| = 1`.

Lean, sorry-free, `lean`-direct exit 0 no warnings, generic `CommRing` (no
ordering used, so none assumed, §7c):
`folio/quantum-observable-universe/lean/QOU/Mass/NonUniformAcRelocatesTheObligation.lean`
— `mirrorSplit_nonuniform_eq`, `mirrorSplit_uniform_eq`,
`mirrorSplit_eq_zero_of_equal_weight`. All three `[propext, Classical.choice,
Quot.sound]`; zero `sorry`/`axiom`.

**SCOPE — scope-(a), and deliberately WEAK. This does NOT close the escape.**
Nothing here says a non-uniform carrier cannot produce the observed 13.63×
growth: the bracket is unconstrained in general, and with enough spread in `a k`
it could. What is shown is that doing so **requires a specified carrier**, which
is the ingredient the arc does not have un-fitted. Read this as *relocated to a
known blocker*, not as *refuted*. Eq. (43) is untouched throughout.

No probe — this is pure structure, and a probe would be padding.

## ROUTE (2) CORRECTION 2026-09-13 — steps (i) and (ii) were ALREADY DONE

This bean's "Next for route (2), in order: (i) give KnotEmbedding an ambient
metric; (ii) write the O'Hara integrand with its intrinsic subtraction; (iii)
only then ask whether it reproduces kappa(A)" describes the PRE-FIX state and is
stale. Measured against the file on main:

  (i) DONE -- KnotEmbedding carries ambientDist, ambient_symm, ambient_nonneg and
      chord_le_arc, added 2026-08-30 by this bean's own ROAST commit. LinkEmbedding
      adds cross-component sep with disjoint and sep_self.
  (ii) DONE -- oharaIntegrand = 1/ambientDist^2 - 1/arcLengthDist^2 exists, and
      oharaIntegrand_nonneg is DERIVED from chord_le_arc, not assumed.
  (iii) The kappa(A) gate is RETIRED by PR #7080: the series constrains only the
      product s*p, so it cannot adjudicate between candidate invariants.

What was actually missing was the INTEGRAL, which the file's own docstrings name
three times. That is now supplied for the mutual channel in PR #7284 (bean
qou-pc85) -- and it needed no O'Hara theorem, because the mutual channel has no
diagonal singularity. Route (2) is no longer blocked on infrastructure.

I reported the blocker from this bean's prose without opening the file. Recording
the correction here so the next reader does not re-pay it.

## CORRECTION 2026-09-13 — the ROAST's O2 argument does not apply to the channel this bean needs

The ROAST above says the literature Mobius/O'Hara energy is "subtracted by
construction", and concludes "a functional whose regularising subtraction is
intrinsic is not vulnerable to that argument. So O2 is a reason to PREFER route
(2) over route (1)'s kernel". I repeated that on PR #7284 before checking it.

IT IS WRONG FOR THE MUTUAL CHANNEL. The intrinsic subtraction is in the SELF
term 1/ambient^2 - 1/arc^2, and by THIS BEAN's own split the self term belongs
to qou-bn8e ("this bean owns only the pairwise/linking channel"). The mutual
term carries no subtraction, and QOU.MobiusEnergy states it in its own theorem:

    mutualIntegrand_eq_ohara_without_subtraction
      -- the O'Hara integrand with the subtraction DROPPED (1/D^2 = 0)

and PR #7284's own section 1 proves mutualIntegrand_pos_of_ne: STRICTLY
POSITIVE, unconditionally, no hypothesis at all. That is exactly the property
that excluded coth under O2 (qou-17mq, PRs #7020/#7080).

So route (2)'s mutual channel is in coth's position, not immune to it. O2 is
NOT a reason to prefer route (2) over route (1) on this ground — that comparison
should be withdrawn.

WHAT SURVIVES, and it is the useful half: the fix is #7080's closure, unchanged
in shape. Zero mean forces the subtraction constant to be the kernel's own mean
— there c0 = <coth>_M, here the mean of 1/sep^2 — so it is determined by the
geometry rather than chosen. Proved sorry-free on #7284
(zeroMeanMutualKernel_integral_zero, zeroMeanMutualKernel_not_pos): the
subtracted kernel satisfies O2 and genuinely changes sign.

The gate is therefore CLEARED, but earned rather than free. Anyone citing
"O'Hara's subtraction protects route (2)" must say which channel they mean.


## 🟩 The library NOW HOLDS the knot-energy literature — 11 sources, incl. O'Hara's original

This bean's own path-5 finding — *"the library holds NO knot-energy source, and my
first grep said the opposite"* — was **true as measured, and the sources were on
disk the whole time**, one directory away from where path 5 looks.

They were in **`uploads/`**, the incoming queue. AGENTS.md: *"corpus-grep path 5
searches `library/` only, so anything still in `uploads/` is invisible to it — an
un-ingested paper will not be found by any 'has the corpus got this?' check,
which is exactly how a held source gets re-derived."* That is this bean, exactly.

Ingested 2026-09-13 (`pdf-structure.py` → `migrate-uploads-to-library.py --apply`
→ `summarize-library.py --apply`), 14 ok / 0 failed:

| doc-id | work |
|---|---|
| `1-s20-0040938391900102-main` | **O'Hara, _Energy of a Knot_, Topology 1991** — the primary |
| `arxiv-1111.6782v2` | Blatt & Reiter, *Stationary Points of O'Hara's Knot Energies* |
| `arxiv-1202.5426v2` | *Hard analysis meets critical knots* — stationary points of the Möbius energy |
| `arxiv-1308.2499v1` | Blatt & Reiter, *Towards a regularity theory for integral Menger curvature* |
| `arxiv-1904.13129v1` | Vorderobermeier, *regularity of critical points for O'Hara's knot energies* |
| `arxiv-1905.06064v1` | Blatt, Reiter & Schikorra, *On O'Hara knot energies I: regularity for critical knots* |
| `arxiv-1908.11677v1` | Kawakami, *Variational formulae and estimates of O'Hara's knot energies* |
| `arxiv-2103.07383v1` | Steenebrügge, *Analyticity of critical points of the generalized integral Menger curvature* |
| `arxiv-2208.12678v4` | Lipton & Nair, *Stationary curves under the Möbius–Plateau energy* |
| `arxiv-2505.02719v2` | Freches, Schumacher, Steenebrügge et al., *Palais–Smale condition in geometric knot theory* |
| `arxiv-2512.02998v1` | Blatt, Gilsbach, Reiter et al., *Stability of knot equivalence at low regularity, symmetric critical knots* |

Measured on the same greps, before → after:

```
tier 1 (INDEX.md) knot-energy rows        0  ->  4
documents mentioning O'Hara (tier 3)           14
O'Hara's own paper greppable                   yes
```

## What this changes for this arc, and what it does NOT

**Does not** retract or confirm anything here. The O2 gate, the mutual-channel
retraction (`b6f0259fe`), the arbitrary-density proof (`bbacee7d9`) and the
orientation-blindness result (`a5694110b`) all stand on their own Lean and are
untouched by what the library holds.

**Does** mean the next pass on this arc can run path 5 for real. In particular
`1905.06064v1` (regularity for critical knots) and `2505.02719v2` (Palais–Smale)
are on exactly the variational question the O2 gate sits in, and **none of them
had been read** when the gate was argued — they could not be.

So: **re-run path 5 before the next "this is open" or "no theorem exists"
declaration on this arc.** The three tiers are cheap now
(`grep -i <topic> library/INDEX.md`, then `summary.json`, then
`grep -rln <topic> library/<doc-id>/sections/`).

## Caution, so the next agent does not over-read this

These are **ingested, not read**. `structure.json` + `sections/` make them
greppable; nobody has adjudicated whether any of them supplies the O'Hara
theorem the mutual channel was said not to need. Holding a source and having
checked it are different claims — that distinction is what `qou-pc85` was
originally about.

## 2026-09-13 — this bean is BLIND to its own successor, and its closing measurement SURVIVES a re-check

Two things, and they point opposite ways. Recording both because the second is a
correction to the line I was building from the first.

### 1. The carrier blocker got an OWNER RULING, and this bean does not know

This bean's terminal state is: every route ends at *"which link is the nucleus?"*,
and `qou-5vhf` establishes the A <= 4 assignments are an admitted AME-driven census
search — so route (2) reaches one kappa point on a fitted carrier and fails this
bean's own no-tuned-constant (CAL-4) gate.

**On 2026-09-08 the owner ruled census OUT and named the replacement**, verbatim:
*"All selection of great words should be done through gamma gamma production and
the semi-definite product solutions at q_0. Shouldn't use census."* That is bean
`qou-ales`, and it has run to **step 10** (PRs #7184, #7207, #7222, #7233), all
sorry-free: the Frobenius-positivity reading selects `beta_Bor` on the whole
interval `1 < q <= 23/20`; the H_6 pp bond `G^3` is selected through branching; the
reading-3 survivors are exactly `3 | k`; and step 10 derives the last measured
quantity of the pp channel in closed form, giving `diproton_unbound_of_response_closed_form`
for every `q > 1` with no measurement.

**Measured: `grep -in "gamma.gamma\|qou-ales\|7184\|7207\|7222\|7233"` on this bean
returns ONE hit, and it is a coincidental digit match inside a number (line 871).**
So the bean whose single terminal blocker is carrier selection carries no record
that carrier selection was ruled on five days ago and has an active arc. Fixed by
this entry.

### 2. But the closing measurement is NOT stale — and I checked because it looked like it was

The natural next move is to ask whether this bean's route-(2) closure is still
valid, because its refutation sits in `he4-link-volume-braid-closure.witness.json`
**computed 2026-07-04**, and the producer's import cone changed after it:
`he4_link_volume_braid_closure` -> `canonical_braid_crossings.atom_canonical_crossings`
-> `mass_at_3A_proper.atom_braid_word_3A`, whose default `intra_order` became
`"borromean"` in `7db032fb48` (2026-09-05). That same commit moved `tr_M(p)` by
45 % and left >= 8 witnesses carrying retired values (`qou-sikd`). Textbook
import-cone drift.

**Re-measured, and the refutation holds** —
`computations/probes/atom_closure_component_count_probe.py`, 5/5, bean `qou-mbbf`:

| isotope | A | comps (borromean) | comps (grouped) | census carrier |
|---|---|---|---|---|
| 2H | 2 | 3 | 3 | Hopf (2) |
| 3H | 3 | **4** | **4** | `8_11` (1) |
| 3He | 3 | **4** | **4** | `L6a4` (3) |
| 4He | 4 | 5 | 5 | none identified |
| 6Li | 6 | 7 | 7 | — |

The two words genuinely differ (asserted, so the invariance is not vacuous) and the
count is identical under both. **Structural reason, not coincidence:** the count is
the orbit count of the induced permutation, and crossing SIGN does not enter it —
the two orderings differ in sign pattern and letter order, not in which
transpositions occur.

**And it is stronger than this bean states.** Not "refuted at the two isotopes where
the answer is checkable" — the closure has exactly `A + 1` components on `3A`
strands at **every** A tested, so the two families agree at no A at all.

### What that leaves

The blocker is real, structural, and not a re-run away. **But it is now a
disagreement between two objects of which only one was ever derived:** the census
carrier (an admitted AME fit, ruled out 2026-09-08) and the `A + 1`-component
closure of the canonical word. This bean has always read the disagreement as
refuting the closure. That reading was reasonable while the carrier was the fixed
point; after the ruling it is the carrier that has no standing.

**Not claimed, and this is the owner's call rather than an agent's:** that `A + 1`
is right. Nothing here derives a binding link, and nothing here reopens route (2) —
its `kappa(A)` gate is still retired (#7080) and its energy machinery still has
nothing un-fitted to consume. What changes is only which of the two disagreeing
objects should be treated as the target.

Volume and geometricity are **NOT** re-measured (`snappy`/`spherogram` absent in
this container); the component count alone decides the identification question.

## 2026-09-13 (later) — the carrier alternative is CLOSED BY MEASUREMENT: the closure is not hyperbolic

The entry above left one question for the owner: since the census carrier is an
admitted AME fit that the 2026-09-08 ruling excludes as a selection mechanism,
should the `A + 1`-component closure of the canonical word become the target
instead? It named the missing input: **is that closure hyperbolic?**

Measured (`computations/probes/atom_closure_geometry_probe.py`, 5/5, SnapPy
calibrated against `Vol(4_1) = 2.0298832128`): **no, and not marginally.** 3H,
3He and 4He are non-geometric with volume exactly 0 in all SIX settings — both
intra-orderings crossed with all three averaging modes — returning `contains
degenerate tetrahedra` on 12/12 randomised attempts each. The 2026-07-04 rows
reproduce exactly under the live word.

**So there is no second candidate.** The closure has no hyperbolic volume to
feed the volume-based binding route; promoting it would delete the route's input
rather than re-base it. This bean's long-standing reading — that the component
mismatch refutes the closure — is correct, and now for a second, independent
reason.

**The blocker restated, sharper than before.** It is not *"which of two objects
is the carrier"*. It is: **the only available carrier is the fitted one**, the
selection mechanism that produced it has been ruled out, and the framework's own
canonical word cannot supply a replacement — refuted from two directions now
(component count, `qou-mbbf`; non-geometricity, here). Route (2)'s machinery
still has nothing un-fitted to consume, and that is now established rather than
inferred from the A<=4 assignment's provenance alone.

**What is still genuinely open**, unchanged: `qou-ales`'s gamma-gamma route
selects WORDS (beta_Bor, the H_6 bond `G^3`) and has not been asked to produce a
binding LINK; the flux leg (eq. 43's topological factor is A-independent, so it
relocates kappa(A) into the per-component flux — a fall of 1.449 across
A = 3...41, derivable from corpus braid geometry, not derived); and `qou-bn8e`'s
self-energy channel via its route (ii).

By-product, filed separately as `qou-v5sr`: the producer's baked `CLOSURE` table
is stale for the two NUCLEON rows (hyperbolic under the live word, recorded
non-geometric), and its own "every mode agrees" comment is false for them. The
volumes are mode-dependent by 2x and are NOT derived quantities — see that bean
before quoting any of them.

## 2026-09-13 (later still) — this bean's OWN TRIP-WIRE IS TRIPPED, by this session's ingest, and the bound it named now exists

The 2026-09-03 upper-bound entry closes with an assertion deliberately left as a
wire: *"the library holds nothing anyway ... **zero** files matching
`ropelength|ideal knot` ... **Asserted so that a future acquisition flips the**
[result]"*. **That acquisition happened today, in this arc's own ingest, and
nobody noticed — including me: I named the flux leg as "next" without reading
the entry that set the wire.**

### Live re-scan, and one self-reference trap avoided

    library/*/sections   7 documents   (was 0)
    library/*/ocr        0
    docs/                0
    computations/        4  <- SELF-REFERENCE, not new hits
    content/             2  <- SELF-REFERENCE, not new hits

The `computations/` and `content/` hits are **this bean's own artifacts**
(`em_linking_upper_bound_precision_budget.py` + its witness,
`MirrorSplitIsASmallFractionOfTheEnergy.lean`) plus two unrelated Frenet/torsion
files. A probe that scans for a term *contains* that term, so a naive re-grep
finds the assertion itself. **The original "zero" was correct.**

All **7** library documents were added **today**, by this session's ingest
commits `d9be1158a9` and `3938aa5ffc`.

### 🟩 And the bound the entry named as missing now EXISTS in the corpus

`library/1-s20-s0166864101002632-main` = **Rawdon & Simon, _Möbius energy of
thick knots_, Topology Appl. 125 (2002) 97-109.**

> **Theorem 8.** If K is a smooth knot in R³ then **E_O4(K) < 4.57 · E_L(K)^{4/3}**

That is an **upper** bound on a Möbius-type energy in terms of a geometric
quantity (ropelength) — precisely what the 2026-09-03 entry named: *"What would
restore a constraint is an UPPER bound, which eq. (43) does not supply."* And
the paper states its own paradigm in terms that cover this arc's kernel:

> *"our goal is partly the theorem itself and partly the paradigm: **any 'energy'
> defined in terms of inverse-square distances should have an analogous bound**,
> with the proof following this model."*

The mutual channel's kernel is `1/sep²`. So the paradigm applies by the source's
own statement, not by analogy I am drawing.

### 🛑 BUT THE ROUTE DOES NOT REVIVE, and the reason is the one the entry gave

That entry is explicit that availability is *"the weaker half of the finding,
not the point"* — the route dies on **precision**. The requirement is unchanged:
the combined slack `(U₁−B₁)+(U₂−B₂)` must beat `ΔE/E ≤ (r−1)/A`, which at
`A = 63` with a generous factor-2 flux ratio is **1.5873016 %**, and the budget
*sharpens 21-fold across the ladder*.

**I have the bound's SHAPE, not its SLACK.** `E < 4.57·L^{4/3}` is an explicit
constant, which is better than the order-of-magnitude estimates the entry
assumed — so the entry's *reason* ("nothing in that literature is tight to a
percent") is now a claim about a bound the corpus can actually inspect, rather
than a general one about the literature. But determining whether it beats
1.587 % needs both sides evaluated on an **actual carrier**.

### So this is the FIFTH independent path to the same terminus

Route (1) pruned (even in `μ̄₁₂₃`). Route (2) → carrier. Route (4) `qou-0hdx`
scrapped → carrier. Flux leg → saturation is prior → the two escapes are one →
carrier. **And now the upper-bound leg, newly supplied, → carrier.**

Combined with today's two measurements — the closure has `A+1` components
(`qou-mbbf`) and is **non-geometric with volume 0 in all six settings** — the
arc's position is: *every path terminates at carrier identification, the only
candidate is the admitted AME fit whose selection mechanism the owner ruled out
on 2026-09-08, and the framework's own canonical word cannot supply a
replacement.*

### What is now genuinely actionable, and it is NOT this bean's

Nothing here moves without a **derived binding link**. `qou-ales` selects
*words* (`β_Bor`, the H₆ bond `G³`) and has never been asked to produce a
*link*. That is the one live question, and it belongs to that bean.

**NOT claimed:** that Theorem 8 is or is not tight enough (unmeasured — it needs
a carrier); that the arc revives; that Rawdon & Simon's paradigm has been
checked against the mutual kernel beyond quoting the authors' own statement.
Beans `qou-mbbf`, `qou-hs0c`; PR #7322.

## CONSTRAINT 3 — ROUTE (2) CANNOT GET ITS MAGNITUDE FROM TOPOLOGY (2026-09-13, qou-dux3)

Route (2) is "Mobius/knot-energy class (nonzero for unlinked pairs; corpus
MobiusEnergy.lean exists)". The hope in that parenthesis is that a knot-energy
bound hands the pairwise channel a parameter-free positive number off the
Borromean topology. It does not, and the reason is now proved rather than
suspected.

MobiusMutualChannel.lean section 9 (17 declarations, sorry-free, all
[propext, Classical.choice, Quot.sound]) derives the LINK analogue of
Bryson-Freedman-He-Wang's Theorem D -- which qou-dux3 had recorded as missing
from the held literature:

    4*pi*|lk(gamma_1, gamma_2)|  <=  E_mutual(gamma_1, gamma_2)

from Gauss's linking integral plus |det(a,b,c)| <= |a||b||c|. Elementary: one
power of |gamma_1 - gamma_2| from the determinant bound cancels the cube in the
Gauss kernel, leaving exactly the Mobius mutual integrand.

WHY IT DOES NOT HELP HERE. Every pairwise lk_ij of the Borromean link is 0
(this bean's own constraint 2, from mirror_split_s3_em_functional_probe.py A3).
So the bound reads 0 <= E_mutual -- and lk_bound_iff_nonneg_of_lk_zero proves
that its conclusion at lk = 0 is EQUIVALENT to section 3's
innerPairEnergy_nonneg, which holds with no hypotheses at all. It adds nothing.

AND NO OTHER TOPOLOGICAL BOUND WILL EITHER. no_positive_uniform_mutual_lower_bound:
no positive constant lower-bounds the mutual pair energy, because the
separatedLink family realises every small positive value via section 3's own
innerPairEnergy_le. Scope (b), invariant cited (the separation bound of
section 1). It excludes TOPOLOGICAL lower bounds only.

WHAT THIS LEAVES ROUTE (2). A geometric magnitude, from a DERIVED
configuration. That is not excluded by anything here and it is now the only
shape route (2) can take. Note the interaction with this bean's gate: a derived
configuration has to reproduce the kappa(A) profile 3.2 -> 2.1-2.3 with no
tuned constant, so "derive the geometry" is the whole of the remaining work,
not a step in it.

RELATION TO CONSTRAINT 2. Consistent, and from the other side. Constraint 2
says an admissible w_ij must be EVEN in mubar_123, killing the linear ansatz.
The Gauss bound is linear in lk, and lk vanishes. Both say the same thing: the
first-order linking channel is blind to the Borromean configuration.

Section 7-8 of the same file separately prove that Mobius invariance FORCES the
inverse-square kernel (uniquely, and on geometrically realisable distance
triples), so route (2)'s kernel is not a modelling choice. The kernel is
settled; the magnitude is the open thing.


## CONSTRAINT 3b — WHERE route (2)'s many-body content must live (2026-09-13, section 9g)

Constraint 3 above is a negative: no topological lower bound reaches the
pairwise channel. Section 9g of MobiusMutualChannel.lean turns it into a
LOCALISATION by composing with this corpus's own pair-locality theorem.

THE INSTINCT THAT IS WRONG, and worth recording because it is the obvious one.
"The Mobius mutual energy is a two-body functional, therefore the channel is
PairLocal, therefore b_3 = 0 by b3_eq_zero_of_pairLocal, therefore route (2) is
dead." The first clause is right; the second DOES NOT FOLLOW. PairLocal
(QOU.Mass.CrossingModelPairLocality) compares a pair's energy ACROSS ASSEMBLIES
-- w3 i j k = w2 i j and w4 i j = w2 i j -- and a two-body functional still
moves when the assembly moves the pair. Being two-body is a statement about the
integrand; pair-locality is a statement about the configurations.

WHAT IS TRUE, 5 declarations, all [propext, Classical.choice, Quot.sound], no
sorryAx; whole file 52/52, lean -DautoImplicit=false -s 65536 exit 0.

  mobiusCrossingModel                     the CrossingModel this channel induces,
                                          one LinkEmbedding per assembly.
  mobiusCrossingModel_pairLocal_of_sep_eq if the assemblies do not move the
                                          pair's separations, it is PairLocal.
  mobius_b3_eq_zero_of_sep_eq             hence b_3 vanishes IDENTICALLY, via
                                          b3_eq_zero_of_pairLocal.
  mobius_b3_ne_zero_forces_moved_sep      contrapositive: any nonzero b_3 from
                                          this channel is ENTIRELY the
                                          assembly's effect on the separations.

AME2020 measures b_3 = +1.4262225 MeV (AmeBindingNotPairwise.ame_b3_eq), so the
hypothesis is not idle.

CONSEQUENCE. Route (2)'s entire many-body content is the configuration change
and nothing else. Read with constraint 3 -- no topological floor -- the two say
the same thing from opposite ends: EVERY NUMBER ROUTE (2) CAN SUPPLY IS A
DERIVED GEOMETRY. That is not a refutation of the route; it is a specification
of what it owes, and it says the route's deliverable is the same object
qou-ales is deriving (gamma-gamma + the confinement SDP at q_0), not a separate
one.

RELEVANCE TO THE b_3 ARC. qou-brng / qou-rwhv / qou-rraz own the extensive term
(measured b_3 = +1.4262 MeV, model exactly 0) and qou-eptr proposes EP/Pachner
as a non-pair-local extensive carrier. Section 9g does not supply that carrier.
What it supplies is the statement that the MOBIUS channel is not disqualified
from contributing -- its b_3 is zero only under a hypothesis (separations
unchanged across assemblies) that a bound configuration does not satisfy.

NOT CLAIMED: that the assemblies DO move the separations in this framework, nor
by how much. That is a geometric measurement section 9g does not make, and it is
the open thing.

## 2026-09-13 — CONSTRAINT 3b's open item is now TRACKED: `qou-a2w5`

Section 9g ends by naming the arc's one precisely-stated open problem — *"that
the assemblies DO move the separations in this framework, nor by how much …
it is the open thing"* — and gives it no tracker. Measured: that phrase occurred
in **exactly one file corpus-wide** (this one), so it was one bean-read away from
being lost inside 1,856 lines.

Extracted to **`qou-a2w5`** with the measurement that decides whether it is
workable today. It is not, and the reason is checked rather than assumed:
`sep` is a **bare field** of `LinkEmbedding` (`MobiusEnergy.lean:228`) carrying
only `sep_symm` / `sep_nonneg` / `disjoint` / `sep_self` — no derivation — and
every concrete `LinkEmbedding` in the tree is a synthetic test family
(`shrinkingLink`, a counterexample; `separatedLink m R`, the family used to
prove no uniform lower bound exists; a bare `Nonempty` witness). **None is a
nucleus.**

**So this is the SIXTH relocation to the carrier blocker** — after routes (1),
(2), (4), the flux leg and the upper-bound leg. Recorded plainly so the new bean
is not read as an independent front.

**What changed is the SHAPE of the requirement, and that is the useful half.**
The carrier blocker was *which census link is the nucleus* — a topological type,
for a hyperbolic-volume lookup. Section 9g needs a canonical **metric**
configuration: separations, not volume. Two consequences worth keeping:

1. `qou-mbbf`'s non-geometricity result does **not** close this. A
   non-hyperbolic link still embeds in `R^3` with perfectly good separations;
   it simply carries no canonical hyperbolic metric. The measurement that
   killed the volume route leaves this one open.
2. The requirement is therefore **strictly weaker** than the volume route's —
   the one direction this arc has not been pushed.

And section 9g's own conclusion matches `qou-mbbf`'s, reached the same day from
the carrier side without contact: **the route's deliverable is the object
`qou-ales` is deriving, not a separate one.** Two independent arrivals.


---

## 2026-09-13 — `qou-9v7t` PINS THIS ARC'S TARGET NUMBER, and neither bean cites the other

Found while correcting `qou-a2w5`'s `b_3` claim (PR #7339). This is a
corpus-grep find, not a derivation: **two beans on the same question, mutually
invisible.**

### The number this arc owes

`qou-9v7t` (2026-08-29, PR #5990,
`computations/b3-charge-decomposition-a3.witness.json`) splits the A = 3
three-body cumulant by isospin and **names the halves**:

| part | value (MeV) | `qou-9v7t`'s own label |
|---|---|---|
| `b3_sym`  | 1.4262225 | *"the strong channel's obligation"* |
| `b3_asym` | 0.3818775 | ***"the EM channel's"*** |

This arc is the **EM-linking** invariant. So the A = 3 figure it owes is
plausibly `b3_asym`, and the widely-quoted `1.4262225` — which `qou-a2w5` and
four `.lean` docstrings cite — belongs to the **strong** channel and is **not**
this arc's target.

**Flagged, NOT concluded.** That route (2)'s `mobiusCrossingModel.b3` is the
asym part rather than the sym part (or neither) is a further read of
`mobiusCrossingModel`, and I have not made it. What is established is only that
the corpus already carries a charge-split with an EM half, and that this arc
does not cite it.

### QUOTE IT TO 5 FIGURES, NOT 7 — measured

The decomposition does **not** close exactly against the A = 3 values
`PairwiseCumulantVanishing.lean:75-76` quotes:

    b3_sym + b3_asym = 1.8081000  vs  b3(3H)  = 1.808100   EXACT
    b3_sym - b3_asym = 1.0443450  vs  b3(3He) = 1.044360   off by 1.5e-5

i.e. `qou-9v7t` computed from a `B(3He)` about **15 eV** below the one that file
quotes. Same class as the 8e-6 MeV residual that file already records on
`b3_sym` ("AME input precision"), and the two are the same defect seen from
opposite ends: sym is low by 7.5e-6 and asym high by 7.5e-6, which is why the
3H sum closes and the 3He difference does not.

**Consequence for this arc:** the EM obligation is `0.38187` MeV good to ~5
significant figures. A route reproducing `0.3818775` to 7 figures would be
matching AME input noise, not physics. Worth knowing *before* a route is graded.

### `qou-9v7t` ALSO STATES THIS ARC'S PREMISE INDEPENDENTLY

Verbatim from that bean:

> the A=3 mirror pair is where the EM channel shows up in binding, and **the
> framework has no EM term in any per-bond factor** (`f_pp = z`, `f_nn = z - h`,
> `f_pn = z - h(1/2 - delta/4)`)

That is this arc's premise — a two-like-charge term `w_ij` absent from the
per-bond factors — reached from the binding side by an agent that was not
working this arc. **Independent corroboration of the premise, from a different
direction.** Note the three factors are charge-*labelled* but carry no charge
*coupling*: `f_pp` and `f_nn` differ by `h`, not by anything electromagnetic.

### THREE CONSTRAINTS ON THIS ARC'S ROUTES, from `qou-9v7t`'s four results

1. **The mirror splitting is the Coulomb displacement energy**, essentially
   exactly: `b3(3H) - b3(3He) = B(3H) - B(3He) = 0.76374` MeV, because the
   pair-additive `3*B(2H)` cancels in a mirror pair. So this arc's A = 3 target
   is not a fitted residual — it is a difference of two measured bindings, which
   is the cleanest kind of target available.
2. **9 of 10 existing candidates get the sign BACKWARDS.** Only the product
   3-bond term is right-signed, and at **21.8%** of the displacement. The
   wrong-signed ones reach 65% magnitude — *worse*, not better. Any new route
   must clear the sign before magnitude is worth measuring.
3. **The current sign is an accident, not a prediction** — two competing non-EM
   sources, `tau_p/tau_n = 1.1600` favouring 3He against a bond-product ratio
   `0.6494` favouring 3H, with different terms dominated by different ones. So
   the framework's present agreement in sign, where it has it, carries no
   evidential weight for this arc.

### THE ABSENCE CLAIM THAT SENT THIS ARC LOOKING, AND IT WAS FALSE

`qou-9v7t` closes: *"what supplies the **EM channel** at A=3 is a second
[question], and nothing in the corpus currently addresses it."*

**The corpus did address it.** This bean was created **2026-08-01**, four weeks
earlier, `in-progress`, with "the two-like-charge EM-linking invariant that owns
the 3He mirror residual" in its own title. So that sentence is an
absence-of-evidence claim that was false when written.

Worth recording for the reason rather than the fault: **corpus-grep path 6
(`.beans/`) was added to AGENTS.md on 2026-08-26 — three days before.** The
first five paths cannot reach a bean, and this arc's statement of the problem
existed **only** as a bean at that date. It is the exact failure mode the path-6
note was written for, landing three days after the fix, and it cost four weeks
of mutual invisibility between two beans on one question.

**Both directions are now recorded**: this entry, and `qou-9v7t` is `completed`
so it takes no update — its "live successor" line stands as a dated record of
what was known then.


---

## 2026-09-13 — §9h LANDED: the charge-antisymmetric content is the configuration change TOO

`MobiusMutualChannel.lean` §9h, two theorems, both sorry-free
(`[propext, Classical.choice, Quot.sound]`; `lean -DautoImplicit=false -s 65536`
exit 0, no output):

* `mobius_b3_congr_of_sep_eq` — two instantiations agreeing on the **pair and
  triple** separations have equal `b_3`. `Lquad` is unconstrained: `b_3` is
  `triple - (pair + pair + pair)`, so the four-component assembly never enters.
* `mobius_b3_differs_forces_sep_differ` — contrapositive: **any** difference in
  `b_3` forces the separations to differ.

**The argument is one observation about the signature, not new machinery.**
`mobiusCrossingModel` takes **no charge argument**: its inputs are link
embeddings and the arclength `s`; `CrossingModel` carries `w2`/`w3`/`w4` and
nothing else; `toBindingMap` is built from those three. There is no point in the
chain where a proton differs from a neutron — **two nuclei are two
instantiations of one functional.**

**What it buys the arc.** `qou-9v7t` records that the framework has **no EM term
in any per-bond factor** (`f_pp = z`, `f_nn = z - h`,
`f_pn = z - h(1/2 - δ/4)` — charge-*labelled*, not charge-*coupled*). §9h says
route (2) **does not need one**: whatever charge-antisymmetric number this
channel can supply is a derived geometry, exactly as §9g found for the many-body
number. **One obligation, not two.** That is a narrowing of the arc — the EM
target and the many-body target collapse onto the same missing object — and it
is emphatically **not** a closure.

**NOT CLAIMED** (in the section docstring, not only here): that the mirror
partners' separations **do** differ in this framework, nor by how much. Same open
item as §9g, now reached from the charge side as well. §9h is **not** a
prediction of `b3_asym`; it says where any such prediction would have to come
from.

**Scope — the arity caveat is real.** `CrossingModel` is `Fin 4`-indexed, so
`b_3 i j k` is a triple's cumulant *inside a four-component model*, while the
mirror pair ³H/³He is A = 3. The theorems are stated for two **arbitrary**
instantiations, which is what is proved; reading them as ³H and ³He is an
interpretation that carries a spare fourth component with it.

**Lean caught the first attempt, which is the point of writing it in Lean.**
`BindingMap` is in namespace `QOU.Mass.PairwiseCumulantVanishing`, so the
unqualified `simp only [BindingMap.b3, …]` was an unknown identifier, the `b_3`
never unfolded, and the `rw` chain then reported "did not find an occurrence" —
an error that reads like a wrong lemma and was a wrong *name*. Rewritten to bind
the six `innerPairEnergy_congr_of_sep_eq` instances as `have`s and pass them to
`simp`, which is also robust to rewrite order.


---

## 2026-09-14 — 🛑 ROUTE (1)'s LENGTH-3 RUNG IS CLOSED BY MEASUREMENT, and this bean does not cite the measurement

Third mutual-invisibility case on this bean in two days (after `qou-9v7t` and
`qou-a2w5`). Corpus-grepped: **this bean cites neither
`computations/probes/milnor_mubar_vanishes_on_every_triple_probe.py` nor bean
`qou-2g9j`**, and that probe answers route (1) directly.

### The measurement

`milnor_mubar_vanishes_on_every_triple_probe.py` (bean `qou-2g9j`, successor to
`qou-768r` route 3) computes `μ̄` on **every triple** of the canonical atom word's
closure:

> **`μ̄ = 0` on EVERY triple, in BOTH crossing-resolution branches, for ²H, ³H,
> ³He, ⁴He, ⁶Li, ⁸Be, ¹⁰B** — across all three indeterminacy classes
> (`Δ = 0` structural, `Δ = 2` the residual, `Δ = 1` no information by
> definition).

**Its positive controls are what make the null worth anything**, and they run
the *same code path*: the Borromean rings (closure of `(σ₁σ₂⁻¹)³`) asserted
**nonzero**, the Hopf link asserted at `μ = 2, lk = 1`. So the zeros are a
result, not a broken implementation.

**Re-run this session: 5/5 assertions pass**, including
`triples_of_the_carrier_with_NONZERO_mubar = 0`. Needed
`PYTHONPATH=computations` — it is one of the `_path_bridge` bootstrap scripts
(`qou-0e1t`).

### Why this closes route (1)'s length-3 rung, and it is NOT the chirality argument

The two existing prunes constrain the **shape** of `E_EM` as a function of
`μ̄₁₂₃`: odd is forbidden (`odd_symmetric_functional_vanishes`), and the sign is
invisible (`exchange_symmetry_forces_agreement_on_pm_one`). What survived was
the **even** branch — `|μ̄₁₂₃|`, `μ̄₁₂₃²` — kept alive by
`even_symmetric_functional_can_be_nonzero`, whose witness `F m = m²` is nonzero
**precisely because the Borromean sits at `μ̄₁₂₃ = ±1`**.

**The derived carrier does not sit at ±1. It sits at 0.** So `F(0) = 0` for that
witness, and for every functional `F` the value is the single constant `F(0)` at
**every** isotope. Two consequences:

1. **No charge-antisymmetric content.** `b3_asym` would be
   `F(μ̄(³H)) − F(μ̄(³He)) = F(0) − F(0) = 0`.
2. **No `κ(A)` profile.** A constant cannot produce an A-dependent one, and
   `κ(A)` spans A = 3…63.

This is **stronger than the chirality prune and independent of it** — it does not
care whether `F` is even, odd, or neither.

### The escape it closes

"Use a different triple" / "use a symmetric function of all of them" is the move
an author reaches for here, and it does not work: the probe measured **every**
triple, so the whole vector is zero and any functional of the vector is equally
constant. Formalised below rather than left as prose.

### 🟢 SETTLED: my question (b) — spatial vs isospin mirror — and the answer is moot

I asked whether `exchange_symmetry_forces_agreement_on_pm_one` blocks the EM
target, since it constrains behaviour under one reflection while `b3_asym` is a
p↔n difference. **Read at the source: `swappedLongitude` exchanges "the two
like-charged components"** — identical-particle exchange, neither a spatial
mirror nor p↔n. So the two reflections are **genuinely different** and the
chirality prune does **not** reach `b3_asym`.

**But it does not matter**, because the vanishing above kills the channel
regardless of reflection. Recorded because the distinction is real and a future
agent will otherwise re-ask it.

### 🛑 SCOPE — and this is where route (1) is NOT dead

Scope (a) **on the derived carrier as computed**, inherited verbatim from the
probe, which states it itself: it does **not** say Milnor invariants vanish on
every carrier (the Borromean control in that same file is a counterexample), and
**it does not touch invariants of length > 3**.

**Route (1)'s own title is "higher-order Milnor / third-order helicity", so
length > 3 IS its stated scope.** What is closed is the **length-3 rung**. And
there is a structural reason the next rung is the natural one: when all length-3
Milnor invariants vanish, the length-4 invariants become **well-defined with
lower indeterminacy**. So the vanishing is not only a prune — it is what makes
the next rung askable.

**NOT CLAIMED:** that any length-4 invariant is nonzero on this carrier
(unmeasured); that route (1) is dead; that the carrier is final — it is not, the
census assignments are retired (`qou-ales`, owner ruling 2026-09-08).

### 🛑 AND THE COMMITTED WITNESS IS STALE IN ITS COUNTS — recorded for `qou-2g9j`

Re-running reproduces the **headline** but not the **population**:

| assertion | committed | fresh (2026-09-14) |
|---|---|---|
| `triples_of_the_carrier_with_NONZERO_mubar` | 0 | **0** ✔ |
| `delta_2_triples_examined` | **256** | **173** (−32.4 %) |

`Δ = 2` is the class the probe's own docstring calls *"THE RESIDUAL — one bit
available, and it is 0"*, so the residual population itself shrank by a third.

**Cause: import-cone drift, not a producer edit.** The producer's only commit
since (`6b2692f7b9`) *creates* the file on this path — a rebase artifact, +328
lines, no content edit — while `canonical_braid_crossings.py` /
`mass_at_3A_proper.py` moved three times in the same window (`ee1ff95d6a`,
`9cef96fbf0`, `99e2ddc1d9`). The canonical braid word changed underneath a
source-stable producer: exactly the class AGENTS.md flags as **invisible to
`git diff <producer>`**.

**Witness deliberately NOT committed.** The fresh run also **degrades the
environment block** — this container lacks `clarabel`, `scipy`, `sympy`, and the
producer's own guard says so: *"the numbers can be identical while the
provenance silently degrades."* Reverted rather than commit a weaker record. The
count correction belongs in a run with the full environment.

### Method note against myself

Four times this session I wrote a conditional label into a command
(`"(empty above = none found)"`) **before** seeing its output, and was wrong every
time — twice on greps that returned hits, once on a witness diff that had
substantive changes, once on a producer-history check that found a commit. A
verdict baked into an invocation is not a check. Stopped.

### 🟩 FORMALISED — three theorems, `MilnorTripleLinkingMagnus.lean`

`lean -DautoImplicit=false -s 65536` → **exit 0, zero bytes of output**.

| theorem | axioms |
|---|---|
| `constant_of_vanishing_invariant` | **none at all** |
| `constant_of_all_triples_vanishing` | `[Quot.sound]` |
| `no_asymmetry_of_all_triples_vanishing` | `[propext, Quot.sound]` |

All sorry-free. The second is the one that closes the escape — it quantifies over
a functional of the **whole family** of triple invariants (`F : (κ → ℤ) → ℤ`),
not one triple, so "use a different triple" and "use a symmetric function of all
of them" are both covered.

**The docstring says plainly that the mathematical content is the HYPOTHESIS,
not the proofs.** The proofs are a rewrite and a `funext`; they are short because
the work was the computation. Writing them down buys two things: the prune is
checkable against the probe by a reader who has neither in context, and the
escape is closed in the statement rather than in prose that a later agent can
reasonably not find. Recorded this way deliberately, so it is not mistaken for a
theorem doing work it is not doing.



---

## 2026-09-14 — ROUTES (1) AND (2) NOW HAVE THE SAME TERMINUS, FOR THE SAME REASON

Recorded as a synthesis, **not** a new theorem. Route (2)'s content is already
localised by §9g (many-body) and §9h (charge-antisymmetric); adding further
`X forces Y` relocations would be padding, and AGENTS.md's Lean discipline says
so explicitly. What is worth writing down is that the two routes converged today.

| | topological channel | what remains |
|---|---|---|
| **(1) Milnor** | **EMPTY — measured.** `μ̄ = 0` on every triple of the derived carrier (`qou-2g9j`). | length ≥ 4, newly well-defined |
| **(2) Möbius** | **UNREACHABLE — proved.** `no_positive_uniform_mutual_lower_bound`: no topological lower bound reaches the pairwise channel (CONSTRAINT 3, `qou-dux3`). | a metric configuration (`sep`), `qou-a2w5` |

**Different mechanisms, same shape.** One channel is empty by computation, the
other unreachable by proof — and in both cases what is left is **geometry the
corpus cannot currently supply**. Route (3) is a third instance: its grading
collapses to degree 0 on the finite `H_{3A}(q)`, and reaching the affine object
needs the von Neumann inductive limit, which `markov-trace-inductive-limit.lean`
marks as open R&D.

**So all three routes are blocked on a MISSING OBJECT rather than on a wrong
idea**, and the three missing objects are different: a higher-length invariant, a
metric configuration, an inductive limit. That is the arc's real state, and it is
more useful than any per-route verdict.

**The one that may close on its own:** route (1) at length ≥ 4. Its input is a
topological invariant **of the braid word**, and `qou-ales` produces words — so
unlike (2) and (3) it needs no infrastructure the corpus lacks, only a
computation nobody has run. **NOT CLAIMED** that any length-4 invariant is
nonzero here; that is unmeasured and is the obvious next probe.


---

## 2026-09-14 — 🛑 MY OWN "NEXT" WAS A FIT, and the ladder is UNASKABLE

**Owner challenge, verbatim:** *"Why are we doing a census?! That's sounds like
fitting. We should be in lean deriving"*

**On the literal reading I was not proposing a census** — every use of the word in
that hand-off was the *retired* census (`8₁₁` / `L6a4`, `qou-5vhf`, ruled out
2026-09-08). The proposal was to compute an invariant of the **derived** word.

**But the challenge is right about the thing underneath, and the entry above is
withdrawn.** "Compute length 4, and if it vanishes, length 5…" is walking the
Milnor ladder until a rung is nonzero — **selection of a discrete parameter
against the target**, which the anti-fit directive names explicitly
(*"Sweeping a discrete parameter for accuracy… Optimal against what? The data."*).
The length would have been chosen by the residual. Same defect as a census, one
level up.

### The derivation that replaces it — the ladder is not merely unwalked, it is unaskable

**Step 1 — the element is not a braid. PRIOR ART; cite it, do not re-derive.**
[`braids-and-knots/markov-disambiguation.md`](../folio/quantum-observable-universe/braids-and-knots/markov-disambiguation.md)
(PR #5765, **2026-08-25**):

> `tr_M` is defined on ALL of `H_n(q)` … no braid, no closure, and no topology
> are needed for the number to exist. What the closure supplies is the
> INTERPRETATION. … for `W` NOT in the image of `ρ : B_n → H_n(q)`, `tr_M(W)` is
> a well-defined number **WITH NO LINK BEHIND IT**.

`computations/binding_is_not_a_link_invariant_probe.py` (bean `qou-brng`)
measures **which** letters leave the image, and the result is sharper than the
tempting "the `d ≠ 0` ones" — under the module convention `σ⁻¹ = σ − h`, a
`d = −h` letter **is** a generator:

    pp   d = 0                 σ_g       IS a braid generator
    nn   d = −h                σ_g − h   IS one too (= σ_g⁻¹)
    pn   d = −h(1/2 − δ/4)               is NOT — the only bond letter that isn't

**Step 2 — the family's LOWEST rung is branch-dependent. MEASURED from the
committed witness, not quoted from the docstring.** To get a link at all the
averaged letters must be **resolved**; `milnor-mubar-vanishes-on-every-triple.witness.json`
records two resolutions, and the indeterminacy classes — determined by the
pairwise linking numbers — differ at **every** isotope:

| isotope | `delta_1` σ → σ⁻¹ | `delta_2` σ → σ⁻¹ |
|---|---|---|
| ²H | 1 → 0 | 0 → 1 |
| ³H | 2 → 0 | 2 → 4 |
| ³He | 3 → 0 | 1 → 4 |
| ⁴He | 5 → 0 | 4 → 9 |
| ⁶Li | 13 → 0 | 12 → 25 |
| ⁸Be | 25 → 0 | 24 → 49 |
| ¹⁰B | 41 → 0 | 40 → 81 |

**14 of 14 compared fields differ.** The producer states the cause itself: *"lk
is branch-dependent, so the Delta classes differ per branch."* So `lk`, the
**length-2** member, is not a function of the element.

**Step 3 — therefore `μ̄₁₂₃ = 0` on both branches is VANISHING, not
well-definedness.** It agrees across resolutions *because it is zero*. The family
was already broken at length 2, so that agreement carries no information about
any higher rung.

**Step 4 — so a nonzero higher rung would be branch-dependent**, and consuming it
would require **choosing a resolution**. That choice is a free parameter selected
against the target. **That is the fit, and it is structural** — not a discipline
failure to be avoided by care, but a property of the object.

### 🟩 FORMALISED — four theorems, `MilnorTripleLinkingMagnus.lean`

`lean -DautoImplicit=false -s 65536` → **exit 0, zero bytes of output.**

| theorem | axioms |
|---|---|
| `not_wellDefinedOnResolutions_of_ne` | **none at all** |
| `not_familyWellDefined_of_one_member_ne` | **none at all** |
| `wellDefined_of_const_zero` | **none at all** |
| `familyWellDefined_nondegenerate` | `[propext, Classical.choice, Quot.sound]` |

`not_familyWellDefined_of_one_member_ne` is load-bearing: **one** branch-dependent
member refutes the whole family, so the `lk` measurement settles the ladder
*before* any higher rung is computed. `wellDefined_of_const_zero` states the
companion — a vanishing member is well-defined **vacuously** — which is what makes
the μ̄₁₂₃ result non-evidence. The fourth is the anti-vacuity witness in both
directions (a constant family satisfies the predicate; a two-resolution identity
family does not), so the predicates are neither unsatisfiable nor trivial.

### What this does to the trichotomy

**Routes (1) and (2) both need a LINK; route (3) does not.** Milnor invariants are
link invariants; Möbius energy is an invariant of an **embedding**. The canonical
object is neither — it is an element of `H_{3A}(q)`. `tr_M` is a *linear
functional on the algebra*, so it evaluates on the superposition directly. That is
why `tr_M(W_atom)` has a value and `μ̄(W_atom)` does not.

**So "the carrier blocker" is a CATEGORY MISMATCH, not a missing lookup.** Six
routes terminated at *"which link IS the nucleus?"* and the answer is that the
question has no referent: there is no map `H_n(q) → Links`, only
`ρ : B_n → H_n(q)` running the other way, and the element is outside its image.
Route (3) is the one asking in the right category — and is blocked on
infrastructure (the von Neumann inductive limit) rather than on a category error.

**NOT CLAIMED:** that no invariant of the element exists (`tr_M` is one); that
some Milnor invariant could not be constant across **all** `2^(2A+1)` resolutions
(only two are recorded, and one member's constancy is not the family's); that
route (1) is refuted for a future carrier that IS a braid. What is derived is
that on the carrier as built, the family is not well-defined.

### One tension, flagged not resolved

`binding_is_not_a_link_invariant_probe` says the word *"leaves the braid image
exactly at the p-n bond"*, while `atom_braid_word_3A`'s docstring describes the
per-**nucleon** block as eleven letters *"two of them averaged (`σ − (h/2)·1`)"* —
and `−h/2` is in the outside set. Different letters (inter-nucleon bond vs
intra-nucleon core), and a `Z ≥ 1, N = 0` word's status turns on it. **Does not
affect anything above**: every nucleus this arc targets has both a proton and a
neutron. Recorded so the next reader does not have to notice it twice.


## Can an EM coupling enter `H_n(q)` AT ALL — six-path survey, 2026-09-14

Owner selected this alongside the even-in-`T_z` Lean front. Survey run as a
corpus-grepper pass; `corpus_search` (path 0) was **not available** — the
`paper-assistant` MCP failed to connect — so every absence below is grep-scoped.
Items marked ✅ I verified directly against the file; the rest are the survey's.

**The premise this arc has been running on is true but NARROW.** "The framework
has no EM term in any per-bond factor" is a statement about `interface_factor`,
not about the framework. EM is already inside the q-algebra twice:

- `prop:em-coupling-projection`: `α_EM(q) = q⁻¹/([9]_q·[10]_q)`, with sorry-free
  bar-parity Lean (`QOU/Interactions/EmCouplingBarParity.lean`).
- `computations/coulomb_energy.py` — *"the EM-sector binding term"*,
  `E_C = (3/5)Z(Z−1)·α_EM·ℏc/R` with `α_EM` **derived** (CODATA only until
  2026-08-09) and `R₀ = λ̄_π = ℏc/m_π`, the CAL-3 length; the empirical
  `r₀ = 1.2 fm` is explicitly *not* the default. The residual import is the
  **form** (uniform charged sphere), not the constants.

So the open question is **coupling, not existence** — and specifically coupling
to the *per-bond* factor, which is the one place it has never been done.

**Two scope-(b) exclusions that bound this arc, with invariants named:**

1. `QOU/Mass/BraneTowerIsospinBlind.lean` — if the per-subset weight is
   **Markov-invariant**, two isobars on the same `3A` strands get an identical
   tower term, so the contribution to mirror splitting is exactly **0**. Invariant
   `tr_M(σ_i) = z`. **Anything Markov-invariant cannot carry charge** — which is
   why a charge coupling has to be a non-Markov-invariant functional. This is the
   sharpest constraint on the whole arc and it was not cited here before.
2. `qou-556v` (completed) — Coulomb cannot come from **any bounded-degree** bond
   graph. Handshake lemma `2E ≤ dn` ⇒ covered-pair share `≤ d/(Z−1) → 0`; at
   Z=82, chain 2.47%, deltahedra 6.17%, close packing 14.81%. Lean
   `QOU/Hecke/BoundedDegreeCoulomb.lean`. Owner reframe: *"it is the FALLOFF, not
   the coupling"* — the q-derived channels are Yukawa (`μ = −ln b`, `b < 1`) and
   the photon is the massless boundary, a different growth class `Θ(n²)`.

**An even-in-`T_z` bond has already been built, and the obvious repair is priced
and LOSES:**

- ✅ `qou-nial` / `bond_rule_dashboard_comparison_probe.py` — the charge
  **product** rule makes the strong channel exactly charge-symmetric
  (`prodRule_like_pairs_are_strong_baseline`), and over 12 nuclei ²H–⁵⁶Fe mean
  `|ln(model/AME)|` goes **0.808 → 0.940**: worse. Its A=3 mirror match is *"a
  flat line crossing a rising curve"* — flat in `A`, identical at `A = 7` where
  the observed splitting has doubled. Own recommendation: **do not switch.**
- `gg_production_bond_probe.py` — replaces every inter-nucleon crossing with the
  flavour-blind `σ_avg = σ − (h/2)·I`, the *same* factor for pp/pn/nn, i.e.
  exactly even in `T_z`. The 78% `L_nn/L_pp` asymmetry collapses toward 0 and
  charge symmetry then breaks only at `δ ≈ 0.14%`. Not wired (gated on the s5-so3
  keystone). **Note the timing:** the 2026-09-08 owner ruling (`qou-ales`) makes
  γγ pair-production construction canonical for braid-word selection, and this
  probe is that ruling applied to the bond layer, written before it.

**Grading status.** The framework's interface grading is `T₃` (odd) — the audit
`2026-08-16-interface-graded-by-t3-but-the-physics-is-graded-by-t.md` says so in
those words, and notes the `T` (even) split already exists algebraically as the
Hecke spectral projectors `P±` with scalars `y_(2)`, `y_(1,1)`, needing **no new
parameter**, and is unused. **Absence (searched, not found):** no `U(1)` factor,
no charge operator, no `T_z` grading attached to an algebra element anywhere in
`lean/QOU/`. So `qou-9v7t`'s "charge-labelled but not charge-coupled" is
confirmed for the bond layer specifically.

**Library gap found in passing:** `library/arxiv-nucl-th-0409040v2/` is the
**Tjon line** paper (Nogga/Epelbaum et al.) — held, `ocr`-tier, and **not in
`references.ts`**, while `docs/audits/2026-08-07-l2-closure-attack-options-non-em-terms.md`
§A7 says *"Tjon appears once, undeveloped"* without knowing the source is held.

**Net for this arc:** route (3) is not refuted and is now better bounded. What is
open is narrower than "can EM enter" — it is *a non-Markov-invariant,
exchange-sensitive per-pair functional that couples charge inside the algebra
rather than labelling it outside*. Bean stays `in-progress`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-14 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
