# H6 result, part 1: a boundary term with a derived coefficient already exists (2026-11-21)

Pre-registration: `h6_boundary_coupling_preregistration.md`. This is in progress; the candidates still to do are listed at the end.

## Found in the corpus: the open U_q chain's surface term

`braids-and-knots/tl-is-the-xxz-chain` (a remark) writes the Temperley–Lieb Hamiltonian as the open XXZ chain:

  `−2 Σ eᵢ = H_XXZ − Δ(n−1) − ½(q − q⁻¹)(σᶻ₁ − σᶻₙ)`.

This is a boundary term with a **fixed, derived coefficient**, `h/2`, and it is **antisymmetric between the two ends**. That matches H5's finding that the two ends pick opposite directions.

Exact checks at n = 3, in `h6_xxz_boundary_probe.py`:
- `Σ eᵢ` commutes with `F₃`, so the full chain is excluded by `commutant_trace_eq`.
- The surface term on its own does **not** commute with `F₃`.
- Its restricted traces are **0 on both the proton and the neutron weight space**, so it gives no n − p difference. On each weight space the σᶻ₁ and σᶻ₃ sums are equal and cancel.

**Verdict for this candidate.** The coefficient is derived, but the term is not a u ↔ d breaker in the trace. Inside the U_q-symmetric object it is the piece that turns SU(2) symmetry into U_q symmetry, and on its own its trace vanishes. Scope (b) for the trace, by exact computation at n = 3. The vanishing trace also follows from the end-antisymmetry.

## Still to evaluate (listed in the pre-registration)

1. The boundary term of non-abelian Stokes, with the same λ.
2. A type-B Markov trace parameter fixed by the convention-D pivot (Geck–Lambropoulou; the corpus cites it in `2026-08-19-bar-involution-is-isospin-conjugation.md`).
3. Choosing the end: `MarkovOrientationForced.lean`, the over-strand rule (#7971), the Reeb orientation.

## Part 2: the remaining candidates (2026-11-21)

Script `h6_end_symmetry_probe.py`, output `h6_end_symmetry_probe.out.txt`. Exact sympy.

| # | candidate | fixes? | free parameter left | conditional on |
|---|---|---|---|---|
| 1 | non-abelian Stokes boundary term | **the corpus does not define it for a wall** | the coefficient | — |
| 2 | type-B Markov trace (Geck–Lambropoulou) | **no** | `x + y` | — |
| 3 | folding | no (expected null, H5 §3) | the eigenvalues | — |
| 4 | `MarkovOrientationForced` | **no** | the end bit | — |
| 5 | over-strand rule (#7971) | **no** | the end bit | — |
| 6 | Reeb orientation | **the corpus does not define it for a wall** | the end bit | — |

**1. Stokes.** `docs/audits/2026-08-30-nonabelian-stokes-and-the-surface-term.md` §0:
- the surface term's *shape* is a theorem on main (`SaturationPeakStructure`);
- its coefficient is not derived ("Nothing here derives `a_V`, `a_S` or `a_C`").

The §2 correction (bean `qou-h7w4`) says Yekutieli's bad set is the singular locus of the
connection forms (α, β). The corpus has no forms (bean `qou-20bk`). So there is no boundary λ to
inherit, and a type-B wall is not a boundary in that statement. Not a hit.

**2. Type-B Markov.** For the strand-1 wall, the pivot-weighted trace value is
`tr(K𝒦)/tr(K) = q²(x+y)/(q²+1)`. It is still free in `x + y`. A trace parameter would also enter
multiplicatively, not as the additive `ε` of `M_bulk + ε·M_wall`. Not a hit.

**4–5. The end is the u ↔ d bit, and the pivot carries it.** Exact:
- strand reversal composed with the flavour swap fixes the Jimbo Ř: `PŘP = (S⊗S)Ř(S⊗S)`;
- it maps the pivot to its inverse: `SKS = K⁻¹`.

So a strand-3 wall under `K` is the image of a strand-1 wall under `K⁻¹`, with p ↔ n exchanged. That
is the 2 ↔ 1/2 of H5 §5 at `q = 1`. The two ends differ only through the orientation of `K`.

`MarkovOrientationForced` and `OverStrandWeight` fix that orientation (with `u = e₁`). They say
nothing about where a wall sits: neither file mentions a boundary. Choosing the end is therefore
the same as choosing which nucleon gets the larger boundary trace, i.e. the sign of n − p. That is
an input bit, not a derived one.

**6. Reeb.** `ReebEpsilon.lean` has no strand ordering and no wall. The corpus does not define it
for a wall.

## H6 verdict

**No hit.** No candidate fixes `ε` or the end.

- Sharper statement: the end bit equals the sign of n − p (via reversal∘swap, proved exactly above).
  So "which end carries the wall" is the same open input as "which nucleon is heavier"; it does not
  add a new unknown.
- Open: a derived additive coupling `ε`. That needs a framework object the corpus does not yet have,
  either a boundary in a Stokes statement with actual forms, or a rule placing a wall. Scope (a).
- Only `M_QCD` was examined. `M_QED` on a boundary still needs `Y` (bean `qou-99qc`).
