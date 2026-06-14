Let $\sigma$ be the bar-involution ([`def:bar-involution`](#def:bar-involution)),
a linear map with $\sigma^2 = \mathrm{id}$. For any $x$,
$$
\mathrm{even}(x) + \mathrm{odd}(x) = (x + \sigma x) + (x - \sigma x) = 2x,
$$
thus the two parities sum to $2x$ (`evenPart_add_oddPart`); when $2$ is invertible
in the coefficient ring (characteristic $\neq 2$), $x$ is half their sum — but
the decomposition itself needs no division. The even part is
$\sigma$-fixed: $\sigma(x + \sigma x) = \sigma x + \sigma^2 x = \sigma x + x =
x + \sigma x$ (`evenPart_fixed`, using $\sigma^2=\mathrm{id}$ and additivity).
The odd part is $\sigma$-anti: $\sigma(x - \sigma x) = \sigma x - x =
-(x - \sigma x)$ (`oddPart_anti`). Hence the bar-even subspace ($\cosh$,
$(q+q^{-1})/2$) and the bar-odd subspace ($\sinh$, $(q-q^{-1})/2$) are
complementary, and any fibre element decomposes uniquely across them. The
binding trace $\tau$ lives in the even subspace and the $Q_\beta$ residue in
the odd subspace, so both are determined by the single element they jointly
span. $\qquad\blacksquare$
