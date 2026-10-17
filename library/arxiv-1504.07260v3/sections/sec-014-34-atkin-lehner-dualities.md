---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-014-34-atkin-lehner-dualities
section_title: "Atkin-Lehner dualities"
section_number: 3.4
pages: 22-25
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.918
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
[]{#s:AtkinLehner label="s:AtkinLehner"}

The Fricke S-duality $S\to -1/NS$ can be generalized to dualities acting on the heterotic axio-dilaton by Atkin-Lehner involutions. Let $e$ be an exact divisor of $N$ (denoted by $e\| N$), i.e $e| N$ and $\gcd(e,N/e)=1$. An Atkin-Lehner involution is an element of $SL(2,\mathbb{R})$ of the form[^1] $$\label{ALdef} W_e=\frac{1}{\sqrt{e}}\begin{pmatrix}
ae & b\\ Nc & de
\end{pmatrix}\qquad \qquad a,b,c,d,e,N\in \mathbb{Z}, \quad ade^2-Nbc=e,\quad e\|N\ .$$Atkin-Lehner involutions are elements of the normalizer of $\Gamma_0(N)$ within $SL(2,\mathbb{R})$ and they have order $2$ modulo $\Gamma_0(N)$, i.e. $W_e^2\in \Gamma_0(N)$. For $e=N$, one recovers the Fricke involution $W_N=\frac{1}{\sqrt{N}}\left(\begin{smallmatrix}
0 & -1\\ N & 0
\end{smallmatrix}\right)$. Let us focus on a CHL model in the type IIA frame (similar arguments extend to the heterotic frame). One can easily verify that, at least in the perturbative limit, the model is invariant under the transformation $$\label{ALmoduli} T_{\text{IIA}}\to T'_{\text{IIA}}=\frac{ae T_{\text{IIA}}+b}{NcT_{\text{IIA}}+de}\qquad U_{\text{IIA}}\to U'_{\text{IIA}}=\frac{ae U_{\text{IIA}}+b}{NcU_{\text{IIA}}+de}\qquad S_{\text{IIA}}\to S'_{\text{IIA}}=S_{\text{IIA}}$$ and $$\label{ALtransf} \begin{pmatrix}
\tilde n & n/N\\ -k & \tilde k
\end{pmatrix}\to \begin{pmatrix}
\tilde n' & n'/N\\ -k' & \tilde k'
\end{pmatrix}=\frac{1}{e} \begin{pmatrix}
de & -c\\ -bN & ae
\end{pmatrix}\begin{pmatrix}
\tilde n & n/N\\ -k & \tilde k
\end{pmatrix}\begin{pmatrix}
de & -b\\ -Nc & ae
\end{pmatrix}\ ,$$where $n,k\in \mathbb{Z}$ (respectively, $\tilde n,\tilde k\in \mathbb{Z}$) are the units of winding and momentum along $S^1$ (resp., $\tilde S^1$). In particular, [\[ALtransf\]](#ALtransf){reference-type="eqref" reference="ALtransf"} is an automorphism of the lattice of winding-momenta and, for each charge in such a lattice, the corresponding left- and right-moving conformal weights $\frac{1}{2}(p_L^2+\tilde p_L^2)$ and $\frac{1}{2}(p_R^2+\tilde p_R^2)$ are invariant under [\[ALmoduli\]](#ALmoduli){reference-type="eqref" reference="ALmoduli"} and [\[ALtransf\]](#ALtransf){reference-type="eqref" reference="ALtransf"}. We will refer to this kind of transformations as a type IIA Atkin-Lehner T-duality.

Let us consider the limit $T'_{\text{IIA}}\to \infty$, where the dual theory decompactifies to a six dimensional model. In this limit, the only states with finite mass are the ones with zero winding $n',\tilde n'$ around the dual torus $S'^1\times \tilde S'^1$. This condition is equivalent to $$\label{zerowind}


\begin{cases} \tilde n'= c^2 \frac{N}{e}\tilde k+c d k-c d n+d^2 e \tilde n=0\\
 n'= -a c N \tilde k+a d e n-b c \frac{ N}{e}k-b d N \tilde n=0
\end{cases}\Leftrightarrow\quad
\begin{cases}ck=-de\tilde n\\ dn=c\frac{N}{e}\tilde k
\end{cases}\ .$$By the condition $ade^2-Nbc=e$ in the definition [\[ALdef\]](#ALdef){reference-type="eqref" reference="ALdef"} it follows that $\gcd(c,e)=1$ and $\gcd(d,N/e)=1$, so that [\[zerowind\]](#zerowind){reference-type="eqref" reference="zerowind"} implies $$k\in e\mathbb{Z}\qquad\qquad n\in \frac{N}{e}\mathbb{Z}\ .$$ Therefore, in the $T'_{\text{IIA}}\to \infty$ limit, the theory contain only states in the $(g^{N/e})^r$-twisted sectors, $r=1,\ldots, e$ and that are invariant under $g^{N/e}$. Thus, the model is a compactification of type IIA on the orbifold CFT $$\mathcal{C}'=\mathcal{C}/\langle g^{N/e}\rangle\ .$$For large but finite $T'$, as a local observer moves around the circle $S'$ by $1/N$-th of a period, a state with $k'$ units of momentum picks a phase $$e^{\frac{2\pi i k'}{N}}=e^{\frac{2\pi i}{N}(a c N \tilde k+a d e k-\frac{N}{e}bc n+b d N \tilde n)}=e^{\frac{2\pi i}{N}(ade k-\frac{N}{e}bc n)}\ .$$This phase corresponds to the action of $g':=g^{ade}\mathcal{Q}^{-\frac{N}{e}bc}$ on the states of $\mathcal{C}'=\mathcal{C}/\langle g^{N/e}\rangle$, where $\mathcal{Q}$ is the quantum symmetry acting by a phase on the twisted sectors of the orbifold CFT $\mathcal{C}'$ and $g$ (with slight abuse of notation) is the symmetry of $\mathcal{C}'$ induced by the symmetry $g$ of $\mathcal{C}$. Notice that $\mathcal{Q}$ has order $e$ and $g$ has order $N/e$ in $\mathcal{C}'$, so that, by the condition $ade-\frac{N}{e}bc=1$, we obtain $$g^{ade}=g^{1+\frac{N}{e}bc}=g\qquad\qquad \mathcal{Q}^{-\frac{N}{e}bc}=\mathcal{Q}^{1-ade}=\mathcal{Q}\ .$$Furthermore, since $\gcd(e,N/e)=1$, it follows that $g'=g\mathcal{Q}$ has order $N$. We conclude that the T-dual theory is type IIA compactified on the orbifold $$\frac{\mathcal{C}'\times S'}{\langle (\delta',g')\rangle}\times \tilde S'\qquad \text{with } \mathcal{C}'=\mathcal{C}/\langle g^{N/e}\rangle,\ g'=g\mathcal{Q}\ ,$$and $\delta'$ is a shift of order $N$ along $S'$. For $e=N$, i.e. the Fricke involution, the induced $g$ has order $1$ in $\mathcal{C}'=\mathcal{C}/\langle g\rangle$, so that $g'=\mathcal{Q}$ is simply the quantum symmetry.

A cumbersome calculation along the lines of [\[a:quantsymm\]](#a:quantsymm){reference-type="ref" reference="a:quantsymm"} shows that if $g$ has Frame shape $\prod_{a|N}a^{m(a)}$, then $g'$ has Frame shape $$\prod_{a|N} a^{m(\frac{ea}{\gcd(a,e)^2})}\ .$$This formula reduces to $\prod_{a|N} a^{m(\frac{N}{a})}$ for the Fricke involution $W_N$. A case by case analysis shows that whenever $g$ has a balanced Frame shape (case 1), then $\mathcal{C}'$ is a K3 model and $g'$ has the same Frame shape as $g$. Therefore, the CHL model in case 1 are self-dual under *all* Atkin-Lehner involutions. On the contrary, the Atkin-Lehner involutions relate the CHL models in case $3$ to the ones in case 2, according to the following duality diagrams: $$\begin{tikzcd}
K3(1^{-4} 2^5 3^4 6^1) \color{red}{\arrow[leftrightarrow,color=blue]{r}{W_6}}\arrow[leftrightarrow,color=blue]{d}{W_2}\arrow[leftrightarrow,color=blue]{dr}[description]{W_3} & 
T^4(1^1 2^4 3^5 6^{-4})\\[20pt] 
K3(1^5 2^{-4} 3^1 6^4)\arrow[leftrightarrow,color=blue]{r}{W_6}\arrow[leftrightarrow,crossing over,color=blue]{ru}[description]{W_3} & K3(1^4 2^1 3^{-4} 6^5) \arrow[leftrightarrow,color=blue]{u}{W_2}
\end{tikzcd}


\qquad \qquad\begin{tikzcd}
K3(1^{-2} 2^3 5^2 10^1) \arrow[leftrightarrow,color=blue]{r}{W_{10}}\arrow[leftrightarrow,color=blue]{d}{W_2}\arrow[leftrightarrow,color=blue]{dr}[description]{W_5} & 

T^4(1^1 2^2 5^3 10^{-2})\\[20pt] 
K3(1^3 2^{-2} 5^1 10^2)\arrow[leftrightarrow,color=blue]{r}{W_{10}}\arrow[leftrightarrow,crossing over,color=blue]{ru}[description]{W_5} & K3(1^2 2^1 5^{-2} 10^3) \arrow[leftrightarrow,color=blue]{u}{W_2}
\end{tikzcd}$$ $$\begin{tikzcd}
K3(1^{-2} 2^2 3^2 4^1 12^1) \arrow[leftrightarrow,color=blue]{r}{W_{12}}\arrow[leftrightarrow,color=blue]{d}{W_4}\arrow[leftrightarrow,color=blue]{dr}[description]{W_3} & 

T^4(1^1  3^1 4^2 6^2 12^{-2})\\[20pt] 
K3(1^1 2^2 3^1 4^{-2} 12^2)\arrow[leftrightarrow,color=blue]{r}{W_{12}}\arrow[leftrightarrow,crossing over,color=blue]{ru}[description]{W_3} & K3(1^2 3^{-2} 4^1 6^2 12^1) \arrow[leftrightarrow,color=blue]{u}{W_4}
\end{tikzcd}$$ $$\begin{tikzcd}
K3(1^{-2} 2^4 3^{-2} 6^4) \arrow[leftrightarrow,color=blue]{r}{W_2,W_{6}}\arrow[leftrightarrow,loop left,color=blue]{}{W_3} & 

T^4(1^4 2^{-2} 3^4 6^{-2})\arrow[leftrightarrow,loop right,color=blue]{}{W_3}
\end{tikzcd}$$ $$\begin{tikzcd}
K3(1^{-1} 2^{-1} 3^3 6^3) \arrow[leftrightarrow,color=blue]{r}{W_3,W_{6}}\arrow[leftrightarrow,loop left,color=blue]{}{W_2} & 

T^4(1^3 2^3 3^{-1} 6^{-1})\arrow[leftrightarrow,loop right,color=blue]{}{W_2}
\end{tikzcd}$$ In these diagrams, the notation $X(\prod_{a|N} a^{m(a)})$, with $X\in \{K3,T^4\}$, denotes a type IIA model on $\frac{X\times T^2}{\mathbb{Z}_N}$, where $\mathbb{Z}_n$ is generated by $(\delta,g)$ and $g$ has Frame shape $\prod_{a|N} a^{m(a)}$.

Under string-string duality, these Atkin-Lehner involutions are mapped to S-duality transformations in the heterotic frame $$S_{\text{het}}\to S'_{\text{het}}=\frac{ae S_{\text{het}}+b}{NcS_{\text{het}}+de}\qquad U_{\text{het}}\to U'_{\text{het}}=\frac{ae U_{\text{het}}+b}{NcU_{\text{het}}+de}\qquad T_{\text{het}}\to T_{\text{het}}'=T_{\text{het}}\ .$$Each node in the diagrams above admits a heterotic dual (or, more generally, a $(4,0)$ dual) and these heterotic (or $(4,0)$) models are related to one each other by a network of Atkin-Lehner S-dualities.

The Atkin-Lehner S-duality $W_e$ acts on the electric-magnetic charges by $$\begin{pmatrix}
Q \\ P
\end{pmatrix}\to  \begin{pmatrix}
Q' \\ P'
\end{pmatrix}=\frac{1}{\sqrt{e}}\begin{pmatrix}
de & -b\\ -Nc & ae
\end{pmatrix} \begin{pmatrix}
Q \\ P
\end{pmatrix}\ .$$As a consequence, the electric and magnetic lattices $\Lambda_e,\Lambda_m$ and $\Lambda_e',\Lambda_m'$ of two CHL models related by $W_e$ must be related as follows $$\Lambda_e'\cong {\rm span}_\mathbb{Z}\Bigl(\sqrt{e}\Lambda_e\cup \frac{1}{\sqrt{e}}\Lambda_m\Bigr)\subset \Lambda_m\otimes \mathbb{R}$$and $$\Lambda_m'\cong {\rm span}_\mathbb{Z}\Bigl(\frac{N}{\sqrt{e}}\Lambda_e\cup \sqrt{e}\Lambda_m\Bigr)\subset \Lambda_m\otimes \mathbb{R}\ .$$ We have verified these relations in several examples.

Finally, we note that an analogous Atkin-Lehner involution is expected to act as T-duality in the heterotic frame or, equivalently, as S-duality in the type IIA frame.

[^1]: The normalization factor $\frac{1}{\sqrt{e}}$ is sometimes omitted in the definition, since it is irrelevant in the action of $W_e$ as a fractional linear transformation on the upper half plane.
