# Canonicalization Review — Path to 1 ppb (Audit 2026-04-27)

**Branch:** `claude/knot-volumes-review-Pgt8o`
**Status:** review only — no code changes; queues two follow-up branches.
**Owner directive:** *"I only want canonical, no more empirical/fitted."*
**Goal:** total residual error ≤ 1 ppb against AME 2020.

---

## TL;DR

The seven named "empirical / fitted" constants in the pipeline are largely
**symptoms of two structural fixes**, not seven independent problems.

1. **Volume → trace.** Replace `B = ρ · m_e · Vol_hyp(K)` with the six-term
   curvature-rank decomposition of the Markov trace `tr_M(T_w)` evaluated
   directly on the GB normal form. SnapPy hyperbolic volume becomes a
   downstream sanity check, not a primary mass input.
2. **2-term blend → 3-term Wedderburn.** Add the chirality channel
   ($H_A^2 \Phi_3$) that the symmetrised 2-term blend drops. This
   eliminates `α* ≈ 0.305807` and `α₄ ≈ 0.8272` as free parameters.

The R5-full SDP-as-solver (replacing historical knot guesses with derived
canonical $T_w$) is a downstream improvement, not a precondition for
either fix above.

---

## 1. Current state — empirical residuals

| Atom | Family | err (ppb)        |
|------|:------:|-----------------:|
| ²H   | 1      | +10.9 M          |
| ³H   | 1      | −1.56 M          |
| ³He  | 1      | −29.7 M          |
| ⁴He  | 2      | +58.7 M          |
| ⁸Be  | 3      | +103.4 M         |
| ¹²C  | 3      | +54.1 M          |
| ¹⁶O  | 3      | +53.0 M          |
| ²⁴Mg | 3      | +90.2 M          |
| ⁴⁰Ca | 3      | +195.1 M         |
| ⁶Li, ⁷Li | 4 (quarantined) | n/a |

Units: `M` = million ppb (10⁶ ppb), i.e. `+10.9 M` ≈ +10.9 × 10⁶ ppb ≈ 1.09 %.

Source: [`mass-table-ppb.witness.json`](../computations/mass-table-ppb.witness.json).
Numerical precision is not the bottleneck — `q₀` is CODATA-bounded at
σ/q ≈ 1.22 × 10⁻⁹, already 1-ppb-class. **All residual is structural-formula
incompleteness.**

---

## 2. The canonical structure (the part the empirical surface obscures)

### 2.1 Mass tower = six-term curvature-rank decomposition

The "mass tower" is **not** an atom-by-atom recursion. It is the
six-term spectral-sequence decomposition of a *single* braid's Markov
trace, stratified by GB filtration depth (curvature-rank) — see
[`six-term-mass-formula-complete.md`](../content/quantum-observable-universe/braids-and-knots/six-term-mass-formula-complete.md):

$$
\mathfrak{m}(\varrho) =
  |\mathrm{tr}_M(T_w)| +
  \sum_i \Phi_q(|\hat V_i|) +
  z^2 \sum_{i<j} \Phi_q(|\hat V_i \hat V_j|) +
  m_e \tau(C) +
  a_K \mathcal{C}_K +
  \sum_{\ell \geq 2} \frac{\mathrm{Res}_{q = \zeta_\ell}[\,\cdot\,]}{q_0 - \zeta_\ell}
$$

| Term | Curvature-rank | Provenance                                    |
|:----:|:--------------:|-----------------------------------------------|
| 1    | 0              | descended Markov / abelian holonomy           |
| 2    | 1              | single-generator brane towers                 |
| 3    | 2              | pair-generator brane towers (Markov param $z$)|
| 4    | universal      | Frobenius co-Casimir                          |
| 5    | ≥ 2            | chirality via Wedderburn-symmetric duality    |
| 6    | ≥ 3            | higher residues (Mittag-Leffler)              |

### 2.2 Ideal-theoretic stratification

The Hecke rewrite ideal
$I = \langle\,\sigma_i^2 - (q-q^{-1})\sigma_i - 1,\ \sigma_i\sigma_{i+1}\sigma_i - \sigma_{i+1}\sigma_i\sigma_{i+1}\,\rangle$
defines the GB filtration $J^\ell(q) = \pi(I^\ell)$ — the elements that
require at least $\ell$ rewrites to reach Gröbner–Shirshov normal form.
Hyperbolic-knot braids ($4_1$, $5_2$, $6_1$, $6_2$, $6_3$, $7_2$–$7_7$,
…) appear as **sub-words** in the atomic GB reduction, each pinned to a
specific (depth, jet, Wedderburn channel) cell — see
[`curvature-rank-gb-stratification.md`](../content/quantum-observable-universe/braids-and-knots/curvature-rank-gb-stratification.md).

