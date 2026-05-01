**Non-magic case**: ${}^{6}\mathrm{Li}$ has $Z = N = 3$, neither on
the magic ladder. Both diagrams have Frobenius arms strictly longer
than their legs (or vice versa), so neither is self-conjugate. The
LR fusion fails the rigidity hypothesis and the dominant composite
$\lambda_A$ inherits substantial $\kappa$-imbalance, producing
non-zero topological flux that is not annihilated algebraically and
must be absorbed by higher-jet-order corrections from the Yekutieli
brane tower.

```tex
\begin{tikzpicture}[scale=0.5, every node/.style={font=\footnotesize}]
  % Proton block: 3 boxes, partition (2,1) — arms longer than legs
  \begin{scope}[shift={(0,0)}]
    \draw[thick, fill=blue!10] (0,1) rectangle (1,2);
    \draw[thick, fill=blue!10] (1,1) rectangle (2,2);
    \draw[thick, fill=blue!10] (0,0) rectangle (1,1);
    % flux vector from the asymmetric arm
    \draw[->, very thick, red!70!black] (2.1,1.5) -- (3.4,2.0)
      node[right]{flux};
    \node at (1,-0.7) {$\lambda_Z\,\;(Z=3)$};
  \end{scope}

  % Neutron block: 3 boxes, identical (2,1) shape
  \begin{scope}[shift={(5,0)}]
    \draw[thick, fill=red!10] (0,1) rectangle (1,2);
    \draw[thick, fill=red!10] (1,1) rectangle (2,2);
    \draw[thick, fill=red!10] (0,0) rectangle (1,1);
    \draw[->, very thick, red!70!black] (2.1,1.5) -- (3.4,2.0)
      node[right]{flux};
    \node at (1,-0.7) {$\lambda_N\,\;(N=3)$};
  \end{scope}

  % LR-fusion arrow
  \draw[->, thick] (10,1) -- (11.5,1) node[midway, above]{LR fusion};

  % Composite: shattered into asymmetric skew components, prominent flux
  \begin{scope}[shift={(12.5,-0.5)}]
    \draw[thick, fill=violet!10] (0,2) rectangle (1,3);
    \draw[thick, fill=violet!10] (1,2) rectangle (2,3);
    \draw[thick, fill=violet!10] (0,1) rectangle (1,2);
    \draw[thick, fill=violet!10] (1,1) rectangle (2,2);
    \draw[thick, fill=violet!10] (0,0) rectangle (1,1);
    \draw[thick, fill=violet!40, dashed] (2,1) rectangle (3,2);
    % large flux vector — non-zero kappa
    \draw[->, ultra thick, red!70!black] (3.2,2.0) -- (5.0,2.8)
      node[right]{$\kappa_{\lambda_A}\neq 0$};
    \draw[->, ultra thick, red!70!black] (3.2,1.0) -- (5.0,0.4)
      node[right]{jet leakage};
    \node at (1.5,-0.9) {$\lambda_A\,\;(A=6)$};
  \end{scope}
\end{tikzpicture}
```

The asymmetric skew structure of $\lambda_A$ forces
$\kappa_{\lambda_A} \neq 0$, so the
[full-twist criterion](#conj:categorical-neutrality-saturated-shells)
fails:
the ribbon operator $\theta_6$ acts non-trivially on $V_{\lambda_A}$
and topological flux propagates through the brane tower. The
spectral sequence of
[homological condensation](#conj:homological-shell-condensation)
does **not** collapse at $E_2$; obstruction classes persist into
$E_\infty^{p, q}$ with $q > 0$, demanding higher-jet-order
corrections from the Yekutieli tower. Empirically ${}^{6}\mathrm{Li}$
is loosely bound (separation energy $\approx 1.5\,\mathrm{MeV}$),
in line with this non-confined diagnosis.
