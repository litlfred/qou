Let $(\mathbf{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category, and let $V$ be a simple object that is symplectically self-dual: there exists an isomorphism $\phi \colon V \xrightarrow{\sim} V^{\vee}$ satisfying $\phi^{\vee} = -\phi$. This alternating condition forces $\mathrm{rank}(V) = 2$. Specifically, the evaluation map $\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through $\Lambda^2 V$, producing an epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$. For $\epsilon$ to be non-degenerate, it is necessary that $\mathrm{rank}(\Lambda^2 V) = 1$. The volume form factorization is:

```tex
\begin{equation}\label{eq:volume-form-factorisation}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  V \otimes V
    \ar[r, "\mathrm{id} \otimes \phi"]
    \ar[d, "\pi"', two heads]
  & V \otimes V^{\vee}
    \ar[d, "\mathrm{ev}_V"]
  \\
  \Lambda^2 V
    \ar[r, "\epsilon"', dashed]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

This construction intrinsically satisfies the volume form requirement of the QOU axioms.
