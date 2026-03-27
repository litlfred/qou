The **$\mathcal{Q}$-value** of a nuclear transition is the
total energy released, distributed among ALL products —
including the recoiling nucleus.

**Definition (physical).**
For a beta decay $\mathcal{N}_{\mathrm{par}} \to \mathcal{N}_{\mathrm{dau}}
+ e + \bar{\nu}$, the $\mathcal{Q}$-value is the sum of the
kinetic energies of ALL products:

$$
  \mathcal{Q}
  \;=\;
  T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}}
$$

where $T_e$ is the electron kinetic energy, $T_{\bar{\nu}}$ is
the antineutrino kinetic energy, and $T_{\mathrm{recoil}}$ is
the kinetic energy of the recoiling daughter nucleus.

**No approximations.**  Standard references often neglect
$T_{\mathrm{recoil}}$ because $T_{\mathrm{recoil}} \sim
\mathcal{Q}^2 / (2 M_{\mathrm{dau}} c^2) \ll \mathcal{Q}$.
We do NOT make this approximation.  All three kinetic energies
are retained.

**Definition (categorical, from crossings).**
In the Descartes framework, $\mathcal{Q}$ is the net change
in crossing energy when the Skein crossing change
$\sigma_k \to \sigma_k^{-1}$ converts one quark flavour:

$$
  \mathcal{Q}
  \;=\;
  E_q(\mathcal{N}_{\mathrm{par}})
  \;-\;
  E_q(\mathcal{N}_{\mathrm{dau}})
  \;-\;
  E_q(e)
  \;-\;
  E_q(\bar{\nu})
$$

where $E_q$ is the total $q$-energy
([q-energy](#def:q-energy)).

Equivalently, $\mathcal{Q}$ is the difference in categorical
actions minus the rest masses of the emitted leptons:

$$
  \mathcal{Q}
  \;=\;
  \bigl[S_q(\mathcal{N}_{\mathrm{par}}) - S_q(\mathcal{N}_{\mathrm{dau}})\bigr]
  \;-\; m_e c^2 - m_{\bar{\nu}} c^2
$$

Since $m_{\bar{\nu}} \approx 0$ (unknot, $\mathrm{Vol} = 0$):

$$
  \mathcal{Q}
  \;=\;
  \Delta S_q - m_e c^2
$$

**Proposition: physical = categorical $\mathcal{Q}$.**

*The kinetic energy sum $T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}}$
equals the crossing energy difference $\Delta S_q - m_e c^2$.*

*Proof.*
Energy conservation in the rest frame of the parent nucleus:

$$
  M_{\mathrm{par}} c^2
  \;=\;
  (M_{\mathrm{dau}} c^2 + T_{\mathrm{recoil}})
  + (m_e c^2 + T_e)
  + (m_{\bar{\nu}} c^2 + T_{\bar{\nu}})
$$

Rearranging:

$$
  T_e + T_{\bar{\nu}} + T_{\mathrm{recoil}}
  \;=\;
  M_{\mathrm{par}} c^2 - M_{\mathrm{dau}} c^2 - m_e c^2
  - m_{\bar{\nu}} c^2
$$

In the categorical framework, $M c^2 = S_q(\mathcal{N})$
(the categorical action IS the rest mass energy,
[q-energy at rest](#def:q-energy)).  Therefore:

$$
  \mathcal{Q}
  \;=\;
  S_q(\mathrm{par}) - S_q(\mathrm{dau}) - S_q(e) - S_q(\bar{\nu})
  \;=\;
  \Delta S_q - m_e c^2 - 0
$$

$\square$

**Crossing-level decomposition.**

The action difference $\Delta S_q$ decomposes into individual
crossing contributions.  Let $\beta_{\mathrm{par}}$ and
$\beta_{\mathrm{dau}}$ be the Gröbner normal form braid words.
They differ at exactly $|\delta p|$ crossings (the converting
nucleon's quarks).  At each changed crossing:

$$
  \Delta E_\times
  \;=\;
  E_\times^{(\epsilon_{\mathrm{par}})}(q)
  - E_\times^{(\epsilon_{\mathrm{dau}})}(q)
$$

For a $d \to u$ crossing change ($\sigma_k^{-1} \to \sigma_k$):
$\Delta E_\times = q - q^{-1} = 0.209$ (in units of $\mu_0$).

The total:

$$
  \mathcal{Q}
  \;=\;
  \sum_{\text{changed crossings}} \Delta E_\times
  \;-\; m_e c^2
$$

**Momentum conservation.**

The three-body kinematics distribute $\mathcal{Q}$ among the
products.  By $q$-momentum conservation:

$$
  p_q(\mathrm{par})
  \;=\;
  p_q(\mathrm{dau}) + p_q(e) + p_q(\bar{\nu})
$$

The electron and antineutrino share the available momentum
continuously (beta spectrum).  The recoil momentum of the
daughter is:

$$
  p_q(\mathrm{recoil})
  \;=\;
  -(p_q(e) + p_q(\bar{\nu}))
$$

and the recoil kinetic energy:

$$
  T_{\mathrm{recoil}}
  \;=\;
  \frac{(p_q(e) + p_q(\bar{\nu}))^2 \cdot \hbar_q}{2 \, [3A_{\mathrm{dau}}]_q}
$$

using the $q$-deformed kinetic energy formula with
$[3A]_q$ strands (quarks in the daughter).

**$\mathcal{Q}$-value as a function of $q$.**

| $q$ | Regime | $\mathcal{Q}$ |
|-----|--------|---------------|
| $q = 1$ | Classical (heat death) | $0$ (no crossing asymmetry) |
| $q = 1.110$ | Our universe | $\mathcal{Q}_{\exp}$ |
| $q \to \infty$ | Big bang | $\to \infty$ (all crossings maximally asymmetric) |

The $\mathcal{Q}$-value interpolates between zero (no weak
decay in the classical limit) and infinity (instantaneous
decay at the big bang), controlled entirely by $q$.
