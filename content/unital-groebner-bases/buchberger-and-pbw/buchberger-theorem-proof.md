We show that if all S-polynomials reduce to zero and $f \in I$, then $f$
has a Gröbner--Shirshov basis representation. Since $G$ generates $I$, choose:

$$f = \sum_i h_i \cdot g_{\gamma_i} \cdot h'_i$$

Expanding in the basis $B$, if for some representation we have
$\LM(\beta_k \cdot g_i \cdot \beta'_{k'}) \leq \LM(f)$ for all terms, we are done.
Otherwise, let $\alpha := \max\{\LM(h_i \cdot g_i \cdot h'_i)\} > \LM(f)$ be
minimal over all representations. Applying
[Proposition 7](#prop:ugb-s-poly-decomposition) to the terms with leading
monomial $\alpha$, we write their sum in terms of S-polynomials. By hypothesis,
these reduce to zero, giving a representation with strictly smaller maximal
term — a contradiction.
$\qquad\blacksquare$
