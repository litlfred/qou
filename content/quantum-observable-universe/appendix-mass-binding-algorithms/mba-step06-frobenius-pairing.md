**Algorithm (Frobenius pairing + self-duality check).**
*Compute the symmetric bilinear pairing
$\langle a, b\rangle_F = \mathrm{tr}_M(a \cdot b)$ on $H_n(q)$ and
verify the categorical self-duality $\Psi = S^2 = \mathrm{id}$
(dualities D3 and D23 in the canonical-derivation tracker).*

### Input

- *Two Hecke normal forms $a, b \in H_n(q)$ (output of Step 2).*
- *Substrate parameter $q \in R$.*

### Output

- *Scalar $\langle a, b\rangle_F \in R[q, q^{-1}]$.*
- *Boolean assertion that $S^2 = \mathrm{id}$ holds on $a$ (and on
  every basis $T_w$).*

### Algorithm

```
1. Compute the product a · b in H_n(q) via GS reduction (Step 2).
2. Apply tr_M to the product (Step 3).
3. Optional: verify self-duality by computing S(a) and S(S(a))
   on each basis element T_w; assert S²(T_w) = T_w.
```

### Correctness conditions

1. *[`def:frobenius-pairing`](#def:frobenius-pairing) defines
   $\langle a, b\rangle_F$ as the Markov trace of the product,
   making it symmetric and non-degenerate.*
2. *[`prop:frobenius-pairing-exists`](#prop:frobenius-pairing-exists)
   gives existence in the QOU rigid-monoidal premise.*
3. *[`prop:frobenius-pairing-unique`](#prop:frobenius-pairing-unique)
   makes the pairing canonical (up to the chosen Markov parameter).*

### Complexity

*$O(\dim H_n(q))$ products + a single trace; dominated by
Step 2 (GS reduction). The $S^2 = \mathrm{id}$ check is
$O(\dim H_n(q))$ basis-element verifications.*

### Python API entry point

```python
from pyhecke import check_frobenius

# Verifies Frobenius positivity Gx ≥ 0 on the standard basis vector x.
ok = check_frobenius(x)
```

*The canonical audit script is
[`computations/audit_frobenius_pairing.py`](../../../computations/audit_frobenius_pairing.py);
the Gram matrix `G` and the Markov-trace vector `TR_M` are
exposed as constants by `pyhecke`.*

### Witness contract

*No standalone numerical witness file. Structural checks live in
`computations/audit_frobenius_pairing.py`; the
$S^2 = \mathrm{id}$ assertion is part of the Hecke-core
regression suite.*

### Notes

*The Frobenius pairing is what makes $H_n(q)$ a **rigid**
Frobenius algebra — the categorical self-duality is dual to it
under decategorification. Both are required for the Wedderburn
decomposition (Step 5) to land in the correct basis.*
