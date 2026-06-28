**Proposition (incompleteness implies non-empty horizon).**
*Let $(P, e, \mathrm{eval})$ be a Turing-complete resolution
system:*

- *$P$ is a set of programs (finite braids),*
- *$e \colon \mathbb{N} \twoheadrightarrow P$ is a surjective
  enumeration (the braid group on finitely many strands is
  countable),*
- *$\mathrm{eval} \colon P \to (\mathbb{N} \to \mathbb{N})$
  maps each program to the total function it computes.*

*The surjectivity of $e$ and the domain $\mathbb{N}$ of
$\mathrm{eval}$ constitute the **arithmetic non-triviality
condition**: $\mathbb{N}$ is embeddable in the system.
Without this, the diagonal argument is vacuous --- a trivial
category has no self-referential capacity and incompleteness
does not apply.*

*Then there exists $f \colon \mathbb{N} \to \mathbb{N}$
not in the image of $\mathrm{eval}$:*

$$
  \exists\, f \colon \mathbb{N} \to \mathbb{N},\;
  \forall\, p \in P,\;
  \mathrm{eval}(p) \neq f.
$$

*The computable fragment is strictly smaller than the full
function space.*
