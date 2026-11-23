**Proposition (conditional on [Quarks as Borromean-linked unknots in the exceptional divisor](#conj:borromean-quark) — shell-structure eigenvalues from photon-electron transfer matrix).**
The **eigenvalues** of the photon-electron transfer matrix $T_{\gamma e}(q)$ determine the orbital shell structure of an atom. Shell $n$ corresponds to the $n$-th power $T_{\gamma e}^n$. The shell energies satisfy a **Chebyshev recurrence** in $q$.

## The characteristic polynomial

The photon-electron transfer matrix ([transfer matrix operator](#def:transfer-matrix-operator)) is $T_{\gamma e} = T_{pp}$:

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

This yields the eigenvalues:

$$
  \lambda_{\pm}(q)
  = 
  \frac{(q - q^{-1}) \pm \sqrt{(q - q^{-1})^2 + 4}}{2}
$$

The discriminant is a perfect square,
$(q-q^{-1})^2 + 4 = q^2 + 2 + q^{-2} = (q+q^{-1})^2$, so
$\sqrt{h^2+4} = [2]_q$, the Temperley–Lieb loop parameter, and the
eigenvalues are exact:

$$
  \lambda_\pm = \frac{h \pm [2]_q}{2}
  = \frac{(q-q^{-1}) \pm (q+q^{-1})}{2},
  \qquad
  \lambda_+ = q, \qquad \lambda_- = -q^{-1}.
$$

These are the Hecke generator's eigenvalues: $\lambda^2 = h\lambda + 1$,
i.e. $(\lambda-q)(\lambda+q^{-1}) = 0$, which identifies this operator as
$\sigma_i$.

**At the substrate parameter $q_0$:**

$$
  q - q^{-1} \approx 0.2091, \quad
  [2]_q \approx 2.010897, \quad
  \lambda_+ \approx 1.109979, \quad
  \lambda_- \approx -0.900918 .
$$

## Shell $n$ from the $n$-th power

Shell $n$ of an atom is the $n$-th power of the transfer matrix at the electron-nucleus junction. Each power corresponds to one **R-I move** (Reidemeister I). This adds one curl to the diagram of the electron's closure, increasing the writhe by $1$ without altering the link type. (In the backup model the closure is the trefoil; under the electron ruling ([electron](#def:electron-knot)) it is the Hopf link.)

Diagonalize $T_{\gamma e} = S \Lambda S^{-1}$:

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

The eigenvector matrix is:

$$
  S = 
  \begin{pmatrix}
    \lambda_+ & \lambda_- \\
    1 & 1
  \end{pmatrix}
$$

The entries of $T_{\gamma e}^n$ are:

$$
  (T^n)_{11}
  = 
  \frac{\lambda_+^{n+1} - \lambda_-^{n+1}}{\lambda_+ - \lambda_-},
  \qquad
  (T^n)_{21}
  = 
  \frac{\lambda_+^n - \lambda_-^n}{\lambda_+ - \lambda_-}
$$

These correspond to **Chebyshev polynomials of the second kind** in the variable $\frac{1}{2}(q - q^{-1})$:

$$
  (T^n)_{21} =  U_{n-1}\!\left(\tfrac{q - q^{-1}}{2}\right)
$$

## The traced volume at shell $n$

The Markov-traced volume at shell $n$ is:

$$
  \hat{V}(n, q)
  = 
  z \cdot (T^n)_{11} + (T^n)_{21}
  = 
  \frac{(z\lambda_+ + 1)\lambda_+^n - (z\lambda_- + 1)\lambda_-^n}
       {\lambda_+ - \lambda_-}
$$

where $z = q^{3}/(q^{2}+1)$ is the Markov parameter (**convention D**).

Define:

$$
  \alpha =  z\lambda_+ + 1, \qquad
  \beta =  z\lambda_- + 1
$$

This gives:

$$
  \hat{V}(n, q) = 
  \frac{\alpha \cdot \lambda_+^n - \beta \cdot \lambda_-^n}
       {\lambda_+ - \lambda_-}
$$

Since $|\lambda_+| > 1 > |\lambda_-|$, the dominant term for large $n$ becomes:

$$
  \hat{V}(n, q)  \sim 
  \frac{\alpha}{\lambda_+ - \lambda_-} \cdot \lambda_+^n
  \qquad (n \gg 1)
$$

The sub-dominant term $\beta \cdot \lambda_-^n = \beta \cdot (-1)^n / \lambda_+^n$ provides an **alternating correction** that decays exponentially.

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

The initial conditions are $\hat{V}(0, q) = 1$ (no crossings) and $\hat{V}(1, q) = z(q - q^{-1}) + 1$ (one crossing).
