import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-surreals-archimedean_seq3.md", "r") as f:
    text = f.read()

replacements = [
    (
        "The companion conjecture\n[`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb)\nreduces the Wightman-axiom portion of the Yang–Mills millennium\nstatement to a single substrate axiom — $C^*$-Frobenius positivity\nof the QOU Frobenius–Hopf substrate at $q = q_0$. This conjecture\nmakes the natural follow-up step: the axiom should be **derivable**\nfrom Wenzl's positivity criterion for\n$\\mathrm{Rep}(U_q(\\mathfrak{sl}_2))$ at $q_0 \\in \\mathbb{R}_{>1}$ —\nnot an independent posit but a consequence of existing unitarity.",
        "The companion conjecture [`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb) reduces the Wightman-axiom portion of the Yang–Mills millennium statement to a single substrate axiom: $C^*$-Frobenius positivity of the QOU Frobenius–Hopf substrate at $q = q_0$. This conjecture takes the natural next step. The axiom should be **derivable** from Wenzl's positivity criterion for $\\mathrm{Rep}(U_q(\\mathfrak{sl}_2))$ at $q_0 \\in \\mathbb{R}_{>1}$. It is not an independent posit, but a consequence of existing unitarity."
    ),
    (
        "The OS-reflection-positivity conjecture\n[`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb)\nleft the substrate $C^*$-Frobenius positivity axiom as the sole\ngenuinely new input needed.",
        "The OS-reflection-positivity conjecture [`conj:os-reflection-positivity-from-reeb`](#conj:os-reflection-positivity-from-reeb) leaves the substrate $C^*$-Frobenius positivity axiom as the sole genuinely new input."
    ),
    (
        "The Hausdorff dimension recurrence\n([Hausdorff recurrence](#rem:hausdorff-dimension-recurrence))\nis the paper's only universal convergence proof: the map\n$q_{n+1} = (q_n^2 - q_n + 1)/q_n$ contracts for all\n$q > 3/4$, with $q = 1$ as a superattracting fixed point\n($F'(1) = 0$).  The $q$-Collatz conjecture has a parallel\nstructure — with one critical difference.",
        "The Hausdorff dimension recurrence ([Hausdorff recurrence](#rem:hausdorff-dimension-recurrence)) provides the only universal convergence proof in this paper. The map $q_{n+1} = (q_n^2 - q_n + 1)/q_n$ contracts for all $q > 3/4$, with $q = 1$ as a superattracting fixed point ($F'(1) = 0$). The $q$-Collatz conjecture shares a parallel structure, but with one critical difference."
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED: {orig[:100]}")
    text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-surreals-archimedean_seq3.md", "w") as f:
    f.write(text)

