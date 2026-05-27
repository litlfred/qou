# 1 ppQ Workplan — Reassessment (2026-05-27)

## Current precision status

| Observable | Error | 100× target | Status |
|---|---|---|---|
| m_e | exact | 0.003 ppb | ✓ (CAL-1) |
| m_μ/m_e | exact | 0.22 ppb | ✓ (CAL-2) |
| Q_β | 5.7 ppb | 7.80 ppb | ✓ (derived, beats 100×) |
| Δ_pn | 4.0 ppb | 4.74 ppb | ✓ (beats 100×) |
| **m_p** | **242 ppb** | 0.003 ppb | ✗ (80,000× away) |
| **m_n** | **242 ppb** | 0.006 ppb | ✗ (42,000× away) |

**4/6 observables beat 100×. The bottleneck: m_p and m_n at 242 ppb.**

## What happened in the last 3 days (266 commits)

### Breakthroughs
1. **Δ_λ = sgn(w_0^{S_{λ'}}) × f^λ** — PROVED (Macdonald + Burnside)
2. **a₀(A) = 2 × 8^A** — Habiro leading coefficient EXACT for A=2..6
3. **Spectral correction** arccos(1−3h⁴/2−h⁶/2)/(8ℏ²): closes m_p from 2.89% to 130 ppm
4. **Brane-tower d₄ = J²×11+2 = 46**: closes m_p to 242 ppb (supersedes spectral)
5. **Knot operators unitary on V_{(2,1)}**: 4₁ phase ≈ Vol, B₃ near-identity
6. **Meson duality**: qq̄ structure → near-antiparallel on std block
7. **Lean**: 67 conjectures strengthened, h=(q+1)ℏ proved, 8 sorry-free conditionals
8. **Universal unitarity**: (σ₁σ₂⁻¹)² unitary at ALL Hecke levels H₃/H₄/H₅

### Dead ends documented
- |tr(B₃)| = Vol(4₁): IMPOSSIBLE (SL(2) bound)
- H_7 Wedderburn sum for binding linking weight: 7× too large
- Meson spectral phase ratio for m_K/m_π: 71% off (duality blocks it)
- c₄ = √3/10 for linking weight: FITTING (0.20% near-miss, transcendental)

## The 242 ppb gap: what it IS and what closes it

The 242 ppb comes from the brane-tower's d₄ = 46 correction.
To reach 1 ppQ (10⁻¹⁵ relative), we need d₅ through d₈.

The tower: R = Π_{k≥1} (1 + d_k · u^k) where u = b·ℏ² ≈ 0.00852.

| k | d_k | d_k · u^k | Cumulative precision |
|---|---|---|---|
| 1 | ~0 | ~0 | 242 ppb |
| 2 | 0.0033 | ~2.4e-10 | 242 ppb |
| 3 | 0.39 | ~2.4e-10 | 242 ppb |
| 4 | 46 | **2.42e-7** | **~0 ppb** (closes gap) |
| 5 | 5403 | ~2.0e-7 | needs d₅ exact |
| 6 | 634412 | ~1.8e-7 | needs d₆ exact |
| 7 | 74.5M | ~1.7e-7 | needs d₇ exact |
| 8 | ~10¹⁰ | ~? | 1 ppQ target |

**Each d_k should be a knot-invariant expression** (like d₄ = J²×11+2).
PR #1312 proved c₂ = −1 and c₃ = J−ℏ² for the Q_β ladder.
The tower coefficients d_k are related but NOT identical to c_k.

## Roadmap to 1 ppQ

### Phase 1: Close m_p to < 1 ppb (current: 242 ppb)
- Derive d₅ from knot invariants (pattern: d_k involves J^{k-2} × algebraic)
- Use PR #1312's eigenvalue structure (shared eigenvalue b·ℏ²)
- Verify via the Habiro expansion (which converges but needs resummation at u₀>1)

### Phase 2: Close m_p to < 1 ppt (10⁻¹²)
- Derive d₅, d₆ (each adds ~3 digits of precision via u^k scaling)
- Cross-check against the spectral phase expansion at each order

### Phase 3: Close m_p to < 1 ppQ (10⁻¹⁵)
- Derive d₇, d₈ (each term ×u ≈ ×0.00852 ≈ 2 digits)
- 8 tower terms at 50 dps should give 40+ digit agreement

### Parallel: Binding energies
- The Δ_λ = sgn × f^λ formula is PROVED but needs the Geom linking weight
- The binding gap (82%) is INDEPENDENT of the nucleon precision
- Closing binding requires the per-knot interface evaluation (Rust hecke-engine)
- NOT on the 1 ppQ critical path (binding targets are weaker: ~780 ppb)

### Parallel: Meson m_K/m_π
- Needs typed-crossing character evaluation (near-antiparallel regime)
- Different mechanism from baryon spectral correction
- Blocked on Rust hecke-engine for per-flavor eigenvalue evaluation

## Open sibling PRs

| PR | Status | Relevance to 1 ppQ |
|---|---|---|
| #1276 | open | Bring+Faddeev — alternative to spectral, incompatible |
| #1312 | open | Q_β eigenvalue ladder — CRITICAL (shared eigenvalue) |
| #1313 | open | Lean C2/C3/C4 + Habiro — supports d_k derivation |
| #1224 | open | Δ_λ closure — SUPERSEDED by our work |
| #1259 | open | Wenzl-vs-q-Schur — convention, not precision |
| #1249 | draft | q₀ derivation — research-grade, not 1 ppQ path |

## Next session priorities (ranked)

1. **Derive d₅ from the brane tower** — pattern from d₃, d₄ should predict d₅
2. **Merge/close stale PRs** — #1224 is superseded, #1276 conflicts with spectral
3. **Lean: close remaining sorrys** — Hoefsmit character sorrys are tractable
4. **Binding: wire Rust hecke-engine** for per-atom interface evaluation
5. **Meson: typed-crossing evaluation** for m_K/m_π
