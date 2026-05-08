# 02 — Pre-Archimedean Derivation Chain

**Goal:** A step-by-step audit of the algebraic-side derivation that the pipeline *says* it implements, with a status badge for every link.

**Boundary:** "Pre-archimedean" = lives in `ℚ(q)` before evaluation at `q = q_0 ∈ ℝ`. The chain's terminus is the substrate parameter `q_0` (FITTED from `Vol(4₁)` and `m_μ/m_e`). Anything that uses real numbers other than `q_0` is post-archimedean and out of scope.

**Status badge:** ⚙ `proved` | 🟡 `has_sorry` | 🟠 `conjecture` (Lean class) | 🔴 `not_started` / `no_block_exists` | 📥 `external_axiom` (Mathlib / SnapPy / CODATA — assumed without proof in QOU)

## Chain summary diagram

| # | Link | Block | Lean | Status | Critical? |
|---|------|-------|------|--------|:---------:|
| 1 | Categorical action (rigid monoidal `𝐂`) | `def:rigid-monoidal-category` (Ch 8 glossary) | Mathlib `CategoryTheory.MonoidalCategory` | ⚙ external | — |
| 2 | Non-abelian Stokes ⇒ Wilson loop = `tr_M` | `rem:yekutieli-stokes` | (none) | 🔴 `not_started` (only a remark) | 🔴 |
| 3a | Jones–Markov trace `tr_M` exists | `thm:jones-markov-trace` (Ch 4) | external `axiom` | 📥 `external_axiom` (Jones 1987) | — |
| 3b | JSJ ↔ Wedderburn correspondence | (no block) | (none) | 🔴 `no_block_exists` | 🔴 |
| 4 | Knot decomposition (link → braid → Hecke) | `def:hecke-algebra` + `thm:markov-equivalence` (Ch 4) | `QOU/Hecke.lean` | 🟡 `has_sorry` for Markov-equivalence completeness | 🟡 |
| 5 | Wedderburn block decomposition of `H_n(q)` | `prop:wedderburn-decomposition` (implicit) | (no Lean file) | 🔴 `no_block_exists` (computed in `wedderburn_pair_volumes.py`, not formalised) | 🟠 |
| 6a | Partitions / hook-length / Hoefsmit cell-content | `def:hoefsmit-projector`, `conj:hoefsmit-ew-cell-content` | `QOU/Hoefsmit.lean` | 🟠 `conjecture` (n=6 disjoint-strand-pair) | 🟠 |
| 6b | Bar-self-dual cell-content trace identity | (implicit in `hecke_character_symbolic.py`) | (no Lean) | 🔴 `no_block_exists` | 🟡 |
| 7 | Frobenius pairing matrix `G` (master formula) | `def:frobenius-pairing` exists; **master formula `⟨O⟩_T = Σ u_i (G⁻¹)_{ij} ⟨O,b_j⟩` not in any block** | partial | 🔴 `no_block_exists` for the master formula | 🔴 |
| 8 | LP/SDP duality ↔ shadow prices (`y_λ`/`u_λ`) | `prop:bw-coefficient-shadow-price`, `prop:operator-selection-lp` | both `has_sorry` | 🟡 `has_sorry` | 🟠 |
| 9 | Gröbner-Shirshov filtration (GB normal forms) | `prop:gb-spectral-sequence` (asserts d_r = 0 for r≥3) | (no Lean) | 🔴 should be downgraded to `conj:` | 🔴 |
| 10 | Jet order on reduced words | `def:jet-order` — block missing | (none) | 🔴 `no_block_exists` | 🟡 |
| 11 | Hecke energy `E_𝔥 = 𝔪_𝔥 · c_q²` (𝔪 from `tr_M`) | `thm:knot-mass-formula-unified` (Ch 4) + `prop:atom-knot-mass-derivation` | `QOU/Torsion/MassIdentity.lean` | 🟡 `has_sorry` for `tower(T_w)` | 🟠 |
| 12 | Brane-tower correction (closes leptonic/hadronic 0.75% gap) | `conj:brane-tower-z-habiro` | `MassIdentity.lean` | 🟠 `conjecture` (Z-Habiro) | 🟠 |
| 13 | Canonical knot identification (input: (Z,N), output: K) | `conj:canonical-knot-id-sdp` | (no Lean) | 🟠 `conjecture`; **only A ≤ 3 implemented; via SnapPy lookup, not categorical** | 🔴 |

