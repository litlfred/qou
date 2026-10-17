---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-010-32-volumes-of-angle-structures
section_title: "Volumes of angle structures"
section_number: 3.2
pages: 13-15
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.974
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:volume}

Recall (\cite{MilnorHypGeom}, for example) that the volume of an ideal hyperbolic tetrahedron, $T$, with dihedral angles $\theta_1$, $\theta_2$, and $\theta_3$ is given by
$$
V(T)=\lob(\theta_1)+\lob(\theta_2)+\lob(\theta_3),
$$
where the Lobachevsky function, $\lob$, is defined as
$$
\lob(x)=-\int_0^x\log|2\sin t|\,dt.
$$  
\begin{defn}\label{def:volume}
For a point $\theta\in\mathcal A(\tau)$, which specifies angles for the $n$ tetrahedra $T_i\in\tau$ and has all $\theta_i\in(0,\pi)$, define the \emph{volume associated to $\theta$}, $\mathcal{V}(\theta)$, by
$$
\mathcal V(\theta) =
\displaystyle{\sum_{i=1}^{n}V(T_i)}= \displaystyle{\sum_{i=1}^{3n}\lob(\theta_i)} 
$$
 and note that $\mathcal{V}(\theta)>0$ for $\theta\in\mathcal A(\tau)$.
\end{defn}

As summarized in~\cite{AngledtoHyperbolic}, $\lob$ is well-defined and continuous on $\R$.  Thus, the definition of~$\mathcal V$ can be extended to the closure of~$\mathcal A(\tau)$, which may include points with coordinates equal to 0 or $\pi$ where the integral itself is improper. If $\theta\in\overline{\mathcal A(\tau)}$, then $\mathcal{V}(\theta)\ge0$.

Straightforward tetrahedra-by-tetrahedra calculations show that for a positive angle structure $\theta$ and a tangent vector $\vec v\in T_\theta\mathcal{A}(\tau)$,
\begin{equation}
    \frac{\partial\mathcal{V}}{\partial \vec v}=\displaystyle{\sum_{i=1}^{3n} -v_i\log \sin \theta_i} \quad\text{ and }\quad\frac{\partial^2\mathcal{V}}{\partial \vec v\, ^2}<0.\label{eq:derivatives}
\end{equation}
See, for example, \cite[Lemma 5.3]{AngledtoHyperbolic}.

Because $\mathcal{V}$ is strictly concave down on~$\mathcal A(\tau)$, any critical point in $\mathcal{A}(\tau)$ is unique and an absolute maximum.  In fact, the first and second partials~\eqref{eq:derivatives} are enough to prove the same for a maximal point on the boundary. 

\begin{prop}\label{prop:maxunique}
Whenever $\mathcal{A}(\tau)\ne\emptyset$, the point at which the volume functional $\mathcal V: \overline{\mathcal A(\tau)}\rightarrow[0,\infty)$ attains its maximum is unique.
\end{prop}

\begin{proof}
If there is a critical point $\alpha$ in $\mathcal A(\tau)$, the strict concavity of $\mathcal{V}$ guarantees that $\alpha$ is unique and that $\mathcal{V}(\alpha)$ is the maximum volume.  If, on the other hand, there is no critical point on the interior, the compactness of $\overline{\mathcal A(\tau)}$ ensures that there is a point $\alpha\in\overline{\mathcal A(\tau)}-\mathcal A(\tau)$ with $\mathcal{V}(\alpha)$ maximal.  To show such an angle structure is unique, we first examine its coordinates.  Because $\alpha\notin\mathcal A(\tau)$, there is at least one tetrahedron in $\tau$ with an assigned angle of $0$ or $\pi$.  The maximality of $\alpha$ further constrains the angles of such a tetrahedron as noted in the following lemma.

\begin{lem}\label{lem:00pi}
When $\mathcal{V}(\alpha)$ is a maximum, any tetrahedron assigned an angle of $0$ or $\pi$ must have angles of $0$, $0$, and $\pi$ in some order. 
\end{lem}

