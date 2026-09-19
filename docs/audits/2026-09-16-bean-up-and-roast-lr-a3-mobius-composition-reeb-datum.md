# Bean-up-and-roast: A = 3 LR branching, the Möbius objective, the composition feasibility program, `RelativeReebDatum`, and the `⋈_{⟨knot_con, phase_space⟩}` reading

**Date:** 2026-09-16 · **Branch:** `claude/sdp-analysis-light-cone-recursion-2026-09-16` (PR #7434, stacked) ·
**Milestone bean:** `qou-cgsn` · **Predecessors:** `2026-09-16-q-stochastic-phase-space-shadow-prices-analysis.md` (PR #7432, merged),
`2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md` (PR #7434).

Owner, 2026-09-16 (gist, verbatim where it matters): *"bean up and roast if not done: build the A = 3
Littlewood–Richardson branching; work the Möbius-energy objective; pose the composition feasibility program;
no object exists for a relative Reeb angle between two knots … that is supposed to be the evaluation/trace of
the substrate phase space at the point — formalize and work on the `RelativeReebDatum` conjecture class; the
knot convolution is really `(knot₁) ⋈_{⟨knot_con, phase_space⟩} (knot₂)` where `⟨knot_con, phase_space⟩` is the
evaluation of the SDP with the phase substrate in the entanglement light cone … fully entangled means all of
the phase space is weighted fully in the negative coefficients of entanglement; no prior entanglement in the γγ
production ⇒ the phase space does not contribute at all; you can see the full γγ production history in the
GB filtration/tower; a shared photon changes the q-torsion/phase angle; if absolutely no common light cone, a
particle and antiparticle annihilate, I guess?"*

"Roast" is the critical-distance license (AGENTS.md): every clause below is read adversarially against the
corpus, with the measurement that decides it where one exists.

---

## 1. TL;DR

| item | state before | what landed (derived, nothing wired) | roast verdict |
|---|---|---|---|
| **1. A = 3 LR branching** | LR engine + `phase_b_lr_branching_constraint_probe` (dimension identities, A = 2..4) existed; the *character* rule was never checked against committed A = 3 data, and the weight identity only at (3,3) → 6 | Lean: iterated `BranchingData` — `c₃`, `branching₃`, `weight_branching₃`, `trM_tensor₃` (sorry-free). Probe: at H₉ the three-factor rule reproduces the committed free products of T and ³He on all 30 blocks (worst 2.6e-49); the (6,3) → 9 weight identity on all 33 pairs (2.5e-51) and the iterated one on all 27 triples (2.0e-51); Σyδ pinned by the bond product | done. The mirror pair's two-row deviation **directions** differ by only `arccos 0.99114 ≈ 7.6°` — almost all of what distinguishes T from ³He is in the weighted *total*, which the bond product already fixes |
| **2. Möbius objective** | no argument in `H_n(q)`, constant free (`qou-uh5f`), no word → curve map (`qou-pzsi`) | Lean: `weighted_deviation_eq_of_trM_eq_mul` — under any multiplicative bond law the weighted deviation is `tr(a)tr(b)(∏ − 1)`, so an objective sees only the *direction* of δ | **GAP** (`qou-ypc5`). And by item 1 the direction barely separates the mirror pair, so even a defined Möbius objective would be ranking on a 7.6° difference |
| **3. Composition feasibility program** | not posed; every corpus program verifies or ranks a *given* composite | Lean: `CompositionProgram` (data, variable, composite, `Feasible` = reading 3, `feasibleSet`), with `trM_nonneg_of_reading3`, `weighted_letterDeviation_ge`, `feasible_unit_iff`. Probe at A = 2 on the alphabet `(1−e)σ₂ + eσ₂⁻¹`: **solved in closed form** (affine in `e`) | **No single-crossing bridge letter is feasible for any `e ∈ [0, 1]`** — the `(5,1)` block is negative at both endpoints (`−0.607`, `−0.758`), so the feasible set is `e ≤ −4.02`, i.e. a positive offset `d ≥ 0.84` with trace ratio `> 1.45` (anti-binding). The feasible letters found are the **even** powers `σ₂^{±2}`; every odd power fails on `(5,1)`. The production defect at A = 2 is the letter's *parity*, not its weight |
| **4. `RelativeReebDatum`** | held (§3b-tax needed content; owner had not specified it) | Lean class committed: `lightCone`, `compose`, `Entangled`; `compose_eq`, `lightCone_of_not_entangled`, `trM_lightCone_mem`; `phaseSpace`, `relAngle := arccos ∘ trM ∘ lightCone`; four consequences proved. Probe: the trace-level candidate `arccos(∏(z_D + d))` is defined on D/T/³He/⁴He (`59.5° / 78.2° / 71.9° / 82.8°`) and monotone in bond count; the block-level ratio is **not** definable (`|χ_atom/χ_free| > 1` on T `(5,4)`, ³He `(9)`, `(5,4)`) | the class is honest but its angle, on the only candidate that is defined, is a function of the bond product alone — `θ = arccos(exp(−B/α))` — so it is the binding form renamed, not a second datum |
| **5. `⋈_{⟨knot_con, phase_space⟩}`** | the picture, in prose | Lean: `InterfaceLetterCrossingMixture` — every production letter is `(1−e)σ + eσ⁻¹` with `e = −d/h`; its trace is `(1−e)z + e(z − h)` | "weighted in the negative coefficients" is **exactly the inverse-crossing weight** `e`, already in every letter (`pp 0`, `pn ½ − δ/4`, `nn 1`; quarks `uu 0`, `ud ½`, `dd 1`). Three of the owner's clauses are then theorems, one is a **decision** (§6 R3), one is unsupported by the corpus (GB history), and the annihilation guess **runs backwards** |

Two decisions are handed to the owner in §8; the default (nothing changes) is safe.

---

## 2. Item 1 — the A = 3 Littlewood–Richardson branching (`qou-672t`)

**What already existed** (corpus-grep, six paths): `computations/substrate/lr_coefficients.py` (`lr_coef`,
`get_lr_table`, skew-tableau enumeration, exact); `probes/phase_b_lr_branching_constraint_probe.py` (builds the
iterated LR profile at A = 3, validates the *dimension* identities, A = 2, 3, 4); `sublemma_2_1_h9_branching_basis.py`
(the Gelfand–Tsetlin block decomposition of the interface operator at H₉, numpy); bean `qou-matm` (Path B
iterated branching disagrees with the *bound* H₁₂ character at O(1) — expected, the bound word is interleaved).
None checked the three-factor **character** rule against committed A = 3 characters, and the weight identity was
measured only at (3,3) → 6 (PR #7434).

**Lean** (`BranchingPushforwardMultiplicativity.lean`, section `Iterated`, all `-DautoImplicit=false` exit 0,
axioms `propext / Classical.choice / Quot.sound`):

* `c₃ μ ν ρ l := Σ_κ c^κ_{μν} c^l_{κρ}` — three-factor multiplicities through the intermediate level;
* `branching₃` — `χ_λ((a ⊗ b) ⊗ c) = Σ_{μνρ} c₃ · χ_μ(a) χ_ν(b) χ_ρ(c)` given `B'.D₁ = B.D`;
* `weight_branching₃` — `Σ_λ y_λ c₃ = y_μ y_ν y_ρ`;
* `trM_tensor₃` — `tr_M((a ⊗ b) ⊗ c) = tr_M(a) tr_M(b) tr_M(c)`.

**Probe** (`probes/lr_a3_three_factor_branching_probe.py`, 8/8, committed inputs only, 60 dps):

| measurement | value |
|---|---|
| LR (6,3) → 9 nonzero entries | 203 (self-checked: `f^μ f^ν f^ρ · 1680 = Σ_λ c₃ f^λ` on all 27 triples) |
| weight identity (6,3) → 9, 33 pairs, worst | `2.5e-51` |
| iterated weight identity, 27 triples, worst | `2.0e-51` |
| three-factor rule vs committed `free` (T, ³He), 60 blocks, worst | `2.6e-49` |
| T: `Σ y δ` / `tr(free)(∏ − 1)` | `−0.112928014` / `−0.112928014` (`tr(free) = 0.1420721`, `∏ = 0.2051356`) |
| ³He: same | `−0.129582389` / `−0.129582389` (`tr(free) = 0.1881786`, `∏ = 0.3113863`) |
| cos(angle between the two unit deviation directions) | **`0.991138686`** (≈ 7.6°) |
| reading 3 on the bound words | both fail on `(8,1)` and `(5,4)` (corroborates `qou-7dal`) |

The last row but one is the roast of item 2: the y-weighted two-row deviation vectors of the mirror pair are
nearly parallel. The direction is `(9): −0.058, (8,1): −0.805, (7,2): −0.450, (6,3): −0.360, (5,4): −0.133` for T
and `(9): +0.072, (8,1): −0.790, (7,2): −0.464, (6,3): −0.365, (5,4): −0.152` for ³He — the one qualitative
difference is the sign on the trivial block.

---

## 3. Item 2 — the Möbius-energy objective (`qou-ypc5`, GAP)

**What is derived.** `weighted_deviation_eq_of_trM_eq_mul`: if `tr_M(atom) = tr_M(a) tr_M(b) · bond`, then
`Σ_λ y_λ δ_λ = tr_M(a) tr_M(b) (bond − 1)`. The corpus's bond law holds to `≤ 9e-51` on all four production
nuclei, so on the composition program the weighted **total** of the deviation is not a variable. Any objective —
linear, Möbius, anything — acts on the *direction* of δ within the hyperplane, and item 1 measured that direction
to be nearly the same for the two A = 3 nuclei.

**What is not there, in order of severity.**

1. **No argument.** `CategoricalMobiusEnergy` takes a `KnotEmbedding` (a curve) and a real `energy`; the
   composition program's variable is an element of `H_{3A}(q)`. There is no map from a word to a curve
   (`qou-pzsi`), so the objective cannot be evaluated on any point of the feasible set.
2. **No zero.** `classicalLimitConst` is a free field of the same structure, proved unconstrained
   (`no_universal_classicalLimitConst`, `qou-uh5f`). A ranking is invariant under a constant shift, so this would
   not block *ranking* — but it blocks any claim that the energy's *value* means something.
3. **Not pre-excluded.** The 2026-08-24 exclusion is for linear objectives; the Möbius energy is quadratic and
   non-local. That is the only thing in its favour and it is a negative statement.

**Honest state:** posing the Möbius objective requires (1) first. Bean `qou-ypc5` records the gap with the
hyperplane lemma as the one derived constraint. No probe was written, deliberately: a Möbius "objective" on the
block vector would be an invented functional, i.e. a fourth calibration in disguise.

---

## 4. Item 3 — the composition feasibility program, posed and solved at A = 2 (`qou-8r6b`)

**Lean** (`CompositionFeasibilityProgram.lean`): `CompositionProgram` — branching data `B`, an alphabet `L` acting on
the composite algebra, a unit letter; `composite ℓ a b := act ℓ (a ⊗ b)`; `Feasible ℓ a b := Reading3 (composite)`
with `Reading3 D x := ∀ l, 0 < y l → 0 ≤ χ l x`; `feasibleSet`. Proved: `trM_nonneg_of_reading3` (reading 3 +
probability weights ⇒ `0 ≤ tr_M`), `weighted_letterDeviation_ge` (a feasible letter cannot cancel the free trace),
`feasible_unit_iff`, `letterDeviation_unit`. No objective.

**Probe** (`probes/composition_feasibility_a2_probe.py`, 8/8). A self-contained mpmath Hoefsmit evaluator
(mirroring `_exact_trace_engine.py`, which needs gmpy2) was **validated first** against committed canonical data
— H₃ proton/neutron characters to `5.4e-50`, H₆ deuteron free and bound characters (Rust + MPFR, 50 dps) to
`1.4e-49` — so the word, the seminormal convention and the pin are all confirmed before any program is solved.

The alphabet: `L_e = σ₂ − e h · 1 = (1−e) σ₂ + e σ₂⁻¹` on the bridge generator, plus the powers `σ₂^m`.
Because `χ_λ(W_free L_e)` is affine in `e`, the feasible set is an interval, computed exactly from the two
endpoint character vectors:

| block (y > 0) | `χ(W_free σ₂)` | `χ(W_free σ₂⁻¹)` | constraint |
|---|---:|---:|---|
| `(6)` | 1.72192 | 1.39760 | `e ≤ 5.309` |
| `(5,1)` | **−0.60684** | **−0.75783** | **`e ≤ −4.019`** |
| `(4,2)` | 0.41542 | 0.24262 | `e ≤ 2.404` |
| `(3,3)` | 0.88689 | 0.54076 | `e ≤ 2.562` |

So the feasible set is `(−∞, −4.019]`: **no mixture weight in `[0, 1]` is feasible** — not `e = 0` (the pp-type
`σ`), not `e = e_pn = 0.49966` (production), not `e = 1` (the nn-type `σ⁻¹`). The bond law
`tr(W_e)/tr(W_free) = z_D − e h` holds along the whole family to `1.7e-50` (`trace_interfaceLetter`, measured
rather than assumed), so on the feasible branch the ratio is `≥ 1.45` — the letter *unbinds*.

| bridge letter | trace ratio | `−log` | reading 3 |
|---|---:|---:|---|
| `σ₂⁻³` | 0.21221 | 1.550 | fails `(5,1)` |
| `σ₂⁻²` | 0.91562 | **0.0882** | **feasible** |
| `σ₂⁻¹` (nn-type) | 0.40363 | 0.907 | fails `(5,1)` |
| `1` (unit) | 1 | 0 | feasible |
| `σ₂` (pp-type) | 0.61269 | 0.490 | fails `(5,1)` |
| `σ₂²` | 1.12809 | −0.120 | **feasible** (anti-binding) |
| `σ₂³` | 0.84853 | 0.164 | fails `(5,1)` |
| production pn `L_{e_pn}` | 0.50823 | 0.677 | fails `(5,1)` |

**Reading.** Under reading 3, whole word, the A = 2 program's feasible letters among those tested are the
**even** crossing powers, and every **odd** one — every single crossing, whatever its σ/σ⁻¹ mixture — is
rejected by `(5,1)`. That is the same block that carries the largest deviation and that rejects the production
deuteron (`qou-7dal`). This is a scope-(a) statement about the tested alphabet (the mixture family and
`|m| ≤ 3`); it is not a proof that every odd bridge word fails. But it moves the diagnosis: the A = 2 defect is
not the *weight* of the pn letter (no weight fixes it) but its *parity* — and parity is already the constraint the
γγ construction imposes (`gammaGamma_length_even`, sorry-free). The one feasible letter that binds, `σ₂⁻²`, gives
`B/α = 0.088` against the production `0.677`; recording that number is not selecting it.

**What the program still needs.** The alphabet at A ≥ 3 (bands `σ_{3k+2}` with the intra letters between; the
mpmath evaluator can do the two-row blocks at H₉, dims ≤ 48, in about a minute; `pyhecke_native` for all blocks),
and reading 3's scope ruling (PR #7434 §8 O2), which decides whether the composite is even the right object to
test.

---

## 5. Item 4 — `RelativeReebDatum` (`qou-jfx8`)

**Class** (`RelativeReebDatum.lean`, over `ℝ` per §7c, parametrised by `BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ`; no
instance):

| field | content |
|---|---|
| `lightCone : A₁ → A₁ → A` | the common entanglement light cone, an element of the composite algebra |
| `compose : A₁ → A₁ → A` | the knot convolution `a ⋈ b` |
| `Entangled : A₁ → A₁ → Prop` | shared prior (γγ) history |
| `compose_eq` | `a ⋈ b = (a ⊗ b) · lightCone a b` (the corpus's `K = ρ(atom) ρ(free)⁻¹`) |
| `lightCone_of_not_entangled` | `¬Entangled a b → lightCone a b = 1` |
| `trM_lightCone_mem` | `tr_M(lightCone a b) ∈ [−1, 1]` |

Derived: `phaseSpace a b := λ ↦ y_λ χ_λ(lightCone a b)` (the "evaluation of the substrate phase space"),
`sum_phaseSpace` (it sums to the trace), `relAngle a b := arccos(tr_M(lightCone a b))`, and the four
no-shared-history consequences (composite = free product, trace factorises, binding form 0, angle 0).

**Probe** (`probes/relative_reeb_datum_trace_angle_probe.py`, 7/7): with `lightCone`'s trace identified with the
bond product (the only trace the corpus has for it),

| nucleus | `tr(light cone) = ∏(z_D + d)` | `θ_trace` | block ratios `|χ_atom/χ_free| ≤ 1` | `χ_atom/dim ∈ [−1,1]` |
|---|---:|---:|---|---|
| D | 0.50823 | 59.454° | 3/4 | 3/4 (`(6)`: 1.56) |
| ³He | 0.31139 | 71.857° | 3/5 (`(9)` 1.116, `(5,4)` −1.146) | 4/5 |
| T | 0.20514 | 78.163° | 4/5 (`(5,4)` −1.729) | 4/5 |
| ⁴He | 0.12568 | 82.780° | 6/7 | 6/7 |

**Roast.**

* The trace-level candidate is well-defined and monotone in the number of bonds, and it is **not new
  information**: `cos θ = tr(atom)/tr(free) = exp(−B/α)`, so `relAngle` is the log-assembly binding form under a
  change of variable. If that is what the relative Reeb angle is, the datum is redundant with `bindingForm`.
* The per-block candidate — the natural relative of the corpus's single-knot `θ_λ = arccos(χ_λ(C₅)/dim λ)` — is
  **not a datum** on the production words: the ratio leaves `[−1, 1]` on three blocks across T and ³He and
  changes sign on `(n−1, 1)` everywhere (the sign flip *is* the reading-3 failure). Normalised by `dim` it stays
  inside `[−1, 1]` on every non-trivial block but exceeds 1 on the trivial block for all four nuclei.
* "At the point": the corpus's only point-level two-object structure is the observation-direction commutator
  `[δq₁, δq₂] = F_q` (`rem:two-observer-parallelogram`), one point, one particle. `lightCone a b ∈ H_{3A}` is not
  localised anywhere. The class leaves it as data because nothing in the corpus produces it; that is the honest
  position and it is why the class has no instance.

---

## 6. Item 5 — the `⋈_{⟨knot_con, phase_space⟩}` reading, clause by clause (`qou-1x56`)

**The derived fact that reorganises the clauses** (`InterfaceLetterCrossingMixture.lean`,
`mul_sub_smul_one_eq_one`, `interfaceLetter_eq_mix`, `trace_interfaceLetter`; measured in the Reeb probe): under
the Hecke relation `σ² = hσ + 1`, `σ⁻¹ = σ − h·1`, so every production letter `σ + d` is

    σ − e h · 1 = (1 − e) σ + e σ⁻¹,    e = −d/h,

with `e_pp = 0`, `e_pn = ½ − δ/4 = 0.49966`, `e_nn = 1`, `e_uu = 0`, `e_ud = ½`, `e_dd = 1`; its bond factor is the
mixture of the two crossing traces, `(1−e) z_D + e (z_D − h) = z_D + d`. The **only negative coefficient a
production letter carries is `−e h`**, the weight on the inverse crossing; `K(2H) = σ₀ + D_PN·1` has exactly one
negative NF coefficient and it is `D_PN = −e_pn h` (`k_versus_selected_operator_probe.py`).

| owner's clause | status | evidence |
|---|---|---|
| R1 "no prior entanglement ⇒ the phase space does not contribute at all" | **theorem**, under reading (i) below | `lightCone = 1 ⇒ compose = tensor ⇒ tr multiplicative ⇒ bindingForm 0, relAngle 0` (`RelativeReebDatum.lean`, from `trM_tensor`) |
| R2 "fully entangled ⇒ all of the phase space weighted in the negative coefficients" | **derived, and it reinterprets the corpus** | the negative coefficient is the inverse-crossing weight `e`; "fully entangled" = `e = 1` = `σ⁻¹` = the nn letter; "not at all" = `e = 0` = `σ` = the pp letter; pn is `½ − δ/4` |
| R3 — but then which pairs are entangled? | **decision, and the corpus contradicts one reading** | under R2 the like pairs are the *extremes* (pp unentangled, nn fully) and the unlike pair the middle. The two-body spectrum needs the unlike pair singled out and both like pairs unbound (`qou-q8vl`: `g_pn` opposite to both like bonds). And the pp letter `σ` with `e = 0` still *binds* (`z_D = 0.613 ≠ 1`) — so either "no contribution" means the light cone is the **unit** (reading (i), the class as written, binding 0) or it means the light cone is the **bare crossing** (reading (ii), the corpus's pp bond, binding `−α log z_D > 0`). The two are different clauses; §8 O2 |
| R4 "you can see the full γγ production history in the GB filtration/tower" | **not supported as stated** | `jet_history_retention_probe.py` Q1: the GS normal form is history-free — two words with the same normal form are indistinguishable downstream; the three `J^•` readings of "history" are excluded (2026-08-16/26 audits); what survives is the support map + `gbDepth` (q-stochastic analysis §4.4). The history is in the *word*; the filtration sees degree, not the sequence |
| R5 "a shared photon changes the q-torsion / phase angle" | **no object** | the class is the placeholder; on the only defined candidate the angle is a function of the bond product (§5) |
| R6 "no common light cone ⇒ particle and antiparticle annihilate, I guess?" | **runs backwards, as the algebra stands** | cancellation `w w⁻¹ = 1` needs the inverse crossings on the *same* strands — maximal shared history. With no shared strands the pair is the free product `w ⊗ w̄`, its trace is `tr(w) tr(w̄)` (`trM_tensor`, proved) and nothing cancels. The only reading that rescues the guess is "annihilate = pass through with zero binding", which is R1 |

The "q-stochastic" content, then, is not a distribution over blocks (the block measure `P` is a weight, PR #7432)
but the Bernoulli weight `e` on the inverse crossing inside each letter — it was in every production word all
along, under the name `d`. What the picture adds beyond the corpus is a *rule* for `e` (from shared history);
what the corpus already says is that no rule assigning `e ∈ [0, 1]` to a single bridge crossing is
reading-3-feasible at A = 2 (§4).

---

## 7. Gaps (beans)

| bean | gap | what would close it |
|---|---|---|
| `qou-ypc5` | Möbius objective has no argument in `H_n(q)`; constant free | a word → curve map (`qou-pzsi`) and a forced zero (`qou-uh5f`) |
| `qou-8r6b` | composition program: alphabet at A ≥ 3 untested; the parity observation is scope-(a) | enumerate bridge bands at H₉ (two-row blocks, mpmath; all blocks with `pyhecke_native`); reading 3's scope ruling (#7434 O2) |
| `qou-jfx8` | `lightCone` is data; the only defined angle candidate is the binding form renamed | an independent construction of the light cone from two histories, or an owner ruling that `θ = arccos ∏(z_D + d)` *is* the datum |
| `qou-1x56` | R3 is a decision; R4 needs an object the corpus does not have | §8 O2; a history-carrying filtration (none of the three excluded readings) |
| `qou-hlbx` (held) | `SubstratePhaseRecursion.phaseOf` still unchosen | #7434 O3 |

---

## 8. Options — default first; each with what it means, costs, risks, commits to

**O1 (default): nothing changes.** The Lean and the three probes stay as derived, consumer-free additions; the
class has no instance; the dashboard is untouched. If the owner says nothing, this is the state.

**O2: rule which "no contribution" the picture means.** *Means:* one sentence — with no shared history the light
cone is (i) the **unit** (the class as written: composite = free product, binding 0, angle 0) or (ii) the **bare
crossing `σ`** (the corpus's pp bond: `e = 0`, binding `−α log z_D = 0.49`). *Costs:* (i) nothing; (ii) one field
changes (`lightCone_of_not_entangled : … = σ`-type generator), and R1 stops being a theorem about zero binding.
*Risks:* (i) makes the corpus's pp bond an *entangled* letter with `e = 0`, i.e. `e` is not the entanglement grade
and R2 needs another carrier; (ii) makes "does not contribute" mean "contributes `z_D`". *Commits to:* what
`Entangled` and `e` mean relative to each other. **Recommendation (judgement):** (i), because it is what the owner
said and it is the reading under which R1, R2 and R6-as-R1 are consistent; the cost is admitting the pp letter is
not "unentangled" in the picture's sense, which is `qou-q8vl` said in the new vocabulary.

**O3: adopt parity as the A = 2 feasibility criterion and test it at A = 3.** *Means:* a probe enumerating
bridge letters of even and odd crossing number at H₉ on the two-row blocks. *Costs:* one probe, ~1 min mpmath
per letter on dims ≤ 48; `pyhecke_native` for the full block set. *Risks:* the two-row restriction is exact for
convention D (`y_λ = 0` off two rows), so the risk is only that even letters at A = 3 also fail, which would be a
result. *Commits to:* nothing beyond the data; it does not select a letter.

**O4: leave the Möbius objective as a gap.** *Means:* `qou-ypc5` stays `todo` with the hyperplane lemma as its one
constraint. *Costs:* nothing. *Risks:* none. *Commits to:* not inventing a functional on the block vector.
**Recommendation:** O4 until `qou-pzsi` moves.

**O5: give `RelativeReebDatum` its trace-level instance.** *Means:* declare `lightCone a b := (a ⊗ b)⁻¹ (a ⋈ b)`
where the corpus has it (`K`), so `relAngle = arccos(∏(z_D + d))`. *Costs:* an instance file. *Risks:* it
makes the angle provably redundant with the binding form (§5), and it needs `(a ⊗ b)` invertible. *Commits to:*
the angle being a rendering of the binding, not a second datum. **Recommendation:** not yet — the class is more
useful open than instantiated with a datum it would immediately prove uninformative.

---

## 9. Discipline

Nothing fitted, nothing selected against a target, nothing wired; the one feasible binding letter's number
(`0.088`) is reported as the feasible set's content, not proposed. All probes read committed proton-pinned
witnesses; `q₀` enters only through the committed `q0Value` string; 60 dps; the exact-integer imports carry
`# float64-ok`. Lean verified `lean -DautoImplicit=false -s 65536` exit 0 per file against the restored cache
plus the overlay of this branch's own oleans; `#print axioms` on every new theorem: `propext`,
`Classical.choice`, `Quot.sound` only. Reading 3's failure on every tested single-crossing letter is stated as
scope (a) (the tested alphabet), not as an exclusion. The owner's annihilation clause is recorded as a question
and is not encoded.
