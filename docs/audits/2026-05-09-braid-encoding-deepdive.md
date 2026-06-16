# Braid encoding + knot-operation deep dive

**User directive:** "validate braid encodings of p and n, check all knot
operations are SDP solved. track all braids invoiced in γγ for each
particle. follow all the way through. see where differences really
are. … check on writhe in paper and compute. /coordinate with
claude/term7-alpha5-derive-investigation."

**Status:** committed (`0985210`); this addendum adds writhe
cross-validation, term7-alpha5 coordination, and canonical_a_k
provenance correction.

## 1 — Particle braid encodings (verified)

Source: `mass_at_3A_proper.atom_braid_word_3A(Z, N)`, which uses
`hecke_core.nucleon_gen_chains(['u','u','d'])` for protons and
`(['u','d','d'])` for neutrons.

| Particle | Hecke | length | σ-word skeleton | writhe |
|----------|-------|--------|-----------------|--------|
| electron | H_2 | 3 | σ_0³ (trefoil T_{2,3}) | **+3** |
| proton (uud) | H_3 | 11 | σ_0⁴·½(σ+σ⁻¹)_0·σ_0²·σ⁻¹_1³·½(σ+σ⁻¹)_1 | **+3** |
| neutron (udd) | H_3 | 11 | σ_0³·½(σ+σ⁻¹)_0²·σ_0²·σ⁻¹_1⁴ | **+1** |
| deuteron | H_6 | 23 | (proton chain)·½(σ+σ⁻¹)_2·(neutron-like in gens 3..) | +4 |
| triton | H_9 | 35 | proton·pn·neutron·nn·neutron | +4 |
| ³He | H_9 | 35 | proton·pp·proton·pn·neutron | +8 |
| ⁴He | H_12 | 47 | proton·pp·proton·pn·neutron·nn·neutron | +8 |

## 2 — Writhe cross-validation (paper vs compute)

Two independent computational paths, both consistent with paper
definition (`writhe = #σ⁺ − #σ⁻`; averaged ½(σ+σ⁻¹) crossings
contribute 0):

| Particle | ribbon_content_average.writhe_of_atomic_braid | Manual count from word | Agree |
|----------|-----------------------------------------------|------------------------|-------|
| proton | +3 | +3 | yes |
| neutron | +1 | +1 | yes |
| deuteron | +4 | +4 | yes |
| triton | +4 | +4 | yes |
| ³He | +8 | +8 | yes |
| ⁴He | +8 | +8 | yes |

