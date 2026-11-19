Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with multiplication $\mu \colon A \otimes A \to A$ and Frobenius form $\int_A \colon A \to \mathbf{1}$. The **Frobenius pairing** is the composite

```tex
\begin{equation}\label{eq:frobenius-pairing}
\langle -, - \rangle \;=\; \textstyle\int_A \circ \mu \colon\;
\begin{tikzcd}[column sep=2.5em, ampersand replacement=\&]
  A \otimes A \ar[r, "\mu"]
  \& A \ar[r, "\int_A"]
  \& \mathbf{1}.
\end{tikzcd}
\end{equation}
```

It is **non-degenerate** if there is a morphism $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ such that the composite

$$
A \xrightarrow{\rho_A^{-1}} A \otimes \mathbf{1}
  \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes (A \otimes A)
  \xrightarrow{\alpha^{-1}} (A \otimes A) \otimes A
  \xrightarrow{\langle -, - \rangle \otimes \mathrm{id}} \mathbf{1} \otimes A
  \xrightarrow{\lambda_A} A
$$

and its mirror image are both $\mathrm{id}_A$.
