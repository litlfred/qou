---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT"
section_id: sec-014-33-overview-of-the-computations
section_title: "Overview of the computations."
section_number: 3.3
pages: 13-16
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.98
doc_brief: "CHARACTER VARIETIES FOR SL(3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
Theoretically, the theorem could be proven using a prime decomposition of the ideal 
$$I_D=\langle L_{e} \cup L_{f}\cup L_{c} \rangle.$$
Indeed, as $\mathrm{Defor}(M, \mathcal T)$ is the zeroes set of this ideal, a prime decomposition would give the three components and we would be able to check their properties.
However, our system depends on $12n$ variables (24 variables in the
case of the figure eight knot complement) and is of rather high degree
(degree $6$ for some equations for the figure eight knot complement). So we are far beyond the scope of the state of the art algorithms of prime decomposition.

We will use the shape of the equations to simplify the system. The method we present is rather general for this kind of systems up to some points (number of factors
in some polynomials). It could be applied, in principle on numerous systems
with the same properties. For example, it can replace the one used in \cite{FKR14}.
Before explaining our method, let us define one more object: \emph{forbidden points}. 

Denote by $S_{D}=L_{e} \cup L_{f}\cup L_{c}$ the set of polynomials generating the ideal $I_{D}$.
Note that if $z \in V ( I_{D} )\subset \bC^{12n}$, then none of its coordinates
  belong to $\{ 1,0 \}$ \ because of the equations induced by the
  {\emph{internal relations}} $L_c$. We hence call {\tmem{forbidden
  points}} the points with any coordinate in $\{ 0,1 \}$ and we introduce 
  $F_{D}= \{ z,z-1,z \in Z \} \subset \mathbb{Q} [ Z ]$. It may seem useless at this point as this is contained in the internal relations.
  But recall that we will eliminate a lot of variables through projections. During these projections, as said before, some spurious components (i.e. all included in forbidden points) may appear. So we will always keep the equations defining the forbidden points and saturate our ideals by these equations. This will lower the number of components and ease the computations.
  
 Here are the steps of our method: 
 
  \begin{itemize}
\item {\bf Step A: elimination.} 
We iteratively detect equations in $S_{D}$ which are affine in a variable, i.e.  of the form 
$$D_{z} ( X )  z_{} -N_{z} ( X )\textrm{ with }X \subset Z \setminus \{ z \},$$ 
and with the additional condition that $D_{z} ( X )$
  cancels only at forbidden points. We can then substitute $z$ by $\frac{N_{z} ( X )}{D_{z}
  ( X )}$ in the other polynomials generating $I_{D}$, take the numerators of
  these equations and remove their factors (algorithm [$\gamma$]) that cancel
  exclusively at forbidden points (and thus never cancel on $\tmop{Defor} ( M,
  \mathcal{T} )$). This gives a new ideal with one less variable and one less equation.
  
At the end of the process, denote by $S_{Y} \subset \mathbb{Q} [ Y ]$ with $Y \subset Z$ the
  remaining equations. We keep in mind, through the set $R_{Y}
  \subset \mathbb{Q} [ Z ]$, the equations used for the substitutions. Of course, by substituting in $R_Y$, we may assume that all these equations express a substituted variable in terms of the variables in $Y$, i.e. they have the form: $D_{z} ( Y ) z-N_{z} ( Y )$, with $z
  \in Z \setminus Y$.
  
We also want to keep in mind the forbidden points. So denote by $F_{Y} \in \mathbb{Q} [ Y ]$
 the list of prime factors that appear in $F_{D}$ after having performed the same substitution.
  
We can interpret the relations $R_{Y} =0$ as a projection $\pi_{Y} : \tmop{Defor} (
  M, \mathcal{T} ) \rightarrow V ( \langle S_{Y} \rangle )$ which is not
  necessarily surjective. However, the complement of the image $V ( \langle S_{Y}
  \rangle ) \setminus \pi_{Y} ( \tmop{Defor} ( M, \mathcal{T} ) )$ only contains
  forbidden points which might have been introduced by the use of
  rational fractions in the substitutions.
  
  So we compute (algorithm $[ \beta ]$) the ideal $I_{Y}$, which is the saturation of $\langle S_{Y}  \rangle$ by $F_{Y}$ in order to get $V ( I_{Y} ) = \overline{\pi_{Y} (
  \tmop{Defor} )}$. The union of the zeroes of the polynomials $F_{Y}$ defines
  the {\tmem{forbidden points}} of $V ( I_{Y} )$ which are images by $\pi_{Y}$
  of the forbidden points of $\mathbb{C}^{12n}$.
  
