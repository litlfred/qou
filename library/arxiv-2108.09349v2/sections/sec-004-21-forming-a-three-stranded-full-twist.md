---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-004-21-forming-a-three-stranded-full-twist
section_title: "Forming a three-stranded full twist"
section_number: 2.1
pages: 3-4
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.987
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:fulltwist}  

Let $S_0$ be the top 6-punctured sphere.  Label the punctures 0 through 5 and divide $S_0$ into eight triangles as shown in Figure~\ref{fig:fulltwist}(a).  Think of the punctures --- and the strands descending from them --- as living in the plane of the page, so $\triangle 025$ is in front of the page and $\triangle 035$ is behind the page.  Their shared edge, 05, passes through the point at infinity.  The colors indicate the identifications on $S_0$ that will yield a full twist:
\begin{description}
\item[gray] $\triangle 025$ is identified to $\triangle 035$ 
\item[white] $\triangle 023$ is identified to $\triangle 523$ 
\item[yellow]$\triangle 012$ in the front is identified to $\triangle 543$ in the front
\item[pink]$\triangle 012$ in the back is identified to $\triangle 543$ in the back
\end{description}
\begin{figure}[ht]\vskip.25in

\begin{overpic}[unit=.25in]{fulltwistbright.pdf}
\put(0.57, 14.5){\tiny0}\put(1.9, 14.5){\tiny1}\put(3.23, 14.5){\tiny2}\put(4.56, 14.5){\tiny3}\put(5.89, 14.5){\tiny4}\put(7.22, 14.5){\tiny5}

\put(10.57, 12){\tiny0}\put(11.24, 12){\tiny1}\put(11.91, 12){\tiny2}\put(15.88, 12){\tiny3}\put(16.55, 12){\tiny4}\put(17.22, 12){\tiny5}

\put(10.57, 6){\tiny0}\put(11.24, 6){\tiny1}\put(11.91, 6){\tiny2}\put(15.88, 6){\tiny3}\put(16.55, 6){\tiny4}\put(17.22, 6){\tiny5}

\put(10.57, 0){\tiny0}\put(11.24, 0){\tiny1}\put(11.91, 0){\tiny2}\put(15.88, 0){\tiny3}\put(16.55, 0){\tiny4}\put(17.22, 0){\tiny5}

\put(0.57, 0){\tiny0}\put(1.24, 0){\tiny1}\put(1.91, 0){\tiny2}\put(5.88, 0){\tiny3}\put(6.55, 0){\tiny4}\put(7.22, 0){\tiny5}

\put(0,15){\small(a)}
\put(9.9,16.5){\small(b)}
\put(9.9,10.5){\small(c)}
\put(9.9,4.5){\small(d)}
\put(0,4.5){\small(e)}

\end{overpic}
\caption{Forming a full twist $C$.\label{fig:fulltwist}}
\end{figure}
To see that identifying $S_0$ to itself in this way is the same as attaching a 3-ball with a full twist removed, first fold $S_0$ along the 23 edge into a cylindrical pillow shown in Figure~\ref{fig:fulltwist}(b).  As we go step-by-step through the identifications, we will follow the punctures (their paths are drawn as strands) and see they sweep out a full twist.  The extra markings --- cyan on the white triangles and gray on the yellow and pink ones --- will help us follow the triangles through each step.  
\begin{itemize}
\item $\triangle 025$ is identified to $\triangle 035$:  Figure~\ref{fig:fulltwist}(c) shows the result of bringing the 2 and 3 strands together to identify the gray triangles.  Placing this triangle in the plane of the page means the 23 (blue) edge forms a belt around a new pillow with half in front, as the 1 and 2 strands are, and half behind as the 3 and 4 strands are.  The left side of the pillow consists of $\triangle 023$ and both $\triangle 012$'s (appearing in the front).  The right side is formed by $\triangle 523$ and both $\triangle 543$'s (in the back).  This diagram is analogous to the third step in Figure~\ref{fig:clasp} in the appendix.
\item $\triangle 023$ is identified to $\triangle 523$:  By pushing the 0 and 5 strands into the pillow until they meet, $\triangle 023$ can be identified to $\triangle 523$ as shown in Figure~\ref{fig:fulltwist}(d).  The 0 strand goes behind 1 and 2 and the 5 strand passes in front of 3 and 4.  The result is not the same as the final step in Figure~\ref{fig:clasp}, because of the presence of the two $\triangle 012$'s and the two $\triangle 543$'s.  While these triangles themselves are not identified yet, their 02 edges and 53 edges (dark red and green) have come together, and they form a sphere with the two pink triangles in front and the two yellow in back.  The interlocked gray and white faces meet along the dark red and green longitudes.  These faces appear behind the sphere on the left and in front on the right.
\item The $\triangle 012$'s are identified to the $\triangle 543$'s:  Bringing strands 1 and 4 together and identifying each $\triangle 012$ to its corresponding $\triangle 543$ collapses the sphere.  The result, shown in Figure~\ref{fig:fulltwist}(e), is the desired positive full twist on three strands (read right to left, the positive direction for the top of the 3-braid with a counterclockwise orientation).  
\end{itemize}

To obtain the triangles for the 6-punctured sphere at the bottom of the product region, rotate $S_0$ about the horizontal line through the punctures, so now the strands of the braid go up, and use the same identifications.  For example, at the bottom $\triangle 023$ is in the front and is identified to $\triangle 523$ in the back.

Having capped off the ends, we turn our attention to placing ideal tetrahedra in the product region, determining their face pairings, and thus defining triangulations~$\tau_{p}$ on the manifolds $X_{p}$ for all~$p$.  We start by constructing a triangulation of $X_{1}$ upon which the other triangulations will be built.
