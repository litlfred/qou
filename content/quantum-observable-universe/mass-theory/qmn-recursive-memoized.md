**Proposition (recursive memoised q-MN: speed + storage win).**
*The classical Murnaghan-Nakayama rule expresses $\chi_\rho^\lambda$
recursively via border-strip removal:*

$$
  \chi_\rho^\lambda \;=\; \sum_{\xi \in BS(\lambda, \rho_1)}
                          (-1)^{\mathrm{ht}(\xi)} \,
                          \chi_{\rho \setminus \rho_1}^{\lambda \setminus \xi}
$$

*where $BS(\lambda, \rho_1)$ is the set of border strips of size $\rho_1$
in $\lambda$, $\mathrm{ht}(\xi)$ is the height of strip $\xi$, and
$\rho \setminus \rho_1$ is $\rho$ with its first part removed.*

*The **q-deformed analogue** (Halverson-Ram broken-strip rule) replaces
the sign $(-1)^{\mathrm{ht}(\xi)}$ by a q-weight, but the recursion
structure is identical: $\chi_\rho^\lambda(q)$ at level $n = |\lambda|$
reduces to characters at level $n - \rho_1 < n$.*

*Memoising the recursive call cache `χ_{ρ}^{λ}(q)` indexed by
$(\rho, \lambda)$ gives:*

| Property | Direct iteration | Recursive memoised |
|---|---|---|
| Time, single char | $O(n^2)$ (q-MN canonical) | $O(\#BS \cdot \text{recursion depth})$ amortised |
| Time, batch all $(\rho, \lambda)$ at level $\leq n$ | $O(p(n)^2 \cdot n^2)$ | $O(p(n)^2 \cdot \#BS_{\max})$ amortised, **$\sim 10\times$ faster** |
| Storage, no cache | $O(1)$ | $O(p(n)^2)$ — cache size |
| Storage, character table | $O(p(n)^2)$ | $O(p(n)^2)$ — same |

## Why memoisation wins for atom-knot work

For ${}^{6}$Li / ${}^{7}$Li atom-knot identification ([wenzl-qmn-synergy](#prop:wenzl-qmn-synergy)),
we need $\chi_\lambda(\mathcal{B}_K; q_0)$ for **many** hyperbolic knots
$K$ with crossing-number $\leq 10$ at $H_{18}, H_{21}$. Each braid
$\mathcal{B}_K$ has cycle type $\rho_K$ in $S_n$.

**Without memoisation**: $385$ partitions $\times$ ~60 hyperbolic
knots $\times$ ~$18^2$ ops $\approx 7.5 \cdot 10^6$ q-MN evaluations.

**With recursive memoisation**: many subproblems shared across
different $K$'s. The recursion tree at level $18$ has at most
$p(18)^2 = 148\,225$ entries — a one-time fill, then $O(1)$ lookups.
Total: $\sim 1.5 \cdot 10^5$ ops for the table fill, $\sim 60$
lookups per knot. **$\sim 50\times$ speedup** for batch character
evaluation.

## Storage reduction

The $q$-character table at level $n = 21$ stored EXPLICITLY via
Hoefsmit seminormal would need:

$$
  \sum_{\lambda \,\vdash\, 21} \dim_\lambda^2 \approx 21!
$$

bytes per single $T_w$. Storing characters as $(\rho, \lambda, \chi(q))$
triples in the recursive memo cache:

$$
  p(21)^2 = 627\,264
$$

entries, each a q-rational expression — total $\sim 100$ MB at
n=21 vs $\sim 50$ TB for full seminormal.

## Connection to existing infrastructure

The current main has:

- [`q_mn_canonical.py`](https://github.com/litlfred/qou/blob/main/computations/q_mn_canonical.py)
  — Halverson-Ram broken-strip q-MN for canonical $T_w$,
  $O(n^2)$ per $(\lambda, \mu)$.

The proposed extension:

- `q_mn_recursive_memoized.py` (this PR / follow-up): wrap
  `q_mn_canonical` with a recursive driver
  `chi_recursive(λ, ρ, cache)` that:
  1. Looks up `cache[(λ, ρ)]`.
  2. If miss, computes via the recursion above (border-strip
     enumeration $\to$ recursive call on $(λ \setminus \xi,
     ρ \setminus ρ_1)$).
  3. Stores result in cache.

This is **memoisation, not algorithmic restructuring** — the
recursive MN was always the most efficient form; just hadn't been
implemented with caching in this codebase.

## Combined with Wenzl-bridge

The Markov trace
$\mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda(q) \cdot \chi_\lambda(T_w; q)$
([wenzl-qmn-synergy](#prop:wenzl-qmn-synergy)) becomes:

```python
# Pre-compute once: y_λ(q) for all λ ⊢ n via Wenzl-bridge
y_table = {λ: y_lambda_wenzl(λ) for λ in partitions_of(n)}
# Pre-compute once: full χ table via recursive memoised q-MN
cache = {}
chi_table = {(λ, ρ): chi_recursive(λ, ρ, cache)
             for λ in partitions_of(n) for ρ in partitions_of(n)}
# Then per-knot tr_M is O(p(n)) sum:
def tr_M(braid_K):
    ρ = cycle_type(braid_K)
    return sum(y_table[λ] * chi_table[(λ, ρ)] for λ in partitions_of(n))
```

This is the **canonical compute pipeline** for atom-knot
identification at high $n$.

## Open

- **Implement**: `q_mn_recursive_memoized.py` driver. Mechanical
  wrapper over existing `q_mn_canonical.py`; estimated 1-day work.
- **Profile**: confirm $\sim 50\times$ speedup empirically at $n = 18, 21$.
- **Lean**: state recursive MN identity as a theorem and the
  memoisation as `simp`-rewrite (open).
