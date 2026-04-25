# Fresh p/n derivation — 2026-04-24

## Motivation

Current mass pipeline uses per-generator `V̂_i^full` decomposition and
Plancherel weights. It shows a persistent ~1% residual for the proton
(−0.136%) and a **structural factor-2 gap** for the neutron (−55% in
the direct tower; the current mass_table_best closes it via
`m_n = m_p + Q_β(³H) + m_e`, which absorbs the failure into a
calibration input).

User raised specific concerns:

1. "We have all quadratic terms?" — current tower keeps only pair
   terms `z² · Φ_q(|V̂_i V̂_j|)` for adjacent `|i−j|=1`. For small braid
   groups (B_3, n=3) there is only one adjacent pair, so this is
   necessarily incomplete relative to the full expansion `Σ_{n≥1} ℏ_q^{2n}·Δ^{(n)}`.
2. "Are you using filtration on jet and tracking scaling?" — the
   paper's prop `mass-endomorphism-tower` gives
   `𝔪(ρ) = 𝔪⁽⁰⁾ + Σ_{n≥1} ℏ_q^{2n}·Δ^{(n)}`. Current code collapses
   this into level-0 + a single pair term. No jet-level tracking.
3. "Multiply topological volume (rational function of q) by Hecke
   energy" — current code uses Plancherel weights `d_q²/[n]_q!` and
   `Φ_q(V̂)` as scalar invariants. Does NOT compute the hyperbolic
   volume of the confined closure as a rational function of q, and
   does NOT use the Hecke energy `E(λ,q) = |y_λ(q)|` (SDP dual shadow
   price) as the weight.
4. "Follow witness → NF → confinement → V_hyp × Hecke-energy → sum
   over partitions with Wedderburn weights" — current pipeline skips
   the "V_hyp × E(λ,q)" step entirely.
5. "Holonomy was dropped in favor of algebra" — paper's non-abelian
   Stokes (Yekutieli) gives a multiplicative-integral / holonomy
   formulation, but the computational pipeline uses the algebraic
   Hecke-trace / Markov-trace shortcut. User notes this is OK because
   residues of meromorphic functions are ultimately algebraic.

## Paper derivation chain (from explore mapping)

| Layer | Block | File |
|---|---|---|
| 1. Frobenius–Hopf | `frobenius-hopf-substrate.md` | algebraic-substrate/ |
| 2. Non-abelian Stokes (Yekutieli) | `yekutieli-quantum-li.md`, `knot-factor-frobenius-pairing.md` | … |
| 3. Knot decomposition via knot operators | `knot-operator-energy.md`, `jet-filtered-knot-factor.md` | braids-and-knots/ |
| 4a. Jet/brane tower filtration | `jet-filtered-knot-factor.md`, `markov-moves-brane-tower.md` | braids-and-knots/ |
| 4b. Kähler differentials Ω¹(A) | `jet-prolongation.md`, `recursive-brane-tower.md` | lifting-and-descent/ |
| 5. SDP dual | `confinement-sdp.md`, `sdp-regime-switch.md` | braids-and-knots/ |

**Hecke energy** (from `knot-operator-energy.md`):
`E(λ, q) := |y_λ(q)| = |w_λ(q)/d_λ(q) − 1/[k]_q!|` — LP/SDP-dual shadow
price, NOT the Plancherel or Markov trace.

**Hyperbolic volume as confined observable** (from
`kashaev-volume-density.md` + `geometric-invariant-piecewise.md`):
V_hyp is EMERGENT via Kashaev limit; torus-type intermediate operators
can still produce a hyperbolic CLOSURE.

## Fresh-derivation algorithm

Given an atom ρ with braid word β in B_n:

1. **Build β_NF in H_n(q)** — from quark ordering via
   `hecke_core.nucleon_gen_chains` (already done in the pipeline).

