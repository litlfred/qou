---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-019-8-quantum-coordinate-rings-and-modified-quantize
section_title: "Quantum coordinate rings and modified quantized enveloping algebras"
section_number: 8
pages: 54-58
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.902
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\subsection{Quantum coordinate ring} Let $U_q(\g)^*$ be $\Hom_{\Q(q)}(U_q(\g),\Q(q))$. Then the comultiplication $\comp$  (see \eqref{eq: comp})   induces the
 multiplication $\mu$ on $U_q(\g)^*$ as follows:
\begin{align*}
 \mu \cl  & U_q(\g)^* \tens U_q(\g)^* \to (\U\tens\U)^*\To[\;(\comp)^*\;]
U_q(\g)^* .
\end{align*}
Later on, it will be convenient to use Sweedler's notation
$\comp(x)=x_{(1)} \tens x_{(2)}$.
With this notation,
$$\text{$\bl fg\br(x)=f(x_{(1)})\,g(x_{(2)})$\quad
for $f,g \in U_q(\g)^*$ and  $x\in\U$.}$$

The $U_q(\g)$-bimodule structure on $U_q(\g)$ induces
a $U_q(\g)$-bimodule structure on $U_q(\g)^*$. Namely,
\begin{align*}
(x \cdot f) (v) =f(vx) \quad \text{ and } \quad (f \cdot x) (v)
=f(xv) \quad\text{ for } f \in U_q(\g)^* \text{ and } x,v \in U_q(\g).
\end{align*}


Then the multiplication $\mu$ is a morphism of a
$U_q(\g)$-bimodule, where $U_q(\g)^* \tens U_q(\g)^*$ has the
structure of a $U_q(\g)$-bimodule via $\comp$. That is, for $f,g \in U_q(\g)^*$ and  $x,y \in U_q(\g)$,  we have
$$ x(fg)y=(x_{(1)}fy_{(1)})(x_{(2)}gy_{(2)}),$$
where $\comp(x)=x_{(1)}\tens x_{(2)}$ and $\comp(y)=y_{(1)}\tens y_{(2)}$.


\begin{definition}
We define the {\em quantum coordinate ring} $A_q(\g)$ as follows:
$$A_q(\g) = \{ u \in U_q(\g)^* \ | \ \text{ $U_q(\g)u$ belongs to $\Oint(\g)$ and $u U_q(\g)$ belongs to $\Oint^\ri(\g)$}\}. $$
\end{definition}

Then, $A_q(\g)$ is a
subring of $U_q(\g)^*$
because {\rm (i)} $\mu$ is $U_q(\g)$-bilinear, {\rm (ii)}  $\Oint(\g)$ and
$\Oint^\ri(\g)$ are closed under the tensor product.

We have the weight decomposition:
$A_q(\g) = \soplus_{\eta,\zeta \in \wl} A_q(\g)_{\eta,\zeta}$, where
$$A_q(\g)_{\eta,\zeta} \seteq \{  \psi \in A_q(\g) \ | \  q^{h_\li} \cdot \psi \cdot q^{h_\ri} = q^{\langle h_\li,\eta \rangle +\langle h_\ri,\zeta \rangle  } \psi
\text{ for } h_\li,h_\ri \in \wl^\vee \},$$
For $\psi \in A_q(\g)_{\eta,\zeta}$, we write
$$ \wt_\li(\psi)=\eta \quad \text{ and } \quad \wt_\ri(\psi)=\zeta.$$

\medskip
For any $V\in\Oint(\g)$, we have the $U_q(\g)$-bilinear homomorphism
$$\Phi_V\colon V\tens (\Dv V)^\ri\to A_q(\g)$$
given by
$$\Phi_V(v\tens \psi^\ri)(a)=\lan \psi^\ri, av\ra=\lan \psi^\ri a, v\ra \quad\text{for $v\in V$,
$\psi\in\Dv V$ and $a\in U_q(\g)$.}$$

\begin{prop} [{\cite[Proposition 7.2.2]{Kas93}}] We have an isomorphism $\Phi$ of $\Uqg$-bimodules
\begin{equation} \label{eq: Phi}
\Phi\cl  \soplus_{\lambda \in \wl^+} V(\lambda) \tens_{\Q(q)}
V(\lambda)^\ri \overset{\sim}{\longrightarrow} A_q(\g)
\end{equation}
given by $\Phi|_{V(\lambda) \tens_{\Q(q)} V(\lambda)^\ri} = \Phi_\lambda \seteq \Phi_{V(\lambda)}$. Namely,
$$ \Phi(u \tens v^\ri)(x)= \lan v^\ri,xu \ra = \lan v^\ri x,u \ra =(v,xu) \text{ for any } v,u \in V(\lambda) \text{ and } x \in U_q(\g).$$
\end{prop}





