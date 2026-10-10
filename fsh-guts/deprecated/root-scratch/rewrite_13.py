import os
import sys

input_file = "/Users/litlfred/space_cats/qou/amalgamated_input/particle-interactions_seq13.md"
output_file = "/Users/litlfred/space_cats/qou/amalgamated_done/particle-interactions_seq13.md"
report_file = "/Users/litlfred/space_cats/qou/amalgamated_done/particle-interactions_seq13.md.report.md"

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(input_file, "r") as f:
    content = f.read()

# I will write the replacements here
replacements = {
    "skein-particle-generation-intro.md": """<!-- FILE_START: skein-particle-generation-intro.md -->
Hadrons factorise uniquely into knot constituents under the relation algebra. A single family of fundamental strands—the torus knots $T_{m,n}$—generates every hadron under Skein moves. The resulting dictionary identifies each torus generator with a physical particle. We read its mass directly from the linking number and constituent volume.

This section presents the constructive hierarchy. We first exhibit $T_{m,n}$ as the generating family for the hadron monoid under Skein moves ([Proposition: Skein generation of hadrons](#prop:skein-generation)). We then split the resulting mass into a topological linking term and an additive constituent volume ([Lemma: Mass functional on a Skein resolution](#lem:mass-functional)). The knot-particle generation encapsulates this structure, assigning a physical colour-tube reading to the constituents ([knot-particle generation](#def:knot-particle)). We identify each generator with a physical particle via the $q$-Schur--Weyl functor ([Proposition: Knot--particle correspondence](#prop:knot-particle)). The dictionary tabulates the resulting matches: torus knots and Hopf links to fundamental fermions, and Borromean composites to baryons ([dictionary](#rem:dictionary)). A visual inventory collects the small-crossing knots with their braid words and assignments ([visual inventory](#rem:visual-inventory)). The subsequent section uses this correspondence to lift the dictionary to a bundle of state spaces over the brane manifold.

_(draft.)_
<!-- FILE_END: skein-particle-generation-intro.md -->""",

    "atomic-braid.md": """<!-- FILE_START: atomic-braid.md -->
**Definition.**
*The **atomic braid** of a neutral atom $(Z, N)$ is the element of $H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons, and $Z$ electrons into a single Hecke algebra with $A + Z$ strands, where $A = Z + N$. The crossing coefficients are:*

See [Table 1](#tbl:atomic-braid-table1-data).

*We determine the **ground-state ordering** by:*

1. *Nuclear ordering: minimize $\Phi_1$ over all permutations of $Z$ protons and $N$ neutrons (exact search for $\binom{A}{Z} \leq 50000$, steepest :refterm[descent]{#descent} otherwise).*
2. *Electron insertion: greedily insert each of $Z$ electrons at the position minimizing $\Phi_1$.*

*This greedy insertion produces **ep pairs**, where each electron sits immediately before its proton. The $\mathfrak{n}e = \mathrm{id}$ crossing implies electrons pass through neutrons without generating Hecke generators.*

*For hydrogen ($A = 1$), the bare $[e, \mathfrak{p}]$ braid is LP-unstable (Proposition \\ref{prop:atomic-lp-stability}). The $\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues $(q^5, -q^{-5})$ instead of bare $(q^{-1}, -q)$.*
<!-- FILE_END: atomic-braid.md -->"""
}

# Wait, there are more blocks. Let's do it directly in Python for the 13 file.
