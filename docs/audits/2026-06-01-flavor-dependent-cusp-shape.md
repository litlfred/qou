# Flavor-dependent cusp shape: does uud-vs-udd reach the complex shape parameter (K₃ volume)?

**Date:** 2026-06-01
**Branch:** `claude/flavor-dependent-cusp-shape-2026-06-01` (PR #1670)
**Scope:** Resolve the SINGLE missing object delimited by the merged
predecessors
([`2026-06-01-complex-fibre-cross-ratio.md`](2026-06-01-complex-fibre-cross-ratio.md),
PR #1669;
[`2026-06-01-vhat-tower-im-cancellation.md`](2026-06-01-vhat-tower-im-cancellation.md),
PR #1663): a **DERIVED flavor-dependent complex shape map**
`Z(braid_word, flavor) → z_i ∈ ℂ∖ℝ` giving DISTINCT proton/neutron
complex shapes, so isospin enters `Σ D` (the K₃ Bloch-Wigner hyperbolic
volume), not just the real Borel regulator `r₁ = Σ ln|V̂_i|` (K₁).

**Compute:**
[`flavor_dependent_cusp_shape.py`](../../computations/flavor_dependent_cusp_shape.py),
witness
[`flavor-dependent-cusp-shape.witness.json`](../../computations/flavor-dependent-cusp-shape.witness.json).
All values RAW @ 60 dps via `WitnessBuilder.wrap_legacy` +
`set_audit_only` (audit-only). No tuning to m_n−m_p / B_AME / known
volumes.

---

## VERDICT

**NO derived flavor→complex-shape map reaches `Σ D` (the K₃
Bloch-Wigner volume). The flavor content does NOT reach the cusp
holonomy in the current framework. The precise missing categorical
object is a DERIVED per-strand flavor→root (equivalently
flavor→meridian-eigenvalue) selection rule whose sign and root are
fixed by the quark content — a flavored decoration of the color sheets
that is currently UNDEFINED. This is a CLEAN NEGATIVE: it does not
close or advance L2 numerically, but it names exactly the remaining
structural gap, and shows it is the SAME gap that
`conj:inter-nucleon-channel-color-tube` names on the real (K₁) side.**

---

## The structural pivot: the color-tube cubic has three roots = three color sheets

The investigation focuses on candidate (b) — the per-strand color-tube
cubic root assignment — because the color-tube cubic is the one
genuinely-complex, derived object that is also indexed by the three
color sheets that flavor decorates.

At a fixed **real** substrate `z = q₀ ≈ 1.10998`, the color-tube cubic
([`def:color-tube-cubic`](../../content/quantum-observable-universe/brings-surface/color-tube-cubic.md))

```
  F(c, z) = c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1)
```

has **negative discriminant**, hence exactly **one real root and one
complex-conjugate pair** (verified at q₀ and at z ∈ {1, 0.5, 1/q₀}):

| root | value at q₀ |
|---|---|
| `c_real` | `−2.85284561…` (real) |
| `c_+` | `−1.29353438… + 1.63355799… i` |
| `c_−` | `−1.29353438… − 1.63355799… i` |

These three roots **are** the three color sheets `(c_r, c_g, c_b)`
([`def:color-tube-fibers`](../../content/quantum-observable-universe/brings-surface/color-tube-fibers.md):
`R_z, G_z, B_z` are the three solutions of the same cubic). The
nucleon flavor content decorates **which sheet each strand carries**:
proton `(u,u,d)`, neutron `(u,d,d)`.

The Bloch-Wigner regulator on these roots (RAW @ 60 dps):

```
  D(c_real) = 0                       (D vanishes on real arguments)
  D(c_+)    = +0.5332714958972856680…
  D(c_−)    = −0.5332714958972856680… (D(z̄) = −D(z))
  Σ D over all three roots = 0
```

So the universal color-tube cubic carries **zero net hyperbolic
volume** — confirming PR #1669's conjugate-pair-cancellation finding,
now sharpened to the three-color-sheet level.

---

## Mechanism (b): per-strand root assignment by flavor

### (b1) One sheet per root — the geometrically natural assignment

Each nucleon has **exactly 3 color sheets**, and the cubic has
**exactly 3 roots**. The natural assignment puts one sheet on each root
(a bijection strand → sheet → root). Under ANY such bijection, both
the proton `(u,u,d)` and the neutron `(u,d,d)` use the **same root
multiset** `{c_real, c_+, c_−}` — flavor only permutes the order of the
sum. Therefore

```
  Σ D(proton) = Σ D(neutron) = D(c_real) + D(c_+) + D(c_−) = 0,
  p/n difference = 0   (exactly).
```

This assignment is **DERIVED** (it is the canonical one-sheet-per-root
reading) but it is **p/n-blind**: flavor cannot reach `Σ D` this way.

### (b2) Flavor-discriminating selection — splits p/n, but is a latent fit

To make flavor reach `Σ D`, a rule must map `u` and `d` to **different**
roots and **reuse** a root when a flavor repeats. Then proton `(u,u,d)`
uses multiset `{r_u, r_u, r_d}` and neutron `(u,d,d)` uses `{r_u, r_d,
r_d}` — genuinely different. Enumerating all 6 injective two-root
selections gives a nonzero p/n difference:

| `u`→ | `d`→ | p/n Σ D difference (raw) |
|---|---|---|
| `c_real` | `c_+` | `−0.5332714958972856680…` |
| `c_real` | `c_−` | `+0.5332714958972856680…` |
| `c_+` | `c_real` | `+0.5332714958972856680…` |
| `c_+` | `c_−` | `+1.0665429917945713360…` |
| `c_−` | `c_real` | `−0.5332714958972856680…` |
| `c_−` | `c_+` | `−1.0665429917945713360…` |

Every entry is exactly a multiple of `D(c_+) = 0.5332714958972856680…`
— because `D(c_real) = 0` and `D(c_−) = −D(c_+)`, so each p/n
difference is just `±D(c_+)` or `±2 D(c_+)`. **The magnitude and sign
are set entirely by the unjustified choice of which root is `u` vs
`d`, not by the quark content.** This is a **LATENT FIT** — the
root-selection rule IS the missing categorical input, and it is exactly
what a discipline review would catch if it were chosen to hit a target.
The probe reports it raw, without selecting a "winning" assignment.

**Why (b2) is not derived.** The color-tube structure gives three
roots but provides **no canonical map** from a quark flavor to a
specific root. The flavor `u`/`d` is an `S₅`/SO(3)-fiber label
(`conj:s5-so3-fiber-action`), and the conjectural weight matrix
`W_{c₁c₂}(F₁,F₂)` of
[`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)
would supply it — but that conjecture is itself unproved and supplies
a **real** weight (the K₁ side), not a root-selection on the complex
cusp variety (the K₃ side).

---

## Mechanism (a): flavored cusp decoration — no derived flavor→holonomy map

Does the flavor modify the Thurston cusp shape `z_k` itself
(meridian/longitude holonomy eigenvalues carrying the flavor)? No:

- The cusp shapes are **fixed by the topological complement**. SnapPy
  ([`snappy-cusp-seeding.witness.json`](../../computations/snappy-cusp-seeding.witness.json))
  gives `m004`/`m003` → `e^{iπ/3}` and `L6a4` (Borromean) → `(1+i)/2`,
  **independent of the algebraic seed** (the bare seeds sit at distance
  0.4–0.9 from the true shapes). The shape is a property of the
  geometry, not of any flavor label.
- The probe reproduces `2·D(e^{iπ/3}) = 2.02988321281930725… =
  2·Cl₂(π/3)` exactly (the figure-8 volume) and records `Vol(ℬ₃) = 8G`
  — both flavor-blind.
- Proton and neutron are the **same unfilled ℬ₃ complement**
  ([`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py)).
  A flavored **Dehn filling** would change the manifold (a filled cusp
  gives a different volume), but that is not the QOU nucleon model —
  both nucleons are the same unfilled link complement.
- `conj:shared-denominator-cusp-holonomy` proposes the algebraic
  denominator zeros `q₀^{−k}` **label** the cusps, but the actual shape
  is `τ_arch(q₀^{−k})`, a function "the subject of further work" — and
  it carries **no flavor dependence** (the denominator `(x;q)_n` is
  flavor-blind; it depends only on the GB-depth `n` of the word).

So mechanism (a) supplies **no derived map** flavor →
meridian/longitude holonomy eigenvalue. The cusp shape does not see the
quark content.

---

## The precise missing categorical object

The flavor content reaches the real K₁ Borel regulator (`Σ ln|V̂_i|`,
the p/n-split `V̂_i` magnitudes) but **does not** reach the K₃
Bloch-Wigner volume `Σ D`, because:

1. the cusp shapes are topology-fixed (flavor-blind), and
2. the color-tube cubic's three roots are used as the **same multiset**
   by both nucleons under the geometrically natural one-sheet-per-root
   assignment, giving `Σ D = 0` for both.

The single missing object is a **DERIVED per-strand flavor→root
selection rule**

```
  ρ : {u, d}  ⟶  {c_real, c_+, c_−}   (or, equivalently,
      flavor ⟶ meridian-eigenvalue / cusp decoration)
```

whose **sign and root are fixed by the quark content** (not chosen),
so that proton `(u,u,d)` and neutron `(u,d,d)` use **different root
multisets** and `Σ D` differs by a derived amount. The framework does
not currently supply `ρ`:

- on the K₁ (real) side, `conj:inter-nucleon-channel-color-tube`
  conjectures the weight `W_{c₁c₂}(F₁,F₂)` (conditional on the unproved
  `conj:s5-so3-fiber-action`) — a real magnitude, not a complex-root
  selection;
- on the K₃ (complex) side, `ρ` is **undefined**.

**This audit shows `ρ` is exactly the same gap on both sides.** The
flavor→color-sheet→root map that would close the K₃ side is the same
`S₅`/SO(3)-fiber decoration that the K₁ conjecture needs. Until
`conj:s5-so3-fiber-action` is formalised as a class supplying a
canonical flavor→root tensor (with no free choice), the K₃ isospin
path is blocked.

---

## What this audit does and does not claim

- **Does** establish, RAW @ 60 dps with zero free parameters, that at
  the real substrate `q₀` the color-tube cubic has one real root and
  one complex-conjugate pair, with `D(c_real) = 0`, `D(c_+) =
  +0.53327…`, `D(c_−) = −0.53327…`, so `Σ D` over the three roots = 0.
- **Does** establish that the geometrically natural one-sheet-per-root
  assignment (b1) is DERIVED but p/n-blind: both nucleons use the same
  root multiset, `Σ D` difference = 0 exactly.
- **Does** establish that a flavor-discriminating selection (b2)
  produces a nonzero p/n `Σ D` difference, but every value is `±D(c_+)`
  or `±2D(c_+)` — set by an unjustified 2-of-3 root choice. It is a
  LATENT FIT: the root-selection rule IS the missing input; reported
  raw, no "winner" selected.
- **Does** establish that the Thurston cusp shapes are topology-fixed
  (flavor-blind), reproducing `2Cl₂(π/3)` and `8G` exactly; there is no
  derived flavor→holonomy-eigenvalue map; p and n are the same unfilled
  ℬ₃ complement.
- **Does** identify the precise missing categorical object: a derived
  per-strand flavor→root (flavor→meridian-eigenvalue) selection rule,
  the same `S₅`/SO(3)-fiber decoration that the K₁ conjecture
  `conj:inter-nucleon-channel-color-tube` needs.
- **Does NOT** propose, fit, or tune any such map. `m_n−m_p` (PDG) is
  the falsification reference only; no value is tuned to it. Does NOT
  wire to production. Does NOT close or advance L2 numerically.

**Single most decision-relevant output:** flavor does NOT reach the
cusp holonomy. The K₃ (volume) and K₁ (flavor) sectors remain
orthogonal because the only complex-shape object indexed by color
sheets — the color-tube cubic — is used as the same root multiset by
both nucleons (Σ D = 0) under the natural assignment, and any
flavor-discriminating root selection is an undefined choice, not a
derivation. The missing object is the flavor→root selection rule,
which is the same gap `conj:s5-so3-fiber-action` /
`conj:inter-nucleon-channel-color-tube` already name on the real side.

---

## Cross-references

- Predecessor (the negative this audit follows up):
  [`2026-06-01-complex-fibre-cross-ratio.md`](2026-06-01-complex-fibre-cross-ratio.md)
  (PR #1669) — complex shapes carry the volume, not isospin.
- Predecessor (the archimedean wall):
  [`2026-06-01-vhat-tower-im-cancellation.md`](2026-06-01-vhat-tower-im-cancellation.md)
  (PR #1663) — `D(real V̂) = 0`.
- Color-tube structure:
  [`def:color-tube-cubic`](../../content/quantum-observable-universe/brings-surface/color-tube-cubic.md),
  [`def:color-tube-fibers`](../../content/quantum-observable-universe/brings-surface/color-tube-fibers.md),
  [`def:color-tube-coordinates`](../../content/quantum-observable-universe/brings-surface/color-tube-coordinates.md).
- The flavor→color-sheet conjectures (the missing map, both sides):
  [`conj:inter-nucleon-channel-color-tube`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md)
  (conditional on `conj:s5-so3-fiber-action`).
- Cusp holonomy:
  [`conj:shared-denominator-cusp-holonomy`](../../content/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.md),
  [`snappy-cusp-seeding.witness.json`](../../computations/snappy-cusp-seeding.witness.json).
- Canonical baryon volume (one ℬ₃ for p and n):
  [`derive_m_baryon_volume_form.py`](../../computations/derive_m_baryon_volume_form.py).
