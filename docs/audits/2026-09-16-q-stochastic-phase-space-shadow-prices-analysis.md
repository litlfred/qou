# q-stochastic phase space from the LP-dual shadow prices — what the corpus holds, what is missing, what would move

Session `qou-0nrt` (beans `qou-mt94` survey, `qou-zu06` this document, `qou-jfx8`
formalize-first), branch `claude/q-stochastic-phase-space-shadow-2026-09-16`.
Owner ask, 2026-09-16: *"Check corpus and give analysis, identify gaps and see
downstream impact. Make sure you work on the jet tower / GB filtration."*

This is an **analysis**, not a construction. Two things landed alongside it
because they are derived rather than proposed: one Lean module and one probe
(§5). Nothing is wired, no number in any dashboard moves, and every option in
§8 waits on the owner.

---

## 0. The picture, decomposed

The owner's message, taken apart into the objects it names. Each is checked
against the corpus in §2–§3.

| # | ingredient (owner's words) | the object it needs |
|---|---|---|
| I1 | "confinement levels … at lower confinement levels like gluons there is more limited entanglement history" | a level `ℓ` and a notion of "fewer directions" at low `ℓ` |
| I2 | "entanglement history in the knot convolution" | a record of past interactions carried by the state |
| I3 | "these directions are the dual shadow prices" | a weight per direction, identified with an LP/SDP dual |
| I4 | "q-stochastic … a q-distribution on phase space according to the weights of the LP-dual shadow [prices]" | a probability measure on a state space, weighted by I3 |
| I5 | "the two particles … share some of their affine computational light cone, that is their 'entangled phase space' the unknown in the ILP/SDP" | a shared sub-object of two states, missing from the program |
| I6 | "a relative vector/angle for their respective Reeb flows … like the start of the parallelogram at the cusp of the ED" | a relative orientation datum between two objects |
| I7 | "they evolve according to the SDP-selected (O'Hara energy functional) knot convolution operator" | an SDP whose objective is the Möbius/O'Hara energy |
| I8 | "the knot convolution is still the operator" | the binding operator `K` |
| I9 | "jet tower / GB filtration" | the tower `A_{n+1} = J¹(A_n)` and the filtration `J^•` of `H_n(q)` |

Vocabulary check, so the negatives below are read correctly: the strings
**"q-stochastic"**, **"entangled phase space"**, **"computational light cone"**
and **"relative Reeb angle"** occur **nowhere** in `content/`, `computations/`
or `docs/` outside this session's own beans. "Entanglement history" occurs
twice: `computations/jet_history_retention_probe.py:26–34` and the title of
bean `qou-dcvv` (body empty). So most of the picture is being named for the
first time; what follows is where its *parts* already live under other names.

---

## 1. TL;DR

1. **The q-distribution already exists, and it is the Markov weight measure.**
   `P(λ) := y_λ(q) · dim V_λ` on the Wedderburn blocks is non-negative and sums
   to `1` — that is Markov axiom M1 read through the Frobenius pairing, proved
   generically this session (`blockMass_sum_eq_one`) and measured on committed
   data at `H_6`, proton pin: `Σ P = 1.0` to 50 dps, support exactly the four
   two-row blocks (convention D), masses `(4,2) 0.414 > (5,1) 0.395 > (6) 0.115
   > (3,3) 0.076`. The Markov trace **is** the `P`-expectation of the normalised
   characters (`trM_eq_expectation`). Nothing new has to be invented for I4;
   what has to be *decided* is which weight family the word "shadow price" means.
2. **"Shadow price" means three different things in the corpus, and they rank
   the directions differently.** (a) the closed-form `u_λ = w_λ/d_λ − 1/[k]_q!`
   of `def:knot-operator-energy`, built on the **Plancherel** family `w_λ`, which
   is *not* a measure (`Σ w_λ(q) ≈ 1.51` at `n = 12`) and is the family bean
   `qou-oots` and `y_lambda_conflation_audit.py` exist to keep apart from `y_λ`;
   (b) the **Markov** `y_λ` of the Frobenius pairing; (c) the **solver dual**
   `y*_λ` of an actual LP. On the deuteron's four two-row blocks, (b) ranks
   `(4,2) > (5,1) > (6) > (3,3)` and (c) ranks `(6) > (3,3) > (5,1) > (4,2)` —
   close to opposite (probe §5.2). The owner's sentence *"these directions are
   the dual shadow prices"* is therefore under-determined until one of the
   three is named.
3. **The scalar dual is dead; the per-channel dual is alive but partly
   degenerate.** `prop:operator-selection-lp` has `y₀* ≡ 0` and a
   positive-dimensional optimum (`docs/audits/2026-08-24-…objective-defect.md`;
   "no linear objective can select 𝓑₃"). The `H_{3A}` program does give a
   non-empty active set, but **`³H` and `³He` get the same one** because the
   Littlewood–Richardson branching that knows `(Z, N)` exists only at `A = 2`
   (`operator_selection_active_set_probe.py`). The positive-sector variant
   separates them — and provably cannot return `K` (`k_versus_selected_operator_probe.py`).
