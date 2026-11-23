A **meson** is a valence-2 [hadron](#def:hadron): a quark--antiquark pair bound by the Hopf link $\mathcal{L}_H$. One forms the meson from two independent [quark--antiquark productions](#def:quark-antiquark-production), pairing a quark from one with an antiquark from the other:

$$
  \mathfrak{M}
  = 
  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

where:

- $T_{01} = \sigma_0\sigma_1 = L_+$ is the up-type crossing pair ([knot notation](#sec:knot-notation-convention)); its closure in $B_3$ is the unknot.
- $T_{10} = \sigma_1\sigma_0 = L_-$ is the down-type crossing pair.
- $\mathcal{L}_H = \sigma_0\sigma_1$ binds the two constituents.

The full braid word is $(\sigma_0\sigma_1)^2 \cdot \sigma_1\sigma_0$, containing 6 crossings on 3 strands.

**Normal form (step-by-step Hecke reduction).**
One writes $h = h_{\mathrm{A}} = q - q^{-1}$ and applies the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$ and the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$.

*Step 1.* For the bound pair $T_{01} \cdot \mathcal{L}_H = (\sigma_0\sigma_1)^2 = \sigma_0\sigma_1\sigma_0\sigma_1$, one applies the braid relation to the rightmost three generators to yield $\sigma_0 \cdot \sigma_0\sigma_1\sigma_0 = \sigma_0^2 \cdot L_-$. The Hecke relation reduces this to:

$$
  (\sigma_0\sigma_1)^2 = h \cdot e^- + L_-
$$

*Step 2.* One multiplies by $T_{10} = \sigma_1\sigma_0$:

| Factor | Product | Hecke reduction |
|:---|:---|:---|
| $L_- \cdot L_-$ | $\sigma_1\sigma_0\sigma_1\sigma_0$ | braid + Hecke: $h \cdot e^- + L_+$ |
| $e^- \cdot L_-$ | $\sigma_0\sigma_1\sigma_0 \cdot \sigma_1\sigma_0$ | two braid + Hecke steps: $h^2 e^- + hL_+ + hL_- + \sigma_1$ |

Collecting terms yields the exact normal form:

$$
  \mathfrak{M}_+ =
  \underbrace{h}_{\sigma_1}\sigma_1 + \underbrace{(h^2 + 1)}_{L_+}\sigma_0\sigma_1 + \underbrace{h^2}_{L_-}\sigma_1\sigma_0 + \underbrace{(h^3 + h)}_{e^-}\sigma_0\sigma_1\sigma_0
$$

At the CODATA root $q_0 \approx 1.1100$ ($h \approx 0.2091$):

$$
  \mathrm{NF}(\mathfrak{M}_+) \approx 0.209\,\sigma_1 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

yielding $\mathrm{net}(\mathfrak{M}_+) \approx +1.515$.

The mirror meson $\mathfrak{M}_- = T_{10} \cdot \mathcal{L}_H \cdot T_{01}$ maintains identical net amplitude but exchanges $\sigma_1$ for $\sigma_0$:

$$
  \mathrm{NF}(\mathfrak{M}_-) \approx 0.209\,\sigma_0 + 1.044\,L_+ + 0.044\,L_- + 0.218\,e^-
$$

Both mesons carry identical $L_\pm$ ($L_+ + L_-$) and $e^-$ content, differing only in the single-generator excitation.

**Particle content.**
The dominant $L_+$ term (coefficient $\approx 1.044$) establishes the binding. The $e^-$ component ($\approx 0.218$) encodes the residual lepton channel. In contrast, the bare quark--antiquark pair ($T_{01} \cdot T_{10}$) yields $\mathrm{net} = +1.418$ and contains a neutrino $\nu$ component in place of the Hopf links. The Hopf link binding actively replaces the neutrino channel and increases the net amplitude by $\approx 0.097$.
