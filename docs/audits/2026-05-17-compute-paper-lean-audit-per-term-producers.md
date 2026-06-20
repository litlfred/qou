# Compute → Paper → Lean audit — per-term producers + y_λ machinery

**Date:** 2026-05-17
**Scope:** Math-bearing functions in the per-term mass-formula
producers (T5 chirality, T6 residues, T7 shell correction) plus the
y_λ Jones–Markov-weight pipeline. Wiring (witness scaffolding, CLI
plumbing, JSON I/O) is intentionally skipped.

**Convention.** Each file gets four short sections — *math claims*,
*paper block backing*, *Lean backing*, *summary verdict*. Files
present:

1. `term6_residues_at_roots.py` (T6 canonical producer)
2. `term6_full_pole_sum.py` (T6 legacy / Schur-Weyl path)
3. `term5_aK_audit.py`
4. `term7_alpha5_crystal_derivation.py`
5. `term7_chi5_basis.py`
6. `term7_height6_partition_enum.py`
7. `y_lambda_symbolic_validate.py`
8. `regenerate_y_lambda_mpfr.py`
9. `y_lambda_macdonald_telescope.py`
10. `markov_weights_symbolic.py`

Missing (acknowledged but not audited): `y_lambda_at.py`.

---

## 1. `term6_residues_at_roots.py` — canonical T6 producer

**Math claims.**
- T6 is defined as the principal-part contribution of the meromorphic
  function tr_M(T_w, q) at **non-zero roots of unity**, evaluated at
  q₀ (`thm:six-term-mass-formula-complete`, Term 6 line in the boxed
  formula).
- The function `lift_q_to_u(tr_sym, q, u)` performs an algebraic
  substitution `q^(k/2) ↦ u^k`, mapping the symbolic Markov trace to
  the u-plane (`u² = q`) on the principal branch `√q = u`. This is a
  pure algebraic rewrite — no analytic content beyond branch choice.
- `power_series_invert(D_poly, u, k)` is a coefficient-by-coefficient
  recurrence: given `D = Σ d_j u^j` with `d_0 ≠ 0`, returns `I` of
  degree `< k` with `D · I ≡ 1 (mod u^k)`. Linear recurrence
  `I[n] = −(1/d_0) Σ_{j≥1} d_j I[n−j]` is exact (no truncation /
  numerical error).
- The math claim of `split_polar_at_u0(tr_u, u, u0_sp)` is the
  rational decomposition

      tr_u(u) = entire(u) + A(u)/u^k + B(u)/Dprime(u)

  where (i) `entire = quot(N // D)` is the polynomial part; (ii)
  `A(u)` (degree `< k`) is the principal part at `u = 0`, obtained
  via `A ≡ R · Dprime^{−1} (mod u^k)`; (iii)
  `B = (R − A·Dprime)/u^k` is an exact polynomial division. The
  **Term 6 value** is then `B(u₀) / Dprime(u₀)` — the principal-part
  contribution at non-zero u-poles, transported back to q₀ via
  `u₀ = √q₀`. The claim that this is the non-zero-roots-of-unity
  residue sum rests on the fact that (a) tr_M(u²) has poles only at
  `u = 0` (Hecke generator pole) and at u-roots of cyclotomic
  factors (which lift the q-roots-of-unity), and (b) the
  partial-fraction split is *the* unique decomposition by elementary
  algebra over `ℚ[u]` (or its localisation).
- Auxiliary closed-form check in `compute_atom`: for canonical pppnnn
  atomic braids, `D(u) = 2^(2A+1) · u^(18Z+21N+1) · (1+u²)^(3A−1)`,
  imported from `d_u_closed_form_proof`. The detected pole order at
  `u = 0` is cross-checked against `18Z + 21N + 1`.

**Paper backing.** Primary block:
[`six-term-mass-formula-complete.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md)
defines T6 = "Σ residues at the non-zero primitive roots of unity"
in the master formula (line 21). Pole-structure backing:
[`full-pole-structure-mass-trace.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.md)
explicitly states the cyclotomic-completion picture: tr_M lies in
the Habiro ring `Ẑ[q]`, has well-defined values at every root of
unity, and the partial-fraction-residue picture is a *formal residue
spectral sum* (i.e. a finite-truncation shadow), not a global
ℂ-meromorphic identity. The producer's correctness as the "Term 6"
value is therefore *conditional* on the cyclotomic-truncation
interpretation: the rational function `tr_u(u) ∈ ℚ(u)` is a
truncated representative whose non-zero-pole principal-part value
at u₀ is what the formula assigns to T6 *for that representative*.