4. **`K` is determined, not selected.** Once the words are fixed,
   `K = ρ(atom)·ρ(free)⁻¹` exists in every block, has closure arity `2A + 1`,
   is not PSD, and lies outside the positive sector on `1 < q < q_c = 3.458`
   (`binding_k_convolution_sdp_probe.py`, 46/46). So "SDP-selected knot
   convolution operator" must mean *the words* are selected — which is the
   γγ + confinement-SDP ruling of `qou-ales`, whose scored element currently
   **fails** reading 3 on `(2,1)` (`qou-99qc`).
5. **The jet tower is the ordered expansion; the GB filtration is not the
   level.** All three readings of `J^•` as a word-depth filtration are
   excluded for the word→partition bridge, and any idempotent-graded filtration
   puts the **unit at the top** (`2026-08-16-three-gb-filtrations-one-name.md`,
   `2026-08-26-the-unit-coefficient-…md`). This session proves the abstract
   form for the energy-ranked level of `def:confinement-level`:
   `level 1 = top` and `level x ≤ level 1` for every `x`
   (`level_one_eq_top`, `level_le_level_one`). So the ladder *quark = 0,
   nucleon = 1, atom = 2* of `def:confined-particle` is **not** the level
   `def:confinement-level` defines, and I1's "fewer directions at low level"
   cannot be read off that definition as written. What *is* proved about
   history: a fresh interaction promotes the whole filtration profile by
   exactly one grade with nothing split (`JetGradePromotion.lean`), the normal
   form itself is history-free (`jet_history_retention_probe.py` Q1), and the
   body-number expansion carries no `ε`-ordering while the jet tower does, with
   ratio `q⁻²` (`BondFactorClassicalFloor.lean`, `BraneTowerLevelAmplitude.lean`).
6. **Three ingredients have no object at all:** the shared light cone /
   entangled phase space (I5) beyond the elementary block-set version proved
   here; the relative Reeb angle between two knots (I6) — the corpus has a
   *single*-knot rotation angle and a two-observer *commutator at one point*;
   and an O'Hara-energy objective for any LP/SDP (I7). The last is the
   interesting absence: the categorical Möbius energy is quadratic and
   non-local, so it is **outside** the class the 2026-08-24 exclusion covers —
   but its Lean carrier's classical limit is currently unconstraining
   (`qou-99qc`), so it selects nothing until the functional is pinned.
7. **Downstream, nothing moves today.** No L2 row, no `c_k`, no Ursell sign
   changes. What the analysis *does* change is where the next tranche should
   go (§8): re-found the level on the block support, and build the `A = 3` LR
   branching — both derived, both fit-free — before any orientation datum is
   introduced.

---

## 2. Per-ingredient corpus state