**Coverage:** Of 13 chain links, **6 are 🔴 critical-severity** (46%): #2, #3b, #5, #7, #9, #13. Two more (#6a, #11) are conditional on `conj:` classes.

## Per-link audit

### Link 1: Categorical action (rigid monoidal category)

- **Input:** none (axiomatic).
- **Output:** A rigid monoidal category `𝐂` with braiding `σ`, unit `𝟏`, dual `(−)^∨`.
- **Statement:** `𝐂` is a rigid braided monoidal category in the sense of Mac Lane / Kassel.
- **Block:** Glossary in Ch 8 (per CLAUDE.md §4b).
- **Lean:** Mathlib `CategoryTheory.MonoidalCategory.Rigid`, `CategoryTheory.Monoidal.Braided`.
- **Status:** ⚙ External (Mathlib).
- **Citation:** `wedderburn_pair_volumes.py`, `hecke_core.py`.
- **Audit:** OK.

### Link 2: Non-abelian Stokes ⇒ Wilson loop = `tr_M(monodromy)`

- **Input:** Categorical action + a connection 1-form `A` (vortex morphism `ϱ : 𝟏 → A`).
- **Output:** Closed-loop Wilson observable identified with the Markov trace of the holonomy braid.
- **Statement:** For any closed loop `γ` in the brane, `W(γ) = tr_M(σ(γ))` where `σ(γ) ∈ H_n(q)` is the holonomy braid.
- **Block:** `rem:yekutieli-stokes` (Ch 4) — **a remark, not a theorem**.
- **Lean:** none.
- **Status:** 🔴 `not_started`. The identification is asserted via Yekutieli's non-abelian Stokes (cited in narrative only).
- **[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-101]**
  - file: `content/quantum-observable-universe/braids-and-knots/yekutieli-stokes.md`
  - description: Wilson loop = `tr_M` is a remark; not formalised. **Steps 3–13 all implicitly depend on this identification.**
  - backing: NONE (only a remark)
  - remediation: Either (a) upgrade to `prop:wilson-loop-markov-trace` with Kohno–Drinfeld KZ-flatness proof; or (b) axiomatise as a Lean class and propagate conditional-class banner to all downstream blocks.

### Link 3a: Jones–Markov trace exists on `H_n(q)`

- **Input:** Hecke algebra `H_n(q)` with parameter `z = 1/(q^(1/2) + q^(-1/2))`.
- **Output:** Trace `tr_M : H_n(q) → ℂ(q)` satisfying Markov properties (M1: cyclic on `H_n`; M2: `tr_M(w·σ_n) = z · tr_M(w)` for `w ∈ H_n`).
- **Block:** `thm:jones-markov-trace`.
- **Lean:** External axiom; not derived in QOU.
- **Status:** 📥 External (Jones 1987 / Kassel 1995).
- **Audit:** OK as external axiom; should be cited via `-- Ref: [jones1987]` in any Lean stub that uses it.

### Link 3b: JSJ decomposition ↔ Wedderburn block decomposition

- **Input:** A link `L` with JSJ decomposition into Seifert + hyperbolic pieces.
- **Output:** A block decomposition of `H_n(q)` into Wedderburn summands indexed by JSJ pieces.
- **Statement (asserted in jsj_alpha_clustering.py):** Per JSJ piece `P`, contribute `ρ_F(P) · Vol_hyp(P)` to the binding-energy sum.
- **Block:** **none** — the claim is implicit in the jsj_alpha_clustering / jsj_verification scripts.
- **Lean:** none.
- **Status:** 🔴 `no_block_exists`. JSJ is used as an external SnapPy black box.
- **[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-102]**
  - file: `folio-assistant/computations/jsj_alpha_clustering.py`, `jsj_verification.py`
  - description: JSJ → Wedderburn map is the categorical lift of SnapPy's algorithmic JSJ; no block formalises this lift.
  - backing: NONE
  - remediation: Author `conj:jsj-wedderburn-correspondence` (cite Thurston, Neumann–Zagier). Status: open conjecture, OK to use SnapPy as black-box external.

