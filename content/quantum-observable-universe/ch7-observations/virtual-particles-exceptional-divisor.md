In quantum field theory, virtual particles are internal lines in
Feynman diagrams: off-shell excitations that mediate forces and
contribute to loop corrections but are never directly detected.
Their "existence" is bounded by the Heisenberg uncertainty relation
$\Delta E \cdot \Delta t \gtrsim \hbar$.  The QOU framework provides
a geometric home for this phenomenon.

**The exceptional divisor as the virtual stage.**

At each brane point $p \in M$, the blow-up replaces $p$ with an
[exceptional divisor](#def:exceptional-divisor)
$E_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$.  This sphere
parametrises the *directions* of departure from the base manifold —
the internal degrees of freedom invisible to the base-level observer.

A virtual particle is an excitation that lives **within** $E_p$:
it is created at the blow-up locus, propagates along the
exceptional divisor (or up into the
[brane tower](#def:recursive-brane-tower) rooted at $E_p$), and is
reabsorbed before it can descend to the base level $A_0$.

**Brane tower levels as virtual depth.**

The [recursive brane tower](#def:recursive-brane-tower)
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
stratifies excitations by their [jet prolongation](#def:jet-prolongation)
level.  Physical (on-shell) particles live at level $A_0$ — they are
knot configurations in the base algebra.  Virtual particles live at
levels $A_n$ with $n \geq 1$:

| Tower level | Algebra | Physical interpretation |
|-------------|---------|----------------------|
| $A_0 = A$ | Coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ | On-shell particles: knots in base manifold |
| $A_1 = J^1(A_0)$ | Sections of frame bundle | 1-virtual: connection fluctuations (gauge bosons) |
| $A_2 = J^1(A_1)$ | Second jet sections | 2-virtual: curvature fluctuations (graviton-like) |
| $A_n$ | $n$-th jet sections | $n$-virtual: $n$-th derivative corrections |

Each level $A_n$ has dimension $3^n \cdot \dim A_0$ (for
$\mathrm{SU}(2)$), so the state space grows exponentially with
virtual depth — but the projection back to $A_0$ collapses all
higher-level structure.

**Why virtual particles are never observed.**

An excitation at level $A_n$ ($n \geq 1$) is invisible at $A_0$
because the canonical projection $\pi_0 \colon A_n \to A_0$
annihilates the $\Omega^1$ components:

$$
  \pi_0(f \otimes \omega_1 \otimes \cdots \otimes \omega_n)
  \;=\;
  f \cdot \varepsilon(\omega_1) \cdots \varepsilon(\omega_n),
$$

where $\varepsilon$ is the counit.  For a form $\omega$ with no
constant part ($\varepsilon(\omega) = 0$), the entire excitation
projects to zero at the base level.  The virtual particle exists
in the tower but casts no shadow on $A_0$.

This is the categorical analogue of the statement that virtual
particles are "off-shell": they satisfy the equations of motion
at their tower level but not at the base level.  The base-level
observer sees only the *net effect* — a correction to the
propagator, an effective force, a shift in energy levels — never
the virtual excitation itself.

**Lifetime from the Heisenberg commutator.**

The [Heisenberg commutator](#rem:heisenberg-commutator) at level
$n$ of the tower is

$$
  [\hat{X}, \hat{P}]_{q_n} \;=\; J\,\hbar_{q_n}, \qquad
  \hbar_{q_n} \;=\; 1 - q_n^{-1},
$$

where $q_n$ is the substrate parameter at the $n$-th level.  The
uncertainty bound $\Delta E \cdot \Delta t \geq \hbar_{q_n} / 2$
limits the lifetime of a virtual excitation at level $n$:

$$
  \Delta t_{\text{virtual}}
  \;\leq\;
  \frac{\hbar_{q_n}}{2\,\Delta E}.
$$

For an excitation that borrows energy $\Delta E$ from the vacuum
at the exceptional divisor, this is the maximum time before the
excitation must be reabsorbed.  Crucially, the excitation's
"worldline" stays within the tower: it is created at $E_p$,
propagates through $A_1, A_2, \ldots$, and returns to $E_p$
without ever descending to $A_0$.

**Virtual pairs at the exceptional divisor.**

The [pair creation energy](#rem:pair-creation-energy) analysis
showed that a photon with $E \geq 2m_e$ can create a real $e^-e^+$
pair at the exceptional divisor.  But what about photons with
$E < 2m_e$?  These can create a **virtual** pair — a trefoil and
its mirror that exist within $E_p$ for time
$\Delta t \leq \hbar_q / (2m_e - E)$ before annihilating back.

This is the QOU description of **vacuum polarisation**: the photon
briefly resolves into a virtual $e^-e^+$ pair within the exceptional
divisor, modifying the effective coupling constant.  The pair never
reaches $A_0$ — it lives and dies in the blow-up geometry.

**Virtual exchange as Skein resolution.**

In the [Reidemeister mass invariance](#rem:reidemeister-mass-invariance)
framework, a virtual pair corresponds to an R-II move: two crossings
of opposite sign are temporarily introduced and then removed.  The
Skein resolution of this pair produces a correction term
$(q - q^{-1}) \cdot L_0$ that modifies the crossing energy without
changing the knot type.  This is precisely a virtual exchange: the
topology is unchanged, but the energy receives a perturbative
correction from the transient crossing pair.

**Summary.**

| QFT concept | QOU realisation |
|-------------|----------------|
| On-shell particle | Knot configuration at level $A_0$ |
| Virtual particle | Excitation at level $A_n$ ($n \geq 1$) in brane tower |
| Propagator | Projection $A_n \to A_0$ (collapses virtual structure) |
| Vacuum polarisation | Virtual pair within exceptional divisor $E_p$ |
| Loop correction | Skein resolution of transient R-II crossing pair |
| Off-shell lifetime | Bounded by $\hbar_{q_n} / (2\Delta E)$ at tower level $n$ |

Virtual particles are not ghostly approximations — they are genuine
excitations of the brane tower that happen to be invisible at the
base level.  Their home is the exceptional divisor and the tower
growing from it.  They "help out" (mediate forces, correct energies,
polarise the vacuum) but are never seen because their worldlines
never descend to $A_0$.
