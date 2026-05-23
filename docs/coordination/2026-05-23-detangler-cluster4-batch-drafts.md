# Detangler cluster-4 remaining splits — batch drafts

**Branch:** `claude/detangler-cluster4-remaining-2026-05-23`
**Watcher:** `local/detangler-integration-watcher`
**Predecessor:** [`docs/coordination/2026-05-22-detangler-backlog-survey.md`](2026-05-22-detangler-backlog-survey.md) §Cluster 4 (drafted 5 of 18, deferred 13)

## Scope

PR #884 closed clusters 1 + 3 + (5 of 18) of cluster-4 splits. The 13 remaining dense sections are drafted below per the Slot F template: per-new-section narrative story + proposed sub-section labels + block partition. Single batch ask follows.

## Story drafts

### P1 — `sec:differential-structures` (20 blocks → 2-way) — quantum-observable-universes

| New section | Story (1-sentence) | Blocks |
|---|---|---:|
| `sec:differential-structures-reeb` | The categorical Reeb derivation: exists / unique / SU(2) instance, plus the projective-line object and contact-affine chart that anchor the differential machinery to the substrate's algebraic structure. | 11 |
| `sec:differential-structures-fiber-adjoint` | The fibre-adjoint involution, its projector onto coadjoint orbits, and the substrate's radial coordinate — the differential-geometric ingredients that the Reeb derivation consumes when it specialises to SU(2). | 9 |

### P2 — `sec:q-special-functions` (19 blocks → 2-way) — quantum-observable-universes

| New section | Story | Blocks |
|---|---|---:|
| `sec:q-special-functions-exp-log` | $q$-exponential and $q$-logarithm: existence + uniqueness theorems, the $p$-adic obstruction, and the finite-field obstruction that prevents naïve specialisation. | 13 |
| `sec:q-special-functions-dilog` | The $q$-dilogarithm (existence + uniqueness + SU(2) form) plus the generating-functions-solve-Reeb-flow result that ties the dilogarithm back to the Reeb derivation. | 6 |

### P3 — `sec:yekutieli-lifting` (22 blocks → 2-way) — lifting-and-descent

| New section | Story | Blocks |
|---|---|---:|
| `sec:yekutieli-lifting-construction` | The Yekutieli lifting condition + quantum characteristic classes (existence + uniqueness): the categorical-lifting machinery that elevates a QU to a QOU via the Frobenius-Hopf substrate. | 14 |
| `sec:yekutieli-lifting-kummer-motivic` | Kummer filtration obstruction + Kummer tower + Hochschild-Kummer connection + motivic substrate / Galois character / motivic-perpetual-obstruction — the motivic enrichment of the lifting condition. | 8 |

### P4 — `sec:archimedean-lifting` (25 blocks → 3-way) — lifting-and-descent

| New section | Story | Blocks |
|---|---|---:|
| `sec:archimedean-lifting-foundations` | Jet-prolongation $\mathbb{C}$, the Yekutieli archimedean band, QU→QOU at the archimedean level, mass-identity $\mathbb{C}$, mass-geometric drag, Euler-characteristic stability, brane-boundary structure — the foundational archimedean-specialisation block. | 10 |
| `sec:archimedean-lifting-topological-mass-formula` | The quantum dilogarithm + its proof + the topological-mass theorem statement + the topological-mass conjecture-extension — the formula's central object. | 4 |
| `sec:archimedean-lifting-topological-mass-variants` | Topological-mass family: eigenspace-decomp / holonomy / transient-localisation / dilogarithm variants + the SU(2) instance + the chapter outro — the variant-and-proof closure of the topological-mass arc. | 11 |

### P5 — `sec:categorical-braiding` (19 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:categorical-braiding-action` | The braid action on tensor products + why $B_3$ + categorical boson-fermion identification + symmetric-quotient colour + braid-base-field + braid-lifting compatibility — the categorical origin of braiding. | 11 |
| `sec:categorical-braiding-hecke-eigenbasis` | Jones-Markov trace + $\mathrm{tr}_M$ Hopf $\sigma_1^2$ closed-form + Hecke log-decomposition + Hecke-algebra-from-braiding + Hecke normal form + dark-vision strand bandwidth + Markov moves brane tower + knot eigenbasis (existence + proof + exhaustiveness) + Feynman eigenbasis — the Hecke quotient and its eigenbasis. | 8 |