### Link 4: Knot decomposition (link → braid → Hecke element)

- **Input:** A link `L` ⊂ S³.
- **Output:** A braid word `β ∈ B_n` (via Alexander), reduced to an element of `H_n(q)` via `(σ_i - q)(σ_i + q^{-1}) = 0`.
- **Statement:** Markov equivalence: two braids `β, β'` represent the same link iff connected by Markov moves M1 (conjugation in `B_n`) and M2 (stabilisation `B_n ↔ B_{n+1}`).
- **Block:** `def:hecke-algebra` + `thm:markov-equivalence` (Ch 4).
- **Lean:** `QOU/Hecke.lean` — partial; Markov-equivalence completeness has `sorry`.
- **Status:** 🟡 `has_sorry`.
- **[AUDIT-FLAG severity=high id=DEEP-2026-05-08-103]** — Markov-equivalence completeness `has_sorry`; cite [markov1936] and discharge.

### Link 5: Wedderburn decomposition of `H_n(q)` over `ℚ(q)`

- **Input:** `H_n(q)` as a `ℚ(q)`-algebra; partitions `λ ⊢ n`.
- **Output:** `H_n(q) ≅ ⊕_{λ⊢n} M_{f_λ}(ℚ(q))` (matrix-algebra decomposition, `f_λ` = number of SYT of shape λ).
- **Statement:** Generic semisimplicity (Hoefsmit 1974 / Murphy 1992).
- **Block:** Implicit in `wedderburn_pair_volumes.py:173-179` (computes block dims).
- **Lean:** **no Lean file**.
- **Status:** 🔴 `no_block_exists`.
- **[AUDIT-FLAG severity=high id=DEEP-2026-05-08-104]** — author `prop:wedderburn-decomposition-h-n-q` with `-- Ref: [hoefsmit1974]`.

### Link 6a: Partitions, hook lengths, Hoefsmit projectors

- **Input:** Partition `λ ⊢ n`, cell `(i,j) ∈ λ`.
- **Output:** Hook length `h_λ(i,j)`; Hoefsmit projector `e_λ ∈ H_n(q)`.
- **Block:** `def:hoefsmit-projector`.
- **Lean:** `QOU/Hoefsmit.lean`.
- **Status:** ⚙ definitional; computational use OK.
- **Audit:** OK.

### Link 6b: Bar-self-dual cell-content trace

