# H7: forms for a Stokes boundary, and the M_QED wall term (pre-registration, 2026-11-21)

The user chose "Search for a forms-based Stokes boundary" on the card and asked, in the thread,
"And do M_QED wall.term". Written before either part is evaluated.

Framework on main (owner-rulings.md, 2026-11-21):
- the photon is `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹`;
- the electron is `σ₀σ₁σ₀` with Hopf-link closure;
- traces are two-term, `M_QCD + M_QED`.

## Part A: connection forms

Non-abelian Stokes (Yekutieli) integrates `α ∈ Ω¹⊗𝔤` and `β ∈ Ω²⊗𝔥` over a kite. Bean `qou-20bk`
says the corpus has no such forms. Part A re-checks that, with the six-path corpus grep, and asks
whether a wall could be a boundary of the kite.

**A form counts** only if it is defined in the corpus, not just named, as an actual 1-form or 2-form
on a stated manifold, with values in a stated Lie algebra or crossed module.

**A hit** needs all three:
1. such forms;
2. a corpus statement whose boundary term is a type-B wall, or a place where one sits;
3. the coefficient of that boundary term fixed with no free number.

The outcome is recorded with the paths searched, including a negative. "Not found in these paths" is
not the same claim as "does not exist".

## Part B: the M_QED wall term

Take the EM1 functional (`em1_photon_exchange_probe.py`): pairs of charge insertions
`Q_a = T³ + Y/2` on distinct quarks at ordered slots, normalised by the plain trace. Insert the
strand-1 wall `𝒦₁` (H5, `d = 0`) into both the numerator and the denominator.

- `Y` stays symbolic. Numbers at `Y = 1/3` are labelled conditional (bean `qou-99qc`).
- Word: V³ = `γ(0,0,qh)·γ(0,0,−q⁻¹h)`. The general ruled photon pair is noted, not computed.
- Questions:
  1. Do the wall eigenvalues `x`, `y` cancel?
  2. Does the result depend on where the wall is inserted?
  3. What is the wall-induced change in `E(n) − E(p)` relative to the bulk EM1 value?

**Not a hit by construction.** The size still enters through `ε` (H6) and through `Y`. The part is
a comparison arm, not a derivation.

## Discipline

No fitting; nothing solved from the measured n − p difference. A number is compared with CODATA
only in a section labelled physics.
