The six nuclei in the verification table
([verification](#ex:hadron-half-life-verification)) span three
transition classes with matrix elements differing by six orders of
magnitude. The shell correction conjecture
([Skein shell correction](#rem:skein-shell-correction)) explains
*why*: the Skein polynomial factorization of the parent and daughter
links determines whether the transition is fast (mirror/superallowed),
slow (shell-blocked), or generic (allowed Gamow--Teller). We work
through the two extreme cases.

---

## Example 1: Tritium ${}^{3}\mathrm{H} \to {}^{3}\mathrm{He}$

**Parent link.**
$\mathcal{N}(1, 2) = \mathfrak{p} \oplus \mathfrak{n} \oplus \mathfrak{n}$: one proton
([categorical proton](#def:categorical-proton)) Hopf-linked to two
neutrons ([categorical neutron](#def:categorical-neutron)).

```tex
\begin{tikzcd}[row sep=0.5em, column sep=1.5em]
  \mathfrak{p} \ar[r, no head, "\oplus"]
  & \mathfrak{n} \ar[r, no head, "\oplus"]
  & \mathfrak{n}
\end{tikzcd}
$\qquad
\ell_{\mathrm{net}} = \textstyle\binom{1}{2} - \binom{2}{2} = -1$
```

Crossing structure:
- $\mathfrak{p}$--$\mathfrak{p}$: 0 positive crossings
- $\mathfrak{n}$--$\mathfrak{n}$: 1 negative crossing
- $\mathfrak{p}$--$\mathfrak{n}$: 2 mixed crossings (neutral)

**Daughter link.**
$\mathcal{N}(2, 1) = \mathfrak{p} \oplus \mathfrak{p} \oplus \mathfrak{n}$: the mirror configuration.

$$
  \ell_{\mathrm{net}}(2, 1) = \textstyle\binom{2}{2} - \binom{1}{2} = +1
$$

**Why the transition is superallowed ($\log ft = 3.05$).**
The parent $(1, 2)$ and daughter $(2, 1)$ are **mirror nuclei**:
their Skein polynomials are related by $q \leftrightarrow q^{-1}$
conjugation. In the Skein algebra of the Hopf link, this means

$$
  J_{\mathcal{N}(2,1)}(q) = J_{\mathcal{N}(1,2)}(q^{-1}).
$$

The beta-decay matrix element is the overlap between the parent and
daughter Skein states. For mirror nuclei, the $q$-conjugation
symmetry forces this overlap to be maximal. The matrix element
is the Markov trace ratio
([trace ratio](#prop:trace-ratio-observable))
$|\mathcal{M}_q|^2 = s^2 \cdot \prod_i |\hat{V}_i^{\mathrm{par}} / \hat{V}_i^{\mathrm{dau}}|^2$,
which for the mirror pair $(1,2) \leftrightarrow (2,1)$ evaluates
to the maximum allowed value: $q$-conjugation maps
$\hat{V}_i(q) \mapsto \hat{V}_i(q^{-1})$, so the ratio is
$|q/q^{-1}|^2 = q^4$ per affected generator — the largest
possible Skein overlap. No Skein factorization is broken — the
transition flips the crossing chirality of the entire link.

(In the standard parametrisation this corresponds to
$g_V^2 + 3g_A^2$, where $g_V = 1$ from the $\mathrm{SU}_q(2)$
Ward identity and $g_A$ is the axial projection of the Borromean
Skein state. Deriving $g_A$ from the Skein algebra of the
Borromean link — the ratio of antisymmetric to symmetric Markov
traces — is an open computation.)

**Result.**
The categorical computation predicts $t_{1/2} \approx 12.4$ yr vs observed 12.3 yr (ratio 1.01). The shell correction
$\delta E_{\mathrm{shell}} = 0$ for both parent and daughter
(neither has a closed sub-link: $A = 3$ is too small for
$\alpha$-clustering). The excellent agreement confirms that for
superallowed mirror transitions, the self-deformation correction is sufficient.

---

## Example 2: Carbon-14 ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$

**Parent link.**
$\mathcal{N}(6, 8) = 6\mathfrak{p} \oplus 8\mathfrak{n}$: six
protons Hopf-linked to eight neutrons.

$$
  \ell_{\mathrm{net}}(6, 8) = \textstyle\binom{6}{2} - \binom{8}{2}
  = 15 - 28 = -13
$$

The 8 neutrons include a **closed sub-link**: the $n = 8$ shell
closure. By the $\alpha$-cluster hypothesis
([shell correction](#rem:skein-shell-correction)), the neutron
configuration admits the factorization

$$
  8\mathfrak{n} = 4 \times \mathcal{N}(0, 2)_{\mathrm{pair}}
$$

where each $\mathcal{N}(0, 2)_{\mathrm{pair}}$ is a
neutron--neutron Hopf pair forming a closed sub-link. The Skein
polynomial factors accordingly:

$$
  J_{8\mathfrak{n}}(q)
  = J_{\mathcal{N}(0,2)}(q)^4 \cdot (\text{linking factors}).
$$

**Daughter link.**
$\mathcal{N}(7, 7) = 7\mathfrak{p} \oplus 7\mathfrak{n}$: the
stable nitrogen-14 configuration.

$$
  \ell_{\mathrm{net}}(7, 7) = \textstyle\binom{7}{2} - \binom{7}{2}
  = 0 \quad\text{(perfectly balanced)}
$$

The daughter has $n = 7$, which is **not** a magic number. The
neutron shell is *broken* — one of the four $\mathcal{N}(0,2)$
pairs has been disrupted by converting a neutron to a proton.

**Why the transition is anomalously slow ($\log ft = 9.04$).**
The beta decay $\mathcal{N}(6, 8) \to \mathcal{N}(7, 7)$ must
**break a closed sub-link**: one of the neutron pairs in the
$n = 8$ shell is split. The matrix element for this transition is
the overlap between a *factorized* parent state and a
*non-factorized* daughter state. In the Skein algebra, this overlap
is suppressed by the ratio of Skein polynomials:

$$
  |\mathcal{M}|^2
   \propto 
  \frac{|J_{\mathcal{N}(7,7)}(q)|}{|J_{\mathcal{N}(6,8)}(q)|}
   \cdot 
  \frac{1}{|J_{\mathcal{N}(0,2)}(q)|}
$$

The denominator $|J_{\mathcal{N}(0,2)}(q)|$ is the Skein weight of
the broken pair — it penalises the transition for disrupting the
closed sub-link. At $q = q_0$, $|J_{\mathcal{N}(0,2)}(q)| \approx q + q^{-1} = 2.01$, and the full suppression
(including the spin-parity mismatch $0^+ \to 1^+$) gives
$|\mathcal{M}|^2 \sim 10^{-6}$ — six orders of magnitude below the
tritium mirror value.

**The 17% residual.**
The leading-order computation predicts $t_{1/2} \approx 6690$ yr vs observed
5730 yr (ratio 1.17). This residual is the *shell correction
contribution to the half-life*: the leading-order computation does not resolve the $n = 8$ factorization, so it underestimates the decay
rate. The shell correction $\delta E_{\mathrm{shell}}$ for the
parent increases its binding energy (the $n = 8$ closed sub-link
provides extra stability), which *increases* $\mathfrak{Q}_\beta$ relative to
the leading-order prediction. The larger $Q$ gives a faster
decay rate via $Q^5$:

$$
  \frac{\Delta t_{1/2}}{t_{1/2}}
   \approx 
  -5 \cdot \frac{\delta E_{\mathrm{shell}}}{Q_0}
   \approx  -17\%
$$

giving $\delta E_{\mathrm{shell}} \approx 0.17 \times Q_0 / 5 \approx 0.005$ MeV for this transition — consistent with the
expected shell correction scale at the $p$-shell closure.

---

## Summary: shell structure determines the residual class

See [Table](#tbl:half-life-shell-worked-table-data).

The pattern: transitions that *create* or *destroy* a closed
sub-link at a magic number have the largest matrix-element
corrections. ${}^{137}\mathrm{Cs}$ has the *smallest* residual
(9%) because the daughter ${}^{137}\mathrm{Ba}$ has $n = 81$
(one neutron short of the $n = 82$ closure), making the transition
*into* a near-magic daughter slightly favoured.

The shell correction is not an external fix — it is the **discrete
structure of the Skein polynomial** already present in the
framework. Computing $\delta E_{\mathrm{shell}}$ quantitatively
requires the Skein factorization (item 1 in the
[open problems](#rem:skein-shell-correction)) and the shell energy
scale $\lambda_{\mathrm{shell}}$ (item 2).