**Lean backing.** The Lean file
[`full-pole-structure-mass-trace.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.lean)
encodes the **polynomial Habiro-ideal property** as a `class
HabiroCompletion` with field `tail_in_ideal`: for every truncation
order N, `qPochhammerPoly N | (trace − Σ_{m<N} a_m · (u;u)_m)`. Two
real-valued lemmas are proved without sorry —
`habiro_truncation_bound` (Pochhammer monotonicity on `0 < q < 1`)
and `habiro_truncation_bound_supercrit` (the `q ↔ q⁻¹` involution
bridge applied to the QOU substrate value `q₀ > 1`). The
partial-fraction split algorithm itself (the producer's actual math
content) is *not* in Lean — the Lean side commits only to the
cyclotomic-completion / Pochhammer-monotonicity infrastructure.

**Summary.** Math is correct as an algorithm. The arithmetic
operations (polynomial division, recurrence inversion, exact rational
substitution at u₀) are bit-exact within sympy. The interpretation
of the output as "the non-zero-roots-of-unity residue contribution
to T6" depends on `full-pole-structure-mass-trace.md`'s Habiro
clarification: this is a finite-truncation observable, not a global
analytic residue. Lean covers the Pochhammer-bound infrastructure
but not the partial-fraction algorithm.

---

## 2. `term6_full_pole_sum.py` — legacy Schur-Weyl-weighted path

**Math claims.**
- Mittag-Leffler expansion `tr_M(T_w, q) = entire(q) + Σ_{n≥2}
  Σ_{j: gcd(j,n)=1} r_n^{(j)}/(q − ζ_n^{(j)})` with primitive
  n-th roots `ζ_n^{(j)}`, residues `r_n^{(j)}`, cutoff `n_max`.
- `cyclotomic_residue(tr_M_expr, zeta, n)` returns the simple-pole
  residue `lim_{q→ζ} (q − ζ) · tr_M`, with `sp.oo` flagged for
  higher-order poles.
- `_higher_order_q_residue_via_sqrt_sub` falls back to a Cauchy
  contour integral in u-space at `u₀ = √ζ` with chain-rule
  integrand `2u · U(u)`. The contour identity
  `∮_{|u−u₀|=r} 2u · U(u) du = 2πi · Res_q[tr_M]` is the correct
  chain rule for `q = u²` and recovers any pole order in `u`.

**Paper backing.** Same block as #1 — but the file *carries a major
explicit caveat at the top*: it consumes
`habiro-coefficients-atomic.witness.json` which is populated by the
*Schur-Weyl* weight `s_λ(q,q⁻¹) / H_q(λ)`, **not** the canonical
Markov tr_M `Σ_λ y_λ χ^λ`. Per the explicit note (lines 9-19) and
the audit caveat embedded in the witness builder, the canonical T6
path is `term6_residues_at_roots.py` and the deuteron split is
`canonical 0.388 vs Schur-Weyl-weighted 0.177` at q₀. The
`full-pole-structure-mass-trace.md` Habiro clarification applies
equally — the primitive roots are dense in `S¹` and the
Mittag-Leffler sum is a finite-truncation symbol, not a global
analytic identity.

**Lean backing.** Same as #1 (`full-pole-structure-mass-trace.lean`).
No Lean reflects the Schur-Weyl-weighted trace path; the Lean class
captures only the canonical Habiro statement.

**Summary.** Math is internally consistent as a Schur-Weyl-weighted
contour calculation. The file is explicitly *non-canonical* for T6 —
its output should be read as "the Schur-Weyl-weighted contribution",
not the paper's T6. The chain-rule contour integral for higher-order
poles is correct (the residue identity 2u·U(u) du = du/dq · q-side
integrand is standard). Kept as documented infrastructure for the
u-substitution method.

---

## 3. `term5_aK_audit.py` — chirality factor cross-check

**Math claims.**
- Closed-form Term-5 chirality:
  `a_K = Π_{c ∈ pn-crossings}(1 + sign(c) · h)`, `h = q − q⁻¹`.
- Gram-matrix form: `a_K = G_{β,β*} / G_{1,1} = tr_M(β · (β*)⁻¹)`.
- Four mirror-braid variants V1–V4 with the involution acting
  variably on σ_i, σ_i⁻¹, averaged crossings. V1 = β⁻¹ in Hecke
  (reverse + invert). V2 = mirror knot K* (invert each, keep order).
  V3 = antipode-style (reverse only). V4 = V2 with explicit
  averaged-crossing-is-self-mirror.
- All variants agree on words containing only σ, σ⁻¹ (no averaged
  crossings) — they only differ in how `½(σ + σ⁻¹)` maps under the
  involution.
- The audit compares closed-form numerical `a_K` vs `tr_M(β · β*)`
  for each variant at q₀, computed via the canonical Hecke division
  + Markov-trace pipeline.

**Paper backing.** The production block
[`six-term-mass-formula-complete.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md)
T5 section explicitly cites both forms, notes the proton 2.2% gap
(closed 1.000 vs Gram-V1 = (1+q²)⁴/(16q⁴) = cosh⁴(log q) ≈ 1.022 at
q₀), and points to this audit as the reconciliation step. The
companion blocks
[`gram-matrix-spectral-connection.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/gram-matrix-spectral-connection.md)
gives the conceptual identity `a_K = G_{β,β*}/G_{1,1}` (Term 5 row in
the Gram-matrix-in-three-terms table) and the *conjecture-class*
[`conj:knot-factor-frobenius-pairing`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/knot-factor-frobenius-pairing.md)
houses the structural identification.

**Lean backing.** [`KnotFactorFrobeniusPairing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean)
defines `class KnotFactorFrobeniusPairing` with a `factorisation_holds`
field — a §3b conjecture class. The class has a trivial `instance
canonical` (Markov trace ≡ 0, Frobenius pairing ≡ 0,
`factorisation_holds` discharged by `rfl`); this is a structural
skeleton only and **encodes no chirality content**. The downstream
conditional theorem `markov_trace_factors` is correct (it just
unpacks the class field). The four-variant audit itself is not
formalised.

