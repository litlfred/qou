# H6: what fixes the boundary-to-bulk coupling and the wall's end (pre-registration, 2026-11-21)

The user chose this on the card ("Both, PR first"; the PR is #8774). Written before any candidate is evaluated.

## Setting

H5 (`h5_result.md`) found that a type-B wall solving the reflection equation fixes the direction:
- a wall at strand 1 keeps u;
- a wall at strand 3 keeps d.

As a letter of the word it changes `T_p/T_n` by O(1), because it reads off flavour content. A small
n − p splitting needs it to enter **additively**:

  `M = M_bulk + ε · M_wall`,

with `ε` fixed by the framework. Two things are open: the value of `ε`, and which end carries the wall.

Framework on main (owner-rulings.md, 2026-11-21):
- the photon is `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`;
- the electron is `σ₀σ₁σ₀` (Hopf-link closure);
- traces are two-term, `M_QCD + M_QED`.

## Candidates, listed before evaluation

**For ε:**
1. **The boundary term of non-abelian Stokes.** Stokes is a step in the derivation chain. If the
   Lagrangian `𝔖 = λ·tr(ℒ)` produces a boundary term with the same λ, then ε is fixed relative to
   the bulk. Check what the corpus Stokes statement says about boundary terms, and whether a
   wall is a legitimate boundary in that statement.
2. **A type-B Markov trace** (Geck–Lambropoulou). Its extra trace parameter for the boundary
   generator could be fixed by the convention-D pivot, as `z_D` is fixed for type A.
3. **Folding** (type B from type A on a doubled strand set, AGENTS.md §7b). This sets the boundary
   eigenvalues equal to a crossing's. H5 shows the eigenvalues cancel from the ratio, so this cannot
   fix ε by itself. It is recorded as an expected null.

**For the end:**
4. The Markov orientation forced in `MarkovOrientationForced.lean`.
5. The over-strand rule that fixes u = e₁ (merged #7971).
6. The orientation of the Reeb direction (Bridge A).

## Classification

Each candidate gets three entries:
- **fixes?** yes, no, or "the corpus does not define it for a wall";
- **free parameter left over?**
- **conditional on?** For example `Y`, for any `M_QED` part.

A **hit** fixes ε with no free number, or fixes the end with no free choice. Both outcomes are
recorded, including a negative.

## Discipline

- No fitting. ε is never solved from the measured n − p difference.
- If a candidate gives a number, it is reported with its comparison to CODATA, marked as physics.
  It is not promoted for being close.
