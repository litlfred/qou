Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe over a
ring $R$ ([quantum observable universe](#def:quantum-observable-universe)), let $q$
denote the
([substrate parameter](#def:substrate-parameter)), and let
$p \colon \mathbf{1} \to A$ be a
([categorical point](#def:categorical-point)).  An
*observation at $p$* is a morphism

$$
  \mathcal{O}_p \;\colon\; A / \mathfrak{m}_p^2
  \;\longrightarrow\; A / \mathfrak{m}_p^2
  \qquad\text{in } \mathcal{C},
$$

acting on germs at $p$, satisfying:

1. **Frobenius compatibility.** The observation preserves
   the Frobenius form at $p$:

   ```tex
   \begin{equation}\label{eq:observation-frobenius}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A / \mathfrak{m}_p^2 \ar[r, "\mathcal{O}_p"] \ar[dr, "\int_{A,p}"']
     & A / \mathfrak{m}_p^2 \ar[d, "\int_{A,p}"] \\
     & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   where $\int_{A,p}$ is the germ of the Frobenius form at $p$.

2. **Substrate perturbation.** The observation shifts the
   deformation parameter $q \mapsto q' = q + \delta q$ via the
   Hopf coaction:

   ```tex
   \begin{equation}\label{eq:observation-substrate}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A \ar[r, "\Delta"] \ar[d, "\mathcal{O}_p"']
     & A \otimes A \ar[r, "\mathcal{O}_p \otimes S"]
     & A \otimes A \ar[d, "\mu"] \\
     A \ar[rr, "\int_A"']
     & & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   with $\delta q(p) = \int_A(\mathcal{O}_p(a_{(1)})\,S(a_{(2)}))$
   evaluated at the point $p$.
