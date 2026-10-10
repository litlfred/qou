---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-023-15-precursors-and-black-holes
section_title: "Precursors and Black Holes"
section_number: 15
pages: 51-54
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
text_source: latex
latex_prose_ratio: 0.657
latex_coverage_ratio: 0.975
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



\subsection{Instability of White Holes}

Earlier I talked about the meaning of the bounce in figure \ref{Foliated-BTZ2} . It resembles the entropy bounce of a confined gas if one constrains the gas to be in a very low entropy state at $t=0$. Let me give names to the various regions of the Penrose diagram. The left and right shaded regions are the left and right black hole exteriors. The upper un-shaded region is the black hole interior in which the complexity evolves in a manner consistent with the second law of complexity (complexity increases). The lower un-shaded region is the counter-intuitive region where complexity decreases. In general relativity it is the \it white hole \rm interior.

In the case of the confined gas, events in which the entropy decreases are never seen in the real world. Even if it were possible to set up the fine-tuned initial condition in the remote past, the bizarre behavior is extremely unstable. A tiny perturbation (the proverbial butterfly), by the time it spreads through the system will turn the evolution around so that the entropy will increase after a short time. 

The second law of complexity is patterned on the second law of thermodynamics and we should expect that the condition of decreasing complexity is unstable in the same way. Let us consider what happens if on the left side we perturb the white hole by adding a single thermal quantum at past time $t_w$. Using the master formula \ref{master-formula},  we vary $\tau_L$ while holding $\tau_R$ fixed.
In the white hole region where $(\tau_L+\tau_R)<<0$ we get, 
\be 
V \sim \log\left[ \frac{1}{2}e^{-\tau_L/2}  +e^{|\tau_w|-\tau_*+\tau_L/2}      \right] + const
\label{WH}
\ee
When $\tau_L$ is very negative the first term in the bracket dominates and $V$ decreases just as it would if no perturbation had been applied. The second term due to the perturbation increases with $\tau_L $. The crossover occurs at 

\be 
 \tau_L(crossover) = - \left(|\tau_w| -\tau_* \right)
\ee
Evidently the perturbation at $t_w$ initiates a process that results in a  reversal of the complexity-decrease after a scrambling time.  For large negative $\tau_L$ this is still deep in the original white hole region.
This shows that the decreasing complexity of the white hole behaves  exactly like the classical entropy of a fine-tuned entropy bounce, being unstable to tiny perturbations.


However I want to emphasize again that it is not an entropic  phenomenon in the usual sense. It is a complexity phenomenon. 


\bn
\bf 
NOTE: THE LIVE VERSION OF LECTURE II ENDS HERE. IT CONTINUES IN LECTURE III.
\rm
