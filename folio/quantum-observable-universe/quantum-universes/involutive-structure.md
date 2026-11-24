Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category. An **involutive structure** on $\mathbf{C}$ is a contravariant endofunctor $\dagger \colon \mathbf{C}^{\mathrm{op}} \to \mathbf{C}$ satisfying:

1. **Identity on objects:** $X^{\dagger} = X$.
2. **Involutivity:** $f^{\dagger\dagger} = f$:

   ```tex
   \begin{equation}\label{eq:involutivity-cd}
   \begin{tikzcd}[column sep=5em]
     X \ar[r, bend left=30, "f = f^{\dagger\dagger}"]
     & Y \ar[l, bend left=30, "f^{\dagger}"]
   \end{tikzcd}
   \end{equation}
   ```

3. **Monoidal compatibility:** $(\mathrm{id}_X \otimes f)^{\dagger} = \mathrm{id}_X \otimes f^{\dagger}$:

   ```tex
   \begin{equation}\label{eq:monoidal-dagger-cd}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     X \otimes Y \ar[r, "\mathrm{id} \otimes f"]
       \ar[d, "(\mathrm{id} \otimes f)^{\dagger}"']
     & X \otimes Z \ar[d, "\mathrm{id} \otimes f^{\dagger}"] \\
     X \otimes Z \ar[r, equal]
     & X \otimes Z
   \end{tikzcd}
   \end{equation}
   ```

4. **Contravariance:** $(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$:

   ```tex
   \begin{equation}\label{eq:dagger-contravariance}
   \begin{tikzcd}[column sep=3em]
     X \ar[r, "f"] & Y \ar[r, "g"] & Z
   \end{tikzcd}
   \quad\xmapsto{\dagger}\quad
   \begin{tikzcd}[column sep=3em]
     Z \ar[r, "g^{\dagger}"] & Y \ar[r, "f^{\dagger}"] & X
   \end{tikzcd}
   \end{equation}
   ```
