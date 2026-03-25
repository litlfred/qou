Let $(\mathbf{C}, \otimes, \mathbf{1})$ be a monoidal category and
let $V$ be an object with dual $V^{\vee}$, evaluation
$\mathrm{ev} \colon V \otimes V^{\vee} \to \mathbf{1}$, and
coevaluation $\mathrm{coev} \colon \mathbf{1} \to V^{\vee} \otimes V$.
The **snake identities** (also called *zig-zag identities*) are the
two equations:

**Left snake identity.**
$$
(\mathrm{ev} \otimes \mathrm{id}_V)
\circ (\mathrm{id}_V \otimes \mathrm{coev})
= \mathrm{id}_V.
$$

More precisely, unfolding the associator and unitor isomorphisms, the
composite
$$
V \xrightarrow{\rho_V^{-1}} V \otimes \mathbf{1}
\xrightarrow{\mathrm{id}_V \otimes \mathrm{coev}}
V \otimes (V^{\vee} \otimes V)
\xrightarrow{\alpha^{-1}_{V, V^{\vee}, V}}
(V \otimes V^{\vee}) \otimes V
\xrightarrow{\mathrm{ev} \otimes \mathrm{id}_V}
\mathbf{1} \otimes V
\xrightarrow{\lambda_V} V
$$
equals $\mathrm{id}_V$.

**Right snake identity.**
The composite
$$
V^{\vee} \xrightarrow{\lambda_{V^{\vee}}^{-1}} \mathbf{1} \otimes V^{\vee}
\xrightarrow{\mathrm{coev} \otimes \mathrm{id}_{V^{\vee}}}
(V^{\vee} \otimes V) \otimes V^{\vee}
\xrightarrow{\alpha_{V^{\vee}, V, V^{\vee}}}
V^{\vee} \otimes (V \otimes V^{\vee})
\xrightarrow{\mathrm{id}_{V^{\vee}} \otimes \mathrm{ev}}
V^{\vee} \otimes \mathbf{1}
\xrightarrow{\rho_{V^{\vee}}} V^{\vee}
$$
equals $\mathrm{id}_{V^{\vee}}$.

These identities express the fact that $(\mathrm{ev}, \mathrm{coev})$
exhibit $V^{\vee}$ as a right dual of $V$ (equivalently, that the pair
forms an *exact pairing* in the sense of
[`CategoryTheory.ExactPairing`](#rem:glossary-exact-pairing)). The
terminology "snake" comes from the graphical calculus, where the
composites trace out an S-shaped curve that straightens to a vertical
line.
