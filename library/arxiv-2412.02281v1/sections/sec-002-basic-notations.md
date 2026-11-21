---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-002-basic-notations
section_title: "Basic Notations"
section_number: null
pages: 3-4
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.737
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
\label{notation}
        We recall some basic notations of $q$-calculus with $0<q<1$ (referring to \cite{gasper2004basic} for more details): 
        \begin{itemize}
            \item The $q$-Pochhammer symbol is 
            \begin{equation*}
          (a ; q)_n:=  \left\{
          \begin{array}{lr}
             1,   & \text{if} \ \ n=0,       \\
\prod_{l=0}^{n-1} (1-aq^{l}),         & \text{if} \ \ n \geq 1.
             \end{array}
\right.
\end{equation*}
Moreover, $(a ; q)_{\infty}:=\prod_{l=0}^{\infty}\left(1-a q^l\right)$ and 
\begin{equation*}
    \left(a_1, a_2, \ldots, a_m ; q\right)_{\infty}:=\left(a_1 ; q\right)_{\infty}\left(a_2 ; q\right)_{\infty} \cdots\left(a_m ; q\right)_{\infty}.
\end{equation*}
\item  The $q$-theta function is
\begin{equation*}
    \theta_q(z):=\sum_{n \in \mathbb{Z}} q^{\frac{n(n-1)}{2}} z^n, \quad  z \in \mathbb{C}^*.
\end{equation*}
It satisfies
\begin{equation}
\label{theta(q z)}
\theta_q(q^n z)=z^{-n}q^{-\frac{n(n-1)}{2}}\theta_q(z)=\theta_q\left(\frac{1}{q^{n-1}z}\right),\quad  n\in \mathbb{Z},
\end{equation}
and the Jacobi's triple product identity
\begin{equation}
\label{Jacobi's triple product identity}
\theta_q(z)=(q,-z,-q / z ; q)_{\infty}.
\end{equation} 
\item  The $q$-exponential function is  
\begin{equation*}
    e_q(z):=\frac{1}{\left((1-q)z;q\right)_{\infty}},
\end{equation*}
with the Taylor expansion
\begin{equation}\label{eq:taylor}
    e_q(z)=\sum_{k=0}^{\infty} \frac{(1-q)^k}{(q;q)_k}z^k, \quad  0 \leq  | z | <1.
\end{equation}
\item The $q$-Gamma function $\Gamma_q(z)$  is
\begin{equation*}
    \Gamma_q(z):=\frac{(q ; q)_{\infty}}{\left(q^z ; q\right)_{\infty}}(1-q)^{1-z}, \quad z\in \mathbb{C}\backslash \{0,-1,-2,...\},
\end{equation*}
{where $q^z$ and $(1-q)^{1-z}$ take the principal values}.
        \end{itemize}
