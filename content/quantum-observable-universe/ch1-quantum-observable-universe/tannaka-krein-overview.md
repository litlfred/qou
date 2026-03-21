The fibre functor $\omega$ of a quantum universe encodes an extraordinary
amount of structure. Tannaka--Krein duality \cite{deligne1990} says:

1. **Reconstruction.** The group $G$ can be recovered from
   $\omega$ alone:
   $G \cong \mathrm{Aut}^{\otimes}(\omega)$,
   the group of monoidal natural automorphisms of $\omega$.
   No *a priori* group is needed; it *emerges* from the
   category and the functor.
2. **Equivalence.** The functor $\omega$ establishes a
   monoidal equivalence
   $\mathcal{C} \simeq \mathrm{Rep}(G)$:
   every object in $\mathcal{C}$ is a representation of the
   reconstructed group.
3. **Rigidity.** Any two fibre functors
   $\omega, \omega' \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$
   are isomorphic (as monoidal functors), and the group they
   reconstruct is the same up to inner automorphism.
4. **Constraint propagation.** Algebraic conditions on
   $\omega$ (such as the volume constraint
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
