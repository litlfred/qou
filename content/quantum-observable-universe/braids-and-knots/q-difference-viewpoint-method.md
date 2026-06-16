### The $q$-difference / root-of-unity viewpoint

Several of the framework's $q$-deformed quantities — the $\mathfrak{Q}_\beta$
Habiro element, the $\alpha_{EM}$ next-order factor
([`prop:alpha-em-habiro-bar-involution`](#prop:alpha-em-habiro-bar-involution)),
and the Markov trace itself — are analysed not through
their power series at $q=1$, but through their behaviour under the
**$q$-difference shift** $\sigma_q : q \mapsto q\zeta$, where $\zeta$
runs over roots of unity. This subsection records the method, which
recurs throughout the categorical-derivation chain.

A Habiro-type element $F(q)$ satisfies a $q$-difference equation of the
form $(1 - \sigma_q)\,F = \delta\,(q;q)_\infty$ (Habiro's equation;
equivalently the level-$1$ Knizhnik–Zamolodchikov connection in
disguise). Three structural features make this tractable:

1. **Fourier diagonalisation.** The shift $\sigma_q$ is diagonalised by
   the Fourier transform over the cyclic group $\langle\zeta\rangle$;
   its eigenvectors are the root-of-unity evaluations $F(\zeta_d)$.
2. **Witten–Reshetikhin–Turaev truncation.** The $q$-Pochhammer
   $(u;u)_m = \prod_{k\le m}(1 - u^k)$ *vanishes* at a primitive
   $d$-th root of unity for $d \le m$. Evaluating a Habiro expansion
   $F = \sum_m a_m\,(u;u)_m / D$ at $\zeta_d$ therefore truncates the
   sum to its first $d$ modes — an exact, finite spectrum.
3. **Mode-by-mode solution.** When $F$ is rational, solving the
   $q$-difference equation reduces to the **partial-fraction
   decomposition** of $F$ over its poles: each pole is one Fourier
   mode, and the modular data (residues at $\zeta_d$) are exact.

This viewpoint is intrinsically **fibre-level**. The variable $q$ is
formal, with $\mathrm{Im}(q)$ unconstrained, and the operative symmetry
is the **bar involution** $q \mapsto q^{-1}$ — not a reality
assumption. Only the *observable* component, obtained by evaluating at
the real archimedean substrate, is real
(cf. the fibre-versus-observable distinction in the front matter). The
root-of-unity spectra and residues are exact identities in the
relevant cyclotomic field, independent of the eventual archimedean
realisation.

The duality between $\alpha_{EM}$ and $\mathfrak{Q}_\beta$ illustrates the method.
Both are Habiro elements with the *same* $q$-difference machinery, yet
they are distinguished by a single modular datum: the $\alpha_{EM}$
element $[2]_q(1-h^2\alpha)$ is a bar-involution fixed point with a
**zero** at $\zeta_4$, while the $\mathfrak{Q}_\beta$ trace difference is *not* a
bar fixed point and has a **pole** at $\zeta_4$. The cleanliness of the
$\alpha_{EM}$ case — a polynomial, bar-fixed, with $q_0$-stable Taylor
coefficients — is precisely why its next-order form was identifiable as
a Habiro element, whereas the $\mathfrak{Q}_\beta$ analogue required the
additional cancellation of a bar-anti-invariant part.
