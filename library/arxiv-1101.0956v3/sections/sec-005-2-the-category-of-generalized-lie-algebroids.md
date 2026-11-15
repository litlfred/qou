---
doc_id: arxiv-1101.0956v3
doc_title: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES"
section_id: sec-005-2-the-category-of-generalized-lie-algebroids
section_title: "The category of generalized Lie algebroids"
section_number: 2
pages: 18-21
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.987
doc_brief: "ALGEBRAIC CONSTRUCTIONS IN THE CATEGORY OF VECTOR BUNDLES — In this paper we present the category of generalized Lie algebroids."
---
In general, if $\mathcal{C}$ is a category, then we denote $\left\vert
\mathcal{C}\right\vert$ the class of objects and for any $A,B{\in }
\left\vert \mathcal{C}\right\vert$, we denote $\mathcal{C}\left( A,B\right)$ the set of morphisms of $A$ source and $B$ target. Let$\mathbf{~Vect},$ $\mathbf{Liealg},~\mathbf{Mod}$**,** $\mathbf{Man}$ and $\mathbf{B}^{
\mathbf{v}}$ be the category of real vector spaces, Lie algebras, modules, manifolds and vector bundles respectively.

We know that if $\left( E,\pi ,M\right) \in \left\vert \mathbf{B}^{\mathbf{v}
}\right\vert ,$ $\Gamma \left( E,\pi ,M\right) =\left\{ u\in \mathbf{Man}
\left( M,E\right) :u\circ \pi =Id_{M}\right\}$ and $\mathcal{F}\left(
M\right) =\mathbf{Man}\left( M,\mathbb{R}\right) ,$ then $\left( \Gamma
\left( E,\pi ,M\right) ,+,\cdot \right)$ is a $\mathcal{F}\left( M\right)$ -module. If  $\left( \varphi ,\varphi _{0}\right) \in \mathbf{B}^{\mathbf{v}
}\left( \left( E,\pi ,M\right) ,\left( E^{\prime },\pi ^{\prime },M^{\prime
}\right) \right)$ such that $\varphi _{0}\in Iso_{\mathbf{Man}}\left(
M,M^{\prime }\right) ,$ then, using the operation $$\begin{array}{ccc}
\mathcal{F}\left( M\right) \times \Gamma \left( E^{\prime },\pi ^{\prime
},M^{\prime }\right) & ^{\underrightarrow{~\ \ \cdot ~\ \ }} & \Gamma \left(
E^{\prime },\pi ^{\prime },M^{\prime }\right) \\
\left( f,u^{\prime }\right) & \longmapsto & f\circ \varphi _{0}^{-1}\cdot
u^{\prime }
\end{array}$$ it results that $\left( \Gamma \left( E^{\prime },\pi ^{\prime },M^{\prime
}\right) ,+,\cdot \right)$ is a $\mathcal{F}\left( M\right)$-module and we obtain the $\mathbf{Mod}$-morphism $$\begin{array}{ccc}
\Gamma \left( E,\pi ,M\right) & ^{\underrightarrow{~\ \ \Gamma \left(
\varphi ,\varphi _{0}\right) ~\ \ }} & \Gamma \left( E^{\prime },\pi
^{\prime },M^{\prime }\right) \\
u & \longmapsto & \Gamma \left( \varphi ,\varphi _{0}\right) u
\end{array}$$ defined by $$\begin{array}{c}
\Gamma \left( \varphi ,\varphi _{0}\right) u\left( y\right) =\varphi \left(
u_{\varphi _{0}^{-1}\left( y\right) }\right) ,
\end{array}$$ for any $y\in M^{\prime }.$

We know that a Lie algebroid is a vector bundle $\left( F,\nu ,N\right) \in
\left\vert \mathbf{B}^{\mathbf{v}}\right\vert$ such that there exists $$\begin{array}{c}
\left( \rho ,Id_{N}\right) \in \mathbf{B}^{\mathbf{v}}\left( \left( F,\nu
,N\right) ,\left( TN,\tau _{N},N\right) \right)
\end{array}$$ and an operation $$\begin{array}{ccc}
\Gamma \left( F,\nu ,N\right) \times \Gamma \left( F,\nu ,N\right) & ^{
\underrightarrow{\,\left[ ,\right] _{F}\,}} & \Gamma \left( F,\nu ,N\right)
\\
\left( u,v\right) & \longmapsto & \left[ u,v\right] _{F}
\end{array}$$ with the following properties:

