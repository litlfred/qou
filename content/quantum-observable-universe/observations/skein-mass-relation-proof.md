The electron is identified with the trefoil $3_1$, a torus knot with
$\mathrm{Vol}_q(\beta_{3_1}) = 0$ in $\mathbb{Z}[q^{\pm 1/2}]$
(see [algebraic quantum volume](#def:algebraic-quantum-volume)),
sitting at the base of the topological tower as the unit against
which all other masses are measured.  The Higgs field is identified
with the figure-eight knot $4_1$
([cohomological embedding](#prop:cohomological-embedding)), whose
algebraic quantum volume $\mathrm{Vol}_q(\beta_{4_1})$ τ-realises
to the hyperbolic-volume constant
$\mathrm{Vol}(4_1) \approx :val[Vol_4_1]{precision=6}$.

Applying the **algebraic** topological mass formula
([algebraic topological mass](#prop:topological-mass-formula-algebraic))
to the muon–electron *ratio* eliminates the overall mass scale and
gives $m_\mu / m_e = \Phi_1(4_1) / \hbar_q^{2}$ at the
$\mathbb{Q}(q)$ level, where
$\Phi_1(4_1) = \tau_{\mathrm{arch}}(\mathrm{Vol}_q(4_1))$ is the
$\tau_{\mathrm{arch}}$-image of the algebraic quantum volume
([`def:algebraic-quantum-volume`](#def:algebraic-quantum-volume)).
Under $\tau_{\mathrm{arch}}$ the value $\Phi_1(4_1)$ specialises
to the numerical hyperbolic volume $\mathrm{Vol}(4_1)$ via the
volume conjecture \cite{kashaev1997, murakami-murakami2001} —
**τ-side naming** of the algebraic value, not a derivation
input. Substituting $\hbar_q = 1 - q^{-1}$ and the CODATA value
$m_\mu / m_e \approx 206.7682827(46)$ yields

$$
  \hbar_q^{2}
  = \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  = \frac{:val[Vol_4_1]{precision=6}}{:val[m_mu_over_e]{precision=7}}
  \approx :val[hbar_q_sq]{precision=4},
  \qquad
  \hbar_q \approx :val[hbar_q]{precision=4},
$$

so $1/q = 1 - :val[hbar_q]{precision=4} = :val[q_inv]{precision=4}$ and $q \approx :val[q_0]{precision=6}$.

The Skein relation itself is the mass-functional analogue of the Kauffman
bracket recursion.  At each crossing in the color-exchange diagram of a
hadron, the three resolutions $L_+$, $L_-$, $L_0$ satisfy
$q\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2}-q^{-1/2})\mathcal{M}(L_0)$.
This relation is inherited from the $q$-deformed $\mathrm{SU}(2)$
Chern--Simons functional on the $1$-jet bundle prolongation of the CR
manifold (see [Chapter](#chap:path-integrals-braiding)).  $\square$
