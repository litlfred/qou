# RESULT — Gresnigt's Clifford braid representation IS a Hecke representation (after `τ = ±iσ`)

Issue #9096. Pre-registration: [`PREREG.md`](PREREG.md) (committed alone, before this
compute). Producer: [`gresnigt_hecke_probe.py`](gresnigt_hecke_probe.py); witness:
[`gresnigt-hecke.witness.json`](gresnigt-hecke.witness.json). **54 / 54 exact checks pass**
(sympy over ℚ(ζ₈), every check an exact zero test; no floats).

Source tested: `library/arxiv-1901.01312v1` (Gresnigt, *Braided fermions from Hurwitz
algebras*) §4.2 pp. 4–5 and §4.3 pp. 5–6. **`arxiv-1711.09011v1`, named in the task, is not
held in `library/`** (no directory, no string match in any `sections/`), so the matrices are
those of 1901.01312, same author, same construction (Kauffman–Lomonaco
`σ_k = (1 + e_{k+1}e_k)/√2`). The Kauffman–Lomonaco paper itself is also not held.

## Verdict

**YES — a Hecke-algebra representation at a root of unity, in disguise.** Precisely:

| claim | result |
|---|---|
| C1 `σ² − √2σ + 1 = 0`, eigenvalues `ζ₈^{±1}`, `σ⁴ = −1`, order 8 | holds for every generator (ℂ, ℍ, Cl(4,0)) |
| C2 braid relations | B₂ (ℂ); all three pairs of B₃^c (ℍ); B₄ and B₄^c from Cl(4,0) |
| C3 unrescaled `σ` in the repo Hecke form `T² = (q−q⁻¹)T + 1` | **no** — eigenvalue product is `+1`, the repo form needs `−1` |
| C3 all scalars `c` with `cσ` Hecke | **exactly `c = ±i`** (`c² = −1`); no real `c` exists |
| C3 `q` for `c = +i` | `q − q⁻¹ = i√2`, `q ∈ {ζ₈, ζ₈³}` |
| C3 `q` for `c = −i` | `q − q⁻¹ = −i√2`, `q ∈ {ζ₈⁵, ζ₈⁷}` |
| C4 rescaling keeps the braid relation | iff the **same** `c` on every generator (`c₁²c₂ = c₁c₂²` ⇒ `c₂ = c₁`) |

So the hand claim "`τ = iσ`, `q = e^{iπ/4}`" is **correct, but `q` is not unique**: within
`c = i` the two solutions `ζ₈` and `ζ₈³ = −ζ₈⁻¹` are the `q ↔ −q⁻¹` relabelling (which
eigenvalue is called the symmetric one), and `c = −i` gives the complex-conjugate pair. All
four primitive 8th roots of unity occur; they are Galois conjugates over ℚ. The point is
**`q² = ±i`, i.e. `q` a primitive 8th root of unity**, fixed up to that symmetry.

The 1-dim complex rep `σ = ζ₈` is a Hecke rep with **no** rescaling (trivial rep at `q = ζ₈`,
or sign rep at `q = ζ₈³`); `σ² − √2σ + 1 = 0` is its minimal polynomial only over ℝ
(ℂ = Cl(0,1) as a real algebra). Over ℝ no rescaling works, since `c` must be `±i`.

## Which irreps (C5)

At `q = ζ₈`: `[2] = √2`, `[3] = 1`, **`[4] = 0`**. So `H₃(ζ₈)` is semisimple and
`H₄(ζ₈)` is not (`q²` has order 4 = e). The non-semisimplicity is visible in the compute: on
`H₄` the five Specht characters are linearly dependent — the solver returns a free parameter
along `χ_(4) − χ_(3,1) + χ_(2,1,1) − χ_(1⁴) = 0` (the weight-1 block of e = 4).

- **ℍ rep of B₃ (τ₁, τ₂), 2-dim:** character `= χ_(2,1)` exactly, coefficients `(0,1,0)`.
  It is the Specht module `S^(2,1)` of `H₃(ζ₈)`, irreducible.