| # | exists | where | status | gap |
|---|---|---|---|---|
| I1 confinement level | yes, twice, inequivalently | `def:confinement-level` (energy-ranked block subalgebra); `def:confined-particle` ladder `quark=0, nucleon=1, atom=2, molecule=3`; `intro-confinement-level.md` ("reduction steps"); `shell-schur-weyl-…-interpretation.md` ("level 3 pair, level 4 shell") | Lean `QOU.BraidKnot.ConfinementLevel` (min over a filtration predicate); existence/uniqueness proved | the definition puts the unit at the top (§4.2), so it is not the ladder; three characterisations, none reconciled |
| I2 entanglement history | measured, one probe + one Lean | `jet_history_retention_probe.py` (Q1–Q4, no witness); `QOU/Knot/JetGradePromotion.lean` (4 theorems, sorry-free); bean `qou-dcvv` (todo, empty) | Q1: NF is **history-free** (same element ⇒ same profile); Q2/Q4: fresh generator ⇒ profile shifts **+1 rigidly**; Q3: negatives = inverse crossings | no content block; history relocates to the tower embedding `H_n → H_{n+1}` and nothing consumes that |
| I3 shadow prices | yes, three families | `def:knot-operator-energy` (`u_λ`, Plancherel `w_λ`); `prop:frobenius-pairing` (`y_λ`); `alg:lp-sdp-dual-emission` + ~50 producers (`y*`) | live consumers of `y*`: CO bond order = `\|active set\|`, VSEPR base angle, `a_K`, `σ_F(k)`, confinement-grading witness; `y₀*` ≡ 0 | which family "shadow price" means is unfixed; the three rank the deuteron's blocks differently (§5.2) |
| I4 q-distribution | yes, unnamed | `P(λ) = y_λ f^λ`: `MarkovNormalisation.lean` (`n = 2, 3`), O3′ probe (`n = 3..12`, all survivors positive); Hecke–Markov chain `prop:hecke-markov-transition` (`p_± = q²/(q²+1), 1/(q²+1)`, ASEP / Mallows) | this session: generic normalisation + expectation + convexity bound (`BlockMeasureFromFrobeniusPairing.lean`) | no block *names* `P` as a measure; the stochastic-mechanics chapter is an announcement ("Nelson-style") with no measure-theoretic block |
| I5 shared light cone / entangled phase space | fragments | `rem:light-cone-affine` (affine chart, causal structure on `M₀`); `def:jet-horizon` (degree-0 blocked, degree ≥1 leaks); `rem:two-observer-parallelogram` (`[δq₁,δq₂] = F_q` at one point) | this session: `entangledSupp(a,b) = {λ : χ_λ(a) ≠ χ_λ(b)}`; empty ⇒ equal traces ⇒ zero log-binding | no object for "the part of two light cones that overlaps"; no LR-branching constraint at `A ≥ 3` |
| I6 relative Reeb angle | no | single-knot angle `θ` (`prop:figure-eight-reeb-rotation`); ED `𝒮_p ≅ ℙ¹` with angles `(φ,ψ)` (`def:exceptional-divisor`); cusp meridian = one Planck step of rapidity `ln q₀` (`meridian-exceptional-divisor-note.md`); bond direction `(1, z)` in TL (`conj:reeb-linking-cwf-normalization`, no instance) | — | no datum relating **two** objects' flows; the "parallelogram" is a commutator of two observation directions at one point, not two knots |
| I7 O'Hara-energy SDP | no | `prop:mobius-energy` (categorical Möbius energy, climax chapter); `ohara1991` cited once (`mobius-surreal-renormalization`); library: Blatt–Vorderobermeier (critical points analytic), Rawdon–Simon (thick knots) | `CategoricalMobiusEnergy.classicalLimit` unconstraining (`qou-99qc`) | every LP/SDP objective in the corpus is linear (`Σ t_i x_i`) or a Frobenius residual; the 2026-08-24 exclusion is for **linear** objectives |
| I8 knot convolution `K` | yes | `def:ew-interface-knot`; `prop:knot-indexed-convolution-grid` (a classification grid); `binding_k_solver.py` `T_w(atom) = K·⊗T_w(nucleon_i)` | `K` determined; arity `2A+1` (46/46); not PSD; outside positive sector on `1 < q < q_c` | "SDP-selected `K`" is ill-posed once the words are fixed; selection lives on the words (`qou-ales`) |
| I9 jet tower / GB filtration | yes, heavily audited | `def:recursive-brane-tower`; `conj:binding-manybody-eq-jet-filtration` (**block exists**: `mass-theory/binding-manybody-jet-filtration.{ts,md,lean}` — a survey agent reported it orphaned; that was a filename miss); `prop:graded-markov-trace-from-gs-filtration` (Lean `opaque`, refactor deferred); `lem:bond-order-eq-jet-degree`; `prop:joint-tower-sdp-confinement` (GB-grading + jet-order constraints in the SDP) | three `J^•` readings excluded; unit-at-top exclusion; promotion +1 proved; body-number not `ε`-ordered, tower ordered by `q⁻²` | the level that indexes "history" is not `J^•` on words; the surviving route is the support map `T_w ↦ supp(T_w)` + `gbDepth` (§4.4) |

---

## 3. Ingredient notes (what the table compresses)

### 3.1 The LP dual: what survives the 2026-08/09 audits

Two readings sit side by side. The *emission contract* (`alg:lp-sdp-dual-emission`,
`alg:confinement-sdp`, AGENTS.md §LP/SDP duals) says *"the dual variables ARE
the binding-energy shadow prices; `y_star > 0` names the most receptive
sub-braids."* The *audit layer* (`2026-08-24-operator-selection-lp-objective-defect.md`,
now written into `operator-selection-lp.md:28–56`, `mass-coefficient-shadow-price.md`,
`knot-operator-energy.md`) establishes: `y₀* ≡ 0` because the NF basis contains
the identity and row 1 of `G x ≥ 0` *is* the objective; the argmin is a face;
`𝓑₃` is not a minimiser; the six-term mass coefficients are closed forms that
never solve an LP, so the shadow-price reading of them is an *interpretation*.

What is load-bearing after that: the **per-channel** `y*_λ` / active set. It
defines `def:knot-operator-energy` → `def:confinement-level`; it sets the CO
bond order (`co_bond_order_active_set.py`, `predicted_order = |active_set|`);
it gates the VSEPR base angle (`domain-weight-vsepr-angles.md`,
`hybridization_sp_gap_braid.py`); it supplies `a_K` (`aK_via_lp_dual_full.py`,
sum of duals over active blocks) and `σ_F(k)` (`sigma_f_electron_shell_chain.py`).
The owner's I3 is therefore *already the corpus's reading of the per-channel
dual* — and the corpus's own measurement says the reading is fragile:

- `H_{3A}` program: `T` and `³He` have the **same active set**
  (`(6,3),(7,2),(8,1),(9)`); only the scalar `y₀*` differs (`+0.0166` vs
  `+0.0288`). The LR branching that would make the program depend on `(Z, N)`
  exists only for the deuteron (`operator_selection_active_set_probe.py` §3).
- Positive sector (`x ≥ 0`, net constraint dropped, demand `u = G x_free` from
  LR profiles): **does** separate `T`/`³He` (supports of size 6 vs 9,
  structural in `q`) — but `x*` is provably not `K` and not proportional to it
  (`k_versus_selected_operator_probe.py`; `K(2H)`'s one negative coefficient is
  exactly `D_PN`, negative on `1 < q < q_c`). Owner ruling 2026-08-31 recorded
  in that probe: the demand may come from the un-positive free product; the
  program is a *forward-time cover*, kept as a probe, deliberately unwired.
