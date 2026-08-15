# Charm mass: derive-then-check of the complex-mass tower_law (negative)

**Date:** 2026-08-02
**Scope:** `conj:complex-mass-constituent-functional` (QOU.MassTheory.ComplexMassConstituent), PR #4584.
**Trigger:** author request to attempt (1) the operator-selection SDP for gg→cc̄ and (2) the complex-mass functional closure.

## What was attempted

The two open steps to actually produce a charm mass from the complex-mass scaffold:

1. **Operator-selection SDP** for the gg→cc̄ channel — which knot-operator the two-gluon demand profile selects.
2. **Close the mass functional** — evaluate `charm_block_determined`: `M(proj 5 s) = contRatio(5)·M(proj 3 s)`, with `contRatio` the plain Morgan–Voyce / Fibonacci continuant ratio `b_n/b_{n-2}`, and compare `Re(block)` to the observed charm/light hierarchy.

## Step 1 — blocked (two independent gaps)

- **No solver in-environment.** numpy / sympy / cvxpy are absent in the sandbox Python; `solve_psd_operator_selection_sdp` cannot run here.
- **No derived demand profile (the real gap).** The two-gluon demand vector for gg→cc̄ is **not derived anywhere in the corpus**. Constructing it is itself open research; inventing one to feed the SDP would be a fit. So step 1 is blocked at the framework level, not just the tooling level.

## Step 2 — clean scope-(a) negative

`computations/charm_mass_tower_probe.py` (pure Python), witness `charm-mass-tower.witness.json`:

| quantity | value |
|---|---|
| substrate argument `X = [2]_q = q₀ + 1/q₀` | 2.011 |
| `contRatio(5)` at substrate | **5.85** |
| `contRatio(7)` at substrate | 5.87 (≈ contRatio(5) → nearly geometric ladder) |
| observed `m_c/m_u` (current) | 577 → needs `X ≈ 24` |
| observed `m_c/m_d` (current) | 270 → needs `X ≈ 16` |
| observed constituent `m_c/m_light` | 4.46 → needs `X ≈ 1.65` |

**Verdict (scope-(a)):** the plain-continuant-ratio reading of `contRatio` is **refuted as the sole hierarchy mechanism**. At the substrate it gives a nearly *n-independent* ~5.85×-per-generation **geometric ladder**, which matches **neither** mass scheme: it undershoots the current-mass charm/light hierarchy by ~100× (would need `X≈24`, wildly off the substrate `X≈2`), and overshoots the constituent-mass ratio by ~30%. The observed quark hierarchy is not a constant continuant ratio.

