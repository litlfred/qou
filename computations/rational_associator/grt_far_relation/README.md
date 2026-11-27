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
- `t3.py`: **exact over Q**, in U(t3). The t-compatibility identity `TCompat` of
  `FarRelation.lean` holds for g = exp(σ3) through degree 5 and fails for g = exp([X,Y]).
  Among degree-3 directions a·[X,[X,Y]] + b·[Y,[X,Y]], only (a,b) = (1,1) satisfies it, and
  (5.13) singles out the same direction; linear (5.14) holds for all four tested. So through degree
  3 of g, (5.13) and (5.14) imply `TCompat`. Runtime about a minute.
- `hexagon_act.py [D]`: **exact over Q**, in U(t3), default D = 5. Solves the hexagon (repo form)
  degree by degree for a group-like phi with degree-2 part [X,Y]/24 (the hexagon alone leaves
  free parameters; the script sets them to 0). With g = exp(σ3) it confirms (5.14) as
  G2 G3 G1 = 1, the identity G1 t13 G1⁻¹ + G3⁻¹ t23 G3 = t13 + t23, and the hexagon of
  φ̃ = φ(gAg⁻¹,B)·g, all through degree 5. With g = exp([X,Y]) all three fail. Imports `t3.py`.
- `exp516.py [D]`: **exact over Q**, default D = 6, runs in about 2 s. It builds the exponential
  for Drinfeld's group law (5.16), Exp(ψ) = Σ_k L^k(1)/k! with L(x) = D_ψ(x) + xψ and
  D_ψ(A) = [ψ, A], D_ψ(B) = 0, then checks Drinfeld's (5.12)–(5.15). It uses an exact normal form
  of U(t4) = U(F(t14,t24,t34)) ⋊ U(t3), so the pentagon check is cheap.
  - Exp(σ3) satisfies all four conditions through degree 8.
  - Ordinary exp(σ3) fails (5.13) and (5.15) at degree 6, and (5.14) at degree 7.
  - Exp([X,[X,Y]]), which is not in grt, fails (5.12) and (5.15) at degree 3.
