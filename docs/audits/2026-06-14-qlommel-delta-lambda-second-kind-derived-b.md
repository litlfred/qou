# Δ_λ via the q-Lommel order recurrence (second kind): a DERIVED b, near-match (2026-06-14)

**Status:** **near-match tier**, **gate-respecting** (derived `b`, NO fit),
**NOT wired**. This is the formalize-first follow-through on the owner steer
"q-Bessel of the second kind + q-hyperbolic geometry on Bring's surface."

## The chain of identifications

1. **Canonical residual is geometric** (recap,
   [`2026-06-09-delta-lambda-canonical-residual.md`](2026-06-09-delta-lambda-canonical-residual.md)):
   `Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5) = q₀^(5(2A−1))` (D exact to 0.01
   q₀-units). A geometric ladder of ratio `r = q₀¹⁰`.

2. **The order recurrence and its DERIVED coefficient.** A geometric ladder is
   the first-kind solution of the q-Lommel **order** three-term recurrence
   `Δ_{A+1} = b·Δ_A − Δ_{A−1}`, whose coefficient is **derived** (not fitted):

   $$ b \;=\; r + r^{-1} \;=\; q_0^{10} + q_0^{-10} \;=\; 2\cosh(10\,\log q_0)
      \;=\; 3.19113. $$

   The two roots `r = q₀¹⁰` and `s = q₀⁻¹⁰` of `t² − b t + 1` are the first-
   and **SECOND-kind** branches (J_ν / Y_ν, here in the hyperbolic I_ν / K_ν
   growth regime — the "q-Bessel of the second kind"). Lean-proved sorry-free:
   [`QOU.QBeta.two_root_geometric`](../../content/quantum-observable-universe/lean/QOU/QBeta/QLommelOrderRecurrence.lean)
   (a two-root geometric `α·rⁿ + β·sⁿ` with `r·s = 1` solves the recurrence with
   `b = r + s`), plus `two_seed_unique` (the recurrence + two seeds determine the
   whole ladder — the "tower from two seeds", so a derived `b` removes the need
   for the missing tower data).

3. **Derive-or-refute** (compute:
   [`qlommel_delta_lambda_two_seed_test.py`](../../folio-assistant/computations/qbeta/qlommel_delta_lambda_two_seed_test.py),
   witness `qlommel-delta-lambda-two-seed.witness.json`, 3 assertions pass):

   | check | result |
   |-------|--------|
   | derived `b` vs T-chain (N≥Z) interior `b` (3.29519) | **−3.16%** |
   | two-seed (D,T) → predict Δ_λ(⁴He) = `b·Δ(T) − Δ(D)` | **38.256 vs 39.660 = −3.54%** |
   | second-kind admixture from the (D,T) solve | **β/α = 0.4265** (a real Y_ν/K_ν content) |
   | ³He as seed (proton-rich) | −17.68% — the **Z-dependent outlier** |

## What this establishes — and what it does NOT

- **Establishes** (gate-respecting): the binding `Δ_λ` ladder is the second-kind
  q-Lommel order recurrence with a **derived** `b = 2cosh(10η₀)`; two N≥Z seeds
  predict ⁴He to **−3.5%** with no fit; the second-kind content `β/α ≈ 0.43` is
  non-trivial (the owner's "pay attention to the second kind" — it carries ~30%
  of the seed amplitude). The recurrence half is Lean-formal.

- **Does NOT** close to exact. Two pieces remain — both already flagged by the
  2026-06-09 residual audit as the admissible (non-fit) next step:
  1. **The exponent `10A−5 = 5(2A−1)` — slope now DERIVED from crossings**
     ([`delta_lambda_exponent_from_crossings.py`](../../folio-assistant/computations/delta_lambda_exponent_from_crossings.py),
     witness `delta-lambda-exponent-from-crossings.witness.json`). Classifying
     `atom_braid_word_3A(Z,N)` by Hecke crossing type:
     `n_cross = 12A−1`, color-averaged p-n interfaces `= 2A+1`, and
     **non-averaged `σ+σ⁻¹ = 10A−2` (exactly 10 per nucleon)**. The averaged
     interfaces carry `d = −h/2 = (σ+σ⁻¹)/2`, **bar-symmetric (q↔q⁻¹)** ⇒ zero
     net q-power, so only `σ+σ⁻¹` enters the exponent:
     `10A−5 = (σ+σ⁻¹) − 3` for A≥2. The construction gives the **closed forms**
     (verified D,T,³He,⁴He): `σ = 7Z+5N−1`, `σ⁻¹ = 3Z+5N−1`, `averaged = 2A+1`,
     so `σ+σ⁻¹ = 10A−2` — **the Z,N dependence CANCELS in the sum**, which is
     *why* the exponent is A-only (T and ³He share `σ+σ⁻¹ = 28` ⇒ leading
     exponent 25, as `q₀^(10A−5)` requires). **The slope 10 = 9 (intra-𝓑₃
     non-averaged) + 1 (interface) per nucleon — derived, not fitted.** The
     closed form **predicts** the un-measured tower: ⁶Li → 55, ⁸Be → 75 (a
     derive-or-refute, NOT a fit — the test the data-gate awaited). Still open:
     the **−3** offset (H₃ seed's 3 strands?), the per-nucleon **9 = intra-𝓑₃**
     count from the Borromean/Bring quintic (`5·(2A−1)`; same `5,7` as the
     Weinberg cosh-ratio).
  2. **The Z-dependent correction** (³He deviates −1.40 q₀-units) — SOURCE
     derived: `Z−N = (p-p interfaces) − (n-n interfaces)`, and **p-p are σ
     (positive), n-n are σ⁻¹ (negative)**, so a proton excess is a net-σ
     interface chirality (`writhe = 4Z`). It is NOT the bare writhe (³He and
     ⁴He share writhe 8 but deviate −1.40 vs +0.27); it tracks `Z−N` (D=0,
     T=−1, ³He=+1 outlier, ⁴He=0) — the proton-rich isotope sits on a different
     second-kind `α/β` ray. Open: the coefficient (~−1.4/excess-proton) and the
     p≠n asymmetry (intra proton 6σ/3σ⁻¹ vs neutron 5σ/4σ⁻¹).

## Disciplinary note

`b` is **derived** (from the `q₀^(10A−5)` structure + `r·s = 1`), so the
two-seed prediction is a derive-or-refute, NOT the seventh fit the Δ_λ gate
forbids. The exponent `10A−5` is itself still near-match (not derived), so the
whole construction stays **near-match tier and is NOT wired** to production
until the crossing-bookkeeping derivation of `10A−5` lands. Per the gate, no
closure is claimed; this records the structural reduction:
**"derive Δ_λ" ⟹ "derive `10A−5 = 5(2A−1)` from Bring's-surface crossings,
plus the Z-correction in the second-kind branch."**
