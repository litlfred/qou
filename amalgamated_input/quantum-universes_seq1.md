<!-- FILE_START: rigid-monoidal-intro.md -->
Why do the axioms of a physical theory land on a rigid braided monoidal category? Two lines of thought converge here. Composing physical processes in sequence and in parallel forces a monoidal structure. Superselection-sector analysis of local observables forces the same. Any compositional theory of physical systems settles into this framework, which we fix before stating the quantum-universe axioms.

We keep two examples in view: the polynomial ring $\mathbb{C}[z]$ and the coordinate ring $\mathcal{O}(\mathrm{SU}(2))$. Objects have tensor products and a unit over a base ring, making the category $R$-linear. Every object $V$ has a dual $V^{\vee}$. The zig-zag (snake) equations make $V^{\vee}$ a right dual. A braiding exchanges tensor factors. The symmetric case $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$ marks the classical limit.

The next section mounts the Frobenius--Hopf object, the fibre functor, and the differential calculus on this scaffold.
<!-- FILE_END: rigid-monoidal-intro.md -->

<!-- FILE_START: snake-identity.md -->
Let $(\mathbf{C}, \otimes, \mathbf{1})$ be a :refterm[monoidal category]{#monoidal-category}. Let $V$ be an object with dual $V^{\vee}$, evaluation $\mathrm{ev} \colon V \otimes V^{\vee} \to \mathbf{1}$, and coevaluation $\mathrm{coev} \colon \mathbf{1} \to V^{\vee} \otimes V$. The **snake identities** are the equations making $(\mathrm{ev}, \mathrm{coev})$ exhibit $V^{\vee}$ as a :refterm[right dual]{#right-dual} of $V$:

```tex
\begin{equation}\label{eq:snake-identities}
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V
    \ar[r, "\mathrm{id} \otimes \mathrm{coev}"]
    \ar[dr, "\mathrm{id}_V"']
  & V \otimes V^{\vee} \otimes V
    \ar[d, "\mathrm{ev} \otimes \mathrm{id}"]
  \\
  & V
\end{tikzcd}
\\[-0.5em]
\text{\small (left snake identity)}
\end{gathered}
\qquad\qquad
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V^{\vee}
    \ar[r, "\mathrm{coev} \otimes \mathrm{id}"]
    \ar[dr, "\mathrm{id}_{V^{\vee}}"']
  & V^{\vee} \otimes V \otimes V^{\vee}
    \ar[d, "\mathrm{id} \otimes \mathrm{ev}"]
  \\
  & V^{\vee}
\end{tikzcd}
\\[-0.5em]
\text{\small (right snake identity)}
\end{gathered}
\end{equation}
```

The pair forms an :defterm[exact pairing]{#exact-pairing}. In graphical calculus, the composites trace an S-shaped curve that straightens to a vertical line.
<!-- FILE_END: snake-identity.md -->

<!-- FILE_START: rigid-monoidal-category.md -->
A **:refterm[monoidal category]{#monoidal-category}** $(\mathbf{C}, \otimes, \mathbf{1})$ is a category equipped with a bifunctor $\otimes \colon \mathbf{C} \times \mathbf{C} \to \mathbf{C}$, a unit object $\mathbf{1}$, and natural isomorphisms expressing associativity and unitality:

```tex
\begin{equation}\label{eq:monoidal-axioms}
\begin{gathered}
\begin{tikzcd}[column sep=3em]
  (X \otimes Y) \otimes Z
    \ar[r, "\alpha_{X,Y,Z}", "\sim"']
  & X \otimes (Y \otimes Z)
\end{tikzcd}
\\[-0.5em]
\text{\small (associativity)}
\end{gathered}
\qquad
\begin{gathered}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \otimes X
    \ar[r, "\ell_X", "\sim"']
  & X
  & X \otimes \mathbf{1}
    \ar[l, "\rho_X"', "\sim"]
\end{tikzcd}
\\[-0.5em]
\text{\small (unitality)}
\end{gathered}
\end{equation}
```

The category is *rigid* if every object $V$ has a dual $V^{\vee}$ together with morphisms $\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$ and $\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$ satisfying the [snake identities](#def:snake-identity).

We say $\mathbf{C}$ is *$R$-linear* for a commutative ring $R$ [without quasi-zeros](#rem:glossary-no-quasi-zeros) if every hom-set is an $R$-module and composition is $R$-bilinear.

The category is *braided monoidal* if it has a natural isomorphism $c_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ compatible with the associator and satisfying the hexagon axioms. The braiding is *symmetric* when $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$. Given a braiding, the *exterior power* $\Lambda^k V$ is the image of the antisymmetriser $\mathrm{Alt}_k = \sum_{\pi \in S_k} \mathrm{sgn}(\pi)\pi$ acting on $V^{\otimes k}$, where permutations act via $c$.
<!-- FILE_END: rigid-monoidal-category.md -->

<!-- FILE_START: monoidal-justification.md -->
Why is a rigid :refterm[monoidal category]{#monoidal-category} the starting point for quantum-geometric structure? Two lines of reasoning converge.

**Information-theoretic necessity.** Picture two subsystems side by side. The tensor product $\otimes$ joining them is the grammar of any physical system possessing inputs and outputs. A compositional language forces a :refterm[monoidal category]{#monoidal-category}. Rigidity follows because processes must be reversible at the level of types. A system of type $V$ bends around to become an input of type $V^{\vee}$, which is the content of the snake identities.

**Physical reconstruction from superselection.** Take an electric charge and its conjugate anticharge. Algebraic quantum field theory arrives at the same structure through superselection sectors. The category of superselection sectors is automatically rigid braided monoidal. The tensor product encodes charge composition. The braiding encodes exchange statistics. Rigidity encodes anticharges. Locality and covariance force the monoidal structure.

These two perspectives make the rigid monoidal framework a well-motivated foundation.
<!-- FILE_END: monoidal-justification.md -->

<!-- FILE_START: rigid-monoidal-vect.md -->
Two rigid monoidal categories run through this paper: the degenerate baseline $\mathrm{Vect}_{\mathbb{C}}$ and the classical example $\mathrm{Rep}(\mathrm{SU}(2))$. Both arise as representations of a function algebra.

The polynomial ring $\mathbb{C}[z]$ is the algebra of functions on $\mathbb{C}$. The category $\mathrm{Vect}_{\mathbb{C}}$ of finite-dimensional complex vector spaces is the simplest $\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}. The tensor product is $V \otimes W$, the unit is $\mathbf{1} = \mathbb{C}$, and the dual is $V^{\vee} = \mathrm{Hom}(V, \mathbb{C})$ with $\mathrm{ev}(v \otimes f) = f(v)$.

The coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ is the algebra of polynomial functions on $\mathrm{SU}(2)$, generated by matrix entries $\alpha, \beta, \bar\alpha, \bar\beta$ with $\alpha\bar\alpha + \beta\bar\beta = 1$. The category $\mathrm{Rep}(\mathrm{SU}(2))$ of finite-dimensional representations is $\mathbb{C}$-linear rigid monoidal. Its simple objects are the spin-$j$ representations $V_j$ ($j = 0, \tfrac12, 1, \ldots$). The *fundamental object* is $V = V_{1/2} \cong \mathbb{C}^2$.
<!-- FILE_END: rigid-monoidal-vect.md -->

