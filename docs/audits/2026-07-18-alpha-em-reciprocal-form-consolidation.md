# α_EM per-loop measure `1/(8π)`: the reciprocal-form wall consolidates to a single located `1/2` (covolume route scope-(b) excluded)

**Date:** 2026-07-18 · **Axis:** α_EM 2-loop / 1ppQ (#3612 headline) · **Tier:**
structural (scope-(a) partial + one scope-(b) exclusion — NOT a closure) ·
**Discipline:** no fit wired, no `c_k`, no tier change; no CODATA read; no
convention tuned toward `8π`.

## The wall (per the derivability map)

The sole load-bearing wall of the α_EM per-loop measure
([`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md))
is: *why does the count `b₁` enter the 1-loop measure **reciprocally** —
`1/(π·b₁)`, in the denominator with a bare `π` — while the proved zero-mode
carries it in the **numerator** over the Area (`b₁/Area = 2/(3π)`)?* The map
scopes the answer to "the RT shadow-world 1-loop determinant computation on the
genus-4 Jacobian — the honest multi-week item."

After the count axis (real `b₁ = 8`, #3920) and the π-power axis (heat-kernel
`−1`, #3909) closed, #3920 left **two numerically-identical readings of `8π`
unselected**:

- **(P)** `π · b₁` — one bare loop-`π` traced over the `b₁` real harmonic sectors;
- **(H)** `(4π) · 2` — the #3909 heat-kernel Gaussian base `(4π)^{d/2}|_{d=2} = 4π`
  × a residual `2`.

## New structural input: the Jacobian covolume

The photon is the `U(1)` gauge field; its moduli of flat connections is the
**Jacobian torus** `J(M) = H¹(M;ℝ)/H¹(M;ℤ)`, real dimension `b₁ = 2g = 8`. The
metric on `H¹` is the intersection form `Q = ⊕^g [[0,1],[-1,0]]` (Poincaré
duality), whose covolume is

```
Vol(J) = √|det Q| = √1 = 1        (UNIMODULAR — Poincaré duality, #3895)
```

This is the one input the earlier per-loop probes did not use. Its consequences:

### 1. The derived 1-loop measure is `1/(4π)`, a factor 2 from the data

The 1-loop photon determinant on the moduli is the heat-kernel Gaussian
normalization dressed by the covolume:

```
1-loop measure = (4π)^{-d/2}|_{d=2} · Vol(J)^{±1} = 1/(4π) · 1 = 1/(4π).
```

Both factors are now derived: the `1/(4π)` heat-kernel (power `−1`, #3909) and
`Vol(J) = 1` (unimodular, here). The derived object is `1/(4π)` — **a factor 2
larger** than the data `1/(8π)`.

### 2. Reading (H) is selected over (P)

The actual 1-loop determinant carries the heat-kernel **base `4π`** (not a bare
`π`), and `Vol(J) = 1` shows that base is **undressed**. So reading (H)
[`(4π)·2`] is the structurally-supported decomposition; the "bare-`π`-per-sector"
picture (P) does not arise from any determinant. This refines #3920's "no proved
invariant selects (P) vs (H)" — the covolume input does select (H).

### 3. scope-(b) exclusion: the residual `2` is NOT a covolume

If the missing factor lived in a Jacobian / lattice covolume it would appear in
`Vol(J)`. But `Vol(J) = 1` (unimodular). **The residual multiplicity cannot be a
lattice/covolume effect** — a structural exclusion citing the proved invariant
(Poincaré-duality unimodularity of the intersection form, #3895).

### 4. The wall consolidates to a single located `1/2`

```
data / derived = 1/(8π) ÷ 1/(4π) = 1/2.
```

The **entire** underived residual is a single factor `1/2`, located precisely
between the derived heat-kernel-on-unimodular-Jacobian `1/(4π)` and the data
`1/(8π)`.

## What this does and does NOT establish

- **DOES:** computes `Vol(J_Bring) = 1` (unimodular); selects reading (H) over
  (P); **scope-(b) excludes** the residual `2` from being a Jacobian covolume;
  consolidates the wall to one located `1/2`.
- **DOES NOT:** derive the `1/2`. Candidate origins are enumerated but not
  forced: the photon's **2 polarizations** / the real⊕complex Hodge doubling
  (#3920); a **θ-graph symmetry factor**; the **Gaussian exponent `½`**. A factor
  of 2 is the single easiest thing to fit, so the value is claimed **OPEN**; only
  the location and the covolume exclusion are claimed.

## Scope discipline (anti-laundering)

No CODATA read; no convention tuned toward `8π`; `Vol(J) = 1` is a Poincaré-
duality fact, not chosen; the `1/2` residual is stated OPEN, not papered over. No
`α_k` wired; no fit; no tier change; `1/(8π)` stays a phase-4 identification.

## Cross-references

- The wall statement: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Count axis (real `b₁ = 8`, the two readings left unselected): [`2026-07-18-alpha-em-multiplicity2-realcomplex-count.md`](2026-07-18-alpha-em-multiplicity2-realcomplex-count.md)
- π-power axis (heat-kernel `1/(4π)`, forced `−1`): [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md)
- Unimodularity of the intersection form (`Σd_i² = 1` discriminant): [`2026-07-18-alpha-em-count-carrying-object.md`](2026-07-18-alpha-em-count-carrying-object.md)
- Probe + witness: [`../../computations/alpha_em/alpha_em_reciprocal_form_probe.py`](../../computations/alpha_em/alpha_em_reciprocal_form_probe.py), `computations/alpha_em/alpha-em-reciprocal-form.witness.json`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
