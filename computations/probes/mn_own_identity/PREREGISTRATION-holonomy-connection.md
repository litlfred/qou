# Pre-registration: the horizontal connection from the braid holonomy (2026-11-21)

Committed before `mn_holonomy_connection_probe.py` is run.

## Corpus basis

`QOU/Torsion/MassTraceIdentity.lean` (sorry-free): the discrete multiplicative integral of a word
of transports is their ordered product, `hol w`, and the mass trace of a cycle is a fixed
functional of `hol w`. The canonical chain (`mba-chain-map.md` step 2) turns non-abelian Stokes
into the Hecke relation, so the transport across a crossing is `σ_i` and the nucleon cycle's
holonomy is `B₃ = (σ₀σ₁⁻¹)³`. Braid generators commute with U_q(sl₂) (Schur–Weyl), so they are
weight-zero: exactly the kind of horizontal operator that §20 showed is needed for `μ ≠ 0`.

## Identification (mine, can be rejected)

Horizontal covariant difference around the nucleon cycle: `∇_hol = hol − 1 = B₃ − 1`
(lattice-gauge convention: transport minus identity). Not ruled in the corpus.

## Tests, exact sympy, on (C²)^{⊗3} with the level-2 Jimbo R-matrix

States are not chosen against a target: they are the eigenvectors of `B₃` itself, normalised,
in each weight space `W_p = (2,1)` and `W_n = (1,2)`.

- H1: spectrum of `B₃` on `W_p` and `W_n` (exact eigenvalues in Q(q)), with multiplicities.
- H2: `μ = eigenvalue − 1` for each eigenstate, and the K-weighted horizontal matter trace
  `q⁻¹·w·μ` (`w = q` proton, `q⁻¹` neutron), and its n − p difference per eigen-branch.
- H3: values at q = 1.
- Pass for the 12: some `μ`, or some n/p or nucleon/electron ratio, equal to 12 identically in q.
  The electron reference is `X_e = σ₀σ₁σ₀` with the same convention (`hol − 1`) on its own
  eigenstates. Anything else is a scope-(a) negative.
