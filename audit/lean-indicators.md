# Lean indicators (per block, with rollups)

_Generated: 2026-04-26T17:10:54.745Z · commit `a58506e2e96d`_

Each row's **Rollup** is a content-addressable SHA-256 over the row's inputs (block) or its children's rollups (section / chapter / paper / folio). Comparing rollups across runs tells you exactly which subtree changed.

Columns: **Sorry** = total active sorry; **Uncited** = sorry without a `-- Ref:` citation in the 3 preceding lines; **Axiom** = `axiom` declarations; **Admit** = `admit` occurrences; **Trivial** = `: True := by trivial` placeholders; **LoC** = Lean code lines (non-comment, non-blank).

## Folio rollup

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **folio** | 1396 | 537 | 169 | 24 | 79 | 0 | 0 | 15111 | `23de7e5d3a59` |

## Papers

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| On the Mechanics of Quantum Observable Universes (`quantum-observable-universe`) | 1355 | 532 | 169 | 24 | 79 | 0 | 0 | 15048 | `bb214ca72c43` |
| Controlled Double-Slit Electron Diffraction (`bach2013-double-slit`) | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `5d3d643bced5` |
| Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings (`unital-groebner-bases`) | 17 | 5 | 0 | 0 | 0 | 0 | 0 | 63 | `e01df857e6fe` |
| Integration of Skewed-Poisson Structures on Non-commutative Formal Groups (`fred2005-formal-groups`) | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `04942cf0f131` |
| QOU Visualizer (`visualizer`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `6f0d2851a83d` |

## Paper: On the Mechanics of Quantum Observable Universes

### Chapters

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction (`introduction`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `7845fc5450ed` |
| Quantum Universes (`quantum-universes`) | 48 | 23 | 7 | 0 | 0 | 0 | 0 | 534 | `18735c23e57f` |
| Quantum Observable Universes (`quantum-observable-universes`) | 206 | 102 | 33 | 0 | 15 | 0 | 0 | 2202 | `5912fe02a02c` |
| Lifting and Descent (`lifting-and-descent`) | 99 | 33 | 2 | 0 | 5 | 0 | 0 | 823 | `3e58e8707325` |
| Braids and Knots (`braids-and-knots`) | 274 | 146 | 76 | 20 | 31 | 0 | 0 | 4323 | `5b4afd3c8c10` |
| Models of QOUs (`models-of-qous`) | 39 | 12 | 0 | 0 | 0 | 0 | 0 | 299 | `0f8b75ef9b92` |
| The Algebraic Substrate (`algebraic-substrate`) | 58 | 25 | 10 | 1 | 2 | 0 | 0 | 486 | `e1d3761723ee` |
| Fluid Dynamics of the Brane (`fluid-dynamics`) | 56 | 6 | 0 | 0 | 0 | 0 | 0 | 51 | `474d7c242a81` |
| Information-Theoretic Perspectives (`information-theory`) | 75 | 30 | 3 | 1 | 1 | 0 | 0 | 1295 | `c5c7259effb4` |
| The Descartes Universe (`descartes-universe`) | 191 | 79 | 24 | 0 | 17 | 0 | 0 | 2951 | `09f5a7eabe11` |
| Particle Interactions and Nuclear Structure (`particle-interactions`) | 74 | 22 | 10 | 2 | 7 | 0 | 0 | 849 | `864e1955aa6f` |
| Physical Observations (`observations`) | 109 | 23 | 4 | 0 | 0 | 0 | 0 | 967 | `c813c6a24f7e` |
| Molecular Construction from Nucleon Braids (`molecular-construction`) | 25 | 11 | 0 | 0 | 1 | 0 | 0 | 208 | `d6cd8ee872d0` |
| $q$-Geometric Langlands Correspondence (`q-geometric-langlands`) | 24 | 7 | 0 | 0 | 0 | 0 | 0 | 7 | `283ec762d0a0` |
| Glossary (`glossary`) | 23 | 8 | 0 | 0 | 0 | 0 | 0 | 53 | `610df52a56fd` |
| Knot-Periodic Table of the Elements (`appendix-knot-periodic-table`) | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `3d45ca614166` |
| Knot Operation Actions Dictionary (`appendix-knot-operations`) | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `99e273cc6ab1` |
| Transfer Matrices (`appendix-transfer-matrices`) | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `66a21c39f950` |
| Atomic Mass Calculations (`appendix-atomic-mass-calculations`) | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `8865203b868f` |
| Surreal-number lift of QOU (appendix) (`appendix-surreals`) | 27 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | `80bd968a6127` |
| Index of Definitions (`index-of-definitions`) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `35129ce2f6d5` |

### Sections

#### Introduction

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Overview | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `92ef7a74edfb` |

#### Quantum Universes

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `54785a519667` |
| Preliminary: rigid monoidal categories | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 62 | `b7600cf9ac3f` |
| The Quantum Universe | 17 | 8 | 3 | 0 | 0 | 0 | 0 | 200 | `51fa40817593` |
| Consequences of the QU axioms | 10 | 3 | 0 | 0 | 0 | 0 | 0 | 73 | `494428ad7859` |
| Structures on a Quantum Universe | 15 | 9 | 4 | 0 | 0 | 0 | 0 | 199 | `c9ab2304deda` |

#### Quantum Observable Universes

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| The Quantum Observable Universe | 9 | 4 | 1 | 0 | 0 | 0 | 0 | 97 | `d86c983b5d86` |
| Emergence from observability | 12 | 7 | 0 | 0 | 1 | 0 | 0 | 154 | `0cc2b991b74c` |
| Maximal torus and weight decomposition | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 80 | `f4779cdf168a` |
| Vectors, hadrons, and the PawLei basis | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 33 | `a0d21a2edf32` |
| Differential structures and gauge actions | 17 | 11 | 1 | 0 | 1 | 0 | 0 | 250 | `2f6b57556cf5` |
| Substrate parameter and deformation | 15 | 9 | 1 | 0 | 3 | 0 | 0 | 325 | `d996bc26806e` |
| Examples of quantum observable universes | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 54 | `49d23f424301` |
| Categorical Dirac operator | 5 | 3 | 2 | 0 | 0 | 0 | 0 | 32 | `37c4286d30d2` |
| Categorical Lagrangian | 5 | 3 | 2 | 0 | 0 | 0 | 0 | 31 | `2b3a3b1deda7` |
| Categorical action | 8 | 4 | 2 | 0 | 0 | 0 | 0 | 93 | `4202975a3dff` |
| Variational equations and wavefronts | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 39 | `54fa535974d0` |
| Particles, fermions, bosons, and observation | 15 | 7 | 2 | 0 | 0 | 0 | 0 | 148 | `2bbbe7834a50` |
| Geometric interpretations | 9 | 1 | 1 | 0 | 10 | 0 | 0 | 62 | `91709acb9de6` |
| Categorical instanton and self-duality | 12 | 7 | 2 | 0 | 0 | 0 | 0 | 132 | `c78f55b5a357` |
| Non-vanishing of $d_q^2$ and jet prolongation | 8 | 6 | 2 | 0 | 0 | 0 | 0 | 155 | `5efb0de36b11` |
| $q$-Deformed operators | 8 | 6 | 0 | 0 | 0 | 0 | 0 | 153 | `f36fb5101f3c` |
| $q$-Harmonic analysis: heat equation, Laplace, Fourier | 38 | 21 | 16 | 0 | 0 | 0 | 0 | 232 | `429af40f084d` |
| Braiding conventions: eigenvalue labelling, ribbon, orientation | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 44 | `9bea7de6cf83` |
| Elaboration: categorical context | 12 | 1 | 0 | 0 | 0 | 0 | 0 | 21 | `e2dac7420872` |
| Non-vanishing of $d_q^2$ and the $q$-jacobiator | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 67 | `3aec30e07b35` |
| Physical elaborations | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `538118853042` |

#### Lifting and Descent

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jet Prolongation and the Recursive Brane Tower | 8 | 3 | 0 | 0 | 0 | 0 | 0 | 59 | `b325a7761a2a` |
| Categorical Lifting: Transport and Torsion | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 36 | `e22484b64dd6` |
| Descent Preliminaries | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 28 | `9f5223032c32` |
| Categorical Lifting and Quantum Characteristic Classes | 17 | 6 | 2 | 0 | 0 | 0 | 0 | 115 | `5094965a583c` |
| Direct Limit Algebra | 11 | 4 | 0 | 0 | 3 | 0 | 0 | 126 | `2a665d5e3a3c` |
| Mass in the Brane Tower | 9 | 4 | 0 | 0 | 0 | 0 | 0 | 58 | `73583f946c54` |
| Betti Numbers and Harmonic Basis | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 12 | `fb3cb99956b7` |
| Descent | 12 | 3 | 0 | 0 | 0 | 0 | 0 | 108 | `a78a37e0855e` |
| Cosimplicial Crossed Groupoid Structure | 10 | 4 | 0 | 0 | 0 | 0 | 0 | 137 | `f50d29cf2d3d` |
| Localized Knots | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 60 | `be48cc2e3577` |
| Archimedean Specialisations | 14 | 3 | 0 | 0 | 2 | 0 | 0 | 84 | `47e32688b073` |

#### Braids and Knots

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `18bd200c5288` |
| Categorical origin of braiding | 16 | 5 | 0 | 0 | 1 | 0 | 0 | 301 | `bf6c91e5c013` |
| Braid group and symmetric group | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 15 | `f952ee5300af` |
| $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ framework | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 64 | `55faa163e1e3` |
| Braid involutions and holonomy | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 21 | `144592c50e9c` |
| The trefoil knot | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `87d1cc18e1a1` |
| Knot fundamental groups | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `48fe893e6c92` |
| Universal enveloping algebras and quantum groups | 10 | 5 | 8 | 0 | 0 | 0 | 0 | 508 | `ab69ed14d74c` |
| Categorical Möbius energy and self-avoidance | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 91 | `0b96db1feae1` |
| Crossing energy and Coulomb charge | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 85 | `90137a8936c0` |
| Lagrange Resolvents and $q$-Deformed Kinematics | 7 | 4 | 1 | 0 | 0 | 0 | 0 | 247 | `d4bc367b2efe` |
| Exceptional Divisor and Vertex Operators | 5 | 3 | 0 | 0 | 1 | 0 | 0 | 49 | `d1fe399e8e0b` |
| Vertex Factorisation and the Markov Trace | 14 | 5 | 6 | 0 | 0 | 0 | 0 | 151 | `beb39db35ea5` |
| Transfer Matrix and Topological Mass | 10 | 6 | 2 | 0 | 1 | 0 | 0 | 159 | `911e17e2dfa0` |
| Braiding Relations and the Spectral Filter | 4 | 3 | 4 | 0 | 11 | 0 | 0 | 161 | `80edb008377f` |
| Hadron Algebra and Knot Factorisation | 11 | 6 | 2 | 0 | 5 | 0 | 0 | 103 | `b5543ef99a17` |
| Skein Generation and Particle Correspondence | 6 | 3 | 1 | 0 | 3 | 0 | 0 | 76 | `ccb2ba0185fd` |
| Bundle Structure and Observation | 7 | 3 | 0 | 0 | 0 | 0 | 0 | 86 | `b39f8bd0e7d7` |
| Borromean Baryons and Reidemeister Invariance | 9 | 6 | 0 | 0 | 8 | 0 | 0 | 188 | `834c4c939d63` |
| Categorical Mass Foundations | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 82 | `549dc631bc63` |
| Calibration and Algebraic Mass Formula | 26 | 18 | 15 | 3 | 1 | 0 | 0 | 481 | `b1b74103676b` |
| Atom, Isotope, and Confinement Levels | 29 | 25 | 13 | 9 | 0 | 0 | 0 | 307 | `6a238a680d4f` |
| Nuclear Binding and Beta Stability | 69 | 34 | 18 | 7 | 0 | 0 | 0 | 1072 | `af8e624e3337` |
| Varying Euler Characteristic and the Mirror Bundle | 14 | 6 | 6 | 1 | 0 | 0 | 0 | 76 | `53cef287eb22` |

#### Models of QOUs

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Physical interpretation and the main result | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 86 | `62d383970fb0` |
| Archimedean specialisations | 21 | 7 | 0 | 0 | 0 | 0 | 0 | 156 | `691778c71053` |
| Non-Archimedean models | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `c4c2ea99da98` |
| Lifting via Formal Groups and Witt Vectors | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 57 | `aaa3f99a008b` |
| Finite fields and Jones polynomials | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `3cabe6b8b15a` |

#### The Algebraic Substrate

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| The algebraic substrate and the Reeb derivation | 10 | 6 | 2 | 1 | 0 | 0 | 0 | 104 | `0ef65afb0e15` |
| The unit particle as a cohomological defect | 7 | 6 | 0 | 0 | 0 | 0 | 0 | 96 | `643153b3e688` |
| The spectral trace and Tannaka--Krein duality | 7 | 4 | 3 | 0 | 2 | 0 | 0 | 79 | `436374e4bbe9` |
| Geometric stability via the Weil bound | 6 | 3 | 3 | 0 | 0 | 0 | 0 | 84 | `14787edec1e9` |
| The classical limit and the macroscopic continuum | 28 | 6 | 2 | 0 | 0 | 0 | 0 | 123 | `697c8e3855db` |

#### Fluid Dynamics of the Brane

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| $q$-deformed hydrodynamics | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 16 | `1ba441d0e6af` |
| Vortex spectrum and helicity | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `cc6e141d9e0b` |
| Turbulence and acoustics | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `01e0be757068` |
| Global regularity for $q > 1$ | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `55774eb8bfe3` |
| The NS obstruction | 18 | 5 | 0 | 0 | 0 | 0 | 0 | 35 | `2bebd809dbd1` |
| Approaches and open problems | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `6eeee2cecc4a` |

#### Information-Theoretic Perspectives

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Emergent Gravity and Information Geometry | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `bff4d4cb4526` |
| Time and Computation | 7 | 2 | 0 | 0 | 0 | 0 | 0 | 39 | `4602a1a511b6` |
| Golden Ratio, Julia Sets, and Discrete Dynamics | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 13 | `1ca77c2fd418` |
| Speed of Light and Mass--Energy Equivalence | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 67 | `710b7c99ffe5` |
| Computation at Planck Time Lengths | 8 | 2 | 1 | 1 | 0 | 0 | 0 | 103 | `195b0f1acd29` |
| P versus NP as a Boundary Condition | 6 | 3 | 0 | 0 | 0 | 0 | 0 | 347 | `ccb3d92dfd1a` |
| $q$-Heat kernel and spectral analysis | 4 | 3 | 2 | 0 | 0 | 0 | 0 | 78 | `da06cc6eb0a9` |
| Statistical Mechanics | 12 | 6 | 0 | 0 | 0 | 0 | 0 | 377 | `f94def39dc2f` |
| Phase Transitions and Sublimation | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 115 | `a40483af0b0b` |
| Incompleteness and the Horizon | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 35 | `dbbd2d9cf97e` |
| Horizons and Aeons | 13 | 7 | 0 | 0 | 1 | 0 | 0 | 121 | `7e0af69e3f03` |
| Quantum Geometry Variants | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `c076df785ab1` |

#### The Descartes Universe

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Why this universe | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `f17fa66e781a` |
| Bring's surface as a QOU | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 79 | `d362ef8494a3` |
| Color tube coordinates | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 29 | `75af94289c5d` |
| Coral fibration and elliptic curves | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 55 | `8e2fdda7d4de` |
| Bundle structures and smoothness | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 35 | `bc96f5d0ed87` |
| Spectral resolvents and gauge structures | 12 | 6 | 3 | 0 | 0 | 0 | 0 | 246 | `dc31c1c8c010` |
| The Descartes condition and lepton spectrum | 19 | 7 | 0 | 0 | 2 | 0 | 0 | 206 | `87f2b7d23db3` |
| Fundamental particles | 50 | 27 | 15 | 0 | 0 | 0 | 0 | 580 | `030b38c86ce6` |
| Nuclear stability and decay | 27 | 15 | 0 | 0 | 2 | 0 | 0 | 913 | `5456160ac256` |
| Atomic shells and the periodic table | 21 | 8 | 5 | 0 | 6 | 0 | 0 | 370 | `c6084fced04a` |
| The Descartes theorem | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 31 | `84e31f67ffd5` |
| Topological mass and the knot-particle spectrum | 18 | 5 | 1 | 0 | 6 | 0 | 0 | 196 | `1e221778190c` |
| Orbital Symmetry and Cohomological Embedding | 6 | 3 | 0 | 0 | 1 | 0 | 0 | 211 | `d603dbf3c489` |

#### Particle Interactions and Nuclear Structure

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| The Gröbner–Shirshov reduction engine | 9 | 5 | 0 | 0 | 5 | 0 | 0 | 274 | `873915127390` |
| Confinement operator selection | 7 | 1 | 1 | 1 | 0 | 0 | 0 | 13 | `77c68fb6e226` |
| Nucleon derivation from pair production | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | `bf1f32c17912` |
| Nuclear binding and magic numbers | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `49a2673f9c33` |
| Derived atom examples | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `814249cace5d` |
| Typed Garside element and Gram-weighted $\mathcal{Q}_q$-value | 3 | 2 | 6 | 0 | 0 | 0 | 0 | 76 | `ac15f9da5b37` |
| Transfer matrices and beta decay | 11 | 3 | 0 | 0 | 0 | 0 | 0 | 205 | `c6be1f2231a1` |
| Atomic braid and Wedderburn mass formula | 20 | 8 | 3 | 1 | 2 | 0 | 0 | 190 | `c4f97619c051` |
| Branching Q-value derivation | 11 | 2 | 0 | 0 | 0 | 0 | 0 | 90 | `fc48d881744c` |

#### Physical Observations

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| The Substrate Consistency Window | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `9467ad64bd54` |
| Particle Identification Conjectures | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 40 | `db822d416fc6` |
| Double-slit experiment | 5 | 2 | 1 | 0 | 0 | 0 | 0 | 61 | `0aa8cbefa40f` |
| Substrate Parameter from Lepton Masses | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 104 | `58fb0a4502d9` |
| Mass Predictions and CODATA Comparison | 14 | 5 | 3 | 0 | 0 | 0 | 0 | 150 | `1d40ca0d2ae9` |
| Beta Decay | 13 | 2 | 0 | 0 | 0 | 0 | 0 | 310 | `8c397fb789d2` |
| Large-Scale Observations | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 13 | `3ab964aa096c` |
| Nuclear Stability | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `863eef88e279` |
| Strangelet Stability and Deconfinement | 11 | 5 | 0 | 0 | 0 | 0 | 0 | 193 | `838bdc62f6c0` |
| Precision Tests | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `27395998ac68` |
| Proton Radius and Gravity Tests | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 48 | `9003d459705c` |
| Crystal Resonance Experiments | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b8a6824935ce` |
| Breit--Wheeler Pair Creation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `cf244426878a` |
| Complexity and Interpretation | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 48 | `ed6c4e159e2d` |
| Transcendence Falsifiability Signatures | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `93d84893a230` |
| Interactive Simulations | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `61a00f4033bb` |

#### Molecular Construction from Nucleon Braids

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| The molecular Hecke algebra | 4 | 3 | 0 | 0 | 1 | 0 | 0 | 24 | `e3dde19c61ab` |
| Electron shells and bonding capacity | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 154 | `35e2d2585b30` |
| Hydrogen molecule $H_2$: the covalent bond prototype | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | `88223780b0be` |
| Carbon monoxide: heteronuclear bonding | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | `f600d22486ff` |
| Carbon dioxide: linear triatomic molecule | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | `1d1420b6de20` |
| Methane: tetrahedral bonding from braid optimization | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | `59009898a57c` |
| Benzene: delocalization from threading links | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 8 | `0c8efc99c64c` |

#### $q$-Geometric Langlands Correspondence

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `ac5523fbcb3c` |
| $\mathbb{G}_m$-torsors and $q$-local systems | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | `ed4b26daf8a2` |
| $q$-Hecke correspondences | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | `b0a7b12bdb73` |
| The $q$-Geometric Langlands conjecture | 7 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | `a5dd1772d0ca` |
| $q$-Opers and the spectral side | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | `b2ac118e8dda` |
| Classical limit and physical interpretation | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `7f97e3529d1b` |

#### Glossary

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Basic categorical notions | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `cbb4a03a1e27` |
| Monoidal structure | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `5f035c0ee3ef` |
| Duality and rigidity | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `af42cc149599` |
| Enrichment | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `9f9a8ef4d659` |
| Geometry and transport | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 32 | `264f46a41424` |
| Groups and symmetry | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 7 | `ae047fc8534a` |
| Information theory | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `47722528e8b5` |
| Elliptic and surface geometry | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 14 | `998dbb37a3dc` |

#### Knot-Periodic Table of the Elements

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Knot diagrams of light atoms | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `bff538532c09` |
| Knot formulas for all elements | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `2e884c7895f2` |
| Knot-centric periodic table | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `295226e2649a` |

#### Knot Operation Actions Dictionary

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Particle normal forms | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `ccada4ef2668` |
| Hecke algebra operations | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `4c2763015c7d` |
| Gluon models and nucleon NF | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b34351f251c7` |
| Knot operator action on basis pairs | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `927c4aa67dd0` |
| Hadron-level knot decomposition table | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b81400d9735a` |

#### Transfer Matrices

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Notation and conventions | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `362be1eb4068` |
| The general transfer matrix | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `f5b55d1c7938` |
| Transfer matrices of knot pairs | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `8f5e8af4e4e6` |
| Interaction and decay matrices | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `3610b6d882aa` |
| Worked examples (light nuclei) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `e2ef011c4b81` |
| Inductive construction ($A \to A+1$) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `ec46e0bb6eaf` |
| Heavy-atom worked examples | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b95cbfcf05c5` |

#### Atomic Mass Calculations

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Method and input parameters | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `d2b04438ac7c` |
| Worked calculations for all elements ($Z = 1$ to $118$) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `73eb4752ec99` |
| Summary and percentage deviations | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `23eabab7a966` |
| $q$-integer mass table (zero fitted parameters) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `e366c85c86e5` |

#### Surreal-number lift of QOU (appendix)

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Motivation and scope | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `5796e230d288` |
| What survives and what breaks | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `a2d46863b451` |
| Surreal construction as a grading | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | `e2e11356078a` |
| Standard-part replaces classical limits | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `d56728c30afc` |
| Conway normal form and asymptotic notation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `bd4fc1bcc416` |
| Named surreals for singular objects | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | `c722c19f94a0` |
| Relaxing strict equalities to $1 + \varepsilon$ | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `8c4369a71a5b` |
| Speculative reformulations | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `3a13ee928328` |
| Characteristic-$p$ companion: nimber surreals | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `1b14e8b9eeae` |
| Outlook | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `4fb40e1cc02a` |

#### Index of Definitions

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Index | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `77de2c02f7c5` |

## Paper: Controlled Double-Slit Electron Diffraction

### Chapters

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Controlled Double-Slit Electron Diffraction (`double-slit-experiment`) | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `17a1c9c9fe1a` |

### Sections

#### Controlled Double-Slit Electron Diffraction

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b2a6aee5d145` |
| Experimental setup | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `39a04c4a9dd9` |
| Results | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `aa9030d95014` |

## Paper: Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings

### Chapters

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings (`unital-groebner-bases-chapter`) | 17 | 5 | 0 | 0 | 0 | 0 | 0 | 63 | `a2335f1434d4` |

### Sections

#### Unital Gröbner--Shirshov Bases over Arbitrary Commutative Ground Rings

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `7e9f4f1aaa6a` |
| Monomials, orderings, and admissible systems | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 35 | `f7aca68593e7` |
| Division algorithm and Gröbner--Shirshov bases | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 28 | `1d27c13c1a61` |
| Main results | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `308fd7c883b7` |

## Paper: Integration of Skewed-Poisson Structures on Non-commutative Formal Groups

### Chapters

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Formal Groups and the Lifting Theorem (`formal-groups-chapter`) | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `abf75b33dfbb` |

### Sections

#### Formal Groups and the Lifting Theorem

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Commutative formal group | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `52cbd8febde2` |
| Skewed-Poisson structure | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `17e95e6f7177` |
| Integration theorem | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `812fc84ba5b3` |
| Gröbner–Shirshov deformation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `fe6516d1dc24` |
| Strong multiplicativity | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `45ae357ecfa0` |
| Witt vector lift | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `9f356d5061e9` |
| Unit-root F-crystal | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `2fb627e31a95` |

## Paper: QOU Visualizer

### Chapters

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Overview (`overview`) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `b1fb66e0f683` |

### Sections

#### Overview

| Name | Blocks | Lean | Sorry | Uncited | Axiom | Admit | Trivial | LoC | Rollup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Introduction | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `ce5d2fe2d183` |
| Bring's Surface | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `823249db98b2` |
| Knot Complements | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `c5c345efa505` |

## Top blocks by uncited sorry

| Block | Chapter | Sorry | Uncited | File |
|---|---|---:|---:|---|
| prop:shell-closure-stability | Braids and Knots | 3 | 3 | `content/quantum-observable-universe/braids-and-knots/shell-closure-stability.lean` |
| prop:confinement-phase-stratification | Braids and Knots | 3 | 3 | `content/quantum-observable-universe/braids-and-knots/confinement-phase-stratification.lean` |
| prop:habiro-expansion-atomic | Braids and Knots | 5 | 2 | `content/quantum-observable-universe/braids-and-knots/habiro-expansion-atomic.lean` |
| prop:partition-sum-proton-residual | Braids and Knots | 3 | 2 | `content/quantum-observable-universe/braids-and-knots/partition-sum-proton-residual.lean` |
| prop:jet-tower-convergence | Braids and Knots | 4 | 2 | `content/quantum-observable-universe/braids-and-knots/jet-tower-convergence.lean` |
| prop:figure-eight-bw-coefficients | Braids and Knots | 2 | 1 | `content/quantum-observable-universe/braids-and-knots/figure-eight-bw-coefficients.lean` |
| def:confinement-category | Braids and Knots | 1 | 1 | `content/quantum-observable-universe/braids-and-knots/confinement-category.lean` |
| def:dressed-particle | Braids and Knots | 1 | 1 | `content/quantum-observable-universe/braids-and-knots/dressed-particle.lean` |
| prop:level-sufficiency | Braids and Knots | 1 | 1 | `content/quantum-observable-universe/braids-and-knots/level-sufficiency.lean` |
| prop:schur-weyl-mass-decomposition | Braids and Knots | 2 | 1 | `content/quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.lean` |
| prop:full-pole-structure-mass-trace | Braids and Knots | 1 | 1 | `content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.lean` |
| prop:unified-curvature-rank-mass-formula | Braids and Knots | 1 | 1 | `content/quantum-observable-universe/braids-and-knots/unified-curvature-rank-mass-formula.lean` |
| def:hyperelliptic-quintic | Braids and Knots | 2 | 1 | `content/quantum-observable-universe/braids-and-knots/hyperelliptic-quintic.lean` |
| thm:substrate-self-duality | The Algebraic Substrate | 1 | 1 | `content/quantum-observable-universe/algebraic-substrate/substrate-self-duality.lean` |
| prop:q-game-of-life | Information-Theoretic Perspectives | 1 | 1 | `content/quantum-observable-universe/information-theory/q-game-of-life.lean` |
| prop:confinement-sdp | Particle Interactions and Nuclear Structure | 1 | 1 | `content/quantum-observable-universe/particle-interactions/confinement-sdp.lean` |
| conj:crossing-graded-mass-expansion | Particle Interactions and Nuclear Structure | 1 | 1 | `content/quantum-observable-universe/particle-interactions/crossing-graded-mass-expansion.lean` |

---

**Staleness**: every row's `Rollup` is the SHA-256 over its inputs and (for non-leaves) its children's rollups. If you commit this report and the rollup at any level changes on the next run, that subtree is stale. Per-block input SHAs are recorded in `audit/lean-indicators.json` (`files.{ts,lean,md}.sha`).
