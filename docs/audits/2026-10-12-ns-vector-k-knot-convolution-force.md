# NS vector K: knot convolution (#) as the external force

Date: 2026-10-12. Bean: `qou-m535` (parent `qou-vo9t`). Siblings: `qou-ocof` (rescue),
`qou-0ueg` (unforced attack vectors).

**Owner idea, verbatim:** *"another option... look at knot convolution # as being the
'force' (see sibling 'ILP/SDP') and this is then more like openai..."*

**Verdict, first.** The corpus has **no object** that would turn a knot, a braid word or an
ILP/SDP selection into a vector field `f(x,t)` on `R^3` or `T^3`. Building that map is the
first missing step. The second missing step is the whole analytic content of any forced
blowup theorem: keeping the residual `f` smooth through the blowup time `T`. Nothing in the
corpus bears on that, and the corpus's own selection program is proved degenerate.

As stated, the proposal is outcome **(d), does not work**. A narrow **(a)** is honestly
statable: a *conditional* forced conjecture that names its missing dictionary. Its only value
beyond the reported analytic construction would be a topological *label* on the seeds of the
cascade. Do **not** add it to the chapter without an owner decision.

Tags: **[D]** derived here · **[S]** standard, cited · **[C]** asserted in the corpus (file:line)
· **[H]** heuristic · **[O]** open.

---

## 1. What "knot convolution #" and "ILP/SDP" are in the corpus

The phrase names three different objects. None of them is spatial or temporal.

**1a. `#` is connected sum of knots** [C]. `braids-and-knots/knot-notation-convention.md:13`
says *"The connected sum is $\mathfrak{K}_1 \mathbin{\#} \mathfrak{K}_2$."* A Hopf-linked
variant `#_Hopf` also appears in `knots-particles-confinement/hadron-operations-closure.md:8`.
Standard fact [S]: the Jones polynomial is multiplicative under `#`. A composite knot
therefore carries no information its prime factors do not.

**1b. "Convolution" is the q-shuffle product `*_q` on the substrate Hopf algebra** [C].
- `mass-theory/hq-bi-filtration.md:15-20` defines the bi-filtration as `H_q^{(n,K)} = { α ∈ G^{(n)} : e_{λ_K} α e_{λ_K} = α }`. Here `n` is the iterated-integral depth and `K` is a knot class, entering only through the central idempotent of its dominant Hecke cell `λ_K`.
- `hq-bi-filtration.md:50`: the product `*_q` sends `(n₁,K₁) × (n₂,K₂)` into a sum over `(n₁+n₂, K')`, where `K'` *"ranges over cell-mergings"*.
- `knot-indexed-convolution-grid-table1-data.md:8` records the same rule.
- `knot-indexed-convolution-grid-context.md:3-5`: knot-indexed operations are **depth-0 algebraic** and acquire transcendental content *"only post-realization via τ_arch"*.

So `*_q` is a product on an algebra of q-polylogarithmic symbols. It has no base space, no
scale and no time.

**1c. The "ILP/SDP" is two different programs, and the corpus says so itself** [C].

1. **The continuous operator-selection LP** (`prop:operator-selection-lp`, `mass-theory/operator-selection-lp.md:1-26`).
   - Variables: `x ∈ R^{n!}`, the normal-form coordinates of an element of `H_n(q)`.
   - Objective: `min Σ t_i x_i`, where `t_i = tr_M(b_i)`.
   - Constraints: the net constraint `Σ x_i = n_target`, Frobenius positivity `Gx ≥ 0`, and boundedness.
   - Duals: `(y₀*, y*)`, the dual program at `:58-70`.
   - **It is proved degenerate** (`:34-56`). Since `b₁ = 1`, the first row of `G` *is* the objective, so the optimum is identically 0 and `y₀* = 0` (*"the net constraint carries no shadow price"*, `:46`). The minimiser set is a positive-dimensional face with at least 6 vertices at `n = 3`, and *"which vertex a solver returns is a property of its pivoting rule"* (`:55-56`). The block states at `:31-32` that the program *"is not"* a selection principle.
