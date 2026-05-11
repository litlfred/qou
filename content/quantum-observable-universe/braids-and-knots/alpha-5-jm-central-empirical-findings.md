**Remark.**

The companion witness
[`alpha-5-jucys-murphy-central.witness.json`](folio-assistant/computations/alpha-5-jucys-murphy-central.witness.json)
(2026-05-09) tests the simplest closed form proposed in
[`prop:mass-formula-iterative-lp-dual`](#prop:mass-formula-iterative-lp-dual)
at the height-6 level ($\ell = 5$):

$$
  \alpha_5(A) \;:=\;
  \sum_{\lambda \vdash 3A,\;\mathrm{ht}(\lambda)=6}
  w_\lambda(q_0) \cdot c_5(\lambda)
$$

with $w_\lambda(q_0) = \dim_q(\lambda)^2 / [3A]_{q_0}!$ and
$c_5(\lambda) = e_5(\{q_0^{2c(\square)} : \square \in \lambda\})$.

**Numerical results (mpmath, 50-digit precision):**

| $A$ | # ht-6 partitions of $3A$ | $\alpha_5(A)$ raw | $\alpha_5(A)/[3A]_{q_0}!$ |
|----:|--------------------------:|------------------:|--------------------------:|
|  2  |  1   | $+5.61 \times 10^{-4}$ | $+6.69 \times 10^{-7}$ |
|  3  |  3   | $+1.98 \times 10^{0}$  | $+3.34 \times 10^{-6}$ |
|  4  | 11   | $+1.65 \times 10^{2}$  | $+1.12 \times 10^{-7}$ |

**Relative spread (normalised):** $\approx 482\%$.

**Conclusion.** The naive form is **not atom-independent**.
This refutes the strongest version of Step 5 in
[`prop:mass-formula-iterative-lp-dual`](#prop:mass-formula-iterative-lp-dual):
the JM-central elementary symmetric polynomial alone does not
reproduce the AME-fitted $\alpha_5 \approx -4.2 \times 10^5$ MeV.

**The structural framework remains intact:**

- [`prop:frobenius-self-duality-forces-lp-dual-extraction`](#prop:frobenius-self-duality-forces-lp-dual-extraction)
  is a theorem (Frobenius (1903), Nakayama (1939)).
- [`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)
  is a theorem (Murphy 1992).
- The GB-filtration stratification by partition height is a
  theorem (Bokut–Chen).

What is open is **which refinement** of the level-$\ell$ closed
form correctly extracts the AME-fitted shell correction.

**Candidate refinements (research directions):**

1. **Per-atom strand recipe.** The braid $\varrho$ is a
   specific element of $H_{3A}(q)$ (see
   [`prop:recursive-atom-knot-atlas`](#prop:recursive-atom-knot-atlas));
   the level-$\ell$ shadow price should be a *recipe-weighted*
   sub-sum, not a sum over all height-$(\ell+1)$ partitions.
   Indicator: in the BW factorisation
   $u_\lambda^* = C_\lambda \cdot S_\lambda(Z, N, A)$, the
   *scaling function* $S_\lambda$ encodes per-atom datum that
   the bare q-content sum lacks.

2. **Refined jet stratification.** GB-filtration may cut by a
   finer index than partition height — e.g. by Frobenius
   coordinate (number of cells above the diagonal), Demazure
   sub-crystal, or canonical-basis depth. The atom-independence
   claim should then apply to the refined level, not to
   $\mathrm{ht}(\lambda) = \ell + 1$ taken as a coarse proxy.

3. **Solve the LP, do not just evaluate $P_\ell$.** The
   structural argument says shadow prices are dual variables of
   the operator-selection LP; "shadow price = central scalar"
   is a leading-order *guess* at how the LP solves. A genuine
   LP-dual computation per
   [`prop:bw-coefficient-shadow-price`](#prop:bw-coefficient-shadow-price)
   that uses $P_\ell$-mediated cost (rather than dim-blind cost)
   would derive the correct atom-dependence — the
   $[3A]_{q_0}!$ normalisation included.

4. **Higher-order $q$-corrections.** The leading-order
   JM-central scalar $c_\ell(\lambda)$ may need
   $O((q-1)^2)$ corrections from the curvature of the
   categorical $q$-connection (see
   [`def:categorical-q-connection`](#def:categorical-q-connection))
   away from the crystal limit.

**$q$-sweep across the physical regime $(1, \varphi)$ (2026-05-09 update).**

To address the question of whether atom-independence might
hold at some specific $q$ in the physical neighbourhood
(not at all $q$ symbolically), the probe also evaluates the
height-6 **q-deformed Wedderburn-weighted average**
(a ratio, so invariant under renormalisation of $\tilde w_\lambda$)

$$
  \langle c_5 \rangle_{\mathrm{ht}=6}(A, q)
  \;:=\;
  \frac{\sum_{\mathrm{ht}(\lambda)=6} \dim_q^2(\lambda)\, c_5(\lambda)}
       {\sum_{\mathrm{ht}(\lambda)=6} \dim_q^2(\lambda)}
$$

(the structurally derived normaliser when the operator-
selection LP is restricted to the height-6 stratum — no
$[3A]_q!$ guess). The relative spread of
$\langle c_5 \rangle_{\mathrm{ht}=6}(A, q)$ across
$A \in \{2,3,4\}$ is:

| $q$ | rel spread (partial-Plancherel-avg) |
|----:|------------------------------------:|
| $1.001$            |    628% |
| $q_0 - 0.01$       |   1327% |
| $q_0$              |   1446% |
| $q_0 + 0.01$       |   1578% |
| $1.20$             |   3339% |
| $1.40$             |  27846% |
| $1.60$             | 256221% |
| $\varphi - \epsilon$ | 279730% |

The spread is **uniformly bad** across the full $|q| \in (1, \varphi)$
range. There is no $q$ in the physical regime at which the
naive JM-central form is atom-independent, and the spread
*grows* with $q$ (driven by the $q^{O(n^2)}$ scaling of
$\dim_q^2$).

**This definitively refutes the simplest closed-form conjecture
at every $q$**, not just at $q_0$. The structural framework
(Frobenius self-duality + Murphy 1992 + GB-filtration) holds;
the specific ansatz "$u^{(\ell)*} \propto \langle c_\ell
\rangle$" does not.

**Negative result, useful science.** This is the kind of
sharply-falsifiable prediction the QOU framework should make.
Reporting the empirical refutation here, rather than burying
the test, makes the next research step well-defined: solve the
LP per (3) above with a *recipe-aware* cost vector, or refine
the stratification per (2).
