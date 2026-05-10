**Remark (chirality structure on Goncharov period classes via the
bar involution).**

The bar involution $* \colon q \mapsto q^{-1}$ on $H_n(q)$ —
equivalently, the Hecke algebra antipode
$* (\sigma_i) = \sigma_i^{-1}$ — acts on the central primitive
idempotents $e_\lambda$ by *partition conjugation*: $*(e_\lambda) =
e_{\lambda'}$ where $\lambda' = $ transpose Young diagram
([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)
Cross-check 3-4).

Under [`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence)
+ [`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic),
this *categorifies* the chirality structure of hyperbolic 3-manifold
volumes:

| Cell-class | Bar action on $e_\lambda$ | Knot type | Period type |
|---|---|---|---|
| **Self-conjugate** ($\lambda = \lambda'$) | $*(e_\lambda) = e_\lambda$ | amphichiral knot | $\mathrm{Vol}(K) = \mathrm{Vol}(\overline{K})$ — *real* period in $\mathcal{P}_2(\mathbb{R})$ |
| **Chiral pair** ($\lambda \neq \lambda'$) | $*(e_\lambda) = e_{\lambda'}$ | chiral knot $K \neq \overline{K}$ | $\mathrm{Vol}(K) = \mathrm{Vol}(\overline{K})$ but $\mathrm{CS}(K) = -\mathrm{CS}(\overline{K})$ — period with a Tate twist |

### The figure-8 row

$4_1$ is amphichiral: $4_1 \cong \overline{4_1}$. Its dominant cell
in $H_4(q)$ is $\lambda = (2, 2)$, the unique self-conjugate
4-partition. Bar-fixed projection $e_{(2,2)}$ → real period
$2\,\mathrm{Cl}_2(\pi/3) \in \mathbb{R}$, no twist.

### A chiral example: trefoil

$3_1$ is chiral: $3_1 \neq \overline{3_1}$. Its dominant cell
$\lambda = (3)$ pairs with $\lambda' = (1, 1, 1)$ under bar:
$*(e_{(3)}) = e_{(1, 1, 1)}$. The volume is $0$ (trefoil is not
hyperbolic) but the *Chern–Simons* invariant
$\mathrm{CS}(3_1) = \pm \pi^2 / 6$ is sign-flipped under bar — the
chirality-twisted depth-3 period in $\mathcal{P}_3 / \mathcal{P}_2$.
This is the depth-3 manifestation of the same chirality structure;
see [`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)
for a Bring-natural depth-3 witness.

### Compatibility with B1's depth filtration

The bar involution preserves the iterated-integral depth filtration:
$* \colon G^{(n)}(\mathcal{H}_q) \to G^{(n)}(\mathcal{H}_q)$. Each
depth $G^{(n)}$ therefore decomposes into bar-eigenspaces:

$$
  G^{(n)}(\mathcal{H}_q) \;=\; G^{(n), +} \;\oplus\; G^{(n), -}
$$

with $G^{(n), \pm}$ the $\pm 1$ eigenspaces of $*$. Under
$\tau_{\mathrm{arch}}$:

- $G^{(n), +} \to \mathcal{P}_n(\mathbb{R})$ — real periods
- $G^{(n), -} \to i \cdot \mathcal{P}_n(\mathbb{R})$ — imaginary
  periods (Tate-twisted; geometrically, these are $\mathrm{CS}$-style
  invariants paired with a $(2\pi i)^n$-factor from the Tate motive)

So each Goncharov period class $\mathcal{P}_n / \mathcal{P}_{n-1}$
inherits a *bar-grading*. Hyperbolic volume sits in $\mathcal{P}_2^+$,
Chern–Simons in $\mathcal{P}_3^-$, multiple polylog values split
according to amphichirality of the underlying motive.

### Provenance and connection to existing paper structure

This is the categorical lift of the amphichirality story already in
the figure-8 block
([`rem:figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)),
recast as period-theoretic structure on $\mathcal{P}_\bullet$. The
bar involution's role is *structural*, not analytic: it organises
period classes by orientation-reversal symmetry of the underlying
motivic substrate.

### Falsifiability

A clean test: pick a chiral hyperbolic knot $K$ with known
$\mathrm{CS}(K) \neq 0$ (e.g. $5_2$ — the simplest chiral
hyperbolic knot, $\mathrm{Vol} \approx 2.8281$,
$\mathrm{CS} \approx -0.1530\,\pi^2$ mod $\pi^2$). Verify:

1. The dominant cell of $5_2$ in $H_4(q)$ (or $H_5(q)$) is a
   *chiral pair*, not self-conjugate.
2. The depth-2 pairing gives $\mathrm{Vol}(5_2)$ (real).
3. The depth-3 pairing on the same cell gives $\mathrm{CS}(5_2)$
   (chirality-twisted).

Discharge: open. The cell identification at $H_5(q)$ is the
technical step.
