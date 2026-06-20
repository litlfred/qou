# Compute / Paper / Lean Audit — Atom Braid + Mass Endomorphism Tower

**Date:** 2026-05-17
**Scope:** Ten computation scripts in
[`computations/`](../../computations/)
that carry the f64 reference for the proton–electron mass ratio
(`mass_endomorphism.py`), the canonical 3A-strand atomic braid +
H_{3A} Wedderburn-character per-generator volume
(`mass_at_3A_proper.py`), and the supporting partition / probe /
jet-tower diagnostics. The audit walks each math-bearing function,
identifies the backing content block(s) and Lean declaration(s),
and flags the f64 / MPFR / `\Phi_q` / `\mathrm{Li}_2^q` distinctions
that drive open issues at the atomic-braid scale.

## 1. `mass_endomorphism.py` — f64 reference; m_p/m_e ≈ 1870

**Math claims walked.**

- `qint`, `qfact`, `qdim` (lines 46–66): symmetric q-integer
  `[k]_q = (q^k − q^{−k})/(q − q^{−1})`, q-factorial, and q-deformed
  Frame–Robinson–Thrall hook-length quantum dimension. Standard
  paper conventions; no novel mathematical content here.
- `Phi_q(z_val, max_k=2000)` (line 80): the non-perturbative quantum
  dilogarithm `Φ_q(z) = ∏_{k≥1}(1 − q^{−k}z)^{−1}` in the **Faddeev**
  (asymmetric q-integer) convention.
- `additive_wedderburn_volumes` (line 98): per-generator
  `V̂_full = w_sym·χ_sym + w_std·V_std + w_alt·χ_alt` via the standard
  transfer-matrix recurrence on H_3(q).
- `mass_from_tower` (line 114): the headline formula
  `𝔪 = |Π V̂_i| + Σ Φ_q(|V̂_i|) + Σ_{i<j} z²·Φ_q(|V̂_i V̂_j|)`,
  with **all pairs** (adjacent + non-adjacent) weighted by z².
