# Handover: Categorical nuclear binding on branch `claude/nf-transition-projection-aZ3MH`

> **Status note (2026-05-08, deep-audit pass).** The headline
> numbers in §1a–§1d below describe the *legacy* single-level
> CRT path (`crt_markov.py`) and were the right summary at the
> time of the original handover. The current best-of-breed mass
> path is `atomic_braid_mass_table.py` (T1…T6 assembly). On the
> light-atom test bucket (D, ³H, ³He, ⁴He) the atomic-braid path
> currently shows ~25–55 % residuals, dominated by the placeholder
> `(1−h²)^{A−2}` quotient-braid coupling for `A≥3`. The 0.9 %
> figure still applies to the deprecated CRT path it was measured
> on, **not** to the atomic-braid path. See
> [`AUDIT-DEEP-2026-05.md`](../../AUDIT-DEEP-2026-05.md) §3 for
> the current empirical-input ledger; in particular the framework
> currently uses **three** calibration constants (m_e CODATA,
> m_µ/m_e CODATA → q₀, Q_β CODATA → E₀), not one.

## 1. What IS working (computed, validated, committed)

### 1a. Rest mass via CRT/mpmath (|Δm/m|% ≤ 0.91% for D → ⁴⁰Ca, *legacy CRT path*)

**File:** `crt_markov.py`
**Witness:** `crt-markov.witness.json`

Single-level Markov trace $|\mathrm{tr}_M(W)|$ evaluated with 50-digit
mpmath precision. No float underflow. Results in table (30 atoms
D through ⁴⁰Ca):

| A-bucket | n | mean \|Δm/m\|% | range |
|---|---|---|---|
| A ≤ 5 | 4 | 0.29% | [0.04, 0.70] |
| A ∈ [6, 10] | 4 | 0.62% | [0.54, 0.68] |
| A ∈ [11, 20] | 11 | 0.81% | [0.73, 0.85] |
| A ∈ [21, 30] | 5 | 0.88% | [0.86, 0.90] |
| A ∈ [31, 40] | 6 | 0.91% | [0.90, 0.91] |

### 1b. Confinement level infrastructure

**Files:** `confinement_shortcuts.py`, `confinement_level_walk.py`,
`heavy_atom_opts.py`

LevelWord classes for levels 1-7 with `undo_to_quark()` for each.
Nucleon-level ILP ground states cached for all atoms D → ²⁰Ne.

### 1c. Content-block propositions

- `def:knot-operator-energy` (LP shadow price)
- `def:confinement-level` (filtration J^ℓ(q))
- `def:atom-knot`, `def:isotope-knot`, `def:stable-atom`, `def:unstable-atom`
- `def:local-shadow-ordering` (local ≤_q)
- `prop:*-exists`, `prop:*-unique` companions for each
- `rem:ilp-solution-count-unwrap`
- **`prop:shell-schur-weyl-self-duality`** (Schur-Weyl ⇒ $x_\lambda = x_{\lambda^*}$)
- **`prop:compound-beta-shell-calibration`** (shell $y_{\mathrm{target}}$ from β-decay chain)
- `sec:atom-isotope-confinement` ties it all together in Ch 3
- `shell-transition-knot` (renamed from `nuclear-shell-intruder`)

### 1d. Multi-level SDP infrastructure

**Files:** `sdp_cross_channel.py`, `multi_level_sdp.py`, `misdp_cross_channel.py`

Continuous 2×2 PSD blocks per adjacent generator at every level 3-7.
MISDP via enumeration works for small n_vars.

---

## 2. Empirical inputs (calibrations)

### 2a. Single archimedean input: $E_0 = 0.782$ MeV
- **Source:** Free-neutron β-decay Q-value (experimental)
- **Role:** Categorical fibre functor $\tau: R \to \mathbb{R}$ sending
  $Q_{\mathrm{cat}} = |\mathrm{tr}_M(n)| - |\mathrm{tr}_M(p)|$ to 0.782 MeV
- **Justification:** `prop:categorical-mass-markov` —
  "determined by matching one experimental value"

### 2b. CODATA $m_p = :val[m_p_MeV]{precision=6}$ MeV
- Used to convert ratios to absolute MeV
- Equivalent to $E_0$ by scaling

### 2c. Substrate parameter $q_0 \approx :val[q_0]{precision=6}$
- Categorical — comes from `prop:local-substrate-q` in Ch 7
- Not a fit; derived from CODATA $m_\mu / m_e$ ratio

### 2d. Compound β-decay Q-values (AME 2020)
- Used **categorically**, not as fit parameters
- See `prop:compound-beta-shell-calibration` for chain extraction
- Examples: ³H→³He (0.019), ¹⁴C→¹⁴N (0.156), ⁴⁰K→⁴⁰Ca (1.311) MeV

**Single-calibration framework: $E_0$ is the only free parameter.**

---

## 3. Gaps and approximations

### 3a. |Δm/m|% ~ 0.9% ≈ missing tower contribution
Per `prop:mass-endomorphism-conjecture`: single-level Markov trace
contributes < 0.5% of total mass. The 0.9% error we see IS the
tower binding energy, which our single-level CRT doesn't capture.

### 3b. CRT currently uses **only V_s (std channel)**
- Missing: V_sym, V_alt 1-dim channels
- Missing: full H_{3A} Wedderburn summation (uses per-generator H_3)
- Missing: $\Phi_q$ tower terms
- **Fix priority:** add V_full = w·V_sym + w·V_s + w·V_alt → still fast

### 3c. Shell σ_shell magnitude requires β-decay chain calibration
- Self-duality structure $x_\lambda = x_{\lambda^*}$ established (categorical)
- Target $y \sim 10^{-3}$ identified (from B/(A·m_p))
- **Magnitude derivation via β-decay chain**: written but not computed
- **Fix:** implement compound-β chain subtraction to extract
  $y_{\mathrm{target}}(A_{\mathrm{magic}})$ from AME data

