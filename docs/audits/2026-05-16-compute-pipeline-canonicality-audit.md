# Compute-pipeline canonicality audit — 6-term mass, E_0, ρ_K

**Date:** 2026-05-16
**Branch:** `claude/post-662-c3-chain-anti-staleness`

User question: *what does the paper say about 6-term mass + canonical
E_0 + ρ_K? Is that all in the compute pipeline?*

## 1  What the paper says

### 1·a  Canonical mass formula (`prop:atomic-mass-gb-nf`)

The paper's **abstract algebraic statement** is

$$
  \mathcal{M}(K) \;=\; m_e \cdot \rho_K \cdot \lvert\!\operatorname{tr}_M\!\bigl(\mathrm{NF}_{\mathrm{GS}}(\beta_K)\bigr)\!\rvert
$$

— $\mathrm{NF}_{\mathrm{GS}}$ is the Gröbner–Shirshov normal form in
$H_n(R, q_0)$; $\operatorname{tr}_M$ is the canonical Jones–Markov
trace; $\rho_K$ is the **categorical density** of the braid class.

The paper presents **three equivalent forms** of this:

| Form | Expression | Inputs | Status (per paper) |
|---|---|---|---|
| (GB-NF) — abstract | $m_e \cdot \rho_K \cdot \lvert\operatorname{tr}_M\rvert$ | $m_e, \beta_K, q_0, \rho_K$ | algebraic; $\rho_K$ currently empirical |
| (constituent) — concrete | $Z m_p + N m_n + Z m_e + \alpha \sum_i \ln \lvert\hat V_i\rvert$ | $m_e, m_p, m_n$ (CODATA), $\beta_K, q_0$ | 0.18% mean error, Z=1..20 |
| **(six-term spectral) — predictive** | $T_1 + T_2 + T_3 + T_4 + T_5 + T_6$ | $m_e, \beta_K, q_0, E_0$ (proton calibration) | **25% under-prediction at ⁴He** per paper |

### 1·b  Canonical E_0 (CAL-3 per `prop:three-calibration-inputs`)

Exactly three external calibration inputs:

| ID | Quantity | (Co)homological role |
|---|---|---|
| CAL-1 | $m_e$ (CODATA) | $H^0$ — mass scale |
| CAL-2 | $m_\mu/m_e \approx 206.768$ | $H^1$ — substrate $q_0$ via Vol(4_1)/ℏ_q² |
| CAL-3 | $Q_\beta(n) \approx 0.78233\;\mathrm{MeV}$ | $H^2$ — hadronic scale $E_0 = Q_\beta(n)/\lvert\Delta(\mathrm{net})\rvert$ |

**Everything else is a prediction**, with the factorisation
$\mathcal{O} = \hat{\mathcal{O}}(q_0) \cdot m_e^a \cdot Q_\beta^c$
for non-negative integer $a, c \in \{0, 1\}$.

### 1·c  ρ_K graded expansion (`prop:rho-k-graded-expansion`)

$$
  m_e \cdot \lvert\operatorname{tr}_M(\beta_K)\rvert \cdot \rho_K
  \;=\;
  \underbrace{Z m_p + N m_n + Z m_e}_{\rho_K^{\mathrm{LO}}\text{-piece (Markov mult.)}}
  + \underbrace{\alpha \sum_i \ln \lvert\hat V_i\rvert}_{\rho_K^{\mathrm{single-gen}}}
  + \underbrace{\alpha z^2 \sum_{i<j} \ln \lvert\hat V_i \hat V_j\rvert_{\mathrm{Wedd}}}_{\rho_K^{\mathrm{pair-gen}}\text{ (open)}}
  + \cdots
$$

