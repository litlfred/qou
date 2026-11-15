Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)), and let $(\nabla_A q, L \wedge F^+)$ be the connection--curvature pair of the ([mass identity](#def:mass-identity)). For each vertical degree $n \geq 0$ in the Reeb decomposition, the restriction of the nonabelian multiplicative integral to $\mathcal{S}_c$ abelianises to the $n$-th prolonged Seiberg--Witten period:

```tex
\begin{equation}\label{eq:mi-sw-abelianisation}
  \bigl\lVert
  \mathrm{MI}\!\!\int_{\mathcal{S}_c}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert_{J^n}
  = 
  \bigl\lvert a_D^{(n)}\bigr\rvert
  = 
  \biggl\lvert\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}\biggr\rvert,
\end{equation}
```

where $\lVert\cdot\rVert_{J^n}$ denotes the Killing-form norm projected onto the $n$-th jet component, and $\lambda_{\mathrm{SW}}^{(n)}$ is the $n$-th prolonged Seiberg--Witten differential. The unprolonged objects are those of Seiberg and Witten: for $\mathcal{N}=2$ $SU(2)$ gauge theory with matter hypermultiplets, the periods $(a, a_D)$ of a meromorphic differential on a family of elliptic curves determine the exact low-energy metric and the masses of the stable BPS states \cite{seiberg-witten1994b}. Mathematically, a Seiberg--Witten differential is a meromorphic $1$-form $\lambda$ on the total space of an algebraically integrable system with $d\lambda = \sigma$, the symplectic form, so that its periods are special coordinates on the base \cite[\S2]{donagi1997}.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
