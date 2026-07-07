<!-- FILE_START: rigid-monoidal-intro.md -->
Why should the axioms of a physical theory land on a category at all, and why a rigid braided monoidal one? Two independent lines of thought answer the same way. Reading a physical process as something one can compose in sequence and in parallel — the Coecke--Kissinger grammar of composable processes — already forces a monoidal structure; superselection-sector analysis in the Haag--DHR tradition arrives at the same place from the algebra of local observables. Any compositional theory of physical systems, approached from either side, settles into a rigid braided monoidal framework, and it is that framework we fix here before stating the quantum-universe axioms.

The setting is concrete before it is abstract. The polynomial ring $\mathbb{C}[z]$ on the affine line and the coordinate ring $\mathcal{O}(\mathrm{SU}(2))$ supply two running examples that recur through every subsequent definition; keeping them in view is enough to see what each piece of structure is for. Objects have tensor products and a unit over a base ring, making the category $R$-linear. Each object $V$ acquires a dual $V^{\vee}$, and the sense in which $V^{\vee}$ is a *right* dual is exactly the zig-zag (snake) equations. A braiding lets tensor factors be exchanged, and the symmetric special case — where exchanging twice returns the identity, $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$ — is singled out as the classical limit within the quantum picture.

On this rigid monoidal scaffold the next section, *The Quantum Universe*, mounts the Frobenius--Hopf object, the fibre functor, and the differential calculus.
<!-- FILE_END: rigid-monoidal-intro.md -->