- **Input:** A bar-self-dual element `tr_pure(w)` for `w` a single-strand power product.
- **Output:** Closed-form q-expansion: e.g. `tr_pure(σ_1^4 σ_3^6 σ_5^8) = 4(q^18 + q^{-18}) + 2(q^10 + q^{-10}) + (q^6+q^{-6}) + 3(q^2+q^{-2})`.
- **Block:** **implicit** in `hecke_character_symbolic.py` (PR #546).
- **Lean:** none.
- **Status:** 🔴 `no_block_exists`.
- **[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-105]** — author `prop:bar-self-dual-cell-content-trace` (closed-form proof straightforward via Hoefsmit).

### Link 7: Frobenius pairing matrix `G` and the master formula

- **Input:** Wedderburn block basis `{b_i}` of `H_n(q)`; partition projectors `{π_λ}`.
- **Output:** Gram matrix `G_{λ,i} = ⟨π_λ, b_i⟩_F` (Frobenius pairing); master formula for any observable on a bound state `T`:
  `⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i · (G^{-1})_{ij} · ⟨O, b_j⟩`
  where `A*(T)` is the LP active set.
- **Block:** `def:frobenius-pairing` exists. **The master formula is not in any block.** It appears only in CLAUDE.md and in `confinement-frobenius-reciprocity.md` narrative.
- **Lean:** partial.
- **Status:** 🔴 `no_block_exists` for the master formula.
- **[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-106]**
  - file: `content/quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md`, `folio-assistant/computations/lp_dual_solver.py`
  - description: The master formula is the *single most-cited* identity in bound-state observables (g_A, binding, Q-values), but it is asserted in narrative only; no `prop:` block, no Lean.
  - backing: NONE (referenced in 8+ scripts)
  - remediation: Author `prop:bound-state-master-formula` with proof from Frobenius reciprocity + LP-strong-duality. **This is the highest-leverage formalisation in the audit.**

### Link 8: LP/SDP duality ↔ shadow prices

- **Input:** LP `min Σ t_i x_i s.t. Σ n_i x_i = n_target, G x ≥ 0`.
- **Output:** Dual variables `y_0` (net), `y_λ ≥ 0` (Frobenius positivity); active set `A* = { i : y_λ[i] > 0 }`.
- **Block:** `prop:bw-coefficient-shadow-price`, `prop:operator-selection-lp`.
- **Lean:** both `has_sorry`.
- **Status:** 🟡 `has_sorry`.
- **Audit:** OK structurally. Master-formula link (#7) is the gap that gates these.

### Link 9: Gröbner-Shirshov filtration / spectral-sequence collapse

- **Input:** `H_n(q)` with the canonical GB.
- **Output:** Decomposition of mass observable into 6 terms (`prop:gb-spectral-sequence` says `d_r = 0` for `r ≥ 3` ⇒ collapse at `E_2`).
- **Block:** `prop:gb-spectral-sequence`.
- **Lean:** (no Lean file; not formalised).
- **Status:** 🔴 The collapse is **asserted, not proved**. The 6 terms are the *result* of running GB reduction in code; the spectral-sequence interpretation is post-hoc.
- **[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-107]**
  - description: Six-term decomposition is algebraically valid (q-rational expressions exist) but the *uniqueness* of the decomposition into these 6 specific terms is not proved.
  - remediation: Downgrade `prop:` → `conj:gb-spectral-sequence`; add a remark stating "alternative formulations may exist".

### Link 10: Jet order on reduced words

- **Input:** Reduced word `w` in GB normal form.
- **Output:** Jet order = lexicographic prefix length.
- **Block:** **missing**.
- **Lean:** none.
- **Status:** 🔴 `no_block_exists`. Used implicitly in `gb_filtration_jet_tracker.py` and `mass_formula_6term.py` term ordering.
- **[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-108]** — author `def:jet-order` + `prop:jet-tower-convergence` for semiclassical limit.

### Link 11: Hecke energy `E_𝔥 = 𝔪_𝔥 · c_q²`

- **Input:** Hadron `𝔥`; categorical mass `𝔪_𝔥 = | tr_M(T_𝔥) |` (with appropriate Wedderburn weighting).
- **Output:** Energy `E_𝔥 = 𝔪_𝔥 · c_q²` where `c_q = 1/(q-1)` is the q-deformed speed of light.
- **Block:** `thm:knot-mass-formula-unified` (Ch 4) + `prop:atom-knot-mass-derivation`.
- **Lean:** `QOU/Torsion/MassIdentity.lean`; has `sorry` for `tower(T_w)`.
- **Status:** 🟡 `has_sorry` (modulo Link 12).
- **Audit:** OK structurally.

### Link 12: Brane-tower correction

- **Input:** Discrepancy between leptonic energy scale `E_0^lept = m_e/(q_0(q_0-1))` and hadronic scale `E_0^had = Q_n / |Δ(net)|` ≈ 0.75%.
- **Output:** A series `tower(T_w)` (conjectured Z-Habiro at `q_0`) absorbing the gap.
- **Block:** `conj:brane-tower-z-habiro`.
- **Status:** 🟠 `conjecture`. Currently the tower is **defined to fit** the leptonic/hadronic gap — i.e. it is a calibration, not a prediction.
- **[AUDIT-FLAG severity=high id=DEEP-2026-05-08-109]**
  - description: Tower term is a free parameter calibrated to close the 0.75% gap. Must be labelled as such in the paper; otherwise the chain has 4 (not 3) calibration constants.
  - remediation: Either (a) prove tower coefficients from Z-Habiro structure; or (b) paper section explicitly admits 4-constant calibration.

### Link 13: Canonical knot identification

- **Input:** Atom `(Z, N)`.
- **Output:** Canonical knot/link `K(Z,N)` and Wedderburn-block coefficients.
- **Block:** `conj:canonical-knot-id-sdp`.
- **Lean:** none.
- **Status:** 🟠 `conjecture` for the SDP; for `A ≤ 3` the implementation is a **SnapPy nearest-volume search** (not categorical).
- **[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-110]**
  - file: `folio-assistant/computations/mass_table_ppb.py`, `folio-assistant/computations/jsj_alpha_clustering.py`
  - description: For D, T, ³He the knot is **chosen by census search** (closest SnapPy volume to target binding). This is a **retrodiction**, not a prediction. For ⁴He the rule is "magic A·8G". For ¹²C/¹⁶O the rule is α-cluster with c_αα calibrated to ¹²C. Net: **no atom in this baseline has its knot derived from (Z,N) alone**.
  - remediation: Implement the predictive direction of `conj:canonical-knot-id-sdp` (input (Z,N) → output K via categorical pipeline). Until then, every atom prediction must be labelled "knot census-assigned" or "calibrated".

## Where the chain "fits / guesses / uses numerology"

Per the user's prompt, the explicit fit/guess points across the chain are:

1. **Eigenvalue choice `(q, -q^{-1})` in Hecke relation** — chosen to match knot polynomials, not derived. *(Acceptable: it's a definitional choice; the choice is consistent with Jones' original construction.)*
2. **`q_0 = 1.10997...` from `m_μ/m_e`** — a fitted calibration constant. *(Acceptable: explicitly the substrate parameter.)*
3. **`E_0` from `Q_n`** — a fitted calibration constant. *(Acceptable IF acknowledged as the third constant; flag if presented as zero-parameter.)*
4. **Brane-tower correction** — defined to fit the leptonic/hadronic 0.75% gap. *(NOT acceptable as a "prediction"; this is a 4th hidden calibration.)*
5. **SnapPy census-assignment for D, T, ³He knots** — pure numerology (nearest-volume search). *(NOT acceptable; cf. DEEP-2026-05-08-110.)*
6. **A·8G "magic rule" for ⁴He** — heuristic. *(NOT acceptable as a derivation; cf. DEEP-2026-05-08-005.)*
7. **`c_αα = m_e · Vol(7²₁)`** — knot 7²₁ choice may be reverse-engineered from ¹²C. *(CRITICAL; cf. DEEP-2026-05-08-005, DEEP-2026-05-08-004.)*
8. **`ρ_F = m_e` vs `2·m_e` rule** — heuristic, no categorical derivation. *(NOT acceptable; cf. DEEP-2026-05-08-010.)*
9. **`n_chir(P) ∈ {1,2}` per JSJ piece** — heuristic, no categorical rule. *(NOT acceptable; cf. DEEP-2026-05-08-011.)*
10. **`Wedderburn weight scheme`** — 3 distinct formulas in 11 scripts (DEEP-2026-05-08-009).

## Critical-path gaps (must be addressed for 1-ppb)

In dependency order (each gates the next):

```
[#2 Yekutieli Stokes — remark only]
   ↓ gates
[#7 Frobenius master formula — narrative only]
   ↓ gates
[#8 LP-dual shadow prices — has_sorry]
   ↓ gates
[#13 Canonical knot ID (predictive direction) — conjecture, only retrodiction implemented]
   ↓ gates
[Every isotope binding-energy prediction]

[#3b JSJ ↔ Wedderburn — no block]
   ↓ gates
[#5 Wedderburn decomposition of H_n(q) — no Lean]
   ↓ gates (in parallel with #7)
[#7 Frobenius master formula]

[#9 GB spectral sequence collapse — asserted only]
   ↓ gates
[Six-term decomposition uniqueness]
   ↓ gates
[Term-by-term audit of mass_formula_6term predictions]

[#12 Brane-tower correction — conjecture, calibrated to fit]
   ↓ gates
[Hadronic mass identity claim]
```

## Conjectural-class chain (conditional results)

If the conditional-class exception (CLAUDE.md §3b-cond) is invoked for the open conjectures, then the conditional theorems would be:

- `prop:bound-state-master-formula [Stokes-CL] [JSJ-Wedd-CL] [Wedderburn-Decomp-CL]` ← #7
- `prop:atom-knot-mass-derivation [BraneTowerCorrection]` ← #11 (already conditional)
- `prop:canonical-knot-prediction [CanonicalKnotID-SDP]` ← #13

This bookkeeping is what enables the paper to honestly report "rigorous conditional on N open conjectures" rather than "ab initio".
