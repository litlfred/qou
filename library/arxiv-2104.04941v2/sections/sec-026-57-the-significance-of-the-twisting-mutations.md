---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-026-57-the-significance-of-the-twisting-mutations
section_title: "The significance of the ``twisting'' mutations"
section_number: 5.7
pages: 31-32
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.893
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:what-does-the-twist-do}

  The quiver mutations $\murot$ and $\muflip$ are intended to compose
  easily without requiring renaming the vertices of the quiver. For
  example, $\murot^2(Q)$ should be identical to $\murot^{-1}(Q)$.

  Unfortunately, quiver mutations that yield equivalent seeds do not
  necessarily preserve the positions of those seeds. For example,
  consider the classic ``pentagon recurrence'', which happens to be
  equivalent to $\murowperm$ on a row which is of Dynkin type $A_2$. The
  switching of positions is exactly the the action of $\sigma_{A_2}$ on
  the Dynkin diagram.

  \begin{figure}[h]
    \centering
    \includestandalone[mode=image|tex]{fig/pentagon-recurrence}

    \caption{The pentagon recurrence.
      \label{fig:pentagon-recurrence}
    }
  \end{figure}

  The $\muint{Oi}$ parts of $\murot$ and $\muflip$, distinguishing them
  from $\murottwist$ and $\mufliptwist$, are exactly to address these
  actions of $\sigma_G$. If desired, shorter mutations may be used at
  the expense of slightly more complicated identifications between
  variables.