-   the equality holds good $$\begin{array}{c}
    \left[ u,f\cdot v\right] _{F}=f\left[ u,v\right] _{F}+\Gamma \left( \rho
    ,Id_{N}\right) \left( u\right) f\cdot v,
    \end{array}$$ for all $u,v\in \Gamma \left( F,\nu ,N\right)$ and $f\in \mathcal{F}\left(
    N\right) ,$

-   the $4$-tuple $\left( \Gamma \left( F,\nu ,N\right)
    ,+,\cdot ,\left[ ,\right] _{F}\right)$ is a Lie $\mathcal{F}\left( N\right)$-algebra$,$

-   the $\mathbf{Mod}$-morphism $\Gamma \left( \rho
    ,Id_{N}\right)$ is a $\mathbf{LieAlg}$-morphism of $\left( \Gamma \left(
    F,\nu ,N\right) ,+,\cdot ,\left[ ,\right] _{F}\right)$ source and $\left(
    \Gamma \left( TN,\tau _{N},N\right) ,+,\cdot ,\left[ ,\right] _{TN}\right)$ target.

**Definition 2.1** Let $M,N\in \left\vert \mathbf{Man}\right\vert ,$ $h\in Iso_{\mathbf{Man}}\left( M,N\right)$ and $\eta \in Iso_{\mathbf{Man}
}\left( N,M\right)$.

If $\left( F,\nu ,N\right) \in \left\vert \mathbf{B}^{\mathbf{v}}\right\vert$ so that there exists $$\begin{array}{c}
\left( \rho ,\eta \right) \in \mathbf{B}^{\mathbf{v}}\left( \left( F,\nu
,N\right) ,\left( TM,\tau _{M},M\right) \right)
\end{array}$$ and an operation $$\begin{array}{ccc}
\Gamma \left( F,\nu ,N\right) \times \Gamma \left( F,\nu ,N\right) & ^{
\underrightarrow{\left[ ,\right] _{F,h}}} & \Gamma \left( F,\nu ,N\right) \\
\left( u,v\right) & \longmapsto & \left[ u,v\right] _{F,h}
\end{array}$$ with the following properties:

$\qquad GLA_{1}$. the equality holds good $$\begin{array}{c}
\left[ u,f\cdot v\right] _{F,h}=f\left[ u,v\right] _{F,h}+\Gamma \left(
Th\circ \rho ,h\circ \eta \right) \left( u\right) f\cdot v,
\end{array}$$   for all $u,v\in \Gamma \left( F,\nu ,N\right)$ and $f\in
\mathcal{F}\left( N\right) .$

$GLA_{2}$. the $4$-tuple $\left( \Gamma \left( F,\nu ,N\right)
,+,\cdot ,\left[ ,\right] _{F,h}\right)$ is a Lie $\mathcal{F}\left(
N\right)$-algebra,

$GLA_{3}$. the $\mathbf{Mod}$-morphism $\Gamma \left( Th\circ \rho ,h\circ
\eta \right)$ is a $\mathbf{LieAlg}$-morphism of $$\left( \Gamma \left( F,\nu ,N\right) ,+,\cdot ,\left[ ,\right] _{F,h}\right)$$ source and $$\left( \Gamma \left( TN,\tau _{N},N\right) ,+,\cdot ,\left[ ,\right]
_{TN}\right)$$ target, then we will say that *the triple* $\left(
\left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta \right)
\right)$ *is a generalized Lie algebroid.* The couple $\left( \left[ ,
\right] _{F,h},\left( \rho ,\eta \right) \right)$ will be called *generalized Lie algebroid structure.*

