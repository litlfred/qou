# Scope: q Constant Interpretation Purge and QOU Realignment

## Architecture
The QOU project comprises expository markdown literature (expository texts detailing the physical concepts of the Quantum Observable Universe) and a computational codebase written in Python and Rust (which implement simulations and numerical calculations, such as double slit experiments, binding energy calculations, and mass derivations). 
- Expository Literature: Located in `content/quantum-observable-universe/` within directories like `introduction/`, `information-theory/`, `climax-volume-mass/`, `mass-theory/`, and `mass-endomorphism/`.
- Computational Codebase: Located in `computations/` and `simulations/`.
- Manifest / To-Do List: `todos/qa-q-CAL-1-2-3-audit.json`.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Investigation and Scoping | Scan scope folders to find violating files, patterns, and code usages. | None | IN_PROGRESS (Conv: bef42011-d115-4f6d-a501-6ad16568cd60) |
| 2 | Markdown Lit Realignment | Rewrite markdown files in scope to satisfy C1, C2, and C3. | M1 | PLANNED |
| 3 | Computational Codebase Refactoring | Scan and refactor Python and Rust files to rename rigid constant names to mass ratio. | M1 | PLANNED |
| 4 | Execution Verification | Execute sample scripts to verify codebase logic is intact. | M3 | PLANNED |
| 5 | Final Verification & Audit | Independent review, challenge testing, and forensic audit of all changes. | M2, M4 | PLANNED |

## Interface Contracts
- Expository markdown must not contain violating terms: "unobservable background parameter", "invisible ether", "rigid global constant".
- Expository markdown must assert $q$ is the local mass ratio.
- Expository markdown must frame around the 3 calibration points: CAL 1 = $m_e$, CAL 2 = $m_\mu$, CAL 3 = $Q_\beta$ as local evolving fields.
- Expository markdown must identify ratio CAL 2 / CAL 1 ($m_\mu/m_e$) as anchoring vacuum expectation value $q_0 \approx 1.1097$.
- Python/Rust variables representing $q$ as abstract constants must be renamed (e.g. `q_constant` -> `q_mass_ratio` or other contextual names) without breaking functionality.
- Computational outputs must remain identical/numerically stable.
