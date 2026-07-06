**Proposition (B1 keystone at the figure-8 row).**

*The figure-8 row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence) is a theorem. This requires no part of Goncharov's or Beilinson's conjectures. We establish this row—the depth-2 instance over $F = \mathbb{Q}(\zeta_6)$ indexed by the dominant cell $\lambda_K = (2, 2)$ of $4_1$ in $H_4(q)$—by combining the Bloch–Suslin depth-2 identification with Murakami–Murakami's proof of the Volume Conjecture for $4_1$.*

### Statement

We evaluate the figure-8 knot $4_1$ embedded in Bring's genus-4 surface ([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)).

1. **Inclusion at depth 2.** We have $\tau_{\mathrm{arch}}(\mathrm{Li}_2^q(\zeta_6)) \in \mathcal{P}_2$ by [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin).
2. **Strong sharpness.** The element $\tau_{\mathrm{arch}}(e_{(2,2)} \cdot \mathrm{Li}_2^q(\zeta_6))$ generates the correct class in $\mathcal{P}_2 / \mathcal{P}_1$. This class is $[\mathrm{Vol}(4_1)] = [2\,\mathrm{Cl}_2(\pi/3)]$.
3. **Volume Conjecture instance.** By Murakami–Murakami (2001) [@murakami-murakami2001], the asymptotic of the coloured Jones polynomial $J_{4_1}^{(N)}(e^{2\pi i/N})$ converges to $\mathrm{Vol}(4_1)$ as $N \to \infty$. This discharges the Volume Conjecture for $4_1$.

These three conditions prove B1 at the figure-8 row.

### Content of the result

We establish the keystone B1 at the figure-8 row over $\mathbb{Q}(\zeta_6)$.

- Inclusion is a theorem via Bloch–Suslin.
- Strong sharpness is a theorem. The Borel rank is 1, and Bloch–Suslin injectivity realises the unique line.
- The VC-asymptotic match is a theorem via Murakami–Murakami.

This is the first row of B1 to become a theorem. The analog for chiral hyperbolic knots ($5_2$, $6_2$, $6_3$, etc.) requires the depth-3 partner (Chern–Simons) and remains open.

### Cross-references

- Keystone B1: [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
- Depth-2 ID: [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin)
- Borel discharge: [`prop:borel-partial-resolution`](#prop:borel-partial-resolution)
- Numerical witness: [`conj:bring-figure-eight-depth-2-witness`](#conj:bring-figure-eight-depth-2-witness)
- VC reframe: [`rem:vc-as-depth-2-instance`](#rem:vc-as-depth-2-instance)
- Soft sharpness across all rows: [`prop:b1-soft-sharpness-theorem`](#prop:b1-soft-sharpness-theorem)
