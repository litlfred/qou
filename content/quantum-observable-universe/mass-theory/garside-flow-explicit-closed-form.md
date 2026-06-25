The Garside trajectory $\sigma_1\sigma_2\sigma_1$ is the most
intricate of the six canonical operators
([six canonical knot operators](#prop:six-canonical-knot-operators);
[Garside as compound Reeb flow](#rem:garside-as-compound-flow)).
The user-flagged concern that "we will need to write PDEs and
hope we can find an exact solution" turns out to be unwarranted:
because the underlying flow is piecewise-linear in the angular
coordinate ([$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)),
the compound trajectory admits a closed-form solution by direct
composition.  This remark records that solution explicitly.

**Setup.**  Parameterise the latitude by $\phi \in [0, \pi]$ and
split into three equal sub-intervals
$I_1 = [0, \pi/3]$, $I_2 = [\pi/3, 2\pi/3]$, $I_3 = [2\pi/3, \pi]$.
The Garside word decomposes one generator per sub-interval:
$\sigma_1$ on $I_1$, $\sigma_2$ on $I_2$, $\sigma_1$ on $I_3$.
For each generator the active/spectator pattern on the colour
tubes $(r, g, b)$ is fixed:

| sub-interval | generator | $k^{(r)}$ | $k^{(g)}$ | $k^{(b)}$ |
|---|---|:-:|:-:|:-:|
| $I_1$ | $\sigma_1$ | $+1$ | $-1$ | $0$ |
| $I_2$ | $\sigma_2$ | $0$  | $+1$ | $-1$ |
| $I_3$ | $\sigma_1$ | $+1$ | $-1$ | $0$ |

**Closed-form trajectory.**  Let
$\psi^{(s)}_0$ denote the input angular position of sector $s$ at
the south foundry $\phi = 0$.  Applying the flow piecewise via
the additive composition rule of
[$q$-Reeb flow on color coords](#def:q-reeb-flow-on-color-coords)
yields the explicit closed form for the angular trajectory:

$$
  \psi^{(r)}(\phi) =
    \begin{cases}
      \psi^{(r)}_0 + q\phi & \phi \in I_1 \\
      \psi^{(r)}_0 + q\pi/3 & \phi \in I_2 \\
      \psi^{(r)}_0 + q\pi/3 + q(\phi - 2\pi/3) & \phi \in I_3
    \end{cases}
$$

$$
  \psi^{(g)}(\phi) =
    \begin{cases}
      \psi^{(g)}_0 - q\phi & \phi \in I_1 \\
      \psi^{(g)}_0 - q\pi/3 + q(\phi - \pi/3) & \phi \in I_2 \\
      \psi^{(g)}_0 - q(\phi - 2\pi/3) & \phi \in I_3
    \end{cases}
$$

The I$_{3}$ branch evaluates to the I$_{2}$ endpoint $\psi^{(g)}(2\pi/3) = \psi^{(g)}_0$
(green has cycled back to its starting position after the $\sigma_2$ sub-flow on $I_2$)
and then decreases at rate $-q$ on the second $\sigma_1$ sub-flow, giving
$\psi^{(g)}(\pi) = \psi^{(g)}_0 - q\pi/3$.

$$
  \psi^{(b)}(\phi) =
    \begin{cases}
      \psi^{(b)}_0 & \phi \in I_1 \\
      \psi^{(b)}_0 - q(\phi - \pi/3) & \phi \in I_2 \\
      \psi^{(b)}_0 - q\pi/3 & \phi \in I_3
    \end{cases}
$$

**North-foundry values ($\phi = \pi$).**  Evaluating at the
output boundary:

$$
\begin{aligned}
  \psi^{(r)}(\pi) &= \psi^{(r)}_0 + q\pi/3 + q\pi/3 = \psi^{(r)}_0 + 2q\pi/3, \\
  \psi^{(g)}(\pi) &= \psi^{(g)}_0 - q\pi/3 + q\pi/3 - q\pi/3 = \psi^{(g)}_0 - q\pi/3, \\
  \psi^{(b)}(\pi) &= \psi^{(b)}_0 - q\pi/3.
\end{aligned}
$$

The **net color-twist accumulated** by each sector across the
Garside trajectory is therefore
$\Delta\psi^{(r)} = +2q\pi/3$,
$\Delta\psi^{(g)} = -q\pi/3$,
$\Delta\psi^{(b)} = -q\pi/3$.
This pattern is **distinct** from the uniform vortex of the
3-cycle (all three sectors advance by the same $\pm 2q\pi/3$):
under Garside, the green sector is the displacement carrier
between the red and blue swap, picking up half the inverse twist
of red and an equal half from blue.

**Sector centre-of-mass check.**  The sum
$\Delta\psi^{(r)} + \Delta\psi^{(g)} + \Delta\psi^{(b)}
 = 2q\pi/3 - q\pi/3 - q\pi/3 = 0$,
The three-sector centre of mass is preserved across the
trajectory (no net global rotation).  This contrasts with the
3-cycle, whose centre of mass shifts by $\pm 2q\pi/3$ since all
three rates are equal-signed.  Centre-of-mass preservation is
the geometric signature of the **transposition class** of
$\sigma_1\sigma_2\sigma_1 = (rb)$ in $S_3$, as predicted by the
boundary-permutation table.

**Why this is not a PDE.**  The Reeb-flow trajectory lives on
the formal-algebraic side of the Archimedean wall.  The flow
equation $\dot\psi = k\,q$ is an ODE in the angular coordinate,
not a PDE — and within each sub-interval the rate $k$ is constant.
The "complicated PDE" the original concern envisioned was really
a *piecewise-affine ODE*, and its solution is the explicit
piecewise expressions above.  This is the same phenomenon as
[generating functions solve Reeb flow](#rem:generating-functions-solve-reeb-flow):
because the substrate dynamics live in the Habiro ring before any
archimedean realisation, the "solution" is a formal-algebraic
expression, not a transcendental analytic object.

**Consequence for the JSJ verdict.**  The Garside trajectory
crosses both Heegaard tori of $\mathcal{R}_p \cong S^3$ — once
at the $I_1 \to I_2$ boundary (red-green pair gives way to
green-blue pair) and once at the $I_2 \to I_3$ boundary
(green-blue pair gives way back to red-green pair) — so the
complement is not Seifert-fibered, in agreement with
[hyperbolic-knot positive volume via Reeb](#rem:hyperbolic-knot-positive-volume-via-reeb).
This is the dynamical-side derivation of the verdict that
the topological-side computation
([Thurston volume additivity](#prop:thurston-volume-additivity))
returns as positive Bloch-Wigner sum.
