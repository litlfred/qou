**Proposition (meson scale independence).**
*The pion mass $m_\pi$ cannot be derived from the substrate
parameters $(m_\mathfrak{e}, q_0)$ alone.  The Hecke algebra
determines the relative meson mass spectrum (character ratios
between mesons) but not the absolute scale $m_\pi$.*

**Proof (representation-theoretic + topological).**

The baryon mass formula uses
$\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ as the geometric
normalization, where $\mathrm{Vol}(\mathcal{B}_3) = 8G > 0$ is
the hyperbolic volume of the Borromean complement.  The meson's
binding topology is the Hopf link $L_+$, whose complement is a
solid torus: $\mathrm{Vol}(\text{Hopf complement}) = 0$.
Without a non-zero hyperbolic volume, there is no geometric
invariant to set the meson mass scale from $(m_\mathfrak{e}, q_0)$.

The Hecke character ratios under additional crossings are derived:
$\chi^{(3)}(K)/\chi^{(3)}(\pi) = q^2$,
$\chi^{(2,1)}(K)/\chi^{(2,1)}(\pi) = 1/(h^2+1)$,
$\chi^{(1^3)}(K)/\chi^{(1^3)}(\pi) = q^{-2}$.
These determine $m_K/m_\pi$ (given $m_\pi$) but not $m_\pi$ itself.
$\square$

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

The companion Lean `meson_scale_independence` states the scale-independence claim and defers its proof via `sorry` (`-- Ref: [manuscript]`).
