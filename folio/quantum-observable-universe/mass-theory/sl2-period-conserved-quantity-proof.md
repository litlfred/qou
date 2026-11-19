*Proof.* Write $a_n := a_D^{(n)}$ and
$H_n = a_{n+1}^2 - \tau\,a_{n+1}a_n + a_n^2$. For the single step, substitute the
recurrence $a_{n+2} = \tau a_{n+1} - a_n$
([symplectic prolongation recurrence](#prop:sl2-prolongation-recurrence)) into
$H_{n+1}$:

$$
\begin{aligned}
H_{n+1}
&= a_{n+2}^2 - \tau\,a_{n+2}a_{n+1} + a_{n+1}^2 \\
&= (\tau a_{n+1} - a_n)^2 - \tau(\tau a_{n+1} - a_n)a_{n+1} + a_{n+1}^2 \\
&= \bigl(\tau^2 a_{n+1}^2 - 2\tau a_{n+1}a_n + a_n^2\bigr)
   - \bigl(\tau^2 a_{n+1}^2 - \tau a_{n+1}a_n\bigr) + a_{n+1}^2 \\
&= a_{n+1}^2 - \tau\,a_{n+1}a_n + a_n^2 \;=\; H_n .
\end{aligned}
$$

This establishes the one-step invariance in [the $\mathrm{SL}_2$ period conserved-quantity proposition](#prop:sl2-period-conserved-quantity): after unfolding the invariant and substituting the recurrence at step $n$, the goal reduces to the polynomial identity above. A straightforward induction on $n$ (base $H_0 = H_0$, step $H_{k+1} = H_k = H_0$) then gives $H_n = H_0$ for all $n$ ([the $\mathrm{SL}_2$ period conserved-quantity proposition](#prop:sl2-period-conserved-quantity)).

The first integral is exactly the quadratic form preserved by
$B \in \mathrm{Sp}(2) = \mathrm{SL}_2$: in the basis $(a_n, a_{n+1})$ the map
$(a_n, a_{n+1}) \mapsto (a_{n+1}, \tau a_{n+1} - a_n)$ is $B$, and
$\det B = 1$ is precisely the statement that $B$ fixes the area form, of which
$H_n$ is the associated symmetric invariant.

**Fork reading.** Over $\mathbb{R}$ with $\tau = 2\cosh\theta > 2$ the level set
$H_n = H_0$ is a hyperbola; an orbit on it has
$a_{n+1}/a_n \to e^{\theta}$, a constant — geometric growth, bounded ratio. The
residue-sum period $a_D^{(n)} = \sum_\lambda \dim_q$
([Seiberg–Witten algebraic residue sum](#prop:sw-period-residue-sum)) instead has
$a_{n+1}/a_n \to \infty$ (factorial growth from the square-root branch points of
the colour cubic), so $H_n \to \infty$ — it lies on no fixed conic and obeys no
$\det = 1$ recurrence. Hence the depth-$2$ $\tau$ is the $n\le 4$ effective germ,
and the genuine prolongation kernel is the q-Bessel-class $q$-difference operator
of [binding $q$-difference recurrence proposition](#prop:binding-genfun-qdifference).
$\qquad\blacksquare$
