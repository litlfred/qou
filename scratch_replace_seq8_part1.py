import os
import re
import sys

def rewrite_blocks(input_path, output_path, new_contents):
    with open(input_path, 'r') as f:
        content = f.read()
    
    # We find blocks by their FILE_START and FILE_END
    for block_name, new_text in new_contents.items():
        pattern = r"(<!-- FILE_START: " + re.escape(block_name) + r" -->\n).*?(\n<!-- FILE_END: " + re.escape(block_name) + r" -->)"
        
        def replacer(match):
            return match.group(1) + new_text + match.group(2)
        
        new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
        if new_content == content:
            print(f"Warning: Block {block_name} not found or not modified.")
        content = new_content

    with open(output_path, 'w') as f:
        f.write(content)
    print(f"Wrote to {output_path}")

new_contents_8 = {
    "intro-hoefsmit-convergence-atomic.md": """The Hoefsmit basis for the Hecke algebra is the categorical analogue of the Young orthogonal form for the symmetric group. It diagonalises the Jucys–Murphy operators and exposes the content-grading that controls the $q$-expansion of the binding-energy formula. This section assembles the universal braid-branching identity driving the Hoefsmit construction, proves its convergence at the substrate parameter, and exhibits the atomic-shell evidence that pins the convergence rate.

The arc proceeds in three layers. The first six blocks establish the universal braid-branching formula, prove the Hoefsmit basis exists in the categorical setting, and reduce the convergence question to a polynomial inequality in the substrate parameter. The middle blocks prove convergence at $q_0 \\approx 1.1097$ and bound the rate, identifying the leading correction term. The closing blocks survey the atomic-shell evidence—the categorical predictions for the $1s, 2s, 2p, \\dots$ shell sequence and their empirical agreement with the noble-gas closure pattern.

The output is the validated Hoefsmit basis with explicit content-grading. The subsequent Markov-axiom analysis exploits this to derive closed-form $\\chi$-characters. The atomic-shell evidence constitutes the strongest empirical validation of the substrate-level construction.""",

    "operator-selection-lp.md": """The confinement LP selects the Borromean link $\\mathcal{B}_3$ as the unique optimizer over the $6$-element NF basis of $H_3(q)$. We formulate the general LP for knot operator selection in $H_n(q)$ for arbitrary strand number $n$. The confinement LP is the special case $n = 3$, $d = 6$.

## Input / Output

**Input.**
- Strand number $n \\geq 2$.
- A basis $\\{b_1, \\ldots, b_d\\}$ of $H_n(q)$ (the NF basis, with $d = n!$).
- Markov traces $t_i = \\mathrm{tr}_M(b_i)$ for each basis element.
- The $d \\times d$ Frobenius Gram matrix $G_{ij} = \\mathrm{tr}_M(b_i \\cdot b_j)$.
- A target net value $n_{\\mathrm{target}} \\in \\mathbb{R}_{>0}$ (the normalised categorical mass of the desired state).

**Output.**
- The optimal coefficient vector $x^* \\in \\mathbb{R}^d$ such that $\\Phi^* = \\sum_{i=1}^{d} x_i^* b_i$ is the minimum-action knot operator satisfying all Frobenius positivity and net constraints.
- The dual certificate $(y_0^*, y^*)$ proving optimality.

## Primal program (operator selection)

**Proposition (general operator selection LP).**
*The knot operator $\\Phi = \\sum_{i=1}^{d} x_i b_i \\in H_n(q)$ for a target interaction with net value $n_{\\mathrm{target}}$ is the solution of the linear program:*

$$
  \\min_{x \\in \\mathbb{R}^d} \\quad \\sum_{i=1}^{d} t_i \\, x_i
$$

*subject to:*

$$
  \\sum_{i=1}^{d} x_i = n_{\\mathrm{target}}
  \\qquad (\\text{net constraint})
$$

$$
  \\sum_{j=1}^{d} G_{ij}\\, x_j \\geq 0
  \\quad \\forall\\, i \\in \\{1, \\ldots, d\\}
  \\qquad (\\text{Frobenius positivity})
$$

$$
  x_i \\geq -M \\quad \\forall\\, i
  \\qquad (\\text{boundedness})
$$

*where $M > 0$ is a constant large enough to ensure boundedness of the feasible polyhedron.*

The objective $\\sum_{i} t_i x_i = \\mathrm{tr}_M(\\Phi)$ is the categorical action. Minimizing it selects the operator of least action among all operators compatible with the Frobenius structure.

The Frobenius positivity constraints $Gx \\geq 0$ encode the demand–supply balance: $\\Phi$ must pair non-negatively with every basis element under the Frobenius inner product. No channel carries unbounded demand.

**LP over motivic shadows, not real numbers.**
*The data feeding the LP—Markov traces $t_i = \\mathrm{tr}_M(b_i)$ and Frobenius Gram entries $G_{ij} = \\mathrm{tr}_M(b_i \\cdot b_j)$—are formal elements of $\\mathbb{Z}[q^{\\pm 1/2}, (q-q^{-1})^{-1}]$, hence elements of the Habiro completion $\\widehat{\\mathbb{Z}[q]}$. The selection of the operator $\\Phi^* = \\sum_i x_i^* b_i$ is a combinatorial problem over the motivic shadows of the motivic substrate (the algebraic data of the Hecke algebra independently of any place-realization). Strong duality is a purely algebraic consequence of the LP. Only after the optimizer is selected does the archimedean realization $\\rho_\\infty$ project the dual prices and objective value into physical binding energies in $\\mathbb{R}$. The non-archimedean realizations $\\rho_p$ recover the LP's cyclotomic shadows at each finite place $p$.*

## Dual program (demand pricing)

By LP duality, the dual is:

$$
  \\max_{y_0, \\, y \\in \\mathbb{R}^d} \\quad n_{\\mathrm{target}} \\cdot y_0
  - M \\sum_{i=1}^{d} s_i
$$

*subject to:*

$$
  y_0 + \\sum_{i=1}^{d} G_{ji}\\, y_i - s_j \\leq t_j
  \\quad \\forall\\, j \\in \\{1, \\ldots, d\\}
$$

$$
  y_i \\geq 0, \\quad s_i \\geq 0 \\quad \\forall\\, i
$$

For large $M$, the slack variables $s_i$ are driven to zero at optimality. The effective dual simplifies to:

$$
  \\max_{y_0, \\, y \\geq 0} \\quad n_{\\mathrm{target}} \\cdot y_0
$$

*subject to:*

$$
  y_0 + \\sum_{i=1}^{d} G_{ji}\\, y_i \\leq t_j
  \\quad \\forall\\, j \\in \\{1, \\ldots, d\\}
$$

## Strong duality

**Proposition (strong duality).**
*The primal and dual programs have equal optimal values:*

$$
  \\sum_{i=1}^{d} t_i \\, x_i^*
  \\;=\\;
  n_{\\mathrm{target}} \\cdot y_0^*
$$""",

    "operator-selection-lp-interpretation.md": """The dual variable $y_0$ is the shadow price of the net constraint: the marginal cost (in units of categorical action) of increasing the target mass $n_{\\mathrm{target}}$ by one unit. The dual variables $y_i \\geq 0$ are the shadow prices of the Frobenius positivity constraints (channel demand prices). A positive $y_i^*$ at optimality indicates that the $i$-th Frobenius constraint is tight, meaning the $i$-th channel is saturated.""",

    "sdp-degeneracy-at-metallic-coincidence.md": """**Observation.** At the cost-coincidence loci of the operator-selection LP/SDP—points $q^* > 0$ where two cost coefficients $t_i(q)$ and $t_j(q)$ become equal—the strict-complementarity condition fails and the SDP is degenerate. These loci coincide exactly with the metallic-ratio ladder $\\{\\delta_n : n \\in \\mathbb{N}^+\\}$.

**The mechanism.** For the $n=2$ LP with basis $\\{\\gamma, \\sigma_0\\}$ of $H_2(q)$, the cost coefficients are

$$
  t_1(q) \\;=\\; 2(q + q^{-1}),
  \\qquad
  t_2(q) \\;=\\; q^2 - q^{-2}.
$$

A direct algebraic calculation gives

$$
  t_1(q) \\;=\\; t_2(q)
  \\quad\\Longleftrightarrow\\quad
  q - q^{-1} \\;=\\; 2
  \\quad\\Longleftrightarrow\\quad
  q \\;=\\; \\delta_{\\rm silver} \\;=\\; 1 + \\sqrt{2}.
$$

At this $q$, the LP optimum is a face of the feasible polytope, not a vertex. Any feasible $x$ satisfying $x_1 + x_2 = n_{\\rm target}$ achieves the same primal cost $t_1 x_1 + t_2 x_2 = t_1 \\cdot n_{\\rm target}$. The dual shadow prices $y_i^*$ become non-unique (multiple optimal $(y_0^*, y^*)$ values), strict complementarity fails, and the active set $\\mathcal{A} = \\{i : y_i^* > 0\\}$ is empty. This is the SDP-degeneracy signature: rapid loss of conditioning, ambiguous identification of binding constraints, and multiple optimal solutions returned.

**Empirical verification.** The $n=2$ LP active-set sweep observed this signature. Below silver the active set was $\\{0\\}$ (row 1 tight), AT silver it was $\\emptyset$ (degenerate), above silver it was $\\{1\\}$ (row 2 tight). The degeneracy at silver is the first non-null result in a series of prior canonical probes that all returned smooth observables.

**Structural significance.** The metallic-ratio ladder sits on the algebraic side: $q = \\delta_n$ is where the Hecke scalar $q - q^{-1}$ takes the integer value $n$, making $\\sigma$ satisfy the integer-coefficient quadratic $\\sigma^2 = n \\sigma + 1$. Smooth observables (Wenzl weights, Jones polynomial signs, $n=3$ per-block character signs) do not see this discrete arithmetic structure because they are rational functions of $q$ with no discontinuities. The LP-vertex combinatorics sees it: cost-coefficient coincidences are algebraic events that translate the arithmetic of $q - q^{-1}$ into a topological change of the optimum's face dimension.

**Physical interpretation.** Identifying the silver coincidence with the CFL phase transition of dense quark matter gives the empirical handle on this algebraic phenomenon. The CFL transition density $\\rho_c$ is the physical realization of the silver-coincidence point. The SDP degeneracy there is the order-parameter discontinuity of the first-order CFL transition. Multiple metallic ratios on the ladder correspond to multiple phase transitions. The bar-mirror $\\varphi^2 \\approx 2.618$ of the deconfinement boundary $q_{\\rm gold} = 1/\\varphi^2$ forms a candidate for the CFL $\\to$ gCFL boundary observed in dense-QCD phenomenology.

**Generalisation (conditional).** For the strand-$n$ LP with basis size $d_n = n!$, the cost coefficients $t_i(q)$ are rational functions of $q$. The pairwise coincidence equations $t_i(q) = t_j(q)$ have rational-function solutions. Those solutions on the metallic ladder constitute the set $S(n) \\subseteq \\{\\delta_k : k \\le n\\}$ of LP-degeneracy points for $n$ strands. For $n=2$, $S(2) = \\{2\\}$ (silver only). For $n=3$, the categorical evaluation returns $\\{\\delta_{\\rm silver}\\}$. The higher-strand characterisation remains conditional.

**Falsifiability handle.** Running an SDP solver on the canonical operator-selection problem at $q$-values near each metallic ratio reveals measurable signs of degeneracy: rising condition-number of the KKT system, multiple optimal solutions reported by the solver, and $y_i^*$ values dropping to tolerance for all $i$ simultaneously. Each observation tests the algebraic identification.""",

    "universal-braid-branching.md": """**Proposition.**
*For any braid $K$ on $3$ strands and any partition $\\lambda \\vdash k$ with $k \\geq 3$, the Frobenius character of $K$ in the irreducible representation $\\rho_\\lambda$ of $H_k(R, q)$ is:*

$$
  \\chi(K, \\lambda)
  = f^{\\lambda/[3]} \\cdot \\chi_K^{\\mathrm{sym}}
  + f^{\\lambda/[2{,}1]} \\cdot \\chi_K^{\\mathrm{std}}
  + f^{\\lambda/[1^3]} \\cdot \\chi_K^{\\mathrm{alt}}
$$

*where $f^{\\lambda/\\mu} = |\\mathrm{SYT}(\\lambda/\\mu)|$ counts saturated chains from $\\mu$ to $\\lambda$ in Young's lattice. The three base characters compute once from the Hoefsmit seminormal form:*

| *Knot $K$* | *$\\chi_K^{\\mathrm{sym}}$* | *$\\chi_K^{\\mathrm{std}}$* | *$\\chi_K^{\\mathrm{alt}}$* |
|:---:|:---:|:---:|:---:|
| *$4_1$ (figure-eight)* | *$1$* | *$2 - [3]_q$* | *$1$* |
| *$B_3$ (Borromean)* | *$1$* | *$(2 - [3])([3]^2 - 4[3] + 1)$* | *$1$* |
| *unknot (identity)* | *$1$* | *$2$* | *$1$* |

**Archimedean specialisation (§7c).** The character values $\\chi^{\\mathrm{sym}}, \\chi^{\\mathrm{alt}}$ and skew-SYT counts are stated as real numbers, forming the archimedean evaluations of the generic $\\mathrm{Chebyshev}/\\mathfrak{sl}_2$ branching over $[\\mathrm{CommRing}\\ R]$.""",

    "hoefsmit-scattering-pipeline.md": """**Proposition (conditional on [`conj:hyperbolic-volume-transcendence`](#conj:hyperbolic-volume-transcendence) and `rem:baryon-period-ratio`).**
*The mass of a nuclear state with braid word $\\beta \\in B_n$ computes via the following functorial pipeline:*

$$
  \\beta
  \\;\\xrightarrow{\\;\\rho_\\lambda\\;}
  \\prod_i \\rho_\\lambda(\\sigma_i)
  \\;\\xrightarrow{\\;\\mathrm{tr}_M\\;}
  J_K(q)
  \\;\\xrightarrow{\\;\\omega\\;}
  \\mathrm{Geom}(K)
  \\;\\xrightarrow{\\;\\times\\, m_e\\;}
  \\mathfrak{m}
$$

*Stage 1 (Hoefsmit). Each crossing $\\sigma_i$ acts on the Wedderburn--Artin block $\\rho_\\lambda$ via the Hoefsmit seminormal matrix. The scattering amplitude from tableau state $T$ to state $T'$ under crossing $\\sigma_i$ is:*

$$
  W_{T \\to T'} = \\langle T' \\mid \\sigma_i \\mid T \\rangle
  = \\begin{cases}
    a_\\rho & T' = T \\quad\\text{(forward scattering)} \\\\
    b_\\rho & T' = (T)_i \\quad\\text{(exchange scattering)} \\\\
    0 & \\text{otherwise}
  \\end{cases}
$$

*where $a_\\rho = h/(1 - q^{-2\\rho})$ is the $q$-deformed axial distance and $b_\\rho = \\sqrt{a_\\rho a_{-\\rho} + 1}$ is the exchange amplitude. The matrix is maximally sparse: at most $2$ nonzeros per row.*

*Stage 2 (Markov trace). The product of Hoefsmit matrices over all crossings in $\\beta$ gives the braid representation matrix $\\rho_\\lambda(\\beta)$. The Markov trace sums over all Wedderburn--Artin blocks:*

$$
  J_K(q) = \\sum_{\\lambda\\,\\vdash\\,k}
  w_\\lambda \\cdot \\frac{\\chi_\\lambda(\\beta)}{\\dim(\\lambda)}
$$

*where $w_\\lambda = \\dim_q(\\lambda)^2 / [k]_q!$ is the Wedderburn--Artin weight and $\\chi_\\lambda(\\beta) = \\mathrm{tr}(\\rho_\\lambda(\\beta))$ is the Frobenius character.*

*By the universal branching rule, $\\chi_\\lambda(\\beta)$ is determined by Young's lattice path counts $f^{\\lambda/\\mu}$ and the three base characters $\\chi^{\\mathrm{sym}}$, $\\chi^{\\mathrm{std}}$, $\\chi^{\\mathrm{alt}}$.*

*Stage 3 (Observation frame). The fibre functor $\\tau$ evaluates the abstract Jones polynomial $J_K(q)$ on the knot complement $S^3 \\setminus K$. The evaluation is geometric, determined by Thurston's geometrization:*

$$
  \\tau(J_K)
  = \\sum_\\lambda w_\\lambda \\cdot
    \\frac{\\chi_\\lambda(\\beta)}{\\dim(\\lambda)}
    \\cdot \\mathrm{Geom}(K)
$$

*The factor $\\mathrm{Geom}(K)$ projects the algebraic trace into a measurable observable: $\\mathrm{Vol}(K)/\\hbar_q^2$ for hyperbolic $K$ (mass/energy), $\\mathrm{CS}(K) \\cdot \\hbar_q^2$ for torus $K$ (coupling phase), or $0$ for the unknot (vacuum).*

*Stage 4 (Physical mass). The mass is the norm of the evaluated trace, scaled by the electron mass $m_e$:*

$$
  \\mathfrak{m}(K) = m_e \\cdot \\mathrm{Geom}(K)
    \\cdot \\sum_\\lambda w_\\lambda \\cdot
    \\frac{\\chi_\\lambda(\\beta)}{\\dim(\\lambda)}
$$

*At Hecke level $k$, this sum truncates to $p(k)$ partitions. The truncation error satisfies:*

$$
  \\mathrm{MAE}(k) \\leq C_0 \\times [2]_q^{-2(k-3)}
$$

*with convergence rate $[2]_q^2 \\approx 4.04$ per level.*

*Proof.*
Each stage proves separately:

**Stage 1** uses the Hoefsmit seminormal form. The $q$-deformation of the classical axial distance $1/\\rho$ to $h/(1 - q^{-2\\rho})$ follows from the Hecke relation $\\sigma_i^2 = h\\sigma_i + 1$ and the requirement $\\det = -1$ for each $2 \\times 2$ block. The eigenvalues are $q$ (symmetric) and $-q^{-1}$ (antisymmetric), which are the eigenvalues of the universal $R$-matrix $\\check{\\mathcal{R}}$ of $U_q(\\mathfrak{sl}_2)$ restricted to the isotypic component of type $\\lambda$.

**Stage 2** uses the Wedderburn--Artin trace identity. The Markov trace $\\mathrm{tr}_M$ factors through the Wedderburn--Artin decomposition $H_k(R, q) \\cong \\bigoplus_\\lambda M_{d_\\lambda}(\\mathbb{C})$. The weight $w_\\lambda$ ensures that $\\mathrm{tr}_M$ is the unique trace satisfying the Markov property $\\mathrm{tr}_M(x\\sigma_k) = z \\cdot \\mathrm{tr}_M(x)$ for $x \\in H_k(R, q)$.

**Stage 3** uses the $\\mathrm{Geom}(K)$ alignment. The observation frame $\\tau$ is the fibre functor of the Tannakian category $(\\mathbf{C}, A, \\tau)$. On the $\\tau$-image (geometric) side, its evaluation on the knot complement is determined by $\\tau$-image Thurston geometrization and the Yekutieli rigid dualizing complex: the UNIQUE non-degenerate pairing $\\langle \\omega_A^\\bullet, S^3 \\setminus K \\rangle_{\\mathrm{Frob}}$ yields $\\mathrm{Vol}(K)/\\hbar_q^2$ for hyperbolic $K$ and $\\mathrm{CS}(K) \\cdot \\hbar_q^2$ for torus $K$. On the algebraic side this is the algebraic-quantum-volume pairing in $\\mathbb{Z}[q^{\\pm 1/2}]$; the geometric reading appears only after applying $\\tau_{\\mathrm{arch}}$. The universality follows from the rigidity of $\\omega_A^\\bullet$ (Yekutieli): the pairing is unique up to the scalar $\\hbar_q^2$, and the scalar is fixed by requiring that $\\mathrm{Geom}(\\bigcirc) = 0$ (vacuum normalisation) and $\\mathrm{Geom}(4_1) \\cdot \\hbar_q^2 = \\mathrm{Vol}(4_1)$ (the figure-eight knot defines $q_0$).

**Stage 4** uses the topological mass formula. The convergence bound follows by induction on $k$ using the Pieri rule for skew tableaux counts: each level $k$ introduces $p(k) - p(k-1)$ new partitions whose total Wedderburn--Artin weight is $O([2]_q^{-2})$ of the previous level's weight, by Plancherel concentration. $\\square$

*Formal asymptotic content. The truncation $\\mathrm{MAE}(k) \\leq C_0 \\cdot [2]_q^{-2(k-3)}$ has $\\operatorname{ordw}\\bigl(\\mathrm{MAE}(k)\\bigr) = -2(k-3)\\,\\operatorname{ordw}([2]_q)$; see Big-O via $\\operatorname{ordw}$ and the body asymptotics catalog.*

**Archimedean specialisation (§7c).** The scattering-amplitude vanishing test is stated over real inputs $v_1,v_2,v_3 : \\mathbb{R}$ with real coefficients. These form the archimedean evaluations of the generic Hoefsmit pipeline over $[\\mathrm{Field}\\ R]$.""",

    "hecke-convergence-bound.md": """**Proposition (convergence bound).**
*Let $\\mathcal{A}$ be the active set of partitions that dominate the Hoefsmit trace. The difference between the full trace $\\mathrm{tr}_M(W)$ and the restricted trace over $\\mathcal{A}$ is bounded by:*

$$
  \\left| \\mathrm{tr}_M(W) - \\sum_{\\lambda \\in \\mathcal{A}} W_\\lambda \\, \\mathrm{tr}_{\\rho_\\lambda}(W) \\right|
  \\;\\leq\\;
  C \\cdot q^{- \\Delta}
$$

*where $\\Delta$ is the gap in content norm between the active set and the next-leading partition, and $C$ depends only on the Coxeter length of $W$.*

This bounds the error introduced by truncating the trace to the dominant channels. The algebraic convergence relies on the rapid decay of the quantum dimensions $W_\\lambda$ outside the active set. The gap $\\Delta$ grows linearly with the strand count $n$, driving the asymptotic suppression of off-shell configurations.""",

    "algebraic-quantum-volume.md": """**Definition (Algebraic Quantum Volume).**
*Let $W \\in H_n(q)$ be a knot operator representing a confined state. The **algebraic quantum volume** of $W$ is its full canonical Markov trace over $\\mathbb{Z}[q^{\\pm 1/2}]$:*

$$
  \\mathrm{Vol}_{\\mathrm{alg}}(W)
  \\;:=\\; \\mathrm{tr}_M(W)
  \\;=\\; \\sum_{\\lambda \\vdash n} W_\\lambda \\, t_\\lambda(W)
$$

*where $W_\\lambda$ are the quantum dimensions and $t_\\lambda(W)$ are the irreducible character traces.*

This defines the exact algebraic quantity that governs the mass expansion. The algebraic volume encodes both the knot topology (via $t_\\lambda$) and the algebraic space structure (via $W_\\lambda$). The archimedean realisation $\\rho_\\infty$ projects this polynomial into the physical binding energy.

**Structure of the sum.** The volume decomposes into independent channel contributions. Each channel $\\lambda$ corresponds to a distinct phase of the $n$-nucleon cluster. The standard partition $(n-1, 1)$ carries the primary interaction strength, while the trivial partition $(n)$ acts as a scalar background field.

**Substrate isolation.** The algebraic volume computes entirely within the categorical substrate, before any numerical evaluation at $q_0$. It represents the pure combinatorial content of the mass formula. The convergence of the $z$-Habiro expansion depends crucially on the algebraic properties of this un-evaluated polynomial."""
}

if __name__ == "__main__":
    rewrite_blocks('/Users/litlfred/space_cats/qou/amalgamated_input/mass-theory_seq8.md', '/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq8.md', new_contents_8)

