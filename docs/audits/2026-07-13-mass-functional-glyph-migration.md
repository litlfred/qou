# Corpus migration: mass functional $\mathcal{M} \to \mathfrak{m}$

**Date:** 2026-07-13
**Branch:** `claude/mass-functional-glyph-migration-2026-07-12`
**Implements:** the owner $\mathcal{M}$ glyph ruling (2026-07-12,
[`notation-collisions.md`](../../content/quantum-observable-universe/notation/notation-collisions.md);
follow-up of PR #3718 /
[`2026-07-12-mass-endomorphism-naming-vs-type.md`](2026-07-12-mass-endomorphism-naming-vs-type.md)).

## The ruling

$\mathcal{M}$ was overloaded ~10 ways across the corpus. The ruling:

- **$\mathcal{M}$** = mass **endomorphism** $\mathcal{M}(K)\in\mathrm{End}_{\mathbf{C}}(X_K)$ (keep)
- **$\mathfrak{m}$** = mass **functional / value** (migrate ← $\mathcal{M}$)
- **$\mathcal{M}_q$** (subscript) = QFT **scattering amplitude** $\lvert\mathcal{M}_q\rvert^2$ (keep)

This migration renames **only the mass-functional/value sense** $\mathcal{M}\to\mathfrak{m}$,
per file, leaving every other $\mathcal{M}$ sense untouched.

## Senses deliberately LEFT as $\mathcal{M}$ (not touched)

A blanket substitution would corrupt these — each stays $\mathcal{M}$:

| Sense | Example | Location |
|---|---|---|
| mass endomorphism | $\mathcal{M}(K)\in\mathrm{End}_{\mathbf{C}}$ | `mass-endomorphism/{binding-qbeta-complex-volume, complex-volume-intro, complex-volume-character-variety-path}`, `notation-register-table7-data` |
| scattering amplitude | $\lvert\mathcal{M}_q\rvert^2$, $\mathcal{M}_e/\mathcal{M}_\mu$ | `observations/trace-ratio-*`, `predicted-spectra/{tau-leptonic-universality, skein-coulomb-enhancement, hadron-half-life}`, `observations/{hadron-half-life-verification, half-life-shell-worked}` |
| moduli space | $\mathcal{M}_{j,K}$, $\mathcal{M}^{\mathrm{inst}}_k$, $\overline{\mathcal{M}}_{0,5}$, $\mathcal{M}_{\nabla_q}$ | `fluid-dynamics/berry-vortex-moduli`, `quantum-observable-universes/categorical-instanton-unique*`, `mass-theory/cl3-zeta5-geometric-realization`, `q-geometric-langlands/q-oper-hecke*` |
| motivic Grothendieck ring | $\widehat{\mathcal{M}}$, $\mathcal{M}:=K_0(\mathrm{Var})$ | `lifting-and-descent/motivic-*`, `mass-theory/{archimedean-realization-functor, motivic-mass-measure}`, `stochastic-mechanics/classical-limit-adelic-assembly` |
| $q$-Hecke eigensheaf | $\mathcal{M}$ on $\mathrm{Bun}_G$ | `q-geometric-langlands/{q-hecke-eigensheaf, q-hecke-eigenvalue*, q-gl-fiber-functor*}` |
| Mach number | $\mathcal{M}=\lvert v\rvert/c_s$ | `fluid-dynamics/acoustic-horizon-conditions` |
| magic-number set | $\mathcal{M}=\{0,2,8,\dots\}$ | `appendix-transfer-matrices/tm-heavy-atom-examples*`, `predicted-spectra/shell-construction-rules` |
| Mikusiński field tower | $\mathcal{M}_q^{(n)}$ | `stochastic-mechanics/graded-baer-star-Hq`, `mass-theory/gb-depth-period-correspondence` |
| molecular braid (Hecke element) | $\mathcal{M}(A_1,\dots)\in H_N(q)$ | `molecular-construction/{molecular-braid, ch4-lp-dual-binding, h2-lp-dual-binding}` |

## Migrated files (functional/value sense → $\mathfrak{m}$)

See the accompanying sweep commit. Each renamed file was grep-verified to
carry **only** the mass-functional/value sense of $\mathcal{M}$ before the
rename; mixed-sense files were hand-checked.
