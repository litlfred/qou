### Computation path (algebraic)

Each row is produced by purely algebraic steps, under the Kashaev
volume--density reading
([Kashaev volume--density](#rem:kashaev-volume-density)):

1. *Extract the braid $\beta_{Z, N}$* from the knot--particle dictionary
   (independent of $q$).
2. *Compute three Laurent polynomials*
   $\mathrm{Vol}_{q}^{(i)}(\beta_{Z, N}) \in \mathbb{Z}[q^{1/2},
   q^{-1/2}]$, $i = 1, 2, 3$, via the Markov trace product
   ([Markov trace product](#thm:markov-trace-product)) on the
   transfer-matrix chain at each Wedderburn branch
   ([algebraic quantum volume](#def:algebraic-quantum-volume)).
3. *Evaluate at* $q = q_{0}$ *and take* $\ln\lvert\cdot\rvert$.

The prediction column is the substitution of step 3 into the
three-invariant mass formula
([Wedderburn mass formula](#thm:wedderburn-mass-formula)).  No
continuous integration, no dilogarithm evaluation; the dependence on
$q_{0}$ is confined to step 3 alone.

| $Z$ | Element | $A$ | $\mathcal{M}_{\mathrm{pred}}$ (MeV) | $\mathcal{M}_{\mathrm{obs}}$ (MeV) | $\Delta$ (MeV) | $\Delta/\mathcal{M}$ |
|:----|:--------|:----|:-------------------------------------|:------------------------------------|:----------------|:---------------------|
| 1 | H | 1 | 938.910 | 938.783 | $+0.127$ | $+0.014\%$ |
| 2 | He | 4 | 3734.624 | 3728.401 | $+6.223$ | $+0.167\%$ |
| 3 | Li | 7 | 6534.188 | 6535.367 | $-1.179$ | $-0.018\%$ |
| 4 | Be | 9 | 8378.704 | 8394.794 | $-16.090$ | $-0.192\%$ |
| 5 | B | 11 | 10237.301 | 10255.103 | $-17.802$ | $-0.174\%$ |
| 6 | C | 12 | 11168.874 | 11177.929 | $-9.056$ | $-0.081\%$ |
| 7 | N | 14 | 13029.983 | 13043.782 | $-13.799$ | $-0.106\%$ |
| 8 | O | 16 | 14890.701 | 14899.169 | $-8.468$ | $-0.057\%$ |
| 9 | F | 19 | 17690.792 | 17696.901 | $-6.109$ | $-0.035\%$ |
| 10 | Ne | 20 | 18615.219 | 18622.835 | $-7.617$ | $-0.041\%$ |
| 11 | Na | 23 | 21418.256 | 21414.830 | $+3.425$ | $+0.016\%$ |
| 12 | Mg | 24 | 22342.658 | 22341.908 | $+0.750$ | $+0.003\%$ |
| 13 | Al | 27 | 25143.149 | 25133.143 | $+10.005$ | $+0.040\%$ |
| 14 | Si | 28 | 26067.918 | 26060.344 | $+7.574$ | $+0.029\%$ |
| 15 | P | 31 | 28872.696 | 28851.873 | $+20.823$ | $+0.072\%$ |
| 16 | S | 32 | 29797.187 | 29781.800 | $+15.387$ | $+0.052\%$ |
| 17 | Cl | 35 | 32597.913 | 32573.283 | $+24.630$ | $+0.076\%$ |
| 18 | Ar | 40 | 37273.796 | 37224.719 | $+49.077$ | $+0.132\%$ |
| 19 | K | 39 | 36324.625 | 36294.464 | $+30.161$ | $+0.083\%$ |
| 20 | Ca | 40 | 37248.739 | 37213.777 | $+34.962$ | $+0.094\%$ |

Mean: $0.074\%$.  Maximum: $0.192\%$.  Zero fitted parameters.

**Witness**: `atom-mass-complete-wedderburn.witness.json`.