- **Cl(4,0) rep of B₄, 4-dim:** splits by chirality `γ = e₁e₂e₃e₄ = ±1` into two 2-dim
  irreducibles:
  - `γ = −1`: character `χ_(2,2)`; `τ₃ = τ₁`. This is `S^(2,2)`, a 4-core, hence simple and
    projective in its own block.
  - `γ = +1`: character `χ_(3,1) − χ_(4)`; `τ₃ = −τ₁⁻¹`. This is the 2-dim simple head
    `D^(3,1)` of the reducible Specht `S^(3,1)` (composition `S^(3,1) = D^(3,1) + D^(4)` in
    the e = 4 block). **This summand is not a Specht module**; it exists only because `q` is
    a root of unity.

(The character identification of the γ = +1 half rests on the exact character equation;
the composition-series reading `S^(3,1) = D^(3,1) + D^(4)` is the standard e = 4 block
structure, not separately computed here.)

## Temperley–Lieb (C6)

**Factors through Temperley–Lieb.** On every consecutive 3-strand window (`τ₁τ₂`, and
`τ₂τ₃` in Cl(4,0)) both the q-symmetriser `Σ q^{ℓ(w)} T_w` and the q-antisymmetriser
`Σ (−q⁻¹)^{ℓ(w)} T_w` act as zero — so it lies in TL under **either** labelling of `q`. It is
in fact killed by both, i.e. it also omits the one-row component on three strands.

## Markov trace (C7)

The normalised matrix trace **is a Markov trace** on `H₂ ⊂ H₃` (ℍ rep) and on `H₃ ⊂ H₄`
(Cl(4,0) rep): `t(x τ_{n−1}) = z·t(x)` for every `x = T_w`, `w ∈ S_{n−1}`, exactly, with

    z = t(τ_{n−1}) = i/√2 = z_D(ζ₈) = ζ₈³/(ζ₈² + 1)         (also = z_D(ζ₈³))

where `ζ₈² + 1 = 1 + i ≠ 0`. So the trace carried by Gresnigt's rep is **convention D's
Markov trace specialised at `q = ζ₈`**. Its weights at n = 3 are `y = (0, 1, 0)`: the
`(1³)` weight vanishes as convention D always forces, and the `(3)` weight vanishes too
because its quantum dimension carries `[4]_q = 0` at this root of unity (the Jones–Wenzl
`p₃` is negligible). That last attribution is the standard reading; the compute measures
only `y = (0,1,0)` and `z = z_D`.

Interpretation (literature, not computed here): `q = e^{iπ/4}`, `q² = i`, is the
`SU(2)` level-2 point (`ℓ = 4`), and the `(1 + e e)/√2` braiding is the Ising / Majorana
braid representation; the result above is the Hecke/TL statement of that.

## Scope and what this does not say

- **`q = ζ₈` is fixed by Gresnigt's construction, not by us.** It is a specialisation of our
  formal `q` — a point of the family, not a selection against any target — and it **must not
  be imported as `q₀`** (q₀ derivation is forbidden; nothing here is compared to data). The
  substrate `q₀ ≈ 1.11` is real; `ζ₈` is on the unit circle; the two are unrelated.
- The circular generators (σ₃ of B₃^c, σ₄ of B₄^c) satisfy the same Hecke relation with the
  same `c` and the cyclic braid relations, so the ℍ rep is a representation of the
  **affine** Hecke algebra of type Ã₂ at `q = ζ₈` (circular B₃ is the Ã₂ Artin group). Only
  the ordinary `H_n` part was decomposed into irreps.
- Photon/electron rulings are not touched: no photon or electron element is built here.
- Chirality: Gresnigt's γ = ±1 halves of Cl(4,0) are **different** `H₄(ζ₈)` modules
  (`S^(2,2)` vs `D^(3,1)`). This is an observation about his rep, not a claim about QOU
  chirality.

## Reproduce

    python3 -u computations/probes/qcd_gresnigt_hecke/gresnigt_hecke_probe.py

(~4 min, sympy 1.14; exit 0 iff all 54 checks pass.)
