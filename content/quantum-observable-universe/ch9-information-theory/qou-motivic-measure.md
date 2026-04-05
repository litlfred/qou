The **$q$-motivic measure** $\mu_q$ assigns elements of the
localized Grothendieck ring to definable subloci of the
[moduli of quantum observables](#def:qo-moduli):

$$
  \mu_q \colon
  \{\text{definable subloci of } \mathfrak{M}_{\mathrm{QO}}\}
  \;\to\; K_0(\mathbf{C})[L_q^{-1}]
$$

where $L_q := [V] \in K_0(\mathbf{C})$ is the class of the
fundamental object ($\dim_q V = [2]_q = q + q^{-1}$), the
categorical analog of the Lefschetz motive
$\mathbb{L} = [\mathbb{A}^1]$ in Denef–Loeser's theory.

For a definable sublocus $\mathcal{D} \subset
\mathfrak{M}_{\mathrm{QO}}$, the measure decomposes along the
[axiom filtration](#def:qou-locus):

$$
  \mu_q(\mathcal{D})
  \;=\; \sum_{k=0}^{3}
  [\mathcal{D} \cap (\mathfrak{M}_k \setminus \mathfrak{M}_{k+1})]
  \cdot L_q^{-k}
$$

where $\mathfrak{M}_0 = \mathfrak{M}_{\mathrm{QO}}$,
$\mathfrak{M}_1 = \mathfrak{M}_{\mathrm{obs}}$,
$\mathfrak{M}_2 = \mathfrak{M}_{\mathrm{meas}}$,
$\mathfrak{M}_3 = \mathfrak{M}_{\mathrm{QOU}}$.

**Properties.**

1. **Additivity**: $\mu_q(\mathcal{D}_1 \sqcup \mathcal{D}_2)
   = \mu_q(\mathcal{D}_1) + \mu_q(\mathcal{D}_2)$.

2. **Multiplicativity under products**: For independent definable
   conditions $\varphi, \psi$, the motivic measure of the
   conjunction is $\mu_q(D(\varphi \wedge \psi))
   = \mu_q(D(\varphi)) \cdot \mu_q(D(\psi))$ in $K_0(\mathbf{C})$.

3. **Dimensional weight**: Each axiom level carries a factor of
   $L_q^{-1}$, so deeper constraints are exponentially suppressed
   — reflecting that QOUs are "rare" in the space of QOs.

The Frobenius trace $\int_A$ on the substrate algebra provides the
categorical integration pairing: for a function
$f \colon \mathcal{D} \to K_0(\mathbf{C})$, the motivic integral
$\int_{\mathcal{D}} f \, d\mu_q$ is computed via the Frobenius
form $\lambda \colon A \to \mathbf{1}$.
