# The Hecke quadratic + e₊/e₋ channels at every rank (2026-07-19)

**Beans:** `qou-genq` (double brick: general-n tower + τ-functor provenance).
**Lean (both sorry-free, `lean`-direct exit 0):**
- [`QOU/Machinery/HeckeDescentQuadratic.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeDescentQuadratic.lean)
  — the minimal **descent structure** (involutive step + rank the step never
  fixes) suffices for the length-rule action, its bilinearity, and the
  **Hecke quadratic**; explicit finite descent structures re-derive the
  merged n = 3, 4 tables (`h3_mulσ₀_eq_mulStep`, `h3_mulσ₁_eq_mulStep`,
  `h4_mulσ₂_eq_mulStep` — the abstract theorem subsumes all five concrete
  quadratics).
- [`QOU/Machinery/HeckeGeneralRankQuadratic.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/HeckeGeneralRankQuadratic.lean)
  — the same over an **arbitrary Coxeter system** via Mathlib
  (`length_mul_simple` toggle + `simple_mul_simple_self`): `mulSimple` and
  **`mulSimple_quadratic`** for every rank simultaneously.

## Wall 1 (general-n tower)

The `hecke_quadratic` field content of `HeckeBraidedPresentation` is now a
**theorem at every rank** (any Coxeter system; a fortiori every Sₙ) at the
action level — previously known only concretely at n = 2, 3, 4. The
remaining general-rank presentation laws (braid, far commutation) need the
exchange/Matsumoto layer and stay OPEN, as do the H_∞ class instances.

## Wall 2 (τ-functor provenance)

**`channel_plus` / `channel_minus`** (both files): for `h = q − q⁻¹`,
`Mv + q⁻¹·v` is a `q`-eigendirection and `Mv − q·v` a `(−q⁻¹)`-eigendirection
of the generator action — the symmetric/antisymmetric **e₊/e₋ channel pair**
(the objects the archimedean τ-functor must send to `(H^{1,0}, H^{0,1})`;
forced shadow #3960, B1 dictionary #3955) now exists as verified
mathematics at every rank, not only at the concrete rungs.

## Environment note

The Mathlib Coxeter cone was absent from this sandbox's partial olean tree;
resolved by lake-cache restore + merging the root-workspace olean tree into
the content-dir tree (`cp -rn`), after which the "missing cone" was zero.

Honesty: no conjecture-class instance declared; nothing wired; `1/(8π)`
stays phase-4. §7c: `CommRing` for module+quadratic, `Field` only for the
channels; no ℝ.
