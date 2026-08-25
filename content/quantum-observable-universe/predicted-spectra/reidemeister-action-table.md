Every braid move acts on the three sectors of the categorical action $\mathfrak{S}_q = \mathfrak{S}_q^{\mathrm{grav}} + \mathfrak{S}_q^{\mathrm{gauge}} + \mathfrak{S}_q^{\mathrm{matter}}$ ([canonical action](#prop:qou-canonical-action)). For a nucleus $\mathcal{N}(Z, N)$ evaluated at the braid representative $\beta \in B_A$,

$$
  \mathfrak{S}_q[\beta]
  = 
  \underbrace{E_0}_{\text{gravity}}
  + 
  \underbrace{\sum_{\text{crossings}} \mathcal{S}_{ij}(q)}_{\text{gauge}}
  + 
  \underbrace{\mathfrak{S}_q^{\mathrm{matter}}}_{\text{matter (Pauli + pairing)}}.
$$

The gauge sector decomposes via the Iwahori–Hecke algebra: each crossing $\sigma_i$ contributes weight $q$ (positive), $q^{-1}$ (negative), or $(q + q^{-1})/2$ (mixed). Each Reidemeister, Markov, and Skein move acts on the three sectors, the hyperbolic volume, and the Markov trace as follows:

```tex
\begin{center}
\begin{adjustbox}{max width=\linewidth}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{l|c|c|c|c|c|c}
\toprule
\textbf{Move} & \textbf{Algebra} &
  $\mathfrak{S}^{\mathrm{grav}}$ &
  $\mathfrak{S}^{\mathrm{gauge}}$ &
  $\mathfrak{S}^{\mathrm{matter}}$ &
  \textbf{Vol} & \textbf{tr} \\
\midrule
R1 (self-twist) &
  $\sigma_i \mapsto \sigma_i \sigma_n$ &
  $0$ &
  $+q \text{ or } +q^{-1}$ &
  $0$ &
  \textbf{changes} &
  $\times z$ \\
\midrule
R2 ($q$-deformed) &
  $\sigma_i^2 = (q{-}q^{-1})\sigma_i + 1$ &
  $0$ &
  \textbf{splits:} $(q{-}q^{-1})\sigma + 1$ &
  $0$ &
  \textbf{changes} &
  \textbf{changes} \\
\midrule
R2 (classical) &
  $\sigma_i \sigma_i^{-1} = 1$ &
  $0$ &
  $0$ (cancels) &
  $0$ &
  preserved &
  preserved \\
\midrule
R3 (Yang--Baxter) &
  $\sigma_i\sigma_{i+1}\sigma_i$
  $= \sigma_{i+1}\sigma_i\sigma_{i+1}$ &
  $0$ &
  $0$ &
  $0$ &
  preserved &
  preserved \\
\midrule
Far comm. &
  $\sigma_i\sigma_j = \sigma_j\sigma_i$ &
  $0$ &
  $0$ &
  $0$ &
  preserved &
  preserved \\
\midrule
Markov I &
  $\beta \mapsto \gamma\beta\gamma^{-1}$ &
  $0$ &
  $0$ &
  $0$ &
  preserved &
  preserved \\
\midrule
Markov II &
  $\beta \mapsto \beta \sigma_n^{\pm 1}$ &
  $0$ &
  $+q^{\pm 1}$ &
  $0$ &
  preserved &
  $\times z$ \\
\midrule
Skein ($\mathfrak{d} \to \mathfrak{u}$) &
  $q[L_+] - q^{-1}[L_-]$
  $= (q^{1/2}{-}q^{-1/2})[L_0]$ &
  $0$ &
  \textbf{emits} $L_0$ &
  $\Delta\mathfrak{S}_q^{\mathrm{matter}}$ &
  \textbf{changes} &
  \textbf{changes} \\
\bottomrule
\end{tabular}
\end{adjustbox}
\end{center}
```
