import os
import re

def rewrite_blocks(input_path, output_path, new_contents):
    with open(input_path, 'r') as f:
        content = f.read()
    
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

new_contents_11_pt1 = {
    "two-row-stratum.md": """## Definition

Let $H_n(q)$ be the Iwahori–Hecke algebra on $n$ strands with the canonical Wedderburn decomposition
$$
  H_n(q) \\;\\cong\\; \\bigoplus_{\\lambda \\vdash n} \\mathrm{End}(V_\\lambda)
$$
indexed by partitions $\\lambda \\vdash n$. The two-row stratum is the subset of partitions with at most two parts:
$$
  \\Lambda^2(n) \\;:=\\; \\{\\, \\lambda \\vdash n : \\ell(\\lambda) \\le 2 \\,\\}
  \\;=\\; \\{\\, (n-k, k) : 0 \\le k \\le \\lfloor n/2 \\rfloor \\,\\}.
$$

The corresponding two-row projection
$$
  \\pi_{\\mathrm{2-row}} \\;\\colon\\; H_n(q) \\;\\to\\;
    \\bigoplus_{\\lambda \\in \\Lambda^2(n)} \\mathrm{End}(V_\\lambda)
$$
is the orthogonal projection onto the two-row Wedderburn subalgebra (idempotent: $\\pi_{\\mathrm{2-row}}^2 = \\pi_{\\mathrm{2-row}}$). The canonical Markov trace splits accordingly:
$$
  \\mathrm{tr}_M(\\beta)
  \\;=\\; \\underbrace{\\sum_{\\lambda \\in \\Lambda^2(n)} y_\\lambda(q) \\cdot \\chi^\\lambda_q(\\beta)}_{\\mathrm{tr}_M(\\pi_{\\mathrm{2-row}}\\,\\beta)}
  \\;+\\; \\underbrace{\\sum_{\\ell(\\lambda) > 2} y_\\lambda(q) \\cdot \\chi^\\lambda_q(\\beta)}_{\\mathrm{tr}_M((1-\\pi_{\\mathrm{2-row}})\\,\\beta)}
$$
with $y_\\lambda$ the Wenzl weight.

## Structural significance

The two-row stratum carries the $\\mathrm{SU}(2)$ Schur–Weyl image. Under the natural restriction
$$
  H_n(q) \\;\\twoheadrightarrow\\; \\mathrm{End}_{\\mathrm{SU}(2)}\\!\\bigl(V^{\\otimes n}\\bigr),
\\quad V = \\mathbb{C}^2,
$$
partitions with $\\ell(\\lambda) > 2$ lie in the kernel. They correspond to higher-rank symmetry components absent from the $\\mathrm{SU}(2)$ spin-pairing observable. The two-row sector is where the $q$-deformed spin observables—including the magic-shell coupling—live.

## Indexing the stratum

$|\\Lambda^2(n)| = \\lfloor n/2 \\rfloor + 1$. For $n = 12$ (the $^4\\mathrm{He}$ strand count) this gives **7** partitions:

$$
\\Lambda^2(12) = \\{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\\}.
$$

Some are distinguished:
- $\\lambda = (n)$: trivial rep; one-dimensional, $V_{(n)} = \\mathbb{C}$.
- $\\lambda = (n-1, 1)$: standard rep; dimension $n - 1$.
- Self-conjugate $\\lambda$ within $\\Lambda^2(n)$: only $(n/2, n/2)$ when $n$ is even (the balanced two-row partition). For $n = 12$, this is $(6, 6)$.

The non-self-conjugate two-row partitions $(n-k, k)$ with $k < n/2$ form mirror pairs under the bar involution $q \\mapsto q^{-1}$.

## Empirical use

The companion canonical evaluation computes the per-partition decomposition $c_\\lambda := y_\\lambda(q_0) \\cdot \\chi^\\lambda_q(\\beta_{^4\\mathrm{He}})$ across all 77 partitions of 12 and finds the two-row stratum $\\Lambda^2(12)$ carries $86.6\\,\\%$ of $\\mathrm{tr}_M(\\beta_{^4\\mathrm{He}})$. The dominant block per atom across $\\{D, T, {}^3\\mathrm{He}, {}^4\\mathrm{He}\\}$ always lies in $\\Lambda^2(3A)$.""",

    "he4-channel-active-set.md": """## Setup

The $^4\\mathrm{He}$ bound state admits three primary compositional channels (each summing to $A = 4$ nucleons):

| channel | constituents | $\\sum \\Delta_\\mathrm{cat}$ (MeV) | residual $t_i$ (MeV) |
|---|---|---:|---:|
| $\\mathrm{D} \\oplus \\mathrm{D}$    | $(1,1) + (1,1)$ | $4.05$ | $\\mathbf{24.16}$ |
| $\\mathrm{T} \\oplus p$             | $(1,2) + (1,0)$ | $7.83$ | $\\mathbf{20.38}$ |
| ${}^3\\mathrm{He} \\oplus n$        | $(2,1) + (0,1)$ | $7.04$ | $\\mathbf{21.18}$ |

The **channel binding residual** is
$$
  t_i \\;:=\\; \\Delta_\\mathrm{cat}({}^4\\mathrm{He}) \\;-\\; \\sum_{j \\in \\mathrm{channel}\\, i} \\Delta_\\mathrm{cat}(j)
$$
—the binding the magic-shell coupling must explain *beyond* the free-constituent sum.

## LP formulation

Apply the general operator-selection LP canonical form with $t \\in \\mathbb{R}^3$ the residual vector above, $G = I_3$ (channels orthogonal at leading order), and
$$
  n_\\mathrm{target} \\;=\\; \\Delta_\\mathrm{coupling}(2, 2)
  \\;=\\; \\Delta_\\mathrm{cat}({}^4\\mathrm{He}) - 2\\,\\Delta_\\mathrm{cat}({}^3\\mathrm{He})
  \\;=\\; 13.197\\,\\mathrm{MeV}
$$
(the doubly-magic anchor).

## Solution

The LP solves uniquely (strong duality holds, duality gap $= 0$; $\\mathrm{primal\\_obj} = \\mathrm{dual\\_obj} = 268.949$). The primal weights $x^\\star$ and dual shadow prices $y^\\star$ are:

| channel $i$ | $x^\\star_i$ | $y^\\star_i$ | status |
|---|---:|---:|---|
| $\\mathrm{D} \\oplus \\mathrm{D}$    | $0$        | $\\mathbf{3.778}$ | active |
| $\\mathrm{T} \\oplus p$             | $13.197$   | $0$              | primal-saturating |
| ${}^3\\mathrm{He} \\oplus n$        | $0$        | $0.796$          | active |

with $y_0^\\star = 20.380$. The **active set** (constraints whose dual variable is positive) is
$$
  \\mathcal{A}({}^4\\mathrm{He}) \\;=\\; \\{\\,\\mathrm{D} \\oplus \\mathrm{D},\\; {}^3\\mathrm{He} \\oplus n\\,\\}.
$$

## Proposition

For the $^4\\mathrm{He}$ operator-selection LP defined above:

1. **Unique primal optimum** at the $\\mathrm{T} \\oplus p$ channel: $x^\\star_{\\mathrm{T} \\oplus p} > 0$ and $x^\\star_i = 0$ for all $i \\neq \\mathrm{T} \\oplus p$.
2. **Active set** $\\mathcal{A}({}^4\\mathrm{He}) = \\{\\,\\mathrm{D} \\oplus \\mathrm{D},\\; {}^3\\mathrm{He} \\oplus n\\,\\}$ (dual-tight constraints).
3. **Dual ordering** $y^\\star_{\\mathrm{D} \\oplus \\mathrm{D}} > y^\\star_{{}^3\\mathrm{He} \\oplus n} > y^\\star_{\\mathrm{T} \\oplus p} = 0$.

## Interpretation

The LP uses the $\\mathrm{T} \\oplus p$ decomposition to satisfy the binding constraint (it has the smallest residual after subtracting free constituents). However, the **shadow prices identify $\\mathrm{D} \\oplus \\mathrm{D}$ as the most binding-receptive sub-braid**: a unit perturbation of the deuteron-pairing channel would change the primal binding cost by $3.778$ MeV per MeV—five times more than the ${}^3\\mathrm{He} \\oplus n$ channel and infinitely more than the $\\mathrm{T} \\oplus p$ channel.

This two-tier structural fingerprint is the channel-level analogue of the Wedderburn-block fingerprint: both identify a $q$-symmetric deuteron-pairing structure as the load-bearing geometry of the doubly-magic magic-shell coupling, while $\\mathrm{T} \\oplus p$ provides the energetic accounting.""",

    "he4-two-row-dominance.md": """## Statement

Let $\\beta_{{}^4\\mathrm{He}}$ denote the canonical atomic braid word for $^4\\mathrm{He}$ on $H_{12}(q)$. Define the per-partition contribution
$$
  c_\\lambda(q_0) \\;:=\\; y_\\lambda(q_0) \\cdot \\chi^\\lambda_q\\!\\bigl(\\beta_{{}^4\\mathrm{He}}\\bigr)
$$
with $y_\\lambda$ the Wenzl weight and $\\chi^\\lambda_q$ the Hoefsmit per-irrep character. Then
$$
  \\sum_{\\lambda \\vdash 12} c_\\lambda(q_0) \\;=\\; \\mathrm{tr}_M\\!\\bigl(\\beta_{{}^4\\mathrm{He}}\\bigr)(q_0).
$$

**Proposition.**
The two-row stratum $\\Lambda^2(12) = \\{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\\}$ carries at least $80\\,\\%$ of the canonical Markov trace at the substrate parameter:
$$
  \\frac{\\bigl|\\sum_{\\lambda \\in \\Lambda^2(12)} c_\\lambda(q_0)\\bigr|}
       {\\bigl|\\mathrm{tr}_M(\\beta_{{}^4\\mathrm{He}})(q_0)\\bigr|}
  \\;\\ge\\; 0.80.
$$

## Empirical verification

The two-row-stratum ratio is **$86.6\\,\\%$**. The top-5 binding-receptive Wedderburn blocks—all in $\\Lambda^2(12)$—account for $86.5\\,\\%$ cumulatively. The trivial rep $(12)$ contributes only $2.9\\,\\%$; the sign rep $(1^{12})$ contributes sub-1e-9.

## Structural interpretation

The two-row stratum carries the SU(2) Schur-Weyl image. Partitions with $\\ell(\\lambda) > 2$ correspond to higher-rank symmetry components absent from the spin-$\\tfrac{1}{2}$ pairing observable. The dominance of $\\Lambda^2(12)$ at $86.6\\,\\%$ provides the algebraic fingerprint of $^4\\mathrm{He}$ as a $q$-symmetric spin-pairing bound state—a substrate-derived characterisation of the magic-shell coupling. The top block $\\lambda^* = (9, 3)$ matches the prediction from the canonical evaluation independently of the empirical residuals.""",

    "markov-trace-frobenius-selection.md": """**Theorem (Markov-trace uniqueness on H_n(R, q)).**
*Any non-degenerate Frobenius form on the Iwahori–Hecke algebra $H_n(R, q)$ at generic $q$ equals the Jones–Markov form $\\tau_M$ block-wise. Therefore, the QOU mass identity uniquely determines $\\tau_M$ as the canonical Markov trace of the framework.*

## The chain: cat-action $\\to$ Markov trace

### Step 1: Cat-action of $\\mathbf{C}$ on the state bundle
A quantum observable universe specifies a rigid monoidal category $\\mathbf{C}$ with a fibre functor $\\tau$. The choice of $\\mathbf{C}$ fixes which Frobenius–Hopf algebra $A$ acts (typically $A = H_n(R, q)$).

### Step 2: Non-abelian Stokes at finite slice
Yekutieli's non-abelian Stokes theorem at finite slice depth gives the multiplicative trace on the closed surface obtained by Markov closure of the braid word $T_w$. The trace is the categorical trace in $\\mathbf{C}$ depending on the fibre functor $\\tau$.

### Step 3: Frobenius pairing — non-degeneracy + Wenzl/Jones uniqueness
The categorical trace descends under $\\tau$ to a Frobenius integral on the algebra. The algebra is a Frobenius algebra relative to this integral, equivalent to a non-degenerate bilinear form. The QOU mass identity uses the Frobenius co-Casimir trace identity, which is well-defined only if $\\tau$ is non-degenerate.

The **Jones–Markov form** $\\tau_M$ is defined by the Markov-peel and is non-degenerate on $H_n(R, q)$ at generic $q$. The Markov-trace uniqueness theorem (Jones / Wenzl) forces $\\tau_M$ to be the unique non-degenerate Frobenius form on the Hecke algebra.

### Step 4: Wedderburn + Markov-trace formula
$\\tau_M$ admits the explicit form $\\tau_M(x) = \\sum_\\lambda y_\\lambda(q) \\cdot \\chi_\\lambda(x)$, with $y_\\lambda(q)$ the Wenzl-bridge weights.

## Discussion
This proposition is a structural theorem about the representation theory of the Hecke algebra, with no empirical input. Uniqueness of $\\tau_M$ as the non-degenerate Frobenius form on $H_n(R, q)$ is axiomatised via the `MarkovTraceUniqueness` class.

## Computational consequence
The QOU production stack computes $\\tau_M$ on the 11-crossing canonical proton / neutron braid via four independent paths which agree to $\\leq 2 \\times 10^{-15}$ at the proton-pinned $q_0$.""",

    "t-beta-markov-frobenius-collapse.md": """**Proposition (Min-Frobenius-norm collapse for $T_\\beta$).**
*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$, equipped with the Jones–Markov trace $\\tau_M : H \\to R$ uniquely determined by the Wenzl–Jones uniqueness theorem. Equip $H$ with the **Frobenius inner product** $\\langle X, Y \\rangle_\\tau := \\tau_M(X \\cdot Y)$. The element of minimum Frobenius norm satisfying the linear constraint $\\tau_M(T_\\beta) = S$ for given $S \\in R$ is*

$$
\\boxed{\\; T_\\beta = S \\cdot 1_H \\;}
$$

*with $\\| T_\\beta \\|^2_\\tau = S^2$.*

## Corollary — observable c_k invariance
The $\\mathfrak{Q}_\\beta$ production rule extracts the $c_k$ Taylor coefficients from $\\tau_M(T_\\beta)(q)$. Under either norm choice (Euclidean L2 or canonical Markov–Frobenius), the SDP constraint $\\tau_M(T_\\beta) = S = \\mathfrak{Q}_\\beta / E_0$ is satisfied identically. Therefore $\\tau_M(T_\\beta)(q) \\equiv S(q)$ in both cases, and the $c_k$ are L2/Markov-invariant.

The L2 picture and the Markov picture differ in which $T_\\beta \\in H_n(R, q)$ forms the canonical primal-feasible operator, but they agree on every observable because observables extract from the constraint, not from the operator's coordinate expansion.

## Categorical reading
Under the Markov–Frobenius norm, $T_\\beta = S \\cdot 1_H$ forms a scalar multiple of the identity. All $q$-dependence of the canonical primal-feasible operator flows through the single $q$-rational scalar $S(q)$. There is no multi-channel SHAPE distributed across the NF basis. This forms the canonical choice from the Wenzl–Jones standpoint: the least-Hecke-Frobenius-norm operator hitting the target trace.""",

    "t-beta-markov-frobenius-collapse-general.md": """**Proposition (Min-Frobenius-norm collapse — general unital R-algebra).**
*Let $R$ be a strict-ordered field, $A$ a unital $R$-algebra, and $\\tau : A \\to R$ an $R$-linear normalised trace. Assume $\\tau$ is positive-semi-definite on squares ($0 \\le \\tau(X \\cdot X)$). Then for any $S \\in R$ and any $X \\in A$ satisfying the linear constraint $\\tau(X) = S$,*

$$
S^2 \\;\\le\\; \\tau(X \\cdot X).
$$

*If, additionally, $\\tau$ is non-degenerate on squares, the lower bound is attained iff $X = S \\cdot 1_A$.*

## Relation to the substrate-model version
This proposition lifts the collapse from the substrate model ($A = R$, $\\tau = \\mathrm{id}$) to the general unital $R$-algebra setting where $A$ may be non-commutative and infinite-dimensional.

## Application to the Iwahori–Hecke algebra
For $A = H_n(R, q)$ at generic $q > 0$ with $\\tau = \\tau_M$, this proposition gives the canonical SDP-min-Frobenius-norm operator for the constraint $\\tau_M(T_\\beta) = S$:

$$
T_\\beta^{\\mathrm{Markov}} \\;=\\; S \\cdot 1_H.
$$

This is the Markov-trace collapse lifted to the genuine non-commutative Hecke algebra. The L2-Euclidean coordinate-norm picture and the Markov-Frobenius picture represent two different operators inside $H_n(R, q)$ that both reproduce the SDP constraint $\\tau_M(T_\\beta) = S$."""
}

if __name__ == "__main__":
    rewrite_blocks('/Users/litlfred/space_cats/qou/amalgamated_input/mass-theory_seq11.md', '/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq11.md', new_contents_11_pt1)
