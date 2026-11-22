---
doc_id: arxiv-1003.4485v2
doc_title: "An Invitation to Higher Gauge Theory"
section_id: sec-002-3-2-categories-and-2-connections
section_title: "2-Categories and 2-Connections"
section_number: 3
pages: 11-12
source_pdf: 1003.4485v2.pdf
source_sha256: 714d73873cecd73a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "An Invitation to Higher Gauge Theory — In this easy introduction to higher gauge theory, we describe parallel trans- port for particles and strings in terms of 2-connections on 2-bundles."
---
\label{2-connections}

Now we want to climb up one dimension, and talk about `2-connections'.
A connection tells us how particles transform as they move along
paths.  A 2-connection will also tell us how \emph{strings} transform as 
they sweep out \emph{surfaces}.  To make this idea precise, we need to take
everything we said in the previous section and boost the dimension
by one.  Instead of categories, we need `2-categories'.  Instead of
groups, we need `2-groups'.  Instead of the path groupoid, we need the
`path 2-groupoid'.  And instead of functors, we need `2-functors'.
When we understand all these things, the analogue of Theorem
\ref{thm:connections} will look strikingly similar to the original
version:

\begin{unnumbered-thm}
For any Lie 2-group $\G$ and any smooth manifold $M$,
there is a one-to-one correspondence between:
\begin{enumerate}
\item 2-connections on the trivial principal $\G$-2-bundle over $M$,
\item pairs consisting of 
a smooth $\g$-valued 1-form $A$ and a smooth $\h$-valued 
2-form $B$ on $M$, such that
\[           \dt(B) = dA + A \wedge A \]
where we use $\dt \maps \h \to \g$, the differential of the map $t \maps
H \to G$, to convert $B$ into a $\g$-valued 2-form, and
\item smooth 2-functors
\[ \hol \maps \P_2(M) \to \G \]
where $\P_2(M)$ is the path 2-groupoid of $M$.
\end{enumerate}
\end{unnumbered-thm}

What does this say?  In brief: there is a way to extract from a Lie
2-group $\G$ a pair of Lie groups $G$ and $H$.  Suppose we have a
1-form $A$ taking values in the Lie algebra of $G$, and a 2-form $B$
valued in the Lie algebra of $H$.  Suppose furthermore that these
forms obey the equation above.  Then we can use
them to consistently define parallel transport, or `holonomies', for
paths and surfaces.  They thus define a `2-connection'.

That is the idea.  But to make it precise, we need 2-categories.
