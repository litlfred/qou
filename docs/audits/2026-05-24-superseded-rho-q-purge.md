# Aggressive purge of SUPERSEDED ρ_q = 1/ℏ_q² (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)  ·  **Triggered by**: owner directive "lets first get remove superseded rho. use canonical derived. fix paper and compute. aggressive removal. update coord docs. rederive mass ratio, q relationships etc. then reasses where error is coming in. lookout for ℂ structure"  ·  **Status**: purge in progress

## Trigger context

This finding closes the loop on the [Q_β net-ansatz fitting finding](2026-05-24-q-beta-net-ansatz-fitting-finding.md) and the [Hermiticity / complex-q audit](2026-05-24-complex-q-historical-trajectory.md):

- **Phase A v2 test** (PR #1127 commit `b54fe1ad` and follow-ups; `q-beta-complex-q-test1-phasea-v2.witness.json`) found **outcome (d)**: the Q_β ansatz **cannot simultaneously fit CAL-2 + CAL-3 for ANY complex q** on the Apollonius circle. The +0.17% residual is positive everywhere on the circle (min +1.31 keV at θ=0 real axis; grows to +508 keV at θ=180°). Im(q) does not close it.
- This rules out the simple "Im(q_0) absorbs the residual" hypothesis under the ansatz.
- Combined with the prior finding that the canonical mass formula uses the **SUPERSEDED** substrate density `ρ_q = 1/ℏ_q²` (per [`mass-endomorphism-tower.md` lines 28-51](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md#L28-L51)), the next decisive step is **purging the SUPERSEDED ρ_q ansatz** and re-deriving the m_μ/m_e (CAL-2) and Q_β (CAL-3) formulas in the canonical operator-valued (Wedderburn-graded) form.

## The SUPERSEDED form

From `mass-endomorphism-tower.md`:

> *"The substrate-only ansatz $\rho_q = 1/\hbar_q^2 \approx 102$ is **structurally wrong**: it is braid-class-independent, but the categorical density $\rho_K$ varies $\sim 30\times$ across atoms ($A = 1$ to $A = 3$; [graded ρ_K expansion](#prop\:rho-k-graded-expansion)). The correct dimensional factor is the **operator-valued** $A^\lambda_{\mu, \nu}(I) \in \mathrm{End}(V_\mu \otimes V_\nu)$ from [hecke branching trace decomp](#prop\:hecke-branching-trace-decomposition), which depends on the specific braid through its LR-block decomposition."*

## The canonical form

Per [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md):

$$m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K = \underbrace{Z m_\mathfrak{p} + N m_\mathfrak{n} + Z m_e}_{\rho_K^{\mathrm{LO}}\text{ (Markov mult., PROVED)}} + \underbrace{\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|}_{\rho_K^{\text{single-gen}}\text{ (PROVED, 0.18\% acc.)}} + \underbrace{\alpha\, z^2 \sum_{i<j} \ln|\hat V_i \hat V_j|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{ (OPEN)}} + \dots$$

with $\alpha = m_e \cdot 8G \approx 3.7445$ MeV (Borromean binding scale).

For ATOMIC braids (Z protons + N neutrons), LO piece is the constituent sum.

For LEPTONS (electron, muon — Z = N = 0 in the nuclear sense), the LO piece is **0** in this form. The lepton mass formula needs a separate derivation that doesn't go through "Z·m_p + N·m_n + Z·m_e" — likely an "intrinsic lepton" pathway via the trefoil ($e^-$) and figure-eight ($μ$) braids directly through the per-braid mass tower without nuclear-constituent decomposition.

**This re-derivation is open work** — see "Re-derivation queue" below.

## Files using SUPERSEDED ρ_q (survey snapshot 2026-05-24)

### Content blocks (13 files)

```
braids-and-knots/algebraic-geometric-dilog-equivalence.md
braids-and-knots/kashaev-volume-density.md
braids-and-knots/kashaev-volume-conjecture.md
braids-and-knots/markov-lambda-knot-operations.md
braids-and-knots/mass-endomorphism-tower.md       (SUPERSEDED note already present)
braids-and-knots/pre-tau-vs-post-tau.md
braids-and-knots/phi-q-tower-algebraic-stratification.md
braids-and-knots/phi-q-tower-jsj-bridge.md
braids-and-knots/two-tier-scaling-pq.md
information-theory/quantum-temperature.md
particle-interactions/frobenius-packing-density.md
particle-interactions/mass-volume-factorization.md
archimedean-universe/e-hartree-categorical-derivation.md
```

### Compute scripts (2 files)

```
computations/q_pinning_50_digit.py
computations/probes/rho_f_categorical_probe.py
```

### Implicit ρ_q usage (Skein formula `Vol(4_1)/ℏ_q²` without naming ρ_q)

```
observations/skein-mass-relation.md                — key CAL-2 input file
braids-and-knots/calibration-inputs.md             — multiple uses
braids-and-knots/pre-archimedean-derivation-chain.md — derivation chain doc
```

## Phase 1 (this PR) — banner pass

Add prominent SUPERSEDED-$\rho_q$ banners with cross-links to this audit doc + the canonical replacement (`prop:rho-k-graded-expansion`) in:

- [x] `observations/skein-mass-relation.md` — banner above the formula + "LO" marker on the formula itself
- [x] `braids-and-knots/calibration-inputs.md` — banner after the formula, "LO" marker
- [ ] `braids-and-knots/mass-endomorphism-tower.md` — already has internal SUPERSEDED block; promote to top-of-file banner
- [ ] `braids-and-knots/pre-archimedean-derivation-chain.md` — banner at the relevant section
- [ ] All other 11 content files — terse banner referencing this audit

## Phase 2 (follow-up; current PR scope) — compute scripts

For `q_pinning_50_digit.py` and `rho_f_categorical_probe.py`:
- Audit whether they use ρ_q as INPUT (then need replacement) or just CONTEXT (then need comment update)
- If input: route through `prop:rho-k-graded-expansion` form
- Update witness JSONs to reflect canonical form

## Phase 3 — re-derivation (open work, queued)

The substantive analytical work the owner is asking for:

1. **Re-derive m_μ/m_e in canonical form.** Lepton-side variant of `prop:rho-k-graded-expansion`. Inputs: trefoil σ_1³ braid for electron, figure-eight (σ_1 σ_2^{-1})² braid for muon. Compute `|tr_M(μ_braid)|/|tr_M(e_braid)|` directly at the operator level via `prop:per-braid-mass-tower`; identify how `Vol(4_1)/ℏ_q²` emerges as the leading-order term and what the operator corrections look like.

2. **Re-derive q_0 from canonical m_μ/m_e formula.** With the canonical form, the equation `(canonical_form_function)(q) = 206.7683` gives a new q_0 estimate. Compare to current real q_0 ≈ 1.10998; the difference is the **size of the operator correction** for the muon ratio.

3. **Re-derive Q_β from canonical mass formulas.** Path B in the [net-ansatz audit](2026-05-24-q-beta-net-ansatz-fitting-finding.md): compute `m(n)` and `m(p)` directly from the per-braid mass tower (operator-valued); subtract; subtract m_e; compare to CODATA. This bypasses the `Q_β = |Δ(net)| · E_0` ansatz entirely.

4. **Re-run complex-q Phase A v2 with canonical Q_β.** If Path B gives a Q_β formula that's not the simple `|·|` ansatz, re-evaluate whether complex q closes the residual under the new formula.

5. **Reassess error source.** Once 1-4 are done, the residual locations can be attributed:
   - Operator correction (size measured in step 1)
   - Tower truncation N=0 (measured in step 3)
   - Φ_q vs Li_2^q (measured in step 3 with both)
   - Im(q_0) (re-tested in step 4)

This is multi-day analytical work; out of scope for this PR but tracked here for follow-up.

## ℂ structure watchpoints

Per owner directive "lookout for ℂ structure":

- The Hoefsmit seminormal basis matrix entries have specific REAL structure for q > 0 real; complex q extension requires analytic continuation with explicit branch choice for `q^{1/2}`. **WATCHED.**
- The Kashaev volume reading (geometry side) is real-q-only as currently stated; needs complex extension for q ∈ ℂ. **WATCHED.**
- Markov trace Plancherel positivity (`tr_M(σ_i^2) > 0`) may break for complex q. **WATCHED.**
- The bar involution `q ↦ q⁻¹` and Hermitian-* `q ↦ q̄⁻¹` differ for complex q; the canonical projection `P_avg` uses bar (per `bar-involution.md` and PR #1153). **WATCHED — already in Path D audit.**

## Coordination

- PR #1153 (sinh-bar-antisymmetric-partner-probe) — the bar/`P_avg`/`P_skew` framework already structurally relates; this purge tightens that connection.
- Coordination ledger update: `docs/coordination/2026-05-24-q-beta-fitting-and-complex-q.md` will be updated with this purge as a new sub-section.

## Status

**Phase 1 (banner pass)**: in progress this commit.
**Phase 2 (compute scripts)**: queued for this PR if cheap; else follow-up.
**Phase 3 (analytical re-derivation)**: queued for follow-up branches per owner's "combine one PR" directive — staged as sequential commits on `claude/gifted-feynman-U7ckD`.
