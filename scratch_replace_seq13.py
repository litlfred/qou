import re

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-surreals-archimedean_seq0.md", "r") as f:
    text = f.read()

replacements = [
    (
        "The point of this survey is to license the appendix's central\nmove: the substrate parameter $q$ may be taken in $\\mathbf{No}$,\nin the infinitesimal neighbourhood of $1$, without disturbing\nany of the algebraic machinery of the main paper. A systematic\nsurvey of the QOU content objects finds that the bulk of the\nformal structure is **purely algebraic**: it depends only on the\nground ring being a field (frequently a field of characteristic\nzero), not on any analytic or topological property of\n$\\mathbb{R}$ or $\\mathbb{C}$.",
        "We present this survey to justify our central move: we may take the substrate parameter $q \\in \\mathbf{No}$ in the infinitesimal neighbourhood of $1$, without disturbing any algebraic machinery of this paper. The bulk of the formal structure is **purely algebraic**. It depends only on the ground ring being a field (typically of characteristic zero), independent of any analytic or topological property of $\\mathbb{R}$ or $\\mathbb{C}$."
    ),
    (
        "The obvious shortcut — \"axiomatise a single integration operator\non $\\mathbf{No}$ and use it everywhere\" — is closed off by a\ntheorem. Costin, Ehrlich, and Friedman [@costin-ehrlich-friedman2015]\nprove a two-sided result on integration over the surreals:",
        "The shortcut of axiomatising a single integration operator on $\\mathbf{No}$ is mathematically closed. Costin, Ehrlich, and Friedman [@costin-ehrlich-friedman2015] prove a two-sided result on integration over the surreals:"
    ),
    (
        "The lesson for QOU is that we do **not** want a measure on all\nof $C(\\mathbf{No})$ — that object does not exist, and trying to\nmanufacture one via a categorical proxy (e.g.\\ asserting the\nFrobenius pairing $\\int_A : A \\otimes A \\to \\mathbf{1}$ at $A =\nC(\\mathbf{No})$) would just smuggle the obstruction into the\naxiom. What we want instead is an audit: for each genuine\nuse of an analytic structure in the main paper, decide whether\nthe use lifts to $\\mathbf{No}$ on the CEF-positive side\n(algebraic / transserial) or whether it requires a\ncustom workaround. The audit below is that exercise.",
        "We do **not** postulate a measure on all of $C(\\mathbf{No})$. That object does not exist. Manufacturing one via a categorical proxy (e.g.\\ asserting the Frobenius pairing $\\int_A : A \\otimes A \\to \\mathbf{1}$ at $A = C(\\mathbf{No})$) smuggles the obstruction into the axiom. Instead, we audit each genuine use of an analytic structure in this paper to determine whether the use lifts to $\\mathbf{No}$ on the CEF-positive side (algebraic / transserial) or requires a custom workaround. We perform this audit below."
    ),
    (
        "A text search for Lebesgue, Haar, and Hausdorff measures across\nthe content objects returns only a handful of matches, almost\nall of which turn out to be *categorical* or *algebraic* by\ncloser inspection:",
        "We evaluate Lebesgue, Haar, and Hausdorff measures across the content objects. Almost all instances are *categorical* or *algebraic* upon inspection:"
    ),
    (
        "The surreal lift is dramatically less lossy than a\nfirst-pass survey suggests. With two narrow exceptions — the\nMöbius energy integral and the hyperbolic-volume side of the\nKashaev comparison — every load-bearing step of the QOU mass\nformula and the categorical axioms transfers to $\\mathbf{No}$\nwithout modification. The appendix's remaining work is\nconstructive, not defensive: building new structures\n(birthday grading, $\\varepsilon$-relaxed axioms, standard-part\nfunctor) in the surreal ambient.",
        "The surreal lift preserves nearly all structure. With two narrow exceptions — the Möbius energy integral and the hyperbolic-volume side of the Kashaev comparison — every load-bearing step of the mass formula and categorical axioms transfers to $\\mathbf{No}$ without modification. The remaining work constructs new structures (birthday grading, $\\varepsilon$-relaxed axioms, standard-part functor) in the surreal ambient."
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals-archimedean_seq0.md", "w") as f:
    f.write(text)

