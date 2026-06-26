Let $\varrho$ be a stable vortex filament of length $L$ in the
brane fluid with [substrate parameter](#def:substrate-parameter)
$q > 1$, and let $\Delta_q$ be the $q$-Laplacian acting on
sections of the normal bundle $N_\varrho$.

Then:

1. The eigenvalues of $\Delta_q$ restricted to $\varrho$ form a
   discrete spectrum $\{\lambda_k^{(q)}\}_{k \geq 1}$ with

   $$
     \lambda_k^{(q)} = 
     [k]_q^2 \cdot \frac{\hbar_q}{L_q^2},
   $$

   where $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ is the
   $q$-integer and $L_q$ is the $q$-deformed filament length.

2. The **intensity levels** of the vortex are indexed by the
   spin label $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$ of the
   $\mathrm{SU}_q(2)$ representation carried by the holonomy
   around $\varrho$.  The vortex energy at level $j$ is

   $$
     E_j^{(q)} = 
     \frac{\hbar_q}{2I_q}[j]_q[j+1]_q,
   $$

   where $I_q$ is the $q$-deformed moment of inertia of the
   filament cross-section.

3. Transitions between intensity levels $j \to j'$ are
   mediated by the ladder modes $E_\pm$ of the weight-space
   decomposition, with selection rule $|j - j'| = 1$.  The
   energy released or absorbed is

   $$
     \Delta E_{j \to j'} = 
     \frac{\hbar_q}{2I_q}
     \bigl([j']_q[j'+1]_q - [j]_q[j+1]_q\bigr).
   $$

4. In the classical limit $q \to 1$:
   - $[k]_q \to k$ and the Kelvin-wave spectrum is recovered.
   - $[j]_q[j+1]_q \to j(j+1)$ and the energy levels reduce to
     the rigid-rotor spectrum of angular momentum theory.
   - The selection rule $\Delta j = \pm 1$ reduces to the
     standard dipole selection rule.
