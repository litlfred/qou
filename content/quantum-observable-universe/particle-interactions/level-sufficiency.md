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

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
