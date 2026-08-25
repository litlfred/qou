*The eightfold-way multiplets --- decuplet ($\mathbf{10}$), octet
($\mathbf{8}$), and singlet ($\mathbf{1}$) --- are the quantum
Schur--Weyl partners of the Hecke algebra $H_3(q)$ acting on
$V^{\otimes 3}$.*

Quantum Schur--Weyl duality (Jimbo \cite{jimbo1986}) states that
$\mathcal{U}_q(\mathfrak{gl}_N)$ and $H_n(q)$ are mutual centralizers
on $V^{\otimes n}$:
$$
  V^{\otimes n}
  \cong \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq N}}
    V_\lambda^{\mathfrak{gl}_N} \otimes S^\lambda_{H_n(q)},
$$
where $\lambda$ ranges over partitions of $n$ with at most $N$ rows,
$V_\lambda^{\mathfrak{gl}_N}$ is the irreducible
$\mathcal{U}_q(\mathfrak{gl}_N)$-module labelled by $\lambda$, and
$S^\lambda_{H_n(q)}$ is the irreducible Hecke module (Specht module)
labelled by the same partition.

At $n = 3$ (three-strand braiding) and $N = 3$ (three-dimensional
fundamental representation), the decomposition reads:
$$
  V^{\otimes 3}
  \cong
  \underbrace{V_{(3)}}_{\dim = 10}
    \otimes S^{(3)}
  \;\oplus\;
  \underbrace{V_{(2,1)}}_{\dim = 8}
    \otimes S^{(2,1)}
  \;\oplus\;
  \underbrace{V_{(1,1,1)}}_{\dim = 1}
    \otimes S^{(1,1,1)}.
$$

The dimensions and multiplicities are:

| $\lambda \vdash 3$ | $\dim V_\lambda^{\mathfrak{gl}_3}$ | $\dim S^\lambda_{H_3}$ | Name |
|---|---|---|---|
| $(3)$ | $10$ (decuplet) | $1$ | symmetric |
| $(2,1)$ | $8$ (octet) | $2$ | mixed |
| $(1^3)$ | $1$ (singlet) | $1$ | antisymmetric |

The total is $10 \cdot 1 + 8 \cdot 2 + 1 \cdot 1 = 27 = 3^3$, as
required.  The Hecke block dimensions $(1, 2, 1)$ are the
*multiplicities* of the flavour irreps, not the irreps themselves.

**The $N = 3$ question.**
The single-fibre tower of the
[braiding](#chap:path-integrals-braiding) and
[Bring's-surface](#chap:brings-surface) chapters has
$\dim V = 2$ (the standard single-fibre construction yields a quantum
form of $\mathrm{SU}(2)$; the Descartes condition $\chi(\mathcal{A}) = -6$
is compatible with but does not uniquely force $N = 2$ --- see the
$\chi$-rank audit).  The
decomposition at $N = 2$ is:
$$
  V^{\otimes 3}
  \cong V_{(3)} \otimes S^{(3)}
  \;\oplus\;
  V_{(2,1)} \otimes S^{(2,1)},
  \qquad
  4 \cdot 1 + 2 \cdot 2 = 8 = 2^3.
$$
The antisymmetric partition $(1^3)$ is *absent* (three rows exceed
$N = 2$).  No choice of $q$ restores it: the row cap is
$\ell(\lambda) \leq \dim V$, which the single-fibre construction fixes at $2$,
and the Drinfeld--Jimbo quantisation does not change dimensions.

**The obstruction, and what is machine-checked about it.**
The following are verified sorry-free in
`QOU/Eightfold/RowCapObstruction.lean`:

- `weyl_dim_alt_eq_zero_iff` --- the alternating channel
  $\dim V_{(1^3)} = \binom{N}{3}$ vanishes *if and only if* $N < 3$.
  This is the obstruction in one line.
- `decuplet_forces_three` --- if the symmetric channel has
  dimension $10$ then $N = 3$.  The implication runs from the decuplet
  dimension to the flavour dimension, in that direction.
- `singlet_forces_three` --- a one-dimensional alternating
  channel likewise pins $N = 3$.
- `schur_weyl_cube_split_two_three` --- the channel
  arithmetic closes at both values ($8 = 4 + 4 + 0$ at $N = 2$;
  $27 = 10 + 16 + 1$ at $N = 3$), so the $N = 2$ deficit sits precisely in the
  vanishing alternating channel and not in some unaccounted-for piece.

**What that Lean does not establish.**
The same caveat applies here as to `Sym2Gate.lean` and
`WeylInvarianceQDeformation.lean` above, and it is load-bearing in this one
place because $N = 3$ is the chapter's central open problem.  What is
machine-checked is the *arithmetic* of the row cap on the channel
dimensions: the file *defines* $\dim V_{(1^3)}^{\mathfrak{gl}_N}$ to be
$\binom{N}{3}$ and then reasons about $\binom{N}{3}$, with every proof a
`Nat.choose` identity, a `decide`, or an `omega`.  That the hook-content
formula gives $\dim V_{(1^3)} = \binom{N}{3}$, and that the Schur--Weyl row
cap is $\ell(\lambda) \leq N$, are standard and cited --- carried by the
definition names and docstrings, not proved.  The file's own docstring
concedes the boundary, noting that Worpitzky's identity is not formalised
here.  So the tier is *standard mathematics, with a sorry-free
machine-checked arithmetic instance* --- not *proved* in the sense the other
Lean-backed rows of this chapter use.

The conclusion is nonetheless correct, because the two cited inputs are
textbook.  The eightfold-way classification is not "approximately available"
at $N = 2$ --- it is structurally unavailable.  This is a scope-(b)
exclusion, and the invariant justifying it is the Schur--Weyl row cap.

`decuplet_forces_three` and `singlet_forces_three` run from an
*observed* channel dimension to $N = 3$; what the framework requires is
$N = 3$ *supplied* by a construction.  That is the affirmative half, and it
remains open.

Therefore, realising the full eightfold way requires $N = 3$.  Within
QOU, this $N = 3$ cannot arise from a single fibre.  The remaining
construction directions are:

1. **Multi-fibre groupoid:** inequivalent fibre objects
   whose interaction space is three-dimensional (T3b).
2. **Octonionic $G_2$ stabilizer:** the Günaydin--Gürsey
   $\mathbf{7} = \mathbf{1} \oplus \mathbf{3} \oplus \bar{\mathbf{3}}$
   provides a non-self-dual triple from $\mathrm{SU}(3) \subset G_2$
   ([Proposition](#prop:color-su3-from-g2)).

**Status of the $\mathrm{Sym}^2$ gate.**  The gate is the
requirement that $\mathrm{Sym}^2(W)$ contain no singlet.  The Lean file
`QOU/Eightfold/Sym2Gate.lean` records the arithmetic of the test
($\dim \mathrm{Sym}^2(\mathbf{3}) = 6$; the icosahedral triple $T_1$
decomposes $1 + 5$ and so carries a singlet, while the octonionic
$\mathbf{3}$ decomposes $6 + 0$ and does not).  What that file
*proves* is only the arithmetic --- its declarations reduce to
identities such as $6 = 6 \wedge 0 = 0$, with the representation-theoretic
content supplied by hand in the statement names, not by the proofs.  So
the correct reading is: the octonionic $\mathbf{3}$ is *not
excluded* by the $\mathrm{Sym}^2$ gate, on a decomposition taken from the
literature.  It is not a machine-checked pass, and the file should not be
cited as one.  Whether the route yields *flavour* $\mathrm{SU}(3)$
(not just colour) remains open.