**Definition 2.2** We define the set of morphisms of $$\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$$ source and $$\left( \left( F^{\prime },\nu ^{\prime },N^{\prime }\right) ,\left[ ,\right]
_{F^{\prime },h^{\prime }},\left( \rho ^{\prime },\eta ^{\prime }\right)
\right)$$ target as being the set $$\begin{array}{c}
\left\{ \left( \varphi ,\varphi _{0}\right) \in \mathbf{B}^{\mathbf{v}
}\left( \left( F,\nu ,N\right) ,\left( F^{\prime },\nu ^{\prime },N^{\prime
}\right) \right) \right\}
\end{array}$$ such that $\varphi _{0}\in Iso_{\mathbf{Man}}\left( N,N^{\prime }\right)$ and the $\mathbf{Mod}$-morphism $\Gamma \left( \varphi ,\varphi _{0}\right)$ is a $\mathbf{LieAlg}$-morphism of $$\left( \Gamma \left( F,\nu ,N\right) ,+,\cdot ,\left[ ,\right] _{F,h}\right)$$ source and $$\left( \Gamma \left( F^{\prime },\nu ^{\prime },N^{\prime }\right) ,+,\cdot
, \left[ ,\right] _{F^{\prime },h^{\prime }}\right)$$ target.

So, we can discuss about *the category* $\mathbf{GLA}$* of generalized Lie algebroids.* Examples of objects of this category are presented in the paper $\left[ 1\right] .$ We remark that $\mathbf{GLA}$ is a subcategory of the category $\mathbf{B}^{\mathbf{v}}.$

Let $\left( \left( F,\nu ,N\right) ,\left[ ,\right] _{F,h},\left( \rho ,\eta
\right) \right)$ be an arbitrary object of the category $\mathbf{GLA}$.

-   Locally, for any $\alpha ,\beta \in \overline{1,p},$ we set $\left[
    t_{\alpha },t_{\beta }\right] _{F,h}=L_{\alpha \beta }^{\gamma }t_{\gamma }.$ We easily obtain that $L_{\alpha \beta }^{\gamma }=-L_{\beta \alpha
    }^{\gamma },~$for any $\alpha ,\beta ,\gamma \in \overline{1,p}.$

The real local functions $L_{\alpha \beta }^{\gamma },~\alpha ,\beta ,\gamma
\in \overline{1,p}$ will be called the *structure functions of the generalized Lie algebroid* $\left( \left( F,\nu ,N\right) ,\left[ ,\right]
_{F,h},\left( \rho ,\eta \right) \right) .$

-   We assume the following diagrams: $$\begin{array}[b]{ccccc}
    F & ^{\underrightarrow{~\ \ \ \rho ~\ \ }} & TM & ^{\underrightarrow{~\ \ \
    Th~\ \ }} & TN \\
    ~\downarrow \nu &  & ~\ \ \ \downarrow \tau _{M} &  & ~\ \ \ \downarrow \tau
    _{N} \\
    N & ^{\underrightarrow{~\ \ \ \eta ~\ \ }} & M & ^{\underrightarrow{~\ \ \
    h~\ \ }} & N \\
    &  &  &  &  \\
    \left( \chi ^{\tilde{\imath}},z^{\alpha }\right) &  & \left(
    x^{i},y^{i}\right) &  & \left( \chi ^{\tilde{\imath}},z^{\tilde{\imath}
    }\right)
    \end{array}$$

    where $i,\tilde{\imath}\in \overline{1,m}$ and $\alpha \in \overline{1,p}.$

    If $$\left( \chi ^{\tilde{\imath}},z^{\alpha }\right) \longrightarrow \left( \chi
    ^{\tilde{\imath}\prime }\left( \chi ^{\tilde{\imath}}\right) ,z^{\alpha
    \prime }\left( \chi ^{\tilde{\imath}},z^{\alpha }\right) \right) ,$$ $$\left( x^{i},y^{i}\right) \longrightarrow \left( x^{i


    {\acute{}}

    }\left( x^{i}\right) ,y^{i


    {\acute{}}

    }\left( x^{i},y^{i}\right) \right)$$ and $$\left( \chi ^{\tilde{\imath}},z^{\tilde{\imath}}\right) \longrightarrow
    \left( \chi ^{\tilde{\imath}\prime }\left( \chi ^{\tilde{\imath}}\right) ,z^{
    \tilde{\imath}\prime }\left( \chi ^{\tilde{\imath}},z^{\tilde{\imath}
    }\right) \right) ,$$ then $$\begin{array}[b]{c}
    z^{\alpha


    {\acute{}}

    }=\Lambda _{\alpha }^{\alpha


    {\acute{}}

    }z^{\alpha }
    \end{array}
    ,$$ $$\begin{array}[b]{c}
    y^{i


    {\acute{}}

    }=\frac{\partial x^{i


    {\acute{}}

    }}{\partial x^{i}}y^{i}
    \end{array}$$ and $$\begin{array}{c}
    z^{\tilde{\imath}\prime }=\frac{\partial \chi ^{\tilde{\imath}\prime }}{
    \partial \chi ^{\tilde{\imath}}}z^{\tilde{\imath}}.
    \end{array}$$