We introduce the
 crystal basis $\big(L^\up(A_q(\g)), B(A_q(\g)) \big)$ of $\Ag$ as the images by $\Phi$ of
$$ \soplus_{\lambda \in \wl^+} L^\up(\lambda) \otimes L^\up(\lambda)^\ri \text{ and }
\bigsqcup_{\lambda \in \wl^+} B(\lambda) \otimes B(\lambda)^\ri.$$
Hence it is a crystal base with respect to the left action of
$\U$ and also the right action of $\U$.
We sometimes write by
$e_i^*$ and $f_i^*$ the operators  of $\Ag$ obtained by the right actions of
$e_i$ and $f_i$.

\medskip
We define the $\A$-form of $\Ag$ by
$$\Ag_\A\seteq\set{\psi\in\Ag}{\lan \psi,\, \U_\A\ran\subset\A}.$$

We define the bar-involution $-$ of $A_q(\g)$ by
$$ \overline{\psi}(x) = \overline{\psi(\overline{x})} \quad \text{ for } \psi \in A_q(\g), \  x \in U_q(\g).$$

Note that the bar-involution is not a ring homomorphism but it satisfies
\eqn
&&\ol{\psi\;\theta\;}=q^{(\wt_\lt(\psi),\wt_\lt(\theta))
-(\wt_\rt(\psi),\wt_\rt(\theta))}\;\ol{\theta}\;\ol{\psi}\quad
\text{for any $\psi$, $\theta\in\Ag$.}
\eneqn
Since we do not use this formula and
it is proved similarly to Proposition~\ref{prop:phimul} below,
we omit its proof.

The triple $\big(\Q\tens \Ag_\A,\,L^\up(A_q(\g)),\,\overline{L^\up(A_q(\g))}\big)$ is balanced (\cite[Theorem 1]{Kas93}), and hence there exists an upper global basis of $\Ag$
$$ \B^\up(A_q(\g))\seteq \{ G^\up(b) \ | \ b \in B^\up(A_q(\g)) \}.$$

For $\la\in\Pd$ and $\mu\in W\la$, we denote by $u_{\mu}$
 the unique member of the upper global basis
of $V(\la)$ with weight $\mu$. It is also a member of the lower global basis.



\begin{prop}\label{prop:Agglobal}
Let $\lambda\in\wl^+$, $w\in W$ and $b\in B(\lambda)$.
Then, $\Phi(G^\up(b)\tens u_{w\lambda}^\ri)$ is a member of
the upper global basis of $A_q(\g)$.
\end{prop}
\begin{proof}
The element $\psi\seteq\Phi(G^\up(b)\tens u_{w\lambda}^\ri)$ is
bar-invariant and a member of crystal basis modulo $q L^\up(A_q(\g))$.
For any $P\in U_q(\g)_\A$,
$$\lan\psi, P\ra=\big( u_{w\lambda}, PG^\up(b)\big)$$
belongs to $\A$ because $PG^\up(b)\in V^\up(\lambda)_\A$ and
$u_{w\lambda}\in V^\low(\lambda)_\A$.
Hence $\psi$ belongs to $\Ag_\A$.
\end{proof}


\medskip


The $\Q(q)$-algebra anti-automorphism $\vphi$ of $\U$ induces
a $\Q(q)$-linear automorphism $\vphi^*$
of $\Ag$
by
$$\bl\vphi^* \psi \br(x)=\psi\bl\vphi(x)\br\quad\text{for any $x\in \U$.}$$
We have
$$\vphi^*\bl\Phi(u\tens v^\rt)\br=\Phi(v\tens u^\rt),$$
and
$$\wtl(\vphi^*\psi)=\wtr(\psi)\qtext \wtr(\vphi^*\psi)=\wtl(\psi).$$
It is obvious that
$\vphi^*$ preserves
$\Ag_\A$, $L^\up(\Ag)$ and $ \B^\up(A_q(\g))$.
\Prop\label{prop:phimul}
$$\vphi^*(\psi\theta)=
q^{(\wtr(\psi),\wtr(\theta))-(\wtl(\psi),\wtl(\theta))}
(\vphi^*\psi)(\vphi^*\theta).$$
\enprop
In order to prove this proposition, we prepare
a sublemma.

