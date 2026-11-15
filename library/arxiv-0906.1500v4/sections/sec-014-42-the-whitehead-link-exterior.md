---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-014-42-the-whitehead-link-exterior
section_title: "The Whitehead link exterior"
section_number: 4.2
pages: 13-14
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.975
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:polynomial_torion_Whiteheadlink}
Let $L$ be the Whitehead link and choose
the following Wirtinger presentation of the Whitehead link group:
\[
\pi_1(E_{L}) = \langle a, b \,|\, awa^{-1}w^{-1} \rangle
\text{ where } w = bab^{-1}a^{-1}b^{-1}ab.
\]
\begin{figure}[h]
  \centering
  \includegraphics[scale=.5]{Whitehead_link_Wirtinger}
  \caption{The Whitehead link with meridians}
  \label{fig:WhiteheadLinkMeridians}
\end{figure}

Hilden, Lozano and Montesionos has shown an
explicit description of the character variety of the Whitehead link
group in~\cite{HLM92:characterization}.  Trace functions play the role
of local coordinates in this description.   We set $x$, $y$ and $v$ as
$x=I_a$, $y=I_b$ and $v=I_{ab}$, where $I_\gamma \colon X(E_L) \to \CC$ is again given by $I_\gamma (\chi) = \chi(\gamma)$.  Then the character variety of
$X(E_L)$ is expressed as
\[
X(E_L) = \{(x, y, v)\in \CC^3 \,|\, p(x, y, v) q(x, y, v) = 0\},
\]
where 
\begin{align*}
  p(x, y, v) &= xy - (x^2 + y^2 - 2)v + xyv^2 - v^3,\\
  q(x, y, v) &= x^2 + y^2 + v^2 -xyv - 4.
\end{align*}
The component of irreducible characters is given by 
\[ 
X^{\mathrm{irr}}(E_L) =\{(x, y, v)\in \CC^3 \,|\, p(x, y, v) = 0\} \setminus R
\]
where $R = \{x = \pm 2, v= \pm y\} \cup \{y = \pm 2, v = \pm x\}$.  We
consider an $\SL$-representation $\rho$ of $\pi_1(E_L)$ whose
character is contained in $X^{\mathrm{irr}}(E_L)$.  

Let $\rho \colon \pi_1(E_L) \to \SL$ be an irreducible representation and consider  
the abelianization $\varphi$ of $\pi_1(E_L)$: $\varphi\colon \pi_1(E_L) \to \ZZ^2 = \langle t_1, t_2 \,|\, t_1t_2 = t_2t_1 \rangle$ defined by $\varphi(a) = t_1$ and $\varphi(b)
= t_2$.  

Using irreducibility of $\rho$, we can suppose that the pair of
$\rho(a)$ and $\rho(b)$ are expressed as (after taking conjugation with eigenvectors of $\rho(a)$ and $\rho(b)$ if necessary):
\[
\rho(a) = 
\left(
  \begin{array}{cc}
    \alpha & 1 \\
    0 & 1/\alpha
  \end{array}
\right)
\quad
\rho(b) = 
\left(
  \begin{array}{cc}
    \beta & 0 \\
    \gamma & 1/\beta
  \end{array}
\right).
\]

Note that we have set the local coordinates $(x, y, v)$ as 
$x = \alpha + \alpha^{-1}$, $y = \beta + \beta^{-1}$ and 
$v = \gamma + \alpha\beta + \alpha^{-1}\beta^{-1}$. 

By using formula in~\cite{Milnor:1968,Kitano, KL},
the polynomial torsion is expressed as 
\[
\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2)
= 
\tau_0 \cdot 
\frac{\det \Phi \left( \frac{\partial}{\partial b}\, awa^{-1}w^{-1}  \right)}{\det \Phi(a-1)}
\]
where $\Phi$ is the linear extension of $\otAd{\varphi}{\rho^{-1}}$ on $\ZZ[\pi_1(E_L)]$.
The Fox differential turns into 
\[
\frac{\partial}{\partial b}\left( {awa^{-1}w^{-1} }\right)
= (a-1)(1 - bab^{-1} - bab^{-1}a^{-1}b^{-1} + bab^{-1}a^{-1}b^{-1}a).
\]
Therefore the polynomial torsion $\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2)$
turns out 
$$\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2) 
= \tau_0 \cdot \det \Phi(1 - bab^{-1} - bab^{-1}a^{-1}b^{-1} +
bab^{-1}a^{-1}b^{-1}a).$$ 
So that, with $\det Ad _{\rho (a)^{-1}} =
\det Ad_{\rho(b)^{-1}} = 1$ in mind,
\begin{align*}
  \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2)
  &= \tau_0 \cdot 
     \det \Phi(1 - bab^{-1} - bab^{-1}a^{-1}b^{-1} + bab^{-1}a^{-1}b^{-1}a)\\
  &= \tau_0 \cdot 
     \det \Phi\left( (bab^{-1}a^{-1})(aba^{-1}b^{-1} - a - b^{-1} + b^{-1}a ) \right)\\
  &= \tau_0 \cdot  
     \det \Phi(aba^{-1}b^{-1} - a - b^{-1} + b^{-1}a ).
\end{align*}


When we choose the basis $\{E, H, F\}$ in $\sll$, the adjoint actions
$Ad_{\rho(a)^{-1}}$ and $Ad_{\rho(b)^{-1}}$ are represented by the following 
upper and lower triangular matrices
\[
Ad_{\rho(a)^{-1}}=
\left(
  \begin{array}{ccc}
    1/\alpha^2 & 2/\alpha & -1 \\
    0 & 1 & -\alpha \\
    0 & 0 & \alpha^2
  \end{array}
\right)\, \hbox{and}\,\,
Ad_{\rho(b)^{-1}}=
\left(
  \begin{array}{ccc}
    1/\beta^2 & 0 & 0 \\
    \gamma/\beta & 1 & 0 \\
    -\gamma^2 & -2\beta\gamma & \beta^2
  \end{array}
\right).
\]

Calculating the determinant and reducing the degree of $\gamma$ by
using the following identity $p(\alpha + \alpha^{-1}, \beta + \beta^{-1}, \gamma + \alpha
\beta + \alpha^{-1}\beta^{-1})=0$, we can see that the polynomial
torsion is expressed as
\begin{align}\label{eqn:PolyTorsion_WL}
  &\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2)\\
  &= \tau_0 \cdot 
    \frac{(t_1-1)(t_2-1)}{t_2^3} 
    \left( -2xyv t_1t_2 +
    x^2 t_1(t_2+1)^2 + y^2 (t_1+1)^2 t_2 - (t_1+1)^2 (t_2+1)^2
    \right). \nonumber
\end{align}
