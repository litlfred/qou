<!-- FILE_START: vectors-hadrons-intro.md -->
The weight decomposition supplied a $T$-equivariant
splitting of $\Omega^\bullet(A)$; we now collect the trace and
basis machinery built on top of it for intertwiner spaces of
tensor powers of the fundamental representation. Remark: Adjoint trace introduces
$\mathrm{tr}_{\mathrm{Ad}} \colon \mathrm{End}(V) \to R$ from
the Frobenius pairing and the fibre-adjoint involution, with
cyclicity inherited from Frobenius and non-degeneracy from
positive-definiteness of the dagger. Proposition: PawLei basis — the Pawlowski--Leitner canonical basis on
$\mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$,
indexed by standard Young tableaux of shape $\lambda \vdash n$
with at most two rows — is constructed by contraction with the
volume form along the unital Gröbner--Shirshov route, with
dimension given by the hook-length formula. Proposition: PawLei inner product uses the adjoint trace to define an orthogonal
pairing on PawLei vectors and identifies it with the
restriction of the Frobenius pairing to $\mathrm{End}(V_j)
\subset A$, so that fibre integration commutes with the
intertwiner expansion of hadron states.

_(draft.)_
<!-- FILE_END: vectors-hadrons-intro.md -->

<!-- FILE_START: adjoint-trace.md -->
The [Frobenius pairing](#def:frobenius-pairing) and the
[fibre-adjoint involution](#prop:fiber-adjoint-involution) together
equip every hom-space $\mathrm{Hom}_{\mathbf{C}}(X, Y)$ with a
canonical sesquilinear form. Define the *adjoint trace* on
endomorphisms of $V$ by

$$
  \mathrm{tr}_{\mathrm{Ad}}(f)
  = 
  \int_A \!\circ \mu \circ (f \otimes \mathrm{id}_{V^{\vee}})
    \circ \mathrm{coev}_V
   \in 
  \mathrm{Hom}(\mathbf{1}, \mathbf{1}) \cong R,
$$

where $\mathrm{coev}_V \colon \mathbf{1} \to V \otimes V^{\vee}$ is
the coevaluation (from rigidity) and $\mu$ is the Frobenius
multiplication on $A$.

This trace has two key properties:

1. **Cyclicity**: $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) = \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited from the
   Frobenius relation.
2. **Non-degeneracy**: the induced pairing
   $\langle f, g \rangle_{\mathrm{Ad}} = \mathrm{tr}_{\mathrm{Ad}}(f^{\dagger} \circ g)$
   is non-degenerate, because $\int_A$ is non-degenerate and the
   dagger is positive-definite.

In the archimedean realisation with $G = \mathrm{SU}(2)$, the adjoint
trace recovers the Killing form on $\mathfrak{su}(2)$:

$$
  \mathrm{tr}_{\mathrm{Ad}}(f)
  = 
  \mathrm{tr}(\mathrm{ad}(f))
  = 
  -2\mathrm{tr}_{\mathbb{C}^2}(f).
$$
<!-- FILE_END: adjoint-trace.md -->

<!-- FILE_START: pawlowski-leitner-basis.md -->
Let $G = \mathrm{SU}(2)$ be the emergent gauge group
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)) and let
$V_{1/2} \cong \mathbb{C}^2$ be the
[spin-$\tfrac{1}{2}$ representation](#rem:spin-half-representation).
For each simple object $V_j$ and tensor power
$V_{1/2}^{\otimes n}$ with $n \geq 2j$, the intertwiner space

$$
  \mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j,
    V_{1/2}^{\otimes n}\bigr)
$$

admits a *canonical* basis — the **PawLei basis** — indexed by
standard Young tableaux of shape $\lambda \vdash n$ with at most
$2$ rows and with $\lambda_1 - \lambda_2 = 2j$.

The construction rests on the
[PBW theorem over commutative rings](unital-groebner-bases:cor:pbw): the unital Gröbner--Shirshov
basis for $U(\mathfrak{su}(2))$ provides a monomial basis for the
enveloping algebra, from which the intertwiner basis is derived by
contraction with the volume form.