- O3′ (block SDP on the radical quotient) is non-degenerate and its selection is
  **atom-independent** (`docs/proposals/2026-09-05-…§9d`).

### 3.2 The weight families, and why the probe compares ranks

`y_lambda_conflation_audit.py` (blocking, in `precision-gates.sh`) exists because
the Plancherel `w_λ(q) = d_q(λ)²/[n]_q!` and the Markov `y_λ` are not a
rescaling of one another: re-weighting the same Magnus `Ω₂` traces flipped the
sign of `P_total` at `A = 3, 4` (`qou-za3q`). `def:knot-operator-energy` builds
its `u_λ` on `w_λ`; `def:confinement-level` sorts by `|u_λ|`. So the *filtration
that defines the confinement level is indexed by the family the corpus's own
gate says must not be called a shadow price of the Frobenius pairing*. That is a
naming fact, not a numerical error — but it means I3 cannot be closed by
pointing at `def:knot-operator-energy`.

### 3.3 The stochastic chapter

`chap:stochastic-mechanics` (79 blocks) contains no Nelson, Itô, Fokker–Planck
or Madelung block; its intro says the Markov trace "admits an interpretation as
a transition kernel" and stops. The genuine `q`-stochastic object is in
`mass-theory`: `prop:hecke-markov-transition` — spectral idempotents
`e_± = (σ ± q^{∓1})/(q + q⁻¹)`, transition probabilities `p_+ = q²/(q²+1)`,
`p_− = 1/(q²+1)`, row-stochastic `K_i = p_+·id + p_−·s_i`, ASEP continuous-time
limit, Mallows stationary measure; Lean `prob_sum_one`, `p_plus_pos`,
`p_minus_pos`, `boltzmann_ratio` sorry-free. The state space of that chain is
SYT paths on the Young graph, not braid closures — so it is a chain *inside a
block*, while the measure of I4 is a measure *over blocks*. Both exist; neither
is joined to the other or to a "phase space".

### 3.4 Möbius energy