### P6 — `sec:vertex-factorisation` (23 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:vertex-factorisation-markov` | Vertex = exceptional-divisor + six operators via vertex factorisation + Breit-Wheeler vertex (with literature trace) + Markov-trace product + Hecke-Markov transition + Markov-lambda knot operations + Markov-chain fluctuations — the vertex/Markov arc. | 13 |
| `sec:vertex-factorisation-feynman` | Feynman eigenbasis decomposition + Feynman trace collapse + Feynman-Markov identification + Feynman categorical trace + Feynman-QOU dictionary + Feynman classical limit — the Feynman-side identification of the vertex factorisation. | 10 |

### P7 — `sec:categorical-mass-foundations` (22 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:categorical-mass-eigenspaces` | Topological-mass categorical eigenspace / descended / transient eigenspace decompositions + their proofs + the categorical-Markov mass identification + atomic-mass GB normal form + the $\rho_K$-graded expansion + Hecke branching trace decomposition + operator-valued magnitude budget + $q$-Hecke seminormal character closure — the eigenspace-side categorical mass foundations. | 14 |
| `sec:categorical-mass-markov-endomorphism` | Recomputed low-isotope mass table + Markov-trace antipode polynomial symmetry + Markov-trace axiomatic closed form + Markov-trace recursive reducer + Markov-Z reconciliation + mass-endomorphism conjecture + categorical-neutrality saturated shells + $\phi_n$ global section — the Markov-trace-side enrichment + mass-endomorphism conjecture. | 8 |

### P8 — `sec:hoefsmit-convergence-atomic` (21 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:hoefsmit-convergence-construction` | Operator-selection LP (now living here per P28) + universal braid branching + Hoefsmit scattering pipeline + Hecke convergence bound + algebraic quantum volume + Habiro ring + Habiro expansion (atomic) + $\mathbb{Z}$-Habiro ring + brane-tower $\mathbb{Z}$-Habiro + per-partition $K_\lambda$ rule — the convergence + Habiro construction. | 11 |
| `sec:hoefsmit-convergence-magic-shells` | Magic-shell stabilization conjecture + two-row stratum + $^4$He channel active set + $^4$He two-row dominance + $^4$He magic-shell fingerprint + Schur-Weyl vanishing + SW-3root rational integrand + Markov-trace Frobenius selection + Hecke 1d-irrep closed-form character + Hoefsmit $V_{21}$ cos-symmetrization — the magic-shell consequences of the Hoefsmit construction. | 10 |

### P9 — `sec:phi-q-markov-schur-weyl-tower` (20 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:phi-q-markov-schur-weyl-foundations` | Markov-trace factorization (now living here per P31) + $\phi_q$ resums trace series + Markov axiom recursive ascent + per-braid mass tower + Schur-Weyl mass decomposition + GB-residue spectral sum + categorical mass positivity + mass-spectrum generating function + graded Markov trace from GS filtration + residue at root — the $\phi_q$ + Markov + Schur-Weyl foundations. | 10 |
| `sec:phi-q-markov-residue-habiro` | $\widehat{V}$-pair commutation trace + tower-pair equality at fixed level + jet-tower uniform $\Delta_{\max}$ + topological-mass formula (algebraic) + residue as braid holonomy + graded-trace residue split + 6-term binding density + full pole structure of mass trace + Habiro residue-sum equivalence — the residue + Habiro identifications that pin the mass tower. | 10 |

### P10 — `sec:plancherel-alpha-ribbon` (19 blocks → 2-way) — braids-and-knots

| New section | Story | Blocks |
|---|---|---:|
| `sec:plancherel-alpha-spectral` | $\alpha_{\mathrm{em}}$ categorical trace + Plancherel term-7 formulation + Plancherel weight boundedness + unified curvature-rank-mass formula + chirality residue mass term + $E_\infty$-page identifications + spectral-sequence $H^3$ explicit + chirality writhe ribbon derivation + Gram-matrix spectral connection — the spectral $\alpha$/ribbon foundations. | 10 |
| `sec:plancherel-knot-factor-mass-tower` | Knot-factor spectral derivation + knot-factor amphicheiral + Borromean-composite knot-factor + shell-closed knot-factor + knot-factor spectral summary + Pauli-factor Wedderburn + mass-formula Wedderburn enumeration + mass-tower coefficient stratification + flavor-dressing functor — the knot-factor + Wedderburn enumeration that closes the mass-tower arc. | 9 |

