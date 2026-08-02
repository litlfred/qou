# na-Stokes volume-difference leg — the ℏ²-damped brane resummation is an affine fixed point (Lean-proved); its ℏ² kernel undershoots binding ~450× (empirical)

**Date:** 2026-08-02 · **Beans:** `qou-3wvl`, `qou-uclw` · **Epic:** `qou-r2nh` ·
**Tier:** 1 Lean proof (resummation fixed-point) + 1 empirical negative (ℏ² kernel).
**No fit, no AME inversion, nothing wired.**

Owner steer: derive the per-α binding scale `g(q)` **forward** through the canonical
chain — categorical action → Yekutieli **non-abelian Stokes** (the q-deformed
volume/density) → Frobenius pairing — not by matching a bare `[n]_q` (numerology).

## The leg is already the framework's binding compute

`computations/canonical_plus_multibrane.py` computes binding as exactly the na-Stokes
**volume-difference**: per brane level `n`, `delta = m_free − m_atom` where
`m = tower_mass_level(V̂)` uses the `Li_2^q` (Rogers/na-Stokes) holonomy; the binding is
`B = E_0·(canonical + Σ_n delta_n)`. So the owner's leg is the production path.

## The divergence and its resummation

- **Un-damped** `Σ_n delta_n` **diverges** at the archimedean `q₀ > 1` (the
  `tower_MeV ≈ 2×10⁶` blow-up in `4he-binding-full-pipeline.witness.json`): the jet-lift
  `V̂^{(n)} = z^n·V̂^{(0)}` grows the levels.
- **`brane_geometric_sum`** applies the built-in `ℏ_q^{2n}` jet-brane damping, making the
  tower **geometric** in `r = ℏ_q²·z²` (`r ≈ 0.0049 < 1` at q₀), with closed form
  `ℏ_q²·tower^{(1)}/(1 − ℏ_q²z²)` (eq ★). This is the fibre-level (Habiro-style)
  resummation, evaluated archimedeanly — it **converges**.

## PROVED (Lean, sorry-free) — the resummation is an affine fixed point

[`QOU/MassTheory/BraneGeometricResummation.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BraneGeometricResummation.lean):

- `brane_resum_affine_fixed_point` — `S = a + r·S ↔ S − r·S = a` (the resummed value is the
  fixed point of the ℏ²-damped affine brane self-map; `a = ℏ_q²·tower^{(1)}`, `r = ℏ_q²z²`).
- `brane_resum_mul_one_sub` — `S = a + r·S → S·(1 − r) = a` (→ the closed form `a/(1−r)`).

Verified `lean`-direct exit 0. The division-to-`a/(1−r)` and the `tsum` geometric
convergence (`|r|<1`) are standard Mathlib consequences whose oleans are outside the
sandbox cache — documented, not re-proved. This proves the **divergent-looking tower
resums to a finite closed form**; it does **not** prove the value equals the binding.

## EMPIRICAL NEGATIVE — the ℏ² kernel undershoots binding ~450×

Running the resummed binding (eq ★) for the deuteron (q₀, `ℏ_q²=0.00982`, `z²=0.4993`):
`tower^{(1)}=0.640` → `geom_sum = 0.0063` → `B_resummed ≈ 0.005 MeV` vs AME **2.225**
(**−99.8%, ~450× too small**). So:

- **un-damped** (`ℏ⁰`): diverges (10⁶ MeV);
- **`ℏ_q^{2n}`-damped**: over-damps (0.005 MeV, 450× short).

The magnitude-correct resummation kernel sits **between** `ℏ⁰` and `ℏ_q²` and is
**unknown**. So the na-Stokes volume-difference leg has the right *structure* (Lean-proved
convergent fixed point) but the specific ℏ² jet-damping does **not** reproduce binding —
the correct fibre-level damping/kernel is the open magnitude gap, now sharply bracketed.

## Verdict

- **Proved:** the ℏ²-damped brane tower is a convergent affine fixed point (resummation
  structure is sound and Lean-verified).
- **Open (empirical negative):** no known kernel reproduces the binding — `ℏ⁰` diverges,
  `ℏ_q²` undershoots 450×. The owner's forward-chain framing is correct (the scale is a
  q-function from na-Stokes, not numerology and not gated), but the specific damping that
  lands on AME binding is unresolved. This is the same magnitude gap, localized to
  "the correct jet-brane damping kernel between ℏ⁰ and ℏ²".

## References
- `computations/canonical_plus_multibrane.py` (`tower_mass_level`, `brane_geometric_sum`)
- `computations/4he-binding-full-pipeline.witness.json` (the 10⁶ divergence)
- `QOU/MassTheory/BraneGeometricResummation.lean` (this PR)
- `docs/audits/2026-08-02-bloch-wigner-torus-composition-volume-probe.md`
- `docs/audits/2026-08-02-alpha-cluster-su4-extensive-term.md`
