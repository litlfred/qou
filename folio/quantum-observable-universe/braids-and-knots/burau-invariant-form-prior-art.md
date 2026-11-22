**Remark (prior art: the Burau representation preserves a sesquilinear form).**
For a matrix $M$ over $\mathbb{Z}[t, t^{-1}]$ let $M^*$ be its transpose with every entry $p(t)$ replaced by $p(t^{-1})$. Squier proves that there is a nonsingular $(n-1) \times (n-1)$ matrix $J_0$ over $\mathbb{Z}[t, t^{-1}]$ with $\beta(w)^* J_0\, \beta(w) = J_0$ for every $w \in B_n$, where $\beta$ is the reduced Burau representation \cite[Theorem, p. 199]{squier1984}. Over $\mathbb{Z}[s, s^{-1}]$ with $s^2 = t$, rescaling the basis by $s^a$ turns $J_0$ into the Hermitian matrix
$$
J = (s + s^{-1})\, I - \sum_a \left(e_{a-1,a} + e_{a,a+1}\right),
$$
and each generator then acts as the reflection $\beta_i(v) = v - (s^2 + 1)\, \langle e_i, v \rangle / \langle e_i, e_i \rangle \; e_i$, with $\langle v, w \rangle = v^* J w$ \cite[\S 3, eqs. (6)--(7), p. 201]{squier1984}.

The [proof of the Borromean fibre theorem](#thm:borromean-character-fibre) uses the Burau representation at $t = -1$. There the substitution $t \mapsto t^{-1}$ fixes $t$, so Squier's identity specialises to $\beta(w)^{\mathsf{T}} J_0(-1)\, \beta(w) = J_0(-1)$: an integral bilinear form preserved by the image of $B_3$. The proof does not use this form; it argues from traces and the $R$, $L$ normal form in $\mathrm{SL}(2,\mathbb{Z})$.

Two points stop the form from being used at $t = -1$ without further work. Nonsingularity is a statement over $\mathbb{Z}[t, t^{-1}]$, so whether $J_0(-1)$ is still nonsingular, and what its signature is, has not been checked here. And at $s = i$ the diagonal entry $\langle e_i, e_i \rangle = s + s^{-1}$ is zero, so the reflection formula above is not defined at that point. The corpus's other $t = -1$ object, the Jordan block of the Hecke generator at $q = i$, is a different module, and Squier's form says nothing about it directly.
