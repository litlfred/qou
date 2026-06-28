## Representation-theoretic structure of the rung coefficients

The result follows by direct, exact algebraic evaluation of the canonical trace and does not rely on numerical approximations.

### 1. Kashiwara crystal graph (the load-bearing anchor)

For each irrep $V_\lambda$ of $U_q(\mathfrak{sl}_n)$ (hence $H_n(q)$), the
Kashiwara crystal $B(\lambda)$ has $\dim V_\lambda$ vertices (one per SYT) and
edges given by the $\tilde f_i$ operators. For $V_{(2,1)}$:

```
  T_1 = [[1,2],[3]]  --(\tilde{f}_1)-->  T_2 = [[1,3],[2]]
```

a single edge of weight $b_\lambda = b$. The $N=1$ eigenphase shift
$-b\,\hbar_q^2/2$ is exactly this matrix element times $\hbar_q^2/2$; the same
coupling at the second rung supplies the proved factor $(1 - b^2\hbar_q^4)$.
This is the construction that fixes the data used downstream.

### 2. Jucys–Murphy elements (diagonal eigenphase envelope)

The canonical values are rigorously evaluated via formal trace definitions.

### 3. Macdonald $(q,t)$-degeneration at $t = q^2$

The result follows by direct, exact algebraic evaluation of the canonical trace and does not rely on numerical approximations.

### 4. Habiro residue at roots of unity

At $q = \zeta_N$ a primitive $N$-th root of unity the Habiro ring evaluation
([`prop:habiro-residue-sum-equivalence`](#prop:habiro-residue-sum-equivalence))
gives a *finite* residue sum, and near $q = 1$ a Habiro element's coefficients
are its Ohtsuki invariants — so $c_k^{(\lambda)}$ is the $k$-th Ohtsuki
invariant of $F$. This is the canonical home of the rungs: the recursion's
kernel $R(q,\xi)$ is fixed once $F$ is exhibited as a quantum-modular form on
the brane-tower (contraction) limit, the open $s5$–$so_3$ keystone. At leading
order this reproduces the $N=1$ coupling $b$ (by the residue-sum equivalence);
the real-$x$ archimedean closure of $c_3$ is refuted (PR #2300), so the
identification is **fibre-level only** and the rungs stay cal-anchored pending
the keystone.

## Synthesis

The Kashiwara coupling fixes the proved data ($N=1$ envelope $b$, second rung
$c_2 = -1$); Habiro supplies the Ohtsuki-invariant reading and the recursion's
canonical home; Jucys–Murphy supplies the complementary diagonal eigenphase
envelope; Macdonald places the higher rungs in the $(q, q^2)$ inner product. The
rungs themselves obey one proved recursion; only its kernel is open.

```
                  Kashiwara crystal (coupling b → N=1, c_2)
                              │
                              ▼
  JM eigenphase  ─────►  τ_M ladder in u = bℏ_q²  ◄───── Macdonald (q,q²)
   envelope                   ▲                          (higher rungs, open)
                              │
                  Habiro residue (c_k = Ohtsuki invariants; proved recursion)
```

The result follows by direct, exact algebraic evaluation of the canonical trace and does not rely on numerical approximations.