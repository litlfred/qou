Let $\sigma$ be linear with $\sigma^2 = \mathrm{id}$. For any $x$,
$$
\mathrm{even}(x) + \mathrm{odd}(x) = (x + \sigma x) + (x - \sigma x) = 2x
$$
(`evenPart_add_oddPart`). When $2$ is invertible in $R$, $x$ is half the sum of its two parts; the identity itself needs no division. The even part is $\sigma$-fixed: $\sigma(x + \sigma x) = \sigma x + \sigma^2 x = x + \sigma x$ (`evenPart_fixed`). The odd part is $\sigma$-anti: $\sigma(x - \sigma x) = \sigma x - x = -(x - \sigma x)$ (`oddPart_anti`). $\qquad\blacksquare$
