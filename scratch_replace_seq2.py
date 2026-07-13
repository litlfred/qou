import sys

with open("/Users/litlfred/space_cats/qou/amalgamated_input/appendix-mass-binding-algorithms_seq2.md", "r") as f:
    text = f.read()

replacements = [
    (
        r"*The categorical action is **fibre-independent**: it depends only\non the rigid-monoidal structure of $\mathbf{C}$, not on the choice\nof fibre functor $\tau$. The archimedean specialisation enters at\nStep 9 (mass identity) via the Markov trace evaluation at $q_0$.*",
        "*The categorical action is **fibre-independent**. It depends strictly on the rigid-monoidal structure of $\\mathbf{C}$, independent of the fibre functor $\\tau$. Archimedean specialisation enters at Step 9 (mass identity) via Markov trace evaluation at $q_0$.*"
    ),
    (
        r"*Confluence of the rewriter is structural: any two reduction\norders end at the same normal form by the Diamond Lemma applied\nto the Hecke and braid relations (both are linear quadratic and\nmutually compatible).*".replace("\\n", "\n"),
        "*The rewriter's confluence is structural. The Diamond Lemma guarantees that any reduction order reaches the same normal form, since the Hecke and braid relations are linear quadratic and mutually compatible.*".replace("\\n", "\n")
    ),
    (
        r"*The reducer is the **single source** of Hecke normal forms in the\nQOU pipeline; every downstream algorithm consumes `NF(w)`, not the\nraw braid word. Treating the normal form as the canonical object\n(rather than the braid) is what makes the rest of the chain\n$q$-rational.*".replace("\\n", "\n"),
        "*The reducer is the **single source** of Hecke normal forms in the pipeline. Every downstream algorithm consumes `NF(w)`, not the raw braid. Treating the normal form as the canonical object makes the subsequent chain $q$-rational.*".replace("\\n", "\n")
    ),
    (
        r"*Large-$A$ scaling (atom braids of step 9b): the multi-nucleon\nbraid word has a **monotone** non-decreasing generator sequence —\nnucleon $k$ uses $\sigma_{3k},\sigma_{3k+1}$ and one interface\ncrossing $\sigma_{3k+2}$, never revisiting a generator — so each\n$O_g$ is a polynomial in a single $\sigma_g$. In the\nmultiplicity-free seminormal (Gelfand–Zetlin) basis $\sigma_g$\nmoves only one level of the chain\n$\varnothing \subset s_1 \subset \cdots \subset s_n = \lambda$, and\ntrace closure forces each $O_g$ to its diagonal block, collapsing\nstep 3–4 to a transfer matrix over fine-Bratteli edges\n$s_g \subset s_{g+1}$. This yields every $\chi^\lambda(\beta)$ in a\nsingle sweep without materialising the $d_\lambda$-dimensional\nHoefsmit representation: the cost is the fine-Bratteli edge count\n(a few thousand at $n = 21$) rather than $n!$, extending the\nnumerical $\mathrm{tr}_M$ at $q_0$ to $A \geq 6$ ($^6$Li, $^7$Li,\nand beyond) in seconds. Implemented in\n[`chi_monotone_transfer.py`](../../../computations/chi_monotone_transfer.py)\nwith the per-atom trace assembly in\n[`tr_m_atom_via_transfer.py`](../../../computations/tr_m_atom_via_transfer.py)\n(witness\n[`tr-m-atom-via-transfer.witness.json`](../../../computations/tr-m-atom-via-transfer.witness.json)),\nvalidated to the 50-dps floor against the Hoefsmit characters\n($n \leq 6$) and the cached per-basis-vector trace witnesses\n($n \leq 12$). The production binding consumers\n[`binding_canonical`](../../../computations/binding_canonical.py)\nand\n[`canonical_tr_m_via_branching`](../../../computations/canonical_tr_m_via_branching.py)\n($A \geq 3$) route their atom-trace through this transfer path (the\nformer brute-force atom-level Wedderburn tower,\n`atom_level_wedderburn_tower.py`, is retained only as a\n$d_\lambda$-explicit cross-check).*".replace("\\n", "\n"),
        "*For large-$A$ scaling (Step 9b atom braids), the multi-nucleon braid word features a **monotone** non-decreasing generator sequence. Nucleon $k$ uses $\\sigma_{3k}, \\sigma_{3k+1}$ and one interface crossing $\\sigma_{3k+2}$, never revisiting a generator. Thus, each $O_g$ is a polynomial in a single $\\sigma_g$.\n\nIn the multiplicity-free seminormal (Gelfand–Zetlin) basis, $\\sigma_g$ moves exactly one level of the chain $\\varnothing \\subset s_1 \\subset \\cdots \\subset s_n = \\lambda$. Trace closure forces each $O_g$ into its diagonal block. This collapses Steps 3–4 into a transfer matrix over fine-Bratteli edges $s_g \\subset s_{g+1}$. We compute every $\\chi^\\lambda(\\beta)$ in a single sweep without materializing the $d_\\lambda$-dimensional Hoefsmit representation. The computational cost scales with the fine-Bratteli edge count (e.g., a few thousand at $n = 21$) rather than $n!$. This extends numerical $\\mathrm{tr}_M$ evaluation at $q_0$ to $A \\geq 6$ ($^6$Li, $^7$Li, and beyond) in seconds.\n\nThe implementation resides in [`chi_monotone_transfer.py`](../../../computations/chi_monotone_transfer.py), with per-atom trace assembly in [`tr_m_atom_via_transfer.py`](../../../computations/tr_m_atom_via_transfer.py) (witness [`tr-m-atom-via-transfer.witness.json`](../../../computations/tr-m-atom-via-transfer.witness.json)). We validate it to the 50-dps floor against Hoefsmit characters ($n \\leq 6$) and cached per-basis-vector trace witnesses ($n \\leq 12$). The production binding consumers [`binding_canonical`](../../../computations/binding_canonical.py) and [`canonical_tr_m_via_branching`](../../../computations/canonical_tr_m_via_branching.py) ($A \\geq 3$) route their atom-trace through this transfer path. The brute-force atom-level Wedderburn tower (`atom_level_wedderburn_tower.py`) serves strictly as a $d_\\lambda$-explicit cross-check.*".replace("\\n", "\n")
    ),
    (
        r"*The Wedderburn decomposition is the **single most expensive\nstep** in the chain for $n > 6$ because $y_\lambda(q)$ involves\nnested $[k]_q$ factors. The native Rust core caches partitions\nacross braid-trace calls.*".replace("\\n", "\n"),
        "*The Wedderburn decomposition is the **most expensive step** in the chain for $n > 6$, as $y_\\lambda(q)$ involves nested $[k]_q$ factors. The native Rust core caches partitions across braid-trace calls.*".replace("\\n", "\n")
    ),
    (
        r"*The Frobenius pairing is what makes $H_n(q)$ a **rigid**\nFrobenius algebra — the categorical self-duality is dual to it\nunder decategorification. Both are required for the Wedderburn\ndecomposition (Step 5) to land in the correct basis.*".replace("\\n", "\n"),
        "*The Frobenius pairing makes $H_n(q)$ a **rigid** Frobenius algebra. Categorical self-duality is dual to it under decategorification. Both ensure the Wedderburn decomposition (Step 5) lands in the correct basis.*".replace("\\n", "\n")
    ),
    (
        r"*$E_2$-collapse is what justifies treating the GS filtration as\n**exact**: any higher differential would re-mix length levels and\nbreak the jet-order matching used by Step 8.*".replace("\\n", "\n"),
        "*$E_2$-collapse justifies treating the GS filtration as **exact**. Any higher differential would re-mix length levels and break the jet-order matching of Step 8.*".replace("\\n", "\n")
    ),
    (
        r"*The jet-prefix truncation is the **gate** between symbolic\n($q$-exact) compute and the archimedean evaluation at $q_0$. The\nchoice of $N$ is precision-driven; see the $c_k$ truncation\nsidecar for the analogous truncation in the $\mathfrak{Q}_\beta$ ladder.*".replace("\\n", "\n"),
        "*The jet-prefix truncation **gates** symbolic ($q$-exact) compute from archimedean evaluation at $q_0$. Target precision determines $N$. See the $c_k$ truncation sidecar for the analogous truncation in the $\\mathfrak{Q}_\\beta$ ladder.*".replace("\\n", "\n")
    )
]

for orig, new in replacements:
    if orig not in text:
        print(f"FAILED TO FIND:\n{orig[:100]}...\n")
    else:
        text = text.replace(orig, new)

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-mass-binding-algorithms_seq2.md", "w") as f:
    f.write(text)
