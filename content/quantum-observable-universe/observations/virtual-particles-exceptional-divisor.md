In quantum field theory, virtual particles are internal lines in
Feynman diagrams: off-shell excitations that mediate forces and
contribute to loop corrections but are never directly detected.
Their "existence" is bounded by the Heisenberg uncertainty relation
$\Delta E \cdot \Delta t \gtrsim \hbar$.  The QOU framework provides
a geometric home for this phenomenon.

**The exceptional divisor as the virtual stage.**

At each brane point $p \in M$, the blow-up replaces $p$ with an
[exceptional divisor](#def:exceptional-divisor)
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$.  This sphere
parametrises the *directions* of departure from the base manifold —
the internal degrees of freedom invisible to the base-level observer.

A virtual particle is an excitation that lives **within** the Reeb
bundle over $\mathcal{S}_p$ --- the Hopf fibration
$U(1) \hookrightarrow S^3 \to \mathcal{S}_p$ where all braiding takes place
([vertex is the exceptional divisor](#prop:vertex-is-exceptional-divisor)).
It is created at the blow-up locus, propagates along the
exceptional divisor (or up into the
[brane tower](#def:recursive-brane-tower) rooted at $\mathcal{S}_p$), and is
reabsorbed before it can descend to the base level $A_0$.

**Brane tower levels as virtual depth.**

The [recursive brane tower](#def:recursive-brane-tower)
$A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$
stratifies excitations by their [jet prolongation](#prop:jet-prolongation)
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

**Non-observability of virtual particles.**

An excitation at level $A_n$ ($n \geq 1$) is invisible at $A_0$
because the canonical projection $\pi_0 \colon A_n \to A_0$
annihilates the $\Omega^1$ components:

$$
  \pi_0(f \otimes \omega_1 \otimes \cdots \otimes \omega_n)
  = 
  f \cdot \varepsilon(\omega_1) \cdots \varepsilon(\omega_n),
$$

where $\varepsilon$ is the counit.  For a form $\omega$ with no
constant part ($\varepsilon(\omega) = 0$), the entire excitation
projects to zero at the base level.  The virtual particle exists
in the tower but casts no shadow on $A_0$.

This is the categorical analogue of the statement that virtual
particles are "off-shell": they satisfy the equations of motion
at their tower level but not at the base level.  The base-level
observer sees only the *net effect* --- a correction to the
propagator, an effective force, a shift in energy levels --- never
the virtual excitation itself.

**Lifetime from the Heisenberg commutator.**

The [Heisenberg commutator](#rem:heisenberg-commutator) at level
$n$ of the tower is

$$
  [\hat{X}, \hat{P}]_{q_n} =  J\hbar_{q_n}, \qquad
  \hbar_{q_n} =  1 - q_n^{-1},
$$

where $q_n$ is the substrate parameter at the $n$-th level.  The
uncertainty bound $\Delta E \cdot \Delta t \geq \hbar_{q_n} / 2$
limits the lifetime of a virtual excitation at level $n$:

$$
  \Delta t_{\text{virtual}}
   \leq 
  \frac{\hbar_{q_n}}{2\Delta E}.
$$

For an excitation that borrows energy $\Delta E$ from the vacuum
at the exceptional divisor, this is the maximum time before the
excitation must be reabsorbed.  The excitation's
"worldline" stays within the tower: it is created at $\mathcal{S}_p$,
propagates through $A_1, A_2, \ldots$, and returns to $\mathcal{S}_p$
without ever descending to $A_0$.
