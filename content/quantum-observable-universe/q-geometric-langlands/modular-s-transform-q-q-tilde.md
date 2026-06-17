**Conjecture (D14 modular $S$-transform closure).**
*Writing the Hecke parameter as $q = e^{2\pi i \tau}$ for a complex
parameter $\tau \in \mathbb{H}$ in the upper half-plane, the modular
$S$-transform $\tau \mapsto -1/\tau$ induces the analytic continuation*

$$
  q  \;\longmapsto\;  \tilde q \;:=\; \exp\!\bigl(2\pi i / \tau\bigr).
$$

*The substrate enters this picture through its **bar image**
$q_0^{-1}$, not through $q_0$ itself: modular convergence requires
$\operatorname{Im}\tau > 0$ (the nome $|e^{2\pi i\tau}| < 1$), and since
$q_0 \approx 1.11 > 1$ the value $q_0 = e^{2\pi i\tau_0}$ has
$\operatorname{Im}\tau_0 < 0$ (lower half-plane). It is $q_0^{-1} \approx
0.901 < 1$ that lands in $\mathbb{H}$. The modular / theta sector of the
framework is therefore intrinsically bar-symmetric (the $\mathrm{Li}_2^q$ /
binding side of the $\Phi_q$-vs-$\mathrm{Li}_2^q$ split), consistent with
D1 acting at the parameter level and $S$ at the modular level.*

*This is a distinct $\mathbb{Z}/2$ duality from the bar involution
$q \mapsto q^{-1}$ (D1): bar acts on the real / parameter level,
$S$-transform acts on the modular level.  Near roots of unity
$q \to e^{2\pi i / k}$ (TQFT level-$k$ Chern-Simons evaluation),
the $S$-transform realises the "small-$q$ $\leftrightarrow$ large-$q$" duality of
the framework's $H_n(q)$ Hecke algebra.*

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
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
asymptotics are governed by the limit $q \to e^{2\pi i / k}$ as
$k \to \infty$.  The $S$-transform realises this limit as the
modular image of the substrate: writing the bar image
$q_0^{-1} = e^{2\pi i \tau_0}$ with $\tau_0 \approx +0.0166\,i$ (small
positive imaginary, near the cusp $\tau \to 0$), the $S$-transform sends
$\tau_0 \mapsto -1/\tau_0 \approx +60.2\,i$ — large positive imaginary
part, i.e. nome $\tilde q \to 0$, the root-of-unity / TQFT limit. (Taking
$q_0$ directly instead of $q_0^{-1}$ would place $\tau_0$ in the lower
half-plane, where the modular continuation does not converge — see the
bar-image remark in the conjecture statement above and the witness
[`computations/probes/d14-theta-bar-side.witness.json`](../../../computations/probes/d14-theta-bar-side.witness.json).)

This gives the framework an **explicit categorical handle** on the
small-$q_0$ $\leftrightarrow$ root-of-unity duality flagged in the 13-driver menu
under driver (viii) Modular $S$-transform.

## Relationship to 's complex-q lift

The complex-q extension landed in PR [#1127](https://github.com/litlfred/qou/pull/1127)
([`prop:q-zero-complex-extension`](#prop:q-zero-complex-extension)
+ [`prop:lusztig-vs-hermitian-bar`](#prop:lusztig-vs-hermitian-bar))
extends the framework's substrate to complex $q$ with $|q| > 1$.
The modular $S$-transform of this conjecture is the natural
**continuation of bar** beyond the real axis:

- Bar (D1) and Hermitian * (D2) coincide on the real axis ($q \in
  \mathbb{R}$); they split for $\mathrm{Im}(q) \neq 0$.
- Modular $S$ (this conjecture, D14) extends the duality structure
  to the **modular upper half-plane** by treating $q = e^{2\pi i
  \tau}$ as the natural parameterisation.

Together, D1 + D2 + D14 give the framework three distinct $\mathbb{Z}/2$
involutions on the Hecke parameter, each acting on a different
parameter manifold:

| Involution | Parameter manifold | Action |
|------------|--------------------|--------|
| D1 bar | real positive axis | $q \mapsto q^{-1}$ |
| D2 Hermitian * | complex with $\|q\| > 1$ | $q \mapsto \bar q^{-1}$ |
| **D14 modular $S$** | modular $\tau \in \mathbb{H}$ | $\tau \mapsto -1/\tau$ |

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A — the $S$-transform is at the
  parameter level, not the Hecke-element level.
- **Jet order**: all-orders (the modular action acts on the entire
  $q$-expansion of every quantity).
- **Bar-symmetry status**: distinct from bar. $S$-transform composed
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
5. **Do not conflate with the named elliptic curves.** The modular
   $\tau$ here is **not** the period $\tau$ of the Descartes/color curve
   $\mathcal{E}_q$ ([`prop:descartes-elliptic-curve`](../predicted-spectra/elliptic-stability-locus.md)):
   the modular nome is $q_0^{-1} \approx 0.90$ (near the cusp) while
   $\mathcal{E}_q$'s period nome is $\approx 0.0029$ (deep in the
   fundamental domain) — a $\sim\!312\times$ mismatch. See
   [`docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md`](../../../docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md).
3. **Connect to D16 Bloch-group**: the modular $S$-transform on the
   $K_3(\mathbb{C})$ regulator gives a natural framework-side
   handle on the analytic structure of the Bloch-Wigner
   dilogarithm.
4. **D14 to closed** requires Lean class `ModularSTransformQQTilde`
   inhabited + numerical witness verifying the volume-conjecture
   asymptotic on $\tilde q_0$.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) D14
  + §2 Cluster D (limit dualities) + adjacent to D2 Hermitian *
- D2 sibling: PR [#1127](https://github.com/litlfred/qou/pull/1127)
  blocks `prop:q-zero-complex-extension` +
  `prop:lusztig-vs-hermitian-bar`
- Volume Conjecture: [`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture)
- D16 Bloch group: [`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
- 13-driver menu driver (viii): [`docs/audits/-lambda-scale-canonical-unification.md`](../../docs/audits/-lambda-scale-canonical-unification.md)
