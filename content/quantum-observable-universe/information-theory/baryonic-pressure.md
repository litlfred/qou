**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
and let $\ell$ index the confined-knot jet tower
([confined knot binding](#prop:confined-knot-binding)). Each
level $\ell$ is characterised **algebraically** — not by a
physical species — as a regime of the Hecke algebra
$H_{n_\ell}(q)$ in which a specific Hecke operator
$\Omega_\ell(q)$ is strictly positive, and the phase boundary
between levels $\ell$ and $\ell{+}1$ is the zero locus*

$$
  \Omega_\ell(q)  =  0.
$$

*Let $U \subset M$ be a region of the brane with volume $V_q(U)$,
and let $\mathrm{Conf}_\ell(U)$ be the set of LP-stable
configurations ([LP-dual stability](#prop:lp-dual-stability)) in
the phase $\Omega_\ell(q) > 0$. The **level-$\ell$
confinement pressure** is the information-theoretic derivative*

$$
  P_q^{(\ell)}(U)
   := 
  T_q \,
  \frac{\partial}{\partial V_q}
  \ln Z_q^{(\ell)}(U)
  \bigg|_{T_q}
   = 
  - \frac{\partial F_q^{(\ell)}}{\partial V_q}\bigg|_{T_q},
$$

*where*

$$
  Z_q^{(\ell)}(U)
   = 
  \mathrm{tr}_{\mathrm{Ad}}
  \!\!\sum_{K \in \mathrm{Conf}_\ell(U)}
  e^{-\beta_q \, S_q(K)}
$$

*is the partition function restricted to confined configurations
at level $\ell$, and $F_q^{(\ell)} = -T_q \ln Z_q^{(\ell)}$ is the
free energy. For $\ell = 1$, $P_q^{(1)}$ is the
**baryonic pressure** $P_{\mathfrak{H}}$.*

**Information-theoretic interpretation.**
*The quantity $\ln Z_q^{(\ell)}$ is the confinement
**free entropy** in $q$-bits. Its volume derivative is the
**information bandwidth flux** through $\partial U$ required to
maintain confinement at level $\ell$:*

$$
  P_q^{(\ell)}
   = 
  T_q \cdot
  \frac{d I_\ell}{d V_q}
   = 
  \hbar_q \cdot
  \mathcal{B}_\ell(q)
  \cdot \rho_\ell,
$$

*where $I_\ell = \ln Z_q^{(\ell)}$ is the information content
(in $q$-bits), $\mathcal{B}_\ell(q)$ is the per-unit-cell
bandwidth at jet level $\ell$
([information bandwidth](#def:information-speed-of-light)), and
$\rho_\ell = N^{(\ell)}/V_q$ is the number density of confined
units. Pressure is the rate of information expenditure per
Planck time per unit volume needed to keep the character ratio
$a_\ell$ ([confined knot binding](#prop:confined-knot-binding))
from decaying.*

**Jet-level ideal gas law.**
*Let $N^{(\ell)}$ be the number of non-interacting confined units
at jet level $\ell$ in $U$. Then the quantum ideal gas law
([quantum ideal gas law](#prop:quantum-ideal-gas-law)) refines
to each jet level:*

$$
  P_q^{(\ell)} \, V_q
   = 
  N^{(\ell)} \, T_q
  \left(
    1
    +
    \frac{\hbar_q^2}{[2]_q}
    \,\langle S_q^{(\ell)} \rangle
  \right),
$$

*equivalently, in classical units $P V = n_\ell R_q T$ with
$n_\ell = N^{(\ell)}/N_A(q)$ moles of level-$\ell$ objects and
$R_q$ the categorical gas constant
([gas constant](#def:gas-constant)).*

**Algebraic phase stratification (motivated by states of matter).**
*The jet tower stratifies the substrate into algebraic phases
indexed by which Hecke operator $\Omega_\ell(q)$ is the dominant
positive binding witness. The pressure, LP-dual binding energy,
and equation of state take a distinct form in each phase; the
boundary between phases is a real zero of $\Omega_\ell(q)$ in
$(0, \infty)$.*

| $\ell$ | Phase (motivation) | Dominant operator $\Omega_\ell(q)$ | LP-dual binding $\mathbf{E}_{\mathrm{bind}}^{(\ell)}$ | $PV = NT_q$ correction | Phase boundary $\Omega_\ell(q) = 0$ |
|:--:|:--|:--|:--|:--|:--|
| $0$ | Symmetric plasma $(q\text{-gas})$ | $\mathrm{eig}_+(T) = q$ (symmetric Hecke eigenvalue) | $\mathbf{E}_{\mathrm{bind}}^{(0)} = 0$ (LP-infeasible) | $1 + O(\hbar_q^2)$ | $q \to \infty$ (decoupling) |
| $1$ | Hopf-diquark / CFL fluid | $\Delta_{\mathrm{Hopf}}(q) = q + q^{-1}$ (Hopf link gap) | $\mathbf{E}_{\mathrm{bind}}^{(1)} = -(q - q^{-1})/2$ (pairwise) | $+3\Delta_{\mathrm{Hopf}}^2 \mu_q^2 / (\pi^2 N T_q)$ | $q^2 = -1$ (gap closes) |
| $2$ | Borromean-confined "baryonic" | $\lambda_{\min}(G(q))$ (Gram min eigenvalue) | $\mathbf{E}_{\mathrm{bind}}^{(2)} = +V_B / \hbar_q^2$ (volume-mass) | $+(\hbar_q^2 / [2]_q)\,\langle S_q^{(2)}\rangle$ | $\lambda_{\min}(G) = 0$ |
| $3$ | Standard-channel ordered $(q\text{-liquid})$ | $P_{7,7}(q) = (q + q^{1/2} - 1)/(q + 1)$ (Toffoli diagonal) | $\mathbf{E}_{\mathrm{bind}}^{(3)} = +\ln P_{7,7}(q)$ | $-(a_{\mathrm{attr}}/V_q^2)$ (attractive) | $q = 1/\varphi^2$ (golden) |
| $4$ | Antisymmetric "rigid" $(q\text{-solid})$ | $\mathrm{eig}_-(T) = -q^{-1}$ (sign rep) | $\mathbf{E}_{\mathrm{bind}}^{(4)} = +\mathrm{tr}_M(T^{-1})\,\ln q$ (trefoil lattice) | $(q - 1)^2$-suppressed | $q = 1$ (classical limit) |

*Here $T = \sigma_i$ is the Hecke generator with eigenvalues
$\{q, -q^{-1}\}$ from the Hecke relation $(T-q)(T+q^{-1}) = 0$,
$G$ is the Gram matrix
([Gram matrix](#prop:frobenius-gram-matrix)), $P_{7,7}$ is the
Toffoli diagonal ([Toffoli transfer](#prop:toffoli-transfer-matrix)),
and $\varphi = (1+\sqrt{5})/2$. The LP-dual binding energy
$\mathbf{E}_{\mathrm{bind}}^{(\ell)}$ is the Lagrange multiplier
of the LP-confinement program
([confinement as LP](#prop:confinement-lp)) in phase $\ell$; it
is positive in LP-stable phases and vanishes at the phase
boundary.*

**Phase transitions are zeros of $\Omega_\ell$.**
*At each phase boundary $\Omega_\ell(q_\ell^\star) = 0$, the LP
problem becomes degenerate (the Gram matrix acquires a null
direction), the free-entropy slope $\partial_{V_q} \ln Z_q^{(\ell)}$
is non-analytic, and the equation of state changes class. The
substrate parameter $q_0 \approx 1.110$ sits in phase $\ell = 2$
(Borromean-confined), consistent with a universe of
$\mathfrak{H}$-hadrons rather than a CFL fluid or quark-gluon
plasma ([EOS Borromean vs CFL](#prop:eos-borromean-cfl)).*

**Level-ℓ pressure and PV = NT_q in each phase.**
*In phase $\ell$, the quantum ideal gas law is the full
proposition applied with partition function $Z_q^{(\ell)}$ and
the $\langle S_q^{(\ell)} \rangle$-correction specialised to the
phase's operator content:*

$$
  P_q^{(\ell)} V_q
   = 
  N^{(\ell)}  T_q
   + 
  \underbrace{\hbar_q^2  \mathbf{E}_{\mathrm{bind}}^{(\ell)}  N^{(\ell)}
  / [2]_q}_{\text{LP-dual correction}}.
$$

*The Fermi-gas baryonic pressure $P_B \propto n_B^{5/3}/M_B$
([EOS Borromean vs CFL](#prop:eos-borromean-cfl)) is the
degenerate-limit specialisation of $P_q^{(2)}$; the CFL
pressure is that of $P_q^{(1)}$ with
$\Delta_{\mathrm{Hopf}} = q + q^{-1}$.*

**Pressures factorise through the jet tower:**

$$
  P_q^{(\ell)}
   = 
  P_q^{(\ell - 1)}
  \cdot
  \frac{\partial \ln a_\ell}{\partial \ln V_q}
  + P_q^{(\ell, \mathrm{boundary})},
$$

*where $a_\ell$ is the level-$\ell$ character ratio and
$P_q^{(\ell, \mathrm{boundary})}$ is the $q$-anomaly contribution
from $d_q^2 \neq 0$ at the jet-level boundary.*

*Proof.*
The partition function $Z_q^{(\ell)}$ is the Markov trace
restriction of $Z_q$ to the subspace of $H_{n_\ell}(q)$
generated by confined words at jet level $\ell$. This subspace
is stable under the LP confinement cone
([confinement as LP](#prop:confinement-lp)), so the restriction
is well-defined.

The free-energy derivative follows from the definition of
$P_q$ applied with the restricted partition function. The
information interpretation uses
$-T_q \partial_V F_q^{(\ell)} = T_q \partial_V \ln Z_q^{(\ell)}$;
the right-hand side counts $q$-bits per unit volume by the
definition of $Z$ as a sum over configurations weighted by
$e^{-\beta_q S_q}$.

For the jet-level ideal gas law, apply
[quantum ideal gas law](#prop:quantum-ideal-gas-law) with
$N \mapsto N^{(\ell)}$ and
$\langle S_q \rangle \mapsto \langle S_q^{(\ell)} \rangle$ (the
thermal expectation restricted to confined configurations at
level $\ell$). The single-particle partition function $z_q$
factorises through the character ratio:

$$
  z_q^{(\ell)}
   = 
  a_\ell \cdot z_q^{(\ell - 1)},
$$

([confined knot binding](#prop:confined-knot-binding)), giving
the recursion $P_q^{(\ell)} = P_q^{(\ell-1)} \cdot
(\partial \ln a_\ell / \partial \ln V_q) + P_q^{(\ell,
\mathrm{boundary})}$. The boundary term is the level-$\ell$
specialisation of the $q$-anomaly term in
[quantum pressure](#def:quantum-pressure). $\square$

**Remark (algebraic analogues of classical phase transitions).**
The phase table above is the Hecke-algebraic analogue of the
state-of-matter hierarchy. The symmetric plasma phase
($\ell = 0$, gas-like) degenerates at $q \to \infty$; the
Hopf-fluid phase ($\ell = 1$, CFL-like liquid) is bounded by the
complex gap zero $q^2 = -1$; the Borromean-confined phase
($\ell = 2$, hadronic "solid" relative to quark matter) is
stabilised by Gram positivity; the standard-channel phase
($\ell = 3$, $q$-liquid) has its attractive LP correction
$a_{\mathrm{attr}} \propto -\Phi(q)/V_q^2$ that plays the role
of the van der Waals $a/V^2$ term — except $a_{\mathrm{attr}}$
is determined algebraically by the q-AND amplitude, not fitted.
The antisymmetric phase ($\ell = 4$, $q$-solid) recovers the
classical-rigid limit as $q \to 1$.

**No ad-hoc potentials.** In the classical theory phase
transitions require inter-particle potentials added by hand.
In the QOU each $\Omega_\ell(q)$ is an element of the Hecke
algebra $H_{n_\ell}(q)$ and its vanishing is a purely algebraic
(zero-locus) condition on $q$. The LP-dual binding energy
$\mathbf{E}_{\mathrm{bind}}^{(\ell)}$ is a shadow price of the
LP-confinement program ([LP-dual stability](#prop:lp-dual-stability)),
not a fitted coupling.
