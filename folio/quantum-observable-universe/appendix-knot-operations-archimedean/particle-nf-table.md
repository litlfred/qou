A particle's Gröbner normal form can be read as an occupancy pattern
over the six basis channels of $H_3(q)$, and that pattern is what
exposes its flavour and mass structure — the
$\mathfrak{d}$--$\mathfrak{u}$ splitting (observation 2 below) shows up
precisely as leakage into the identity channel.  With that reading in
view:

Every fundamental particle in the knot--particle dictionary
([Knot--particle dictionary](#rem:knot-particle-dictionary))
has a unique Gröbner normal form in the Iwahori--Hecke algebra
$H_3(q)$ with $q = q_0 = 1.109978595642739\ldots$ (muon pin, 16 dps).

The **basis** of $H_3(q)$ in normal form is
$\{\ \mathbf{1},\ \sigma_0,\ \sigma_1,\ \sigma_0\sigma_1,\
\sigma_1\sigma_0,\ \sigma_0\sigma_1\sigma_0\ \}$,
which correspond to the particle content
$\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}$.

**Table K.1: Fundamental particle NF decomposition.**

See [Table](#tbl:particle-nf-table-table-data).

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
   bleeds the Hecke amplitude $-h_{\mathrm{A}} \approx -0.209$ (with
   $h_{\mathrm{A}} = q - q^{-1}$) into the $\gamma$ (identity)
   channel.  This leakage is the origin of the $\mathfrak{d}$--$\mathfrak{u}$
   mass splitting.

3. **Positron** $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$
   contains all six basis elements.  The net $\approx 0.451$ is
   the mirror-trefoil's Jones polynomial at $q_0$.

4. **Gluon** $L_{\pm}$ is already a basis element of $H_3(q)$.
   The Borromean braid $B_3 = (\sigma_0\sigma_1^{-1})^3$ contains
   both $L_+$ and $L_-$ in its NF.  This is the
   Hopf link $\mathcal{L}_H$ from [Definition](#def:borromean-baryon):
   $B = \mathcal{B}_3 \oplus \mathcal{L}_H$.

5. **Hopf self-link** $\sigma_i^2 = h_{\mathrm{A}}\cdot\sigma_i +
   \mathbf{1}$.  This is the Hecke relation itself — squaring
   any crossing yields the identity (photon) plus an
   $h_{\mathrm{A}}$-weighted crossing.

6. **Single-crossing unknot quarks.**  Each quark enters as a
   single-crossing unknot rather than the full three-crossing word
   $\sigma_0\sigma_1\sigma_0$: that assignment triples
   $|\Delta \times E_0|$ to $-2.51$ MeV, whereas the
   single-crossing assignment gives $\Delta \times E_0 = -0.782$ MeV,
   in agreement with CODATA.
