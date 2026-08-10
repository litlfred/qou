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

That comparison needs a caveat larger than the residual it reports.

$\kappa_{\mathrm{observed}}$ is not a value measured at the single-magic anchors. It is the value measured at **one** of them. The fit that produced it ran at both, in the decomposition

$$
  \Delta_{\mathrm{coupling}}(Z, N) \;\approx\; [A-2]_q \cdot E_0 \log(1/h)
  \;+\; (n_{pp} - n_{nn}) \cdot \kappa \cdot h \cdot E_0,
$$

and the two anchors did not agree:

| anchor | excess | slope |
|---|---|---|
| ${}^{3}$He $(2,1)$ | $+1$ | $-1.0707908\;\text{MeV}$ |
| ${}^{3}$H $(1,2)$ | $-1$ | $+0.2023095\;\text{MeV}$ |

They differ in sign and by a factor of $5.3$. The hypothesis under test was that a single $\kappa$ holds across the anchors, and the producing computation recorded that it does not. The ${}^{3}$He arm is what became $\kappa_{\mathrm{observed}}$; the ${}^{3}$H arm was not carried forward.

Two further points follow. The fit was to $\Delta_{\mathrm{coupling}}$, which is not the atomic binding this block's opening sentence attributes to $\kappa$. And $\delta \approx 3.4 \times 10^{-4}$ is agreement with one arm of an inconsistent pair, so it measures much less than its size suggests: a residual of $3.4 \times 10^{-4}$ against a quantity whose companion measurement differs by $130\%$ carries no evidential weight of that order.

This is the whole of the numerical evidence for the conjecture.

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

## What the index counts

The q-factorial's index admits several readings that all give $3$ at the $A = 3$ anchors — the mass number $A$, the magic number plus one $A_{\mathrm{magic}} + 1$, or a constant — and they diverge from the $A_{\mathrm{magic}} = 8$ shell upward. The evidence favours the constant, and identifies what the constant counts.

The nucleon is the Borromean link, carried by the braid word $(\sigma_1 \sigma_2^{-1})^3$. That word uses the generators $\sigma_1, \sigma_2$, so $\beta_{\mathrm{Bor}} \in B_3$ and its Markov trace lives in $H_3(q)$. **The $3$ is the strand count internal to a single nucleon**, and it is the same $3$ for every nucleus, because every nucleon carries the same Borromean structure regardless of $A$ or $A_{\mathrm{magic}}$.

The identification is supported by the normalization already in use elsewhere: the Borromean observable is $F_{\mathrm{Bor}} = |\mathrm{tr}_M(\beta_{\mathrm{Bor}})| / y_{(3)}(q)$, normalizing the trace of that same 3-strand braid by that same weight. On this reading $\kappa$'s normalization is not a nuclear quantity at all — it is the Markov normalization of the nucleon's own braid — and $\kappa$ is therefore shell-independent, which is what the Lean sibling encodes by giving `kappaClosed` no shell index.

This also dissolves an apparent tension. The trivial partition $(3)$ is fully symmetric, whereas the flavour content of the $A = 3$ anchors is $\mathfrak{p}\mathfrak{p}\mathfrak{n}$ or $\mathfrak{p}\mathfrak{n}\mathfrak{n}$, of mixed symmetry $(2,1)$. The two partitions index different things: $(2,1)$ partitions the three *nucleons* of the nucleus, $(3)$ partitions the three *strands* of one nucleon. That they are both partitions of $3$ at these anchors is a coincidence of the anchors, not a conflict.

It is an identification rather than a theorem — two quantities that are numerically equal and that both normalize a Markov trace at $n = 3$. What it buys is falsifiability: it converts a three-way ambiguity into the single prediction that $\kappa$ does not vary with the shell, which a shell-8 evaluation can test once the excess convention is settled.

## What the excess counts

Two definitions of $(n_{pp}, n_{nn})$ appear in the corpus: the canonical-braid interface counts $n_{pp} = \max(0, Z-1)$, and the unordered pair counts $n_{pp} = Z(Z-1)/2$. They agree at the $A = 3$ anchors and differ by a factor of $7$ at the $8$ shell, so the anchors cannot separate them. The corpus can.

They are not competing definitions of one quantity. They are different quantities sharing a symbol. The **difference** $(n_{pp} - n_{nn})$ occurs nowhere in the corpus except here; the pair counts occur only in the **sum** $(n_{pp} + n_{nn})$, inside the isovector term $\Delta_{T=1}$, under a different normalization and a different partition. No block forms the difference of the pair counts.

