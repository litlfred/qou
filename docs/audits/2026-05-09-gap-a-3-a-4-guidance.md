# Guidance for new agents: attacking GAP-A-3 + GAP-A-4

**Date:** 2026-05-09
**Audience:** New Claude Code agent picking up the binding-energy
derivation problem
**Context:** Pentagon-uv-commutation is now closed (conditional on
the Woronowicz left-rule); the all-orders mass tower is algebraically
well-defined; the binding-energy gap nevertheless remains. The next
targets are **GAP-A-3** (brane-tower level selection) and **GAP-A-4**
(per-block prefactor `ρ(Z, N)`).

## What's already established

- Three CAL-3 inputs: `m_e`, `m_p`, `m_n` (CODATA 2022). Everything
  else should be derived. `Q_β = m_n − m_p − m_e ≈ 0.78 MeV` is
  arithmetic from CAL-3.
- Categorical scalars `|tr_M(β_K)|` are derivable to machine ε for
  K ∈ {p, n, D, T, ³He} (3 independent paths agree on PR #572 +
  this branch).
- ⁴He per-λ chi cache as of 2026-05-09 (this session): saved at
  [`computations/chi-helium-4-h12-numeric.witness.json`](../../computations/chi-helium-4-h12-numeric.witness.json).
  77 partitions of 12, |tr_M(⁴He)| = 0.0553483.
