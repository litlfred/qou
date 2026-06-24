**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with fibre functor
$\tau \colon \mathbf{C} \to \mathbf{Arch}$ to the category of
archimedean realizations (smooth manifolds, real Hilbert spaces,
or any chosen archimedean target). For every braid
$\beta \in H_n(R, q)$, the real-valued knot volume $\mathrm{Vol}(K_\beta)$
of its closure factors strictly through $\tau$:*

$$
  \begin{tikzcd}[row sep=2.4em, column sep=4em]
    \mathrm{End}_{\mathbf{C}}(A^{\otimes n})
      \arrow[r, "\mathrm{tr}_M"]
      \arrow[d, "\tau_{\mathrm{arch}}"']
    & \mathbb{Z}[q^{1/2}, q^{-1/2}]
      \arrow[d, "\tau_{\mathrm{arch}}"]
    \\
    \tau(\mathrm{End}_{\mathbf{C}}(A^{\otimes n}))
      \arrow[r, "\mathrm{tr}_M^{\mathrm{arch}}"']
    & \mathbb{R}
  \end{tikzcd}
$$

*and there is no other archimedean route. Equivalently, the
diagram of QOU outputs commutes,*

$$
  \mathrm{Vol}(K_\beta)
  \;=\;
  \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\;
  (\pi_\infty \circ \tau)\bigl(\mathrm{Vol}_q(\beta)\bigr),
$$

*where $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$ is the
[adelic archimedean projection](#def:adelic-substrate) and
$\tau$ is the QOU fibre functor.*

**Identification.**
On the algebraic-quantum-volume part of $\mathrm{End}_{\mathbf{C}}(A^{\otimes n})$,
$\tau_{\mathrm{arch}}$ coincides with the
[archimedean realization functor](#def:archimedean-realization-functor)
$\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}$.
Concretely:

$$
  \tau_{\mathrm{arch}}
  \;=\;
  \mathcal{R}_{\mathrm{top}}\big|_{\widehat{\mathcal{M}}_{\mathrm{Vol}}}
  \;=\;
  \mathcal{R}_{\mathrm{top}} \circ \mu,
$$

i.e. $\mathcal{R}_{\mathrm{top}}$ is just $\tau$'s archimedean
restriction, and $\mu$ is the
[motivic mass measure](#def:motivic-mass-measure) that prepares the
input. The fibre functor $\tau$ is the *only* exit from $\mathbf{C}$
to the laboratory continuum; the realization functor is its
canonical computation rule on quantum-volume motives.

**Sketch.**
$(\Rightarrow)$ Any composite $\mathbf{C} \to \mathbb{R}$ that
preserves tensor products and dualities of $\mathbf{C}$ and lands
in archimedean spaces is, by Tannaka–Krein duality / rigidity, a
fibre functor — hence $\tau$ up to natural isomorphism. The
$\tau$-image of $\mathrm{Vol}_q(\beta)$ is therefore the unique
archimedean output.

$(\Leftarrow)$ Given $\tau$, the composite $\tau \circ \mathrm{Vol}_q$
takes values in archimedean realizations of the trace of the
braid representation. Restriction to $\mathbb{R}$ via $\pi_\infty$
recovers exactly $\ln |\mathrm{Vol}_{q_0}(\beta)|$, the standard
formula
([algebraic quantum volume](#def:algebraic-quantum-volume)).

**Consequence.**
Any physical computation of a knot volume in QOU — Kashaev limit,
Bloch–Wigner dilogarithm, hyperbolic-volume formula
([$q$-Kashaev volume density](#rem:kashaev-volume-density),
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization))
— is the value of the same composite $\pi_\infty \circ \tau$.
There is no archimedean side-channel: every real-valued QOU
observable is the $\tau$-shadow of a categorical morphism.

## Lean formalization

The companion Lean `vol_through_tau_factors` currently encodes an existence stub (`∃ v, True`) pending a faithful statement; the sketch above is the intended content, deferred via `sorry` (`-- Ref: [kashaev1997]`, `[manuscript]`).
