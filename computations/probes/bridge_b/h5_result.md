# H5 result: the type-B boundary datum (2026-11-21)

Pre-registration: `h5_boundary_datum_preregistration.md`. Scripts: `h5_reflection_equation_solve.py`,
`h5_boundary_traces_probe.py`, `h5_evaluate.py`; output in `h5_output.txt`. All exact sympy in `q`;
values at the proton pin are 40-digit mpmath from the exact rational `q₀`.

## 1. Solutions of the reflection equation

For the Jimbo Ř, `Ř𝒦₁Ř𝒦₁ = 𝒦₁Ř𝒦₁Ř` with `𝒦 = [[a,b],[c,d]]` has exactly two families:

- `𝒦 = d·1`: a scalar, so it is a null.
- `d = 0`: `𝒦 = [[a, b], [c, 0]]` with `bc ≠ 0`.

So the reflection equation itself **fixes the direction**: the diagonal entry on `e₂` (the d direction) must
vanish. That asymmetry comes from where `h` sits in the Jimbo Ř, the same convention that makes
`u = e₁` (merged #7971). Nothing is chosen by hand.

## 2. It breaks the symmetry

`𝒦₁` does not commute with `F₃`, so `commutant_trace_eq` does not apply.

## 3. Is its size fixed?

`𝒦` has eigenvalues `x, y` (`a = x + y`, `bc = −xy`). The torus symmetry of Ř removes `b`. The free data
are the two eigenvalues, the type-B Hecke parameters.

They do not matter for the **ratio**. A restricted trace sees only the diagonal of `𝒦` on strand 1,
which is `(x + y)·|e₁⟩⟨e₁|`, and the factor `x + y` cancels. No condition (C1)–(C4) is needed.

## 4. Traces, γγ word V³ with one boundary insertion

The result is the same for all 7 insertion points:

- `T_p = −q (x+y) (q⁶ − 3q⁴ + 3q² − 3)`
- `T_n = (x+y) (q⁶ − 2q⁴ + 3q² − 1) / q⁵`
- `T_p / T_n = −q⁶ (q⁶ − 3q⁴ + 3q² − 3) / (q⁶ − 2q⁴ + 3q² − 1)`

At `q₀` this is `T_p/T_n = 2.4287166711934138787…`, against the pivot `q₀² = 1.2320524541667639…`. That is
a ratio of `1.9712770044648407…` to the pivot. **At q = 1 the ratio is exactly 2.**

## Verdict

**Under the pre-registered criterion this is a hit**: the datum solves the reflection equation, breaks
`F₃`, has no free number in the ratio, and is not the pivot. **But it is not a small mass splitting.** The
value 2 at `q = 1` shows what the boundary measures. It projects strand 1 onto `u`. The proton has two
states with strand 1 equal to `u`, the neutron one. So the boundary reads off **flavour content**, and the
`q`-deformation dresses that count.

Read as a mass through a linear trace → MeV map (the B1 reading, already refuted at scope (a)), it would
give a relative n − p difference of order 1. The measured value is about 0.14 % (CODATA; that comparison
is physics). As a perturbation of the bulk word, the boundary term would need a coefficient ε, and nothing
fixes ε. So the **direction** is now derived, from the reflection equation, but the **size** of the
splitting is not. Scope (a).

## What this adds to the record

- The first framework-internal object that picks the u direction without an imported number: the
  reflection-equation boundary for the Jimbo Ř.
- The remaining gap is now sharper. A derived n − p splitting needs the weight of the boundary relative
  to the bulk, a coupling, derived from the framework.

Not yet checked: words other than V³; boundaries on strand 3 (the mirror end); and the bar-image
`q → q⁻¹`, which should move the zero to the other diagonal entry.

## 5. Consistency sweep (2026-11-21) — this CORRECTS §1 and the verdict

Scripts: `h5_boundary_sweep_probe.py`, output `h5_boundary_sweep_probe.out.txt`. All exact.

| case | RE forces | T_p/T_n at q = 1 |
|---|---|---|
| wall at strand 1, V³ | `d = 0` (keeps u) | 2 |
| wall at strand 1, V⁶ | `d = 0` | 2 (a different q-function, given in the output) |
| **wall at strand 3, V³** | **`a = 0` (keeps d)** | **1/2** |
| bar image (`q → q⁻¹`), strand 1, V³ | `d = 0` | 2 |

**Correction.** §1 said the reflection equation picks the u direction with nothing chosen. That is
true only once the end is chosen. A wall at strand 1 picks u; a wall at strand 3 picks d. So the
direction is fixed by a **binary choice of which end carries the boundary**, a left/right (chirality-type)
datum. It is not free of input, but the input is one bit rather than a real number. The bar image does
not flip it: my guess in §4 that `q → q⁻¹` would move the zero was wrong.

The `q = 1` values (2 and 1/2) are the flavour counts: 2 vs 1 states with strand 1 = u, and 1 vs 2 with
strand 3 = d. The size of a splitting (the boundary-to-bulk coupling) is still not fixed. Only the
invertible branch (`bc ≠ 0`, resp. `bc ≠ 0` with `a = 0`) is a braid generator; the singular branches
give the same ratio and are listed in the output only for completeness.

Revised verdict: **direction fixed up to one binary end-choice; size not fixed. Scope (a). Not a hit
on the size question.**

## 6. Re-check against the current framework on main (2026-11-21)

`docs/coordination/owner-rulings.md` on main sets the rules this section checks against:
- The photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`, and γγ words use all three photon terms.
- The electron is `σ₀σ₁σ₀`, with Hopf-link closure.
- The scoreboard uses the two-term Lagrangian trace `M_QCD + M_QED`.

Script: `h5_ruled_photon_probe.py`, output in `h5_ruled_photon_probe.out.txt`. It uses exact sympy, with symbolic `φ` for two independent photons.

- **§1 (the reflection-equation solutions) and §5 (the wall's end picks the direction) are unaffected.** Neither depends on the word.
- **§4 holds only for V³.** V³ is the special pair `γ(0,0,qh)·γ(0,0,−q⁻¹h)`, and the general γγ result reduces to it exactly. For a general pair `γ(φ)γ(φ′)` the ratio `T_p/T_n` depends on the photon parameters. It also **depends on where the boundary is inserted**. At `q = 1`, with a wall at strand 1, it is `(2φ₀φ₀′ + φ₀ + φ₀₁φ₀′ + φ₀₁φ₁′ + φ₁φ₀₁′ + 2φ₁φ₁′ + φ₀′ + 2) / (φ₀φ₀′ + φ₀φ₀₁′ + φ₁φ₁′ + φ₁ + φ₁′ + 1)`, not 2. The claims "2 at q = 1" and "the same at every insertion point" are therefore V³ facts, not general ones.
- **Two-term trace.** This section computes only the `M_QCD` term. On a boundary insertion, the `M_QED` charge term would need the charges `Q = T³ + Y/2`, and with them the conditional input `Y`. It is not computed here.

Verdict unchanged. The direction is fixed up to the choice of end. The size is not fixed. With the ruled photon, the
size now also depends on the photon parameters and on where the boundary is placed.