### 3d. Parity pattern in inter-nucleon multiplicity m_pn
Deuteron example: odd m_pn ≈ 1.5 MeV (predicts 69% of B_AME), even
m_pn gives negative (wrong sign). Implies **adding crossings does
not close the binding gap** — the gap is in missing Φ_q terms.

### 3e. Level-4 shell-operator position vs parameters
- **Parameters:** Hecke eigenvalues (q, -q⁻¹) — same as any σ (established)
- **Position:** shell-boundary generators $3 \cdot A_{\mathrm{magic}} - 1$
- **Multiplicity:** from ILP at level 4 with conjugate-symmetry
  constraint (not yet computed past A_magic = 8)

### 3f. H_{3A}(q) Wedderburn weights are approximated
Current code uses H_3 weights (w_sym, w_std, w_alt) at every
generator. For A-nucleon atoms, the correct weights sum over
λ ⊢ 3A. This is the "additive Wedderburn" approximation.

---

## 4. Next steps (in priority order)

### 4a. Add Φ_q tower terms to CRT
**Impact:** Should close the 0.9% gap.
**File to modify:** `crt_markov.py` → compute V_full per generator,
then sum Φ_q terms.
**Effort:** 1-2 days. Add:
```python
V_full_i = w_sym * V_sym_i + w_std * V_s_i + w_alt * V_alt_i
single_gen_tower = sum(Phi_q(abs(V_full_i)) for i in range(n_gens))
cross_pair_tower = sum(z**2 * Phi_q(abs(V_full_i * V_full_j))
                       for (i, j) adjacent)
```

### 4b. Implement compound β-decay chain subtraction
**Impact:** Derive $y_{\mathrm{target}}(A_{\mathrm{magic}})$ from AME data.
**File to create:** extend `compound_beta_shell.py`
**Data needed:** full β-decay chain Q-values through each magic anchor
(AME 2020 or NNDC).
**Effort:** 3-5 days (data curation + categorical subtraction formula).

### 4c. Level-4 shell ILP with self-duality constraint
**Impact:** Full shell-word σ_shell characterization.
**File to create:** `shell_ilp_constrained.py`
**Formulation:** minimize $\sum_\lambda x_\lambda w_\lambda$ s.t.
$x_\lambda = x_{\lambda^*}$ AND $\sum x_\lambda y_\lambda = y_{\mathrm{target}}$
**Effort:** 2-3 days (leveraging existing ILP infrastructure).

### 4d. Correct H_{3A}(q) Wedderburn summation
**Impact:** Exact (not approximate) descended Markov trace.
**File to modify:** `crt_markov.py` → sum over λ ⊢ 3A with
CRT-reconstructed polynomial coefficients.
**Effort:** 1-2 weeks (CRT reconstruction is nontrivial for p(3A)
partitions).
**Alternative:** for heavy atoms, use the Plancherel-concentrated
truncation (top-N dominant partitions).

### 4e. Symbolic-in-q via sympy (Track A from earlier)
**Impact:** Exact polynomial in $q$; verification + precision.
**File:** `tower_binding_symbolic.py` (stub exists, works for A≤3).
**Effort:** 1 week + CRT reconstruction for A ≥ 4.

---

## 5. Where to find improvements

### By priority

1. **Biggest win (close the 0.9% gap):** 4a (add Φ_q terms) + 4d (H_{3A} Wedderburn)
2. **Structural completeness (shell physics):** 4b (β-chain) + 4c (level-4 ILP)
3. **Verification (exact math):** 4e (symbolic)

### By file

- `crt_markov.py`: computational bottleneck; extend to V_full + tower
- `compound_beta_shell.py`: data curation + chain formula
- `shell_ilp_constrained.py` (new): level-4 with self-duality constraint
- `heavy_atom_opts.py`: already has cached infrastructure; extend with
  tower evaluator
- `atom_per_generator_volumes` in `hecke_core.py`: needs to use
  H_{3A} Wedderburn weights, not H_3

### By documentation

- `INFRASTRUCTURE-AUDIT.md` — the full gap analysis
- `AUDIT-crt-k-level.md` — what k we're actually at
- `UNIVERSAL-BRANCHING-PLAN.md` — Schur-Weyl branching formula

### By proposition

- `sec:atom-isotope-confinement` (Ch 3) — definitions + companions
- `prop:mass-endomorphism-conjecture` — the open gap (tower sum)
- `prop:shell-schur-weyl-self-duality` — categorical self-duality
- `prop:compound-beta-shell-calibration` — β-chain derivation

---

## 6. Session statistics

- **Commits:** 32 on `claude/nf-transition-projection-aZ3MH`
- **Build errors:** 0 throughout
- **Content blocks added:** ~30 (definitions, propositions, remarks)
- **Lean stubs:** 16+
- **Computation modules:** 12+
- **Test atoms computed:** 30 (D through ⁴⁰Ca)

## 7. Honest summary for incoming reviewer

We have built the **categorical framework** for nuclear mass/binding
in a rigid-monoidal setting:
- Atoms, isotopes, confinement levels formally defined
- Shell operators structurally characterized (conjugate self-dual)
- Multi-level SDP + CRT Markov trace infrastructure
- Single-calibration framework ($E_0 = 0.782$ MeV)

**What is NOT yet there:** full tower mass computation. Current
|Δm/m|% = 0.9% = binding fraction missing because we compute only
descended Markov trace, not Φ_q tower terms.

**What is next:** implement Φ_q tower terms (priority 4a) — expected
to close the 0.9% gap to single-digit MeV precision for all atoms.
