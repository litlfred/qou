**Proposition (per-block character closed forms, antipode pairing,
vanishing at $q = 1$).**
*For all $q > 0$,*

$$
  \chi_{(3)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q},
$$
$$
  \chi_{(2,1)}(\Delta_{T_\beta})(q)
  \;=\; \frac{(q^2 - 1)(-q^4 - 1)}{4q^3},
$$
$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; -\frac{(q^2 - 1)(q^2 + 1)^2}{4q^5}.
$$

*Each block vanishes at $q = 1$ (the classical point), and the
antipode pairing*

$$
  \chi_{(1,1,1)}(\Delta_{T_\beta})(q)
  \;=\; q^{-4} \cdot \chi_{(3)}(\Delta_{T_\beta})(q)
$$

*holds for all $q > 0$.*
## Cross-references

- The probe computation:
  [`computations/qbeta/qbeta_c3_multiblock_recursion_attack.py`](../../../computations/qbeta/qbeta_c3_multiblock_recursion_attack.py)
  (witness `qbeta-c3-multiblock-recursion-attack.witness.json`).
- The pre-archimedean recursion for $z$: 
  [`computations/qbeta/qbeta_prearchimedean_z_recursion.py`](../../../computations/qbeta/qbeta_prearchimedean_z_recursion.py).
- The downstream c$_k$ conjectures:
  [`conj:qbeta-c-k-closed-forms`](#conj:qbeta-c-k-closed-forms)
  (axiomatised; conditional on the Habiro element identification).
- The 1ppQ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