Putting this in a diagram, we have :
\begin{center}
  \begin{tabular}{ccc}
    $\mathbb{C}^{12n}$ & $\rightarrow$ & $\mathbb{C}^{\sharp Y}$\\
    $\tmop{Defor} ( M, \mathcal{T} )$ & $\approx_{\pi_{Y}}$ & $V ( I_{Y} )
    \setminus ( \cup_{f \in F_{Y}} V ( f ) )$\\
    $( x,y )$ & $\rightarrow$ & $y$\\
    $\left( \frac{N_{x} ( y )}{D_{x} ( y )} ,y \right)$ & $\leftarrow$ & $y.$
  \end{tabular}
\end{center}
  \item {\bf Step B: splitting.} In $I_{Y}$, we find a polynomial
  $P_{Y} \in \mathbb{Q} [ Y ]$ that factorizes (algorithm [$\gamma$]) into
  $k$ factors in $\mathbb{Q} [ Y ]$ : $P_{Y} = \prod_{i=1 \ldots k} P_{Y,i}$.
  
  By construction, as $\tmop{Defor} ( M, \mathcal{T} )$ does not contain
  forbidden points, we then get $\tmop{Defor} ( M, \mathcal{T} ) = \cup_{i=1
  \ldots k} V ( J_{Y,i} )$, where $J_{Y,i} \subset \mathbb{Q} [ Z ]$ is the
  saturation of $I_{D} + \langle P_{Y,i} \rangle$ by $F_{D}$.
  
  We can even further saturate our ideals, in order to avoid the same component appearing twice. We  perform cascading
  saturations  for some permutation $\sigma$ of the indices: we iteratively compute
  (algorithm $[ \beta ]$)  the ideal $I_{Y, \sigma ( i )} =I_{Y} + \langle
  P_{Y, \sigma ( i )} \rangle$ and saturate this ideal by $F_{Y}$ as well as
  with $\{ P_{Y, \sigma ( 1 )} , \ldots ,P_{Y, \sigma ( i-1 )} \}$ \ in order
  to remove possible components that are already in $I_{Y, \sigma ( 1 )} ,
  \ldots ,I_{Y, \sigma ( i-1 )}$. The efficiency of the process strongly
  depends on the chosen permutation.
  
At the end of this step, one can set $D_{i} =V ( I_{Y,i} +I_{D} )$. By construction, $D_i$ is the inverse image by $\pi_i$ of the zeroes set of $I_{Y,i}$. And we get the decomposition: 
$$\tmop{Defor} ( M,
  \mathcal{T} ) = \cup_{i=1 \ldots k} D_{i}.$$
  
  \item {\bf Step C: further elimination.} The ideals $I_{Y,i}$ are still too big to perform 
  directly a prime decomposition. So, for each $I_{Y,i}$, we apply once again step A. We may 
  even try to iteratively apply Steps A and B and so on, but in our case, a single additional 
  pass of Step A turns out to be enough. So we explain only this single pass.
  
  Indeed, for each $I_{Y,i}$, we find a polynomial that is affine in
  one of the variables and, moreover, can be written $a_{i} ( z ) y+b_{i} ( z
  )$ with $z \in Y_{i} =Y \setminus \{ y \}$ and $a_{i} ( z^{} )$ only vanishing at forbidden points. We stress that 
  the suitable variable $y$ to eliminate depends on the different ideals $I_{Y,i}$.
  
  The result of Step A is then an ideal $I_{Y_{i}} \subset \mathbb{Q}
  [ Y_{i} ]$ together with a projection $\pi_{Y_{i}} :V ( I_{Y,i} ) \rightarrow V (
  I_{Y_{i}} )$ and a set of polynomials
  $F_{Y_{i}}$ (defining the {\tmem{forbidden points}} of $V ( I_{Y_{i}} )$)
  such that we get: $$\overline{\pi_{Y_{i}} ( V ( I_{Y,i} ) )} =V ( I_{Y_{i}} ).$$
  
  Setting $\pi_{i} = \pi_{Y_{i}} \circ \pi_{Y}$, we may write
  $\overline{\pi_{i} ( D_{i} )} =V ( I_{Y_{i}} )$ and get the diagram similar to the previous 
  one:
 
