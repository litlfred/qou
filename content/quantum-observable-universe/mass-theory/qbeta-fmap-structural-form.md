# Structural f-map Derivation Strategy

The f-map $\mathcal{F}$ structurally connects the exact Habiro trace difference $\Delta\text{tr}_M$ to the categorical precision ladder $c_k(q)$.

## 1. Exploratory Series: The Pole Obstruction
To understand why Form A requires a non-trivial categorical map rather than a simple algebraic correction, we generated the exact power series of the ratio $\mathcal{F}(q) = \frac{\Delta(\text{net})}{\Delta\text{tr}_M(q)}$ in terms of $w = q-1$.

Because $\Delta(\text{net}) = q^2 - 2q - 1 = -2 + w^2$ is non-vanishing at $q=1$, but the Markov trace difference $\Delta\text{tr}_M(q)$ vanishes at $q=1$ (yielding a leading term of $-\frac{5}{4}w$), their ratio exhibits a pole:
$$ \frac{\Delta(\text{net})}{\Delta\text{tr}_M(q)} = \frac{8}{5w} - \frac{12}{25} - \frac{92}{125}w + \mathcal{O}(w^2) $$

Since the precision ladder variable $u = b\hbar_q^2$ scales as $\mathcal{O}(w^2)$, it is impossible to express this scalar ratio as a formal power series in $u$. **Conclusion: The f-map cannot be a scalar operator.** It must be a structured transformation on the operator spectrum.

## 2. Derivation Pathways (The 13-Driver Options)

Based on the scoping, we will pursue the formalized f-map via the non-scalar categorical drivers:

### A. Faddeev Recursion (Modular limit)
The Habiro coefficients $a_m \in \mathbb{Z}[u]$ inherently encode the cyclotomic completion. The Faddeev $\Phi_q$ function relates the $q$-difference of the Markov parameter $z(q)$ directly to the modular dual expansion. This bypasses the $1/w$ pole by evaluating the trace at the operator level before taking the classical trace.

### B. Hexagon Equations ($V_{(2,1)}$ projection)
The Hexagon equations extract the $c_k$ coefficients as the braiding eigenvalues on the fundamental representations. The character difference $\chi_{(2,1)}$ contributes the dominant structural form:
$$ \mathcal{F}_{\text{hex}}(w) = \frac{\Delta(\text{net})}{\Delta\chi_{(2,1)}} = \frac{2}{w} + 1 - \frac{11}{2}w + \mathcal{O}(w^2) $$
While also singular as a scalar, the Hexagon equations apply $\mathcal{F}$ as a functor mapping representation weights $y_\lambda$ into the categorical ladder, resolving the singularity algebraically.

### C. Direct Cyclotomic Polynomial Map
The exact integer sequence $a_m$ from the witness can be algorithmically mapped to the $c_k$ sequence by matching the cyclotomic poles of the Habiro expansion to the roots of the $q$-Pochhammer symbols in the ladder. 

## Next Steps
We will begin formally scaffolding the **Direct Cyclotomic Map** (Option 3) alongside the **Hexagon Equations** (Option 2) in Lean to rigorously define the functor mapping the Habiro coefficients $a_m$ to the precision ladder $c_k$.