2. **Tree-decompose by channel** at each mixed (1, −h/2) factor (the
   Kauffman-bracket smoothing). Each mixed factor bifurcates into
   σ_i and σ_i^{−1} branches. For B₃+gluons proton, count of mixed
   factors = 2 (one on g0, one on g1), giving 4 branches. For
   neutron = 2 (both on g0), also 4 branches.

3. **For each branch**, compute the physical braid word β_k as a
   sequence of ±σ_i, then take the trace closure in S³.

4. **Identify closure topology** via SnapPy (link / knot type,
   hyperbolic volume, or flag as torus/satellite).

5. **Per-partition decomposition**: for each λ ⊢ n compute:
   - χ_λ(β_NF) via Hoefsmit (already have)
   - E(λ, q) via SDP dual (via `confinement_sdp.py` infrastructure)
   - If the closure of β in the λ-block is hyperbolic, its
     V_hyp(λ, q) as a rational function (Kashaev limit).

6. **Sum**: `m(ρ) = Σ_λ E(λ, q) · V_hyp(λ) · |χ_λ(β_NF)|` — user's
   specification; to be validated against CODATA.

7. **Report**:
   - Branch list with closure topology per channel choice
   - Per-partition E(λ), V_hyp, χ contributions
   - Aggregate mass vs CODATA

## What to revalidate from older findings

Because the current pipeline skips the Hecke-energy × V_hyp step:

- **ρ_F = m_e · n_chir**: derived assuming density × volume with
  ρ_F = m_e · n_chir. The n_chir input comes from the dominant
  Wedderburn block rank (see `chi_inter_and_nchir_rank.py`). Should
  re-derive with Hecke energies instead of Plancherel weights — the
  dominant block may shift.

- **α = m_e · 8G** in `std_matrix_trace_closed_form.py`: uses a fixed
  Catalan constant in the α prefactor. If V_hyp is treated as
  rational in q (not a fixed constant), this prefactor changes.

- **Jet-tower suppression ℏ_q^{2n}**: per `prop:mass-endomorphism-tower`
  is DERIVED from the Kähler structure, not phenomenological. The
  current code's z² pair term corresponds to ONE piece of the
  n≥1 tail; no n≥2 contributions.

- **Plancherel vs Markov convention**: earlier work
  (`markov_weight_verification.py`) confirmed the pipeline uses
  Plancherel `d_q²/[n]_q!` weights, while the Jones polynomial needs
  Markov `z = 1/(q^{½}+q^{−½})`. Hecke energy is a THIRD weight
  (SDP-dual shadow price). Fresh derivation should clarify which is
  the physically correct one.

## Implementation plan

Single script `fresh_derivation_pn.py`:

- Step A: build β_NF for proton, neutron (reuse existing)
- Step B: enumerate channel branches
- Step C: for each branch, build physical braid as tuple of ±σ_i
  integers, close via SnapPy `Link.braid_word`, get `volume()` or
  flag torus/unlink
- Step D: tabulate V_hyp across branches
- Step E: compute SDP dual y_λ(q) via existing `confinement_sdp.py`
  adapted for n=3
- Step F: Σ_λ E(λ) · V_hyp(β_λ) · χ_λ(β_NF)
- Step G: compare against CODATA for p, n

Output: `fresh-derivation-pn.witness.json`

## Open architectural questions for user

- Is the "confined closure" per-block (via Young idempotent e_λ · β)
  or per-branch (via channel choice)? The paper defines knot
  operators as Wedderburn blocks but doesn't specify which closure
  gives V_hyp(λ).
- Should Hecke energy `E(λ)` multiply V_hyp(λ) for that block, or
  is the mass a sum over BRANCHES (channel choices) rather than
  blocks (partitions)?
- Is the prefactor `m_e · n_chir` right, or should it be
  `m_e` alone (with n_chir absorbed into E(λ))?

These affect the assembly step F and need user guidance before
committing to a specific formula.
