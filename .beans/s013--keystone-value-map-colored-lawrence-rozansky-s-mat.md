---
# s013
title: 'Keystone value-map: colored Lawrence-Rozansky S-matrix for Σ(2,3,5) → bwS0=d_q/D'
status: completed
type: task
priority: normal
created_at: 2026-06-30T23:50:37Z
updated_at: 2026-07-04T14:16:24Z
---


## Context (2026-06-30, merged PR #3190)

The s5-so3 keystone reduced to one field `bwS0 λ = d_q(λ)/D`
(`KeystoneVerlindeSMatrixBridge.lean`, `BWVacuumRowIsHecke`): does the geometric
WRT(S³/2I)=WRT(Σ(2,3,5)) data realize that unit vector? PR #3190 advanced the
geometric (colored-insertion) side; THIS bean is the remaining **value step**.

### What is established (PR #3190, `keystone_colored_sigma235_wrt.py`)
- Coloring the order-5 icosahedral fibre of Σ(2,3,5) by SU(2) colour α shifts the
  Lawrence–Zagier false-theta support `30(1±1/2±1/3±α/5)`. α=1 → bare {1,11,19,29}
  (validates the formula); α=2 → {7,13,17,23}; together = all 8 E₈ exponents.
- Bare support {1,11,19,29} = **H₄ exponents** (4D 600-cell, degrees {2,12,20,30},
  h=30); colour split = the **H₄ ⊂ E₈ folding**.
