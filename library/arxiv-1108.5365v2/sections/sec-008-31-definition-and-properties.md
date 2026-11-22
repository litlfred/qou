---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-008-31-definition-and-properties
section_title: "Definition and properties"
section_number: 3.1
pages: 16-19
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.957
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:QDilog:Def}
Throughout this section, we let $q=e^{\pi i b^2}$ where $b^2\in \R\setminus\Q$ and $0<b^2<1$, so that $|q|=1$. We also denote $Q=b+b\inv$.

Let $\w:=(w_1,w_2)\in\C^2$.

\begin{Def}The Double Zeta function is defined as
\Eq{\ze_2(s,z|\w):=\sum_{m_1,m_2\in\Z_{\geq0}}(z+m_1w_1+m_2w_2)^{-s}.}

The Double Gamma function is defined as
\Eq{\G_2(z|\w):=\exp\left(\frac{\partial}{\partial
s}\ze_2(s,z|\w)|_{s=0}\right).}

Let
\Eq{\G_b(x):=\G_2(x|b,b\inv).}

The Quantum Dilogarithm is defined as the function:
\Eq{S_b(x):=\frac{\G_b(x)}{\G_b(Q-x)}.}

The following form is often useful, and will be used throughout
this paper: \Eq{G_b(x):=e^{\frac{\pi i}{2}x(x-Q)}S_b(x).}
\end{Def}

Let us also relate $G_b$ to another well-known expression by Ruijsenaars \cite{Ru}
\begin{Lem}\label{GbG}
\Eq{G_b(z)=G(b,b\inv;iz-\frac{iQ}{2})e^{\frac{\pi i}{2}z(z-Q)},}
where
\Eq{G(a_+,a_-;z):=\exp\left(i\int_0^\oo \frac{dy}{y}\left(\frac{\sin 2yz}{2\sinh(a_+y)\sinh(a_-y)}-\frac{z}{a_+a_-y}\right)\right)}
with $|Im(z)|<(a_++a_-)/2$ and extends meromorphically to the whole complex plane.
\end{Lem}

The quantum dilogarithm satisfies the following properties:
\begin{Prop} Self-Duality:
\Eq{S_b(x)=S_{b\inv}(x),\tab G_b(x)=G_{b\inv}(x);}

Functional equations: \Eq{\label{funceq}S_b(x+b^{\pm1})=2\sin(\pi
b^{\pm1}x)S_b(x),\tab G_b(x+b^{\pm 1})=(1-e^{2\pi ib^{\pm 1}x})G_b(x);}

Reflection property:
\Eq{\label{reflection}S_b(x)S_b(Q-x)=1,\tab G_b(x)G_b(Q-x)=e^{\pi ix(x-Q)};}

Complex Conjugation: \Eq{\overline{S_b(x)}=\frac{1}{S_b(Q-\over[x])},\tab \overline{G_b(x)}=\frac{1}{G_b(Q-\bar{x})},}
in particular \Eq{\label{gb1}\left|S_b(\frac{Q}{2}+ix)\right|=\left|G_b(\frac{Q}{2}+ix)\right|=1 \mbox{ for $x\in\R$};}

Analyticity:

$S_b(x)$ and $G_b(x)$ are meromorphic functions with poles at
$x=-nb-mb\inv$ and zeros at $x=Q+nb+mb\inv$, for $n,m\in\Z_{\geq0}$;

\label{asymp} Asymptotic Properties:
\Eq{G_b(x)\sim\left\{\begin{array}{cc}\bar{\ze_b}&Im(x)\to+\oo\\\ze_b
e^{\pi ix(x-Q)}&Im(x)\to-\oo\end{array},\right.}
where
\Eq{\ze_b=e^{\frac{\pi i}{4}+\frac{\pi i}{12}(b^2+b^{-2})};}

\label{residue} Residues:
\Eq{\lim_{x\to 0} xG_b(x)=\frac{1}{2\pi},} or more generally,
\Eq{Res\frac{1}{G_b(Q+z)}=-\frac{1}{2\pi}\prod_{k=1}^n(1-q^{2k})\inv\prod_{l=1}^m(1-\widetilde{q}^{2l})\inv}
at $z=nb+mb\inv, n,m\in\Z_{\geq0}$ and $\widetilde{q}=e^{\pi i
b^{-2}}$.
\end{Prop}

From the asymptotic properties, we have the following useful corollary that is needed when we deal with interchanging of order of integrations:
\begin{Cor} \label{asymp} For $s,t\in\C, x\in\R$, the asymptotic behavior of the ratio is given by
\Eq{\left|\frac{G_b(s+ix)}{G_b(t+ix)}\right|\sim\left\{\begin{array}{cc}1&x\to+\oo\\e^{2\pi x Re(t-s)}&x\to-\oo\end{array}.\right.}
\end{Cor}

By analytic continuation in $b$, there exists a classical limit for $G_b(x)$ given in \cite{Ip}:
\begin{Thm}\label{classicallimit} For $q=e^{\pi ib^2}$, by letting $b^2\to i0^+$ we have
\Eq{\lim_{b\to 0} \frac{G_b(bx)}{\sqrt{-i}|b|(1-q^2)^{x-1}}=\G(x),}
where $\sqrt{-i}=e^{-\frac{\pi i}{4}}$ and $-\frac{\pi}{2}<\arg(1-q^2)<\frac{\pi}{2}$. The limit converges uniformly for any compact set in $\C$.
\end{Thm}

We will also need another important variant of the quantum dilogarithm function:
\Eq{g_b(x):=\frac{\bar{\ze_b}}{G_b(\frac{Q}{2}+\frac{1}{2\pi i b}\log x)},}
where $|g_b(x)|=1$ when $x\in\R_{>0}$ due to \eqref{gb1}.
\begin{Lem} Let $u, v$ be self-adjoint operators with $uv=q^2vu$, $q=e^{\pi i b^2}$. Then
\Eq{\label{qexp}g_b(u)g_b(v)=g_b(u+v),}
\Eq{\label{qpenta}g_b(v)g_b(u)=g_b(u)g_b(q\inv uv)g_b(v).}
\end{Lem}

\eqref{qexp} and \eqref{qpenta} are often referred to as the quantum exponential and the quantum pentagon relations, which follows from the other properties:
\Eq{\label{qsum1}g_b(u)^*vg_b(u) = q\inv uv+v,}
\Eq{\label{qsum2}g_b(v)ug_b(v)^*=u+q\inv uv.}
