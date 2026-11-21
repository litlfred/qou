---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-010-42-formal-products-and-composition
section_title: "Formal products and composition"
section_number: 4.2
pages: 20-20
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.981
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Suppose $a$ and $b$ are the relative homology classes of
two open paths on $\tilde\Sigma$.  If the end of $a$ coincides with the start of $b$,
we let $a+b$ denote the relative homology class of
the concatenation of $a$ and $b$.
Then we introduce a product law on our formal variables:
\begin{equation} \label{eq:X-product-law}
 X_a X_b = \begin{cases} X_{a+b} & \text{if the end of $a$ is the start of $b$}, \\
            0 & \text{otherwise}.
           \end{cases}
\end{equation}

\insfig{three-surface-operators}{Three surface defects connected by two interfaces.  (This picture
lives in the three-dimensional space where the field theory $S[\fg,C,D]$ is defined; we have factored
out the time direction.)}
We can now state one of the key properties of the generating functions $F(\wp, \vartheta)$:
if $\wp$ and $\wp'$ are paths on $C$
which can be concatenated to make a smooth path $\wp \wp'$
(with the end of $\wp$ attached to the start of $\wp'$),
and if both $(\wp, \vartheta)$ and $(\wp', \vartheta)$ are generic,
then
\begin{equation} \label{eq:composition}
 F(\wp, \vartheta) F(\wp', \vartheta) = F(\wp \wp', \vartheta).
\end{equation}
Here is the physical reason for \eqref{eq:composition}.  We consider three surface defects
$\bS_{z_1}$, $\bS_{z_2}$, $\bS_{z_3}$, connected by two interfaces $L_{\wp,\vartheta}$
and $L_{\wp',\vartheta}$, as shown in Figure \ref{fig:three-surface-operators}.  The Hilbert space $\CH$ of framed BPS states
in this situation should be independent of the separation between the interfaces.
For large separations, since the framed BPS states
are localized near the interfaces,
$\CH$ is a tensor product between a space of framed BPS states for the interface $\wp$ and
one for the interface $\wp'$.  On the other hand, by considering the limit of zero separation,
we see that $\CH$ is the space of framed BPS states for the interface $\wp \wp'$.
Equating these two descriptions of $\CH$ gives \eqref{eq:composition}.

(One could wonder whether there should be a $\pm$ sign on the right side of \eqref{eq:composition}; this amounts to asking whether
our rules for fixing the signs of $F(\wp, \vartheta)$, $F(\wp', \vartheta)$ and $F(\wp\wp', \vartheta)$ are compatible with one another.
Fortunately, it will follow from our explicit rules below that there is no sign needed.)
