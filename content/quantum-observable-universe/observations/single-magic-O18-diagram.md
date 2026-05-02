**Single magic case**: ${}^{18}\mathrm{O}$ has $Z = 8$ (magic) and
$N = 10$ (non-magic, two extra neutrons beyond the $N = 8$ shell).
The proton diagram $\lambda_Z$ is the saturated, self-conjugate
$3\times 3$ staircase block of size $8$ (the canonical magic-$8$
shape). The neutron diagram $\lambda_N$ has two unpaired boxes
projecting outward from the magic-$8$ core, breaking self-conjugacy.

```tex
\begin{tikzpicture}[scale=0.45, every node/.style={font=\footnotesize}]
  % Proton block: saturated self-conjugate 8-shape (magic 8 staircase)
  \begin{scope}[shift={(0,0)}]
    \draw[thick, fill=blue!10] (0,2) rectangle (1,3);
    \draw[thick, fill=blue!10] (1,2) rectangle (2,3);
    \draw[thick, fill=blue!10] (2,2) rectangle (3,3);
    \draw[thick, fill=blue!10] (0,1) rectangle (1,2);
    \draw[thick, fill=blue!10] (1,1) rectangle (2,2);
    \draw[thick, fill=blue!10] (2,1) rectangle (3,2);
    \draw[thick, fill=blue!10] (0,0) rectangle (1,1);
    \draw[thick, fill=blue!10] (1,0) rectangle (2,1);
    \node at (1.5,-0.6) {$\lambda_Z\,\;(Z=8,\;\kappa_{\lambda_Z}=0)$};
  \end{scope}

  % Neutron block: 8-core + 2 unpaired boxes (frayed)
  \begin{scope}[shift={(5,0)}]
    \draw[thick, fill=red!10] (0,2) rectangle (1,3);
    \draw[thick, fill=red!10] (1,2) rectangle (2,3);
    \draw[thick, fill=red!10] (2,2) rectangle (3,3);
    \draw[thick, fill=red!10] (0,1) rectangle (1,2);
    \draw[thick, fill=red!10] (1,1) rectangle (2,2);
    \draw[thick, fill=red!10] (2,1) rectangle (3,2);
    \draw[thick, fill=red!10] (0,0) rectangle (1,1);
    \draw[thick, fill=red!10] (1,0) rectangle (2,1);
    % unpaired (frayed) boxes
    \draw[thick, fill=red!40, dashed] (3,2) rectangle (4,3);
    \draw[thick, fill=red!40, dashed] (3,1) rectangle (4,2);
    \node at (2,-0.6) {$\lambda_N\,\;(N=10,\;\kappa_{\lambda_N}\neq 0)$};
  \end{scope}

  % LR-fusion arrow
  \draw[->, thick] (10.5,1.5) -- (12,1.5)
    node[midway, above]{LR fusion};

  % Composite: dominant module retains rigid Z-core but shows frayed overhang
  \begin{scope}[shift={(13,-0.5)}]
    \foreach \x in {0,1,2} \foreach \y in {2,3} {
      \draw[thick, fill=violet!10] (\x,\y) rectangle (\x+1,\y+1);
    }
    \foreach \x in {0,1,2} {
      \draw[thick, fill=violet!10] (\x,1) rectangle (\x+1,2);
    }
    \foreach \x in {0,1} {
      \draw[thick, fill=violet!10] (\x,0) rectangle (\x+1,1);
    }
    % frayed N overhang propagates
    \draw[thick, fill=violet!40, dashed] (3,2) rectangle (4,3);
    \draw[thick, fill=violet!40, dashed] (3,1) rectangle (4,2);
    % topological flux vector
    \draw[->, very thick, red!70!black] (4.2,2.5) -- (5.6,3.0)
      node[right]{$\kappa_{\lambda_A}\neq 0$};
    \node at (2,-0.9) {$\lambda_A\,\;(A=18)$};
  \end{scope}
\end{tikzpicture}
```

The composite $\lambda_A$ retains the rigid $\lambda_Z$ core but
inherits the unpaired boxes from $\lambda_N$. Content additivity
gives

$$
  \kappa_{\lambda_A}
  \;=\;
  \kappa_{\lambda_Z} + \kappa_{\lambda_N}
  \;=\;
  0 + (\text{positive}) \;\neq\; 0,
$$

so the global topological charge does not vanish: ${}^{18}\mathrm{O}$
is single-magic, not double-magic. The
[homological-condensation criterion](#conj:homological-shell-condensation)
fails at $A = 18$, consistent with ${}^{18}\mathrm{O}$ not being on
the double-magic list.
