The jet horizon ([jet horizon](#def:jet-horizon)) provides an algebraic model of a black hole event horizon.

Hawking radiation \cite{hawking1975} predicts that black holes emit thermal radiation at temperature $T_H = \hbar c^3 / (8\pi G M k_B)$. This radiation carries no internal information. It exhibits a Planck spectrum determined entirely by the mass $M$.

The jet-horizon framework translates this into a direct algebraic interpretation:

1. **Degree-$0$ data is trapped.** The horizon ideal $\mathfrak{h} \subset A_0$ blocks all zeroth-order sections. No particle identity (knot type or crossing structure) crosses the horizon. This states the information paradox algebraically: the full fibre data of $A_0$ remains inaccessible from the outside.

2. **Degree $\geq 1$ data leaks.** The quotients $A_1/A_0$ and $A_2/A_0$ carry non-trivial sections across $\mathcal{H}$. These constitute the first and second Taylor coefficients of the energy function (linear transport as winding number, curvature as linking number). This data is thermal. It depends on statistical properties (temperature $\sim \eta_q$, operational entropy ([operational entropy](#def:operational-entropy))) rather than individual particle states.

3. **The Bekenstein--Hawking entropy** \cite{bekenstein1973} $S = A / (4\ell_P^2)$ counts the independent degree $\geq 1$ sections on the horizon surface $\mathcal{H}$. In the QOU framework, the area $A$ is the rank of $\Gamma(\mathcal{H}, A_1/A_0)$. This rank measures the dimension of the first-order jet data that the horizon can support.

4. **No photons escape.** Photons are degree-$0$ objects ($K = \varnothing$, step $0$ in the jet-Planck correspondence ([jet-Planck steps](#rem:jet-planck-steps))). The horizon ideal blocks them alongside all other degree-$0$ data. What an external observer detects as "thermal photons" are actually degree-$1$ winding modes lacking knot identity. These are the Hawking quanta.
