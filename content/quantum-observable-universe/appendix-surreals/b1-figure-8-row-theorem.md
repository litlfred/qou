**Proposition (B1 keystone is theorem-level at the figure-8 row —
combining Bloch–Suslin depth-2 identification with Murakami–Murakami's
proof of the Volume Conjecture for $4_1$).**

*The figure-8 row of [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
("B1") — the depth-2 instance over $F = \mathbb{Q}(\zeta_6)$
indexed by the dominant cell $\lambda_K = (2, 2)$ of $4_1$ in
$H_4(q)$ — is **theorem-level**, requiring no part of Goncharov's
or Beilinson's conjectures.*

### Statement

For the figure-8 knot $4_1$ embedded in Bring's genus-4 surface
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)):

1. **Inclusion at depth 2**: $\tau_{\mathrm{arch}}(\mathrm{Li}_2^q(\zeta_6))
   \in \mathcal{P}_2$ — by [`prop:depth-2-identification-bloch-suslin`](#prop:depth-2-identification-bloch-suslin).
2. **Strong sharpness at the figure-8 row**: $\tau_{\mathrm{arch}}(e_{(2,2)}
   \cdot \mathrm{Li}_2^q(\zeta_6))$ generates the *correct* class
   in $\mathcal{P}_2 / \mathcal{P}_1$ — namely
   $[\mathrm{Vol}(4_1)] = [2\,\mathrm{Cl}_2(\pi/3)]$.
3. **Volume Conjecture instance**: by Murakami–Murakami 2001 [@murakami-murakami2001],
   the asymptotic of the coloured Jones polynomial $J_{4_1}^{(N)}(e^{2\pi i/N})$
   converges to $\mathrm{Vol}(4_1)$ as $N \to \infty$ — discharging
   the Volume Conjecture for $4_1$ specifically.

Combining (1)–(3) yields: B1 at the figure-8 row is a **theorem**.
