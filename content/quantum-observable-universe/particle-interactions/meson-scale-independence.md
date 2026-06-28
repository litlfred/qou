**Proposition (meson scale independence).**
*The pion mass $m_\pi$ cannot be derived from the substrate
parameters $(m_\mathfrak{e}, q_0)$ alone.  The Hecke algebra
determines the relative meson mass spectrum (character ratios
between mesons) but not the absolute scale $m_\pi$.*
## Calibration structure

The three calibration inputs are independent physical measurements,
each associated with a decay process:

| Anchor | Observable | Jet order | Measurement |
|--------|-----------|-----------|-------------|
| **CAL-1** | $m_\mathfrak{e}$ | $h^0$ | electron mass (Penning trap) |
| **CAL-2** | $\mathfrak{D}_\beta$ | $h^2$ | neutron $\beta$-decay width ($\tau_n = \hbar / \mathfrak{D}_\beta$) |
| **CAL-3** | $\mathfrak{D}_\pi$ | $h^3$ | pion decay width ($\tau_\pi = \hbar / \mathfrak{D}_\pi$) |

CAL-2 determines $\mathfrak{Q}_\beta = m_n - m_p - m_\mathfrak{e}$ from the
neutron lifetime, which in turn fixes $q_0$ via the substrate
identity.  CAL-3 determines $m_\pi$ from the pion lifetime, which
fixes the meson mass scale.  All other masses (proton, neutron,
muon, kaon, $\ldots$) are derived from these three inputs.

The $h^1$ jet order is absent: the bar involution
$q \mapsto q^{-1}$ forces all Markov traces of writhe-zero braids
to be even functions of $h$.  The $h^3$ order enters through
the flavor-split $X = (q-1)^2(1-q^{-4})/3 = h^3/6 + \cdots$,
which is a skein difference (not a single-braid Markov trace).

## Lean formalization

The companion Lean `meson_scale_independence` encodes the geometric core of the obstruction: the Hopf-link complement (meson binding topology) has hyperbolic volume $0$ while the Borromean complement (baryon) has positive volume, so the volume-scaling map $m_\mathfrak{e}\cdot\mathrm{Vol}(K)\cdot\rho/\hbar_q^2$ sends the meson's geometric scale to $0$ independently of $(m_\mathfrak{e}, q_0)$. The absolute scale therefore enters only through the independent calibration CAL-3 ($\mathfrak{D}_\pi$). The Lean is sorry-free.
