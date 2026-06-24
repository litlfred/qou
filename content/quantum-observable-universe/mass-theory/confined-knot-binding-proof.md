The equality $W_{\mathrm{sym}} = W_{\mathrm{alt}}$ follows from
$\dim_q(\lambda_{\mathrm{sym}}) = \dim_q(\lambda_{\mathrm{alt}}) = 1$
for the one-dimensional representations of $H_3(R, q)$.
The Wedderburn weight is $w_\lambda = d_q(\lambda)^2 / [n]_q!$,
and $d_q((3)) = d_q((1,1,1)) = 1$.

For the symmetric crossing $(c, d) = (1, -H_A/2)$:

$$
  \chi_{\mathrm{sym}} + \chi_{\mathrm{alt}}
  = (q - H_A/2) + (-q^{-1} - H_A/2)
  = q - q^{-1} - H_A = 0
$$

since $H_A = q - q^{-1}$.  Therefore the weighted sum vanishes:
$W_{\mathrm{sym}} \cdot \chi_{\mathrm{sym}}
+ W_{\mathrm{alt}} \cdot \chi_{\mathrm{alt}}
= W_{\mathrm{sym}}(\chi_{\mathrm{sym}} + \chi_{\mathrm{alt}}) = 0$.

The standard-representation volume $z - H_A/2$ follows from the
transfer matrix with initial condition $(a_0, b_0) = (0, 1)$:
$(a, b) = (1, -H_A/2)$, giving
$\chi_{\mathrm{std}} = z \cdot 1 + (-H_A/2) = z - H_A/2$.

For a general confined state at jet level $\ell$, the character
ratio $a_\ell$ compares the accumulated Wedderburn volume of
the confined braid word against the tensor product of free
constituent volumes.  The product $\prod_\ell a_\ell$ telescopes
through the jet tower:

$$
  \prod_\ell a_\ell
  = \frac{\hat{V}(\text{nucleus})}
         {\prod_{\text{nucleons}} \hat{V}(\text{nucleon})}
  \cdot
  \frac{\prod_{\text{nucleons}} \hat{V}(\text{nucleon})}
       {\prod_{\text{quarks}} \hat{V}(\text{quark})}
  \cdot \dotsb
$$

Each factor is determined by the Hecke algebra multiplication
rules applied to the crossing parameters at that level.
$\qquad\blacksquare$
