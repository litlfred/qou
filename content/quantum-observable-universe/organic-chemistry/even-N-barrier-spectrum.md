**Statement.**
The predicted ring-closure barriers
$\Delta E_{\mathrm{closure}}(N)$ for even $N \in \{4, 6, 8, 10, 12, 14\}$
follow a **monotone-increasing linear trend** in $N$:

$$
  \Delta E_{\mathrm{closure}}(N)
   = 
  C_{0} + C_{1}\,N
  \qquad\text{with}\qquad
  C_{1} = \tfrac{1}{2}\,\lvert q + q^{-1}\rvert_{\mathrm{mol}} > 0.
$$

The slope $C_{1}$ is determined by the threading half-weight
([threading half-weight](#prop:threading-half-weight)): each
additional pair of carbons adds half a crossing-energy unit to the
barrier, since the threading link's per-atom Alexander weight is
$\tfrac{1}{2}$ in the classical limit.

**Numerical fit.**
Least-squares linear fit to the predictions of
[ring closure barrier (quantitative)](#prop:ring-closure-barrier-quantitative)
gives slope $C_{1} \approx 9.84\ \mathrm{kJ/mol}$ per added carbon
and intercept $C_{0} \approx -15.5\ \mathrm{kJ/mol}$.  The slope
agrees with the half-weight prediction
$\tfrac{1}{2}\,\lvert q + q^{-1}\rvert_{\mathrm{mol}} \approx 11.2\ \mathrm{kJ/mol}$
to within $12\%$, the residual deviation being the
$\mathcal{O}((q-1)^{2})$ correction from $q_{0} \neq 1$.

**Falsifiability.**
The experimental closure / aromatisation barriers from the data
file are *approximately flat* or *weakly decreasing* in $N$:
$\{260, 290, 240, 220, 210, 200\}\ \mathrm{kJ/mol}$ for
$N = 4, 6, 8, 10, 12, 14$.  This sign-disagreement with the
predicted monotone-increasing trend is a key falsifier of the simple
single-Hopf-link energy model and indicates that additional
contributions — entropic, ring-strain, and Hückel-electronic — must
dominate beyond the topological barrier.  The witness records the
disagreement quantitatively for the chapter to address.
