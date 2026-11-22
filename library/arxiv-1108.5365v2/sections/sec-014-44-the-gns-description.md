---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-014-44-the-gns-description
section_title: "The GNS description"
section_number: 4.4
pages: 28-31
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.926
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:QPlane:GNS}
The GNS representation enables us to bring the quantum plane into the Hilbert space level, where the algebra is realized as operators on certain Hilbert space. This Hilbert space is nothing but the space of ``$L^2$ functions on the quantum plane", which gives the necessary background later to describe the $L^2$ functions on $GL_q^+(2,\R)$ using the quantum double construction. This will allow us to state the main theorem (Theorem \ref{main}) on the decomposition of $L^2(GL_q^+(2,\R))$ into the fundamental principal series representations of $U_{q\til[q]}(\gl(2,\R))$ with certain Plancherel measure.

Now equipped with the left invariant Haar functional $h$, we can describe completely the GNS representation of $\cA$ using $h$ as the weight.

\begin{Thm} \label{GNSmap}
Let $\cH=L^2(\R\x \R)$ be the completion of $L^2(\R) \ox \cW$ equipped with the inner product
\Eq{\<f,g\> = \int_\R\int_\R \overline{g(s,t+\frac{iQ}{2})}f(s,t+\frac{iQ}{2})dsdt,}
and the $L^2$ norm
\Eq{\|f\|^2 = \iint |f(s,t+\frac{iQ}{2})|^2dsdt.}
Then the GNS map is simply given by
\Eq{\L\left(\int_{\R+i0}\int_\R f(s,t)A^{ib\inv s}B^{ib\inv t}dsdt \right) = f(s,t).}
In particular, the Haar functional is a faithful weight.

The action $\pi$ is given by the multiplication of $\cA$ on itself:
\Eq{\pi(a)\L(b):=\L(ab),\tab a,b\in\cA.}
\end{Thm}

First of all, let us note that $\cA$ is closed under *:
\begin{Prop} The conjugation map $T$ is given by
\Eq{T(f)=\over[f](-s,-t)e^{2\pi ist},}
where we denote by $\over[f](z):=\overline{f(\over[z])}$.

We observe that $\over[f](-s,-t)e^{2\pi ist}$ still satisfies all the analytic properties required to be an element of $\cA$: it is entire analytic in $s$, meromorphic in $t$ with possible poles at $t=-inb-imb\inv$, etc. see Definition \ref{qplanedef}.
\end{Prop}
\begin{proof}
\begin{eqnarray*}
&&\left(\int_{\R+i0}\int_\R f(s,t)A^{ib\inv s}B^{ib\inv t}dsdt \right)^* \\
&=&\int_{\R+i0}\int_\R \over[f(s,t)] B^{-ib\inv \over[t]}A^{-ib\inv \over[s]}d\over[s]d\over[t]\\
&=&\int_{\R-i0}\int_\R \overline{f(\over[s],\over[t])} B^{-ib\inv t}A^{-ib\inv s}dsdt\\
&=&\int_{\R-i0}\int_\R  \overline{f(\over[s],\over[t])}e^{2\pi i s t}A^{-ib\inv s}B^{-ib\inv t}dsdt\\
&=&\int_{\R+i0}\int_\R \overline{f(-\over[s],-\over[t])}e^{2\pi i st}A^{ib\inv s}B^{ib\inv t}dsdt\\
&=&\int_{\R+i0}\int_\R  \over[f](-s,-t)e^{2\pi i st}A^{ib\inv s}B^{ib\inv t}dsdt.
\end{eqnarray*}
\end{proof}

