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

### The three factors are one bar-orbit

Writing $\overline{\phantom{x}}$ for the involution $q \mapsto q^{-1}$, the
positive and negative factors are **bar-conjugates of each other**:

$$
  \overline{z} \;=\; \frac{q^{-3}}{q^{-2}+1} \;=\; \frac{1}{q\,(q^{2}+1)}
  \;=\; z - h .
$$

So $f_{pp} = z$ and $f_{nn} = \overline{z}$, and the p-n factor is exactly
their mean,

$$
  z - \tfrac{h}{2} \;=\; \tfrac{1}{2}\bigl(z + \overline{z}\bigr),
$$

which is the bar-symmetriser of $z$ — manifestly bar-even. The name
"bar-invariant p-n interface" is therefore literal rather than descriptive:
the p-n factor is not merely *a* bar-invariant choice, it is *the*
bar-symmetrisation of the p-p factor.

This also fixes where a flavour weighting can act. The colour-tube-weighted
form of the p-n factor is the same mean, **tilted**:

$$
  z - h\Bigl(\tfrac{1}{2} - \tfrac{\delta}{4}\Bigr)
  \;=\; w_{p}\, f_{pp} + w_{n}\, f_{nn},
  \qquad
  w_{p} = \tfrac{1}{2} + \tfrac{\delta}{4},
  \quad
  w_{n} = \tfrac{1}{2} - \tfrac{\delta}{4},
  \quad
  w_{p} + w_{n} = 1,
$$

with $\delta$ the substrate flavour split of
[`prop:flavor-split-substrate`](#prop:flavor-split-substrate). A like-flavour
bond has no mean to tilt — averaging $f_{pp}$ with itself returns $f_{pp}$ for
any weights summing to one — which is why the weighting is defined at the p-n
interface and nowhere else.

**The tilt is not bar-invariant.** $\delta$ is bar-mixed,
$\overline{\delta} = -q^{2}\delta$, and

$$
  \overline{f^{\,\mathrm{weighted}}_{pn}} - f^{\,\mathrm{weighted}}_{pn}
  \;=\; \frac{(q-1)^{5}(q+1)^{3}(q^{2}+1)}{12\,q^{5}},
$$

nonzero for $q \neq 1$ (about $1.67 \times 10^{-5}$ at the substrate anchor).
The unweighted factor above is the only one of the two that is bar-even, and
the derivation in this proof — trace-linearity from the single Markov axiom —
yields that one. The weighted form requires $\delta$ as an additional input
and is therefore not obtained here.

### The obstruction is one factor of $q^{2}$, and it is repairable

Write a general weighted p-n factor with offset $\varepsilon$,
$f_{pn}(\varepsilon) = (\tfrac12 + \varepsilon) f_{pp} + (\tfrac12 - \varepsilon) f_{nn}$.
Since $f_{nn} = \overline{f_{pp}}$, the involution *swaps* the two terms, so

$$
  \overline{f_{pn}} - f_{pn}
  \;=\; -\bigl(\overline{\varepsilon} + \varepsilon\bigr)\,\frac{q^{2}-1}{q},
$$

which vanishes **iff $\overline{\varepsilon} = -\varepsilon$** — the offset must
be bar-**odd**. (Not bar-even: symmetrising the weight is the wrong repair.)

The colour weighting uses $\varepsilon = \delta/4$, and
$\overline{\delta} = -q^{2}\delta$, so it misses bar-oddness by exactly a factor
of $q^{2}$ and nothing else. That factor localises: in the factored form
$\delta \sim \hbar_q^{2}\, h_q\, [2]_q$ of
[`prop:flavor-split-substrate`](#prop:flavor-split-substrate), the Hecke
crossing $h_q$ is already bar-odd and the doublet integer $[2]_q$ is bar-even,
so the **entire** obstruction is the $\hbar_q^{2}$ prefactor — the two quanta of
substrate Planck action.

Consequently a bar-invariant colour weighting **exists**: $\varepsilon = q\,\delta\,E/4$
is bar-odd for *any* bar-even $E$, since $\overline{q\delta} = -q\delta$. Two
natural members are $E = 1$ and $E = [2]_q/2$ (the latter being the bar-odd
projection of $\delta$), differing from the current offset by 11–12 % and hence
by order $8 \times 10^{-6}$ in $f_{pn}$.

**Bar-invariance is necessary but not sufficient.** It fixes the parity and
leaves a whole bar-even function $E$ free, so it does not by itself determine
the weighting; selecting $E$ requires re-deriving the colour weighting from the
colour-tube geometry, and no particular $E$ is asserted here. All of the above
is checked exactly in
[`pn_interface_bar_structure_probe.py`](../../../computations/probes/pn_interface_bar_structure_probe.py)
(17 assertions), and the four identities that are field-theoretic rather than
substrate-specific — $\overline{z} = z - h$, the bar-symmetriser form, the bar
defect $-(\overline{\varepsilon} + \varepsilon)h$, and the bar-even-iff-offset-bar-odd
equivalence — are formalised over an arbitrary characteristic-zero field in
[`QOU/MassTheory/PnInterfaceBarStructure.lean`](../lean/QOU/MassTheory/PnInterfaceBarStructure.lean),
sorry-free (`#print axioms`: `propext`, `Classical.choice`, `Quot.sound` only).

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

### Constit-side companion identity (conjectural)

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
($0.033\%$ rel. err.).  Combining $(\star)$ with the
constit-side conjecture yields the **full per-Z $\mathrm{tr}_M$ step**
$$
  \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
  \;=\; z \cdot (2q - 1) \,+\, O(h^4)
  \;=\; \frac{2q - 1}{q^{1/2} + q^{-1/2}} \,+\, O(h^4).
$$
