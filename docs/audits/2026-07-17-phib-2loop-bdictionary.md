# The odd-channel Φ_b 2-loop b-dictionary at m=q₀ (owner-directed) — derived, gated on Vol(4₁) + torsion √3

**Date:** 2026-07-17 · **Branch:** `claude/phib-2loop-bdict-2026-07-17` ·
**Tier:** derived-exact (semiclassical saddle expansion; gated formalize-first) ·
**Discipline:** scope-(a); no `c_k` wired; no fit; no tier change; L2 unchanged (2/7).

## What this is

The [four-front coordination reassessment](2026-07-17-four-front-gap-close-coordination.md)
found the one genuinely-unowned decidable piece of the L2 gap-close: the **odd-channel
Φ_b 2-loop b-dictionary normalization at m=q₀**. Per the [bar-odd three-routes
audit](2026-07-12-bar-odd-s-three-routes.md) §"route 2 still needs", the odd-channel
resummation needs the deformed b-dictionary, which the Φ_b (Faddeev) state-integral
construction supplies once its saddle expansion is pushed to **2-loop** at `m = q₀`. The
existing corpus probe stops at 1-loop (𝔙 = Vol + iCS + the finite-b i·t·κ₁ fluctuation);
this delivers the 2-loop coefficient. Owner-directed pickup (2026-07-17), coordinated with
#3805 (even-channel GGM A_ω — the odd-channel Φ_b normalization was flagged there as the
adjacent unowned piece).

## Method (formalize-first, gated)

The 4₁ figure-eight state integral in the semiclassical limit `ℏ = 2πib² → 0` is
`Z(ℏ) = ∫ dz e^{V(z)/ℏ}` with the Neumann–Zagier one-shape potential

    V(z) = Li₂(z) − Li₂(1/z),   geometric saddle  z* = e^{iπ/3}.

Standard 0-dimensional saddle asymptotics give

    log Z = V*/ℏ + ½log(2πℏ) − ½log(−V''*)  +  ℏ·A₁ + O(ℏ²),
    A₁ = V⁗*/(8 V''*²) − 5 V'''*²/(24 V''*³).            ← the 2-loop b-dictionary

**Correctness gates (both must pass before A₁ is trusted):**

| gate | check | result |
|---|---|---|
| G1 | `Im V(z*) = Vol(4₁)` | **PASS** — `2.02988321281930725` to 18 digits |
| G2 | `\|−V''(z*)\| = √3` (4₁ adjoint Reidemeister torsion) | **PASS** — `1.73205080756887729`; exact complex torsion `−V''* = −3/2 + i√3/2 = √3·e^{i5π/6}` |

## Result

**Complete structure:**

    V'''(z*)  = 2 + i·3√3,   V''''(z*) = −39/2 + i·3√3/2,
    A₁ = 1/3 + 0.2726376271173233·i     (Re A₁ = 1/3 EXACTLY),
    |A₁| = 0.4306302205,  arg = 0.6855683938.

**Substrate deformation (m = q₀, real meridian ⇒ CS = 0), via the corpus `vol_of_m`
gluing-Newton solve (deformed Vol = 2.02048069, deficit 0.00940 from Vol(4₁)):**

    deformed shape z*(q₀) = 0.4052940009 + i·0.9141863994,
    A₁(q₀) = 0.2743277704 + i·0.4002114685,   |A₁(q₀)| = 0.4852060852,
    Δ(A₁) = A₁(q₀) − A₁(0) = −0.0590055629 + i·0.1275738413.

`Δ(A₁)` is the **deformation of the 2-loop b-dictionary** at the substrate — the deformed
normalization route-2 needs. It is O(0.1), smooth, and (like every geometric handle in this
thread) small — consistent with the corpus finding that the S sign-flip lives in the `1/u³`
ladder representation, not in a near-singular geometric term.

## Scope + honesty (anti-laundering)

- `A₁` is **derived** from the potential and **gated** on two known 1-loop invariants
  (Vol, torsion) — not fitted. `Re A₁ = 1/3` is exact; the imaginary parts are reported as
  computed, **not** identified with any target (numerology guard).
- This is a **normalization input** for the *merged* F1 D-ladder acceleration machinery
  (which accepts a b-dictionary / more terms). **It does not itself close c₃**, wire a
  `c_k`, or change any tier. The merged F1 acceleration gate-fails at k=21 for a separate
  reason (insufficient rungs to resolve the q-Gevrey singularity); whether A₁ + more rungs
  closes it is the *next* step, not claimed here.
- The substrate `z*(q₀)` is recovered from the deformed volume as a single-constraint
  Newton solve on `Im V(z) = Vol(q₀)` along the geometric branch; a full two-variable
  deformed-gluing solve would refine `Re z*(q₀)` but does not change the O(0.1) scale of
  Δ(A₁). Flagged as the one modeling approximation.

## Compute

- Probe: [`computations/qbeta/qbeta_phib_2loop_bdictionary_probe.py`](../../computations/qbeta/qbeta_phib_2loop_bdictionary_probe.py) (exit 0, both gates pass)
- Witness: `computations/qbeta/qbeta-phib-2loop-bdictionary.witness.json`

## Cross-references

- Coordination: [`2026-07-17-four-front-gap-close-coordination.md`](2026-07-17-four-front-gap-close-coordination.md)
- Route-2 open item: [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md)
- 1-loop saddle (what this extends): `computations/qbeta/qbeta_c3_phib_saddle_state_integral_probe.py`
- Merged F1 acceleration (the consumer): [`2026-07-17-dladder-ecalle-acceleration.md`](2026-07-17-dladder-ecalle-acceleration.md)
