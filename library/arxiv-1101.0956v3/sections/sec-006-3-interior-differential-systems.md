---
doc_id: arxiv-1101.0956v3
doc_title: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES"
section_id: sec-006-3-interior-differential-systems
section_title: "Interior Differential Systems"
section_number: 3
pages: 21-23
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.96
doc_brief: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES — In this paper we present the category of generalized Lie algebroids."
---
Let $\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$ be an object of the category $\mathbf{GLA}$.

Let $\mathcal{AF}_{F}$ be a vector fibred $\left( n+p\right)$-atlas for the vector bundle $\left( F,\nu ,N\right)$ and let $\mathcal{AF}_{TM}$ be a vector fibred $\left( m+m\right)$-atlas for the vector bundle $\left(
TM,\tau _{M},M\right)$.

Let $\left( h^{\ast }F,h^{\ast }\nu ,M\right)$ be the pull-back vector bundle through $h.$

If $\left( U,\xi _{U}\right) \in \mathcal{AF}_{TM}$ and $\left(
V,s_{V}\right) \in \mathcal{AF}_{F}$ such that $U\cap h^{-1}\left( V\right)
\neq \phi$, then we define the application $$\begin{array}{ccc}
h^{\ast }\nu ^{-1}(U{\cap }h^{-1}(V))) & {}^{\underrightarrow{\bar{s}_{U{
\cap }h^{-1}(V)}}} & \left( U{\cap }h^{-1}(V)\right) {\times }\mathbb{R}^{p}
\\
\left( \varkappa ,z\left( h\left( \varkappa \right) \right) \right) &
\longmapsto & \left( \varkappa ,t_{V,h\left( \varkappa \right) }^{-1}z\left(
h\left( \varkappa \right) \right) \right).
\end{array}$$

**Proposition 3.1** *The set* $$\begin{array}{c}
\overline{\mathcal{AF}}_{F}\overset{put}{=}\underset{U\cap h^{-1}\left(
V\right) \neq \phi }{\underset{\left( U,\xi _{U}\right) \in \mathcal{AF}
_{TM},~\left( V,s_{V}\right) \in \mathcal{AF}_{F}}{\tbigcup }}\left\{ \left(
U\cap h^{-1}\left( V\right) ,\bar{s}_{U{\cap }h^{-1}(V)}\right) \right\}
\end{array}$$ *is a vector fibred* $m+p$*-atlas for the vector bundle* $\left(
h^{\ast }F,h^{\ast }\nu ,M\right) .$

*If* $z=z^{\alpha }t_{\alpha }\in \Gamma \left( F,\nu ,N\right) ,$ *then we obtain the section* $$\begin{array}{c}
Z=\left( z^{\alpha }\circ h\right) T_{\alpha }\in \Gamma \left( h^{\ast
}F,h^{\ast }\nu ,M\right)
\end{array}$$ *such that* $Z\left( x\right) =z\left( h\left( x\right) \right) ,$ *for any* $x\in U\cap h^{-1}\left( V\right) .$

**Theorem 3.1** *Let* $\Big({\overset{h^{\ast }F}{\rho }},Id_{M}
\Big)$ *be the* $\mathbf{B}^{\mathbf{v}}$*-morphism of* $\left(
h^{\ast }F,h^{\ast }\nu ,M\right)$ *source and* $\left( TM,\tau
_{M},M\right)$ *target, where* $$\begin{array}{rcl}
h^{\ast }F & ^{\underrightarrow{\overset{h^{\ast }F}{\rho }}} & TM \\
\displaystyle Z^{\alpha }T_{\alpha }\left( x\right) & \longmapsto & 
\displaystyle\left( Z^{\alpha }\cdot \rho _{\alpha }^{i}\circ h\right) \frac{
\partial }{\partial x^{i}}\left( x\right)
\end{array}
\leqno(3.1)$$