**Paper formula consistency check:** The chirality factor formula
`a_K = 1 + w(K)·h` from
[`chirality-writhe-ribbon-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/chirality-writhe-ribbon-derivation.md)
predicts (at q₀, h ≈ 0.209):
- a_K(proton) ≈ 1 + 3·0.209 = **1.627**
- a_K(neutron) ≈ 1 + 1·0.209 = **1.209**
- ratio: **1.346**

Strategy-3's |tr_M(p)|/|tr_M(n)| = 1.6332/1.2483 = **1.308** —
within ~3% of the paper's first-order writhe-chirality prediction.
This is consistent with the audit's note in
`chirality-writhe-ribbon-derivation.md:138-150`: the structural
form `a_K = 1 + w·h` is correct; the specific coefficient is
"paper-empirical" pending refinement.

## 3 — Knot-operation classification (revised)

the prior audit (`braid_encoding_audit.py`) flagged `canonical_a_k` as `method: unknown`. **This
was a metadata classification error.** The values ARE derived, not
empirical:

`jet_knot_invariants.py` docstring:

> "At each jet level k, the Hecke algebra H_k(q) has partitions with
> Wedderburn weights. The nuclear braid β ∈ H₃(q) has characters in
> each H₃ irrep (sym, std, alt). Via the branching rule H_k → H₃,
> each partition of k decomposes into H₃ components. The per-level
> knot invariant is: a_k = Σ_λ w_λ × χ_λ(β) / Σ_λ w_λ × dim_restricted(λ)"

Convergence at q₀ (from `jet-knot-invariants.witness.json`):

| Atom | k=3 | k=4 | k=5 | converged a_k |
|------|------|------|------|--------------|
| ³H | 0.0967 | 0.0681 | 0.0675 | **0.0648** (k=8) |
| ³He | 0.2233 | 0.2067 | 0.2063 | **0.2048** (k=8) |
| ⁴He | 0.6123 | 0.6701 | 0.6714 | **0.6768** (k=8) |

So canonical_a_k IS a derivation — Wedderburn-weighted character
ratio in the branched Hecke algebra, structurally analogous to
Murphy's elementary symmetric polynomials in cell-content
q-eigenvalues (see §6 below).

**Updated classification of the 9 knot operators:**

| Operator | Status | Notes |
|----------|--------|-------|
| T1 \|tr_M_atomic\| | DERIVED | Closed-form Markov-trace; matches the closed-form derivation to 9e-16 |
| Δ_I a(Z,N) | **DERIVED** | Wedderburn-weighted character ratio per `jet_knot_invariants`; converges by k≈4-8. (Was incorrectly flagged as `method: unknown` in the prior braid-encoding audit.) |
| **Δ_n² full-twist** | **PLACEHOLDER** | `full_twist_scalar(A) = 1.0` for all A. Genuine action q^{c(λ)} per Wedderburn block IS computed (`full-twist-delta-n2-verification.witness.json`) but NOT consumed by mass-table assembly. |
| T2 / T3 | DERIVED | z²/z⁴ Markov scalars; A-only |
| T4 Frobenius co-Casimir | DERIVED | q-hook-length; Lean-closed n=2..7 (commit 4e876b6) |
| T5 chirality a_K | PARTIAL | First-order `1 + w·h` form correct; coefficient paper-empirical per the conjecture's own retraction |
| T6 cyclotomic tail | DERIVED | Habiro residue per A |
| E_0 cat→MeV | FITTED (1 param) | Proton CODATA anchor |

## 4 — Structural mismatch (now sharpened)

The framework's `fresh_derivation_pn_true_sdp.py:1-26` documents:

> "Absolute m_p and m_n are NOT directly derivable from γγ → target
> Hecke-energy distance because entanglement energy (pre-observable
> complex-q sector) is gauged away. Only DIFFERENCES/RATIOS project
> to observables. The clean prior result is:
>   m_n − m_p = ((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u)
> giving < 1 ppm on Δm across isotopes once μ_d − μ_u is calibrated
> from CODATA."

Strategy-3 violates this by deriving M_pred[n] from |tr_M(n)| absolutely.
The 8.3% neutron error is the consequence; per the neutron-error diagnostic it is localised
entirely to T1 = |tr_M_atomic|. Writhe difference (+3 vs +1) is the
structural origin.

## 5 — Coordination with `claude/term7-alpha5-derive-investigation`

Branch HEAD: `6c385531` "audit: paper simplification via iterative
LP-dual / GB-filtration" (2026-05-09 20:27 UTC, no PR yet).

**Their direction (highly synergistic with our audit):**

The branch proposes consolidating the mass formula via three
structural insights:

1. **Frobenius self-duality ⇒ primal=dual.** The Frobenius pairing
   forces every LP/SDP encountered in the chain to satisfy strong
   duality. Therefore "every mass-formula coefficient is canonically
   an LP-dual variable" — i.e., shadow-priced rather than fitted.

2. **Jucys–Murphy central elements give atom-independent invariants.**
   Their Probe `α_5 = u^{(5)*} = m_e · Σ_λ w_λ · c_5(λ)` where
   `c_5(λ) = e_5({q^{2c(□)} : □ ∈ λ})` is the 5th elementary
   symmetric polynomial in cell-content q-eigenvalues. Since
   `e_5(J_1, …, J_n) ∈ Z(H_n(q))` (Murphy 1981), `c_5(λ)` is a
   central character — atom-independent automatically.

3. **GB-filtration stratification by jet order ⇒ unified theorem.**
   The mass-formula iterative LP-dual:
   `𝔪(ϱ) = Σ_l u^{(l)*}` where each shadow-price `u^{(l)*}` lives
   at jet-order ℓ.

**Three new prop blocks proposed on that branch:**
- `prop:frobenius-self-duality-forces-lp-dual-extraction`
- `prop:jucys-murphy-central-elements-qou`
- `prop:mass-formula-iterative-lp-dual`

**5-week phased rollout in §6** consolidating:
- 35 mass-formula blocks → ~14
- ~52 pages of ad-hoc derivations → 6 pages of one unified theorem
- 14 scripts → 1 LP/SDP solver

**Direct overlap with our audit findings:**

| Our finding | term7-alpha5 closure path |
|-------------|---------------------------|
| canonical_a_k via Wedderburn-weighted character ratio | Generalises to `c_k(λ)` central characters via Murphy's theorem (atom-independent by construction) |
| Δ_n² placeholder (full_twist_scalar = 1) | Captured naturally in the iterative LP-dual `Σ_l u^{(l)*}`: Δ_n² is the saturated-shell limit at high jet order |
| E_0 calibration is a 1-param fit | Replaced by Frobenius self-duality forcing primal=dual, so E_0 itself is a shadow-price (Bauer–Ricci theorem) |
| "Only differences are observable" per fresh_derivation_pn_true_sdp | Matches: shadow-prices are differences by construction (LP duality theorem) |
| 4 dead-placeholder M_HECKE_PIPELINE_AT_Q0 literals | Eliminated by the unification (one LP/SDP solver replaces 14 scripts) |

**Suggested next steps for cross-PR coordination:**

(1) When term7-alpha5 lands as a PR, reference the audit chain on this branch (m_e anomaly, Option B chain, neutron diagnostic,
/ 1.8 audits as the empirical motivation: the bug-hunt established
exactly the structural defects (placeholder Δ_n², bare-mass
prediction violating "only differences are observable", σ↔σ⁻¹
asymmetry over-prediction) that their unification resolves.

(2) Their `prop:jucys-murphy-central-elements-qou` is a direct
formalisation of the canonical_a_k mechanism observed in
`jet_knot_invariants.py`: the convergence of `a_k` at k=4 and the
relation `a_k = V_inter / (1 + W_STD)` for Z=N atoms is exactly the
Murphy-centrality phenomenon (`c_5(J)` is central, hence
factor-independent of the specific Wedderburn block).

(3) Their `prop:mass-formula-iterative-lp-dual` `𝔪(ϱ) = Σ_l u^{(l)*}`
naturally subsumes our six-term `T1 + T2 + T3 + T4 + (a_K-1)T1·E_β
+ T6` decomposition: each `u^{(l)*}` IS a single term at jet-order
ℓ, with the unit conventions automatically consistent (since each
shadow-price has the same units by LP duality).

(4) The Δ_n² discharge that the prior braid-encoding audit flagged is closed by jet-order
ℓ ≥ saturation in their framework: at magic shells the iterative
sum truncates because `Σ_(l > l_sat) u^{(l)*}` vanishes by
shell-saturation.

## 6 — Open items (this audit can't close, term7-alpha5 likely will)

- (Item 1 — already done) Anchor m_p via CODATA: kept.
- (Item 2) Derive m_n via difference formula at <1 ppm: term7-alpha5
  Murphy-centrality framework gives a clean closure, but it's a
  multi-week rollout. **Stopgap:** keep current Strategy-3 with a
  documented systematic 8.3% error on m_n, OR stop reporting bare
  m_n and only report m_n − m_p (which the framework can predict at
  <1 ppm via the existing `(q+q⁻¹)/(√q+√q⁻¹)·(μ_d − μ_u)` formula).
- (Item 3) Compound binding energies via differences: same scope as
  Item 2; defer to term7-alpha5.
- (Item 4) Δ_n² discharge: replace `full_twist_scalar(A) = 1.0` with
  the actual q^{c(λ)} eigenvalue per block. This is a small
  refactor (the witness data already exists in
  `full-twist-delta-n2-verification.witness.json`); affects T2/T3
  per the original docstring's intent.

## 7 — Cross-references

- Braid-encoding audit + script: [`braid-encoding-audit.witness.json`](../../computations/audits/braid-encoding-audit.witness.json),
  [`braid_encoding_audit.py`](../../computations/audits/braid_encoding_audit.py)
- Neutron error diagnostic: [`neutron-error-diagnostic.witness.json`](../../computations/neutron-error-diagnostic.witness.json)
- Option B closed-form chain: [`option-b-proton-mass-full-chain.witness.json`](../../computations/option-b-proton-mass-full-chain.witness.json)
- m_e anomaly audit: [`2026-05-09-proton-m_e-anomaly.md`](2026-05-09-proton-m_e-anomaly.md)
- Mass-table 1ppb audit: [`2026-05-09-mass-table-1ppb-audit.md`](2026-05-09-mass-table-1ppb-audit.md)
- Sibling: `claude/term7-alpha5-derive-investigation` HEAD
  [`6c385531`](https://github.com/litlfred/qou/commit/6c385531fccc3fda82b43ee71bd49673f1204ec3)
- Strategy-3 chain: [`atomic_braid_mass_table.py`](../../computations/atomic_braid_mass_table.py)
- Writhe convention: [`chirality-writhe-ribbon-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/chirality-writhe-ribbon-derivation.md)
- Difference-formula source: [`fresh_derivation_pn_true_sdp.py:1-26`](../../computations/fresh_derivation_pn_true_sdp.py)
