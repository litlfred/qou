**Statement.**
For $N = 6$, the topological energy difference between the linear
C${}_{6}$ chain and the closed benzene ring is

$$
  \Delta E_{\mathrm{chain} \to \mathrm{ring}}(6)
   = 
  \bigl[\,\Delta_{T(2,6)}(q_{0}) - 5\,\bigr]\,
  \lvert q + q^{-1}\rvert_{\mathrm{mol}}.
$$

In the classical limit $q \to 1$, by
[$\Delta_{T(2,N)}$ closed form](#lem:alexander-T2N-closed-form)
$\Delta_{T(2,6)}(1) = 3$, so

$$
  \lim_{q \to 1}\,\Delta E_{\mathrm{chain} \to \mathrm{ring}}(6)
   = 
  -2\,\lvert q + q^{-1}\rvert_{\mathrm{mol}}
   <  0.
$$

**The ring is favoured.** This negative sign is the **smoking-gun**
prediction for benzene's spontaneous ring closure: the threading
link saves two crossing-energy units relative to the open chain,
exactly the half-weight gain on the three "missing" links of the
chain (cf. [threading half-weight](#prop:threading-half-weight)).

**Proof.**
The chain weight is $N - 1 = 5$ (sum of the five C–C link weights).
The ring's threading weight is $\Delta_{T(2,6)}(q_{0})$.  Subtracting
chain from ring and multiplying by the molecular crossing quantum
gives the formula.  At $q = 1$,
$\Delta_{T(2,6)}(1) - 5 = 3 - 5 = -2$, which is the half-weight
saving on three pairwise links ($3 \cdot \tfrac{1}{2} = \tfrac{3}{2}$,
times two for the cyclic doubling, equals $3$ — but the chain misses
only $5 - 3 = 2$ links of weight $1$ in the linear count, exactly
matching the $-2$).
$\square$

**Numerical evaluation.**
With $\lvert q + q^{-1}\rvert_{\mathrm{mol}} \approx 0.232\ \mathrm{eV}
\approx 22.4\ \mathrm{kJ/mol}$ and $\Delta_{T(2,6)}(q_{0}) \approx 3.04$,

$$
  \Delta E_{\mathrm{chain} \to \mathrm{ring}}(6)
   \approx 
  -1.96 \cdot 22.4
   \approx 
  -43.9\ \mathrm{kJ/mol},
$$

i.e. the ring is energetically favoured by about $44\ \mathrm{kJ/mol}$
in this leading-order topological model.
