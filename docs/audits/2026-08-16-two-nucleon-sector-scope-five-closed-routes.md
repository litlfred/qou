# The two-nucleon sector: what is wrong, and five closed routes to fixing it

**Date:** 2026-08-16
**Branch:** `claude/l2-1ppq-mass-binding-mh643j` (PR #4973)
**Beans:** `qou-0pzi`, `qou-pjx4`, `qou-brg3`, `qou-7nwg`, `qou-shts`
**Status:** scope finding — a negative, consolidated. No repair is proposed.

> **⚠ SUPERSEDED 2026-08-16 by
> [`2026-08-16-two-nucleon-sector-final-state-eight-closures.md`](2026-08-16-two-nucleon-sector-final-state-eight-closures.md).**
> Three more routes have since closed — the **entire T-odd class** (the framing
> cancels in the two-nucleon total, which is floored at `α·log 4`), a **uniform
> `α` rescale** (empty intersection with the many-body deficit), and full `H₆`
> (route 6, already retracted in §4b below). §§1–4 of this document stand as
> written. **§5 and §6 are WITHDRAWN** — see the successor's §5 for why: §5's
> item 1 cites the very `H₆` analysis that §4b retracts, and §6's
> "remaining candidates" all route through the interface, which is now closed as
> a class rather than candidate-by-candidate.

---

## 1. The defect

`_bond_type_L` defines each per-bond suppression as the **isolated** two-nucleon
log-trace-ratio, `L_X = ln(tr_free/tr_atom)` at `(Z,N) = (2,0), (1,1), (0,2)`. So
`L_pp` **is** the diproton and `L_nn` **is** the dineutron — directly falsifiable,
with no many-body reasoning in between.

| system | framework | nature (Machleidt CD-Bonn Table XI) | |
|---|---:|---|---|
| pn (deuteron) | **+2.8328** MeV | `a_t = +5.419 fm`, `B = +2.2246` — BOUND | 27.3 % over |
| pp (diproton) | **+2.5416** MeV | `a^N_pp = −17.3 fm` — **UNBOUND** | **WRONG SIGN** |
| nn (dineutron) | **+3.3069** MeV | `a^N_nn = −18.9 fm` — **UNBOUND** | **WRONG SIGN** |

**Two of three two-nucleon systems are qualitatively wrong.** Not a magnitude
miss — the framework predicts bound states that do not exist. The non-existence of
the diproton and dineutron is textbook, and is precisely what makes the deuteron
special. Not a normalisation artifact either: the un-normalised exact traces are
`+2.0507` and `+3.7978`, same sign.

This reframes the axis. Magnitude residuals (the chain is 3.01× low at its
asymptote, 27.3 % over at the deuteron) invite a missing additive term. A **sign**
error in two of three directly-constructed channels says the per-bond object may
not be the two-nucleon interaction at all.

## 2. Where it comes from — proved, not conjectured

The single-crossing interface scalar is `μ = z + d` with `z = q³/(q²+1)` and
`d ∈ [−h, 0]`. Binding is `B = −α log μ`, so `B > 0 ⟺ μ < 1`. The family is
increasing in `d`, hence capped by `z`, and

> `z < 1 ⟺ q³ < q² + 1`, which at `q₀ ≈ 1.10998` reads `1.3676 < 2.2321`.

**Every** admissible single crossing binds. Unbinding would need
`q > 1.46557…` (the real root of `q³ = q²+1`); the substrate sits **24 % below**,
so this is not a near-miss a correction could flip. Coulomb does not explain it
either: `E_C(diproton) = 1.14 MeV` against `+2.54` (net still bound), and
`E_C(dineutron) = 0` exactly while the dineutron is the harder case.

Sorry-free in [`SingleCrossingAlwaysBinds.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SingleCrossingAlwaysBinds.lean),
including the exact gap `z − h = 1/(q(q²+1))`.

## 3. The five closed routes

| # | route | why it fails | status |
|---|---|---|---|
| 1 | single crossing, any admissible `d` | `μ ≤ z < 1` | **Lean**, scope-(b) |
| 2 | `T₃`-graded writhe | `T₃` gives `pp` a **non-negative** exponent; non-negative exponents on a base in `(0,1)` bind *harder* | **Lean**, scope-(b) |
| 3 | stacked powers `σ^m` | the writhe factor is common to both channels and **cancels in the ratio**; the surviving `q^{2m}` orders them backwards (need `m > −5.33` and `m ≤ −21.98`) | measured + **Lean** ratio lemmas |
| 4 | writhe-derived framing `f` | every candidate (`interface`, `full word`, `nucleon sum`) leaves **nn** at `f = 1–2` against a required `f ≥ 3` | measured, 3 candidates |
| 5 | operator-selection LP | on **projectors**: orthogonal ⇒ Gram diagonal ⇒ no discrimination (10–11 of 11 active at every target; well-posed, gap 3.8e-13). On **sub-words and production templates**: the Frobenius form is **indefinite** (eigenvalues −1.579, −1.140), so the program is unbounded and the solver returns a box corner (`max\|x*\| = 3.6e6` vs `M_bound = 1e6`) — it does not validly select at all | measured, both bases |

> **Correction (2026-08-16).** An earlier revision of this row read the sub-word
> basis as "discriminates stably, 7 of 11, but on braid adjacency" and compared
> block support (0.241 active vs 0.271 rejected). That was an **artifact of the
> box constraint**, not a selection, and is retracted — the apparent *stability*
> across targets was the corner not moving. The production interface templates
> are worse still: their Gram has **rank 6 of 11**, because `{c·σ_g + d·1}` spans
> only `span{1, σ_g}` and the `d`-offsets add no direction beyond the identity.
> The correct statement is stronger than the retracted one: the LP's core premise
> — Frobenius positivity — **fails** on the two-nucleon operator set, so the
> question "which operators does it select" has no well-posed answer there.

> **Convergence with `qou-k4ul` (sibling, merged as #5216, 2026-08-16).** A
> sibling independently found the Lean `operator_selection_lp` was **false as
> stated** — its context carried only data and no hypotheses, so it asserted
> `IsFeasible x_star` for every instance, `0 = 1` included. The fix makes it
> **conditional**, carrying the dual certificate as hypotheses about the data
> (`s_nonneg`, `dual_feasible`, `x_star_feasible`, `zero_gap`), and closes with
> the open question:
>
> > *"If the substrate's concrete `x*`/`y₀*` do not satisfy these hypotheses, the
> > claimed optimum is wrong."*
>
> **This audit supplies that measurement for the two-nucleon instance: they are
> not satisfied.** The Frobenius Gram is indefinite (`−1.579, −1.140`), so the
> program is unbounded and the solver returns a box corner at
> `max|x*| = 3.6e6` against `M_bound = 1e6` — there is no optimal `x*` for a
> certificate to certify, and `zero_gap` / `x_star_feasible` have nothing to hold
> of. The two findings are the same defect from opposite ends: theirs that the
> theorem asserted more than its hypotheses could support, mine that the
> substrate instance cannot supply those hypotheses. Neither result depends on
> the other, and together they close the route from both sides.

Route 2 deserves emphasis: the corpus's `T₃` grading is *principled* — crossing
sign is the writhe, and the writhe carries `I₃`. It is aimed at the **small**
effect. Across `T₃` at fixed `T=1` the scattering lengths vary ~25 %
(`Δa_CIB = 6.44 fm` on ~20 fm); across **`T`** the sign **flips**
(`−23.7 → +5.4 fm`). The framework grades by the modulating quantum number and
not by the flipping one.

## 4. What survives

### 4a. The Lean interface theorems — the durable core

None of these routed through `atom_character_raw`, so none is touched by the
retraction in §4b. All sorry-free, `lean`-direct exit 0 against the real import
cone, axioms `[propext, Classical.choice, Quot.sound]` or fewer.

**`QOU/QBeta/SingleCrossingAlwaysBinds.lean`** — 14 declarations. The core of the
negative result:

| theorem | content |
|---|---|
| `markovZ_lt_one` | `z < 1 ⟺ q³ < q² + 1` — the mechanism |
| `markovZ_sub_heckeH` | `z − h = 1/(q(q²+1))` **exactly**; the family never degenerates |
| `h_lt_markovZ` | hence `h < z` for every `q > 0`, unconditionally |
| `interface_mem_Ioo` | `0 < z + d < 1` on the whole admissible interval |
| `single_crossing_binds` | `−α·log(z+d) > 0`: **every** admissible single crossing binds |
| `nonneg_writhe_cannot_unbind` | `0 ≤ e`, `0 ≤ c ≤ 1`, `0 < μ < 1` ⟹ `μ·c^e < 1` |
| `t3_grading_cannot_unbind_pp` | the `T₃` grading gives `pp` a non-negative exponent, so it **cannot** unbind at any magnitude |
| `unbinding_needs_large_q` | contrapositive: unbinding forces `q² + 1 ≤ q³` |
| `common_factor_cancels_in_ratio` | a T-blind grading cannot discriminate the channels |
| `reciprocal_factors_scale_ratio` + `reciprocal_ratio_strictMono` | a reciprocal (T-odd) grading can, strictly monotonically |
| `writhe_normalisation_binds_harder`, `markovZ_pos`, `substrate_satisfies_hypothesis` | supporting |

**`QOU/MassTheory/ChainBindingNoSaturationPeak.lean`** — `hyperbola_no_interior_max`,
`chainPerNucleon_eq_hyperbola` (with `c₁` independent of the p/n imbalance `d`),
`chain_no_saturation_peak`.

**`QOU/MassTheory/OrderTruncationGeometricTail.lean`** — `le_geometric_of_ratio`,
`le_geometric_of_ratio'`, `tail_lt_of_ratio`: a per-order ratio bound gives an
explicit truncation order.

**`QOU/Mass/CubeMomentLowerBound.lean`** — step (C) of the tower growth bound
unconditionally, plus the weakenings reducing (D) to a ratio bound.

**Keystone (`PolynomialShadowRigidity`, `KeystoneRootsOfUnityReduction`,
`KeystoneFramingTrivialAtRootsOfUnity`)** — rigidity discharged on the rational
carrier; the archimedean step made free for rational sides; the concrete
RT/Seifert row closed negatively (`f·c(λ) = 0 ⟹ f = 0`).

**`QOU/Mathlib/BurnsideViaBranching.lean`** — `sum_sq_step`,
`sum_sq_factorial_of_step` (the latter depends on **no axioms**).

**These theorems are why the negative result is a finding rather than a failed
attempt.** `single_crossing_binds` and `t3_grading_cannot_unbind_pp` are what turn
"the diproton comes out wrong" into "the diproton *cannot* come out right in this
construction, and here is the invariant."

### 4b. The empirical positives — one retracted, one standing

* ~~**`H_6` has the range and the right orientation.**~~ **RETRACTED
  2026-08-16 — this was false, and it was the one positive structural result on
  the axis.** The per-block characters came from `pyhecke.trace.atom_character_raw`;
  production uses `chi_all_lambda_reduced_block` (fine-Bratteli transfer) and the
  two are different objects — agreeing exactly on the 1-dim blocks, disagreeing on
  every multi-dim one with no consistent factor (−3.80, −2.24, −154.5, …). The
  transfer routine is correct: `Σ y_λ χ_λ` over it reproduces `tr_free/tr_atom`
  exactly for all three systems.

  Corrected, with the same `y_λ`: `(6,) 1.110/1.006/0.901`,
  `(5,1) 0.611/0.542/0.408`, `(4,2) 0.328/0.186/0.111`, `(3,3) 0.928/0.919/0.934`.
  **Three of the four surviving blocks BIND.** The only one above 1 is the trivial
  rep at `r = q = 1.110`, which is forced for a 1-dim rep with one extra crossing
  and is therefore not a finding. So `H_6` does **not** carry the range
  `span{1,σ}` lacks — the weighted maximum is `q ≈ 1.11`, not 6.46 — and
  **route 6 (drop the 2-dim subalgebra) joins the closed list.**

  How it got past me: the probe validated the characters against the Hecke
  eigenvalues on the 1-dim blocks and passed to every digit. Those are precisely
  the two blocks where the routines agree — a validation exercising only the
  1-dim blocks cannot detect a defect in the multi-dim ones, and produced false
  confidence rather than none.
* **The ribbon twist is `T`-odd.** `θ_λ = q^{c(λ)}` with `c(λ') = −c(λ)` gives the
  symmetric block `q^{+f}` and the antisymmetric `q^{−f}` — reciprocal, so the
  ratio moves as `q^{2f}` and the channels **can** be reordered. This is the
  property the writhe lacks, and it is derived. At `f = 3` the signs come out
  right for the first time on this axis (`B(T=1) = −0.121` vs nature `≈ −0.07`;
  `B(T=0) = +7.16` vs deuteron `+2.22`).

**`f = 3` is not derived** — it is the smallest integer above a threshold, and
adopting it because it reproduces the data is a fit, blocked by the same
discipline as the seven `Δ_λ` ansätze. Route 4 was the attempt to derive it and
it failed.

## 5. Two obstructions any repair must address

1. **7 of 11 `H_6` blocks have `r_λ < 0`** — the character changes sign between
   the atom and free words, so `−α ln r` is **undefined** and a per-block binding
   energy does not exist there. Any per-block decomposition must first say what a
   negative character ratio means.
2. **No selection principle.** With 11 blocks, choosing the ones that give the
   right answer is a fit; route 5 removes the one candidate justification that was
   available for making that choice.

## 6. Honest statement of where this leaves the axis

The two-nucleon sector needs a **structural change**, not a correction. Every
magnitude result on the binding axis — the collective-term budget, the saturation
analysis, the per-bond chain — is conditional on a decomposition that fails its
most basic external check.

What is *not* affected: the chain's **additivity** is independently verified to
`1.78e-15` against the exact `p(3A)` trace (see
[`2026-08-15-...`](../../computations/probes/chain_binding_hyperbola_no_peak_probe.py)
CHECK 1b), every Lean theorem stands, and the dimensionless ratios elsewhere in
the framework (`m_K/m_π` at 51 ppb, parameter-free) are untouched. This is a
scope finding about one sector, not about the framework.

**Remaining candidates**, all routing around operator overlap: an index, a
positivity condition, or a variational criterion. And the `H_6` range result says
such a principle would have something to select *from* — which routes 1–3 did not.
