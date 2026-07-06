# Next session workplan (from claude/unit-modulus session, 2026-05-27)

## Priority 1: m_K/m_π = J₂₅/J₂₃ × (9/5)² derivation
- Match: 0.23% (3.545 vs CODATA 3.537)
- Jones ratio J₂₅/J₂₃ = 1.094 (algebraic, Hecke-derived)
- Seifert volume ratio 9/5 = (3π/5)/(π/3) (topological)
- Squaring: one per quark (qq̄ has 2 constituents)
- PROVE the squaring from the two-quark meson structure
- Scripts: meson_eigenvalue_analysis.py, meson_typed_crossing_probe.py

## Priority 2: Cherry-pick/integrate PR #1331
- Hoefsmit 2×2 matrices witness (open, complements σ₁-diagonal)
- Cross-validate against our eigenvalue table
- b² discrepancy: #1331 reports b²≈1.167 vs our proved b²=0.753
  → different convention (σ₂ rho=2 vs σ₁ rho=1). Reconcile.

## Priority 3: q₀ derivation (PR #1249)
- #1332 finding: figure-eight phase ≈ Vol(4₁) on (2,1)
  → connects spectral-collapse (Path a) to knot volume
- The unit-modulus theorem constrains: |λ|=1, phase = θ
  → if θ = Vol(4₁) is EXACT, then q₀ satisfying this = derivation
- Check: does acos(tr(ρ_{(2,1)}(4₁))/2) = Vol(4₁)?

## Priority 4: Stale PR cleanup
- #1259 (q-Schur): superseded by Habiro-exact. Close or heavy rebase.
- #1276 (Bring + compact-q-dilog): findings absorbed into main. Close or merge audit doc.
- #1224 (Δ_λ synthesis): Δ_λ = sgn×dim now proved. Close.
- #1317 (integration-watch): needs rebase, mechanical fixes.

## What's on main (key state)
- Dashboard: 4/6 beats 100× (m_e, m_μ, Q_β, Δ_pn)
- Q_β: 0.00 ppQ at N=4 (Habiro-exact)
- m_p/m_n: 242 ppb (need q₀ derivation)
- Lean: 91 sorry's (down from 272), BraidsAndKnots sorry-free
- Meson: symmetric dominance proved, unit-modulus + Borromean λ=-1
- Eigenvalue: b²=(h²+3)/(h²+4), c₂=-1, Habiro terminates M=8
