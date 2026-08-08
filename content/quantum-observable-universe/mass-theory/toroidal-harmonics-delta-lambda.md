# Toroidal Harmonics and the $\Delta_\lambda$ Mass Gap

Bridging the mass calculation from the canonical base $m_{\text{can}}$ to the AME2020 experimental frontier requires resolving the $\Delta_\lambda$ normalization shift (the shell-filling fraction $c_\lambda$).

## The Toroidal JSJ Equivalence

The Markov parameter recursion $c_k$ drives the strong-force topological trace. It constitutes a discrete evaluation of the knot complement's toroidal structure.

Let $q = e^{-\eta}$. The Markov parameter

$$
  z(q) = \frac{\sqrt{q}}{1+q}, \qquad w = z^2 = \frac{1}{2(\cosh\eta + 1)},
$$

is equivalently parametrised by $w$. Under the change of variables $x = \cosh\eta = \frac{1}{2w} - 1$, the continuous Legendre differential equation for the Toroidal Harmonics of half-integer degree $n-1/2$:

$$ (1 - x^2) y'' - 2x y' + (n^2 - 1/4) y = 0 $$

reduces exactly to the polynomial generating function ODE of the $z$-recursion:

$$ 4w^2(4w - 1) f'' + 16w^2 f' + (4n^2 - 1) f = 0 $$

This explicit map establishes that the topological evaluation $B_{\text{sym}}$ is the discrete shadow of the Toroidal JSJ decomposition. Evaluating $P_{n-1/2}^m(\cosh\eta)$ over the SU(4) Plancherel measure is *proposed* as a candidate route to the $\Delta_\lambda$ normalization for heavy nuclei; that closure itself remains **open** (the $\Delta_\lambda$ gate — see the three-calibration discipline).

## An exploratory golden-ratio near-match ($\Delta_\lambda$ remains open)

> **Exploratory near-match — not a derivation, not a $\Delta_\lambda$ closure.**
> The evaluation below anchors on the Fibonacci-anyon value
> $q_0 = 1/\phi \approx 0.618$, which is **not** the substrate modulus
> $q_0 \approx 1.110$. It is a numerical coincidence at an unrelated anchor,
> not a parameter-free evaluation on the substrate, and it does **not** determine
> $\Delta_\lambda$, which stays open under the three-calibration discipline;
> six ansätze have failed. It is recorded as a candidate Bring/Fibonacci lead to
> be *derived or refuted*, not as a result.

The toroidal ratio $P_{-1/2}/P_{1/2}$ drives the scaling gap $c_\lambda$. At the
Fibonacci-anyon anchor $q_0 = 1/\phi = \frac{\sqrt{5}-1}{2}$ (the fivefold Bring
structure), the geometric coordinate is $\cosh \eta = \frac{\sqrt{5}}{2} \approx 1.1180$.

Evaluating the toroidal harmonics at this anchor yields

$$ c_\lambda^{\text{topological}} = \frac{P_{-1/2}\left(\frac{\sqrt{5}}{2}\right)}{P_{1/2}\left(\frac{\sqrt{5}}{2}\right)} \approx 0.944649. $$

This is numerically close to the empirical ${}^4\text{He}$ shell-filling fraction
$c_\lambda^{\text{exp}} \approx 0.943503$ ($\approx 0.1\%$) — but at an anchor
unrelated to the substrate $q_0$. Absent a derivation linking the Bring golden
ratio to the ${}^4\text{He}$ $\Delta_\lambda$ normalization (and an evaluation at
the actual substrate $q_0$), it is an exploratory coincidence, not a
parameter-free constant and not a closure of $\Delta_\lambda$.
