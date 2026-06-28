Let $\mathcal{S}_0$ be a big bang state
([big bang state](#def:big-bang-state)) in an affine chart $U$,
and let $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
be the brane tower
([jet prolongation](#prop:jet-prolongation)).

The **cosmic microwave background** (CMB) of $\mathcal{S}_0$
is the boundary datum

$$
  \mathrm{CMB}(\mathcal{S}_0)
  = 
  \bigl(
    \Gamma(U, A_1/A_0)|_{\mathcal{S}_0}, 
    \Gamma(U, A_2/A_0)|_{\mathcal{S}_0}
  \bigr)
$$

— the pair of degree-$1$ (linear transport) and degree-$2$
(curvature) jet data at $\mathcal{S}_0$.  Since
$A_0|_{\mathcal{S}_0} = 0$ (the defining condition of a big
bang state), the CMB is equivalently the restriction of
$A_1 \oplus A_2$ to $\mathcal{S}_0$:

$$
  \mathrm{CMB}(\mathcal{S}_0)
   \cong 
  \bigl(A_1 \oplus A_2\bigr)\big|_{\mathcal{S}_0}.
$$

**Content of the CMB.**

| Degree | Jet data | Physical content |
|:---:|:---|:---|
| $1$ | $A_1/A_0$: linear transport | Photon polarization modes ($\sigma_0, \sigma_1$), winding numbers, first-order correlations |
| $2$ | $A_2/A_0$: curvature | Hopf-link cross-terms ($L_{\pm}$), linking numbers, power spectrum |

**Exclusions from the CMB.**

Degree-$0$ data ($A_0$) is absent: no photon identity
$\mathbf{1}$, no particle labels, no knot types.  The CMB
is **thermal** in the precise sense that it carries the
**color content** $(\varphi_0, \varphi_1)$ of the boundary
photons ([photon color content](#rem:cmb-photon-color-content))
without their individual identities (degree $0$).

**Role in aeon structure.**
If $\mathcal{S}_0$ is the past boundary of an aeon $\mathcal{A}$
([aeon](#def:aeon)), then $\mathrm{CMB}(\mathcal{S}_0)$ is the
seed from which the aeon's forward light cone unfolds.  The first
Planck step $\mathcal{S}_0 \to \mathcal{S}_1$ regenerates
non-trivial degree-$0$ data by applying the Reeb flow $f_q$ to
the degree-$1$ transport data — the CMB "condenses" into
particles.

If $\mathcal{S}_0$ is also the future boundary of a preceding
aeon $\mathcal{A}'$, then $\mathrm{CMB}(\mathcal{S}_0)$ is
inherited from the terminal horizon of $\mathcal{A}'$
([aeon boundary generates chart](#rem:aeon-boundary-generates-chart)):
the CMB of one aeon is the thermal remnant of the previous
aeon's final state.
