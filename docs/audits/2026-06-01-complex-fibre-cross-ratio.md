# Complex-fibre cross-ratio: does a derived complex shape parameter carry the p/n signal?

**Date:** 2026-06-01
**Branch:** `claude/complex-fibre-cross-ratio-2026-06-01` (PR #1669)
**Scope:** Investigate the direction flagged (not resolved) by the merged
PR #1663
([`2026-06-01-vhat-tower-im-cancellation.md`](2026-06-01-vhat-tower-im-cancellation.md)
§"next direction") and PR #1657
([`2026-06-01-convergence-safe-vhat-tower.md`](2026-06-01-convergence-safe-vhat-tower.md)):
the per-crossing factors `V̂_i` are **real** Markov-trace scalars, so the
Bloch-Wigner dilogarithm vanishes on them (`D(real V̂_i) = 0`). The
predecessor's honest negative was that no DERIVED real archimedean
projection retains the continued-`Li_2^q` magnitude, because the
τ-functor's derived real image is `D`, and `D` collapses on real
arguments.

**Hypothesis under test (predecessor's flag):** the binding/isospin
signal should live in a genuinely COMPLEX fibre object — a hyperbolic
cross-ratio `z ∈ ℂ∖ℝ` (the shape parameter of an ideal hyperbolic
tetrahedron), where `D(z) ≠ 0` — BEFORE the τ-functor. Is there a
canonical, derivation-motivated complex per-crossing `z_i` whose
`Σ_i D(z_i)` is the archimedean volume contribution, related to the real
`V̂_i` by a known map, and carrying the p/n distinction?

**Compute:**
[`complex_fibre_cross_ratio.py`](../../computations/complex_fibre_cross_ratio.py),
witness
[`complex-fibre-cross-ratio.witness.json`](../../computations/complex-fibre-cross-ratio.witness.json).
All values RAW @ 60 dps via `WitnessBuilder.wrap_legacy` + `set_audit_only`
(audit-only). No tuning to m_p / B_AME / known volumes.

---

## VERDICT

**The framework HAS a derived complex cross-ratio / shape-parameter
object, and its `Σ D(z)` is finite, real, and zero-parameter — but it
carries the absolute VOLUME (mass scale), NOT the p/n distinction. The
complex-fibre cross-ratio is therefore NOT the L2 isospin path. This is a
CLEAN NEGATIVE that delimits exactly the missing categorical input.**

Two derived complex shape-parameter objects exist in the corpus, both
genuinely complex (`Im z ≠ 0`) so `D(z) ≠ 0`:

1. **The color-tube cubic** `F(c,z) = c³+(4z+1)c²+(6z²+3z+1)c+(4z³+3z²+2z+1)`
   ([`def:color-tube-cubic`](../../content/quantum-observable-universe/brings-surface/color-tube-cubic.md)),
   whose discriminant `Δ(z)=0` has complex roots `z_c` (e.g.
   `−0.975±0.223i`, `0.106±0.937i`).
2. **The Thurston / Neumann–Zagier ideal-tetrahedron shape parameters**
   `z_k` of hyperbolic knot/link complements
   ([`prop:thurston-volume-additivity`](../../content/quantum-observable-universe/mass-theory/thurston-volume-additivity.md)),
   e.g. figure-8 `4_1` shape `e^{iπ/3}` and Borromean octahedra.

Both reproduce the canonical volumes **exactly, zero free parameters**:

| object | `Σ D(z)` (raw, 40 dps) | canonical target | match |
|---|---|---|---|
| figure-8 `4_1` (2 tetrahedra `e^{iπ/3}`) | `2.0298832128…` | `2·Cl₂(π/3)` | ✓ |
| Borromean `ℬ_3` (2 ideal octahedra) | `7.3277247534…` | `8G` (Catalan) | ✓ |
| color-tube cubic complex roots | `0` | — | conjugate-pair cancel |
| real `V̂_i` (Hoefsmit Markov trace) | `≈ 1.8×10⁻⁷¹ ≈ 0` | `0` (real arg) | ✓ |

So the answer to "does a derived complex `z` with `D(z)≠0` exist?" is
**yes**. The answer to "does it carry isospin?" is **no** — for three
independent structural reasons below.

---

## Q1/Q2 — the complex shape object exists; `Σ D` is finite, real, zero-param

`D(z) = Im Li_2(z) + arg(1−z)·log|z|` is the Beilinson regulator
`r_2 : K_3(ℂ) → ℝ` (the unique Bloch-Suslin pentagon-coherent real
functional), per
[`prop:vol-through-tau`](../../content/quantum-observable-universe/mass-theory/vol-through-tau.md)
+
[`archimedean-functor-uniqueness`](../../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.md).
It is real by construction and **non-zero exactly on complex cross-ratios**.

Evaluated on the genuine derived shapes it reproduces the production
constants exactly: `Vol(4_1) = 2·Cl₂(π/3) = 2.02988…` (the
[`:val[Vol_4_1]`](../../content/quantum-observable-universe/mass-theory/figure-8-archimedean-illustration.md)
constant) and `Vol(ℬ_3) = 8G = 7.32772…` (the production substrate
constant in
[`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py)).
Confirmed: the complex-fibre cross-ratio gives a finite, real, zero-param
volume natively — exactly as the predecessor anticipated D would, on
COMPLEX arguments.

---

## Q3 — the complex shapes do NOT carry the p/n distinction (3 reasons)

**(a) The color-tube cubic is knot-independent.** Its coefficients are
`C(4,1)=4`, `C(4,2)=6`, `C(4,3)=4` and its constant term is
`d/dz[z⁴+z³+z²+z]`
([`color-tube-cubic.md`](../../content/quantum-observable-universe/brings-surface/color-tube-cubic.md)):
a fixed Bring-surface structure, **identical for every particle**. Its
discriminant roots come in complex-conjugate pairs, and `D(z̄) = −D(z)`,
so `Σ D(z_c) = 0` (raw): the universal cubic carries **no net hyperbolic
volume** and **cannot** supply a p/n signal.

**(b) Proton and neutron share the SAME complement.** The canonical
baryon is the 3-quark **Borromean linking `ℬ_3`** for both proton (uud)
and neutron (udd)
([`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py):
`Vol(ℬ_3) = 8·Cl₂(π/3)` is one constant for both). Same complement →
same ideal-octahedral shapes → **identical `Σ D`** → p/n difference in
`Σ D(z) = 0` (raw). The complex-shape volume is the absolute mass scale,
**not** the isospin splitting.

**(c) The flavor (p/n) content lives in the REAL sector.** The only
flavor-dependent per-crossing object the framework derives is the **real**
`V̂_i`, which has `D(V̂_i) = 0`. Its p/n signal lives in the magnitude
(`|V̂_proton σ₀| = 1.146` vs `|V̂_neutron σ₀| = 1.004`), i.e. in the
**Borel regulator** `r_1 = Σ ln|V̂_i|` mapping to `K_1(ℂ)` — a different
K-group from the `K_3`/`B(ℂ)` volume. The isospin refinement beyond the
uniform-flavor rule is the **conjectural real color-sheet weighting**
`W_{c₁c₂}(F₁,F₂)`
([`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)),
conditional on `conj:s5-so3-fiber-action` — still unproved, and `D`-free.

---

## Q4 — the V̂_i live in `K_1` (Borel), not `K_3` (Beilinson)

The framework's own
[`quantum-bloch-group.md`](../../content/quantum-observable-universe/mass-theory/quantum-bloch-group.md)
states the regulator placement explicitly:

| Side | Bloch group | Regulator | K-group |
|---|---|---|---|
| Pre-archimedean | `𝔅(ℤ̂[q])` | `½ Σ ln(V̂·V̄)` | (Habiro, bar-symmetric) |
| **Archimedean (real q₀, real V̂)** | `B(ℂ)` | `Σ ln\|V̂_i\|` | **Borel `r_1 : K_1(ℂ)→ℝ`** |

The complex shape parameters `z_k` and their `D(z_k) = r_2` live in the
**separate** `K_3 / B(ℂ)` object (the Thurston cusp variety / color-tube
structure). The probe confirms the K-group separation numerically:
`D(real V̂_proton) ≈ 1.8×10⁻⁷¹ ≈ 0` (the V̂_i contribute **zero**
Beilinson `r_2`), while their Borel `r_1 = Σ ln|V̂|` is non-zero and
p/n-split. **The p/n signal is a `K_1` (log-magnitude) phenomenon; the
hyperbolic volume is a `K_3` phenomenon. They are orthogonal.**

---

## The precise MISSING object (the L2 isospin requirement)

The connecting map `V̂_i → z_i` (real Markov trace → complex shape) is
**NOT derived**. The strongest attempt,
[`conj:shared-denominator-cusp-holonomy`](../../content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md),
proposes the algebraic denominator roots `q₀^{−k}` label the cusps `z_k`,
but
[`snappy-cusp-seeding.witness.json`](../../computations/snappy-cusp-seeding.witness.json)
shows the bare seeds sit at distance **0.4–0.9** from SnapPy's true
shapes `z_k`; the actual shape is a non-trivial function
`τ_arch(q₀^{−k})` whose form is **explicitly "the subject of further
work"**.

What L2 isospin needs is a **DERIVED flavor-dependent complex shape map**

```
  z_i  =  Z(braid_word, flavor_content)  ∈  ℂ∖ℝ
```

such that

1. `Σ_i D(z_i)` is the hyperbolic volume of the **actual** nucleon
   complement (`K_3 / r_2` content);
2. `z_i` depends on the **uud-vs-udd** flavor content, so proton and
   neutron get **DIFFERENT** shapes / volumes (the isospin splitting
   enters `Σ D`, not just the real `r_1`);
3. the real `V̂_i` are its Borel-`r_1` shadow (the `K_1 → K_3`
   refinement).

The framework derives the `(3)`-direction (`V̂ → K_1`) and has the
universal Bring color-tube cubic, but **not** the flavor-sensitive `Z`
map giving distinct p/n shapes. This flavor-dependent complex shape is
exactly the categorical input the L2 isospin sector currently lacks.

---

## What this audit does and does not claim

- **Does** establish, at 60 dps with zero free parameters, that the
  framework HAS derived complex cross-ratio objects (color-tube cubic
  `z_c`, Thurston shapes `z_k`) and that `D` evaluated on the genuine
  derived shapes reproduces `Vol(4_1) = 2Cl₂(π/3)` and `Vol(ℬ_3) = 8G`
  **exactly** — confirming the complex-fibre route gives a finite, real
  volume natively (the predecessor's anticipated behaviour of `D` on
  complex arguments).
- **Does** establish three independent structural reasons the complex-
  shape object is **p/n-blind**: (a) the color-tube cubic is knot-
  independent with `Σ D = 0` (conjugate-pair cancellation); (b) proton
  and neutron share the same `ℬ_3` complement → identical `Σ D`; (c) the
  flavor content lives in the real `V̂_i` (`K_1 / r_1`, with `D(V̂)=0`)
  and the conjectural real color-sheet weighting.
- **Does** confirm, numerically, the K-group separation stated in
  `quantum-bloch-group.md`: `D(real V̂) ≈ 1e-71 ≈ 0`, so the V̂_i carry
  zero Beilinson `r_2` — the p/n signal is `K_1`, the volume is `K_3`,
  orthogonal.
- **Does** identify the precise missing object: a DERIVED flavor-
  dependent complex shape map `Z(braid, flavor) → z_i ∈ ℂ∖ℝ` giving
  distinct proton/neutron complements. The `V̂ → z` map is currently not
  derived (`snappy-cusp-seeding`: 0.4–0.9 distance; `τ_arch` map "subject
  of further work").
- **Does NOT** propose, fit, or tune any such map. `{e, p, n}` are the
  falsification test; `m_e` is the CAL-1 dimensional anchor only. No
  value is tuned to m_p / B_AME / known volumes. Does NOT wire to
  production.

**Single most decision-relevant output:** the complex-fibre cross-ratio
is the right object for the absolute **VOLUME** (it reproduces
`2Cl₂(π/3)` and `8G` natively, `D` real and non-zero on complex shapes —
resolving the predecessor's "`D` collapses on real V̂" wall in the only
way it can: by using genuinely complex shapes). But it is **p/n-blind**:
the canonical complex shapes do not depend on nucleon flavor content. The
isospin signal is a separate `K_1` / real-color-sheet phenomenon. So the
complex-fibre cross-ratio is **NOT the L2 isospin path** — the missing
categorical input is a flavor-dependent complex shape map, which the
framework does not currently supply.

---

## Cross-references

- Predecessor (the negative this audit follows up):
  [`2026-06-01-vhat-tower-im-cancellation.md`](2026-06-01-vhat-tower-im-cancellation.md)
  (PR #1663) — `D(real V̂)=0`, continued tower is a real wall.
- Predecessor (the convergence-safe continuation):
  [`2026-06-01-convergence-safe-vhat-tower.md`](2026-06-01-convergence-safe-vhat-tower.md)
  (PR #1657).
- Derived complex shape structure:
  [`prop:thurston-volume-additivity`](../../content/quantum-observable-universe/mass-theory/thurston-volume-additivity.md),
  [`def:color-tube-cubic`](../../content/quantum-observable-universe/brings-surface/color-tube-cubic.md),
  [`conj:shared-denominator-cusp-holonomy`](../../content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md).
- K-group placement of V̂_i:
  [`quantum-bloch-group.md`](../../content/quantum-observable-universe/mass-theory/quantum-bloch-group.md).
- The conjectural real isospin refinement:
  [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).
- Canonical baryon volume formula (one `Vol(ℬ_3)` for p and n):
  [`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py).
