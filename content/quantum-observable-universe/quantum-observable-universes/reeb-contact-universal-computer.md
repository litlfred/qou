The
[categorical Reeb derivation](#def:categorical-reeb-derivation)
$\xi_q$ is derived from the Frobenius pairing and the Hopf
algebra structure on $A$ via the Cartan magic formula
$\mathcal{L}_{\xi_q}\varTheta = 0$, $\iota_{\xi_q}\varTheta = 1$.
The horizontal projection of $\xi_q$ onto the state bundle
$\mathcal{S}$ is the Reeb vector field of the contact form
$\varTheta$ — a genuine contact-3-geometric object on each
fibre $\mathcal{S}_p$.

Cardona–Miranda–Peralta-Salas–Presas
\cite{cardona2021}
prove that on any closed 3-manifold equipped with a contact
form one can construct a Reeb vector field whose first-return
map encodes a universal Turing machine. The trajectory-
reachability problem for such fields is undecidable; the Reeb
flow is computationally universal in the classical sense of
Church and Turing. The proof uses an explicit *plug*
construction (after Wilson and Kuperberg) glued into a contact
3-ball; the plug is contact-embeddable in any contact
3-manifold.

**Corollary for the QOU substrate.**
Because $\xi_q$ is the Reeb derivation of a contact form
$\varTheta$ on the state bundle, every fibre $\mathcal{S}_p$
inherits — by the Cardona–Miranda–Peralta-Salas–Presas
construction — the structural capacity to embed a Turing-
complete Reeb flow. Universal computation is therefore not a
property the QOU has to *postulate*; it is a property the QOU
*inherits* from the contact geometry that the
[Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)
forces on $\mathcal{S}$.

This sharpens the
[classical-to-quantum bridge](#rem:reeb-flow-bridge): the same
Reeb flow that replaces the prime-counting logarithm by a
periodic-orbit spectrum is, viewed metrically, a universal
computer in the sense of Cardona–Miranda–Peralta-Salas–Presas.
The QOU's substrate carries one geometry; that geometry already
contains a Turing-complete dynamical system.

**Entry of the $q$-deformation.**
The Cardona et al. theorem is stated at a fixed Riemannian
metric. The QOU's substrate parameter $q$ specifies a
one-parameter family of metrics, each yielding its own contact
form $\varTheta_q$ and Reeb field $R_{\varTheta_q}$. The
classical limit $q \to 1$ recovers the metric of the Cardona–
Miranda construction; for $q > 1$ the deformation is contact-
isotopic
([rem:reeb-flow-bridge](#rem:reeb-flow-bridge)), so
universality is preserved through the family. The discrete
roots-of-unity specialisations are then the quantum-mechanical
shadow of this classical universal computer — recovered through
the [skein-Turing correspondence](#rem:skein-turing-machine)
and the
[Reeb-flow Turing-completeness remark](#rem:reeb-turing-completeness)
in Chapter 10.

The takeaway: when a sceptic asks "where in the QOU does
universal computation come from?", the answer is — from the
contact geometry on $\mathcal{S}$, which is forced by the
Frobenius–Hopf axioms, and which is already known classically
to be capable of encoding a Turing machine.
