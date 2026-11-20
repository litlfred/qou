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
and $S$ has no real root while $(q^2+1)^2 > 0$, so the cofactor is strictly positive on all of $\mathbb{R}$. The flip amplitude is therefore $-\hbar_\times$ times something positive, while the cone coordinate is $+\hbar_\times$ — giving $P_{7,6}(q)\,\hbar_\times(q) \leq 0$ for every $q > 0$. Formalized in `QOU.Information.toffoliFlip_mul_coneCoord_nonpos`, with the symbolic cross-check in [`toffoli_sign_inversion_is_structural.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_sign_inversion_is_structural.py) (7/7).

This is a **scope-(b) exclusion**, and the invariant is the factorisation above: no reduction in which the cone condition *inherits* the flip amplitude's sign can hold, at any anchor or in any convention, because the two carry exactly opposite signs of the same factor. It does **not** exclude a reduction carrying a *negative* proportionality — one in which the cone condition follows $-P_{7,6}$ — and that is the natural remaining candidate.

No claim of LP-instability is made, and none is available: the condition as stated is satisfied. The downstream statement that $\{q\text{-Toffoli}, H\}$ generates universal reversible computation on the Reeb bundles inherits that opening.

**Every sign and zero claim above is Lean-proved.** Nothing in this arc rests on evaluation at a single anchor:

| claim | theorem |
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

All use only the axioms `propext`, `Classical.choice` and `Quot.sound`. The antisymmetry defect is exact and vanishes only at $q = 1$, so "reversing the crossing negates it" fails everywhere except the classical limit. Symbolic cross-check: [`toffoli_amplitude_sign_claims.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_amplitude_sign_claims.py), 9/9.

**The reduction is refuted by a zero-set argument.** The proof reduces the cone condition to $P_{7,7}W_{\mathrm{std}}$ *"with the appropriate sign from"* $P_{7,6}$. A product vanishes exactly where a factor does, so such a reduction forces the cone condition's zero set into the union of the factors'. With the symbolic Gram — validated against the production `gram_matrix_mp` at five values of $q$ — the cone condition is a **single** constraint, the one indexed by the longest word $\sigma_0\sigma_1\sigma_0$:

$$
  (G\vec t)_5 \;=\; \frac{q^{10}+q^{6}-q^{4}+q^{2}-1}{(q^2+1)^2}
$$

| quantity | zeros on $q > 0$ |
|---|---|
| the cone constraint $(G\vec t)_5$ | one, at $q_c \approx 0.8944802929$ |
| $P_{7,7}W_{\mathrm{std}} = (q^7+q^3)/(q^4+4q^2+1)$ | **none** — strictly positive |
| $P_{7,6}$ | one, at $q = 1$ |

Since $q_c \neq 1$, the cone's zero is accounted for by neither factor, so no reduction of the stated form holds. The numerator is irreducible over $\mathbb{Q}$ and has exactly one positive real root, matching the bisected threshold to $1.14\times10^{-46}$. Proved without the intermediate value theorem and without $q_c$'s value in `cone_sign_change_unexplained_by_factors`: across $[1/2, 9/10]$ the cone constraint changes sign while both claimed factors stay strictly positive at each endpoint.

**Why the reduction had to fail: the relation exists, but at degree 2.** The eight amplitudes generate the whole field $\mathbb{Q}(q)$ — four of them reconstruct $q$ itself, via $M_{33}/M_{44} = q^4$ and $P_{7,7}/M_{00} = q^6$ — so asking whether the cone condition is *some* rational expression in them has no content. Restricting the form does. Over the common denominator $q^6(q^2+1)^4$ the ambient space of numerators is $21$-dimensional, and the degree-$2$ span of the amplitudes has rank $15$: a proper subspace of **codimension $6$**, which a generic rational function does not meet. The cone constraint is in it, and four amplitudes already suffice:

$$
  (G\vec t)_5 \;=\; -\tfrac{4}{9}
  \;+\; \tfrac{5}{36}M_{00}^2 \;-\; \tfrac{20}{3}M_{00}M_{33} \;-\; \tfrac{10}{9}M_{00}M_{44} \;+\; \tfrac{5}{18}M_{00}P_{7,7}
  \;-\; \tfrac{28}{9}M_{33}^2 \;+\; \tfrac{20}{3}M_{33}M_{44} \;+\; \tfrac{38}{9}M_{33}P_{7,7} \;+\; \tfrac{20}{9}M_{44}^2 \;+\; \tfrac{5}{36}P_{7,7}^2
$$

