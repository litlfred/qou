# QA drain — predicted-spectra particle-identity cluster (proof-statement-integrity)

Slice of the `proof-statement-integrity` backlog: 5 blocks under
`content/quantum-observable-universe/predicted-spectra/`.

| Block | Mismatch (from qa.json notes) | Fix |
|-------|-------------------------------|-----|
| `categorical-proton-unique` | unsound axiom `Subsingleton CategoricalProton` (false: free real fields) | Context-class conditional uniqueness |
| `categorical-neutron-unique` | unsound axiom `Subsingleton CategoricalNeutron` (false) | Context-class conditional uniqueness |
| `antiparticle-crossing-reversal` | `lean.ref` decl absent; md sign+bar reversal not stated | Context-class bundling all 4 md claims |
| `integer-stability` | ref decl absent; convex-quadratic exactness not formalized | Context-class convex-quadratic integer minimiser |
| `baryon-product-from-alt` | vacuous `True→True` placeholder | Context-class Alt-isotype projector identity |

One slice = one PR. Proven pattern from MERGED #1984/#1996/#1997.
