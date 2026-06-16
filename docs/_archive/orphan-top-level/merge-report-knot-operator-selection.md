# Merge Report: `claude/knot-operator-selection-7Pqd6`

## Branch summary

- **94 commits** ahead of main
- **69 new content files** (`.ts` + `.md` + `.lean` triples)
- **52 new computation scripts** (Python witnesses under `computations/`)
- **590 modified content files** (mostly `.md` prose edits and `.ts` manifest updates)

## New content blocks (this branch)

### Chapter 3: Braids and Knots (`braids-and-knots/`)
| Block | Kind | Description |
|-------|------|-------------|
| `def:typed-crossing-operator` | definition | Typed crossing $C(f_i,f_j;\sigma_k)$ from quark flavors |
| `prop:categorical-mass-markov` | proposition | Single-level mass = $|\mathrm{tr}_M(\beta)|$ via Nakayama |
| `rem:mass-element-nf` | remark | Degree filtration: $\gamma$-coefficient = 0 (photon massless) |
| `conj:mass-endomorphism-conjecture` | conjecture | Tower-summed mass element |
| `prop:three-parameters-wedderburn` | proposition | $H_3(q) \cong M_1 \oplus M_2 \oplus M_1$: 3 irreps → 3 inputs |
| `prop:calibration-inputs` | proposition | Three calibration inputs: $q$, $m_e$, $\mathcal{Q}_\beta$ |
| `rem:energy-scale-planck` | remark | $E_0 \approx m_e \cdot c_q^2 \cdot \hbar_q$ |
| `def:nucleon-hecke-element` | definition | Nucleon as Hecke element in $H_3(q)$ NF basis |

### Chapter 6: The Descartes Universe (`descartes-universe/`)
| Block | Kind | Description |
|-------|------|-------------|
| `def:breit-wheeler-pair-production` | definition | Pair production via Frobenius dual |
| `prop:knot-operator-selection` | proposition | Multi-channel selection via spectral decomposition |
| `prop:frobenius-gram-matrix` | proposition | 6×6 Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ |
| `def:typed-garside-element` | definition | **NEW** — Typed Garside staircase, all $\binom{A}{2}$ crossings |
| `prop:gram-weighted-qvalue` | proposition | **NEW** — $Q = (\sum w_k^G \Delta_k) \times N \times m_e$ |
| `rem:gram-weight-eigenstructure` | remark | **NEW** — Eigenstructure of $G$ and adjoint character weight |
| `prop:ground-state-ordering` | proposition | GS from transfer matrix eigenvalue structure |
| `prop:transfer-matrix-identities` | proposition | $T_{pp} \cdot T_{nn} = I$ and $T_{pn}^2 = [2]_q^2/4 \cdot I$ |
| `prop:neutron-qvalue-symbolic` | proposition | Symbolic $\mathcal{Q}_\beta(n)$ formula |

### Appendix: Knot Operations (`appendix-knot-operations/`)
| Block | Kind | Description |
|-------|------|-------------|
| `rem:knot-operator-basis-table` | remark | Full 6×6 NF product table |
| `rem:particle-nf-table` | remark | Particle NF decompositions |
| `rem:hecke-operations` | remark | Hecke multiplication examples |

## Key computation witnesses

| Script | Result |
|--------|--------|
| `tbeta-dual-action.py` | $T_\beta^\vee$ traceless; ${}^{14}\mathrm{C}$ emits $L_+ - L_-$ (negative eigenspace of $G$) |
| `shell-knot-qvalues.py` | Shell algorithm: ${}^{14}\mathrm{C}$ at $+0.9\%$ with $T_{3,5}$ |
| `knot-ops-on-6he.py` | All knot operators via $G^{-1}$ on ${}^6\mathrm{He}$ — no single operator reaches 3.508 MeV |
| `h6-full-computation.py` | Full $H_6(q)$: 988 NF terms for ${}^6\mathrm{He}$ Garside element |
| `he4-full-word.py` | ${}^4\mathrm{He}$ Garside: 18 terms, identity = 0, Gram signature $(7{+}, 1{-})$ |
| `borromean-shell-qvalues.py` | Doubly-magic correction: ${}^{40}\mathrm{K}$ improved $-45\% \to -20\%$ |

## Merge conflicts

### `descartes-universe/descartes-universe.ts` (chapter manifest)

**Conflict type:** block ordering within sections.

Both main and this branch added blocks to `sec:nuclear-stability-decay` (§3c).
Main added: `ground-state-ordering`, `transfer-matrix-identities`, `neutron-qvalue-symbolic`.
This branch added those plus: `typed-garside-element`, `gram-weighted-qvalue`, `gram-weight-eigenstructure`.

**Resolution:** keep all blocks, ordered:
1. Existing transfer matrix blocks (main)
2. `typed-garside-element` (definition, depends on transfer matrix)
3. `gram-weighted-qvalue` (proposition, depends on Garside + Gram)
4. `gram-weight-eigenstructure` (remark, interprets proposition)

### `braids-and-knots/braids-and-knots.ts` (chapter manifest)

**Conflict type:** same — block additions in different positions.

**Resolution:** straightforward interleave; no blocks reference the same dependencies.

### `observations/observations.ts`

**Conflict type:** minor — new observation blocks added by both branches.

**Resolution:** append our additions after main's.

### Other `.ts` manifests

Minor `uses[]` and `tags[]` updates. Auto-mergeable.

## Relation to `claude/refine-atom-construction-ay72P`

That branch extends this one with 17 additional content blocks:
- `confinement-lp` (LP formulation of operator selection)
- `derived-atom` (atom construction from pair production)
- `demand-stability` (stability via demand profiles)
- Derived NF witnesses for H, D, ⁴He

It MOVED our 3 new blocks out of §3c into §3d and added its own blocks to §3b. This is a section-placement question, not a conflict. Recommendation: keep our blocks in §3c (they extend the Q-value computation), keep refine-atom's blocks in §3b (they extend the confinement/construction chain).

## No conflicts

- All 69 new content files: unique to this branch, merge cleanly
- All 52 computation scripts: additive, no overlaps
- All Lean files: new stubs, no existing declarations modified