*Using the operation* $$\begin{array}{ccc}
\Gamma \left( h^{\ast }F,h^{\ast }\nu ,M\right) \times \Gamma \left( h^{\ast
}F,h^{\ast }\nu ,M\right) & ^{\underrightarrow{~\ \ \left[ ,\right]
_{h^{\ast }F}~\ \ }} & \Gamma \left( h^{\ast }F,h^{\ast }\nu ,M\right)
\end{array}$$ *defined by* $$\begin{array}{ll}
\left[ T_{\alpha },T_{\beta }\right] _{h^{\ast }F} & =\left( L_{\alpha \beta
}^{\gamma }\circ h\right) T_{\gamma },\vspace*{1mm} \\
\left[ T_{\alpha },fT_{\beta }\right] _{h^{\ast }F} & \displaystyle=f\left(
L_{\alpha \beta }^{\gamma }\circ h\right) T_{\gamma }+\left( \rho _{\alpha
}^{i}\circ h\right) \frac{\partial f}{\partial x^{i}}T_{\beta },\vspace*{1mm}
\\
\left[ fT_{\alpha },T_{\beta }\right] _{h^{\ast }F} & =-\left[ T_{\beta
},fT_{\alpha }\right] _{h^{\ast }F},
\end{array}
\leqno(3.2)$$ *for any* $f\in \mathcal{F}\left( M\right) ,$ *it results that* $$\begin{array}{c}
\left( \left( h^{\ast }F,h^{\ast }\nu ,M\right) ,\left[ ,\right] _{h^{\ast
}F},\left( \overset{h^{\ast }F}{\rho },Id_{M}\right) \right)
\end{array}$$ is a Lie algebroid which is called *the pull-back Lie algebroid of the generalized Lie algebroid* $\left( \left( F,\nu ,N\right) ,\left[ ,\right]
_{F,h},\left( \rho ,\eta \right) \right) .$

**Definition 3.1** Any vector subbundle $\left( E,\pi ,M\right)$ of the pull-back vector bundle $\left( h^{\ast }F,h^{\ast }\nu ,M\right)$ will be called *interior differential system (IDS) of the generalized Lie algebroid* $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right) .$$

In particular, if $h=Id_{N}=\eta$, then we obtain the definition of the IDS of a Lie algebroid. (see $\left[ {2}\right]$)

*Remark 3.1* If $\left( E,\pi ,M\right)$ is an IDS of the generalized Lie algebroid $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right) ,$$ then we obtain a vector subbundle $\left( E^{0},\pi ^{0},M\right)$ of the vector bundle $\left( \overset{\ast }{h^{\ast }F},\overset{\ast }{h^{\ast
}\nu },M\right)$ such that $$\Gamma \left( E^{0},\pi ^{0},M\right) \overset{put}{=}\left\{ \Omega \in
\Gamma \left( \overset{\ast }{h^{\ast }F},\overset{\ast }{h^{\ast }\nu }
,M\right) :\Omega \left( S\right) =0,~\forall S\in \Gamma \left( E,\pi
,M\right) \right\} .$$

The vector subbundle $\left( E^{0},\pi ^{0},M\right)$ will be called *the annihilator vector subbundle of the IDS* $\left( E,\pi ,M\right) .$

**Proposition 3.1** *If* $\left( E,\pi ,M\right)$* is an IDS of the generalized Lie algebroid* $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ *such that* $\Gamma \left( E,\pi ,M\right) =\left\langle
S_{1},...,S_{r}\right\rangle$*, then it exists* $\Theta
^{r+1},...,\Theta ^{p}\in \Gamma \left( \overset{\ast }{h^{\ast }F},\overset{
\ast }{h^{\ast }\nu },M\right)$* linearly independent such that* $\Gamma \left( E^{0},\pi ^{0},M\right) =\left\langle \Theta ^{r+1},...,\Theta
^{p}\right\rangle .$

**Definition 3.2** The IDS $\left( E,\pi ,M\right)$ of the generalized Lie algebroid $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ will be called *involutive* if $\left[ S,T\right] _{h^{\ast }F}\in
\Gamma \left( E,\pi ,M\right) ,~$for any $S,T\in \Gamma \left( E,\pi
,M\right) .$

**Proposition 3.2** *If* $\left( E,\pi ,M\right)$* is an IDS of the generalized Lie algebroid* $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ *and* $\left\{ S_{1},...,S_{r}\right\}$* is a base for the* $\mathcal{F}\left( M\right)$*-submodule* $\left( \Gamma \left( E,\pi
,M\right) ,+,\cdot \right)$* then* $\left( E,\pi ,M\right)$* is involutive if and only if* $\left[ S_{a},S_{b}\right] _{h^{\ast }F}\in
\Gamma \left( E,\pi ,M\right) ,~$for any $a,b\in \overline{1,r}.$