Next we describe the product in terms of $f(s,t)$:
\begin{Prop} \label{producttwisted}The product of two elements in $\cA$ is given by:
\Eq{(f\cdot g)(s,t)=\int_C\int_\R f(s-s',t-t')g(s',t')e^{2\pi is'(t-t')} ds' dt'}
i.e. a twisted convolution. Here $C$ is the contour that, with possible poles, goes below $t'=t$ and above $t'=0$.
\end{Prop}
\begin{proof}
\begin{eqnarray*}
&&\left(\int_{\R+i0}\int_\R f(s,t)A^{ib\inv s}B^{ib\inv t}dsdt\right)\left(\int_{\R+i0}\int_\R g(s',t')A^{ib\inv s'}B^{ib\inv t'}ds'dt'\right)\\
&=&\int_{\R+i0}\int_\R\int_{\R+i0}\int_\R f(s,t)g(s',t')e^{2\pi is't}A^{ib\inv (s+s')}B^{ib\inv (t+t')} ds'dt' dsdt\\
&=&\int_{\R+i0}\int_\R\left(\int_C\int_\R f(s-s',t-t')g(s',t')e^{2\pi is'(t-t')}ds'dt'\right)A^{ib\inv s}B^{ib\inv t} dsdt,\\
\end{eqnarray*}
where in the last step, the shift in $t$ will push the contour of $t'$ to go below $t'=t$.
\end{proof}

\begin{proof}[Proof of Theorem \ref{GNSmap}] Using the formula for the Haar functional, and the definition of the GNS inner product, we have
\begin{eqnarray*}
\<f,g\>&=&h(g^*f) \\
&=&h(\over[g](-s,-t)e^{2\pi ist}\cdot f(s,t))\\
&=&h\left(\int_{\R+i0}\int_\R \over[g](s'-s,t'-t)e^{2\pi i(s-s')(t-t')}f(s',t')e^{2\pi is'(t-t')} ds'dt'\right)\\
&=&h\left(\int_{\R+i0}\int_\R \over[g](s'-s,t'-t)f(s',t')e^{2\pi is(t-t')} ds'dt'\right)\\
&=&\int_{\R+i0}\int_\R \over[g](s',t'-iQ)f(s',t') ds'dt'\\
&=&\int_{\R}\int_\R \over[g](s',t'-\frac{iQ}{2})f(s',t'+\frac{iQ}{2}) ds'dt'\\
&=&\int_{\R}\int_\R \over[g(s',t'+\frac{iQ}{2})]f(s',t'+\frac{iQ}{2}) ds'dt',
\end{eqnarray*}
where in the second to last line, we do a shift in the contour of $t$ by $\frac{iQ}{2}$ by holomorphicity.
\end{proof}

Finally we read off the representation $\pi$ of $\cA$ on the functions $f(s,t)\in\cH$:
\begin{Prop} The representation $\pi: \cA\inj \cB(\cH)$ is given by
\Eq{\pi(A)=e^{-2\pi bp_s},\tab \pi(B)=e^{2\pi bs}e^{-2\pi bp_t},}
where $p_s=\frac{1}{2\pi i}\del[,s]$, so that $e^{2\pi bp_s}\cdot f(s)=f(s-ib)$. Similarly for $p_t$.
\end{Prop}
\begin{proof}
$A$ acts on $f(s,t)$ by:
\begin{eqnarray*}
&&A^{ib\inv s'}\iint f(s,t) A^{ib\inv s}B^{ib\inv t}dsdt\\
&=&\iint f(s,t) A^{ib\inv (s+s')}B^{ib\inv t}dsdt\\
&=&\iint f(s-s',t) A^{ib\inv s}B^{ib\inv t}dsdt.\\
\end{eqnarray*}
Hence $A^{ib\inv s'}\cdot f(s,t) = f(s-s', t)$, or $A= e^{-2\pi bp_s} .$

Similarly, 
\begin{eqnarray*}
&&B^{ib\inv t'}\iint f(s,t) A^{ib\inv s}B^{ib\inv t}dsdt\\
&=&\iint f(s,t) e^{2\pi ist'}A^{ib\inv s}B^{ib\inv (t+t')}dsdt\\
&=&\iint f(s,t-t') e^{2\pi ist'}A^{ib\inv s}B^{ib\inv t}dsdt.\\
\end{eqnarray*}
Hence $B^{ib\inv t'}\cdot f(s,t) = e^{2\pi i st'}f(s,t-t')$, or $B=e^{2\pi bs}e^{-2\pi b p_t}$.
\end{proof}

We will take this Hilbert space $\cH$ as our canonical choice, when we introduce right measure and the dual space.