The interface counts, by contrast, are introduced for exactly this purpose: their defining block states that they *encode the $Z \leftrightarrow N$ asymmetry directly*, and that *the interface asymmetry isolates the ${}^{3}$He anomaly*. A difference is what measures an asymmetry; a sum is not.

The categorical layers agree with that reading. The interface counts are a braid object — the $A-1$ inter-nucleon interface generators $\sigma_{3k+2}$ of the canonical atomic braid $\beta(Z, N) \in H_{3A}(q)$ — which is the layer $\kappa$'s normalization was placed in above. The pair count is a combinatorial quantity with no braid-generator realization in the canonical ordering.

So $\kappa$ multiplies the interface excess. Since $\max(0, m-1) - \max(0, m-2) = 1$ for every $m \geq 2$, that excess is $\pm 1$ at every single-magic mirror pair $(m, m-1)$ and $(m-1, m)$, at every shell — it does not grow with $Z$.

## The resulting prediction

With the normalization's index fixed by the nucleon's strand count and the excess fixed to the interface counts, $\kappa$'s contribution to the binding at a single-magic mirror pair is

$$
  \kappa \cdot (n_{pp} - n_{nn}) \;\approx\; \mp\,1.0704\;\text{MeV},
$$

the same value at $A_{\mathrm{magic}} = 2, 8, 20, 28, 50, 82, 126$. Neither factor varies with the shell: the first because it counts strands inside a nucleon, the second because it counts interfaces adjacent to a closed shell.

The prediction is a single number, fixed without reference to any anchor beyond $A = 3$. Any single-magic mirror pair at a higher shell can contradict it.

## The test, and its outcome

The mirror pair is the right probe, because the isoscalar bulk cancels: both nuclides share $A$, so their binding difference isolates the charge-asymmetric terms. Subtracting the electrostatic displacement leaves

$$
  \text{residual} \;:=\; \bigl[B(Z{=}m{-}1) - B(Z{=}m)\bigr] \;-\; \Delta E_{\mathrm{Coulomb}},
$$

which the prediction says should be $\approx -2.14\;\text{MeV}$ at every shell.

It is not. Measured against AME binding energies, with the electrostatic term taken from the framework's own Coulomb module (whose $\alpha_{\mathrm{EM}}$ is derived from $q_0$ rather than imported), the residual is between $0.07$ and $1.81\;\text{MeV}$ in magnitude, depending on shell and on the radius model — three to thirty times smaller than predicted.

The radius scale is the one genuinely uncertain input, so it was swept rather than chosen: the derived value $\bar\lambda_\pi$, the empirical heavy-nucleus constant $1.2\;\text{fm}$, and the value implied by the measured ${}^{3}$He charge radius. The conclusion does not depend on which is used, and the reason is structural rather than numerical: **the residual is not constant in $A$**, while the prediction is a single shell-independent number. Under the derived radius it changes sign between $A = 3$ and $A = 15$. No choice of radius converts a varying residual into a constant one.

The $A = 3$ anchor is the sharpest case, because it is where $\kappa$ was fixed. There the residual is at most $\approx 0.23\;\text{MeV}$ under any radius model, against a predicted $2.14\;\text{MeV}$ — short by at least a factor of nine.

## What this establishes, and what it does not

This is a scope-limited negative. It says that the additive, shell-independent term $\kappa \cdot (n_{pp} - n_{nn})$, set against an electrostatic baseline, does not appear in the mirror-split data. It does **not** exclude $\kappa$ as an ingredient of some other decomposition: no invariant forbidding that has been proved, and none is claimed here.

What it does establish is narrower and more useful. The empirical value $\kappa \approx -1.0708\;\text{MeV}$ was recorded as the observed slope at the single-magic anchors, but those anchors leave an order of magnitude too little room for it once electrostatics is accounted for. So that value did not come from this decomposition — and indeed it did not: it came from a fit to $\Delta_{\mathrm{coupling}}$, a different observable, as recorded above.

The two negatives are independent, which is what makes them worth having together. The mirror-split test says no term of this form and size appears in the binding data. The provenance says the value being matched was one arm of a measurement its own computation reported as inconsistent. The first could have been repaired by finding the right decomposition; the second cannot, because it concerns the number itself.
