**Statement.**
The molecular crossing-energy quantum $\lvert q + q^{-1}\rvert_{\mathrm{mol}}$ is related to the nuclear quantum
$\lvert q + q^{-1}\rvert_{\mathrm{nuc}}$ by the dimensionless
electronic-to-nuclear scale-separation factor

$$
  \lvert q + q^{-1}\rvert_{\mathrm{mol}}
   = 
  \alpha^{2}\,\frac{m_{e}}{m_{p}}\,
  \lvert q + q^{-1}\rvert_{\mathrm{nuc}}.
$$

**Numerical evaluation.**
With CODATA 2018 values
$\alpha = 7.2973525693 \times 10^{-3}$,
$m_{e}/m_{p} = 5.4461702151 \times 10^{-4}$,
and the manuscript's nuclear quantum
$\lvert q + q^{-1}\rvert_{\mathrm{nuc}} \approx 8\ \mathrm{MeV}$,
the scale-separation factor is

$$
  \alpha^{2}\,\frac{m_{e}}{m_{p}}
   \approx 
  2.90 \times 10^{-8},
$$

yielding

$$
  \lvert q + q^{-1}\rvert_{\mathrm{mol}}
   \approx 
  0.232\ \mathrm{eV}
   \approx 
  22.4\ \mathrm{kJ/mol}
   \approx 
  5.35\ \mathrm{kcal/mol}.
$$

**Remark.**
This computed value lies **below** the order-of-magnitude estimate
of $1\text{--}2\ \mathrm{eV}$ asserted in
[chain-ring comparison](#prop:chain-ring-comparison).  Two
explanations are consistent with the present data:

1. The nuclear quantum
   $\lvert q + q^{-1}\rvert_{\mathrm{nuc}}$ used in the order-of-magnitude
   estimate may be larger than $8\ \mathrm{MeV}$ — a value of
   $\sim 35\text{--}70\ \mathrm{MeV}$ would reproduce the manuscript
   range.  This question is downstream of the Skein-binding
   Lagrangian computation in the observations chapter.

2. An additional multiplicative factor — for example, an Alexander-weight
   ratio carrying the bond-order information — may multiply the
   scale-separation formula at the molecular level.

The witness `crossing-energy-mol.witness.json` records the formula
verification and the residual numerical discrepancy.
