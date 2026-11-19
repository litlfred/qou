# Toroidal Harmonics and the $\Delta_\lambda$ Mass Gap

Bridging the mass calculation from the canonical base $m_{\text{can}}$ to the AME2020 experimental frontier requires resolving the $\Delta_\lambda$ normalization shift (the shell-filling fraction $c_\lambda$).

## The toroidal change of variables

The toroidal Legendre equation of half-integer degree $n - \tfrac12$,

$$
(1 - x^2)\, y'' - 2x\, y' + \left(n^2 - \tfrac14\right) y = 0,
$$

is carried by the substitution $x = \frac{1}{2w} - 1$ (equivalently $w = \frac{1}{2(x+1)}$), after multiplication by $4$, exactly onto the second-order equation

$$
4w^2(4w - 1)\, f'' + 16 w^2 f' + (4n^2 - 1) f = 0 .
$$

This is a change of variables and holds for every choice of what $w$ is later identified with; it is independent of any Markov-trace convention.

## Identifying $w$ with a Markov loop value (convention D)

Write $q = e^{\eta}$, so $\eta = \ln q$ and $[2]_q = q + q^{-1} = 2\cosh\eta$. The canonical Markov parameter is

$$
z(q) = \frac{q^3}{q^2 + 1} = \frac{q^2}{[2]_q} = \frac{e^{2\eta}}{2\cosh\eta},
$$

and the negative loop value is $z_-(q) = z(q) - (q - q^{-1}) = \frac{1}{q(q^2+1)}$. The bar involution $q \mapsto q^{-1}$ exchanges them, $z(q^{-1}) = z_-(q)$, so $z$ itself is not a function of $\cosh\eta$ and $w = z^2$ does **not** satisfy $\frac{1}{2w} - 1 = \cosh\eta$. At the aether modulus $q_0 \approx 1.10998$ one has $z^2 \approx 0.375387$, against $\frac{1}{2(\cosh\eta_0 + 1)} \approx 0.249321$; <!-- literal-source: closed-form evaluation of 1/(2*z_D^2) - 1 at q_0 --> the corresponding $x = \frac{1}{2z^2} - 1 \approx 0.331960$ is less than $1$, so it is not $\cosh$ of any real angle. The identification $w = z^2$ therefore has no toroidal reading.

The bar-invariant combination of the two loop values does have one:

$$
w = z\, z_- = \frac{1}{[2]_q^{\,2}} = \frac{1}{2(\cosh 2\eta + 1)}, \qquad x = \frac{1}{2w} - 1 = \cosh 2\eta .
$$

So under the canonical weight the toroidal coordinate is $\cosh 2\eta$, the full angle of $q$, rather than a half angle. At $q_0$: $\eta_0 = \ln q_0 \approx 0.104341$, $w = z z_- \approx 0.247298$, and $x = \cosh 2\eta_0 \approx 1.021853$.

Whether this $w$ is the variable of the generating function of the Markov-parameter recursion is **not established**: the recursion $4(n+1)a_{n+1} + 6n\,a_n + (2n-1)a_{n-1} = 0$ is written in the variable $q - 1$, which is a different quantity. The proposition establishes only the change of variables above; identifying $w$ with the $z$-recursion generating variable or interpreting $B_{\text{sym}}$ as a discrete shadow of a toroidal JSJ decomposition is conjectural. Evaluating $P_{n-1/2}^m$ over the SU(4) Plancherel measure is a *proposed* route to the $\Delta_\lambda$ normalization for heavy nuclei; that closure remains **open** (the $\Delta_\lambda$ gate — see the three-calibration discipline).

## An exploratory golden-ratio comparison (conjectural $\Delta_\lambda$ scale)

> **Exploratory comparison (distinct from a derivation or a $\Delta_\lambda$ closure).**
> The anchor below is the Fibonacci-anyon value $q = 1/\phi \approx 0.618$ rather than
> the aether modulus $q_0 \approx 1.110$. Nothing here determines
> $\Delta_\lambda$, which stays open under the three-calibration discipline.

<!-- literal-source: AME 2020 4He binding ratio B_AME/E_gate and Legendre ratios P_{-1/2}/P_{1/2} at x = 3/2 and cosh(2*eta_0) -->
The comparison target is the ${}^4\text{He}$ shell-filling fraction $c_\lambda^{\text{exp}} = B_{\text{AME}}/E_{\text{gate}} \approx 0.943503$, which contains the experimental binding and is therefore not an independent quantity. Under the convention-D identification $x = \cosh 2\eta$, the Fibonacci anchor $q = 1/\phi$ gives $x = \cosh(2\ln\phi) = \frac{3}{2}$ and

<!-- literal-source: closed-form Legendre function ratio P_{-1/2}(3/2)/P_{1/2}(3/2) = 0.804485 -->
$$
\frac{P_{-1/2}\left(\frac{3}{2}\right)}{P_{1/2}\left(\frac{3}{2}\right)} \approx 0.804485,
$$

<!-- literal-source: closed-form Legendre function ratio P_{-1/2}(cosh 2*eta_0)/P_{1/2}(cosh 2*eta_0) -->
which is $14.7\,\%$ below $c_\lambda^{\text{exp}}$. At the aether itself, $x = \cosh 2\eta_0$ gives $P_{-1/2}/P_{1/2} \approx 0.989206$, $4.8\,\%$ above it. Neither is a match. The earlier $0.1\,\%$ near-match at $x = \frac{\sqrt5}{2}$ arose only through the convention-C identification $x = \cosh\eta$ and does not survive under the canonical weight.
