### Proof (Markov axiom + Hecke skein)

For a positive interface generator $\sigma_g$, the **Markov axiom**
([`thm:jones-markov-trace`](#thm:jones-markov-trace)) gives
$$
  \mathrm{tr}_M(\alpha \cdot \sigma_g) \;=\; z \cdot \mathrm{tr}_M(\alpha)
  \qquad \forall\, \alpha \in H_{n}(q).
$$
For a negative interface generator $\sigma_g^{-1}$, the **Hecke skein
relation** $\sigma_g^{-1} = \sigma_g - h \cdot \mathbf{1}$ combined
with linearity of $\mathrm{tr}_M$ gives
$$
  \mathrm{tr}_M(\alpha \cdot \sigma_g^{-1})
  \;=\; \mathrm{tr}_M(\alpha \cdot \sigma_g) - h \cdot \mathrm{tr}_M(\alpha)
  \;=\; (z - h) \cdot \mathrm{tr}_M(\alpha).
$$
Iterating over the $p_+(K) + p_-(K)$ interface generators of
$\bowtie_K$ — each one is "topmost" relative to the constituent
sub-braid below it — and applying the appropriate factor per sign
yields the boxed identity ($\star$).

### Averaged (bar-invariant) p-n interface

The same single Markov input fixes a **third** interface factor. The
canonical p-n boundary (`closed_form_tau_M.canonical_interface_kinds`,
`prop:averaging-resonance-rule`) carries no preferred chirality, so it is
the **bar-invariant** ($q \leftrightarrow q^{-1}$ symmetric) crossing
$$
  \sigma_{\mathrm{bar}} \;:=\; \tfrac{1}{2}\bigl(\sigma_g + \sigma_g^{-1}\bigr)
  \;=\; \sigma_g - \tfrac{h}{2}\cdot\mathbf{1},
$$
the last equality again from the Hecke skein $\sigma_g^{-1} = \sigma_g - h$.
Linearity of $\mathrm{tr}_M$ then gives
$$
  \mathrm{tr}_M(\alpha\cdot\sigma_{\mathrm{bar}})
  \;=\; \mathrm{tr}_M(\alpha\cdot\sigma_g) - \tfrac{h}{2}\,\mathrm{tr}_M(\alpha)
  \;=\; \Bigl(z - \tfrac{h}{2}\Bigr)\cdot\mathrm{tr}_M(\alpha).
$$
Thus **all three** per-interface factors — $z$ (positive), $z-h$
(negative), $z-\tfrac{h}{2}$ (bar-invariant p-n) — follow by
trace-linearity from the *single* Markov axiom $\mathrm{tr}_M(\alpha\sigma_g) =
z\,\mathrm{tr}_M(\alpha)$ plus the skein $\sigma_g^{-1}=\sigma_g-h$; none is an
independent input or a fit. The division-free form
$\mathrm{tr}_M(\alpha(\sigma_g+\sigma_g^{-1})) = (2z-h)\,\mathrm{tr}_M(\alpha)$ is
formalised over a generic commutative ring as
`interface_knot_markov_z_bar_symmetric` (the $\tfrac12$ normalisation is
deferred to the archimedean realisation, per the base-ring convention).

### categorical verification (4 atoms, exact representation Rust kernel)

Computed via the canonical formalism
using `pyhecke_native` for full $\mathrm{tr}_M$ at $H_n$ for $n \in \{6, 9, 12\}$:

| atom | $A$ | $p_+$ | $p_-$ | $\mathrm{tr}_M^{\mathrm{FULL}}/\mathrm{tr}_M^{\mathrm{CONSTIT}}$ | predicted $z^{p_+}(z-h)^{p_-}$ | rel. err. |
|---|:-:|:-:|:-:|---:|---:|---:|
| D    | 2 | 1 | 0 | 0.49932033 | 0.49932033 | $5\times10^{-16}$ |
| T    | 3 | 1 | 1 | 0.14493273 | 0.14493273 | $9\times10^{-16}$ |
| ${}^{3}$He  | 3 | 2 | 0 | 0.24932080 | 0.24932080 | $1\times10^{-15}$ |
| ${}^{4}$He  | 4 | 2 | 1 | 0.07236786 | 0.07236786 | $1\times10^{-15}$ |

Max rel. err. across all 4 atoms: $\sim 10^{-15}$ — exact at f64 precision.

Per-atom interface census (from `atom_braid_word_3A`):

- **D**: $p \cdot \sigma_3 \cdot n$ — 1 positive (p-n).
- **T**: $p \cdot \sigma_3 \cdot n \cdot \sigma_6^{-1} \cdot n$ — 1 positive (p-n) + 1 negative (n-n).
- **${}^{3}$He**: $p \cdot \sigma_3 \cdot p \cdot \sigma_6 \cdot n$ — 2 positive (p-p, p-n).
- **${}^{4}$He**: $p \cdot \sigma_3 \cdot p \cdot \sigma_6 \cdot n \cdot \sigma_9^{-1} \cdot n$ — 2 positive (p-p, p-n) + 1 negative (n-n).

### Structural reading

The interface knot $\bowtie_K$ is **categorically the Markov-axiom
boundary contribution** to the canonical atomic braid:

- **Positive interface** $\sigma_g$ (p-p or p-n boundary) $\to$ factor $z$ exactly
  (single application of the Markov axiom).
- **Negative interface** $\sigma_g^{-1}$ (n-n boundary, antisymmetric quark
  pair) $\to$ factor $z - h$ exactly (Markov axiom + Hecke skein $\sigma^{-1} =
  \sigma - h \cdot \mathbf{1}$).

The crossing-sign / nucleon-flavor pairing is encoded in
$\bowtie_K$ via $p_+(K)$ and $p_-(K)$ counts — these are determined
structurally by the canonical-braid construction, not phenomenologically
fit.

This locks 's interface-knot factorisation as
*derivation-grade*: each interface in the canonical atomic braid
contributes a Markov-trace factor that is either $z$ or $z - h$,
determined by the crossing sign. No empirical-fit parameter remains
at the $\mathrm{tr}_M$ level.

### Constit-side companion identity (Phase 5g, conjectural)

The factorisation $(\star)$ isolates the **interface** contribution
to the $\mathrm{tr}_M$ ratio.  The complementary **constit** factor —
$\mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}})$ at varying $Z$ — admits its own
clean categorical form at the substrate point:
$$
  \frac{\mathrm{tr}_M\!\bigl(\beta_{(Z+1, N)}^{\mathrm{constit}}\bigr)}
       {\mathrm{tr}_M\!\bigl(\beta_{(Z, N)}^{\mathrm{constit}}\bigr)}
  \;=\; (2q - 1) \,+\, O(h^4)
  \quad\text{at }q_0.
$$
This is the content of
`conj:constit-factor-2q-minus-1`
(Phase 5g, $0.033\%$ rel. err.).  Combining $(\star)$ with the
constit-side conjecture yields the **full per-Z $\mathrm{tr}_M$ step**
$$
  \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
  \;=\; z \cdot (2q - 1) \,+\, O(h^4)
  \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} \,+\, O(h^4).
$$
