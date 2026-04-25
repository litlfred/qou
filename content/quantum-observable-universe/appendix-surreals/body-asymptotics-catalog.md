The main paper states a number of analytic error bounds in
classical Big-O / little-o / geometric-tail form. This remark
catalogs each of them and records the equivalent surreal
$\ordw$-statement under the convention of
[Big-O via $\ordw$](#rem:conway-normal-form). The body of the paper
is **not rewritten** in $\preceq$ / $\prec$ form; this catalog is
the formal anchor that body propositions point to.

## Body-paper analytic bounds

### Chapter: Braids and Knots

| Body block | Bound (as written) | $\ordw$-form |
|---|---|---|
| [Hecke convergence bound](#prop:hecke-convergence-bound) | $\mathrm{MAE}(k) \leq C \cdot r^{-(k-3)}$, $r \approx 4$ | $\ordw\bigl(\mathrm{MAE}(k)\bigr) = -(k-3)\,\ordw(r)$ |
| [Hoefsmit scattering pipeline](#prop:hoefsmit-scattering-pipeline) | $\mathrm{MAE}(k) \leq C_0 [2]_q^{-2(k-3)}$ | $\ordw\bigl(\mathrm{MAE}(k)\bigr) = -2(k-3)\,\ordw([2]_q)$ |
| [Jet-tower convergence](#prop:jet-tower-convergence) | tail $\leq \Delta_{\max} \cdot \dfrac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}$ | $\ordw(\text{tail}) = 2(N+1)\,\ordw(\hbar_q)$ |
| [Universal braid branching](#prop:universal-braid-branching) | per-level Plancherel weight $O([2]_q^{-2})$ | $\ordw(\text{per-level weight}) = -2\,\ordw([2]_q)$ |
| [Unified iterative correction](#prop:unified-iterative-correction) | Féray–Méliot $O(1/\sqrt{A})$ | $\ordw\bigl(\text{accumulator}\bigr) = -\tfrac{1}{2}\,\ordw(A)$ |
| [Möbius energy proof](#prf:mobius-energy) | regularised $\int_{S^1 \times S^1} d\ell(x)\,d\ell(y)/|x-y|^2$ (Lebesgue on $S^1$) | surreal Loeb-measure replacement per [calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon) §5; $\ordw(\text{regulariser}) = \ordw(\varepsilon)$ |
| [Mass-endomorphism jet tower](#rem:mass-endomorphism-jet-tower) | open: uniform boundedness $\lvert \Delta^{(n)} \rvert \leq \Delta_{\max}$ | [surreal blow-up calculus](#def:surreal-blowup-calculus) at each jet level; $\ordw(\Delta^{(n)}) \geq 0$ conjectured |

### Chapter: Fluid Dynamics

| Body block | Bound (as written) | $\ordw$-form |
|---|---|---|
| [NS obstruction computation](#prop:ns-obstruction-computation) | $|j^n v|_\Sigma \sim \Gamma/d^{n+1}$, $\sim 1/(T^*-t)^{(n+1)/2}$ | $\ordw\bigl(\lvert j^n v\rvert_\Sigma\bigr) = -(n+1)\,\ordw(d) = -\tfrac{n+1}{2}\,\ordw(T^*-t)$ |

### Classical-limit blocks

| Body block | Classical limit | Surreal replacement |
|---|---|---|
| [Feynman classical limit](#prop:feynman-classical-limit) | $q \to 1$ degeneration of $H_n(q) \to k[S_n]$ | [standard-part functor](#def:standard-part-functor) at $q = 1 + \varepsilon$ (cf.\ [classical-limit standard-part](#conj:classical-limit-stpart)) |
| [Kashaev volume--density](#rem:kashaev-volume-density) | $\mathrm{Vol}(K) = 2\pi \lim_{N \to \infty} \log\lvert J_N \rvert / N$ | $\mathrm{Vol}(K) = \mathrm{st}\bigl(\text{coloured trace at } q = e^{2\pi i/N}\bigr)$ (cf.\ [Kashaev as standard-part](#conj:kashaev-surreal)) |

## Reading conventions

For each entry above, the classical statement and the
$\ordw$-statement are **logically equivalent** under the dictionary
of [Big-O via $\ordw$](#rem:conway-normal-form):

- A classical bound $|f| \leq C \cdot g$ with $C$ a positive real
  constant is equivalent to $\ordw(f) \leq \ordw(g)$ (i.e.\
  $f \preceq g$).
- A classical $f = O(g)$ is equivalent to $\ordw(f) \leq \ordw(g)$.
- A classical $f \sim g$ is equivalent to $\ordw(f) = \ordw(g)$
  with matching leading coefficient ($f \simeq g$).
- A classical limit $\lim_{x \to x_0} f(x) = L$ in the body is
  recoverable as $\mathrm{st}\bigl(f(x_0 + \varepsilon)\bigr) = L$
  for an infinitesimal $\varepsilon$
  ([standard-part functor](#def:standard-part-functor)).

The catalog is non-load-bearing. It exists so that body
propositions can carry a single forward reference to the surreal
appendix without rewriting their statement, and so that the
appendix's notational machinery is visibly anchored in concrete
body content rather than left as an isolated convention.

## Engineering note

The recursive jet structures (mass endomorphism brane tower,
Yekutieli jet prolongation, NS jet correction $\delta_n$) all
admit the same surreal reading: each level adds one factor of
the relevant infinitesimal ($\hbar_q$ in the brane tower, $d$ in
the NS Biot--Savart structure), so the $\ordw$ of the level-$n$
correction is linear in $n$. This is the
[surreal blow-up calculus](#def:surreal-blowup-calculus) at work,
and it matches the geometric-series tail bounds in the body
without requiring any change in body notation.
