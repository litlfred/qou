Every fundamental particle in the knot--particle dictionary
([Knot--particle dictionary](#rem:knot-particle-dictionary))
has a unique Gröbner normal form in the Iwahori--Hecke algebra
$H_3(q)$ with $q = q_0 = 1.109978595554181\ldots$ (50 dps).

The **basis** of $H_3(q)$ in normal form is
$\{\ \mathbf{1},\ \sigma_0,\ \sigma_1,\ \sigma_0\sigma_1,\
\sigma_1\sigma_0,\ \sigma_0\sigma_1\sigma_0\ \}$,
which correspond to the particle content
$\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}$.

**Table K.1: Fundamental particle NF decomposition.**

| Particle | Knot | Hecke word | $\gamma$ | $\sigma_0$ | $\sigma_1$ | $L_+$ | $L_-$ | $e^-$ | net |
|----------|------|-----------|------:|------:|------:|------:|------:|------:|----:|
| $\nu$ | unknot $0_1$ | $\mathbf{1}$ | $+1$ | — | — | — | — | — | $+1.000$ |
| $\gamma$ | point $\varnothing$ | $\mathbf{1}$ | $+1$ | — | — | — | — | — | $+1.000$ |
| $\sigma_0$ | virtual | $\sigma_0$ | — | $+1$ | — | — | — | — | $+1.000$ |
| $\sigma_1$ | virtual | $\sigma_1$ | — | — | $+1$ | — | — | — | $+1.000$ |
| $L_+$ (gluon) | Hopf $T(2,2)$ | $\sigma_0\sigma_1$ | — | — | — | $+1$ | — | — | $+1.000$ |
| $L_-$ (gluon) | Hopf $T(2,2)$ | $\sigma_1\sigma_0$ | — | — | — | — | $+1$ | — | $+1.000$ |
| $e^-$ | trefoil $3_1$ | $\sigma_0\sigma_1\sigma_0$ | — | — | — | — | — | $+1$ | $+1.000$ |
| $e^+$ | mirror $3_1$ | $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ | $-0.218$ | $+0.044$ | $+0.044$ | $-0.209$ | $-0.209$ | $+1$ | $+0.451$ |
| $\mathfrak{u}$ | unknot $(+)$ | $\sigma_0$ | — | $+1$ | — | — | — | — | $+1.000$ |
| $\mathfrak{d}$ | unknot $(-)$ | $\sigma_0^{-1}$ | $-0.209$ | $+1$ | — | — | — | — | $+0.791$ |

**Quark knot type** ([Borromean baryon](#def:borromean-baryon)).
Quarks are **unknots** $K_{0_1}$ Borromean-linked in the
exceptional divisor.  The up/down flavour arises from the
**crossing orientation** of each unknot within $\mathcal{B}_3$:
$\mathfrak{u} = \sigma$ (positive), $\mathfrak{d} = \sigma^{-1}$
(negative).  Table 4 of the
[dictionary](#rem:knot-particle-dictionary) lists the *lepton
partner* from which each quark descends on the exceptional
divisor ($\mathfrak{u} \leftarrow T_{2,3}$,
$\mathfrak{d} \leftarrow T_{2,3}^{\sigma}$), not the quark's
own knot type.

**Key observations:**

1. **Up quark** $\mathfrak{u} = \sigma_0$ (positive crossing
   orientation within $\mathcal{B}_3$).  Same Hecke word as
   $\sigma_0$; the quark is distinguished by its Borromean
   environment, not its Hecke algebra element.

2. **Down quark** $\mathfrak{d} = \sigma_0^{-1} = \sigma_0 -
   (q - q^{-1})\mathbf{1}$.  The negative crossing orientation
   bleeds $-\mathrm{HA} \approx -0.209$ into the $\gamma$ (identity)
   channel.  This leakage is the origin of the $\mathfrak{d}$--$\mathfrak{u}$
   mass splitting.

3. **Positron** $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$
   contains all six basis elements.  The net $\approx 0.451$ is
   the mirror-trefoil's Jones polynomial at $q_0$.

4. **Gluon** $L_{\pm}$ is already a basis element of $H_3(q)$.
   The Borromean braid $B_3 = (\sigma_0\sigma_1^{-1})^3$ contains
   both $L_+$ and $L_-$ in its NF, confirming that the gluon
   field is encoded in the Borromean structure.  This is the
   Hopf link $\mathcal{L}_H$ from [Definition](#def:borromean-baryon):
   $B = \mathcal{B}_3 \bowtie \mathcal{L}_H$.

5. **Hopf self-link** $\sigma_i^2 = \mathrm{HA}\cdot\sigma_i +
   \mathbf{1}$.  This is the Hecke relation itself — squaring
   any crossing yields the identity (photon) plus a
   HA-weighted crossing.

6. **Trefoil vs unknot test.**  Using full trefoil words
   $\sigma_0\sigma_1\sigma_0$ as quark crossings (Model T)
   gives $\Delta \times E_0 = -2.51$ MeV, overshooting
   CODATA by $3\times$.  Single-crossing unknots (Model S)
   give $\Delta \times E_0 = -0.782$ MeV, matching CODATA
   exactly (witness: `trefoil-quark-nucleon-nf.witness.json`).