with $\alpha = m_e \cdot 8G$ ([binding scale Catalan](#prop:binding-scale-catalan)).

**The LO piece is tautological** — $|\operatorname{tr}_M|$ cancels:

$$
  \rho_K^{\mathrm{LO}} \cdot m_e \cdot \lvert\operatorname{tr}_M\rvert
  = \frac{Z m_p + N m_n}{m_e \lvert\operatorname{tr}_M\rvert} \cdot m_e \cdot \lvert\operatorname{tr}_M\rvert
  = Z m_p + N m_n.
$$

**The non-tautological content lives in the second-order term**
$\operatorname{Binding}(K) = m_e \cdot \Sigma_\lambda y_\lambda(q) \chi^\lambda(\beta_K) \Delta_\lambda(K)$.

## 2  What's in the compute pipeline

The main mass-table compute lives in
[`paper_six_term_isotope_sweep.py`](../../computations/sweeps/paper_six_term_isotope_sweep.py).
Two assembly paths:

### (a) `paper_six_term_mass(Z, N, ...)` — six-term form

Computes T_1 through T_6 and sums. The path used by `run_sweep_for_mode`.

| Term | Pipeline status |
|---|---|
| T_1 = $\lvert\operatorname{tr}_M(\beta_K)\rvert$ | ✅ canonical (per-irrep numeric Hoefsmit; matches paper exactly) |
| T_2 single-gen brane tower | ⚠ **PATHOLOGICAL at $q_0$** (paper notes; PR #524 documented $\Phi_q(0.99) \approx 6.7 \times 10^5$ amplification). Multiple fallback modes (`li2q`, `habiro`, `per-partition-k`, `drop`) try to avoid the pathology. |
| T_3 pair-gen brane tower | ⚠ **PATHOLOGICAL at $q_0$** (same as T_2) |
| T_4 = $m_e \cdot \tau(C_{\dim_q})$ | ✅ canonical (Lean-proved `frobenius_codim_universal`) |
| T_5 = chirality factor a_K | ✅ canonical V2 = $\tau(\beta \cdot \beta_{\mathrm{mirror}}^{-1})$ (PR #654) |
| T_6 cyclotomic tail | ✅ canonical (Habiro residue witness; loaded from `term6-habiro-residue-mpfr-50dps.witness.json`) |

The sweep then composes:
- Per-derivation: $B = E_0 \Delta T_1 + \alpha \Delta(T_2 + T_3) + m_e \Delta T_4 + E_0 (a_K-1) T_1 + \Delta T_6$, $M_\mathrm{pred} = \mathrm{constituent} - B$. Uses **two configurations** (bound vs free) and differences them.
- Proton-fit (legacy): collapses to single E_0 fit at A=1, leaks errors with A.

### (b) `atomic_mass_via_rho_k.py` — ρ_K form (LO)

Per `prop:rho-k-graded-expansion` LO ansatz:
$$
  \rho_K^{\mathrm{LO}}(Z, N) = \frac{Z m_p + N m_n}{m_e \cdot \lvert\operatorname{tr}_M(K)\rvert}.
$$

The script's own header acknowledges **LO is tautological** — $|\operatorname{tr}_M|$ cancels and you get back $Z m_p + N m_n$. The "residual" reported IS the binding energy (the framework's null prediction at LO).

### (c) `binding_K_direct.py` — non-tautological NLO

Computes the binding directly as
$\operatorname{Binding}(K) = m_e \cdot \Sigma_\lambda y_\lambda(q) \chi^\lambda(\beta_K) \Delta_\lambda(K)$
where $\Delta_\lambda(K)$ are per-partition mass shifts. **Status: $\Delta_\lambda$ values still being derived** (PRs #602, #603, #613 raced this; status unclear post-merge).

## 3  Audit — what's not canonical in the pipeline

### 3·a  Pathology: T_2 / T_3 specialisation at $q_0$ is **not Markov-invariant**

Per `prop:six-term-mass-formula-complete` §Term 2:

> "The specialisation evaluates the quantum dilogarithm on a per-generator amplitude $|\hat V_i|$ which is **not** Markov-invariant — different reduced words for the same braid give different per-generator amplitudes but the same Markov trace."

The pipeline has **multiple ad-hoc fallback modes** (`drop`, `li2q`, `habiro`, `per-partition-k`, `combined`) to route around this pathology. These are mitigations, not derivations. **None is canonical per the paper.**

The paper marks T_2 / T_3 status as **"TRACE in R-side; PATHOLOGICAL at $q_0$ archimedean"** — the canonical algebraic form $\sum_i z \cdot \mathrm{Vol}_q^{(\{i\})}(\beta)$ IS Markov-invariant, but the archimedean specialisation through $\Phi_q$ isn't. The pipeline uses the specialisation, not the algebraic form.

**Action**: T_2 / T_3 in the sweep are computed via the archimedean specialisation. To bring this canonical, the pipeline would need to compute $\mathrm{Vol}_q^{(\{i\})}(\beta)$ as a Markov trace over the transfer-matrix chain (per the paper) — not via $\Phi_q(|\hat V_i^{\mathrm{full}}|)$.

### 3·b  E_0 source — TWO paths in pipeline, neither fully canonical

The pipeline has `q_beta_source` flag with three modes (set up on this branch):

| mode | E_0 source | Canonical per CAL-3? |
|---|---|---|
| `"codata"` | $E_0 = Q_\beta(n) / \lvert\Delta(\mathrm{net})\rvert$ with $Q_\beta(n)$ as CAL-3 input | ✅ matches CAL-3 (this is the design) |
| `"form_a_cos"` | $Q_A \cdot \cos(\alpha_{N1})$ — substrate-derived Form A + c_2 = b² | ❌ predicts $Q_\beta$ (not consumes it); 306 ppm residual |
| `"full_chain_n4"` | Q_A · cos · (1−b²ℏ⁴) · (1−2b³ℏ⁶) · (1+(b²+½)b⁴ℏ⁸) | ❌ predicts Q_β (17.7 ppb residual) |

The legacy "proton-fit" path in `run_sweep_for_mode` collapses E_0 from a single proton anchor — **violates CAL-3** (uses m_p instead of Q_β). The substrate path `e_0_full_mev()` correctly uses Q_β.

**Per CAL-3**: the canonical path is `codata` (treats Q_β as input). The substrate-derived paths (`form_a_cos`, `full_chain_n4`) test whether the framework can predict Q_β internally — they are *audit-only* unless one accepts dropping CAL-3 in favor of a fully substrate-derived chain.

### 3·c  ρ_K — pipeline has LO only; non-tautological NLO unwired

Per `prop:rho-k-graded-expansion`:
- ρ_K^LO: ✅ computed (`atomic_mass_via_rho_k.py`) — but **tautological**
- ρ_K single-gen: ⚠ pieces present (T_2 expansion) but with the $\Phi_q$ pathology
- ρ_K pair-gen: ❌ **open**
- $\Delta_\lambda(K)$ per-partition shifts (binding): **not yet derived**

The pipeline's `M_predicted` comes from the **six-term form**, not the ρ_K form. These are paper-equivalent in principle, but the six-term form has the T_2/T_3 pathology baked in.

**`binding_K_direct.py` would compute the canonical binding** if $\Delta_\lambda$ values were available — they aren't.

### 3·d  Coulomb correction status

Per [`def:coulomb-charge`](../../content/quantum-observable-universe/braids-and-knots/coulomb-charge.md):

$$
  E_{\mathrm{cross}}(\mathfrak{H}) = \tfrac{1}{2}(n_+ + n_-)(q + q^{-1}) + Q(\mathfrak{H})(q - q^{-1})
$$

The antisymmetric Q(𝔥)·h piece IS the categorical Coulomb. **This is already in T_1 by construction** (T_1 = $|\operatorname{tr}_M(\beta_K)|$ sees all crossings with their signs).

The M5 probe on this branch confirmed this empirically: adding Q·h·E_0 *on top* of M_pred makes the MAE worse (1.00× — see [m4-coulomb-bottleneck.md](2026-05-16-m4-coulomb-bottleneck.md)). Coulomb is canonically inside T_1, not a separate term.

### 3·e  Magic-shell coupling — empirical κ in M4 probe

The M4 / interface-type-resolved probe used $\kappa = -1.07$ MeV/excess as an **empirical** fit from PR #656. **No canonical derivation of κ** in the paper. The `prop:magic-shell-coupling-witness` block notes this is a candidate D-2 = q-Catalan with Z/N-dependent SYT-shape corrections — but the q-Catalan derivation isn't wired into the pipeline.

### 3·f  Chirality V2 status

The V2 chirality `a_K = τ(β · β_mirror⁻¹)` is now production-default in `paper_six_term_mass(..., chirality_source="v2")`. This matches `prop:chirality-dual-space-derivation` per CLAUDE.md §V2. Closed-form fallback (`Π(1 + sign·h)`) is retained for back-compat but not canonical.

✅ canonical.

### 3·g  m_p / m_n chain closure

Per PR #663's audit: `low_isotope_mass_table.py` uses an m_p sanity guard (1% threshold) that flags the m_p chain as **`derivation_pending`** — not yet categorically closed via `build_proton_mass_50dps_chain.py` Workplan 2 Phase 2. The 6-term pipeline currently uses CODATA m_p / m_n in some places (via the validation aliases). This is allowed per CAL-3 (which makes Q_β the H² anchor, NOT m_p) — but for full 1 ppb closure, the m_p chain must close categorically.

## 4  Summary table — canonicality status

| Component | In pipeline? | Canonical per paper? | Notes |
|---|---|---|---|
| T_1 = \|tr_M\| | ✅ | ✅ | per-irrep Hoefsmit; matches paper |
| T_2 single-gen | ✅ | ❌ **pathological at q_0** | uses Φ_q specialisation (non-Markov-invariant); multiple ad-hoc fallback modes |
| T_3 pair-gen | ✅ | ❌ **pathological at q_0** | same as T_2 |
| T_4 Frobenius co-Casimir | ✅ | ✅ | Lean-proved |
| T_5 chirality V2 | ✅ | ✅ | substrate-derived (PR #654) |
| T_6 cyclotomic tail | ✅ | ✅ | from Habiro witness |
| E_0 (CAL-3) | ✅ | ✅ (in `codata` mode) | substrate-derived modes are audit-only |
| ρ_K LO | ✅ | ⚠ **tautological** | $\|\operatorname{tr}_M\|$ cancels by construction |
| ρ_K NLO (binding) | ⚠ skeleton | ❌ **Δ_λ not derived** | `binding_K_direct.py` exists but Δ_λ values open |
| Coulomb (Q·h) | ✅ inside T_1 | ✅ | M5 confirmed adding on top double-counts |
| Magic-shell coupling κ | ⚠ in M4 probe | ❌ **empirical** | candidate D-2 (q-Catalan) unwired |
| m_p, m_n closure | ❌ uses CODATA | ⚠ **derivation_pending** per #663 | Workplan 2 Phase 2 open |

## 5  Recommended path to canonical compute pipeline

1. **Derive Δ_λ per-partition mass shifts** (the NLO ρ_K piece). Unlocks `binding_K_direct.py` as the canonical non-tautological binding formula. Open per PRs #602, #603, #613 status.
2. **Fix T_2 / T_3 pathology**: replace $\Phi_q(|\hat V_i|)$ specialisation with the algebraic Markov-invariant form $\sum_i z \cdot \mathrm{Vol}_q^{(\{i\})}(\beta)$ from `prop:mass-endomorphism-tower` §Algebraic form.
3. **Derive κ for magic-shell coupling categorically** (D-2 q-Catalan candidate from #656). Closes the empirical fit in M4.
4. **Close m_p chain** via `build_proton_mass_50dps_chain.py` per PR #663's audit recommendation.
5. **After all 4**: re-emit mass table. Expected: substantially lower MAE because (a) tautology removed → real predictions, (b) T_2/T_3 no longer dominated by Φ_q amplification, (c) magic-shell coupling is now structural not empirical, (d) m_p baseline closes.

The current M2/M3/M4/M5 mass-table sequence has hit a wall not because of more c_k coefficients, but because **the compute pipeline is computing the wrong terms**.
