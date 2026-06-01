# Reeb–Bring geometric escape test — does Reeb rotation distinguish p from n?

**Status:** IN PROGRESS (branch `claude/reeb-bring-geometric-escape-2026-06-01`).
**Date:** 2026-06-01.
**Probe:** [`folio-assistant/computations/reeb_rotation_pn_test.py`](../../folio-assistant/computations/reeb_rotation_pn_test.py)
**Witness:** `folio-assistant/computations/reeb-rotation-pn-test-reeb.witness.json`

## The hypothesis under test

Sessions on `main` (PRs #1604/#1605/#1606) proved a *per-partition*
impossibility theorem: any function `f(λ)` of abstract partition
(character-level) data is constant across Markov-equivalent knots and
therefore cannot produce `m_n − m_p = 1.293 MeV`. The signal localises to
"the braid word / strand count," not per-partition data.

**The escape:** the binding/mass energy may be GEOMETRIC — the rotation of
the Reeb bundle, a per-knot-**operator** quantity computed from the actual
braid word, NOT from the abstract character. If the proton-knot operator
and the neutron-knot operator act with different Reeb rotation, the geometry
distinguishes p from n even when their characters coincide.

**Decisive test (zero free parameters):** compute the q-Reeb rotation
(eigen-phase structure of the seminormal braid-word operator, per Wedderburn
block) for the proton braid and the neutron braid at substrate `q₀`, and ask:
does it DIFFER? Report raw numbers either way. No tuning to `m_n − m_p`.

## What the operators are (substrate-derived, zero tuning)

`q₀ = 1.1099785827513808`, `h = q₀ − q₀⁻¹ = 0.20906029879563937`.

Single nucleon ⇒ `A = 1` ⇒ 3-strand braid in `H₃(q)` (gens 0, 1), no
inter-nucleon crossing. The braid words come from
`mass_at_3A_proper.atom_braid_word_3A(Z, N)`, built from B₃ = (σ₀σ₁⁻¹)³ plus
typed quark crossings (proton = `uud`, neutron = `udd`). The proton and
neutron are **genuinely different elements of H₃(q)**:

| | g0 averaged (`−h/2`) crossings | g1 full (`−h`) crossings |
|---|---|---|
| proton (uud) | 1 | three `−h` + one `−h/2` |
| neutron (udd) | 2 | four `−h` |

Canonical-convention check (`atom_canonical_crossings`) agrees: proton g0 has
one `averaged`, neutron g0 has two `averaged`; proton g1 ends `…sigma_inv,
averaged`, neutron g1 ends `…sigma_inv, sigma_inv`.

## Preliminary result (full numbers in witness)

Per Wedderburn block λ ⊢ 3, eigenvalues of the braid-word operator
`Π (c·σ_g + d·I)`:

- **Eigenvalue PHASES (the Reeb rotation `arg(eigenvalue)`) are bit-identical
  for p and n** — every eigenvalue is real, phases ∈ {0, π} in both. The
  phase-sum difference is exactly 0 in all three blocks.
- **Eigenvalue MODULI differ** between p and n (e.g. block (3): 1.382 vs
  1.122; block (1,1,1): 0.739 vs 0.911). The distinguishing data is in the
  growth/writhe channel (`|eigenvalue|`), not the rotation/phase channel.

So under the standard q-Reeb reading (`θ_λ = arccos(χ_λ/dim_λ)`, phase =
`arg`), **the Reeb ROTATION does NOT distinguish p from n; the WRITHE/growth
amplitude does.** (Full block table, characters, and difference signs in the
witness.)

## Interpretation — which escape is live

(Filled in below after the full probe + scale analysis.)
