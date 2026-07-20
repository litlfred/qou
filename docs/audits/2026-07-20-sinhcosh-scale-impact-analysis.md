# Impact analysis: what the sinh/cosh (bar-even/odd) structure changes for mass & binding compute, and whether it must be tracked up the mass scale

**Date:** 2026-07-20
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20` (PR #4139)
**Status:** AUDIT — impact assessment. Distinguishes PROVED inputs from PROBE
inputs throughout (per the proof≠probe discipline). No compute is re-wired
here; this scopes *whether* it should be and *where*.

## 0. The inputs, tiered by epistemic status

| Fact | Tier | Source |
|---|---|---|
| Binding period `a_D^{(n)} = I(n)/n` is Gevrey-½ | **PROVED (Lean)** | `QOU.Mass.BindingGevreyHalf` |
| q-lift kernel C1 exact: `[m+2]_q b_{m+2}=b_{m+1}+b_m`, c(q)=1 | **PROVED (Lean)** | `qlift_normalized_kernel_exists` |
| C1 (slope ½) and GGM/Stokes (slopes ±1) are distinct q-diff modules | **PROVED (5 routes; invariant = isoclinicity)** | gauge-gap synthesis |
| sinh/cosh slope arithmetic (square + bar-even/odd reaches {−1,+1}) | **PROVED (Lean)** | `ThetaSlopeArithmetic` |
| GS cumulative q-degree = C(m,2) | **PROVED (Lean)** | `gs_cumulative_degree` |
| theta-order CONSTANT across jet order (slope ½ scale-invariant) | **PROBE** (curvature 0.49998, drift 6e-4) | theta-jet-GB probe |
| `θ_m ~ ½·C(m,2)` analytic bridge | **PROBE** (leading order) | theta-jet-GB probe |
| C1 **is** the binding module's generating function | **CONJECTURE** (keystone) | `conj:qdifference-kernel-prolongation-symbol` |
| naive sinh/cosh sym² exactly reproduces GGM | **REFUTED scope-(a)** | Door-iii probe |

## 1. The physical dictionary

In the framework, **bar-even = cosh = mass** (the muon-anchored binding energy)
and **bar-odd = sinh = decay width** (Q_β). The gauge-gap result says these are
carried by **two distinct q-difference modules**: C1 (the binding kernel, pure
isoclinic slope ½, bar-non-symmetric — the cosh face) and GGM/eq-49 (the Stokes
carrier, anisoclinic {−1,+1}, bar-symmetric — the sinh/cosh ± pair). The
sinh/cosh twist (`ThetaSlopeArithmetic`) relates them at the *slope* level only;
Door-iii refutes the naive *exact* identification, so **they do not collapse to
one computable object.**

## 2. Impact on MASS / BINDING compute (bar-even / cosh)

**Headline: for stable-isotope mass & binding, nothing changes, and there is a
positive scale-invariance result.**

1. **The kernel does NOT need per-nucleus re-derivation.** The theta-order
   (slope ½) is **constant across jet order** (PROBE, but backed by the PROVED
   Gevrey-½ order and the PROVED slope arithmetic). The binding module's
   Gevrey-½ character is an intrinsic invariant, *not* graded by jet order `n`
   (equivalently, not by mass number `A`). So the q-lift kernel `[m+2]_q
   b_{m+2}=b_{m+1}+b_m` is the **same at every A** — you extend the jet sum to
   higher `n`, you do not re-solve for a new kernel. This is a simplification,
   not a new obligation.
2. **The cumulative growth `θ_m ~ m²/4` grades with `m`, but that is bookkeeping,
   not a twist.** What increases with scale is the *cumulative* GS degree
   `C(m,2)` (PROVED), i.e. the depth of the jet/GS filtration you sum over — a
   monotone accumulation, not a sinh/cosh mixing. No per-step twist tracking is
   required for the binding magnitude.
3. **Caveat (the honest one):** the scale-invariance in (1) is *conditional on
   the keystone* `C1 = binding module` (CONJECTURE). If that fails, the
   slope-½-is-scale-invariant claim must be re-checked against whatever the true
   binding OGF is. Flag this in any compute that leans on it.

## 3. Do we track sinh/cosh twisting up the scale? — the precise answer

**For the binding energy of a bar-even (stable) configuration: NO.** A stable
nucleus's binding is the pure cosh (bar-even) object; the bar-odd (sinh) content
is the *decay width* Q_β, a **separate observable on a separate module**. You do
not track a sinh admixture in the binding of a stable isotope — there isn't one
to track.

**Where sinh/cosh tracking DOES become required, up the scale:**

- **β-unstable isotopes / approach to the drip line.** As `A` (and isospin
  asymmetry) grows, Q_β grows relative to the binding. The bar-odd (sinh)
  channel is then physically active, and the **joint bar-even/bar-odd
  decomposition** of the isotope's spectrum must be tracked — but as **two
  coupled observables on two modules**, not as a twist inside one kernel. The
  gauge-gap result is a *constraint* here: **do not attempt to derive Q_β from
  the binding kernel by any rational/gauge transform** — the five routes prove
  they are different modules; Q_β must be computed on its own (GGM/Stokes)
  carrier.
- **The bar-parity grade is the thing to carry.** The actionable bookkeeping is
  to tag every observable by bar-parity (mass/binding = even/cosh; Q_β / decay =
  odd/sinh) and route each to its own module. The `sinh/cosh twist` is the
  *relationship* between the two graded sectors (framework bar involution), not
  a correction that accumulates inside either one.

## 4. Concrete recommendations for the compute layer

1. **Mass table (stable isotopes):** no change. Keep the muon-anchored Hecke
   energy via `canonical_mass.py` and the jet-filtration binding; the kernel is
   scale-invariant (§2.1). Do **not** add a per-A sinh correction to binding —
   there is no derived one, and adding a fitted one violates the anti-fit rule.
2. **Q_β / decay observables:** compute on the bar-odd (GGM/Stokes) carrier
   independently. Add a guard/annotation that Q_β is NOT to be routed through
   the binding kernel (encode the five-route module distinction as a
   producer-side check, analogous to the canonical-mass guardrail).
3. **β-unstable / drip-line extensions (future):** when these are attempted,
   carry the explicit bar-even ⊕ bar-odd grading and compute the two sectors on
   their two modules, coupling only through the framework bar involution. Track
   the *balance* (which sector dominates), never a twist inside a single kernel.
4. **Keystone dependency:** any compute that cites §2.1 scale-invariance must
   cite `conj:qdifference-kernel-prolongation-symbol` as its conditional
   premise (conditional-proved ≠ premise-established).

## 5. Bottom line

The sinh/cosh finding **simplifies** the binding/mass compute (scale-invariant
kernel, no per-nucleus re-derivation) and **constrains** the decay compute (Q_β
is a distinct module — never gauge-derive it from binding). "Tracking sinh/cosh
up the scale" is required only as **bar-parity sector bookkeeping** for
β-unstable systems, not as an accumulating twist inside the binding kernel.
Everything load-bearing here is PROVED except the keystone `C1 = binding module`
and the theta-constancy probe; both are flagged as the conditional premises.
