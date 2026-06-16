For light atoms on the **doubly-symmetric line $Z = N = k$**, the
canonical Kashaev binding-energy law

$$
  B_{\rm Kashaev} \;=\; \rho_{\rm struct} \cdot m_e \cdot
  \mathrm{Vol}_{\rm hyp}(K_A)
$$

acquires a **substrate-q correction** at finite $q$ that we
conjecture takes the form

$$
  B(Z\!=\!N\!=\!k,\;q)
  \;=\;
  m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A) \cdot
  \bigl(\rho_{\rm struct} + A - [A]_q\bigr),
  \qquad A = 2k.
$$

At $q = 1$: $[A]_q = A$, recovering the classical integer Kashaev
law.

### Empirical support

Numerical match at $q_0 = 1.10998\ldots$ for the four atoms in the table
([per-atom δρ probe](../../../computations/per-atom-rho-deviation.witness.json)):

| atom | err (Kashaev) | err (corrected) | improvement |
|------|--------------:|----------------:|------------:|
| ${}^2$H   | $+1.090\,\%$  | $+0.011\,\%$    | $\times 99$ |
| ${}^4$He  | $+5.867\,\%$  | $+0.057\,\%$    | $\times 103$ |
| ${}^{12}$C  | $+5.410\,\%$  | $+0.063\,\%$    | $\times 86$ |
| ${}^{16}$O  | $+5.301\,\%$  | $+0.152\,\%$    | $\times 35$ |

${}^{12}$C and ${}^{16}$O close *via propagation* through the existing α-cluster
formula: their predicted binding energies are derived from
$B(\!^4\!\mathrm{He})$ as
$B(\!^{4n}\!\mathrm{X}) = n \cdot B(\!^4\!\mathrm{He}) + \binom{n}{2} \cdot c_{\alpha\alpha}$;
once $B(\!^4\!\mathrm{He})$ closes, the doubly-magic α-cluster chain
follows without re-fitting.

### Categorical interpretation

The dimensional anomaly $A - [A]_q$ identifies as the deficit of the
**q-dimension of the natural representation**
$V^{(A-1)} = \mathrm{Sym}^{A-1}(V)$ of $U_q(\mathfrak{sl}_2)$:

$$
  A - [A]_q
  \;=\;
  \dim_\mathbb{C} V^{(A-1)} \;-\; q\text{-dim}_q V^{(A-1)}.
$$

At $q > 1$ the q-dimension exceeds the integer dimension, so the
correction has sign $-([A]_q - A) < 0$: the integer Kashaev law
**overestimates** the binding by exactly the dimensional anomaly,
scaled by $m_e \cdot \mathrm{Vol}_{\rm hyp}(K_A)$.

### Why Z=N specifically

The Z=N line has a Z$\leftrightarrow$N exchange symmetry of the substrate fluid
that the formula respects. For $Z \neq N$ atoms (${}^{3}$H, ${}^{3}$He), the
formula fails: ${}^{3}$H and ${}^{3}$He have q-corrections differing by $2.9\,\%$,
ruling out any Z$\leftrightarrow$N exchange-symmetric closed form and pointing to
a **Coulomb-asymmetry** correction
(cf. [Coulomb-q-Hecke audit](../../../docs/audits/-coulomb-q-hecke-principled.md))
that the substrate alone cannot absorb.
