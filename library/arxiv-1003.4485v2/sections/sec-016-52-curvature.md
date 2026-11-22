---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-016-52-curvature
section_title: "Curvature"
section_number: 5.2
pages: 46-47
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.82
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{curvature}

Suppose $\G$ is a Lie 2-group whose crossed module is $(G,H,t,
\alpha)$, and let $(\g,\h,\dt,\dalpha)$ be the corresponding
differential crossed module.  Suppose we have a \define{connection} on
the trivial $\G$-2-bundle over $M$: that is, a $\g$-valued 1-form $A$
and an $\h$-valued 2-form $B$.  

As in ordinary gauge theory, we may define the \define{curvature} of
this connection to be the $\g$-valued 2-form given by:
\[                 F = dA + A \wedge A  .\]
We also have another $\g$-valued 2-form, the \define{fake curvature}
$F - \dt(B)$.  Recall from Section \ref{2-connections} that only a
connection with vanishing fake curvature counts as a 2-connection.  In
other words, we need $\dt(B) = F$ to obtain well-defined parallel
transport over surfaces.  

We may also define the \define{2-curvature} of a connection in higher gauge
theory.  This is the $\h$-valued 3-form given by:
\[                 Z = dB + \dalpha(A) \wedge B  .\]
In the second term here, we compose $\dalpha \maps \g \to \aut(H)$
with the $\g$-valued 1-form $A$ and obtain an $\aut(H)$-valued
function $\dalpha(g)$.  Then we wedge this with $B$, letting $\aut(H)$
act on $\h$ as part of this process, and obtain an $\h$-valued 2-form.

The intuitive idea of 2-curvature is this: just as the curvature 
describes the holonomy of a connection around an infinitesimal loop, 
the 2-curvature describes the holonomy of a 2-connection over an 
infinitesimal 2-sphere.  This can be made precise using formulas for
holonomies over surfaces \cite{MartinsPicken:2007, SchreiberWaldorf:gerbes}

If the 2-curvature of a 2-connection vanishes, the holonomy over a surface
will not change if we apply a smooth homotopy to that surface while
keeping its edges fixed.  A 2-connection whose curvature and 2-curvature
both vanish truly deserves to be called \define{flat}.  We have seen
flat 2-connections already in our discussion of 4-dimensional $BF$
theory in Section \ref{tangent}: the solutions of this theory are 
flat 2-connections.