The neutron's extra **6₁ knot at (depth 3, jet 1, std channel)** is the
canonical algebraic origin of p/n mass splitting. *That* is the kind
of structure a canonical mass derivation consumes — sub-ideal pattern,
not ambient hyperbolic volume.

### 2.3 What's wired

[`computations/joint-tower-sdp-rust.witness.json`](../computations/joint-tower-sdp-rust.witness.json)
contains, for 7 particles (quark, electron, proton, neutron, D, T, ³He),
the full GB-NF data:

| Particle | `max_grade` | Filtration shape (terms per grade)    | Wedderburn blocks |
|---------:|:-----------:|---------------------------------------|:-----------------:|
| D        | 2           | {0: 1, 1: 2, 2: 2}                    | 3                 |
| T        | 9           | {0–9: 1, 3, 6, 10, 13, 14, 11, 7, 4, 1} | 7               |
| ³He      | 2           | {0: 1, 1: 2, 2: 2}                    | 3                 |

³He's partition-[3] Wedderburn block eigenvalue is exactly **1.0000**
(PSD-saturated, α* = 1) — a clean canonical signal.
**`b_pred_mev` is `null` for all three** — the certificate exists, but
the six-term formula consumer that turns it into a mass prediction has
not been wired.

### 2.4 What's not wired

| Component                                  | Status |
|--------------------------------------------|:------:|
| GB-NF reducer (R2)                         | ✅      |
| Wedderburn-block PSD evaluator (R3)        | ✅      |
| Cross-level LR embedding (R4)              | ✅      |
| PSD-cone α* bisection verifier (R5-min)    | ✅      |
| Clarabel SDP, $H_3$–$H_8$ at $L=2$ (R5-full)| ✅ (was self-inflicted svec bug, fixed `807a3af`) |
| `hp_volume@50dps` Markov-closure helper    | ✅      |
| **Six-term formula consumer**              | ❌ — none of the existing scripts read filtration cert + Wedderburn blocks → produce `b_pred_mev` |
| **3-term Wedderburn (chirality channel)**  | ❌ — `alpha_blend_tower.py` uses 2-term blend, hides chirality in α* |
| **R5.6 Wedderburn-block SDP decomposition**| ❌ — needed for $H_{18}$+ (⁶Li/⁷Li/Family 3 unknown $T_w$) |
| **R5-full SDP-as-solver** (registry mode)  | ❌ — current binary verifies historical guesses; does not derive canonical $T_w$ |

---

## 3. The empirical surface (7 constants → 2 root causes)

| # | Constant                       | Family    | Root cause     | Eliminated by |
|---|--------------------------------|-----------|----------------|---------------|
| 1 | `α* ≈ 0.305807` (Frobenius-antipode blend)   | universal | 2-term blend drops chirality | Fix 2 |
| 2 | `c_αα = m_e · Vol(7²₁)`                      | 3         | volume-as-input              | Fix 1 |
| 3 | `Vol(6₂)`, `Vol(8₁₁)`, `Vol(L6a4)`           | 1         | volume-as-input              | Fix 1 |
| 4 | `Vol(K11a259)`, `Vol(L11a62)`, `ρ=5`         | 4         | volume-as-input + R5.6 gap   | Fix 1 + R5.6 |
| 5 | `α₄ ≈ 0.8272` (n→p transition)               | universal | 2-term blend drops chirality | Fix 2 |
| 6 | per-isotope `(α, r)` ladder fits             | 1–3       | residual patches             | redundant once 1+2 land |
| 7 | `E_0 = 0.782 MeV` (β-decay Q)                | universal | = CODATA `m_n − m_p − m_e`   | label as fibre-functor input (not "empirical") |

### 3.1 Why `α*` is not closed-form

PSLQ at 25 digits over $\{1, G, \pi, 1/\pi, q_0, \hbar_q\}$ with
`maxcoeff = 10⁶` **falsifies** $\alpha^* = G/3$ (and every q-deformed
candidate). The reason is structural, not numerical: `α*` lives in the
S-even subspace of the symmetrised blend, while chirality is
S-anti-invariant and vanishes under Frobenius symmetrisation. `α*` is
absorbing what the **chirality term $H_A^2 \Phi_3$** should contribute
in the full 3-term Wedderburn formula — see
[`alpha_blend_tower.py:151–193`](../computations/alpha/alpha_blend_tower.py).