- `tr_M_atomic_at_q0(Z, N)` (line 199): canonical atomic Jones–Markov
  trace via recursive-ascent (#508), delegating to
  `markov_peel.tr_M_atomic`. Returns f64 from sympy-30dps evaluation.
- `__main__`: prints electron/proton/neutron decomposition, then
  iterates the recursive-ascent trace over six light atoms
  (p, n, D, T, ³He, ⁴He).

**Paper backing.**

- Primary block:
  [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md).
  The boxed proposition (post-2026-05-03 revision) **now uses
  `−Li_2^q(−|V̂_i|)` (symmetric q-dilogarithm)**, not the Faddeev
  Φ_q this script computes. The script's docstring and `mass_from_tower`
  cross-term over **all pairs** matches the recent expansion of the
  proposition to the full quadratic channel (`prop:markov-pair-z2`
  derivation: adjacent pairs reduce via Hecke + one peel,
  non-adjacent via far-commutativity + two peels — same z² weight).
- Secondary block:
  [`thm:knot-mass-formula-unified`](../../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md).
  The boxed theorem also writes `Li_2^q(−|·|)` since 2026-05-03; the
  brane-tower-evaluation note explicitly flags that the literal
  Φ_q form (i.e. this script) is "Markov-invariance-broken at q_0"
  and produces the −737 MeV mirror-nucleus pathology.

**Lean status.**

[`mass-endomorphism-tower.lean`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean)
has a two-tier `Pre`/`Arch` split. `QOU.MassEndomorphism.Arch.mass`
mirrors the **older** Φ_q + adjacent-pairs form (lines 100–108),
not the new `Li_2^q` + all-pairs form in the .md. The headline
theorem `proton_electron_ratio` is **conditional on a
`MassEvaluation q` class** (axiomatized numerical input) — a
canonical example of AGENTS.md §3b-cond. No `sorry`; the class
instance is the only unproved input. The Lean and the .md
**diverge** on (a) which q-dilogarithm and (b) adjacent-only vs
all-pairs — a documented drift that the script's f64 form
contradicts in two places.

**Summary.** Script is the f64 reference for the Φ_q tower (1.8%
proton–electron ratio at q_0). It implements the *literal*
proposition statement as it stood pre-2026-05-03 (Faddeev Φ_q,
all-pairs z²). The paper has since refactored to symmetric
`Li_2^q` per the Briggs–Klein integration witness; the .py / .lean
have not yet been migrated. Cross-term z² weight is now correctly
applied to every pair `(i, j)` with `i < j` — adjacent-only was
empirically refuted by `adjacent-vs-full-probe.witness.json`.

## 2. `mass_at_3A_proper.py` — canonical 3A-strand atom braid + per-generator V̂

**Math claims walked.**

- `jones_wenzl_weight(shape, q, z)` (line 75): Ocneanu/Jones–Wenzl
  weight `ω_λ(q,z) = z^{n−1}·∏_x (1 − z·q^{2c(x)})/(1 − q^{2h(x)})`,
  with content `c(x)=j−i` and hook `h(x)`. The accompanying comment
  notes Σ ω_λ = 1 — the canonical Plancherel-normalised Jones–Wenzl
  formula (Jones 1985 Thm 5.1; Wenzl 1988).
- `normalized_plancherel_weights_3A(A)`: `ω_λ = w_λ^Planch / Σ w_μ`,
  re-normalises `dim_q²/[n]_q!` to sum to 1. The comment is candid
  that this is an empirical regulariser to keep V̂_i in the physical
  range [−1, 1] near q_0 (so Φ_q does not pole); it is **not** the
  canonical Markov-trace parameter z.
- `atom_braid_word_3A(Z, N, m_pp, m_pn, m_nn, include_inter)` (line 230):
  **canonical 3A-strand atomic braid word generation**. For each
  nucleon k in ordering `['p']*Z + ['n']*N`:
  - intra-g0 pass: `_PROTON_G0` or `_NEUTRON_G0` (from `hecke_core`)
    applied at generator `3k`.
  - intra-g1 pass: `_PROTON_G1` / `_NEUTRON_G1` applied at `3k+1`.
  - inter-nucleon pass (if `include_inter=True` and `k < A−1`): one
    of `(1.0, 0.0)` (pp), `(1.0, −h)` (nn), `(1.0, −h/2)` (pn)
    at generator `3k+2`, repeated `m_pp/m_nn/m_pn` times.

  This is the operator-valued σ_3 interface convention: the braid
  is `β_Z · I_{n,n+1} · β_N` for a Z-then-N ordering, where the
  inter-nucleon generator at position `3k+2` mediates between the
  k-th nucleon (occupying strands 3k..3k+2) and the (k+1)-th
  (occupying 3k+3..3k+5). This is **not** a disjoint tensor
  product; the inter-nucleon σ_{3k+2} crossing is a true H_{3A}
  generator, identical to what
  `hecke_core.atom_per_generator_volumes` (lines 3029–3079) uses.

- `chi_lambda_of_word(sigmas, dim, word, n_gens_required)` (line 271):
  character `χ_λ(W) = tr(Π_k (c_k·σ_{g_k}^λ + d_k·I))` in the λ-irrep
  via build_seminormal_matrices (or its sparse variant). Idiomatic
  Hoefsmit evaluation.
- `markov_trace_3A` (line 304): Σ_λ (d_q²/[3A]_q!)·χ_λ(W)/d_λ —
  the **Plancherel-weighted** sum. The docstring is explicit that
  this is **NOT** the canonical Jones–Markov trace at q ≠ 1; it is
  marked `[DEPRECATED]` and points to `markov_trace_canonical`
  for the axiomatically-correct path.
- `per_generator_V_hat_3A(Z, N, …, weight_scheme="normalized_plancherel")`
  (line 363): for each i ∈ {0,…,3A−2}, the chain at i is
  `W_i = Π_k (c_k·σ_i + d_k·𝟏)`, and
  `V̂_i = Σ_{λ⊢3A} w_λ·χ_λ(W_i)/d_λ`. This is the **H_{3A}**
  Wedderburn-weighted analogue of `hecke_core.atom_per_generator_volumes`'s
  per-generator V̂ (which weights via H_3 only).
- `phi_q_safe(z_val, cap_frac=0.98)` and `log_phi_q` (lines 460, 487):
  saturation-clipped Φ_q to keep the divergence at |z| → q tractable
  numerically. Acknowledged regularisation — same symptom as the
  "V_full saturation near q₀" note in HANDOVER-STATUS.
- `mass_from_tower_safe(vols, cap_frac, cross_mode)` (line 509):
  mirror of `mass_endomorphism.mass_from_tower` with three `cross_mode`
  options — `"adjacent"`, `"full"`, `"full_z2pow"`. The default
  `cross_mode="full"` in `binding_3A_tower` matches the corrected
  z² convention.
- `binding_3A_tower` (line 559): the **full-tower** binding
  `B = E_0·(𝔪_free − 𝔪_atom)` with per-generator V̂_i from the
  H_{3A} character sum. E_0 = 0.78233341 MeV (β-decay Q), no Catalan
  prefactor. **This is the MPFR-port target for the present PR.**
- `binding_3A` (line 614): legacy single-brane Markov-trace binding,
  marked `[DEPRECATED — Plancherel-weighted]`.

**Paper backing.**

- The atom-braid word generator `atom_braid_word_3A` is the
  canonical computational object cited by
  [`prop:confined-knot-binding`](../../content/quantum-observable-universe/braids-and-knots/confined-knot-binding.md):
  *"β = T_w = atom_braid_word_3A(Z, N)"*. The .md's three-channel
  Wedderburn decomposition matches the script's character-sum form
  (paper uses H_3 per generator; script extends to H_{3A}).
- The per-generator V̂_i computed via `per_generator_V_hat_3A` is
  the H_{3A}-graded refinement of
  [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)'s
  `\hat V_i^{\mathrm{full}}`, anchored on `prop:atomic-braid-mass`
  (the three-invariant mass formula).
- The β-decay E_0 = 0.78233341 MeV calibration is
  `prop:categorical-mass-markov` (single fibre-functor scalar).

**Lean status.**

No direct Lean file for `atom_braid_word_3A` or
`per_generator_V_hat_3A`. The atomic braid is implicitly the
`T_w` in `categorical-mass-markov.lean`'s `MarkovAlgebra` typeclass
(line 47 onward): trace, J^1 ideal, descent property. The Lean
side **does not yet expose the per-generator chain**; it treats
T_w as an opaque element of an abstract `MarkovAlgebra`. There is
therefore no Lean cross-check that the script's `atom_braid_word_3A`
chain matches the paper's `T_w` GS normal form — that match is
verified only at the witness layer (`atomic-tr-m-mpfr-50dps.witness.json`
agrees with the recursive-ascent trace to ~1e-15).

**Summary.** This script is the workhorse: it generates the
canonical 3A-strand atom-braid word per nucleon ordering, runs
the H_{3A} character sum for both single-brane Markov trace and
the full Φ_q tower, and emits both Markov and tower binding paths
for D / T / ³He / ⁴He / ⁶Li (limited by `max_A` since p(3A) grows
fast). The `weight_scheme="normalized_plancherel"` is candidly an
empirical regulariser, **not** the canonical Jones–Markov weight
— `prop:categorical-mass-markov` plus the `MassEvaluation` class
upstream are the formally-correct path. The MPFR-50dps port
should preserve this convention split (keep an `ocneanu_weights_3A`
audit path; default to `normalized_plancherel`).

## 3. `mass_formula_6term.py` — f64 6-term reference

**Math claims walked.**

The integrated 6-term mass formula per `thm:knot-mass-formula-unified`:
1. **Term 1** — `term_1_descended(Z, N, include_inter)`: |tr_M(T_w)|
   via numerical Hoefsmit at H_{3A}, delegating to
   `light_isotope_sweep.tr_M_at_q0`.
2. **Term 2+3** — `term_23_brane_tower(Z, N, include_inter)`:
   Σ_i Φ_q(|V̂_i|) + z²·Σ_{i<j} Φ_q(|V̂_i V̂_j|), via
   `hecke_core.atom_per_generator_volumes`. Returns a `status` field
   (`ok`/`near-pole`/`divergent`) when `max |V̂_i|` ≥ 0.95 / ≥ 1.05.
3. **Term 4** — `term_4_frobenius(A)`: m_e · Σ_{λ⊢3A} 1/dim_q(λ),
   the canonical per-3A algebraic form per
   `thm:frobenius-codim-universal` (loaded from
   `probe-term4-conventions.witness.json`). Also returns the
   per-vortex (1·m_e·(2 + 1/[2]_q)) and per-A (A·that) heuristics
   for back-comparison.
4. **Term 5** — `term_5_chirality_bw(Z, N, knot_type)`: paper's
   Bethe–Weizsäcker with knot-type chirality factor (chiral+,
   amphichiral, borromean, none), via `bw_chirality_isotopes`.
5. **Term 6** — declared absent / open in the docstring.

**Paper backing.**

- Primary:
  [`thm:knot-mass-formula-unified`](../../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md).
  The boxed formula matches Term 1 + (T2+T3) + Term 4; the
  brane-tower-evaluation note in the .md (added 2026-05-03) is
  what flags this script's tower form as Markov-invariance-broken
  at q_0 and predicts the −737 MeV mirror-nucleus pathology that
  `brane_tower_isospin_diagnosis.py` then documents in full.
- The `.ts` for the unified theorem points at
  [`mass_formula_6term_mpfr_50dps.py`](../../computations/mass_formula_6term_mpfr_50dps.py)
  as the *current* canonical computation, demoting this file
  to a reference / fallback. (Witness:
  `mass-formula-6term-mpfr-50dps.witness.json`.)

**Lean status.**

[`knot-mass-formula-unified.lean`](../../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.lean)
axiomatises a `UnifiedKnotMass` class with fields for each piece
(`descended`, `tower`, `frobenius_correction`) and the unifying
identity. Concrete-model components (`descendedMarkov`, `braneTower`)
return zero — the Lean does not yet evaluate them. The S3 axioms
at n ∈ {2,3,4,5} are discharged (`rfl` theorems via partial
`def` with `match n`); n ≥ 6 is a `frobeniusCoCasimirTraceFallback`
opaque. So the **Frobenius piece is Lean-closed at small n; the
descended and tower pieces are stubs**.

**Summary.** This script is the f64 anchor of the full 6-term
sum and the cleanest implementation of the per-3A canonical Term 4
(distinct from the per-vortex / per-A heuristics that other scripts
still use). The MPFR-50dps companion is now the canonical witness
for `thm:knot-mass-formula-unified`. Term 6 ("jet-level prefix
corrections") is OPEN; the .md is explicit that the boxed Kashaev
specialisation produces hundreds-of-MeV isospin pathologies at q_0
and a derivation-level fix is needed (paths 1, 2, 3 in the .md).

## 4. `atom_mass_additive_baseline.py`

**Math claims walked.**

- Atomic mass `M_atom ≈ Z·M_p + N·M_n + Z·M_e − E_binding(A,Z)`
  with `M_p`, `M_n`, `M_e` from CODATA 2022. Computes the
  Δ_binding residual against AME2020 for 10 light isotopes.
- Asserts the structural identity `constituent_mass(1,0) = M_p + M_e`
  to 1e-12 tolerance (a bit-stability check on IEEE 754 arithmetic).
- Reports `max Δ_binding` and average binding per nucleon.

**Paper backing.**

- Auxiliary; supports
  [`rem:frobenius-packing-density`](../../content/quantum-observable-universe/particle-interactions/frobenius-packing-density.md)
  as the additive-form binding-energy column that the QOU
  `ρ_F · V_hyp` law is expected to reproduce.

**Lean status.** N/A — phenomenology / experimental constants
reconciliation; no formalisation target.

**Summary.** This script is the correct additive baseline that
the multiplicative `atom_mass_derived.py` is **not**. AME2020
hydrogen matches to <100 ppb (publication-rounding-limited at 3 dp);
A ≥ 4 residual averages 7.224 MeV/A, within 4% of empirical SEMF.
The witness is `audit_only` (not a 1 ppb gate).

## 5. `atom_mass_derived.py`

**Math claims walked.**

The script builds B_3-confined nucleons from typed crossings,
multiplies them via `hecke_mul`, reduces to Gröbner–Shirshov
normal form (Hecke + Yang–Baxter + far-commutativity), and
derives atomic mass as `M = tr_M(atom NF) × E_0` where
`E_0 = M_p / tr_M(proton)`.

The header carries a prominent **STRUCTURAL BUG — DO NOT TRUST OUTPUT**
banner: composing nucleon Markov traces *multiplicatively* does
not represent atomic mass. The right LP-dual / shadow-price
structural object lives in `prop:operator-selection-lp`; the right
experimental comparison is the *additive* sum in
`atom_mass_additive_baseline.py` (item 4 above).

The proton/neutron primitives (`PROTON_NF`, `NEUTRON_NF`,
`PROTON_TR`, `NEUTRON_TR`) are correct and still used by downstream
scripts (`cross-check-trM-1ppb`, `atomic_braid_mass_table`).

**Paper backing.**

[`rem:atom-mass-full-hecke`](../../content/quantum-observable-universe/observations/atom-mass-full-hecke.md)
is the closest content block — three-channel decomposition of H_3(q)
with exact rationals at q = 111/100, Skein binding Lagrangian for
Z = 1..10. The Wedderburn-weighting machinery matches this script's
`PROTON_NF`/`NEUTRON_NF` reduction, but the .md's binding column
uses the **additive** Skein-Lagrangian path, *not* multiplicative
`tr_atom × E_0`.

**Lean status.** No direct Lean. The `MarkovAlgebra` typeclass in
`categorical-mass-markov.lean` carries the descended-trace identity
that the proton/neutron primitives compute.

**Summary.** Deprecated by author flag (header banner + PR #577
postscript in `brane_tower_isospin_diagnosis.py`). Preserved for
its nucleon primitives only; do NOT extend.

## 6. `atom_mass_partition.py`

**Math claims walked.**

Partition-by-partition Markov trace at H_n(q) — one
seminormal-form matrix per λ ⊢ n, then
`tr_M(β) = Σ_λ (d_λ²/n!)·Φ_λ`
where `Φ_λ = Σ_gen ln|tr(M_gen^λ)|` is the log-product of generator
traces in the λ-irrep. Tests on ⁴He = `ppnn` (4 strands).

The seminormal construction (`hecke_generator_matrix`, line 127)
follows the standard rule: same-row → eigenvalue q, same-column →
eigenvalue −q⁻¹, mixed → 2×2 block with trace H_A and determinant
−1.

**Paper backing.**

Loose backing via
[`prop:categorical-mass-markov`](../../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md)
+ `rem:atom-mass-full-hecke` (three-channel decomposition at A = 1).
The Wedderburn weight `d_λ²/n!` is the classical Plancherel weight,
**not** the q-deformed `dim_q²/[n]_q!` used by `mass_at_3A_proper.py`
— this script uses the *classical-limit* Plancherel measure even
though it evaluates at q_0 ≈ 1.11. See the notation register
collision rule on Plancherel `w_λ` vs q-deformed `\tilde w_λ`:
this script silently uses the bare `w_λ` form, which is acceptable
only as a comparison baseline.

**Lean status.** N/A — exploratory probe.

**Summary.** Diagnostic / pedagogical script; demonstrates that
the full Markov trace polynomial-time decomposes per partition.
The log-tr form `Σ ln|tr|` is **not** the canonical mass formula
(which is `|Π V̂_i|` + tower + Frobenius); this is a different
spectral invariant used elsewhere as `α · Σ ln|V̂_i|` in
`prop:atomic-braid-mass`.

## 7. `brane_tower_isospin_diagnosis.py`

**Math claims walked.**

Diagnoses the −737 MeV T − ³He pathology of the 6-term formula.
Localises the source to **T2/T3** (the brane tower):

1. T1 is irrelevant (sub-MeV).
2. T2 dominates by 10⁶ (10⁵ Hecke units per generator × ~10 gens).
3. `Φ_q(0.989) ≈ 6.7×10⁵` — typical generator value sits near the
   pole.
4. Per-generator |V̂_i| for T vs ³He differ at inter-nucleon
   positions (gen 2, 5); the 10⁵× amplification of these tiny
   differences gives ~470 MeV scale ≈ the 737 MeV pathology.
5. The canonical Markov trace does NOT have this problem.

**Verdict (POSTSCRIPT, PR #577 audit, 2026-05-09):** Same root
combination-law mistake as `atom_mass_derived.py` and
`atomic_braid_mass_table.py` — atomic mass is **additive** in
constituents, not multiplicative. Path (A) — auditing (c, d) tables
— is a wild goose chase. Path (B) — normalising Φ_q — addresses
symptom not cause. Path (C) — Φ_q only at roots of unity — is
closer to truth. The correct path: recast T2/T3 as additive
contributions to E_binding(A, Z) via `ρ_F · V_hyp`
(`rem:frobenius-packing-density`).

**Paper backing.**

This script's diagnosis is **the** evidence behind the
`prop:mass-endomorphism-tower` .md note (added 2026-05-03):
the boxed Φ_q form is "Markov-invariance-broken at q_0" and the
.md's "trace reformulation (Plancherel series)" + Heine identity
+ Kähler-derivative paths are the proposed fixes.

**Lean status.** N/A — diagnostic.

**Summary.** Negative-result witness. Treat as canonical
characterisation of the multiplicative pathology; do NOT use as
evidence about the (c, d) tables, which are correct. The
recommendation is to move to the algebraic R-side form
`Σ_S z^{|S|}·Vol_q^{(S)}(β)` (Markov-invariant by construction)
or the Heine-series / Habiro reformulation.

## 8. `brane_tower_two_avenues_probe.py`

**Math claims walked.**

Concrete numerical exploration of two structural avenues for
restoring isospin invariance to T2/T3:

- **Avenue 1 (Kähler-derivative)**: `∂/∂q tr_M(β)` and
  `∂²/∂q² tr_M(β)` on the global atomic braid via central
  finite-difference at q_0 (eps = 1e-25 mpmath at 50 dps).
  Trace-form of a Markov-invariant trace is automatically
  Markov-invariant.
- **Avenue 2 (Frobenius-antipode symmetrisation)**:
  `T2_sym(β) = ½·(T2_legacy(β) + T2_legacy(S(β)))`, where
  S sends `σ ↔ σ⁻¹` in (c, d) form via `(c, d) ↦ (c, d − c·h)`.
  Under the convention "u ↔ d under S", proton (uud) ↔ neutron
  (udd), so braid(T = 1p+2n) ↔ braid(³He = 2p+1n). Therefore
  `T2_sym(T) = T2_sym(³He)` by construction for mirror nuclei.
  The probe verifies this empirically and reports whether the
  symmetrisation gives physically reasonable values for
  non-mirror cases.

**Paper backing.**

Both avenues are listed in the
[`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
.md "Trace-reformulation (Plancherel series)" + "Kähler-derivative"
notes. Gist hash recorded in the script header
(`b3459bf9143dd03234a9fc55c370f6f4`).

**Lean status.** N/A — exploratory.

**Summary.** Positive-result probe in support of `prop:markov-pair-z2`
and the trace-form reformulation. Avenue 2 is mathematically clean
(involutive, structural) but may not improve non-mirror predictions;
Avenue 1 is the more general path-forward but needs integration into
T2 + T3 derivation. **Empirical observation:** Avenue 2's
`T2_sym(T)/T2_sym(³He) ratio ≈ 1` to within 1% confirms S maps T's
atomic braid onto ³He's at the (c, d) level.

## 9. `jet_knot_invariants.py`

**Math claims walked.**

Per-level knot invariants `a_k = Σ_λ w_λ·χ_λ(β) / Σ_λ w_λ·dim_restricted(λ)`
under the branching `H_k → H_3`, summed over partitions of k. Tests
on T, ³He, ⁴He, ⁶Li, ⁷Li, ⁹Be, ¹²C, ¹⁶O at k = 3..8. Key claim
in docstring: **a_k converges by k = 4** — k = 3 carries the nuclear
braid's topology, k ≥ 4 corrections are topology-independent.

For Z = N even-even with `sp = V_std = ap`:
  `a_k = V_inter / (1 + W_STD)`.
For Z = N odd-odd with `sp = −ap`:
  `a_k = W_STD · V_std / (1 + W_STD)`.

`internuc_characters(Z, N)` builds the transfer-matrix chain over
all internucleon crossings and returns the three characters
`(sp, V_std, ap)` in symbolic q.

**Paper backing.**

[`prop:confined-knot-binding`](../../content/quantum-observable-universe/braids-and-knots/confined-knot-binding.md)
defines the per-level knot factor `a_ℓ = V̂_ℓ(confined)/V̂_ℓ(free)`
at jet levels 0 (quark), 1 (nucleon), 2 (nucleus). The witness
script `jet_knot_invariants.py` is the **named compute** on the
content block's .ts. This script's a_k is the per-level character
ratio sampled at H_k for k = 3..8 — slightly different from the
.md's jet-level `a_ℓ` (which is a fixed ℓ ∈ {0, 1, 2}), but the
*same algebraic object* (character ratio under Wedderburn weighting).

**Lean status.**

`confined-knot-binding.ts` declares `lean.ref` =
`qou:QOU.BraidKnot.confined_knot_binding`, but I did not find a
sibling `confined-knot-binding.lean` under braids-and-knots. The
Lean target appears to be unwired.

**Summary.** Convergence-by-k=4 is the empirical content; the
algebraic form `V_inter/(1+W_STD)` (or `W_STD·V_std/(1+W_STD)` for
odd-odd) is closed-form in q. Script is a clean witness for the
content block's character-ratio decomposition. Lean side is open
(no `.lean` for this proposition yet).

## 10. `jet_tower_delta_max.py`

**Math claims walked.**

Measurement witness for `conj:jet-tower-uniform-delta-max`.
Runs `unified_lift.binding_unified(Z, N)` (which already computes
delta_n per jet level inside `unified_lift.py` line 158+) on
{D, T, ³He} across n = 1..N_MAX = 8 (configurable via env var).
For each atom records:
- per-level `Δ^(n) = 𝔪^(n)(free) − 𝔪^(n)(atom)` history;
- max `|Δ^(n)|` (the empirical Δ_max);
- geometric-decay ratio `|ℏ_q^{2n}·Δ^(n)| / |ℏ_q^{2(n−1)}·Δ^(n−1)|`
  — the conjecture predicts ≈ ℏ_q² ≈ 0.00982 once Δ_max saturates;
- `uniform_bound_pass` flag (true if `|Δ^(n)|` does not grow,
  modulo 1e-6 tolerance).

Aggregate pass: every atom passes. The witness now carries
`add_assertion("aggregate_uniform_bound_pass", computed, 1.0, tol=0.0)`
so `allPassed` reflects it (PR #578).

**Is this a T8+ candidate?**

The script is the **path (b) deliverable** for workplan task **P3.4**
on
[`conj:jet-tower-uniform-delta-max`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-uniform-delta-max.md).
It is **not** a Term 8 candidate in the 6-term formula. It is the
**measurement infrastructure for the uniform-bound hypothesis** of
`prop:jet-tower-convergence`. If naming the conjecture as
"T8+ candidate" refers to a 7-or-more-term extension of
`thm:knot-mass-formula-unified`, the answer is: **no, this measures
the convergence rate of the recursive jet ascent, not a new mass
term**. The truncation to N terms in `prop:jet-tower-convergence`
yields a geometric tail bound *modulo* the conjecture in this
script's name.

**Paper backing.**

- Primary:
  [`conj:jet-tower-uniform-delta-max`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-uniform-delta-max.md)
  — names the uniform-boundedness hypothesis and points at this
  script as the path (b) resolution.
- Secondary:
  [`prop:jet-tower-convergence`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-convergence.md)
  — geometric tail bound conditional on the conjecture; states
  `|Δ^(n)|·ℏ_q^{2n}` decays as `ℏ_q^2 ≈ 0.00982` once bounded.

**Lean status.**

[`jet-tower-uniform-delta-max.lean`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-uniform-delta-max.lean)
declares `class JetTowerUniformDeltaMax (ρ : Type*)` with fields
`delta`, `delta_max`, `delta_max_nonneg`, `uniform_bound` — a clean
**conditional-class** (AGENTS.md §3b-cond) axiomatisation of the
conjecture. `geometric_tail_bound_abstract` is the conditional
theorem under the class. A trivial-delta `canonical` instance is
provided (zero delta everywhere), discharging the §3b-cond
hypothesis with empty content.

[`jet-tower-convergence.lean`](../../content/quantum-observable-universe/braids-and-knots/jet-tower-convergence.lean)
proves `jet_tower_tail_bound` **fully** in Mathlib — no `sorry`.
Summability via Weierstrass M-test (`summable_tower_terms`),
geometric tail via `tsum_geometric_of_lt_one`, and the
engineering corollary `jet_levels_for_precision` for the N-bound.
This is the **strongest formalised result** in the audit: it is
the proof that under a uniform-Δ bound, the jet tower converges
geometrically with explicit error budget.

**Summary.** Best-formalised compute in the audit. Lean side is
fully verified modulo the named conjecture; the conjecture's
`Lean class` is a textbook conditional-class instance; the .py
script is the empirical evidence (`aggregate_uniform_bound_pass`
flag) supporting the conjecture's plausibility at n = 1..8 for
D, T, ³He. **Not a new mass term.**

## Cross-cutting notes

**f64 vs MPFR distinction.** Of the ten files, three are
explicitly 50-dps mpmath:
- `mass_at_3A_proper.py` (mp.mp.dps = 50 inferred via callers).
- `brane_tower_two_avenues_probe.py` (`mp.mp.dps = 50`).
- `brane_tower_isospin_diagnosis.py` (`mp.mp.dps = 30`).

The rest are f64, including `mass_endomorphism.py`. The
PR's MPFR port lifts `mass_endomorphism.py`'s Φ_q tower to 50 dps
(via `mass_formula_6term_mpfr_50dps.py`); this audit confirms that
the f64 reference at q_0 reproduces the 1.8% proton–electron error
the .md headlines, so the MPFR port should match to ≥ 4 sig fig and
extend stability to A ≥ 4 atoms where intra-nucleon |V̂_i| → 1 makes
f64 Φ_q evaluation unreliable.

**Atom-braid convention.** The canonical 3A-strand atom-braid word
is generated by `atom_braid_word_3A` in `mass_at_3A_proper.py`
(line 230), with operator-valued σ at every position (no disjoint
tensor product). Inter-nucleon generators `3k+2` mediate between
the k-th and (k+1)-th nucleon; the (c, d) pairs encode pp / nn / pn
flavour content via the standard `(1, 0)` / `(1, −h)` / `(1, −h/2)`
prescriptions. This convention is shared with
`hecke_core.atom_per_generator_volumes` and is the basis of every
witness that feeds the canonical Markov-trace path.

**Φ_q vs Li_2^q discrepancy.** Six of the ten scripts call the
Faddeev `Phi_q` (asymmetric q-integers); the
`prop:mass-endomorphism-tower` .md, since 2026-05-03, has migrated
to the symmetric `Li_2^q`. The Lean's `quantumDilog` (mass-endomorphism-tower.lean
line 88) still mirrors the old Φ_q convention. **This is a documented
narrative–compute–Lean drift** that the proof-narrative-lean-equivalence
skill should resolve in a follow-up; the open question (per the .md
"Open" note) is whether `Li_2^q(−|V̂_i|)` evaluation cures the
mirror-nucleus pathology in `brane_tower_isospin_diagnosis.py`.

**Operator-selection LP duals.** None of the ten scripts in scope
emit LP/SDP dual fields (none of them solve an LP). The
LP-dual baseline rule in AGENTS.md applies to operator-selection
scripts (`crt_markov.py`, `multi_level_sdp.py`,
`misdp_cross_channel.py`, etc.), not to this set. No CI hint
collisions expected.

## Open issues flagged

1. **`prop:mass-endomorphism-tower` .lean drift.** Mass formula
   uses adjacent-only sum + Faddeev Φ_q; .md uses all-pairs +
   symmetric `Li_2^q`. Resolve by either updating the Lean to
   the symmetric form or back-porting the .md update.
2. **`atom_braid_word_3A` has no Lean.** The canonical chain
   generation lives only in Python; the `MarkovAlgebra` typeclass
   on the Lean side treats T_w as opaque. Closing this requires a
   constructive Lean definition of the atom-braid word.
3. **`confined-knot-binding.lean` missing.** Block's `.ts`
   declares the Lean ref but no `.lean` sibling exists.
4. **Φ_q tower is Markov-invariance-broken at q_0.** Three
   diagnoses agree (isospin pathology, additivity refutation, Φ_q
   pole near `|V̂_i|=1`). The reformulation paths (Heine series,
   Kähler-derivative, Frobenius antipode, ρ_F · V_hyp) are
   actively explored; none are yet a closed substitute for
   T2 + T3 + T6 at the atomic-braid scale.
5. **`jet_tower_delta_max.py` is the best-formalised path.**
   Full Mathlib proof + class instance + witness assertion +
   conditional-class structure — should be cited as the
   template for other open §3b-cond conjectures (Δ_max,
   `MassEvaluation`, etc.).