- E₈ exponents pair under Coxeter `e↔30−e` into 4 dual pairs ↔ the 4 conjugation
  classes of bwS0 at n=5, **4↔4 monotone** in magnitude. The Coxeter ℤ₂ mirrors the
  transpose/chirality ℤ₂ `λ↔λ′` of `S_{0λ}=S_{0λ′}` — supplying the `W_λ=W_{λ′}`
  symmetry the bosonic-colour foreclosure (#2608) showed `m_d` violates.
- **Value-map prune:** the naive exponent q-dimension `[e]_q` is REFUTED
  (`d_q/[e]_q` = 1.00, 0.54, 0.39, 0.36, non-constant).

### The task (the value step)
Derive the **genuine colored Lawrence–Rozansky / Hikami S-matrix amplitude** for the
colored Σ(2,3,5) invariant — the per-colour, per-block residue weights (NOT the total
`Ψ^{(α)}`, one number per colour; NOT the exponent label's `[e]_q`) — and check whether
it reproduces `bwS0(λ) = d_q(λ)/D` for n=5 (the lepton block), then general n.

### Discipline
- Validate each step against the bare invariant (α=1 must reproduce `Ψ(1/q₀)=2.3296`).
- No fit; no forced `Ψ=W_λ` numerology. The colored-amplitude FORMULA is where
  fabrication risk is real — build it rigorously against the literature structure
  (Lawrence–Rozansky 1999; Hikami arXiv:1811.05376, 2205.01282), not by guessing.
- Owner-gated keystone scope (narrow Subgoal-2 reversal, 2026-06-19).
- Feeds PR #2503 (keystone DG Step-1). Coordinate there.

### Cross-refs
- Audit: `docs/audits/2026-06-30-keystone-colored-sigma235-e8-family.md`
- Probe: `computations/probes/keystone_colored_sigma235_wrt.py`
- Bare probe: `docs/audits/scripts/keystone_habiro_wrt_s3_2i_probe.py`
- Modular-cat id: `docs/audits/2026-06-22-keystone-modular-category-identification.md`
- Ledger: `docs/coordination/s5-so3-keystone.md`

## First-pass result (2026-07-01, PR pending): compact candidates pruned

`keystone_valuemap_screen_s013.py` screened the natural closed-form value maps
against the 4 target d_q at q₀ (each class assigned its E₈ dual-pair exponent):
- **C1 [e]_q, C2 sin(πe/30), C3 sinh(ηe) — ALL REFUTED.** d_q=(1,4.11,5.22,6.22)
  vs [e]_q=(1,7.63,13.55,17.34); the E₈ exponents are NOT the value-map labels.
- **Sharp positive:** 3 of 4 d_q are single balanced q-integers with HECKE labels
  {1,4,5} (d_q(5)=[1], d_q(4,1)=[4], d_q(3,2)=[5]); only the self-conjugate ≥3-row
  d_q(3,1,1)=[4][3]/[2] is a product. **Difficulty is concentrated at the
  self-conjugate block** (where the SU(2) gate failed).
- **Narrowed target:** since compact maps fail and the arena is non-compact E_q(2)
  (2026-06-22 id), the value map is the **Hahn–Exton q-Bessel vacuum row**. Next:
  use the corpus q-Bessel infra (reeb-phase-qbessel) to compute the q-Bessel
  amplitude reproducing [1],[4],[5] on near-standard blocks + [4][3]/[2] on (3,1,1).

## Sharpened step-(a) target recorded (2026-07-01)

`docs/scope/2026-07-01-s013-qbessel-radial-part-target.md` records the falsifiable
q-Bessel radial-part target for the DG session: the 2nd-kind measure at the four λ⊢5
points must return {[1], [4], [5], [4][3]/[2]} (up to 1/D + the Z(5) normalisation).
The **discriminating test** is the self-conjugate (3,1,1) = [4][3]/[2] — the sole
non-single-q-integer block, and the ≥3-row block where the compact SU(2) gate failed.
Missing ingredient (⇒ owner-gated DG, not numerics): the partition-λ → q-Bessel-lattice
map, which is the open construction (inventing it = fabrication). Handoff to #2503.

## Lean obligation formalized (2026-07-02): KeystoneQBesselRadialTarget.lean

`QOU/BraidKnot/KeystoneQBesselRadialTarget.lean` (lean-direct exit 0, sorry-free,
generic `[Field R]` per §7c) makes the step-(a) target machine-checked:
- **Shape identities proved**: `d_q(5)=[1]`, `d_q(4,1)=[4]`, `d_q(3,2)=[5]`,
  `d_q(3,1,1)·[2]=[4][3]` (multiplicative, no nonzero hypotheses) + the division
  corollary `dq_311_div`.
- **Obligation class** `QBesselRadialPartRealization` (OPEN, no instance): lattice map
  + radial weight CONSTRAINED to the corpus-formalized Jackson second-kind q-Bessel
  contiguity + transpose-equivariance + `realizes : weight(pt λ) = S0 λ`.
- **Content theorems**: `realization_on_orbit` — any realization puts the whole vacuum
  row on ONE q-Bessel coefficient orbit (falsifiable, not an arbitrary table);
  `realization_discriminating_block` — the self-conjugate kill-test
  `w·D·[2] = [4][3]` derived, machine-checked.
The open `latticePt` construction remains the owner-gated DG object (#2503).

## Second-pass result (2026-07-02): residue character DERIVED; channels + q-Bessel rows pruned

`keystone_valuemap_qbessel_gate_s013.py` + audit
`docs/audits/2026-07-02-keystone-valuemap-qbessel-gate.md`. Primary sources firewalled
in sandbox (arXiv 403 on all routes) — round restricted to derivable/machine-verifiable:

- **POSITIVE (derived, sympy-exact + 50 dps):** the colored LR residue character from the
  sinh-product rational identity. α=1 reproduces bare {1,11,19,29}; α=1∪α=2 = E₈; supports
  5-periodic in colour (α=4≡α=1, α=3≡α=2). **All residue weights are ±1 (pure sign)** —
  the value map cannot live in the residue data.
- **POSITIVE (validated):** per-exponent channel decomposition Ψ^{(α)} = Σ_e Ψ̃^{(e)};
  α=1 channel sum = 2.329577 = bare invariant. The 8 channel values at 1/q₀ computed.
- **PRUNE (a):** channel/pair-sum/pair-diff amplitudes ≠ value map; analytic q→1 gate:
  channel ratios → L(0,χ_e) ∝ (30−e) — DECREASING in e at every anchor while d_q INCREASES.
- **PRUNE (a):** single-argument (q-)Bessel vacuum rows (ordinary J_e(x) vs classical dims;
  Hahn–Exton J_e(x;q₀⁻²) vs d_q; pair-symmetrized variants) all fail the 1-dof
  overdetermined gate (best 13% off vs 1e-6 bar).

### Remaining open step (literature-gated)
The genuine E_q(2) q-Hankel/Plancherel pairing with per-channel arguments
(Koelink–Swarttouw kernel) / the true colored LR-Hikami amplitude at the modular-transform
level. **Needs the primary sources:** run from a network-open environment, or owner drops
into `library/`: Hikami arXiv:1811.05376; Andersen–Mistegård arXiv:2205.01282;
Lawrence–Rozansky CMP 205 (1999).

## Third-pass result (2026-07-02, papers uploaded): value step SETTLED at the false-theta level — REFUTED

Owner uploaded the sources (commit `ece271823`; the paywalled LR CMP turned out
unnecessary). `keystone_valuemap_genuine_smatrix_s013.py` + audit
`docs/audits/2026-07-02-keystone-valuemap-genuine-smatrix.md`:

- **The genuine Σ(2,3,5) family is D=2** (Hikami 3.1/3.3): every colouring of the order-5
  fibre spans {(1,1,1),(1,1,2)} — the colored family of #3190 is 2-dimensional as
  functions; "4↔4" is support-level only. Hikami's χ^{(111)}/χ^{(112)} = the round-2
  sympy-derived characters EXACTLY (eq. 5.6 = the derived identity).
- **Transcription machine-validated end-to-end:** Theorem 10 exact (≤1e−38, N=3..11);
  φ=181/30 from Dedekind sums; S² = 1; vacuum row = Cor 12 flat-connection weights.
- **Vacuum row = (2/√5)(sin π/5, sin 2π/5), ratio = φ (golden)**; CS = −1/120, −49/120;
  magnitudes = √(Reidemeister torsion) (Thm 14).
- **VERDICT (scope (a), object = the Σ(2,3,5) false-theta S-matrix): bwS0 = d_q/D (4
  classes, ratios 1/4.11/5.22/6.22) is NOT the vacuum row of this object — type (2≠4) +
  value (φ) mismatch.** The geometric route cannot close on S³/2I itself.
- Redirects: larger-D Seifert data (D(3,4,5)=6, γ=4); colored Ẑ/GPPV blocks (Murakami
  2205.01282 in library/); or accept `BWVacuumRowIsHecke` as non-geometric. Owner decision
  needed on which (if any) to pursue — the original owner-gated scope (WRT(S³/2I)) is
  exhausted at this level.

## CLOSED (2026-07-03): answered NEGATIVELY at every geometric level; route 2 → bean rt2f

Owner redirect "4 1 2" executed: #3208 merged; route 1 (larger-D Seifert) executed on the
count-matching Σ(3,4,5) (γ=4; Theorem 9 exact ≤1.2e−38; flat row = (1,√2,φ,√2φ) — refuted
vs d_q and classical dims) and CLOSED as a class by the **constancy exclusion**: Seifert/
plumbed S-matrix entries are constant algebraic sine-products (no q in Hikami 3.8), while
d_q(4,1)/d_q(5) = [4]_q is nonconstant in q — no constant row realizes the fibre-level
`BWVacuumRowIsHecke`; single-anchor coincidences are the fitted mode the discipline
rejects. Probe: `keystone_route1_sigma345_constancy_s013.py`; audit:
`docs/audits/2026-07-03-keystone-route1-closed-route2-scoped.md`. Route 2 (colored
Ẑ/F_K(x,q) q-function blocks — the surviving type-correct class) handed to bean `rt2f`
(owner-gated). Positives that stand: E₈/H₄ support combinatorics (#3190); the
derived-character ↔ Hikami eq. 5.6 cross-validation; Lean shape identities + the
`QBesselRadialPartRealization` obligation (DG sibling).
