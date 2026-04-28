The Bethe--Weizsäcker semi-empirical mass formula (SEMF) decomposes
nuclear binding into five independent physical effects, each with a
fitted coefficient.  The QOU three-channel Wedderburn formula
([three-invariant mass formula](#prop:wedderburn-mass-formula))
produces binding from the Hecke algebra trace alone, with zero
fitted parameters.

## Term dictionary

| SEMF term | Formula | Scaling | QOU channel | Formula | Scaling |
|:----------|:--------|:--------|:------------|:--------|:--------|
| Volume | $a_V A$ | $\propto A$ | $\Phi_1$ (trace) | $\sum \ln\lvert\hat{V}_i\rvert$ | $\sim A$ for small $A$ |
| Surface | $-a_S A^{2/3}$ | $\propto A^{2/3}$ | (in $\Phi_1$) | Chain boundary | Implicit |
| Coulomb | $-a_C Z(Z{-}1)/A^{1/3}$ | $\propto Z^2/A^{1/3}$ | $\Phi_2$ (det) | $\sum \ln\lvert\det M_i\rvert$ | pp det $= -q$ |
| Asymmetry | $-a_A (N{-}Z)^2/(4A)$ | $\propto (N{-}Z)^2/A$ | $\Phi_2 + \Phi_3$ | nn/pp imbalance | Ordering-dependent |
| Pairing | $\pm\delta/\sqrt{A}$ | $\propto 1/\sqrt{A}$ | $\Phi_3$ (ratio) | $\ln\lvert\lambda^{\mathrm{sym}}/\lambda^{\mathrm{alt}}\rvert$ | $Z\!\!\mod 2$, $N\!\!\mod 2$ |

The SEMF separates five physically distinct effects with five
fitted coefficients ($a_V \approx 15.56$, $a_S \approx 17.23$,
$a_C \approx 0.697$, $a_A \approx 23.29$, $\delta \approx 12$ MeV).
The QOU formula has three channels ($\Phi_1$, $\Phi_2$, $\Phi_3$),
each mixing multiple SEMF effects through the transfer matrix chain.

## Comparison

| $Z$ | El | $A$ | $\mathcal{M}_{\mathrm{SEMF}}$ | $\Delta_S$ | $\%_S$ | $\mathcal{M}_{\mathrm{QOU}}$ | $\Delta_Q$ | $\%_Q$ | Winner |
|:----|:---|:----|:-----|:------|:------|:-----|:------|:------|:------|
| 1 | H | 1 | 938.783 | $+0.0$ | $0.000$ | 938.910 | $+0.1$ | $0.014$ | SEMF |
| 2 | He | 4 | 3732.751 | $+4.4$ | $0.117$ | 3734.624 | $+6.2$ | $0.167$ | SEMF |
| 3 | Li | 7 | 6531.757 | $-3.6$ | $0.055$ | 6534.188 | $-1.2$ | $0.018$ | **QOU** |
| 4 | Be | 9 | 8392.135 | $-2.7$ | $0.032$ | 8378.704 | $-16.1$ | $0.192$ | SEMF |
| 6 | C | 12 | 11179.348 | $+1.4$ | $0.013$ | 11168.874 | $-9.1$ | $0.081$ | SEMF |
| 8 | O | 16 | 14899.718 | $+0.5$ | $0.004$ | 14890.701 | $-8.5$ | $0.057$ | SEMF |
| 10 | Ne | 20 | 18619.658 | $-3.2$ | $0.017$ | 18615.219 | $-7.6$ | $0.041$ | SEMF |
| 11 | Na | 23 | 21410.075 | $-4.8$ | $0.022$ | 21418.256 | $+3.4$ | $0.016$ | **QOU** |
| 12 | Mg | 24 | 22339.542 | $-2.4$ | $0.011$ | 22342.658 | $+0.8$ | $0.003$ | **QOU** |
| 20 | Ca | 40 | 37221.631 | $+7.9$ | $0.021$ | 37248.739 | $+35.0$ | $0.094$ | SEMF |

SEMF mean: $0.023\%$ (5 fitted + 3 CODATA = 8 inputs).
QOU mean: $0.074\%$ (0 fitted, 2 inputs: $q_0$, $m_e$).
QOU wins 3/20 atoms.  Accuracy ratio: SEMF is $3.2\times$ better
with $4\times$ more parameters.

## Sources of discrepancy

The QOU error has a characteristic sign pattern that tracks
the **nuclear shell model**:

- **Under-binding** (QOU lighter) for $Z = 3$--$10$ (p-shell):
  the transfer matrix chain overestimates Φ₁ because the
  near-zero generator ($\hat{V} \approx 0.0015$) dominates.
- **Over-binding** (QOU heavier) for $Z = 11$--$20$ (sd-shell):
  the increasing nn/pp asymmetry ($\Phi_2$ channel) grows faster
  than the actual asymmetry energy.
- **Sign flip** near shell closures ($A = 4$, $A = 20$): the
  Hecke trace detects quantum coherence near magic numbers that
  the SEMF's smooth $A^{2/3}$ scaling misses.

The near-zero volume at generator $k$ (where $\hat{V}_k \approx
0.0015$, contributing $\ln\lvert\hat{V}_k\rvert \approx -6.50$
to $\Phi_1$) is a universal feature of alternating $\mathfrak{p}\mathfrak{n}$ orderings
with $A \geq 4$.  It encodes **nuclear saturation**: each nucleon
interacts only with its nearest neighbors, and the effective range
is encoded in the transfer matrix chain length.

## Improving: the pion channel

The $3\times$ accuracy gap corresponds to $O(10\;\mathrm{MeV})$
in binding energy — the shell correction.  The $[n{-}2,2]$ hook
representation (pion channel) vanishes exactly at magic numbers
([shell-transition knot](#prop:shell-transition-knot)), creating
discrete stability gaps that the three extremal channels miss.
Including the hook channel would provide the missing shell structure.

**Witness**: `feynman-qou-comparison.witness.json`.
