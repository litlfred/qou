---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-014-34-comparison-of-different-parameters
section_title: "Comparison of different parameters"
section_number: 3.4
pages: 34-38
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.967
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
Let $k$ be real valued and let $q$ be positive. We will investigate what happens to the 
homology of the algebras 
$\mh H (\tilde{\mc R},k) \rtimes \Gamma ,\, \mc H (\mc R,q) \rtimes \Gamma$ and 
$\mc S (\mc R ,q) \rtimes \Gamma$ when we replace $k$ by $\ep k \; (\ep \in \C^\times)$ and 
$q$ by $q^\ep \; (\ep \in \C \setminus i \R)$. For the Schwartz algebras we must of 
course take $\ep$ real.

Recall the analytic families of representations $\pi_{\sigma_{w,i}}$ from Lemma \ref{lem:6.3} 
and $\pi_{\rho_w}$ from Corollary \ref{cor:6.5}. As discussed in the proof Theorem 
\ref{thm:6.6}, adjusting the parameter function by $\ep$ corresponds to applying 
$m_\ep^*$ to $\sigma_{w,i}$ and $\rho_w$. Let
\[
\begin{array}{lll}
\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma & \to & 
\mc O (\mf t^{\rho_w}) \otimes \mr{End}_\C (V_{\rho_w}^\Gamma), \\
\mc H (\mc R,q^\ep) \rtimes \Gamma & \to & 
\mc O (T^{\sigma_{w,i}}) \otimes \mr{End}_\C (V_{\sigma_{w,i}}^\Gamma), \\
\mc S (\mc R,q) \rtimes \Gamma & \to & 
C^\infty (T_{un}^{\sigma_{w,i}}) \otimes \mr{End}_\C (V_{\sigma_{w,i}}^\Gamma)
\end{array}
\]
be the corresponding algebra homomorphisms. By Theorems \ref{thm:7.1}, \ref{thm:8.2} and 
\ref{thm:9.1} these induce isomorphisms
\begin{align*}
& HH_* (\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma) \to \bigoplus_{w \in \langle W' \rangle} 
\Omega^* (\mf t^{\rho_w} )^{\mc G_{\rho_w}} \cong  \bigoplus_{w \in \langle W' \rangle} 
\Omega (\mf t^w)^{Z_{W'}(w)} , \\
&  HH_* (\mc H (\mc R,q^\ep) \rtimes \Gamma) \to \bigoplus_{w \in \langle W' \rangle} 
\bigoplus_{i=1}^{c(w)} \Omega^* (T^{\sigma_{w,i}} )^{\mc G_{\sigma_{w,i}}} \cong
\bigoplus_{w \in \langle W' \rangle} \Omega^* (T^w )^{Z_{W'}(w)} ,\\
& HH_* (\mc S (\mc R,q^\ep) \rtimes \Gamma) \to \bigoplus_{w \in \langle W' \rangle} 
\bigoplus_{i=1}^{c(w)} \Omega_{sm}^* (T_{un}^{\sigma_{w,i}})^{\mc G_{\sigma_{w,i}}} \cong
\bigoplus_{w \in \langle W' \rangle} \Omega_{sm}^* (T_{un}^w )^{Z_{W'}(w)} .
\end{align*}
The action of $Z (\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma) \cong \mc O (\mf t)^{W'}$ on
$\Omega^* (\mf t^{\rho_w})$ is via the embedding
\[
\mf t^{\rho_w} \to \mf t : \lambda \mapsto cc(m_\ep^* (\rho_w)) + \lambda = 
\ep \, cc( \rho_w) + \lambda .                                  
\]
The translation factor $cc(m_\ep^* (\rho_w)) \in \mf t$ is a representative for the 
central character of $m_\ep^* (\rho_w)$. 
Similarly, the actions of $Z (\mc H (\mc R,q^\ep) \rtimes \Gamma) \cong \mc O (T )^{W'}$ on 
$\Omega^* (T^w)$ and on $\Omega^*_{sm} (T^w_{un})$ go via the embedding
\[
T^{\sigma_{w,i}} \to T : t \mapsto cc (m_\ep^* (\sigma_{w,i})) t . 
\]
Here $cc (m_\ep^* (\sigma_{w,i})) \in T_{un}$ is a representative for the central character 
of $\sigma_{w,i}$, and by \eqref{eq:6.weights} it lies in $Y \otimes S^1 q^{\ep \Z / 2}$.

Now we will generalize these results to the case $\ep = 0$. Recall the maps
\[
\zeta^\vee : G \big( \mh H (\tilde{\mc R},\ep k \big) \rtimes \Gamma \big) \to 
G \big( S (\mf t^*) \rtimes \Gamma \big)
\]
from Theorem \ref{thm:6.4} and
\[
\zeta^\vee : G \big( \mc  H (\mc R, q^\ep) \rtimes \Gamma \big) \to 
G \big( \C [X] \rtimes W' \big) 
\]
from Theorem \ref{thm:6.6}. These maps send analytic families to other analytic families, 
because they commute with parabolic induction.

\begin{thm} \label{thm:10.1}
\enuma{
\item Let $k$ be real valued and let $\ep \in \C^\times$. There exists a unique isomorphism 
\[
HH_* (\zeta^\vee) : HH_* (S (\mf t^*) \rtimes W') \to 
HH_* (\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma)
\]
such that 
\[
HH_* (\pi_\rho) \circ HH_* (\zeta^\vee) = HH_* ( \zeta^\vee (\pi_\rho))
\]
for all analytic families of $\mh H (\tilde{\mc R}, \ep k) \rtimes \Gamma$-representations 
$\{ \pi_\rho (\lambda) \mid \lambda \in \mf t^\rho \}$.
\item Let $q$ be positive and let $\ep \in \C \setminus i\R$. There exists a unique isomorphism 
\[
HH_* (\zeta^\vee) : HH_* (\C [X] \rtimes W') \to HH_* (\mc H (\mc R,q^\ep) \rtimes \Gamma)
\]
such that 
\[
HH_* (\pi_\sigma) \circ HH_* (\zeta^\vee) = HH_* ( \zeta^\vee (\pi_\sigma))
\]
for all analytic families of $\mc H (\mc R,q^\ep) \rtimes \Gamma$-representations 
$\{ \pi_\sigma (t) \mid t \in T^\sigma \}$.
\item Let $q$ be positive. There exists a unique isomorphism 
\[
HH_* (\zeta^\vee) : HH_* (\mc S (X) \rtimes W') \to HH_* (\mc S (\mc R,q) \rtimes \Gamma)
\]
such that 
\[
HH_* (\pi_\sigma) \circ HH_* (\zeta^\vee) = HH_* ( \zeta^\vee (\pi_\sigma))
\]
for all analytic families of $\mc S (\mc R,q) \rtimes \Gamma$-representations 
$\{ \pi_\sigma (t) \mid t \in T_{un}^\sigma \}$.
} 
\noindent In all three settings the analogous statements for cyclic and periodic 
cyclic homology are also valid.
\end{thm}
\emph{Proof.}
We will only prove (a), the other parts follow in the same way. The construction of
the $\pi_{\rho_w}$ and the proof of Lemma \ref{lem:6.3} show that the analytic families
\begin{equation}\label{eq:10.1}
\{ \zeta^\vee (\pi_{\rho_w} (\lambda)) \mid w \in \langle W' \rangle , 
\lambda \in \mf t^{\rho_w} \}
\end{equation}
fulfill Corollary \ref{cor:6.5} for $\mh H (\tilde{\mc R},0) \rtimes \Gamma = S (\mf t^*) 
\rtimes W'$. We remark that the representations \eqref{eq:10.1} can be reducible, even
for generic $\lambda$. But since this does not affect the arguments in Section 
\ref{sec:HGHA}, we may ignore it. In particular Theorem \ref{thm:7.1} holds for
$S(\mf t^*) \rtimes W'$ with \eqref{eq:10.1}. Now the condition of the theorem enforces
that $HH_* (\zeta^\vee)$ is the composite isomorphism 
\[
HH_* (S(\mf t^*) \rtimes W') \longrightarrow \bigoplus_{w \in \langle W' \rangle} \Omega^* 
(\mf t^{\rho_w} )^{\mc W'_{\rho_w}} \xrightarrow{\: HH_* (\tilde \rho )^{-1} \:} 
HH_* (\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma ) .
\]
For all $w \in \langle W' \rangle$ this map satisfies
\[
HH_* (\pi_{\rho_w}) \circ HH_* (\zeta^\vee) = HH_* ( \zeta^\vee (\pi_{\rho_w})) .
\]
Thus it remains to check compatibility with an arbitrary analytic family of
$\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma$-representations $\{ \pi_\rho (\lambda) \mid
\lambda \in \mf t^{\rho} \}$. Let $\lambda$ be a generic point of $\mf t^\rho$.
By Corollary \ref{cor:6.5}.c we can find $n_\rho \in \N, n_w \in \Z$ and 
$\mu_{w,\lambda} \in \mf t^{\rho_w}$ such that
\begin{equation} \label{eq:10.2}
n_\rho \pi_\rho (\lambda) = \sum_{w \in \langle W' \rangle} n_w \pi_{\rho_w}(\mu_{w,\lambda})
\quad \text{in} \quad G \big( \mh H (\tilde{\mc R},\ep k) \rtimes \Gamma \big) .
\end{equation}
The genericity of $\lambda$ implies $n_w = 0$ unless $W' \mf t^{\rho_w} \supset W' \mf t^\rho$.
Comparing the central characters also shows that there exist $\tilde w \in W'$ with
\[
\tilde \lambda + cc (\pi_\rho (0)) = \mu_{w,\lambda} + cc (\pi_{\rho_w}(0)) ,
\]
for suitable representatives $cc (\pi)$ of the central character of the representations
$\pi$ under consideration. Hence we may take
\[
\mu_{w,\lambda} = \tilde w \lambda + cc(\pi_\rho (0)) - cc (\pi_{\rho_w} (0)) =: 
\tilde \lambda + \mu_w .
\]
Since $\lambda$ was generic, with this choice of $\mu_{w,\lambda}$ \eqref{eq:10.2} becomes
valid for all generic $\lambda \in \mf t\rho$, which then by continuity extends to the 
whole of $\mf t^\rho$. Next we bring the terms $n_w < 0$ to the other side and obtain
\[
n_\rho \pi_\rho (\lambda) + \sum_{w \in \langle W' \rangle_-} -n_w \pi_{\rho_w}(\tilde \lambda 
+ \mu_w) = \sum_{w \in \langle W' \rangle_+} n_w \pi_{\rho_w}(\tilde \lambda + \mu_w) .
\]
This is an equality in $G (\mh H (\tilde{\mc R},\ep k) \rtimes \Gamma)$, but the 
representations on the both sides need not be isomorphic. Since Hochschild homology does not 
distinguish direct sums from nontrivial extensions \cite[Theorem 1.2.15]{Lod}, we may 
nevertheless treat it as an equivalence of 
$\mh H (\tilde{\mc R},k) \rtimes \Gamma$-representations. Consequently
\[
n_\rho HH_* (\pi_\rho ) + \sum_{w \in \langle W' \rangle_-} -n_w 
HH_* (\pi_{\rho_w})\big|_{\mu_w + \tilde w \mf t^\rho} = 
\sum_{w \in \langle W' \rangle_+} n_w HH_* (\pi_{\rho_w}) \big|_{\mu_w + \tilde w \mf t^\rho}
\]
as maps 
\[
HH_* \big( \mh H (\tilde{\mc R},\ep k) \rtimes \Gamma \big) \to HH_* (\mc O (\mf t^\rho)) 
\cong \Omega^* (\mf t^\rho) .
\]
Now he aforementioned compatibility of $HH_* (\zeta^\vee)$ with the $\pi_{\rho_w}$ and the
additivity of $\zeta^\vee$ show that 
\[
HH_* (\pi_\rho) \circ HH_* (\zeta^\vee) = HH_* ( \zeta^\vee (\pi_\rho)) ,
\]
as required. The analogous statements for (periodic) cyclic homology can be proved in the 
same way, using Corollary \ref{cor:7.2}. $\qquad \Box$
\vspace{2mm}

In \cite[Theorem 4.4.2]{Sol-Irr} the author constructed a homomorphism of Fr\'echet algebras
\[
\zeta_0 : \mc S (X) \rtimes W' \to \mc S (\mc R,q) \rtimes \Gamma .
\]
It is related to Theorem \ref{thm:6.2} by \cite[Corollary 4.4.3]{Sol-Irr}: $\zeta^\vee (\pi)
\cong \pi \circ \zeta_0$ for all irreducible $\mc S (\mc R,q) \rtimes \Gamma$-representations. 
Furthermore it was shown in \cite[Theorems 5.1.4 and 5.2.1]{Sol-Irr} that $\zeta_0$ induces 
isomorphisms on topological $K$-theory and on periodic cyclic homology.
With Theorem \ref{thm:10.1} we can improve on this:

\begin{prop} \label{prop:10.2}
Let $q$ be positive.
\enuma{
\item $HH_* (\zeta_0) = HH_* (\zeta^\vee) : HH_* (\mc S (X) \rtimes W') \to
HH_* (\mc S (\mc R,q) \rtimes \Gamma )$.
\item There exists a natural commutative diagram
\[
\begin{array}{ccc}
HH_* (\C [X] \rtimes W') & \to & HH_* (\mc S (X) \rtimes W') \\
\downarrow \scs{HH_* (\zeta^\vee)} & & \downarrow \scs{HH_* (\zeta_0)} \\
HH_* (\mc H (\mc R,q) \rtimes \Gamma) & \to & HH_* (\mc S (\mc R,q) \rtimes \Gamma)
\end{array}
\]
in which the horizontal maps are induced by inclusions of algebras and the
vertical maps are isomorphisms.
\item The analogues of (a) and (b) for cyclic and periodic cyclic homology are
also valid.
}
\end{prop}
\emph{Proof.}
By \cite[Lemma 4.2.3 and Theorem 4.4.2.e]{Sol-Irr}
\[
\pi_\sigma (t) \circ \zeta_0 = \zeta^\vee (\pi_\sigma (t))
\]
for every tempered analytic family of $\mc H (\mc R,q) \rtimes \Gamma$-representations
$\{ \pi_\sigma (t) \mid t \in T^\sigma_{un} \}$. Thus (a) follows from the unicity part
of Theorem \ref{thm:10.1}.c. That and Theorem \ref{thm:10.1} directly imply (b) and (c).
$\qquad \Box$ \vspace{3mm}
