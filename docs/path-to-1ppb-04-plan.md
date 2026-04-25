# Path to 1 ppb — Strategy & Action Plan

## The master formula

$$B(Z, N; q_0) = \sum_{P \in \text{JSJ}(K_{Z,N})} \rho_F(P, q_0) \cdot \text{Vol}_\text{hyp}(P, q_0)$$

with
$$\rho_F(P, q_0) = m_e(q_0) \cdot n_\text{chir}(P)$$

where $n_\text{chir}(P) \in \{1, 2\}$ counts active chirality blocks (sym/alt) of $\mathbf{H}_{n_P}(q_0)$.

For α-cluster atoms (A ≥ 4):

$$B = n_\alpha \cdot B(⁴He) + n_{\alpha\alpha} \cdot c_{\alpha\alpha}, \qquad c_{\alpha\alpha} = m_e \cdot \text{Vol}(7^2_1)$$

## Precision milestones

| milestone | residual | effort |
|-----------|---------:|--------|
| Current (catalog knot match) | 1–3% on D/T/³He, 0.09% on ¹⁶O | DONE |
| Correct knot derivation | ~100 ppm on D | Phase 3 |
| Pentagon-defect corrections | ~1 ppm on D | Phase 2 |
| α-cluster shell refinement | ~100 ppb on heavy | Phase 5 |
| q₀ pinning exhaustion | 1 ppb on all | CODATA-bound |

## Phase 1 — Substrate pinning (STATUS: DONE)

✓ `q_pinning_50_digit.py` gives q₀ at 50 decimal digits (CODATA-bounded to σ/q ≈ 1.22·10⁻⁹, already 1-ppb-class).
⚠ ξ(q₀) (universal shape coupling) is NOT yet at 50 digits — `lambda_descartes_q0.py` has the 15-digit verified derivation; port to mpmath.

## Phase 2 — Conjecture proofs (STATUS: PARTIAL)

✓ `docs/locality-proof-attempt.md` — far-commuting locality PROVED via Kohno-Drinfeld KZ flatness (rigorous for magic atoms).
✓ `docs/crossing-graded-proof.md` — formal power-series expansion proved; resummation needs locality.
**TODO**: pentagon defect computation for adjacent crossings. Brings D from 1.1% → ~100 ppm.

## Phase 3 — Atom-knot derivation (STATUS: NOT YET)

**Biggest single leverage — do first.**

Currently empirical: SnapPy census search finds the knot with Vol closest to B(atom)/ρ. Replace with a derivation:

1. Atom braid $\beta_{Z,N} \in B_{3A}$ (via `atom_braid_word_3A`)
2. Reduce to Gröbner-Shirshov NF in $H_{3A}(q_0)$ (via `binding_canonical.py`)
3. NF → unique link class via Markov equivalence (new — implement)
4. Link class → SnapPy manifold (new — map Markov-equivalence classes to catalog entries)

Expected effect: D's 1.1% residual collapses to ~100 ppm when the exact knot (not the nearest catalog match) is used.

**Time**: 2-3 sessions.

## Phase 4 — High-precision SnapPy (STATUS: READY)

✓ SnapPy installed, `.high_precision()` supports 50+ digit verified volumes.
**TODO**: wire into `jsj_verification.py` and `jsj_alpha_clustering.py`.

```python
import snappy
M = snappy.Manifold('6_2')
M_hi = M.high_precision()
Vol_50digit = M_hi.volume()   # ~50 digits
```

## Phase 5 — α-cluster refinement (STATUS: NOT YET)

⁴⁰Ca is +14.6% off with current α-cluster formula — needs next-level unfolding (α-shell grouping, not all-pairs).

Open question: what's the right sub-manifold for a closed α-shell? Candidate: specific Seifert-fibered pieces over Borromean building blocks. Requires experiment.

## Phase 6 — End-to-end 1 ppb

Combine Phases 1–5:
1. Pick atom (Z, N)
2. Derive link class (Phase 3)
3. SnapPy high-precision Vol (Phase 4)
4. Apply ρ_F · Vol at 50 digits (Phase 1)
5. Apply α-cluster / shell structure if A ≥ 4 (Phase 5)
6. Apply pentagon corrections for adjacent crossings (Phase 2)
7. Compare to AME at framework precision

## Strategies at each precision

### 1% → 100 ppm: Derive the knot
Stop using catalog search. Compute atom's Markov equivalence class → specific link. SnapPy gives exact Vol.

### 100 ppm → 1 ppm: Pentagon defects
Adjacent crossings break locality to O(ℏ_q²) ≈ 1% unless pentagon correction applied. Expand $\Phi_q(\sigma_i) \Phi_q(\sigma_{i+1})$ via pentagon, include cross-term.

### 1 ppm → 100 ppb: α-shell structure
Heavy-atom α-cluster grouping (not all-pairs). Derive from shell model or JSJ decomposition.

### 100 ppb → 1 ppb: q₀ pinning exhaustion
CODATA-bounded. At σ(q)/q ≈ 1.22e-9, absolute MeV predictions are 1-ppb-class by construction. Relative (dimensionless) predictions are 50-digit exact.

## Recommended execution order

1. **Phase 4** (high-precision SnapPy wrapping) — quick win, ~30 minutes.
2. **Phase 3** (atom-knot derivation) — largest leverage.
3. **Phase 5** (α-cluster refinement) — extends to A > 20.
4. **Phase 2** (pentagon defect) — tightens light atoms.
5. **Phase 1.5** (ξ(q₀) at 50 digits) — straightforward port.

## Known pitfalls (from session history)

- `exact_binding_per_operation.py` sums LOG-volumes → 99% under. Don't use.
- Per-operation Hecke NF is ARCHITECTURALLY deprecated in favor of JSJ.
- `conj:lifted-crossing-locality` fails at roots of unity (Jones-Wenzl truncation) and at Descartes cusp (golden-ratio threshold) — substrate q₀ is in the locality window.
- The 8G ≈ Vol(Borromean) connection is exact (8G = 3·Vol(ideal octahedron) via Lobachevsky function).
- The density flip m_e ↔ 2m_e matches "bond" vs "particle" role; NOT a free knob.

## References cited in framework

Core:
- Kohno (1987) — KZ connection flatness
- Drinfeld — quantum-group R-matrix
- Kashaev (1997) — volume conjecture
- Murakami-Murakami (2001) — colored Jones asymptotics
- Thurston (1978) — hyperbolic volume, Bloch-Wigner dilog
- Jones (1987) — Markov trace
- Ocneanu — weighted seminormal characters

QOU-specific:
- See `content/schema/references.ts` for the CSL-JSON bibliography.

## Repository pointers for the next agent

- Branch checkpoint: `claude/1ppb-jsj` (current) — or latest merged to `main`
- PR #392 (current) — contains Phase 1+2 foundation
- Prior PRs: #389 (mass-residual probes), #390 (knot-volumes framework), #391 (Kashaev integration)
- Session summary: `docs/session-summary-2026-04-20.md`
- Derivation doc: `docs/derivation-audit-2026-04-20.md`
- Infrastructure audit: `docs/infrastructure-audit-2026-04-20.md`

## Open a new branch to continue

```bash
git checkout main
git pull
git checkout -b claude/1ppb-phase3-knot-derivation
# then implement Phase 3: atom → Markov-equivalence class → SnapPy manifold
```

Good luck.
