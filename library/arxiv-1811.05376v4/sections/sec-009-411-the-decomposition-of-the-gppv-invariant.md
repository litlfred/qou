---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-009-411-the-decomposition-of-the-gppv-invariant
section_title: "The decomposition of the GPPV invariant"
section_number: 4.1.1
pages: 27-31
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.988
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
Recall that $q=\exp(2 \pi i \tau)$ with $\tau \in \mathfrak{h}$ where $\mathfrak{h}$ denotes the upper half plane, and recall the definitions of $F \in \mathcal{M}(\mathbb{C})$ and $g \in \mathbb{C}[x]$ given in [\[def:F\]](#def:F){reference-type="eqref" reference="def:F"}. Let $\tilde\Gamma_+ = e^{\frac{\pi i}{4}}$.

::: lemma
[]{#Lemmaet label="Lemmaet"} Introduce the holomorphic functions $\mathcal{L},R \in \mathcal{O}(\mathfrak{h})$ given by $$\begin{aligned}
    \mathcal{L}(\tau) &= \frac{2\lambda}{\sqrt{\tau}} \int_{\varGamma_+} e^{-x /\tau} \mathcal{B}(\mathop{\mathrm{Z}}_0)(x) \ \mathop{\mathrm{{d}\hskip-.6mm}}x,
    \\  R(\tau) &= -\frac{2 \lambda} {\sqrt{\tau} } \sum_{m=0 }^{\infty}  \mathop{\mathrm{Res}}\left( \exp\left( \frac{g(\xi)}{\tau}\right) F(\xi) ,\xi= 2 \pi i m\right).
    
\end{aligned}$$ Then we have that $$\label{eq:sumoftwoparts}
    q^{\Delta}\hat{\mathop{\mathrm{Z}}}_0(q)= \mathcal{L}(\tau)+R(\tau).$$ For $\tau$ in the first quadrant $\mathfrak{h}_+ = \{z\in \mathfrak{h} \mid \Re(z) >0\}$ we have that $$\label{eq:DEDEFORMATION}
        \mathcal{L}(\tau) = \frac{2\lambda}{\sqrt{\tau}} \int_{0}^{\infty} e^{-x /\tau} \mathcal{B}(\mathop{\mathrm{Z}}_0)(x) \ \mathop{\mathrm{{d}\hskip-.6mm}}x.$$
:::

::: proof
*Proof of Lemma [\[Lemmaet\]](#Lemmaet){reference-type="ref" reference="Lemmaet"}.* Recall the contour formula from Theorem [\[thm:zedhat\]](#thm:zedhat){reference-type="ref" reference="thm:zedhat"}

$$q^{\Delta} \hat{\mathop{\mathrm{Z}}}_0(q) =\mathop{\mathrm{I}}(\tau) = \frac{\lambda}{\sqrt{\tau}} \int_{\varGamma} \exp(-x /\tau) \mathcal{B}(\mathop{\mathrm{Z}}_0)(x) \ \mathop{\mathrm{{d}\hskip-.6mm}}x.$$ Under the coordinate change $$x=y^2$$ the contour $\varGamma$ corresponds to the contour $$\varPsi= e^{i\pi \frac38}\mathbb{R}_{+}+e^{i\pi \frac18}\mathbb{R}_+$$ Therefore we have that $$q^{\Delta} \hat{\mathop{\mathrm{Z}}}_0(q)= \frac{\lambda}{\sqrt{\tau}} \int_{\varPsi} \exp(-y^2 /\tau) \mathcal{B}(\mathop{\mathrm{Z}}_0)(y^2)2y \ \mathop{\mathrm{{d}\hskip-.6mm}}y.$$ Introduce the meromorphic function $B \in \mathcal{M}(\mathbb{C})$ given for all $y \in \mathbb{C}$ by $$\label{eq:defB} B(y)=2y\mathcal{B}(\mathop{\mathrm{Z}}_0)(y^2).$$ By Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"} we have that $$\label{eq:B}
B(y)= \frac{2\kappa}{\pi i} G\left( \exp\left(\frac{\kappa y}{P}\right)\right)=\frac{2\kappa}{\pi i} F\left(\frac{\kappa y}{2}\right).$$ From [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} we see that $B$ is periodic with period $\kappa$, i.e. for all $m\in \mathbb{Z}$ we have that $$\label{eq:periodicity}
B(y+\kappa m)=B(y).$$

Let $\mathcal{P}$ be the set of poles of $B$. It follows from Theorem [\[2.1\]](#2.1){reference-type="ref" reference="2.1"} that $\mathcal{P}$ is a subset of the axis $e^{\pi i/4}\mathbb{R}$ and that $$\{ -\omega^2  \mid  \omega \in \mathcal{P}  \}  = 2\pi i\mathop{\mathrm{CS}}_{\mathbb{C}}(X) + 2\pi i\mathbb{Z}.$$ Write $$\varPsi_\pm= e^{i \pi (\frac14 \mp \frac18)}\mathbb{R}_+.$$ We will now apply Cauchy's residue theorem to move $\varPsi_-$ across $e^{i \pi /4}\mathbb{R}_+$ to $\varPsi_+$ in order to obtain the formula [\[eq:sumoftwoparts\]](#eq:sumoftwoparts){reference-type="eqref" reference="eq:sumoftwoparts"}. Deform $\varPsi_\pm$ on the complement of a neighbourhood around the origin to two curves $L_\pm$, which are parallel to $e^{i \pi /4}\mathbb{R}_+$ outside this neighbourhood of the origin, as indicated in Figure [1](#fig:ContourL){reference-type="ref" reference="fig:ContourL"}. Set $$L=L_+ \cup L_-.$$ We first show that $$\label{eq:shiftofContour} \int_{\varPsi} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y= \int_{L} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y,$$ and then we show that the right hand side of [\[eq:shiftofContour\]](#eq:shiftofContour){reference-type="eqref" reference="eq:shiftofContour"} can be rewritten as a sum of residues. Let $R>0$ be a positive constant, and let $R_\pm$ be the arc segment of the circle of radius $R$, which connects $\varPsi_\pm$ and $L_\pm$. Because $L_\pm$ is parallel to $\kappa \mathbb{R}_+$ outside a neighbourhood of the origin, there exists a real positive constant $b_0 >0$ such that every $y \in R_\pm$ is of the form $$y= \kappa a \pm b, (a,b) \in \mathbb{R}_+ \times [b_0,+\infty)$$ and therefore exists a positive real constant $A>0$ independent of $R$, which gives an upper bound $$\left\lvert \frac{1}{1-e^{-\kappa y}}\right\rvert <\frac{1}{1-\exp\left(-\Re(\kappa) b_0\right)}:=A>0$$ for all $y \in R_+$. It follows that we obtain a uniform estimate $$\begin{aligned}
 \label{eq:Estimation1} \begin{split} B(y) &= 2^{n-2}\frac{2\kappa}{\pi i}\frac{\prod_{j=1}^n \sinh(\frac{\kappa y}{2p_j})}{\left( e^{\kappa y/2}(1-e^{-y\kappa }) \right)^{n-2}}
\\&=  O \left( e^{-y\kappa /2}\prod_{j=1}^n \sinh\left(\frac{\kappa y}{2p_j}\right) \right)= O(e^{A_1R}). \end{split}  
\end{aligned}$$ for all $y \in R_+$ for a real constant $A_1$. For fixed $\tau$, there exists a positive real constant $A_2>0$ giving a uniform bound on $R_+$ $$\label{eq:Estimation2}
e^{-y^2/\tau}=O(e^{-A_2R^2}).$$ By combining the estimates [\[eq:Estimation1\]](#eq:Estimation1){reference-type="eqref" reference="eq:Estimation1"} and [\[eq:Estimation2\]](#eq:Estimation2){reference-type="eqref" reference="eq:Estimation2"}, and using that the arc length of $R_\pm$ is proportional to $R$, we obtain the estimate $$\int_{R_+} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y= O(Re^{-A_2R^2+A_1R}).$$ By similar reasoning, there exists constants $B_2>0,B_1 \in \mathbb{R}$ giving the estimate $$\int_{R_-} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y= O(Re^{-B_2R^2+B_1R}).$$ Thus we obtain that $$\label{eq:LimitZero}
\lim_{R \rightarrow \infty} \sum_{\epsilon \in \{\pm1\}} \int_{R_\epsilon} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y=0,$$ which gives the desired identity [\[eq:shiftofContour\]](#eq:shiftofContour){reference-type="eqref" reference="eq:shiftofContour"} .

We now turn to the computation of $\int_{L}  \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y$. For each $m\in \mathbb{N}$, let $L_m$ be a small line segment with $$L_m \cap e^{i\pi/4}\mathbb{R}_+=\{m \kappa\},$$ and which meets $e^{i\pi/4}\mathbb{R}_+$ in a right angle. We can arrange that $L_m$ is of fixed lenght and that $L_m$ meet $L_\pm$ in a point. Thus we have $$\label{eq:periodicity2} L_m=L_0+m\kappa$$ Let $L^m_\pm$ be the bounded component of $L_\pm \setminus L_m,$ and let $\mathcal{P}_m \subset \mathcal{P}$ be the set of poles of $B$ that lie within the bounded component of the complement of the contour $$\varPsi_m = L^m_+ \cup L_m  \cup L^m_-.$$ See Figure [1](#fig:ContourL){reference-type="ref" reference="fig:ContourL"}.

![The contours $L_\pm, L^m_\pm$ and $\varPsi_\pm$ and the subset of poles $\mathcal{P}_m$ drawn rotated, such that $\kappa \mathbb{R}_+$ points straight up.](ContourL){#fig:ContourL}

Equip $\varPsi_m$ with the counter clockwise orientation. An application of Cauchy's residue theorem now gives $$\begin{gathered}
 \label{eq:dabel} \begin{split}
2\pi i\sum_{\omega \in \mathcal{P}_m} \mathop{\mathrm{Res}}(e^{-y^2/\tau}B(y), y=\omega)  =  \int_{\varPsi_m} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y
\\ =\int_{L_m} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y +\sum_{\epsilon \in \{\pm1\}} \epsilon  \int_{L^m_\epsilon} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y. \end{split} 
\end{gathered}$$ Because $B$ is $\kappa$ periodic as stated in [\[eq:periodicity\]](#eq:periodicity){reference-type="eqref" reference="eq:periodicity"} and $L_{m}=L_0+ m\kappa$, we see that that there exists $C>0$ giving a uniform bound $$C> \sup \{ \lvert B(y) \rvert \ \mid \ y \in \cup_{m\in \mathbb{N}} L_m \}.$$ Because of this universal bound, it is easy too see that $$\lim_{m \rightarrow \infty} \int_{L_m} \exp(-y^2/\tau) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y=0.$$ It follows that the right hand side of [\[eq:dabel\]](#eq:dabel){reference-type="eqref" reference="eq:dabel"} converges to $$\sum_{\epsilon \in \{\pm1\}} \int_{L_\epsilon} \exp(-y^2/ \tau) B(y)  \ \mathop{\mathrm{{d}\hskip-.6mm}}y=\sum_{\epsilon \in \{\pm1\}} \epsilon  \int_{\varPsi_\epsilon} \exp(-y^2/ \tau) B(y)  \ \mathop{\mathrm{{d}\hskip-.6mm}}y.$$ This also implies that the sum of residues is convergent.

Let us now recall a simple transformation law for residues. Let $z_0\in \mathbb{C}$ and let $f\in \mathcal{M}_{z_0}(\mathbb{C})$ be the germ of a meromorphic function with a pole at $z_0.$ Assume $w_0 \in \mathbb{C}$ and that $z \in \mathcal{O}_{w_0}(\mathbb{C})$ satisfies $z(w_0)=z_0, \dot{z}(w_0)\not=0.$ If either $z_0$ is a simple pole, or $z(w)$ is linear in $w,$ then we have that $$\label{ResiduePropositionFormula}
\text{Res}(f(z(w)), w=w_0)= \frac{\text{Res}(f(z),z=z(w_0))}{\dot{z}(w_0)}.$$ Introduce the variable $$\label{eq:xi}
\xi= \frac{\kappa y}{2}.$$ By using the relation [\[eq:B\]](#eq:B){reference-type="eqref" reference="eq:B"} between $B$ and $F$, the relation [\[eq:defB\]](#eq:defB){reference-type="eqref" reference="eq:defB"} between $B$ and $\mathcal{B}(\mathop{\mathrm{Z}}_0)$ and the tranformation law [\[ResiduePropositionFormula\]](#ResiduePropositionFormula){reference-type="eqref" reference="ResiduePropositionFormula"} we obtain $$\begin{aligned}
 \begin{split} 
q^{\Delta} \hat{\mathop{\mathrm{Z}}}_0(q)& = \frac{\lambda}{\tau} \int_{\varPsi} \exp\left(-\frac{y^2}{\tau}\right) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y
\\&=\frac{2\lambda}{\tau} \left( \int_{\varPsi_+} \exp\left(-\frac{y^2}{\tau}\right) B(y) \ \mathop{\mathrm{{d}\hskip-.6mm}}y -  2\pi i\sum_{\omega \in \mathcal{P}} \mathop{\mathrm{Res}}(e^{-y^2/\tau}B(y), y=\omega)  \right)
\\ &= \frac{2\lambda}{\tau} \left( \int_{\Gamma_+} \exp\left(-\frac{x}{\tau}\right) \mathcal{B}(\mathop{\mathrm{Z}}_0)(x) \ \mathop{\mathrm{{d}\hskip-.6mm}}x -  \sum_{m=1}^{\infty} \mathop{\mathrm{Res}}(e^{-g(\xi)/\tau}F(\xi), \xi=2\pi i m) \right)
\\ &= \mathcal{L}(\tau)+R(\tau). \end{split}
\end{aligned}$$ Finally, we prove [\[eq:DEDEFORMATION\]](#eq:DEDEFORMATION){reference-type="eqref" reference="eq:DEDEFORMATION"} for $\tau \in \mathfrak{h}_+$. First observe that for $x$ and $\tau$ in the upper right half plane we have $$\label{Positve}
\Re(x/\tau) >0.$$ Push the contour $\tilde{\Gamma}_+$ to $\mathbb{R}_+$. If the integral is invariant under this deformation of the contour, we obtain the desired identity. To see that the integral is invariant under this deformation of the contour, we apply a limiting argument, together with Cauchy's residue formula. To that end, let $R>0$ be a positive parameter, and let $C_R$ be the arc segment of the circle of radius $R$, which connects $R$ to $Re^{i\pi \frac{3}{4}}$ and stays in the upper half plane. As we are not moving the contour across any singularities of $\mathcal{B}(\mathop{\mathrm{Z}}_0),$ the only difficulty is to show that $$\label{eq:LIIMITzero}
\lim_{R\rightarrow +\infty} \int_{ C_R} e^{-x / \tau} \mathcal{B}(\mathop{\mathrm{Z}}_0)(x) \ \mathop{\mathrm{{d}\hskip-.6mm}}x=0.$$ As $C_R$ remain at least a fixed distance away from the axis of poles of $\mathcal{B}(\mathop{\mathrm{Z}}_0)(x)$, the limit [\[eq:LIIMITzero\]](#eq:LIIMITzero){reference-type="eqref" reference="eq:LIIMITzero"} follows by [\[Positve\]](#Positve){reference-type="eqref" reference="Positve"} together with arguments similar to the arguments giving the limit [\[eq:LimitZero\]](#eq:LimitZero){reference-type="eqref" reference="eq:LimitZero"} above. ◻
:::
