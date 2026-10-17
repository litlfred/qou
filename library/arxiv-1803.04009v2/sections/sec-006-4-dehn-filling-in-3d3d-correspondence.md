---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-006-4-dehn-filling-in-3d3d-correspondence
section_title: "Dehn filling in 3d/3d correspondence"
section_number: 4
pages: 38-41
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.995
---
[]{#sec : Dehn-filling label="sec : Dehn-filling"}

In this section, we generalize the DGG's construction to obtain $T^{6d}_{\rm irred}[M]$ for closed 3-manifolds $M$ by incorporating Dehn filling operation. Refer to [@Pei:2015jsa; @Gadde:2013sca; @Gukov:2017kmk; @Alday:2017yxk] for previous discussions on Dehn filling operation in the context of 3d/3d correspondence and the construction of 3d theory, which we will denote $T^{6d}_{(\rm  irred)^c}[M]$, labelled by Seifert manifolds $M$.[^1]

## Dehn filling on $T^{6d}_{\rm irred}[N]$

For a hyperbolic knot complement $N$ and a primitive boundary cycle $(pA+qB) \in H_1 (\partial N, \mathbb{Z})$,

$$\begin{aligned}
T^{6d}_{\rm irred}[N_{pA+qB}] = (\textrm{Giving a nilpotent vev to  $\mu$ of  $T^{6d}_{\rm irred}[N,pA+qB]$})\;.
\end{aligned}$$

The fact that the closing of codimension-2 defects (i.e., knots) corresponds to giving the nilpotent vev to $\mu$ is standard in 4d class S theories. See e.g., [@Tachikawa:2013kta] and references therein. This is also in accord with our terminology 'closable/non-closable', because non-closable cycles have empty $\mu$ and hence it is not possible to do the above operation while preserving supersymmetry. See Table [1](#table:closing){reference-type="ref" reference="table:closing"} below.

::: {#table:closing}
   $pA+qB \in H_1 \big{(}\partial N,\mathbb{Z}\big{)}$             $T^{6d}_{\rm irred}[N_{pA+qB}]$
  ----------------------------------------------------- ------------------------------------------------------
        non-exceptional ($\Rightarrow$ closable)                           non-trivial SCFT
                exceptional and closable                 Gapped theory (possibly with decoupled free chirals)
                      non-closable                                           SUSY broken

  : Basic property of $T^{6d}_{\rm irred}[N_{pA+qB}]$. A primitive boundary cycle $pA+qB$ is called exceptional if $N_{pA+qB}$ is non-hyperbolic.
:::

If the $A$ is non-closable and $q=1$, the above relation can be simplified as follows. The theory $T^{6d}_{\rm irred}[N, pA+B]$ is related to the theory $T^{6d}_{\rm irred}[N,A;B]$ by the transformation $ST^p \in SL(2,{\mathbb Z})$ as \^6d\_irred\[N, pA+B\] = T\^6d\_irred\[N,A;B\] - su(2)\_p - T\[SU(2)\], where $su(2)_p$ is gauging the $su(2)$ symmetry of $T^{6d}_{\rm irred}[N,A;B]$ and the $su(2)_H$ symmetry of $T[SU(2)]$. The Chern-Simons level of this group is $p+[\text{original value}]$, where $[\text{original value}]$ means the contribution of $T^{6d}_{\rm irred}[N,A;B]$ to the Chern-Simons level. To specify this contribution, we have to specify not only the $A$-cycle, but also the $B$-cycle. This is the reason why we are writing $B$ explicitly in the notation $T^{6d}_{\rm irred}[N,A;B]$.

Now, the operator $\mu$ comes from the moment map operator of $T[SU(2)]$ associated to the $su(2)_C$ symmetry which is not gauged. If we give a nilpotent vev to this operator $\mu$, the $T[SU(2)]$ becomes massive and flows to an empty theory in the low energy limit up to the Goldstone multiplets associated to the symmetry breaking of $su(2)_C$ by the vev [@Gaiotto:2008ak]. Neglecting those Goldstone multiplets, the $T[SU(2)]$ disappears and hence we get

$$\begin{aligned}
\begin{split}
T^{6d}_{\rm irred}[N_{pA+B}] &= (\textrm{Gauging $su(2)$ of $T^{6d}_{\rm irred}[N,A;B]$ with additional CS level $p$})\;, 
\\
&= (\textrm{Gauging $su(2)$ of $T^{DGG}[N,A;B]$ with additional CS level $p$})\;.
\label{integral Dehn filling = gauging}
\end{split}
\end{aligned}$$

where we have assumed that $A$ is non-closable and hence $T^{6d}_{\rm irred}[N,A;B] = T^{DGG}[N,A;B]$.

As examples, we consider closed 3-manifolds obtained from $m003/m004/m015$ by performing a Dehn filling. Combing [\[TDGG\[m004\]reproduced\]](#TDGG[m004]reproduced){reference-type="eqref" reference="TDGG[m004]reproduced"},[\[TDGG\[m015\]\]](#TDGG[m015]){reference-type="eqref" reference="TDGG[m015]"} and [\[integral Dehn filling = gauging\]](#integral Dehn filling = gauging){reference-type="eqref" reference="integral Dehn filling = gauging"}, we have[^2]

$$\begin{aligned}
\begin{split}
&T^{6d}_{\rm irred}[(m003)_{ p(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)} = \overline{(S^3\backslash \mathbf{5}^2_1)_{5\mu_1 -  \lambda_1,~ p(2\mu_2-\lambda)+(\mu_2-\lambda_2)}} ]
\\
& = \frac{\textrm{A $u(1)_0$ vector coupled to 2 chrials of charge +1}  }{SU(2)_{p+1/2}}\;,
\\
&T^{6d}_{\rm irred}[(m004)_{ p \mu_2 + (\lambda_2+2 \mu_2)} =(S^3\backslash \mathbf{4}_1)_{(p+2) \mu + \lambda} ]
\\
& = \frac{\textrm{A $u(1)_0$ vector coupled to 2 chrials of charge +1}  }{SO(3)_{p+2}}\;,
\\
&T^{6d}_{\rm irred}[(m015)_{ p \mu_2 + (-2\mu_2- \lambda_2)} =(S^3\backslash \mathbf{5}_2)_{(p-2)\mu + \lambda}]
\\
& = \frac{\textrm{A $u(1)_{-1/2}$ vector coupled to 3 chrials of charge +1}  }{SO(3)_{p-6}}\;.
 \label{Theory for m003/m004 Dehn-filled}
\end{split}
\end{aligned}$$

Here the notation $/G_k$ means that we couple a vector multiplet of group $G$ with the Chern-Simons level $k$. The theories in the numerator has $SU(3)$ symmetry at IR as argued in sec. [\[sec:SU(3)\]](#sec:SU(3)){reference-type="ref" reference="sec:SU(3)"} and we are gauging its $SO(3)/SU(2)$ subgroup. Since the $u(1)_X$ is embedded to the $SU(2)$ (resp. $SO(3)$) in a way that $\mathbf{2}_{su(2)} = (\pm 1)_{u(1)_X}$ (resp. $\mathbf{2}_{su(2)} = (\pm \frac{1}2)_{u(1)_X}$), the CS level $+1$ for $u(1)_X$ in [\[TDGG\[m004\]reproduced\]](#TDGG[m004]reproduced){reference-type="eqref" reference="TDGG[m004]reproduced"} corresponds to CS level $1/2$ (resp. 2) for the $su(2)$. Similarly the CS level $-3$ for $u(1)_X$ in [\[TDGG\[m015\]\]](#TDGG[m015]){reference-type="eqref" reference="TDGG[m015]"} corresponds to CS level $-6$ for the $su(2)$. A parity operation filps the signs of CS levels of the $T^{6d}_{\rm irred}$ theories. The parity operation corresponds to orientation reversal on the internal 3-manifold. It is compatible with following topological facts

$$\begin{aligned}
\begin{split}
 &(m003)_{p(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)}  =\overline{(m003)_{(-p-1)(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)}}\;,
 \\
 &
 (m004)_{ p \mu_2 + (\lambda_2+2 \mu_2)}  =\overline{ (m004)_{ (-p-4) \mu_2 + (\lambda_2+2 \mu_2)} }\;.
 \end{split}
\end{aligned}$$

After gauging $SU(2)/SO(3)$ subgroup of $SU(3)$, the resulting theory generically has following flavor symmetry

$$\begin{aligned}
\begin{split}
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{5}^2_1)_{5\mu_1 -  \lambda_1,~ p(2\mu_2-\lambda)+(\mu_2-\lambda_2)}] \; \textrm{has $u(1)$ flavor symmetry }
\\
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{4}_1)_{(p+2)\mu_2 +\lambda_2}] \; \textrm{has no flavor symmetry }
\\
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{5}_2)_{(p-2)\mu + \lambda}]  \; \textrm{has $u(1)$ flavor symmetry }
\end{split}
\end{aligned}$$

