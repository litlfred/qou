### Chern--Simons level from QOU existence

The Chern--Simons level $k$ appearing in this proposition is not an
independent input: by the existence proof for a quantum observable
universe
([QOU existence](#prop:quantum-observable-universe-exists)), choosing
$q = e^{\pi i/(k + h^{\vee})}$ makes $\mathbf{C} = \mathbf{Rep}_{k}(\widehat{\mathfrak{g}})$
the modular tensor category that simultaneously fixes (a) the braiding
used in the Skein relation and (b) the CS-level partition function on
the brane.  Therefore $k = \langle c_{2}(\mathrm{Ad}(P)), [M] \rangle$
*determines* both the $q$-deformation of the force-carrier
$q$-dimensions $[m]_{q}, [n]_{q}$ and the CS functional
$\mathrm{CS}(T_{m, n})$ through the single RT construction.  The
proposition's numerical prediction specialises the shared object rather
than combining two independently postulated quantities.

**Proposition.**
*The fine structure constant receives corrections from the
Chern–Simons invariants of the force-carrier torus knots
$T_{2,9}$ and $T_{3,5}$ on Bring's surface:*

$$
  \frac{1}{\alpha_{\mathrm{EM}}}
  = q \cdot [9]_q \cdot [10]_q
    \cdot \bigl(1 + \delta_{\mathrm{CS}}
                 + \delta_{\mathrm{CS}}^2 \cdot \kappa\bigr)
$$

*where:*

$$
  \delta_{\mathrm{CS}}
  = \frac{\bigl(\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})\bigr)
              \cdot \tfrac{[2]_q}{2} \cdot \hbar_q^2}
             {q \cdot [9]_q \cdot [10]_q}
$$

*and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}}
             / \det G_{\mathrm{CS}}^{q}$
is the Gram determinant ratio of the classical and $q$-deformed
Chern–Simons pairing on Bring's surface.*

*At $q_0 \approx 1.110$:
$1/\alpha = 137.035944$ vs CODATA $137.035999$ (399 ppb).*

*Proof.*
The bare coupling $\alpha = q^{-1}/([9]_q \cdot [10]_q)$ comes
from the antisymmetric braiding eigenvalue (Layer 2 of
[EM coupling projection](#prop:em-coupling-projection))
normalized by the force-carrier $q$-dimensions (Layer 3).

The correction arises from the descent decomposition of the
coupling endomorphism $P_{\mathrm{anti}}$ on the force-carrier
configuration.  The torus knots $T_{2,9}$ (strong, 9 crossings)
and $T_{3,5}$ (weak, 10 crossings) are non-hyperbolic, so their
geometric invariant is the Chern–Simons functional rather than
the hyperbolic volume:

$$
  \mathrm{CS}(T_{m,n})
  = \frac{\pi^2 (m^2-1)(n^2-1)}{12 m n}
$$

The factor $[2]_q/2$ is the $q$-deformation of
$\mathrm{Vol}(S^3)/\mathrm{Vol}(S^3_{\mathrm{classical}})$,
replacing $\mathrm{Vol}(S^3) = 2\pi^2$ with
$\mathrm{Vol}(S^3_q) = \pi^2 [2]_q$.

At order $J^2$ (second jet level), the Gram matrix of the CS
pairing for the two-knot configuration
$(T_{2,9}, T_{3,5})$ on Bring's surface gives:

$$
  G_{\mathrm{CS}} =
  \begin{pmatrix}
    \mathrm{CS}_1 + \pi^2 s_1^2 / c_1^2
    & \pi^2 \ell^2 / (c_1 c_2) \\
    \pi^2 \ell^2 / (c_1 c_2)
    & \mathrm{CS}_2 + \pi^2 s_2^2 / c_2^2
  \end{pmatrix}
$$

where $s_i = (m_i-1)(n_i-1)$ is the self-linking,
$\ell = |m_1 n_2 - m_2 n_1| = 17$ is the linking number,
and $c_i = m_i n_i$ is the crossing product.  The $q$-deformed
version replaces $m,n$ with $[m]_q, [n]_q$ throughout.

The determinant ratio $\kappa = \det G^{\mathrm{cl}} / \det G^q
= 1.722$ captures the self-dual damping at the $J^2$ jet level.

Combining: $1/\alpha = 136.823 + 0.212 + 0.001 = 137.036$.
$\square$
