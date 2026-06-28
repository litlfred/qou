The [$(q, z)$-bicompletion](#def:qz-bicompletion)
$\widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}$ sits at the apex of a diagram
of cyclotomic completions; its raison d'être is the conjectural mass
element, whose existence and utility we record here together with the
open questions it raises.

The bicompletion sits at the apex of the diagram of cyclotomic
completions:

$$
\begin{array}{ccc}
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
  & \xrightarrow{\;\;z \,\mapsto\, 0\;\;}
  & \widehat{\mathbb{Z}[q]} \\
  \big\downarrow {q \,\mapsto\, q_0} & & \big\downarrow {q \,\mapsto\, q_0} \\
  \widehat{\mathbb{Z}[q^{\pm 1}_0][z]}_z
  & \xrightarrow{\;\;\;\;\;\;\;\;\;\;}
  & \mathbb{Z}[q^{\pm 1}_0][z] \\
\end{array}
$$

(viewed as the natural projection lattice; the bottom-right is the
"realised" ring at the substrate parameter $q_0$).

| Direction | Cyclotomic ideal | Universal element | Cyclotomic projections |
|:---|:---|:---|:---|
| $q$-only ([Habiro ring](#def:habiro-ring)) | $((q;q)_m)$ | colored Jones $J_K \in \widehat{\mathbb{Z}[q]}$ | $J_N(K)$ via $q \mapsto \zeta_N$ |
| $z$-only ([$z$-Habiro ring](#def:z-habiro-ring)) | $(P_n(q, z))$ | brane-tower element (conjectural) | level-$n$ cyclotomic truncation |
| $(q, z)$-joint (this block) | $((q;q)_m \cdot P_n(q,z))$ | mass-element (conjectural) | $J_N$-data + brane-tower data jointly |

## The conjectural mass element in the bicompletion

### Rationale for the bicompletion

The mass-element [conjecture](#conj:mass-endomorphism) connects two
quantum invariants that live in **different** cyclotomic
completions:

1. The **colored Jones** $J_N(K; q)$ of the closed braid $K$ lives in
   $\widehat{\mathbb{Z}[q]}$, encoding the **knot's topological**
   content via cyclotomic projections at $q = \zeta_N$
   (Volume Conjecture).

2. The **brane-tower partial sums** $\Phi_{\mathrm{mass}}^{(N)}(\beta) = \sum_{i=1}^{N}\Phi_q(z_i)$
   live in $\widehat{\mathbb{Z}[q^{\pm 1}][z]}_z$
   (conjectural — see [brane-tower in $z$-Habiro](#conj:brane-tower-z-habiro)),
   encoding the **algebraic-volume** content via cyclotomic projections at
   the structurally determined level $n_\star(\mathfrak{H})$.

The mass formula
$\mathfrak{m}_{q,\mathcal{K}}(T_w) = \sum_\lambda \tilde w_\lambda(q) \cdot \chi_\lambda(\rho(\beta))/\dim_q V_\lambda$
relates these two pieces through the q-deformed Wedderburn-weighted
Markov-trace pairing, which depends on $q$ (through the q-deformed
weights $\tilde w_\lambda = \dim_q^2/[n]_q!$) and on $z$ (through
algebraic-volume coordinates).
A single ambient ring carrying **both** cyclotomic structures is
required to express the relation as an algebraic identity rather
than a coincidence of two independent specialisations.

### Conjectural utility

The bicompletion is **defined**; the **conjectural utility** is that
the mass element

$$
  \mathfrak{m}^{\widehat{\;}}(\beta)
  \;\in\;
  \widehat{\mathbb{Z}[q^{\pm 1}, z]}_{q,z}
$$

(the conjectural lift of $\mathfrak{m}_{q,\mathcal{K}}$ to the
bicompletion) **simultaneously** recovers:

- the colored Jones invariants under $z \mapsto 0$ followed by
  cyclotomic-in-$q$ projection at $q = \zeta_N$, and
- the brane-tower partial sums under $q \mapsto q_0$ followed by
  cyclotomic-in-$z$ projection at level $n_\star(\mathfrak{H})$.

If such $\mathfrak{m}^{\widehat{\;}}$ exists, the **Volume Conjecture**
(asymptotic relation between $J_N$ and $\mathrm{Vol}(K)$) becomes a
**consequence** of the algebraic identity in the bicompletion: the
two cyclotomic projections of the same bicompletion element must
agree on their common image in $\mathbb{R}$ via the realisation
functor.

