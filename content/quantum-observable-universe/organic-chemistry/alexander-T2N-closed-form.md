**Statement.**
For every integer $N \ge 2$, the symmetric Alexander polynomial of
the torus link $T(2,N)$ admits the closed form

$$
  \Delta_{T(2,2m)}(q)
   = 
  \frac{q^{m} - q^{-m}}{q - q^{-1}}
   = 
  q^{m-1} + q^{m-3} + \cdots + q^{-(m-1)}
  \qquad (\text{even } N = 2m),
$$

$$
  \Delta_{T(2,2m+1)}(q)
   = 
  \frac{q^{2m+1} + q^{-(2m+1)}}{q + q^{-1}}
  \qquad (\text{odd } N = 2m+1).
$$

In particular, the values used by the chapter
([threading link](#def:threading-link), [ring closure
barrier](#prop:ring-closure-barrier)) are recovered as

$$
  \Delta_{T(2,2)}(q) = 1,
  \quad
  \Delta_{T(2,4)}(q) = q + q^{-1},
  \quad
  \Delta_{T(2,6)}(q) = q^{2} + 1 + q^{-2},
  \quad
  \Delta_{T(2,8)}(q) = q^{3} + q + q^{-1} + q^{-3}.
$$

**Defining identity.**
Both branches are characterised by the algebraic identities

$$
  (q - q^{-1})\,\Delta_{T(2,2m)}(q) = q^{m} - q^{-m},
  \qquad
  (q + q^{-1})\,\Delta_{T(2,2m+1)}(q) = q^{2m+1} + q^{-(2m+1)},
$$

each verified symbolically for $N = 2, \dots, 12$ by the
computational witness.