The $u(1)$ for the 3rd case comes from the topological symmetry of $u(1)_{-1/2}$ gauge symmetry of the theory in the numerator. The above is correct when $|p|$ is large enough where the semiclassical analysis is reliable. When $|p|$ is small, the theories could have accidental symmetries. Actually from following topological fact (see Figure. [\[fig:rational-surgery-moves\]](#fig:rational-surgery-moves){reference-type="ref" reference="fig:rational-surgery-moves"}),

$$\begin{aligned}
(S^3\backslash \mathbf{4}_1)_{ -5 \mu +\lambda } = (S^3\backslash \mathbf{5}_2)_{5\mu +\lambda}
\end{aligned}$$

we can conclude that $T^{6d}_{\rm irred}[(S^3\backslash \mathbf{4}_1)_{(p+2)\mu_2 +\lambda_2}]$ has accidental $u(1)$ symmetry for $p=3$ and $p=-7$. We will come back to this point in sec [\[sec: Duality/Surgery\]](#sec: Duality/Surgery){reference-type="ref" reference="sec: Duality/Surgery"}.

[^1]: Their theory $T^{6d}_{(\rm  irred)^c}[M]$ is different from our $T^{6d}_{\rm irred}[M]$ theory. For example, when $M$ is a Lens space, their $T^{6d}_{(\rm  irred)^c}[M]$ is a non-trivial SCFT while supersymmetry is broken in our $T^{6d}_{\rm  irred}[M]$ theory. As discussed in section  [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}, we need to specify a point $P \in {\cal M}_{\rm vacua}(T^{6d}[M] \textrm{ on } \mathbb{R}^3)$ to obtain a 3d effective theory. Their theory may correspond to different choice of $P$ other than $P_{\rm SCFT}$ in [\[Relation-T6d-TDGG:intro\]](#Relation-T6d-TDGG:intro){reference-type="eqref" reference="Relation-T6d-TDGG:intro"}.

[^2]: Taking account of orientation reversal in [\[m015/m017 from whitehead\]](#m015/m017 from whitehead){reference-type="eqref" reference="m015/m017 from whitehead"}, the boundary 1-cycle basis $(\mu_2, \lambda_2)$ of the $S^3\backslash \mathbf{5}_2$ induced from the basis of $S^3\backslash \mathbf{5}^2_1$ can be identified with $(\mu, -\lambda)$=(meridian, -(longitude)) of the knot complement. For $S^3 \backslash \mathbf{4}_1$ case, on the other hand, the $(\mu_2, \lambda_2)$ can be identified with $(\mu, \lambda)$ without sign change. Note that there is no orientation reversal in [\[m003/m004 from whitehead\]](#m003/m004 from whitehead){reference-type="eqref" reference="m003/m004 from whitehead"}.
