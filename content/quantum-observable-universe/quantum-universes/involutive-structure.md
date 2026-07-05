An involutive structure abstracts the adjoint — the
conjugate-transpose of Hilbert-space linear algebra — so that the
$\mathrm{SU}(2)$ representation category (and any rigid monoidal
category) carries a $\ast$-operation, induced by the Hopf antipode.
The axioms record exactly the properties the adjoint enjoys.

Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal
category. An **involutive structure** (also called a
*$\ast$-structure* or *dagger structure*) on $\mathbf{C}$ is
a contravariant endofunctor
$\dagger \colon \mathbf{C}^{\mathrm{op}} \to \mathbf{C}$ satisfying:

1. **Identity on objects:** $X^{\dagger} = X$ for every
   object $X$.
2. **Involutivity:** $f^{\dagger\dagger} = f$ for every
   morphism $f$, depicted:

   ```tex
   \begin{equation}\label{eq:involutivity-cd}
   \begin{tikzcd}[column sep=5em]
     X \ar[r, bend left=30, "f = f^{\dagger\dagger}"]
     & Y \ar[l, bend left=30, "f^{\dagger}"]
   \end{tikzcd}
   \end{equation}
   ```

3. **Monoidal compatibility:**
   $(\mathrm{id}_X \otimes f)^{\dagger} = \mathrm{id}_X \otimes f^{\dagger}$.

4. **Contravariance:**
   $(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$:

   ```tex
   \begin{equation}\label{eq:dagger-contravariance}
   \begin{tikzcd}[column sep=3em]
     X \ar[r, "f"] & Y \ar[r, "g"] & Z
   \end{tikzcd}
   \quad\xmapsto{\dagger}\quad
   \begin{tikzcd}[column sep=3em]
     Z \ar[r, "g^{\dagger}"] & Y \ar[r, "f^{\dagger}"] & X
   \end{tikzcd}
   \qquad\text{(contravariance)}
   \end{equation}
   ```

For the Hopf algebra $A$ in a quantum universe, the antipode $S$ provides
a natural involutive structure on the representation category via
$f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$. In the
$\mathrm{SU}(2)$ example, this is the Hilbert-space adjoint
([dagger on SU(2)](#ex:dagger-su2)).
