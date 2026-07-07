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

new_contents_8_pt2 = {
    "habiro-ring.md": """**Definition (Habiro ring).**
*Let $R = \\mathbb{Z}[q]$. The **$q$-Habiro ring** $\\widehat{\\mathbb{Z}[q]}_q$ is the inverse limit of the polynomial rings $R / ( (q; q)_n )$ as $n \\to \\infty$, where $(q; q)_n = \\prod_{k=1}^n (1 - q^k)$ is the $q$-Pochhammer symbol:*

$$
  \\widehat{\\mathbb{Z}[q]}_q
  \\;:=\\;
  \\varprojlim_n \\frac{\\mathbb{Z}[q]}{((q; q)_n)}.
$$

*Elements of the $q$-Habiro ring are formal power series of the form $\\sum_{n=0}^\\infty c_n(q) \\, (q; q)_n$ with $c_n \\in \\mathbb{Z}[q]$.*

The Habiro ring completes the polynomial ring $\\mathbb{Z}[q]$ at the cyclotomic ideals. It forms the natural home for quantum topological invariants evaluated at roots of unity, where the terms $(q; q)_n$ vanish for $n$ large enough, truncating the infinite series to a finite sum.

**Application to QOU.** The algebraic quantum volume evaluates as a finite sum precisely because its components belong to a generalized Habiro ring where the truncation depth connects to the physical shell structure.""",

    "habiro-expansion-atomic.md": """**Proposition (atomic Habiro expansion).**
*The algebraic quantum volume of a confined atom $\\mathfrak{H}$ admits a $q$-Habiro expansion:*

$$
  \\mathrm{Vol}_{\\mathrm{alg}}(\\mathfrak{H})
  \\;=\\;
  \\sum_{n=0}^N c_n(q) \\, (q; q)_n
$$

*where the truncation depth $N$ correlates with the number of valence nucleons.*

This proposition guarantees that the binding energy formula terminates algebraically when evaluated at a root of unity. The coefficients $c_n(q)$ determine the specific shell contributions. This structure bridges the categorical operator traces to the empirical magic-shell mass phenomenology.""",

    "z-habiro-ring.md": """**Definition (z-Habiro ring).**
*Let $R = \\mathbb{Z}[q^{\\pm 1}][z]$. The **$z$-Habiro ring** $\\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$ is the inverse limit of the quotient rings $R / (P_n(q, z))$ as $n \\to \\infty$, where $P_n(q, z) = \\prod_{k=1}^n (1 - q^{-k}z)$ is the $z$-Pochhammer analog:*

$$
  \\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z
  \\;:=\\;
  \\varprojlim_n \\frac{\\mathbb{Z}[q^{\\pm 1}][z]}{(P_n(q, z))}.
$$

*Elements are formal series $\\sum_{n=0}^\\infty c_n(q, z) \\, P_n(q, z)$ with $c_n \\in \\mathbb{Z}[q^{\\pm 1}][z]$.*

The $z$-Habiro ring provides the algebraic completion needed to formalize the brane-tower contributions. The infinite product $\\Phi_q(z) = \\prod_{k\\geq 1} (1 - q^{-k}z)^{-1}$ is ill-defined as a polynomial but exists as a formal limit within this completion.

**Role in the mass formula.** The transient (brane-tower) component of the Hecke mass element lives naturally in the $z$-Habiro ring. Its evaluation at physical $(q, z)$ values relies on the algebraic truncation properties of this ring.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.""",

    "quantum-dilog-convergence.md": """**Proposition (convergence of the quantum dilogarithm).**
*Let $q \\in \\mathbb{R}$ with $1 < q$, and let $z \\in \\mathbb{R}$ with $|z| < q$. Then the quantum dilogarithm*

$$
  \\Phi_q(z) \\;=\\; \\prod_{k \\geq 1} \\bigl(1 - q^{-k} z\\bigr)^{-1}
$$

*is multipliable: the infinite product converges to a well-defined, non-zero real number.*""",

    "brane-tower-z-habiro.md": """The mass-endomorphism conjecture states that the Hecke mass element $\\Phi_{\\mathrm{mass}}$ admits a closed-form NF decomposition. Its **transient (brane-tower) component** is the sum

$$
  \\Phi_{\\mathrm{mass}}^{\\mathrm{trans}}(\\beta)
  \\;=\\;
  \\sum_{i=1}^{N} \\Phi_q(z_i),
$$

where $z_i = |\\hat{V}_i^{\\mathrm{full}}|$ are the per-generator additive Wedderburn traced-volume magnitudes, and $\\Phi_q$ is the quantum dilogarithm.

For low isotopes $\\{D, T, {}^3\\mathrm{He}\\}$, the per-generator volumes satisfy $z_i \\in [0.85, 1.0]$—just below the first pole of $\\Phi_q$ at $z = q_0 \\approx 1.11$. Canonical evaluations $\\Phi_q(0.989) \\approx 6.7 \\times 10^5$ and $\\Phi_q(1) \\approx 9 \\times 10^5$ show each summand is enormous; the analytic brane tower dominates the mass formula by orders of magnitude beyond the empirical binding.

Two regularizations exist but neither uniformly closes the gap:
1. **Yekutieli truncation** at GB filtration depth $k_{\\max}$ (empirical, not structural).
2. **$q$-Habiro completion**, regularizing in $q$, not $z$.

## Statement

**Conjecture (brane tower in $z$-Habiro).**
*Let $\\mathfrak{H}$ be a confined particle/atom with per-generator volumes $\\{\\hat{V}_i(q)\\}_{i=1}^{N}$ in $\\mathbb{Z}[q^{\\pm 1/2}]$. The brane-tower partial sums form a Cauchy sequence in the $z$-Habiro topology as $N$ varies. Their limit exists as an algebraic element $\\widetilde{\\Phi}_q^{\\mathrm{tower}}(\\beta) \\in \\widehat{\\mathbb{Z}[q^{\\pm 1}][z]}_z$, well-defined purely algebraically.*

*Furthermore, there exists a **canonical level-selection rule***

$$
  n_\\star \\;:\\; \\{\\text{confined particles}\\} \\;\\longrightarrow\\; \\mathbb{N}_{\\geq 1},
  \\qquad
  \\mathfrak{H} \\;\\longmapsto\\; n_\\star(\\mathfrak{H}),
$$

*derivable from QOU substrate data alone, such that the cyclotomic projection evaluated at $q = q_0$ and $z = z_i$ recovers the empirical brane-tower contribution to the binding $B(\\mathfrak{H})$ uniformly across atoms.*

## Consequences of the conjecture

If true, the conjecture:
1. **Replaces the analytic infinite product** $\\Phi_q(z)$ with an algebraic element.
2. **Promotes Yekutieli truncation** to a **structural cyclotomic projection** at a canonical level.
3. **Predicts the level-selection rule** $n_\\star$ structurally.

## The open component: $n_\\star$

The level-selection rule $n_\\star$ forms the open part. A correct $n_\\star$ must be a structural invariant of $\\mathfrak{H}$, reproduce the empirical $B(\\mathfrak{H})$ across atoms, and be derivable without external calibration.

**Empirical observation.** A uniform-depth canonical evaluation sweeping $k \\in \\{1, 2, 3, 4, 5, 6, 8, 10\\}$ across $\\{D, T, {}^3\\mathrm{He}\\}$ shows:
1. The absolute formula overshoots at every uniform $k$.
2. The subtractive form has a sign-flip at $k = 2$.
3. ${}^3\\mathrm{He}$ overshoots at every $k \\geq 2$ in subtractive form.

## Relation to the $q$-Habiro picture

The two completions remain independent. The full picture forms a bicompletion at the bigraded ideal generated by both $(q;q)_n$ and $P_n(q,z)$, where colored Jones data and brane-tower data coexist. Construction of the bicompletion is open.

## Falsifiability

The conjecture is falsifiable by computation:
1. Pick a candidate $n_\\star$ rule.
2. Compute the projection at $q_0$ for each isotope.
3. Form the binding $B(\\mathfrak{H})$.
4. Compare with the AME values $\\{2.224566, 8.481798, 7.71806\\}$ MeV.

A candidate rule closing all three to within $\\sim 5\\%$ without per-atom retuning constitutes the empirical signature.

## Surviving claims after closure attempts

Six candidate families have been probed and refuted. The remaining claims are:
1. **Algebraic Cauchy-limit claim**: Remains untouched and open. The analytic prerequisite is proved. The sole algebraic gap is identifying which coefficient family reproduces $\\Phi_q$.
2. **$n_\\star$ existence claim**: Refuted across probed forms; remains open.

## Structural finding: pair-knot operators are selected at closed shells

Independent of the refuted forms, the LP dual active set distinguishes the pair-knot composites $\\sigma_{pp}, \\sigma_{nn}$ from per-generator operators exactly at magic configurations, exposing the operator-level signature of shell closure.

## Structural finding: $Z \\leftrightarrow N$ isospin symmetry

At the canonical Markov-trace operator-volume level, the two magic-shell sub-braids are isomorphic Hecke elements: $\\mathrm{tr}_M(\\sigma_{pp}) = \\mathrm{tr}_M(\\sigma_{nn}) = 0.0622$, rendering $Z \\leftrightarrow N$ isospin symmetry exact.

## Structural conclusion

No probed choice recovers the light-isotope binding uniformly; the ${}^3\\mathrm{He}$ gap represents a structural deficit at $A=3$, not an operator-volume choice.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs (real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$). Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.""",

    "hoefsmit-ew-cell-content.md": """**Theorem (Hoefsmit cell-content identification of EW triplet).**
*Let $R$ be the categorical coefficient ring with $q \\in R$ generic. The electroweak force-carriers $W^\\pm, Z, H$—identified topologically as the 2-component torus links $T(2,4), T(2,6), T(2,8)$ on Bring's surface—are realised inside $\\mathrm{End}_R(V^{\\otimes 6})$ as the **disjoint-strand-pair** Hoefsmit projectors:*

$$
  W \\;\\longleftrightarrow\\; \\sigma_1^{\\,4} \\;\\;(\\text{strands 1--2}),
  \\quad
  Z \\;\\longleftrightarrow\\; \\sigma_3^{\\,6} \\;\\;(\\text{strands 3--4}),
  \\quad
  H \\;\\longleftrightarrow\\; \\sigma_5^{\\,8} \\;\\;(\\text{strands 5--6}).
$$

*Strand count $n = 6$ is the **minimum** at which all three carriers admit simultaneous non-trivial action with pairwise-commuting generators. The pure-eigenspace tableaux multiplicities identify eight pairwise-orthogonal projectors.*

### Statement (formal)

For $n = 6$, the standard Young tableaux supply the Hoefsmit seminormal basis. A tableau is **pure for $(\\sigma_1, \\sigma_3, \\sigma_5)$** if all three generators act diagonally. The enumeration shows exactly **20 such pure tableaux**, distributed across eight sym/alt eigenvalue patterns.

### Minimality of $n = 6$

Each EW carrier acts on a single strand-pair. Three carriers need three disjoint strand-pairs. For $n < 6$, carriers share strand-pairs, their generators no longer commute, and the simultaneous-eigenspace decomposition degenerates.

### Refinement: coupling via interface knot

The disjoint-product framing treats $W, Z, H$ as independent. The corrected EW braid uses an **interface knot** $\\bowtie_K \\in H_6(q)$ to mediate the coupling, analogous to the inter-nucleon interface in the deuteron derivation. The corrected braid is:

$$
  \\beta_{\\rm EW}(\\bowtie_K)
  \\;:=\\;
  \\sigma_1^{\\,4} \\cdot \\bowtie_K^{(W \\to Z)} \\cdot \\sigma_3^{\\,6}
  \\cdot \\bowtie_K^{(Z \\to H)} \\cdot \\sigma_5^{\\,8} \\cdot \\bowtie_K^{(H \\to W)}.
$$

This modifies pattern multiplicities, impacts bar-self-duality, gives the Higgs-vev automorphism a concrete form, and twists the 8 pure patterns.

### Resolution of the dimension-collapse issue

The six EW projectors live as rank-1 to rank-3 projectors in $\\mathrm{End}_R(V^{\\otimes 6})$. They sit alongside two non-EW projectors (vacuum and fully-broken), resolving the dimension-collapse issue of the $H_2(q)$-only completeness sum.

### The Plancherel weight is a degenerate special case

The earlier Plancherel-weighted multiplier framing is incorrect. The structural multiplier is the direct unweighted trace $\\mathrm{tr}_{\\rm pure}$, which preserves bar-self-duality automatically from the disjoint-strand-pair construction.

### Implication for $N_v$ derivation

The constrained-PSLQ basis for $N_v$ must use the direct cell-content trace $\\mathrm{tr}_{\\rm pure}$ as the structural input, demoting the Plancherel framing to a degenerate special case.

### Historical alignment: quaternionic electroweak theory

The disjoint-strand-pair identification parallels Morita's quaternionic formulation of the electroweak sector. The QOU tetraplectic boundary supplies a geometric home for the $\\mathrm{SU}(2)$ structures. The unit-quaternion actions are norm-preserving and commute; identifying these algebraic actions with physical carriers is an interpretive alignment, not a derivation."""
}

if __name__ == "__main__":
    rewrite_blocks('/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq8.md', '/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq8.md', new_contents_8_pt2)
