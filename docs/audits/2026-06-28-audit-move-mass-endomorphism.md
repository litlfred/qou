# Audit: Move Mass Endomorphism Numerical Comments

Extracted infrastructure and numerical testing commentary from `content/quantum-observable-universe/mass-endomorphism/`:
## mass-endomorphism-conjecture.md

```markdown
1. *Yekutieli finite-slice truncation
 ([atom-knot-mass-derivation §Architecture](#prop:atom-knot-mass-derivation)).
 The non-abelian Stokes theorem at finite slice depth gives a
 finite multiplicative integral; per-atom max slice depth equals
 the GB filtration* $\mathrm{max\_grade}$ *recorded in
 `joint-tower-sdp-h6-h9.witness.json`. Truncating the* $\Phi_q$
 *product at this depth reduces* $\Phi_q(0.989)$ *from* $6.7 \times 10^5$
 *to* $46.5$ *for* $\mathrm{max\_grade}=2$ *(D's filtration depth).*
 *Empirical test in*
 [`probe_phiq_yekutieli_truncation.py`](https://github.com/litlfred/qou/blob/claude/continue-pr-442-DJRWm/computations/probe_phiq_yekutieli_truncation.py):
 *the free-minus-atom subtraction* $E_0 \cdot (\mathrm{tower}^{\mathrm{free}}_{\leq k_{\max}} - \mathrm{tower}^{\mathrm{atom}}_{\leq k_{\max}})$
 *gives* $B(D) \approx +1.74 \mathrm{MeV}$ *(error* $-22\%$*) but
 fails for* $T$ *(deeper filtration* $k_{\max}=9$ *gives* $B(T) \approx 1449 \mathrm{MeV}$, *grossly off).*
```

```markdown
**Status ( PR [#638](https://github.com/litlfred/qou/pull/638)):**
Claim (b) is **refuted across six probed families** — scalar
uniform-$k$, scalar $\ell n_0 + k$, per-eigenvalue operator-valued,
multiplicity / Type-B-folded-crystal, pair-knot product-volume, and
pair-knot Markov-trace + full Frobenius Gram + LP/SDP duals — by
the conjecture's own $\sim 5\%$ falsifiability criterion. See
[`docs/audits/-brane-tower-n_star-closure-audit.md`](../../../docs/audits/-brane-tower-n_star-closure-audit.md)
for the consolidated landscape. Claim (a) (algebraic Cauchy-limit)
is **untouched** by the refutation; partial progress in
[`PhiQConvergence.lean`](../lean/QOU/MassEndomorphism/PhiQConvergence.lean)
(PR [#637](https://github.com/litlfred/qou/pull/637) +
[#639](https://github.com/litlfred/qou/pull/639)).
```

```markdown
**Implication for this conjecture's open path.** The brane-tower
contribution to the multi-term mass formula is **not** going to be
closed by a level-selection rule alone — the ${}^3\mathrm{He}$
residual survives every operator-volume convention probed, pointing
at a structural deficit of the brane-tower formula itself at the
$A=3$ / $n_0=9$ regime (positive LP-dual finding: pair-knot
operators $\sigma_{pp}/\sigma_{nn}$ ARE structurally selected at
magic shells; $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn})
= 0.0622$ exactly under Hoefsmit seminormal). The path forward is
either:
```

## explicit-central-idempotent.md

```markdown
> **Scope correction note.** Earlier versions of this
> proposition ranged the inner Lagrange product over cells of $\lambda$
> only (i.e., $\square \in \lambda$).  With that scope, the off-block
> projection does NOT vanish: the JM eigenvalue $q^{2c(T'(k))}$ for
> $T' \in \mathrm{SYT}(\mu \neq \lambda)$ may not lie in
> $\{c(\square; q) : \square \in \lambda\}$, so the Lagrange factor
> fails to kill that direction.  The corrected scope above ranges
> over $\mathrm{C}(n)$ (the union of contents across every $\mu$),
> which is exactly the candidate set of joint JM eigenvalues across
> all Wedderburn blocks.  Numerically verified to $\sim 10^{-50}$ in
> [`explicit-central-idempotent-probe.witness.json`](../../../computations/probes/explicit-central-idempotent-probe.witness.json):
> own-block residue $0$, off-block residue $0$, completeness
> residue $0$ under the corrected scope; literal-scope off-block
> residue $\approx 32$ at $q_0$ for $n = 3$.
```

## recomputed-low-isotope-mass-table-table4-data.md

