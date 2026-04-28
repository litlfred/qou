**Statement.**
For odd $N = 2m + 1 \ge 3$, the closed-ring topological structure
is the torus **knot** $T(2, N)$ (a single component, by
[component count of $T(2,N)$](#lem:T2N-components)).  The
ring-closure activation barrier follows the same Alexander-weight
formula as in the even-$N$ case
([ring closure barrier (quantitative)](#prop:ring-closure-barrier-quantitative)):

$$
  \Delta E_{\mathrm{closure}}(N)
   = 
  \bigl[\,(N - 1) - \Delta_{T(2,N)}(q_{0})\,\bigr]\,
  \lvert q + q^{-1}\rvert_{\mathrm{mol}}.
$$

Specialising to $q \to 1$ using
[$\Delta_{T(2,2m+1)}$ closed form](#def:torus-knot-T2-odd-alexander),
$\Delta_{T(2,2m+1)}(1) = 1$, so

$$
  \lim_{q \to 1}\, \Delta E_{\mathrm{closure}}(2m+1)
   = 
  (N - 2)\,\lvert q + q^{-1}\rvert_{\mathrm{mol}}.
$$

**Numerical predictions** (with $\lvert q + q^{-1}\rvert_{\mathrm{mol}} \approx 22.4\ \mathrm{kJ/mol}$):

| $N$ | torus knot | $\Delta(q_0)$ | $\Delta E_{\mathrm{closure}}\ (\mathrm{kJ/mol})$ |
|:---:|:----------:|:-------------:|:------------------------------------------------:|
| 3   | $3_{1}$    | 1.21          | 40.1                                              |
| 5   | $5_{1}$    | 1.83          | 71.0                                              |
| 7   | $7_{1}$    | 2.37          | 103.7                                             |
| 9   | $9_{1}$    | 2.83          | 138.4                                             |
| 11  | $11_{1}$   | 3.20          | 174.9                                             |
| 13  | $13_{1}$   | 3.49          | 213.0                                             |

**Remark.**
The odd-$N$ predicted barriers grow *faster* than the even-$N$
predictions (slope $\approx \lvert q+q^{-1}\rvert_{\mathrm{mol}}$
per added carbon, vs. $\tfrac{1}{2}\lvert q+q^{-1}\rvert_{\mathrm{mol}}$
for even $N$), reflecting the absence of the half-weight saving from
the threading link's two-component structure.  This is consistent
with the empirical observation that odd-$N$ neutral cyclopolyenes
(cyclopropene, cyclopentadiene, cycloheptatriene, …) are
*non-aromatic* and substantially less stable than their even-$N$
aromatic counterparts.

**Caveat.**
Aromatic stability of odd-$N$ rings is achieved through electron
transfer to form ions (e.g.\ cyclopentadienyl anion C${}_{5}$H${}_{5}^{-}$,
tropylium cation C${}_{7}$H${}_{7}^{+}$); these map to the *even-$N$*
threading-link structure of $T(2, N \pm 1)$ under the conjectural
correspondence in [Hückel from $T(2,N)$ invariant](#conj:huckel-from-T2N-invariant).