There is no closed form for `α*` in the 2-term frame because the
quantity it patches is structurally outside that frame.

### 3.2 Family 1 D/T/³He are *not* a numerical-precision issue

The volumes 4.4008 / 8.2863 / 7.3277 are correct hyperbolic constants
(Vol(6₂), Vol(8₁₁), Vol(L6a4) = 8G). The methodology is tagged
`manual-historical-volume-match` because:

- D's true Markov trace from `[1,-2,1,1,1,-2]` does **not** equal the
  Jones polynomial of $6_2$; the AME match is approximate.
- D's GB-NF actually contains named sub-patterns: trefoil (length 3) +
  Hopf link (length 2) + electron bridge (length 3) — see
  [`d-nf-knot-operators.md`](../content/quantum-observable-universe/braids-and-knots/d-nf-knot-operators.md).
- The canonical formula consumes that structure via the six-term
  decomposition. `Vol(6₂) · m_e` is a coarse approximation of the
  rank-1 term *only*.

---

## 4. Recommended sequenced plan

### Sprint A — canonical mass for Family 1 (this branch's follow-up)

**A1.** Implement the six-term formula consumer that reads
[`joint-tower-sdp-rust.witness.json`](../computations/joint-tower-sdp-rust.witness.json)
per-atom certificates and produces `b_pred_mev` from `filtration_certificate.by_grade`
+ `wedderburn_blocks` directly. **No SnapPy volumes anywhere in the path.**

**A2.** Run on D/T/³He; report ppb residuals against AME. This becomes
the new baseline for Family 1.

**A3.** Update [`recursive-atom-knot-atlas.md`](../content/quantum-observable-universe/braids-and-knots/recursive-atom-knot-atlas.md):
flip Family 1 methodology tag from `manual-historical-volume-match` to
`canonical-six-term-from-gb-nf`, with the sub-ideal pattern (trefoil +
Hopf + electron bridge for D, etc.) documented per atom.

**Eliminates constants:** #3 (Family 1 volumes).
**Effort:** ~1 day. **Pure consumption** — every input already lives in
the witness.

### Sprint B — 3-term Wedderburn upgrade

**B1.** Reformulate `alpha_blend_tower.py` to include the chirality
channel $H_A^2 \Phi_3$. Reference the antipode-Frobenius symmetrisation
analysis in
[`chirality-from-frobenius-self-pairing.md`](../content/quantum-observable-universe/braids-and-knots/chirality-from-frobenius-self-pairing.md).

**B2.** Rerun neutron / proton mass derivation; α* and α₄ should be
either closed-form expressions in `q₀` or removed entirely from the
blend.

**B3.** Update content blocks to remove the phenomenological framing of
α* and document the 3-term derivation.

**Eliminates constants:** #1 (α*), #5 (α₄).
**Effort:** ~half-day theory + half-day code. Depends on A1 if Family 1
ppb is to be re-checked under the new chirality term.

### Sprint C — α-cluster Family 3 (⁸Be–⁴⁰Ca) canonical

**C1.** Replace the empirical `c_αα = m_e · Vol(7²₁)` constant with the
six-term formula applied to the JSJ-decomposed α-cluster atom. The
`prop:atom-knot-mass-derivation` α-cluster recursion already lives in
the content layer; the consumer needs extending past Family 1.

**Eliminates constants:** #2 (c_αα).
**Effort:** ~2 days; depends on A1.

### Sprint D — R5.6 Wedderburn-block SDP decomposition + Family 4

**D1.** Implement Wedderburn-block decomposition in the R5-full SDP
solver to make $H_{18}$ (⁶Li) and $H_{21}$ (⁷Li) memory-feasible —
[`R5_FULL_PLAN.md` §R5.6](../tools/hecke-engine/R5_FULL_PLAN.md).

**D2.** Run R5-full as solver mode (not verifier mode) for ⁶Li, ⁷Li
with α + light-cluster ansatz; emit canonical $T_w$.

**D3.** Apply six-term consumer (A1) to derive Family 4 masses.
De-quarantine ⁶Li / ⁷Li.

**Eliminates constants:** #4 (Family 4 volumes + ρ).
**Effort:** ~3-5 days.