```tex
\begin{equation}\label{eq:pawlei-basis-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\epsilon^{\vee}"]
  & \Lambda^2 V_{1/2} \ar[r, hook]
  & V_{1/2}^{\otimes n} \ar[r, "\pi_j"]
  & V_j
\end{tikzcd}
\qquad\text{(PawLei contraction)}
\end{equation}
```

Concretely, the volume form
$\epsilon \colon \Lambda^2 V_{1/2} \to \mathbf{1}$ and its dual
$\epsilon^{\vee} \colon \mathbf{1} \to \Lambda^2 V_{1/2}$ generate
*contraction operators* on tensor powers. The PawLei basis elements
are obtained by applying a specific sequence of pairwise contractions
(determined by the tableau) to the highest-weight vector
$e_+^{\otimes (j+m)} \otimes e_-^{\otimes (j-m)}$, then
symmetrising according to the row structure of the tableau.

The dimension of the intertwiner space is given by the hook-length
formula:

$$
  \dim\mathrm{Hom}_{\mathrm{SU}(2)}\!\bigl(V_j,
    V_{1/2}^{\otimes n}\bigr)
  = 
  \frac{(2j+1) n!}{(\tfrac{n}{2}+j+1)!(\tfrac{n}{2}-j)!}
$$

when $n \equiv 2j \pmod{2}$, and zero otherwise.

The PBW basis underlying this construction is established via unital
Gröbner--Shirshov bases in \cite{leitnerpawloski2004}.
<!-- FILE_END: pawlowski-leitner-basis.md -->

<!-- FILE_START: pawlowski-leitner-inner-product.md -->
The [adjoint trace](#rem:adjoint-trace) induces a canonical inner
product on intertwiner spaces. For
$\phi, \psi \in \mathrm{Hom}_{\mathrm{SU}(2)}(V_j, V_{1/2}^{\otimes n})$, define

$$
  \langle \phi, \psi \rangle_{\mathrm{PL}}
  = 
  \mathrm{tr}_{\mathrm{Ad}}\!\bigl(\phi^{\dagger} \circ \psi\bigr)
  = 
  \int_A \!\circ \mu \circ
    (\phi^{\dagger} \circ \psi \otimes \mathrm{id})
    \circ \mathrm{coev}_{V_j}.
$$

```tex
\begin{equation}\label{eq:pawlei-inner-product-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "\mathrm{coev}_{V_j}"]
  & V_j \otimes V_j^{\vee}
    \ar[r, "\phi^{\dagger} \circ \psi \otimes \mathrm{id}"]
  & A \otimes V_j^{\vee}
    \ar[r, "\int_A \circ \mu"]
  & \mathbf{1}
\end{tikzcd}
\qquad\text{(PawLei inner product)}
\end{equation}
```

The [PawLei basis](#prop:pawlowski-leitner-basis)
$\{T_{\lambda}\}$ is *orthogonal* with respect to this pairing:

$$
  \langle T_{\lambda}, T_{\mu} \rangle_{\mathrm{PL}}
  = 
  \delta_{\lambda\mu} \|T_{\lambda}\|^2,
$$

where the norm-squared $\|T_{\lambda}\|^2$ is a positive rational
number computable from the hook lengths of the tableau $\lambda$.

This orthogonality has two consequences for the QOU framework:

1. **Decomposition of hadron states.** A
   [categorical hadron](#def:hadron) of valence $n$ can be
   uniquely expanded in the PawLei basis, with
   coefficients that are the partial-wave
   amplitudes.
2. **Compatibility with the Frobenius form.** The inner product
   $\langle{-},{-}\rangle_{\mathrm{PL}}$ agrees with the restriction
   of the [Frobenius pairing](#def:frobenius-pairing) to
   $\mathrm{End}(V_j) \subset A$, ensuring that integration over the
   fibre and decomposition into basis elements commute.

The algebraic foundations (PBW bases over commutative rings) are
established in \cite{leitnerpawloski2004}; norm formulas follow from
the Temperley--Lieb calculus and $6j$-symbols.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: pawlowski-leitner-inner-product.md -->

