The framework's $H_n(q)$ Hecke algebra carries a small-$q$
$\leftrightarrow$ root-of-unity duality, and the conjecture below
supplies its modular mechanism.

**Conjecture (modular $S$-transform closure).**
*Writing the Hecke parameter as $q = e^{2\pi i \tau}$ for a complex
parameter $\tau \in \mathbb{H}$ in the upper half-plane, the modular
$S$-transform $\tau \mapsto -1/\tau$ induces the analytic continuation*

$$
  q  \;\longmapsto\;  \tilde q \;:=\; \exp\!\bigl(-2\pi i / \tau\bigr).
$$

The substrate enters this picture through its bar image $q_0^{-1}$, not through $q_0$. Modular convergence requires $\mathrm{Im}\tau > 0$. Because $q_0 \approx 1.11 > 1$, the value $q_0 = e^{2\pi i\tau_0}$ has $\mathrm{Im}\tau_0 < 0$. Only $q_0^{-1} \approx 0.901 < 1$ lands in $\mathbb{H}$. The modular sector is intrinsically bar-symmetric. A proved instance of a $q \leftrightarrow \tilde q$ pairing of this kind: the Andersen--Kashaev state integral of the figure-eight knot is a bilinear combination of two $q$-hypergeometric series, each evaluated once at $q$ and once at the modular partner $\tilde q = e^{-2\pi i/\tau}$, with $\tau = b^2$ \cite[\S1.3]{garoufalidis2013}.

The $S$-transform provides a structural duality. The parameter $q$ admits a bar-symmetric real parameterisation ($q \in \mathbb{R}_{>0}$) and a modular parameterisation ($q = e^{2\pi i \tau}$). The analytic continuation of every Hecke quantity to the modular parameter is well-defined. The $S$-transform $\tau \mapsto -1/\tau$ provides a categorical duality complementing the bar involution.

## The structural duality

The Hecke parameter has two natural parameterisations:

| Parameterisation | Relation |
|------------------|----------|
| Bar-symmetric `q` (real, framework standard) | $q \in \mathbb{R}_{>0}$, bar: $q \mapsto q^{-1}$ |
| Modular `τ` (complex, upper half-plane) | $q = e^{2\pi i \tau}$, $S$: $\tau \mapsto -1/\tau$ |

These are **distinct** parameterisations of the same Hecke
algebra. Bar is an involution on the "real" axis of the q-plane;
$S$ is an involution on the modular parameter $\tau$.

**The conjecture**: the analytic continuation of every Hecke
quantity to modular parameter is well-defined, and the $S$-transform
$\tau \mapsto -1/\tau$ gives a categorical duality complementing
bar.

## Connection to TQFT / Volume Conjecture

The Kashaev Volume Conjecture
([conj:kashaev-volume-conjecture](#conj:kashaev-volume-conjecture))
asymptotics are governed by the limit $q \to e^{2\pi i / k}$ as
$k \to \infty$.  The $S$-transform realises this limit as the
modular image of the substrate: writing the bar image
$q_0^{-1} = e^{2\pi i \tau_0}$ with $\tau_0 \approx +0.0166\,i$ (small
positive imaginary, near the cusp $\tau \to 0$), the $S$-transform sends
$\tau_0 \mapsto -1/\tau_0 \approx +60.2\,i$ — large positive imaginary
part, i.e. nome $\tilde q \to 0$, the root-of-unity / TQFT limit. (The
choice of $q_0^{-1}$ over $q_0$ is the bar-image point of the conjecture
statement above.)

This gives the framework an **explicit categorical handle** on the
small-$q_0$ $\leftrightarrow$ root-of-unity duality.

## Relationship to the complex-$q$ lift

The complex-$q$ extension
([prop:q-zero-complex-extension](#prop:q-zero-complex-extension)
+ [prop:lusztig-vs-hermitian-bar](#prop:lusztig-vs-hermitian-bar))
extends the framework's substrate to complex $q$ with $|q| > 1$.
The modular $S$-transform of this conjecture is the natural
**continuation of bar** beyond the real axis:

- The bar involution and the Hermitian $*$ coincide on the real axis ($q \in
  \mathbb{R}$); they split for $\mathrm{Im}(q) \neq 0$.
- The modular $S$-transform (this conjecture) extends the duality structure
  to the **modular upper half-plane** by treating $q = e^{2\pi i
  \tau}$ as the natural parameterisation.

Together the bar involution, the Hermitian $*$ and the modular $S$-transform
give the framework three distinct $\mathbb{Z}/2$
involutions on the Hecke parameter, each acting on a different
parameter manifold:

| Involution | Parameter manifold | Action |
|------------|--------------------|--------|
| bar | real positive axis | $q \mapsto q^{-1}$ |
| Hermitian $*$ | complex with $\|q\| > 1$ | $q \mapsto \bar q^{-1}$ |
| **modular $S$** | modular $\tau \in \mathbb{H}$ | $\tau \mapsto -1/\tau$ |

## Structural position

- **GB filtration level.** None: the $S$-transform is at the
  parameter level, not the Hecke-element level.
- **Jet order.** All orders: the modular action acts on the entire
  $q$-expansion of every quantity.
- **Bar-symmetry.** Distinct from bar. The $S$-transform composed
  with bar gives a $\mathbb{Z}/2 \times \mathbb{Z}/2$ structure on
  the modular q-parameter space.

## Open R&D

1. **Analytic continuation framework**: verify every framework
   quantity (Hecke generators, Frobenius pairing, Markov trace,
   Wedderburn weights $y_\lambda$) has well-defined modular
   continuation to complex $\tau$.
2. **Numerical check**: at the bar image $q_0^{-1}$ (the convergent
   branch), compute the $S$-transform $\tilde q_0$ and verify the Volume
   Conjecture asymptotic on $\tilde q_0$ matches the framework's bare-volume
   evaluation.
3. **Do not conflate with the named elliptic curves.** The modular
   $\tau$ here is **not** the period $\tau$ of the Descartes/color curve
   $\mathcal{E}_q$ ([prop:descartes-elliptic-curve](../brings-surface/descartes-elliptic-curve.md)):
   the modular nome is $q_0^{-1} \approx 0.90$ (near the cusp) while
   $\mathcal{E}_q$'s period nome is $\approx 0.0029$ (deep in the
   fundamental domain) — a $\sim\!312\times$ mismatch.
4. **Connect to the Bloch-group route**: the modular $S$-transform on the
   $K_3(\mathbb{C})$ regulator gives a natural framework-side
   handle on the analytic structure of the Bloch-Wigner
   dilogarithm.
5. Closing the conjecture requires a numerical witness verifying the
   volume-conjecture asymptotic on $\tilde q_0$.

## Cross-references

- The complex-$q$ lift: the complex-$q_0$ extension proposition and the Lusztig-versus-Hermitian bar comparison
- Volume Conjecture: [conj:kashaev-volume-conjecture](#conj:kashaev-volume-conjecture)
- The Bloch-group route: [conj:borromean-bloch-group-element](../mass-theory/borromean-bloch-group-element.md)

**Archimedean specialisation.** Modular convergence is an archimedean statement: the estimates use $\mathrm{Im}\,\tau$ and $\exp$ over $\mathbb{R}$, so it sits on the archimedean side of the substrate wall.