### Sprint E — residual cleanup

**E1.** Once A–D land, audit per-isotope ladder fits (#6) — most should
be redundant. Delete those that are. Document any that genuinely
encode missing structure (and queue them as their own work item).

**E2.** Label `E_0 = 0.782 MeV` (#7) as `fibre-functor-input` (= CODATA
`m_n − m_p − m_e`, the free-neutron β-decay Q-value) — not empirical,
but a measurement input.

**Eliminates constants:** #6, #7. **Effort:** ~half-day.

### Sprint F — sub-ppm refinements (after canonicalization)

- Pentagon-defect $\mathcal{O}(\hbar_q^2)$ Faddeev resummation
  → light atoms 1% → ~100 ppm.
- Markov-equivalence knot ID (replaces SnapPy census search)
  → 100 ppm → 1 ppm.
- R5-full SDP-as-solver in registry mode — replace historical knot
  guesses (D ↔ 6₂, T ↔ 8₁₁, ³He ↔ L6a4) with derived canonical $T_w$.
  Once this lands, the *braid words* in
  [`joint_tower_sdp.rs:55–124`](../tools/hecke-engine/src/bin/joint_tower_sdp.rs)
  become canonical too.

---

## 5. Cross-references

- [`docs/path-to-1ppb-04-plan.md`](path-to-1ppb-04-plan.md) — strategic roadmap (volume-based; this doc supersedes the volume framing for Sprint A)
- [`docs/b-over-a-error-budget.md`](b-over-a-error-budget.md) — Tier 3 error decomposition by family
- [`tools/hecke-engine/R5_FULL_PLAN.md`](../tools/hecke-engine/R5_FULL_PLAN.md) — R5.1–R5.8 sequenced plan
- [`tools/hecke-engine/R5_5_BUG_REPORT.md`](../tools/hecke-engine/R5_5_BUG_REPORT.md) — svec post-mortem (issue resolved)
- [`prop:atom-knot-mass-derivation`](../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) — pipeline status table
- [`prop:joint-tower-sdp-confinement`](../content/quantum-observable-universe/braids-and-knots/joint-tower-sdp-confinement.md) — design spec
- [`computations/joint-tower-sdp-rust.witness.json`](../computations/joint-tower-sdp-rust.witness.json) — current GB-NF + Wedderburn data for 7 particles

---

## 6. Decisions captured on this branch

1. **Mass tower = six-term curvature-rank decomposition of a single
   braid's Markov trace** — not an atom-by-atom recursion. Confirmed
   against `six-term-mass-formula-complete.md` and
   `curvature-rank-gb-stratification.md`.

2. **`α*` is not closed-form** in any q-deformed frame. PSLQ-falsified
   at 25 digits. The canonical fix is structural (3-term Wedderburn
   upgrade), not algebraic.

3. **The R2 GB-NF for D, T, ³He is computed and stored** — but the
   six-term formula consumer that converts it to a mass prediction
   has not been wired. That is the single highest-leverage gap, and
   it is the proposed Sprint A.

4. **R5-full Clarabel "bug at $d \geq 4$" was a self-inflicted svec
   col-major upper/lower triangular bug** (commit `807a3af`); not a
   solver issue. The remaining R5-full task is R5.6 (Wedderburn-block
   memory decomposition for $H_{18}$+).

5. **Hyperbolic volumes are downstream interpretation, not primary
   input.** Once the six-term consumer (A1) lands, the volume table
   in the atom-knot atlas is a sanity check — the canonical mass
   prediction comes from Markov trace on GB-NF.

6. **Two follow-up branches queued from this review:**
   - `claude/six-term-formula-consumer-family-1` (Sprint A)
   - `claude/three-term-wedderburn-upgrade` (Sprint B)

---

## Appendix: Theoretical-gap audit corrections (2026-04-27, post-rounds 2/3)

The original gap audit (above) named two specific theoretical gaps that
have substantively better state than initially asserted.

### D2 (α_em closed form) — substantively closed

The original framing — *"PSLQ-falsified at 25 digits in `{1, G, π, 1/π, q₀, ℏ_q}`"* —
**conflated α_em (fine-structure) with α\* (the empirical mixing constant
in the 2-term blend)**. PSLQ falsified `α*`, not `α_em`. The correct
state is:

- **Closed form** ([`alpha_em_pslq_uniqueness.py`](../computations/alpha/alpha_em_pslq_uniqueness.py)):

  $$\frac{1}{\alpha_{EM}} \;=\; 45 \cdot [3]_q \cdot \bigl(1 + \delta_{CS} + 8q \cdot \delta_{CS}^2\bigr), \qquad \delta_{CS} = \hbar_q^{4} \cdot [5]_q.$$

- **Reproduces CODATA to ~7 ppb** at the q_0 precision floor. CODATA
  m_μ/m_e is bounded to ~22 ppb, propagating to q_0 → α_em — the
  formula sits inside the q_0-uncertainty band.

- **PSLQ uniqueness** ([`alpha-em-pslq-uniqueness.witness.json`](../computations/alpha/alpha-em-pslq-uniqueness.witness.json), 2026-04-26): no
  competing integer relation found in 52-element basis at tolerances
  tol_dps ∈ {50, 100, 200}. Above 200 dps PSLQ runs to its precision
  ceiling without finding alternatives.

- **Derivable from q_0 alone** — no separate calibration input needed.

**Status:** structurally closed. Open work is incremental: push PSLQ
uniqueness to higher tol_dps if a tighter falsifiability bound is
desired.

### E2 (Lean formalization of the six-term formula) — already 5/6 sorry-free

The original audit asserted *"only Term 4 has sorry-free Lean"*. Direct
inspection of the Lean files (counting actual `sorry` tactic uses, not
in-comment matches) shows **the six-term formula has only 3 actual
sorrys, distributed across 2 files** — and 5 of 6 terms are already
sorry-free at the proof level:

| Term | Lean file | Actual `sorry` tactic uses |
|------|-----------|:------:|
| T1 (descended Markov trace) | [`categorical-mass-markov.lean`](../content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.lean) | **0 ✓** |
| T2 / T3 (brane tower) | [`mass-endomorphism-tower.lean`](../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.lean) | **0 ✓** |
| T4 (Frobenius co-Casimir) | [`frobenius-codim-universal.lean`](../content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.lean) | **0 ✓** |
| T5 (chirality) | [`chirality-dual-space-derivation.lean`](../content/quantum-observable-universe/braids-and-knots/chirality-dual-space-derivation.lean) | **0 ✓** |
| T6 (full pole structure) | [`full-pole-structure-mass-trace.lean`](../content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.lean) | **0 ✓** |
| T6 (cyclotomic-residue spectral sum) | [`gb-residue-spectral-sum.lean`](../content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.lean) | **2** (line 86 in-type + line 89 body) |
| support (Markov trace product) | [`markov-trace-product.lean`](../content/quantum-observable-universe/braids-and-knots/markov-trace-product.lean) | **2** (line 110, line 120) |

**Remaining work — 3 distinct sorry sites:**

1. [`markov-trace-product.lean:110`](../content/quantum-observable-universe/braids-and-knots/markov-trace-product.lean) — `markov_trace_product`
   theorem. The proof outline is documented (Markov property recursion
   from i = n-2 down to i = 0; Jones 1987 + Kassel 1995). Substantial
   inductive proof; hard sorry.

2. [`markov-trace-product.lean:120`](../content/quantum-observable-universe/braids-and-knots/markov-trace-product.lean) — `degree_bound`
   theorem. **Stub: the type is literally `True`**, so `sorry` is
   trivially closeable but the sorry-removal would be vacuous. The
   actual mathematical claim (`polynomial degree ≤ n²−1`) is in the
   comment, not in the type signature. Honest fix requires *first*
   strengthening the type to express the claim, then closing it; the
   sorry should not be removed without strengthening.

3. [`gb-residue-spectral-sum.lean:86 + :89`](../content/quantum-observable-universe/braids-and-knots/gb-residue-spectral-sum.lean) —
   `spectral_sum_finite` theorem. Two sorrys: one inside the type
   signature (`S.roots⟨0, sorry⟩` Fin index) and one in the body.
   The statement asserts that above the confinement level `ℓ(K, q)`,
   the graded Markov trace vanishes (`prop:confinement-level-unique`).
   Substantial; the in-type sorry needs to be replaced with a real
   index proof first.

**Status:** E2 is ~80% closed (5 of 6 terms sorry-free at the
mathematical claim level; only T6 cyclotomic-residue spectral sum
and one supporting Markov-trace-product theorem remain, plus the
`degree_bound` placeholder). Original audit overcounted by a factor
of ~2 (claimed 5 terms unproved; actual is 1 term + 1 support
+ 1 placeholder).

---

## Appendix: Post-rebase reuse audit (2026-04-27, after rebasing onto PR #454 + adjacent upstream work)

Three upstream commits landed during this branch's lifetime that
directly address items previously flagged as pending here.

1. **`atomic_tr_m_mpfr_50dps.py` + `atomic-tr-m-mpfr-50dps.witness.json`**
   compute `tr_M(T_w, q_0)` for proton, neutron, deuteron, tritium,
   ³He at 50 dps in the canonical 3A-strand atom-braid convention
   via the Hoefsmit + Wenzl bridge (`Σ_λ y_λ · χ_λ`).  This
   supersedes the per-particle scope of `probe_neutron_gap_round2.py`
   on this branch — round-2 only had Habiro-witness coverage for
   the H₃ proton + neutron and could not directly evaluate atomic
   tr_M for D/T/³He.  Round-2's −25 % H₃-convention finding still
   stands as a per-nucleon datum, but D/T/³He follow-up should now
   consume the upstream witness directly rather than reinventing
   the bridge.

2. **`audit(2H): markov_trace = 0 is structural; 6_2 ID is refuted`**
   (commit `4cbc08f18`).  This refutes the historical knot
   identification D ↔ 6₂ that this PR's Sprint A v5 naïve
   AME-assembly inherits via `tower_isotope_absolute.compute_isotope_tower`.
   Sprint A v5's assembly should be revised — its caveat block
   already flags the open combination convention; the revised
   convention should reflect the upstream refutation rather than
   silently using `6_2`.  Marked as a follow-up.

3. **`R5.6: design doc for Wedderburn-block decomposition`**
   (commit `61e29d500`).  Closes the previously-pending item
   *"R5.6 Wedderburn-block SDP decomposition needed for H_18+
   memory feasibility"* — the design doc is now upstream; future
   ⁶Li / ⁷Li dequarantine work should consume that design rather
   than re-scoping it.

No code on this branch needs to be deleted as a result of the
reuse audit (the round-2/3 probes are still independently valuable
data points; v5 is honest baseline data, not a canonical accuracy
claim).  But the canonicalization-review's pending-work table
above should be read with these upstream developments in mind:
two pending items are now in flight upstream (atomic tr_M, R5.6
design), and one assumption (D ↔ 6₂) is upstream-refuted.

### Second post-rebase audit (after PR #456 merge)

PR #456 landed substantial new infrastructure:

- `term4_frobenius_mpfr_50dps.py` + witness — Term 4 numeric n=2..11
- `term5_chirality_mpfr_50dps.py` + witness — Term 5 at 50 dps
- `term6_habiro_residue_mpfr_50dps.py` + witness — Term 6 at 50 dps
- `terms_2_3_brane_tower_mpfr_50dps.py` + `terms_2_3_atom_per_gen_mpfr_50dps.py` — Terms 2+3 for {electron, p, n} AND {D, T, ³He} (3A-strand)
- `atomic_tr_m_via_wenzl_bridge.py` + witness — refutes 8₁₁ for ³H and L₆ₐ₄ for ³He (in addition to the prior 6₂ refutation for ²H)
- `unified_mass_table_50dps.py` + `unified-mass-table-mpfr-50dps.witness.json` —
  **the canonical aggregator**, summing all six terms per atom

The unified mass-table aggregator's per-atom predictions exhibit
exactly the same structural gap that this branch's round-1, round-2,
round-4, and round-5 probes quantified independently: the proton
lands at ~+1.3 % (matching round-1's V_3term proton residual), and
the neutron / D / T / ³He show ~−55 % to −63 % residuals —
matching round-1's −56 % neutron baseline and round-5's brane-tower
~−58 % deuteron predictions.

This **cross-validation between independent probes and the upstream
unified aggregator** strengthens the canonicalization-review's
conclusion that the central remaining theoretical gap is the
combination convention itself (or an analogue of round-3's
3-input Skein-pair structural input that lifts to atoms), not the
numerical implementation of any single term.

No code on this branch needs deletion as a result of the PR #456
landing — round-3's 3-input-canonical and round-4/5's atomic-
assembly probes remain independently informative quantifications
(they show how each candidate atomic combination convention
fares).  The `unified_mass_table_50dps.py` witness is the
canonical place to read off the current six-term sum's accuracy;
this branch's probes are the canonical place to read off how
various alternative assemblies fare.
