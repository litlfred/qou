---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.964
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
The program of Fock--Goncharov, starting with
  \cite{fockgoncharov2006}, aims to describe representation spaces of
  hyperbolic surfaces into Lie groups by moduli spaces defined by
  polynomial equations. These moduli spaces carry a positive structure
  (see \cref{def:positive-structure}), and in the case of the Lie group
  $\PSL_2(\mathbb{R})$, the associated positive spaces can be identified
  with Teichmüller space and decorated Teichmüller space. For more
  complicated Lie groups, these positive spaces give (decorated) higher
  Teichmüller spaces.

  Our result regards an additional structure, a cluster ensemble
  structure (see \cref{sec:cluster-ensembles}), which allows
  manipulating these moduli spaces efficiently via quivers.

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.40\textwidth}
      \centering
      \includestandalone[mode=image|tex,height=1.5in]{fig/sigma-1}
      \caption{Cutting $\Sigma$ into a fundamental domain.
        \label{fig:sigma-1}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.40\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-2}

      \caption{Embedding a fundamental domain for $\Sigma$ into the disk
        model for hyperbolic space.
        \label{fig:sigma-2}
      }
    \end{subfigure}
    \caption{Putting a hyperbolic structure on $\Sigma$.
      \label{fig:rho-by-fundamental-domain}
    }
  \end{figure}