**This is scope-(a), not (b).** It refutes `contRatio = b_n/b_{n-2}` as the *whole* story; it does **not** exclude the complex-mass functional. The missing steepness could live in the complex-volume / Chern-Simons **imaginary** part (untested here — no solver, and the composite charmed-hadron braid's complex volume is underived), or `contRatio` could be a non-continuant categorical object. Both are open.

## Consequence for the scaffold (PR #4584)

The Lean class stands (it does not assert `contRatio = b_n/b_{n-2}`; that identification is narrative). But the natural first guess for `contRatio` is now **empirically excluded** at the substrate, sharpening the open closure: a viable `contRatio` must be either steeper-than-continuant (current scheme) or carried by the Im/CS part. No charm mass is predicted; `m_c` remains OPEN.

## Follow-up ("go" — the Im/CS handle): the carrier is scope-(b) excluded

The step-2 negative pointed to the complex-volume **imaginary (Chern–Simons)**
part as the possible source of the missing steepness. Applied to the **carrier**
knot $T_{3,5}$, this is now structurally excluded:

- **$T_{3,5}$ is a torus knot** (it is $10_{124}$, the $(3,5)$-torus knot).
- **Torus knots are non-hyperbolic**, so $\mathrm{Vol}(T_{3,5}) = 0$ — the real
  part of any complex-volume reading of the carrier is **identically zero**
  (no mass from $\mathrm{Re}$).
- **Torus-knot Chern–Simons invariants are rational**, bounded $O(1)$ (values in
  $\tfrac{1}{4pq}\mathbb{Z} \bmod 1$ for $T_{p,q}$) — the imaginary part is a
  bounded rational, not a GeV-scale quantity.

**Scope-(b) exclusion (cite the invariant: torus knots are non-hyperbolic,
$\mathrm{Vol}=0$, $\mathrm{CS}\in\mathbb{Q}$).** *Neither* the real *nor* the
imaginary part of the **carrier** $T_{3,5}$'s complex volume can be the charm
mass. This is stronger than step 2's scope-(a) result and is a permanent
structural fact, not a numerical near-miss.

**Consequence — the open problem is now sharp.** The charm mass, if it is a
complex-volume functional at all, must be the complex volume of the **composite
charmed-hadron braid** (e.g. a $\Lambda_c$ or $D$-meson braid closure), *not* the
carrier. Composite braids/links *can* be hyperbolic (nonzero volume), so this is
not excluded — but the specific composite charmed-hadron braid is **not defined
anywhere in the corpus** (heavy-flavour composites are open, per
`flavor-dressing-functor.md`), and computing its hyperbolic volume needs SnapPy
(absent here, no numpy). So the path is: *(i) define a candidate charmed-hadron
composite braid, (ii) compute its complex volume, (iii) project onto the charm
block.* All three open; step (ii) additionally needs compute infra.

## Steps (i)–(iii) executed with SnapPy — parameter-free negative (+ a coincidence, stated as such)

SnapPy installed successfully (`pip install snappy_manifolds snappy`), unblocking
composite-braid volume computation. `computations/charm_composite_volume_probe.py`,
witness `charm-composite-volume.witness.json`.

**Construction (parameter-free):** proton = Borromean baryon = closure of
$(\sigma_1\sigma_2^{-1})^3$ (Vol $=2V_{\rm oct}=7.3277$, 3 components). Generation
windings $n=3,5,7$ ⇒ the natural non-tuned family is $(\sigma_1\sigma_2^{-1})^n$.

| $n$ | Vol | components | mass ratio comparison |
|---|---|---|---|
| 3 (proton) | 7.3277 | **3** (3-quark link) | — |
| 5 (charm) | 17.0857 | **1** (KNOT) | Vol(5)/Vol(3) = 2.332 vs $\Lambda_c/p$ = 2.437 (**−4.3%**) |
| 7 (bottom) | 26.0544 | **1** (KNOT) | Vol(7)/Vol(3) = 3.556 vs $\Lambda_b/p$ = 5.989 (**−40.6%**) |
| 9 | 34.6759 | 3 | — |

**The 4% charm near-coincidence is DISQUALIFIED, not a result:**
1. **Wrong topology.** $(\sigma_1\sigma_2^{-1})^5$ is a **knot** (1 component), not a
   3-quark (3-component) baryon — the permutation $(123)^5=(132)$ is a 3-cycle. A
   charmed baryon must keep 3 components.
2. **Next point fails.** Bottom ($n=7$, also a knot) misses by ~40%. A 4% hit on
   one point with a 40% miss on the next is a coincidence, not a pattern.
3. **Non-canonical law.** The comparison assumes mass $\propto$ Vol (constant
   density), which is *not* the canonical absolute-mass law (muon-anchored Hecke
   energy).

**Topologically-correct 3-component candidates** (Borromean + one-strand winding,
permutation kept trivial): ratios 1.34, 1.43, 1.51, 2.17 — none hits the charm
ratio 2.437, and closing the gap by adding twists is a **tuned twist count = fit**.

**Verdict (scope-(a)):** no parameter-free composite-braid volume reproduces the
charmed-baryon mass ratio; the single near-coincidence is topologically
disqualified and non-repeating. **$m_c$ stays OPEN.** What changed materially:
**SnapPy is now available**, so principled follow-ups (variable-density law,
the Frobenius charm-block *projection* rather than the raw baryon volume, complex
volume $=$ Vol $+ i\,$CS with the CS part) are now computable — this negative
rules out only the crudest "mass $\propto$ raw composite volume" reading.

## Beans (env has no beans CLI — recorded here)

- **GAP (charm-mass step 1):** derive the two-gluon demand profile for gg→cc̄ in the skein-operator basis `{γ,σ₀,σ₁,L₊,L₋,e⁻}`, then run `solve_psd_operator_selection_sdp` to test whether it selects the `n=5` channel.
- **GAP (charm-mass step 2):** the continuant-ratio `contRatio` is scope-(a) refuted; test the complex-volume/CS (Im) contribution to the hierarchy once a composite charmed-hadron braid + its complex volume are available.
- **GAP (charm-mass carrier, closed as scope-(b)):** the carrier `T(3,5)`'s complex volume cannot be the charm mass (torus knot ⟹ Vol=0, CS∈ℚ). Charm mass must be the **composite** charmed-hadron braid's complex volume.
- **GAP (charm-mass composite):** define a candidate charmed-hadron composite braid (e.g. Λ_c = udc as a modification of the Borromean baryon braid 𝓑₃ with one strand carrying the n=5 winding), compute its hyperbolic + complex volume (needs SnapPy), project onto the charm block. Foundational missing object.