2. **The finite knot-operator ILP** (`computations/universal-ilp.py:5-6`; `computations/qbeta/qbeta_knot_operator_ilp_ohara_cost_probe.py:6-9`).
   - Variables: `x_K ∈ {0,1}` over a *finite catalogue* of braid words.
   - Constraints: `Σ x_K = 1`, and reading-3 feasibility of the dressed element.
   - Objective: `min E(K)`, where `E` is the crossing count or O'Hara energy, with tiebreaker `min |tr_M|`.
   - It is solved by exhaustion and has no LP relaxation (`ohara:11-14`).
   - Two caveats are recorded on the probe itself. First, the count objective *"picks only the LENGTH"* and the `|tr_M|` tiebreaker *"is silently doing the real selection"* (`ohara:53-56`). Second, `universal-ilp.py` aborts at Level 4 on an undefined function (`:14-30`, bean `qou-uilp`).
   - The H₆ probe (`qbeta_knot_operator_ilp_h6_tower_probe.py:4-16`) records that the H₃ catalogue cannot even contain the γγ operator.

**What the ILP selects** [D, from 1c]: one braid word from a finite list, at one Hecke level.
The selection is driven by length plus a trace tiebreaker. It does not output a scale, a time,
an amplitude or a spatial profile. There is **no** sequence of levels with shrinking scales,
and the only dual-bearing program has zero shadow price.

## 2. Is there a map from a knot or braid word to a vector field?

**Not in the corpus** [C, absence measured on the surfaces named here].

- `fluid-dynamics/braid-fluid.md` is a `remark` (`braid-fluid.ts:3`), and its table (`braid-fluid-table-data.md:1-9`) is a dictionary of *interpretations*: braiding ↦ "half-twist vortex exchange", Markov trace ↦ "topological helicity". The only mathematical statement in it is standard [S]: filament configurations have `π₁(Conf_n/S_n) = B_n` (`braid-fluid.md:10`). That is a statement about *homotopy classes of motions*. It is not a map from braid words to velocity fields.
- Neither `q-navier-stokes.md` (`:4-36`) nor `ns-classical-formulation.md` has a forcing term. `ns-obstruction.md:15` now states that the chapter's problem is the **unforced** one, alternatives (A)/(B).

Absence scope: I searched the fluid-dynamics chapter, `mass-theory/*convolution*`,
`*operator-selection*`, beans matching `ILP`+`convolution|connected sum` (only `qou-m535`
itself), and branches `ns-attack`, `ns-rescue` and `ns-followup` (none touches forcing). I did
not run a full `library/` grep. "The corpus has no dictionary" is therefore measured on those
surfaces; "none exists" is not claimed.

**The standard dictionaries that do exist** [S], all from outside the corpus. They are
already mapped in `docs/audits/2026-10-12-ns-attack-vectors-unforced.md:49,81-83`.
- Enciso–Peralta-Salas: any link is realised by the vortex lines of a steady Euler or Beltrami field.
- Enciso–Lucà–Peralta-Salas: smooth NS solutions create and destroy vortex knots in arbitrarily short time **while remaining smooth**.
- Etnyre–Ghrist: rotational Beltrami fields are Reeb fields. The rescue audit (`2026-10-12-ns-rescue-reformulations.md:180`) shows the model's own Reeb field gives a **globally smooth** NS solution `e^{-νt}V`.

So the knot-to-field map the proposal needs exists in the literature. It points toward
**regularity**: knot type is neither conserved by viscous NS nor an obstruction to smoothness.

## 3. The structural comparison with the reported cascade

The OpenAI paper is unverified and relayed by the owner (bean `qou-ocof:40`). It is not held
in `library/`, and nothing below relies on it being correct.