\begin{proof}[Proof of Lemma~\ref{lem:00pi}]
By Condition~(2) of Definition~\ref{def:anglestructure}, the angles in a tetrahedron must sum to~$\pi$, so this statement is obviously true if one angle in a tetrahedron is assigned~$\pi$ or if two angles are assigned $0$. We now argue, as also noted in \cite[Proposition~7.1]{GwithF2Bridge} and~\cite[Proposition~7]{DehnFillings}, that  assigning exactly one $0$ angle contradicts the maximality of~$\alpha$. 

Consider, for example, a tetrahedron, $T_0\in\tau$, with nonnegative angles $0$, $\theta_0$, and $\pi-\theta_0$. For any $0<\lambda<1$, define a family of tetrahedra $T(t)|_{t\ge0}$ with angles $\theta_1=t$, $\theta_2=\theta_0-\lambda t$, and $\theta_3=\pi-(t+\theta_0-\lambda t)$, so $T(0)=T_0$ and, as $t$ increases, the angles of the tetrahedron change --- $\theta_1$ is increased, while $\theta_2$ and $\theta_3$ are decreased.  The first partial in~\eqref{eq:derivatives} restricted to this family of tetrahedra yields
$$
\frac{dV(T(t))}{dt}\Big|_{t=0^+}=\displaystyle{\sum_{i=1}^{3} -\frac{d\theta_i}{dt} \log \sin \theta_i}\Big|_{t=0^+}=+\infty.
$$
In other words, increasing the solitary $0$ angle by a small amount would increase $T_0$'s volume (and thus the total volume $\mathcal{V}$) by a much larger amount, violating the maximality of~$\alpha$.  Thus, if a maximal angle structure assigns any angles in $\{0,\pi\}$ to a tetrahedron, two of its angles are assigned $0$ and one~$\pi$, thus proving the lemma.  We call a tetrahedron with angles in $\{0,\pi\}$ \emph{flat} and observe that its volume is~$0$.
\end{proof}

Returning to the proof of Proposition~\ref{prop:maxunique}, we will use the constraints Lemma~\ref{lem:00pi} imposes on the coordinates of a maximal point $\alpha\in\overline{\mathcal A(\tau)}-\mathcal A(\tau)$ to prove that $\alpha$ is unique. Let $\beta$ be in $\overline{\mathcal A(\tau)}-\mathcal A(\tau)$ with $\mathcal{V}(\beta)=\mathcal{V}(\alpha)$ and let $\mu\in[0,\pi]^{3n}$ be the point whose coordinates are determined by averaging those of $\alpha$ and~$\beta$. Then $\mu\in\overline{\mathcal A(\tau)}$, because the set $\overline{\mathcal A(\tau)}$ is convex.  We will examine the volume of each tetrahedron $T$ under the angle structure assigned by~$\mu$ and will denote this volume by $\mathcal{V}(\mu|_T)$.

