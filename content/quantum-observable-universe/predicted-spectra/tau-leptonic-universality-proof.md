The $T_{3,5}$ weak vertex acts as a **mediator** between the
parent tau $T_{2,7}$ and the daughter lepton $T_{2,n_\ell}$.
In the Iwahori--Hecke algebra $H_3(q)$, one may form the product
$T_{2,n_\ell} \cdot T_{3,5} \cdot T_{2,7}$ and reduce to
normal form.  However, the correct physical amplitude is **not**
this product trace.

The key observation is that the weak vertex **creates** the
daughter lepton (topological quantum number conservation) rather
than composing with it.  The $T_{3,5}$ braid mediates the
crossing change; the daughter lepton $T_{2,n_\ell}$ and the two
neutrinos ($\nu = \mathbf{1}$) are produced as separate link
components.  The transition amplitude therefore **factorises**:

$$
  \mathcal{M}(\tau \to \ell\bar\nu\nu_\tau)
  = 
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5})
   \times 
  (\text{kinematic factors depending on } m_\ell).
$$

Since $\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})$ is independent
of which daughter lepton is created, the matrix element
$|\mathcal{M}|^2$ cancels in the ratio, leaving only the
phase-space factor $f(m_\ell^2 / m_\tau^2)$.

**Contrast with the product model.**
If one instead treats the amplitude as
$\mathrm{tr}_3(T_{2,n_\ell} \cdot T_{3,5} \cdot T_{2,7})$,
the non-commutativity of $H_3(q)$ introduces a
daughter-dependent correction that breaks universality:
$|\mathcal{M}_e|^2 / |\mathcal{M}_\mu|^2 \approx 0.69 \neq 1$.
The product model treats the daughter as **composed** with the
vertex rather than **created** by it, violating the topological
separation of link components in the Skein decomposition
([lepton number](#def:lepton-number-categorical)). $\square$
