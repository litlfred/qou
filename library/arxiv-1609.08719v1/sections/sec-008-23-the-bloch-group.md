---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-008-23-the-bloch-group
section_title: "The Bloch group"
section_number: 2.3
pages: 4-4
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.637
latex_coverage_ratio: 1.0
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
\label{subsec:bloch-group}



\begin{definition}
  For any field $F$, the \definedterm{Pre-Bloch group on $F$}, denoted
  $\prebloch{F}$, is defined as
    \[ \prebloch{F} = \frac{\langle \set{z \in F
          \given z \ne 0_F, 1_F} \rangle}{[z_1] - [z_2] +
        \left[\frac{z_2}{z_1}\right] - \left[\frac{1 - z_2}{1 -
            z_1}\right] + \left[ \frac{1 - z_2^{-1}}{1 -
            z_1^{-1}}\right]}. \]
  \end{definition}

  The relation in the denominator is known as the \definedterm{Five
    Term Relation}. The variables $z_1$ and $z_2$ are to be understood
  as cross-ratios of hyperbolic simplices. The relation encodes that
  the union of two simplices with volumes $[z_1]$ and $[z_2]$ is also
  the union of three simplices with volumes $[\frac{z_2}{z_1}]$,
  $[\frac{1 - z_2}{1 - z_1}]$, and
  $[ \frac{1 - z_2^{-1}}{1 - z_1^{-1}}]$. This equivalence is called
  the Pachner $2$-$3$ move (see figure~\ref{fig:pachner-2-3}).

