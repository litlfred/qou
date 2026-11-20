By [A fixed-depth recurrence for the prolonged periods exists (Cayley–Hamilton)](#prop:prolonged-periods-fixed-depth)
the prolongation acts through a $2\times 2$ operator $B$ on the $W$-Hodge plane,
and Cayley--Hamilton gives $B^2 = \mathrm{tr}(B)\,B - \det(B)\,\mathbf 1$.

The cup-product pairing $\langle\alpha,\beta\rangle = \int \alpha\wedge\beta$ on
$H^1$ is a symplectic form preserved by the Gauss--Manin monodromy (it is
topological, hence flat for $\nabla$). It is $S_5$-invariant and restricts
non-degenerately to the rank-$2$ $W$-isotypic Hodge plane (the Hodge--Riemann
bilinear relations make $\langle H^{1,0}, H^{0,1}\rangle$ a perfect pairing).
Therefore $B$ preserves a non-degenerate alternating form on a $2$-dimensional
space, i.e. $B \in \mathrm{Sp}(2) = \mathrm{SL}_2$, so $\det B = 1$.

Substituting $\det B = 1$ into Cayley--Hamilton gives
$B^2 = \tau\,B - \mathbf 1$ with $\tau = \mathrm{tr}\, B$. Multiplying by
$B^n$ and using $B^{n}\!\cdot B^2 = B^{n+2}$, $B^{n}\!\cdot B = B^{n+1}$,
$$
B^{\,n+2} = B^n(\tau B - \mathbf 1) = \tau\,B^{\,n+1} - B^{\,n},
$$
which is the Lean theorem
[`QOU.Mass.sl2_prolongation_recurrence`](#prop:sl2-prolongation-recurrence)
(`rw [pow_add, hCH, mul_sub, mul_one, mul_smul_comm, ← pow_succ]`). Applying the
period functional $\varphi(\,\cdot\,v_0)$ gives
$a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}$, leaving the single unknown
$\tau$, recoverable from any three consecutive periods as
$\tau = (a_D^{(n)} + a_D^{(n+2)})/a_D^{(n+1)}$. $\qquad\blacksquare$
