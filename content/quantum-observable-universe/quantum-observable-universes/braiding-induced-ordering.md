**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
([QOU](#def:quantum-observable-universe)) whose braiding
$c_{V,V} \colon V \otimes V \to V \otimes V$ is non-symmetric
($c_{V,V}^2 \neq \mathrm{id}$).  Then $c_{V,V}$ determines
a canonical admissible well-ordering $\prec_c$ on the monomial
basis $B$ of the Iwahori--Hecke algebra $H_n(q)$ of $A$.*

**Construction.**  The monomial basis $B$ of $H_n(q)$ consists
of reduced positive braid monomials
$w = \sigma_{i_1}\sigma_{i_2}\cdots\sigma_{i_k}$ —
the images of the braiding $c_{V,V}$ under
$\rho_n(\sigma_i) = \mathrm{id}^{\otimes(i-1)} \otimes c_{V,V} \otimes \mathrm{id}^{\otimes(n-i-1)}$
([braid action on tensor powers](#prop:braid-action-tensor)).
The braiding $c_{V,V}$ (as opposed to its inverse
$c_{V,V}^{-1}$) defines "positive crossing" — forward time.

*Definition.* A **well-ordering** on a set $S$ is a total
order $\prec$ such that every non-empty subset of $S$ has a
least element.  Equivalently: there are no infinite strictly
descending chains $s_1 \succ s_2 \succ s_3 \succ \cdots$.

*Definition.* The **degree-lexicographic ordering** $\prec_c$
on $B$ is: $w \prec_c w'$ if and only if

$$
  \ell(w) < \ell(w'),
  \quad\text{or}\quad
  \ell(w) = \ell(w')  \text{and}
  (i_1, \ldots, i_k) <_{\mathrm{lex}} (i_1', \ldots, i_k')
$$

where $\ell(w) = k$ is the word length (number of crossings)
and $<_{\mathrm{lex}}$ is lexicographic order on the generator
indices $i_j \in \{1, \ldots, n-1\}$.
