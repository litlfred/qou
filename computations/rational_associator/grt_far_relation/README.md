# Far relation [s13, s24] for the GRT-transported family (bean qou-3fdg)

Run from this directory. No floats: `Fraction` (exact) or integer arithmetic mod a prime.

- `rank2.py`: degree-2 spans. DK4 relations 11; bracketing-local commutations 10; together 11.
- `deg4q.py`: **exact over Q.** Take g with degree-2 part [X,Y]. That part satisfies the
  pentagon to its order and (5.13). Then [s13,s24] has a nonzero degree-4 part in U(t4)
  (22-entry residual after reduction modulo the DK ideal).
- `test5.py [prime]`: degree 5, mod p. Among degree-3 Lie elements only
  [X,[X,Y]] + [Y,[X,Y]] (the grt element σ3) satisfies the pentagon. For it, [s13,s24]_5 lies in
  the DK ideal; for the three other directions tested it does not. Checked with p = 2147483629 and
  p = 1000000007. dim U(t4)_4 = 301 and dim U(t4)_5 = 966 agree with the Hilbert series
  1/((1-t)(1-2t)(1-3t)).
- `coef.py`, `gen.py`: ±1 coefficients and the generator of the Lean lemmas `dk4_of_locals`,
  `locals_of_dk4` and `commute_total`.
