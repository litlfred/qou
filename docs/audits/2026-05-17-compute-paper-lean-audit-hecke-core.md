# Compute → paper → Lean audit: Hecke-core (7 files)

**Scope.** Walk each math-bearing function in seven Hecke compute files,
match it to a content block (`.md`/`.ts`) in
`content/quantum-observable-universe/`, and check the sibling `.lean`
status (PROVEN / HAS_SORRY w/Ref / MISSING). Imports / I/O / CLI glue
skipped per instructions.

**Date.** 2026-05-17. Branch state at audit time.

**Legend.**
- **STANDARD** — universal math; no QOU-specific theorem required.
- **PROVEN** — Lean theorem closed, no `sorry`.
- **HAS_SORRY** — Lean sibling exists but at least one `sorry`;
  cited reference noted.
- **STUB** — Lean sibling exists but placeholder content (e.g.
  `wenzlSchurElement := 0 * (...)`).
- **LEAN_MISSING** — paper block present, no `.lean` sibling.
- **PAPER_MISSING** — compute claim with no narrative block.

---

## 1. `computations/substrate/hecke_core.py`  (3173 LOC)

Largest of the seven — canonical Hecke infrastructure for `H_3(q)`
extended with partition-table machinery and per-generator atomic
construction.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 216–237 | `q_hook_product(λ)` | Hook-product `$H_q(λ) = \prod_x [h_x]_q$` |
| 240–245 | `q_factorial(n)` | `$[n]_q!$` |
| 248–260 | `partitions_of(n)` | Combinatorial enumeration |
| 263–279 | `partition_dimension(λ)` | Hook-length formula `$d_λ = n!/\prod h_x$` |
| 282–296 | `partition_conjugate(λ)`, `partition_is_self_conjugate` | Young-diagram transpose |
| 299–324 | `partition_jet_depth(λ)` | Max content magnitude |
| 327–340 | `q_dimension(λ)`, `wedderburn_weight(λ)` | `$d_q = [n]_q!/H_q$`, `$w_λ = d_q^2/[n]_q!$` |
| 343–383 | `q_laplacian_eigenvalue(λ)` | JM-Casimir `$μ_λ = \sum_□ [c]_q[c+1]_q$` |
| 386–411 | `q_resolvent_weight(λ, s)` | Resolvent `$1/(μ_λ + s_*)$` from q-heat spectrum |
| 414–441 | `lp_shadow_price(λ)` | LP-dual price `$y_λ = w_λ/d_λ - y_0$` |
| 465–505 | `_count_syts_by_12_relation` | SYT count by (1,2)-relation |
| 508–516 | `partition_character_sigma1(λ)` | `$χ_λ(σ_1) = q\cdot n_r + (-q^{-1})n_c + h\cdot n_m$` |
| 519–533 | `partition_spectral_log_rate(λ)` | Average per-crossing log rate |
| 718–787 | `build_atom_nf_exact(Z,N)` | Exact NF for atomic braid via `hm_exact` |
| 790–807 | `nf_channel_exact(nf)` | Sym/std/alt channel decomposition `$χ_λ$` |
| 810–833 | `knot_factor(Z,N)` | A-specific topological factor (A=3: `$1-h^2$`) |
| 836–841 | `check_frobenius(nf)` | `$G\cdot x \ge 0$` (Frobenius positivity) |
| 848–923 | `build_atom_nf(Z,N)` | Build atom NF: B₃ + quark + inter-nucleon + electron crossings |
| 930–947 | `vertex_volume(chain)` | 3-channel Wedderburn-weighted volume `$V_{full}$` |
| 950–984 | `nucleon_gen_chains(quarks)` | Per-gen crossings for one nucleon (B₃ + quarks + 2 gluon) |
| 992–1051 | `atom_gen_chains(Z,N)` | Per-gen crossings for atom |
| 1052–1095 | `atom_V_full`, `_chain_V_full` | Atom-level full volumes |
| 1096–1141 | `_crossing_coeff`, `_phi1_from_ordering` | `$Φ_1 = \sum \ln|z\cdot a + b|$` |
| 1160–1265 | `_phi1_nuclear`, `compute_phi1_full` | Three-invariant `$Φ_1,Φ_2,Φ_3$` accumulators |
| 1281–1411 | `_vertex_channels`, `molecular_binding_nf`, `molecular_binding_frobenius` | Molecular binding via vertex channels |
| 1591–1744 | `_standard_tableaux`, `_swap_tab`, `_build_ysn_matrices` | YSN-matrix construction (Hoefsmit seminormal) |
| 1907–2226 | `unified_iterative_correction` | Iterative LP-dual binding accumulator across partitions of k=2..k_max |
| 2233–2298 | `atom_character_raw(Z,N,entry)` | `$χ_λ(\text{atom braid})$` via YSN-matrix multiplication |
| 2383–2455 | `conjugate_pair_cross_term` | Self-conjugate `$λ + λ'$` pairing |
| 2621–2689 | `atom_markov_trace(Z,N)` | `$tr_M(\text{atom}) = \sum_λ w_λ χ_λ$` |
| 2691–2744 | `atom_frobenius_norm_sq` | Frobenius-pairing inner product per partition |
| 2746–2884 | `atom_per_generator_volumes` | Per-σᵢ Wedderburn-weighted volumes |
| 2931–2985 | `binding_from_frobenius_pairing` | Binding via Frobenius positivity |
| 2987–3075 | `sdp_cross_channel_contribution` | PSD-SDP cross-channel piece |
| 3077–3096 | `binding_energy(Z,N)` | Total binding `$E_B$` |
| 3098–3138 | `build_nucleon_nf(quarks)` | Nucleon NF (Borromean B₃ × pairwise) |
| 3139–3161 | `q_value_beta`, `atom_mass(Z,N)` | β-decay Q-value, total atomic mass |

