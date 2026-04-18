**Remark.** Symbolic reduction of $\gamma^{(4)} \cdot \mathfrak{p}$
on the explicit proton quark word
$\mathfrak{p} = B_3 \cdot (\sigma_0 - \varepsilon_{12})
(\sigma_0 - \varepsilon_{13})(\sigma_1 - \varepsilon_{23})$
specialised to $(u,u,d)$ gives a clean signature in the $[e^-]$
channel:

$$
  [e^-]\bigl(\gamma^{(4)} \cdot \mathfrak{p}\bigr)
  =
  \underbrace{\tfrac{H_A^6}{4} + \tfrac{H_A^4}{4} - H_A^2}_{\text{proton baseline}}
  + \varphi_0\bigl(\tfrac{H_A^7}{4} + \tfrac{3H_A^5}{4}\bigr)
  + \varphi_1\bigl(-\tfrac{H_A^7}{4} - \tfrac{5H_A^5}{4} - \tfrac{3H_A^3}{2} + \tfrac{H_A}{2}\bigr)
  + \varphi_{01}\bigl(\tfrac{H_A^6}{4} + H_A^4 + \tfrac{5H_A^2}{4}\bigr).
$$

**Monotonicity of $\varphi_{01}$.** Every monomial in the
$\varphi_{01}$ coefficient is positive (and every monomial in the
$\varphi_0$ coefficient is non-negative), whereas the $\varphi_1$
coefficient changes sign with $H_A$.  In particular:

| $\varphi$-channel | $[e^-]$ coefficient sign | Physical meaning |
|:---:|:---:|:---|
| $\varphi_0$ (horizontal) | $\geq 0$ for $H_A \geq 0$ | Monotone, weak |
| $\varphi_1$ (vertical) | sign-flipping | Mode-mixing cancellation |
| $\varphi_{01}$ (Hopf) | $> 0$ for all $H_A > 0$ | **Strict monotone enhancement** |

The Hopf-dressing parameter $\varphi_{01}$ is therefore the unique
polarisation content of the photon that unambiguously deposits
positive $e^-$ amplitude — i.e.\ drives pair creation — at *any*
value of the substrate parameter.

**Testable prediction.** Two beams of real photons with identical
horizontal linear polarisation ($\varphi_0$ matched, $\varphi_1 = 0$)
but differing Hopf content $\varphi_{01}$ should produce pair-creation
yields that scale monotonically with $\varphi_{01}$.  Experimentally,
the Hopf content is encoded in the relative phase between the two
Jones-vector components that generates a twisted wavefront: vortex
beams (Laguerre--Gauss, orbital-angular-momentum modes) carry
non-trivial $\varphi_{01}$, while purely linearly polarised
plane-wave photons have $\varphi_{01} = 0$.  The QOU prediction is
an excess pair-creation rate in OAM-mode photon--photon collisions
over plane-wave collisions at the same energy.

**Contrast with Breit--Wheeler cosine anisotropy.** The STAR and
ATLAS $\cos(2\phi)$ modulation
([rem:breit-wheeler-observation](#rem:breit-wheeler-observation))
probes the $\varphi_0 \leftrightarrow \varphi_1$ asymmetry
($\varphi_{01} = 0$ regime).  The prediction here is a *distinct*
effect — not modulation but an absolute yield enhancement — in the
previously-unprobed $\varphi_{01}$ channel.

**Witness:** `gamma4-hits-proton-quark-words.py`.
