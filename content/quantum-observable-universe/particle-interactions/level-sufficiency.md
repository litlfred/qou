**Proposition.**
*Let $P = (\mathrm{name}, \ell, [K]_M, n_0)$ be a
[confined particle](#def:confined-particle) and let*

$$
  \uparrow_\ell \colon P \longrightarrow P^{\uparrow}
  \quad\text{with}\quad
  P^{\uparrow} = (\mathrm{name}, \ell - 1, [\iota(K)]_M, n_1)
$$

*be an unfolding morphism in the
[confinement category](#def:confinement-category), where
$\iota: H_{n_0}(R, q) \hookrightarrow H_{n_1}(R, q)$ is the Hecke inclusion
and $n_1 \ge n_0$.  If the coarse witnessed partition truncation
satisfies*

$$
  k_{\max}(P, q) \le n_0
  \qquad (\text{coarse SDP captures full content}),
$$

*then the Markov trace is preserved along the unfolding:*

$$
  \mathrm{tr}_M\!\left(T_w^{\downarrow}\right)
  \;=\;
  \mathrm{tr}_M\!\left(T_w^{\uparrow}\right)
  \quad\text{in }\mathbb{C}(q),
$$

*where $T_w^{\downarrow} \in H_{n_0}(q)$ and
$T_w^{\uparrow} \in H_{n_1}(q)$ are the Gröbner–Shirshov normal forms
of $K$ at coarse and fine levels respectively.  Consequently, every
trace-class invariant $\mathcal{F}$ of $P$ — mass
$\mathfrak{m}(P)$, binding $B(P)$, Jones polynomial
$J_P(q)$ — takes the same value on $P$ and $P^{\uparrow}$:*

$$
  \mathcal{F}(P) \;=\; \mathcal{F}(P^{\uparrow}).
$$

*The coarsest level at which
$k_{\max}(P, q, n) \le n$ is **computationally sufficient**:
unfolding to any deeper level is superfluous for trace-class
invariants.*

*

**Converse (unfolding necessity).**
*If $k_{\max}(P, q) > n_0$ — the witnessed partition content of $P$
exceeds the coarse strand count — then no representation of
$T_w^{\downarrow}$ as an element of $H_{n_0}(q)$ captures all tight
dual blocks of the [confinement SDP](#prop:confinement-sdp).
Unfolding to the smallest level $n_1$ with
$k_{\max}(P, q, n_1) \le n_1$ is strictly required; the unfolded
trace $\mathrm{tr}_M(T_w^{\uparrow})$ differs from any coarse
surrogate by contributions from the additional blocks.  Magic shell
closure and multi-operator binding configurations
($\mu(S, q) \ge 2$) are the principal triggers.*

**Corollary (default-coarse computability).**
*Every trace-class invariant $\mathcal{F}$ computed at the coarsest
level satisfying $k_{\max} \le n$ is exact.  Default-coarse
computation is not a performance heuristic — it is the content of
this proposition.*
