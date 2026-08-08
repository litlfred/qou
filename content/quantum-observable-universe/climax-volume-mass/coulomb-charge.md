Let $\mathfrak{H}$ be a knot composite with braid word $\beta$. Let $n_+(\beta)$ and $n_-(\beta)$ denote the number of positive and negative crossings in $\beta$. We define the **Coulomb charge** of $\mathfrak{H}$ as:

$$
  Q(\mathfrak{H}) =  \tfrac{1}{2}\bigl(n_+(\beta) - n_-(\beta)\bigr).
$$

The crossing energy ([crossing energy](#def:crossing-energy)) assigns $q$ to each positive crossing and $-q^{-1}$ to each negative one — the two eigenvalues of the Hecke generator $\sigma_i$ — so

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) = n_+ q - n_- q^{-1}.
$$

Splitting that into parts even and odd under the bar involution $q \leftrightarrow q^{-1}$ gives

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  =
  \underbrace{\tfrac{1}{2}(n_+ - n_-)(q + q^{-1})}_{\text{bar-even}} +
  \underbrace{\tfrac{1}{2}(n_+ + n_-)(q - q^{-1})}_{\text{bar-odd}},
$$

which reconstructs $n_+ q - n_- q^{-1}$ identically, for all $n_+$ and $n_-$.

**Which multiplicity sits on which channel.** The bar-even coefficient is
$\tfrac{1}{2}(n_+ - n_-) = Q(\mathfrak{H})$, the Coulomb charge. The bar-odd
coefficient is $\tfrac{1}{2}(n_+ + n_-)$, half the *total* crossing count. The
pairing matters: exchanging the two multiplicities leaves the split agreeing with
$\mathfrak{E}_{\mathrm{cross}}$ only when $n_- = 0$, and inverts which channel
$Q$ controls.

Two consequences follow directly, and neither is optional:

- The bar-odd coefficient $\tfrac{1}{2}(n_+ + n_-)$ is a crossing *count*, hence
  non-negative. The bar-odd term therefore **cannot change sign** with the
  chirality of the composite, so it cannot carry an attractive-versus-repulsive
  distinction driven by $Q$.
- $Q(\mathfrak{H})$ instead scales the bar-even term, which is the channel the
  framework reads as strong binding.

The ratio of bar-odd to bar-even contributions is

$$
  \frac{\mathfrak{E}^{\text{odd}}}{\mathfrak{E}^{\text{even}}}
  = \frac{n_+ + n_-}{n_+ - n_-}\,\tanh(\ln q),
$$

which reduces to $\tanh(\ln q) \approx 0.104$ at $q = q_0$ **only when
$n_- = 0$**. For a composite with $(n_+, n_-) = (2, 1)$ the ratio is
$3\tanh(\ln q) \approx 0.312$, so the unqualified constant is not a property of
the decomposition but of the chirally pure case.

**Open: what the bar-odd channel is.** Reading the bar-odd term as *the
electromagnetic correction* requires a route from $Q$ to that term, and the
decomposition does not supply one: the bar-odd coefficient is a crossing count,
while $Q$ sits on the bar-even side. The Coulomb charge $Q = w/2$ is unaffected —
it is defined above and used elsewhere on its own terms — but this block makes no
claim identifying either channel with electromagnetism. Supplying such a route,
or relabelling the channels, is open.