**Summary.** Math claims are well-defined per variant. The audit's
function is *to surface* the closed-form / Gram-matrix discrepancy
across V1–V4 against the empirical spectrum, not to assert
agreement. Wall-time caveats in the docstring (V2 alone takes >34
min for deuteron) match the symbolic-blowup pattern; `--variants V1`
is the fast canonical path. Lean side is a placeholder class with a
trivial instance — the conjecture proper still rides on the
narrative. Cross-check vs the V2 chirality probe in
`term5_v2_chirality.py` (referenced in user's brief, already
audited) belongs in a follow-up reconciliation pass.

---

## 4. `term7_alpha5_crystal_derivation.py` — α_5 · S_crystal(A) derivation

**Math claims.**
- `crystal_chi_lambda(shape, word)`: trace of the q→0 (crystal-limit)
  signed-permutation action of a braid word on the SYT-basis of the
  λ-irrep. The action of σ_i on a SYT T is `T ↦ sign(ρ_T(i)) · T`
  where `ρ_T(i) = contents[T[i+1]] − contents[T[i]]` is the *axial
  distance*; ρ > 0 ↦ +1, ρ < 0 ↦ −1, ρ = 0 ↦ 0. The trace then
  reduces to a fixed-point sum-of-sign-products over SYT(λ).
- `plancherel_weight(shape) = f_λ² / n!` (classical Plancherel
  measure at q = 1).
- `S_crystal(A) = Σ_{λ ⊢ 3A, height(λ) ≤ 6} w_λ(q=1) · χ_λ_crystal(β_A)`.
- The output is interpreted as the **crystal-side prediction** of
  T7's shell-correction sum: no free parameter, only the structural
  invariant of the braid topology + the height-6 partition support.
- The assertion `S_crystal_4He_isobar_independent` checks that ⁴He
  (doubly magic) has `|S_crystal(⁴He)| < 10·|S_crystal(³He)| + 1`
  — a structural cancellation pattern.