-   We assume that $\left( \theta ,\mu \right) \overset{put}{=}\left(
    Th\circ \rho ,h\circ \eta \right)$. If $z^{\alpha }t_{\alpha }\in \Gamma
    \left( F,\nu ,N\right)$ is arbitrary, then $$\begin{array}[t]{l}
    \displaystyle
    \begin{array}{c}
    \Gamma \left( Th\circ \rho ,h\circ \eta \right) \left( z^{\alpha }t_{\alpha
    }\right) f\left( h\circ \eta \left( \varkappa \right) \right) =\vspace*{1mm}
    \\
    =\left( \theta _{\alpha }^{\tilde{\imath}}z^{\alpha }\frac{\partial f}{
    \partial \varkappa ^{\tilde{\imath}}}\right) \left( h\circ \eta \left(
    \varkappa \right) \right) =\left( \left( \rho _{\alpha }^{i}\circ h\right)
    \left( z^{\alpha }\circ h\right) \frac{\partial f\circ h}{\partial x^{i}}
    \right) \left( \eta \left( \varkappa \right) \right) ,
    \end{array}
    \end{array}
    \leqno(2.1)$$ for any $f\in \mathcal{F}\left( N\right)$ and $\varkappa \in N.$

The coefficients $\rho _{\alpha }^{i}$ respectively $\theta _{\alpha }^{
\tilde{\imath}}$ change to $\rho _{\alpha


{\acute{}}

}^{i


{\acute{}}

}$ respectively $\theta _{\alpha


{\acute{}}

}^{\tilde{\imath}


{\acute{}}

}$ according to the rule: $$\begin{array}{c}
\rho _{\alpha


{\acute{}}

}^{i


{\acute{}}

}=\Lambda _{\alpha


{\acute{}}

}^{\alpha }\rho _{\alpha }^{i}\displaystyle\frac{\partial x^{i


{\acute{}}

}}{\partial x^{i}},
\end{array}
\leqno(2.2)$$ respectively $$\begin{array}{c}
\theta _{\alpha


{\acute{}}

}^{\tilde{\imath}


{\acute{}}

}=\Lambda _{\alpha


{\acute{}}

}^{\alpha }\theta _{\alpha }^{\tilde{\imath}}\displaystyle\frac{\partial
\varkappa ^{\tilde{\imath}


{\acute{}}

}}{\partial \varkappa ^{\tilde{\imath}}},
\end{array}
\leqno(2.3)$$ where $$\left\Vert \Lambda _{\alpha


{\acute{}}

}^{\alpha }\right\Vert =\left\Vert \Lambda _{\alpha }^{\alpha


{\acute{}}

}\right\Vert ^{-1}.$$

*Remark 2.1* *The following equalities hold good:* $$\begin{array}{c}
\displaystyle\rho _{\alpha }^{i}\circ h\frac{\partial f\circ h}{\partial
x^{i}}=\left( \theta _{\alpha }^{\tilde{\imath}}\frac{\partial f}{\partial
\varkappa ^{\tilde{\imath}}}\right) \circ h,\forall f\in \mathcal{F}\left(
N\right) .
\end{array}
\leqno(2.4)$$ *and* $$\begin{array}{c}
\displaystyle\left( L_{\alpha \beta }^{\gamma }\circ h\right) \left( \rho
_{\gamma }^{k}\circ h\right) =\left( \rho _{\alpha }^{i}\circ h\right) \frac{
\partial \left( \rho _{\beta }^{k}\circ h\right) }{\partial x^{i}}-\left(
\rho _{\beta }^{j}\circ h\right) \frac{\partial \left( \rho _{\alpha
}^{k}\circ h\right) }{\partial x^{j}}.
\end{array}
\leqno(2.5)$$
