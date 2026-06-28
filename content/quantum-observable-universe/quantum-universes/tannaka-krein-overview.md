The fibre functor $\tau$ of a quantum universe encodes an extraordinary
amount of structure. Tannaka--Krein duality \cite{deligne1990} says:

1. **Reconstruction.** The group $G$ can be recovered from
   $\tau$ alone:
   $G \cong \mathrm{Aut}^{\otimes}(\tau)$,
   the group of monoidal natural automorphisms of $\tau$.
   No *a priori* group is needed; it *emerges* from the
   category and the functor.
2. **Equivalence.** The functor $\tau$ establishes a
   monoidal equivalence
   $\mathbf{C} \simeq \mathrm{Rep}(G)$:
   every object in $\mathbf{C}$ is a representation of the
   reconstructed group.
3. **Rigidity.** Any two fibre functors
   $\tau, \tau' \colon \mathbf{C} \to R\text{-}\mathrm{Mod}$
   are isomorphic (as monoidal functors), and the group they
   reconstruct is the same up to inner automorphism.
4. **Constraint propagation.** Algebraic conditions on
   $\tau$ (such as the volume constraint
   $\epsilon \colon \Lambda^2 V \twoheadrightarrow \mathbf{1}$)
   propagate to $G$: they cut down the automorphism group from
   $\mathrm{GL}$ to a smaller subgroup (in our case, $\det = 1$
   forces $\mathrm{SL}$; positive-definiteness then forces $\mathrm{SU}$).

In the classical setting, Tannaka--Krein recovers a compact group from
its representations \cite{tannaka1939}. The version we use is
Deligne's algebraic generalisation \cite{deligne1990}, which works
over any field and reconstructs an affine group scheme. For quantum
groups ($q \neq 1$), the appropriate extension is due to
Woronowicz \cite{woronowicz1988}.

**Origin of $q$.**  The deformation parameter $q$ is not
imposed from outside. When the braiding $c_{V,V}$ on the
fundamental object $V$ is non-symmetric ($c_{V,V}^2 \neq \mathrm{id}$),
$q$ is the eigenvalue of $c_{V,V}$ on the symmetric summand
$S^2 V$ — a purely categorical invariant extracted from the
Hecke relation $(T - q)(T + q^{-1}) = 0$. Woronowicz's
reconstruction then recovers $\mathrm{SU}_q(2)$ as
$\mathrm{End}^{\otimes}(\tau)$ with this categorically determined
$q$. The full derivation is given in
[§Substrate parameter](#sec:substrate-parameter).
