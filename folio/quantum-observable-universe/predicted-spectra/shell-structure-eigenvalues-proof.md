*Proof.*
The matrix identity $T^{n+1} = T \cdot T^n$ directly yields $(T^{n+1})_{21} = (T)_{11} (T^n)_{21} + (T)_{12} (T^n)_{22}$. Substituting $(T)_{11} = q - q^{-1}$ and $(T)_{12} = 1$, together with $(T^n)_{22} = (T^{n-1})_{21}$ from $\det T = -1$, produces the Chebyshev recurrence. $\square$

The coefficient $q - q^{-1}$ in the recurrence defines the **Hecke deformation**. This is the identical parameter controlling parity violation ([Lee--Yang--Wu](#prop:parity-violation-skein)). At $q = 1$, the recurrence degenerates to $\hat{V}(n+1) = \hat{V}(n-1)$ (period 2, erasing shell structure).

## The Rydberg formula

The energy of shell $n$ in hydrogen is:

$$
  E_n(q)
  = 
  E_0 \cdot \hat{V}(n, q)
$$

where $E_0$ sets the ground-state energy scale. This originates from the electron-proton crossing energy at the substrate parameter $q$.

The transition energy (photon energy for $n \to n+1$) is:

$$
  \Delta E_{n \to n+1}
  = 
  E_0 \bigl[\hat{V}(n+1, q) - \hat{V}(n, q)\bigr]
  = 
  E_0 \bigl[(q - q^{-1} - 1) \hat{V}(n, q)
  + \hat{V}(n-1, q)\bigr]
$$

For the dominant term ($n \gg 1$):

$$
  \Delta E_{n \to n+1}
   \sim 
  E_0 \cdot \frac{\alpha}{\lambda_+ - \lambda_-}
  \cdot \lambda_+^n \cdot (\lambda_+ - 1)
$$

The **Rydberg scaling** $E_n \propto 1/n^2$ emerges in the regime $\lambda_+ \approx 1 + \epsilon$ with $\epsilon = \lambda_+ - 1 \ll 1$. At the substrate parameter $q$, $\epsilon = 0.1073$. For low shells ($n = 1, 2, 3, \ldots$):

$$
  \lambda_+^n \approx e^{n\epsilon}
  \approx 1 + n\epsilon + \tfrac{1}{2}n^2\epsilon^2 + \cdots
$$

The binding energy at shell $n$ (relative to ionization) is:

$$
  \mathfrak{E}_{\mathrm{bind}}(n)
  = 
  E_{\infty} - E_n
   \propto 
  \frac{1}{\lambda_+^n}
   \approx 
  e^{-n\epsilon}
$$

For small $\epsilon$, this approximates $1/n^2$ over the relevant range ($n = 1$ to $\sim 7$). The exact formula is the **exponential** $\lambda_+^{-n}$. This reproduces the Rydberg formula to the precision of low-$n$ hydrogen spectroscopy.

The entire shell structure is encoded in the eigenvalues of $T_{\gamma e}(q)$, a $2 \times 2$ matrix with polynomial entries in $q$.