\begin{figure}[h]
  \tikzset{ c/.style={every coordinate/.try} }
  \begin{tikzpicture}[framed]
    \coordinate (A) at (0,0);
    \coordinate (Albl) at (-0.3,1);
    \coordinate (B) at (1.7,-0.3);
    \coordinate (Blbl) at (1.6,-1);
    \coordinate (C) at (1.9,0.1);
    \coordinate (Clbl) at (1.8,0.9);
    \coordinate (D) at (1,1);
    \coordinate (Dlbl) at (0.2,1.4);
    \coordinate (E) at (1,-1);
    \coordinate (Elbl) at (0.2,-1.4);

    \begin{scope}[every coordinate/.style={shift={(0,0.3)}}]
      \filldraw[opacity=0.1] ([c]A) -- ([c]B) -- ([c]C) -- cycle;
      \filldraw[opacity=0.1] ([c]A) -- ([c]B) -- ([c]D) -- cycle;
      \filldraw[opacity=0.1] ([c]D) -- ([c]B) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]B) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]D) -- ([c]B);
      \draw ([c]D) -- ([c]C);
    \end{scope}

    \begin{scope}[every coordinate/.style={shift={(0,-0.3)}}]
      \filldraw[opacity=0.1] ([c]A) -- ([c]B) -- ([c]C) -- cycle;
      \filldraw[opacity=0.1] ([c]A) -- ([c]B) -- ([c]E) -- cycle;
      \filldraw[opacity=0.1] ([c]E) -- ([c]B) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]B) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]E) -- ([c]B);
      \draw ([c]E) -- ([c]C);
    \end{scope}

    \draw[gray, dashed] ([shift={(0,0.3)}]A) -- ([shift={(0,-0.3)}]A);
    \draw[gray, dashed] ([shift={(0,0.3)}]B) -- ([shift={(0,-0.3)}]B);
    \draw[gray, dashed] ([shift={(0,0.3)}]C) -- ([shift={(0,-0.3)}]C);

    \node at (2.5,0) {$\longleftrightarrow$};

    \begin{scope}[every coordinate/.style={shift={(3,0)}}]
      \draw ([c]A) -- ([c]D) -- ([c]B) -- ([c]C) -- ([c]E) -- cycle;
      \draw ([c]A) -- ([c]B) -- ([c]E);
      \draw ([c]A) -- ([c]C) -- ([c]D);


      \node (abubble) at ([c]A) {};
      \node (alabel) at ([c]Albl) {$0$};
      \draw [->] (alabel) -- (abubble);

      \node (bbubble) at ([c]B) {};
      \node (blabel) at ([c]Blbl) {$1$};
      \draw [->] (blabel) -- (bbubble);

      \node (cbubble) at ([c]C) {};
      \node (clabel) at ([c]Clbl) {$\infty$};
      \draw [->] (clabel) -- (cbubble);

      \node (dbubble) at ([c]D) {};
      \node (dlabel) at ([c]Dlbl) {$z_1$};
      \draw [->] (dlabel) -- (dbubble);

      \node (ebubble) at ([c]E) {};
      \node (elabel) at ([c]Elbl) {$z_2$};
      \draw [->] (elabel) -- (ebubble);
    \end{scope}

    \node at (5.5,0) {$\longleftrightarrow$};

    \begin{scope}[every coordinate/.style={shift={(6,0)}}]
      \filldraw[opacity=0.1] ([c]D) -- ([c]A) -- ([c]B) -- cycle;
      \filldraw[opacity=0.1] ([c]D) -- ([c]E) -- ([c]B) -- cycle;
      \filldraw[opacity=0.1] ([c]D) -- ([c]A) -- ([c]E) -- cycle;
      \draw ([c]A) -- ([c]D) -- ([c]B) -- cycle;
      \draw ([c]A) -- ([c]E) -- ([c]B);
      \draw ([c]E) -- ([c]D);
    \end{scope}

    \begin{scope}[every coordinate/.style={shift={(8,0)}}]
      \filldraw[opacity=0.1] ([c]D) -- ([c]C) -- ([c]B) -- cycle;
      \filldraw[opacity=0.1] ([c]D) -- ([c]B) -- ([c]E) -- cycle;
      \filldraw[opacity=0.1] ([c]E) -- ([c]D) -- ([c]C) -- cycle;
      \draw ([c]D) -- ([c]C) -- ([c]B) -- cycle;
      \draw ([c]D) -- ([c]E) -- ([c]B);
      \draw ([c]E) -- ([c]C);
    \end{scope}

    \begin{scope}[every coordinate/.style={shift={(7.4,0.2)}}]
      \filldraw[opacity=0.1] ([c]A) -- ([c]D) -- ([c]C) -- cycle;
      \filldraw[opacity=0.1] ([c]A) -- ([c]D) -- ([c]C) -- cycle;
      \filldraw[opacity=0.1] ([c]A) -- ([c]E) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]D) -- ([c]C) -- cycle;
      \draw ([c]A) -- ([c]E) -- ([c]C);
      \draw ([c]E) -- ([c]D);
    \end{scope}

    \draw[gray, dashed] ([shift={(6,0)}]D) -- ([shift={(8,0)}]D)
                        -- ([shift={(7.4,0.2)}]D) -- cycle;
    \draw[gray, dashed] ([shift={(6,0)}]E) -- ([shift={(8,0)}]E)
                        -- ([shift={(7.4,0.2)}]E) -- cycle;
  \end{tikzpicture}
  \caption{The Pachner $2$-$3$ move.}
  \label{fig:pachner-2-3}
\end{figure}

\begin{definition}
  For any field $F$, the \definedterm{Bloch group on $F$}, denoted
  $\bloch{F}$, is the kernel of the map
  $d : \prebloch{F} \to F^{\ast} \wedge_{\mathbb{Z}} F^{\ast}$ defined
  by \[ d: [z] \mapsto z \wedge (1-z). \]
\end{definition}

The map $d$ is an analogue of the Dehn invariant map
\parencite{neumannhilberts3rd}, which (for $F = \mathbb{C}$) fits into
an exact sequence of scissors congruence described in
e.g.\ \parencite{dupontscissors}. Thus, understanding
$\bloch{F} = \ker d$ provides insight into scissors congruence groups
and generalizations of Hilbert's third problem.
