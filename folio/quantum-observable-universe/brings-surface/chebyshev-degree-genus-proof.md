**Proof.**
The Hecke relation $T^2 = s T + \mathbf{1}$ (where $s = q - q^{-1}$)
gives the recurrence $a_{n+1} = s \cdot a_n + a_{n-1}$ with
$a_0 = 0$, $a_1 = 1$.  For odd $n$, each step increases the
degree in $s$ by $1$, so $\deg_s a_n = n - 1$.  Since odd-indexed
$a_n$ involve only even powers of $s$, write $u = s^2$ and
obtain $\deg_u a_n = (n-1)/2$.

For $T_{2,p}$, the Seifert genus is $(2-1)(p-1)/2 = (p-1)/2$,
confirming $\deg_u a_p = g(T_{2,p})$.

The leading coefficient: the recurrence shows that the leading
term of $a_{2k+1}$ in $u$ is $u^k$ with coefficient $1$ (each
multiplication by $s$ raises the degree by $1$, and the leading
term picks up no lower-order contamination from $a_{n-1}$).
$\square$
