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

new_contents_11_pt2 = {
    "pn-averaging-uniqueness.md": """**Proposition (canonical p-n averaging uniqueness).**
*Any two p-n interface averaging functionals $\\sigma_{pn}, \\sigma_{pn}'$ on $H_{3A}(R, q)$ that both satisfy (a) **bar-invariance** $\\sigma_{pn}(q) = \\sigma_{pn}(q^{-1})$, (b) **color-flavor compatibility** (Bring color-tube symmetry over quark composition), and (c) **standard normalisation** $\\sigma_{pn} = z$ with the same $z$ are equal block-wise. Hence the canonical p-n averaging is uniquely determined by these three structural hypotheses.*

## Setting
The QOU mass identity at $A \\geq 2$ contracts a per-interface averaging functional $\\sigma_{pn}$ across the p-n boundary slice in $H_{3A}(R, q)$. Both candidates (uniform bar-invariant and Bring color-tube weighted) satisfy bar-invariance and standard normalisation; they differ on the per-sheet color weighting. The uniqueness theorem states that once color-flavor compatibility is fixed, the averaging is determined.

### Derivation chain for the closed-form weight
The substrate evaluation $w(t, t', q) = 1/(1 - h_q \\cdot q^{10})$ is derived, not empirical. Bring's surface has genus $g = 4$. The genus-4 force-carrier pair is $\\{T(2,9), T(3,5)\\}$. The formula $\\alpha_{\\text{shift}}(T_{p,k}) = k \\cdot (p-1)$ specialises at $(p, k) = (3, 5)$ to $10$, which is the pole order of $\\sigma$ on $T(3,5)$. The Bring color-tube weight inherits this pole order: $q^{10}$ is the $\\alpha_{\\text{shift}}(T(3,5))$-th power.

## Lean structure
The uniqueness is staged via conditional classes: `BarInvariant`, `ColorFlavorCompatible` (open), and `StandardNorm`. Conditional on the three classes, `theorem pn_averaging_unique` proves $\\sigma_{pn} = \\sigma_{pn}'$ sorry-free. Closing the open class forms the genuine open math.""",

    "averaging-resonance-rule.md": """**Theorem (averaging-resonant rung selection rule).**
*Let $\\sigma_{\\mathrm{avg}} = \\tfrac{1}{2}(\\sigma + \\sigma^{-1})$ be the bar-symmetric averaged-crossing operator on $H_{n_{\\mathrm{total}}}(R, q)$, and let $P_{\\mathrm{avg}} = (1 + \\overline{\\,\\cdot\\,})/2$ be the bar-invariant averaging projection. For canonical typed-$\\mathbf{B}_3$ braids of total strand count $n_{\\mathrm{total}}$ admitting the half-fill cyclic structure, the unique $\\sigma_{\\mathrm{avg}}$-resonant rung is*

$$
  k_{\\mathrm{res}}
  \\;=\\;
  \\left\\lfloor \\frac{n_{\\mathrm{total}}}{2} \\right\\rfloor
  \\;+\\; \\mathbb{1}_{\\mathrm{wrap}}(n_{\\mathrm{total}}),
$$

*where the wrap indicator $\\mathbb{1}_{\\mathrm{wrap}}$ adds one when the half-fill cycle closes through the proton recipe's inter-nucleon interface; otherwise zero.*

## Structural content
Two layers compose:
1. **Half-fill cyclicity** — the bar-invariant projection restricted to a typed-$\\mathbf{B}_3$ braid admits the canonical Markov-trace expansion at the half-fill rung. This supplies the rung selection.
2. **Bar-invariant magnitude** — at the selected rung, the fingerprint contributes magnitude $1/2$ to the resonant Markov-trace coefficient.

The two layers together yield $c_5 = -b^2 - 1/2$ at rung $k = 5$. This proposition supplies the rung-selection layer.

## The $k = 5$ selection
For the proton typed-$\\mathbf{B}_3$ braid with $n_{\\mathrm{total}} = 9$, the half-fill floor is $4$ and the wrap-around contribution is $+1$, giving $k_{\\mathrm{res}} = 5$. The wrap-around contribution forms a structural consequence of the inter-nucleon interface closing the cycle.

Defining this explicit averaging resonance rule as the predictive mechanism for the typed-$B_3$ proton recipe forms a mathematically novel structural claim.""",

    "meson-color-tube-uniqueness.md": """**Proposition (meson m_K/m_π ratio uniqueness via the α_shift universal chain).**
*The substrate-evaluated ratio $m_K^2 / m_\\pi^2$ factors uniquely through the two torus knots $T(2, 3)$ and $T(2, 4)$ as $[\\alpha_{\\text{shift}}(T(2,3))]_q \\cdot [\\alpha_{\\text{shift}}(T(2,4))]_q = [3]_q \\cdot [4]_q$, with the $q$-integer indices forced by the proved $\\alpha_{\\text{shift}} = k \\cdot (p - 1)$ formula.*

## The meson force-carrier pair $\{T(2, 3), T(2, 4)\}$
The $\\alpha_{\\text{shift}}$ universal derivation chain identifies the relevant torus knots. $T(2, 3)$ (trefoil) gives $[3]_q$, and $T(2, 4)$ gives $[4]_q$. The pair forms the smallest non-trivial torus-knot pair on the substrate's Hecke-algebra surface.

## Lean structure
The uniqueness is staged via conditional classes: `MesonGMORFactorization` and `MesonForceCarrierPair`. Given the two classes, the ratio factors sorry-free.

## Remaining open math
- Why specifically the smallest non-trivial torus-knot pair carries the meson force-carrier role.
- The closed-form $q$-character evaluation $[n]_q(q_0)$ at the substrate value (shared with the resolvent open math).

This block provides the structural reason for the two $q$-integer indices. The $\\alpha_{\\text{shift}}$ identification embeds the meson into the same universal pole-order chain as $1/\\alpha_{\\rm EM}$ and the Bring color-tube p-n averaging weight.""",

    "bring-residue-resolvent.md": """**Proposition (Bring residue $\\to$ canonical resolvent form).**
*The substrate evaluation of the residue / Schwarz integral on Bring's surface around the simple pole of order $n$ of $\\sigma$ on the torus knot $T(p, k)$ with $\\alpha_{\\text{shift}}(p, k) = n$ yields the canonical resolvent form $F_n(q) = 1 / (1 - h_q \\cdot q^n)$ where $h_q = q - q^{-1}$. This forms the shared closed-form derivation across the $\\alpha_{\\text{shift}}$ universal chain's specialisations.*

## The shared smaller-scope open math
The resolvent step derivations share the closed form from the contour-integral evaluation on Bring's surface. This proposition scaffolds that derivation as a single Lean class and theorem, then specialises to the concrete pole orders used downstream.

## Lean structure
`BringResidueAtOrder` axiomatises the contour-integral evaluation. Its sole field `pole_nonzero` records the pole non-vanishing. The canonical resolvent satisfies the resolvent equation sorry-free. Specialisations include pole orders 10 (p-n averaging), 9 ($1/\\alpha_{\\rm EM}$), and 3, 4 (meson pair).

Closing `BringResidueAtOrder n q` requires either an analytic route (residue machinery) or an algebraic route (Bloch-Suslin framework). Both routes converge on the same closed form. Closing the class once discharges the residue open math across all three PRs.""",

    "binding-alpha-shift-extension.md": """**Proposition (binding $A\\ge3$ via per-rep Reeb phase at a force-carrier torus knot).**
*The light-atom binding energy $B(A) = m_e \\cdot \\rho_0 \\cdot \\alpha_{\\text{shift}}(T(p_A, k_A))$ is uniquely determined by the substrate-universal per-rep Reeb coupling $\\rho_0$ pinned by the deuteron, and the substrate-fixed force-carrier torus knot $T(p_A, k_A)$ per nucleus. Both legs route through the proved $\\alpha_{\\mathrm{shift}} = k\\cdot(p-1)$ formula.*

## Setting — the $A \\ge 3$ binding gap
The binding-endomorphism analogy closes the deuteron but undershoots $A \\ge 3$. The extensive observable lives in the per-rep $q$-Reeb rotation phase on the column-rich irrep of a substrate-fixed force-carrier torus knot. $\\alpha_{\\text{shift}}(T_{p, k})$ forms the pole order of $\\sigma$ on the column-rich irrep.

## The unification
Per nucleus $A$, identifying the force-carrier torus knot $T(p_A, k_A)$ gives the binding closure. The deuteron candidate $T(2, 3)$ is motivated by being the smallest non-trivial torus knot and the canonical boundary torus knot of $\\mathcal{B}_3$. Calibration consistency gives the abstract substrate coupling $\\rho_0 \\approx 1.451$.

## Lean structure
`BindingPerRepReebPhase` provides the substrate axiom for per-rep Reeb phase factorisation. `BindingForceCarrierKnot` states the per-$A$ pole order realises via the proved formula. Consolidating all four nuclei into one instance carries the full Phase-3 candidate table.

## Remaining open math
Phase 3 identifies the specific $(p_A, k_A)$ for each light nucleus. Closing Phase 3 requires the per-nucleus minimisation argument on $H_{3A}(q)$'s Wedderburn block at the binding's smallest non-trivial irrep.""",

    "magic-A-binding-formula.md": """**Theorem (conditional on `conj:magic-numbers-bring` and `prop:gravity-spectral-prefactor`).**
*For a light nucleus $^A_Z\\mathfrak{X}$ that is doubly magic, the binding energy admits the closed form*

$$
  \\mathfrak{B}(^A_Z\\mathfrak{X}) \\;=\\; \\rho_F \\cdot \\mathfrak{m}_e \\cdot A \\cdot 8G
$$

*where $G$ is Catalan's constant, $8G = \\mathrm{Vol}(\\mathrm{Borromean})$ is the universal residue prefactor, and $\\rho_F \\in \\mathbb{R}$ is the substrate-determined structural prefactor.*

*Specialised to $^4_2\\mathrm{He}$ with $\\rho_F = 2$:*

$$
  \\mathfrak{B}(^4_2\\mathrm{He})
    \\;=\\; 2 \\cdot \\mathfrak{m}_e \\cdot 4 \\cdot 8G
    \\;\\approx\\; 29.956\\;\\mathrm{MeV}
$$

*This is a relative miss of $+5.9\\%$. It is tighter than the alpha-shift formula, which assumes a single hyperbolic force-carrier knot per nucleus—an assumption breaking for doubly-magic nuclei.*

## Necessity of a separate doubly-magic formula
The framework's two binding paths apply to distinct categorical regimes. At a doubly-magic level, the Littlewood–Richardson fusion collapses to a single self-conjugate Specht module. There is no Wedderburn channel to absorb further binding through Hecke crossings. The per-rep Reeb phase mechanism vanishes, and the binding is set by the universal Borromean residue $8G$ scaled by nucleon count. The doubly-magic case represents exactly this rectangular-spike limit.

## $\\rho_F$ for $^4_2\\mathrm{He}$
The substrate-determined prefactor for $^4_2\\mathrm{He}$ is $\\rho_F = 2$, consumed as an input hypothesis on the instance. The categorical derivation of the integer $2$ is not closed in this proposition. The comparison witness quantifies the $80\\times$ gap closure for $^4_2\\mathrm{He}$."""
}

if __name__ == "__main__":
    rewrite_blocks('/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq11.md', '/Users/litlfred/space_cats/qou/amalgamated_done/mass-theory_seq11.md', new_contents_11_pt2)