```markdown
| Path | Time (5 atoms) | Precision floor |
|---|---:|---:|
| Canonical reducer (`markov_trace_recursive`, 50 dps mpmath) | ~30 s | $10^{-50}$ |
| Hybrid partition-sum (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$) | ~66 s | $10^{-14}$ (machine $\varepsilon$) |
| Full mpmath partition-sum | ~5–10 min | $10^{-50}$ |
| Pure float64 partition-sum (legacy) | ~1 s | $10^{-5}$ at $n = 9$ |
| Pure symbolic Wenzl + symbolic χ^λ | timeout (>4 min) | exact |

```

## qbeta-per-block-chi-closed-forms-proof.md

```markdown
- A closed form for $\Delta\tau_M(q) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(q)$.
  Why: the canonical Wenzl–Markov weights $y_\lambda(q)$ from
  `markov_weights_symbolic.solve_y_lambda(3)` involve $\sqrt q$ (via
  the Markov parameter $z = 1/(\sqrt q + 1/\sqrt q)$) and are NOT
  rational in $q$. A first version of this file attempted to prove
  a closed form for $\Delta\tau_M$ using an incorrect rational guess
  for $y_\lambda$; that version was retracted. The companion probe
  `qbeta_c3_multiblock_recursion_attack.py` does emit a Δτ_M closed
  form, but using a **non-canonical rational surrogate** for $y_\lambda$
  (marked in the script's docstring and witness JSON) — it is
  a NEAR-MATCH diagnostic, not a derivation. Proving the actual
  $\Delta\tau_M$ identity requires square-root handling beyond the
  `ring` tactic and is open.
- The empirical $c_3 \approx -2$ identity. Per the 1ppQ-Q$_\beta$
  ledger ([`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md)),
  $c_3 = -2$ is settled as a NEAR-MATCH with non-zero cross-anchor
  swing, NOT a Taylor-exact closure.
- The f-map identification. The Habiro element scaling map
  $f : \Delta\tau_M(\sqrt u) \mapsto \mathfrak{Q}_\beta(c_3 \text{ at } u^3)$
  remains the keystone of the 1ppQ closure.
```

## qou-motivic-galois-instance.md

```markdown
1. **Extraction**
   ([`computations/probes/habiro_frobenius_probe.py`](../../../computations/probes/habiro_frobenius_probe.py)).
   For each atom in
   `habiro-coefficients-atomic.witness.json` (proton, neutron,
   deuteron) and each prime $p \in \{2, 3, 5, 7, 11, 13\}$, evaluate
   $f$ at $u = \zeta_{2p}$. Witness:
   `habiro-frobenius-probe.witness.json` field `frob_p_complex`.
```

## phi-d-syt-count-conjecture.md

```markdown
Testing this is the next concrete R&D step: extend
`probe_per_wedderburn_block_ck.py` from n=3 to n=4 with the
canonical typed-B_4 braid recipe.
```

## rho-k-graded-expansion-table1-data.md

```markdown
| Probe | Mean \|err\| | Max \|err\| | Witness |
|:---|---:|---:|:---|
| Single-gen only ($\alpha \sum \ln\|V_i\|$) | $0.25\%$ | $0.35\%$ | `atomic-braid-mass-paper-formula` |
| + naive log-additive pair $\Sigma \ln\|V_i V_j\|$ | $9.0\%$ | $17.9\%$ | `rho-k-pair-gen-extension` |
| + Wedderburn-coupled pair $\Sigma \ln\|V_i V_j\|_{\mathrm{Wedd}}$ | $4.7\%$ | $8.9\%$ | `rho-k-pair-gen-v2-wedderburn` |

```

## recomputed-low-isotope-mass-table.md

```markdown
1. **Canonical Markov-axiom reducer** —
   [`markov_trace_recursive.markov_trace_of_word`](../../../computations/markov/markov_trace_recursive.py)
   at mpfr 50-dps; reference values stored in
   [`atomic-tr-m-mpfr-50dps.witness.json`](../../../computations/atomic-tr-m-mpfr-50dps.witness.json).
2. **Hybrid partition-sum** (this PR) — 30-dps sympy `Float`
   for $y_\lambda$ via Wenzl's Schur principal specialization,
   float64 for $\chi^\lambda_q$ via Hoefsmit seminormal matrices,
   per-`n` cache.  Module:
   [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../computations/wedderburn_jones_markov.py);
   driver: [`tr_m_q_hecke_seminormal.py`](../../../computations/tr_m_q_hecke_seminormal.py).
3. **Symbolic partition-sum** — full 50-dps mpmath via
   [`rho_k_h3a_refinement.py`](../../../computations/rho_k_h3a_refinement.py),
   the production path for binding-fraction $\Delta_\lambda$ analysis.
