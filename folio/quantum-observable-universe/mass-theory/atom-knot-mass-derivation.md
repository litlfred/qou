*Let $\mathfrak{H}$ be a confined particle with canonical Hecke element $T_w$ in Gröbner–Shirshov normal form. Its categorical mass invariant is the exact finite sum:*

$$
 M(\mathfrak{H}) \;=\; \nu_{\mathrm{SDP}} \cdot \bigl[\,\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})\,\bigr].
$$

*After applying the Archimedean realization functor at $q = q_0$, the physical binding energy is:*

$$
 B(\mathfrak{H}) \;=\; m_e \cdot M(\mathfrak{H}) \big|_{q = q_0}.
$$

*The derivation evaluates Yekutieli's multiplicative integral at finite slices. Since the GB spectral sequence collapses at $E_2$, no higher slices contribute. The computation relies entirely on the pre-Archimedean data encoded in the GB-filtration jet-order certificate.*

The Lean sibling carries one condition the display above leaves implicit: that the certificate under discussion is one the pipeline actually emitted. A `MassDerivationCertificate` is a tuple of numbers, and its type records no provenance — a tuple with a negative $B_{\mathrm{pred}}$ is well-typed. Stated for *every* certificate, the mass identity is false, so the conditional class carries an `IsPipelineDerived` predicate and the theorem takes it as a hypothesis. The ten AME-validated atoms below are proved to satisfy the identity directly, without the class.

Two hypotheses that appear in the Lean statement are shown there to be free rather than load-bearing: the $E_2$-collapse condition unfolds to $2 = 2$ and is discharged by reflexivity, and the Yekutieli condition is inhabitation of the braid-element type, which the mass identity does not mention.
