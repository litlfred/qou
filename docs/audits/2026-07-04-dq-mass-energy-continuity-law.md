# The ∂_q mass–energy continuity law — the QOU analogue of the Magueijo–Barrow modified-continuity equation

**Date:** 2026-07-04
**Branch:** `claude/mu-p-tension-closure-uua4os`
**Executes:** follow-up **#2** of [`2026-07-02-bekenstein-vsl-review.md`](2026-07-02-bekenstein-vsl-review.md) §3.3/§5 (bean `4big`)
**Probe:** [`scripts/dq_mass_energy_continuity_probe.py`](scripts/dq_mass_energy_continuity_probe.py) (self-contained, sympy-exact, exit 0)
**Companion:** [`2026-07-04-qdot-substrate-drift-bound.md`](2026-07-04-qdot-substrate-drift-bound.md) (follow-up #3)

## What this closes

The review's §3.3 recorded a scope-limited gap: Magueijo–Barrow's technical
heart is the *modified continuity equation* — the explicit statement of what
sources what when `c` varies — and the QOU corpus proved `E = 𝔪·c_q²` only *at
fixed q*, with no `∂_q` conservation statement. This audit supplies it. The
`∂_q` identity is **rigorous** — it is calculus on the *proved*
`thm:mass-energy-equivalence`, not a new postulate; only the cosmological
reading (`q` = cosmic time) is speculative, and it stays bracketed.

## The derivation

Corpus objects (exact): `c_q = 1/(q−1)`, `E_𝔥 = 𝔪_𝔥·c_q² = 𝔪_𝔥/(q−1)²`
(`thm:mass-energy-equivalence`), `ℏ_q = (q−1)/q`.

The speed of light obeys an **autonomous ODE** — its defining property:

$$
\frac{dc_q}{dq} = -c_q^2 .
$$

Differentiating `E = 𝔪(q)·c_q²` along `q` and substituting gives the
**continuity law** (sympy-exact):

$$
\boxed{\;\frac{dE}{dq} + 2\,c_q\,E \;=\; c_q^2\,\frac{d\mathfrak m}{dq}\;}
$$

- The `2 c_q E` term is the **c_q-variation source** — the QOU analogue of the
  Magueijo–Barrow source `−(ċ/c)·ρc²`. It vanishes **iff** `q` is fixed
  (`c_q` constant), recovering ordinary conservation.
- The `c_q² d𝔪/dq` term is the **mass-flow source**.

## What is conserved as q flows

The **categorical mass `𝔪`** — the knot's topological / fibre content — is
scale-free (a q-invariant). With `d𝔪/dq = 0`,

$$
\frac{dE}{dq} = -2\,c_q\,E \neq 0,\qquad E(q) \propto c_q^2,
$$

so the **crossing energy is NOT conserved** along the q-flow: a varying `c_q`
creates/destroys energy, exactly the minimal-VSL phenomenology. The QOU answer
to the review's question ("mass, energy, or neither?") is therefore precise:
**categorical mass is the invariant; crossing energy scales as `c_q²` and is not
conserved.** This is the fibre-vs-observable split — the topological object is
q-fixed, its archimedean (MeV) evaluation rides `c_q²`.

## The review's germ-commutator tie-in does not hold (critical-distance note)

§3.3 floated identifying the source term with the germ-commutator /
`q`-curvature blocks (`prop:germ-commutator-q-curvature`, `F_q = (q−1)𝓕_q^intr`).
Checked and **refuted as stated**: the source coefficient `2c_q ∝ (q−1)⁻¹`
scales **inversely** to `F_q ∝ (q−1)`, so there is no clean identification. The
source is intrinsically the `c_q` ODE (`−c_q²`), a spatial-`∂_q` object, not the
two-observer curvature 2-form `F_q`. (A relation the algebra *does* hand back
cleanly: `c_q·ℏ_q = 1/q`.) This is a scope-(a) negative on the *identification*,
not on the continuity law, which stands exactly.

## Scope / discipline

The continuity law is a rigorous corollary of a proved theorem. The
**cosmological reading** — promoting `q` to a diffusing field in cosmic time —
stays **bracketed-speculative**: the corpus's own q-flow dynamics
(`q-harmonic-flow`) is an explicit **conjecture/ansatz** (kind `conjecture`, not
a derived PDE), so this audit makes no cosmological claim — it only records the
`∂_q` structure the Magueijo–Barrow comparison demands, per the review. Nothing
wired; CAL-1/2/3 untouched. Promotion to a content `remark`
(`interprets: thm:mass-energy-equivalence`) is the natural follow-on once the
cosmological framing is decided. Review follow-up **#1** (Ellis–Uzan remark
block) remains open; **#3** (q̇/q drift bound) landed in the companion audit.