\begin{center}
    \begin{tabular}{ccc}
      $\mathbb{C}^{12n}$ & $\rightarrow$ & $\mathbb{C}^{\sharp Y-1}$ \\

      $D_{i}$ & $\approx_{\pi_{Y_i}}$ & $V ( I_{Y_i} ) \setminus ( \cup_{f \in
      F_{Y_i}} V ( f ) )$ \\







    \end{tabular}
\end{center}




















Beware that the different projections $\pi_{Y_i}$ are only defined on their respective component $D_i$ and do not land in the same space, as the last eliminated variable may differ for different components.
  
  \item {\bf Step D: Prime decomposition.} At this stage, each ideal $I_{Y_{i}}$ belongs to 
  the scope of a Prime Decomposition algorithm (named here algorithm [$\eta$]). Doing so, we 
  extract the $\mathbb{Q}$-irreducible components or just a check that the $I_{Y_{i}}$ 
  is prime. We denote by $I_{Y_i,k}$ the different prime ideals appearing in the decomposition of $I_{Y_i}$. 
\end{itemize}


The Steps $A$ to $D$ are general functions that also have been applied
for other computations, for example for computing unipotent solutions for many
cases of varieties with a triangulation involving up to $4$ tetrahedra (\cite{FKR14}).

At this point, we have a decomposition of $\mathrm{Defor}(M,\mathcal T)$ in components, for which we have a prime decomposition. Proving the theorem for this decomposition is now just a matter of checking properties and here the method is very specific to the figure eight knot complement. Other manifolds $M$ may give other behaviors. In particular, it turns out in our case that, at this step, each ideal $I_{Y_i}$ has a component principal and prime and maybe another component of lesser dimension and which is redundant:
\begin{itemize}
  \item {\bf Specific Step $1$: irreducibility and smoothness} Check that for each $i$ there is a unique prime ideal of maximal dimension among the prime factors. We denote here by $I_{Y_i,1}$ this prime factor. Check that $\mathrm{Defor}(M,\mathcal T)$ is included in the union of the $\pi_i^{-1}(I_{Y_i,1})$. In other terms, the components of lesser dimension are redundant. Then check that each $I_{Y_{i} ,1} \subset \mathbb{Q} [ Y_{i} ]$ is  a  principal ideal of $\mathbb{Q} [ Y_{i} ]$ (the output of algorithm
  [$\alpha$] is a unique polynomial), and, if so, denote by $H_{i} \in
  \mathbb{Q} [ Y_{i} ]$ its generator.
  
  Eventually verify (algorithm [$\gamma$]) that $H_{i}$ is irreducible in
  $\mathbb{C} [ Y_{i} ]$ and check that the singular points of each $H_{i}$
  are exclusively forbidden points.
  
  \item {\bf Specific Step $2$: connectedness.} Let $I_{i}$ be the ideal generated by $I_{Y_i,1}$ and $I_D$. It verifies that $V ( I_{i} ) =D_{i}$. We compute (algorithm [$\alpha$]) the ideal $I_{1} + \ldots +I_{k}$. And we check if is not trivial.
\end{itemize}
If the results of these two specific steps are indeed what is announced, then the theorem is easily proven: $\pi_{i} ( D_{i} )$ is a dense open
  set in $V ( H_{i} )$ which is a smooth affine (irreducible) variety so that
  $\pi_{i} ( D_{i} )$ and thus $D_{i}$ are smooth and connected. Moreover,  as the ideal $I_{1} + \ldots +I_{k}$ is not trivial, we get that $D_{1} \cap \ldots \cap D_{k}$ is a non empty 
  set of points. As each $D_i$ is connected, we conclude that $\tmop{Defor} ( M, \mathcal{T} ) = \cup_{i=1 \ldots k} D_{i}$ is connected.
