An inductive Gröbner–Shirshov reduction provides the canonical evaluation vehicle for the Pauli normal-form invariants in the Iwahori–Hecke algebra $H_A(q)$. Executing the reduction in exact Laurent arithmetic prevents rounding-error accumulation during word reduction, while extending the braid one strand at a time keeps the strand-count induction aligned with the nucleon-number induction $A \mapsto A + 1$.

## Crossing convention

All evaluations use the unimodular $(1, -h_{\mathrm{A}})$ crossing convention, writing $h_{\mathrm{A}} = q - q^{-1}$ for the discriminant of the quadratic Hecke relation:

| Crossing type | $(c, d)$ | Algebraic generator |
|:---:|:---:|:---|
| $\mathfrak{p}\mathfrak{p}$ (proton–proton) | $(1, 0)$ | positive crossing $\sigma$ |
| $\mathfrak{n}\mathfrak{n}$ (neutron–neutron) | $(1, -h_{\mathrm{A}})$ | negative crossing $\sigma^{-1} = \sigma - h_{\mathrm{A}}$ |
| $\mathfrak{p}\mathfrak{n}$ (mixed) | $(1, -h_{\mathrm{A}}/2)$ | symmetric average $\tfrac{1}{2}(\sigma + \sigma^{-1})$ |

Each negative-crossing transfer matrix satisfies $\det T_{\mathfrak{n}\mathfrak{n}} = -1$ (unimodular), matching the Iwahori–Hecke inverse relation $\sigma^{-1} = \sigma - (q - q^{-1})$.

## Inductive construction

The normal form is constructed strand by strand from $A = 2$ up to the target mass number. At each step $A \to A + 1$:

1. **Extend:** multiply the current normal form on the right by the affine Hecke factor $(c\,\sigma_{A-1} + d)$, with $(c, d)$ chosen according to the crossing type above.
2. **Reduce:** apply the quadratic Iwahori–Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ and the braid relations to eliminate all non-reduced Coxeter words.
3. **Project modulo $I_8$ (adjacency-correlation ideal):** reduce adjacent two-generator products $\sigma_i \sigma_{i+1}$ modulo the adjacency-correlation ideal into single-generator normal-form representatives.
4. **Project modulo $I_9$ (closed-shell-chain ideal):** absorb closed shell-chain extensions $w \cdot \sigma_j$ into their reduced prefix $w$ whenever both belong to the same closed shell chain.
5. **Accumulate:** evaluate the alternating Pauli functional $\mathrm{tr}_{\mathrm{alt}} = \sum_w c_w(q)\,(-q^{-1})^{\ell(w)}$ and the symmetric net functional $\mathrm{net} = \sum_w c_w(q)\,q^{\ell(w)}$.

Quotienting each freshly extended word modulo $I_8 + I_9$ in steps 3 and 4 collapses structurally determined words back into the per-generator transfer-matrix factorisation, keeping the surviving Coxeter support bounded well below the ambient dimension $A!$ of $H_A(q)$.

## Exact Laurent arithmetic and arbitrary-precision transfer evaluation

For light nuclei ($A \leq 12$), every intermediate coefficient is maintained symbolically in the Laurent polynomial ring $\mathbb{Z}[\check{q}, \check{q}^{-1}]$ with $\check{q} = q^{1/2}$; the dyadic denominator $2^{p_n}$ introduced by the mixed $\mathfrak{p}\mathfrak{n}$ factor cancels identically in the dimensionless Pauli ratio $F_{\mathrm{Pauli}} = |\mathrm{tr}_{\mathrm{alt}}| / |\mathrm{net}|$.

For larger mass numbers ($A \geq 13$), symbolic Laurent coefficient polynomials are replaced at the final evaluation point $q = q_0$ by arbitrary-precision real ball/interval evaluation ($\geq 80$ decimal digits) of the $2 \times 2$ Hecke transfer-matrix recurrence
$$
  T(h_{\mathrm{A}}; c, d)
  \;=\;
  \begin{pmatrix} c\,h_{\mathrm{A}} + d & c \\ c & d \end{pmatrix},
  \qquad
  C^k \;=\; a_k(h_{\mathrm{A}})\,C + b_k(h_{\mathrm{A}}),
$$
along the monotone strand tower, avoiding exponential growth in symbolic Laurent polynomial degree while preserving rigorous enclosure of $F_{\mathrm{Pauli}}$ with zero hardware floating-point approximation.
