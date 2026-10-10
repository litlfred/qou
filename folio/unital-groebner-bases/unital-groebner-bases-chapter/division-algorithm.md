**Input:** $R$ a commutative ring with unity, $A$ an $R$-algebra
which is free as an $R$-module and without quasi-zeros, $(B, <)$ an
[admissible system](#def:admissible-system) on $A$, a subset
$I \subseteq A$, and $f \in A$.

**Output:** $\tilde{f} \in I$ and $r \in O(I)$ (the *remainder* of
$f$ on **division** by $I$) so that $f = r + \tilde{f}$.

1. Set $i := 0$, $f_0 := f$.
2. **While** $f_i \neq 0$:
   - Set $i := i + 1$.
   - **If** there is no $h \in I$ with $\mathrm{LT}(h) \mid f$:
     set $r_i := \mathrm{LT}(f)$ and $f_i := f_{i-1} - r_i$.
   - **Else**: choose $h_i \in I$ with
     $0 \neq \mathrm{LT}(h_i) \mid f_{i-1}$; choose
     $\lambda_i \in R^*$, $u_i, v_i \in B$ so that
     $\lambda_i \mathrm{LT}(u_i \cdot h_i \cdot v_i) = \mathrm{LT}(f_{i-1})$;
     set $f_i := f_{i-1} - \lambda_i u_i \cdot h_i \cdot v_i$ and
     $r_i := 0$.
3. Return $r := \sum_i r_i$ and
   $\tilde{f} := \sum_i \lambda_i u_i \cdot h_i \cdot v_i = f - r$.

Because we do not specify how to choose $h_i$ (nor $u_i, v_i$),
the output is not in general unique.
