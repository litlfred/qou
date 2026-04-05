The **QOU locus** $\mathfrak{M}_{\mathrm{QOU}} \subset
\mathfrak{M}_{\mathrm{QO}}$ is the definable sublocus of the
[moduli of quantum observables](#def:qo-moduli) where the remaining
[QOU axioms](#def:quantum-observable-universe) hold. Each axiom is
a first-order condition in
$\mathcal{L}_{\mathrm{RMC}}$:

1. **Observability**:
   $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ —
   no hidden global symmetries; every internal degree of freedom is
   accessible to measurement.

2. **Measurability**:
   $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$ —
   the adjoint representation is anomaly-free (Chern classes vanish).

3. **Volume constraint**:
   $\exists\, \varepsilon \colon \Lambda^2 V \twoheadrightarrow
   \mathbf{1}$ — a non-degenerate antisymmetric pairing exists,
   forcing the gauge group to $\mathrm{SU}(2)$.

These define a descending **axiom filtration**:

$$
  \mathfrak{M}_{\mathrm{QO}}
  \;\supset\; \mathfrak{M}_{\mathrm{obs}}
  \;\supset\; \mathfrak{M}_{\mathrm{meas}}
  \;\supset\; \mathfrak{M}_{\mathrm{QOU}}
$$

where each inclusion is a definable embedding. The
[axiom independence](#rem:axiom-independence) result confirms these
inclusions are **strict** — no axiom is redundant.

Each level of the filtration is itself a definable class: the
sentences expressing observability, measurability, and the volume
constraint are first-order in $\mathcal{L}_{\mathrm{RMC}}$. This
is the prerequisite for applying the $q$-motivic measure: the
definability of the filtration allows each axiom's "cost" to be
measured in the Grothendieck ring.
