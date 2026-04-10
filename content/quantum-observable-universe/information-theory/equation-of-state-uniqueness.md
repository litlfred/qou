**Proposition (equation of state uniqueness).**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$.  Let
$d_1 = \dim_k HH^1(\mathcal{U}_q, \mathrm{Ad})$ be the
dimension of the outer derivation space.  Then:*

**(a)** *The space of independent first-order deformations of
the partition function $Z_q$ is $d_1$-dimensional.  Each
independent deformation direction generates an independent
equation of state via $F_q = -T_q \ln Z_q$.*

**(b)** *For a QOU with $G = \mathrm{SU}(2)$, $d_1 = 1$
([obstruction reduction](#thm:qou-obstruction-reduction)),
so there is exactly one independent equation of state:*

$$
  \dim\bigl(\text{independent equations of state}\bigr)
  \;=\;
  \dim HH^1(\mathcal{U}_q, \mathrm{Ad})
  \;=\; 1.
$$

*The quantum ideal gas law
$P_q V_q = N T_q (1 + \hbar_q^2 \langle S_q \rangle / [2]_q)$
([ideal gas law](#prop:quantum-ideal-gas-law)) is the unique
such relation.*

*Proof of (a).*
The partition function $Z_q$ depends on the Frobenius--Hopf
algebra $A_q$, which varies over the deformation space
$\mathrm{Def}(A) \subset HH^1(\mathcal{U}_q, \mathrm{Ad})$.
A first-order deformation $\phi \in HH^1$ changes the algebra
$A_q \mapsto A_q + \epsilon \, \phi$, which changes the
single-particle partition function
$z_q \mapsto z_q + \epsilon \, \partial_\phi z_q$, which
changes the free energy
$F_q \mapsto F_q + \epsilon \, \partial_\phi F_q$, which
produces a new thermodynamic identity
$\partial_\phi(P_q V_q - N T_q(\cdots)) = 0$.

Two deformation directions $\phi_1, \phi_2 \in HH^1$ produce
independent equations of state iff $\phi_1$ and $\phi_2$ are
linearly independent in $HH^1$ --- i.e., they deform the
algebra in genuinely different ways.  The number of such
independent directions is $\dim HH^1$.  $\square$

*Proof of (b).*
By the obstruction reduction theorem
([reduction theorem](#thm:qou-obstruction-reduction)):
$\dim HH^1(\mathcal{U}_q, \mathrm{Ad}) = 1$ for a QOU with
$G = \mathrm{SU}(2)$.  The unique deformation direction is
$q$ itself --- the Drinfeld--Jimbo parameter.  Every
thermodynamic quantity ($P_q$, $V_q$, $T_q$, $S_q$, $F_q$)
is a function of $q$ alone (and $N$, $|U|$).  The partition
function has one parameter; the equation of state is one
relation.  $\square$

**What uniqueness means.**

The ideal gas law is not one equation among many --- it is
the **only** polynomial relation extractable from the
partition function at degree $0$.  All other thermodynamic
identities (Clausius--Clapeyron, Maxwell relations, Gibbs--Duhem)
are **derived** from it via Legendre transforms and partial
derivatives.  They are not independent: they carry no
information beyond the single equation of state.

Concretely, the thermodynamic identities form a one-dimensional
vector space:

$$
  \mathrm{span}\bigl\{
    P_q V_q - N T_q(1 + \cdots)
  \bigr\}
  \;\cong\; HH^1(\mathrm{Ad})
  \;\cong\; k.
$$

Any "new" equation of state would require a second deformation
parameter independent of $q$ --- a second direction in $HH^1$.
The obstruction reduction theorem forbids this.

**Contrast with a general quantum universe.**

A general QU with $\dim HH^1 = d_1 > 1$ could support $d_1$
independent equations of state --- $d_1$ macroscopic laws
that cannot be derived from each other.  Each would correspond
to a separate deformation parameter of the Frobenius algebra.
The QOU axiom (observability) is what collapses this to $d_1 = 1$:
by killing $HH^0$ (no hidden symmetries), Frobenius--Poincar\'{e}
duality forces $HH^{d-1} = (HH^1)^\vee$ and the dimension
count propagates through the Hochschild tower.

**The observational test.**

If a second independent equation of state were discovered in
nature --- a macroscopic thermodynamic law not derivable from
$PV = NkT$ and its Legendre transforms --- it would require
$\dim HH^1 \geq 2$, which would falsify the QOU observability
axiom.  The absence of such a law in three centuries of
thermodynamics is consistent with $HH^1 = 1$.