\begin{description}
    \item [Case 1] If $\alpha$ and $\beta$ assign the same angles to a tetrahedron $T$, then their average $\mu$ does as well, so $\mathcal{V}(\mu|_T)$ is equal to $\mathcal{V}(\alpha|_T)$ (and also $\mathcal{V}(\beta|_T)$).
    
    \item[Case 2] If $\alpha$ and $\beta$ assign different angles to a tetrahedron $T$ and both $\alpha|_T$ and $\beta|_T$ are flat, then, because $\alpha$ and $\beta$ are maximum points, the angles must be $0$, $0$, and $\pi$ (in different orders), and the coordinates of $\mu|_T$ are $0$, $\frac\pi2$, and $\frac\pi2$ in some order.  In this case, $\mathcal{V}(\mu|_T)$ equals $0$ just as $\mathcal{V}(\alpha|_T)$ and $\mathcal{V}(\beta|_{T})$ do.
    
    \item[Case 3] If $\alpha$ and $\beta$ assign different angles to a tetrahedron~$T$ and at least one of $\alpha|_T$ or $\beta|_T$ is not flat, we will argue that $\mathcal{V}(\mu|_T)$ is strictly greater than the average of $\mathcal{V}(\alpha|_T)$ and $\mathcal{V}(\beta|_T)$.  Without loss of generality suppose $\alpha|_T$ is not flat.  Define $\gamma(t)$ to be the line segment joining $\alpha|_T$ and~$\beta|_T$:
    $$
    \gamma(t)=t\alpha|_T + (1-t)\beta|_T \text{ for } t\in[0,1].
    $$
    Let $V(t)$ be the volume of the tetrahedron whose angles are given by $\gamma(t)$.  As a restriction of $\mathcal{V}$, the function $V$ is continuous on $[0,1]$.  Also, because $\alpha|_T$ is not flat, $\gamma$ is in $(0,\pi)^3$ for $0<t\le 1$, so $V$ is differentiable on $(0,1]$ and by the second partial in~\eqref{eq:derivatives}, $V^{\prime\prime}<0$.  Applying the Mean Value Theorem to $V$ yields points $c_1\in\left(0,\frac12\right)$ and $c_2\in\left(\frac12,1\right)$ with   
    \begin{align*}
        V^\prime(c_1)&=2\left(V\left(\textstyle{\frac12}\right)-V\left(0\right)\right)\\
        V^\prime(c_2)&=2\left(V\left(1\right)-V\left(\textstyle{\frac12}\right)\right)
    \end{align*}
    and negative second derivatives, so $V^\prime(c_1)>V^\prime(c_2)$, which means 
    \begin{equation*}
        2V\left(\textstyle{{\frac12}}\right)>V(1)+V(0).\footnote{If neither $\alpha|_T$ nor $\beta|_T$ is flat, this inequality follows immediately from the strict concavity of $V$.  We appeal to the Mean Value Theorem, because, in general, strict concavity does not extend to the boundary of $\mathcal A(\tau)$.}
    \end{equation*}
    Because $V\left(\textstyle{\frac12}\right)=\mathcal{V}(\mu|_T)$, $V(1)=\mathcal{V}(\alpha|_T)$, and $V(0)=\mathcal{V}(\beta|_T)$, this inequality implies $\mathcal{V}(\mu|_T)>\frac12(\mathcal{V}(\alpha|_T)+\mathcal{V}(\beta|_T))$.  
\end{description}

In all cases, the volume of a tetrahedron $T$ computed using $\mu$, the average of the angle structures, is greater than or equal to the average of the volumes of $T$ computed using the angle structures $\alpha$ and $\beta$, so summing the individual volumes over all tetrahedra in $\tau$ yields
$$
\mathcal{V}(\mu)\ge\textstyle{\frac12}(\mathcal{V}(\alpha)+\mathcal{V}(\beta))=\mathcal{V}(\alpha)
$$
with equality only when there are no tetrahedra in Case~3.  But $\mathcal{V}(\alpha)$ is the maximum volume, so $\mathcal{V}(\mu)\le\mathcal{V}(\alpha)$, meaning $\mathcal{V}(\mu)=\mathcal{V}(\alpha)$ and there are no Case~3 tetrahedra.  The
only way $\alpha$ and $\beta$ can assign different angles to a tetrahedron~$T$ is if $\alpha|_T$ and $\beta|_T$ are both flat (Case 2).  In this case,  $\mathcal{V}(\mu)=\mathcal{V}(\alpha)$, so $\mu$ is also maximal, but, as we have seen, the coordinates of $\mu|_T$ are $0$, $\frac\pi2$, and $\frac\pi2$, which is not allowed for maximal angle structures.  Therefore, $\alpha$ and $\beta$ cannot assign different angles to any of the tetrahedra and $\beta=\alpha$, which is the unique maximum point.
\end{proof}

Positive angle structures that maximize the total volume play an important role in the Casson-Rivin program.
