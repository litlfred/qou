**Proposition (symplectic prolongation $\Rightarrow$ one-parameter recurrence).**

The recurrence on the prolonged Seiberg--Witten periods has depth $2$
([`prop:prolonged-periods-fixed-depth`](#prop:prolonged-periods-fixed-depth)
together with the $S_5$-Hodge count $H^1 = 2W$): the $2\times 2$ prolongation
operator $B$ on the Hodge multiplicity plane carries the whole kernel,
$R = x^2 - \operatorname{tr}(B)\,x + \det(B)$.

The Gauss--Manin monodromy **preserves the principal polarisation** of the
curve — the cup-product symplectic form on $H^1$, which restricts
non-degenerately to the rank-$2$ $W$-isotypic Hodge plane (the polarisation is
$S_5$-invariant). Hence $B \in \mathrm{Sp}(2) = \mathrm{SL}_2$ and

$$
\boxed{\;\det B = 1\;}
\qquad\Longrightarrow\qquad
R = x^2 - \tau\,x + 1,\quad \tau := \operatorname{tr} B,
$$

consequently the prolonged periods satisfy the one-parameter "Lucas/Chebyshev" recurrence

$$
a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)} .
$$

The kernel $R$ is therefore reduced to the **single** number $\tau = \operatorname{tr} B$,
the trace of the prolongation monodromy. The non-hyperbolic torus sector
confirms the form: its recurrence is $x^2 - 2\cosh(2\eta_0)\,x + 1$, i.e.
$\det = 1$ with $\tau = 2\cosh(2\eta_0)$. For the hyperbolic binding sector
$\tau = 2\cosh\theta$ for a prolongation rapidity $\theta$; pinning $\theta$ is
the last open number of the keystone, and is solvable from three residue
weights via $\tau = (a_D^{(2)} + a_D^{(4)})/a_D^{(3)}$.

The Lean witness
[`QOU.Mass.sl2_prolongation_recurrence`](#prop:sl2-prolongation-recurrence)
proves the recurrence form from the $\det B = 1$ Cayley--Hamilton relation,
sorry-free.
