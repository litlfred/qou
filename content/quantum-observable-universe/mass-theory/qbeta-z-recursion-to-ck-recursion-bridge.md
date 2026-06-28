**Proposition (forward form of the $z$-recursion).** *For any
`ZRecursionCoeffs` instance with Taylor coefficient sequence $a_n$,
and for $n \geq 1$,*

$$
  a_{n+1} = -\frac{3n}{2(n+1)} \cdot a_n
            -\frac{2n-1}{4(n+1)} \cdot a_{n-1}.
$$

*Equivalently, $a_{n+1}$ is a linear combination of $a_n$ and $a_{n-1}$
with $n$-dependent coefficients (kernel functions of $n$, NOT constant
in $n$).*
## Cross-references

- Parent block #1 (upstream):
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (`ZRecursionCoeffs` class).
- Parent block #2 (sibling on main):
  [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
  (`CKRecursion` structure).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
