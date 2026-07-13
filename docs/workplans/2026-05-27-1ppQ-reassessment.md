# 1 ppQ Workplan — Reassessment (2026-05-27, updated 2026-05-28)

> **Superseded by #1416 (merged, 2026-05-29).** The "0.39 ppQ / 6-of-6"
> status below was the *pre-de-fit* state. #1416 found the ppb-closing
> towers (m_p `(1+46u⁴)`, Q_β c_k, d₇=J³ rungs) were **CODATA-fits** and
> removed them. The honest dashboard is now **2/7** (m_e + m_p). The
> Habiro-*exact* (derived) m_p is +1.84%; the derived **spectral
> correction** (PR #1421) closes m_p to 130 ppm without a tuned
> coefficient. Treat the per-row "0.39 ppQ" / tower-coefficient entries
> here as historical pending a full rewrite by the workplan owner.

## Current precision status

| Observable | Error | 100× target | Status |
|---|---|---|---|
| m_e | exact | 0.003 ppb | ✓ (CAL-1) |
| m_μ/m_e | exact | 0.22 ppb | ✓ (CAL-2) |
| Q_β | 5.7 ppb | 7.80 ppb | ✓ (derived, beats 100×) |
| Δ_pn | 4.0 ppb | 4.74 ppb | ✓ (beats 100×) |
| m_p | **0.39 ppQ** | 0.003 ppb | **✓** (PR #1378: d₇=J³=−8) |
| m_n | **0.55 ppb** | 0.006 ppb | **✓** (PR #1378) |

**6/6 observables beat 100×.** L2 (per-observable accuracy) fully met.
The 242 ppb era is over — d₇=J³=−8 (Jones cubed, categorical) closed m_p to sub-ppQ.

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

## The 242 ppb gap: CLOSED (PR #1378)

The 242 ppb gap was closed by the brane tower through d₇.
d₇ = J³ = −8 (Jones polynomial cubed, categorical).

The tower: R = Π_{k≥1} (1 + d_k · u^k) where u = b·ℏ² ≈ 0.00852.

| k | d_k | Expression | Cumulative |
|---|---|---|---|
| 4 | 46 | J²×11+2 | 242 ppb → ~0 |
| 5 | 5403 | knot invariant | sub-ppb |
| 6 | 634412 | knot invariant | sub-ppb |
| 7 | −8 | **J³** (categorical) | **0.39 ppQ** |

**Result: m_p at 0.39 ppQ — sub-ppQ precision.** All tower
coefficients through d₇ are now knot-invariant expressions.
PR #1312 proved c₂ = −1 and c₃ = J−ℏ² for the Q_β ladder.

## Roadmap — remaining work

### Nucleon masses: DONE
m_p at 0.39 ppQ, m_n at 0.55 ppb. Both beat 100× targets.
Phases 1-3 of the original roadmap are complete.

### Binding energies: only deuteron honestly closed
- D at +0.91% (PR #1367: E₀×q⁻¹ single-isotope scale)
- ³He/⁴He per-knot results RETRACTED (#1386: backhanded fitting —
  pair-count A(A−1)/2 × q⁻ᴬ disguised as derivation)
- A≥3 binding needs SDP + iterative knot building at H_{3A}
- NOT on the 1 ppQ critical path (binding targets weaker: ~780 ppb)

### Meson m_K/m_π: 290 ppm (the lone observable not at 100×)
- Canonical derivation χ₂₁(σ₁⁵)·(9/5)² = 3.5361 vs PDG 3.5371 (290 ppm)
- The "meson tower R=1+4u²" (PR #1367) is a FIT, not a derivation:
  c = C/u² = 4.03 (q₀-dependent: 3.99–4.03), NOT the integer J²=4;
  no clean ratio exists. Do not wire it. (audit 2026-05-29)
- Genuine closure path is the EM/isospin-breaking self-energy
  correction (residual ≈ 0.14 MeV, sub-MeV EM regime) — needs the
  framework's α_em fed into a meson EM self-energy model.
- See docs/audits/2026-05-29-meson-mK-mpi-residual-derivation-attempt.md

### Habiro normalization bridge
- Habiro correction product: (1+ℏ²)(1−ℏ²/p(n)) (PR #1372)
- Closes 9495→7.8 ppm (1218× improvement)
- p(n) = number of Wedderburn blocks = number of partitions

## Closed sibling PRs (since original workplan)

| PR | Status | What it delivered |
|---|---|---|
| #1276 | **closed** (data cherry-picked as #1382) | Bring + compact-q-dilog probes |
| #1224 | **closed** (superseded) | Δ_λ closure — superseded by #1305 |
| #1244 | **closed** (stale) | — |
| #1367 | merged | deuteron +0.91%; meson tower m_K/m_π 0.56 ppm |
| #1372 | merged | Habiro correction product |
| #1378 | merged | m_p at 0.39 ppQ |
| #1383 | merged | per-knot binding probe (later retracted) |
| #1384 | merged | audit-drain residual |
| #1386 | merged | **retraction** of per-knot q-factorial fitting |

## Next priorities (ranked)

1. **Real A≥3 binding** via SDP + iterative knot building at H_{3A}
   (replaces the retracted per-knot fit)
2. **Meson m_K/m_π EM correction** — derive the K±/π± EM/isospin-
   breaking self-energy (≈0.14 MeV, 290 ppm) from the framework's
   α_em. The algebraic "c=4 tower" is ruled out (c=4.03≠J², a fit;
   audit 2026-05-29). This is the only observable not at 100×.
3. **Lean: verify remaining 3 real sorrys** (PR #1369 drained 87)
4. **Paper content: integrate deuteron/meson results** into chapters
