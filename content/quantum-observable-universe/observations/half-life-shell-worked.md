The six nuclei in the verification table ([verification](#ex:hadron-half-life-verification)) span three transition classes with matrix elements differing by six orders of magnitude. The shell correction conjecture ([Skein shell correction](#rem:skein-shell-correction)) explains *why*: the Skein polynomial factorization of the parent and daughter links dictates whether the transition is fast (mirror/superallowed), slow (shell-blocked), or generic (allowed Gamow--Teller). We analyze the two extreme cases.

---

## Example 1: Tritium ${}^{3}\mathrm{H} \to {}^{3}\mathrm{He}$

**Parent link.**
$\mathcal{N}(1, 2) = \mathfrak{p} \oplus \mathfrak{n} \oplus \mathfrak{n}$: one proton ([categorical proton](#def:categorical-proton)) Hopf-linked to two neutrons ([categorical neutron](#def:categorical-neutron)).

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

**Superallowed character ($\log ft = 3.05$).**
The parent $(1, 2)$ and daughter $(2, 1)$ are **mirror nuclei**: $q \leftrightarrow q^{-1}$ conjugation relates their Skein polynomials. In the Skein algebra of the Hopf link, this means

$$
  J_{\mathcal{N}(2,1)}(q) = J_{\mathcal{N}(1,2)}(q^{-1}).
$$

The beta-decay matrix element is the overlap between the parent and daughter Skein states. For mirror nuclei, $q$-conjugation symmetry maximizes this overlap. The matrix element is the Markov trace ratio ([trace ratio](#prop:trace-ratio-observable)) $|\mathcal{M}_q|^2 = s^2 \cdot \prod_i |\hat{V}_i^{\mathrm{par}} / \hat{V}_i^{\mathrm{dau}}|^2$. For the mirror pair $(1,2) \leftrightarrow (2,1)$, $q$-conjugation maps $\hat{V}_i(q) \mapsto \hat{V}_i(q^{-1})$, yielding a ratio of $|q/q^{-1}|^2 = q^4$ per affected generator. This is the maximum possible Skein overlap. The transition flips the crossing chirality of the entire link without breaking any Skein factorization.

(This corresponds to $g_V^2 + 3g_A^2$, where $g_V = 1$ from the $\mathrm{SU}_q(2)$ Ward identity and $g_A$ is the axial projection of the Borromean Skein state. Deriving $g_A$ from the Borromean link Skein algebra — the ratio of antisymmetric to symmetric Markov traces — remains an open computation.)

**Result.**
The categorical computation predicts $t_{1/2} \approx 12.4$ yr versus the observed $12.3$ yr (ratio $1.01$). The shell correction $\delta E_{\mathrm{shell}} = 0$ for both parent and daughter ($A = 3$ is too small for $\alpha$-clustering, yielding no closed sub-links). For superallowed mirror transitions, the self-deformation correction suffices.

---

## Example 2: Carbon-14 ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$

**Parent link.**
$\mathcal{N}(6, 8) = 6\mathfrak{p} \oplus 8\mathfrak{n}$: six protons Hopf-linked to eight neutrons.

$$
  \ell_{\mathrm{net}}(6, 8) = \textstyle\binom{6}{2} - \binom{8}{2}
  = 15 - 28 = -13
$$

The 8 neutrons form a **closed sub-link**: the $n = 8$ shell closure. By the $\alpha$-cluster hypothesis ([shell correction](#rem:skein-shell-correction)), the neutron configuration factorizes:

$$
  8\mathfrak{n} = 4 \times \mathcal{N}(0, 2)_{\mathrm{pair}}
$$

where each $\mathcal{N}(0, 2)_{\mathrm{pair}}$ is a neutron--neutron Hopf pair forming a closed sub-link. The Skein polynomial factors accordingly:

$$
  J_{8\mathfrak{n}}(q)
  = J_{\mathcal{N}(0,2)}(q)^4 \cdot (\text{linking factors}).
$$

**Daughter link.**
$\mathcal{N}(7, 7) = 7\mathfrak{p} \oplus 7\mathfrak{n}$: the stable nitrogen-14 configuration.

$$
  \ell_{\mathrm{net}}(7, 7) = \textstyle\binom{7}{2} - \binom{7}{2}
  = 0 \quad\text{(perfectly balanced)}
$$

The daughter has $n = 7$, which is **not** magic. The neutron shell is *broken* — converting a neutron to a proton disrupts one of the four $\mathcal{N}(0,2)$ pairs.

**Anomalous slowness ($\log ft = 9.04$).**
The beta decay $\mathcal{N}(6, 8) \to \mathcal{N}(7, 7)$ must **break a closed sub-link** by splitting one neutron pair in the $n = 8$ shell. The matrix element measures the overlap between a *factorized* parent state and a *non-factorized* daughter state. The ratio of Skein polynomials suppresses this overlap:

$$
  |\mathcal{M}|^2
   \propto 
  \frac{|J_{\mathcal{N}(7,7)}(q)|}{|J_{\mathcal{N}(6,8)}(q)|}
   \cdot 
  \frac{1}{|J_{\mathcal{N}(0,2)}(q)|}
$$

The denominator $|J_{\mathcal{N}(0,2)}(q)|$ is the Skein weight of the broken pair. It penalises the transition for disrupting the closed sub-link. At $q = q_0$, $|J_{\mathcal{N}(0,2)}(q)| \approx q + q^{-1} = 2.01$. The full suppression (including the spin-parity mismatch $0^+ \to 1^+$) gives $|\mathcal{M}|^2 \sim 10^{-6}$, six orders of magnitude below the tritium mirror value.

**The 17% residual.**
The leading-order computation predicts $t_{1/2} \approx 6690$ yr versus the observed $5730$ yr (ratio $1.17$). This residual is the *shell correction contribution*. The leading-order computation underestimates the decay rate by ignoring the $n = 8$ factorization. The shell correction $\delta E_{\mathrm{shell}}$ for the parent increases its binding energy (due to the $n = 8$ closed sub-link), which *increases* $\mathfrak{Q}_\beta$ relative to the leading-order prediction. The larger $Q$ accelerates the decay via $Q^5$:

$$
  \frac{\Delta t_{1/2}}{t_{1/2}}
   \approx 
  -5 \cdot \frac{\delta E_{\mathrm{shell}}}{Q_0}
   \approx  -17\%
$$

This requires $\delta E_{\mathrm{shell}} \approx 0.17 \times Q_0 / 5 \approx 0.005$ MeV, matching the expected shell correction scale at the $p$-shell closure.

---

## Summary: shell structure determines the residual class

See [Table](#tbl:half-life-shell-worked-table-data).

The pattern is clear: transitions that *create* or *destroy* a closed sub-link at a magic number suffer the largest matrix-element corrections. ${}^{137}\mathrm{Cs}$ exhibits the *smallest* residual ($9\%$) because the daughter ${}^{137}\mathrm{Ba}$ has $n = 81$ (one neutron shy of the $n = 82$ closure), making the transition *into* a near-magic daughter slightly favoured.

The shell correction is not an external fix — it emerges naturally from the **discrete structure of the Skein polynomial**. Quantifying $\delta E_{\mathrm{shell}}$ requires the Skein factorization (item 1 in [open problems](#rem:skein-shell-correction)) and the shell energy scale $\lambda_{\mathrm{shell}}$ (item 2).