### P12 — `sec:archimedean-models` — **DONE ON MAIN** (ch5/audit Rec 1-3)

Already split on main in commits `2c722cae0` + `737deea6f` + `b2dea4d5b` + `4829571fc` (2026-05-22 ch5/audit). The single 22-block sec:archimedean-models was decomposed into 8 sub-sections (sec:physical-interpretation, sec:headline-conjectures, sec:archimedean-witnesses, sec:categorical-differential-bridge, sec:non-archimedean-models, sec:witt-vector-lifting, sec:finite-fields, sec:archimedean-encounter) plus 4 blocks moved to descartes-universe/sec:physical-regimes. This batch's P12 draft is superseded; not re-executed.

### P14 — `sec:atomic-shells` (22 blocks → 2-way) — descartes-universe

| New section | Story | Blocks |
|---|---|---:|
| `sec:atomic-shells-foundations` | Shell-structure eigenvalues + shell-eigenvalue properties + quantum-dilogarithm volume + Reidemeister action table + topology-geometry boundary + elliptic-stability locus + shell-closure normal form + torus-knot shell binding + skein finiteness bound + RJ canonical inner product + RJ inner-product interpretation + spectral decomposition $Q$-value + shell construction rules — the shell-construction foundations. | 13 |
| `sec:atomic-shells-element-instances` | Electron-shells Hopf + helium Hopf diagram + noble-gas characterization + metallic-character knot + francium extremal metal + hydrogen shell writhe + hydrogen orbitals + hydrogen-orbital tables — the per-element instances of the shell-construction rules (light atoms + noble gases + metals + hydrogen orbital structure). | 9 |

### P16 — `sec:atomic-braid-mass` (21 blocks → 2-way) — particle-interactions

| New section | Story | Blocks |
|---|---|---:|
| `sec:atomic-braid-mass-foundations` | Atomic-braid LP stability + $q$-integer mass formula + universal ILP algorithm + neutron-proton splitting + color-pairing binding + mass table $Z = 1$-20 + atomic NF witness + step-LP verification + Gröbner reduction methods + tower binding energy + mass categorical descent + Thurston-volume additivity — the atomic-braid LP + mass-formula foundations. | 12 |
| `sec:atomic-braid-mass-crossing-locality-cpt` | Mass-volume factorization + crossing-graded mass expansion + lifted-crossing locality + $q$-holonomy locality derivation + Frobenius-packing density + CPT orbit closure density + bar-involution invariance + soft-confinement at $q_0$ — the crossing-graded + locality + CPT-orbit consequences that close the atomic-braid mass arc. | 8 |

## Naming convention check

Per Slot I "No new `generic-section-name`" invariant: the proposed labels above avoid the `^sec:(.*-)?(part-\d+|extras|misc-\d+)$` regex by using descriptive suffixes (`-foundations`, `-construction`, `-implications`, `-curvature`, `-spectral`, `-magic-shells`, etc.). The detangler invariant is satisfied.

## Story-coherence check

Each proposed split has an opening prose draft (1-2 paragraph stories above) that:

- Names the concept the new section establishes (opener);
- Connects backwards to what the prior section / sub-section settled (`gives us X`);
- Sets up what the next section / sub-section picks up (`leaves with Y`).

Per Slot F template: each split is "paired with a story-coherence ask" so the split is actionable.

## Approval ask

Single batch ask follows (see chat). Once approved, the splits execute as one commit per section (13 commits) on this branch, each with the corresponding new opening prose block + reorg-map R6 entry. Estimated wall time: 30-60 min execution after approval.

## Cluster-4 closure path

After this batch: 18 of 18 H5 dense sections resolved.

Expected post-execution graph delta:
- H5 dense sections: 13 → 0
- H7 remark-ratio: minor ↑ (new opening prose blocks)
- H1 / H2 / H3 / H4 / H6: unchanged (splits don't move blocks across chapter manifests; only re-organise within)