- The Δ_λ derivation race PR (#613) compared 5 closure principles
  (Occam / co-Casimir / LP-shadow / Wenzl-bridge / Frobenius-pairing
  min-norm). All 5 fail or trivialise — the open problem is genuinely
  GAP-A-3 / GAP-A-4 and not the closure principle.

## GAP-A-3 — brane-tower level selection `n_*(K)`

### Problem statement

Per `conj:brane-level-selection` and `rem:mass-endomorphism-jet-tower`,
the mass tower is in principle an infinite sum over jet levels:

$$\mathfrak{m}(K) \;=\; \bigl|\textstyle\prod V^{(0)}\bigr| \;+\; \sum_{n=0}^{\infty}\bigl[\,\Sigma_1^{(n)} + z^2\,\Sigma_2^{(n)}\,\bigr].$$

But for any *confined* particle `K`, the physical mass should depend
only on FINITELY many levels (the brane tower "saturates" at some
`n_*(K)`). The conjecture asks for an explicit categorical formula
for `n_*(K)`.

### What's known

- For low isotopes (D, T, ³He, ⁴He), `n_*` is chosen empirically by
  matching binding energies — this is a fit, not a derivation.
- The geometric tail bound `z^2 / (1 - z^2) ≈ 0.33` (at q_0) means
  truncating at `n_* ≥ 5` gives < 0.1% relative error in the tower
  sum. So the truncation is "soft" for stable atoms.

### Hypothesis space (try in order)

1. **`n_*(K) = ℓ(K)/A`** where ℓ(K) is the GS Coxeter length of the
   canonical word and A = Z + N. For `β_p`, ℓ = 11, A = 1, so
   `n_* = 11`. For β_D, ℓ = 23, A = 2, `n_* ≈ 11`. Test: does this
   give correct binding for D? **Probably no** (current pair-only
   already over-shoots by 3×; truncating earlier won't help).

2. **`n_*(K) = depth of confinement SDP`** — the SDP solver
   `lp_dual_solver.solve_psd_operator_selection_sdp` returns a
   PSD-rank that may equal `n_*`. Test: compute the SDP rank for
   D, T, ³He, ⁴He using existing infra; check if it's a small integer.

3. **`n_*(K) = number of irreducible Wedderburn blocks with non-zero
   y_λ χ^λ(β_K)`** (the "active" partitions). For D this is 11; for
   T/³He it's 30. Probably too big; test anyway.

4. **`n_*(K) = JSJ decomposition depth`** — for the canonical knot
   `K_atom` (per the GAP-A-1 census-assigned identification: D ↔ 6_2,
   T ↔ 8_11, ³He ↔ L_6a4), compute the JSJ tree depth. SnapPy can
   do this. Test: depth(6_2) = 1? depth(8_11) = ?

### How to attack

Step-by-step plan:

1. **Implement `additive_wedderburn_volumes_at_jet_level(n)` for
   `n ≥ 1`.** This is the prerequisite for testing ANY `n_*`
   hypothesis empirically. Currently only `n = 0` exists in
   `mass_endomorphism.py`. The level-(n+1) volumes come from the
   level-n ones via the jet prolongation `J^1` per
   `prop:jet-prolongation`. Concretely: `V_i^{(n+1)}` lives in
   `A_n ⊗ Ω¹(A_n)`; pulling back through Schur–Weyl–Hecke gives a
   matrix-coefficient formula in terms of `V_i^{(n)}` and the
   modular automorphism (per the pentagon closure `Û V̂ = q² V̂ Û`).

2. **Compute `M_K(n)` = level-truncated mass** for n = 0, 1, 2, 3
   on D, T, ³He, ⁴He.

3. **Find `n_*(K)`** = the truncation that matches `M_AME(K)` to
   within (say) 0.1%. Tabulate.

4. **Look for a categorical pattern** — compare `n_*(K)` to ℓ(K),
   A, Z, N, SDP rank, JSJ depth. Whichever matches across all 4 atoms
   is the candidate categorical rule.

### Useful files

- [`mass_endomorphism.py`](../../computations/mass_endomorphism.py) — level-0 V̂ + tower
- [`canonical_tower.py`](../../computations/canonical_tower.py) — alternative level-0 tower
- [`recursive-brane-tower.md`](../../content/quantum-observable-universe/lifting-and-descent/recursive-brane-tower.md) — definition of A_{n+1} = J^1(A_n)
- [`jet-prolongation.md`](../../content/quantum-observable-universe/lifting-and-descent/jet-prolongation.md) — the J^1 functor

## GAP-A-4 — structural prefactor `ρ(Z, N)`

### Problem statement

The mass formula `M(K) = m_e · ρ(Z, N) · |tr_M(β_K)|` carries an
overall scalar `ρ(Z, N) ∈ ℤ_{>0}` that's currently a per-atom fit:

| atom | ρ (observed) |
|---|---|
| p | 1 |
| n | 1 |
| D (n=6) | 1 |
| T (n=9) | 2 |
| ³He (n=9) | 2 |

The conjecture `conj:rho-prefactor-structural` proposes
`ρ = ⌊dim_q(λ*)⌉` where `λ*(K)` is the dominant Wedderburn block.

### Today's finding (2026-05-09)

**The conjecture as stated FAILS.** Tested with `λ* = argmax |y_λ χ^λ|`
(the natural definition of "dominant"):

| atom | dominant λ* | dim_q(λ*) at q_0 | ⌊dim_q(λ*)⌉ | observed ρ |
|---|---|---:|---:|---:|
| D | [5,1] | 5.220 | 5 | **1** |
| T | [6,3] | 62.25 | 62 | **2** |
| ³He | [6,3] | 62.25 | 62 | **2** |

⌊dim_q(λ*)⌉ over-predicts by factors of 5, 31, 31. The conjecture's
RHS is way too big.

### Hypothesis space (alternative `ρ` rules)

1. **`ρ(K) = number of orthogonal Wedderburn copies`** — count copies
   of the dominant block in the *isotypic* decomposition, not its
   dimension. For D: dominant block [5,1] appears once, so ρ = 1. ✓
   For T/³He: dominant block [6,3] appears... need to compute.
   This is the most promising next test.

2. **`ρ(K) = ⌊dim_q(λ*) / d_λ⌉`** where `d_λ` = ordinary Specht dim.
   For D: dim_q([5,1])/d_[5,1] = 5.22/5 ≈ 1.04 → 1. ✓ For T:
   dim_q([6,3])/d_[6,3] = 62.25/48 = 1.30 → 1. ✗ (observed 2).

3. **`ρ(K) = isospin multiplicity`** — for T (Z=1, N=2) and ³He
   (Z=2, N=1), they form an isospin doublet (T = 1/2). Multiplicity
   = 2I+1 = 2. ✓ For D (Z=N=1, isospin 0 or 1?), depends on the
   nuclear ground state. D ground state has I = 0 → ρ = 1. ✓
   For ⁴He (Z=N=2), I = 0 → ρ = 1. **Most physically motivated.**

4. **`ρ(K) = parity of A`** or **`ρ(K) = 1 + (A − Z − N) mod 2`** —
   trivial / wrong; A = Z + N always.

5. **`ρ(K) = 1 + (number of non-empty isospin orbits in the canonical
   word β_K)`** — count the m_pp, m_pn, m_nn interface contributions
   in `atom_braid_word_3A`. For D (1 pp/np interface): ρ = 2? But
   observed is 1. Test on other atoms.

### How to attack

1. **Test hypothesis 3 (isospin multiplicity)** first — it has the
   strongest physical motivation and matches D, T, ³He, p, n with
   trivial computation. If it also predicts ρ(⁴He) = 1 correctly,
   that's strong evidence.

2. **Test hypothesis 1** (orthogonal Wedderburn copies) — needs
   computing the multiplicity of the dominant block in the
   isotypic decomposition of `H_n(q)|_{β_K}` for n ≥ 6.

3. **For each candidate rule, derive `ρ` categorically** — the
   conjecture only counts as "closed" if the rule comes from a
   first-principles structural identity (not a per-atom fit).

### Useful files

- [`conj-rho-prefactor-structural.md`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.md)
- [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
- [`derivation-audit-report.md` § GAP-A-4](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md)
- [`tr-m-q-hecke-seminormal.witness.json`](../../computations/tr-m-q-hecke-seminormal.witness.json) — top-3 contributions per atom

## Joint GAP-A-3 + GAP-A-4 attack

Note that `n_*(K)` and `ρ(K)` are coupled: the mass formula
`M(K) = m_e · ρ · |tr_M^{(≤n_*)}|` has both as multiplicative
prefactors on the truncated tower. Fitting both jointly:

$$\rho(K)\,|\,\textstyle\sum_{n=0}^{n_*}\,\text{level-}n\text{ contribution}\,|\;=\;M(K)/m_e.$$

For D (M/m_e ≈ 3670, |level-0 only| ≈ 9990 from production):
`ρ_D · |⋯| = 3670` ⇒ `ρ_D · (≤ 9990) = 3670` ⇒ ρ_D ≤ 0.37 — but ρ ∈ ℤ_{>0}. So no integer ρ matches at level-0; we MUST go to higher levels (or different volumes) to get the magnitude right. **The level-(n ≥ 1) contributions must REDUCE the mass, not add to it.**

This contradicts the geometric-tail interpretation (which gives a
positive 33% correction). So either:

1. Higher-level contributions enter with **alternating signs** (the
   pentagon-ascension residuals oscillate), OR

2. The production code's level-0 V̂ values are **wrong** (already a
   factor-of-3 too big), and the correct V̂'s are smaller — which
   would mean the V̂-construction itself needs revision (a deeper
   GAP than A-3 / A-4).

**Verifying which of (1) or (2) holds is the most important first
step for a new agent.** Direct test: compute level-1 V̂'s from the
J^1 jet prolongation; if they differ in sign from level-0, hypothesis
(1) holds. If their level-0 reduction simplifies to ~3× smaller than
the current additive-Wedderburn formula, hypothesis (2) holds.

## Suggested workflow for the new agent

1. Read this guidance + the audit doc + the closure doc (in that order).
2. Look at the ⁴He chi cache from this session (77 partitions, 50-dps).
3. Pick GAP-A-3 OR GAP-A-4 based on tractability.
4. Implement Step 1 of the corresponding "How to attack" section above.
5. Document findings as a new audit doc; do NOT push without
   `ci=billing` clearance from the user.
6. Open a PR with one test result per atom.

## Cross-references

- Today's findings: [`2026-05-09-pentagon-uv-commutation-woronowicz-closure.md`](2026-05-09-pentagon-uv-commutation-woronowicz-closure.md)
- Truncation handling: [`2026-05-09-truncation-handling-after-pentagon-closure.md`](2026-05-09-truncation-handling-after-pentagon-closure.md)
- Mass-table audit: [`2026-05-09-mass-table-fitting-audit.md`](2026-05-09-mass-table-fitting-audit.md)
- Open conjectures: [`derivation-audit-report.md`](../../content/quantum-observable-universe/braids-and-knots/derivation-audit-report.md)