`prop:mobius-energy` and the climax-chapter blocks define a categorical
Möbius/O'Hara energy; no LP/SDP in the corpus has it as objective. The
2026-08-24 exclusion — *no linear objective can select `𝓑₃`* — is a statement
about linear functionals of `x`; the Möbius energy is a quadratic non-local
functional of the curve, so I7 is **not** pre-excluded. Two obstacles before it
can select anything: (i) `CategoricalMobiusEnergy.classicalLimit` carries its
constant as a free field, so it is satisfiable for any pair of energies
(`classicalLimit_unconstraining`, sorry-free; reported on #7390, not repaired,
owner call); (ii) what the energy is a functional *of* in the Hecke setting (a
word? a block vector? the closure's geometric realisation?) is not defined.
Library holds the two analytic results one would cite (critical points of the
Möbius energy are analytic; thick knots have bounded energy).

### 3.5 Molecular scale — the orientation is an output

For I1's "larger scale" clause: in `molecular-construction` and
`organic-chemistry` the combining operation is braid insertion + `q`-Young
symmetriser (`def:molecular-assembly-projector`, `def:molecular-hopf-chain`,
`prop:molecular-bond-binding-from-trefoil-insertion`), and **geometry is derived
from the LP dual**: methane's tetrahedron from `y_sym > 0`
(`prop:ch4-lp-dual-binding`), VSEPR angles from domain counts and `q^ℓ` weights
with *"we fit no angle"*, `C_{2v}` as the stabiliser of the projector. The one
directional gate is discrete (`sp³ ↔ pure-p` flip; `E_HB = h² E_cov`). So an
*input* relative orientation (I6) would reverse the chapter's derivation
direction. That is not an objection; it is the blast radius.

---

## 4. The jet tower / GB filtration, worked

### 4.1 What is settled (cite, do not re-derive)

- **Three inequivalent `J^•`** under one name — rewrite-depth, ideal-power
  image (provably `⊥` for `ℓ ≥ 1`, `WordFiltrationObstruction.lean`), Coxeter
  length — and all three excluded for the word-depth ↔ partition-depth bridge
  (`2026-08-16-three-gb-filtrations-one-name.md` + its superseding note;
  `2026-08-26-no-shift-rescues-the-word-partition-bridge.md`).
- **Unit at the top.** `1 = Σ_λ e_λ` uses every idempotent, and `τ(e_λ) ≠ 0`
  for every `λ`, so in any filtration spanned by normal forms the unit is
  dragged to the bottom while any idempotent-graded filtration puts it at the
  top; the two meet only for a constant grading. Scope-(b), invariant cited
  (`2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md`).
- **Spectral sequence is a no-go, not a tool** (`2026-08-25-…`).
- **Grade promotion is rigid.** Embedding `H_n → H_{n+1}` and multiplying by
  the new generator `T_n` shifts the whole GS profile by exactly `+1`
  (`JetGradePromotion.lean`: `sub_top_not_inversion`,
  `sub_top_inversion_after`; measured on eight words in
  `jet_history_retention_probe.py` Q4).
- **The tower, not body number, is the ordered expansion.** Every bond factor
  is `1/2` at `q = 1`, so `b₃(½,½,½) = −5/8 ≠ 0` — the body-number expansion has
  `ε`-valuation `0` (`BondFactorClassicalFloor.lean`:
  `bondFactor_classical`, `b3corpus_classical`, `b3_bondModel_classical`;
  probe 15/15); the jet tower `T(ρ) = Σ ℏ_q^{2n} Δ^{(n)}(ρ)` has geometric
  remainder ratio `q⁻²` (`rem:brane-tower-q-laplacian-decay-interpretation`,
  `BraneTowerLevelAmplitude.lean`).

### 4.2 New this session: the energy-ranked level puts the unit at the top

`def:confinement-level` sorts blocks by energy `E(λ, q)` and sets
`J^ℓ = ⟨λ : E(λ) ≤ E_ℓ⟩`, `ℓ(K, q) = min{ℓ : T_w ∈ J^ℓ}`. Whatever
"subalgebra generated by" means (unital or not), an element with full block
support is in `J^ℓ` only at the top, and the unit has full support because
`χ_λ(1) = dim V_λ ≠ 0`. Formally, for the character-support level
`level_E(x) = max{E(λ) : χ_λ(x) ≠ 0}`:

```
level_one_eq_top   : level E 1 = univ.sup E
level_le_level_one : level E x ≤ level E 1
```

(`BlockMeasureFromFrobeniusPairing.lean`, sorry-free, axioms
`propext, Classical.choice, Quot.sound`). Consequences:

1. The trivial closure and every free constituent product's neutral element sit
   at the **maximal** level. The ladder *quark = 0, nucleon = 1, atom = 2* of
   `def:confined-particle` — the ladder I1 speaks in — is a **different
   integer** from `ℓ(K, q)`. `intro-confinement-level.md`'s "how many
   reduction steps" is a third.
2. "Fewer directions at lower level" is true of the *support*
   `supp(T_w) ⊆ Λ`, not of an energy threshold: what a word at a given scale
   can see is the set of blocks its normal form touches, and under convention D
   that set is at most the two-row partitions (`massWeight_eq_zero_of_three_rows_of_wenzl`).
   For the deuteron it is exactly `{(6), (5,1), (4,2), (3,3)}` (§5.2).
3. The consumers that read `ℓ(K, q)` as the ladder —
   `stable-atom-decidable-proof.md` step 2, `ilp-solution-count-unwrap.md`,
   `unstable-atom-decay-phase.md`, the `confinement-grading-correspondence`
   witness ("LP active set = KLR support", `k_max ≤ 7`) — inherit the
   mismatch. No number in them is wrong; the *index* is.

### 4.3 What "history" can mean after the exclusions

The 2026-08-28 hypothesis in `jet_history_retention_probe.py` — *"previous
entanglement data will be shifted to a higher order upon subsequent particle
interactions … retained in the full filtration"* — survives in exactly the form
the probe and the Lean give it:

- the **normal form forgets the path** (Q1: same element ⇒ same profile,
  different jet log) — so history is not in `T_w ∈ H_n`;
- history enters through the **tower embedding**: the composite of an
  interaction lives in `H_m`, `m > n`, and the prior state's profile is carried
  up by exactly one grade per fresh generator (Q2/Q4, proved);
- the graded Markov trace `tr_{M,ℓ}` on `J^ℓ/J^{ℓ+1}`
  (`prop:graded-markov-trace-from-gs-filtration`) would read that history
  grade by grade — but its Lean is a `noncomputable opaque` with the refactor
  to `def + theorem` deferred, and which `J^•` it filters is the same
  three-way ambiguity.

So the honest statement of I2 today: **history = the grade of the tower
embedding, carried rigidly, invisible to the trace, and not yet indexed by any
filtration the corpus has been able to define on words.**

### 4.4 The route the audits leave open

`2026-08-26-the-unit-coefficient…md` §5: any statistic with `d(empty word) = 0`
is dead on arrival; re-found the indexing on the **partition side** via the
support map `T_w ↦ supp(T_w)` and `gbDepth λ` (already relocated onto the
Jucys–Murphy content axis by `gbDepth_eq_content_spread`). The block measure of
§5 is exactly a function on that partition side. Combining the two:

> the "directions" of I1/I3 are the blocks `λ ∈ supp(T_w)`; the weight of a
> direction is `P(λ) = y_λ dim V_λ` (or its `χ`-weighted displacement
> `y_λ(χ_λ(atom) − χ_λ(free))`); the level is a function of the support
> (`max gbDepth` or the two-row cap), not of an energy threshold.

That is a re-founding, not a fix, and it is **not done here** (§8, O2).

---

## 5. What landed this session (derived, not proposed)

### 5.1 Lean — `QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean`

Abstract Frobenius-pairing data `(trM, y, χ, dim)` with `trM = Σ y_λ χ_λ`,
`χ_λ(1) = dim λ`, `trM 1 = 1`; generic over `CommRing` / `Field`, with the one
`ℝ` theorem in the companion `BlockMeasureBindingFormArchimedean.lean` (§7c).
Verified `lean -DautoImplicit=false -s 65536`, exit 0, no warnings; `#print
axioms` on all seven theorems: `propext, Classical.choice, Quot.sound` only.

| declaration | content |
|---|---|
| `blockMass_sum_eq_one` | `Σ_λ y_λ dim λ = 1` — M1 through the pairing |
| `trM_eq_expectation` | `trM x = Σ_λ P(λ) · χ_λ(x)/dim λ` |
| `trM_le_of_normalised_le`, `le_trM_of_le_normalised` | with `y ≥ 0`, `trM x` lies between the min and max normalised character — the falsifiable content of "probability" (fails for `w_λ`) |
| `entangledSupp`, `trM_eq_of_entangledSupp_empty` | blocks where two elements' characters differ; empty ⇒ equal traces |
| `bindingForm_eq_zero_of_entangledSupp_empty` (ℝ; companion file `BlockMeasureBindingFormArchimedean.lean`, §7c split) | no shared block ⇒ `−α log(tr_M(atom)/tr_M(free)) = 0` |
| `charSupp`, `level`, `level_le_top`, `level_one_eq_top`, `level_le_level_one` | §4.2 |

Positivity of the convention-D weights is a **hypothesis** (`IsProbability`),
not derived; the corpus measures it (`sdp_o3prime_weight_positivity_probe.py`,
`n = 3..12`) and no general-`n` theorem exists. Registered in `QOU.lean`.

### 5.2 Probe — `computations/probes/deuteron_block_measure_entangled_support_probe.py`

Committed inputs only: `y-lambda-at-q0.witness.json` (proton pin, convention D,
`n = 6`), `atom-chi-rust-d.witness.json` (`χ_λ` of atom and free words, MPFR),
`deuteron-real-sdp.witness.json` (LP dual). mpmath 60 dps on the witnesses'
50-dps strings; `f^λ` exact. 6/6; witness beside the script;
`weight_family: markov_y_lambda_convention_D` declared.

| λ | `f^λ` | `y_λ` | `P = y f` | `χ_atom` | `χ_free` | `y(χ_A − χ_F)` | LP `y*` |
|---|---:|---:|---:|---:|---:|---:|---:|
| (6) | 1 | 0.11532 | 0.11532 | 1.55987 | 1.55131 | +0.00099 | 1.560 |
| (5,1) | 5 | 0.07895 | 0.39476 | −0.68229 | 0.72222 | **−0.11089** | 0.643 |
| (4,2) | 9 | 0.04603 | 0.41429 | 0.32908 | 0.82659 | −0.02290 | 0.186 |
| (3,3) | 5 | 0.01512 | 0.07562 | 0.71395 | 1.65567 | −0.01424 | 0.850 |
| seven ≥3-row blocks | — | 0 | 0 | (differ) | (differ) | 0 | 0.168 each |

- `Σ_λ P(λ) = 1.0` (50 dps); two-row masses positive; ≥3-row masses zero.
- Raw `χ` differs on **11/11** blocks; `y`-weighted entangled support is
  **exactly the four two-row blocks**, dominated by `(5,1)` (68 % of the
  absolute displacement).
- **Rank by `P`:** `(4,2) > (5,1) > (6) > (3,3)`. **Rank by LP `y*`:**
  `(6) > (3,3) > (5,1) > (4,2)`. The solver's filler value `0.1684` sits on
  every zero-weight block, i.e. its active set is *everything*
  (`active_set = [0..10]`, `y₀* = 2e-48`).
- From the pairing, `tr_M(atom) = 0.15197`, `tr_M(free) = 0.29902`. The LP
  witness records `tr_M_beta_D = 0.57517`. Both witnesses were last
  regenerated in the same commit (`870c65d84b`, 2026-09-15), so this is **not**
  the `7db032fb48` element-generation artifact; which element or normalisation
  `deuteron_real_sdp.py` traces is **not adjudicated here** and is recorded as
  a caveat in the witness.

### 5.3 What is deliberately NOT here

No conjecture class for I5/I6/I7 is committed. The §3b-tax rule requires a
carrier to assert real content; the content of "relative Reeb angle" and
"entangled phase space" is precisely what §6 says is undefined, so a class now
would be an empty marker or a guess. The Lean text that *would* be committed
under O3 is in §8 so the owner can read it before it exists.

---

## 6. Gaps

| # | gap | what would close it | cost |
|---|---|---|---|
| G1 | "shadow price" names three families; the confinement level is indexed by the one the conflation gate excludes | an owner ruling naming the family (O2 names `y_λ`); then re-index `def:knot-operator-energy`, `def:confinement-level` | 2 content blocks + Lean docstrings + `hecke_core_legacy.lp_shadow_price`; `confinement-grading` witness re-run |
| G2 | the level of `def:confinement-level` puts the unit at the top; the ladder of `def:confined-particle` is a different integer | re-found the level on the support map + `gbDepth` (audit §5 route) | new definition block; 4 consumer blocks re-read; the `k_max ≤ 7` witness re-run |
| G3 | no LR branching at `A ≥ 3`: `T`/`³He` indistinguishable to the `H_{3A}` program | compute `H_9 ⊃ H_3^{⊗3}` restriction multiplicities and the branched demand; **needs `pyhecke`** (absent in this container) | one producer; mechanical; the "shared phase space" becomes computable as joint-vs-product block masses |
| G4 | no probability object over *closures*; the Hecke–Markov chain is inside a block, `P` is over blocks; neither is joined to the other | a block that states `P` as the measure of record and relates the two | expository; no compute |
| G5 | no relative-orientation datum between two objects; ED angles `(φ,ψ)` are per point, `θ` is per knot | a definition — but its *content* (what two Reeb flows' relative angle changes in the Hecke data) is unknown; see O3 | a primary conjecture class, no instance |
| G6 | no non-linear (Möbius) objective; the carrier's classical limit is unconstraining | pin `classicalLimitConst` (owner call, `qou-99qc`); define the functional's argument in `H_n(q)` | formalize-first tranche; risk of another non-selecting route |
| G7 | `prop:graded-markov-trace-from-gs-filtration`'s Lean is `opaque`; which `J^•` it filters is ambiguous | the deferred `def + theorem` refactor, on the partition-side filtration | one Lean file; no numbers |
| G8 | `tr_M(atom)` from the pairing (0.152) vs `deuteron_real_sdp`'s recorded `tr_M_beta_D` (0.575) on witnesses from the same commit | read `deuteron_real_sdp.py` to see which element/normalisation it traces | ½ h; reported, not adjudicated |
| G9 | bean `qou-dcvv` has an empty body while its question is half-answered (Q1 measured, Q2/Q4 proved) | append the status (done in this PR); leave `todo` — the normal-form question is still open on the partition side | — |

---

## 7. Downstream impact

- **L2 dashboard / `Q_β` / `m_n` / `Δ_pn` / `m_K/m_π`:** no number moves.
  Nothing here changes an element, a weight, or a pin.
- **`qou-ales` / `qou-99qc` (element selection):** reading 3 of the confinement
  SDP — *"`χ_λ(w) ≥ 0` on every block with `y_λ > 0`"* — is, in this session's
  terms, **Frobenius positivity on `supp P`**. The rejection of
  `nuc11_interleaved` on `(2,1)` is a statement about the block measure's
  support. The block-measure reading therefore *sharpens* the ruling's
  vocabulary and changes none of its verdicts.
- **Ursell `b₃` sign (`qou-rwhv`, `qou-q8vl`, `qou-82mc`):** the chain bonds'
  traces are `P`-expectations; the sign-mixed pattern `b₃ > 0` needs is a
  statement about per-bond entangled supports. No change; a future per-bond
  `entangledSupp` table is the natural next measurement.
- **`qou-brng` (extensive term):** untouched. A distribution over blocks is
  intensive; it does not supply the super-pairwise additive term.
- **Confinement chapter (`def:confinement-level` and its four ILP consumers,
  `confinement-grading-correspondence` + witness):** the *index* is shown to be
  a different integer from the ladder (§4.2). No block is edited in this PR;
  G2 is the fix and it is an owner decision.
- **Molecular chapter:** an input orientation would invert "geometry is an
  output of the dual". Not touched.
- **`y_lambda_conflation_audit.py`:** the new probe declares `weight_family`
  and is clean; the analysis *names* the conflation at
  `def:knot-operator-energy` but does not sweep it (ask-first).
- **`conj:binding-manybody-eq-jet-filtration` consumers** (`binding-closure-conditional`,
  `jet-filtration-binding-extensive`, `binding-genfun-qdifference`,
  `linear-chain-bond-count`, `cyclotomic-boundary-at-keystone`): unchanged.
  The conjecture block exists; a survey agent's "orphaned label" report was a
  filename miss and is not propagated.

---

## 8. Options — each with what it means, costs, risks, commits to; default first

**Default (O1): nothing changes.** The Lean module and the probe stay as
derived, consumer-free additions. The confinement level keeps its Plancherel
index and its unit-at-top property; the L2 rows, `qou-ales` and `qou-brng` are
untouched. Safe to defer indefinitely.

**O2 — name the Markov block measure `P(λ) = y_λ dim V_λ` as the "q-distribution
on the block space" and re-found the level on the support.**
*Means:* one definition block (`def:markov-block-measure`) stating `P`, its
normalisation (Lean above), the convention-D two-row support, and the trace as
its expectation; `def:knot-operator-energy` and `def:confinement-level` re-indexed
from `w_λ` to `y_λ`, and the level redefined via `supp(T_w)` (§4.4).
*Costs:* 1 new block, 2 edited definitions, `hecke_core_legacy.lp_shadow_price`
and `confinement-grading-correspondence-conditional-witness` re-run (`pyhecke`
needed), 4 consumer blocks re-read (`stable-atom-decidable-proof`,
`ilp-solution-count-unwrap`, `unstable-atom-decay-phase`,
`shell-schur-weyl-self-duality-interpretation`). Roughly one tranche.
*Risks:* the tabulated confinement levels of every atom change (they are indexed
by a different family); the KLR-correspondence witness may stop matching. Both
are findings, not losses — the current match is against the excluded index.
*Commits to:* "shadow price of a direction" = `y_λ` everywhere; the Plancherel
`w_λ` is retired from the level (it stays wherever Molien/Plancherel is the
right object, per the 2026-09-05/08 rulings on `Φ_k`).

**O3 — formalise the relative Reeb datum as a primary conjecture class.**
*Means:* commit the following (no instance, content-bearing fields), after
which any block that uses it is `[RelativeReebDatum …]`-conditional:

```lean
/-- Two interacting closures carry a relative datum `angle ∈ S` (the owner's
"start of the parallelogram at the cusp of the ED") that DETERMINES the block
measure of the composite from the two incoming block measures. -/
class RelativeReebDatum (R : Type*) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (Λ₁ Λ₂ Λ : Type*) [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ] (S : Type*) : Prop where
  compose : (Λ₁ → R) → (Λ₂ → R) → S → (Λ → R)
  compose_nonneg : ∀ P Q s l, (∀ i, 0 ≤ P i) → (∀ j, 0 ≤ Q j) → 0 ≤ compose P Q s l
  compose_sum_one : ∀ P Q s, ∑ i, P i = 1 → ∑ j, Q j = 1 → ∑ l, compose P Q s l = 1
  /-- the datum matters: two values of `s` give different composites somewhere -/
  datum_nondegenerate : ∃ P Q s s', compose P Q s ≠ compose P Q s'
```

*Costs:* one Lean file, one conjecture block; nothing downstream.
*Risks:* it names an object whose physics is unknown; per §3b-tax it is honest
only while it has no instance and no consumer treats it as established. It
would also be the first place the corpus makes orientation an *input* (§3.5).
*Commits to:* a research direction, not a result. **My judgement: premature
until O5 shows whether `(Z, N)`-branching alone already separates the `A = 3`
pair.**

**O4 — re-pose selection with the categorical Möbius energy as objective.**
*Means:* replace `min Σ t_i x_i` by `min E_Möb(·)` over the same feasible set;
the 2026-08-24 linear exclusion does not apply.
*Costs:* first pin `classicalLimitConst` (`qou-99qc`, owner call) and define
what the functional takes as argument in `H_n(q)`; then a formalize-first
tranche before any solve.
*Risks:* the corpus has already retired two selection objectives for selecting
nothing (`2026-08-24`, O3′ §9d); a third with an undefined argument is the
same failure. Also `pyhecke`/`clarabel` absent here.
*Commits to:* an energy-based selection principle, which would need to be
shown *not* to be selection against the target (§NO FITTING).

**O5 — build the `A = 3` Littlewood–Richardson branching (the constraint the
corpus itself names as missing).**
*Means:* compute restriction multiplicities `H_9 ⊃ H_3^{⊗3}` and the branched
demand for `T` and `³He`; then the joint block measure of the bound word
against the pushforward of the product measure — the elementary
"entangled phase space" of I5 made computable (`entangledSupp` per bond, and
its mass).
*Costs:* one producer with `pyhecke_native` (not installable here; build with
`maturin` per AGENTS.md); mechanical; no new principle.
*Risks:* none to existing numbers; it is the input `nucleus_real_sdp.py`'s own
`note` field asks for.
*Commits to:* nothing beyond the data — but it is the measurement that would
tell us whether I6 is needed at nuclear scale at all.

**Recommendation, marked as judgement:** **O2 + O5**, in that order; O3 only
if O5 leaves `T`/`³He` degenerate under the block measure; O4 after `qou-99qc`
closes and never before. O1 is safe.

---

## 9. Discipline

- **No fit, no wiring, no tier change.** The probe reads three committed
  witnesses; the Lean is generic over a commutative ring / field with the
  archimedean log in its own section (§7c).
- **Corpus-grep** (six paths + `.beans/`) run for every "none found" above:
  `q-stochastic`, `entangled phase space`, `computational light cone`,
  `relative Reeb angle`, `O'Hara` × `objective|LP|SDP`, `phase space` ×
  `measure|distribution`, `entanglement history`, `knot convolution`. Library
  tiers 1–3 checked for O'Hara/Möbius (three documents; none couples to a
  program). The `ocr/` tier was not needed (no hit was a stub).
- **Corrected in passing:** a survey agent reported
  `conj:binding-manybody-eq-jet-filtration` as an orphaned label with no
  `.ts`/`.md`. All five sibling files exist; the report was a filename miss.
- **Not claimed:** that `P` is *the* q-distribution of the owner's picture; that
  the LP dual is wrong; that any refuted route is structurally excluded beyond
  the invariants the cited audits name; any binding number.
- **Beans:** `qou-mt94` (survey) completed; `qou-zu06` (this document)
  completed; `qou-jfx8` in progress (Lean landed; class not committed pending
  O3); `qou-dcvv` appended, left `todo`; `qou-0nrt` milestone open with the
  option list above.
