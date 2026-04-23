# JSJ + knot-Vol — Canonical Pipeline (1 ppb path)

*Decision (2026-04-23, post-PR-#390 merge): the JSJ + knot-volume + α-cluster pipeline is the canonical path for nuclear binding predictions. The per-operation Hecke-NF approach (`exact_binding_per_operation.py`) under-predicts by 85-99% across all atoms and is deprecated.*

## Pipeline overview

For each atom (Z, N):

1. **Atom braid** $\beta_{Z,N} \in B_{3A}$ (existing `atom_braid_word_3A`)
2. **Hecke NF** in $H_{3A}(q_0)$ via Gröbner-Shirshov reduction
3. **Link class** identified from NF (Markov equivalence)
4. **Hyperbolic 3-manifold** $K_{Z,N} = S^3 \setminus (\text{closure of link})$
5. **JSJ decomposition** into hyperbolic + Seifert pieces $\{P_\alpha\}$
6. **Per-piece volume** via SnapPy verified high-precision: $\text{Vol}_\text{hyp}(P_\alpha)$
7. **Frobenius packing density** per piece: $\rho_F(P_\alpha) = m_e(q_0) \cdot n_\text{chir}(P_\alpha)$
8. **Mass** $\mathfrak{m}(K_{Z,N}) = \sum_\alpha \rho_F(P_\alpha) \cdot \text{Vol}_\text{hyp}(P_\alpha)$
9. **Binding** $B(Z, N) = \mathfrak{m}(\text{free atom}) - \mathfrak{m}(\text{bound atom})$

For magic / doubly-magic atoms with α-cluster structure, use the unfolded form:

$$B(Z, N) = n_\alpha(Z,N) \cdot B(⁴He) + n_\text{pair}(Z,N) \cdot c_{\alpha\alpha}$$

with $c_{\alpha\alpha} = m_e(q_0) \cdot \text{Vol}(7^2_1)$.

## Status of canonical components

| component | status | precision target |
|-----------|--------|:----------------:|
| Atom braid → NF | implemented (Hecke reduction) | exact |
| NF → link class | **NOT YET** — currently empirical via SnapPy census | future |
| Link → SnapPy manifold | works for catalog matches | needs Step 2 |
| SnapPy verified volume | works (50+ digit) | trivially exact |
| Frobenius packing $\rho_F$ | proved at $q_0$ at 50 digits | exact |
| α-cluster decomposition | works (4He, 12C, 16O fit) | 0.1-6% |

## Why per-op NF is deprecated

`exact_binding_per_operation.py` produces:
- D: B_pred 0.016 vs AME 2.22 (−99%)
- T: B_pred 1.26 vs AME 8.48 (−85%)
- ⁴He: B_pred 0.66 vs AME 28.30 (−98%)
- All atoms: 85-99% under-prediction

The structural issue: per-operation NF computes $\sum_i \ln |\hat V_i|$ — a sum of LOGARITHMS — but the JSJ-additive volume formula needs $\sum_i V_i$ (sum of VOLUMES). These differ by $\exp$. The per-op pipeline is using the WRONG functional.

Reconciliation requires either:
- Apply $\exp$ to the per-op result to get the right magnitude (heuristic fix)
- Replace $\sum \ln |V|$ with $\sum |V|$ in the per-op formula (structural fix)
- Switch to the additive JSJ formula entirely (architectural fix — what we're doing)

The α-cluster + knot-Vol + Frobenius-packing-density approach gives the right magnitudes from first principles. **It is the canonical path.**

## Action plan to 1 ppb

### Phase 1 — Substrate pinning (DONE)
✓ `q_pinning_50_digit.py` pins $q_0$, $\hbar_q^2$, $\rho_q$, z_markov at 50 digits.
⚠ ξ(q₀) is NOT YET at 50 digits — the Descartes-curve placeholder was disabled; the 15-digit verified path exists in `lambda_descartes_q0.py` on main and must be ported.
✓ CODATA m_μ/m_e bound: 1.22e-9 relative on $q_0$. 1 ppb is at the EDGE.

### Phase 2 — Conjecture proofs (PARTIAL)
✓ `docs/locality-proof-attempt.md`: far-commuting case PROVED (Kohno-Drinfeld); adjacent case approximate to $O(\hbar_q^2)$.
✓ `docs/crossing-graded-proof.md`: formal series proved; resummation requires locality.
- **TO DO**: Pentagon defect computation for adjacent locality. Brings light atoms from 1.1% to ~100 ppm.

### Phase 3 — Atom-knot derivation (NOT YET)
- **TO DO**: implement Hecke NF → Markov-equivalence → unique link class.
- Currently empirical (SnapPy census search). Removing this step removes the leading source of error for D/T/³He.

### Phase 4 — High-precision SnapPy
- ✓ SnapPy installed, supports `M.high_precision()` for verified ~50-digit volumes.
- **TO DO**: integrate `M.high_precision().volume()` into `jsj_alpha_clustering.py`.

### Phase 5 — α-cluster refinement (NOT YET)
- ⁴He at +5.9% from $4 \cdot 8G$ — structural.
- ¹⁶O at +0.09% from 4α + 6 couplings — exceptional.
- ⁴⁰Ca at +14% — needs **next-level unfolding** (α-shell grouping).

### Phase 6 — End-to-end 1 ppb evaluation
With Phases 1-5 complete:
1. Pick atom (Z, N)
2. Derive link class (Phase 3)
3. SnapPy high-precision Vol (Phase 4)
4. Apply $\rho_F \cdot \text{Vol}$ at 50 digits (Phase 1)
5. For magic atoms, use α-cluster (Phase 5)
6. Compare to AME at framework precision (~1.22e-9 limited by CODATA)

## Realistic milestone schedule

| milestone | precision | timeline |
|-----------|:---------:|----------|
| ⁴He at 6% (current) | $6 \times 10^{-2}$ | DONE |
| ¹⁶O at 0.09% (current) | $9 \times 10^{-4}$ | DONE |
| D at 100 ppm via correct knot | $10^{-4}$ | Phase 3 |
| D at 1 ppm via pentagon corrections | $10^{-6}$ | Phase 2 + 3 |
| D at 100 ppb via crossing-graded | $10^{-7}$ | Phase 2 + 3 + 5 |
| D at 1 ppb (CODATA-limited) | $10^{-9}$ | All phases + better m_μ/m_e |

## Recommended execution order

1. **Phase 4** (high-precision SnapPy) — quick win, gives 50-digit Vol immediately.
2. **Phase 3** (atom-knot derivation) — biggest leap (1% → 100 ppm).
3. **Phase 5** (α-cluster refinement) — addresses heavy atoms.
4. **Phase 2** (pentagon defect) — pushes light atoms to ppm.
5. **Phase 1.5** (CODATA improvement) — wait for next CODATA release for sub-ppb.
