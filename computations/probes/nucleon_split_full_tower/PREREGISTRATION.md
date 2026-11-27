# Pre-registration: nucleon split on the full tower, all strands

Written 2026-11-27, before the probe printed any MeV value. Branch
`claude/nucleon-split-full-tower-2026-11-27`. Beans `qou-myts`, `qou-99qc`.

**What was already known when this was written.** The order-zero cell `2E₀·log q = 0.873537 MeV`
and the tower cell `0.882197 MeV` are on main (#9453, #9475). The prediction below is that the
full tower reproduces exactly these numbers; that prediction is written down here, before the
check, so that a different outcome cannot be explained away.

Owner, 2026-11-27: "make sure you work on all strands on the full tower", "dervie k-weight
expoentn", "dont look at leadgin term only".

## Observable

`m_n − m_p = E·log(τ_p/τ_n)` (Gibbs map, #9475, no coupling term). On `n` strands,

    τ_x(W) = Σ_T Σ_{b : b|_T ∈ weight(x)} k(b)·⟨b|W|b⟩

where `b` runs over **every** colouring of all `n` strands by `u, d`, `k(b)` is the
`K^{⊗n}` eigenvalue with the Markov-forced weight, and `T` runs over the tagged-nucleon positions.
`weight(p)` = two `u` among the three tagged strands, `weight(n)` = one `u`. Both nucleons use the
same element `W` (the single-element setting of #9453; distinct elements are route 2, not this
work).

* **Primary**: `T` = each nucleon block `{3i, 3i+1, 3i+2}`, summed over all blocks.
* **Secondary, reported**: `T` = every 3-subset of strands, summed; and each `T` separately.
* Never a picked position: the sum over `T` and over colourings is the observable.

## Tower levels and elements

`n = 3, 6, 9`. `n = 3, 6` exact over ℚ(q) (sympy); `n = 9` exact in `Fraction` at the rational
points `q = 11/10, 3/2` (no float). Elements: the Borromean core `V³ = (σ₀σ₁⁻¹)³`; its embeddings
with spectators; the 58 six-strand γγ reading-3 survivors of
`gg_six_strand/six-strand-neutral-selection.witness.json` (all of them); at `n = 9` the three-core
product and products with interface letters; and seeded random words (to test universality, not to
select). Convention D throughout: the full Frobenius pairing on `(C²)^{⊗n}` is the sum over all
two-row `λ ⊢ n`, and convention D gives every three-or-more-row `λ` weight zero, so the
`(C²)^{⊗n}` trace is the complete sum over all `λ`. Exact arithmetic: no truncation in `q`.

## The K-weight exponent

Derived, not chosen: Lean `NucleonSplitFullTower.markov_forces_K` (any 2×2 `K` with a Markov
partial trace for the corpus braiding has `q²·K_dd = K_uu`). The probe re-derives it by solving the
Markov equations with sympy, independently. Whatever exponent the tower gives is reported.
`CODATA/(E₀ log q) ≈ 2.96` is a diagnostic only and drives nothing.

## Colour-weighted convention (R3, `bring_color_weighted`)

It acts on the p–n **interface** letter, `σ − h(½ − δ/4)·1`, with `δ = flavor_split_leading(q)`,
which the code labels `(m_n − m_p)/M_N`. It will be applied as an element-level modification
(shared by both nucleons) and reported. It will **not** be used as a nucleon-dependent weight in a
derivation of `m_n − m_p`, because its input `δ` is that quantity; that use is recorded as a fork.

## Limit n → ∞

If the ratio is `q²` at every computed level, the limit is reported as "constant, by theorem"
only for what Lean proves, and as "checked at n = 3, 6, 9" for the entangling case, which is not
formalised for general `n`. If the ratio moves with `n`, every level's value is reported and no
extrapolation is made.

## Scales

Both `E₀`: `qbeta_e0.order_zero` and `qbeta_e0.canonical` (tower-summed), proton `q₀`.
Comparison with CODATA `m_n − m_p` only at the end.
