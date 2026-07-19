
The Kashaev Volume Conjecture
([`conj:kashaev-volume-conjecture`](#conj:kashaev-volume-conjecture))
asymptotics are governed by the limit $q \to e^{2\pi i / k}$ as
$k \to \infty$.  The $S$-transform realises this limit as the
modular image of the substrate: writing the bar image
$q_0^{-1} = e^{2\pi i \tau_0}$ with $\tau_0 \approx +0.0166\,i$ (small
positive imaginary, near the cusp $\tau \to 0$), the $S$-transform sends
$\tau_0 \mapsto -1/\tau_0 \approx +60.2\,i$ — large positive imaginary
part, i.e. nome $\tilde q \to 0$, the root-of-unity / TQFT limit. (The
choice of $q_0^{-1}$ over $q_0$ is the bar-image point of the conjecture
statement above; witness
[`computations/probes/d14-theta-bar-side.witness.json`](../../../computations/probes/d14-theta-bar-side.witness.json).)

This gives the framework an **explicit categorical handle** on the
small-$q_0$ $\leftrightarrow$ root-of-unity duality.

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

(The labels D1, D2, D14 — and D16 below — index entries in the
duality tracker listed under Cross-references.)

Together, D1 + D2 + D14 give the framework three distinct $\mathbb{Z}/2$
involutions on the Hecke parameter, each acting on a different
parameter manifold:

| Involution | Parameter manifold | Action |
|------------|--------------------|--------|
| D1 bar | real positive axis | $q \mapsto q^{-1}$ |
| D2 Hermitian * | complex with $\|q\| > 1$ | $q \mapsto \bar q^{-1}$ |
| **D14 modular $S$** | modular $\tau \in \mathbb{H}$ | $\tau \mapsto -1/\tau$ |

