---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-011-33-action-of-a-rotating-btz-black-hole
section_title: "Action of a rotating BTZ black hole"
section_number: 3.3
pages: 21-22
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.956
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
\label{subsec-rotating}

A rotating black hole in $(2+1)$-dimensional AdS space has metric
\begin{equation}
ds^2=-f(r)dt^2+\frac{1}{f(r)}dr^2+r^2\left(d\phi-\frac{8GJ}{2r^2}dt\right)^2
\end{equation}
\begin{align}
f(r)=\frac{r^2}{\lads^2}-8G M+\frac{(8G J)^2}{4r^2} =\frac{(r^2-r_+^2)(r^2-r_-^2)}{r^2 \lads^2}.
\end{align}
The inner horizon ($r_-$) and outer horizon ($r_+$) are at
\begin{align}
&8G M=\frac{r_+^2+r_-^2}{\lads^2},\ \ \frac{8G J}{\lads}=\frac{2r_+r_-}{\lads^2}. \label{eq:BTZformulaforMJ}
\end{align}
The angular momentum is bounded above
\begin{equation}
M\geq\frac{J}{\lads}.
\end{equation}
This bound is saturated at extremality. The Penrose diagram for the rotating case is similar to that for the charged case in Fig.~\ref{fig-incrementalcharged}, and at late time, the EH contribution to the action of the Wheeler-DeWitt patch is
\begin{align}
\frac{d \CA_{\textrm{EH}}}{dt_L} 
 =-\frac{(r_+^2-r_-^2)}{4G \lads^2}.
\end{align}
The YGH surface contribution to the action can also be calculated, and as before it is $-2$ times the EH part, so the total rate of change of the action is
\begin{align}
\boxed{\frac{d\CA\textrm{ction}}{dt}=\frac{r_+^2-r_-^2}{4G \lads^2}=2\sqrt{M^2-\frac{J^2}{\lads^2}}.}
\label{rothole-action}
\end{align}
{Extremal rotating BTZ black holes ($J \rightarrow \lads M$) are all torque and no action.}