| Reported construction | Nearest corpus object | Match? |
|---|---|---|
| Self-similar anisotropic axisymmetric vortex core | none (the corpus works on Bring and `M = PSL₂`, not axisymmetric `R^3`) | no |
| Cascade of oscillatory pulses at shrinking scales `λ_k → ∞` | depth tower `G^{(0)} ⊆ G^{(1)} ⊆ …` (`hq-bi-filtration.md:5-6`); iterated `#` / `*_q` | **formal only** [H]: depth is transcendence degree, not spatial frequency |
| Each level chosen to cancel the leading residual | one ILP selection per level | **no**: the ILP has one level, its LP form is degenerate, and its objective is a knot energy, not a residual |
| Reynolds stress `⟨u'⊗u'⟩` balancing the residual | Frobenius / Gram pairing `G_ij = tr_M(b_i b_j)` | [H] analogy only: both are quadratic pairings, but no map exists between them |
| Exponentially small seed forces amplified by Rayleigh/centrifugal instability | none | no: the corpus has no linear-instability analysis on any flow that could blow up |

**The one honest point of contact** [H]: an iterated tower of operations, one selected per
level, is the *shape* of a multiscale cascade. Tao's averaged-NS blowup (JAMS 29 (2016)) is the
standard precedent for "design the cascade combinatorially, then prove the analysis" [S]. In
Tao's case all the difficulty lay in the analysis, and the combinatorics did not transfer to
true NS. The shape match carries no estimate.

## 4. What a non-vacuous forced statement must prove

**4a. The residual trick** [D, standard]. For any smooth `u` on `[0,T)` with `div u = 0`, set
`f := ∂_t u + (u·∇)u + ∇p − νΔu`. Then `(u,f)` solves forced NS. Two consequences:
- "There is a force making the flow blow up" is trivially true on `[0,T)`. Take any smooth `u` with `‖u(t)‖_∞ → ∞`.
- Fefferman's (C)/(D) require `f` smooth on `R^3 × [0,∞)` (with decay on `R^3`), so in particular smooth **through and after `T`**. The whole theorem is the statement that the singular part of `f` cancels.

**4b. Smoothness forces the seeds to be superpolynomially small** [D]. Write the force as
`f = Σ_k f_k`, with `f_k` at frequency `λ_k → ∞`, amplitude `a_k`, and unit-scale profiles.
- Then `‖f_k‖_{C^m} ≍ a_k λ_k^m`.
- So `f ∈ C^m` requires `Σ_k a_k λ_k^m < ∞`.
- `f ∈ C^∞` therefore requires `a_k = O(λ_k^{-m})` for **every** `m`.

The force cannot *drive* the cascade. It can only *seed* it, and every unit of growth must come
from the nonlinear and linearised dynamics. This is consistent with the relayed "exponentially
small forces amplified by instability" [H, since the source is unverified]. It means the content
of a forced theorem lives in the **amplification estimates and the error control**, not in the
choice of seeds.

**4c. Consequence for the proposal** [D from 4b + §1]. The proposal would at best do one thing:
assign to each level `k` the knot or braid label of the seed `f_k`, chosen by the ILP. Two
problems follow.
1. **The selection is unconstrained by the dynamics.** Viscous NS changes knot type freely and smoothly (Enciso–Lucà–Peralta-Salas [S]), so the label of a seed is not dynamically protected. Nothing forces the knot type of `f_k` to persist into `u`.
2. **It is selection against the target.** Choosing each seed *because* the resulting flow blows up is the residual trick moved to a discrete alphabet. Under AGENTS.md "NO FITTING, EXCEPT CAL-1/2/3", it is selecting an object because it reproduces the target. That is legitimate in analysis, where Tao and the relayed paper both design their cascades, **only** when the smoothness of `f` and the amplification are then **proved**. A knot label adds no proof obligation and discharges none.

**4d. Does anything in the corpus bear on 4a/4b?** [C]. No. The corpus's NS results concern the
obstruction `NS(A)` built from `χ(A)`, and their status after the item-3 retraction is recorded
in `2026-10-12-ns-chain-after-item3-retraction.md`. The corpus has no Sobolev or energy
estimate for classical NS on `R^3` or `T^3`. Its q-side regularity blocks (`q-bkm-criterion`,
`q-aubin-lions`, `q-ns-wellposedness`) concern the q-system, and none has a forcing term.

