*The per-unit-excess magic-shell coupling slope $\kappa$, which controls the $(n_{pp} - n_{nn})$ excess contribution to atomic binding at the single-magic anchors $(Z, N) = (2, 1)$ and $(1, 2)$, is conjectured to admit the closed categorical form*

$$
  \boxed{\,
  \kappa \;=\; -\,\frac{E_0 \cdot \log(1/h)}{[2]_q \cdot [3]_q}
  \,}
$$

*where $E_0 = m_e / (q(q-1))$ is the Hecke energy scale, $h = q - q^{-1}$ is the Hecke deformation parameter, and $[n]_q = (q^n - q^{-n}) / (q - q^{-1})$ is the q-bracket.*

## Why this is a conjecture and not a proposition

The shape of the right-hand side was not derived from the categorical substrate. Both of its factors were identified against the $(2,2)$ doubly-magic anchor: the magic-shell quantum $E_0 \cdot \log(1/h)$ and the normalization $[2]_q \cdot [3]_q$ were selected so that the expression reproduced the coupling slope measured there. An expression obtained that way is a fit, whatever the structural motivation attached to its factors afterwards.

The three-calibration discipline admits exactly three inputs — $m_e$, $\mathfrak{D}_\beta$, and $\mathfrak{D}_\pi$ — so there is no fourth calibration slot into which an anchor-identified form could be declared. That leaves two dispositions for a block of this kind, and only one of them is honest: demote it to a conjecture. The alternative, a provable block kind carrying an acknowledgement that its content was fitted, states a fit in the voice of a derivation.

What remains open is therefore not the arithmetic but the derivation: whether $-E_0 \log(1/h) / ([2]_q [3]_q)$ can be obtained from the substrate without consulting the anchor at all.

## Numerical evidence

Evaluating at the substrate parameter $q_0 = 1.109978595554181\ldots$:

$$
  \kappa_{\mathrm{categorical}} \approx -\frac{4.1860 \cdot 1.5651}{6.1206}
  \approx -1.0704239\;\text{MeV}
$$

Against the observed physical value at the single-magic anchors:

$$
  \kappa_{\mathrm{observed}} \approx -1.0707908\;\text{MeV}
$$

The ratio is $0.999657$, a relative residual of

$$
  \delta \;=\; \left| \frac{\kappa_{\mathrm{categorical}} - \kappa_{\mathrm{observed}}}{\kappa_{\mathrm{observed}}} \right|
  \;\approx\; 3.4 \times 10^{-4}.
$$

Two things are worth separating here. The anchors $(2,1)$ and $(1,2)$ were **not** used to fix the form — that was done at $(2,2)$ — so the agreement at them is a genuine cross-check rather than a restatement of the fit. That is the whole of the evidence for the conjecture. But $\delta \approx 3.4 \times 10^{-4}$ is not zero, and nothing in the present account says what it is. It is recorded here as an open quantity, not absorbed into the word "agreement": a derivation of the closed form would have to either predict $\delta$ or predict a corrected form that removes it.

## Structural motivation

The two factors carry the following readings, which motivate the shape but do not derive it.

1. **H7a energy quantum** $E_0 \cdot \log(1/h)$ — the per-shell magic-coupling magnitude, read as the logarithm of the Hecke deformation.
2. **q-factorial normalization** $[2]_q \cdot [3]_q = [3]_q!$, normalizing the H7a quantum to a per-excess slope.

The second factor was previously described as the quantum dimension of a $V_2 \otimes V_3$ Schur–Weyl tensor product. That description does not survive inspection, in two ways. It collides with the eightfold chapter's Schur–Weyl decomposition, which at $n = 3$ has $\mathfrak{gl}_3$ factors of dimension $10$, $8$ and $1$ — a different object sharing the name. And it presents as a product of *two* channel indices what is a *single* q-factorial: $[2]_q [3]_q = [3]_q!$, proved in the Lean sibling as `qBracket_normaliser_eq_qFactorial`.

The q-factorial reading connects the normalization to objects already load-bearing elsewhere in the framework. The Borromean observable is $F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| \cdot [3]_q! / q^3$, and the q-Schur Markov weight of the trivial partition is $y_{(3)}(q) = q^3 / [3]_q!$. So the normalization is

$$
  [2]_q \cdot [3]_q \;=\; [3]_q! \;=\; \frac{q^3}{y_{(3)}(q)},
$$

the inverse Markov weight of $(3) \vdash 3$. This is a reading of the existing expression, not a new claim about $\kappa$: it changes what the denominator *is*, not what it evaluates to.

$$
  \kappa \;=\; \underbrace{-E_0 \cdot \log(1/h)}_{\text{H7a quantum}}
  \;\cdot\; \underbrace{\frac{1}{[2]_q \cdot [3]_q}}_{\text{LR-fusion normalization}}
$$

The negative sign tracks the orientation convention for the $(n_{pp} - n_{nn})$ excess. Unlike the shape itself, the sign is not fitted: it follows from $E_0 > 0$, $\log(1/h) > 0$ for $0 < h < 1$, and $[2]_q, [3]_q > 0$ at $q > 1$, and is proved in the Lean sibling as `kappaClosed_neg`.

## What would settle it

The conjecture is discharged by a derivation of the closed form from the substrate that does not consult a magic anchor at any step. Three structural facts already available constrain such a derivation.

The sign is forced, as above. The $q$-brackets in the denominator are the canonical balanced brackets, tied to `QOU.QInteger.qIntBal` by `qBracket_eq_canonical`, so the normalization is not free to be reinterpreted as a geometric or rescaled bracket. And the denominator is the q-factorial $[3]_q!$, hence $q^3 / y_{(3)}(q)$, which gives the missing piece a categorical handle: a derivation must say which partition's Markov weight appears, and why.

That last point also delimits what the present agreement establishes. Both the index of the q-factorial and the definition of the excess $(n_{pp} - n_{nn})$ admit more than one reading in the corpus, and every reading coincides at the $A = 3$ anchors — the only anchors $\kappa$ has been evaluated at. The readings diverge from the $A_{\mathrm{magic}} = 8$ shell upward. So the $0.034\%$ agreement is evidence about the value at $A = 3$ and carries little information about $\kappa$ away from it; a shell-8 evaluation performed before those two readings are fixed would measure the choice rather than the physics.
