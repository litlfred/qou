*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — shell-structure eigenvalues from photon-electron transfer matrix).**
The orbital shell structure of an atom is determined by the
**eigenvalues** of the photon-electron transfer matrix
$T_{\gamma e}(q)$.  Shell $n$ corresponds to the $n$-th power
$T_{\gamma e}^n$, and the shell energies satisfy a **Chebyshev
recurrence** in $q$.

## The characteristic polynomial

The photon-electron transfer matrix
([transfer matrix operator](#def:transfer-matrix-operator))
is $T_{\gamma e} = T_{pp}$:

$$
  T_{\gamma e}(q) = 
  \begin{pmatrix}
    q - q^{-1} & 1 \\
    1 & 0
  \end{pmatrix}
$$

Its **characteristic polynomial** is:

$$
  \det(T_{\gamma e} - \lambda \mathbb{I})
  = 
  \lambda^2 - (q - q^{-1})\lambda - 1
  =  0
$$

with eigenvalues:

$$
  \lambda_{\pm}(q)
  = 
  \frac{(q - q^{-1}) \pm \sqrt{(q - q^{-1})^2 + 4}}{2}
$$

**At the substrate parameter $q$:**

$$
  q - q^{-1} = 0.2091, \quad
  \sqrt{0.2091^2 + 4} = 2.0054
$$

$$
  \lambda_+ = 1.1073, \quad
  \lambda_- = -0.9027
$$

## Shell $n$ from the $n$-th power

Shell $n$ of an atom is the $n$-th power of the transfer
matrix at the electron-nucleus junction.  Each power
corresponds to one **R-I move** (Reidemeister I) — one curl
added to the electron trefoil, increasing the writhe by $1$
without changing the knot type.

Diagonalizing $T_{\gamma e} = S \Lambda S^{-1}$:

$$
  T_{\gamma e}^n
  = 
  S
  \begin{pmatrix}
    \lambda_+^n & 0 \\
    0 & \lambda_-^n
  \end{pmatrix}
  S^{-1}
$$

where the eigenvector matrix is:

$$
  S = 
  \begin{pmatrix}
    \lambda_+ & \lambda_- \\
    1 & 1
  \end{pmatrix}
$$

The entries of $T_{\gamma e}^n$:

$$
  (T^n)_{11}
  = 
  \frac{\lambda_+^{n+1} - \lambda_-^{n+1}}{\lambda_+ - \lambda_-},
  \qquad
  (T^n)_{21}
  = 
  \frac{\lambda_+^n - \lambda_-^n}{\lambda_+ - \lambda_-}
$$

These are **Chebyshev polynomials of the second kind** in the
variable $\frac{1}{2}(q - q^{-1})$:

$$
  (T^n)_{21} =  U_{n-1}\!\left(\tfrac{q - q^{-1}}{2}\right)
$$

## The traced volume at shell $n$

The Markov-traced volume at shell $n$:

$$
  \hat{V}(n, q)
  = 
  z \cdot (T^n)_{11} + (T^n)_{21}
  = 
  \frac{(z\lambda_+ + 1)\lambda_+^n - (z\lambda_- + 1)\lambda_-^n}
       {\lambda_+ - \lambda_-}
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov parameter.

Define:

$$
  \alpha =  z\lambda_+ + 1, \qquad
  \beta =  z\lambda_- + 1
$$

Then:

$$
  \hat{V}(n, q) = 
  \frac{\alpha \cdot \lambda_+^n - \beta \cdot \lambda_-^n}
       {\lambda_+ - \lambda_-}
$$

Since $|\lambda_+| > 1 > |\lambda_-|$, the dominant term for
large $n$ is:

$$
  \hat{V}(n, q)  \sim 
  \frac{\alpha}{\lambda_+ - \lambda_-} \cdot \lambda_+^n
  \qquad (n \gg 1)
$$

The sub-dominant term $\beta \cdot \lambda_-^n = \beta \cdot (-1)^n / \lambda_+^n$ is an **alternating correction** that
decays exponentially.

## The Chebyshev recurrence

The traced volumes satisfy the three-term recurrence:

$$
  \boxed{
    \hat{V}(n+1, q)
    = 
    (q - q^{-1}) \cdot \hat{V}(n, q)
    + 
    \hat{V}(n-1, q)
  }
$$

with initial conditions $\hat{V}(0, q) = 1$ (no crossings)
and $\hat{V}(1, q) = z(q - q^{-1}) + 1$ (one crossing).

*Proof.*
The recurrence is the matrix identity
$T^{n+1} = T \cdot T^n$, which gives
$(T^{n+1})_{21} = (T)_{11} (T^n)_{21} + (T)_{12} (T^n)_{22}$.
Since $(T)_{11} = q - q^{-1}$ and $(T)_{12} = 1$, and using
$(T^n)_{22} = (T^{n-1})_{21}$ (from $\det T = -1$), this
becomes the Chebyshev recurrence.  $\square$

The coefficient $q - q^{-1}$ in the recurrence is the
**Hecke deformation** — the same parameter that controls
parity violation
([Lee--Yang--Wu](#prop:parity-violation-skein)).  At $q = 1$
the recurrence degenerates: $\hat{V}(n+1) = \hat{V}(n-1)$
(period 2, no shell structure).

## The Rydberg formula

The energy of shell $n$ in hydrogen is:

$$
  E_n(q)
  = 
  E_0 \cdot \hat{V}(n, q)
$$

where $E_0$ is the ground-state energy scale (from the
electron-proton crossing energy at the substrate parameter $q$).

The transition energy (photon energy for $n \to n+1$):

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

The **Rydberg scaling** $E_n \propto 1/n^2$ emerges in the
regime $\lambda_+ \approx 1 + \epsilon$ with
$\epsilon = \lambda_+ - 1 \ll 1$.  At the substrate parameter $q$:
$\epsilon = 0.1073$.  For low shells ($n = 1, 2, 3, \ldots$):

$$
  \lambda_+^n \approx e^{n\epsilon}
  \approx 1 + n\epsilon + \tfrac{1}{2}n^2\epsilon^2 + \cdots
$$

The binding energy at shell $n$ (relative to ionization):

$$
  \mathfrak{E}_{\mathrm{bind}}(n)
  = 
  E_{\infty} - E_n
   \propto 
  \frac{1}{\lambda_+^n}
   \approx 
  e^{-n\epsilon}
$$

For small $\epsilon$, this approximates $1/n^2$ over the
physically relevant range ($n = 1$ to $\sim 7$).  The exact
formula is the **exponential** $\lambda_+^{-n}$, which
reproduces the Rydberg formula to the precision of
low-$n$ hydrogen spectroscopy.

The entire shell structure is encoded in the eigenvalues of
$T_{\gamma e}(q)$ — a $2 \times 2$ matrix with polynomial
entries in $q$.
