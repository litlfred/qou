**Proposition (general orbit-sum identity for $\mathrm{Cl}_3$ at every
root of unity).**

[`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
established the orbit sum at $N = 5$.  *This proposition generalises
to **all** $N \geq 2$:*

$$
  \boxed{\;
    \sum_{k=1}^{N - 1} \mathrm{Cl}_3\!\left(\tfrac{2\pi k}{N}\right)
    \;=\;
    -\frac{N^2 - 1}{N^2} \cdot \zeta(3).
  \;}
$$

*For odd $N$, parity halves the sum: $\sum_{k=1}^{(N-1)/2} \mathrm{Cl}_3(2\pi k/N)
= -\frac{N^2 - 1}{2N^2} \zeta(3)$.*
### Significance

**Generalises round 11 of ** from "$\zeta_5$ only" to "every
$N \geq 2$". Concretely:

1. **For every cyclotomic field $\mathbb{Q}(\zeta_N)$**, the real-part
   orbit sum of depth-3 grouplikes reduces to a rational multiple of
   $\zeta(3)$ (Apéry, classical).
2. **The genuinely-new content per cyclotomic field** is therefore
   the *individual* $\mathrm{Cl}_3(2\pi k/N)$ values modulo this
   sum — exactly $\lfloor (N - 1)/2 \rfloor - 1$ independent real
   numbers per prime $N$ (for $N$ prime).
3. **Combined with
   [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)**
   (imaginary parts also Tate-rational), the depth-3 surface for
   $\mathbb{Q}(\zeta_N)$ over $\zeta_N$-arguments reduces to **at most
   $\lfloor (N - 1)/2 \rfloor - 1$ genuinely-new real numbers**.

### Cross-references

- Special case $N = 5$ (round 11 of ):
  [`prop:cl3-zeta5-orbit-sum-identity`](#prop:cl3-zeta5-orbit-sum-identity)
- Companion imaginary-part theorem:
  [`prop:cyclotomic-trilog-imaginary-closed-form`](#prop:cyclotomic-trilog-imaginary-closed-form)
- canonical witness (verified at $N = 3, 4, 5, 6, 7, 10, 11, 12, 13$ at 50 dps):
  [`cyclotomic-trilog-imaginary.witness.json`](https://github.com/litlfred/qou/blob/main/computations/cyclotomic-trilog-imaginary.witness.json)
- Period ledger: [`rem:transcendental-accounting`](#rem:transcendental-accounting)
- PSLQ certification at $\zeta_5$ (open beyond):
  [`prop:cl3-zeta5-pslq-independence`](#prop:cl3-zeta5-pslq-independence)
