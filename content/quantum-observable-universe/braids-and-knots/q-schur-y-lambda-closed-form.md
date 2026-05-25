**Proposition (q-Schur Plancherel weight closed form).**
*The q-Schur Plancherel weights $y_\lambda(q)$ on the Iwahori-Hecke
algebra $H_n(q)$, characterized by the Markov axiom*

$$
  \mathrm{tr}_M(\sigma_i \cdot w) = (q - q^{-1}) \cdot \mathrm{tr}_M(w)
  \quad \text{for } w \in H_{n-1}(q),
$$

*have the closed-form expression*

$$
  y_\lambda(q) \;=\; \frac{q^{c(\lambda)}}{[n]_q!},
  \qquad \text{where } c(\lambda) = \sum_{(i,j) \in \lambda} (j - i),
$$

*the **content sum** of partition $\lambda \vdash n$. Here $[n]_q!$ is
the $q$-factorial $[n]_q! := \prod_{k=1}^n [k]_q$ with
$[k]_q = (q^k - q^{-k}) / (q - q^{-1})$.*

## Why this is closed form (and Wenzl JM isn't)

The q-Schur Plancherel weights are the **principal specialization** of
Schur polynomials at the geometric sequence $(1, q, q^2, \ldots, q^{n-1})$.
Cells of the partition $\lambda$ contribute multiplicatively to the
principal-specialization formula, giving the clean product over cells.

The **Wenzl Jones-Markov** convention (with $\mathrm{tr}(\sigma_i) = z =
1/(\sqrt{q} + 1/\sqrt{q})$, used by the framework's Borromean-based mass
formula) does NOT admit this principal-specialization structure. Its
weights solve a Schur-orthogonality sum rather than a product:

$$
  y_\lambda^{\mathrm{Wenzl}}(q) \;=\; \frac{1}{[n]_q!}
  \sum_{\mu \vdash n} |C_\mu|_q \cdot z^{n - r(\mu)} \cdot \chi_\lambda^q(\mu).
$$

The sum runs over all cycle types (= partitions of n) and uses
q-deformed character values. This is computationally O(p(n)²) (or LP)
and has no simpler closed form.

## Verification (H_2 cross-check)

For $\lambda = (2)$: cells at (0,0), (0,1); contents 0, 1; $c(\lambda) = 1$.
$[2]_q! = [1]_q \cdot [2]_q = (q + q^{-1})$.

$$
  y_{(2)}(q) \;=\; \frac{q^1}{q + q^{-1}} \;=\; \frac{q}{[2]_q}.
$$

For $\lambda = (1, 1)$: cells at (0,0), (1,0); contents 0, -1; $c(\lambda) = -1$.

$$
  y_{(1,1)}(q) \;=\; \frac{q^{-1}}{q + q^{-1}} \;=\; \frac{q^{-1}}{[2]_q}.
$$

These match the H_2 hardcoded values used by sibling's T(2,k) torus
knot closed form (commit `5418678c8`).

## Markov-normalization check

$$
  \sum_{\lambda \vdash n} y_\lambda(q) \cdot \dim_q(\lambda) \;=\; 1
$$

where $\dim_q(\lambda) = [n]_q! / \prod_{(i,j) \in \lambda} [h(i,j)]_q$
is the q-dimension. This holds by the principal-specialization
identity $\sum_\lambda s_\lambda(1, q, \ldots, q^{n-1}) \cdot \chi_\lambda(1)$ = (volume of relevant character).

## Production implementation

The Rust upstream `pyhecke_native.trace_weights_n_q_schur(n, q)` (PR
[#1256](https://github.com/litlfred/qou/pull/1256), commit `4059af433`)
implements this closed form directly:

```rust
fn trace_weights_n_q_schur(n: usize, q: f64) -> Vec<f64> {
    let qint = |k: i32| (q.powi(k) - q.powi(-k)) / (q - 1.0/q);
    let qfact_n: f64 = (1..=n as i32).map(|k| qint(k)).product();
    seminormal::partitions_of(n).iter().map(|shape| {
        let content_sum: i32 = shape.iter().enumerate()
            .flat_map(|(i, &row)| (0..row).map(move |j| j as i32 - i as i32))
            .sum();
        q.powi(content_sum) / qfact_n
    }).collect()
}
```

Cost: O(p(n) · n) — instant for any n. Verified to match the H_2
hardcoded formula exactly to machine precision (|diff| ≤ 5e-15).

## Diagnostics (§Slot J)

- **GB filtration**: N/A (the formula is purely at the partition
  level, not at a specific Hecke element)
- **Jet order**: all-orders (closed form, exact in $q$)
- **Bar-symmetry**: under $q \mapsto q^{-1}$, $c(\lambda) \mapsto -c(\lambda)$
  and $[n]_q! \mapsto [n]_q!$ (q-factorial is bar-symmetric). So
  $y_\lambda(q^{-1}) = q^{-2c(\lambda)} y_\lambda(q)$ — *not* bar-symmetric
  for non-self-conjugate partitions. For $\lambda = \lambda^T$
  (self-conjugate), $c(\lambda) = 0$ and the weight IS bar-invariant.

## Distinction from Wenzl Jones-Markov

This proposition characterises ONE of two Markov-trace conventions used
in the framework:

| Convention | $\mathrm{tr}(\sigma_i)$ | $y_\lambda(q)$ | Closed form? | Used by |
|------------|-------------------------|----------------|--------------|---------|
| **q-Schur** (this prop) | $h = q - q^{-1}$ | $q^{c(\lambda)} / [n]_q!$ | **YES** (this prop) | Torus knots, lepton tower |
| **Wenzl JM** | $z = 1/(\sqrt{q} + 1/\sqrt{q})$ | Schur-orthogonality sum | **NO** | Mass formula (Borromean) |

See [`docs/audits/2026-05-25-markov-trace-convention-audit.md`](../../docs/audits/2026-05-25-markov-trace-convention-audit.md)
for the framework-wide convention inventory.

## Cross-references

- [`prop:borromean-markov-trace-closed-form`](#prop:borromean-markov-trace-closed-form)
  — uses Wenzl JM convention (distinct from this prop)
- [`def:hecke-normal-form`](#def:hecke-normal-form)
- Sibling commit `5418678c8` — H_2 T(2,k) closed form using this prop
- PR [#1256](https://github.com/litlfred/qou/pull/1256) — Rust upstream `trace_weights_n_q_schur`
- PR [#1258](https://github.com/litlfred/qou/pull/1258) — generalized torus-knot closed-form consumer
