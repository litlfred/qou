---
doc_id: arxiv-q-alg-9504020v1
doc_title: "A link invariant from quantum dilogarithm"
section_id: sec-003-4-three-dimensional-description
section_title: "Three-Dimensional Description"
section_number: 4
pages: 5-9
source_pdf: 9504020v1.pdf
source_sha256: 0baef40fa9934c91
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.99
doc_brief: "A link invariant from quantum dilogarithm — The link invariant, arising from the cyclic quantum dilogarithm via the particular R-matrix construction, is proved to coincide with the invariant of"
---
[]{#sec3 label="sec3"}

In this section we establish the connection of the link invariant constructed in Sect. [\[sec2\]](#sec2){reference-type="ref" reference="sec2"} with the invariant of triangulated links of [@K], related in turn to cyclic quantum dilogarithm [@FK]. First, remind the necessary formulas from [@K] in slightly different notations.

We will assume that the integer $N$ is odd, and the square root of $\omega$ will be thought to be taken as an $N$-th root of unity: $$\omega^{1/2}=\omega^{(N+1)/2}.$$ For complex $x,y,z$, satisfying the Fermat equation $$x^N+y^N=z^N,\label{Fermat}$$ and integers $m,n$ define the function $$w(x,y,z|m,n)=w(x,y,z|m-n)\omega^{n^2/2},$$ where $$w(x,y,z|n)=\prod_{j=1}^n{y\over z-x\omega^j}.$$ The Fermat equation ([\[Fermat\]](#Fermat){reference-type="ref" reference="Fermat"}) ensures the periodicity relation: $$w(x,y,z|n+N)=w(x,y,z|n).$$ This latter property enables us to consider the finite set $Z_N$ instead of $Z$.

For any non-coinciding complex numbers $z_0,z_1,z_2,z_3$, and $\a,\b,\g,\d,a,c\in Z_N$ define two functions: $$T^{0123}(a,c)_{\a,\b}^{\g,\d}=
\rho_{0123}\omega^{c(\g-\a)+\a\d+ac/2}w(x_{03}x_{12},x_{01}x_{23},
x_{02}x_{13}|\g-a,\a)\delta_{\b,\g+\d},\label{T}$$ and $$\overline T^{0123}(a,c)^{\a,\b}_{\g,\d}=
{\overline\rho_{0123}\omega^{c(\g-\a)-\a\d-ac/2}\delta_{\b,\g+\d}\over
w(x_{03}x_{12}/\omega,x_{01}x_{23},
x_{02}x_{13}|\g+a,\a)},\label{Tbar}$$ where $$x_{ij}=(z_i-z_j)^{1/N},\quad i,j=0,1,2,3,$$ with $N$-th root being chosen to be real for real difference $z_i-z_j$; scalar functions $\rho_{0123}$ and $\overline\rho_{0123}$ depend on only $z$'s and their explicit form can be found in [@K]. These symbols can be associated with tetrahedrons in $R^3$ as is described below.

In what follows for a polyhedron $X$, considered as a collection of vertices, edges, triangles, and tetrahedrons, we will denote by $\Lambda_i(X)$, $i=0,1,2,3$ the sets of simplices of corresponding dimension. Consider a topological [^1] tetrahedron $t$ in $R^3$. Order the vertices by fixing a bijective map $$u\colon \{0,1,2,3\}\ni i\mapsto u_i\in\Lambda_0(t).$$ Put an arrow on each edge, pointing from a "larger" vertex (with respect to above ordering) to a "smaller" one. Each face also gets its' own orientation. Let $u_l$ be the top of the tetrahedron. Let us look from it down at the vertices $u_i,u_j,u_k$, where $$\{i,j,k\}=\{0,1,2,3\}\setminus \{l\},\quad i<j<k.$$ We will see two possible views: either $u_i,u_j,u_k$, in the order which they are written, go round in the counter-clockwise direction (the "right" orientation) or, in the clockwise one (the "left" orientation). The tetrahedron itself has two possible orientations in the following sense. Call the tetrahedron "right (left)"-oriented if the face $u_0u_1u_2$ has the right (left) orientation in the above sense.

Introduce three maps: $$s\colon \Lambda_0(t)\to C,\quad c\colon \Lambda_1(t)\to Z_N,
\quad\alpha\colon \Lambda_2(t)\to Z_N,\label{charge}$$ where $s$ is injective, and $c$ satisfies the following relations: $$\sum_{e\ni v}c(e)=1/2,\quad v\in\Lambda_0(t).$$ Let $c_{ij}=c(u_iu_j)$ ($u_iu_j$ is the edge having ends $u_i$ and $u_j$), $\alpha_i=\alpha(u_ju_ku_l)$, $\{j,k,l\}=\{0,1,2,3\}\setminus\{i\}$, and $z_i=s(u_i)$. Define the symbol associated with the tetrahedron $t$: $$t_u(s,c,\alpha)=\cases{ T^{0123}(c_{01},c_{12})
_{\alpha_3,\alpha_1}^{\alpha_2,\alpha_0},& right orientation;\cr
\overline T^{0123}(c_{01},c_{12})
^{\alpha_3,\alpha_1}_{\alpha_2,\alpha_0},& left orientation.\cr}\label{tetr}$$ The variables associated with the second map in ([\[charge\]](#charge){reference-type="ref" reference="charge"}) will be called $Z_N$-charges. Using symbols ([\[tetr\]](#tetr){reference-type="ref" reference="tetr"}), one can associate a "partition" function to any finitely triangulated three-manifold with a triangulated tangle passing through the all interior 0-simplices. The construction goes as follows.

Let $M$ be a finite triangulation of an oriented 3-dimensional manifold with boundary. Fix a subset of 1-simplices $T\subset\Lambda_1(M\setminus\partial M)$ in such a way that any interior 0-simplex belongs to exactly two elements from $T$, so the latter is some triangulated tangle in $M$, passing through the all interior vertices. Denote $I=\{0,1,\ldots,K-1\}$, where $K$ is the number of vertices in $M$, and fix the following maps: $$u\colon I\to\Lambda_0(M),\quad s\colon\Lambda_0(M)\to C,\quad
c_T\colon\Lambda_3(M)\times\Lambda_1(M)\to Z_N,\quad
\alpha\colon\Lambda_2(M)\to Z_N,\label{allmaps}$$ where $u$ is bijective, $s$, injective, and $c_T$ satisfies the restrictions: $$e\not\in\Lambda_1(t)\Rightarrow c_T(t,e)=0;
\quad\sum_{e\ni v}c_T(t,e)=1/2,\quad v\in t\in\Lambda_3(M);$$ $$\sum_{t\in\Lambda_3(M)}c_T(t,e)=\cases{0,&$e\in T$;\cr
                       1,&$e\in
\Lambda_1(M\setminus\partial M)\setminus T$.\cr}$$ Denote the total $Z_N$-charges on $\Lambda_1(\partial M)$ by $$\partial c_{tot}\colon \Lambda_1(\partial M)\ni e\mapsto
\sum_{t\in\Lambda_3(M)}c_T(t,e)\in Z_N,$$ and also the restrictions of the remained maps in ([\[allmaps\]](#allmaps){reference-type="ref" reference="allmaps"}) by $$\partial u\colon\Lambda_0(\partial M)\to I,\quad
\partial s\colon\Lambda_0(\partial M)\to C,\quad
\partial\alpha\colon\Lambda_2(\partial M)\to Z_N.$$ Then, the partition function reads: $$M_{\partial u}(T,\partial s,\partial c_{tot},\partial\alpha)=N^{-K_0}
\sum_{\alpha,\partial\a=\mathrm{fixed}}
\prod_{t\in\Lambda_3(M)}
t_u(s,c_T,\alpha)\prod_{e\in\Lambda_1(M\setminus\partial M)\setminus T}
\langle s(\partial e)
\rangle^{-1},\label{partfun}$$ where $$\langle s(\partial e)\rangle=(s(u_j)-s(u_i))^{(N-1)/N},\quad e=u_iu_j;$$ and $K_0$ being the number of interior 0-simplices. As is reflected in the left hand side of ([\[partfun\]](#partfun){reference-type="ref" reference="partfun"}), the partition function depends (up to $N$-th roots of unity) only on the boundary data as well as on the topological class of the triangulated tangle (see [@K] for the definition). This is the consequence of the relations the symbols ([\[tetr\]](#tetr){reference-type="ref" reference="tetr"}) satisfy, which are described in [@K]. When $\partial M=\emptyset$ partition function ([\[partfun\]](#partfun){reference-type="ref" reference="partfun"}) multiplied by $N^2$ reduces to the invariant of triangulated links [@K].

To make contact with the results of Sect. [\[sec2\]](#sec2){reference-type="ref" reference="sec2"}, we have just to specify the triangulated 3-manifold with tangle, corresponding to $R$-symbol ([\[R\]](#R){reference-type="ref" reference="R"}). The most economic way is to consider singular triangulated manifolds [@TV].

Let $u_1,u_2,u_3,u_4$ be four points in $R^3$, specifying the right-oriented tetrahedron $u_1u_2u_3u_4$. Glue to four faces of the latter four other tetrahedrons $$u_1u_2u_4u_5,\quad u_2u_3u_4u_{5'},\quad u_0u_1u_2u_3,
\quad u_{0'}u_1u_3u_4.$$ We have added four new vertices $u_0,u_{0'},u_5,u_{5'}$. Among the latter identify the "primed" vertices with the corresponding "non-primed" ones: $$u_0=u_{0'},\quad u_5=u_{5'}.$$ While doing this, we glue also the added tetrahedrons pairwise along the corresponding faces. As a result we get a triangulated octahedron $u_0u_1u_2u_3u_4u_5$. The next step consists in attaching four more tetrahedrons, $$u_0u_1u_2u_5,\quad u_0u_2u_3u_5,\quad u_0u_3u_4u_5,
\quad u_0u_1u_4u_5,$$ to the octahedron, each one being glued along two faces. For example, tetrahedron $u_0u_1u_2u_5$ is attached along faces $u_0u_1u_2$ and $u_1u_2u_5$, and similarly the others. Thus we obtain singular triangulated three-ball $B$, where among others four different 1-simplices have coinciding ends $u_0$ and $u_5$. We will distinguish them by specifying the tetrahedron to which they belong. For example, $$_{12}\in \Lambda_1(u_0u_1u_2u_5),$$ and similarly for the others. Besides, $\Lambda_2(\partial B)$ consists of four pairs of 2-simplices, each being given by one and the same triple of vertices: $$\Lambda_2(\partial B)=\{[u_0u_iu_5]^{\pm},\quad i=1,2,3,4\},$$ where we distinguish elements within each pair by their orientation ($+$ ($-$) corresponds to the right (left) orientation). To write down the partition function, we have to specify the tangle. Let us choose it as follows: $$T=\{u_1u_3,u_2u_4\}.$$ Now, providing $B$ with additional data ([\[allmaps\]](#allmaps){reference-type="ref" reference="allmaps"}), one can calculate the partition function ([\[partfun\]](#partfun){reference-type="ref" reference="partfun"}). The result reads: $$\begin{aligned}
\lefteqn{B_{\partial u}(T,\partial s,\partial c_{tot},
\partial\alpha)}\qquad\nonumber\\
&&=(s_{05})^{N-1}
\sum_{i_1,i_2,i_3,i_4=0}^{N-1}R(i_1,i_2,i_3,i_4|c_{12},c_{23},c_{34},c_{14})
\prod_{m=1}^4\psi_{m,i_m}^{\a_m^--\a_m^++c_m},\label{octahed}
\end{aligned}$$ where $$\a_m^\pm=\alpha([u_0u_mu_5]^{\pm}),\quad s_{ij}=(s(u_i)-s(u_j))^{1/N}$$ $$c_m=\partial c_{tot}(u_mu_5),\quad c_{ij}=\partial c_{tot}([u_0u_5]_{ij}),$$ and $$\psi_{m,j}^k=\omega^{jk}s_{0m}^{[k-1]}s_{m5}^{[-k]},$$ see also ([\[brac\]](#brac){reference-type="ref" reference="brac"}). The role of $\psi$-functions is to intertwine the indices of different nature. Note that the $Z_N$-charges are related with the angle-dependent data for the enhanced $R$-matrix.

Formula ([\[octahed\]](#octahed){reference-type="ref" reference="octahed"}) enables us to prove the second part of Theorem [\[theo\]](#theo){reference-type="ref" reference="theo"}. Indeed, let we are given a link, represented by a two-strand tangle. Then, using correspondence ([\[octahed\]](#octahed){reference-type="ref" reference="octahed"}), we associate to the latter partition function of a singular triangulated three-ball with four boundary 0-simplices, the tangle by its strands being attached to two of them. To get the invariant in $S^3$, we have to glue the ball with another (empty) one, making the tangle to pass through the other two vertices and converting it into the link under consideration. This last process is equivalent to choosing boundary conditions ([\[boundary\]](#boundary){reference-type="ref" reference="boundary"}).

One can prove also the YBE ([\[YBE\]](#YBE){reference-type="ref" reference="YBE"}) via consideration the triangulated three-balls, corresponding to two sides of YBE, and transforming them to each other by a sequence of elementary moves defined in [@K].

A remark is in order. In [@K1] it has been shown that the universal $R$-matrix in Drinfeld double can be represented as a product of solutions to the constant pentagon relation, the canonical element in Heisenberg double being such solution. This construction can be extended also to the case of non-constant solutions to the pentagon relation. In particular, using cyclic quantum dilogarithm of [@FK] and specializing the parameters, one can derive $R$-matrix ([\[R-matrix\]](#R-matrix){reference-type="ref" reference="R-matrix"}). The derivation given in this section is essentially equivalent to the latter. On the other hand, the cyclic quantum dilogarithm can be obtained from the quantum dilogarithm with $q$ non-root of unity [^2] in the limit, where $q$ approaches a root of unity [@BR]. Thus, it is natural to consider $R$-matrix ([\[R-matrix\]](#R-matrix){reference-type="ref" reference="R-matrix"}) as a cyclic counterpart of the universal $R$-matrix in $U_q(sl(2))$.

[^1]: the term "topological" here means that edges and faces of the tetrahedron can be curved

[^2]: in this case the quantum dilogarithm is precisely the canonical element in Heisenberg double of $BU_q(sl(2))$, the Borel sub-algebra of $U_q(sl(2))$ [@K]
