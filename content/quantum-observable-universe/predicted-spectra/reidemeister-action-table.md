Every braid move acts on the three sectors of the categorical action $\mathfrak{S}_q = \mathfrak{S}_q^{\mathrm{grav}} + \mathfrak{S}_q^{\mathrm{gauge}} + \mathfrak{S}_q^{\mathrm{matter}}$ ([canonical action](#prop:qou-canonical-action)). We catalog what each move preserves, what it changes, and what must be tracked for mass and energy calculations.

**The categorical action on a nuclear link.**
For a nucleus $\mathcal{N}(Z, N)$ evaluated at the braid representative $\beta \in B_A$:

$$
  \mathfrak{S}_q[\beta]
  = 
  \underbrace{E_0}_{\text{gravity}}
  + 
  \underbrace{\sum_{\text{crossings}} \mathcal{S}_{ij}(q)}_{\text{gauge}}
  + 
  \underbrace{\mathfrak{S}_q^{\mathrm{matter}}}_{\text{matter (Pauli + pairing)}}.
$$

The gauge sector decomposes via the Iwahori–Hecke algebra. Each crossing $\sigma_i$ contributes weight $q$ (positive), $q^{-1}$ (negative), or $(q + q^{-1})/2$ (mixed).

**Complete move table.**

```tex
\begin{center}
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
  $\beta \mapsto \beta \sigma_n^{± 1}$ &
  $0$ &
  $+q^{± 1}$ &
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
\end{center}
```

**Reading the table for mass/energy calculations.**

1. **Mass:** $\mathrm{Vol}(S^3 \setminus K) / \hbar_q^2$. Only moves that change the volume change the mass. R2 ($q$-deformed), R1, and Skein change the volume. R3, far-comm, and Markov I preserve it.
2. **Binding energy:** $\mathfrak{S}_q^{\mathrm{gauge}}$ evaluated on the Gröbner–Shirshov normal form. R2 ($q$-deformed) is the only Gröbner–Shirshov relation that changes the gauge sector. Each application splits $T^2 \to (q - q^{-1})T + 1$, releasing $q - q^{-1}$ of Coulomb energy and $1$ of volume binding. R3 and far-comm rearrange crossings without energy cost.
3. **$Q$-value:** $\mathfrak{S}_q[\text{parent}] - \mathfrak{S}_q[\text{daughter}]$. The Skein crossing change ($\mathfrak{d} \to \mathfrak{u}$) produces the transition, and the $L_0$ emission carries the electron and antineutrino. The energy released is the gauge sector difference between parent and daughter normal forms. This difference comes entirely from the differing number and type of R2 ($q$-deformed) steps.
4. **Markov trace:** $\prod_i \hat{V}_i$ (the link invariant). R1 and Markov II multiply by $z$ (changing the trace but not the link type). R2 ($q$-deformed) changes the trace through the Hecke coefficients. R3 and far-comm preserve the trace.

**Tracking the ${}^{14}\mathrm{C}$ decay.**

| Quantity | Formula | Source moves |
|----------|---------|:---:|
| Parent mass | $\text{Vol}(\mathcal{N}(6,8)) / \hbar_q^2$ | R2 steps in parent |
| Daughter mass | $\text{Vol}(\mathcal{N}(7,7)) / \hbar_q^2$ | R2 steps in daughter |
| $Q$-value | $M_{\text{par}} - M_{\text{dau}} - m_e$ | Difference in R2 steps |
| $L_0$ amplitude | Skein weight of $e^- \sqcup \nu^{\sigma}$ | Skein crossing change |
| Matrix element | $\lVert\hat{V}(L_0)\rVert^2$ | R2 at converting generator |
| Writhe correction | $(-q^{3/4})^{-\Delta w}$ | R1 (writhe change = $A - 1$) |
| Half-life | $\ln 2 / (\lVert M_q\rVert^2 \times f(Z, Q))$ | All of the above |

**The $q$-deformed R2 is the engine of nuclear physics.**

At $q = 1$ (classical), $T^2 = 1$. All crossings cancel, yielding no binding energy, no Coulomb repulsion, and no beta decay. All nuclear configurations at fixed $A$ are degenerate.

At the substrate parameter $q_0$, $T^2 = 0.209T + 1$. The crossing asymmetry $0.209 = q - q^{-1}$ splits the degeneracy. The $0.209T$ term is the electromagnetic interaction (Coulomb repulsion between protons, Coulomb enhancement of beta decay). The $1$ term is the strong interaction (volume binding, independent of crossing chirality). Every nuclear observable—mass, binding energy, $Q$-value, half-life, shell structure—traces back to this single deformation parameter through the R2 Hecke relation.