**Paper backing.**
[`shell-correction-term-seven.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.md)
§Status (lines 191-227) explicitly cites this script's witness and
states the closed form `S_crystal(A) = Σ_{λ ⊢ 3A, height(λ) ≤ 6}
w_λ(q=1) · χ_λ^crystal(β_A)`. The bound `height(λ) ≤ 6` is
documented as **cumulative GS-filtration through level 5**, refining
the per-stratum χ_5 originally defined in the same block. The
${}^4$He value `S_crystal(⁴He) ≈ −0.991241` is named as the
no-free-parameter structural invariant. Crystal-limit χ_λ backing:
[`crystal-isospin-degeneracy.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md)
documents the crystal-limit signed-permutation action on SYT (lines
30-70 region).

**Lean backing.**
[`shell-correction-term-seven.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.lean)
encodes `class ShellCorrectionTermSeven` with five fields: `h_star`,
`shadow_price`, `scaling`, `term_seven_value`, plus two `Prop`-valued
fields (`term_seven_decomposition`, `sub_percent_accuracy`). The
two downstream theorems `term_seven_decomposition_apply` and
`term_seven_sub_percent` are fully verified by Lean modulo the
class instance — this is the §3b-cond conditional-class pattern
done correctly. The **crystal-graph realisation** that the producer
relies on (`χ_λ_crystal` = signed-permutation trace) is itself a
separate conjecture
([`conj:crystal-graph-realization`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md))
about the Brundan–Kleshchev / KLR ↔ Hecke bijection — the producer
inherits its conjectural status.

**Summary.** The script implements `χ_λ_crystal` as the trace of a
signed permutation determined by axial-distance signs, which is the
literature-standard crystal-limit character (Lecouvey,
Brundan–Kleshchev). The Plancherel weight `f²/n!` is correctly the
q=1 limit of the canonical q-deformed Wedderburn weight `tilde w_λ =
dim_q²/[n]_q!` per
[`wedderburn-weight-canonical.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md).
The math is sound conditional on the crystal-graph-realisation
conjecture; α_5 itself remains AME-calibrated (not yet derived).
Two minor authoring details:

- The producer's `crystal_chi_lambda` only handles the *diagonal*
  contribution to the SYT permutation action (when T is a fixed
  point of the SYT permutation induced by β); off-diagonal
  SYT-swaps in the column-rich support are explicitly skipped per
  the docstring. This is correct for the QOU atomic braid words
  where the crystal action is diagonal in the chosen SYT-basis, but
  the limitation should be flagged when extending to other braid
  classes.
