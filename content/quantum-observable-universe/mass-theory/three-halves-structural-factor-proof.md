Each identity is a Laurent-polynomial equality in $q$ and $q^{-1}$, so it
holds over any field once both sides are expanded and the common
denominator (a power of $q$) is cleared. We give the muon set explicitly
and refer the tau set, which is the same bookkeeping at higher degree, to
the Lean witnesses.

Write $h = q - q^{-1}$, so $h^2 = q^2 - 2 + q^{-2}$, and recall the
symmetric $q$-integers $[2]_q = q + q^{-1}$, $[3]_q = q^2 + 1 + q^{-2}$,
$[4]_q = q^3 + q + q^{-1} + q^{-3}$.

**Muon set.**

- $3 + h^2 = 3 + (q^2 - 2 + q^{-2}) = q^2 + 1 + q^{-2} = [3]_q$
  (`three_plus_h_sq_eq_bracket3`).
- $2 + h^2 = q^2 + q^{-2}$, hence
  $(2 + h^2)\,[2]_q = (q^2 + q^{-2})(q + q^{-1}) = q^3 + q + q^{-1} + q^{-3} = [4]_q$
  (`two_plus_h_sq_times_bracket2_eq_bracket4`).
- Dividing the second identity by $[4]_q$ and the first by $(2+h^2)$ gives
  the closure factor
  $\dfrac{3 + h^2}{2 + h^2} = \dfrac{[3]_q\,[2]_q}{[4]_q}$
  (`three_halves_factor_eq_q_brackets`); the division is legitimate since
  $2 + h^2 = q^2 + q^{-2} \neq 0$ and $[4]_q \neq 0$ for $q \neq 0$ in a
  field.

**Tau set.** The reduction
$[6]_q = [2]_q\,[3]_q\,(1 + h^2)$ and its consequence
$\dfrac{[5]_q\,[3]_q}{[6]_q} = \dfrac{[5]_q}{[2]_q\,(1 + h^2)}$
are the same Laurent-polynomial identities one degree higher
($1 + h^2 = q^2 - 1 + q^{-2}$); expanding both sides and clearing the
$q^{5}$ denominator reduces each to a polynomial identity. The mechanical
expansion is discharged in Lean by `field_simp; ring`
(`bracket6_eq_bracket2_bracket3_times_one_plus_h_sq`,
`bracket5_bracket3_div_bracket6`).

All five are proved over generic `[Field R]` per AGENTS.md §7c, and the
numerical cross-checks at the substrate $q_0 \approx 1.110$ agree to
$\leq 10^{-40}$ in the `tau-amphichiral-sdp-probe` witness. $\qquad\blacksquare$