```

```markdown
with $\mathcal{B}_K = \mathtt{atom\_braid\_word\_3A}(Z, N) \in H_{3A}(q)$
the canonical 3A-strand atomic braid (β-decay-operator-unfolded form;
see [`mass_at_3A_proper.atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)),
$y_\lambda$ the canonical Wenzl Markov weight (see
[`prop:markov-trace-recursive-reducer`](markov-trace-recursive-reducer.md)),
$\chi^\lambda$ the Hoefsmit q-character of the atomic braid, and
$\Delta_\lambda(K)$ the per-Wedderburn-block binding fraction.
```

```markdown
Reference scripts:
[`atomic_mass_via_rho_k.py`](../../../computations/atomic_mass_via_rho_k.py)
(LO baseline, retained as reference);
[`binding_K_direct.py`](../../../computations/binding_K_direct.py)
(direct binding formulation; consumes $\Delta_\lambda$ from the
in-flight derivation race in PRs #602 / #603 / #613).
```

```markdown
The $+0.168\%$ / $+1.31$ keV residual is the **brane-tower
truncation correction** ([`neutron-qvalue-symbolic.md:110-114`](../particle-interactions/neutron-qvalue-symbolic.md)):
the derived $E_0 = m_e/(q_0(q_0-1))$ is the single-level
(Planck-tick) approximation; the exact tower-summed $E_0$ would
absorb this $0.17\%$. Closure path: Workplan 2 Phase 2 50-dps
$m_e^{\mathrm{Hecke}}$ lift.
```

```markdown
Witness:
[`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json)
( derived via
[`derived_masses.q_beta_predicted_mev`](../../../computations/derived_masses.py)).
3 assertions pass: residual $<0.5\%$, residual $<2$ keV,
single-wrap residual $<$ typed-crossings residual.
```

```markdown
The proton, neutron, and light-nucleus rest masses do **not** yet
have a FULL framework prediction wired. The LO form above is
tautological by construction (the $|\mathrm{tr}_M|$ factor cancels
exactly in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$,
so $\mathcal{M}^{\mathrm{LO}}_\text{pred} = Z m_p + N m_n$); the
Strategy-3 multi-term implementation in
[`atomic_braid_mass_table.py`](../../../computations/atomic_braid_mass_table.py)
has a known structural bug (multiplicative T1 base instead of
additive LP active-set, per its own deprecation banner lines 24-46).
Per owner directive, neither is the FULL framework
prediction — both should be replaced by the unified knot mass
formula $M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| +
\mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$ once the LP-dual
shadow-price closure ([`prop:operator-selection-lp`](operator-selection-lp.md))
or Phase 2 50-dps $m_e^{\mathrm{Hecke}}$ lift lands.
```

```markdown
The accessors
[`derived_masses.proton_mass_mev`](../../../computations/derived_masses.py)
and friends raise `NotImplementedError` with pointers to these
blockers; consumers must NOT fall back to the LO or Strategy-3 forms.
```

```markdown
**1. The 0.000 % on $p$ and $n$ is a calibration-discipline
violation, not a prediction.** The ρ_K leading-order ansatz used
in this table consumes $m_p$ and $m_n$ as CODATA inputs (via
[`computations/substrate/codata_constants.py`](../../../computations/substrate/codata_constants.py)),
so for $K = p$ ($Z = 1, N = 0$) and $K = n$ ($Z = 0, N = 1$)
the formula returns the input mass exactly. **This is a bug, not
a feature**: the QOU framework admits exactly three calibration
inputs ([three calibration inputs](three-calibration-inputs.md))
— CAL-1 $= m_e$, CAL-2 $= \mathfrak{D}_\beta$ (proxy $m_\mu/m_e$,
fixing $q_0$), CAL-3 $= \mathfrak{D}_\pi$ (proxy $m_\pi$, the meson
scale). The hadronic energy scale $E_0 = m_e/(q_0(q_0-1))$ is
**derived** from CAL-1 + CAL-2 (equivalently $E_0 = \mathfrak{Q}_\beta(n)/\lvert\Delta(\mathrm{net})\rvert$
via the CAL-2 proxy $\mathfrak{Q}_\beta$), not a calibration input. $m_p$ and $m_n$
are **predictions** of the framework, derivable as
$m_p = |\mathrm{tr}_M(p, q_0)| \cdot E_0$ and
$m_n = m_p + \mathfrak{Q}_\beta + m_e$ per the 3-input convention recommended
in [`neutron-gap-probes-round3.witness.json`](../../../computations/neutron-gap-probes-round3.witness.json).
The script-side migration is tracked as Workplan 0b
(see [`docs/audits/-1ppb-workplan-update.md`](../../../docs/audits/-1ppb-workplan-update.md));
until it lands, the $0.000\%$ rows above are tautologies and the
$D / T / {}^{3}\mathrm{He}$ residuals understate the true binding
prediction error by the n/p split scale ($\sim 0.14\%$).
```

```markdown
- $\rho_K^{\text{full}}(Z, N) = \rho_K^{\mathrm{LO}}(Z, N) + (1/|\mathrm{tr}_M|)
  \cdot \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda(K)$
  ([`rho_k_h3a_refinement.py`](../../../computations/rho_k_h3a_refinement.py)
  on  deuteron-only proof-of-concept; closure error
  $2.7 \times 10^{-48}$ MeV by construction).
- The per-block binding fractions $\Delta_\lambda(K)$ — currently
  determined by Occam's-razor minimal-perturbation selection
  (single dominant partition); the categorical derivation of
  $\Delta_\lambda$ from first principles is an open research
  question.
```

```markdown
The hybrid technique (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$,
with per-`n` cache) is the **recommended default** for
partition-sum consumers needing better than $10^{-5}$ agreement
without the overhead of full 50-dps mpmath.
```

```markdown
The atomic-shift exponent $\mathrm{shift}_{\mathrm{NF}}(\mathcal{B}_K)$
that controls the $u$-power in the $D(u)$ denominator
([`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md))
is now categorically verified for the proton by direct symbolic
Hoefsmit pole-order analysis
([`per_irrep_pole_proton_h3.py`](../../../computations/per_irrep_pole_proton_h3.py),
witness:
[`per-irrep-pole-proton-h3.witness.json`](../../../computations/per-irrep-pole-proton-h3.witness.json)):
```

```markdown
**Cross-confirmation:** the orthogonal computation in
[`shift_from_nf_basis.py`](../../../computations/shift_from_nf_basis.py)
(NF-basis decomposition, recorded in
[`shift-from-nf-basis.witness.json`](../../../computations/shift-from-nf-basis.witness.json))
independently reports `shift_proton_h3 = 19` — two independent
symbolic methods agree exactly on the per-proton u-pole.
```

```markdown
**Multi-nucleon verification (deuteron):**
[`per_irrep_pole_deuteron_h6.py`](../../../computations/per_irrep_pole_deuteron_h6.py)
(witness:
[`per-irrep-pole-deuteron-h6.witness.json`](../../../computations/per-irrep-pole-deuteron-h6.witness.json))
extends Path A to $A = 2$ via three optimisations: cached
symbolic $y_\lambda(q)$ for $n = 6$, auto-cached symbolic
$\chi^\lambda_q(\beta_D)$
([`chi-deuteron-h6.witness.json`](../../../computations/chi-deuteron-h6.witness.json)),
and per-term pole order. The per-term maximum is uniquely $40$
at $\lambda = (4, 1, 1)$, so
```

## chi-per-irrep-cyclotomic-closed-forms.md

```markdown
The full matrix product expansion + trace, followed by `sympy.cancel +
sympy.factor`, yields $-(q^4+1)(q^2-1)/(4q^3)$ — the closed form above.
The probe `probe_per_wedderburn_block_ck.py` performs this symbolic
computation; the witness file records the result bit-exactly.
```

```markdown
- **Cyclotomic Hecke algebras at depth $n$**: Ariki-Koike algebras and
  their representations carry cyclotomic structure tied to the
  parameters via $\Phi_d(q)$ factors. See e.g. Mathas, *Iwahori-Hecke
  Algebras and Schur Algebras of the Symmetric Group* (1999), §3 on
  Specht modules with cyclotomic decomposition.
- **Conjugate-partition character symmetry**: standard Hecke
  representation-theory fact; cf. Kassel, *Quantum Groups* (GTM 155)
  §V.5 on Iwahori-Hecke characters under partition conjugation.
- **Content sums and q-content invariants**: the
  q-content sum $c(\lambda)$ appears in the Hoefsmit seminormal-form
  axial distance formulae (Hoefsmit 1974 thesis); the relationship
  $\text{denominator exponent} \sim |c(\lambda)|$ for the character
  difference is a probe finding suggestive of a deeper
  hook-content-formula derivation.
```

```markdown
Probe `probe_per_wedderburn_block_ck.py` (witness:
`per-wedderburn-block-ck.witness.json`) computes the symbolic
$\chi_\lambda(\mathcal{B}_p), \chi_\lambda(\mathcal{B}_n)$ via the existing
`q_character_on_braid_word` infrastructure, applies `sympy.cancel +
sympy.factor`, and reports the three closed forms above plus all
$\varepsilon^k$ coefficients ($k = 0..12$) of the difference at
$q = 1 + \varepsilon$. The witness data backs every Lean closed-form
theorem in this module empirically.

```

## multi-link-jones-q1-extension.md

```markdown
**Empirically this fails**: at $q_0$ at 50 dps via
[`probe_q_beta_c5_c6_multilink.py`](../../computations/probe_q_beta_c5_c6_multilink.py),
```

```markdown
4. **A `MultiLinkJonesAtOne` class** with fields `c5_candidate`,
   `c6_candidate` for downstream consumers to plug in any specific
   candidate values they want to test. The default instance uses the
   probe's "best simple integer" candidates ($c_5 = +8$, $c_6 = 16$),
   **explicitly flagged as exploratory placeholders, not closure
   values**.
```

```markdown
## Concrete next probe
```

## rho-k-graded-expansion.md

```markdown
**Pair-coupling structure** (`wedderburn_pair_volumes.py`):
the Wedderburn-decomposed inner product
```

```markdown
**Empirical findings** (probes on $Z = 1..20$):
```

```markdown
- `rho-k-markov-multiplicativity.witness.json` — Wenzl branching identity verified to $3 \times 10^{-14}$.
- `rho-k-pair-gen-extension.witness.json` — pair-gen probe Z=1..20: naive log-additive degrades; documents open Wedderburn-coupling needed.
- `rho-k-scaling-structure.witness.json` — empirical LO-residual structural analysis.
- `atomic-braid-mass-paper-formula.witness.json` — single-gen accuracy across $Z=1..20$.
```

## markov-trace-recursive-reducer.md

```markdown
**Step 1 (Hecke-basis expansion).** Apply iterated Hecke quadratic
to expand
$\beta = \sum_{w \in S_n} c_w(q) \, T_w$
in the canonical basis. The
[`HeckeElement`](https://github.com/litlfred/qou/blob/main/computations/gb_filtration_jet_tracker.py)
class implements this symbolically over $\mathbb{Q}(q)$ via the
ascending/descending case split on Coxeter length.
```

```markdown
Numerical evaluation at $q_0$ for the canonical atomic-braid
words ([`markov_trace_axiomatic_multi_atom.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_axiomatic_multi_atom.py)):
```

```markdown
The deuteron's value matches $\operatorname{tr}_M(\text{proton})
\cdot \operatorname{tr}_M(\text{neutron})$ to mpmath-exact (50 dps)
precision, confirming the disjoint-product property.
```

```markdown
The proton value matches the prior Hecke-power expansion in
[`markov_trace_atomic_proton_full.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_atomic_proton_full.py)
([`prop:markov-trace-axiomatic-closed-form`](#prop:markov-trace-axiomatic-closed-form))
at 50-dps (mpmath) precision, providing an independent cross-check
via two different reduction strategies. (Earlier float64 evaluations
of the same identity are recorded in the witness as probes; the
matching claim is at 50 dps.)
```

```markdown
- [`computations/markov/markov_trace_recursive.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_recursive.py) — algorithm + H_3..H_6 unit tests.
- [`computations/markov/markov_trace_axiomatic_multi_atom.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_axiomatic_multi_atom.py) — proton/neutron/deuteron anchor + disjoint-product check.
```

## markov-trace-axiomatic-closed-form-interpretation.md

```markdown
Outstanding work towards full automation is captured in
[`markov-axiom-recursive-ascent`](#def:markov-axiom-recursive-ascent):
a recursive symbolic reducer for general $H_n$ words, currently
implemented in `markov_trace_recursive.py` with a known truncation
bug for $n \geq 4$ that does not affect the $H_3$ proton case.
```

## hecke-branching-trace-decomposition.md

```markdown
- The hypothesis $q^{1/2} + q^{-1/2} > 2$ is sharp for semisimplicity
  (Wenzl 1988, §1); below it, the Wedderburn decomposition fails and
  the $A^\lambda_{\mu,\nu}$ decomposition is not well-defined. The
  substrate value $q_0 > 1$ is comfortably inside the regime.
- Halverson–Ram 1998 give an explicit combinatorial Murnaghan–
  Nakayama-type rule for evaluating
  $\operatorname{tr}\,A^\lambda_{\mu,\nu}(I)$ when $I$ is a product
  of Murphy generators; this is the computational ingredient used by
  `probe_operator_valued_ansatze_from_mass_endo.py`.
- The same statement holds for any inclusion
  $H_{n_1}(q) \otimes \cdots \otimes H_{n_k}(q) \hookrightarrow
  H_{\sum n_i}(q)$ (iterate the branching).

```

## chi-v21-hoefsmit-matrix-derivation.md

```markdown
The character on the canonical 11-crossing typed-$\mathbf{B}_3$ braids
is `tr` of the matrix product. The probe `probe_per_wedderburn_block_ck.py`
symbolically computes (via `q_character_on_braid_word` + `sympy.cancel`):
```

```markdown
The probe data shows V_(2,1) ε^k coefficients grow polynomially
(`0, -1, 0.5, -2.5, 3.5, -5, 6.75, ...`). This follows from the
Laurent decomposition: at $q = 1 + \varepsilon$,
- $-q^3/4$ contributes a degree-3 polynomial in $\varepsilon$ (zero beyond $k=3$)
- $q/4$ contributes a linear polynomial (zero beyond $k=1$)
- $-q^{-1}/4$ and $q^{-3}/4$ contribute geometric series, growing
  polynomially in $k$ via $\binom{k+m-1}{m-1}$ binomial coefficients
  (where $m$ is the negative power)
```

```markdown
The scalar / rational-identity level closure here, combined with
sympy's symbolic verification in the probe, **establishes the
closed form empirically + structurally**; the missing piece is a
Lean-level proof tying the matrix-product to the rational form.
```

```markdown
theorem chi_v21_matrix_trace_identity (q : ℝ) (hq : q ≠ 0) :
    chi_v21_on_word q beta_n_word_v21
      - chi_v21_on_word q beta_p_word_v21
      = chi_V21_difference_factored q := by
  sorry  -- empirically verified via sympy in the probe
```
```

## tau-M-asymptotic-rep-theory-interpretation.md

```markdown
The rung coefficients are the $q$-Bessel power-series coefficients of the fibre
Habiro element $F$, obeying the proved first-order recurrence
$c_k(1-q^k)(1-q^{\nu+k}) = -q^{k-1}c_{k-1}$ (Lean:
`QOU.QBeta.qbessel_second_order_recurrence`, sorry-free). Four constructions in
Hecke representation theory describe this *same* expansion from complementary
angles; they are structural anchors, not independent numerical derivations — a
distinction an earlier four-anchor cross-check (archived probe
`_deprecated/probes/probe_tau_M_four_anchors.py`) blurred, as noted per
construction.
```

```markdown
The Jucys–Murphy elements $J_k \in Z(H_n(q))$ ($2 \leq k \leq n$) generate the
centre, with $J_k|_{V_\lambda^T} = q^{c_T(k)} - q^{-c_T(k)}\hbar_q$, $c_T(k)$ the
$q$-content of the cell holding $k$ in SYT $T$. For $V_{(2,1)}$ on $H_3$, $J_3$
has eigenvalues $\pm h$ ($h = q - q^{-1}$), so $p_1(J_3) = 0$ while
$p_2(J_3) = 2h^2$. Because $J_k$ is *diagonal* in the seminormal basis, it
produces the $\pm h$ eigenphase envelope but cannot, on its own, generate the
off-diagonal coupling $b$ that lives in $\sigma_1$; the JM data is therefore
**complementary** to the Kashiwara coupling, not an independent route to the
$N=1$ term. (The archived probe reported "$c_1^{\mathrm{JM}} = 0$" from
$p_1 = 0$ and mis-indexed the $O(\hbar_q^2)$ quantity
$p_2/2 = h^2 = (q+1)^2\hbar_q^2$ as a higher rung; both are artefacts of the
wrong index, not a disagreement with the Kashiwara value.)
```

```markdown
Macdonald polynomials $P_\lambda(x; q, t)$ interpolate between Schur ($t = q$),
Hall–Littlewood ($q = 0$), and zonal ($t = q^2$) specialisations. The $t = q^2$
point is the "second deformation parameter" absent from Form A, and the
$(q,t)$-inner-product expansion in powers of $(t/q^2 - 1)$ is the natural home
for the higher rungs. The normalisation must be taken with care: the bare zonal
norm $\langle P_\lambda, P_\lambda\rangle_{q,q^2}$ is an $O(1)$ quantity (for
$V_{(2,1)}$ it tends to $20/9$ as $q \to 1$, not to $1$), so a coefficient must
be read from a ratio that is $1 + O(\hbar_q^2)$, not from
$(\text{norm} - 1)/\hbar_q^2$. With the correct normalisation this anchor is
open; the archived probe's large candidate was the un-normalised artefact.
```

```markdown
Empirical verification per probe sequence:
1. [`probe_q_beta_per_irrep_cos.py`](../../../computations/probe_q_beta_per_irrep_cos.py) — $V_{(2,1)}$ character + KL decategorification.
2. [`probe_q_beta_three_irrep_closed_form.py`](../../../computations/probe_q_beta_three_irrep_closed_form.py) — 1-d closed forms (rep-theory triviality).
3. [`probe_q_beta_operator_valued_N1.py`](../../../computations/probe_q_beta_operator_valued_N1.py) — Kashiwara $\tilde f_1$ at $N=1$ (envelope coupling $b$).
4. [`probe_q_beta_operator_valued_N2.py`](../../../computations/probe_q_beta_operator_valued_N2.py) — second rung $(1 - b^2\hbar_q^4)$, $c_2 = -1$.

```

## q-hecke-seminormal-character-closure.md

```markdown
**Proposition (q-Hecke partition-sum closure).** *Let $\mathcal{B}_K$ be the
canonical atomic-braid word for atom $(Z, N)$ — i.e. the
$(c, d, \mathrm{gen\_idx})$ word produced by
[`atom_braid_word_3A`](../../../computations/mass_at_3A_proper.py)
($\mathcal{B}_p \cdot I \cdot \mathcal{B}_n$ with $I = \sigma_{n_1} - \frac{h}{2} \cdot 1$
the inter-nucleon interface). For each $\lambda \vdash 3A$ let
$\rho_\lambda^q$ be the Hoefsmit seminormal representation at $q$
([`hecke_characters.build_seminormal_matrices`](../../../computations/hecke/hecke_characters.py))
and let $y_\lambda(q)$ be the Jones-Markov weight via Wenzl's Schur
principal specialization
([`markov_weights_symbolic.solve_y_lambda`](../../../computations/markov/markov_weights_symbolic.py)).
Then the partition-sum form of the canonical Markov trace,*
```

```markdown
[`computations/tr_m_q_hecke_seminormal.py`](../../../computations/tr_m_q_hecke_seminormal.py)
produces
[`tr-m-q-hecke-seminormal.witness.json`](../../../computations/tr-m-q-hecke-seminormal.witness.json)
(10 / 10 assertions pass — five atoms $\times$ two tolerance bands at
$10^{-3}$ and $10^{-6}$):
```

```markdown
The numerical agreement is at **machine epsilon** for all five
atoms (hybrid precision: 30-dps sympy `Float` for $y_\lambda$ +
float64 for $\chi^\lambda_q$). 's
[`rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py)
implements the same closure with **mpmath at 50 dps**, achieving
$1.4 \times 10^{-16}$ on the deuteron (commit
[`c068550c`](https://github.com/litlfred/qou/commit/c068550c)).
```

```markdown
| Path | Module | Use case |
|---|---|---|
| Recursive Markov-axiom | [`markov_trace_recursive.markov_trace_of_word`](../../../computations/markov/markov_trace_recursive.py) | Production $\mathrm{tr}_M$ for mass-table predictions |
| Symbolic partition-sum (50-dps mpmath) | [`rho_k_h3a_refinement.py`](https://github.com/litlfred/qou/blob/claude/refactor-computation-framework-iCqhG/computations/rho_k_h3a_refinement.py) | Per-block $\rho_K$ binding-fraction $\Delta_\lambda$ analysis |
| Float64 partition-sum | [`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`](../../../computations/wedderburn_jones_markov.py) | Fast cross-check + reusable API |
```

## qbeta-per-block-chi-closed-forms.md

```markdown
- The probe computation:
  [`computations/qbeta/qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
  (witness `qbeta-c3-multiblock-recursion-attack.witness.json`).
- The pre-archimedean recursion for $z$: 
  [`computations/qbeta/qbeta_prearchimedean_z_recursion.py`](../../../computations/qbeta/qbeta_prearchimedean_z_recursion.py).
- The downstream c$_k$ conjectures:
  [`conj:qbeta-c-k-closed-forms`](#conj:qbeta-c-k-closed-forms)
  (axiomatised; conditional on the Habiro element identification).
- The 1ppQ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).

```

## markov-trace-antipode-polynomial-symmetry.md

```markdown
- `computations/poly_q_proof_probe.py` — sympy-exact verification.
- `computations/poly-q-proof.witness.json` — proof certificate.
```

## atomic-mass-gb-nf-interpretation.md

```markdown
**Empirical values** (from
`rho-k-codata-vs-six-term.witness.json`, evaluated at $q_0$ via
50-dps Markov trace of `markov_peel.tr_M_atomic`):
```

```markdown
where the $2^{2A+1}$ and $(1+u^2)^{3A-1}$ factors are proved
categorically but the per-nucleon shift exponents
($\mathrm{shift}_{\mathfrak{p}} = 20$,
$\mathrm{shift}_{\mathfrak{n}} = 16$ for `include_inter=False`) are
characterised only via integer-LP. The clean torus-knot limit
$\alpha_{\mathrm{shift}}(T_{p,k}) = k(p-1)$ on $V_{(1^p)}$ is proved
([torus-knot pole order](#prop:alpha-shift-torus-knot)) and powers
the multiplicative-chain identity for $\alpha_{EM}^{-1}$
([$\alpha_{EM}$ chain](#prop:alpha-em-shift-multiplicative-chain)),
but the atomic-braid case carries a strand-context-dependent profile
$(1, 4, 0, 0, 1, 0)$ for the per-crossing shift contributions whose
categorical origin is open. The atomic-shift coefficients
$(18, 21, 1)$ governing
[`prop:per-nucleon-shift-additive-linearity`](per-nucleon-shift-additive-linearity.md)
are now **categorically verified** for the proton and deuteron via
the symbolic Hoefsmit pole-order analysis in
[`per_irrep_pole_atom.py`](../../computations/per_irrep_pole_atom.py)
(witnesses
[`per-irrep-pole-proton-h3.witness.json`](../../computations/per-irrep-pole-proton-h3.witness.json)
+
[`per-irrep-pole-deuteron-h6.witness.json`](../../computations/per-irrep-pole-deuteron-h6.witness.json)),
closing the per-nucleon contribution to $\mathrm{shift}_{\mathrm{NF}}$
that controls the $u$-power in $D(u)$. Closing the strand-context
profile $(1, 4, 0, 0, 1, 0)$ remains open.
```

```markdown
**Negative result on the simple shift-anchor ansatz**
(`u-shift-mass-anchor-probe.witness.json`).
No combination of $\mathrm{shift}_{\mathfrak{p}}, \mathrm{shift}_{\mathfrak{n}}$
and the $q_0$-derived constants $(q_0, c_q, \hbar_q, z, [n]_q)$
reproduces both nucleon anchors to better than $11\%$. The closest
single-formula fit, $\mathrm{shift} \cdot q \cdot c_q^2 \approx 1835.4$,
matches $m_{\mathfrak{p}}/m_e$ to $0.04\%$ but fails for the neutron
($20\%$ error). The integer 4-unit shift differential ($20 \to 16$)
is structurally too coarse to encode the $0.14\%$ CODATA
$m_{\mathfrak{n}} - m_{\mathfrak{p}}$ splitting — the splitting
must be encoded in the per-irrep character data, not in the scalar
shift exponent alone.
```

## conj-qbeta-c-k-closed-forms.md

```markdown
The framework PROVES $c_3 = J_{\text{Hopf}}(q{=}1) = -2$ via the
2-strand sub-braid argument (Fact 3 of
[`prop:q-beta-c3-hopf-three-fold-markov`](#prop:q-beta-c3-hopf-three-fold-markov)).
The higher-rung coefficients $c_4, c_5, c_6, c_7$ have **empirical
closed forms** extracted from the SDP-$T_\beta$ framework (
[`computations/qbeta/qbeta_decay_sdp_full_ck.py`](../../computations/qbeta/qbeta_decay_sdp_full_ck.py))
with sub-percent residuals, but **no first-principles categorical
derivation is yet known**.
```

```markdown
Verified by `qbeta_decay_sdp_full_ck.py` (4 assertions pass).
```

## per-block-hopf-jones-absorption-pattern.md

```markdown
Verified at $q_0$ via
[`computations/qbeta/qbeta_per_block_paper_closed_forms.py`](../../computations/qbeta/qbeta_per_block_paper_closed_forms.py)
+
[`qbeta-per-block-paper-closed-forms.witness.json`](../../computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json).

```

## qbeta-delta-tau-surrogate-taylor-coefficients.md

```markdown
*Source: SymPy computation in
[`qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
(Step 2: Taylor expansion to 12 orders), serialised in
[`qbeta-c3-multiblock-recursion-attack.witness.json`](../../../computations/qbeta/qbeta-c3-multiblock-recursion-attack.witness.json)
under `taylor_coeffs_w_expansion`.*
```

```markdown
**Reliability of the witness values.** The SymPy script in
[`qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
applies `sp.series(... w, 0, 12)` to the closed form
```

## chi-v3-closed-form-proof.md

```markdown
Following the user direction "first prove formally V" + "V_3 ε^k
pattern" on the per-Wedderburn-block probe (#672), this block
delivers a **complete formal proof** of the V_(3) component:
```

```markdown
This matches the probe output `+1/4, -1/4, +1/4, ...` for $k = 6, 7, 8, ...$ exactly.
```

## markov-trace-axiomatic-closed-form-proof.md

```markdown
**Step 5: Substitution and simplification.** Substituting $h = q -
q^{-1}$ and $z = 1/(q^{1/2}+q^{-1/2})$ and clearing denominators
gives a rational function in $q^{1/2}$ with denominator
$q^{10}(q+1)^3$ (verified by `sp.cancel` in
`markov_trace_atomic_proton_full.py`).
```

```markdown
Substituting $q_0 = 1.109978595554181\ldots$ (50 dps) and evaluating with `mpmath`:
```

```markdown
- `computations/markov/markov_trace_atomic_proton_full.py` — full
  proton word $\sigma_1^7\sigma_2^4$ with `sp.cancel` rationalisation.
- `computations/markov/markov_trace_axiomatic_proton.py` — pedagogical
  $\sigma_1\sigma_2\sigma_1$ demonstration of the methodology.
- `computations/markov/markov_trace_recursive.py` — partial recursive
  reducer (see *Methodology generalisation* above).
```

