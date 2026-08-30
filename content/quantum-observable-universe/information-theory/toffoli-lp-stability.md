Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realized as the $3$-strand braid word with traced volume matrix $M(q)$. Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis. Express the $q$-Toffoli in normal-form coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:

1. **(Stability region.)** Under the canonical convention $z_D = q^3/(q^2+1)$ the amplitudes the Toffoli construction produces are
$$
  P_{6,6} = \frac{(q^4+1)(q^4+q^2+2)}{4q(q^2+1)^2},
  \qquad
  P_{7,7} = \frac{q^3(q^4+1)}{(q^2+1)^2},
$$
$$
  P_{7,6} = -\frac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2},
  \qquad
  P_{6,7} = \frac{(q-1)(q+1)(2q^6+q^4+q^2+1)}{2q(q^2+1)^2}.
$$
The two diagonal amplitudes are strictly positive on $q > 0$; each off-diagonal amplitude has exactly one zero there, at $q = 1$, since its sextic factor is positive for every real $q$. So the derived family has **one** operator zero on $(0,\infty)$, not three, and $P_{7,6} < 0$ for every $q > 1$ — including the substrate value. The two further thresholds this item used to name,
$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
$$
are the roots of two objects the derivation retires: $q_\star$ is the root of the convention-$C$ diagonal $(q + \sqrt q - 1)/(q+1)$, and $q_\Phi$ the root of the published $\Phi$, which is not in the image of the Toffoli construction under any indexing or convention ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). They are recorded here as history, not as properties of the gate.

