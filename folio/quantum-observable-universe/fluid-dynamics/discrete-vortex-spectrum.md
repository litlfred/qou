Let $\varrho$ denote a stable vortex filament of length $L$ in the brane fluid with [aether parameter](#def:substrate-parameter) $q > 1$. Let $\Delta_q$ denote the $q$-Laplacian acting on sections of the normal bundle $N_\varrho$.

Then:

1. The eigenvalues of $\Delta_q$ restricted to $\varrho$ form a discrete spectrum $\{\lambda_k^{(q)}\}_{k \geq 1}$ scaling as

   $$
     \lambda_k^{(q)} = 
     [k]_q^2 \cdot \frac{\hbar_q}{L_q^2},
   $$

   where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the $q$-integer and $L_q$ is the $q$-deformed filament length.

2. The spin label $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ of the $\mathrm{SU}_q(2)$ representation carried by the holonomy around $\varrho$ indexes the **intensity levels** of the vortex. The vortex energy at level $j$ equals

   $$
     E_j^{(q)} = 
     \frac{\hbar_q}{2I_q}[j]_q[j+1]_q,
   $$

   where $I_q$ represents the $q$-deformed moment of inertia of the filament cross-section.

3. The ladder modes $E_\pm$ of the weight-space decomposition mediate transitions between intensity levels $j \to j'$ under the strict selection rule $|j - j'| = 1$. The energy exchanged evaluates to

   $$
     \Delta E_{j \to j'} = 
     \frac{\hbar_q}{2I_q}
     \bigl([j']_q[j'+1]_q - [j]_q[j+1]_q\bigr).
   $$

4. In the classical limit $q \to 1$:
   - $[k]_q \to k$, returning the classical Kelvin-wave spectrum.
   - $[j]_q[j+1]_q \to j(j+1)$, reducing the energy levels to the rigid-rotor spectrum of standard angular momentum.
   - The selection rule $\Delta j = \pm 1$ reduces to the classical dipole selection rule.
