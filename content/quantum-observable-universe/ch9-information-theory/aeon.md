Let $U \subset M_0$ be an affine chart with information-theoretic
time $\mathcal{T}$
([information-theoretic time](#def:information-theoretic-time))
and let $\mathcal{S}_k$ denote the configuration at step $k$
([bundle initial conditions](#def:bundle-initial-conditions)).

An **aeon** is a maximal connected open interval
$(a, b) \subseteq \mathbb{Z}$ (with $a \in \mathbb{Z} \cup \{-\infty\}$,
$b \in \mathbb{Z} \cup \{+\infty\}$) such that:

1. For every $k \in (a, b)$, the degree-$0$ algebra is
   non-trivial: $\Gamma(U, A_0|_{\mathcal{S}_k}) \neq 0$.
2. If $a > -\infty$, then $\mathcal{S}_a$ is a jet horizon
   ([jet horizon](#def:jet-horizon)) or a big bang state
   ([big bang state](#def:big-bang-state)):
   $\Gamma(U, A_0|_{\mathcal{S}_a}) = 0$.
3. If $b < +\infty$, then $\mathcal{S}_b$ is a jet horizon:
   $\Gamma(U, A_0|_{\mathcal{S}_b}) = 0$.

The boundaries $\mathcal{S}_a$ and $\mathcal{S}_b$ (when finite)
are the **aeon boundaries**.  An aeon is **past-complete** if
$a = -\infty$ and **future-complete** if $b = +\infty$.

**Boundary data.**
At an aeon boundary $\mathcal{S}_a$ or $\mathcal{S}_b$, the
degree-$0$ data vanishes but the higher-jet data persists.  The
**boundary datum** is the pair

$$
  \partial\mathcal{A}
  \;=\;
  \bigl(\,
    \Gamma(U,\, A_1/A_0)|_{\mathcal{S}_a},\;\;
    \Gamma(U,\, A_2/A_0)|_{\mathcal{S}_a}
  \,\bigr)
$$

— the linear (degree-$1$) and curvature (degree-$2$) jet data
that survives the horizon.  This is the algebraic analogue of
the CMB: thermal radiation without particle identity.

**Aeon adjacency.**
Two aeons $\mathcal{A} = (a, b)$ and $\mathcal{A}' = (b, c)$ are
**adjacent** if they share a boundary at $\mathcal{S}_b$.
The boundary datum $\partial\mathcal{A}|_b$ of the first aeon
serves as the seed for the second: the forward light cone of
$\mathcal{A}'$ unfolds from the degree $\geq 1$ data inherited
from $\mathcal{A}$.

**Reverse flow.**
The backward iteration $f_q^{-1}$ applied to configurations
$\mathcal{S}_k, \mathcal{S}_{k-1}, \ldots$ reverses
computation.  If this sequence reaches a step $a$ where
$A_0|_{\mathcal{S}_a} = 0$, the affine chart acquires a past
boundary — a big bang state.  Whether this occurs depends on
the dynamics: the framework does not assume past-completeness
or past-incompleteness.
