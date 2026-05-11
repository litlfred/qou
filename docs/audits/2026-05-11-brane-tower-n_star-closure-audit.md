# Brane-tower `n_⋆` closure audit (PR #638)

**Date:** 2026-05-11
**Branch:** `claude/close-level-selection-rule-bvMvw` ([PR #638](https://github.com/litlfred/qou/pull/638))
**Conjecture:** [`conj:brane-tower-z-habiro`](../../content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.md)
**Author:** Claude (autonomous session, user-directed)

This audit consolidates the five-way refutation of the brane-tower
`n_⋆` existence claim and the **positive structural finding** from
the operator-selection LP dual that the pair-knot composite
operators `σ_pp` / `σ_nn` are selected at magic-shell atoms — both
informing the surviving open question after the closure.

## What the conjecture asserts

`conj:brane-tower-z-habiro` has two independent claims:

1. **Algebraic Cauchy-limit:** the partial brane-tower sums
   $\widetilde{\Phi}^{(N)}(\beta) = \sum_{i=1}^{N}
   \mathrm{Trunc}_{<n}[\Phi_q(\hat V_i)]$ form a Cauchy sequence in
   the $z$-Habiro topology and converge to an algebraic element
   $\widetilde{\Phi}_q^{\mathrm{tower}}(\beta) \in
   \widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$.
2. **Substrate-derived `n_⋆` existence:** there exists a canonical
   level-selection rule `n_⋆ : 𝔥 ↦ ℕ_{≥ 1}` derivable from QOU
   substrate data alone such that the cyclotomic projection
   $\pi_{n_⋆}^{(z)}(\widetilde{\Phi}_q^{\mathrm{tower}}(\beta_𝔥))$
   recovers the empirical brane-tower contribution uniformly across
   atoms (no per-atom retuning).

The conjecture's own falsifiability criterion (`brane-tower-z-habiro.md`
§"Falsifiability"): a candidate rule must close all three AME light
isotopes $\{D, T, ^3\mathrm{He}\}$ to within $\sim 5\%$.  We adopt a
$10\%$ working bound to be robust against rounding.

## Probe families tested (chronological)

| # | Family | Best case | Worst-atom max abs err | Verdict |
|:-:|:---|:---|:---|:---:|
| 1 | Scalar uniform `k` | $k=2$ subtractive | $+134\%$ (³He) | refuted |
| 2 | Scalar $\ell \cdot n_0 + k$ | $(14, 27, 20)$ | $\sim 10^7\%$ (³He) | refuted |
| 3 | Per-eigenvalue operator-valued | $k=1$ uniform | $64.75\%$ (T) | refuted |
| 4 | Multiplicity / Type-B-fold | R2 mult-trunc op | $55.97\%$ (³He) | refuted |
| 5 | Pair-knot product-volume | $\{Z=2, N=2\}$ collapse | $1056.9\%$ (T)$^\ast$ | refuted |
| 6 | Pair-knot Markov-trace + full Gram + SDP | $n_\star$ from family 4 | $996.6\%$ (T) | refuted |

$^\ast$ Note: ⁴He under family 5 lands at $-19.43\%$ — the closest
closure across all probes — but D, T, ³He are far off; non-uniform.

Each row is recorded as an explicit refutation theorem in
[`brane-tower-z-habiro.lean`](../../content/quantum-observable-universe/braids-and-knots/brane-tower-z-habiro.lean)
discharged by `norm_num` from the witness data.  The combined
five-way conjunction is `nStar_all_probed_forms_refuted`.

### Witness inventory

| Witness | Computes | Engine |
|:---|:---|:---|
| [`probe-phiq-uniform-k.witness.json`](../../folio-assistant/computations/probe-phiq-uniform-k.witness.json) | family 1 (uniform `k` sweep) | scipy |
| [`probe-phiq-n-star-rule.witness.json`](../../folio-assistant/computations/probe-phiq-n-star-rule.witness.json) | family 2 ($\ell n_0 + k$) | scipy |
| [`probe-phiq-operator-valued.witness.json`](../../folio-assistant/computations/probe-phiq-operator-valued.witness.json) | family 3 (per-eigenvalue), persists eigenvalue spectra | numpy + Hoefsmit |
| [`probe-phiq-avg-chi-over-classical-dim.witness.json`](../../folio-assistant/computations/probe-phiq-avg-chi-over-classical-dim.witness.json) | family 3 historical Wedderburn-block-average variant (audit only) | numpy |
| [`probe-phiq-multiplicity-refined.witness.json`](../../folio-assistant/computations/probe-phiq-multiplicity-refined.witness.json) | family 4 (R1–R4 rules in both scalar and operator-valued) | numpy |
| [`probe-phiq-pair-knot-magic-shell.witness.json`](../../folio-assistant/computations/probe-phiq-pair-knot-magic-shell.witness.json) | family 5 (pair-knot product-volume + operator-selection LP dual, diagonal Gram) | scipy linprog |
| [`probe-phiq-pair-knot-markov-trace.witness.json`](../../folio-assistant/computations/probe-phiq-pair-knot-markov-trace.witness.json) | family 5 refinement (Markov-trace composite + full Frobenius Gram + LP **and** SDP duals) | scipy + cvxpy/SCS |

## Positive structural finding from the LP/SDP dual

While the level-selection existence claim is refuted across all five
probed families, the **operator-selection LP dual** per
[`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md)
and CLAUDE.md "LP / SDP duals — first-class infra" produces a
structural finding worth recording:

> **Pair-knot composite operators $\sigma_{pp}$ / $\sigma_{nn}$ are
> in the active set EXACTLY when the atom has the corresponding
> magic shell.** Strong duality holds (gap $\leq$ numerical
> precision) for every atom; the dual active set is non-trivial:

| Atom | Magic shells | LP-dual active set | Pair-knot active? |
|:-:|:-:|:-:|:-:|
| D | none | $\{\sigma_0, \sigma_1, \sigma_3, \sigma_4\}$ | absent (no shell) |
| T | $N{=}2$ | $\{\sigma_0, \sigma_1, \sigma_2, \sigma_3, \sigma_4, \sigma_6, \sigma_7, \sigma_{nn}\}$ | $\sigma_{nn}$ active |
| ³He | $Z{=}2$ | $\{\sigma_0, \sigma_1, \sigma_2, \sigma_3, \sigma_4, \sigma_6, \sigma_7, \sigma_{pp}\}$ | $\sigma_{pp}$ active |
| ⁴He | $Z{=}2{+}N{=}2$ | full basis $\cup \{\sigma_{pp}, \sigma_{nn}\}$ | both active |

This is the operator-level signature of $Z=2$ / $N=2$ closed-shell
structure in the substrate algebra: pair-knot composites are
structurally distinguishable from per-generator operators precisely
at magic configurations.

The Lean form is `lpDualActiveSetIncludesPairKnotAtMagicShells :
Prop := True` — a boolean record consumed by audit tooling; the
substantive content lives in the witness data.

## Surviving open paths

The closure refutes every probed `n_⋆` family but **does not refute
the conjecture in full**: two open paths remain.

### Open path 1 — algebraic Cauchy-limit half

Claim 1 of the conjecture (Cauchy-sequence convergence in the
$z$-Habiro topology) is untouched by the witnesses, which test only
the level-selection existence claim 2.  A direct algebraic proof
proceeds via the cyclotomic projections $\pi_n^{(z)}$ on the
[$z$-Habiro ring](../../content/quantum-observable-universe/braids-and-knots/z-habiro-ring.md);
this is independent of `n_⋆`.

PR #637 (merged to main as `a267f86d`) added
[`PhiQConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean)
which makes substantive progress on this path (Lean structure for
Φ_q convergence).  My refutation is complementary: it closes the
$n_⋆$ existence claim at the level of empirical witness data; their
work closes the algebraic Cauchy-limit claim at the Lean structural
level.  No contradiction.

### Open path 2 — ³He structural gap (real, audited)

The ³He binding gap survives every probed `n_⋆` rule.  Under the
best probed combination (R2 mult-truncated operator-valued at
$n_⋆^{³\mathrm{He}} = 1$), ³He's residual is $-55.97\%$.  Under
pair-knot product-volume collapse ($\sigma_{pp}$ as single
composite), ³He is at $+218.7\%$; ⁴He at $-19.4\%$.

**Markov-trace audit (B.1, 2026-05-11):**
[`probe_tr_m_he3_audit.py`](../../folio-assistant/computations/probe_tr_m_he3_audit.py)
([witness](../../folio-assistant/computations/tr-m-he3-audit.witness.json))
cross-checked $|\mathrm{tr}_M(\beta)|$ for $\{D, T, ^3\mathrm{He}\}$
via two independent canonical paths:

- **Path 1 (Hoefsmit seminormal + Wedderburn sum):** the path used
  in all six PR #638 probe families.
- **Path 2 (Markov-axiom recursive ascent):**
  `markov_peel.tr_M_atomic` — Gröbner-Shirshov reduction in
  $H_n(q)$ then peel the top generator at 30 dps symbolic.

Results:

| Atom | Hoefsmit (float64) | Markov-peel (symbolic 30dps) | $|\Delta|$ |
|:-:|---:|---:|---:|
| D | $0.3882864713$ | $0.3882864715$ | $2.6 \times 10^{-10}$ |
| T | $0.1040539888$ | $0.1040521187$ | $1.9 \times 10^{-6}$ |
| ³He | $0.2065441289$ | $0.2065408586$ | $3.3 \times 10^{-6}$ |

**Conclusion: the ³He structural gap is REAL.** The two canonical
paths agree on ³He at $1.6 \times 10^{-5}$ relative precision —
well within the $\sim 55\%$ binding-formula residual.  No
Markov-trace mis-count can account for the gap.

**Side-finding (precision):** $n = 9$ Hoefsmit seminormal in float64
introduces $\sim 1.5 \times 10^{-5}$ relative error vs the symbolic
50dps Markov-peel.  This is irrelevant for the structural-gap
analysis (the gap is $\sim 10^4 \times$ larger than the precision
floor) but matters for downstream $1$ ppb mass-prediction work — see
[PR #640](https://github.com/litlfred/qou/pull/640) for 50dps
neutron-mass chain.  The brane-tower probes in PR #638 should be
re-run at mpmath 50dps if quantitative claims at the $10^{-5}$
relative level become needed; the current $\sim 10\%$
falsifiability bound is unaffected.

**Cyclotomic-locus check (C.1, 2026-05-11):** $q_0 \approx 1.110$ is
real and not near any cyclotomic locus $q^k = 1$ (only $q = 1$ is on
$\mathbb{R}$; distance $0.11$ away).  The Hecke algebra $H_9(q_0)$
is fully semisimple at $q_0$ since $[n]_{q_0} > 0$ for all $n \leq
9$.  The ³He gap is therefore **not** a cyclotomic-degeneracy
artifact; the structural deficit is in the brane-tower formula
itself, not the substrate algebra.

### What the LP-dual evidence points at next

The LP-dual evidence suggests the right refinement: replace the
simple product-volume convention $|\hat V_{\text{shell}}| =
\prod_{i} |\hat V_i|$ by the actual Markov trace
$\mathrm{tr}_M(\sigma_{i_1} \cdots \sigma_{i_k})$ of the shell
sub-braid as a single Hecke element via Hoefsmit seminormal.  The
diagonal Frobenius Gram approximation $G_{ij} = \delta_{ij}
|\hat V_i|^2$ used in family 5 would then be replaced by the full
$G_{ij} = \mathrm{tr}_M(\sigma_i \sigma_j)$.

The Markov-trace refinement was implemented in
[`probe_phiq_pair_knot_markov_trace.py`](../../folio-assistant/computations/probe_phiq_pair_knot_markov_trace.py)
([witness](../../folio-assistant/computations/probe-phiq-pair-knot-markov-trace.witness.json));
**also refuted**:

| Atom | Markov-trace tower at $n_\star$ | $B_{\text{pred}}$ MeV | $B_{\text{AME}}$ MeV | err |
|:-:|---:|---:|---:|---:|
| D ($n_\star{=}1$) | $31.07$ | $17.71$ | $2.225$ | $+696\%$ |
| T ($n_\star{=}2$) | $88.36$ | $93.01$ | $8.482$ | $+997\%$ |
| ³He ($n_\star{=}1$) | $16.46$ | $19.64$ | $7.718$ | $+154\%$ |

Strong duality verified via BOTH LP (gap $< 10^{-15}$) and SDP
(gap $< 10^{-6}$, cvxpy / SCS) at the **full Frobenius Gram**
$G_{ij} = \mathrm{tr}_M(\sigma_i \sigma_j)$ for $i, j$ ranging over
the generator basis (pair-knot composite diagonal $G_{pp,pp} = t_{pp}^2$
as a partial extension).

### Z=2 / N=2 symmetry IS restored at the Markov-trace level

Notable structural finding: $\mathrm{tr}_M(\sigma_{pp}) = \mathrm{tr}_M(\sigma_{nn}) = 0.0622$ **exactly**.

This is the operator-level $Z \leftrightarrow N$ isospin symmetry the
LP-dual was pointing at.  The $1.326\times$ ratio asymmetry seen in
family 5's $\Delta_{\text{shell}}$ calibration was an artifact of
the product-volume convention $|\hat V_{\text{shell}}| =
\prod_{i} |\hat V_i|$ — the actual Markov-trace value is identical
for both magic shells because the two shell sub-braids are
isomorphic Hecke elements (4 intra-strand generators with identical
algebraic structure under the Hecke quadratic relation).

The symmetry restoration is a positive structural finding worth
recording even though the closure attempt failed.

### Structural conclusion

The brane-tower formula's `Φ_q`-truncated tower at any pair-knot
operator-volume convention (product, geometric mean, or canonical
Markov trace) produces inflated values at small $n_\star$ regardless
of the choice.  The ³He gap is therefore **not** an operator-volume
issue — the brane-tower formula itself has a structural deficit at
the AME light-isotope scale.

### Open path 3 — Z=2 / N=2 magic-shell symmetry

Family 5 also extracted magic-shell corrections from ³He and ⁴He
residuals:
- $\Delta_{\text{shell}}(Z{=}2)$ from ³He: $-16.88$ MeV
- $\Delta_{\text{shell}}(N{=}2)$ from ⁴He: $+22.38$ MeV

The corrections have **opposite signs** and differ by $1.326\times$
in magnitude — Z=2 / N=2 symmetry fails under the simple
product-volume convention.  Whether the Markov-trace refinement
restores the symmetry is one of the assertions of the family-5
refinement probe.

## Status of the surviving open paths (D-phase scoping, 2026-05-11)

### D.1 — Algebraic Cauchy-limit half (open, in flight on #639)

PR [#639](https://github.com/litlfred/qou/pull/639) is actively
closing sorries in
[`PhiQConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean)
— `summable_q_inv_geometric` and `quantumDilog_factors_nonzero` are
both being closed in that PR. Their work is the direct path forward
on Claim 1 of `conj:brane-tower-z-habiro`. Coordination intent
posted [on #639](https://github.com/litlfred/qou/pull/639#issuecomment-4423678285);
my refutation theorems will integrate with the
`RecoversWithRelativeError` predicate after #639 merges (Phase B.3).

### D.2 — Other AME isotopes (scoping, deferred to follow-up)

Available chi caches in `folio-assistant/computations/`:
`chi-proton-h3`, `chi-neutron-h3`, `chi-deuteron-h6`,
`chi-tritium-h9`, `chi-helium-3-h9`, `chi-helium-4-h12` (the last
uses a DEPRECATED disjoint-word convention; the canonical
`atom_braid_word_3A(2,2)` is computed in this session via
`markov_peel.tr_M_atomic` — see Phase B.2).

Extension to A ≥ 5 isotopes (⁵Li at n=15, ⁶Li at n=18, ⁷Li at
n=21, ⁹Be at n=27, ¹²C at n=36) is **heavy compute**: Hoefsmit
seminormal at n=15 already has partition count ~176 with dims up
to ~30000+; the recursive markov_peel path scales better but still
~hours per atom symbolically. **Deferred to a follow-up PR**; not
required for the level-selection closure (the AME light-isotope
sample {D, T, ³He, ⁴He} suffices for the refutation across six
families).


1. **Ship the closure as-is.**  The five-way refutation + LP-dual
   structural finding is a substantive result independent of the
   Markov-trace refinement outcome.  The block kind stays
   `conjecture`; the surviving open paths are clearly delineated.

2. **Integrate with `BraneTowerNStar.lean` on main.**  Commit
   `a267f86d` (PR #637) added a substantive `RecoversWithRelativeError`
   predicate.  My refutation theorems can be rephrased in terms of
   that predicate: "no `n_⋆` produces a
   `RecoversWithRelativeError 0.10 B_AME` instance uniformly across
   the AME light-isotope sample".  This integration is the cleanest
   way to surface the closure in the Lean structural layer.

3. **Open-path follow-up: Markov-trace pair-knot + full SDP.**
   If the Markov-trace refinement closes ³He / ⁴He, the conjecture's
   level-selection claim is RESTORED (with a refined operator-volume
   convention).  If it does not, the structural blocker is deeper
   than operator-volume choice and points at the brane-tower formula
   itself (Markov trace + magic-shell correction term as separate
   contributions).

4. **Update `mass-endomorphism-conjecture` framing.**  The parent
   conjecture explicitly cites brane-tower-z-habiro as the closure
   path.  Now that the level-selection claim is refuted, the parent
   conjecture's open-path pointer should reference the surviving
   algebraic Cauchy-limit and ³He-structural-gap branches instead.

## Coordination

- [#637](https://github.com/litlfred/qou/pull/637) "FULL Q_β
  prediction + non-calibrated mass framework cleanup" merged
  `a267f86d` adding `BraneTowerNStar.lean` (substantive Lean
  predicate); coordinated via the consolidated comment on PR #638.
- [#636](https://github.com/litlfred/qou/pull/636) Plancherel audit
  merged `c5617390`; no overlap with brane-tower files.
- Gemini code-review on PR #638 acknowledged "no further comments"
  after the consolidated 12-thread response in
  [`00292059`](https://github.com/litlfred/qou/commit/00292059).
- Copilot code-review fully addressed in the same response.

## Provenance

| Phase | Commit | Adds |
|:-:|:-:|:---|
| Scalar closure | [`d757bc69`](https://github.com/litlfred/qou/commit/d757bc69) | Families 1, 2 refutation theorems + first witnesses |
| Op-valued + review fixes | [`e2204a4a`](https://github.com/litlfred/qou/commit/e2204a4a) + [`00292059`](https://github.com/litlfred/qou/commit/00292059) | Family 3 refutation + review-batch response |
| Multiplicity / Type-B-fold | [`8efb07e7`](https://github.com/litlfred/qou/commit/8efb07e7) | Family 4 refutation + crystal-basis research integration |
| Pair-knot magic-shell | [`9ac5148c`](https://github.com/litlfred/qou/commit/9ac5148c) | Family 5 (product-volume) refutation + LP-dual structural finding |
| Markov-trace refinement + SDP + this audit | _(commits land after the Markov-trace probe completes)_ | Family-5 refinement + full Gram + SDP dual + this audit |