- `height_6_partitions(n)` returns partitions with at most 6 parts
  (consistent with the narrative's cumulative `height ≤ 6` reading).
  This matches the .md's explicit refinement note (line 196).

---

## 5. `term7_chi5_basis.py` — q-deformed Wedderburn-weight basis at A=2..6

**Math claims.**
- Encodes the χ_5 partition-side basis:
  `χ_5(T_w) := Σ_{λ ⊢ 3A, ht(λ) = 6} w_λ(q) · χ^λ(T_w)` with
  `w_λ = dim_q(λ)² / [n]_q!` and `dim_q(λ) = [n]_q!/Π[h_x]_q`
  (hook-content formula).
- `q_int(k, q) = (q^k − 1)/(q − 1)` is the **unsymmetric quantum
  integer**, not the symmetric form `(q^k − q^{−k})/(q − q^{−1})`.
  The docstring notes both give the same `dim_q` up to a power of
  `q` that cancels in the numerator/denominator ratio — correct
  for the hook-content formula because both numerator `[n]_q!` and
  denominator `Π[h_x]_q` are q-factorials of the same length, so
  the prefactor cancels exactly.
- Output: per-partition `dim_q` + Wedderburn weight `w_λ = d²/[n]_q!`
  at q₀ = 1.1099785955541805 to 60 dps, plus `Σ w_λ` as an upper
  bound on `|χ_5(T_w)|` when `|χ^λ| ≤ 1`.

**Paper backing.** Direct backing in
[`shell-correction-term-seven.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.md)
(§"Structural form of χ_5", lines 122-137). The per-stratum
height-6 reading (`ht(λ) = 6`) is the original projector; the
cumulative `ht(λ) ≤ 6` reading lives in `term7_alpha5_crystal_derivation.py`.
The naming convention `w_λ` here matches the "q-deformed Wedderburn-block
weight" in
[`wedderburn-weight-canonical.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/wedderburn-weight-canonical.md)
— and note that `wedderburn-weight-canonical.md` carries a AGENTS.md
register flag: the q-deformed weight should be written `tilde w_λ`
with a tilde to disambiguate from the classical Plancherel measure
`w_λ`. The producer uses plain `w_λ` in its docstring and JSON —
strictly speaking it should be `tilde w_λ` to match the register.

**Lean backing.** Same class
([`ShellCorrectionTermSeven`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/shell-correction-term-seven.lean))
as #4. The hook-content closed form is not in Lean here; the
Macdonald hook-content telescope
([`macdonald-hook-telescope.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.lean))
contains the closest formal statement, with a single `sorry`
pointing at the classical Stanley/Macdonald reference for the
regular-representation Frobenius identity.

**Summary.** Math is the standard q-deformed Wedderburn weight via
unsymmetric q-integers — correct and clean. The "audit-only" tag in
the witness JSON correctly flags this as a precursor to the full α_5
fit, blocked on extending the GS-filtration jet tracker to H_n for
n ≥ 4. Notation drift: `w_λ` in the docstring should be `tilde w_λ`
per the register's collision rules. Otherwise no math defects.

---

## 6. `term7_height6_partition_enum.py` — partition basis + α_5 amplitude estimator

**Math claims.**
- Same hook-content formula and unsymmetric q-integer infrastructure
  as #5 (the two files are siblings — #5 imports from a shared core,
  #6 is the earlier first-pass).
- New math content: structural α_5 amplitude estimator
  `ρ_α_5 = dominant_weight / total_weight`, plus `top_5_share`.
  This is a *structural* estimator — the docstring carefully states
  "this is a structural amplitude estimator, not a fit". The
  Mayer-Goeppert shell-closure argument is cited as motivation but
  not used to derive a numerical α_5.
- `partitions_of_height(n, height)` returns partitions with
  **exactly** `height` non-zero parts (not `at most`) — the stricter
  reading from the χ_5 per-stratum definition, matching the original
  projector in `shell-correction-term-seven.md` (line 125: `ht(λ) =
  6`).

**Paper backing.** Same as #5. The cumulative-vs-per-stratum reading
divergence between #5/#6 (per-stratum, `=`) and #4 (cumulative, `≤`)
matches the narrative's explicit refinement note (§Status: "The
bound height(λ) ≤ 6 matches the implemented enumeration in
term7_alpha5_crystal_derivation.py … it refines the per-stratum χ_5
projector defined earlier in this document by including
contributions from the lower strata ℓ = 0, …, 4"). Both readings
are correctly supported by the narrative — and the producer #6 is
the per-stratum reading, #4 is the cumulative reading. No
inconsistency.

**Lean backing.** Same class as #4/#5.

**Summary.** Clean partition enumeration + Wedderburn weights. The
α_5 amplitude estimator is a structural-but-not-derived heuristic,
correctly tagged. Same `tilde w_λ` vs `w_λ` notation drift as #5.
The fork between #5's `at most height` and #6's `exactly height` is
deliberate and documented.

---

## 7. `y_lambda_symbolic_validate.py` — three-test validation of Wenzl-bridge y_λ

**Math claims.**
- **Test 1 (cross-q)**: at five q probes ∈ {1.05, 1.08, q₀, 1.15,
  1.20}, the Wenzl-bridge numeric y_λ agrees with reference
  (MPFR witness or higher-precision Wenzl-bridge) to `max abs diff
  < 10⁻³⁰`.
- **Test 2 (Markov-axiom M3)**: `Σ_λ y_λ · d_λ = 1` (M3 = `tr_M(1) = 1`).
  Symbolic for n ≤ 4 (exact 0); numeric for n ≥ 5 (residual < 10⁻⁴⁰
  at 80 dps).
- **Test 3 (Markov-trace defining identity)**: `Σ_λ y_λ · χ_λ(σ_{w_μ})
  = z^{n−len(μ)}` for the extreme cycle types `μ = (n,)` and
  `μ = (1,…,1)`. The RHS comes from iterating the Markov axiom
  `tr_M(σ_i x) = z · tr_M(x)`; for a length-`n−len(μ)` cycle-type
  representative this gives exactly `z^{n−len(μ)}`.
- `chi_lambda_symbolic(partition, word, q)` builds the Hoefsmit
  seminormal σ_i matrices on SYT(λ): diagonal entry `a = h/(1 −
  q^{-2ρ})`, off-diagonal entry `√(a·a' + 1)` with ρ the axial
  distance. The matrices are correctly Hoefsmit's representation in
  the Brink-Howlett-style normalisation.
- Markov-axiom-rename audit: the script carefully disambiguates
  Markov-axiom M3 (`Σ y_λ d_λ = 1`) from the genuine Plancherel
  identity (`Σ d_λ²/n! = 1`); per the audit at
  `docs/audits/2026-05-11-plancherel-usage-audit.md` (Finding D)
  these are not the same. The script's prior name
  `test_2_plancherel` is retained as a back-compat alias.

**Paper backing.** Direct: [`y-lambda-closed-form-wenzl-bridge.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.md)
states the boxed closed form. Markov-trace defining identity is
[`prop:markov-pair-z2`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md)
(adjacent / non-adjacent case z²; iterating gives the z^{n−len(μ)}
identity). The terminology disambiguation (`tr_M(1) = 1` ≠
classical Plancherel `Σ d_λ²/n! = 1`) is recorded in
`wedderburn-weight-canonical.md` and the cited audit.

**Lean backing.** [`y-lambda-closed-form-wenzl-bridge.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/y-lambda-closed-form-wenzl-bridge.lean):
the main theorem `y_lambda_closed_form_wenzl_bridge` is *currently
discharged on a stub model* (the `wenzlSchurElement` is a
content-bearing zero, so both sides reduce to 0 via `zero_mul`).
The two uniqueness layers (`wenzl_bridge_unique_definitional` =
rfl-discharge, `wenzl_bridge_unique_categorical` = conditional on
`MarkovTraceFamilyOneDim` class) are correctly structured per
AGENTS.md §3b-cond. `y_lambda_bridge_numerical_agreement : True :=
trivial` is a witness-pointer placeholder.

**Summary.** Math claims are correctly stated and numerically
verified across the documented n=2..12 range with the documented
tolerances. The script's Markov-vs-Plancherel disambiguation is
done with rigor and matches the recent audit. The Lean theorem
holds on a stub model; the genuine categorical content rests on
the Wenzl bridge + Chlouveraki HDR 6.20 class hypothesis.

---

## 8. `regenerate_y_lambda_mpfr.py` — true-50-dps y_λ regenerator

**Math claims.**
- No new math: the script reads exact symbolic y_λ expressions from
  `y-lambda-wenzl-bridge-symbolic-witness.json` (produced by the
  Wenzl-bridge closed form per #7) and evaluates each at q₀ to 50
  dps via `sp.sympify(...).subs(q, q_0_str_50dps).evalf(50)`,
  followed by an `mpmath.mpf` round-trip for string-format canonicalisation.
- Headers (lines 4-26) document a substantive precision fix: the
  previous MPFR witness was f64-truncated at digit ~14 (claimed 50
  dps but only 14 honest digits). This script side-steps the f64
  truncation by passing `mp.nstr(Q_MP, 50)` as a decimal string
  directly to sympy, so every y_λ value is honest 50-dps.

**Paper backing.** Same as #7 (Wenzl-bridge closed form). The audit
trail (AUDIT-DEEP-2026-05.md §7; PR #564) is referenced in the
witness JSON.

**Lean backing.** None — purely numerical regeneration.

**Summary.** No new math; precision fix only. Correct and clean.

---

## 9. `y_lambda_macdonald_telescope.py` — closed-form Macdonald telescope

**Math claims.**
- The Macdonald hook-content **telescope identity**:
  `Z_n := Σ_{λ ⊢ n} f_λ · s_{λ,X}(Q) = ((1−X)/(1−Q))^n`, where
  `s_{λ,X}(Q) = Q^{n(λ)} · Π_{x∈λ}(1 − X·Q^{c(x)})/(1 − Q^{h(x)})`.
- Identity ★: `Σ_{λ ⊢ n} f_λ · s_λ = p_1^n` (Stanley EC2 Cor.
  7.12.5; Macdonald I.3 ex.1) — the regular-representation
  Frobenius identity. Under the principal specialisation in r
  variables `x_i ↦ q^{i−1}`, `p_1 ↦ 1 + q + ⋯ + q^{r−1} =
  (1−q^r)/(1−q)`. Substituting `q ↦ Q`, `X = Q^r` gives `Z_n =
  ((1−X)/(1−Q))^n`.
- Closed form ♣ for y_λ collapses to
  `y_λ = Q^{n(λ)} · (1−Q)^n/(1−X)^n · Π(1 − X·Q^{c(x)})/(1 − Q^{h(x)})`
  — O(n) per partition, no `sympy.simplify` needed.
- `verify_telescope_identity(n_max)` symbolically checks
  `sp.cancel(Z_n − ((1−X)/(1−Q))^n) == 0` for n = 0..n_max
  (sandbox-mode 0..6, CI-extended 0..8).
- `verify_telescope_collapse` checks per-partition agreement of ♣
  vs raw `s_λ/Z_n`.
- `cross_check_mpfr` numerically spot-checks ♣ against the MPFR
  Hoefsmit-matrix witness.

**Paper backing.** [`macdonald-hook-telescope.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.md)
states the proposition (boxed `Z_n = ((1−X)/(1−Q))^n` and boxed
`y_λ` closed form), proves it from the principal specialisation of
the regular-representation Frobenius identity, and references this
script as the empirical witness (n = 0..6 symbolic, MPFR
cross-check max |Δ| ≈ 2.5×10⁻⁵¹).

**Lean backing.** [`macdonald-hook-telescope.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/macdonald-hook-telescope.lean):
`theorem macdonald_hook_telescope` is stated abstractly as
`wenzlNormalizationOfShape n Q X = telescopeRHS n Q X` and proved
with a single `sorry` carrying a `[stanley1999] Cor. 7.12.5`
citation. Downstream `theorem y_lambda_closed_form_via_telescope`
is unfolded via `macdonald_hook_telescope`. A
`macdonald_hook_telescope_witness_scope` theorem records the
n = 0..6 partition-count sum `1+1+2+3+5+7+11 = 30` and is proved
by `decide`.

**Summary.** This is the cleanest entry in the suite: math claim is
the standard Stanley/Macdonald identity, principal specialisation
makes it directly applicable to the Wenzl-bridge, the empirical
verification is exhaustive (every partition of every n ≤ 6
symbolic; MPFR cross-check to ~10⁻⁵¹). Lean state is correctly a
single sorry pointing at the cited reference — the conventional
formalisation is to import the classical identity from Mathlib's
combinatorics library, which is currently still developing the
relevant symmetric-function machinery. CI extension flag
`QOU_EXTEND_SCOPE=1` to push to n = 8 is documented.

---

## 10. `markov_weights_symbolic.py` — closed-form y_λ at H_3 + ladder solve

**Math claims.**
- For n = 3: solves the 3×3 linear system `A · y = b` where
  `A_{ij} = χ^{λ_j}(σ_1 ⋯ σ_{i−1})` (the "ladder" basis), `b_i = z^i`.
  By Markov-axiom descent, `tr_M(σ_1 ⋯ σ_{i−1}) = z^{i−1}`, so the
  system determines y_λ uniquely (the basis spans
  `Span(class indicators)` and is invertible at generic q). Output:
  three closed-form rational expressions in `Q = q²`.
- For n ≥ 4: falls back to the Wenzl Schur-principal-specialisation
  formula `y_λ = s_λ(1, Q, …, Q^{r−1}) / Σ_μ d_μ s_μ(...)` (= ♣ from
  #9 above) because the ladder linear system is rank-deficient.
- Convention bridge: Wenzl level `r` is encoded via `X = Q^r =
  z_W/(1 − Q + z_W)` with `z_W = q·z` (the `g = q·σ` affine
  convention shift).
- `tr_M_canonical(crossings, n) = Σ_λ y_λ(q) · χ^λ(β)` reconstructs
  the canonical Markov trace from y_λ and Hoefsmit characters.
  Cross-validated at q₀ against `markov_peel`'s proton (1.0653062286)
  and neutron (0.9232332972) values.
- `hooks_and_contents(lam)`: standard hook/content combinatorics
  with `arm + leg + 1` hook formula and `c(x) = j − i` content.

**Paper backing.** Same as #7/#9 (`y-lambda-closed-form-wenzl-bridge.md`,
`macdonald-hook-telescope.md`). The Markov axioms `tr_M(1) = 1,
tr_M(σ_i x) = z tr_M(x), tr_M(xy) = tr_M(yx)` are from
[`markov-pair-z2.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md)
and `prop:jones-markov-trace`. The Schur-principal-specialisation
form is the `y-lambda-closed-form-wenzl-bridge.md` boxed identity.

**Lean backing.** Same as #7 (`y-lambda-closed-form-wenzl-bridge.lean`).
The H_3 ladder linear-system path is not separately formalised.

**Summary.** Two-path implementation (ladder solve at n ≤ 3, Schur
principal specialisation for n ≥ 4) is correct and well-motivated.
The n ≤ 3 path provides an independent derivation of y_λ from the
bare Markov axioms — a good cross-check on the Wenzl-bridge form.
The proton/neutron at-q₀ numerical agreement to all printed digits
is exact (matches `markov_peel` reference values).

---

## Cross-file consistency findings

1. **T6 split is canonical.** The canonical T6 path is
   `term6_residues_at_roots.py`; `term6_full_pole_sum.py` is the
   non-canonical Schur-Weyl-weighted path. Both files are explicit
   about this — the latter carries a verbose top-of-file convention
   caveat with the canonical/Schur-Weyl deuteron-split numbers.

2. **T7 height-6 reading: two valid readings, both implemented.**
   `term7_chi5_basis.py` and `term7_height6_partition_enum.py` use
   the per-stratum reading (exactly height 6); `term7_alpha5_crystal_derivation.py`
   uses the cumulative reading (height ≤ 6). The narrative
   (`shell-correction-term-seven.md` §Status) documents both and
   notes the latter refines the former by including lower strata.

3. **Markov M3 vs Plancherel disambiguation is enforced.**
   `y_lambda_symbolic_validate.py` renamed `test_2_plancherel →
   test_2_markov_m3` per the May-2026 audit; the cited
   `wedderburn-weight-canonical.md` distinguishes the q-deformed
   Wedderburn weight `tilde w_λ` (which does not sum to 1 at q ≠ 1
   — empirically ≈ 1.51 at q₀, n = 12) from the classical
   Plancherel measure `w_λ = d²/n!` (which sums to 1 exactly).

4. **Notation register compliance — minor drift.** The T7 producers
   (#5, #6) use bare `w_λ` in docstrings/JSON for the q-deformed
   Wedderburn weight; per the register the q-deformed form should
   carry a tilde (`tilde w_λ`). Computational correctness is
   unaffected — the formula `d²/[n]_q!` is the canonical
   `tilde w_λ` regardless of letter choice. Worth a follow-up
   notation pass.

5. **Lean coverage is asymmetric.** y_λ machinery (Wenzl bridge +
   Macdonald telescope) has the most developed Lean side: classes
   exist, conditional theorems compile, single explicit `sorry`s
   point at standard references (Stanley/Macdonald). T5/T7 sit on
   §3b conjecture classes with trivial skeleton instances; the
   crystal-graph-realisation conjecture remains the gating
   conditional for T7. T6 has the Habiro-completion class + two
   Pochhammer-bound lemmas proved without sorry, but the
   partial-fraction algorithm is not formalised.

6. **Crystal χ_λ implementation caveat.** `crystal_chi_lambda`
   handles only the diagonal contribution to the SYT permutation
   action (T fixed under the β-induced SYT permutation). For the
   QOU atomic braid words this is exactly the relevant case, but
   should be flagged when extending to non-diagonal braid classes.

## Recommended follow-ups (out of scope for this audit)

- Reconcile `w_λ` ↔ `tilde w_λ` notation in T7 producer docstrings
  and JSON.
- Cross-comparison between the canonical T6
  (`term6_residues_at_roots.py`) and the Schur-Weyl-weighted T6
  (`term6_full_pole_sum.py`) on a common atom set, surfacing the
  numerical gap explicitly per atom — the deuteron 0.388 vs 0.177
  split is already documented, but a per-atom table would be
  useful.
- Tighten the `crystal_chi_lambda` docstring to explicitly state the
  diagonal-only restriction; consider extending to non-diagonal
  cases when QOU extends past atomic braid words.
- Promote `macdonald-hook-telescope.lean`'s `sorry` to a Mathlib
  import once `Mathlib.Combinatorics.Symmetric.PrincipalSpecialization`
  (or equivalent) lands.
