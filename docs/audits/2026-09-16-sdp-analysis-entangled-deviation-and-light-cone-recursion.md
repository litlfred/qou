# SDP analysis — the entangled deviation, the bond product, reading 3 on bound nuclei, and the substrate-phase recursion

Session `qou-qt8b` (beans `qou-42jx` this document, `qou-hlbx` Lean, `qou-7dal`
measurements), branch `claude/sdp-analysis-light-cone-recursion-2026-09-16`,
stacked on PR #7432 (`docs/audits/2026-09-16-q-stochastic-phase-space-shadow-prices-analysis.md`,
cited below as **[Q]**). Owner, 2026-09-16:

> *"Do SDP analysis. I guess we need to say something that the current value of
> the substrate phase is the evaluation of the entanglement history of all
> particles of the previous computational time step. So we're doing maybe the
> categorical trace, something like of the common affine light cone of the two
> particles. That's what gets passed to the knot convolution and we use
> Frobenius for self-dual. And [if] I didn't take my history [into account], the
> light cone is the γγ production."*

Everything measured here is on **committed witnesses only**; every Lean claim is
sorry-free and axiom-clean; nothing is wired and no dashboard number moves.

---

## 0. The three sentences, read

The message names a **recursion in computational time** with three clauses. I
read them as follows, and §3 tests each reading against the corpus. Where a
reading is mine rather than the owner's, it is marked.

