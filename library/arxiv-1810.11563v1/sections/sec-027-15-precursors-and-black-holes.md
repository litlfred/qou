---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-027-15-precursors-and-black-holes
section_title: "Precursors and Black Holes"
section_number: 15
pages: 51-54
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.985
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
In defining precursor operators in AdS/CFT it is tempting to identify the single qubit operator $W$ with a local low-dimension CFT field. However, local fields when they act inject infinite energy into the CFT system and this is not what we want. The remedy is to smear the field over a time interval. We would like the energy of the field to be such that it would increase the entropy of the black hole by one thermal unit. This means that the energy should be equal to the temperature. We therefore assume that $W_L$ is an operator that adds a thermal quantum to the left-side black hole. 

Now let us apply the precursor $ U^{\dag}(t_w) W_L \ U(t_w)$ to the thermofield-double state: 
\bea
|\Psi(t_w)\ra &\equiv&   U^{\dag}(t_w) W_L \ U(t_w) |TFD\ra \cr \cr
\eq W_L(t_w)|TFD\ra
\eea
The operator $W_L(t_L)$ is a Schrodinger picture operator  that acts at $t =0,$ but its effect is exactly the same as adding a thermal quantum to the left side at time  $t_w.$ We will be especially interested in the case of large negative $t_w.$ This shown in figure \ref{shock-wave}.

When $|t_w|>> t_*$ the infalling quantum created by $W_L$ undergoes a large blue shift as it falls to the horizon. The result is that for most of its world line it is an extremely energetic shock wave. This is despite the fact that the thermal quantum makes an extremely small change in the energy of the black hole. 

 
\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{shock-wave.pdf}
\caption{}
\label{shock-wave}
\end{center}
\end{figure}


The shock wave has a large effect on the geometry but an easy way to understand it is through the Dray-'t Hooft effect ( T.~Dray and G.~'t Hooft,
  
  Nucl.\ Phys.\ B {\bf 253}, 173 (1985)) Instead of redrawing the Penrose diagram to reflect the gravitational back reaction on the shape of the diagram we can use the rule that any trajectory  crossing the shock wave gets displaced and jumps as shown in figure \ref{shock-wave-maxslice2} where we see the maximal slice anchored on both sides at $t=0$. The jump is from the point $a$ to the point $b$.

Without the shock wave the maximal slice at $t=0$ has no volume behind the horizon; it passes right through the bifurcate horizon. But as one can see from figure \ref{shock-wave-maxslice2} the shock wave causes the maximal slice to gain a significant volume as indicated by the dark blue surfaces.


\begin{figure}[H]
\begin{center}
\includegraphics[scale=.3]{shoc-wave-maxslice2.pdf}
\caption{}
\label{shock-wave-maxslice2}
\end{center}
\end{figure}


In order to study the effects of such a shock wave I will give a general ``master formula" for the volume of the maximal slice as a function of the anchoring times $t_L, \ t_R$ and $t_w.$ The formula was derived by Shenker and Stanford 
\url{https://arxiv.org/pdf/1306.0622.pdf}
in another context but it was shown in Stanford-Susskind 
\url{https://arxiv.org/pdf/1406.2678.pdf}
 that it is a good approximation to the volume of maximal slices\footnote{It is a good approximation as long as the times are not exponentially large, at which the classical geometric description is expected to break down.}. It is a purely classical consequence  of general relativity,



\bn

\be 
\frac{V}{G\l} = S \ \log{\{
\cosh{\frac{\tau_L + \tau_R}{2}} 
+e^{(|\tau_w|-\tau_*) +\frac{1}{2}(\tau_L -\tau_R)}
\}}
\label{master-formula}
\ee

\bn
where $\tau$ is the dimensionless Rindler time, $\tau = 2\pi t/{\beta,}$ and $S$ is the entropy.

Let us consider the complexity $V/Gl_{ads}$ at $t_L = t_R =0.$ The answer should be the complexity of the precursor itself since the complexity of the TFD is zero. Using $S\approx K$ we find,
\be 
\CC(0,0) = K \log\left(1 + e^{(|\tau_w|-\tau_*)} \ \right),
\ee
in agreement with \ref{compcircuit}. 
This is a truly remarkable result that relates classical solutions of general relativity to properties of quantum circuit complexity.


The relation between complexity and volume is very general. It applies to any number of shock waves sent in at any times. It also applies to localized non-spherical shock waves,  D. Roberts, D. Stanford and L. Susskind,
\url{https://arxiv.org/pdf/1409.8180.pdf} .
