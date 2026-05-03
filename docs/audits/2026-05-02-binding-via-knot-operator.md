# Real binding via knot operator — framework status

## User direction

> "real bind via knot operator that reduces binding energy. may not
> be observable not operator"

## Framework's existing binding mechanism

`prop:derived-mass-formula-light-isotopes` already encodes binding
via knot-operator structure:

$$
\mathcal{M}(Z, N) = Z\,\mathfrak{m}_p + N\,\mathfrak{m}_n + Z\,m_e + \alpha (\Phi_1 - 2[3]_q \Phi_2 + H_A^2 \Phi_3) + \Delta_W + \Delta_{T=1}
$$

Two binding-reducing terms (both *subtract* mass = bind nucleons):

- $\Delta_W = -m_e \cdot H_q((2,2)) \cdot \min(Z, N)/A$ (Wigner T=0 np pairing)
- $\Delta_{T=1} = -m_e \cdot H_q((2,2)) \cdot (n_{pp}+n_{nn})/A$ (T=1 isovector)

The 3-term Wedderburn correction $\alpha (\Phi_1 - 2[3]_q \Phi_2 +
H_A^2 \Phi_3)$ is sign-bearing — its second term carries a
$-2[3]_q$ coefficient, so it CAN reduce mass.

## Performance: framework's own scorecard

| isotope | $M_{\text{pred}}$ MeV | CODATA MeV | mass error | binding error |
|---------|----------------------:|-----------:|-----------:|--------------:|
| $^1$H, n | exact (Φ=0) | exact | 0.000% | — |
| D | 1875.20 | 1876.12 | -0.049% | +41% |
| T | 2812.62 | 2809.43 | +0.114% | -38% |
| $^3$He | 2811.85 | 2809.41 | +0.087% | -32% |
| $^4$He | 3749.88 | 3728.40 | **+0.576%** | **-76%** |
| $^6$Li | 5625.69 | 5603.05 | +0.404% | -71% |
| $^7$Li | 6552.03 | 6535.37 | +0.255% | -42% |

Framework explicitly states (block.md:62):

> *The under-binding pattern is structural: the formula misses an
> intra-shell binding mechanism present in nature. Closing the gap
> universally requires a new derived term (not phenomenological
> patches), which remains an open research direction.*

## What the missing knot operator is

Per `prop:knot-operator-transition`, each $A \to A+1$ transition
has a definite knot type:

| transition | operator | knot |
|------------|----------|------|
| $p \to D$ | $\sigma_0 - h/2$ | unknot → single crossing |
| $D \to {}^3$H,He | $\sigma^{\pm 1}(\sigma_0 - h/2)$ | Hopf link |
| ${}^3 \to {}^4$He | $(\sigma_0-h/2)(\sigma_1-h/2)\sigma_0$ | **trefoil** $T_{2,3}$ |

The trefoil-completion at $A=4$ closes the topology, "explaining
why $^4$He has the strongest binding per nucleon among light
nuclei."

The MISSING binding mechanism: a **closure-energy operator** $K$
that activates when the braid-word completes a knot type. At
$A=4$ the trefoil closes; the closure energy contributes binding
that's not in the per-generator inter-nucleon $\Phi_1, \Phi_2,
\Phi_3$ chain.

## The user's hint, decoded

"may not be observable not operator" — the closure-energy
operator $K$ lives in the **morphism category** (transition
operators between states), not in the **observable algebra**
(Hermitian operators with eigenvalue measurements). It's a
categorical structure, not a quantum-mechanical observable.

Implementation-wise: $K$ acts on the braid word AT THE POINT OF
KNOT CLOSURE, contributing a topological correction. For 4He
the closure type is trefoil ($T_{2,3}$); the q-Jones polynomial
of the trefoil at $q_0$ is

$$
J_{3_1}(q) = -q^{-4} + q^{-3} + q^{-1} \quad \text{(reduced bracket)}
$$

evaluated at $q_0 \approx 1.110$ gives $\sim$ a value that should
encode the trefoil closure energy.

## Status

This is **research-grade**: the framework acknowledges the gap
and the user's directive points at the right mechanism, but the
explicit derivation of the closure-energy operator $K$ from
$q_0$ remains open. The per-braid mass tower's 1% spread sits on
top of the framework's 30-76% under-binding; both reflect the
same missing $K$-operator.

The implementation path:

1. Identify knot-completion type at each $A$ (per
   `knot-operator-transition`).
2. Derive closure energy from q-Jones polynomial of that knot.
3. Add to the mass formula as $- E_{\text{closure}}(A)$.
4. Verify cal/m_e spread closes.

But this requires deriving $E_{\text{closure}}(A)$ from
categorical first principles (not fitting). Open work.