<!-- FILE_START: snake-identity.md -->
Let $(\mathbf{C}, \otimes, \mathbf{1})$ be a :refterm[monoidal category]{#monoidal-category} and
let $V$ be an object with dual $V^{\vee}$, evaluation
$\mathrm{ev} \colon V \otimes V^{\vee} \to \mathbf{1}$, and
coevaluation $\mathrm{coev} \colon \mathbf{1} \to V^{\vee} \otimes V$.
The **snake identities** (also called *zig-zag identities*) are the
equations that make $(\mathrm{ev}, \mathrm{coev})$ exhibit $V^{\vee}$
as a dual of $V$; they are the two commutative diagrams:

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

These identities express the fact that $(\mathrm{ev}, \mathrm{coev})$
exhibit $V^{\vee}$ as a :refterm[right dual]{#right-dual} of $V$ (equivalently, that the pair
forms an :defterm[exact pairing]{#exact-pairing}). The
terminology "snake" comes from the graphical calculus, where the
composites trace out an S-shaped curve that straightens to a vertical
line.
<!-- FILE_END: snake-identity.md -->

<!-- FILE_START: rigid-monoidal-category.md -->
A **:refterm[monoidal category]{#monoidal-category}** $(\mathbf{C}, \otimes, \mathbf{1})$ is a
category equipped with a bifunctor
$\otimes \colon \mathbf{C} \times \mathbf{C} \to \mathbf{C}$ (the
*tensor product*), a unit object $\mathbf{1}$, and natural
isomorphisms expressing associativity and unitality:

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

The category is *rigid* if every object $V$ has a *dual*
$V^{\vee}$ together with morphisms
$\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$
and
$\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$
satisfying the [snake identities](#def:snake-identity).

We say $\mathbf{C}$ is *$R$-linear* (for a commutative ring $R$)
if every hom-set is an $R$-module and composition is $R$-bilinear.
We require $R$ to be [without quasi-zeros](#rem:glossary-no-quasi-zeros).

The category is *braided monoidal* if it is further equipped with a
natural isomorphism (the *braiding*)
$c_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$
compatible with the associator and satisfying the hexagon axioms.
When $c_{Y,X} \circ c_{X,Y} = \mathrm{id}$ the braiding is
*symmetric* (as in $\mathbf{Vect}$); in general
$c^2 \neq \mathrm{id}$ (as in $\mathbf{Rep}(\mathrm{SU}_q(2))$).  Given a braiding,
the *exterior power* $\Lambda^k V$ is defined as the image of the
antisymmetriser
$\mathrm{Alt}_k = \sum_{\pi \in S_k} \mathrm{sgn}(\pi)\pi$ acting
on $V^{\otimes k}$, where permutations act via $c$.
<!-- FILE_END: rigid-monoidal-category.md -->

<!-- FILE_START: monoidal-justification.md -->
Before stating the formal definition, we pause to explain why a rigid
:refterm[monoidal category]{#monoidal-category} is the inevitable starting point for any theory of
quantum-geometric structure. Two independent lines of reasoning
converge on the same conclusion.

**Information-theoretic necessity.** Picture two subsystems placed
side by side — a pair of qubits, or an apparatus alongside the system
it measures. Coecke and Kissinger
\cite{coecke2017} demonstrate that the tensor product $\otimes$ that
joins them is
not an algebraic convenience but the *grammar* of any physical system
possessing inputs and outputs. The moment one demands a compositional
language — where composite systems are described by combining
subsystems, and processes compose both sequentially (via $\circ$) and
in parallel (via $\otimes$) — one is forced into a :refterm[monoidal category]{#monoidal-category}.
Rigidity (the existence of duals) then follows from the requirement
that every process be reversible at the level of type structure: a
system of type $V$ can always be "bent around" to become an input of
type $V^{\vee}$, which is precisely the content of the snake
identities.

**Physical reconstruction from superselection.** Take an electric
charge and its conjugate anticharge — a sector and the sector that
neutralizes it when the two are fused. From an entirely
different direction, Haag's algebraic quantum field theory
\cite{haag1996} arrives at the same structure through the analysis of
superselection sectors. In the DHR (Doplicher--Haag--Roberts)
framework, the category of superselection sectors of any reasonable
quantum field theory is automatically a rigid braided monoidal
category: the tensor product encodes the composition of charges, the
braiding encodes the exchange statistics of sectors, and rigidity
encodes the existence of anticharges (conjugate sectors). The monoidal
structure is not imposed — it is *forced* by the locality and
covariance axioms of quantum physics.

These two perspectives — one from the logic of processes, the other
from the geometry of measurements — make the rigid monoidal framework
a uniquely well-motivated foundation. The definition that follows
captures exactly this structure.
<!-- FILE_END: monoidal-justification.md -->

<!-- FILE_START: rigid-monoidal-vect.md -->
Two rigid monoidal categories run through the paper: the degenerate
baseline $\mathrm{Vect}_{\mathbb{C}}$, and the classical running example
$\mathrm{Rep}(\mathrm{SU}(2))$ — the symmetric ($q \to 1$) limit of the
framework's $\mathrm{Rep}(\mathrm{SU}_q(2))$.  Each arises as
representations of a function algebra, so
we read them off from that algebra in turn.

The polynomial ring $\mathbb{C}[z]$ is the algebra of functions on the
complex line $\mathbb{C}$.  The category
$\mathrm{Vect}_{\mathbb{C}}$ of finite-dimensional complex vector spaces
is the simplest $\mathbb{C}$-linear rigid :refterm[monoidal category]{#monoidal-category}: the tensor
product is $V \otimes W$, the unit is $\mathbf{1} = \mathbb{C}$, and the
dual is $V^{\vee} = \mathrm{Hom}(V, \mathbb{C})$ with
$\mathrm{ev}(v \otimes f) = f(v)$.

Similarly, the *coordinate ring* $\mathcal{O}(\mathrm{SU}(2))$ is
the algebra of polynomial functions on the group $\mathrm{SU}(2)$,
generated by the matrix entries $\alpha, \beta, \bar\alpha, \bar\beta$
with $\alpha\bar\alpha + \beta\bar\beta = 1$.  The category
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ of finite-dimensional
representations is $\mathbb{C}$-linear rigid monoidal.  Its simple
objects are the spin-$j$ representations $V_j$
($j = 0, \tfrac12, 1, \ldots$, $\dim V_j = 2j+1$).  The
*fundamental object* is $V = V_{1/2} \cong \mathbb{C}^2$.
<!-- FILE_END: rigid-monoidal-vect.md -->

