# Whitehead 4G third instance: route decision (W2, bean qou-5wq0)

**Date**: 2026-08-02 · **Milestone**: qou-k49o (PR #4400) · **Sources**:
`library/arxiv-math-0611181v2/0611181v2.pdf` (van der Veen, arXiv:math/0611181 v2, read in
full), `library/1172-3/1172-3.pdf` (Habiro, RIMS Kōkyūroku 1172). Transcription
+ 4-anchor verification: `computations/whitehead_vdv_lemma1.py`,
`computations/whitehead-vdv-lemma1.witness.json` (all anchors PASS).

## The formula (vdV Lemma 1, transcribed)

At $t = e^{2\pi i/N}$, with
$\chi_{N,n} = e^{n(n+1-N)\pi i/(2N)}$,
$S_{n,k} = \prod_{j=1}^{n} \frac{2\sin^2((k+j)\pi/N)}{\sin(j\pi/N)}$:

- **$b = 1$** (the Whitehead link proper is $W_{0,1,1,0}$):
  $J_N = \varphi_N \sum_{n=0}^{N-1} (2n+1)\,\chi_{N,n}^{4a-c+d}
  \bigl(\sum_{k=0}^{N-1-n} S_{n,k}\bigr)^{c+d}$ — the outer $n$-sum
  carries unimodular phases ($4a-c+d = -1$ for the Whitehead link).
- **$b \ge 2$**: $J_N = 0$ for even $N$; for $N = 2M+1$ the sum
  collapses to the single $n = M$ slice:
  $J_N = \varphi_N\, N^b\, \chi_{N,M}^{4a-c+d}
  \bigl(\sum_{k=0}^{M} S_{M,k}\bigr)^{c+d}$.

$\mathrm{Vol}(W_{a,b,c,d}) = 8(c+d)\Lambda(\pi/4)$ (vdV via octahedral
decomposition, his [10]); for $c+d = 1$ this is $4G = 4\,\mathrm{Cl}_2(\pi/2)$.

## Route split (the W2 verdict)

| Route | Modulus structure | Squeeze feasibility |
|---|---|---|
| $b = 1$ (Whitehead link) | $\|J_N\|$ = modulus of a **phase-weighted** sum; non-cancellation is vdV Lemma 4 (Fresnel/erfc stationary phase, Steps 3–6) | **NOT elementary.** The Gaussian analysis is a genuine analytic input; formalizing it is a separate project. Scope-limited negative in the sense of AGENTS.md §refuted-discipline (a): the *elementary* bricks alone do not reach $\|J_N\|$; nothing is structurally excluded. |
| $b \ge 2$ chain, $N = 2M+1$ odd (e.g. $W_{0,2,1,0}$) | $\|J_N\| = N^b\,\bigl(\sum_{k=0}^M S_{M,k}\bigr)^{c+d}$ **exactly** — phase-free positive sum (anchor A4 modulus identity) | **Fully elementary, 1D.** Same brick inventory as the 4₁/Borromean squeezes; simpler than Borromean (no vanishing-term analysis, no mirror-sign absorption: every sine factor is strictly positive since $k+j \le 2M < N$). |

**Decision: formalize the $b \ge 2$ chain $W_{0,2,1,0}$** (2 belts, one
positive clasp, $\mathrm{Vol} = 4G$) as the third volume-conjecture
instance. The $b=1$ Whitehead link's Lemma-4 input becomes a named
conditional class if we later want the link-level statement.

## Lean target (bricks W3–W5)

Carrier (`whiteheadTerm`/`whiteheadKashaev`, parametrized by $M$,
$N := 2M+1$):

$$P_M = \sum_{k=0}^{M} S_{M,k}, \qquad
\log S_{M,k} = 2\,s_{M+k} - 2\,s_k - s_M,\quad
s_m = \sum_{j=1}^{m} \log\bigl(2\sin(j\pi/N)\bigr).$$

Indices stay in range: $M + k \le 2M = N-1$. Deviation brick: each $s$
is the existing Riemann sum with $|s_m + \tfrac{N}{2\pi}\mathrm{Cl}_2(2\pi m/N)|
\le$ masterErr-type bound (E5c-4, $k$-uniform), so
$|\tfrac{2\pi}{N}\log S_{M,k} - g_N(k)| \le 5 \cdot \text{masterErr}(N)$
(coefficient sum $2+2+1$).

Continuum functional (the W5 brick), $\theta = 2\pi k/N$, $\theta_M \to \pi$:

$$g(\theta) = 2\,\mathrm{Cl}_2(\theta) - 2\,\mathrm{Cl}_2(\theta + \pi),
\qquad g'(\theta) = 2\log\Bigl|\frac{\sin((\theta+\pi)/2)}{\sin(\theta/2)}\Bigr|.$$

$g' = 0 \iff \sin((\theta+\pi)/2) = \sin(\theta/2) \iff \theta = \pi/2$
(unique in $(0,\pi)$); $g(0) = -2\,\mathrm{Cl}_2(\pi) = 0$,
$g(\pi) = 2\,\mathrm{Cl}_2(\pi) - 2\,\mathrm{Cl}_2(2\pi) = 0$, and
$g(\pi/2) = 2G - 2(-G) = 4G$ (antisymmetry $\mathrm{Cl}_2(2\pi - \theta)
= -\mathrm{Cl}_2(\theta)$). This is *simpler* than the Borromean
functional (no duplication step needed).

Final theorem (sorry-free target):

$$\lim_{M\to\infty} \frac{2\pi}{2M+1}\,\log P_M = 4G
\quad\Longrightarrow\quad
\lim \frac{2\pi}{N}\log\|J_N(W_{0,2,1,0})\| = 4G = \mathrm{Vol},$$

the second arrow being the exact modulus identity
$\|J_N\| = N^2 P_M$ plus $\tfrac{2\pi}{N}\cdot 2\log N \to 0$ (trivial).
The identification of Lemma 1's closed form with the diagrammatic
invariant is the cited input (same epistemic tier as the Borromean
carrier's GL2011/Habiro identification; here it is additionally
anchor-verified against the generic-$t$ tangle formula and the corpus's
independent Borromean transcription).

Numeric confirmation of the target (witness, anchor A3): 3-parameter
tail fit of the chain rate over $N \in \{101,\dots,401\}$ gives
$V = 3.66396$ vs $4G = 3.66386$ (err $9.3\times 10^{-5}$).