### (B) Paper backing & (C) Lean status (key claims only)

| Compute claim | Paper block (`.md`) | Label | Lean |
|---|---|---|---|
| Hoefsmit YSN matrices (`_build_ysn_matrices`, lines 1647–1744) | [hoefsmit-seminormal-form.md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md) | `prop:hoefsmit-seminormal-form` | **PROVEN (core lemmas).** `hoefsmit_block_det`, `hoefsmit_block_trace`, `hoefsmit_product_rho2`, `figure_eight_hoefsmit_trace` all closed in [hoefsmit-seminormal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.lean) (no sorry). Diagonal entry `$a_ρ = h/(1-q^{-2ρ})$`, off-diagonal `$b²=a·a'+1$`, det=−1 all proved. **The full ρ_λ(σᵢ): H_n(q) → M_{d_λ} representation property (braid + Hecke relations on the matrices) is NOT a Lean theorem** — only the 2×2 block algebraic identities. |
| Hecke quadratic `σ² = (q−q⁻¹)σ + 1` | [hecke-algebra-from-braiding.md](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md) | `rem:hecke-algebra-from-braiding` | **LEAN_MISSING.** Remark cites `thm:jones-markov-trace` and `prop:braiding-eigenvalue-extraction`, but the quadratic relation itself is asserted at the level of categorical eigenvalues, not formalized as a Lean equation on a Hecke-algebra type. |
| Braid relation `σᵢσⱼσᵢ = σⱼσᵢσⱼ` (`|i−j|=1`) | [braid-group.md](../../content/quantum-observable-universe/braids-and-knots/braid-group.md) | `def:braid-group` | **PROVEN as definition.** `BraidGroupData.braid_relation` in [braid-group.lean](../../content/quantum-observable-universe/braids-and-knots/braid-group.lean) — axiomatized as a structure field. STANDARD; no further theorem needed. |
| `$y_λ = d_q(λ)^2/[n]_q!$` Wedderburn weight (lines 335–340) | [y-lambda-closed-form-wenzl-bridge.md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md) + [wedderburn-weight-canonical.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) | `prop:y-lambda-closed-form-wenzl-bridge`, `prop:wedderburn-weight-canonical` | **STUB.** `wenzlSchurElement` and `wenzlNormalization` in [y-lambda-closed-form-wenzl-bridge.lean](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.lean) are placeholder definitions (`0 * (...)`); `y_lambda_closed_form_wenzl_bridge` discharges to `simp` on stubs (not a real proof). Definitional uniqueness layer is `rfl`-discharged; categorical uniqueness is conditional on the `MarkovTraceFamilyOneDim` class whose `unique : True` field is itself a placeholder. **Per `CLAUDE.md` notation register, `w_λ` in this file (lines 335–340) is the q-deformed Wedderburn weight — should be `$\tilde w_λ$` not bare `w_λ`** (see Plancherel boundary). Confusion is acknowledged in `hecke_3a_weights.wedderburn_weight` docstring (lines 146–162) but **not** here. |
| Wedderburn 3-block decomp `$H_3(q) = M_1 \oplus M_{n-1} \oplus M_1$` | [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md) + [three-parameters-wedderburn.md](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) | `thm:wedderburn-mass-formula`, `prop:three-parameters-wedderburn` | **PROVEN AT TOP LEVEL.** [wedderburn-mass-formula.lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean) `extremal_irreps_count` proves the 1-1-(n−1) extremal-irrep count by `rfl`. The actual Wedderburn-Artin theorem itself is STANDARD (Mathlib); the QOU-specific claim is just dimension counting. |
| Three-invariant mass formula `$M = Z m_p + N m_n + Z m_e + α(Φ_1 - 2[3]_q Φ_2 + H_A^2 Φ_3)$` (lines 1214–1265) | [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md) | `thm:wedderburn-mass-formula` | **STUB.** Lean `atomicMass` is just a Σ; no theorem connects it to `Φ_1, Φ_2, Φ_3` invariants of a transfer-matrix chain. The proof is a "sketch" in the `.md`. |
| LP-dual shadow price `$y_λ = w_λ/d_λ - 1/[k]_q!$` (lines 414–441) | [bw-coefficient-shadow-price](../../content/quantum-observable-universe/braids-and-knots/) (referenced via `prop:bw-coefficient-shadow-price`) | `prop:bw-coefficient-shadow-price` | **NEEDS CHECK.** Cited in `lp_shadow_price` docstring; primary citation is to that block (`.md` exists in repo). |
| q-Laplacian eigenvalue `$μ_λ = \sum_□ [c]_q[c+1]_q$` (lines 343–383) | Referenced as `prop:q-heat-kernel-peter-weyl` + `def:q-heat-equation` | `prop:q-heat-kernel-peter-weyl` | **NEEDS CHECK** (not in this audit's seven-file scope; cited block is outside braids-and-knots/ root). |
| Atomic NF construction (B₃ + quark + electron + inter-nucleon crossings, `build_atom_nf`) | [atomic-mass-gb-nf.md](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) + [nucleon-hecke-element.md](../../content/quantum-observable-universe/braids-and-knots/nucleon-hecke-element.md) | `prop:atomic-mass-gb-nf`, `def:nucleon-hecke-element` | **PROVEN (abstract structure).** [atomic-mass-gb-nf.lean](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.lean) defines `GBNFAlgebra` class with `markov_descends_through_NF` proved (no sorry); `atomicMassGBNF_descends` proved. **Concrete instance for `build_atom_nf` is NOT formalized** — Lean only states the abstract descent theorem. |
| Crossing eigenvalue rules (pp: σ, nn: σ⁻¹, pn: ½(σ+σ⁻¹)) | [hecke-mass-element.md](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.md) | `def:hecke-mass-element` | **PROVEN (abstract).** [hecke-mass-element.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-element.lean) has `mass_upper_bound`, `mass_exact` proved (no sorry). The specific pp/nn/pn crossing rule is not formalized as a theorem on `crossing_coeffs`. |
| Markov property `$tr_M(x σ_n) = z · tr_M(x)$` and product factorization | [hecke-markov-transition.md](../../content/quantum-observable-universe/braids-and-knots/hecke-markov-transition.md) | `prop:hecke-markov-transition` | **HAS_SORRY** at line 244 (`markov_chain_factorization_exists`), `Ref: [jones1987]` — STANDARD external (Jones 1987 Thm 5.1). Spectral-idempotent + probability sum=1 + Boltzmann ratio = q² are all PROVEN. |
| Hook-length formula `$d_λ = n!/\prod h_x$` | STANDARD | — | **STANDARD** (Frame–Robinson–Thrall 1954). Not paper-specific. |

### Summary for `hecke_core.py`

Most foundational compute primitives have backing prose blocks; the
Hoefsmit construction, Wedderburn 3-block decomposition, and the
GB-NF descent abstraction are formalized. **Three gaps**:

1. **Hecke quadratic relation has no `.lean`** for the algebra-level
   statement (only the 2×2 block algebraic identity).
2. **Wenzl-bridge `y_λ` closed form is a STUB** — the `wenzlSchurElement`
   is `0 * (...)`, so the main theorem trivially holds on the
   placeholder model. This is acknowledged in the file as a deliberate
   pre-Mathlib stub.
3. **No instance proves that `build_atom_nf(Z,N)` is the GB-NF** of the
   atomic braid in a concrete `GBNFAlgebra` instance — the abstract
   class is formalized, but the bridge to the Python NF is empirical.

---

## 2. `computations/hecke/hecke_characters.py`  (493 LOC)

Hoefsmit-matrix character engine with f64 + MPFR + symbolic-q hooks.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 52–64 | `partitions_of(n)` | partition enumeration (duplicate of core) |
| 67–73 | `young_diagram_cells(shape)` | (row, col) cells |
| 76–121 | `standard_young_tableaux(shape)` | SYT enumeration |
| 128–219 | `build_seminormal_matrices(shape, q)` | Build `$ρ_λ(σ_1), \ldots, ρ_λ(σ_{n-1})$`: axial dist `$ρ$`, diag `$a_ρ = h/(1-q^{-2ρ})$`, off-diag `$b² = a a' + 1$` |
| 280–387 | `chi_lambda_braid(shape, word, q, precision)` | `$χ_λ(β)$` = trace of product of matrices `$ρ_λ(σ_{i})$` or `$ρ_λ(σ_i)^{-1} = ρ_λ(σ_i) − h I$` |
| 390–397 | `crossing_coeffs(t_i, t_j)` | pp/nn/pn (c,d) coefficients |
| 400–449 | `nuclear_braid_character(Z,N,σ_λ,dim,n_gens)` | Atomic braid character `$χ_λ(β_{Z,N})$` |
| 456–474 | `qfac(n)`, `young_hooks(shape)`, `dim_q(shape)` | q-factorial, hooks, quantum dimension |

### (B)/(C) status

- **Hoefsmit construction** (lines 128–219): paper = [hoefsmit-seminormal-form.md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md), Lean = **partial PROVEN** (2×2 block identities only).
- **`χ_λ(β)` via matrix-product trace** (lines 280–387): paper = [q-hecke-seminormal-character-closure.md](../../content/quantum-observable-universe/braids-and-knots/q-hecke-seminormal-character-closure.md) (`prop:q-hecke-seminormal-character-closure`), Lean = **MISSING** (no `.lean` sibling).
- **Inverse via `σ⁻¹ = σ − h`** (lines 380–384): paper backing in [hecke-algebra-from-braiding.md](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md), Lean **MISSING**. This is a direct consequence of the Hecke quadratic relation; STANDARD modulo that.
- **`dim_q(λ)` via hook formula**: STANDARD (Frame-Robinson-Thrall q-deformation).

### Summary

Pure rep-theory engine. The Hoefsmit construction is partially Lean-backed
at the block level, but the full `ρ_λ` matrix-trace character is not
formalized. The character computation is the load-bearing primitive for
every downstream binding/mass result.

---

## 3. `computations/hecke/hecke_character_symbolic.py`  (453 LOC)

Symbolic-in-q character via `sympy.Matrix`. Marked DEPRECATION-CANDIDATE
but still imported.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 66–117 | `young_diagram_cells`, `standard_young_tableaux` | SYT enumeration (sympy-backed) |
| 120–194 | `_hoefsmit_cached`, `_hoefsmit_build`, `hoefsmit_matrices_symbolic` | Hoefsmit matrices with sympy.Symbol q |
| 202–231 | `_q_character_compute(shape, braid_crossings, q)` | Symbolic trace product `$\text{tr}(\prod (σ_g + d_g I))$` |
| 278–328 | `q_character_on_braid_word` | Cached wrapper with witness lookup |

### (B)/(C) status

Same backing block as #2 ([hoefsmit-seminormal-form.md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md), [q-hecke-seminormal-character-closure.md](../../content/quantum-observable-universe/braids-and-knots/q-hecke-seminormal-character-closure.md)). Lean status same as #2 — Hoefsmit blocks PROVEN, full character MISSING. This file is the sympy mirror of `hecke_characters.py`; the math claims duplicate.

The `__main__` block (lines 355–453) demonstrates the q-character distinguishes proton/neutron (`Q_cat = tr_M(n) − tr_M(p)`) — referenced from [hadron-exists.md](../../content/quantum-observable-universe/braids-and-knots/hadron-exists.md) and `prop:schur-weyl-mass-decomposition`. The numerical comparison is empirical (witness JSON), not a Lean theorem.

---

## 4. `computations/hecke/hecke_3a_weights.py`  (314 LOC)

Wedderburn weights at `$H_{3A}(q)$` (q-deformed Plancherel) — full enumeration over `$λ ⊢ 3A$`.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 46–60 | `partitions_of_n(n)` | partition enumeration |
| 63–85 | `partitions_bounded(n,max_part,max_length)` | Bounded enumeration (Vershik–Kerov limit shape) |
| 90–94 | `q_int(k)` | `$[k]_q = (q^k - q^{-k})/(q - q^{-1})$` (q-integer) |
| 100–105 | `q_fact(n)` | `$[n]_q!$` |
| 108–116 | `hook_lengths(shape)` | All `$h_λ(x) = \text{arm} + \text{leg} + 1$` |
| 119–129 | `classical_dim(shape)` | Hook-length formula `$d_λ = n!/\prod h_x$` |
| 132–142 | `q_dim(shape)` | Quantum dim `$d_q(λ) = [n]_q!/\prod[h_x]_q$` |
| 145–167 | `wedderburn_weight(shape)` | **`$\tilde w_λ = d_q^2/[n]_q!$`** (q-Plancherel) — explicitly NOT the Markov-trace `$y_λ$` per notation register |
| 170–176 | `_plancherel_bound(n)` | Vershik-Kerov shape cap `$2\lceil\sqrt n\rceil + 2$` |
| 179–218 | `plancherel_topn(n, top_n)` | Top-N partitions by `$\tilde w_λ$` |
| 221–248 | `wedderburn_weights_3a(A)`, `normalization_3a(A)`, `dominant_shape(n)` | `$H_{3A}$`-level enumeration |

### (B)/(C) status

| Compute claim | Paper block | Label | Lean |
|---|---|---|---|
| `$\tilde w_λ = d_q(λ)^2/[n]_q!$` Wedderburn weight (with warning that this is q-Plancherel, NOT `$y_λ$`) | [wedderburn-weight-canonical.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md) | `prop:wedderburn-weight-canonical` | **PROVEN (definitionally).** [wedderburn-weight-canonical.lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.lean) — definition exists. Sum boundedness in [plancherel-weight-boundedness.lean](../../content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.lean). |
| Markov-trace `$y_λ$` ≠ q-Plancherel `$\tilde w_λ$` warning (lines 146–162) | [y-lambda-closed-form-wenzl-bridge.md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md) | `prop:y-lambda-closed-form-wenzl-bridge` | **STUB** (see #1). The audit docstring in code at lines 154–162 references `docs/audits/2026-05-08-p3-h-3a-divergence.md` (a docs/audits/ artefact, not a content block). |
| Vershik-Kerov limit shape `$λ_1 ∼ 2√n$` bound | STANDARD (Vershik 1977, Logan-Shepp 1977) | — | **STANDARD.** |
| q-integer `$[k]_q$`, q-factorial, hook formula, q-dim | STANDARD | — | **STANDARD.** `quantumInt` is defined in [wedderburn-mass-formula.lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean) (line 68). |

### Summary

Clean separation: this file restricts itself to the q-Plancherel weight
`$\tilde w_λ$` and explicitly disclaims the Markov-trace `$y_λ$` use case.
That self-discipline matches the notation register requirement.
**No gaps specific to this file** beyond the Wenzl-bridge stub already
noted in #1.

---

## 5. `computations/hecke/hecke_wedderburn.py`  (258 LOC)

`δ_q` Wedderburn decomposition: per-irrep `$χ_λ$` for any braid word.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 75–92 | `chi_lambda(shape, word)` | `$χ_λ(σ_{w_1} σ_{w_2} \ldots)$` via cached YSN matrices |
| 95–128 | `delta_q(word, n)` | Map `$λ \mapsto χ_λ(\beta)$` for all `$λ ⊢ n$` |
| 131–152 | `wedderburn_decompose(word, n)` | Full per-`$λ$` data: `$χ_λ$`, `$d_q$`, `$f^λ$`, `$w_λ$`, contribution `$w_λ χ_λ / f^λ$` |
| 155–158 | `trM_via_wedderburn(word, n)` | **Markov trace `$tr_M = \sum_λ w_λ χ_λ / f^λ$`** |
| 165–173 | `force_carrier_channel(p, n)` | T_{p,*} → `$λ = (p, 1^{n-p})$` |
| 176–190 | `force_carrier_q_dim(p, k)` | `$δ_q(T_{p,k}) = q^k − q^{-k}$` |
| 197–207 | `alpha_em_from_delta_q()` | `$α_{EM} = h^2/(q · δ_q(T_{2,9}) · δ_q(T_{3,5}))$` |

### (B)/(C) status

| Compute claim | Paper block | Label | Lean |
|---|---|---|---|
| `$δ_q$` decoration (per-irrep character) | [delta-q-decoration.md](../../content/quantum-observable-universe/braids-and-knots/delta-q-decoration.md) | `def:delta-q-decoration` | **HAS_SORRY.** [delta-q-decoration.lean](../../content/quantum-observable-universe/braids-and-knots/delta-q-decoration.lean) line 32 — 1 sorry. (Could not inspect body in this audit; cited Ref TBD — flag.) |
| Markov trace via Wedderburn sum `$tr_M = \sum w_λ χ_λ / f^λ$` (line 158) | [wedderburn-trace-identity.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md) + [hecke-branching-trace-decomposition.md](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md) | `prop:wedderburn-trace-identity`, `prop:hecke-branching-trace-decomposition` | **HAS_SORRY** in [hecke-branching-trace-decomposition.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.lean) (3 sorries, line 155 with detailed comment classifying it as "typeclass bookkeeping gap, not a math gap"). [wedderburn-trace-identity.lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.lean) status not directly confirmed but listed alongside the trace blocks. |
| Force-carrier `$T_{p,q}$` intertwines via `$λ = (p, 1^{n-p})$` (lines 165–173) | [force-carrier-intertwining-correspondence.md](../../content/quantum-observable-universe/braids-and-knots/force-carrier-intertwining-correspondence.md) | `prop:force-carrier-intertwining-correspondence` | **HAS_SORRY** (1 sorry; cited Ref TBD). |
| `$α_{EM} = h^2/(q · δ_q(T_{2,9}) · δ_q(T_{3,5}))$` identity (lines 197–207) | [alpha-em-categorical-trace.md](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md) + [alpha-em-categorical-trace-ratio.md](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.md) | `prop:alpha-em-categorical-trace`, `prop:alpha-em-categorical-trace-ratio` | **LEAN** sibling [alpha-em-categorical-trace-ratio.lean](../../content/quantum-observable-universe/descartes-universe/alpha-em-categorical-trace-ratio.lean) exists; status not confirmed. |
| Torus-knot `$δ_q(T_{2,k}) = q^k − q^{-k}$` (Rosso–Jones placeholder; lines 176–190) | code self-flags as "placeholder — proper Rosso-Jones formula deferred" | — | **PAPER_MISSING for `T_{3,5}` arm of the alpha identity** — code uses `q^10 − q^{-10}` not the actual Rosso-Jones value. Code comment acknowledges this. Affects `alpha_em_from_delta_q()` correctness as a formal identity. |

### Summary

The `δ_q` Wedderburn decomposition has full paper backing and partial
Lean coverage. **Gap**: the `force_carrier_q_dim(3, 10) = q^10 − q^{-10}`
substitution for `$T_{3,5}$` is acknowledged as a placeholder in the
code itself — does NOT match the Rosso-Jones torus-knot formula. This
makes `alpha_em_from_delta_q()` an empirical identity, not a derivation.

---

## 6. `computations/hecke/hecke_division.py`  (951 LOC)

Instrumented Gröbner-Shirshov division algorithm in `$H_n(q)$`.
Marked DEPRECATION-CANDIDATE but still live.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 158–183 | `HeckeDivision.__init__` | Hecke quadratic `$σ² = (q − q^{-1})σ + 1$`; inverse `$σ^{-1} = σ − h$` |
| 418–432 | `crossing_positive`, `crossing_negative`, `crossing_mixed` | pp = σ, nn = σ⁻¹ = σ − h, pn = ½(σ + σ⁻¹) = σ − h/2 |
| 486–510 | `borromean_B3()` | `$B_3 = (σ_0 σ_1^{-1})^3$` (Borromean confinement braid) |
| 514–559 | `nuclear_braid(p, n)` | B₃ + pairwise crossings, reducing after each step |
| 563–721 | `reduce(elem)` | GS division: **Hecke `$σ_i² → h·σ_i + 1$`**, **far-comm `$σ_iσ_j → σ_jσ_i$`** (|i−j|≥2), **Yang–Baxter `$σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}$`** |
| 725–751 | `markov_trace(elem, n_strands)` | Recursive Markov trace via `$z_{Markov} = 1/(q^{1/2} + q^{-1/2})$` |

### (B)/(C) status

| Compute claim | Paper block | Label | Lean |
|---|---|---|---|
| Hecke quadratic relation `$σ² = (q − q^{-1})σ + 1$` | [hecke-algebra-from-braiding.md](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md) (see also [y-lambda-closed-form-wenzl-bridge.md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md) line 3 and [atom-knot-mass-derivation.md](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)) | `rem:hecke-algebra-from-braiding`, `def:hecke-normal-form` | **LEAN_MISSING.** [hecke-normal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.lean) lists `RewriteRule.hecke` constructor but does NOT prove the quadratic equation on any concrete algebra. The relation is a *definitional axiom* of the Iwahori-Hecke algebra (presentation) and STANDARD in the literature; the **content gap is the absence of a Lean Hecke-algebra type with the quadratic relation as a structure field** (cf. `BraidGroupData.braid_relation` which DOES this for braids). |
| Braid relation (Yang-Baxter) `$σ_iσ_{i+1}σ_i = σ_{i+1}σ_iσ_{i+1}$` | [braid-group.md](../../content/quantum-observable-universe/braids-and-knots/braid-group.md) | `def:braid-group` | **PROVEN as structure field** (see #1). STANDARD. |
| Far commutativity `$σ_iσ_j = σ_jσ_i$` for `|i−j|≥2` | STANDARD (Artin braid relations) | — | **LEAN_MISSING** as an explicit theorem. `BraidGroupData` only encodes the adjacent braid relation; far-commutativity should follow but is not in the Lean structure. STANDARD math. |
| GS basis `{σ_i² − h σ_i − 1, σ_iσ_{i+1}σ_i − σ_{i+1}σ_iσ_{i+1}, σ_iσ_j − σ_jσ_i}` is confluent → unique NF | [hecke-normal-form.md](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md) + [atomic-mass-gb-nf.md](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) | `def:hecke-normal-form`, `prop:atomic-mass-gb-nf` | **PROVEN at the abstract level.** `nf_basis3_card : 6 = 3!` in [hecke-normal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.lean) — STANDARD count. **The Diamond/Bergman confluence proof is referenced but not formalized.** [atomic-mass-gb-nf.lean](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.lean) abstracts the GB-NF as a class with `NF_GS_idem` + `tr_M_factors_through_NF` fields; no `sorry`, but the concrete Iwahori-Hecke instance is not provided. |
| Borromean `$B_3 = (σ_0 σ_1^{-1})^3$` confinement braid | [hadron-exists.md](../../content/quantum-observable-universe/braids-and-knots/hadron-exists.md) + [confined-particle.md](../../content/quantum-observable-universe/braids-and-knots/confined-particle.md) | `prop:hadron-exists`, `def:confined-particle` | **CHECK** — backing exists in paper. Lean status not directly inspected. |
| Markov trace recursion `$tr_M(x σ_n) = z · tr_M(x)$` (with `$z = 1/(q^{1/2} + q^{-1/2})$`) | [hecke-markov-transition.md](../../content/quantum-observable-universe/braids-and-knots/hecke-markov-transition.md) + [jones-markov-trace.md](../../content/quantum-observable-universe/braids-and-knots/jones-markov-trace.md) | `prop:hecke-markov-transition`, `thm:jones-markov-trace` | **HAS_SORRY** in [hecke-markov-transition.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-markov-transition.lean) line 244 (`Ref: [jones1987]` — STANDARD external). Spectral idempotent piece proven. |

### Summary

The GS algorithm is **mostly empirical**: the Diamond Lemma confluence
of `{Hecke, YB, far-comm}` is asserted in `.md` and the algorithm
encoded in Python, but **the Lean Hecke-algebra carrier with the
quadratic relation does not exist** as a concrete instance. The
abstract `GBNFAlgebra` class formalizes the descent property
correctly but doesn't construct the algebra.

---

## 7. `computations/hecke/hecke_engine.py`  (358 LOC)

Hecke trace engine: factored Markov trace + e(I)/e(R) at converting generator, exact rational arithmetic with `q = 111/100`.

### (A) Math claims inventory

| Line(s) | Function | Claim |
|---|---|---|
| 44–62 | `HeckeRational.__init__`, `crossing(ti, tj)` | pp/nn/pn (c,d) crossing coefficients |
| 64–81 | `traced_volume(gen_idx, ordering)` | `$\hat V_i = z M_{10} + M_{11}$` via 2×2 transfer matrix product over `$j > i$` |
| 83–90 | `markov_trace(ordering)` | `$\prod_i \hat V_i$` (factored over generators) |
| 92–99 | `eIeR(par, dau, conv)` | `$e(I)/e(R) = |V_{par} − V_{dau}|/|V_{par}|$` at converting generator |
| 108–116 | `_channel_weights()` | `$w_{sym}, w_{std}, w_{alt}$` summing to 1 |
| 118–134 | `lambda_sym`, `lambda_alt` | `$λ^{sym} = \prod(cq + d)$`, `$λ^{alt} = \prod(-c/q + d)$` |
| 136–149 | `V_full(gen_idx, ordering)` | **Wedderburn-weighted volume `$V^{full}_i = w_{sym} λ^{sym} + w_{std} V^{std} + w_{alt} λ^{alt}$`** |
| 183–214 | `ground_state_ordering(p,n)` | Exact min-energy ordering (≤14) or alternating heuristic |
| 223–289 | `compute(p, n)` | Full nucleus result: trace, e(I)/e(R), generator volumes |

### (B)/(C) status

| Compute claim | Paper block | Label | Lean |
|---|---|---|---|
| Factored Markov trace `$tr_M = \prod \hat V_i$` (the 2×2 transfer matrix in the standard rep) | [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md) §proof sketch + [hecke-markov-transition.md](../../content/quantum-observable-universe/braids-and-knots/hecke-markov-transition.md) (`MarkovChainFactorization`) | `thm:wedderburn-mass-formula`, `prop:hecke-markov-transition` | **HAS_SORRY** — see #1, #6. Factorization is formalized abstractly in `MarkovChainFactorization.factorization` (proof field), but no theorem proves it from the Hecke axioms. |
| `$V_i^{full} = w_{sym} λ^{sym} + w_{std} V^{std} + w_{alt} λ^{alt}$` (3-channel Wedderburn vol) | [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md) | `thm:wedderburn-mass-formula` | **STUB** at top-level (see #1). The `extremal_irreps_count` only proves the dimension counts (1, n−1, 1); the volume sum formula is not a Lean theorem. |
| `$w_{sym} = w_{alt} = 1/([2]_q^2 + 2)$`, `$w_{std} = [2]_q^2/([2]_q^2 + 2)$` (sum to 1) | [three-parameters-wedderburn.md](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) | `prop:three-parameters-wedderburn` | **CHECK** — paper backing exists; Lean status for an explicit weight-sum theorem not confirmed in this audit. STANDARD identity (`$1^2 + (n-1)^2 + 1^2$` over `$n!$` for `$S_3$`-irrep dim². For the q-deformation it follows from `$\sum_λ d_q(λ)^2 = [n]_q!$` on $H_3$). |
| 1-dim irrep characters (`$χ^{sym}$` evaluates `$σ → q$`, `$χ^{alt}$` evaluates `$σ → -q^{-1}$`) | [hecke-1d-irrep-closed-form-character.md](../../content/quantum-observable-universe/braids-and-knots/) (`prop:hecke-1d-irrep-closed-form-character`) | `prop:hecke-1d-irrep-closed-form-character` | **CHECK** — block exists by label; Lean status not directly inspected in audit scope. |
| Ground-state ordering as `arg min` energy over `$\binom{A}{p}$` configurations | Heuristic — no specific paper theorem; defaults to interleaved | — | **STANDARD** combinatorial optimization. No paper-level claim. |
| `$e(I)/e(R) = (V_{par} − V_{dau})/V_{par}$` at converting generator (β-decay) | Connects to [hecke-mass-trace.md](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.md) and the β-decay Q-value identity in `hecke_core.q_value_beta` | `prop:hecke-mass-trace` | **CHECK** — block exists. |

### Summary

`hecke_engine.py` is the rational-arithmetic counterpart of `hecke_core`'s
3-channel Wedderburn decomposition. **Same gaps as #1**: the 3-channel
mass formula is paper-asserted but Lean-stubbed; the factorization
of `tr_M` over generators relies on the unproved `markov_chain_factorization_exists`
(`HAS_SORRY` in `hecke-markov-transition.lean`).

---

## (D) Summary table

| File | Major claims | Paper backing | Lean status | Gaps |
|---|---|---|---|---|
| `hecke_core.py` | ~40 functions, Hoefsmit YSN + GS-NF + Wedderburn 3-channel + atom-NF + LP-dual + mass formula | Comprehensive (10+ blocks) | Mostly partial; abstracts proved, concrete instances missing | Hecke quadratic has no algebra-level Lean type; Wenzl `y_λ` is STUB; full mass formula `Φ_1,Φ_2,Φ_3` not connected to invariants in Lean |
| `hecke_characters.py` | Hoefsmit construction + braid character `χ_λ(β)` | [hoefsmit-seminormal-form.md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md), [q-hecke-seminormal-character-closure.md](../../content/quantum-observable-universe/braids-and-knots/q-hecke-seminormal-character-closure.md) | Block-level Lean proofs; full character trace MISSING | Inverse `σ⁻¹ = σ − h` not in Lean directly |
| `hecke_character_symbolic.py` | Sympy mirror of #2 | Same as #2 | Same as #2 | Same as #2 (file marked DEPRECATION-CANDIDATE) |
| `hecke_3a_weights.py` | q-Plancherel `$\tilde w_λ$` enumeration; explicit non-Markov disclaimer | [wedderburn-weight-canonical.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md), [plancherel-weight-boundedness.md](../../content/quantum-observable-universe/braids-and-knots/plancherel-weight-boundedness.md) | PROVEN (definitions + boundedness) | None specific |
| `hecke_wedderburn.py` | δ_q decoration; `$tr_M = Σ w_λ χ_λ/f^λ$`; force-carrier; `α_EM` identity | [delta-q-decoration.md](../../content/quantum-observable-universe/braids-and-knots/delta-q-decoration.md), [wedderburn-trace-identity.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md), [force-carrier-intertwining-correspondence.md](../../content/quantum-observable-universe/braids-and-knots/force-carrier-intertwining-correspondence.md), [alpha-em-categorical-trace.md](../../content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md) | HAS_SORRY in delta-q (1), force-carrier (1), branching (3) | `force_carrier_q_dim(3, 10)` is admitted Rosso-Jones placeholder; affects `α_EM` derivation |
| `hecke_division.py` | GS division on H_n(q): Hecke + YB + far-comm rewrite rules; Markov trace | [hecke-normal-form.md](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md), [atomic-mass-gb-nf.md](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md), [hecke-algebra-from-braiding.md](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md) | Abstract GBNFAlgebra class PROVEN (no sorry); concrete H_n(q) instance MISSING; Hecke quadratic STILL NOT in Lean as a type-level identity | File is DEPRECATION-CANDIDATE but live; Diamond/Bergman confluence not formalized |
| `hecke_engine.py` | Rational-arithmetic 3-channel `$V^{full}_i$`; factored Markov trace | [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md), [three-parameters-wedderburn.md](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md), [hecke-mass-trace.md](../../content/quantum-observable-universe/braids-and-knots/hecke-mass-trace.md) | STUB at top level (same as `hecke_core`'s `V_full`) | Same as #1: Φ-invariant connection unproven |

---

## Focus questions

### Hecke quadratic relation `$T_i^2 = (q − q^{-1})T_i + 1$`

- **Paper**: stated in [hecke-algebra-from-braiding.md](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md) as `$(T - q)(T + q^{-1}) = 0$` (eigenvalue form). Restated in [y-lambda-closed-form-wenzl-bridge.md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md) line 3.
- **Lean**: **NOT type-level.** [hecke-normal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hecke-normal-form.lean) lists `RewriteRule.hecke` as a constructor (rewrite rule index) but does NOT prove the equation on any algebra. The Hoefsmit 2×2 block identity (which encodes the relation at the matrix level) IS proved in [hoefsmit-seminormal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.lean) (`hoefsmit_block_det`). 
- **STANDARD math** — definitional in the literature (Bourbaki, Kassel, Humphreys).

### Braid relations

- **Paper**: [braid-group.md](../../content/quantum-observable-universe/braids-and-knots/braid-group.md) (B₃ adjacent relation). Far commutativity is implicit.
- **Lean**: [braid-group.lean](../../content/quantum-observable-universe/braids-and-knots/braid-group.lean) — `BraidGroupData.braid_relation` PROVEN as structure field. Far commutativity NOT in the Lean structure (would need additional structure field).

### Hoefsmit seminormal matrix construction

- **Paper**: [hoefsmit-seminormal-form.md](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md) (`prop:hoefsmit-seminormal-form`). Full statement including Hecke + braid relations + R-matrix identification.
- **Lean**: [hoefsmit-seminormal-form.lean](../../content/quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.lean) — partial PROVEN. The four core lemmas (`hoefsmit_block_det`, `hoefsmit_block_trace`, `hoefsmit_product_rho2`, `figure_eight_hoefsmit_trace`) are closed without sorry. **Missing**: the actual representation property `ρ_λ : H_n(q) → M_{d_λ}` — i.e. that the full matrix construction satisfies the Hecke + braid relations as a homomorphism.

### Wenzl Markov weights `$y_λ = \dim_q(λ)^2 / [n]_q!$`

- **Paper**: [y-lambda-closed-form-wenzl-bridge.md](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md). The relation `$y_λ ≠ \tilde w_λ$` at `q ≠ 1` is explicitly noted. The closed form via Schur principal specialization is given.
- **Lean**: [y-lambda-closed-form-wenzl-bridge.lean](../../content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.lean) — **STUB**. `wenzlSchurElement := 0 * (...)`. The main theorem trivially holds on the placeholder model. Uniqueness is `rfl` at the definitional layer, conditional at the categorical layer (`MarkovTraceFamilyOneDim.unique : True`). Empirical numerical agreement is recorded as `True := trivial`.

### Wedderburn decomposition + 1-dim irrep characters

- **Paper**: [wedderburn-mass-formula.md](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.md), [three-parameters-wedderburn.md](../../content/quantum-observable-universe/braids-and-knots/three-parameters-wedderburn.md) for H₃(q) = M_1 ⊕ M_2 ⊕ M_1. [hecke-1d-irrep-closed-form-character.md](../../content/quantum-observable-universe/braids-and-knots/) for `χ^sym, χ^alt`.
- **Lean**: [wedderburn-mass-formula.lean](../../content/quantum-observable-universe/braids-and-knots/wedderburn-mass-formula.lean) proves dimensions count (1, n−1, 1). The Wedderburn-Artin theorem itself is STANDARD (Mathlib). The 1-dim character formulas `$χ^{sym}(σ) = q$`, `$χ^{alt}(σ) = -q^{-1}$` are eigenvalues of the Hecke generator, which falls out of the Hecke quadratic — but with no algebra-level Lean type for `H_n(q)`, the characters themselves are not Lean-defined.

---

## Honest gap summary

The Hecke compute infrastructure is **rich** and **paper-anchored**:
every major claim in these seven files has a corresponding content
block. Lean coverage is **uneven**:

1. **Foundational algebra (Hecke quadratic + braid + far-comm) has no concrete Lean type.** Braid generators are structure fields in `BraidGroupData`; Hecke generators are not. The closest is `RewriteRule.hecke` (an index, not a relation).
2. **Hoefsmit construction is partial-PROVEN at the block level** — the 2×2 algebraic identities are closed, but the full `ρ_λ` homomorphism property is not.
3. **The Wenzl-bridge `y_λ` closed form is a STUB.** `wenzlSchurElement = 0 * (...)`. Empirical agreement to 10⁻¹⁶ across 270 partitions is recorded only as `True := trivial`. Conditional-on-class machinery is honored per `CLAUDE.md §3b-cond`.
4. **The three-invariant mass formula** `$Φ_1, Φ_2, Φ_3$` is paper-asserted with a sketch proof; the Lean only formalizes the dimension count of the three extremal irreps.
5. **The GS division algorithm in `hecke_division.py` has no concrete H_n(q) carrier.** `GBNFAlgebra` is an abstract class with `tr_M_factors_through_NF` as a field; no instance constructs the actual algebra and verifies the rewriting rules are confluent (Diamond Lemma).
6. **`force_carrier_q_dim(3, 10)` is a self-acknowledged placeholder** for the Rosso–Jones `$T_{3,5}$` torus-knot formula. This affects `alpha_em_from_delta_q()` correctness.

Everything else (q-integers, q-factorial, hook formula, classical
partition combinatorics, Plancherel limit shape, etc.) is **STANDARD**
math and has no QOU-specific theorem to prove — it's properly cited
to the literature where used.

**Net assessment.** The compute layer is ahead of the Lean layer by
roughly one structural step: the abstract classes (`GBNFAlgebra`,
`MarkovTraceFamilyOneDim`, `BraidGroupData`) are formalized; the
concrete Iwahori-Hecke algebra instance that ties everything together
is not. Closing this gap would require a Lean `HeckeAlgebra n q`
type with the quadratic + braid + far-comm relations as structure
fields, plus an instance proving it satisfies `GBNFAlgebra` and
hosts the Hoefsmit reps.
