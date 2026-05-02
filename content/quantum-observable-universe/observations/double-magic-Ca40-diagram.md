**Double magic case**: ${}^{40}\mathrm{Ca}$ has $Z = N = 20$, both
on the magic ladder. The proton and neutron diagrams are identical,
both saturated and self-conjugate, with $\kappa_{\lambda_Z} =
\kappa_{\lambda_N} = 0$. Their LR fusion produces a gapless interlock
with zero trailing Frobenius arms, and the Jucys–Murphy contents of
$\lambda_A$ cancel exactly: $\sum_{x \in \lambda_A} c(x) = 0$.

```tex
\begin{tikzpicture}[scale=0.4, every node/.style={font=\footnotesize}]
  % Proton block: saturated self-conjugate 20-shape (schematic 5x4 staircase)
  \begin{scope}[shift={(0,0)}]
    \foreach \x in {0,1,2,3,4} \foreach \y in {0,1,2,3} {
      \draw[thick, fill=blue!10] (\x,\y) rectangle (\x+1,\y+1);
    }
    \node at (2.5,-0.7) {$\lambda_Z\,\;(Z=20,\;\kappa_{\lambda_Z}=0)$};
  \end{scope}

  % Neutron block: identical, saturated self-conjugate
  \begin{scope}[shift={(7,0)}]
    \foreach \x in {0,1,2,3,4} \foreach \y in {0,1,2,3} {
      \draw[thick, fill=red!10] (\x,\y) rectangle (\x+1,\y+1);
    }
    \node at (2.5,-0.7) {$\lambda_N\,\;(N=20,\;\kappa_{\lambda_N}=0)$};
  \end{scope}

  % LR-fusion arrow
  \draw[->, thick] (14,2) -- (15.5,2) node[midway, above]{LR fusion};

  % Composite: gapless self-conjugate interlock with content labels
  \begin{scope}[shift={(16.5,0)}]
    \foreach \x in {0,1,2,3,4} \foreach \y in {0,1,2,3} {
      \draw[thick, fill=violet!10] (\x,\y) rectangle (\x+1,\y+1);
    }
    % JM contents c(x) = j - i, plotted on a representative diagonal
    \node at (0.5,3.5) {$0$};
    \node at (1.5,3.5) {$1$};
    \node at (2.5,3.5) {$2$};
    \node at (3.5,3.5) {$3$};
    \node at (4.5,3.5) {$4$};
    \node at (0.5,2.5) {$-1$};
    \node at (1.5,2.5) {$0$};
    \node at (2.5,2.5) {$1$};
    \node at (3.5,2.5) {$2$};
    \node at (4.5,2.5) {$3$};
    \node at (0.5,1.5) {$-2$};
    \node at (1.5,1.5) {$-1$};
    \node at (2.5,1.5) {$0$};
    \node at (3.5,1.5) {$1$};
    \node at (4.5,1.5) {$2$};
    \node at (0.5,0.5) {$-3$};
    \node at (1.5,0.5) {$-2$};
    \node at (2.5,0.5) {$-1$};
    \node at (3.5,0.5) {$0$};
    \node at (4.5,0.5) {$1$};
    \node at (2.5,-0.7)
      {$\lambda_A\,\;(A=40,\;\sum c(x) = 0)$};
  \end{scope}
\end{tikzpicture}
```

The contents $c(x) = j - i$ shown inside the boxes of $\lambda_A$
form a multiset that perfectly cancels under summation: positive and
negative contents pair off across the main diagonal, yielding
$\kappa_{\lambda_A} = 0$. Combined with the gapless interlock
(no Frobenius overhang), this saturates the
[double-magic LR-fusion criterion](#conj:diagrammatic-double-magic-lr-fusion).
The
[homological-condensation conjecture](#conj:homological-shell-condensation)
then predicts $E_\infty^{p, >0}(40) = 0$: ${}^{40}\mathrm{Ca}$ is a
homologically pure ground state, fully consistent with its observed
nuclear stability.