2. **(The operator threshold.)** The derived family has a single threshold on $(0,\infty)$:
See [Table 1](#tbl:toffoli-lp-stability-table1-data).
At $q = 1$ both off-diagonal amplitudes vanish through their common factor $(q-1)$: the classical reversible Toffoli has trivial off-diagonal amplitude. Neither diagonal amplitude vanishes anywhere on $q > 0$, and neither off-diagonal sextic factor has a positive real root, so $q = 1$ is the only threshold. The two thresholds this item used to name are recorded in the table as history: $q_\star$ is where the **convention-$C$** diagonal $(q + \sqrt q - 1)/(q+1)$ vanishes — a property of the excised frame, not of the gate — and $q_\Phi$ is a root of the retired $\Phi$.

3. **(Dual shadow prices.)** For $q > 1$, the LP dual admits bounded shadow prices $y_i^*(q)$ satisfying:
$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$
where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. **Open (2026-08-09).** The figure previously quoted here, $\kappa(G(q_0)) \approx 3.03$, is withdrawn. It came from a Gram matrix built with the naive length rule $\mathrm{tr}_M(T_w) = z^{\ell(w)}$ — the pre-2026-05-19 $\mathrm{tr}_M(e^-) = z^3$ bug — under the excised convention C, in float64, at a superseded 17-digit $q_0$; it corresponds to no convention in the registry. Under the production convention D the Markov–Gram form is **singular**, so $\lambda_{\max}/\lambda_{\min}$ in the ordinary sense is infinite and the bound above is not available on the full six-dimensional NF span. Whether the shadow-price bound is to be re-posed on the quotient by the radical is the same decision as for Term 4 of the six-term mass identity and is reserved for the owner. The replacement value must be read off a regenerated `toffoli-lp-stability.witness.json`; it is not to be hand-edited, and the producer needs three fixes (convention, trace rule, precision) before it can be re-run.

4. **(Physical-substrate stability — the positivity does not hold as stated.)** At $q_0 \approx 1.110$, under convention $D$:
$$
  P_{7,7}(q_0) \,\approx\, 0.6912,
  \qquad
  P_{7,6}(q_0) \,\approx\, -0.1438.
$$
The diagonal is strictly positive; the target-flip amplitude is **negative**, and is negative throughout $q > 1$. The figures this item previously carried, $P_{7,7}(q_0) \approx 0.5514$ and $\Phi(q_0) \approx 0.0495$, were the convention-$C$ diagonal and the retired $\Phi$ respectively.

The stability argument recorded in the proof block runs through the positivity of *both* amplitudes, so it does not close on the derived family. What that costs is bounded by which step it enters: the proof reduces feasibility of $G\vec t(q) \geq 0$ to the positivity of $P_{7,7}(q)\,W_{\mathrm{std}}(q)$ *"with the appropriate sign from $\Phi(q)$"*, and that qualifying clause is asserted without derivation — nothing in the corpus says what the sign is or why. The first factor survives: $P_{7,7}(q_0)\,W_{\mathrm{std}}(q_0) \approx 0.4624 > 0$.

**The stated condition has now been measured directly, and it holds.** Rather than settle the reduction, one can construct $T_q$ and evaluate $G\vec t(q_0) \geq 0$ itself. The element is implicit in the crossing coefficients — $C_{ij} = c_j\sigma_i + d_j$ is an algebra element, and the chain recursion is $(a\sigma+b)(c\sigma+d)$ reduced by $\sigma^2 = \hbar_\times\sigma + 1$ — so for the all-proton ordering
$$
  T_q \;=\; \sigma_1 \;+\; \hbar_\times\,\sigma_0\sigma_1,
  \qquad \hbar_\times = q - q^{-1}.
$$
Against the production Gram, every component of $G\vec t(q_0)$ is strictly positive, for all eight strand-type orderings ([`toffoli_nf_coordinates_and_lp_feasibility.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_nf_coordinates_and_lp_feasibility.py)). So the substrate satisfies the LP condition this proposition states.

**Two qualifications, both of which bound what that is worth.** First, the Gram is entrywise non-negative, and $\vec t$ is too for the all-proton ordering, so *for that ordering* positivity is forced by shape with no cancellation possible — 2 of the 8 orderings are trivial in this sense and 6 are not. Second, and more consequential: $\vec t$ acquires a negative component exactly when $\hbar_\times < 0$, i.e. on $0 < q < 1$ — the *opposite* side of $q = 1$ from where $P_{7,6}$ is negative. The amplitude sign and the cone condition disagree about which regime is the admissible one, so the reduction above does not merely mix index spaces.

**That sign inversion is now proved to be an identity, and it excludes the reduction as written.** Since $\hbar_\times = (q-1)(q+1)/q$, the flip amplitude factors as
$$
  P_{7,6}(q) \;=\; -\,\hbar_\times\,\cdot\,\frac{S(q)}{2(q^2+1)^2},
  \qquad S(q) = q^6+q^4+2q^2+1,
$$
and $S$ has no real root while $(q^2+1)^2 > 0$, so the cofactor is strictly positive on all of $\mathbb{R}$. The flip amplitude is therefore $-\hbar_\times$ times something positive, while the cone coordinate is $+\hbar_\times$ — giving $P_{7,6}(q)\,\hbar_\times(q) \leq 0$ for every $q > 0$. Sorry-free in `QOU.Information.toffoliFlip_mul_coneCoord_nonpos`, with the symbolic cross-check in [`toffoli_sign_inversion_is_structural.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_sign_inversion_is_structural.py) (7/7).

This is a **scope-(b) exclusion**, and the invariant is the factorisation above: no reduction in which the cone condition *inherits* the flip amplitude's sign can hold, at any anchor or in any convention, because the two carry exactly opposite signs of the same factor. It does **not** exclude a reduction carrying a *negative* proportionality — one in which the cone condition follows $-P_{7,6}$ — and that is the natural remaining candidate.

No claim of LP-instability is made, and none is available: the condition as stated is satisfied. The downstream statement that $\{q\text{-Toffoli}, H\}$ generates universal reversible computation on the Reeb bundles inherits that opening.

**Every sign and zero claim above is Lean-proved.** Nothing in this arc rests on evaluation at a single anchor:

| claim | theorem (`QOU.Information.*`) |
|---|---|
| $P_{7,7} > 0$ on $q > 0$, no positive root | `toffoliDiagonal_pos` |
| $P_{6,6} > 0$ on $q > 0$ | `toffoliP66_pos` |
| $P_{7,6}$'s only positive zero is $q = 1$ | `toffoliFlip_eq_zero_iff` |
| $P_{7,6} < 0$ on $q > 1$, the substrate side | `toffoliFlip_neg_of_one_lt` |
| $P_{7,6} > 0$ on $0 < q < 1$ | `toffoliFlip_pos_of_lt_one` |
| $P_{6,7} + P_{7,6} = q(q-1)^2(q+1)^2/2(q^2+1)$ | `toffoli_antisymmetry_defect` |
| the flip channel is **not** antisymmetric | `toffoli_not_antisymmetric` |
| $W_{\mathrm{std}} > 0$ and $P_{7,7}W_{\mathrm{std}} > 0$ | `wStd_pos`, `toffoliDiagonal_mul_wStd_pos` |
| $\mathrm{sign}\,P_{7,6} = -\mathrm{sign}\,\hbar_\times$ | `toffoliFlip_mul_coneCoord_nonpos` |

All sorry-free, axioms `[propext, Classical.choice, Quot.sound]`. The antisymmetry defect is exact and vanishes only at $q = 1$, so "reversing the crossing negates it" fails everywhere except the classical limit. Symbolic cross-check: [`toffoli_amplitude_sign_claims.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_amplitude_sign_claims.py), 9/9.

**Substrate stability table:**
See [Table 2](#tbl:toffoli-lp-stability-table2-data).
