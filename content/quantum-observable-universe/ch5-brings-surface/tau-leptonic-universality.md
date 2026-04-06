The tau lepton decays leptonically via the $T_{3,5}$ weak
vertex ([beta decay](#def:beta-decay-skein)).  The **factorised
model** — in which the squared matrix element is
$|\mathcal{M}|^2 = |\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})|^2$,
independent of the daughter lepton — **predicts lepton
universality** directly from the Hecke algebra structure.

## Statement

Let $T_{3,5} = (\sigma_0 \sigma_1)^5$ be the weak vertex in
$H_3(q)$, and let $f(x)$ denote the phase-space factor for
$\tau \to \ell \, \bar\nu_\ell \, \nu_\tau$ with
$x = (m_\ell / m_\tau)^2$:

$$
  f(x)
  = 1 - 8x + 8x^3 - x^4 - 12 x^2 \ln x.
$$

Then the ratio of leptonic branching fractions is

$$
  \frac{\mathrm{BR}(\tau \to e\,\bar\nu_e\,\nu_\tau)}
       {\mathrm{BR}(\tau \to \mu\,\bar\nu_\mu\,\nu_\tau)}
  \;=\;
  \frac{|\mathcal{M}_e|^2 \cdot f(m_e^2/m_\tau^2)}
       {|\mathcal{M}_\mu|^2 \cdot f(m_\mu^2/m_\tau^2)}.
$$

In the **factorised model**, the Markov trace of the weak vertex
is the universal matrix element:

$$
  |\mathcal{M}_e|^2
  \;=\;
  |\mathcal{M}_\mu|^2
  \;=\;
  \bigl|\mathrm{tr}_{\mathrm{Markov}}(T_{3,5})\bigr|^2,
$$

so the matrix-element ratio is exactly $1$, and the branching
ratio reduces to the **pure phase-space ratio**:

$$
  \frac{\mathrm{BR}(\tau \to e)}{\mathrm{BR}(\tau \to \mu)}
  \;=\;
  \frac{f(m_e^2 / m_\tau^2)}{f(m_\mu^2 / m_\tau^2)}.
$$

## Proof sketch

The $T_{3,5}$ weak vertex acts as a **mediator** between the
parent tau $T_{2,7}$ and the daughter lepton $T_{2,n_\ell}$.
In the Hecke algebra $H_3(q)$, one may form the product
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
  \mathcal{M}(\tau \to \ell\,\bar\nu\,\nu_\tau)
  \;=\;
  \mathrm{tr}_{\mathrm{Markov}}(T_{3,5})
  \;\times\;
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

## Physical significance

Lepton universality — the statement that the weak interaction
couples equally to all lepton generations — is here a
**consequence** of the $T_{3,5}$ braid being the unique
cross-family mediator on the Bring surface
([fivefold symmetry](#rem:fivefold-symmetry)).  Its Markov trace
$\mathcal{W}(q) = \mathrm{tr}_{\mathrm{Markov}}((\sigma_0
\sigma_1)^5)$ is a property of the weak vertex alone, not of
the daughter channel.  Universality is broken only by kinematics
(the daughter mass entering through the phase-space integral),
not by the vertex.