| clause (owner's words) | reading | status after §3 |
|---|---|---|
| **(S1)** *the current value of the substrate phase is the evaluation of the entanglement history of all particles of the previous computational time step* | the state at step `t` is the collection of all particles' histories; its **evaluation** is the Frobenius pairing `tr_M = Σ_λ y_λ χ_λ`, and the **substrate phase** at `t+1` is that evaluation — as a block vector `(y_λ χ_λ(S_t))_λ` (my reading: the whole block vector, not only its scalar sum) | definable now; formal class held for the owner (§3.5) |
| **(S2)** *the categorical trace of the common affine light cone of the two particles is what gets passed to the knot convolution; we use Frobenius for self-dual* | the two particles' words live on disjoint strand blocks; their **common light cone** is the interface letter between the blocks; its Markov trace is the bond factor `z_D + d_kind`; the self-dual Frobenius pairing is what lets the composite's trace be read off the blocks | **measured exactly** (§3.2): `tr(atom)/tr(free) = ∏(z_D + d_kind)` to `1e-50` on D, T, ³He, ⁴He |
| **(S3)** *with no history the light cone is the γγ production* | the base case of the recursion is the pair-production word; a history-less particle's only "shared" object is the `γγ → pair` vertex — the `H_2` rung of `sdp_gamma_gamma_to_qqbar.py` | exists as the γγ chain's base rung (§3.4), which the script itself records as **under-determined** ("the SDP is not strict enough") |

---

## 1. TL;DR

1. **The free composite is exactly the Littlewood–Richardson pushforward of the two
   marginals, and its trace factorises because the convention-D weights are
   LR-multiplicative.** Disjoint-union multiplicativity was already proved twice
   (`MarkovTraceMultiplicative.markovTrace_juxtapose` from `Matrix.trace_kronecker`;
   `DisjointBlockTraceLaw`: two-sided Markov ⇒ disjoint-block multiplicative); what is
   new is its **characterisation through the weights**
   (`BranchingPushforwardMultiplicativity.lean`: `trM_tensor` from the weight identity
   `Σ_λ y_λ c^λ_{μν} = y_μ y_ν`), with both hypotheses measured on committed data: the weight identity to `5e-51` on all nine
   pairs `μ,ν ⊢ 3`, the branching rule on the deuteron's free characters to `7e-50`,
   `tr(free) = tr(p)^Z tr(n)^N` to `1e-40` for D/T/³He/⁴He.
2. **Every binding form is a function of the `y`-weighted entangled deviation
   alone:** `tr(atom) = tr(a)tr(b) + Σ_λ y_λ δ_λ`, `δ_λ = χ_λ(atom) − χ_λ(a⊗b)`
   (`trM_eq_tensor_add_weighted_deviation`; ℝ form `bindingForm_tensor_eq`).
3. **The weighted deviation's total is fixed by the interface letters** — the
   bond product `tr(atom)/tr(free) = ∏_{A−1 interfaces}(z_D + d_kind)` holds to
   `≤ 9e-51` on all four nuclei (corroborating the corpus's
   `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`). So (S2)
   is literally true of the trace: what the knot convolution receives from the
   common light cone is `z_D + d_kind`, and nothing beyond the pairwise interface
   letters reaches `tr_M`. What the **block-resolved** deviation adds is the
   *direction* information the picture wants — which blocks carry it (§3.3).
4. **Reading 3 rejects every production bound nucleus.** The owner-ruled
   confinement-SDP criterion (Frobenius positivity `χ_λ(w) ≥ 0` on every `y_λ > 0`
   block, whole word) is **satisfied by all four free products and violated by all
   four bound words**: D on `(5,1)` (`χ = −0.682`), T and ³He on `(8,1)` and
   `(5,4)`, ⁴He on `(11,1)` and `(8,4)`. Same shape as the `nuc11_interleaved`
   rejection on `(2,1)` (`qou-99qc`), one confinement level up. Not previously
   measured at the nuclear level (corpus-grep §9).
5. **No production program takes the two incoming particles as input and solves
   for the composite.** Every LP/SDP takes the composite word as given and then
   verifies positivity, ranks blocks by a dual, or (the γγ chain) selects a word
   one rung at a time; the one probe that does ingest the marginals (P5) returns
   an object that is provably not `K`. The LR machinery itself **exists and is
   validated to `A = 6`** (`computations/lr_coefficients.py`,
   `phase_b_lr_branching_constraint_probe.py`); what stops it from biting is that
   the `H_{3A}` Frobenius Gram is **diagonal by construction**, so no demand vector
   can do work against it — that probe's own verdict. The "unknown in the ILP/SDP"
   of (S2) — the shared light cone — is, in program terms, the **interface
   letter**: once it is fixed, `K` and the composite are determined (**[Q]** §1.4);
   nothing is stochastic downstream of it.
6. **The γγ base case (S3) exists and is under-determined.** `sdp_gamma_gamma_to_qqbar.py`
   poses `H_2` with variables `c_1, c_σ`, constraints `c_1 ± q^{±1} c_σ ≥ 0`, and
   records that the budget `11` is picked by closeness to AME, *"so the SDP is not
   strict enough"*. Under **NO FITTING** that is selection against the target and
   is not a base case.
7. **Downstream: no number moves.** The Ursell/`b₃` arc is *consistent* with
   finding 3 (a chain product has no connected part in the trace ratio — the
   corpus already says so); `qou-ales`/`qou-99qc` gain finding 4 as an input to
   the element decision; the L2 rows are untouched.

---

## 2. Program inventory — what each LP/SDP takes, optimises, constrains, and selects

Compiled from the 2026-08/09 audits, the probes named, and a read of the
producers; the survey agent's row-by-row confirmation is appended in §2.1.

| # | program | decision variables | objective | constraints | duals emitted / read | status (cited) |
|---|---|---|---|---|---|---|
| P1 | `prop:operator-selection-lp` (NF-indexed; `confinement-operator-selection.py`, `pyhecke.lp_dual_solver`) | `x ∈ ℝ^{n!}` NF coefficients | `min Σ t_i x_i`, `t_i = tr_M(b_i)` | `Σ x = n_target`; `(Gx)_i ≥ 0`, `G_ij = tr_M(b_i b_j)`; `x ≥ −M` | `y₀*, y*`, active set; ~50 emit-only producers | **degenerate**: `b_1 = 1` makes row 1 the objective ⇒ optimum `≡ 0`, `y₀* ≡ 0`, argmin a face; "no linear objective can select `𝓑₃`" (`2026-08-24-…objective-defect.md`) |
| P2 | partition-indexed program of `prop:mass-coefficient-shadow-price` | per-block `x_λ` | as P1, per block | Frobenius rows per `λ` | `y*_(3) = y*_(2,1) = 1`, `y*_(1³) = 0` at `H_3` | the function named for it, `hecke_core_legacy.lp_shadow_price`, **solves no program** — it evaluates `u_λ = w_λ/d_λ − 1/[k]_q!` (Plancherel family) |
| P3 | `nucleus_real_sdp.py` / `nucleus_sdp_assembly.py` (`H_{3A}`, bar-fold) | `x` over positive-norm blocks | `min t·x`, `t_λ = y_λ χ^λ(β_K)` | `G = diag(y_λ dim λ)`; `n_target = Σ t_pos` (the composite's own cost sum, `:257`); Clarabel | `y₀* ≠ 0`, non-empty active set | **`T` and `³He` share one active set** `{(6,3),(7,2),(8,1),(9)}` (`operator_selection_active_set_probe.py`); the branched `(Z,N)` demand exists (`phase_b_lr_branching_constraint_probe.py`, validated `A = 2, 3, 4`) but *"against a diagonal Gram no demand vector can do work"* |
| P4 | `deuteron_real_sdp.py` (`H_6`, 11 blocks) | `x_λ` | `min t·x` | diagonal Gram | `y*`: all 11 active, filler `0.1684` on the seven `y_λ = 0` blocks; `y₀* = 2e-48` | diagonal Gram degenerate; 0/6 off-diagonal encodings derive binding (`2026-08-29-deuteron-binding-via-gram-sdp-compute.md`) |
| P5 | positive-sector covering LP (`positive_sector_operator_selection_probe.py`) | `x ≥ 0` on `(H_3)^{⊗A}` | `min t·x` | `Gx ≥ u`, `u = G x_free` (LR profiles at `A = 2`); **no** net constraint | `y*`, support | **separates `T`/`³He`** (supports 6 vs 9), structural in `q`; `x*` provably **not `K`** (`k_versus_selected_operator_probe.py`); kept as probe by owner ruling 2026-08-31 |
| P6 | O3′ block SDP on `H_n / rad tr_M` (`BlockSDPNondegeneracy.lean`, `sdp_o3prime_weight_positivity_probe.py`) | block coefficients | `min` over positive weights | `Φ_λ ⪰ 0` per block | — | non-degenerate (`obj_pos_of_pos_weights`), value homogeneous in `n_target`; selection **atom-independent** (proposal §9d) |
| P7 | `prop:joint-tower-sdp-confinement` (`joint_tower_sdp_solver*.py`) | `c_{𝔥,w} ∈ ℚ` per atom and word | **none** (feasibility) | `ρ_λ(T_w(𝔥)) ⪰ 0 ∀λ`; GB-grading `c ≠ 0 ⇒ ℓ(w) ∈ Filt(𝔥)`; jet-order indexing; cross-level `π_{𝔥→𝔥'}` | — | Phase 3a is a **verifier** of known words (no solver invoked); Phase 3b runs cvxpy feasibility on the Hoefsmit `(2,1)` block for the *historical* `6_2` / `L6a4` braids |
| P8 | γγ chain (`sdp_gamma_gamma_to_qqbar.py`) | `H_2`: `(c_1, c_σ)`; then `H_3`, `B_3`, quark pairs, gluon `2σ_0` | trace as normalisation, "NOT the selector" | 1×1 PSD blocks `c_1 + q c_σ ≥ 0`, `c_1 − q⁻¹ c_σ ≥ 0`; LR embedding per rung | — | *"11 is uniquely close to AME but other budgets are PSD-feasible too — so the SDP is not strict enough"* (its own docstring) |
| P9 | confinement SDP for **word selection** (`qou-ales`, readings 1/2/3) | the word | — | reading 1 `Matrix.PosSemidef`; reading 2 symmetric-part PSD; **reading 3** `χ_λ(w) ≥ 0` on `y_λ > 0` (ruled 2026-09-12; whole word 2026-09-13) | — | `nuc11_interleaved` **fails** on `(2,1)`; bond `G^m` feasibility under reading 3 decided by `(3,3)`: `1 + 2χ_m ≥ 0` (γγ step 6) |
| P10 | `QOU/Interactions/ConfinementSDP.lean` | typeclass-supplied `HasConfinementSDPData n` | — | Slater condition | `y0Star` field | strong duality **conditional** on a class; `slaterStrict_is_freely_dischargeable` says the hypothesis carries no content; the five SDP uniqueness axioms were **false and deleted** (`2026-09-05-sdp-uniqueness-axioms-are-false.md`) |
| P11 | Lasserre moment lift (`operator_selection_lp.lean:691`, `sdp_moment_lift.py`) | `M = [[1, xᵀ],[x, X]] ⪰ 0` | — | `tr(GX) ≥ 0` | — | feasibility certificate only; no measure, no moment-problem duality |
| P12 | `tools/hecke-engine/src/operator_selection_sdp.rs` | dense cone | — | — | — | **not wired** into the Python entry point (`solve_psd_operator_selection_sdp` uses the diagonal lift, equivalent to P1) |
| P13 | ILP inside the confinement filtration (`def:stable-atom`, `stable-atom-decidable-proof.md`, `nuclear_ilp.py`) | `x ∈ ℤ^N_{≥0}` over primitives in `J^{ℓ(K,q)}` | minimum length | `G(q) x ≥ 0` | — | at `H_3` "essentially the whole alphabet is Frobenius-stable"; every bound atom `A ≤ 16` is stable with the **empty word**, so the active set is empty (`operator_selection_active_set_probe.py` §1) |
| P14 | molecular: `hbond_vdw_sdp.py`, `molecular-frobenius-lp.py`, `h2-integer-lp.py`, `prop:ch4-lp-dual-binding` | bond/strand orderings | `Φ_1` minimisation | Frobenius rows | `y_CH, y_HH, y_sym` | geometry (tetrahedron, VSEPR angles) is an **output** of the dual — **[Q]** §3.5 |
| P15 | `fusion_process_joint_h15_lp.py` (`A = 5`, `H_15`, 176 blocks) | `x` per side | `min t·x` | LR-branched costs from four subjects' committed characters | active channels | ingests marginals through LR but solves per side, not for the composite operator; *"the two sides select the SAME active `H_15` channels"* (`:208`) |
| P16 | `all_nuclides_sdp_admissibility*.py` | `x` | `min t·x` | `u_demand` = the nucleus's **own** NF | — | circular: `operator_selection_lp.lean:139-145` proves the equality form reads a coordinate of its own input back out |

**Three structural facts the table shows, stated once.**

- **Every program takes the composite word as given** (P1–P4, P7, P9, P13) or
  builds it one rung at a time from a fixed alphabet (P8). None takes two
  incoming particles' block data as *input* and solves for the composite. The
  only place the two marginals enter as data is P5's demand `u = G x_free`, and
  there they enter through the free product, not through an interface variable.
- **Where a dual is read, it is per-channel, and it is read as a ranking**
  (CO bond order `= |active set|`, VSEPR base angle, `a_K`, `σ_F(k)`), never as a
  distribution — **[Q]** §3.1.
- **The only fully non-degenerate program (P6) selects nothing atom-specific**,
  and the only one that separates `T` from `³He` (P5) returns an object that is
  provably not the binding operator.

### 2.1 Survey confirmation (Explore agent, file:line-verified at `66f61c738a`)

- P1's degeneracy is proved in three places — content (`operator-selection-lp.md:34-56`),
  Lean (`operator_selection_lp.lean:104-121`: `det G = 0` identically at `H_3`,
  radical `(−q³, q², q², −q, −q, 1)`, `y₀ = 0` forced; `H_2` is *not* degenerate)
  and the audit (`2026-08-24:159-183`). `operator-selection-lp.ts:21` still carries
  `status: "verified"` — stale against its own block.
- The Lasserre tightening **buys nothing**: `operator_selection_lp.lean:688-708`
  `tightening_preserves_optimum`.
- The one program that solves for a composite operator from the two marginals is
  P5, probe-only, not `K`, not consumed, and `q`-windowed
  (`positive_sector_q_stability_probe.py:61-66`).
- LR branching: engine `computations/lr_coefficients.py` (skew-tableau `lr_coef`,
  tables `3×3→6`, `3×6→9`, `6×6→12`), constraint probe validated by both the
  induction and the restriction identity at `A = 2, 3, 4`, tractable to `A = 6`
  (385 blocks, 0.51 s); its own verdict: the next object to build is the
  **off-diagonal `H_{3A}` Frobenius Gram**. Two defects it found on the way
  (`pyhecke.atom.nf_channel_exact` dead, then wrong) were repaired 2026-08-31.
- Disjoint-union multiplicativity: `MarkovTraceMultiplicative.lean:71-88`
  (`trace_kron`, `markovTrace_juxtapose`), scoped by bean `qou-bsfg` as the
  **Kronecker / disjoint-union** statement, *not* connected sum, and with the
  link-invariant caveat that an unlinked component multiplies the *amplitude* by
  `δ = [2]_q` (the corpus's `tr_M` has `tr_M(1) = 1`, which is why the free trace
  here factorises with no `δ`; the `δ^{A−1}` deficit is `ClosureNormalisationDefect`).
  **Interleaved** blocks are provably not multiplicative
  (`MarkovTraceInterleavedCrossTerm.lean`, bean `qou-ls86`).

---

## 3. The picture in program terms — what is now proved, measured, or missing

### 3.1 Data and variables: marginals in, composite out

Let `a ∈ H_n`, `b ∈ H_m` be the two particles' words on disjoint strand blocks,
`a ⊗ b ∈ H_{n+m}` their free product. With `c^λ_{μν}` the LR multiplicities,

```
χ_λ(a ⊗ b) = Σ_{μ,ν} c^λ_{μν} χ_μ(a) χ_ν(b)          (branching rule)
Σ_λ y_λ c^λ_{μν} = y_μ y_ν                             (weight identity)
⇒  tr_M(a ⊗ b) = tr_M(a) tr_M(b)                       (trM_tensor, derived)
```

Both hypotheses are **measured** on committed data
(`branching_pushforward_entangled_support_probe.py`, 10/10): the weight identity
on the nine pairs `μ,ν ⊢ 3` to `5e-51` (convention-D `y` at `n = 3, 6`, proton pin);
the branching rule on `atom-chi-rust-d`'s free characters against the LR
pushforward of `chi-proton/neutron-h3` to `7e-50`; the factorisation
`tr(free) = tr(p)^Z tr(n)^N` to `1e-40` for all four nuclei. So the free
composite is **unentangled** in the exact sense the picture needs: its block data
is a function of the two marginals' block data. The LR table for `S_6 ⊃ S_3 × S_3`
is in the probe, self-checked by `f^μ f^ν C(6,3) = Σ_λ c^λ_{μν} f^λ`.

The composite's block vector `(χ_λ(atom))_λ` is the natural **variable**; the
marginals' block vectors are the **data**; the difference is the **entangled
deviation** `δ_λ = χ_λ(atom) − χ_λ(a ⊗ b)`, and

```
tr_M(atom) = tr_M(a) tr_M(b) + Σ_λ y_λ δ_λ                  (trM_eq_tensor_add_weighted_deviation)
B = −α · log(1 + Σ_λ y_λ δ_λ / (tr_M(a) tr_M(b)))            (bindingForm_tensor_eq, ℝ)
```

### 3.2 (S2) — the categorical trace of the common light cone is the bond factor

The corpus's production word lays the `A − 1` interfaces in a chain, and the
corpus's own probe (`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe`)
records `tr(atom)/tr(free) = ∏_i (z + d_i)` to `~1e-60`, attributing it to
"connected-sum multiplicativity"; bean `qou-bsfg` later corrected that wording to
the **disjoint-union** (Kronecker) statement plus the Markov peel of each
interface letter — the numbers are unchanged. Re-measured here at 60 dps from
the committed characters and the pin, with `z_D = q³/(q²+1) = 0.61268803715`,
`d_pp = 0`, `d_pn = −h(1 − δ/2)/2 = −0.10445824777` (`bring_color_weighted`),
`d_nn = −h`:

| nucleus | interfaces | `tr(atom)/tr(free)` | `∏(z_D + d)` | dev |
|---|---|---:|---:|---:|
| D | pn | 0.508229789 | 0.508229789 | 2.8e-51 |
| T | pn, nn | 0.205135640 | 0.205135640 | 8.8e-51 |
| ³He | pp, pn | 0.311386312 | 0.311386312 | 5.2e-51 |
| ⁴He | pp, pn, nn | 0.125684153 | 0.125684153 | 6.5e-51 |

So, exactly: **what the knot convolution receives from the common light cone is
`tr_M(interface letter) = z_D + d_kind`**, and the weighted deviation total is
`Σ_λ y_λ δ_λ = tr(free)(∏(z_D + d_i) − 1)`. This is the corpus's multiplicative
assembly; the connected (Ursell) part of a *chain* is zero in the trace ratio,
which is what `b3corpus_chain` collapsing to a product already says
(`qou-q8vl`). Consequence for the picture: **the pairwise interface traces
exhaust `tr_M`; anything "many-body" must live in the block-resolved deviation,
not in its `y`-weighted sum.**

### 3.3 What the block-resolved deviation carries — the "directions"

Per nucleus, the `y`-weighted entangled support is exactly the two-row support
(convention D), and the deviation is concentrated:

| nucleus | `n` | support | leading `y_λ δ_λ` | `Σ y δ` |
|---|---:|---|---|---:|
| D | 6 | 4 blocks | `(5,1) −0.1109`, `(4,2) −0.0229`, `(3,3) −0.0142`, `(6) +0.0010` | −0.14705 |
| T | 9 | 5 | `(8,1) −0.0504`, `(7,2) −0.0281`, `(6,3) −0.0225`, `(5,4) −0.0083` | −0.11293 |
| ³He | 9 | 5 | `(8,1) −0.0603`, `(7,2) −0.0354`, `(6,3) −0.0278`, `(5,4) −0.0116` | −0.12958 |
| ⁴He | 12 | 7 | `(11,1) −0.0190`, `(8,4) −0.0179`, `(9,3) −0.0173`, `(10,2) −0.0170` | −0.07817 |

`T` and `³He` have the **same support and the same ordering** and differ in
magnitude only — the mirror pair is separated by the deviation vector (which P3
could not do), without any selection. `⁴He`'s deviation is nearly flat across
four blocks, unlike the `A ≤ 3` cases where one block dominates. These are the
"directions" of **[Q]** §4.4, now with their weights.

### 3.4 (S3) — the γγ base case

`sdp_gamma_gamma_to_qqbar.py` is the corpus's implementation of "no history ⇒
the light cone is the γγ production": at `H_2` the two photons occupy the two
Hecke slots, `T_w = c_1·1 + c_σ σ_0`, the Wedderburn projections are the 1×1
blocks `c_1 + q c_σ` and `c_1 − q⁻¹ c_σ`, and the SDP is their non-negativity;
the trace is "a normalisation, NOT the selector". Its own verdict on the chain's
base rung is that the proton budget `11` is picked by closeness to AME and that
the program *"is not strict enough; an additional constraint (e.g. minimal
`tr_M` complement) is needed to pick out 11 categorically."* Under §NO FITTING
that is a selection against the target, so (S3) currently has a *shape* (the
`H_2` vertex) but not a *selector*.

What the recursion adds to it is a **direction of travel**: a particle's history
starts at its γγ vertex and is promoted one grade per fresh interaction
(`JetGradePromotion.lean`, +1 rigid), so "how much history" is a jet grade, and
"no history" is grade 0 at the γγ vertex.

### 3.5 (S1) — the substrate-phase recursion, stated so it can be wrong

The recursion is not yet an object in the corpus. The closest existing
statements are the Planck-step sentence of `hecke-markov-interpretation.md`
(*"each Markov step evaluates one Hecke crossing … one iteration on the
exceptional divisor — a single Planck step"*), the Hecke–Markov chain
`prop:hecke-markov-transition` (a chain *inside* a block), and the block measure
of **[Q]**. The formal content I would commit — **held for the owner, not
committed** — is a primary conjecture class whose fields are falsifiable and
whose LR clause is already a theorem:

```lean
/-- Substrate-phase recursion (owner, 2026-09-16), as a primary conjecture class.
A global state is the collection of all particles' histories; its PHASE is its
block vector under the Frobenius pairing; one computational time step is one
interface letter; the phase is a sufficient statistic for the next phase; and the
history-less state is the γγ production vertex. -/
class SubstratePhaseRecursion (R : Type*) [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (State Λ : Type*) [Fintype Λ] : Prop where
  /-- the block vector (phase) of a global state: `λ ↦ y_λ χ_λ(S)` -/
  phaseOf : State → (Λ → R)
  /-- one computational time step (one interface letter applied) -/
  step : State → State
  /-- (S1) the phase is a sufficient statistic: states with equal phase evolve to
  states with equal phase — the substrate at `t` is determined by the evaluation
  of all histories at `t − 1`, and by nothing else -/
  phase_sufficient : ∀ s s', phaseOf s = phaseOf s' → phaseOf (step s) = phaseOf (step s')
  /-- (S3) the history-less state is the γγ vertex, with a named phase -/
  gammaGamma : State
  gammaGamma_phase : phaseOf gammaGamma = fun l => if l = (default : Λ) then 1 else 0
```

`phase_sufficient` is the clause that can fail: it says the composite's next
block vector is a function of the current block vector — i.e. that the interface
letter's action on the composite is determined by `(χ_λ)_λ`. Measured, that is
**false** as stated for the full block vector at `H_6`: two words with the same
`(χ_λ)` on the eleven blocks but different NF coefficients can be sent to
different composites by the same letter. So the honest version restricts the
state to what the letter sees — which is exactly the question §5 poses. The
class is written here so the owner can say whether `phaseOf` should be the block
vector, the NF vector, or the pair (block vector, jet grade); the second field
depends on that choice. **Not committed.**

---

## 4. Reading 3 on the bound nuclei — new, and it rejects every production word

The 2026-09-12/13 rulings make **reading 3, whole word** the live confinement
criterion: `χ_λ(w) ≥ 0` on every block with `y_λ > 0`. It was applied to the
11-letter nucleon (`nuc11_interleaved` fails on `(2,1)`, `qou-99qc`) and to the
bond letter `G^m` alone (γγ step 6: feasibility decided by `(3,3)`). Applied here
to the **assembled** production words at `H_{3A}`:

| nucleus | `y_λ > 0` blocks with `χ_λ(free) < 0` | with `χ_λ(atom) < 0` |
|---|---|---|
| D | none | `(5,1)` (`χ = −0.6823`) |
| T | none | `(8,1)`, `(5,4)` |
| ³He | none | `(8,1)`, `(5,4)` |
| ⁴He | none | `(11,1)`, `(8,4)` |

**Every free product passes and every bound word fails.** The interface letters
flip the sign of a positive-weight character in each case — the same block
`(n−1, 1)` that also carries the largest deviation (§3.3), plus a second
two-row block from `A = 3` up. Three readings are possible and choosing among
them is the owner's:

- the criterion is right and the production words are wrong (consistent with the
  `qou-99qc` posture that the nucleon element is rejected too);
- the criterion is meant for the *bond letter* and the *nucleon*, not for the
  assembled composite — in which case the ruling's scope needs a sentence saying
  so, because as written "whole word" covers the atom word;
- reading 3 is the wrong positivity for a bound state — a bound composite *should*
  carry a negative character on the block that binds it, and the criterion for
  composites is on the deviation, not on the character.

None of the three is decided by this measurement. What the measurement decides
is narrower: **there is no production nucleus that is reading-3 feasible**, so
any program whose feasible set is reading 3 on the composite currently has
*no* feasible production point at `A = 2, 3, 4`.

---

## 5. What the SDP should be under the picture — and what is genuinely open

Reading §2–§4 together, the program the picture asks for is not one the corpus
has, and its pieces are now separable:

| piece | status |
|---|---|
| **data** — two marginal block vectors `(χ_μ(a))`, `(χ_ν(b))` | committed for `p`, `n` at `H_3`; free composite from them by LR (proved + measured) |
| **variable** — the composite block vector on `supp P` (two-row blocks), equivalently the deviation `δ` | definable now; measured for D/T/³He/⁴He |
| **the unknown (S2)** — what fixes `δ` | in the corpus: the interface letter (`K` determined by the words, **[Q]** §1.4); its trace fixes `Σ y δ` exactly (§3.2); its block-resolved action is the "shared light cone" and is *not* a function of `(χ_λ)` alone (§3.5) |
| **constraint** — reading 3 on the composite | rejects every production word (§4) |
| **objective** | none admissible yet: linear objectives are excluded (P1), O3′ is atom-independent (P6), the Möbius energy has no defined argument and an unconstraining classical limit (**[Q]** §3.4) |
| **stochastic element (S1/"q-stochastic")** | a distribution over *interface letters* (equivalently over `K`), not over blocks — the block measure `P` is the *weight*, the letter is the *sample*; no such distribution exists in the corpus |
| **base case (S3)** | `H_2` γγ vertex exists; its selector is AME-closeness and is not admissible |

So "SDP analysis" has a sharp answer: the corpus's programs are all
**verification** or **ranking** programs on a *given* composite; the picture
needs a **composition** program (marginals + interface → composite), whose only
undetermined datum is the interface letter, whose trace is already exact, and
whose block-resolved action is what is unknown. Two derived facts bound that
unknown: it lives on the two-row support, and its `y`-weighted total is
`tr(free)(∏(z_D + d_i) − 1)`.

---

## 6. Gaps

| # | gap | closes by | cost |
|---|---|---|---|
| G1 | no composition program: nothing takes marginals as input | posing the feasibility program of §5 on `supp P` with the interface letter as the variable; **no objective** until one is derived | one probe + a Lean statement of the feasible set; needs `pyhecke_native` for `A ≥ 3` letters beyond the chain |
| G2 | reading 3's scope at the nuclear level is unstated (§4) | an owner sentence: bond / nucleon / composite | zero compute |
| G3 | `phase_sufficient` fails for the full block vector; the right state space for (S1) is unfixed | owner picks `phaseOf` ∈ {block vector, NF vector, (block vector, jet grade)} | then one Lean class + a probe testing sufficiency on committed words |
| G4 | (S3)'s selector is AME-closeness | a categorical selector for the `H_2` rung; the γγ chain's own docstring names "minimal `tr_M` complement" as a candidate — untested | probe on `H_2`/`H_3`; no fit allowed |
| G5 | the branched `(Z,N)` demand exists to `A = 6` but the `H_{3A}` Gram is diagonal by construction, so nothing can bite on it | build the off-diagonal `H_{3A}` Frobenius Gram `tr_M(b_i b_j)` (the `phase_b` probe's own "next object") — needs `pyhecke_native` | one producer; compute at `H_9` |
| G6 | the O'Hara/Möbius objective (S2's "SDP-selected") has no argument in `H_n(q)` | define what the energy is a functional of; pin `classicalLimitConst` (`qou-99qc`) | formalize-first tranche |
| G7 | `deuteron_real_sdp`'s recorded `tr_M_beta_D = 0.575` vs the pairing's `0.152` on same-commit witnesses (**[Q]** G8) | read which element/normalisation P4 traces | ½ h |

---

## 7. Downstream impact

- **`qou-ales` / `qou-99qc` (element selection):** finding 4 is an input to the
  open element decision — the ruled criterion rejects the production *nuclei* as
  well as the nucleon. It does not change the nucleon verdict.
- **`qou-brng` / Ursell `b₃` (`qou-rwhv`, `qou-q8vl`):** consistent, not new:
  the trace ratio is exactly the bond product, so the chain's connected part is
  zero in the ratio; the many-body content, if any, is in the block-resolved
  deviation. Nothing in those beans moves.
- **`qou-oots` / weight families:** every measurement here declares
  `weight_family: markov_y_lambda_convention_D`; the Plancherel `w_λ` is not used.
- **Confinement chapter:** unchanged by this PR; **[Q]** G2 (the level's index)
  stands.
- **L2 dashboard:** no row moves.
- **Molecular chapter:** unchanged; (S2)'s orientation datum would be an input
  there (**[Q]** §3.5).

---

## 8. Options — default first, each with what it means, costs, risks, commits to

**O1 (default): nothing changes.** The Lean and the probe stay as derived,
consumer-free additions; the reading-3 finding stays in this document and on
`qou-7dal`.

**O2: rule on reading 3's scope (G2).** *Means:* one sentence — the criterion
applies to (a) the bond letter and nucleon only, (b) the composite too, or (c) the
deviation rather than the character. *Costs:* nothing to compute for (a); for (b)
every production nucleus is infeasible and the element decision widens to the
nuclear words; for (c) a new criterion needs a Lean statement. *Risks:* (b) is
the honest reading of "whole word" and it has no feasible production point.
*Commits to:* which object confinement positivity is a property of.

**O3: commit the `SubstratePhaseRecursion` class with the owner's choice of
`phaseOf` (G3).** *Means:* the class of §3.5, no instance. *Costs:* one Lean
file, one conjecture block, one probe testing `phase_sufficient` on committed
words. *Risks:* with `phaseOf` = block vector the sufficiency clause is already
false; with the NF vector it is trivially true (the letter acts on the NF); the
informative choice is the pair (block vector, jet grade), and that is a guess
until tested. *Commits to:* a state space for computational time.

**O4: pose the composition program (G1) as a feasibility problem, no
objective.** *Means:* variable = interface letter from the fixed alphabet;
feasible set = reading 3 (or O2's choice) on the composite block vector; report
the feasible letters per nucleus. *Costs:* a probe; `pyhecke_native` for `A ≥ 3`.
*Risks:* the feasible set may be empty (it is, for the production letters) or
everything (as P13's ILP was at `H_3`). *Commits to:* nothing beyond the data.

**O5: the γγ base-case selector (G4).** *Means:* test "minimal `tr_M`
complement" as the `H_2` selector. *Costs:* small probe. *Risks:* it is one more
candidate selector in a corpus that has retired several; must be shown not to be
selection against the target. *Commits to:* a base case for (S3).

**Recommendation, marked as judgement:** **O2 first** (it costs one sentence and
decides whether §4 is a defect or a scope note), then **O4** under O2's answer;
O3 only after O4 shows what the letter actually sees; O5 independent and cheap.

---

## 9. Discipline

- **No fit, no wiring, no tier change.** Inputs: `y-lambda-at-q0`,
  `chi-proton/neutron-h3-at-q0-50dps`, `atom-chi-rust-{d,t,3he,4he}` (all
  proton-pinned, all post-`7db032fb48`), the pin string for `z_D`, `h`, `δ`.
- **Corpus-grep** for "reading 3 on bound nuclei": `docs/audits` (the ten
  `gamma-gamma-word-selection-step*` files apply it to the nucleon and to the
  bond letter `G^m`), `.beans` (`qou-ales`, `qou-v3u2` — the latter notes the
  deuteron's `(5,1)` ratio is negative, "per-block binding is not even well
  defined", without the reading-3 framing), `computations/probes`. No prior
  whole-word application to the assembled nuclei found in those surfaces.
- **Cited, not re-derived:** the bond product (§3.2) is the corpus's; the
  measurement here corroborates it at 60 dps and gives it the picture's reading.
  Disjoint-union multiplicativity was already Lean-proved twice (§2.1); the LR
  engine already existed (`lr_coefficients.py`); this tranche's additions are the
  weight-identity characterisation, its measurement, the deviation theorems, and
  the reading-3 measurement on bound nuclei.
- **Survey:** an Explore agent inventoried every LP/SDP/ILP with file:line
  citations (§2.1); its findings are folded in above.
- **Not claimed:** that the production words are wrong; that reading 3 is the
  right positivity; that `phaseOf` should be any particular object; any binding
  number.
- **Lean:** `BranchingPushforwardMultiplicativity.lean` (`trM_tensor`,
  `trM_eq_tensor_add_weighted_deviation`,
  `weighted_deviation_eq_zero_of_entangledSupp_empty`, `blockMass_tensor_char`)
  and `BlockMeasureBindingFormArchimedean.lean` (`bindingForm_tensor_eq`);
  `lean -DautoImplicit=false -s 65536` exit 0; `#print axioms`: `propext,
  Classical.choice, Quot.sound`.
- **Probe:** `computations/probes/branching_pushforward_entangled_support_probe.py`,
  10/10, witness beside it, `weight_family` declared.