Formalized in `QOU.Information.cone_eq_quadratic_in_amplitudes`, with `coneCoordRow5_pos_iff` carrying the sign from the numerator to the constraint. Only $+$ and $\times$ appear: no division by an amplitude, hence no reconstruction of $q$. The *cross* terms are load-bearing — the span of the amplitudes and their squares alone has rank $14$ and does **not** contain the constraint.

This sharpens the refutation rather than softening it. A monomial vanishes exactly where a factor does; a degree-$2$ polynomial can vanish where none of its terms does, and that is precisely the mechanism producing the root at $q_c$. So the published reduction was the right kind of relation in the wrong class: it needed cancellation *between* products, which a single product cannot supply. Whether any member of the (one-parameter) solution family has a Hecke-theoretic reading is open. Measurement: [`toffoli_cone_in_entry_subring.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_cone_in_entry_subring.py), 8/8.

**The natural coordinates are the Markov and Hecke parameters, and there the expression is forced.** The rational coefficients above are a fact about the amplitude basis, not about the constraint. Writing $z = q^3/(q^2+1)$ for the Markov parameter and $\hbar_\times = q - 1/q$ for the Hecke deformation of $\sigma^2 = \hbar_\times\sigma + 1$,

$$
  (G\vec t)_5 \;=\; z^2 \;+\; 2\hbar_\times z \;+\; 3\hbar_\times^2 z^2 \;+\; \hbar_\times^3 z \;+\; \hbar_\times^4 z^2 ,
$$

with integer coefficients $(1,2,3,1,1)$ and no denominators. **Degree $6$ is minimal** — no polynomial in $(z,\hbar_\times)$ of total degree $\leq 5$ equals it — and minimal degree is a genuine invariant of the class. Formalized in `QOU.Information.cone_eq_markov_hecke_polynomial`.

**The coefficient string, however, is not an invariant.** The two parameters are algebraically dependent, satisfying the irreducible degree-$4$ relation

$$
  \hbar_\times^3 z - \hbar_\times^2 z^2 + 4\hbar_\times z - 4z^2 + 1 \;=\; 0 ,
$$

so $\mathbb{Q}[z,\hbar_\times]$ is not a polynomial ring but the coordinate ring of an affine rational curve, and a polynomial representative is unique only modulo that relation. The degree-$6$ representatives form a **six-parameter family**: $-1 + 4z^2 - 3\hbar_\times z + 4z^4 + \hbar_\times^2 z^4$ is an equally integral one, differing from the first by $(\hbar_\times z + z^2 + 1)$ times the relation. A reproducible choice is the grevlex normal form $\hbar_\times^5 z + 4\hbar_\times^3 z + \hbar_\times^2 - 2\hbar_\times z + 5z^2 - 1$, but even that depends on the term order. The relation is in `QOU.Information.markov_hecke_relation`; it is a fact about $H_n(q)$ and its Markov trace, not about the $q$-Toffoli.

This is **forced, not fitted**. Every Markov trace of a Hecke word lies in $\mathbb{Z}[z,\hbar_\times]$ — the Markov property $\mathrm{tr}(x\sigma_{\mathrm{last}}) = z\,\mathrm{tr}(x)$ removes the highest generator and the quadratic relation reduces the rest — and the corpus already carries that as a table, `QOU.Machinery.MarkovTraceH4.TRM`, whose entries 9 and 13 are $\hbar_\times z^2 + z = \mathrm{tr}(\sigma_0\sigma_1\sigma_0)$. Since the $q$-Toffoli's normal-form coordinates are $\vec t = (0,0,1,\hbar_\times,0,0)$, that is $T_q = \sigma_1 + \hbar_\times\sigma_0\sigma_1$, the constraint $(G\vec t)_5 = \mathrm{tr}(W\sigma_1) + \hbar_\times\mathrm{tr}(W\sigma_0\sigma_1)$ lies in $\mathbb{Z}[z,\hbar_\times]$ before any computation is done.

Both parameters are needed: the constraint's minimal polynomial over $\mathbb{Q}(z)$ has degree $3$ and over $\mathbb{Q}(\hbar_\times)$ degree $2$, so it is a function of neither alone. Since those degrees are coprime, $\mathbb{Q}(z,\hbar_\times) = \mathbb{Q}(q)$ and the content is the subring statement, not a field one. Separately, the numerator is neither reciprocal nor anti-reciprocal, so it is the Alexander polynomial of no knot — a scope-(b) exclusion resting on the reciprocity invariant. Measurement: [`toffoli_cone_in_markov_hecke_parameters.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_cone_in_markov_hecke_parameters.py), 13/13.

**Substrate stability table:**
See [Table 2](#tbl:toffoli-lp-stability-table2-data).
