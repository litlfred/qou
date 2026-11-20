### Proof (Markov axiom + Hecke skein)

For a positive interface generator $\sigma_g$, the **Markov axiom**
([Existence and non-degeneracy of the Markov trace (Jones, 1987)](#thm:jones-markov-trace)) gives
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
These two identities apply when the interface generator is the last
letter. In $\mathcal{B}_K$ an interface generator sits *between* two
blocks, so the iteration needs a block-multiplicativity lemma.

**Lemma (block multiplicativity).** Let $x \in H_{k+1}(q)$, let
$y \in H_m(q)$, and let $\mathrm{sh}_{k+1}(y)$ be $y$ with every
$\sigma_i$ replaced by $\sigma_{i+k+1}$. Then
$$
  \mathrm{tr}_M\bigl(x\,\mathrm{sh}_{k+1}(y)\bigr) = \mathrm{tr}_M(x)\,\mathrm{tr}_M(y),
  \qquad
  \mathrm{tr}_M\bigl(x\,\sigma_k\,\mathrm{sh}_{k+1}(y)\bigr) = z\,\mathrm{tr}_M(x)\,\mathrm{tr}_M(y).
$$

*Proof.* Put $a = x$ or $a = x\sigma_k$; in both cases $a$ lies in
$H_{k+2}(q)$. Consider the linear map $y \mapsto \mathrm{tr}_M(a\,\mathrm{sh}_{k+1}(y))$.
For $m = 1$ it gives $\mathrm{tr}_M(a)$. For $m \ge 2$, write a basis
element of $H_m(q)$ as $T_u\,\sigma_{m-1}\,T_v$ with $u, v \in S_{m-1}$, or
as $T_u$ with $u \in S_{m-1}$. In the first case $\mathrm{sh}(T_v)\,a\,\mathrm{sh}(T_u)$ lies in
$H_{m+k}(q)$, so cyclicity, the Markov property for the top generator
$\sigma_{m+k}$, and cyclicity again give
$$
  \mathrm{tr}_M\bigl(a\,\mathrm{sh}(T_u)\,\sigma_{m+k}\,\mathrm{sh}(T_v)\bigr)
  = z\,\mathrm{tr}_M\bigl(\mathrm{sh}(T_v)\,a\,\mathrm{sh}(T_u)\bigr)
  = z\,\mathrm{tr}_M\bigl(a\,\mathrm{sh}(T_u T_v)\bigr).
$$
In the second case $\mathrm{sh}(T_u)$ lies in $H_{m+k}(q)$ and the trace
restricts. This is the same recursion that computes $\mathrm{tr}_M(y)$ from
$\mathrm{tr}_M(1) = 1$, so the map equals $\mathrm{tr}_M(a)\,\mathrm{tr}_M(y)$.
The Markov property gives $\mathrm{tr}_M(x\sigma_k) = z\,\mathrm{tr}_M(x)$. $\square$

Now write $\mathcal{B}_K = b_1\,\varepsilon_1\,b_2\,\varepsilon_2 \cdots
\varepsilon_{A-1}\,b_A$, where $b_i$ is the word of the $i$-th nucleon on
its own block of strands and $\varepsilon_i = \sigma_{g_i}^{\pm 1}$ joins
blocks $i$ and $i+1$; the vacuum braid is $b_1 b_2 \cdots b_A$. Applying
the lemma $A - 1$ times, with $\sigma^{-1} = \sigma - h$ for the negative
connectors, gives $\mathrm{tr}_M(\mathcal{B}_K) = z^{p_+}(z-h)^{p_-}
\prod_i \mathrm{tr}_M(b_i)$, and $\mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}})
= \prod_i \mathrm{tr}_M(b_i)$. Dividing yields the boxed identity
($\star$). An exact check over $\mathbb{Q}$ at $q = 2$ (three blocks on
nine strands, one positive and one negative connector) reproduces
$z(z-h)$.

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
[Substrate-pure derivation of the $u$--$d$ flavor split](#prop:flavor-split-substrate). A like-flavour
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
[Substrate-pure derivation of the $u$--$d$ flavor split](#prop:flavor-split-substrate), the Hecke
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
using only the axioms `propext`, `Classical.choice` and `Quot.sound`.

### Full-trace verification at convention D (4 atoms)

$\mathrm{tr}_M$ is evaluated as $\sum_\lambda y_\lambda\,\chi_\lambda$ with the
convention-D weights at $z = q^3/(q^2+1)$ and Hoefsmit characters in MPFR at the
proton pin $q_0$, for $H_n$ with $n \in \{6, 9, 12\}$; averaged letters are expanded
by linearity, and the route is checked against the independent Markov-ascent trace
before use. Census word ($p$-$n$ interface $=\sigma_g$, as listed below):

| atom | $A$ | $p_+$ | $p_-$ | $\mathrm{tr}_M^{\mathrm{FULL}}/\mathrm{tr}_M^{\mathrm{CONSTIT}}$ | predicted $z^{p_+}(z-h)^{p_-}$ | rel. err. |
|---|:-:|:-:|:-:|---:|---:|---:|
| D    | 2 | 1 | 0 | 0.61268804 | 0.61268804 | $4\times10^{-51}$ |
| T    | 3 | 1 | 1 | 0.24729789 | 0.24729789 | $2\times10^{-50}$ |
| ${}^{3}$He  | 3 | 2 | 0 | 0.37538663 | 0.37538663 | $3\times10^{-50}$ |
| ${}^{4}$He  | 4 | 2 | 1 | 0.15151646 | 0.15151646 | $4\times10^{-51}$ |

The live canonical word carries the bar-invariant colour-weighted $p$-$n$ letter
$\sigma_g - h(\tfrac12 - \tfrac{\delta}{4})$ instead of $\sigma_g$; with that factor in
place of $z$ the ratios are $\approx 0.50822979$, $0.20513564$, $0.31138631$ and
$0.12568415$, again equal to the predicted product to $\le 5\times10^{-50}$ (and
likewise for the colour-blind $\sigma_g - h/2$). The identity ($\star$) therefore holds
at convention D on every word tested, at the $10^{-50}$ floor of the arithmetic.

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
`conj:constit-factor-2q-minus-1`, whose $0.033\%$ agreement was measured at the
excised convention-C weight on the earlier grouped intra-nucleon word.

**The step does not survive at convention D.** The constituent product is
multiplicative over disjoint strand blocks (checked to $10^{-50}$), so the constit
step is the single-proton trace $\mathrm{tr}_M(\beta_p)$. At $z = q^3/(q^2+1)$ and
$q_0$ this is $\approx 0.62932840$ on the canonical (alternating) word and
$\approx 1.14575969$ on the grouped word, against $2q_0 - 1 \approx 1.21995717$:
misses of $48.4\%$ and $6.1\%$. The full per-$Z$ step on the canonical word is
correspondingly $\approx 0.38558198$, not $q^3(2q-1)/(q^2+1) \approx 0.7475$. This is a
scope-limited negative: the identification $(2q-1)$ for the constit factor does not
hold at convention D for either intra-nucleon ordering; it says nothing about
whether some other closed form describes the D-frame step. The C-era formula
$\tfrac{2q-1}{q^{1/2}+q^{-1/2}}$ is kept only as a historical form.
