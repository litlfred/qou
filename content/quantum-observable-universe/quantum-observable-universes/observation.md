Let $(\mathbf{C}, A, \tau)$ be a quantum observable
universe with state bundle $\mathcal{S} \to M$, let $q$
denote the
([substrate parameter](#def:substrate-parameter)), let
$p \colon \mathbf{1} \to A$ be a
([categorical point](#def:categorical-point)), and let
$U \subset M$ be an open causal neighbourhood of $p$.

An *intent on $U$* is a pair $(\mathfrak{O}, \epsilon)$
where $\epsilon \in \{+1, -1\}$ is the **direction** and

$$
  \mathfrak{O}  \in 
  \Gamma\bigl(U, \mathrm{Ad}(J^1 \mathcal{S})\bigr)
$$

is a section of the adjoint bundle of the $1$-jet
prolongation of $\mathcal{S}$.  The sign $\epsilon$
determines the arrow of time:
$\epsilon = +1$ (braiding, $\sigma_i$, forward under
$\prec_c$) or $\epsilon = -1$ (unbraiding,
$\sigma_i^{-1}$, backward).

The section $\mathfrak{O}$ satisfies:

1. **Frobenius compatibility.** The observation preserves
   the Frobenius form on $U$:

   ```tex
   \begin{equation}\label{eq:observation-frobenius}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A / \mathfrak{m}_p^2 \ar[r, "\mathfrak{O}_p"] \ar[dr, "\int_{A,p}"']
     & A / \mathfrak{m}_p^2 \ar[d, "\int_{A,p}"] \\
     & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   at every $p \in U$, where $\int_{A,p}$ is the germ of
   the Frobenius form.  Measurement is consistent: the trace
   is preserved.

2. **Adjoint backreaction.** The observation acts on the
   colour fibre via the adjoint representation of $G$.  At
   each point $p$, the section $\mathfrak{O}_p$ conjugates by
   $G$: it rotates the colour degrees of freedom, shifting
   the substrate parameter $q \mapsto q' = q + \delta q$
   via the Hopf coaction:

   ```tex
   \begin{equation}\label{eq:observation-substrate}
   \begin{tikzcd}[row sep=2.5em, column sep=3em]
     A \ar[r, "\Delta"] \ar[d, "\mathfrak{O}_p"']
     & A \otimes A \ar[r, "\mathfrak{O}_p \otimes S"]
     & A \otimes A \ar[d, "\mu"] \\
     A \ar[rr, "\int_A"']
     & & \mathbf{1}
   \end{tikzcd}
   \end{equation}
   ```

   with $\delta q(p) = \int_A(\mathfrak{O}_p(a_{(1)})S(a_{(2)}))$.
   Observing the universe changes it: the act of reading the
   field feeds back through the colour fibre into the Reeb
   flow.

An intent at a **point** is the restriction
$\mathfrak{O}_p = \mathfrak{O}|_p$, recovering the germ-level
endomorphism $\mathfrak{O}_p \colon A / \mathfrak{m}_p^2 \to A / \mathfrak{m}_p^2$.  The sign $\epsilon$ determines
whether the crossing injected at $p$ is $\sigma_i$ (forward,
$\epsilon = +1$) or $\sigma_i^{-1}$ (backward,
$\epsilon = -1$) in the braiding-induced ordering $\prec_c$.
