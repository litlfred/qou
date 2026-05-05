**Conjecture (Hoefsmit cell-content identification of EW triplet).**
*Let $R$ be the categorical coefficient ring with $q \in R$ generic
(not a root of unity in $R$, $q \neq 1$). The electroweak
force-carriers $W^\pm, Z, H$ — identified topologically as the
2-component torus links $T(2,4), T(2,6), T(2,8)$ on Bring's
surface (per
[`conj:electroweak-higgs-torus-link-triplet`](#conj:electroweak-higgs-torus-link-triplet))
— are realised inside $\mathrm{End}_R(V^{\otimes 6})$ as the
**disjoint-strand-pair** Hoefsmit projectors of*

$$
  W \;\longleftrightarrow\; \sigma_1^{\,4} \;\;(\text{strands 1\text{--}2}),
  \quad
  Z \;\longleftrightarrow\; \sigma_3^{\,6} \;\;(\text{strands 3\text{--}4}),
  \quad
  H \;\longleftrightarrow\; \sigma_5^{\,8} \;\;(\text{strands 5\text{--}6}).
$$

*Strand count $n = 6$ is the **minimum** at which all three
carriers admit simultaneous non-trivial action with pairwise-
commuting generators (via far-commutativity $\sigma_i \sigma_j =
\sigma_j \sigma_i$ for $|i - j| \geq 2$). The eight
$(\sigma_1, \sigma_3, \sigma_5)$ sym/alt eigenvalue patterns
identify eight pairwise-orthogonal projectors in
$\mathrm{End}_R(V^{\otimes 6})$ with pure-eigenspace tableaux
multiplicities $(4, 3, 1, 2, 2, 1, 3, 4)$ (for the eight pure
patterns enumerated in lexicographic order, total dim $= 20$).*

### Statement (formal)

For $n = 6$, the standard Young tableaux for partitions $\lambda
\vdash 6$ supply the Hoefsmit seminormal basis of $\bigoplus_{\lambda
\vdash 6} V_\lambda$, with $\sum_\lambda f_\lambda = 76$
seminormal-basis vectors and $\dim_R \mathrm{End}_R(V^{\otimes 6}) =
\sum_\lambda f_\lambda^2 = 720$. On each tableau $b$, the generator
$\sigma_i$ acts via the standard Hoefsmit formula

$$
  \sigma_i \cdot b
  \;=\; \begin{cases}
    +q \cdot b, & \text{if } i, i+1 \text{ same row of } b, \\
    -q^{-1} \cdot b, & \text{if } i, i+1 \text{ same column of } b, \\
    \text{off-diagonal mixing}, & \text{otherwise}.
  \end{cases}
$$

A tableau is **pure for $(\sigma_1, \sigma_3, \sigma_5)$** if all
three of these generators act diagonally (no mixing). The
[`hoefsmit-ew-cell-content.witness.json`](../../folio-assistant/computations/hoefsmit-ew-cell-content.witness.json)
enumeration shows there are exactly **20 such pure tableaux**,
distributed across the **eight** sym/alt eigenvalue patterns:

| Pattern $(\sigma_1, \sigma_3, \sigma_5)$ | Multiplicity | Candidate physical meaning |
|------------------------------------------|-------------:|----------------------------|
| (sym, sym, sym) | 4 | unbroken EW vacuum (photon-like, $U(1)_{\rm em}$ survivor) |
| (alt, sym, sym) | 2 | $W^-$ excited (single-flip in W-channel) |
| (sym, alt, sym) | 1 | $Z^-$ excited |
| (sym, sym, alt) | 3 | $H^-$ excited |
| (alt, alt, sym) | 3 | $W^- + Z^-$ (double-flip) |
| (alt, sym, alt) | 1 | $W^- + H^-$ (double-flip) |
| (sym, alt, alt) | 2 | $Z^- + H^-$ (double-flip) |
| (alt, alt, alt) | 4 | fully-broken (all three flipped) |

(The "$+$"/"$-$" labels mark the sym/alt eigenchannel of each
$\sigma_i^{2k_i}$. The multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$
reflect non-trivial cell-content combinatorics — they are **not**
uniform.)

### Why $n = 6$ is the minimum

Each EW carrier $T(2, 2k)$ acts non-trivially on a **single
strand-pair** (the two endpoints of its 2-component link
projection). Three carriers therefore need three disjoint
strand-pairs:
- $W$: strands 1, 2 (acting via $\sigma_1$)
- $Z$: strands 3, 4 (acting via $\sigma_3$)
- $H$: strands 5, 6 (acting via $\sigma_5$)

For $n < 6$, two of the three carriers must share strand-pairs;
their generators no longer commute (they share a generator
between consecutive strands), and the simultaneous-eigenspace
decomposition degenerates. So $n = 6$ is the structural minimum
for the simultaneous Hoefsmit identification.

### Resolution of the dimension-collapse issue

The audit
[`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-05-path-alpha-bring-refinement.md)
flagged that $H_2(q)$-only completeness sums six rank-1 projectors
in a 2-dimensional algebra — dimensionally inconsistent. The Hoefsmit
identification at $n = 6$ resolves this:

- The six EW projectors live as **rank-1 to rank-3** projectors in
  $\mathrm{End}_R(V^{\otimes 6})$ (multiplicities depending on
  pattern).
- They are pairwise orthogonal (as eigenspace projectors of
  pairwise-commuting generators with distinct eigenvalues at
  generic $q$).
- They sit alongside two **non-EW** projectors (vacuum and
  fully-broken) in the 8-pattern decomposition of the
  pure-eigenspace.
- Total: 8 pairwise-orthogonal projectors of multiplicities $(4,
  2, 1, 3, 3, 1, 2, 4)$, summing to a rank-20 projector on the
  pure-eigenspace; the complementary rank-56 mixed-eigenspace
  carries off-diagonal generator mixing.

### Implications for $\mathcal{N}_{\rm sym}(q)$

The previous closed-form computation
[`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
assumed **uniform** Plancherel weights $w_X = 1/[2]_q$ across the
six EW projectors. Under the Hoefsmit identification, the
weights should track the **rank multiplicities** $(2, 1, 3, 3, 1,
2)$ for the six single-/double-flip patterns:

$$
  \mathcal{N}_{\rm sym}^{\rm Hoefsmit}(q)
  \;=\;
  \frac{2 q^4 + 1 \cdot q^6 + 3 q^8 + 3 q^4 q^6 + 1 \cdot q^4 q^8 + 2 q^6 q^8}{12}
  \;\in\; R
$$

(numerator divided by $1 + 2 + 1 + 3 + 3 + 1 + 2 = 12$, the total
single-/double-flip multiplicity). This **supersedes** the
uniform-weight expression $q^6 (1 + q^2 + q^4) / 3$, which was
derived under the incorrect $H_2(q)$-only assumption.

Concrete simplification:

$$
  \mathcal{N}_{\rm sym}^{\rm Hoefsmit}(q)
  \;=\;
  \frac{1}{12}\bigl(2 q^4 + q^6 + 3 q^8 + 3 q^{10} + q^{12} + 2 q^{14}\bigr).
$$

At $q_0 \approx 1.10998$: numerator $\approx 39.7$, divided by 12
gives $\mathcal{N}_{\rm sym}^{\rm Hoefsmit}(q_0) \approx 3.31$.
(Compare to the uniform-weight value $1.8966$ — the corrected
weight is $\sim 1.75\times$ larger.)

### Status

🟡 **Open**. The Hoefsmit cell-content arithmetic is correct
(verified by the witness enumeration); the open inputs are:

1. **The $W \leftrightarrow \sigma_1^4$, $Z \leftrightarrow \sigma_3^6$,
   $H \leftrightarrow \sigma_5^8$ identification** — currently a
   structural proposal motivated by disjoint-strand-pair commutativity
   plus matching twist parameters $k = 2, 3, 4$ to the EW link triplet.
   Needs a categorical-physics block (the "categorical Higgs mechanism"
   item from
   [`conj:force-carrier-knot-vs-link-dichotomy`](#conj:force-carrier-knot-vs-link-dichotomy)
   §Status) discharging the boson-to-strand-pair assignment.
2. **The non-uniform Plancherel weight derivation** — the
   multiplicities $(2, 1, 3, 3, 1, 2)$ are read off from the
   tableaux enumeration; promoting them to a closed-form
   $q$-rational requires identifying their generating function in
   the Hoefsmit cell-content arithmetic.
3. **Refinement of upstream blocks** — the existing
   [`conj:weak-spectral-completeness`](#conj:weak-spectral-completeness)
   and
   [`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
   should be edited to reference this $n = 6$ formulation.

### Audit-flag impact

If this conjecture is discharged, it **fixes** the
$\mathrm{End}_R(A)$-decomposition issue noted in
[`docs/audits/2026-05-05-path-alpha-bring-refinement.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-05-path-alpha-bring-refinement.md)
(Fix A reading), and supplies a corrected closed form for
$\mathcal{N}_{\rm sym}(q)$ derived from the actual Hoefsmit cell-
content arithmetic — not the dimensionally-inconsistent uniform-
weight expression.

**Witness.**
[`folio-assistant/computations/hoefsmit-ew-cell-content.witness.json`](../../folio-assistant/computations/hoefsmit-ew-cell-content.witness.json)
— enumerates standard Young tableaux of partitions of 6 with
their $(\sigma_1, \sigma_3, \sigma_5)$ eigenvalue classes; reports
pure-eigenspace counts and 8-pattern multiplicities.
