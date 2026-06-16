**Remark (archimedean shadow of the algebraic residue).** *This
remark records the **archimedean realisation** of the algebraic
residue formula on the principal Galois orbit
([sw-period thimble equivalence](#prop:sw-period-thimble-equivalence)
A2.4).  No formal claim is made here; the rigorous statement lives
in the cited proposition.  The Picard–Lefschetz picture is retained
because it (i) connects the QOU framework to a substantial
literature (\[pham1965], \[witten2011], \[seidel2008]) and (ii)
makes the algebraic residue's selection of the principal orbit
**visualisable** as a steepest-descent contour decomposition.*

Let $F(z, \mathbf{c}) = \mathbf{c}^3 + (4z+1)\mathbf{c}^2 +
(6z^2+3z+1)\mathbf{c} + (4z^3+3z^2+2z+1)$ denote the
([color-tube cubic](#rem:color-tube-cubic)), and let
$\lambda_{\mathrm{SW}}^{(k)}$ denote the Seiberg–Witten differential
at vertical degree $k$. After applying the archimedean fibre functor
$\tau$, the discriminant $\Delta(z) = -(16 z^6 + 24 z^5 + 35 z^4 +
50 z^3 + 35 z^2 + 24 z + 16) \in \mathbb{Z}[z]$ has six complex
roots forming three Galois orbits under
$\langle z\mapsto\bar z,\,z\mapsto 1/z\rangle$ (palindromy):

| Orbit | Representatives | $|z|$ |
|---|---|---|
| **Principal** | $z_c^\pm \approx 0.106 \pm 0.937i$ | $0.943$ (innermost) |
| Inverse | $1/z_c^\pm \approx 0.119 \pm 1.054i$ | $1.060$ |
| Unit | $w, \bar w \approx -0.975 \pm 0.223i$ | $1.000$ (on the unit circle) |

For each $z_c$, the *Picard–Lefschetz thimble*
$\mathcal{J}_{z_c}$ is the steepest-descent contour of
$\mathrm{Re}(S)$ emanating from $z_c$ along
$\hat u = e^{-i\arg H(z_c)/2}$ where
$H(z_c) = \partial^2 S/\partial z^2|_{z_c}$.  The witness
[`picard-lefschetz-thimble.witness.json`](https://github.com/litlfred/qou/blob/main/computations/picard-lefschetz-thimble.witness.json)
records the numerical values; substrate $m_p$ closure is the
algebraic statement, not a thimble integral
([`sw-period thimble equivalence`](#prop:sw-period-thimble-equivalence)).

**Why this is a remark, not a definition.**
*After the algebraic-residue swap, the thimble picture is no longer
required for any rigorous derivation in the paper.  Every claim
about masses, integration limits, and Morse walls is established
$R$-side over $\mathbb{Z}[q^{\pm 1/2}, \zeta_5]$.  The thimble
description survives as **exposition** — readers who know
Picard–Lefschetz / Fukaya–Seidel theory can recognise the
algebraic residue as the $\tau$-image of a thimble period.  Readers
who don't can skip this block without losing any formal content.*