## 5. Options

**(a) Honest conditional conjecture** [O]. *Conditional on* a dictionary `Φ` from braid words
`β` (with scale `λ` and amplitude `a`) to smooth compactly supported divergence-free fields
`Φ(β; λ, a) ∈ C_c^∞(R^3)` — **which the corpus does not have**:

> There exist braid words `β_k` (one per level) and `λ_k ↑ ∞`, with `a_k = O(λ_k^{-m})` for all `m`, such that NS forced by `f = Σ_k Φ(β_k; λ_k, a_k) χ_k(t)` from `u(0) = 0` has `‖u(t)‖_∞ → ∞` as `t ↑ T`.

This is a **dependent** conjecture, with `Φ` as its explicit hypothesis. It is strictly weaker
than the reported theorem, which needs no braid labels. If the report is correct, the
conjecture is true for the trivial reason that the reported seeds can be relabelled. It is a
well-posed statement, but it adds **no** content beyond the analytic theorem.

**(b) What it could add beyond the analytic construction** [H]. Only one thing would: if
*topological* data of the seeds (linking, helicity, `tr_M` at `q₀`) **constrained** the
amplification rate, for example a lower bound on growth in terms of `J_K`. No such statement
exists in the literature I know or in the corpus. The 2D fact that point vortices preserve
braid type [S] has no 3D-viscous analogue.

**(c) First concrete step, if the owner wants to pursue it.** Formalise 4b, not the knot side.
- In Lean, over `ℝ` (archimedean, as §7c requires), state: a `structure ForcingSchedule` with fields `λ k`, `a k` and a `C^m`-norm hypothesis `‖f_k‖_{C^m} ≤ a_k λ_k^m`.
- Prove the necessary condition `(∀ m, Summable (fun k ↦ a k * λ k ^ m)) → ∀ m, a k * λ k ^ m → 0`. This is elementary and falsifiable.
- It fixes the budget any knot-labelled forcing must respect, independently of the dictionary.
- The second step would be a probe: define `Φ` for `n = 2` filament exchanges (a `σ₁` half-twist realised as a prescribed smooth vortex-pair rotation), compute the residual `f`, and confirm that it stays smooth and that the flow does not blow up. This **tests the dictionary** and is expected to be a negative (scope a).

**(d) Why the proposal as stated does not work.** Five reasons:
1. No knot-to-field dictionary exists in the corpus (§2).
2. `#` and `*_q` have no scale or time (§1b).
3. The dual-bearing LP is degenerate (`operator-selection-lp.md:34-56`).
4. The finite ILP selects by length plus a tiebreaker (§1c).
5. Smoothness of `f` forces the knot-labelled part to be negligible, so all the content stays analytic (§4b-4c).

**Recommendation (my judgement, not a finding):** take (d), and do not add a forced conjecture
to the chapter now. If the owner wants the thread kept alive, do only step (c)'s Lean lemma,
which is cheap, honest and reusable, and leave `qou-m535` open.

## 6. How a forced statement would coexist with alternatives (A)/(B)

`ns-obstruction.md:15` makes the **unforced** alternatives (A)/(B) the stated target. A forced
result (C)/(D) **does not imply** (A)/(B) in either direction [S, Fefferman's problem statement].
If anything were ever added, it would belong in a separate, clearly headed remark ("The forced
problem") placed after the Setting paragraph. That remark would:
- cite the external construction, once it has been verified and ingested into `library/`;
- state any knot-labelled variant as **conditional** on `Φ`;
- state explicitly that `NS(A)`, which concerns the unforced problem, is unaffected.

**Default if the owner says nothing:** the chapter stays unforced-only, this audit records the
negative, and `qou-m535` stays open per AGENTS.md rule 13a (it concerns an open conjecture).

Precision note: this audit contains no numerics. Every claim is structural or cites a file
line. No content block was edited.