Let $\xi$ be the $\Q(q)$-algebra automorphism of $\Uq$ given by
$$\xi(e_i)=q_i^{-1}t_ie_i, \quad\xi(f_i)=q_if_it_i^{-1},\quad \xi(q^h)=q^h.$$
We can easily see
\eqn
&&(\xi\tens\xi)\circ\Cmp=\Cmm\circ\xi.
\label{eq:Dexi}
\eneqn

Let $\xi^*$ be the automorphism of $\Ag$ given by
$$(\xi^*\psi)(x)=\psi(\xi(x))\quad\text{for $\psi\in\Ag$ and $x\in\Uq$.}$$

\Sub\label{sub:xi}
We have
\eqn
&&\xi^*(\psi)=q^{A(\wt_\lt(\psi),\wt_\rt(\psi))}\psi,\label{eq:xistar}
\eneqn
 where $A(\la,\mu)=\dfrac{1}{2}\bl(\mu,\mu)-(\la,\la)\br$.
\ensub
\Proof
Let us show that, for each $x$, the following equality
\eq
&&\psi(\xi(x))=q^{A(\wt_\lt(\psi),\wt_\rt(\psi))}\psi(x)\label{eq:xi}
\eneq
holds for any $\psi$.

The equality \eqref{eq:xi} is obviously true for $x=q^h$.
If \eqref{eq:xi} is true for $x$, then
\eqn
&&\xi^*(\psi)(xe_i)=\psi\bl\xi(xe_i)\br=\psi\bl\xi(x)e_it_i)q_i\\
&&=q^{(\al_i,\wt_\lt(\psi))+(\al_i ,\al_i)/2}\psi(\xi(x)e_i)\\
&&=q^{(\al_i,\wt_\lt(\psi))+(\al_i , \al_i)/2}\bl\xi^*(e_i\psi)\br(x)\\
&&=q^{(\al_i,\wt_\lt(\psi))+(\al_i , \al_i)/2+A(\wt_\lt(\psi)+\al_i,\wt_\rt(\psi))}
(e_i\psi)(x).
\eneqn
Since $\Vert\la+\al_i\Vert^2
=\Vert\la\Vert^2+2(\al_i,\la)+ \Vert \al_i\Vert^2 $,
\eqref{eq:xi} holds for $xe_i$.
Similarly if
\eqref{eq:xi} holds for $x$,
then it holds for $xf_i$.
\QED

\Proof[{Proof of Proposition~\ref{prop:phimul}}]
We have
\eqn
&&(\vphi\circ\vphi)\circ \Cmm=\Cmp\circ \vphi.
\label{eq:phiC}
\eneqn
Hence, we have
\begin{align*}
\lan \vphi^*(\psi\theta), x\ran
&=\lan\psi\theta,\vphi(x)\ran\\
&=\lan\psi\tens\theta,\Cmp(\vphi(x))\ran\\
&=\lan\psi\tens\theta,(\vphi\tens\vphi)\circ\Cmm(x)\ran\\
&=\lan \vphi^*(\psi)\tens\vphi^*(\theta),\;\Cmm(x)\ran.
\end{align*}
 It follows that
\begin{align*}
\lan \xi^*(\vphi^*(\psi\theta)),x\ran
&=\lan\vphi^*(\psi\theta), \xi (x)\ran
=\lan \vphi^*(\psi)\tens\vphi^*(\theta),\Cmm(\xi(x))\ran\\
&=\lan\vphi^*(\psi)\tens\vphi^*(\theta),(\xi\tens\xi)\circ\Cmp x \ran\\
&=\lan \xi^*\vphi^*(\psi)\tens\xi^*\vphi^*(\theta),\Cmp x \ran\\
&=\lan\bl\xi^*\vphi^*(\psi)\br\bl\xi^*\vphi^*(\theta)\br,x\ran\\
&=q^{A(\wtr(\psi),\wtl(\psi))+A(\wtr(\theta),\wtl(\theta))}
\lan  (\vphi^*\psi)\,(\vphi^*\theta) ,\,x\ran.
\end{align*}
 Therefore we obtain
$$\vphi^*(\psi\theta)=q^c(\vphi^*\psi)\,(\vphi^*\theta)$$
with
\eqn
&&c=A(\wtr(\psi),\wtl(\psi))+A(\wtr(\theta),\wtl(\theta))-
A(\wtr(\psi)+\wtr(\theta),\wtl(\psi)+\wtl(\theta))\\
&&\hs{2ex}=(\wtr(\psi),\wtr(\theta))-(\wtl(\psi),\wtl(\theta)).
\eneqn
\QED
