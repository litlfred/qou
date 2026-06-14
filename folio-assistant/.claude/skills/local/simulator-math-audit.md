---
name: simulator-math-audit
roles: [collaborator, owner, auditor]
---

# Simulator Math Audit Skill

## Role
Ensure that all simulators defined in the repository accurately reflect the underlying mathematical formulas, specifically checking surface area, mass formulas, and physical constants.

## Instructions
1. **Identify Simulators**: Locate all simulator blocks (`kind: "simulator"`) within the `content/` directory and their corresponding `.html` visualisations.
2. **Cross-reference Math**: For each simulator, find the formal definitions (propositions, theorems, equations) it visualises.
3. **Verify Formulas and Constants**:
   - Check surface area formulas for mathematical alignment.
   - Check mass calculations and constants against the Lean formalisation and LaTeX equations.
   - **CRITICAL**: No hardcoded variables or constants are allowed in the simulators. All constants (like $M_e$, $G_F$, $N_A$) and mathematical functions MUST be referenced dynamically from the formal `qou-mass` compute substrate or imported directly from the paper's canonical source of truth. Simulators must act like the compute side of the repository.
4. **Report Deviations**: Create an audit report for any simulator that deviates from the formal math. Use the QA sidecar queues to coordinate fixes.
5. **Teamwork**: Coordinate with other agents using hierarchical `.beans` files. Delegate specific checks (e.g. mass formulas vs surface formulas) to specialised agents.
