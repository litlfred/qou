Let $\partial$ be the horizon functor
([horizon functor](#def:horizon-functor)) and let
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
be the brane tower
([jet prolongation](#prop:jet-prolongation)).

The **CMB functor** is the composition

$$
  \mathrm{CMB}
  \;\colon\;
  \pi_0\!\bigl(\mathrm{Bun}^{\circ}\bigr)
  \;\xrightarrow{\;\partial\;}
  \mathcal{P}\!\bigl(\mathrm{Bun} \setminus \mathrm{Bun}^{\circ}\bigr)
  \;\xrightarrow{\;\varinjlim (A_1/A_0 \oplus A_2/A_0)\;}
  \mathbf{Mod}_R
$$

that sends each aeon $\mathcal{A}$ to the colimit of the
degree $\geq 1$ jet quotients over its boundary:

$$
  \mathrm{CMB}(\mathcal{A})
  \;=\;
  \varinjlim_{\mathcal{S} \in \partial(\mathcal{A})}
  \bigl(A_1/A_0 \oplus A_2/A_0\bigr)\big|_{\mathcal{S}}.
$$

The target category $\mathbf{Mod}_R$ is the category of
$R$-modules (sections of the jet quotient sheaves over the
boundary).

**Components.**

| Factor | Jet degree | Content |
|:---|:---:|:---|
| $\varinjlim\, (A_1/A_0)|_{\partial\mathcal{A}}$ | $1$ | Linear transport: winding modes, first-order correlations |
| $\varinjlim\, (A_2/A_0)|_{\partial\mathcal{A}}$ | $2$ | Curvature: linking modes, power spectrum |

The colimit is taken over the directed system of all diagrams
in $\mathcal{A}$ that converge to boundary objects.  It
aggregates the degree $\geq 1$ data from **every light cone**
within the aeon that reaches the boundary — not just one
computation sequence.

**Relation to the pointwise CMB.**
For a single boundary object $\mathcal{S}_0 \in \partial(\mathcal{A})$,
the pointwise CMB
([CMB boundary datum](#def:cmb-boundary-datum))
$\mathrm{CMB}(\mathcal{S}_0) = (A_1/A_0, A_2/A_0)|_{\mathcal{S}_0}$
is the stalk of the CMB functor at $\mathcal{S}_0$.  The full
CMB functor is the sheafification over the entire boundary.

**Conformal invariance.**
By [conformal invariance at the jet horizon](#prop:horizon-conformal-invariance),
the CMB functor is independent of the choice of generator of
the horizon ideal $\mathfrak{h} \subset A_0$.  It depends only
on the vanishing locus — the conformal class of $A_0$.
