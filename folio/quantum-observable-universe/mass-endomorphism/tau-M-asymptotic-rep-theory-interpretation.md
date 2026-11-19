## Representation-theoretic structure of the rung coefficients

### 1. Kashiwara crystal graph (the load-bearing anchor)

For each irreducible representation $V_\lambda$ of $U_q(\mathfrak{sl}_n)$ (and hence $H_n(q)$), the Kashiwara crystal $B(\lambda)$ contains $\dim V_\lambda$ vertices (one per standard Young tableau) and edges given by the $\tilde f_i$ operators. For $V_{(2,1)}$:

```
  T_1 = [[1,2],[3]]  --(\tilde{f}_1)-->  T_2 = [[1,3],[2]]
```

This single edge has weight $b_\lambda = b$. The $N=1$ eigenphase shift $-b\,\hbar_q^2/2$ equals this matrix element multiplied by $\hbar_q^2/2$. The same coupling enters the second-rung factor $(1 - b^2\hbar_q^4)$, which is taken as given here rather than derived. This construction fixes the data used downstream.

### 2. Jucys–Murphy elements (diagonal eigenphase envelope)

The canonical values are rigorously evaluated using formal trace definitions.

### 3. Macdonald $(q,t)$-degeneration at $t = q^2$

The degeneration $t = q^2$ carries the Macdonald pairing onto the coordinate in which the relevant $H_3$ scalar invariants are rational. Its role among the four anchors is placement rather than evaluation: it locates the higher rung coefficients $c_k$, $k \ge 3$, in the $(q, q^2)$ inner product, but determines none of them. No closed form for a rung beyond $c_2$ follows from the degeneration alone. The higher rungs remain open and calibration-anchored.

### 4. Habiro residue at roots of unity

At $q = \zeta_N$, a primitive $N$-th root of unity, the Habiro ring evaluation ([Habiro residue-sum equivalence](#prop:habiro-residue-sum-equivalence)) yields a finite residue sum. Near $q = 1$, the coefficients of a Habiro element match its Ohtsuki invariants. Thus, $c_k^{(\lambda)}$ is the $k$-th Ohtsuki invariant of $F$. This forms the canonical home of the rungs. The recursion's kernel $R(q,\xi)$ is determined once $F$ is exhibited as a quantum-modular form on the brane-tower (contraction) limit (the open $s5$–$so_3$ fibre action). At leading order, this reproduces the $N=1$ coupling $b$ through the residue-sum equivalence. The real-$x$ archimedean closure of $c_3$ is refuted; the identification remains strictly fibre-level, and the rungs stay calibration-anchored pending that fibre action.

## Synthesis

The Kashiwara coupling fixes the $N=1$ envelope $b$ and enters the second-rung factor, whose ladder reading is $c_2 = -1$. Habiro provides the Ohtsuki-invariant reading and the canonical home of the recursion. Jucys–Murphy supplies the complementary diagonal eigenphase envelope. Macdonald places the higher rungs in the $(q, q^2)$ inner product. The rungs are conjectured to obey a single recursion whose kernel is open.

```
                  Kashiwara crystal (coupling b → N=1, c_2)
                              │
                              ▼
  JM eigenphase  ─────►  τ_M ladder in u = bℏ_q²  ◄───── Macdonald (q,q²)
   envelope                   ▲                          (higher rungs, open)
                              │
                  Habiro residue (c_k = Ohtsuki invariants; proved recursion)
```
